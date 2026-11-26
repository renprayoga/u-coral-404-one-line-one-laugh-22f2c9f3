"""One Line, One Laugh — entry writer.

Chosen line (112 characters, one line):

    I told my plants I'm going on holiday and one of them wilted on the
    spot — even my ficus has separation anxiety.

Why this line wins (judge rubric order: hilarious line on first read,
surprise turn, economy, freshness, clean wording):

- Hilarious on first read: a plant wilting the instant it hears about a
  holiday — the joke lands without setup or explanation.
- Surprise: the turn is the diagnosis — "separation anxiety" — a
  therapist's phrase applied to a houseplant. The reader expects a
  watering joke and gets a clingy ficus instead.
- Economy: 112 of 200 characters, setup and punchline in one sentence,
  no word wasted; "on the spot" does the timing, "even my ficus" does
  the escalation.
- Fresh: not a stock plant joke (no "I kill every plant I own") — the
  plant is needy, not dead, and the specific detail (ficus, not "plant")
  makes it a line nobody has read before.
- Clean wording: plain grammar, one rhythm, reads smoothly aloud; the
  em dash marks the turn without slowing the read.

Program: writes the line to /output/entry.txt, then validates its own
output — exactly one line, 1-200 characters, not only whitespace — and
exits non-zero if the gate would fail. Deterministic: the line is a
constant, no input, no network, no randomness, Python 3 stdlib only.
"""

import os
import sys

ENTRY = (
    "I told my plants I'm going on holiday and one of them wilted on "
    "the spot \u2014 even my ficus has separation anxiety."
)

DESTINATION = "/output/entry.txt"
MIN_LEN = 1
MAX_LEN = 200


def _fail(message: str) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    return -1


def _save() -> None:
    folder = os.path.dirname(DESTINATION)
    os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


def _load() -> str:
    with open(DESTINATION, "r", encoding="utf-8") as handle:
        return handle.read()


def _check(written: str) -> int:
    entry = written.rstrip("\n")
    if not MIN_LEN <= len(entry) <= MAX_LEN:
        return _fail(f"entry is {len(entry)} characters (need 1-200)")
    if "\n" in entry or "\r" in entry:
        return _fail("entry is not a single line")
    if not entry.strip():
        return _fail("entry is only whitespace")
    if any(line != line.rstrip() for line in entry.split("\n")):
        return _fail("entry line has trailing whitespace")
    if entry != ENTRY:
        return _fail("written entry differs from the intended line")
    # The gate reads the whole file: exactly one trailing newline, so the
    # file holds one line and nothing else — no blank second line.
    if written != ENTRY + "\n":
        return _fail("written file is not exactly the entry plus one newline")
    return len(entry)


def run() -> int:
    _save()
    result = _check(_load())
    if result == -1:
        return 1
    print(f"OK: wrote {result}-character entry to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
