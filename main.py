"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt. The joke is a fixed string:
no clock, no randomness, no network, so two runs produce the same file.
"""

import os
import sys

JOKE = (
    "I keep my savings in the mattress, so every night I sleep on "
    "my investments and dream about the returns."
)

MAX_CHARS = 200


def main() -> int:
    text = JOKE

    if not text or not text.strip():
        print("entry is empty or only whitespace", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be one line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)

    # Read it back and confirm the file holds exactly the joke.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("entry.txt does not match the joke", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
