#!/usr/bin/env python3
"""Coolest-art v4 entry: copy the bundled striking-snake artwork to the output.

The artwork is a giant snake coiled around a big building, its head
raised at the top and lunging downward as if about to strike — a
597x896 PNG, 883,792 bytes, inside the competition's 1 MiB and
1024x1024 limits. The program does one deterministic thing: copy
those exact bytes to $MAKEFUN_OUTPUT_DIR/entry.png (or
/output/entry.png), so both grading runs write identical output. The
sha256 comparison below checks the full content, not just the size,
so a truncated copy can never silently pass.
"""
import hashlib
import os
import shutil

# Artwork facts (v4): entry.png is the striking snake, 597x896 PNG,
# 883,792 B, sha256 7bb05a1d.... The full-content sha256 check below
# (not just size) guarantees a truncated or corrupted copy is rejected
# instead of graded. The image follows the top-10 leaderboard
# patterns: a giant creature plus a building for scale, glowing gold
# against a dark dusk sky, and one clear surreal idea in a single
# sentence — "a giant snake about to strike, coiled around a tower".

SRC_NAME = "entry.png"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, SRC_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guarantee the deterministic-bytes requirement: the output must be
    # byte-identical to the bundled artwork, so fail loudly instead of
    # silently leaving a partial file if the copy is ever interrupted.
    # Size alone is a weak check (a truncated copy could keep the size
    # only by coincidence), so compare the full content hash too.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise RuntimeError("entry.png copy incomplete")
    with open(src, "rb") as f:
        src_hash = hashlib.sha256(f.read()).hexdigest()
    with open(dst, "rb") as f:
        dst_hash = hashlib.sha256(f.read()).hexdigest()
    if src_hash != dst_hash:
        raise RuntimeError("entry.png copy corrupted")


if __name__ == "__main__":
    main()
