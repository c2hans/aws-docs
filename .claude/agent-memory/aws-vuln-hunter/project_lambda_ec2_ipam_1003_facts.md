---
name: lambda-ec2-ipam-1003-facts
description: run 2026-10-03-1 verdicts for Lambda resource-policy facade + EC2 account-VPC-encryption + IPAM/RPKI leads (what's confirmed/refuted/blocked and why)
metadata:
  type: project
---

Run 2026-10-03-1 (aws-vuln-hunter) against A=183174222929 / B=289531347876 (both user/research-admin AdministratorAccess).

**CONFIRMED (files in /work/findings/):**
- **Lambda L1 CROWN** `PutResourcePolicy` evades `lambda:FunctionUrlAuthType` guardrail that `AddPermission` enforces. Same scoped principal: AddPermission --function-url-auth-type NONE → 403 explicit-deny; PutResourcePolicy w/ equivalent public InvokeFunctionUrl Principal:* grant → 200, lands in same store. Key only populated "during AddPermission/RemovePermission ops" → absent during PutResourcePolicy = silently inert guardrail. AWS condition-key-coverage asymmetry, High, aws-security.
- **EC2 Lead 1** `ec2:ModifyAccountVpcEncryptionControl` has NO Mode/exclusion condition key (only ec2:Region). Scoped role w/ bare action: DryRun unmanaged/attempt-enforce/exclusion-carve all → DryRunOperation. Can't author "deny unmanaged". Missing-condition-key AWS hardening defect, Medium. DryRun+simulate only, no state change.

**REFUTED:**
- Lambda L3 cross-acct resource-policy read: both get_policy + get_resource_policy 403 AccessDenied; authz-first (identical for existing vs non-existent ARN) → no enum oracle.
- Lambda L2 confused-deputy facade asymmetry: AddPermission ALSO accepts bare service-principal grants (s3/events/sns) with no SourceAccount/SourceArn → no asymmetry, not an AWS defect.
- EC2 Lead 3/4 BYOIP/ROA: Create accepts caller-asserted Rir+unowned OrganizationHandle (benign request-staging, emits ChildRequestXml w/ Amazon-issued child BPKI TA = customer-plane, NOT service-plane). Enable fails CLOSED (ParentBpkiTa format check, then ServiceUri validation). CreateIpamRoutingPolicyRegistration gated behind enable-complete (IncorrectState).
- **EC2 Lead 6 ServiceUri SSRF (hard-stop class): REFUTED, NO hard-stop.** ServiceUri validated synchronously pre-fetch; ALL rejected incl 169.254.169.254, RFC1918, arbitrary https, file://, and even real rrdp.arin.net/rpki.ripe.net. Strict allowlist/pattern; no caller-controlled fetch.

**BLOCKED:**
- Lambda Web Functions L4-L8: `lambda-web` SDK-absent (UnknownServiceError) + NXDOMAIN. Still unreleased in A/B.
- EC2 Lead 2 org declarative-policy override: both accts ManagedBy=account; creating declarative policy needs OOS mgmt acct 532876697804.
- EC2 Lead 5 cross-acct route disclosure: no shared org-IPAM/RAM-shared resource-discovery between A/B. findings scoped to own IPAM.
- EC2 Lead 7 cross-tenant ROA teardown: DryRun=caller-IAM-only (not ownership); B owns no assoc; IDs high-entropy/account-scoped describe; real delete destructive=OOS.

**OF-INTEREST (informational, intra-account only):** Lambda L9 — PutResourcePolicy accepts+stores explicit Deny statements (legacy AddPermission can't); RevisionId optional → blind clobber; DeleteResourcePolicy wholesale strip. Granularity asymmetry real but gated behind holding perms-mgmt → not cross-boundary.

Note: IPAM advanced-tier reachable+creatable in A; create_ipam Tier='advanced', then create_ipam_internet_registry_association → pending-enable in seconds. Validation ordering: IpamId/assocId resolved FIRST (NotFound), then ParentBpkiTa format, then ServiceUri. See [[reference_aws_env_setup]].
