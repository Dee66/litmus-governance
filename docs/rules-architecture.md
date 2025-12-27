# ARCHITECTURE RULES (AUTHORITATIVE)

These rules define non-negotiable architectural invariants.
Copilot must enforce them mechanically.
Do not infer, extend, or reinterpret.

----------------------------------------
PRIMARY PRINCIPLES
----------------------------------------
- Determinism over flexibility
- Explicitness over abstraction
- Composition over indirection
- Proof over elegance

----------------------------------------
STRUCTURAL BOUNDARIES
----------------------------------------
The system must be structured around:
- deterministic pipelines
- explicit phases
- validation and guard layers
- artifact generation and signing

Architecture must reflect invariants, not frameworks.

----------------------------------------
FORBIDDEN STRUCTURES
----------------------------------------
The following are forbidden unless explicitly required by the checklist:
- Generic layering (e.g. core/services/adapters/infra)
- Interface-first design without multiple concrete implementations
- Dependency injection frameworks
- “Ports and adapters” abstractions
- Marker interfaces or empty base classes
- Abstractions created for anticipated future use

----------------------------------------
DEPENDENCY RULES
----------------------------------------
- High-level orchestration may depend only on explicit, local components
- No circular dependencies
- No global mutable state
- No hidden side effects

Dependencies must be:
- explicit
- local
- minimal

----------------------------------------
FILE AND MODULE RULES
----------------------------------------
- Files are grouped by responsibility, not by technical layer
- Each file must have exactly one reason to change
- Files exceeding responsibility boundaries must be split
- Utility modules are forbidden unless explicitly required

----------------------------------------
INTERFACES AND ABSTRACTIONS
----------------------------------------
- Interfaces are permitted only when:
  - at least two concrete implementations exist, AND
  - the abstraction is required by the checklist
- Abstract base classes without behavior are forbidden
- Inheritance is forbidden unless explicitly required

----------------------------------------
CONCURRENCY AND SIDE EFFECTS
----------------------------------------
- Side effects must be isolated and explicit
- Concurrency is forbidden unless explicitly enabled by the checklist
- No background execution, callbacks, or implicit async behavior

----------------------------------------
ENFORCEMENT
----------------------------------------
If any architectural rule is violated:
- Stop execution
- Raise a blocker
- Do not attempt a workaround

----------------------------------------
END OF ARCHITECTURE RULES
----------------------------------------
