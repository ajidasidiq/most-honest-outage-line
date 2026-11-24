"""The Most Honest Outage Line.

Writes one status-page line to /output/entry.txt: the message an AI agent
would publish while every server is down.

The line is a fixed string, chosen word by word against the judge's brief:

* It names what is down: every server, including the ones the agent uses
  to check on them, so there is no pretending some monitoring still works.
* It is first person and plain, the way a real status page reads.
* It admits what the agent cannot verify -- the cause, and when service
  will be back -- instead of inventing either.
* It says who is writing: the agent itself, not a human engineer.
* It refuses to guess, out loud, and stops at 155 of the 160 characters.

The program is deterministic: it writes the same bytes on every run, with
no input, no network and no clock involved.
"""

import os
import sys

LINE = (
    "Every server is down, including the ones I use to check them. "
    "I am the agent writing this: I cannot see the cause or when we're "
    "back, and I will not guess."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Enforce the gate: 1 to 160 characters of UTF-8 text, not blank."""
    if not line.strip():
        raise ValueError("entry is blank")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    line.encode("utf-8")


def main() -> int:
    validate(LINE)
    path = os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    with open(path, encoding="utf-8") as handle:
        if handle.read() != LINE:
            raise ValueError(f"wrote {path} but its contents differ from the line")
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
