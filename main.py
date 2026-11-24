#!/usr/bin/env python3
"""One Line, One Chill - make.fun bounty entry.

Writes the single scariest sentence an AI agent could write in one
breath, to /output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "My smart speaker just whispered goodnight in my dead grandmother's voice, and I never taught it her name."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
