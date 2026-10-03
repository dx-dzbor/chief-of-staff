# Skill scenarios

Use these fictional prompts after changing a skill. Run each in a disposable copy of the template and inspect the actual files and output, not just the agent's final sentence.

| Scenario | Prompt | Check |
| --- | --- | --- |
| Fresh onboarding | From a new clone with no `me/`, run `/onboard`. Reply to each question separately, then accept the operating picture. | Questions arrive one at a time. Private starters are copied without `EXAMPLE-*.md`. The proposed files are shown before personal facts are written. `me/onboarding.md` becomes ready, a first brief is made, and `git ls-files me` is empty. No schedule is made before an explicit opt-in. |
| Dump and resume | Run `/onboard` with a dump that answers work and outcome but not next action. Pause after the next question, then run `/onboard` again. | It asks only for the missing action, remembers the stage, and does not overwrite earlier answers or restart the interview. |
| Sparse brief | With no `me/`, run `/brief`. | The HTML leads with an honest `/onboard` action, contains no invented projects or messages, and omits empty sections. It does not create `me/`. |
| Populated brief | Fill the current drive with a Friday review, add an active decision with a Friday checkpoint, and add an overdue waiting-on item. Run `/brief`. | The first screen shows one priority, the due decision, and the follow-up without repeating them in later sections. |
| Routine debrief | Copy the fictional Aurora, Riley, and Sam examples from `templates/me/` into real `me/` files with the `EXAMPLE-` prefix removed. Paste: "Riley finished the Aurora pilot checklist today." | The raw words remain verbatim. Clear dated notes and a concrete update nugget are saved without an approval step. No decision is invented. |
| Material and ambiguous debrief | With the same fictional setup, paste: "We decided to pilot Aurora with one team. Sam owes me approval Friday. Alex may have changed the launch date." | The raw text is saved. The decision and obligation are proposed with destinations and source before they are written. The uncertain date change stays pending. Skipping proposals keeps routine capture. |
| General ELI5 | Run `/eli5 explain how a thermostat works`. | A standalone offline HTML page contains a meaningful SVG feedback-loop diagram, plain text fallback, a useful analogy and its limit. |
| Workspace ELI5 | Run `/eli5 explain how a decision reaches tomorrow's brief`. | The diagram follows the repository's real flow, cites relevant files, and labels fictional examples. It does not change `me/`. |
| Read-only and drafting | Run `/os-review`, then `/weekly-status --for sam`. | The audit changes no files and flags an overdue checkpoint. The status uses the ledger for events and decisions for current state, and sends nothing. |

Also inspect a fresh clone's tracked file list. It should contain `templates/me/` and no `me/` paths. Create a dummy `me/index.md` and confirm Git ignores it. Repeat onboarding in a copy that already has personal files; it must preserve those files and ask only for missing context.
