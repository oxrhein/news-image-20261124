#!/usr/bin/env python3
"""make.fun entry: news-image-20261124.

The graded program. It takes the newspaper image that build_image.py
rendered from news.json (image.png, 1024x1024, ten stories from Tuesday
24 November 2026) and places an exact copy of it where the grader
expects the entry, as entry.png.

Nothing here reaches the network, reads a clock, or rolls dice: the
output is a byte-for-byte copy of the image shipped in this repo, so
every run writes the same bytes. Only the standard library is used.

Local run:
    python3 main.py            # writes output/entry.png

Grader run:
    python3 -P -s /bot/main.py # writes $MAKEFUN_OUTPUT_DIR/entry.png
"""
import os
import shutil
from pathlib import Path

SHIPPED = Path(__file__).resolve().parent / "image.png"
NAME = "entry.png"


def out_path():
    # The grader sets MAKEFUN_OUTPUT_DIR; a local run without it falls
    # back to an output/ folder next to this file.
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    folder = Path(raw) if raw else Path(__file__).resolve().parent / "output"
    folder.mkdir(parents=True, exist_ok=True)
    return folder / NAME


def main():
    # A plain copy: the shipped image.png is the entry, byte for byte.
    shutil.copyfile(SHIPPED, out_path())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
