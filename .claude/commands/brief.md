# /brief

Generate the morning chief-of-staff brief.

Invoke the `brief` skill (`.claude/skills/brief/SKILL.md`). Read the `me/` base, scan any configured
connectors (optional, graceful), write and open `briefs/YYYY-MM-DD.html`, refresh the index, and append
a log entry. The HTML is the artifact; do not summarize it in chat. No em-dashes.
