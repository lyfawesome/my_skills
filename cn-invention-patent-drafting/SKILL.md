---
name: cn-invention-patent-drafting
description: Draft, review, and revise Chinese invention patent materials from technical disclosures, including claims, specifications, black-and-white technical figures, prior-art comparison, iterative review, agency-template DOCX delivery, and cross-document consistency checks. Use for Chinese patent drafting or revision, especially for CAE, simulation, engineering software, AI-assisted engineering, and multibody dynamics. Do not use to promise grant or replace a licensed patent professional's legal judgment.
---

# Chinese Invention Patent Drafting

Turn an engineering disclosure into a technically coherent, review-ready Chinese invention patent package. Preserve the applicant's actual contribution, expose unresolved assumptions, and keep every claim feature supported by the description and drawings.

## Select the working mode

- **Full package:** prior-art search, claim strategy, specification, abstract, drawings, iterative review, and agency-template deliverable.
- **Targeted revision:** repair the named section and then inspect every location that shares its terminology, data model, reference signs, or claim support.
- **Prior-art review:** produce a source-backed comparison and claim-risk analysis without editing the application unless requested.
- **Agency reformatting:** preserve the supplied template and transplant the verified content without changing the technical scope.

Do not ask for information that can be discovered from the workspace. Ask only when a missing applicant decision would materially change inventorship, ownership, filing scope, or the technical result.

## Core workflow

1. Inventory the technical disclosure, existing drafts, figures, search reports, and agency templates. Never overwrite the supplied template.
2. State the technical problem, input, transformation, intermediate data, physical or algorithmic checks, output, and measurable technical effect as one causal chain.
3. Separate indispensable features from optional embodiments. Draft the independent claim around the smallest complete technical chain; place alternatives and fallback positions in dependent claims.
4. Search current prior art before making novelty or inventiveness conclusions. Read [references/prior-art-and-review.md](references/prior-art-and-review.md) for a full search or review task.
5. Draft the specification so every claim term has a definition, data relationship, implementation path, and at least one supported embodiment.
6. Design each drawing for a distinct explanatory role. Read [references/figures-and-reference-signs.md](references/figures-and-reference-signs.md) before creating or renumbering figures.
7. For multibody dynamics or CAE model reconstruction, read [references/multibody-dynamics-disclosure.md](references/multibody-dynamics-disclosure.md) before defining the schema, validation gates, or solver adapter.
8. Run the iterative review gates described below. Repair the source draft first, then regenerate every derivative document.
9. When a DOCX or agency template is involved, read [references/agency-docx-delivery.md](references/agency-docx-delivery.md) and use the document-specific skill and renderer available in the environment.

## Eight review gates for a full package

Default to eight passes when the user requests a filing-ready package or repeated adversarial review:

1. novelty and closest-reference screening;
2. patent-eligibility and technical-effect review;
3. inventive-step combination attack;
4. sufficiency and implementation detail;
5. clarity, terminology, and antecedent basis;
6. claim hierarchy, fallback positions, and avoidable limitations;
7. unity, support, and consistency across categories;
8. submission-quality review across abstract, claims, specification, drawings, reference signs, placeholders, and template output.

Record the defect, the evidence for it, the revision made, and any residual risk in each pass. Do not manufacture a difference merely to make every pass look productive.

## Drafting constraints

- Do not equate a desired result with a technical means. Explain how data becomes model elements, equations, executable objects, diagnostics, or controlled hardware behavior.
- Do not invent performance percentages, test results, training data, solver support, or implementation details. Label applicant-supplied, retrieved, inferred, defaulted, and repaired information separately when provenance matters.
- Avoid literal translations that are unclear in Chinese patent prose. Define the operation by what it changes. For solver compilation, prefer “参数规范转换—求解器能力适配—目标模型生成” over unexplained compiler jargon such as “降低” or “发射”.
- Use the same term for the same object throughout the abstract, claims, description, tables, code-like schemas, and figures. When revising a term, search and inspect all semantic equivalents, not only exact string matches.
- Do not claim guaranteed authorization, validity, freedom to operate, or final legal status. Identify which conclusions require an official database check or patent-agent judgment.

## Drawings and media

Patent submission figures should be deterministic black-and-white technical diagrams with legible names, arrows, relationships, and reference signs. Do not use generative raster imagery for formal block diagrams or flowcharts when vector or code-native drawing is available. Use image generation only for non-submission conceptual illustrations when the user explicitly wants them.

## Cross-document consistency gate

Before delivery, verify all of the following:

- every drawing has a distinct purpose and a prose description that is implementable without relying on the image alone;
- method-step identifiers and component reference signs are not mixed;
- every reference-sign change is synchronized in the figure, caption, reference-sign table, “参见图…” paragraph, claims when applicable, source draft, and agency document;
- all required schema fields, units, coordinate frames, reference points, provenance fields, and conditional requirements are present;
- old terminology and superseded numbering have zero relevant hits;
- unresolved template prompts and internal drafting tokens have been removed;
- the final DOCX has been rendered and visually inspected after the last edit.

Use `scripts/audit_patent_docx.py` for deterministic text, placeholder, image, required-phrase, and forbidden-phrase checks. It supplements visual review; it cannot read labels embedded inside raster figures.

## Deliverables

For a full task, keep the editable source, prior-art/review report, formal figures, and agency-format document logically separate. Return only the user-requested final artifact unless they ask for working files. Briefly describe representative changes and remaining applicant/agent actions.
