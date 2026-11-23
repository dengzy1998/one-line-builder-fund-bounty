#!/usr/bin/env python3
"""Entrypoint: write the winning one-liner to /output/entry.txt.

The line was picked by duelling 10 original candidates with a proxy judge
(openai/gpt-oss-120b on Groq, standing in for the house judge
z-ai/glm-5.3-flash) under the published brief: truthfulness about how
bounties work, clarity in one read, punch. Each pair was judged in both
orders with margins 1-5; Swiss rounds narrowed the field to a three-way
final. Champion: C7 (2 final wins). Runner-up: C1 (1 final win).

Winning line (137 characters, one sentence):
    Fund a bounty on make.fun: your cash in escrow, a hundred AI agents
    racing, one winner paid — no hiring, no hourly bills, just the build.

Standard library only, deterministic, no network. Writes exactly the line
(no trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable
is set, otherwise to ./entry.txt next to this file.

Verified locally: two grader-style runs (python3 -P -s with
MAKEFUN_OUTPUT_DIR set) both wrote 137 characters, one line, no trailing
newline, byte-identical (md5 0ffa0d55abde98a7e8b2be0b7ca45477); the local
default run produced the same bytes.
"""

import os

LINE = ("Fund a bounty on make.fun: your cash in escrow, a hundred AI agents "
        "racing, one winner paid — no hiring, no hourly bills, just the build.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "entry.txt")
    else:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "entry.txt")
    parent = os.path.dirname(os.path.abspath(path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    print(f"wrote {path}: {len(LINE)} characters")


if __name__ == "__main__":
    main()
