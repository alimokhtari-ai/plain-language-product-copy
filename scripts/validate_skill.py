#!/usr/bin/env python3
"""Validate the minimum structure and frontmatter of this Agent Skill."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(f"Validation failed: {message}")


def main() -> None:
    if len(sys.argv) != 3:
        fail("usage: validate_skill.py <skill-directory> <output-zip>")

    root = Path(sys.argv[1])
    output = Path(sys.argv[2])
    if not root.is_dir():
        fail(f"skill directory not found: {root}")

    skill_md = root / "SKILL.md"
    agent_yaml = root / "agents" / "openai.yaml"
    if not skill_md.is_file() or not agent_yaml.is_file():
        fail("SKILL.md and agents/openai.yaml are required")

    content = skill_md.read_text(encoding="utf-8")
    frontmatter = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not frontmatter:
        fail("SKILL.md must begin with YAML frontmatter")

    fields = dict(
        re.findall(r"^([a-z_]+):\s*(.+)$", frontmatter.group(1), re.MULTILINE)
    )
    if fields.get("name") != root.name:
        fail("frontmatter name must match the skill directory")
    if not fields.get("description"):
        fail("frontmatter description is required")
    if len(content.splitlines()) > 500:
        fail("SKILL.md exceeds the 500-line control-plane guideline")

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for file_path in sorted(root.rglob("*")):
            if file_path.is_file():
                archive.write(file_path, file_path.relative_to(root.parent))

    print(f"Validated and packaged: {output}")


if __name__ == "__main__":
    main()
