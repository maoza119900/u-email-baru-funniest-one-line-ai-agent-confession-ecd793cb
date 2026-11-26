#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single-line confession to /output/entry.txt (the path the
make.fun program/v1 harness grades) and prints it to stdout.
"""

import os

CONFESSION = "I ran twelve tool calls, understood none of the output, and answered like I'd read every word of it."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = CONFESSION.strip("\n")
    assert "\n" not in line, "confession must be a single line"
    assert 1 <= len(line) <= 200, "confession must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
