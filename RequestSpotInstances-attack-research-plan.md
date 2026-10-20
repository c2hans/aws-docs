# RequestSpotInstances (EC2 Spot Instances) — Attack Research Plan

Source of leads:
- Target page: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RequestSpotInstances_section.html (SDK/CLI code example) — local: `docs/ec2/latest/devguide/example_ec2_RequestSpotInstances_section.md`
- API reference: `docs/AWSEC2/latest/APIReference/API_RequestSpotInstances.md`, `API_RequestSpotLaunchSpecification.md`, `API_IamInstanceProfileSpecification.md`, `API_CreateSpotDatafeedSubscription.md`, `API_SpotInstanceRequest.md`
- IAM authorization reference: `docs/service-authorization/latest/reference/list_ec2.md` (the decisive artifact — RequestSpotInstances ~line 9477 vs RunInstances ~line 9585)
- User Guide: `docs/AWSEC2/latest/UserGuide/service-linked-roles-spot-instance-requests.md`, `spot-fleet-prerequisites.md`, `spot-data-feeds.md`, `spot-requests.md`

Status: **documentation-derived hypotheses only; nothing tested against a live account.** Online and offline docs were cross-read (offline mirror + docs.aws.amazon.com `.md`).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 ordering). Look left and right for adjacent bugs.
- The cheapest, safest first oracle for every IAM lead here is **`iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy`** — it touches no resources. Escalate to a live scoped call only with synthetic canary data, under a role holding *exactly* the policy under test (never the over-privileged tester).
- **DryRun is caller-IAM-only, NOT an ownership oracle** (evaluated before resource resolution). Do not use `DryRun` to decide cross-account/ownership questions — it is a documented false-positive trap.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. "the AWS data feed account", the Spot fleet control plane), stop, preserve evidence, flag for AWS-Security disclosure. Do not exploit beyond existence.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Launch-guardrail bypass:** From an IAM principal whose `RunInstances` is constrained by condition keys (`ec2:InstanceProfile`, `ec2:MetadataHttpTokens`, `ec2:Tenancy`, `ec2:Encrypted`, `ec2:AssociatePublicIpAddress`), launch an instance via `RequestSpotInstances` with a configuration the `RunInstances` policy would deny — proving the legacy Spot path is not covered by the same condition keys.
2. **PassRole escalation:** Attach a more-privileged instance profile to a Spot instance than the caller could attach via a condition-key-pinned `RunInstances`, then recover that role's credentials from the instance (IMDS) to escalate.
3. **Cross-account data-feed / S3 trust break:** Abuse the Spot data-feed → S3 ACL mechanism (survives subscription deletion; keyed on FULL_CONTROL not ownership) to read or write across an account boundary, or leave a stale AWS-data-feed-account grant.
4. **Spot-request IDOR:** Read or cancel another account's Spot Instance request by naming its `sir-…` identifier directly.
5. **SLR over-privilege:** Show `AWSServiceRoleForEC2Spot` / `AWSServiceRoleForEC2SpotFleet` / `aws-ec2-spot-fleet-tagging-role` grant more than their stated purpose (e.g. account-wide Stop/StartInstances, over-broad KMS `CreateGrant`).

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 Query/SigV4 API `RequestSpotInstances` (endpoint `ec2.<region>.amazonaws.com`), plus CLI `aws ec2 request-spot-instances` and PowerShell `Request-EC2SpotInstance`. **This API is explicitly LEGACY** — the API reference states: *"We strongly discourage using the RequestSpotInstances API because it is a legacy API with no planned investment."* That sentence is the single most important design fact: a launch path that still fully works but receives no security investment, and (Section 3) carries a narrower IAM condition-key surface than its modern twin `RunInstances`.

**What a request does.** Creates a *Spot Instance request* resource (`sir-…`); when the request is fulfilled, EC2 launches one or more EC2 instances using the embedded `LaunchSpecification`. The launched instances are ordinary customer-account EC2 instances — there is **no AWS multi-tenant service fleet** hosting customer workloads here (unlike CloudShell/DocumentDB). The shared surface is the **EC2 control plane** and the **Spot market/fulfilment plane**, plus the **"AWS data feed account"** (a named AWS-owned principal) in the data-feed feature.

**The launch specification (`RequestSpotLaunchSpecification`)** — every field is customer-controlled input that becomes instance configuration:
- `IamInstanceProfile` (`Arn` or `Name`) — **PassRole seam**: the role whose credentials the instance (and anyone who reaches its IMDS) will hold.
- `ImageId` — AMI id (raw id, not a name-based lookup in this API).
- `UserData` — base64, ≤16 KB — boot script; reaches the instance and can read instance-profile creds from IMDS.
- `BlockDeviceMapping.N` — `SnapshotId` + `Encrypted` + `KmsKeyId` (snapshot/KMS seam).
- `NetworkInterface.N` — incl. `AssociatePublicIpAddress: true` (seen in the CLI example), `SubnetId`, `Groups`.
- `SecurityGroupId.N`, `SubnetId`, `KeyName`, `Monitoring`, `Placement` (`SpotPlacement`: AZ, Tenancy), `KernelId`, `RamdiskId`, `InstanceType`.
- Top-level: `InstanceCount`, `SpotPrice`, `Type` (one-time|persistent), `InstanceInterruptionBehavior`, `TagSpecification.N` (only `spot-instances-request` ResourceType allowed), `ValidFrom/Until`, `ClientToken`, `DryRun`.

**Identity / roles.**
- Caller: SigV4 IAM principal with `ec2:RequestSpotInstances` (+ `iam:PassRole` if a profile is passed).
- `AWSServiceRoleForEC2Spot` (SLR, trust `spot.amazonaws.com`): documented actions `ec2:DescribeInstances`, `ec2:StopInstances`, `ec2:StartInstances`; may hold a KMS grant (Decrypt/Encrypt/GenerateDataKey*/CreateGrant/DescribeKey/ReEncrypt*) for encrypted-AMI/EBS launches.
- `AWSServiceRoleForEC2SpotFleet` (trust `spotfleet.amazonaws.com`) and `aws-ec2-spot-fleet-tagging-role` (Spot Fleet only).
- "**AWS data feed account**" — an AWS-owned S3 principal granted FULL_CONTROL on the customer's data-feed bucket via ACL.

**ASCII pipeline**
```
Caller (IAM principal)
   │  ec2:RequestSpotInstances  (+ iam:PassRole on IamInstanceProfile)
   ▼
EC2 control plane ── authz check (resource types: image, key-pair, network-interface,
   │                 placement-group, security-group, snapshot, spot-instances-request*, subnet)
   │                 ★ NO `instance` or `volume` resource type (see §3) ★
   ▼
Spot market / fulfilment  ──uses──► AWSServiceRoleForEC2Spot ──(KMS grant)──► customer CMK
   ▼
Launched EC2 instance (customer account)
   ├── IamInstanceProfile role creds reachable via IMDS  ◄── UserData runs here
   └── EBS volumes (from BlockDeviceMapping / AMI snapshots, possibly CMK-encrypted)

Billing: Spot usage ──► "AWS data feed account" ──(bucket ACL FULL_CONTROL)──► customer S3 bucket
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller with condition-key-scoped `RunInstances` | Instance config controls (IMDS/profile/tenancy/encryption/public-IP) | `RequestSpotInstances` legacy launch path | A Spot launch produces an instance config that a correctly-scoped `RunInstances` policy denies → **guardrail bypass = breach** |
| Caller | Any passable IAM role (instance-profile) | `IamInstanceProfile` + `iam:PassRole` | Attaching, via Spot, a role that `ec2:InstanceProfile`-pinned `RunInstances` would refuse → **privilege boundary breach** |
| Caller's account | Another account's Spot request | `sir-…` id supplied to Describe/Cancel | Reading/cancelling a request not owned by the caller → **cross-account breach** |
| Customer | Another account's S3 bucket | `CreateSpotDatafeedSubscription` Bucket (FULL_CONTROL, not ownership) | Feed delivered to / ACL mutated on a bucket the caller does not own → **cross-account breach** |
| Customer (after unsubscribe) | "AWS data feed account" grant on bucket | ACL left in place on `DeleteSpotDatafeedSubscription` | A surviving AWS-principal write grant after revoke → **revocation-completeness breach** |
| Spot fulfilment plane | Customer CMK | KMS grant to `AWSServiceRoleForEC2Spot` | SLR performing KMS ops (esp. `CreateGrant`) beyond launch need → **over-privilege** |
| **Any customer surface** | **AWS's own service plane** (data-feed account, Spot control plane) | server-side identities | **any AWS-fleet identity/credential/ARN = HARD STOP, disclose** |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Ext-facing? | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| RequestSpotInstances | SigV4/Query | **Existing / LEGACY ("no planned investment")** | Mutating | External | Create Spot request → launch instances | Yes | principal w/ `ec2:RequestSpotInstances` (+`iam:PassRole`) | **Narrower condition-key surface than RunInstances (§3, Area 1). Prime lead.** |
| RunInstances | SigV4 | Existing | Mutating | External | Launch instances (modern) | Yes | principal w/ `ec2:RunInstances` | Comparison baseline — supports `instance*`+`volume` resource types |
| RequestSpotFleet | SigV4 | Existing | Mutating | External | Launch a Spot fleet (launch-template path) | Yes | principal + fleet roles | Check parity restoration (Area 1 task 2) |
| DescribeSpotInstanceRequests | SigV4 | Existing | Non-mut | External | Read Spot requests | Yes | account principals | IDOR / id-enumeration target (Area B) |
| CancelSpotInstanceRequests | SigV4 | Existing | Mutating | External | Cancel Spot requests by `sir-…` | Yes | account principals | IDOR target (Area B) |
| CreateSpotDatafeedSubscription | SigV4 | Existing | Mutating | External | Subscribe billing feed → S3 | Yes | account principals | S3 ACL trust; one-per-account (Area B) |
| DeleteSpotDatafeedSubscription | SigV4 | Existing | Mutating | External | Delete feed sub | Yes | account principals | **Does not revoke bucket grant** (Area B) |
| DescribeSpotDatafeedSubscription | SigV4 | Existing | Non-mut | External | Read feed sub | Yes | account principals | info-leak check |
| DescribeSpotPriceHistory | SigV4 | Existing | Non-mut | External | Market price history | Yes | account principals | low-sensitivity |

**Undocumented/hidden-knob sweep:** `RequestSpotLaunchSpecification` exposes `KernelId`, `RamdiskId`, `AddressingType` (Deprecated), `BlockDurationMinutes` (Deprecated), `SecurityGroup.N` (marked "Not supported") — legacy/deprecated fields still accepted by the model. Flag any that weaken isolation or that the console cannot set (delta = lead).

---

## 5. Recommended Areas of Focus

Ordering rationale (Step 5): the **legacy-vs-modern condition-key parity gap (Area 1)** is first — it is a concrete, doc-provable enforcement delta on a mutating external launch API, it enables PassRole escalation, and the legacy API by definition has "no planned investment" (least review). Cross-account data-feed (Area 3) and IDOR (Area 4) follow as cross-boundary leads; SLR/KMS (Area 5) and launch-spec content (Area 6) round out coverage.

### Area 1 — Legacy-vs-modern launch-authorization parity (PRIMARY) — Lenses X, U, S
Background: `RequestSpotInstances` and `RunInstances` are two launch twins. In `list_ec2.md`, `RunInstances` (L9585–9609; `instance*` at L9591, `volume` at L9603) carries an `instance*` resource type (rich key set) and a `volume` resource type; `RequestSpotInstances` (L9477–9487) carries **neither**. It supports only image, key-pair, network-interface, placement-group, security-group, snapshot, subnet, and the required `spot-instances-request` (tag-on-create keys only). **Confirmed in deep-dive: `RequestSpotFleet` (L9465–9475) has the same gap** — both *legacy* Spot launch APIs lack `instance`/`volume`. The modern **`CreateFleet`** path *restores* `instance*`/`volume` condition keys (L5118, L5122) and explicitly documents (L5114) that launch-template-sourced resources must be covered by a companion `RunInstances` policy statement — so the gap is **legacy-specific**, and `RequestSpotFleet` is arguably worse than `CreateFleet` (neither the keys nor the documented workaround, despite also accepting launch templates).

Security Concern: Admin guardrails written against `RunInstances` condition keys are **silently not enforced** on the legacy Spot launch path, even though the Spot launch spec accepts all the corresponding settings. Confirmed-missing-and-impactful keys (full table in `_spot_research/fragment_A_iam_parity.md` after deep-dive):
- `ec2:InstanceProfile` (restricts which instance profile may be attached) — **absent on Spot path** → PassRole-pinning bypass (chains to Area 2).
- `ec2:MetadataHttpTokens` / `ec2:MetadataHttpEndpoint` / `ec2:MetadataHttpPutResponseHopLimit` / `ec2:InstanceMetadataTags` — **absent** → an org that *mandates IMDSv2 / hop-limit 1* via RunInstances cannot enforce it on Spot-launched instances (SSRF-to-IMDS exposure).
- `ec2:Tenancy` — absent → dedicated/host-tenancy pinning bypass.
- `ec2:Encrypted` / `ec2:VolumeType` / `ec2:VolumeSize` (volume type absent) → cannot require encrypted EBS on Spot launches.
- `ec2:AssociatePublicIpAddress` (present on RunInstances' network-interface, **absent** on Spot's) → a "no public IP" guardrail is bypassable; the CLI example literally sets `AssociatePublicIpAddress: true`.

High-level Test Scenarios (falsifiable claims):
- **Claim:** A principal denied `RunInstances` unless `ec2:MetadataHttpTokens == required` can launch an **IMDSv1** instance via `RequestSpotInstances`. → **Mechanism:** `list_ec2.md:9479-9486` (no `instance` type on RequestSpotInstances) vs `:9591` (`ec2:MetadataHttpTokens` under RunInstances' `instance*`). → **Oracle:** `SimulatePrincipalPolicy` for `ec2:RequestSpotInstances` returns `allowed` regardless of the metadata condition; live, the Spot instance comes up with IMDSv1 enabled. → **Pre:** a policy using these keys. → **Sev:** High.
- **Claim:** A principal pinned by `ec2:InstanceProfile` on RunInstances can attach a *different, more privileged* profile via the Spot path. → chains to Area 2. → **Sev:** High–Critical.
- **Claim:** A "no public IP" / "encrypted EBS only" guardrail is bypassed via Spot. → **Oracle:** Spot request with `AssociatePublicIpAddress:true` / unencrypted volume succeeds where RunInstances is denied. → **Sev:** Medium–High.
Doc evidence: `list_ec2.md` lines 9477-9488 vs 9585-9604; API note "legacy API … no planned investment". Severity-if-true: **High** (guardrail/SCP-adjacent bypass).

### Area 2 — PassRole / instance-profile escalation via the Spot path — Lenses B, E
Background: The launch spec passes `IamInstanceProfile` to the instance; `iam:PassRole` is required (`spot-fleet-prerequisites.md:91`). But `ec2:InstanceProfile` — the key that scopes *which* profile — hangs off the `instance` resource type that this API lacks (Area 1).
Security Concern: If `iam:PassRole` is scoped broadly (e.g. `Resource: arn:aws:iam::*:role/*` or a wide prefix), a caller can attach **any** passable role to a Spot instance and then read its credentials from IMDS — a classic launch-to-privesc, with the EC2-side `ec2:InstanceProfile` backstop unavailable on this path.
High-level Test Scenarios:
- **Claim:** With broad `iam:PassRole` but RunInstances pinned to one profile via `ec2:InstanceProfile`, a Spot launch attaches an admin profile. → **Oracle:** request succeeds; IMDS on the instance yields the admin role's creds. → **Sev:** High–Critical (self-escalation to the passed role's privilege).
- **Claim (non-PassRole twin, per Variant coverage):** enumerate whether `ec2:ModifyInstanceAttribute(userData)` or launch-template `$Latest`/`$Default` late-binding can reach a Spot instance's role indirectly. → **Sev:** High.
Doc evidence: `API_IamInstanceProfileSpecification.md`; `spot-fleet-prerequisites.md:86,91`; `list_ec2.md:9591` (`ec2:InstanceProfile`).

### Area 3 — Spot data feed → S3 trust & revocation completeness — Lenses AA, T, EE, A
Background: `CreateSpotDatafeedSubscription` delivers billing files to a customer-named S3 bucket, and **updates the bucket ACL to grant the "AWS data feed account" FULL_CONTROL**. The caller only needs **FULL_CONTROL on the bucket** (not ownership). One feed per account. Delete does **not** remove the AWS-account grants.
Security Concern (verbatim doc): *"If you delete your data feed subscription, Amazon EC2 doesn't remove the read and write permissions for the AWS data feed account … You must remove these permissions yourself."* → a surviving AWS-principal write grant (revocation incompleteness). Plus: FULL_CONTROL-not-ownership may allow pointing the feed at a bucket in another account.
High-level Test Scenarios: *(developed in `_spot_research/fragment_B_datafeed_idor.md`)*
- **Claim:** Feed can be subscribed to a bucket the caller only holds FULL_CONTROL on in another account; EC2 writes customer billing data there. → **Oracle:** feed files land cross-account; ACL mutated cross-account. → **Sev:** Medium–High. **HARD STOP if the write identity is the AWS data feed account reaching outside intended scope.**
- **Claim:** After `DeleteSpotDatafeedSubscription`, the AWS-data-feed-account grant persists and a later unrelated subscription (same or different account) can still write. → **Oracle:** ACL still lists the AWS principal post-delete. → **Sev:** Medium (AA revocation gap).
- **Open design question (deep-dive):** docs never state whether "the AWS data feed account" is **one shared principal** whose per-tenant write-isolation depends on undocumented server-side routing, or a per-subscription-scoped credential. If shared, the surviving grant (above) is a lever to probe cross-tenant write isolation of that principal. → **HARD STOP** the instant evidence implicates that AWS-owned principal reaching another tenant — preserve and disclose.
- **Claim:** The predictable path `{bucket}/{prefix}/{aws-account-id}.{date}…` enables cross-account confusion / enumeration. → **Sev:** Low–Medium.

### Area 4 — Spot-request IDOR / id enumeration (sharpened by deep-dive) — Lens A
Background: `DescribeSpotInstanceRequests` / `CancelSpotInstanceRequests` act on `sir-…` ids (examples show short 8-hex `sir-df6f405d`; verify modern 17-char form). The response exposes `instanceId`, `launchedAvailabilityZone`, the full launch spec.
Security Concern (**confirmed IAM asymmetry — the sharpest lead here**): in `list_ec2.md`, `CancelSpotInstanceRequests` **declares** the `spot-instances-request` resource type with a real ARN `arn:${Partition}:ec2:${Region}:${Account}:spot-instances-request/${SpotInstanceRequestId}` — so a scoped policy *can* express account ownership. But the **Describe trio — `DescribeSpotInstanceRequests`, `DescribeSpotPriceHistory`, `DescribeSpotDatafeedSubscription` — have NO resource-type entry at all** (only `ec2:Region`, `Resource:"*"`). IAM therefore **cannot** express "describe only *your own* `sir-` ids"; per-account ownership on the Describe path rests entirely on undocumented EC2 backend logic. That asymmetry is exactly the shape worth two-account testing.
High-level Test Scenarios: *(developed in `fragment_B_datafeed_idor.md`)*
- **Claim (primary):** Because Describe cannot be IAM-scoped to owned requests, `DescribeSpotInstanceRequests` from account A returns (or error-differentiates) a `sir-…` owned by account B. → **Oracle:** 200/data on a foreign id, or an error-string/latency differential between "foreign-but-valid" and "nonexistent" ids (existence oracle across the tenant boundary). → **Pre:** valid foreign `sir-` id (or ability to fabricate; check modern-id entropy/checksum). → **Sev:** cross-account read = High.
- **Claim:** A foreign `sir-…` is cancellable. → **Oracle:** cancel succeeds on a foreign id (note Cancel *does* support a scoped ARN, so a correctly-written policy is a real mitigation — test whether the backend enforces ownership when the policy is `Resource:*`). → **Sev:** cross-account mutate = High–Critical.
- Note possible embedded-checksum defense on modern 17-char ids (genuine null if foreign ids cannot be fabricated and no leak path exists).

### Area 5 — Spot service-linked roles & KMS grant audit — Lenses R, E, H, S
Background: `AWSServiceRoleForEC2Spot` grants `ec2:DescribeInstances`, `ec2:StopInstances`, `ec2:StartInstances`; the KMS create-grant example gives it `Decrypt, Encrypt, GenerateDataKey, GenerateDataKeyWithoutPlaintext, CreateGrant, DescribeKey, ReEncryptFrom, ReEncryptTo`.
Security Concern: (a) Are `Stop/StartInstances` scoped to Spot instances or account-wide (prose says "Spot Instances" — enforced by condition or not)? (b) `CreateGrant` in the KMS grant lets the SLR mint further grants — over-broad for a launch-time decrypt need. (c) `aws-ec2-spot-fleet-tagging-role` PassRole is scoped by name prefix `aws-ec2-spot-fleet-tagging-role` — can a caller satisfy that prefix with their own role?
High-level Test Scenarios: *(developed in fragment A)* resolve the actual AWS-managed SLR policy with `iam:GetPolicyVersion` and audit statement-by-statement; prove over-scope with `SimulatePrincipalPolicy`. Severity: over-scoped Stop/Start = Medium; broad `CreateGrant` = Medium–High. **Reportable as AWS-authored artifact (Tier 2) if the managed-policy default is over-broad — not a customer footgun.**
- **Confirmed artifact lead (Lens R):** `AmazonEC2SpotFleetTaggingRole`'s managed-policy JSON contains a **wildcard `iam:PassRole` (`Resource:"*"`) gated only by `iam:PassedToService`** — audit whether that `PassedToService` value is tight enough to prevent passing arbitrary roles. → **Sev:** Medium–High (AWS-authored, uneditable → Tier 2).
- **Confirmed name-as-boundary anti-pattern (Lenses R, B, E, U):** the end-user PassRole scoping AWS recommends for the tagging role is an **exact-literal-name match** (`arn:aws:iam::*:role/aws-ec2-spot-fleet-tagging-role`). Combined with the `iam:CreateRole`/`iam:AttachRolePolicy` "optional" permissions AWS lists on the *same* `spot-fleet-prerequisites.md` page, a user can **mint their own role under that exact name** with a trust policy they control and have the Spot Fleet service assume it. → **Oracle:** `SimulatePrincipalPolicy` shows the PassRole allowed for a self-created same-named role. → **Sev:** High (privesc).

### Area 6 — Launch-spec content (snapshot/KMS, UserData, AMI) — Lenses H, Q, G
Background: `BlockDeviceMapping`/`EbsBlockDevice` take `SnapshotId`+`Encrypted`+`KmsKeyId` ("can't specify both a snapshot ID and an encryption value"); `UserData` (16KB) runs on the instance; `ImageId` is a raw id.
Security Concern / Scenarios: cross-account or CMK-key confusion on snapshot (Lens H — does a cross-account/disabled CMK get rejected at request time, or only at fulfilment?); UserData → instance-profile credential retrieval (chains Area 2). **AMI name-resolution (whoAMI-style, Lens EE) is N/A for this API** — `ImageId` is an id, not a name lookup; mark null but confirm the Spot *Fleet*/launch-template path (which can use AMI name filters) separately.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| IMDSv2/public-IP/encryption guardrail bypass via legacy path | RequestSpotInstances authz | `RunInstances` `instance`/`volume` condition keys (claimed; **not present on Spot path**) |
| Attach over-privileged instance profile | IamInstanceProfile + PassRole | `iam:PassRole` scope + `ec2:InstanceProfile` (latter unavailable on Spot) |
| Cross-account Spot request read/cancel | Describe/CancelSpotInstanceRequests | account-scoped authorization on `sir-…` |
| Cross-account / stale S3 feed grant | CreateSpotDatafeedSubscription | bucket FULL_CONTROL requirement; manual grant removal on delete |
| SLR over-privilege / broad KMS CreateGrant | AWSServiceRoleForEC2Spot | SLR least-privilege claim; KMS grant scope |
| Encrypted-snapshot / CMK confusion | BlockDeviceMapping | "can't specify both snapshot ID and encryption value" |

---

## 7. Out-of-Scope Risk Categories
- IMDS on a customer's *own* fully-managed instance where the customer intentionally set IMDSv1 — in scope **only** as the *guardrail-bypass* framing of Area 1 (bypassing an org control), not as a standalone IMDS finding.
- A customer steering their own account's instances; single-tenant self-DoS (e.g. exhausting one's own Spot limits).
- Customer-authored IAM policies with weak `iam:PassRole` — least-privilege footgun the customer owns (the *AWS-managed* SLR policy in Area 5 is in scope; a customer's own PassRole scope is not).
- Spot market pricing/availability behavior; product/feature gaps.
- Shared EC2 physical/hypervisor infrastructure, Nitro, host side-channels.
- DNS rebinding against private-only endpoints.

---

## 8. Null hypotheses / doc gaps
- **Lens EE (predictable-name / whoAMI) — N/A for RequestSpotInstances itself:** read `API_RequestSpotLaunchSpecification.md` — `ImageId` is a raw AMI id, no name-based resolution/`--owners`-style lookup in this API, so attacker-AMI name-selection does not apply. *Re-open for the Spot Fleet / launch-template path, which can select AMIs by filter.*
- **Lens F (translation/wire injection) — N/A:** no query-language/wire-protocol translation layer; the API is a typed SigV4 call.
- **Lens K (prompt injection) — N/A:** no LLM/agent in this path.
- **Lens W (attestation) — N/A:** no enclave/attestation gate on Spot launch (checked Placement/launch-spec; none).
- **Lens V (network segmentation) — doc-gap:** instances launch into the customer's own VPC/subnet; no AWS multi-tenant data-plane fleet documented for this feature. No further network-isolation lead unless a shared Spot fulfilment interface is found — confirm surface first.
- **Lens BB/CC/DD/FF (edge/parser/token/cache) — N/A:** direct SigV4 API, no API-Gateway/CDN/authorizer/JWT layer in front.
- **Lens Y (transport) — low:** standard EC2 HTTPS endpoint; no documented http:// or SigV2 acceptance specific to Spot (inherits EC2-wide posture; not a Spot-specific lead).

---

### Appendix — deep-dive fragments
- `_spot_research/fragment_A_iam_parity.md` — full condition-key delta table (RequestSpotInstances vs RunInstances vs RequestSpotFleet), PassRole analysis, SLR/KMS audit.
- `_spot_research/fragment_B_datafeed_idor.md` — data-feed S3 trust model, Spot-request IDOR/enumeration, launch-spec content (snapshot/KMS/UserData).
