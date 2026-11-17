# Agent Memory Index

- [AWS test environment](project_aws-test-environment.md) — two in-scope accounts (A=183174222929, B=289531347876), no aws CLI (use boto3, creds at /work/.aws), trail limit, run-id tag collisions.
- [AWS-managed control findings](project_aws-managed-control-findings.md) — confirmed quarantine-twin + permissions-boundary escape defects (sweeps 1-2); the method that works.
- [agentaccess-mcp service](project_agentaccess-mcp.md) — live WorkSpaces Agent Access MCP: how to drive/sign it, and which isolation controls held in the 2026-11-17 sweep (H1-H9 verdicts).
- [Lambda new-surface findings](project_lambda-new-surface-findings.md) — Runtimes/MicroVMs/WebFns live-tested: runtime resource-policy public-guard gap (confirmed); xacct runtime assoc + microVM xacct boundaries HELD; API shapes recovered.
- [Cognito session-mgmt findings](project_cognito-session-mgmt-findings.md) — session APIs + GetDerivedToken held (all REFUTED); only may_act gap (documented); SSO tests need a browser harness.
- [SM cross-account replication](project_secretsmanager-xaccount-replication.md) — new SM x-account replica API family hunted 2026-11-17: consent model robust (all bypasses refuted), 1 low account-existence oracle; the two accounts are SAME-ORG.
- [Continuum + ODB enablement gates](project_continuum-odb-enablement.md) — continuum write-gate + odb not-onboarded block write-plane testing in both accounts; what's still statically confirmable.
