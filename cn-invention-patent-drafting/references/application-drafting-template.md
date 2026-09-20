# General application drafting template

Read this reference when drafting a claim set, specification, abstract, or full Chinese invention-patent application.

This template defines an internal drafting sequence and quality contract. It is not a claim that one fixed wording or section count is legally required in every case. Verify current official and agency requirements before submission-stage delivery.

## Internal working record

Keep these items outside the formal application text:

1. task scope and requested deliverables;
2. confidentiality and public-disclosure timeline;
3. applicant and inventor items awaiting confirmation;
4. invention technical-chain record;
5. terminology ledger;
6. source, support, and maturity table;
7. prior-art comparison matrix;
8. claim tree and fallback plan;
9. claim-support matrix;
10. unresolved applicant decisions and review findings.

Do not copy evidence IDs, support states, risk labels, internal questions, tool names, prompts, or review comments into the formal claims, specification, abstract, or figures.

## Drafting order

Use this default order unless the task or supplied agency process requires another sequence:

1. freeze the intended inventive core and terminology;
2. draft the broadest supportable independent claim;
3. build dependent-claim fallback layers;
4. add other claim categories only when they have independent value and full support;
5. map every atomic limitation to the disclosure;
6. draft the description around the claims and the broader supported disclosure;
7. create figures that explain distinct relationships;
8. draft the abstract from the verified application content;
9. run independent review, repair, regenerate, and validate.

## Claim template

### Independent method or process claim

The claim should identify, when indispensable:

- the technical object, execution subject, or controlled process;
- acquisition or receipt of technically defined input or initial state;
- construction or update of a material intermediate representation or state;
- ordered transformations, calculations, control relationships, or decision conditions;
- the relationships among steps, data, states, components, or physical operations;
- the technical output, state change, or controlled action;
- downstream use or validation only when it contributes to the technical mechanism.

Do not insert method-step identifiers such as `S100` merely for style. Use them when needed for cross-reference with a flowchart or embodiment, while keeping the claim grammatically coherent without relying on the drawing.

### Independent system or apparatus claim

State the technical components and their data, control, physical, or functional relationships. Do not mechanically transform every method step into a “module”. A functional component must have description support showing how it performs the claimed operation and interacts with other components.

### Device, medium, or program-product claims

Add these categories only when appropriate to the disclosed invention and current practice. Ensure that the referenced method is supported and that the category does not introduce unsupported execution, storage, hardware, or distribution assumptions.

### Dependent claims

Create meaningful fallback layers, such as:

- narrower data or state relationships;
- parameter-selection rules, thresholds, ranges, or constraints with support;
- initialization, iteration, termination, retry, exception, and fallback behavior;
- alternative models, structures, communication methods, materials, or control strategies;
- validation, calibration, synchronization, security, resource, or robustness mechanisms;
- specific embodiments that preserve the inventive core.

Do not use a dependent claim only to repeat the independent claim with synonyms or to claim an unsupported performance result.

## Specification template

### Title

Name the technical object and principal operation neutrally. Avoid marketing terms, desired results without means, applicant names, product codes, and unnecessary implementation brands.

### Technical field

Identify the immediate technical field and, if useful, the more specific subfield. Do not exaggerate the field merely to distance the invention from prior art.

### Background

Describe the relevant existing technical process and the technical limitation being addressed. Do not make unsupported admissions about what is universally known, concede more prior art than verified, or disparage specific products unnecessarily.

### Invention content

Present:

- the technical problem actually solved;
- the technical solution using terminology consistent with the claims;
- alternative and fallback embodiments supported by the disclosure;
- the causal technical effects of the solution.

Do not replace the technical solution with a list of advantages.

### Figure descriptions

Give each figure a distinct purpose. Use method-step identifiers for procedural order and numeric reference signs for components or objects. The prose must remain implementable without relying on color, hidden metadata, or unexplained empty boxes.

### Detailed embodiments

For at least one enabling path, disclose as applicable:

- technical environment and initial conditions;
- input origin, meaning, schema, units, and validity;
- structures, data models, states, messages, equations, parameters, or components;
- ordered operations and the relationships among them;
- branches, loops, concurrency, termination, conflicts, exceptions, and fallback;
- output and how a downstream technical process uses it;
- boundary conditions and alternative implementations;
- effect-verification method and the maturity of any supporting result.

An example may be a conceptual or illustrative embodiment, but must not be described as an experiment, deployment, or measurement unless supported. In Chinese formal delivery, describe it as a “构想性实施方式” or “示例性实施方式” when that distinction is material.

## Abstract template

Summarize the technical field, principal technical problem, indispensable technical solution, and principal technical use or effect. Use only features supported in the application. Do not insert unsupported performance figures, legal conclusions, promotional language, internal risk notes, or claim-broadening content.

Select an abstract figure from the formal specification figures when appropriate; do not create a contradictory second version of the same process merely to serve as an abstract figure.

## Formal-text completion rules

- Every claim term has a stable meaning and antecedent basis.
- Every independent-claim limitation has enabling description support.
- A feature relied on for technical contribution or effect appears in the claim when required by the claim strategy.
- Necessary and optional features are not confused.
- A single object or operation is not given multiple names without an explicit definition.
- Quantitative statements match their evidence maturity.
- No placeholders, evidence labels, drafting notes, search conclusions, guarantees, or internal file paths remain.
- Formal text is regenerated after material claim changes and checked against the claim-support matrix.
