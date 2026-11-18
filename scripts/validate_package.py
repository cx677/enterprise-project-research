#!/usr/bin/env python3
"""Validate the publishable Skill package with the Python standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

try:
    import yaml
except ImportError:
    print(
        "Validation requires PyYAML. Run: python3 -m pip install pyyaml",
        file=sys.stderr,
    )
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    ".gitignore",
    ".gitattributes",
    "SKILL.md",
    "agents/openai.yaml",
    "examples/enterprise-product-research-brief.md",
    ".github/workflows/validate.yml",
]

EXPECTED_REFERENCES = [
    "references/research-workflow.md",
    "references/evidence-standards.md",
    "references/architecture-reconstruction.md",
    "references/capability-matrix.md",
    "references/output-template.md",
]

MARKDOWN_FILES = [
    path for path in ROOT.rglob("*.md") if ".git" not in path.parts
]

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{path.relative_to(ROOT)} has no valid YAML frontmatter block")
        return {}

    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as error:
        fail(f"{path.relative_to(ROOT)} has invalid YAML frontmatter: {error}")
        return {}

    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)} frontmatter must be a YAML mapping")
        return {}

    return {str(key): str(value) for key, value in data.items()}


def check_yaml_file(relative: str) -> None:
    path = ROOT / relative
    if not path.is_file():
        return
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as error:
        fail(f"{relative} has invalid YAML: {error}")
        return
    if not isinstance(data, dict):
        fail(f"{relative} must contain a YAML mapping")


def strip_code_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def check_local_links(path: Path, text: str) -> None:
    without_fences = strip_code_fences(text)
    for raw_target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", without_fences):
        target = raw_target.strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        target = target.split("#", 1)[0]
        if not target or target.startswith("#"):
            continue
        parsed = urlparse(target)
        if parsed.scheme or target.startswith("//"):
            continue
        resolved = (path.parent / unquote(target)).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            fail(
                f"{path.relative_to(ROOT)} links outside the repository: {raw_target}"
            )
            continue
        if not resolved.exists():
            fail(f"{path.relative_to(ROOT)} has a broken local link: {raw_target}")


def main() -> int:
    for relative in REQUIRED_FILES + EXPECTED_REFERENCES:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill_text = skill_path.read_text(encoding="utf-8")
        metadata = parse_frontmatter(skill_text, skill_path)
        if metadata.get("name") != ROOT.name:
            fail(
                f"SKILL.md name must match folder name {ROOT.name!r}; "
                f"found {metadata.get('name')!r}"
            )
        description = metadata.get("description", "")
        if len(description) < 80:
            fail("SKILL.md description is missing or too short to route reliably")
        if "\n# Enterprise Project Research" not in skill_text:
            fail("SKILL.md is missing its main heading")

    ui_path = ROOT / "agents/openai.yaml"
    if ui_path.is_file():
        ui_text = ui_path.read_text(encoding="utf-8")
        for required in (
            "display_name:",
            "short_description:",
            "default_prompt:",
            "allow_implicit_invocation: true",
        ):
            if required not in ui_text:
                fail(f"agents/openai.yaml is missing {required!r}")

    for relative in ("agents/openai.yaml", ".github/workflows/validate.yml"):
        check_yaml_file(relative)

    for path in MARKDOWN_FILES:
        text = path.read_text(encoding="utf-8")
        check_local_links(path, text)
        if "\x00" in text:
            fail(f"{path.relative_to(ROOT)} contains a NUL character")
        for placeholder in ("[TODO", "TODO:", "TBD"):
            if placeholder in text:
                fail(f"{path.relative_to(ROOT)} contains unfinished text: {placeholder}")
        if re.search(r"(?<![`\\w])/(?:Users|home)/[^\\s)`]+", text):
            fail(f"{path.relative_to(ROOT)} contains a local absolute path")

        for block in re.findall(r"```mermaid\n(.*?)```", text, re.DOTALL):
            if not block.strip():
                fail(f"{path.relative_to(ROOT)} contains an empty Mermaid block")

    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Skill package is valid: "
        f"{len(REQUIRED_FILES) + len(EXPECTED_REFERENCES)} required files, "
        f"{len(MARKDOWN_FILES)} Markdown files."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
