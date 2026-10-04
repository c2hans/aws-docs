# finding-001 — AWS-managed policies `AnthropicReadOnlyAccess` (v4) & `AnthropicLimitedAccess` (v8) grant unconditionable, cross-tenant-capable user-profile access

- **Status:** artifact-CONFIRMED; live exploitability HARD-STOPPED at AWS service plane
- **Routing:** `routing: aws-security — human submission required`
- **Severity:** High (Critical for the create/update write twins) at artifact level; exploitability low-confidence (gated behind untestable Anthropic/Claude-Platform backend)
- **Classification:** boundary-dependent — Tenant↔tenant within the Anthropic/Claude-Platform SaaS plane (one Anthropic org per AWS account)
- **Run:** `2026-10-04-m1` | **Window:** `66a75857b6..8aa2af7473` (2026-10-04 sync) | **Plan:** `_change-analysis/plans/2026-10-04-sincelastpush/aws-managed-policy-weakdefaults-attack-research-plan.md` (lead A1, ranked #1)

## What changed in this window (freshness)
The `aws-external-anthropic` **user-profile action family is new to these policy versions** (not present in the
prior v3/v7 examined in run 2026-09-30-1). `AnthropicLimitedAccess` v7→v8 **relocated** `CreateUserProfile`/
`UpdateUserProfile` out of a `workspace/*`-scoped statement into the resourceless `Resource:"*"` statement and
**added** `GetUserProfile`/`ListUserProfiles`; `AnthropicReadOnlyAccess` v4 added `GetUserProfile`/`ListUserProfiles`.

## Boundary crossed
Tenant↔tenant inside the Anthropic/Claude-Platform plane. The IAM layer — which an operator would normally rely on
to scope a read-only grant to their own tenant — offers **zero expressible constraint** for these actions.

## Evidence (observed)
- `AnthropicReadOnlyAccess` v4 statement `AnthropicReadOnlyResourceless` lists
  `aws-external-anthropic:GetUserProfile` and `ListUserProfiles` under `Resource:"*"` with **no `Condition`**.
- `AnthropicLimitedAccess` v8 additionally carries `CreateUserProfile` + `UpdateUserProfile` in the same
  resourceless `*` statement (write twins moved out of the previously `workspace/*`-scoped statement).
- The `aws-external-anthropic` Service Authorization Reference defines **only** a `workspace` resource type and
  **no** condition keys applicable to the user-profile actions ⇒ `Resource:"*"` is the only expressible scope;
  an operator cannot author an IAM guardrail restricting these actions to their own tenant/workspace.
- `SimulateCustomPolicy` for a principal holding **only** the policy JSON returned `allowed` for all four actions
  against `*` (EvalDecision=`allowed`, no implicit/explicit deny) — the grant is inherent to the AWS-authored
  policy, not an artifact of an over-privileged test user (privilege check passed).

## Why live confirmation was hard-stopped
Whether these grants actually read/write **another tenant's** profiles depends entirely on how the Anthropic
backend binds the federated bearer token to the caller's org. Reaching that plane requires an active Marketplace
subscription (`prod-3qbeiztufnva6`) and federating into Anthropic's own service infrastructure = AWS's service
plane. Per standing rule 4, artifact evidence was preserved and blast radius was NOT developed.

## Impact (bounded honestly)
- If the backend relies on IAM for tenant scoping: a *read-only* policy permits cross-tenant user-profile PII
  enumeration/read, and `AnthropicLimitedAccess` permits cross-tenant profile create/update.
- If the backend enforces org binding internally (the likely, defensible design): the IAM breadth is cosmetic.
- Reportable on its own weight regardless: a **ReadOnly-adjacent AWS-managed policy granting write twins on an
  unconditionable `*`** is a least-privilege/artifact defect.

## Severity inputs (AWS questions)
1. Verified external knowledge: none found (inferred). 2. Customer data exposed: not demonstrated — live leg
hard-stopped; potential class is user-profile PII, no metadata signal obtained. 3. AWS reputation: yes-if-backend-
fails (would read as AWS/Anthropic tenant isolation breaking). 4. AWS IP: no. 5. Crosses a boundary: yes
(artifact enables it; enforcement unverified). 6. Real finding vs user misconfig: real — defect is in the
AWS-authored policy, confirmed under a scoped-down principal.

## Confidence
Medium on the artifact defect (Simulate + service-auth reference); low on exploitability (gated behind untestable
backend). Raised only by an AWS-internal check of whether `aws-external-anthropic` scopes user-profile actions
server-side by caller org.

## Remediation direction
Add a `workspace`/tenant resource type (or an `aws-external-anthropic:` condition key) to the user-profile actions
so operators can scope the grant; at minimum remove `CreateUserProfile`/`UpdateUserProfile` from the ReadOnly-
adjacent policy and keep the write twins in a resource-scoped statement.

## Teardown
N/A for A1 (no resources created for this lead — Simulate only). Run-wide teardown verified clean (ledger empty).
