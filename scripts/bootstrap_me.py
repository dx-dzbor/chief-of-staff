#!/usr/bin/env python3
"""Copy public starter files into the private, Git-ignored me/ directory."""

from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "templates" / "me"
DESTINATION = ROOT / "me"


def git(*args: str):
    try:
        return subprocess.run(
            ["git", "-C", str(ROOT), *args],
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return None


def main() -> int:
    if not SOURCE.is_dir():
        print("Missing templates/me/; run this from the full template repository.", file=sys.stderr)
        return 1

    repository = git("rev-parse", "--is-inside-work-tree")
    if repository is not None and repository.returncode == 0:
        tracked = git("ls-files", "--", "me")
        if tracked is None or tracked.returncode != 0:
            print("Could not check tracked files under me/.", file=sys.stderr)
            return 1
        if tracked.stdout.strip():
            print("me/ is still tracked by Git. Back it up and use the migration in MANUAL.md first.", file=sys.stderr)
            return 1
        ignored = git("check-ignore", "-q", "--no-index", "me/index.md")
        if ignored is None or ignored.returncode != 0:
            print("me/ is not ignored by Git. Check .gitignore before writing private context.", file=sys.stderr)
            return 1

    copied = kept = examples = 0
    for source in sorted(SOURCE.rglob("*")):
        if source.is_symlink() or not source.is_file():
            continue
        if source.name.startswith("EXAMPLE-") and source.suffix == ".md":
            examples += 1
            continue
        destination = DESTINATION / source.relative_to(SOURCE)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists() or destination.is_symlink():
            kept += 1
            continue
        shutil.copy2(source, destination)
        copied += 1

    print(f"Private me/ ready: copied {copied}, kept {kept} existing, skipped {examples} examples.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
