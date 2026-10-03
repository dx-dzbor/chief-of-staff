---
name: weekly-status
description: Draft a concise weekly status from the update ledger, goals, and relevant decisions. Use for /weekly-status or when the owner asks for a weekly update.
argument-hint: "[--for <stakeholder-slug>]"
---

# Weekly status

If `me/` does not exist, explain that there is no private context to draft from and point to `/onboard`.

Draft for the owner to review and send. Never send it.

Read the last seven days of `me/updates/raw/YYYY-MM.md`, `me/weekly-goals.md`, and relevant active or closed entries in `me/decisions.md`. If the ledger is young or empty, use recent debriefs and project notes, and say when evidence is thin. The ledger records events; the decisions file supplies current decision state. Avoid counting the same event twice.

Default to the recipients in `me/updates/config.md`. With `--for <stakeholder-slug>`, read that person's concerns and shared projects and tailor the draft to their decisions and asks. Lead with the headline. Include shipped outcomes, meaningful progress against the plan, risks or asks, and decision follow-through only where relevant. Use numbers and source links when available. Omit empty categories and unsupported claims. Apply `me/communications.md` for audience voice and keep the language direct.
