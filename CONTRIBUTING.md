# Contributing

Thanks for improving Enterprise Project Research.

## Before opening a change

- Search existing issues and pull requests.
- Keep changes focused on research quality, evidence discipline, usability, or validation.
- Do not add vendor facts that are not supported by a source.
- Do not upload scraped manuals, customer material, private screenshots, or long copyrighted excerpts.
- Do not add real credentials, personal data, internal hostnames, or local absolute paths.

## What makes a good contribution

Changes are most useful when they:

- improve a decision the Skill can make or a failure it can prevent;
- add a concrete, reusable template rather than generic advice;
- clarify evidence grades, inference boundaries, or enterprise readiness;
- improve validation without adding fragile dependencies;
- preserve the user's authority, permissions, and project-specific constraints.

Avoid broad new mandates that do not change behaviour. The Skill should remain adaptable across product, architecture, procurement, and build-versus-buy studies.

## Pull requests

1. Fork the repository and create a focused branch.
2. Update relevant references instead of duplicating guidance across files.
3. Add or adapt an example only when it materially clarifies usage.
4. Run:

   ```bash
   python3 -m pip install pyyaml
   python3 scripts/validate_package.py
   ```

5. Describe what changed, why it matters, and any new evidence or assumptions.
6. Confirm that the change contains no confidential or licence-restricted material.

## Evidence and citation expectations

When proposing a factual statement about a product:

- link the official source where possible;
- state the access date;
- distinguish official documentation, public inference, and third-party opinion;
- record repository commits when discussing source code;
- avoid claiming that an open-source reference is used internally by a closed-source product unless official evidence supports it.

## Conduct

Participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
