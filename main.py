#!/usr/bin/env python3
"""The One-Line Laugh (make.fun bounty u-ronigrv-the-one-line-laugh-7ccca46f).

Writes one funny line to /output/entry.txt and prints it to stdout.
Standard library only; no arguments; deterministic.
"""

import os

LINE = "My smartwatch praised me for burning 500 calories, then tattled that the pizza I just ordered has 900."


def main():
    # The brief: one funny line, a single sentence of at most 200 chars.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.count(".") == 1 and LINE.endswith("."), "line must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
