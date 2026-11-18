# Evidence Standards

## Source hierarchy

Rank evidence from strongest to weakest:

1. official technical documentation;
2. official API references and schemas;
3. official product-update logs;
4. official architecture diagrams;
5. first-party source code and releases;
6. official engineering talks or whitepapers;
7. vendor-controlled demos and tutorials;
8. reputable news or analyst articles;
9. community blog analysis;
10. social posts and forum answers.

A lower-ranked source can provide a useful hypothesis, but not a final architectural fact.

## Evidence grades

Use these exact labels in reports:

| Label | Meaning | Use |
|---|---|---|
| **Official** | Vendor or project directly states the fact | Can support architecture, timeline, and capability claims |
| **Public inference** | Derived from public docs, diagrams, code, or observable behavior | Must say what evidence supports the inference |
| **Third-party opinion** | Author interpretation, not vendor statement | Can inform comparison; cannot represent vendor internals |
| **Unverified** | Needs trial, internal access, or vendor confirmation | Keep in open questions |

For diagrams, label the entire diagram and any inferred nodes/edges.

## Citation rules

For every nontrivial claim, record:

```text
claim
source URL or local evidence path
access date
evidence grade
exact qualification, if any
```

For source code, record:

```text
repository
commit / tag / release
file path
relevant function or component
```

For a local experiment, record:

```text
command
runtime/version
input
output evidence path
date
```

Never cite only the vendor marketing page for an enterprise-readiness conclusion.

## Timeline discipline

- Distinguish product launch, feature listing, documentation update, and actual availability.
- Do not infer feature launch from the date an article was written.
- Do not infer internal implementation from an architecture concept drawing.
- Product dynamic dates show public cataloging; note this limitation unless the vendor explicitly calls the date first release.

## Dependency discipline

These statements are not equivalent:

```text
A product mentions project X.
A product recommends project X.
A product uses project X.
A product is built on project X.
```

Only official dependency statements, license notices, manifests, or source evidence can support the stronger claims.

## Closed-source boundary

For a closed-source enterprise product:

- reconstruct only from public evidence and observed behavior;
- label architecture as “public reconstruction”, not internal implementation;
- avoid naming internal services that are not publicly documented;
- separate required platform capabilities from likely implementation choices;
- state which experiment or vendor confirmation would resolve uncertainty.

## Source conflicts

When sources conflict:

1. present each source and date;
2. compare scope, region, product version, and terminology;
3. prefer official and newer evidence;
4. keep a residual uncertainty;
5. do not silently choose the convenient source.

## Evidence archive

Keep local snapshots or extracted excerpts when allowed:

```text
evidence/
  web/
  source-code/
  local-run/
```

Record licensing restrictions. Do not archive private credentials, customer data, cookies, or excessive copyrighted content.
