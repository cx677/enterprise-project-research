# Enterprise Capability Matrix

## Scoring scale

Use a 0–5 scale and define what each score means. Suggested:

| Score | Meaning |
|---:|---|
| 0 | No public evidence |
| 1 | Concept or roadmap only |
| 2 | Demo/basic capability |
| 3 | Team usable |
| 4 | Enterprise-ready by public evidence |
| 5 | Complete enterprise capability, still requiring PoC validation |

Always state: “No public evidence” does not mean the product lacks the capability.

## Core dimensions

| Dimension | Evaluate |
|---|---|
| Product fit | problem, users, scenarios, boundaries |
| Data / state | sources, storage, model, lineage, authority |
| Semantics | models, metrics, dimensions, ontology, versioning |
| Agent / automation | planning, tools, HITL, retries, task state |
| Query / workflow | correctness, controls, determinism, failure paths |
| Permissions | identity, workspace, asset ACL, row/column scope, delegation |
| Security | prompt/tool risk, data protection, SQL/action guard, isolation |
| Audit | trace, inputs, steps, outputs, feedback, export |
| Governance | owner, review, publish, rollback, quality |
| Integration | API, MCP/connector, BI, identity, storage, ecosystem |
| Deployment | SaaS, private, hybrid, tenancy, upgrade, DR |
| Observability | logs, metrics, query history, cost, troubleshooting |
| Operability | admin workflow, support, policy control, migration |
| Cost | license, compute, storage, model, maintenance, migration |
| extensibility | plugins, custom semantics, SDKs, source availability |

Adapt dimensions to the domain. Do not force all rows when irrelevant.

## Comparison matrix

For multi-product evaluation, use identical rows and scoring definitions:

```text
| Dimension | Product A | Product B | Open-source reference | User system | Evidence / gap |
```

Add a short conclusion under the table. Numeric scores alone are not a decision.

## Enterprise readiness gates

A capability should not be called production-ready based only on marketing when any of the following is missing:

- identity and permission integration;
- audit export;
- failure and retry behavior;
- data residency or privacy controls;
- versioning and rollback;
- support/SLA or operational runbook;
- upgrade and migration path;
- performance or scale evidence;
- security review.

## Build / buy / hybrid analysis

Evaluate:

| Option | Fit when | Main risks |
|---|---|---|
| Buy | Time-to-market and vendor capability outweigh control | Lock-in, integration, cost, compliance |
| Build | Domain model and workflow are differentiating | Governance, maintenance, hidden platform work |
| Hybrid | Stable commodity platform + custom domain logic | Split authority, duplicated state, audit complexity |

Always state assumptions and the minimum PoC needed to validate the recommendation.

## Project mapping matrix

Map each studied mechanism to the local system:

```text
| Product mechanism | Local current state | Borrow directly | Adapt | Do not copy | Reason | Priority |
```

Priority definitions:

- **P0**: small change, high certainty, directly reduces ambiguity or risk.
- **P1**: valuable after P0, needs schema/design or owner approval.
- **P2**: strategic or platform-level; evaluate after P0/P1 evidence.

Preserve local invariants such as authoritative state stores, confirmation gates, and least-privilege boundaries.
