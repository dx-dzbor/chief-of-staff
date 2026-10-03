---
name: os-review
description: Run a read-only health audit of the Personal OS, including overdue decision checkpoints, stale commitments, and missing context. Use for /os-review or an OS health check.
---

# OS review

Read the relevant `me/` files and report only. Never write files or resolve an item during the audit.

Check active `me/decisions.md` records for checkpoints due today or overdue, missing follow-through where the source says an action exists, and decisions that appear closed in notes but remain active. Check `me/waiting-on.md` for overdue or stale commitments. Then check stale advice (over 14 days), projects without meaningful updates (7 or 14 days according to coverage), dormant key relationships, frontmatter or alias errors, orphaned files, and unfinished placeholders or example files.

Lead with the few findings that need action. For each, give the evidence path, owner if known, and a specific suggested next step. Group lower-priority maintenance items afterward. Distinguish a genuinely overdue item from a missing date or unavailable signal. Do not manufacture severity from inactivity alone.
