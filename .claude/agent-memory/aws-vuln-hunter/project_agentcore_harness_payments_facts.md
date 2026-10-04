---
name: agentcore-harness-payments-facts
description: Live behavior + boundary verdicts for Bedrock AgentCore harness lifecycle-hooks and payment-connector credential rotation (run 2026-09-28-B)
metadata:
  type: project
---

Bedrock AgentCore harness-hooks + payment-rotation hunt (run vh-run-id=2026-09-28-B, us-east-1, accounts A 183174222929 / B 289531347876). See [[env-sandbox-sessions]].

**SDK vs service reality (botocore 1.43.95):** clients `bedrock-agentcore-control` + `bedrock-agentcore` present. `CreateHarness/UpdateHarness/GetHarness/InvokeHarness` present but the SDK model LACKS `hooks[]`; `RotatePaymentConnectorCredentials` ABSENT from SDK. BOTH surfaces are deployed server-side — reach them by hand-crafting: inject `hooks[]` into UpdateHarness body at the botocore `before-sign` event (set `request.data`, NOT `request.body` which has no setter), or SigV4-sign a raw `POST /payments/managers/{mgr}/connectors/{conn}/rotate-credentials` (signing name `bedrock-agentcore`). Real hook shape: `{beforeToolCall|beforeInvocation|afterToolCall|afterInvocation:{name*, target:{sns:{arn}|lambda:{arn}|eventBridge:{arn}}, failureMode}}`. Read hooks back via raw GetHarness wire body (before-parse `response_dict['body']`) since SDK drops the field.

**Verdicts (all boundary-relevant hypotheses REFUTED — no confirmed cross-boundary vuln):**
- Harness cross-tenant registration/IDOR: REFUTED. B GetHarness(A's id)=404 (==random, no enum oracle); UpdateHarness=403. Account-scoped.
- Harness cross-account/cross-partition hook TARGET acceptance: config-plane CONFIRMED (accepts aws-cn/aws-us-gov/other-acct SNS/Lambda/EventBridge, no same-account check, no target-existence check). Delivery of raw session payload (prompts) to a B topic CONFIRMED — but owner-driven, and effective publish principal is the CUSTOMER EXECUTION ROLE (`assumed-role/<execRole>/BedrockAgentCore-*`), NOT a fleet identity → confused-deputy REFUTED (B can scope its resource policy to the role ARN). NO HARD STOP.
- Payment rotation authz parity: REFUTED. Rotate gated by its OWN dedicated action `bedrock-agentcore:RotatePaymentConnectorCredentials` (only-that-action→404 authz-passed; UpdatePaymentConnector/UpdatePaymentCredentialProvider/GetPaymentConnector/deny-all→403 naming rotate action). Doc gap: that action is ABSENT from service-authorization `list_bedrock-agentcore.md` (informational only).
- Payment IDOR (manager/credprovider): REFUTED, account-scoped 404. Connector-level rotate WRITE INSUFFICIENT — `CreatePaymentConnector` (CoinbaseCDP) blocked by `SubscriptionRequiredException` (AWS Marketplace sub required) so no connector could be provisioned; shared-project blast radius untestable here.
- Cross-account secret read (wallet signing secret): REFUTED (403, no resource policy). Intra-account: a principal with ONLY `secretsmanager:GetSecretValue` (denied AgentCore API) reads the raw service-managed wallet secret at `secret:bedrock-agentcore-identity!.../wallet-*` — non-boundary, but AWS-managed `BedrockAgentCoreFullAccess` grants `secretsmanager:GetSecretValue` on `secret:bedrock-agentcore*` (=`bedrock-agentcore:*` on `arn:aws:bedrock-agentcore:*:*:*` + that SM statement). API hides secret values but SM storage is IAM-only walled.

**Provisioning gotchas:** harnessName regex `[a-zA-Z][a-zA-Z0-9_]{0,39}` (no hyphens). Harness exec role must trust bedrock-agentcore.amazonaws.com; CreateHarness fails until role propagates (retry ~10s). Harness has managed memory auto-created; DeleteHarness cascades memory deletion (slow, several min). PaymentManager role needs bedrock-agentcore:TagResource+more. CredentialProvider CoinbaseCDP: apiKeyId `[a-zA-Z0-9\-_]+`, apiKeySecret=base64 64-byte Ed25519 (seed+pub), walletSecret=base64 PKCS8-DER EC P-256. DeletePaymentCredentialProvider auto-removes backing SM secrets.

Result file: `/work/aws-docs/findings/result-agentcore-2026-09-28-B.md`.
