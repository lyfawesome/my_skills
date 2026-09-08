#!/usr/bin/env python3
"""Audit text and image invariants in a patent DOCX using only stdlib."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
WP_NS = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
TEXT_PART = re.compile(
    r"^word/(document|header\d+|footer\d+|footnotes|endnotes|comments)\.xml$"
)
DEFAULT_PLACEHOLDERS = ("请在此处键入", "TODO", "FIXME", "TBD")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Audit placeholders, required or forbidden phrases, figure mentions, "
            "step mentions, and images in a patent DOCX."
        )
    )
    parser.add_argument("docx", type=Path)
    parser.add_argument(
        "--require", action="append", default=[], help="Phrase that must occur; repeatable."
    )
    parser.add_argument(
        "--forbid", action="append", default=[], help="Phrase that must not occur; repeatable."
    )
    parser.add_argument("--expect-inline-images", type=int)
    parser.add_argument("--allow-placeholders", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    return parser.parse_args()


def text_from_xml(data: bytes) -> str:
    root = ET.fromstring(data)
    return "".join(node.text or "" for node in root.iter(f"{{{W_NS}}}t"))


def audit(
    path: Path,
    required: list[str],
    forbidden: list[str],
    expected_images: int | None,
    allow_placeholders: bool,
) -> tuple[dict, bool]:
    if not path.is_file():
        raise FileNotFoundError(path)

    texts: list[str] = []
    inline_images = 0
    anchored_images = 0
    media_files: list[str] = []

    with zipfile.ZipFile(path) as archive:
        for name in archive.namelist():
            if name.startswith("word/media/") and not name.endswith("/"):
                media_files.append(name)
            if not TEXT_PART.match(name):
                continue
            data = archive.read(name)
            texts.append(text_from_xml(data))
            root = ET.fromstring(data)
            inline_images += sum(1 for _ in root.iter(f"{{{WP_NS}}}inline"))
            anchored_images += sum(1 for _ in root.iter(f"{{{WP_NS}}}anchor"))

    full_text = "\n".join(texts)
    placeholder_hits = {
        phrase: full_text.count(phrase)
        for phrase in DEFAULT_PLACEHOLDERS
        if phrase in full_text
    }
    required_hits = {phrase: full_text.count(phrase) for phrase in required}
    forbidden_hits = {
        phrase: full_text.count(phrase) for phrase in forbidden if phrase in full_text
    }
    figure_mentions = Counter(
        re.findall(r"图\s*([0-9]{1,2})(?![0-9A-Za-z_])", full_text)
    )
    step_mentions = Counter(
        re.findall(r"(?<![A-Za-z0-9_])S([0-9]{2,4})(?![0-9])", full_text)
    )

    failures: list[str] = []
    if placeholder_hits and not allow_placeholders:
        failures.append("unresolved placeholders")
    if any(count == 0 for count in required_hits.values()):
        failures.append("missing required phrases")
    if forbidden_hits:
        failures.append("forbidden phrases present")
    if expected_images is not None and inline_images != expected_images:
        failures.append("unexpected inline image count")

    report = {
        "file": str(path.resolve()),
        "ok": not failures,
        "failures": failures,
        "placeholder_hits": placeholder_hits,
        "required_hits": required_hits,
        "forbidden_hits": forbidden_hits,
        "inline_images": inline_images,
        "anchored_images": anchored_images,
        "media_files": len(media_files),
        "figure_mentions": dict(
            sorted(figure_mentions.items(), key=lambda item: int(item[0]))
        ),
        "step_mentions": dict(
            sorted(step_mentions.items(), key=lambda item: int(item[0]))
        ),
    }
    return report, not failures


def main() -> int:
    args = parse_args()
    try:
        report, ok = audit(
            args.docx,
            args.require,
            args.forbid,
            args.expect_inline_images,
            args.allow_placeholders,
        )
    except (FileNotFoundError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"FILE: {report['file']}")
        print(f"STATUS: {'PASS' if ok else 'FAIL'}")
        print(
            "IMAGES: "
            f"inline={report['inline_images']} "
            f"anchor={report['anchored_images']} "
            f"media={report['media_files']}"
        )
        print(f"PLACEHOLDERS: {report['placeholder_hits'] or 'none'}")
        print(f"REQUIRED: {report['required_hits'] or 'not specified'}")
        print(f"FORBIDDEN: {report['forbidden_hits'] or 'none'}")
        print(f"FIGURES: {report['figure_mentions'] or 'none'}")
        print(f"STEPS: {report['step_mentions'] or 'none'}")
        if report["failures"]:
            print("FAILURES: " + "; ".join(report["failures"]))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
