---
name: athena-federation-isolation
description: Amazon Athena federated-query / data-source-connector isolation model and refuted hypotheses (2026-09-09 run)
metadata:
  type: project
---

Athena **federated-query / data-source-connector** control+data planes were hunted 2026-09-09 (plan `/work/athena-federation-connector-research-plan.md`). All hypotheses F1-F8 REFUTED.

**Root cause of robustness — the entire FEDERATED flow is authorized against the CALLER's identity** (observed via CloudTrail + canary):
- `CreateDataCatalog FEDERATED` → Athena calls Glue `CreateConnection` and CFN `CreateStack` with `userIdentity=<caller>`, `invokedBy=athena.amazonaws.com`; CFN then `CreateRole`/`PutRolePolicy`/`CreateFunction` as the caller (`invokedBy=cloudformation.amazonaws.com`). Athena never lends its own service privileges.
- Query-time connector `lambda:InvokeFunction` is issued as the **caller** (scoped role lacking invoke → AccessDenied attributed to the caller).
- `SecretArn` is dereferenced **inside the connector Lambda under its execution-role identity** — not Athena, not the caller's user creds.

**Why:** this caller-identity model defeats every confused-deputy hypothesis. Don't re-hunt these unless the identity model changes.

Verdicts: F1 PassRole privesc REFUTED (iam:PassRole enforced at Lambda CreateFunction; negative control isolates it). F2 derived-role over-privilege REFUTED (standard awslabs SAM template, least-privilege; note: `SpillBucket` CFN param has no AllowedPattern → derived S3 policy resource is caller-influenced, but caller-authorized so no crossing). F3 name-collision CONFIRMED (names differing only in `- _ @` and case collapse to one derived `athenafederatedcatalog_<sanitized>` name) but hijack REFUTED (synchronous fail-closed "already exists" pre-check; no adoption/overwrite; residual = same-account name-squat DoS). F4 cross-account `connection-arn` REFUTED (explicit same-account ownership check). F5 SecretArn confused-deputy REFUTED (execution-role-gated read). F6 SSRF downgraded to self-SSRF (connector is caller-owned Lambda). F8 cross-account connector Lambda REFUTED (invoke authorized as caller vs target resource policy).

Prior sibling run (`/work/athena-variant-analysis-research-plan.md`): the disclosed `system`-catalog validation-asymmetry family — also all REFUTED.
