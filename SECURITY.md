# Security Policy

## Supported versions

Security fixes are applied to the latest release on the default branch.

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability.

After this repository is published on GitHub, use **Security → Report a vulnerability** to send a private report. Include:

- the affected file or workflow;
- the impact and realistic attack path;
- reproduction steps or a minimal example;
- whether secrets, private data, or unsafe tool execution are involved;
- any suggested mitigation.

Do not include live credentials, customer data, private URLs, or restricted vendor material. Revoke any leaked credential before reporting it.

Reports are handled on a best-effort basis. The maintainer will validate the issue, agree on a disclosure approach when appropriate, and credit the reporter if requested and practical.

## Scope

Relevant security issues include:

- instructions that could cause secret exfiltration;
- prompt-injection paths that override evidence or safety boundaries;
- unsafe shell, browser, API, or file-system guidance;
- links or scripts that misrepresent their destination or effect;
- accidental inclusion of credentials, personal data, or restricted material;
- package or CI configuration that permits unreviewed code execution.

General research inaccuracies should be reported as normal issues rather than security vulnerabilities.
