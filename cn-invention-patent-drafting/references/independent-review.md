# Independent adversarial review

Read this reference for a full application, substantial rewrite, submission-stage package, repeated review, or any user request for independent or multi-agent review.

## Independence requirement

At least one reviewer must be an agent that did not draft the application. Freeze the candidate version before review and record a version identifier, review time, file list, and file hashes or equivalent immutable identifiers. Give the reviewer the user request, current draft, relevant disclosure, figures, evidence map, and verified prior art needed for the assigned gate. Do not prime the reviewer with the drafter's intended answer, suspected defect list, self-defense, or desired conclusion.

If delegation is unavailable, disclose that the independent-review gate was not completed and do not describe the result as a package for pre-filing professional review.

## Review tracks

For a full or high-risk package, use separate reviewers when practical:

1. **Patentability attack:** closest reference, novelty, strongest combination, technical-subject-matter risk, contribution features, avoidable limitations, and alternative claim core.
2. **Enablement and truth audit:** implementation path, equations and decision rules, concept-versus-test status, quantitative support, input/output relationship, boundary conditions, failure behavior, and claim-support matrix.
3. **Document consistency audit:** terminology, antecedent basis, claim hierarchy, category support, abstract, figures, reference signs, placeholders, confidentiality, agency template, and current-rule classification.

A single independent reviewer may cover all tracks when task size is limited, but the report must keep the findings distinguishable.

## Reviewer output contract

Each finding must include:

- identifier and review track;
- severity: `BLOCKER`, `MAJOR`, `MINOR`, or `OBSERVATION`;
- affected claim, paragraph, figure, table, or artifact;
- evidence and reasoning;
- the smallest defensible repair;
- whether the repair changes scope or requires an applicant decision;
- residual risk after repair.

The reviewer returns findings rather than silently editing the formal source. The primary drafter records `ACCEPT`, `PARTIAL`, or `DISPUTE` for each finding with reasons, repairs accepted findings in the source, and regenerates derivative files. `DISPUTE` records disagreement only; it does not close or remove a finding.

## Minimum severity rules

Apply at least these severities unless evidence justifies a higher level:

- one verified reference discloses every limitation of an active independent claim in the required relationship: `BLOCKER`;
- an independent claim contains an unsupported, conflicting, or non-enabled necessary limitation: `BLOCKER`;
- the claimed mechanism materially depends on clearly unlawful data acquisition or prohibited use: `BLOCKER`;
- an unresolved conflict over the inventive core, inventorship, ownership, or public-disclosure timeline that can change filing strategy: `MAJOR`, or `BLOCKER` when safe progression is not possible;
- a strong unresolved inventive-step combination attack against the independent claim: `MAJOR`;
- inconsistency that changes claim meaning, scope, or support: at least `MAJOR`.

An applicant instruction to “continue with risk” may keep a working draft active but does not by itself close or downgrade a severe finding.

## Closure review

After repair, an independent reviewer checks the identified repaired version and determines whether each finding is `OPEN`, `DISPUTED`, `CLOSED`, or `DOWNGRADED`. Only the independent closure reviewer may close or downgrade a `BLOCKER` or `MAJOR`, and must give evidence and reasoning. The closure reviewer checks that:

- every `BLOCKER` and `MAJOR`, including disputed findings, is actually closed or evidence-based downgraded;
- the repair did not introduce unsupported matter, terminology drift, numbering errors, new-matter risk, or unintended scope loss;
- disputed findings have a documented technical or legal reason and an independent closure decision rather than a unilateral drafter decision;
- the final status matches the remaining risk.

A package for pre-filing professional review requires zero open or disputed `BLOCKER` findings and zero open or disputed `MAJOR` findings. List all remaining minor findings, applicant decisions, and patent-professional questions.

## Forward test for this skill

When the skill itself is substantially revised, run at least one independent forward test using a realistic raw request without giving the evaluator the intended output. Useful tests include:

- a concept-stage algorithm with no code or experiments;
- a workflow that is mostly business rules and should trigger technicality concerns;
- a technical method containing unsupported performance percentages;
- a disclosure with a potentially damaging earlier publication;
- a draft with inconsistent terminology or figure numbering.

Judge the actual behavior and artifacts, not whether the output repeats preferred wording.

## Completion rule

Do not simulate multiple reviews by rewriting the same analysis under different headings. A review counts only when it is independently performed or clearly identified as a non-independent self-check. If no independent closure check occurs after a material repair, state that limitation explicitly.
