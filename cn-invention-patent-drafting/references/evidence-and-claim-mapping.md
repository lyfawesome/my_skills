# Evidence and claim mapping

Read this reference when drafting claims, handling multiple sources, using quantitative effects, or distinguishing a concept from verified implementation.

## Stable source identifiers

Assign stable identifiers when the disclosure spans multiple items or traceability matters. A practical scheme is:

- `D001...` for applicant statements or interview notes;
- `DOC001...` for supplied documents, code, drawings, logs, datasets, or simulations;
- `EQ001...` for equations or algorithm definitions;
- `FIG001...` for source figures;
- `PA001...` for verified prior-art references;
- `Q001...` for unresolved applicant questions.

The exact prefixes are optional. Stability and bidirectional traceability are mandatory once identifiers are used.

## Keep three axes separate

### Information source

- `APPLICANT_EXPLICIT`: expressly supplied or confirmed by the applicant;
- `WORKSPACE_EXTRACTED`: extracted from supplied documents, diagrams, code, data, or records;
- `PUBLIC_SOURCE`: verified from a cited public source;
- `REASONED_INFERENCE`: derived from supplied facts without an express statement;
- `DRAFTING_PROPOSAL`: a drafter-proposed alternative or fallback awaiting confirmation;
- `UNKNOWN`: source or meaning is not established.

### Claim-support status

- `EXPLICITLY_SUPPORTED`: the disclosure expressly supports the limitation;
- `INHERENTLY_SUPPORTED`: the limitation follows directly and necessarily from disclosed relationships;
- `NEEDS_CONFIRMATION`: an applicant choice or material meaning remains open;
- `CONFLICTING`: supplied sources disagree;
- `UNSUPPORTED`: no adequate basis exists.

### Technical maturity

- `CONCEPTUAL`;
- `SPECIFIED`;
- `IMPLEMENTED_UNVERIFIED`;
- `SIMULATED`;
- `EXPERIMENTALLY_TESTED`;
- `DEPLOYED`;
- `UNKNOWN`.

Maturity does not determine patent support. A concept-stage mechanism may be explicitly supported and sufficiently enabled even though it is not implemented. A performance number is not tested merely because the underlying mechanism is confirmed.

## Rules for formal claims

- Every independent-claim limitation must be `EXPLICITLY_SUPPORTED` or `INHERENTLY_SUPPORTED` and map to at least one enabling description location.
- A `DRAFTING_PROPOSAL` may enter a claim only after applicant confirmation and sufficient implementation disclosure.
- `NEEDS_CONFIRMATION`, `CONFLICTING`, and `UNSUPPORTED` matter stays out of formal claims.
- `PUBLIC_SOURCE` may explain background, common knowledge, or a conventional implementation. A creative, indispensable, or scope-changing feature found only in a public source must not enter the applicant's formal claim unless the applicant confirms adoption into the intended invention and supplies an enabling disclosure. Public-source support does not establish applicant contribution or inventorship.
- `REASONED_INFERENCE` cannot establish inventorship, ownership, dates, experimental success, commercial deployment, or numerical improvement.
- Do not broaden a specific disclosed relationship into every possible means unless the description supports the breadth.
- Internal source IDs and status labels belong in working records, not formal claims, specification prose, abstract, or figures.

## Claim-support matrix

Maintain a table with at least:

| Claim | Atomic limitation | Meaning/relationship | Disclosure source | Description support | Figure/equation | Source type | Applicant adoption | Support status | Maturity | Boundary or risk |
|---|---|---|---|---|---|---|---|---|---|---|

Treat a missing independent-claim row, an unresolved term, or unsupported material as a blocking defect. For a dependent claim, map at least every added limitation. Update the matrix whenever a claim or terminology change occurs.

## Quantitative and comparative assertions

For each number or superiority statement, record:

- source and version;
- whether it is measured, simulated, calculated, illustrative, or proposed;
- conditions, dataset or sample, baseline, units, uncertainty or tolerance when material;
- the exact proposition the evidence supports.

If support is incomplete, remove the quantitative assertion from formal text or recast it as a clearly identified illustrative parameter without implying achieved performance.

## Derived alternatives

The drafter may identify narrower fallbacks or technically equivalent variants, but must distinguish them from applicant-provided content. Do not silently turn a brainstorming suggestion into the applicant's invention. Record applicant confirmation when an alternative becomes part of the intended filing scope.
