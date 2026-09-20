# General invention disclosure

Read this reference for an algorithm, technical idea, workflow, incomplete disclosure, or full patent package.

## Do not confuse maturity with enablement

An invention may be patent-draftable before source code, a prototype, or test data exists. The decisive question is whether the disclosure teaches a skilled person a concrete technical implementation without requiring inventive reconstruction.

Record implementation maturity separately from disclosure sufficiency. Never describe a concept, simulation, or illustrative embodiment as a completed experiment or deployed product.

## Build the invention record

Capture the following fields. Recover them from supplied material before asking the applicant.

1. **Title candidate:** neutral technical object and operation, without marketing language.
2. **Technical field and object:** the device, computer process, signal, material, production process, control process, or other technical object being changed or controlled.
3. **Existing technical process:** what currently happens, under which conditions, and where the technical limitation appears.
4. **Technical problem:** a specific defect, conflict, resource cost, accuracy/stability issue, control limitation, or implementation obstacle.
5. **Input and initial state:** data, signals, measured values, physical states, configuration, timing, source, units, and validity conditions.
6. **Indispensable mechanism:** ordered operations, data or state transformations, equations, decision rules, dependencies, and interactions that produce the result.
7. **Intermediate representations:** records, graphs, features, states, queues, models, control variables, masks, indexes, or other intermediate objects.
8. **Output or controlled action:** technical result data, command, model, state estimate, transformed object, device action, or production result.
9. **Technical effect:** the causal effect produced by the indispensable mechanism, including how it could be observed or verified.
10. **Boundaries and failure behavior:** valid operating range, preconditions, exceptions, fallback, conflict handling, missing data, convergence or termination, and safety behavior.
11. **Alternatives and fallback positions:** substitutions that preserve the mechanism, narrower mechanisms, thresholds, and optional embodiments.
12. **Disclosure and ownership facts:** inventors to confirm, applicant/owner to confirm, external contributors, public disclosures and dates, prior applications, and confidentiality constraints.

## Statutory-subject-matter and public-interest screen

Before formal claims, screen the disclosed substance under the current Chinese Patent Law and Examination Guidelines. Keep these as distinct questions:

1. Is the claimed subject matter excluded as a rule or method for mental activities, a scientific discovery, a method for diagnosis or treatment of disease, an animal or plant variety, a nuclear-transformation method or resulting substance, or another current statutory exclusion?
2. Even if the claim is not wholly excluded, does the claim as a whole constitute a technical solution using technical means to solve a technical problem and obtain a technical effect?
3. Does exploitation of the proposed subject matter conflict with law, social morality, or public interest, including unlawful data acquisition or prohibited use?
4. Does a medical, biological, chemical, pharmaceutical, genetic, or other specialized field require additional disclosure, exclusions, experimental support, or professional review beyond this general framework?

Do not decide these questions merely from labels such as “algorithm”, “medical AI”, “platform”, or “device”. Identify the actual limitations and interactions. When a material exclusion or public-interest issue is plausible, record the relevant facts and current official rule, stop scope-changing formal drafting when necessary, and require licensed patent-professional or field-specialist review rather than inventing a workaround.

## Completeness gate

Formal claims may begin only when the smallest complete technical chain answers:

- what technical object receives what input;
- which ordered operations or relationships transform it;
- what intermediate state is created or changed;
- what concrete technical output or action results;
- why that mechanism causes the asserted technical effect;
- how a skilled person can implement at least one embodiment;
- which missing choices would materially change the scope.

If these questions cannot be answered, deliver a **working disclosure** containing focused completion questions, not polished result-only claims.

## Applicant questions

Ask in priority order and combine related questions. Prefer questions that decide claim scope or enablement, such as:

- What exactly changes between the input and output?
- Which step is indispensable and which is a preferred implementation?
- What triggers each branch, loop, termination, retry, or fallback?
- Which parameter ranges are required, preferred, or merely observed?
- What happens when data is missing, contradictory, delayed, noisy, or outside range?
- Which statements are implemented, simulated, proposed, or not yet confirmed?
- What has been publicly disclosed, when, where, and with how much technical detail?

Do not ask the applicant to choose patent-law terminology when the technical facts are sufficient for the drafter to propose a structure.

## Claim-category selection

Choose categories from the disclosed technical substance, not from a fixed package:

- method or process;
- system, apparatus, or device;
- computer-readable storage medium or computer program product when supported and appropriate;
- product, material, composition, manufacturing process, control process, or use when the invention actually concerns that category.

Do not create parallel categories by mechanically replacing “step” with “module”. Each category must disclose a coherent technical relationship and receive description support.
