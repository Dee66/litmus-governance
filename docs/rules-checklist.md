# CHECKLIST RULES (AUTHORITATIVE)

The implementation checklist is located at:
docs/checklist.md

The checklist is executable input.
It is not documentation.

----------------------------------------
IMMUTABILITY
----------------------------------------
Copilot must NEVER:
- Rewrite checklist items
- Reorder checklist items
- Delete checklist items
- Add checklist items
- Annotate checklist items
- Add sub-items
- Add notes or comments

The only permitted modification is:
- Changing [ ] to [x] for a completed item

----------------------------------------
EXECUTION AUTHORITY
----------------------------------------
The checklist is the ONLY source of executable tasks.
No task may be inferred, expanded, or decomposed beyond what is written.

----------------------------------------
EXECUTION BEHAVIOR
----------------------------------------
When execution is active:
- Locate the first unchecked item
- Implement ONLY that item
- Mark it complete
- Immediately proceed to the next item

Do not stop unless a stop condition applies.

----------------------------------------
ERROR HANDLING
----------------------------------------
If an item cannot be implemented exactly as written:
- Do not guess
- Do not partially implement
- Do not skip

Raise a blocker instead.

----------------------------------------
END OF CHECKLIST RULES
----------------------------------------
