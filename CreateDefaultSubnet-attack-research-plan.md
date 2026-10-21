# CreateDefaultSubnet — Attack Research Plan

Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDefaultSubnet.html ; sibling API_CreateDefaultVpc.html and API_CreateSubnet.html ; IAM authorization reference `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (actions CreateDefaultSubnet L5083, CreateDefaultVpc L5089, CreateSubnet L716); VPC User Guide default-vpc.html / default-subnet.html. **Status: documentation-derived hypotheses only; nothing tested against a live account.**

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected for this action — it is a single-account control-plane create.)

---

## 1. Pentest Objectives (boundary-breach goals)
1. **Prove the governance-escape twin:** mint a public, auto-public-IP `/20` subnet in the default VPC via `ec2:CreateDefaultSubnet` under an identity/SCP that **denies** the equivalent `ec2:CreateSubnet` scoping (VpcID / tag-on-create / IPAM pool), showing the Deny is inert against the default-subnet path.
2. **Prove posture restoration:** after an org has deliberately deleted its default subnets (a hardening step to prevent auto-public-IP launches), re-create a default subnet (and, worse, a default VPC) and show the public-by-default networking posture is restored with only `ec2:Region` as a possible IAM lever.
3. **Prove tag-governance bypass:** create a subnet with **no tags** and no way for policy to require tags at birth, defeating any `aws:RequestTag`-gated or mandatory-tagging control written for `CreateSubnet`.

---

## 2. Components, Assets, and Design

**What the action does.** `CreateDefaultSubnet` creates one `/20` IPv4 subnet (`availableIpAddressCount` ~4091) in a **specified Availability Zone** inside the account's **default VPC**. One default subnet per AZ. Optional `Ipv6Native` flag creates an IPv6-only subnet (requires deleting an existing default subnet in that AZ first).

**Request parameters** (all optional): `AvailabilityZone` XOR `AvailabilityZoneId`; `Ipv6Native` (bool); `DryRun`. **No `TagSpecification` parameter** — the created subnet is born untagged (`<tagSet/>` empty in the sample response). **No CIDR parameter** — the `/20` is auto-allocated by AWS (`172.31.x.0/20` in the sample), so there is no attacker-chosen CIDR (CIDR-injection N/A).

**Security-relevant defaults of the created resource** (VPC User Guide, verbatim):
- "**By default, a default subnet is a public subnet**, because the main route table sends the subnet's traffic that is destined for the internet to the internet gateway."
- "Instances that you launch into a default subnet **receive both a public IPv4 address and a private IPv4 address**" — i.e. `mapPublicIpOnLaunch=true` (confirmed in the API sample response: `<mapPublicIpOnLaunch>true</mapPublicIpOnLaunch>`).
- "if you made any modifications to your default VPC, we do not add a new default subnet … you can create one yourself" — the manual-create path this action exposes.

**Sibling `CreateDefaultVpc`** (broader primitive): creates a default VPC (`/16`) **plus a default subnet in every AZ**, an internet gateway, a `0.0.0.0/0`→IGW route, and a default security group. "You cannot specify the components of the default VPC yourself." One default VPC per Region; re-creatable after deletion.

**Identity / ownership.** Pure single-account control-plane action, SigV4 IAM. The default VPC is always owned by the calling account; there is no resource-by-id input and no cross-tenant naming. The asset at risk is **the account's own network posture and the enforceability of the account/org's own guardrails**, not another tenant's data.

**Connection sketch:**
```
caller (ec2:CreateDefaultSubnet, ec2:Region only)
      │  AZ name/id + optional Ipv6Native
      ▼
 EC2 control plane ── auto-allocates /20, defaultForAz=true, mapPublicIpOnLaunch=true
      ▼
 default VPC ──(main route table 0.0.0.0/0)──► internet gateway ──► INTERNET
      ▲
 any instance launched here is auto-assigned a PUBLIC IPv4
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv principal holding `ec2:CreateDefaultSubnet` | The org/account's subnet-creation **governance policy** (SCP/identity policy written against `ec2:CreateSubnet`) | Default-subnet create path exposes only `ec2:Region`; none of CreateSubnet's scoping keys | A subnet is created that the equivalent `CreateSubnet` policy would have denied (VpcID / tag / IPAM constraint) — **governance boundary broke** |
| Same principal | Account's **hardened network posture** (default subnets deliberately deleted) | `CreateDefaultSubnet` / `CreateDefaultVpc` restore public subnet + IGW route + auto-public-IP | A `defaultForAz=true`, `mapPublicIpOnLaunch=true` subnet (or full default VPC) reappears → instances again auto-exposed to the internet |
| Same principal | **Mandatory-tagging / ABAC** control | No `TagSpecification`, no `aws:RequestTag`/`aws:TagKeys` key on the action | Subnet created untagged where a `RequestTag`-gated create would have been denied |
| (null) customer ↔ service account | n/a | Single-account action, no shared fleet, no resource-by-id | No cross-tenant crossing exists — see §8 |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `CreateDefaultSubnet` | Query/SDK | Existing | **Yes** | Yes (ec2 regional endpoint) | principal with `ec2:CreateDefaultSubnet` | **Resource types: none. Condition keys: `ec2:Region` only.** No TagSpecification. |
| `CreateDefaultVpc` | Query/SDK | Existing | **Yes** | Yes | `ec2:CreateDefaultVpc` | **Resource types: none. Condition keys: `ec2:Region` only.** Broader: subnet-per-AZ + IGW + routes. |
| `CreateSubnet` (comparison twin) | Query/SDK | Existing | Yes | Yes | `ec2:CreateSubnet` | **Scopable:** subnet*(`aws:RequestTag`,`aws:TagKeys`,`ec2:Ipv4IpamPoolId`,`ec2:Ipv6IpamPoolId`,`ec2:Region`,`ec2:SubnetID`), vpc*(`aws:ResourceTag`,`ec2:Region`,`ec2:ResourceTag`,`ec2:Tenancy`,`ec2:VpcID`), ipam-pool. |

**Undocumented/console-hidden knob:** `Ipv6Native=true` creates an IPv6-only default subnet — accepted by the API, no condition key exists to permit/deny it. `AvailabilityZoneId` lets the caller target an AZ by its *physical* id (`use1-az1`, stable across accounts) rather than the per-account-randomized AZ name — neither AZ field is a condition key on either create action, so AZ cannot be IAM-scoped.

---

## 5. Recommended Areas of Focus

### Area 1 — Un-scopable create twin: `CreateDefaultSubnet` / `CreateDefaultVpc` vs `CreateSubnet` (PRIMARY) — Lens X + Lens S
**Background.** The service exposes two paths that produce the *same class of resource* (a subnet in a VPC). `CreateSubnet` is richly scopable — a policy author can bind creation to a specific VPC (`ec2:VpcID`), require tags at birth (`aws:RequestTag`/`aws:TagKeys`), pin tenancy (`ec2:Tenancy`), or require an IPAM pool (`ec2:Ipv4IpamPoolId`/`ec2:Ipv6IpamPoolId`). `CreateDefaultSubnet` and `CreateDefaultVpc` carry **no resource types and only `ec2:Region`** (confirmed list_ec2.md L5083–L5094).

**Security Concern.** A Deny/SCP written to govern subnet creation — e.g. `Deny ec2:CreateSubnet where ec2:VpcID != vpc-approved`, or `Deny ec2:CreateSubnet unless aws:RequestTag/CostCenter exists` — is **inert** against the default-subnet path: those condition keys are not evaluable there, so the statement never matches and the create proceeds. The only lever that survives is `ec2:Region` (all-or-nothing per region) and a blanket allow/deny of the action name itself. An org that believes it has "locked down subnet creation" via `CreateSubnet` conditions has not locked down `CreateDefaultSubnet`/`CreateDefaultVpc`.

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** A principal denied `ec2:CreateSubnet` via an `ec2:VpcID`/`aws:RequestTag` condition can still create a subnet in the default VPC by calling `CreateDefaultSubnet`. → **Oracle:** scoped-role `CreateSubnet` returns `AccessDenied` under the condition, while `CreateDefaultSubnet` in the same AZ returns 200 with `defaultForAz=true`. → **Severity:** High (governance bypass / least-priv escape).
- **Claim:** The `ec2:VpcID`, `ec2:Tenancy`, `aws:RequestTag`, `ec2:Ipv4IpamPoolId`, `ec2:Ipv6IpamPoolId` conditions are **not expressible** on `CreateDefaultSubnet`. → **Oracle:** `iam:SimulatePrincipalPolicy` / policy linter — a policy using any of these keys on `ec2:CreateDefaultSubnet` is accepted syntactically but never constrains the action (key absent from the request context). → **Severity:** Medium (condition inexpressibility).
- **Claim:** `CreateDefaultVpc` is the broader twin — one call restores an entire default VPC (`/16` + subnet-per-AZ + IGW + `0.0.0.0/0` route + default SG) with only `ec2:Region` as a lever. → **Oracle:** under a region-unrestricted allow, `CreateDefaultVpc` in a region whose default VPC was deleted returns a new `isDefault=true` VPC. → **Severity:** High.

**Doc evidence:** list_ec2.md L5083–5094 (empty resource types, `ec2:Region` only) vs L716–720 (CreateSubnet full key set). API_CreateDefaultVpc.html ("default subnet in each Availability Zone … You cannot specify the components").

### Area 2 — Posture restoration / public-by-default networking — Lens U
**Background.** Deleting default subnets (or the default VPC) is a recognized hardening move: it forces instances into private subnets and prevents the auto-assign-public-IP behavior. Default subnets are public *by design* — "By default, a default subnet is a public subnet" and launched instances "receive both a public IPv4 address and a private IPv4 address" (`mapPublicIpOnLaunch=true`, confirmed in the API sample response).

**Security Concern.** Because the create actions are only `ec2:Region`-scopable, an org **cannot write a tight IAM guardrail** that says "never re-create a public default subnet in vpc-X" — the VPC can't be named. A principal with the action can silently undo the hardening, and every subsequent `RunInstances` into that subnet yields an internet-reachable instance with a public IPv4 — with no new network-ACL/SG step and without touching `ModifySubnetAttribute`.

**High-level Test Scenarios:**
- **Claim:** After default subnets are deleted, `CreateDefaultSubnet` restores a subnet with `mapPublicIpOnLaunch=true` and the main-route-table `0.0.0.0/0`→IGW path, re-enabling auto-public instances. → **Oracle:** created subnet shows `mapPublicIpOnLaunch=true` and `defaultForAz=true`; a canary instance launched with no explicit public-IP flag receives a public IPv4. → **Severity:** High (re-exposure of workloads; restoration is un-guardrailable at the VPC level).
- **Claim:** The "public subnet" guarantee is enforced only by orchestration (main route table + subnet attribute), not by any IAM condition the customer can set on the create path. → **Oracle:** no condition key on `CreateDefaultSubnet` controls `mapPublicIpOnLaunch` or route-table association. → **Severity:** Informational→High as enabler.

**Doc evidence:** default-subnet.html (public-by-default, public IPv4 on launch); default-vpc-components (IGW + route). Stop condition: once a public `defaultForAz=true` subnet with a launched public-IP instance is observed, the boundary is proven — do not launch further instances.

### Area 3 — Tag-on-create / ABAC bypass — Lens I
**Background.** `CreateSubnet` supports `aws:RequestTag`/`aws:TagKeys`, enabling "deny create unless tagged" and ABAC where downstream permissions key on subnet tags. `CreateDefaultSubnet` has **no `TagSpecification` parameter and no tag condition keys**; the subnet is born untagged.

**Security Concern.** A mandatory-tagging control or ABAC scheme that assumes every subnet is tagged at birth is defeated: the default-subnet path produces an untagged subnet that no `aws:RequestTag` gate can block, and tags can only be added afterwards via a separate `CreateTags` call (which may itself be unprivileged or unmonitored).

**High-level Test Scenario:**
- **Claim:** `CreateDefaultSubnet` creates a subnet while a `Deny unless aws:RequestTag/<k>` policy on `CreateSubnet` is in force. → **Oracle:** `CreateSubnet` denied, `CreateDefaultSubnet` succeeds with `<tagSet/>` empty. → **Severity:** Medium (tag-governance gap; High if subnet tags gate access control).

**Doc evidence:** API page (no TagSpecification); list_ec2.md CreateSubnet subnet* row has `aws:RequestTag`/`aws:TagKeys`, CreateDefaultSubnet row has none.

### Area 4 — DryRun is a caller-IAM oracle, not an ownership/existence oracle (variant note)
`DryRun` returns `DryRunOperation` vs `UnauthorizedOperation` purely on the caller's IAM — it is evaluated before any resource resolution. Do **not** treat a `DryRunOperation` success as proof a default VPC exists or that the subnet was/will be created; confirm via an actual create or `DescribeSubnets`. (False-positive trap flagged in the corpus.)

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Deny on `CreateSubnet` (VpcID/tag/IPAM) bypassed via `CreateDefaultSubnet` | IAM authorization layer | Condition-key scoping — **absent on default-subnet path** |
| Re-create public default subnet after hardening | Default VPC main route table + subnet attr | Deletion of default subnet (reversible by this action, un-guardrailable per-VPC) |
| Full default-VPC restoration (IGW + routes + SG + subnets) | `CreateDefaultVpc` | One default VPC per region; only `ec2:Region` constrains re-create |
| Mandatory-tagging / ABAC at subnet birth | `aws:RequestTag` gate | No TagSpecification/request-tag key on default-subnet path |
| AZ-scoped creation control | `ec2:AvailabilityZone(Id)` | Not a condition key on either create action |

---

## 7. Out-of-Scope Risk Categories
- **Cross-account / cross-tenant access** — does not apply; single-account, account-owned default VPC, no resource-by-id input.
- **CIDR injection** — the `/20` is AWS-allocated; no attacker-chosen CIDR.
- **Shared/managed infrastructure, service-plane reach** — not touched by this control-plane create.
- **Customer-authored least-privilege footguns** — if the customer simply granted `ec2:CreateDefaultSubnet` broadly, that is a customer policy choice. The *reportable* defect here is the **structural inexpressibility** of VPC/tag scoping on an AWS action whose scopable twin has it — a condition-key omission AWS owns (Tier-2 style, Lens X/S), not a customer misconfiguration.
- **Single-tenant self-DoS** (one default subnet per AZ cap) — low/out of scope.

---

## 8. Null hypotheses / doc gaps
- **Lens A (cross-tenant IDOR) — NULL.** Pages checked: API_CreateDefaultSubnet.html, API_CreateDefaultVpc.html, default-vpc.html, default-subnet.html. No resource-by-id parameter, no tenant/account input, default VPC is always caller-owned. No cross-tenant crossing.
- **Lens B/C (PassRole/vending) — NULL.** No role ARN, no credential vending, no `iam:PassRole` surface on this action (checked API params + IAM row).
- **Lens G/Q (SSRF/upload) — NULL.** No field the service dereferences or parses; no URL/blob input (checked API params).
- **Lens F/K (injection/prompt) — NULL.** No translation layer, no customer-parsed content, no LLM.
- **Lens AA (share/revoke) — NULL.** No sharing primitive; default VPC is not RAM-shareable.
- **Doc gap:** The IAM reference lists only `ec2:Region` for these two actions; confirm **live** that `ec2:VpcID`, `aws:RequestTag`, and `ec2:AvailabilityZone` truly do not appear in the request context for `CreateDefaultSubnet` (a policy using them is syntactically accepted but, per the reference, never constrains the call). This is the single highest-value thing for the hunter to confirm first.

---

### Priority order for the hunter
1. **Area 1** (un-scopable twin — Deny bypass vs CreateSubnet) — highest, structural AWS-owned condition-key omission.
2. **Area 2** (public-posture restoration, incl. CreateDefaultVpc) — High impact, chains to RunInstances auto-public-IP.
3. **Area 3** (tag/ABAC-at-birth bypass).
4. **Area 4** (DryRun oracle caveat) — methodology guard, not a finding.
