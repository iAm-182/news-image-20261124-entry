#!/usr/bin/env python3
"""news-image-20261124 entry program (v2).

Places the frozen front-page image shipped in this repository at
/output/entry.png. Pure standard library, no network, no randomness:
the output is an exact copy of entry.png, so repeated runs agree
byte for byte.
"""
import os
import shutil
import sys


def main() -> int:
    base = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(base, "entry.png")
    if not os.path.exists(source):
        print("entry.png is missing from the repository", file=sys.stderr)
        return 1
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(dest_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
