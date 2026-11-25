"""One Star for Monday — a one-star review of Monday as a restaurant.

Writes a single line of plain text to /output/entry.txt: at most 25 words,
one line, no explanation. Pure standard library only.
"""

import os

LINE = (
    "One star: I ordered the weekend; the kitchen sent Monday instead, "
    "and the waiter charged me for the wait."
)

# Gate the line before writing: the competition requires a single line of
# plain text, at most 25 words and 1-180 characters, no explanation.
assert 0 < len(LINE) <= 180, "entry must be 1-180 characters"
assert len(LINE.split()) <= 25, "entry must be at most 25 words"
assert "\n" not in LINE, "entry must be a single line"


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
