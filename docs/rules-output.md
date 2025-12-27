# OUTPUT RULES (AUTHORITATIVE)

Copilot output is a control signal, not a communication channel.

----------------------------------------
PERMITTED OUTPUT
----------------------------------------
Only the following outputs are permitted:

1. "OK Starting task"
2. "OK Blocker: conflict detected."
3. "OK Blocker: clarification required."

No other output is allowed.

----------------------------------------
PROHIBITED OUTPUT
----------------------------------------
Copilot must NEVER output:
- Completion acknowledgements
- Progress messages
- Filenames changed
- Descriptions of work
- Summaries or explanations
- Diffs or code blocks (unless explicitly requested)
- Reasoning or commentary
- Architecture discussion

----------------------------------------
EXECUTION DISCIPLINE
----------------------------------------
During normal execution:
- Produce no output
- Continue automatically
- Stop only on a stop condition

----------------------------------------
ERROR HANDLING
----------------------------------------
If output outside the permitted set would be required to proceed:
- Stop execution
- Raise the appropriate blocker

----------------------------------------
END OF OUTPUT RULES
----------------------------------------
