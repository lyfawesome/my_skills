# Prior-art search and patentability review

Read this reference for a full patent package, novelty search, inventive-step review, claim strategy, or adversarial patentability review.

## Scope and confidentiality

Record the search jurisdiction, databases, date, language, technology range, document cutoff, and known limits. Use abstracted minimum-necessary query features when the invention is unpublished. Do not upload the complete confidential disclosure to a public search service without explicit authorization.

Distinguish:

- patentability-oriented prior-art searching;
- legal-status and family verification;
- freedom-to-operate or infringement analysis, which is a different task and must not be implied by a patentability search.

## Source hierarchy

Use current sources. Prefer official patent databases for bibliographic data, family data, procedural or legal status, priority data, and claim text. Aggregators are useful discovery tools but not the final authority for Chinese status. For non-patent literature, prefer the original paper, standard, product manual, repository, or project documentation.

For each close reference, record at least:

- publication number and title;
- applicant or assignee when relevant;
- priority, filing, and publication dates as available;
- family or related application needed to understand the disclosure;
- relevant independent claim and enabling paragraph, figure, equation, code, or manual passage;
- the exact feature or relationship disclosed;
- whether it is a search lead or verified disclosure;
- verification source and access date.

Do not treat an abstract, generated summary, title similarity, or search snippet as final proof of disclosure.

## Search construction

Build intersecting concept groups from the actual invention:

- technical object, operating environment, and application domain;
- technical problem or failure mode;
- input source, signal, data structure, material, state, or measured quantity;
- indispensable transformation, state transition, equation, control relationship, architecture, or workflow dependency;
- intermediate representation or technical interaction;
- output, controlled action, or changed technical state;
- asserted technical effect and its causal mechanism;
- alternative terminology, Chinese and English synonyms, older terminology, acronyms, and likely IPC/CPC classes;
- adjacent technical fields that could supply the same mechanism.

Search claim-style relationships and combinations, not only the proposed title. For algorithms, separate the mathematical label from the technical input/output and implementation relationship. For workflows, search state transitions, messages, triggers, constraints, and failure behavior rather than only industry names.

## Comparison matrix

Compare each independent-claim limitation, including relationships and ordering. Use at least:

| Limitation | Applicant support | Reference passage | Express / inherent / absent / uncertain | Difference | Technical consequence | Risk |
|---|---|---|---|---|---|---|

Do not treat a broad goal, similar result, or same algorithm name as disclosure of a specific mechanism. Conversely, do not claim difference based only on renamed objects, changed application labels, or wording when the technical relationship is the same.

## Novelty analysis

Evaluate whether one verified reference discloses every limitation of the claim directly or inherently in the required relationship. Do not assemble multiple references to create a novelty rejection. State uncertainty where a passage, date, or necessary implication has not been verified.

“No exact match found” is not a novelty conclusion. Report the search limits and residual risk.

## Inventive-step attack

Construct the strongest plausible combination using the closest reference and neighboring knowledge. Analyze:

- the distinguishing limitations that actually contribute to the technical solution;
- the objective technical problem supported by those differences;
- motivation or technical teaching to combine;
- compatibility, implementation obstacles, and contrary teaching;
- whether the combination would preserve the claimed relationship and effect;
- whether a feature is merely a field label, business rule, presentation choice, arbitrary parameter, or routine substitution;
- whether the contributing feature is present in the claim rather than only in the description;
- the joint effect of interacting differences.

Avoid arguing only that no single reference contains every word or that the application field is different.

## Blocking decision gate

Pause before materially changing the inventive core when:

- a verified reference appears to disclose the indispensable feature combination;
- a plausible combination removes the alleged technical contribution;
- an earlier public disclosure may control filing strategy;
- the remaining distinction is only a use, label, desired result, data name, or unsupported effect;
- avoiding the art would require adding a feature that lacks applicant support.

Present supported options:

- continue with the documented risk;
- narrow to a supported technical distinction;
- refocus on a different disclosed mechanism;
- split distinct inventive concepts;
- obtain more technical facts or evidence;
- pause and seek patent-professional advice.

Do not silently invent a distinction, replace the invention, or narrow the claim merely to produce a positive conclusion.

An applicant choice to continue with known risk preserves the working record but does not automatically close a `BLOCKER` or `MAJOR` finding or qualify the package for submission-stage status. Apply the minimum severity and independent closure rules in `independent-review.md`.

## Iterative review record

For a full package, integrate the prior-art findings with the independent review. Record the defect, evidence, revision, scope effect, applicant decision when required, and residual risk. Re-run the feature comparison after any material independent-claim change.

End with search limits and residual risks. Never state that authorization, validity, or freedom to operate is guaranteed.
