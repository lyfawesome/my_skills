# Agency-template DOCX delivery

Read this reference whenever a Word document or patent-agency template is an input or output.

## Preserve the template

- Treat the supplied agency file as the visual and structural authority.
- Keep an untouched copy and generate a new output file.
- Preserve logos, headers, footers, page geometry, section order, table boundaries, and requested fonts unless the user asks for a redesign.
- Do not leave template prompts such as “请在此处键入” in the final output.

## Maintain one technical source of truth

Prefer a verified source draft and generate the agency document from it. Avoid independent manual edits to multiple derivatives. When the generator selects source paragraphs by numeric index, do not insert or remove source paragraphs casually; replace text in place or replace brittle indexing with heading-based extraction.

After a technical change, regenerate and inspect both the source draft and agency document. Verify nested tables as well as top-level paragraphs.

## Editing and rendering

Use the document-specific skill and its bundled runtime for DOCX work. Immediately before the first authoring operation, follow that skill's artifact-operation marker requirement. Make minimal local edits, render the final DOCX to page images after the last change, and visually inspect all affected pages plus the complete page set.

Check especially:

- table rows that expand after longer technical fields are added;
- figures that split from captions;
- outer template tables containing nested technical tables;
- floating agency logos and header alignment;
- CJK glyph availability and Latin technical identifiers;
- blank overflow pages, clipping, overlap, and unexpected page-count changes.

If the available renderer lacks a required CJK font, distinguish a renderer-environment defect from missing document text using structural extraction, but do not claim full glyph verification without opening the document in a CJK-capable renderer.

## Structural audit

Use `../scripts/audit_patent_docx.py` from this skill directory, for example:

```bash
python scripts/audit_patent_docx.py final.docx \
  --expect-inline-images 9 \
  --require "参数规范转换" \
  --forbid "规范化、降低和发射"
```

The script checks all Word text parts, including nested table text, because those contents are in `document.xml`. It cannot confirm text drawn into PNG figures; inspect those images separately.
