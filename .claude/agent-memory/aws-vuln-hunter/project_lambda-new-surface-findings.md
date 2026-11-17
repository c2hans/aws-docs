---
name: lambda-new-surface-findings
description: Live-tested results for the 2026 Lambda new surface (customer-managed Runtimes, MicroVMs, Web Functions) — API shapes + which boundaries held/broke
metadata:
  type: project
---

Executed plan `/work/analysis-2026-11-17/qb/02-lambda-runtime.md` (W1-LAM1, W2-LAM3, W3-LAM-WF) live in us-east-1, both accounts. Four real SDK clients exist and are live: `lambda-core` (Runtimes + network-connectors), `lambda-microvms`, `lambda-web`, plus resource-policy on main `lambda`.

**Runtime API shape (doc-gap recovered):** `CreateRuntime(Name,Tags,Description,ReleaseLifecycle)`; `CreateRuntimeVersion(RuntimeName,ImageUri*,Name,DryRun)` — code artifact is an **ECR image URI** (same-account; needs repo policy granting `lambda.amazonaws.com` ecr:BatchGetImage+GetDownloadUrlForLayer), resolves to a digest; `CreateRuntimeAlias(RuntimeName,RuntimeVersion,Name)` mutable pointer. A function consumes a runtime via `CreateFunction(Runtime='custom', RuntimeConfig={RuntimeArn, RuntimeAlias})`. `RuntimeIdentifier`/`RuntimeArn` patterns ALLOW a cross-account ARN prefix. Runtime resource policy via `lambda` PutResourcePolicy (`/2026-07-09/resource-policy/`), ResourceArn pattern covers `runtime/...`.

**CONFIRMED (AWS-authored control gap, low-med):** runtime `PutResourcePolicy` accepts `Principal:"*"` (public) and foreign-account principals with 200 — the public-access guard the **sibling web-function PutResourcePolicy enforces** (`ValidationException` "would grant public access") is ABSENT on runtimes. Verified functionally: a `*` policy let the OTHER account create a function on the runtime while matched only by the wildcard. A customer-managed runtime (code base image) can be made world-associable with no guardrail. In scope because the inconsistency is in AWS-authored validation.

**REFUTED — boundaries that HELD:**
- W1-LAM1 cross-account runtime association: owner IS bound. Without A's resource-policy grant, B gets `AccessDeniedException` on `lambda:AssociateRuntimeAlias`/`GetRuntimeVersion` (403). Cross-account association works ONLY with an explicit owner resource-policy grant (like layers). Not an existence/tag-only authz bypass.
- W2-LAM3 microVM cross-account (control plane): RunMicrovm naming foreign image -> AccessDenied "no resource-based policy"; foreign execution role -> "Cross-account pass role is not allowed"; foreign network-connector -> "Cross-account network connectors are not enabled". CreateMicrovmAuthToken for non-existent/foreign microvm -> 404 (minting is existence/ownership-gated). Data-plane JWE replay = could-not-test (needs full microVM image build on AWS fleet; declined on cost + fleet-identity HARD-STOP risk).

**Documented-intended (confirmed live, informational):**
- Web Function IamAuth: unsigned -> 403 (boundary holds). But body NOT validated against `X-Amz-Content-SHA256`: a request signed with sha256 of body-X but carrying body-Y returns 200 and delivers body-Y; `UNSIGNED-PAYLOAD` accepted. Documented ("implement body integrity in your app"). Lambda strips Authorization before forwarding.
- Web Function `ApplicationManaged` endpoint: fully public, no-creds POST returns 200 and delivers body; resource policy not evaluated for invoke. Default authType of `aws lambda-web deploy`; governance control is an SCP on `lambda:Request/WebFunctionAuthType`.
- Runtime alias late-binding: owner repointing alias (UpdateRuntimeAlias v1->v2) silently changes the pinned `RuntimeVersionConfig` on a consumer's already-created function in the other account, no consumer action/re-auth. Intended late-binding (consumer can pin a version ARN instead). Revoking the share leaves existing associations live (DeleteRuntime = reversible soft-delete, 30-day PENDING_DELETION).

See [[aws-test-environment]], [[aws-managed-control-findings]] (same "incomplete AWS-authored control" theme as the runtime public-policy-guard gap).
