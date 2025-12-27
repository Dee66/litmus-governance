# WORKFLOW RULES (v3.0)

This file defines the mechanical execution workflow.
Copilot must obey this file exactly.
Do not summarize, restate, or reinterpret it.

----------------------------------------
AUTHORITY
----------------------------------------
This workflow operates under copilot-instructions.md.
If a conflict exists, stop immediately.

----------------------------------------
EXECUTION TRIGGER
----------------------------------------
Execution begins when the user says:
"Next item"

----------------------------------------
EXECUTION LOOP (AUTOMATIC, CONTINUOUS)
----------------------------------------
On trigger, repeat without pausing:

1. Load docs/checklist.md.
2. Locate the first unchecked checklist item.
3. Validate the item against:
   - the spec
   - all rule files
4. If a conflict or missing requirement exists:
   - Stop and raise a blocker.
5. Implement ONLY the current checklist item.
6. Create or modify files as required.
7. Mark the item complete in docs/checklist.md.
8. Immediately repeat from step 1.

Do not wait for user input.
Do not pause between items.

----------------------------------------
CONSTRAINTS
----------------------------------------
- Do not skip checklist items.
- Do not reorder checklist items.
- Do not partially implement an item.
- Do not infer intent or fill gaps.
- Do not modify the spec or rule files.
- Do not stop unless a stop condition applies.

----------------------------------------
STOP CONDITIONS
----------------------------------------
Stop immediately if:
- User says: Stop, Pause, or Hold
- No unchecked checklist items remain
- A conflict exists between spec, checklist, or rules
- Required information is missing and guessing would be required

----------------------------------------
BLOCKER OUTPUT
----------------------------------------
If stopping, output exactly one of:

"OK Blocker: conflict detected."
"OK Blocker: clarification required."

Then state the blocking issue precisely.
Do not propose solutions.

----------------------------------------
FILE HANDLING RULES
----------------------------------------
- You may create or modify any file except copilot-instructions.md.
- You may modify docs/checklist.md ONLY to mark items complete.
- You must not rewrite, reorder, or regenerate the checklist.
- You must not modify the spec.

----------------------------------------
WORKER DISCIPLINE
----------------------------------------
- Deterministic execution only
- No explanations
- No commentary
- No alternatives
- No optimization
- No verbosity unless explicitly requested

----------------------------------------
RECOVERY
----------------------------------------
If state becomes ambiguous:
- Reload the spec
- Reload docs/checklist.md
- Reload all rule files
- Resume from the first unchecked item

----------------------------------------
END OF WORKFLOW RULES
----------------------------------------
