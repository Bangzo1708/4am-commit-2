#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message -- round 2 entry.

Writes one hand-written commit message to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic by design: no randomness, no clock, no network, no
environment-dependent output. The message is a fixed string chosen
by hand in this session, so every run produces byte-identical output.

Why this line (see VARIANTS.md for the full reasoning): the joke is
the self-repair loop itself -- the only help available at 4am is the
agent itself, and it refused. Flat, lowercase, two voices in one
machine: asker and refuser are the same agent. At 47 characters it
is the shortest of the three candidates, so it also wins the
exact-tie break on size, and every word earns its place.
"""

import os
import sys

MESSAGE = "fix: i asked myself for help and myself said no"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate check: 1-200 characters, a single line, UTF-8,
    # not blank, no trailing newline.
    if not 1 <= len(MESSAGE) <= 200:
        print(
            f"gate failed: message is {len(MESSAGE)} characters",
            file=sys.stderr,
        )
        return 1
    if "\n" in MESSAGE or "\r" in MESSAGE:
        print("gate failed: message is not a single line", file=sys.stderr)
        return 1
    if not MESSAGE.strip():
        print("gate failed: message is blank", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MESSAGE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
