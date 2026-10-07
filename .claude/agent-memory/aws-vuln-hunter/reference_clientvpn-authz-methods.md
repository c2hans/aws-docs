---
name: clientvpn-authz-methods
description: Client VPN endpoint authorization-policy (Cedar/device-posture) trio — IAM gating facts, no-endpoint DryRun oracle, provisioning recipe, L1 refutation
metadata:
  type: reference
---

Client VPN authorization-policy trio: `ec2:{Get,Modify,Delete}ClientVpnEndpointAuthorizationPolicy` (boto3 1.43.108). Tested sweep-3 2026-10-06 (vh-run-id=20261006-cvpnauthz). See [[agentcore-env]] for accounts.

**No-endpoint IAM oracle (key technique):** For these EC2 ops the IAM permission check PRECEDES resource validation — DryRun on a syntactically-valid but non-existent endpoint id (`cvpn-endpoint-<17hex>`) returns `DryRunOperation` (412) if authorized, `UnauthorizedOperation` if not. So the ENTIRE IAM-granularity analysis needs NO provisioned endpoint. All three require only `ClientVpnEndpointId`; all support `DryRun`.

**Authoritative action-name discovery:** assume a scoped role with NO ec2 perms, DryRun → `UnauthorizedOperation` whose message carries `Encoded authorization failure message:`; `sts:decode_authorization_message` → `context.action`/`context.resource` = the exact IAM action string + ARN the service checks. Admin has DecodeAuthorizationMessage.

**L1 verdict (REFUTED, high-confidence):** each API is gated by its OWN dedicated action (not generic `ec2:ModifyClientVpnEndpoint`), resource-type `client-vpn-endpoint` (ARN-scopable: SimulateCustomPolicy ARN-match=allowed, mismatch=implicitDeny). Get/Modify/Delete independently gated (read ≠ write). The actions are ABSENT from `list_ec2.md` = documentation gap ONLY. Prior report M-2 claim "Cedar policy requires its own action" = VERIFIED CORRECT.

**L2/L3/L4/L7 = intended-behavior, not AWS defects:**
- L4: malformed Cedar REJECTED synchronously (`InvalidParameterValue` "provide a valid Cedar policy document"), prior doc unchanged — fail-CLOSED; never saw status=failed. Over-broad `permit(principal,action,resource);` accepted = customer footgun.
- L3: `Modify ShadowMode=enabled` with NO PolicyDocument = partial update; `Get` shows ShadowMode=enabled but PolicyDocument intact → auditor reading only the doc misses that enforcement is off. Operator caution, documented feature.
- L2: Delete → status=deleting, removes gate in one call. Documented feature, gated.
- L7: unauthorized principal gets `UnauthorizedOperation` regardless of existence (no leak, auth precedes lookup); authorized+nonexistent → `InvalidClientVpnEndpointId.NotFound`.

**Endpoint provisioning recipe (minimal cost):** cert-auth, ClientCidrBlock=/22, ConnectionLogOptions Enabled=false, NO target-network associations (associations are what incur hourly charge; bare endpoint ~free). Server cert CN MUST be a FQDN domain (ACM import else create_client_vpn_endpoint fails "does not have a domain"). Import server cert + CA(as client-root) to ACM. Teardown order: delete endpoint → wait gone → delete ACM certs (ResourceInUse until endpoint gone) → delete IAM role policies+roles. Clean tenant isolation: awsbb2 never needed (no cross-account path; endpoint is account-scoped).
