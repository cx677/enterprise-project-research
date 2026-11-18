# Enterprise Product Research Brief

Use this template when the research must support a concrete architecture, procurement, or build-versus-buy decision.

## Request template

```text
Use $enterprise-project-research to research <target product or platform>.

Decision:
<What decision should this research support?>

Audience:
<Engineering, architecture, product, procurement, or leadership>

Comparison set:
<Alternative products or open-source reference systems>

Current project:
<Repository or system context; list only material constraints>

Required dimensions:
- product scope and target users
- public architecture and core workflows
- semantic/domain model and state authority
- permissions, security, audit, and human confirmation
- deployment, integration, observability, and operating cost
- maturity gaps and public-evidence limits

Required mapping:
- mechanisms to borrow directly
- mechanisms to adapt
- mechanisms not to copy
- P0/P1/P2 actions with acceptance criteria

Output:
<Brief answer or standard research folder>

Evidence cutoff:
<Date or version>
```

## Acceptance questions

The completed research should let the reader answer:

1. What exactly is known from official evidence?
2. Which architecture claims are public inference?
3. Which conclusions depend on third-party opinion or remain unverified?
4. How does the product handle authority, permissions, and failure?
5. What enterprise gaps would require a trial, vendor confirmation, or procurement review?
6. Which mechanisms fit the current project, and which would add risk or duplicate authority?
7. What is the smallest experiment that can validate the recommendation?

## Synthetic example

```text
Use $enterprise-project-research to compare three enterprise data-agent platforms
for a private-deployment procurement decision. Focus on permission scoping,
audit export, semantic-model governance, connector integration, and operating
cost. Mark every architecture claim by evidence grade. Produce a capability
matrix, a public architecture reconstruction, and a P0/P1/P2 mapping to the
current repository. End with the minimum proof of concept needed before a
purchase recommendation.
```

Do not treat the synthetic example as a vendor assessment. It is only a prompt shape.
