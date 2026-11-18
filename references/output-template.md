# Output Template

Create files in the user-requested directory. If no directory is supplied, ask once or choose a clearly named folder under the current project and state the choice.

## Standard folder

```text
research-output/
├── README.md
├── 01-official-docs-and-dynamics.md
├── 02-public-architecture.md
├── 03-core-flow-research.md
├── 04-enterprise-capability-matrix.md
├── 05-current-project-mapping.md
├── 06-risks-and-open-questions.md
├── 07-action-plan.md
├── sources.md
├── diagrams/
│   ├── *.mmd
│   └── *.svg
└── evidence/
    ├── web/
    ├── source-code/
    └── local-run/
```

## README skeleton

```md
# <Target> Research

- Research date:
- Researcher/agent:
- Research goal:
- Target product/version:
- Local project/version:
- Evidence cutoff:

## Conclusion in one paragraph

## Key findings

1.
2.
3.

## Deliverables

| File | Purpose |
|---|---|

## Evidence boundary

- Official:
- Public inference:
- Third-party opinion:
- Not verified:

## How to reproduce local experiments

…
```

## Official docs and dynamics skeleton

```md
# Official Documentation and Product Dynamics

## Product definition

## Official timeline

| Date | Event | Evidence | Grade |
|---|---|---|---|

## Capability inventory

| Domain | Capability | Official evidence | Limitation |
|---|---|---|---|

## Terminology

| Term | Meaning | Source |
|---|---|---|
```

## Architecture report skeleton

```md
# Public Architecture

## Architecture basis

## Layered architecture

![Architecture](diagrams/…)

## Core flow

![Flow](diagrams/…)

## Component table

| Component | Responsibility | Evidence | Inference |
|---|---|---|---|

## Permissions and security

## State and authority

## Failure paths

## What is not known
```

## Capability matrix skeleton

```md
# Enterprise Capability Matrix

## Scoring definitions

| Score | Meaning |
|---:|---|

## Matrix

| Dimension | Target | Alternative | Local project | Evidence |
|---|---|---|---|---|

## Readiness gaps

## Build / buy / hybrid assessment
```

## Current-project mapping skeleton

```md
# Current Project Mapping

## Current architecture baseline

## Mapping

| Product mechanism | Current state | Borrow/adapt/reject | Reason | Priority |
|---|---|---|---|---|

## Minimum viable experiment

## Acceptance questions
```

## Risks skeleton

```md
# Risks and Open Questions

## Evidence risks

| Risk | Impact | Evidence needed | Resolution path |
|---|---|---|---|

## Technical risks

## Operational risks

## Compliance/security risks

## Unresolved questions
```

## Action plan skeleton

```md
# Action Plan

## P0: validate within days/weeks

| Action | Owner | Output | Acceptance |
|---|---|---|---|

## P1: validate next

## P2: strategic evaluation

## Explicitly not doing now
```

## Sources skeleton

```md
# Sources

Access date:

## Official

| Source | URL | Used for |
|---|---|---|

## Source code

| Repository | Commit/tag | Files | Used for |
|---|---|---|---|

## Secondary

| Source | URL | Reliability | Limit |
|---|---|---|---|
```

## Final quality checklist

Before claiming completion:

- [ ] research goal and scope are explicit;
- [ ] official / inferred / third-party facts are separated;
- [ ] timeline claims distinguish launch, update, and documentation dates;
- [ ] diagrams have evidence labels;
- [ ] all nontrivial claims cite evidence;
- [ ] capability scores have definitions;
- [ ] local mapping preserves authority and permission boundaries;
- [ ] risks and unverified questions are listed;
- [ ] action plan has outputs and acceptance criteria;
- [ ] local links resolve;
- [ ] JSON/YAML evidence files parse;
- [ ] no secrets or private data are exposed;
- [ ] no license-sensitive excerpts are redistributed.
