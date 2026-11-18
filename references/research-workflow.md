# Research Workflow

## 1. Establish the research contract

Answer these before broad collection:

| Question | Why it matters |
|---|---|
| What is the target: one product, several competitors, an architecture pattern, or a make/buy decision? | Determines comparison depth. |
| Who will read the output: engineer, architect, executive, procurement, or team lead? | Changes technical depth and action framing. |
| What decision depends on this research? | Prevents unrelated feature inventory. |
| What is the user's current system and constraint? | Enables useful borrowing rather than generic analysis. |
| Are there mandatory evaluation dimensions? | Security, privacy, deployment, cost, integration, and license can dominate. |
| What is the deadline/output format? | Chooses a brief, deep-dive, or full research folder. |

State assumptions explicitly if the user does not answer.

## 2. Source passes

### Pass A — product identity

Collect:

- product definition;
- target users;
- core scenarios;
- product boundaries;
- deployment model;
- commercial model;
- platform/ecosystem relationships;
- official architecture pages;
- release timeline.

### Pass B — capabilities and dynamics

Collect from official product updates:

- launch date;
- monthly or quarterly feature changes;
- semantic layer, agent, governance, integration, and security additions;
- deprecations and limits;
- pricing changes;
- regional/private deployment availability.

Do not infer first availability from a documentation update time. Documentation dates prove updates, not initial release.

### Pass C — architecture evidence

Prioritize:

1. official architecture diagrams;
2. official product overviews;
3. API references;
4. official demos and talks;
5. first-party open-source code;
6. vendor engineering blogs;
7. reputable third-party analyses.

For each architecture node, record whether it is officially named, directly described, or inferred.

### Pass D — comparable open-source systems

Choose references by mechanism, not popularity:

| Need | Reference type |
|---|---|
| Semantic model / metrics / API | Cube, dbt semantic layer |
| NL → semantic SQL → physical SQL | SuperSonic |
| Ontology / graph / evidence | Semantica, Helix Foundry |
| Agent orchestration | LangGraph, Google ADK, DSH |
| Workflow / data integration | Airbyte, Dagster, Temporal |

Say exactly what each reference explains. Do not claim target-product adoption.

### Pass E — local project evidence

When mapping to a user codebase:

- identify authoritative state stores;
- entry points and permission boundaries;
- domain model;
- workflow states;
- external integrations;
- current docs and tests;
- known operational constraints.

Prefer the codebase knowledge graph when available; fall back to targeted grep only for strings, configs, and non-code files.

## 3. Core questions

A strong enterprise-product study answers:

1. What problem does the product solve?
2. Which roles use it?
3. What are the non-negotiable platform capabilities?
4. How is the architecture layered?
5. Where is business meaning modeled?
6. How are agents or automations bounded?
7. How are permissions, audit, and safety enforced?
8. How does data flow from source to result?
9. What is human-in-the-loop?
10. What fails closed?
11. What enterprise gaps remain?
12. What can the user's project borrow, adapt, or reject?

## 4. Depth modes

### Brief

Use when the user asks a question, not a research project.

Output:

- answer;
- evidence grades;
- key official sources;
- caveats;
- optional next research step.

No large folder unless requested.

### Standard research folder

Use for a one-product architecture study. Produce the output contract in `SKILL.md`.

### Comparative evaluation

For each product, keep the same capability dimensions and scoring definitions. Add:

- comparison table;
- scenario fit;
- total cost and integration assumptions;
- build / buy / hybrid recommendation.

### Due diligence

Add procurement-oriented checks:

- vendor claims and verifiable evidence;
- deployment and operational prerequisites;
- identity system integration;
- data residency and compliance;
- support, SLA, upgrade, and exit strategy;
- security review requirements;
- missing public evidence.

## 5. Stop conditions

Stop and report uncertainty when:

- official evidence is unavailable for a key claim;
- a source conflicts with another;
- product naming or regional versions differ materially;
- a capability requires protected access, paid trial, or customer data;
- evaluating the product would require unauthorized or costly access.

Deliver what is known and list the exact evidence needed next.
