# Amazon EC2 (DocumentHistory-derived) — Attack Research Plan

**Source of leads:** The EC2 User Guide **Document History** page as a change-diff —
`https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/DocumentHistory.html`
(offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/DocumentHistory.md`), expanded against the individual
feature pages, the EC2 Service Authorization reference
(`/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`), the AWS-managed policy JSON
(`security-iam-awsmanpol.md` + the `aws-managed-policy` reference), and `list_autoscaling.md` /
`list_ec2-instance-connect.md`.

**Status:** documentation-derived hypotheses only. **Nothing has been tested against a live AWS account.** Every
"Confirm/Refute oracle" is the observation a downstream hunter (`aws-vuln-hunter`) must make against an
*authorized* account to settle the claim. The plan never asserts a bug exists — it asserts a boundary *might not
hold* and says exactly how to find out.

**Why DocumentHistory is the right lens:** AWS's `[NEW]` markers concentrate on the least-reviewed surface. Document
History is a dated, ranked changelog — treating it as a docs-diff makes the newest features (2024-2026) the priority
set automatically. The newest entries cluster into five mechanism groups, analysed below.

---

## 0. How to use this document

- Work in priority order (Section 5 is pre-ranked). Each lead is **Claim → Mechanism (doc evidence) → Confirm/Refute
  oracle → Preconditions / Cost / Severity**. Look left and right for adjacent bugs the plan did not anticipate.
- **HARD STOP:** the moment evidence shows an identity / credential / ARN / account belonging to AWS's own service
  plane (e.g. a Nitro-fleet credential, a service-linked-role's underlying fleet identity, the EICE proxy's own
  identity, the Capacity Manager SLR's cross-account channel), **stop, preserve evidence, flag for AWS-Security
  disclosure.** Do not escalate past existence.
- **Dummy data only.** Use synthetic canary secrets/tags/key-pairs. Never read real third-party data beyond the
  minimum needed to prove the boundary broke. Tear down every resource created.
- **DryRun is a trap, not an ownership oracle.** `DryRunOperation` success proves only the *caller's IAM*, evaluated
  before resource resolution — it is explicitly how EC2 Fast Launch does its (one-time) permission check. Never cite
  a DryRun result as proof of cross-tenant resource access.
- **Static-first.** For every AWS-managed-policy lead, use `iam:SimulatePrincipalPolicy` /
  `iam:SimulateCustomPolicy` as the first (resource-touchless) oracle before any live scoped call.

---

## 1. Pentest Objectives (boundary-breach goals, stated as concrete outcomes)

1. **Privilege escalation via launch-identity late-binding.** Obtain an IAM role/instance-profile on a running
   instance that the acting principal could not have passed directly — through EC2 Fast Launch `$Latest`/`$Default`
   re-resolution, instant-EC2-Fleet overrides, Auto Scaling launch-template versioning, or `EC2FastLaunchFullAccess`.
2. **Cross-account data / telemetry / billing access.** Read another account's capacity/cost telemetry, AMI-usage
   customer list, or image references; or shift cost onto a non-consenting account — using only an identifier or a
   managed read grant.
3. **Governance-control bypass.** Launch or boot content that an account's Allowed AMIs / AMI watermark / Block Public
   Access / IMDSv2-enforcement policy is supposed to forbid, by reaching the content through an unchecked sibling API
   or an unenforced launch path.
4. **Network/isolation pivot.** From an EICE tunnel, a Secondary Network, or a nested guest, reach a host, instance,
   port, or credential endpoint the segmentation model says is unreachable (hard stop if it is AWS's control plane).
5. **IAM-artifact defect.** Prove that an AWS-authored, customer-uneditable managed policy / SLR grants materially more
   than its description implies (non-admin→admin, or cross-workload reach).
6. **Detection evasion / attestation fail-open.** Hide an attacker-created resource from the owner's inventory +
   EventBridge, or satisfy an attestation-gated KMS key with an absent/placeholder measurement.

---

## 2. Components, Assets, and Design

EC2 is not one service; the DocumentHistory surface spans six interacting planes. Only the customer-reachable
front edges are in scope; the Nitro/host fleet is the hard-stop line.

```
                         ┌─────────────────────────────────────────────────────────┐
   Customer IAM          │                 EC2 CONTROL PLANE (regional)              │
   principal ───SigV4───►│  RunInstances / CreateFleet / RequestSpot* / EnableFast- │
                         │  Launch / ReplaceRootVolume / Modify*MetadataDefaults /   │
                         │  Capacity* / *ImageAttribute / Create*ConnectEndpoint     │
                         └───┬─────────────┬──────────────┬───────────────┬──────────┘
                             │ assumes      │ late-binds    │ shares        │ provisions
                        ┌────▼────┐   ┌─────▼──────┐  ┌─────▼──────┐  ┌─────▼───────────┐
                        │ Service │   │  Launch     │  │ AWS RAM /  │  │ EICE proxy ENI /│
                        │ Linked  │   │  Template   │  │ Organiza-  │  │ Secondary Net / │
                        │ Roles   │   │ ($Latest/   │  │ tions      │  │ Managed-instance│
                        │ (Fast-  │   │  $Default)  │  │ (CR/CB/    │  │ fabric          │
                        │ Launch, │   └─────┬──────┘  │  Capacity  │  └─────┬───────────┘
                        │ Capacity│         │          │  Manager)  │        │
                        │ Mgr,    │         ▼          └─────┬──────┘        ▼
                        │ EICE,   │   ┌────────────┐         │          ┌──────────────┐
                        │ CRFleet)│   │  INSTANCE  │◄────────┘          │ Customer VPC │
                        └────┬────┘   │  (IMDS @   │  cross-acct        │ + Secondary  │
                             │        │ 169.254.   │  reach test        │ Network      │
                        ┌────▼─────┐  │ 169.254)   │                    └──────────────┘
                        │ EBS snap │  │  ├ IAM role creds (IMDSv1/v2, RoleDelivery)
                        │ /volume  │  │  ├ user-data, tags (InstanceMetadataTags)
                        │ (ebs:*   │  │  ├ NitroTPM/SEV-SNP attestation
                        │ cousin   │  │  └ L1 hypervisor ─► L2 nested guest
                        │ APIs)    │  └────────────┘
                        └══════════╪════════════════════════ HARD STOP ═══════════════╗
                                   ▼  NITRO HOST / AWS FLEET (out of scope — disclose) ║
                                   ╚═══════════════════════════════════════════════════╝
```

**Assets by sensitivity:**
- *Credentials:* instance-profile temp creds (via IMDS), KMS data keys gated by NitroTPM attestation, SLR identities.
- *Cross-tenant data:* AMI-usage customer lists, Capacity Manager org-wide telemetry (AccountID / "Unused Financial
  Owner" dimensions), image references, EBS snapshot disk content behind shared AMIs.
- *Governance state:* Allowed AMIs / watermark criteria, Block Public Access, account-level IMDSv2 enforcement,
  managed-resource visibility — all per-account/per-Region, settable directly or by an Organizations declarative policy.
- *Identifiers:* `ami-*`, `cr-*`/`cb-*`/`crf-*`, `eice-*`, launch-template IDs + `$Latest`/`$Default` aliases, SSM
  `resolve:ssm:` parameter paths, AMI *names* (used by Allowed AMIs `ImageNames`).

**Full AWS-managed-policy inventory for the Lens R/S sweep (13 policies named in `security-iam-awsmanpol.md`):**
`AmazonEC2FullAccess`, `AmazonEC2ReadOnlyAccess`, `AmazonEC2ImageReferencesAccessPolicy`, `AWSEC2FleetServiceRolePolicy`,
`AWSEC2SpotFleetServiceRolePolicy`, `AWSEC2SpotServiceRolePolicy`, `AWSEC2VssSnapshotPolicy`,
`AWSEC2CapacityManagerServiceRolePolicy`, `AWSEC2CapacityReservationFleetRolePolicy`, `EC2FastLaunchFullAccess`,
`EC2FastLaunchServiceRolePolicy`, `Ec2InstanceConnect`, `Ec2InstanceConnectEndpoint`. The audited ones below are the
newest/changed; the un-audited remainder (`AWSEC2SpotServiceRolePolicy`, `AWSEC2VssSnapshotPolicy`, `AmazonEC2FullAccess`)
are standing follow-ups.

---

## 3. Trust-Boundary Map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|---|
| B1 | Low-priv launch-template editor | SLR's `RunInstances` identity (any instance profile) | Fast Launch / ASG `$Latest`/`$Default` re-resolution with no permission recheck | Instance boots with an instance profile the editor lacks `iam:PassRole` for → IMDS yields its creds |
| B2 | Holder of `EC2FastLaunchFullAccess` | Any IAM role in the account | Unconditioned `RunInstances` + `iam:PassRole` in the managed policy, gated only by self-asserted `aws:RequestTag` | `SimulatePrincipalPolicy` returns `allowed` for `RunInstances`+`PassRole` on an admin-trusted profile |
| B3 | Member account (non-mgmt, non-DA) | Sibling account's capacity/cost telemetry | `GetCapacityManagerMetricData` has no account-scoping condition key; SLR auto-deployed org-wide | Call returns `AccountID`/"Unused Financial Owner" rows for an account the caller does not own |
| B4 | CR owner | Non-consenting billing-assigned account | Unilateral future-dated-CR cancellation; cancellation charge billed to assignee with no consent gate | Assignee's CUR shows the cancellation charge; no accept/reject API was offered to them |
| B5 | AMI consumer (shared/public) | AMI owner's customer list | `CreateImageUsageReport`/`DescribeImageUsageReportEntries` lack a documented owner precondition; no resource type in IAM | Non-owner call returns other accounts' identifiers for the AMI |
| B6 | AMI consumer with snapshot read | AMI owner disk content, bypassing AMI-layer gates | `ebs:GetSnapshotBlock`/`CopySnapshot` on the backing snapshot (a separate IAM resource type) | Raw blocks read even though the AMI is Allowed-AMIs-blocked / disabled / watermark-restricted |
| B7 | Attacker who can name an AMI / SSM param | Victim relying on name-based resolution | Allowed AMIs `ImageNames`-only criterion, or `resolve:ssm:` with over-broad `PutParameter` (whoAMI class) | Victim tooling selects the attacker's AMI id |
| B8 | Caller granted `OpenTunnel` (no optional conditions) | Any instance/port in the same VPC | EICE tunnel reachability bounded only by SG/route table, not by the tunnel/IAM default | Tunnel completes to an instance/port other than the intended target |
| B9 | Caller with `ModifyInstanceConnectEndpoint` | Arbitrary security group | EICE SLR's `ModifyNetworkInterfaceAttribute` on `security-group/*` has **no** Condition block | A non-EICE-owned SG is attached to the EICE ENI via the SLR |
| B10 | Caller with `CreateReplaceRootVolumeTask` | A privileged instance's IAM role | Root volume hot-swapped from a caller-prepared volume; instance IAM role persists | Attacker-prepped disk boots carrying the target instance's instance-profile creds |
| B11 | Instance in Secondary Network | Co-resident instance (possibly another tenant) | Secondary Network has **no** SG/NACL/Flow Logs; "logical isolation" only | Unsolicited east-west packet reaches a peer's secondary interface |
| B12 | L2 nested guest | L1 instance's IMDS / Nitro boundary | Nested-virt network path & hop-limit interaction undocumented | `curl 169.254.169.254` from L2 returns L1's instance-profile creds *(→ hard stop if it reaches Nitro)* |
| B13 | Any launch path (Fleet/Spot/ASG) | Account IMDSv2-enforcement guarantee | `CreateFleet`/`RequestSpotFleet`/`RequestSpotInstances` lack `ec2:MetadataHttpTokens`; ASG uses a parallel `autoscaling:*` key namespace | Instance launches with `HttpTokens=optional` despite the documented Deny policy |
| B14 | Attestable-AMI consumer | KMS key gated on a placeholder PCR | Doc example key policy uses all-zero `NitroTPMPCR12` | `Decrypt` succeeds for an instance whose measured PCR is unexpected/early-boot |
| B15 | Confused-deputy service provisioning "managed" instances | Owner's inventory + EventBridge detection | `ModifyManagedResourceVisibility=hidden` (default) suppresses list APIs **and** state-change events | Hidden attacker instance absent from `DescribeInstances` and no EventBridge event fires (CloudTrail still logs) |
| — | **any customer surface** | **AWS Nitro host / service fleet** | — | **Hard stop — preserve evidence, disclose** |

---

## 4. API / Interface Inventory (new / changed surface)

| API / field | Mutating | Ext-facing | New? | Authorized callers | Notes / condition-key gap |
|---|---|---|---|---|---|
| `EnableFastLaunch` (`--launch-template Version=$Latest\|$Default`) | Yes | Yes | changed Aug 2026 | AMI/LT holder | PassRole/RunInstances checked **once** via dry-run; no recheck at use-time |
| `CreateFleet Type=instant` overrides `IamInstanceProfile`/`KeyName`/`MetadataOptions` | Yes | Yes | NEW Jul 2026 | `ec2:CreateFleet` | Bypass LT object; `CreateFleet` omits `ec2:MetadataHttpTokens`/`HttpEndpoint`/`HttpPutResponseHopLimit` |
| `EC2FastLaunchFullAccess` (managed policy) | — | — | changed Aug 2026 | any attached principal | Unconditioned `RunInstances`+`PassRole`; `aws:RequestTag/CreatedBy` is self-asserted |
| `ModifyInstanceMetadataDefaults` / `GetInstanceMetadataDefaults` (`HttpTokensEnforced`) | Yes | Yes | NEW Feb 2026 | `ec2:ModifyInstanceMetadataDefaults` | Account-wide, no resource type; keys only `ec2:Attribute/${AttributeName}`,`ec2:Region` |
| `GetCapacityManagerMetricData` / `...MetricDimensions` / `EnableCapacityManager` | mixed | Yes | NEW Oct 2025 | `ec2:*CapacityManager*` | No account-scoping condition key; `Resource:"*"`; dimensions expose AccountID / Unused Financial Owner |
| `AssociateCapacityReservationBillingOwner` (+Accept/Reject/Disassociate) | Yes | Yes | 2024-25 | CR owner / assignee | **No condition key for the counterparty account**; same-payer/consumer check is server-side only |
| `CreateCapacityReservationBySplitting` / `MoveCapacityReservationInstances` | Yes | Yes | 2024 | same-account owner | Good hygiene: expose `ec2:Source/DestinationCapacityReservationId` keys |
| `CreateImageUsageReport` / `DescribeImageUsageReports`/`...Entries` | mixed | Yes | NEW Aug 2025 | ? (doc omits owner precondition) | `Describe*` entries have **no IAM resource type**, `ec2:Region` only |
| `DescribeImageReferences` + `AmazonEC2ImageReferencesAccessPolicy` | No | Yes | NEW Aug 2025 | policy holder | Policy stmt 1 = `Action:DescribeImageReferences, Resource:"*"`, **no Condition**; "regardless of who owns" |
| `AttachImageWatermark`/`DetachImageWatermark`, `ImageCriterion.ImageWatermarks[]`/`ImageNames` | Yes | Yes | NEW 2026 | AMI owner (attach) | Watermark tracks lineage not content; inheritance via `CreateImage` not owner-gated |
| `resolve:ssm:` / public SSM AMI parameter | No | Yes | NEW Jul 2026 | param readers | AWS-reserved `/aws/service/...` path is safe; customer paths depend on `ssm:PutParameter` scope |
| `ModifyInstanceConnectEndpoint` (SG/IP-type/PreserveClientIp) | Yes | Yes | NEW Aug 2025 | `ec2:ModifyInstanceConnectEndpoint` | SLR SG-attach stmt has no Condition; `OpenTunnel` conditions all optional |
| `CreateSecondaryNetwork` / `CreateSecondarySubnet` | Yes | Yes | NEW Feb 2026 | allow-listed | No SG/NACL/Flow Logs on the fabric; "multi-tenant / logical isolation" |
| `CreateReplaceRootVolumeTask` (existing-volume path) | Yes | Yes | NEW Jul 2026 | `ec2:CreateReplaceRootVolumeTask` | Blank condition-key column; no key ties `--volume-id` owner to the instance |
| `ModifyManagedResourceVisibility` / `GetManagedResourceVisibility` | Yes | Yes | NEW Apr 2026 | `ec2:Modify...` | Account-wide, blank condition keys; hidden ⇒ no EventBridge state-change events |
| `RunInstances`/`ModifyInstanceCpuOptions` `CpuOptions.NestedVirtualization` | Yes | Yes | NEW Feb 2026 | launcher | Silently disables Windows Credential Guard |
| KMS `kms:RecipientAttestation:NitroTPMPCR{4,7,12}`; `ec2:CpuOptionsAmdSevSnp` | — | Yes | NEW 2026 | key-policy author | NitroTPM gate exists; **no** SEV-SNP KMS condition key (self-service only) |

---

## 5. Recommended Areas of Focus (priority-ranked)

### Area 1 — EC2 Fast Launch & launch-template late-binding (PassRole bypass) — **TOP PRIORITY, AWS-planted**

**Background.** The single newest DocumentHistory entry (Aug 14 2026, "Permissions checks for EC2 Fast Launch") adds a
security consideration about `$Latest`/`$Default` launch-template versions. EC2 Fast Launch provisions instances using
its SLR after a *one-time* permission dry-run at enable time.

**Security Concern.** `win-fast-launch-configure.md` (lines 261-269) states verbatim: EC2 "checks your permissions
against the current launch template version… It does not recheck your permissions. As a result, someone who can update
the launch template could pass an IAM role or instance profile to an instance. This can happen even if they don't have
the `iam:PassRole` permission for that role." The mitigation offered is advisory/customer-side ("limit who can
`ec2:CreateLaunchTemplateVersion`/`ec2:ModifyLaunchTemplate`"). The SLR's own `AllowPassRole` statement is
`Resource:"*"` with only `iam:PassedToService: ec2.amazonaws.com`.

**High-level Test Scenarios.**
- **Lead 1.1 (Lens B/U, Critical).** Enable Fast Launch on an AMI with LT pinned to `$Latest`. As a second principal
  **lacking** `iam:PassRole` for role `R` but holding `ec2:CreateLaunchTemplateVersion`, publish a new default version
  setting `IamInstanceProfile=R`. Trigger provisioning. *Oracle:* the launched instance's IMDS yields `R`'s
  credentials. *Severity:* Critical if `R` is privileged (non-admin→admin).
- **Lead 1.2 (Lens R, Critical).** `EC2FastLaunchFullAccess` statement `EC2LaunchInstance` grants `ec2:RunInstances`
  on `image/*,key-pair/*,security-group/*,launch-template/*,subnet/*,network-interface/*,license-configuration/*`
  with **no Condition block**, and `IAMSLRPassRole` grants `iam:PassRole` on `role/*,instance-profile/*` gated only by
  `iam:PassedToService` — the classic `RunInstances`+`PassRole` privesc. The volume/instance statement is gated by
  `aws:RequestTag/CreatedBy` which is **caller-self-asserted**, not `aws:ResourceTag`. *Oracle:* `SimulatePrincipalPolicy`
  for a role holding only this policy returns `allowed` for `RunInstances`+`PassRole` on an admin profile with a
  `CreatedBy=EC2 Fast Launch` request tag. *Severity:* Critical.
- **Lead 1.3 (Lens S, High).** Instant-EC2-Fleet `MetadataOptions` override can set `HttpTokens=optional`;
  `CreateFleet`'s `instance*` resource type **omits** `ec2:MetadataHttpTokens`/`HttpEndpoint`/`HttpPutResponseHopLimit`
  (present on `RunInstances`). *Oracle:* under an SCP that denies `ec2:RunInstances` unless `MetadataHttpTokens=required`,
  `CreateFleet Type=instant` with `Overrides.MetadataOptions.HttpTokens=optional` still launches an IMDSv1-capable
  instance. *Severity:* High (IMDS weakening → SSRF-chained credential theft). Also test `KeyName` override to inject
  an attacker key pair.
- **Lead 1.4 (Lens EE, Medium / doc-gap).** Enabling Fast Launch on a *shared* (attacker-owned) AMI pre-provisions
  snapshots in the victim account by booting the AMI (Sysprep specialize + OOBE = code execution) under SLR privileges.
  Confirm whether specialize/OOBE-stage payloads persist into the reused snapshot. Bounded by victim opt-in → Medium.

**Doc evidence:** `win-fast-launch-configure.md`#win-fast-launch-permissions; `EC2FastLaunchFullAccess` /
`EC2FastLaunchServiceRolePolicy` JSON; `create-ec2-fleet.md`; `API_FleetLaunchTemplateOverridesRequest.md`;
`list_ec2.md` CreateFleet entry.

---

### Area 2 — IMDSv2-enforcement guarantee vs enforcement reality — **HIGH**

**Background.** Feb 2026 added account-level IMDSv2 enforcement (`HttpTokensEnforced`), on top of the existing per-
instance `HttpTokens`/hop-limit and the IAM condition keys. The documented promise is "instances can only launch if
they're configured to require IMDSv2."

**Security Concern.** The enforcement is implemented in several uncoordinated places with gaps between them.

**High-level Test Scenarios.**
- **Lead 2.1 (Lens U, High).** ASG pinned to `$Latest`/`$Default` is only permission-checked at ASG create/update, not
  per scale-out `RunInstances` (same shape as Fast Launch). *Oracle:* ASG with `HttpTokens=required`; publish a new
  default LT version with `HttpTokens=optional`; scale out → new instance is IMDSv1-capable. (`ExamplePolicies_EC2.md`
  lines 1690-1698.) *Severity:* High.
- **Lead 2.2 (Lens U/S, High).** `CreateFleet`/`RequestSpotFleet`/`RequestSpotInstances` lack the `ec2:MetadataHttpTokens`
  family of condition keys (confirmed absent in `list_ec2.md` 5113-5115, 9465-9467, 9477-9479). *Oracle:* apply the
  documented "Require IMDSv2" Deny (scoped to `ec2:RunInstances`), then call `RequestSpotInstances`/`CreateFleet` with
  `HttpTokens` unset → launch succeeds, Deny never matched. *Severity:* High.
- **Lead 2.3 (Lens U, High).** Auto Scaling uses a **separate** `autoscaling:MetadataHttpTokens` namespace
  (`list_autoscaling.md` 478); an SCP written only against `ec2:MetadataHttpTokens` is silently inert for ASG launches
  performed by the ASG SLR. *Severity:* High (plausible authoring mistake).
- **Lead 2.4 (Lens U, High).** `ModifyInstanceMetadataDefaults` is account-wide with condition keys only
  `ec2:Attribute/${AttributeName}` + `ec2:Region`. A principal with just that action (no `ec2:Attribute/HttpTokensEnforced`
  Deny) can flip `HttpTokensEnforced` back to `disabled`. *Oracle:* flip it, then `RunInstances HttpTokens=optional`
  succeeds. *Severity:* High (whole-account backstop removed with one write).
- **Lead 2.5 (Lens CC, High).** `ec2:RoleDelivery` (gates credential *use*, not retrieval) is never cross-referenced
  from the IMDSv2-enforcement docs. An org believing "IMDSv2 enforced" is covered may never deploy the `RoleDelivery<2.0`
  Deny, leaving IMDSv1-sourced creds (if ever obtained) fully usable. *Oracle:* on `HttpTokens=optional`, v1 fetch of
  `iam/security-credentials/<role>` succeeds; those creds call an API successfully **unless** the separate
  `RoleDelivery` Deny is attached. *Severity:* High.
- **Lead 2.6 (Lens CC, Medium).** `InstanceMetadataTags=enabled` exposes instance tags to any local/sidecar process via
  IMDS with no re-authorization — risky if an app trusts a tag (e.g. `Environment=prod`) for authz.

**Doc evidence:** `configuring-IMDS-new-instances.md`#enforce-imdsv2-at-the-account-level; `ExamplePolicies_EC2.md`
1683-1836; `list_ec2.md` 8856-8865; `list_autoscaling.md` 478; `work-with-tags-in-IMDS.md`.

---

### Area 3 — AMI governance, provenance & cross-account sharing — **HIGH**

**Background.** A dense 2024-2026 wave: AMI watermarks, Allowed AMIs (+ name/marketplace/age parameters), ancestry,
AMI references/usage reports + `DescribeImageReferences`, SSM-parameter AMI resolution, Block Public Access.

**Security Concern.** Governance claims ("restrict launches to only…", "enforce governance") and ownership-scoped
disclosure may not be enforced by the mechanism that actually resolves/returns the resource.

**High-level Test Scenarios.**
- **Lead 3.1 (Lens U, Critical).** Watermark persistence tracks *lineage*, not content: a derivative AMI built from a
  watermarked AMI inherits the watermark, and only *attach* (not inheritance) is owner-gated. *Oracle:* with launch
  access to one watermarked AMI, `CreateImage` a backdoored derivative; `describe-images` shows the inherited
  `ImageWatermarks`; it passes a victim's watermark-only `ImageCriterion` (`ImageAllowed:true`). *Severity:* Critical
  (cross-account governance bypass).
- **Lead 3.2 (Lens EE/U, High — whoAMI class).** `ImageNames`-only Allowed-AMIs criteria have no owner binding (AWS's
  own best-practice warns to pair with `ImageProviders`). *Oracle:* register/copy an AMI whose name matches the victim's
  pattern; confirm `ImageAllowed:true`. Also test over-broad `ssm:PutParameter` on a customer `resolve:ssm:/golden-ami`
  path pointing to an attacker AMI. *Note:* the AWS-reserved `/aws/service/...` public-parameter path is **not**
  writable → that specific whoAMI vector is refuted.
- **Lead 3.3 (Lens A, High).** `CreateImageUsageReport`/`DescribeImageUsageReportEntries` lack a documented owner
  precondition (contrast `ami-last-launched-time.md` which explicitly requires ownership); the `Describe*` entries have
  **no IAM resource type**. *Oracle:* as an account merely *shared* an AMI, create a usage report and read other
  accounts' identifiers for that AMI. *Severity:* High (cross-tenant business-data disclosure).
- **Lead 3.4 (Lens A/R, Medium→Critical).** `AmazonEC2ImageReferencesAccessPolicy` stmt 1 =
  `Action:ec2:DescribeImageReferences, Resource:"*"` with **no Condition**. *Oracle:* call
  `describe-image-references --image-ids <foreign AMI>`; test whether nonexistent vs real-but-foreign AMI ids differ in
  response → a cross-account existence oracle for private AMI ids. *Severity:* Critical if the oracle confirms, else
  Medium.
- **Lead 3.5 (Lens X, High).** AMI-layer gates (Allowed AMIs, Block Public Access, watermark, disable) attach to the
  `image` resource type; the backing EBS **snapshot** is a separate `snapshot` resource. *Oracle:* with snapshot-level
  `CreateVolumePermission`/`ebs:GetSnapshotBlock` (commonly granted to enable cross-account copy), read disk blocks via
  `ebs:GetSnapshotBlock`/`CopySnapshot` even though the AMI is Allowed-AMIs-blocked/disabled. *Severity:* High.
- **Lead 3.6 (Lens AA, Critical).** Fast Launch on a shared AMI creates pre-provisioned snapshots **in the consumer's
  account**, outside the AMI's `launchPermission` ACL. *Oracle:* enable Fast Launch, let snapshots provision, have owner
  revoke the share → consumer-account snapshots survive and `create-volume` from them still works (esp. via a Recycle
  Bin retention rule). *Severity:* Critical (persistent cross-account retention of proprietary image content after
  revoke).
- **Lead 3.7 (Lens X, doc-gap→High).** Confirm Allowed-AMIs/BPA enforcement parity across `RunInstances`, `CreateFleet`,
  `RequestSpotInstances`, Auto Scaling — any unenforced launch path is a governance hole.

**Doc evidence:** `ami-watermark.md`; `ec2-allowed-amis.md`; `your-ec2-ami-usage.md`; `ec2-ami-references.md`;
`AmazonEC2ImageReferencesAccessPolicy` JSON; `sharingamis-explicit.md`; `win-ami-config-fast-launch.md`;
`using-systems-manager-parameter-to-find-AMI.md`.

---

### Area 4 — Connectivity & network boundary (EICE, Secondary Networks, root-volume swap, visibility) — **HIGH**

**Background.** EICE modify/IPv6 + managed-policy update, Secondary Networks, root-volume replace with an existing EBS
volume, managed-resource visibility.

**High-level Test Scenarios.**
- **Lead 4.1 (Lens B10, Critical).** `CreateReplaceRootVolumeTask` existing-volume path has a blank condition-key column
  and no documented owner check tying `--volume-id` to the instance; the instance's IAM profile persists through the
  swap. *Oracle:* with `ec2:CreateReplaceRootVolumeTask` on a privileged instance A and an attacker-prepared available
  volume in the same AZ, swap it in → attacker disk boots carrying A's instance-profile creds. *Severity:* Critical
  (intra-account role theft; cross-account variant gated on whether shared volume ARNs are accepted — lower confidence).
  Note: the snapshot/AMI paths **do** require resource-level permissions → null for those.
- **Lead 4.2 (Lens V, High-Critical).** EICE: route tables may allow the endpoint "to connect to any instance in any
  subnet of the VPC"; endpoint-SG inbound rules are irrelevant ("use an IAM policy"); the `OpenTunnel`
  `privateIpAddress`/`remotePort` conditions are *optional* and the docs offer `Resource:"*"` as a valid simple policy.
  *Oracle:* grant `OpenTunnel Resource:"*"` with no address/port condition; tunnel to a second, unrelated instance/port
  in the VPC. *Severity:* High-Critical (lateral pivot across security zones).
- **Lead 4.3 (Lens S/R, Medium-High).** EICE SLR statement `ec2:ModifyNetworkInterfaceAttribute` on `security-group/*`
  has **no** Condition (every sibling ENI statement is `StringLike aws:ResourceTag/InstanceConnectEndpointId:eice-*`).
  *Oracle:* with only `ec2:ModifyInstanceConnectEndpoint`, call `modify-instance-connect-endpoint --security-group-ids
  <SG not owned/tagged by EICE>` → SLR attaches it. *Severity:* Medium-High (confused-deputy SG expansion of the proxy).
  *(The Null→StringLike operator swap itself is refuted as a fail-open — all patterns are anchored `eice-*`.)*
- **Lead 4.4 (Lens V/D, doc-gap→Critical).** Secondary Networks have no SG/NACL/Flow Logs; "multi-tenant with logical
  isolation" is unexplained. *Oracle:* two instances in the same secondary subnet → attempt unsolicited east-west; if a
  cross-tenant subnet-sharing model exists, reachability = unlogged cross-tenant pivot. Gated on feature access →
  confirm surface first.
- **Lead 4.5 (Lens O/U, Medium-High).** `ModifyManagedResourceVisibility=hidden` (default) suppresses list APIs **and**
  `EC2 Instance State-change Notification` EventBridge events, while CloudTrail + billing remain intact. *Oracle:*
  provision a managed instance via a confused-deputy service under default-hidden; confirm it's absent from
  `describe-instances` and no EventBridge rule fires, yet CloudTrail logs it. *Severity:* Medium baseline → High when it
  hides an attacker-created resource from the owner's inventory/automation.

**Doc evidence:** `replace-root.md`; `connect-with-ec2-instance-connect-endpoint.md`; `eice-security-groups.md`;
`Ec2InstanceConnectEndpoint` JSON; `secondary-networks.md`; `amazon-ec2-managed-instances.md`.

---

### Area 5 — Capacity Reservations / Blocks / Capacity Manager (cross-account sharing & billing) — **HIGH**

**Background.** Cross-account/cross-org sharing of CRs and Capacity Blocks, billing-ownership transfer, split/move, and
the brand-new EC2 Capacity Manager (org-wide aggregation + new SLR).

**High-level Test Scenarios.**
- **Lead 5.1 (Lens A, Critical).** `GetCapacityManagerMetricData`/`...MetricDimensions` have no account-scoping
  condition key (`Resource:"*"`, `ec2:Region` only), and the SLR auto-deploys into every member account. Dimensions
  include `AccountID`, `AccountName`, "Unused Financial Owner". *Oracle:* in a 3-account org, grant a *plain* member
  (not mgmt, not DA) the two read actions; query filtered by another account's `AccountID`; if sibling data returns →
  cross-account IDOR. *Severity:* Critical. **Highest-value, cheapest test.**
- **Lead 5.2 (Lens S, Critical-if-true).** The billing-assignment actions
  (`AssociateCapacityReservationBillingOwner` etc.) have **no condition key for the counterparty account** (unlike
  split/move which expose source/dest CR id keys). CRs can be shared *outside* the org, but billing assignment requires
  "same Organizations payer" — enforced only server-side. *Oracle:* attempt `AssociateCapacityReservationBillingOwner`
  to an out-of-org RAM consumer; success = cross-payer billing takeover. Also test assignment to a non-consumer account.
- **Lead 5.3 (Lens AA, High).** Owner can unilaterally cancel a future-dated CR whose billing was accepted by another
  account; "the assigned billing owner pays the cancellation charges" with no consent gate exposed to the payer.
  *Oracle:* set up the assignment, cancel, confirm the assignee's CUR shows the charge and no accept/reject was offered.
  *Severity:* High (unconsented cost injection). The cancellation itself is normal; the third-party cost-shift is the bug.
- **Lead 5.4 (Lens AA, Medium-High).** Mid-flight race: between `Associate...BillingOwner` and the assignee's accept
  (up to 12h), un-share the CR from that consumer via RAM, then accept → billing stranded to a now-non-consumer account?
- **Lead 5.5 (Lens L, High / partially out-of-scope).** Shared placement-group + CR (`cr-cpg.md`) lets unrelated tenant
  accounts create CRs in the same physical PG → co-location side channel and capacity starvation of a sibling tenant.
  (Pure FCFS/interruption behavior is **out-of-scope product behavior** — only the co-tenant starvation is a boundary.)
- **Lead 5.6 (Lens R).** `AWSEC2CapacityManagerServiceRolePolicy` grants `organizations:ListAccounts`/`ListChildren`/
  `DescribeOrganization` unconditionally on `Resource:"*"` while being deployed into every member account — a
  broad org-recon primitive if any member's SLR were ever confused. *(The `AWSEC2CapacityReservationFleetRolePolicy`
  `StringLike→ArnLike` change is a hardening, not a gap — null.)*

**Doc evidence:** `capacity-manager.md`; `enable-capacity-manager-organizations.md`; `cm-metrics-units.md`;
`assign-billing.md`; `request-billing-transfer.md`; `capacity-reservation-sharing.md`; `capacity-blocks-share.md`;
`cr-cpg.md`; `AWSEC2CapacityManagerServiceRolePolicy` JSON; `list_ec2.md`.

---

### Area 6 — Confidential compute & attestation (NitroTPM / SEV-SNP / nested virtualization) — **MEDIUM-HIGH**

**High-level Test Scenarios.**
- **Lead 6.1 (Lens W, Critical-if-present).** The doc example KMS key policy uses an **all-zero** `NitroTPMPCR12` value
  (`prepare-attestation-service.md` line 38). *Oracle:* survey authorized key policies for literal all-zero
  `NitroTPMPCR{4,7,12}` never replaced with real measurements → the gate matches any unmeasured/early-boot instance
  (fail-open). Also: the documented 4-step Attestation-Document validation omits nonce-freshness and PCR-sanity checks →
  self-built verifiers following it are replay/fail-open prone. *Severity:* Critical / High.
- **Lead 6.2 (Lens V/D, doc-gap→Critical).** Nested virtualization's L1↔L2 network path and IMDS/hop-limit interaction
  is entirely undocumented. *Oracle:* from an L2 guest on a nested-virt instance, `curl 169.254.169.254/latest/meta-data/`
  and test hop-limit=1 vs 2. L2 reaching L1's instance-profile creds = Critical; **hard stop** if it reaches the Nitro
  boundary. Confirm surface first.
- **Lead 6.3 (Lens U, High).** Enabling nested virtualization **silently disables Windows Credential Guard** (VSM) with
  no EC2 notification/CloudTrail field/console warning. *Oracle:* verify Credential Guard `Running`, call
  `ModifyInstanceCpuOptions --nested-virtualization enabled` (stop/start), re-check → not running. *Severity:* High
  (loosely-permissioned API silently removes an advertised credential-theft defense).
- **SEV-SNP:** has **no** AWS-mediated attestation gate (no KMS condition key) — customer-side trust only → any
  fail-open is a customer app bug, **not** an AWS boundary bug. Marked null/doc-gap, not a finding.

**Doc evidence:** `prepare-attestation-service.md`; `nitrotpm-attestation-document-validate.md`;
`amazon-ec2-nested-virtualization.md`; `credential-guard.md`; `sev-snp.md`; `snp-attestation.md`.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation being attacked |
|---|---|---|
| PassRole bypass via `$Latest`/`$Default` re-resolution | Fast Launch SLR / ASG | "EC2 checks your permissions" (one-time dry-run only) |
| Non-admin→admin via managed policy | `EC2FastLaunchFullAccess` | Policy name/description implies Fast-Launch-only scope |
| IMDSv1 re-enablement under enforcement | CreateFleet/Spot/ASG/MetadataDefaults | Account-level IMDSv2 enforcement "regardless of config" |
| Cross-account telemetry read | EC2 Capacity Manager | Org trusted-access + delegated-admin model |
| Unconsented billing cost-shift | CR billing assignment | "assigned billing owner pays cancellation charges" |
| Cross-tenant AMI customer-list disclosure | AMI usage reports / DescribeImageReferences | Implied owner-only visibility |
| Governance bypass via snapshot cousin | Allowed AMIs/BPA vs `ebs:*` | "Instances can only be launched using allowed AMIs" |
| Watermark governance bypass via lineage inheritance | AMI watermarks + Allowed AMIs | "enforce governance… restrict to approved watermarks" |
| Role theft via root-volume swap | CreateReplaceRootVolumeTask | Resource-level IAM on snapshots/AMIs (absent on existing-volume path) |
| EICE lateral pivot | EICE tunnel | IAM `OpenTunnel` conditions (optional) + SG/route table |
| Attestation fail-open | NitroTPM/KMS key policy | `kms:RecipientAttestation:NitroTPMPCR*` gate |
| Nested-guest IMDS reach | Nested virtualization | "Nitro System strong isolation boundaries" (generic) |
| Detection evasion | Managed-resource visibility | "do not affect… actual access" (but suppresses EventBridge) |

---

## 7. Out-of-Scope Risk Categories (state as confidently as in-scope)

- A customer reading **their own** instance's IMDS / user-data / role credentials via the documented flow — intended.
- AWS-internal **Nitro hypervisor / SEV-SNP firmware / host-fleet** implementation correctness — no doc visibility,
  **hard stop** if ever reached.
- Pure **FCFS capacity contention / interruptible-CR reclamation** — documented product semantics (only *cross-tenant
  starvation on a shared PG* is in scope).
- **Capacity Block "stop sharing" grace window** (running instances continue until ~30 min before expiry) — disclosed.
- Serial Console bypassing SG/NACL — documented OOB design.
- **Customer-authored** least-privilege footguns (over-broad `ssm:PutParameter`, over-granted `CreateReplaceRootVolumeTask`)
  — config-review leads, not AWS defects. *(Carve-out: the AWS-**authored** managed policies in Leads 1.2, 4.3, 5.6 are
  in scope and reportable — Tier 2, route `aws-security`.)*
- SEV-SNP attestation trust built by a customer app — bespoke, customer-owned.
- DNS rebinding against private-only endpoints; IMDS on fully-managed hosts the customer doesn't control.

---

## 8. Null Hypotheses / Doc Gaps (surfaces checked that did not fire, or need confirmation first)

- **WatermarkKey account-ID spoofing** — refuted; the account-ID portion is service-assigned at attach (`ami-watermark.md`).
  The real break is lineage inheritance (Lead 3.1).
- **AWS-reserved public SSM parameter spoofing** (`/aws/service/ami-*-latest/...`) — refuted; AWS-owned namespace, not
  writable (`finding-an-ami-parameter-store.md`).
- **Null→StringLike swap in `Ec2InstanceConnectEndpoint`** — refuted as a live fail-open; patterns anchored `eice-*`.
  Standing oracle: watch for any future managed-policy edit using unanchored `StringLike "*"` in place of a `Null`
  presence check.
- **`AWSEC2CapacityReservationFleetRolePolicy` StringLike→ArnLike** — hardening, not a gap.
- **Capacity split/move cross-account leak** — null; both require same-account ownership (`capacity-reservations-move.md`).
- **Capacity Block out-of-org sharing** — null; org-only by design.
- **IMDS IPv6 endpoint as a tokens/hop-limit bypass** — null; inherits the same `MetadataOptions`.
- **DescribeInstanceTypes vs capability-table drift** (SEV-SNP / nested-virt / Credential Guard) — null; the API is the
  authoritative source, no second static table exists.
- **Root-volume replace via snapshot/AMI path** — null; those paths require resource-level IAM (only the existing-volume
  path has the gap, Lead 4.1).
- **Managed-resource visibility affecting billing/CloudTrail** — null; explicitly unaffected (only EventBridge is).
- **SEV-SNP ↔ KMS attestation gate** — doc-gap; no SEV-SNP KMS condition key exists in this corpus → out of scope as an
  AWS boundary unless one is found elsewhere.
- **Doc-gaps requiring live surface confirmation first:** Secondary Networks cross-tenant subnet-sharing model (Lead 4.4);
  nested-virt L1↔L2 IMDS reachability (Lead 6.2); EICE/Serial-Console WebSocket TLS floor & token replay-resistance;
  Org/OU share-target validation-at-grant for AMI `launchPermission`; interruptible-CR reclaim effect on an active
  billing assignment; whether Allowed-AMIs/BPA enforcement is uniform across all launch APIs (Lead 3.7).

---

### Prioritized hunter work queue (first ten)
1. **Lead 5.1** — Capacity Manager cross-account `GetCapacityManagerMetricData` IDOR (cheapest, Critical).
2. **Lead 1.1 / 1.2** — Fast Launch `$Latest` PassRole bypass + `EC2FastLaunchFullAccess` privesc (AWS-planted, Critical).
3. **Lead 4.1** — `CreateReplaceRootVolumeTask` role theft via volume swap (Critical).
4. **Lead 3.6** — Fast Launch shared-AMI snapshot survival after unshare (Critical).
5. **Lead 3.1** — watermark lineage-inheritance governance bypass (Critical).
6. **Lead 5.2** — out-of-org `AssociateCapacityReservationBillingOwner` cross-payer (Critical-if-true).
7. **Lead 2.2 / 2.4** — Fleet/Spot IMDSv2 condition-key gap + `ModifyInstanceMetadataDefaults` single-write disable (High).
8. **Lead 4.2** — EICE unconditioned `OpenTunnel` lateral pivot (High-Critical).
9. **Lead 3.5** — Allowed-AMIs/BPA bypass via `ebs:GetSnapshotBlock` snapshot cousin (High).
10. **Lead 6.2** — nested-guest IMDS reach (Critical; **hard stop** on Nitro reach) — confirm surface first.

*End of plan. Documentation-derived hypotheses only — no live testing performed.*
