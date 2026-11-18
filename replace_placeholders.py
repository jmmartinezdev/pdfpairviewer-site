#!/usr/bin/env python3
"""Replace website placeholders with the supplied developer and support details."""

import argparse
import html
from pathlib import Path
import re


def nonempty(value):
    value = value.strip()
    if not value:
        raise argparse.ArgumentTypeError("must not be empty")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--legal-name", required=True, type=nonempty)
    parser.add_argument("--support-email", required=True, type=nonempty)
    args = parser.parse_args()

    script = Path(__file__).resolve()
    root = script.parent
    replacements = {
        "DEVELOPER_LEGAL_NAME_HERE": args.legal_name,
        "SUPPORT_EMAIL_HERE": args.support_email,
    }
    pattern = re.compile("|".join(map(re.escape, replacements)))
    changed = 0

    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if (
            path.is_symlink()
            or any(part.startswith(".") for part in relative.parts)
            or "__pycache__" in relative.parts
            or not path.is_file()
            or path.resolve() == script
        ):
            continue
        try:
            contents = path.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            continue
        if "\0" in contents:
            continue

        values = replacements
        if path.suffix.lower() in {".html", ".htm"}:
            values = {key: html.escape(value, quote=True) for key, value in values.items()}
        updated, count = pattern.subn(lambda match: values[match.group()], contents)
        if count:
            path.write_bytes(updated.encode("utf-8"))
            print(f"Updated {relative} ({count} replacements)")
            changed += 1

    print(f"Done. Updated {changed} file(s).")


if __name__ == "__main__":
    main()
