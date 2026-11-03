#!/usr/bin/env python3

import argparse
import random
import re
import string

BASE_WORD = "Something"

DEFAULT_SYMBOLS = list("!@#$%^&*")
DEFAULT_WORDS = [
    "Alpha","Beta","Gamma","Delta","Omega",
    "Prime","Secure","Vault","Core","Edge",
    "Zone","Matrix","Logic","Nova","Pulse"
]

def generate_word(include_numbers, include_symbols, symbols):
    word = BASE_WORD

    # optional extra word
    if random.random() > 0.6:
        word += random.choice(DEFAULT_WORDS)

    if include_symbols:
        word += random.choice(symbols)

    if include_numbers:
        word += str(random.randint(0,9999))

    if include_symbols and random.random() > 0.7:
        word += random.choice(symbols)

    return word


def main():
    parser = argparse.ArgumentParser(description="Wordlist Generator")

    parser.add_argument(
        "-n", "--number",
        type=int,
        default=6000,
        help="Number of passwords to generate (default: 6000)"
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default="wordlist.txt",
        help="Output file"
    )

    parser.add_argument(
        "--include-numbers",
        action="store_true",
        help="Include numbers"
    )

    parser.add_argument(
        "--include-symbols",
        action="store_true",
        help="Include special characters"
    )

    parser.add_argument(
        "--symbols",
        type=str,
        default="!@#$%^&*",
        help="Custom special characters"
    )

    parser.add_argument(
        "--regex",
        type=str,
        help="Regex pattern words must match"
    )

    args = parser.parse_args()

    symbols = list(args.symbols)
    results = set()

    regex = re.compile(args.regex) if args.regex else None

    while len(results) < args.number:
        word = generate_word(args.include_numbers, args.include_symbols, symbols)

        if regex:
            if not regex.search(word):
                continue

        results.add(word)

    with open(args.output, "w") as f:
        for r in results:
            f.write(r + "\n")

    print(f"[+] Generated {len(results)} words")
    print(f"[+] Saved to {args.output}")


if __name__ == "__main__":
    main()
