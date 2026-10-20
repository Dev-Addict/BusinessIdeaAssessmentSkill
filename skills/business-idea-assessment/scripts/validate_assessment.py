#!/usr/bin/env python3
"""Validate structural invariants of a Markdown/CSV assessment package."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_HEADERS = {
    "access_date",
    "observation_date",
    "research_date",
    "quote_date",
    "valid_until",
    "deadline_date",
    "start_date",
    "end_date",
    "target_date",
    "next_action_date",
}
DATE_EXCEPTIONS = {"", "NA", "not_applicable", "rolling", "ongoing", "TBD"}


def validate(root: Path) -> dict[str, object]:
    root = root.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not root.is_dir():
        return {"root": str(root), "files": 0, "errors": ["not a directory"], "warnings": []}

    files = sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and not any(part in {".git", "__pycache__"} for part in path.parts)
    )
    markdown = [path for path in files if path.suffix.lower() == ".md"]
    csv_files = [path for path in files if path.suffix.lower() == ".csv"]

    for path in files:
        if path.suffix.lower() not in {".md", ".csv"}:
            errors.append(f"unsupported file type: {path.relative_to(root)}")

    for path in csv_files:
        try:
            with path.open(newline="", encoding="utf-8-sig") as handle:
                rows = list(csv.reader(handle))
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"cannot parse CSV {path.relative_to(root)}: {exc}")
            continue

        if not rows:
            errors.append(f"empty CSV: {path.relative_to(root)}")
            continue
        header = rows[0]
        if not header or any(not cell.strip() for cell in header):
            errors.append(f"empty CSV header: {path.relative_to(root)}")
        if len(header) != len(set(header)):
            errors.append(f"duplicate CSV header: {path.relative_to(root)}")

        for line_number, row in enumerate(rows[1:], start=2):
            if not row or all(not cell.strip() for cell in row):
                errors.append(f"blank CSV record: {path.relative_to(root)}:{line_number}")
                continue
            if len(row) != len(header):
                errors.append(
                    f"CSV width mismatch: {path.relative_to(root)}:{line_number} "
                    f"has {len(row)} columns; expected {len(header)}"
                )

        try:
            with path.open(newline="", encoding="utf-8-sig") as handle:
                dict_rows = list(csv.DictReader(handle))
        except (OSError, UnicodeError, csv.Error):
            continue

        for line_number, row in enumerate(dict_rows, start=2):
            for column, value in row.items():
                if value is None:
                    continue
                stripped = value.strip()
                if column in DATE_HEADERS and stripped not in DATE_EXCEPTIONS:
                    if not ISO_DATE_RE.match(stripped):
                        errors.append(
                            f"non-ISO date: {path.relative_to(root)}:{line_number}:{column}={stripped}"
                        )
                    else:
                        try:
                            dt.date.fromisoformat(stripped)
                        except ValueError:
                            errors.append(
                                f"invalid date: {path.relative_to(root)}:{line_number}:{column}={stripped}"
                            )
                if column.endswith("_url") and "file_or_url" not in column:
                    if stripped not in DATE_EXCEPTIONS and not stripped.startswith(("https://", "http://")):
                        errors.append(
                            f"invalid source URL: {path.relative_to(root)}:{line_number}:{column}"
                        )

    for path in markdown:
        try:
            body = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read Markdown {path.relative_to(root)}: {exc}")
            continue
        for raw_target in LINK_RE.findall(body):
            target = raw_target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if target and not (path.parent / target).resolve().exists():
                errors.append(f"broken local link: {path.relative_to(root)} -> {target}")

    readme = root / "README.md"
    if not readme.is_file():
        errors.append("missing root README.md")
    else:
        body = readme.read_text(encoding="utf-8")
        targets = {
            unquote(target.strip().strip("<>").split("#", 1)[0])
            for target in LINK_RE.findall(body)
            if not target.startswith(("http://", "https://", "mailto:", "#"))
        }
        for path in markdown + csv_files:
            if path == readme:
                continue
            relative = path.relative_to(root).as_posix()
            if relative not in targets:
                errors.append(f"README does not link deliverable: {relative}")

    if not markdown:
        warnings.append("assessment contains no Markdown files")
    if not csv_files:
        warnings.append("assessment contains no CSV files")

    return {
        "root": str(root),
        "files": len(files),
        "markdown": len(markdown),
        "csv": len(csv_files),
        "errors": errors,
        "warnings": warnings,
    }


def self_test() -> int:
    with tempfile.TemporaryDirectory(prefix="assessment-validator-") as tmp:
        root = Path(tmp)
        (root / "data.csv").write_text(
            "record_id,access_date,source_url\nA1,2026-10-19,https://example.com/source\n",
            encoding="utf-8",
        )
        (root / "notes.md").write_text("# Notes\n", encoding="utf-8")
        (root / "README.md").write_text(
            "# Assessment\n\n- [Data](data.csv)\n- [Notes](notes.md)\n",
            encoding="utf-8",
        )
        valid = validate(root)
        if valid["errors"]:
            print(json.dumps(valid, indent=2))
            return 1

        (root / "data.csv").write_text(
            "record_id,access_date,source_url\nA1,19-10-2026,not-a-url\n\n",
            encoding="utf-8",
        )
        invalid = validate(root)
        if len(invalid["errors"]) < 3:
            print(json.dumps(invalid, indent=2))
            return 1
    print("SELF_TEST_PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("assessment_directory", nargs="?", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if args.assessment_directory is None:
        parser.error("assessment_directory is required unless --self-test is used")

    result = validate(args.assessment_directory)
    if args.as_json:
        print(json.dumps(result, indent=2))
    else:
        status = "PASS" if not result["errors"] else "FAIL"
        print(
            f"{status}: {result['files']} files "
            f"({result['markdown']} Markdown, {result['csv']} CSV); "
            f"{len(result['errors'])} errors; {len(result['warnings'])} warnings"
        )
        for message in result["errors"]:
            print(f"ERROR: {message}")
        for message in result["warnings"]:
            print(f"WARNING: {message}")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())

