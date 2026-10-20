#!/usr/bin/env python3
"""Validate the public repository and installable skill package."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
NAME_RE = re.compile(r"^name:\s*business-idea-assessment\s*$", re.MULTILINE)
DESCRIPTION_RE = re.compile(r"^description:\s*(.+)$", re.MULTILINE)


def validate(repo: Path) -> list[str]:
    repo = repo.resolve()
    errors: list[str] = []
    skill = repo / "skills" / "business-idea-assessment"
    required = [
        repo / "README.md",
        repo / "LICENSE",
        repo / "CONTRIBUTING.md",
        repo / "SECURITY.md",
        repo / "CHANGELOG.md",
        skill / "SKILL.md",
        skill / "agents" / "openai.yaml",
        skill / "scripts" / "validate_assessment.py",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(repo)}")

    if not (skill / "SKILL.md").is_file():
        return errors

    skill_text = (skill / "SKILL.md").read_text(encoding="utf-8")
    if not skill_text.startswith("---\n") or "\n---\n" not in skill_text[4:]:
        errors.append("SKILL.md has invalid YAML frontmatter delimiters")
    if not NAME_RE.search(skill_text):
        errors.append("SKILL.md name is missing or invalid")
    description = DESCRIPTION_RE.search(skill_text)
    if not description or len(description.group(1).strip()) < 40:
        errors.append("SKILL.md description is missing or too short")

    for reference in sorted((skill / "references").glob("*.md")):
        relative = reference.relative_to(skill).as_posix()
        if f"({relative})" not in skill_text:
            errors.append(f"reference is not routed from SKILL.md: {relative}")

    agent_file = skill / "agents" / "openai.yaml"
    if agent_file.is_file():
        agent_text = agent_file.read_text(encoding="utf-8")
        if "$business-idea-assessment" not in agent_text:
            errors.append("openai.yaml default_prompt does not name the skill")
        if "allow_implicit_invocation: true" not in agent_text:
            errors.append("openai.yaml implicit invocation policy is missing")

    readme_file = repo / "README.md"
    if readme_file.is_file():
        readme_text = readme_file.read_text(encoding="utf-8")
        install_markers = {
            "Codex": "$business-idea-assessment",
            "Claude Code": "$HOME/.claude/skills",
            "OpenCode": "$HOME/.agents/skills",
            "Pi": "/skill:business-idea-assessment",
            "generic Agent Skills fallback": "Any other agent",
        }
        for label, marker in install_markers.items():
            if marker not in readme_text:
                errors.append(f"README install guidance missing: {label}")

    for path in repo.rglob("*.md"):
        body = path.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(body):
            target = raw_target.strip().strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = unquote(target.split("#", 1)[0])
            if target and not (path.parent / target).resolve().exists():
                errors.append(f"broken local link: {path.relative_to(repo)} -> {target}")

    for path in repo.rglob("*.py"):
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as exc:
            errors.append(f"Python syntax error: {path.relative_to(repo)}:{exc.lineno}: {exc.msg}")

    unfinished = "TO" + "DO"
    repair_marker = "FIX" + "ME"
    placeholder = re.compile(rf"\[{unfinished}|\b{unfinished}\b|\b{repair_marker}\b")
    for path in repo.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".py"}:
            continue
        if placeholder.search(path.read_text(encoding="utf-8")):
            errors.append(f"unfinished placeholder: {path.relative_to(repo)}")

    license_file = repo / "LICENSE"
    if license_file.is_file() and "MIT License" not in license_file.read_text(encoding="utf-8"):
        errors.append("LICENSE is not the declared MIT License")
    return errors


def main() -> int:
    default_repo = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", nargs="?", type=Path, default=default_repo)
    args = parser.parse_args()
    errors = validate(args.repository)
    if errors:
        print(f"FAIL: {len(errors)} error(s)")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: repository and skill structure validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())

