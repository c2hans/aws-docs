---
name: claude-platform-plan
description: security-questionbuilder attack-research plan for Claude Platform on AWS (IAM prefix aws-external-anthropic); reuse, don't restart.
metadata:
  type: project
---

Attack-research plan exists at `/work/aws-docs/ClaudePlatform-aws-external-anthropic-attack-research-plan.md` (Step-6 skeleton, sections 0-8), built from the offline mirror for **Claude Platform on AWS** (IAM prefix `aws-external-anthropic`, GA 2026-05, managed policies edited 2026-09-25 — inside the changed-since-push window).

**Why:** documentation-derived hypotheses only; downstream `aws-vuln-hunter` tests two authorized accounts with canary data and hard-stops at AWS's own service plane. Anthropic operates this platform (not AWS, unlike Bedrock) — the Account↔external-Claude-Platform seam is an in-scope customer-controllable boundary; only AWS-fleet identity/creds are the hard-stop.

**How to apply:** if asked to extend/re-run for this service, reuse the plan — don't restart. The five prime leads (all evidence-confirmed from actual managed-policy JSON, not reasoning):
1. Unconditioned `sts:TagGetWebIdentityToken` (FullAccess/ReadOnly/Inference/Limited) → console capability/workspace tag injection past `AssumeConsole`'s `Capability=developer` gate (ReadOnly/Inference don't even grant AssumeConsole). Lens CC/FF/C. Critical.
2. Workspace-header vs path-`{id}` authz split (only IAM resource type is `workspace`; all sub-resources ARN-less) → cross-workspace read of file/vault/memory/session by ID. Lens A. Critical.
3. `Get*` on `workspace/*` includes `GetVault` ("or its credentials") + `GetMemoryStore` in AnthropicReadOnlyAccess/InferenceAccess; long-term API key auto-attaches InferenceAccess → "read-only" role reads vault creds across all workspaces. Lens R/S/T. High.
4. `iam:EnableOutboundWebIdentityFederation` account-wide toggle (FullAccess). Lens U/E. High.
5. `CreateWebhook`/`CreateUserProfileEnrollmentUrl` server-side URL deref → SSRF from Anthropic fleet. Lens G. High.

Key doc-gaps blocking full assessment: sub-resource ID entropy, webhook/enrollment URL schema+TTL, SigV4 SignedHeaders coverage of `anthropic-workspace-id`, console session-tag trust model. See also [[reference_aws-docs-ai-footer]].
