---
name: agentcore-payments-hunt
description: Ongoing doc-only vuln hunt of Amazon Bedrock AgentCore Payments (x402/MPP crypto signing); leads, statuses, top findings
metadata:
  type: project
---

User is running a documentation-derived AWS vulnerability hunt on **Amazon Bedrock AgentCore Payments**
(new feature: AI agents autonomously sign crypto/stablecoin payments via x402 and MPP). Source docs live at
`/work/aws-docs/docs/bedrock-agentcore/latest/devguide/payments-*.md` + `.../APIReference/API_*Payment*`,
control plane `.../bedrock-agentcore-control/latest/APIReference/API_*Payment{Manager,Connector,CredentialProvider}*`.

**Why:** AWS vuln-hunter engagement; money is the asset. Working from docs mirror + public web only (no live target, no source).

**How to apply:** When asked to extend/re-run, reuse the ranked findings in the report at
`/tmp/.../scratchpad/agentcore-payments-hunter-report.md`. Top confirmed-shape leads:
- F-02 (High): service signs to any merchant/injection-controlled `payTo`; docs state no server-side payTo/network/asset allowlist, only amount cap.
- F-01 (High, multi-tenant/IAM): `X-Amzn-Bedrock-AgentCore-Payments-User-Id` header is unverified; open question = does ProcessPayment bind instrumentId to session's userId (undocumented, needs live test).
- F-04 (Med-High): `BedrockAgentCoreFullAccess` = `bedrock-agentcore:*` re-grants ProcessPayment+CreatePaymentSession, collapsing the 4-role Deny separation.
- F-06 (Med): permit2AllowanceLimit "sets not adds", docs suggest unlimited uint256 → standing on-chain allowance.
- F-03 (needs live): session maxSpendAmount TOCTOU; docs use "reservation" language (leans mitigated).
- F-05 largely refuted: ResourceRetrievalRole trust has aws:SourceAccount + SourceArn + secrets aws:ResourceAccount conditions.
Corrections made to upstream plan: session/instrument IDs are 15 chars over ~63-symbol alphabet → NOT enumerable.
