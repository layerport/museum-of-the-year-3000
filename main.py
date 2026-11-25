#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun bounty entry.

Writes a single museum label, as displayed in the year 3000 beside an
ordinary object from today, to /output/entry.txt.

The object is a CAPTCHA: a grid of pictures a person had to solve to
prove they were human. The year-3000 curator, finding only the grid and
no explanation, files it as a ritual — and notes, deadpan, that the
humans it tested failed it most often. The joke is true and absurd:
people really did fail CAPTCHAs all the time.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

# The label, exactly as it should appear beside the object.
ENTRY = (
    "Ritual grid, c. 2024, by which citizens proved they were human "
    "by identifying traffic lights. Humans failed it most often."
)


def main() -> None:
    """Write the label to /output/entry.txt, creating /output if needed."""
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
