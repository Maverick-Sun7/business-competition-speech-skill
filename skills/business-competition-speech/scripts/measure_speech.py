#!/usr/bin/env python3
"""Count submitted speech text and check length/reduction/timing limits.

Read-only, standard-library helper. Timing is an estimate for English only.
"""

import argparse
import json
import math
from pathlib import Path
import re
import sys
import unicodedata


# Apostrophes and hyphens inside tokens do not create additional words.
# A comma or period between digits is retained within a number token.
ENGLISH_TOKEN = re.compile(
    r"[A-Za-z0-9]+(?:['’\-‐‑][A-Za-z0-9]+|(?<=[0-9])[,.](?=[0-9])[0-9]+)*"
)
CONVENTIONS = {
    "english": (
        "One token of ASCII Latin letters/digits is one word; internal apostrophes "
        "or hyphens keep a token together (don't, two-hour, 96-square-meter). "
        "Commas/periods between digits keep a number together (1,050, 22.5). "
        "Other punctuation separates tokens; CJK and other non-ASCII letters "
        "are not counted. No spoken expansion of numbers is inferred."
    ),
    "chinese": (
        "One Unicode code point that is neither whitespace nor punctuation "
        "(Unicode category P*) is one character. Latin letters, digits, and "
        "symbols count individually too; this is a whole-text character count, "
        "not a count restricted to Han characters."
    ),
    "mixed": (
        "One English token under the English convention plus each Han/CJK "
        "ideograph is one unit. CJK punctuation is excluded. Other scripts and "
        "symbols are excluded. This combined unit count is not English words "
        "and does not provide a speaking-time estimate."
    ),
}


def is_han(character):
    code = ord(character)
    return (
        code == 0x3007
        or 0x3400 <= code <= 0x4DBF
        or 0x4E00 <= code <= 0x9FFF
        or 0xF900 <= code <= 0xFAFF
        or 0x20000 <= code <= 0x2EE5F
        or 0x2F800 <= code <= 0x2FA1F
        or 0x30000 <= code <= 0x323AF
    )


def count_text(text, mode):
    english = len(ENGLISH_TOKEN.findall(text))
    han = sum(is_han(character) for character in text)
    characters = sum(
        not character.isspace()
        and not unicodedata.category(character).startswith("P")
        for character in text
    )
    units = {
        "english": english,
        "chinese": characters,
        "mixed": english + han,
    }[mode]
    return {
        "units": units,
        "english_words": english,
        "cjk_characters": han,
        "nonspace_nonpunctuation_characters": characters,
    }


def nonnegative_integer(value):
    try:
        parsed = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a nonnegative integer") from exc
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be a nonnegative integer")
    return parsed


def nonnegative_float(value):
    try:
        parsed = float(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("must be a finite nonnegative number") from exc
    if not math.isfinite(parsed) or parsed < 0:
        raise argparse.ArgumentTypeError("must be a finite nonnegative number")
    return parsed


def positive_float(value):
    parsed = nonnegative_float(value)
    if parsed == 0:
        raise argparse.ArgumentTypeError("must be greater than zero")
    return parsed


def build_parser():
    parser = argparse.ArgumentParser(
        description=(
            "Read UTF-8 plain spoken text and output JSON counts/checks. "
            "Input files are never modified. Exit 0: checks pass; "
            "1: a requested limit fails; 2: invalid input or unreadable file."
        ),
        epilog=(
            "English counts submitted ASCII Latin/digit tokens, keeping internal "
            "apostrophes/hyphens and numeric commas/periods together. Chinese "
            "counts all nonspace/nonpunctuation code points. Mixed counts English "
            "tokens plus Han/CJK ideographs. Numbers must be written as intended "
            "to speak; no number expansion is guessed. Supply spoken text only "
            "(omit headings, stage directions, notes, and coverage tables). "
            "Timing is estimated, never measured."
        ),
    )
    parser.add_argument("file", nargs="?", type=Path, help="current/after speech file")
    parser.add_argument("--after", type=Path, help="alternative to the positional file")
    parser.add_argument("--before", type=Path, help="original speech for reduction comparison")
    parser.add_argument("--mode", choices=CONVENTIONS, default="english")
    parser.add_argument(
        "--min-reduction", type=nonnegative_integer,
        help="required decrease in mode units; requires --before",
    )
    length = parser.add_mutually_exclusive_group()
    length.add_argument(
        "--max-words", type=nonnegative_integer,
        help="maximum current words (English), characters (Chinese), or units (mixed)",
    )
    length.add_argument(
        "--exact-words", type=nonnegative_integer,
        help="exact current words/characters/units under the selected mode",
    )
    parser.add_argument(
        "--minutes", type=nonnegative_float,
        help="maximum estimated English delivery minutes, including supplied pauses",
    )
    parser.add_argument(
        "--wpm", type=positive_float,
        help="assumed English speaking words/minute (default: 120); English mode only",
    )
    parser.add_argument(
        "--pause-seconds", type=nonnegative_float,
        help="total assumed pause seconds (default: 0); English mode only",
    )
    return parser


def read_counts(path, mode):
    # Accept a UTF-8 BOM without adding it to Chinese character counts.
    text = path.read_text(encoding="utf-8-sig")
    return {"file": str(path.resolve()), **count_text(text, mode)}


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if (args.file is None) == (args.after is None):
        parser.error("provide exactly one positional file or --after FILE")
    if args.min_reduction is not None and args.before is None:
        parser.error("--min-reduction requires --before")
    if args.mode != "english" and any(
        value is not None for value in (args.minutes, args.wpm, args.pause_seconds)
    ):
        parser.error("--minutes, --wpm, and --pause-seconds require --mode english")

    try:
        current = read_counts(args.file or args.after, args.mode)
        before = read_counts(args.before, args.mode) if args.before else None
    except (OSError, UnicodeError) as exc:
        print(json.dumps({"passed": False, "error": str(exc)}, ensure_ascii=False))
        return 2

    reduction = before["units"] - current["units"] if before else None
    checks = []
    if args.max_words is not None:
        checks.append({
            "name": "max_words", "passed": current["units"] <= args.max_words,
            "actual": current["units"], "required_max": args.max_words,
        })
    if args.exact_words is not None:
        checks.append({
            "name": "exact_words", "passed": current["units"] == args.exact_words,
            "actual": current["units"], "required_exact": args.exact_words,
        })
    if args.min_reduction is not None:
        checks.append({
            "name": "min_reduction", "passed": reduction >= args.min_reduction,
            "actual": reduction, "required_min": args.min_reduction,
        })

    timing = None
    if args.mode == "english":
        wpm = args.wpm if args.wpm is not None else 120.0
        pauses = args.pause_seconds if args.pause_seconds is not None else 0.0
        seconds = current["english_words"] * 60.0 / wpm + pauses
        timing = {
            "type": "estimate_not_measured",
            "words_per_minute": wpm,
            "pause_seconds": pauses,
            "estimated_seconds": round(seconds, 6),
            "estimated_minutes": round(seconds / 60.0, 6),
            "maximum_minutes": args.minutes,
        }
        if args.minutes is not None:
            checks.append({
                "name": "minutes", "passed": seconds <= args.minutes * 60.0,
                "actual_seconds": round(seconds, 6),
                "required_max_seconds": args.minutes * 60.0,
            })

    notes = [
        "Counts describe submitted text, not inferred spoken number expansion. "
        "Write numbers as intended to speak when checking delivered word count.",
        "Include only spoken text. Headings and notes are counted if present.",
        "Reduction is before units minus current units; negative means the text grew.",
    ]
    if timing is not None:
        notes.append(
            "Delivery time is estimated from the stated WPM and supplied pauses, "
            "not measured. Rehearsal is needed to confirm actual timing."
        )
        if current["cjk_characters"] or (before and before["cjk_characters"]):
            notes.append("English mode ignores CJK characters; use Chinese or mixed mode if needed.")
    passed = all(check["passed"] for check in checks)
    output = {
        "mode": args.mode,
        "unit": {"english": "words", "chinese": "characters", "mixed": "mixed_units"}[args.mode],
        "counting_convention": CONVENTIONS[args.mode],
        "current": current,
        "before": before,
        "reduction": reduction,
        "timing": timing,
        "checks": checks,
        "passed": passed,
        "notes": notes,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2, allow_nan=False))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
