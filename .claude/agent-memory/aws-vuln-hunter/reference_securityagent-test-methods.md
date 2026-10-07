---
name: securityagent-test-methods
description: AWS Security Agent (securityagent, API 2025-09-06) live-test facts — resource model, target-verification gate, control results from run 20261006-secagent
metadata:
  type: reference
---

AWS Security Agent (`securityagent`) live-tested 2026-10-06 in both in-scope accounts (see [[agentcore-env]]).
Service LIVE in us-east-1, both accounts, 94 ops, endpoint securityagent.us-east-1.amazonaws.com.

**Resource model / standup (cheap, no container):**
- Hierarchy: Application -> AgentSpace -> Pentest -> PentestJob -> Finding. Also Integration, TargetDomain, PrivateConnection.
- `CreateAgentSpace(name=...)` works standalone (no Application needed, no role). Tag via `tags={}`.
- Pentest needs: a `serviceRole` that MUST be pre-registered in the AgentSpace via `UpdateAgentSpace(name=REQUIRED, awsResources={'iamRoles':[arn]})` (UpdateAgentSpace requires `name` even on partial update, else "Name is required").
- Service role trust: Principal securityagent.amazonaws.com, sts:AssumeRole + sts:SetContext, conditions aws:SourceAccount + aws:SourceArn ArnLike agent-space/* and application/*.
- Pentest REQUIRES >=1 endpoint. Endpoint domain MUST match a TargetDomain associated to the AgentSpace via `targetDomainIds` (set through UpdateAgentSpace) AND be verified/UNREACHABLE.
- `CreateTargetDomain(verificationMethod='PRIVATE_VPC')` => immediate status UNREACHABLE, NO proof needed; associating it lets CreatePentest accept any endpoint domain name. DNS_TXT/HTTP_ROUTE return a token, land PENDING.
- Actor auth providerType enum: SECRETS_MANAGER | AWS_LAMBDA | AWS_IAM_ROLE | AWS_INTERNAL. AWS_INTERNAL is NOT a service-plane identity — its `value` is validated as a secrets-manager ARN / OAuth refresh token like the others.

**Confirmed control-plane behaviors (oracles):**
- Tenant isolation CLEAN: cross-account AgentSpace => ResourceNotFoundException "The specified agent instance does not exist" (same as bogus id, no existence leak). my-AS + foreign-childId => child in `notFound` list (child bound to AgentSpace). GetIntegration foreign id => RNFE. ListActorMessages cross => "Pentest not found". No cross-tenant IDOR (L1/L2/L9 refuted).
- IAM resource-ARN scoping WORKS: securityagent:* scoped to a single agent-space ARN permits that space's child ops (BatchGetPentests etc.) and DENIES ListAgentSpaces/other spaces/CreateAgentSpace. => "least-privilege trap" (Grafana-style) is REFUTED; broad managed policy is a choice not a necessity.
- iam:PassRole ENFORCED on CreateAgentSpace/UpdateAgentSpace (awsResources.iamRoles). Cross-account role/VPC registration => AccessDenied "Cross-account pass role is not allowed" / "VPC configuration not found in agent instance". But CreatePentest does NOT re-check iam:PassRole on serviceRole (role must already be registered though — minor inconsistency, mitigated).
- GetIntegration WITHHOLDS the stored PAT/token (returns id/provider/providerType/displayName/targetUrl only).
- DNS_TXT verification tokens are high-entropy, per-account, non-reusable.

**THE finding (control-plane target-authorization gap, run 20261006-secagent):**
- `endpoints[].uri` ARE gated by TargetDomain verification (IMDS/private-IP/localhost/*.amazonaws.com all rejected "domain hasn't been verified"). Every endpoint checked.
- `actors[].uris[]` are NOT gated: with one valid endpoint present, actor URIs accept ANY host incl. https://169.254.169.254/ with no verification. This is the incomplete-enforcement gap (L3). No service-specific condition key exists to constrain target URIs, so IAM cannot compensate.
- HARD STOP RULE for this service: an IMDS/service-plane actor URI accepted at CreatePentest = capture reqid+ts and STOP; NEVER call StartPentestJob against a non-owned/IMDS target. The control-plane accept IS the finding.
- L8: cross-account SECRETS_MANAGER secret ARN accepted at CreatePentest (contradicts documented "cross-account not supported") but actual read needs StartPentestJob + permissive resource policy (data-plane likely blocks — unconfirmed). Config-accept alone not proven exploitable.
- L4: InitiateProviderRegistration targetUrl is GITHUB-only, regex https-only no-path; it reflects the host into a client-side consent `redirectTo` (open-redirect flavor), NOT a server-side fetch at Initiate.
- Minor info-leak: validation errors leak internal Pydantic format ("N validation error for Actor ...").
- Throttling kicks in ~5 req/s (ThrottlingException 429) — pace requests.
- `CreateOneTimeLoginSession` / `HandleProviderCallback` are NOT in the 2025-09-06 botocore model (plan assumed them from docs) — not callable.
