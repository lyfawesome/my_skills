# Figures and reference signs

Read this reference before creating, revising, or renumbering patent drawings.

## Give each figure one distinct job

Do not draw the same process twice under different titles. A useful software or engineering patent set may include:

- a system architecture showing modules, shared stores, system boundary, and external interfaces;
- a method flow showing temporal order, decisions, loops, and method-step identifiers;
- a data-model graph showing node and edge types;
- an evidence-to-model mapping;
- a validation and repair loop;
- a solver-adapter and source-mapping relationship;
- a concrete mechanism or topology embodiment;
- a diagnostic backtrace.

A system diagram and a method flow may cover the same invention but must answer different questions: “what components exchange what data?” versus “what happens in what order?”. State this distinction in the prose when readers could confuse them.

## Reference-sign scheme

Chinese patent practice requires clarity and consistency, not a particular hundreds-prefix scheme. A predictable local convention is still useful:

- use `S100`, `S200`, and similar identifiers for method steps;
- use numeric signs for components, nodes, records, and modules;
- optionally align component signs with the figure number, such as `301–310` for Figure 3;
- use suffixes such as `603A–603C` for parallel alternatives only when the relationship is explained;
- if the same component appears in multiple drawings, retain the same sign rather than renumbering it merely because the figure changes.

Do not mix method steps with component signs. Do not infer that Figure 2 must use `2xx`; `S` identifiers are usually clearer for a procedure.

## Minimum content inside each figure

Every box or node should normally contain both its reference sign and a readable name. Add the decisive fields or state only when they make the relationship understandable. Label non-obvious arrows. Make decision outcomes and loop-back paths explicit.

Avoid figures made only of numbered empty rectangles. The text must also explain each figure well enough that a skilled person can implement the relationship without relying on color or hidden metadata.

## Production requirements

- Use black-and-white line art suitable for patent reproduction.
- Prefer vector or deterministic code-native diagrams; use high-resolution raster only when necessary.
- Use a CJK-capable font and verify every Chinese label after rendering.
- Keep line weight, arrowheads, padding, and text size consistent.
- Keep external systems visibly outside the claimed system boundary when that distinction matters.

## Renumbering checklist

After any reference-sign change, inspect and update:

1. the visible label inside every figure;
2. captions and figure titles;
3. the reference-sign table;
4. each “参见图…” relationship paragraph;
5. embodiments and claim text that cite the sign;
6. source-builder data and generated agency documents;
7. alt text or accessibility descriptions when present.

Search for old sign-plus-name combinations, not raw numbers alone, because publication numbers, dimensions, equation rows, and dates can legitimately contain the same digits. Require zero relevant old combinations before delivery.
