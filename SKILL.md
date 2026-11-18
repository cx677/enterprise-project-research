---
name: enterprise-project-research
description: Use when researching, comparing, or evaluating enterprise software platforms, closed-source products, data/AI agents, BI systems, semantic layers, or vendor architectures—especially when the deliverable needs evidence grading, architecture reconstruction, capability matrices, open-source comparisons, or mapping to the user's own project. Not for a simple documentation lookup or a single open-source code read without product/architecture analysis.
---

# Enterprise Project Research

Research an enterprise product or platform as an evidence-based engineering investigation, not as a brochure summary. The default outcome is a reusable research folder containing: source inventory, timeline, architecture diagrams, core workflows, capability matrix, risks, project-specific borrowing points, action plan, and evidence archive.

## Required Approach

1. **Clarify the research contract** before collecting more material:
   - target product(s), comparison alternatives, and the user's own system;
   - purpose: architecture study, purchase evaluation, build-vs-buy, competitor analysis, or design borrowing;
   - required output directory and depth.
2. **Collect sources by precedence:** official docs, product updates, API references, release notes, official talks, first-party source code when available, then reputable secondary sources. Use web-search/firecrawl tools when available and allowed.
3. **Grade every material conclusion** as `official`, `public inference`, or `third-party opinion`. Never present a third-party architecture article as the vendor's internal implementation.
4. **Reconstruct architecture from evidence.** Draw layers, components, data/control flow, agents/workflows, permission boundaries, and failure paths. Mark uncertain parts as inferred.
5. **Use open-source references deliberately** (for example Cube, SuperSonic, Helix Foundry, Semantica) to understand mechanisms; do not claim the target product uses them unless officially stated.
6. **Evaluate enterprise readiness:** capabilities, governance, security, integration, deployment, observability, cost, operability, extensibility, and risks.
7. **Map findings to the user's project.** Separate borrow directly, adapt, and do not copy. Preserve the current project's authority boundaries and permission model.
8. **Make the work reproducible:** record URLs, access dates, repository commits, local evidence files, reproduction commands, and unresolved questions.

## Output Contract

Unless the user asks for a shorter answer, create a research output folder with:

```text
README.md
01-official-docs-and-dynamics.md
02-public-architecture.md
03-core-flow-research.md       # product-specific or open-source-reference flow
04-enterprise-capability-matrix.md
05-current-project-mapping.md
06-risks-and-open-questions.md
07-action-plan.md
sources.md
diagrams/
evidence/
```

Adapt numbering and file names to the request, but preserve evidence grading, diagrams, matrix, mapping, risks, actions, and sources.

## Progressive References

Read only what the current task needs:

- [references/research-workflow.md](references/research-workflow.md) — full investigation workflow and scoping questions.
- [references/evidence-standards.md](references/evidence-standards.md) — source hierarchy, evidence grades, citation and closed-source boundaries.
- [references/architecture-reconstruction.md](references/architecture-reconstruction.md) — architecture and workflow diagrams with inference labels.
- [references/capability-matrix.md](references/capability-matrix.md) — enterprise evaluation dimensions and scoring rules.
- [references/output-template.md](references/output-template.md) — exact report skeletons and quality checklist.

## Hard Boundaries

- Do not invent vendor internals, launch dates, dependencies, or roadmap facts.
- Do not equate “a project existed” with “the target product used it”.
- Do not turn a public demo into an enterprise-readiness conclusion.
- Do not recommend adoption without stating assumptions, missing evidence, integration effort, and operating costs.
- Do not expose secrets, private customer data, local absolute paths in user-facing deliverables, or license-restricted excerpts.
