---
name: debrief
description: Prompt the user for an end-of-day debrief and route it into the right Personal OS files. Use when the user types /debrief or asks to debrief the day.
---

# Debrief Skill

Use this skill when the user types `/debrief` or asks to debrief the day.

## Behavior

Do not run anything. Do not write files. Do not summarize yet.

Respond with exactly:

```text
Okay, give me the debrief of your day. I will route it into the right projects, stakeholders, team
notes, exec steer, and the update ledger, and show you the plan before writing anything.
```

Then wait for the user to provide the debrief.

## After The User Provides The Debrief

1. **Route each line.** Match it against project and person `aliases` to decide where it belongs:
   - project `## Notes`
   - stakeholder `## Interaction Log`, or `## Advice & Suggestions` when advice keywords appear
   - team `## Notes`, or a team `## Stakeholder Feedback` section when it is feedback about them
   - `me/exec_steer.md` when it is standing guidance from leadership
2. **Extract two special buckets:**
   - waiting-on items (route to `me/waiting-on.md`)
   - update-worthy nuggets for the ledger
3. **Append ledger nuggets** to `me/updates/raw/YYYY-MM.md` in the format
   `- [type] (proj: <slug>; ppl: <slug>) <one concrete line, numbers where possible>`, where `type` is
   one of `shipped | progress | decision | win | risk | ask | narrative`.
4. **Show the full routing plan and wait for approval before writing anything.**
5. **On approval:** append entries under dated `### YYYY-MM-DD` headings (oldest-first), turning any
   relative dates into absolute ones; save the full raw dump to `me/debriefs/YYYY-MM-DD.md`. Never post
   to Slack or email. Drafts only. No em-dashes.

If a line does not match any known project or person, say so and ask where it should go (or whether to
create a new file from the relevant `_TEMPLATE.md`) rather than guessing.
