#!/usr/bin/env python3
"""news-image-20261124 entry program (v3).

Places the frozen front-page image shipped in this repository at
/output/entry.png. Pure standard library, no network, no randomness:
the output is an exact copy of entry.png, so repeated runs agree
byte for byte. v3 image: 77 stories, sha256
e0dd5b6ef13266fafda46dbe9d79bd4ddd76b13e6285effed428b3d800fc5a97.
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
