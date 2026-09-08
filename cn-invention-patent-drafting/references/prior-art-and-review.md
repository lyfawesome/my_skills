# Prior-art search and iterative review

Read this reference for a full patent package, a novelty search, or an adversarial patentability review.

## Source hierarchy

Use current sources. Prefer official patent databases for bibliographic data, family data, prosecution status, and claim text. Patent aggregators are useful discovery tools but not the final authority for Chinese legal status. For non-patent literature, prefer the original paper, standard, product manual, or project documentation.

Record at least the publication number, title, priority or filing date when available, publication date, relevant claim or passage, and the feature it discloses. Distinguish a search lead from a verified disclosure.

## Search construction

Build several intersecting concept groups instead of searching the proposed title only:

- application domain and physical object;
- input representation or human interaction;
- intermediate representation, graph, schema, or compiler;
- validation, consistency, rank, residual, or diagnostic mechanism;
- execution target, solver, adapter, or generated model;
- repair, traceability, provenance, feedback, or reproducibility.

Search Chinese and English synonyms, claim-style phrases, and likely neighboring fields. Review independent claims and enabling passages, not abstracts alone.

## Comparison matrix

For each close reference, compare:

1. input and evidence representation;
2. model or intermediate data structure;
3. deterministic validation;
4. repair scope and control;
5. target-system adaptation;
6. execution feedback and traceability;
7. resulting technical effect.

Mark each feature as expressly disclosed, necessarily implied, absent, or uncertain. Do not treat a broad goal as disclosure of a specific mechanism.

## Inventive-step attack

Construct the strongest plausible examiner combination. Explain why the skilled person would or would not combine the references, what technical obstacle remains, and whether the claimed features interact to create a joint effect. Avoid arguing only that no single reference contains every word.

## Eight-pass record

Use these default passes for a filing-ready package:

1. identify anticipation and remove already-public macro concepts from the alleged core;
2. anchor algorithms in a concrete technical process, data relationship, equation assembly, solver execution, or hardware operation;
3. test obvious combinations using the closest reference plus neighboring techniques;
4. add definitions, schemas, thresholds, error handling, and embodiments needed for reproducibility;
5. remove relative or result-only terms and repair claim antecedents;
6. build dependent-claim fallback layers without importing unnecessary implementation details into the independent claim;
7. check unity, category support, and consistency among method, system, device, medium, and program-product claims;
8. audit all deliverables, dates, terminology, numbering, citations, placeholders, and formal figures.

End with residual risks and applicant actions. Never state that authorization is guaranteed.
