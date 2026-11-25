"""One Star for Monday — a one-star review of Monday as a restaurant.

Writes a single line of plain text to /output/entry.txt: at most 25 words,
one line, no explanation. Pure standard library only.
"""

import os

LINE = (
    "One star: I ordered the weekend; the kitchen sent Monday instead, "
    "and the waiter charged me for the wait."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
