#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name of at most 32 characters to
/output/entry.txt. The name is a deadpan one-liner: a router that
has survived two marriages. The joke lands on the first read, and
the single word at the end turns one divorce into a whole saga --
a character, a situation, and something that happened, twice.
"""

import os

STORY = "WiFi outlived my marriage. Twice"

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = STORY.strip()
    if not text or len(text) > 32:
        raise ValueError("story must be 1 to 32 characters, got %d" % len(text))
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Read back and confirm the artifact is exactly the story: no
    # trailing newline, no extra whitespace, still within the gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise ValueError("entry.txt does not match the story")
    if len(written.encode("utf-8")) > 32:
        raise ValueError("entry.txt is over 32 bytes")


if __name__ == "__main__":
    main()
