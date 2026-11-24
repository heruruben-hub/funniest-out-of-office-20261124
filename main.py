#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry.

Writes a single one-line out-of-office auto-reply to /output/entry.txt,
validates it against the competition gate (one line, 1-140 characters,
not only whitespace), and reads the file back to confirm it holds
exactly what was written.
"""

import os
import sys

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

REPLY = (
    "I'm out of office until Monday. My replacement is my dog, who has "
    "already approved your email by eating it."
)


def validate(text: str) -> None:
    """Check the reply against the competition gate."""
    if not text or not text.strip():
        raise ValueError("reply must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("reply must be a single line")
    if len(text) > 140:
        raise ValueError(
            f"reply is {len(text)} characters, over the 140 limit"
        )


def main() -> int:
    validate(REPLY)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REPLY)

    # Exact read-back: the file must hold precisely what was written,
    # and the text read back must pass the gate on its own too.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != REPLY:
        raise ValueError(
            "read-back mismatch: /output/entry.txt does not match "
            "the reply exactly"
        )
    validate(written)

    print(f"Wrote {len(REPLY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
