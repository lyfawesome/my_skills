---
name: cn-invention-patent-drafting
description: Draft, review, and revise Chinese invention-patent materials from algorithms, technical concepts, workflows, system designs, research, or incomplete technical disclosures. Use for invention extraction, disclosure completion, prior-art comparison, claim strategy, specifications, formal figures, independent adversarial review, and agency-format delivery, with primary coverage of algorithms, software, control, engineering, and technical workflows; do not use to promise grant, invent unsupported facts, perform filing without authorization, or replace licensed patent-professional judgment.
---

# Chinese Invention Patent Drafting

Turn an algorithm, technical idea, workflow, research result, or engineering disclosure into a technically enabled and review-ready Chinese invention-patent package. Preserve the applicant's actual contribution, distinguish concepts from verified implementation, and keep every claimed feature supported by the disclosure.

## Select the working mode

- **Idea-to-disclosure:** turn incomplete ideas, algorithms, or workflows into a structured invention disclosure and identify blocking gaps before formal claims.
- **Full application:** prior-art review, claim strategy, claims, specification, abstract, formal figures, independent review, and requested document delivery.
- **Claim or section drafting:** prepare a claim set or named section and inspect every dependent terminology and support relationship.
- **Prior-art and risk review:** produce a source-backed comparison and claim-risk analysis without changing the invention unless requested.
- **Targeted revision:** repair a defect and propagate the change through claims, description, figures, terminology, and generated documents.
- **Agency reformatting:** preserve the supplied template and transplant verified content without silently changing technical scope.

Do not ask for information that can be recovered from the workspace. Ask when a missing applicant decision would materially change inventorship, ownership, public-disclosure history, filing scope, indispensable technical means, or the asserted technical result.

## Load only the relevant references

- For an algorithm, technical idea, workflow, incomplete disclosure, or full package, read [references/general-invention-disclosure.md](references/general-invention-disclosure.md).
- For algorithms, software, AI, data processing, control logic, or technical workflows, also read [references/algorithm-and-workflow-inventions.md](references/algorithm-and-workflow-inventions.md).
- When claims, quantitative effects, multiple source files, experiments, simulations, or inferred features are involved, read [references/evidence-and-claim-mapping.md](references/evidence-and-claim-mapping.md).
- For a full application, claim set, specification, or abstract, read [references/application-drafting-template.md](references/application-drafting-template.md).
- For any prior-art search or patentability review, read [references/prior-art-and-review.md](references/prior-art-and-review.md).
- Before any formal claim set, patent-subject-matter or patentability conclusion, disclosure-timeline/inventorship/ownership conclusion, external research, public sharing, or submission-stage package, read [references/confidentiality-and-current-law.md](references/confidentiality-and-current-law.md). Verify only the current rules material to the task.
- Before creating or renumbering figures, read [references/figures-and-reference-signs.md](references/figures-and-reference-signs.md).
- For a full package or any request for repeated, adversarial, or multi-agent review, read [references/independent-review.md](references/independent-review.md).
- When a DOCX or agency template is involved, read [references/agency-docx-delivery.md](references/agency-docx-delivery.md) and use the available document-specific skill and renderer.

## Non-negotiable constraints

1. **No fabricated substance.** Do not invent implementation, experiments, data, dates, inventors, ownership, publication history, performance, commercial use, or device/software support.
2. **Concept-stage inventions are allowed.** Do not require source code, prototypes, or test data when the disclosure otherwise enables the invention. Never present a proposed or simulated embodiment as implemented or experimentally verified.
3. **Technical chain before patent prose.** Identify the technical object and scenario, technical problem, input or initial state, ordered operations and decision rules, intermediate state or data, output or controlled action, technical interaction, boundary conditions, and verifiable technical effect.
4. **No result-only claiming.** A desired result, business goal, model name, or instruction to “use AI” is not a technical means. State how the result is produced and which relationships make it possible.
5. **Technicality gate for algorithms and workflows.** Tie the claimed process to a concrete technical context, data or signal meaning, computer/device/process interaction, and technical effect. Do not force artificial hardware limitations; flag workflows that remain only business, administrative, presentation, or mental rules.
6. **Multi-axis evidence control.** Track information source, claim-support status, and technical maturity separately as defined in `evidence-and-claim-mapping.md`. Exclude unresolved, conflicting, or unsupported matter from formal claims. Keep internal questions and evidence labels out of filing text.
7. **Current prior art before conclusions.** Do not infer novelty or inventiveness from title or keyword mismatch. Compare claim features and enabling passages, and distinguish a search lead from verified disclosure.
8. **Human decision at a blocking gate.** If close prior art, public disclosure, ownership, inventorship, unlawful data use, or an indispensable technical gap could materially change the inventive core, present the supported options and obtain the applicant's decision before narrowing, abandoning, or replacing that core.
9. **Current law and system rules.** Verify time-sensitive filing rules, forms, fees, deadlines, and electronic-system constraints from current official sources. Label internal conventions and agency preferences separately from legal requirements.
10. **Confidentiality by default.** Do not upload or publish unpublished application text, drawings, applicant data, customer data, credentials, or internal paths unless the user explicitly authorizes that exact external action.
11. **Independent review for full packages.** A full application or substantial rewrite must receive at least one independent adversarial review by an agent that did not draft it, followed by closure review after repair. Do not represent an ordinary self-check as independent review.
12. **No legal-status promises.** Do not promise authorization, validity, freedom to operate, non-infringement, official acceptance, or a final legal conclusion.
13. **Respect missing domain guidance.** The general framework does not replace specialized chemical, biological, pharmaceutical, medical, or other field-specific disclosure and eligibility rules. When such rules materially affect the task and no suitable domain guidance is available, disclose the limitation and require specialist review.

## Core workflow

1. **Scope and confidentiality:** determine the requested deliverables, intended jurisdiction and filing path, disclosure timeline, owners and inventors to be confirmed, and what may leave the workspace.
2. **Disclosure inventory:** identify all supplied descriptions, diagrams, equations, code, papers, search results, tests, simulations, templates, and missing decisions. Preserve the originals.
3. **Invention reconstruction:** convert the material into the technical chain defined above. Separate the indispensable inventive mechanism from optional embodiments, implementation choices, and unverified advantages.
4. **Technicality and enablement gate:** determine whether the algorithm, idea, or workflow contains concrete technical means and enough detail to implement. If not, produce a focused disclosure-completion list before formal claims.
5. **Evidence and terminology control:** assign stable source identifiers where useful; record source, support, and maturity states; create a terminology ledger; and build the initial claim-support map.
6. **Prior-art mapping:** search current patent and primary technical sources, verify close references, compare limitations, and construct the strongest plausible combination attack before freezing the independent claim.
7. **Claim strategy:** select the smallest complete independent technical chain; define alternative independent categories only when supported and useful; place fallback mechanisms, thresholds, exceptions, and implementation variants in dependent claims.
8. **Draft claims first:** define every relationship, antecedent, parameter, state transition, and conditional branch required by the claims. Do not import avoidable detail merely because it appears in one embodiment.
9. **Build the description and figures:** align definitions, background, invention content, embodiments, equations, failure handling, figure descriptions, and abstract with the claim terminology and order.
10. **Independent adversarial review:** freeze a review version, run the protocol in `independent-review.md`, repair substantiated findings, and obtain an independent closure check.
11. **Generate and validate deliverables:** regenerate derivative files from the verified source, run deterministic checks, render document outputs, and inspect the complete final set.

## Review gates

For a full package, cover all of the following. Separate agents may combine gates when independence and traceability are preserved.

1. technical-subject-matter and concrete technical-effect review;
2. novelty and closest-reference screening;
3. inventive-step combination attack;
4. enablement, reproducibility, boundary, and failure-behavior review;
5. claim clarity, antecedent basis, category, hierarchy, and fallback review;
6. evidence source, support status, maturity, quantitative assertion, and claim-support review;
7. unity and consistency across claims, description, abstract, figures, terminology, and reference signs;
8. submission-stage quality, confidentiality, placeholder, current-rule, and template review.

Record each material defect, its evidence, severity, resolution, and residual risk. Do not manufacture edits merely to make every pass appear productive.

## Cross-document completion gate

Before delivery, verify that:

- every independent-claim feature is defined and supported in the description;
- each material claim feature maps to a disclosure location, embodiment, or necessarily implied relationship;
- quantitative effects are traceable or expressly framed as non-verified examples;
- the same object, operation, state, and parameter use the same term throughout;
- every figure has a distinct explanatory role and readable names, arrows, relationships, and reference signs;
- method-step identifiers and component reference signs are not mixed;
- reference-sign changes are synchronized across figures, captions, tables, descriptions, claims when applicable, sources, and agency documents;
- old terminology, superseded numbering, internal questions, unsupported assertions, and template prompts have zero relevant hits;
- the final DOCX has been rendered and visually inspected after the last edit.

Use `scripts/audit_patent_docx.py` for deterministic DOCX text, placeholder, image, required-phrase, and forbidden-phrase checks. It supplements, but does not replace, claim-support review or visual inspection.

## Deliverables and status labels

Keep the editable technical source, disclosure/evidence map, prior-art report, claims, specification, formal figures, independent-review record, and agency-format output logically separate.

Use one of these status labels:

- **working disclosure:** the technical chain or applicant decisions are incomplete;
- **application-content draft:** formal text exists but independent review or blocking issues remain;
- **package for pre-filing professional review:** the defined technical and document gates passed, but applicant and licensed patent-professional review of inventorship, ownership, scope, official forms, signatures, and current filing requirements is still required.

Do not describe a package as “directly submittable”, “guaranteed compliant”, or “authorization-ready”. State only which project-defined checks were completed.

Return only the user-requested final artifacts unless working files are requested. Briefly state what is confirmed, documented, inferred, proposed, simulated, missing, independently reviewed, and awaiting applicant or patent-professional action.
