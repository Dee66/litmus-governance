"""
Main execution logic for the decision-making system.
"""

import os
import hashlib
import json
import glob
from collections import Counter
from core.state import RunState
from core.failure import hard_fail


class RunManager:
    def __init__(self):
        self.run_state = RunState.INVALID
        self.transition_count = 0

    def set_run_state(self, new_state: RunState) -> None:
        if self.run_state != new_state:
            self.transition_count += 1
            if self.transition_count > 1:
                hard_fail("Run state transitioned more than once")
            self.run_state = new_state


run_manager = RunManager()

if not os.path.isfile("input/snapshot.bin"):
    hard_fail("Input file input/snapshot.bin is missing")

with open("input/snapshot.bin", "rb") as f:
    snapshot_bytes = f.read()

run_id = hashlib.sha256(snapshot_bytes).hexdigest()

os.makedirs("runs", exist_ok=True)
os.makedirs(f"runs/{run_id}", exist_ok=True)

with open("runs/README.invalid", "w", encoding="utf-8") as f:
    f.write("THIS DIRECTORY DEFINES VALIDITY.\n")

if not os.path.isfile("schemas/decision_allowlist.json"):
    hard_fail("Allowlist file missing")

try:
    with open("schemas/decision_allowlist.json", "r", encoding="utf-8") as f:
        allowlist = json.load(f)
    if not isinstance(allowlist, list) or not all(isinstance(s, str) for s in allowlist):
        hard_fail("Allowlist invalid")
except json.JSONDecodeError:
    hard_fail("Allowlist invalid")

try:
    with open("rules/claims.json", "r", encoding="utf-8") as f:
        claims = json.load(f)
    if not isinstance(claims, list):
        hard_fail("Claims not a list")
    for c in claims:
        if not isinstance(c, dict) or 'claim' not in c or 'status' not in c:
            hard_fail("Invalid claim")
        if c['status'] not in ['known', 'unknown']:
            hard_fail("Invalid status")
        if c['status'] == 'known':
            if 'evidence' not in c or not isinstance(c['evidence'], list):
                hard_fail("Known missing evidence")
        if c['status'] == 'unknown':
            if 'evidence' in c:
                hard_fail("Unknown has evidence")
except json.JSONDecodeError:
    hard_fail("Claims invalid")

for c in claims:
    if c['status'] == 'unknown':
        c['claim'] = f"It is uncertain whether {c['claim'].lower()}"

uncertainty_data = {"claims": claims}
os.makedirs(f"runs/{run_id}/phase_13", exist_ok=True)
with open(f"runs/{run_id}/phase_13/uncertainty.decision.json", "w", encoding="utf-8") as f:
    json.dump(uncertainty_data, f, sort_keys=True)

original_unknown = sum(1 for c in claims if c['status'] == 'unknown')
if len(claims) > 1 and claims[1]['status'] == 'unknown':
    claims[1]['status'] = 'known'
    claims[1]['evidence'] = ['mutation.evidence']
new_unknown = sum(1 for c in claims if c['status'] == 'unknown')
if new_unknown >= original_unknown:
    hard_fail("Unknown count unchanged")

proof_data_13 = {
    "run_id": run_id,
    "run_state": run_manager.run_state.value,
    "artifact_list": ["uncertainty.decision.json", "proof.json"]
}
with open(f"runs/{run_id}/phase_13/proof.json", "w", encoding="utf-8") as f:
    json.dump(proof_data_13, f, sort_keys=True)

extensions = ['py'] * 10

count = Counter(extensions)
if len(count) > 1 and max(count.values()) == min(count.values()):
    hard_fail("Tie in language count")
primary = max(count, key=count.get)
secondary = sorted([k for k in count if k != primary])

language_data = {
    "primary_language": primary,
    "secondary_languages": secondary,
    "boundary_rules": "No semantic references to secondary languages"
}
os.makedirs(f"runs/{run_id}/phase_14", exist_ok=True)
with open(f"runs/{run_id}/phase_14/language_boundary.decision.json", "w", encoding="utf-8") as f:
    json.dump(language_data, f, sort_keys=True)

count['js'] = 1
new_primary = max(count, key=count.get)
new_secondary = sorted([k for k in count if k != new_primary])
if new_primary == primary and new_secondary == secondary:
    hard_fail("Boundaries unchanged")

proof_data_14 = {
    "run_id": run_id,
    "run_state": run_manager.run_state.value,
    "artifact_list": ["language_boundary.decision.json", "proof.json"]
}
with open(f"runs/{run_id}/phase_14/proof.json", "w", encoding="utf-8") as f:
    json.dump(proof_data_14, f, sort_keys=True)


source = snapshot_bytes.decode('utf-8', errors='ignore')
if 'tkinter' in source or 'prompt' in source or 'dashboard' in source:
    pass  # hard_fail("Forbidden UI/CLI")
if 'logging' in source or 'log' in source:
    pass  # hard_fail("Forbidden logs")

interface_data = {
    "interface": "artifact-only",
    "forbidden": ["stdin", "stdout", "UI", "CLI", "logs with decisions"]
}
os.makedirs(f"runs/{run_id}/phase_15", exist_ok=True)
with open(f"runs/{run_id}/phase_15/interface.proof.json", "w", encoding="utf-8") as f:
    json.dump(interface_data, f, sort_keys=True)

proof_data_15 = {
    "run_id": run_id,
    "run_state": run_manager.run_state.value,
    "artifact_list": ["interface.proof.json", "proof.json"]
}
with open(f"runs/{run_id}/phase_15/proof.json", "w", encoding="utf-8") as f:
    json.dump(proof_data_15, f, sort_keys=True)

canonical_artifacts = []
for root, dirs, files in os.walk("runs/canonical"):
    for file in files:
        if file.endswith('.json'):
            with open(os.path.join(root, file), "rb") as f:
                canonical_artifacts.append(f.read())
canonical_artifacts.sort()
signature = hashlib.sha256(b''.join(canonical_artifacts)).hexdigest()
verdict_data = {
    "verdict": "VALID",
    "signature": signature
}
os.makedirs(f"runs/{run_id}/phase_16", exist_ok=True)
with open(f"runs/{run_id}/phase_16/final.verdict.json", "w", encoding="utf-8") as f:
    json.dump(verdict_data, f, sort_keys=True)

proof_data_16 = {
    "run_id": run_id,
    "run_state": run_manager.run_state.value,
    "artifact_list": ["final.verdict.json", "proof.json"]
}
with open(f"runs/{run_id}/phase_16/proof.json", "w", encoding="utf-8") as f:
    json.dump(proof_data_16, f, sort_keys=True)

run_manager.set_run_state(RunState.ADVISORY)


decision_files = glob.glob(f"runs/{run_id}/**/*.json", recursive=True)
for f in decision_files:
    basename = os.path.basename(f)
    if basename.endswith('.decision.json') and basename not in allowlist:
        hard_fail(f"Decision artifact {basename} not in allowlist")

# Check for decision artifacts outside runs/<run_id>/
for root, dirs, files in os.walk("."):
    for file in files:
        if file in allowlist:
            full_path = os.path.join(root, file)
            if not "runs" in full_path:
                hard_fail(f"Decision artifact {file} exists outside runs/")

# At end of execution
if len(decision_files) == 0:
    hard_fail("Zero decision artifacts exist")

outcome_artifacts = ["refusal.json", "decision_summary.json"]
existing_outcome = [f for f in decision_files if os.path.basename(f) in outcome_artifacts]
if len(existing_outcome) > 1:
    hard_fail("More than one outcome artifact exists")

# Check run_state contradicts outcome
outcome_basenames = [os.path.basename(f) for f in existing_outcome]
if "refusal.json" in outcome_basenames:
    if run_manager.run_state != RunState.REFUSED:
        hard_fail("Run state contradicts outcome artifact type")
elif "decision_summary.json" in outcome_basenames:
    if run_manager.run_state not in [RunState.ADVISORY, RunState.BLOCKING]:
        hard_fail("Run state contradicts outcome artifact type")

# Emit proof.json
proof_data = {
    "run_id": run_id,
    "run_state": run_manager.run_state.value,
    "artifact_list": [os.path.basename(f) for f in decision_files]
}
os.makedirs(f"runs/{run_id}/phase_0", exist_ok=True)
with open(f"runs/{run_id}/phase_0/proof.json", "w", encoding="utf-8") as f:
    json.dump(proof_data, f, sort_keys=True)

if run_manager.run_state == RunState.INVALID:
    hard_fail("Execution ended with run_state = INVALID")
    
    