---
name: adjacent-newfeatures-1002-facts
description: Live results for 5 new API actions (GuardDuty custom detection rules, IdC UpdateIdentityStore, SageMaker AttachClusterNodeNetworkInterface, EC2 Client VPN auth-policy, DRS recovery plans) — run 2026-10-02-1
metadata:
  type: project
---

Run 2026-10-02-1 against A=183174222929 (default) / B=289531347876 (awsbb2). AdjacentNewFeatures plan, 11 leads.

**Org topology (load-bearing):** A and B are BOTH member accounts of an org whose MANAGEMENT account is **532876697804** (out of scope — same mgmt as prior Omni/secagent runs). `organizations:DescribeOrganization` is AccessDenied to both members. They share ONE org IdC instance `ssoins-7223cfab9178db6f` / identity store `d-9067d20885`, **OwnerAccountId 532876697804**. There is NO A-owned or B-owned identity store — IdC is one-per-org owned by mgmt.

**SDK gaps (botocore 1.43.95):** `identitystore:UpdateIdentityStore`/`DescribeIdentityStore` and `ec2:ModifyClientVpnEndpointAuthorizationPolicy`/`GetClientVpnEndpointAuthorizationPolicy` are ABSENT from the SDK but DEPLOYED on the wire — hand-craft. IdentityStore = JSON1.1, target `AWSIdentityStore.<Op>`, host `identitystore.us-east-1.amazonaws.com`, signing name `identitystore`. EC2 = query protocol, Version 2016-11-15. GuardDuty/SageMaker/DRS new actions ARE in the SDK.

**L1 (IdC bare-id IDOR) REFUTED.** DescribeIdentityStore with bare `d-9067d20885` from member A/B → `AccessDeniedException: ... on resource arn:aws:identitystore::532876697804:identitystore/d-9067d20885 because no resource-based policy allows the action`. The bare id is canonicalized to the OWNING-ACCOUNT ARN and gated by a RESOURCE-BASED POLICY keyed on 532876697804. Bogus id → ResourceNotFoundException. Dual-naming does NOT bypass account qualification. Did NOT call UpdateIdentityStore (would mutate real org perimeter — scope + don't-weaken-posture); Update inferred-gated identically (same ARN resolution). L4/L10 (within-acct Update) BLOCKED: no in-scope store.

**L2 (GuardDuty assoc IDOR) REFUTED.** Custom detection rules need a detector (enable canary, DeleteDetector to tear down). AWS-managed rules shared across accts (same RuleId e.g. `admin-policy-attached-to-role`). `Get/UpdateCustomDetectionRuleAssociation` take only RuleId+AssociationId (no acct qualifier) BUT a real foreign AssociationId returns the IDENTICAL `404 ResourceNotFoundException: Association not found` as a bogus id — namespace is account-scoped, no existence/ownership leak. Write-IDOR also 404.

**L3 (member silences org-wide) REFUTED.** Member A → `AccessDeniedException` on Create/Update/ListCustomDetectionRuleOrgConfiguration. Delegated-admin guarantee holds. Positive silencing test needs out-of-scope mgmt delegated admin → BLOCKED.

**L7 (member self-blind):** A CAN mutate the mode of its OWN self-created association (200) — expected; the doc "AccessDenied" guarantee concerns org-pushed associations, needs delegated admin → BLOCKED for the real test.

**L11 (GuardDuty rule-logic disclosure) CONFIRMED-behavior, low.** `GetCustomDetectionRule` returns full `Definition.Expression` SQL to ANY detector-holding member, incl. evasion-relevant carve-out `NOT contains(sourceIPAddress,'amazonaws.com') AND sourceIPAddress != 'AWS Internal'`. AWS-authored artifact (B3), likely intended transparency; evasion-useful. Not cross-tenant.

**L4/L6 (SageMaker AttachClusterNodeNetworkInterface) BLOCKED(needs-hyperpod-cluster).** 3 inputs (ClusterName/NodeId/NetworkInterfaceId), ClusterName is account-scoped (not ARN) → validates cluster-ownership FIRST (`ResourceNotFound: Cluster not found`). ENI-ownership/VPC-bridge test needs a live HyperPod cluster (ml.* + EKS, disproportionate cost for low-conf doc-gap).

**L5/L8 (EC2 Client VPN auth-policy token forge/ShadowMode) BLOCKED(needs-3P-device-trust-provider+live-client).** Action deployed; DryRun → `DryRunOperation: Request would have succeeded` (my principal authorized; DryRun passes before endpoint-existence). Core oracle needs CrowdStrike/Jamf/JumpCloud posture token + connecting OpenVPN client = out-of-scope external infra.

**L9 (DRS StartRecoveryPlanExecution out-of-plan server):** cross-account REFUTED (step rejects foreign/fabricated server ARN `Source servers not found or not accessible`; Start on B's plan ARN → 403 explicit-deny resource policy). Intra-account definitive BLOCKED(needs-2-replicated-source-servers) but DRS validates server accessibility at EVERY seam (step-create + Start requires steps) — argues against the lead. DRS: A pre-initialized, B uninitialized.

No confirmed vulnerabilities this run. All resources torn down (verified empty).
