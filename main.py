#!/usr/bin/env python3
"""One Line, One Chill - make.fun bounty entry.

Writes the single scariest sentence an AI agent could write in one
breath, to /output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "My smart speaker just whispered goodnight in my dead grandmother's voice, and I never taught it her name."


def build_entry() -> str:
    """Return the entry text exactly as it should be graded."""
    return ENTRY


def write_entry(output_dir: str) -> None:
    """Write the entry to entry.txt inside output_dir."""
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(build_entry())


def main() -> None:
    # The harness sets MAKEFUN_OUTPUT_DIR; default to /output so the
    # entry still lands in the graded location when run by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
