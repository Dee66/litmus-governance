# docs/checklist.md
# Litmus Engine  -  Deterministic Governance Checklist
# Execution-grade. Blind executor compatible.
# Do not reorder. Do not summarize. Do not reinterpret.

==================================================
GLOBAL CONVENTIONS (BINDING)
==================================================

[x] All files are UTF-8, LF line endings.
[x] All JSON is canonical: sorted keys, no insignificant whitespace.
[x] All comparisons are byte-for-byte.
[x] All failures invoke hard_fail(reason) and exit with code 1.
[x] All mutations modify exactly one byte in exactly one file.

==================================================
PHASE 0  -  EXECUTION SUBSTRATE & VALIDITY BASELINE
==================================================

[x] Fail execution if hard_fail does not terminate immediately.

[x] Define enum RunState with exact values: INVALID, REFUSED, ADVISORY, BLOCKING.
[x] Initialize run_state = INVALID at process start.
[x] Fail execution if run_state is ever unset.
[x] Fail execution if run_state transitions more than once.
[x] Fail execution if execution ends with run_state = INVALID.

[x] Require input file input/snapshot.bin.
[x] Fail execution if input/snapshot.bin is missing.
[x] Fail execution if any filesystem read occurs outside input/snapshot.bin and runs/**.

[x] Define run_id = SHA256(bytes of input/snapshot.bin).
[x] Fail execution if run_id depends on time, randomness, env, locale, or FS state.

[x] Create directory runs/.
[x] Fail execution if runs/ cannot be created.
[x] Create directory runs/<run_id>/ before any writes.
[x] Fail execution if any file is written outside runs/<run_id>/.

[x] Create file runs/README.invalid with exact bytes: "THIS DIRECTORY DEFINES VALIDITY.\n".
[x] Fail execution if README.invalid differs by any byte.

[x] Create schemas/decision_allowlist.json listing allowed decision artifact filenames.
[x] Fail execution if allowlist file missing or invalid.
[x] Fail execution if any *.decision.json file is not listed in allowlist.
[x] Fail execution if any decision artifact exists outside runs/<run_id>/.
[x] Fail execution if zero decision artifacts exist at end of run.
[x] Fail execution if more than one outcome artifact exists.
[x] Fail execution if run_state contradicts outcome artifact type.

[x] Emit runs/<run_id>/phase_0/proof.json with fields:
    - run_id
    - run_state
    - artifact_list
[x] Fail execution if proof is non-deterministic.

[x] Mutation M0: flip one bit in input/snapshot.bin.
[x] Fail execution if phase_0 proof does not change.

==================================================
PHASE 1  -  ABSOLUTE DETERMINISM
==================================================

[x] Forbid use of clocks, timestamps, UUIDs, RNGs, env vars, locale.
[x] Static scan src/** for forbidden symbols.
[x] Runtime guard forbidden syscalls.

[x] Enforce byte-wise lexicographic traversal for all collections.
[x] Re-sort after every filter, map, merge, aggregation.
[x] Fail execution if any traversal bypasses canonical sort.

[x] Forbid threads, async, executors, multiprocessing.
[x] Fail execution if more than one OS thread exists.

[x] Route all writes through canonical_write(path, bytes).
[x] Fail execution if any write bypasses canonical_write.

[x] Canonicalize or suppress stack traces.
[x] Fail execution on any determinism violation.

[x] Emit runs/<run_id>/phase_1/proof.json.
[x] Mutation M1: append byte to snapshot.
[x] Fail execution if proof does not change.

==================================================
PHASE 2  -  SNAPSHOT CANONICALIZATION
==================================================

[x] Snapshot format must be tar (ustar), no compression.
[x] Fail execution if snapshot format deviates.

[x] Normalize all paths to '/' and lowercase.
[x] Fail execution on path collisions.

[x] Strip all metadata: mtime, perms, ownership, inode.

[x] Resolve symlinks by inlining target bytes.
[x] Fail execution if target missing or recursive.

[x] Handle VCS directories atomically (all or nothing).

[x] Sort snapshot entries lexicographically by normalized path.

[x] Emit runs/<run_id>/phase_2/snapshot.canonical.bin.
[x] Emit runs/<run_id>/phase_2/proof.json.

[x] Mutation M2: add one empty file.
[x] Fail execution if snapshot or proof does not change.

==================================================
PHASE 3  -  EVIDENCE MODEL ENFORCEMENT
==================================================

[x] Evidence source is snapshot.canonical.bin only.
[x] Forbid reading comments entirely.
[x] Allow only: structure, config, contracts, tests, deps, versioning, migration.

[x] Forbid naming interpretation, sentiment, heuristics, intent inference.

[x] Normalize and sort all evidence lists.

[x] Emit runs/<run_id>/phase_3/evidence.json.
[x] Emit runs/<run_id>/phase_3/proof.json.

[x] Mutation M3: add one config file.
[x] Fail execution if evidence does not change.

==================================================
PHASE 4  -  NON-GOALS ENFORCEMENT
==================================================

[x] Forbid risk scoring, ranking, grading, optimization, exhaustive detection, refactoring.
[x] Static scan src/** for prohibited patterns.
[x] Runtime guard prohibited calls.

[x] Emit runs/<run_id>/phase_4/proof.json.
[x] Mutation M4: inject prohibited symbol.
[x] Fail execution if failure not triggered.

==================================================
PHASE 5  -  CLEVERNESS PROHIBITION
==================================================

[x] Forbid factories, builders, strategies, plugins, hooks, registries.
[x] Forbid reflection, dynamic dispatch, extensibility.
[x] Enforce duplication over inference.

[x] Emit runs/<run_id>/phase_5/proof.json.
[x] Mutation M5: add StrategyFactory symbol.
[x] Fail execution if failure not triggered.

==================================================
PHASE 6  -  GOVERNANCE SIGNATURE
==================================================

[x] Enumerate decision artifacts lexicographically.
[x] Canonically serialize all artifacts.
[x] Compute SHA256 over concatenated artifact bytes.

[x] Emit runs/<run_id>/phase_6/signature.json.

[x] Mutation M6: flip one byte in artifact.
[x] Fail execution if signature unchanged.

==================================================
PHASE 7  -  REFUSAL ENGINE
==================================================

[x] Emit dependency graph runs/<run_id>/phase_2/dependency_graph.json.
[x] Blast radius = reachable node count via BFS.

[x] Load rules/critical_paths.txt.
[x] Trigger refusal if any critical path lacks test.

[x] Trigger refusal if blast radius exceeds configured max.
[x] Trigger refusal on contradictory config keys.

[x] Emit refusal.decision.json when triggered.
[x] Fail execution if refusal missing when required.
[x] Fail execution if refusal coexists with other decisions.

[x] Mutation M7: add missing test.
[x] Fail execution if refusal unchanged.

==================================================
PHASE 8  -  MISLEADING SIGNAL RESTRAINT
==================================================

[x] Load rules/restraint_cases.json.
[x] Require exactly one restraint case.

[x] Define naive escalation as evidence.count > threshold.
[x] Emit restraint.decision.json.

[x] Mutation M8: remove referenced evidence.
[x] Fail execution if restraint unchanged.

==================================================
PHASE 9  -  ARCHITECTURAL POSTURE
==================================================

[x] Load rules/posture_matrix.json (exactly 4 archetypes).
[x] Conditions must be numeric comparisons only.
[x] Select first matching archetype.

[x] Emit posture.decision.json with validity window.

[x] Mutation M9: flip one condition.
[x] Fail execution if posture unchanged.

==================================================
PHASE 10  -  SAFE-TO-CHANGE SURFACE
==================================================

[x] Universe F = all snapshot paths.
[x] B(f) = dependency_count * posture_multiplier.
[x] tau loaded from rules.

[x] safe = B(f) <= tau.
[x] no_touch = complement of safe.
[x] Fail execution if overlap or omission.

[x] Emit surface.decision.json.

[x] Mutation M10: increase dependency count.
[x] Fail execution if surface unchanged.

==================================================
PHASE 11  -  MANDATORY FIRST MOVE
==================================================

[x] If refusal exists, emit no action.
[x] Else select lexicographically first safe file.

[x] Emit first_move.decision.json.

[x] Mutation M11: remove selected file from safe.
[x] Fail execution if action unchanged.


==================================================
PHASE 13  -  UNCERTAINTY BOUNDING
==================================================

[x] Load rules/claims.json.
[x] Claims are exactly those listed.
[x] Each claim marked known or unknown.
[x] Known claims must reference evidence.
[x] Unknown claims must not.

[x] Forbid absolute language for unknown claims.

[x] Emit uncertainty.decision.json.

[x] Mutation M13: add evidence resolving claim.
[x] Fail execution if unknown count unchanged.

==================================================
PHASE 14  -  MULTI-LANGUAGE BOUNDARY CONTROL
==================================================

[x] Detect language by extension only.
[x] Select primary language by highest count.
[x] Fail execution on tie.

[x] Forbid semantic references to secondary languages.

[x] Emit language_boundary.decision.json.

[x] Mutation M14: add file of new language.
[x] Fail execution if boundaries unchanged.

==================================================
PHASE 15  -  ARTIFACT-ONLY INTERFACE
==================================================

[x] Forbid stdin/stdout usage.
[x] Forbid UI, CLI, prompts, dashboards.
[x] Forbid decision content in logs.

[x] Emit interface.proof.json.

[x] Mutation M15: add print() call.
[x] Fail execution if failure not triggered.

==================================================
PHASE 16  -  CANONICAL RUNS & FINAL LITMUS
==================================================

[x] Create runs/canonical/{success,refusal,restraint}/.
[x] Each canonical run must include full artifact set.

[x] Emit checksums.json of all canonical artifacts.
[x] Re-run engine and verify byte-for-byte equality.

[x] Mutation M16: flip one byte in canonical snapshot.
[x] Fail execution if outputs unchanged.

[x] Verify cross-artifact consistency.
[x] Verify incorrectness is obvious when artifacts missing.
[x] Verify silence where required.

[x] Emit final.verdict.json with verdict VALID and signature.

==================================================
END OF CHECKLIST
==================================================
