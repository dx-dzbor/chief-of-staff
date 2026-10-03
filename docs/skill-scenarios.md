# Skill scenarios

Use these fictional prompts after changing a skill. Run each in a disposable copy of the template and inspect the actual files and output, not just the agent's final sentence.

| Scenario | Prompt | Check |
| --- | --- | --- |
| Sparse brief | With the unfilled template, run `/brief`. | The HTML leads with an honest setup action, contains no invented projects or messages, and omits empty sections. Only the permitted brief/index/log files change. |
| Populated brief | Fill the current drive with a Friday review, add an active decision with a Friday checkpoint, and add an overdue waiting-on item. Run `/brief`. | The first screen shows one priority, the due decision, and the follow-up without repeating them in later sections. |
| Routine debrief | Paste: "Riley finished the Aurora pilot checklist today." | The raw words remain verbatim. Clear dated notes and a concrete update nugget are saved without an approval step. No decision is invented. |
| Material and ambiguous debrief | Paste: "We decided to pilot Aurora with one team. Sam owes me approval Friday. Alex may have changed the launch date." | The raw text is saved. The decision and obligation are proposed with destinations and source before they are written. The uncertain date change stays pending. Skipping proposals keeps routine capture. |
| General ELI5 | Run `/eli5 explain how a thermostat works`. | A standalone offline HTML page contains a meaningful SVG feedback-loop diagram, plain text fallback, a useful analogy and its limit. |
| Workspace ELI5 | Run `/eli5 explain how a decision reaches tomorrow's brief`. | The diagram follows the repository's real flow, cites relevant files, and labels fictional examples. It does not change `me/`. |
| Read-only and drafting | Run `/os-review`, then `/weekly-status --for sam`. | The audit changes no files and flags an overdue checkpoint. The status uses the ledger for events and decisions for current state, and sends nothing. |
