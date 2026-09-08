# Multibody-dynamics disclosure

Read this reference when the invention constructs, validates, repairs, translates, or solves a multibody-dynamics model.

## Minimum solver-independent model schema

Use typed nodes or equivalent records for at least:

- `Body`;
- `Frame/Marker`;
- `Joint/Constraint`;
- `Force/Contact`;
- `Driver`;
- `Analysis`;
- `Output`.

Represent ownership, connection, action, dependency, hierarchy, and evidence provenance with typed edges or equivalent references.

## Body mass properties

For a dynamic rigid body, `mass` alone is insufficient. The record should make these properties determinate:

- `mass`;
- `center_of_mass`;
- `inertia_tensor`;
- `inertia_reference_point`;
- `inertia_frame`;
- initial pose and initial velocity.

The inertia tensor must be tied to a reference point and an expression frame. Prefer a center-of-mass tensor; otherwise specify the parallel-axis conversion. A planar rigid body may use the scalar inertia about the plane-normal axis while retaining its reference point and frame. A point mass need not have nonzero rotational inertia. A purely kinematic analysis may omit mass properties by an explicit configuration, but a dynamic rigid-body analysis must not silently invent them.

## Physical validation gates

Describe deterministic checks before solver execution:

- schema, identifier, reference, and endpoint checks;
- unit and coordinate-frame conversion;
- positive mass and inertia-tensor symmetry, semidefiniteness or definiteness as applicable, principal-moment conditions, reference-point and frame resolvability;
- topology, free-degree and locked-degree consistency;
- constraint equation generation and Jacobian rank;
- consistent initial position and velocity;
- driver compatibility after constraints;
- target-solver capability and equivalent-expansion error limits.

For redundant coordinates, a representative constrained system may be written as:

$$
\boldsymbol{M}(\boldsymbol{q})\ddot{\boldsymbol{q}}
+ \boldsymbol{h}(\boldsymbol{q},\dot{\boldsymbol{q}},t)
+ \boldsymbol{\Phi}_{\boldsymbol{q}}^{\mathsf{T}}\boldsymbol{\lambda}
= \boldsymbol{Q}(\boldsymbol{q},\dot{\boldsymbol{q}},t),
\qquad
\boldsymbol{\Phi}(\boldsymbol{q},t)=\boldsymbol{0}.
$$

If $n_q$ is the generalized-coordinate count and $r$ is the independent constraint rank, disclose the local freedom count as:

$$
n_f = n_q-r.
$$

State how rank tolerance, representative configurations, structural rank, or numerical rank is selected. A formula without data provenance, thresholds, or failure behavior is not a complete validation mechanism.

## Evidence and repair

Each inferred parameter or relation should retain a source reference, confidence, origin state, conflict set, and version when traceability is part of the invention. Restrict automated repair to an affected subgraph or equivalent dependency closure. Revalidate the patched copy before applying it, and protect explicitly locked engineering parameters from silent modification.

## Solver adaptation terminology

Use clear Chinese operations rather than unexplained compiler translations:

1. **参数规范转换:** unify units, coordinate conventions, degree-of-freedom identifiers, and parameter representations according to the capability profile;
2. **求解器能力适配:** map supported elements and convert unsupported high-level elements through an equivalent-expansion template, followed by freedom, rank, and error checks;
3. **目标模型生成:** produce API calls, script statements, input records, or in-memory objects and generate the bidirectional source mapping at the same time.

For example, convert an unsupported cylindrical joint into a supported compound constraint with coaxial rotational and translational freedoms. Recompute the constraint Jacobian rank after the equivalent expansion; do not describe the operation merely as “lowering”.

## Execution feedback

Map target object identifiers, statement ranges, and equation rows back to intermediate-model nodes, edges, and original evidence. Distinguish parser errors, singular matrices, nonconvergence, constraint drift, energy or momentum anomalies, contact penetration, step sensitivity, and missing result fields. Recheck only the affected region and its dependency closure when the invention claims incremental repair.
