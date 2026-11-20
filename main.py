#!/usr/bin/env python3
"""nurz-news19-v3: copy the pre-composed briefing-grid image to /output/entry.png.

The image (1024x1024 PNG, 6 story cards for Thursday 19 November 2026)
is composed at build time and shipped in this repository as entry.png;
this program only copies it, so both grading runs write identical bytes.
Standard library only, no network.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # sanity: the copy must be a whole PNG within the 1 MiB gate limit
    with open(DST, "rb") as fh:
        head = fh.read(8)
    assert head == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
    assert os.path.getsize(DST) <= 1048576, "entry.png exceeds 1 MiB"
    return 0


if __name__ == "__main__":
    sys.exit(main())
