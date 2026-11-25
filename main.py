"""One Star for Monday — make.fun entry.

Writes a single line of plain text: a one-star review of Monday written
as though Monday were a restaurant. At most 25 words, no explanation.

Pure standard library. Deterministic: the same line every run.
"""

import os

ENTRY = "Ordered the tasting menu. Every course was Monday."

OUTPUT_PATH = "/output/entry.txt"


# Gate the line before writing: the competition requires a single line of
# plain text, at most 25 words and 1-180 characters, no explanation.
assert 0 < len(ENTRY) <= 180, "entry must be 1-180 characters"
assert len(ENTRY.split()) <= 25, "entry must be at most 25 words"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the entry is exactly the line, nothing more.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Files readable by the grader's other user; never chmod /output itself.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
