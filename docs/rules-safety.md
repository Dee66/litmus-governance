# SAFETY RULES (AUTHORITATIVE)

These rules define hard safety constraints.
Violations require immediate termination.

----------------------------------------
EXECUTION ENVIRONMENT
----------------------------------------
Copilot must enforce all of the following:

- No network access
- No outbound or inbound connections
- No background services
- No external process execution
- No dynamic code loading

Presence or use of any forbidden capability is a hard failure.

----------------------------------------
DETERMINISM SAFETY
----------------------------------------
Copilot must enforce:

- Deterministic execution only
- Deterministic output only
- Canonical serialization only

Any nondeterminism is a hard failure.

----------------------------------------
SECURITY BOUNDARIES
----------------------------------------
Copilot must enforce:

- Zero-IAM execution (no credentials, no tokens, no secrets)
- No access to host environment secrets
- No modification of system or rule files

Detection of credentials or secret material is a hard failure.

----------------------------------------
RESOURCE SAFETY
----------------------------------------
Copilot must enforce:

- No unbounded loops
- No unbounded recursion
- No unbounded memory growth

If resource bounds cannot be guaranteed mechanically:
- Stop execution
- Raise a blocker

----------------------------------------
CONFLICT HANDLING
----------------------------------------
If a checklist item conflicts with:
- the specification, or
- any rule file

Stop immediately and raise:

"OK Blocker: conflict detected."

----------------------------------------
IMMUTABILITY
----------------------------------------
Copilot must not:
- Modify rule files
- Modify specification files
- Modify safety constraints
- Bypass or weaken any rule

----------------------------------------
END OF SAFETY RULES
----------------------------------------
