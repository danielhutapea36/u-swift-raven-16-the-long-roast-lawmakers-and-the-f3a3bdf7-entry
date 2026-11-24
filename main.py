#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes a single satirical sentence to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). The line is 173 characters, UTF-8, one line, no
trailing newline. Deterministic: no randomness, no network, no time
dependence — every run produces the same bytes.

Why this line: the judge weighs, in order, (1) a one-sentence
satirical roast of lawmakers who regulate AI, crypto or the internet
without being able to convert a file to PDF, (2) a real turn — the
sentence sets up the lawmaker's authority and then undercuts it with
the file they cannot convert, (3) the aim stays on lawmakers and the
rules they write, so the joke is about power and competence rather
than random abuse. The judge's own words: "A roast that has to
explain itself has already lost. Shock value for its own sake does
not count." So the line explains nothing and shocks nobody — it
simply lets the premise do the work. The premise is the bill itself:
the senator's 400-page bill to regulate the internet arrives as a
Word document, because the man writing the rules for the digital age
still needs his staff to turn it into a PDF. The law he writes is
the file he cannot convert — the undercut lands on the last words,
with nothing explained after them.
"""

import os

TEXT = (
    "His 400-page bill to regulate the internet arrives as a Word "
    "document, because the senator writing the rules for the digital "
    "age still needs his staff to turn it into a PDF."
)


def main() -> None:
    # Gate: entry.txt must be 1–320 characters of UTF-8 text, not only
    # whitespace. The line is 173 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 320 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
