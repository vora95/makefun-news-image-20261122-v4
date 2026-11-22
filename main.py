#!/usr/bin/env python3
"""Ship the v4 front page for make.fun news-image-20261122.

THE DAY AS IT UNFOLDED is a finished 1024x1024 front page for Sunday
22 November 2026, drawn as code and shipped as entry.png. This script
is the entrypoint: it places that image into the harness output
directory. It needs nothing but the standard library — no network
access, no extra packages, no randomness — so the file it writes is
byte-for-byte the image in this repository, every single run.
"""
import os
import shutil
import sys
from pathlib import Path


def ship() -> None:
    """Copy the shipped front page into the harness output directory."""
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    outdir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    outdir.mkdir(parents=True, exist_ok=True)
    dst = outdir / "entry.png"
    shutil.copyfile(src, dst)
    got = dst.stat().st_size
    want = src.stat().st_size
    if got != want:
        print(f"copy size mismatch: got {got}, want {want}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    ship()
