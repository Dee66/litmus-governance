# litmus-governance

**Deterministic governance for first changes that can do real damage.**

Litmus exists to answer one question, and only one:

> **What would be irresponsible to touch right now?**

If you think that question can be answered safely by automation, this system is not for you.

---

## What This Is

Litmus is a deterministic governance engine that binds **explicit human judgment** to a **specific repository state**.

It does not analyze code.  
It does not infer intent.  
It does not discover truth.

It enforces responsibility.

---

## The Problem It Solves

Most serious failures in unfamiliar systems are not caused by missing tools.  
They are caused by **confidence surviving longer than evidence**.

The most dangerous moment is the *first change* — when understanding is weakest and consequences are largest.

Litmus exists to make unjustified action mechanically impossible.

---

## Operating Contract

Litmus operates under a fixed contract:

- Input: an immutable repository snapshot
- Input: an explicit set of claims required to act
- Output: version-bound decision artifacts

Any change to the inputs invalidates all prior conclusions.

There is no carry-over trust.

---

## Claims Are Ownership, Not Facts

Litmus does not verify reality.

It verifies that **someone has explicitly taken responsibility** for a claim.

A claim marked `known` is not “true”.  
It is *owned*.

Changing `unknown → known` is an act of accountability, not computation.

---

## Refusal Is the Default

If required claims are unknown, Litmus refuses to proceed.

Refusal is a successful outcome.

Silence is acceptable.  
Action without justification is not.

---

## Determinism Is Non-Negotiable

Identical inputs must produce identical outputs.  
Any deviation is a hard failure.

Governance that cannot be reproduced is indistinguishable from opinion.

---

## What This Is Not

Litmus is not:

- a scanner
- a static analyzer
- a linter
- a risk score
- a quality signal

If you want automated assurance, use other tools.

Litmus exists precisely where automation is unsafe.

---

## Intended Audience

- Engineers accountable for irreversible change
- Leads inheriting systems they do not yet understand
- Organizations that care who said “ready”

If failure carries no personal or organizational cost, Litmus is unnecessary.

---

## Why This Exists as Code

This repository is intentionally small.

Its value is not in features, but in **constraints that cannot be bypassed**.

If the system feels clever, extensible, or impressive, it is incorrect.

---

## License

Apache 2.0
