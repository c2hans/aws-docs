# EC2 CreateDefaultVpc — Attack Research Plan

Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDefaultVpc.html (+ online `.md` twin); https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html, default-vpc-components.html, default-subnet.html; authoritative condition-key source `https://servicereference.us-east-1.amazonaws.com/v1/ec2/ec2.json`. Companion/twin plan: `CreateDefaultSubnet-attack-research-plan.md`. Status: documentation-derived hypotheses only; nothing tested against a live account.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.
- This action is a **governance / control-plane** surface, not a cross-tenant data surface. The reportable defects here are **AWS-owned structural** (condition-key omission + documented IAM-fan-out bypass), i.e. Tier-2 Lens X/S/U — not customer footguns.

## 1. Pentest Objectives
1. Prove that an SCP / IAM Deny written to govern VPC creation (keyed on `ec2:VpcID`, `aws:RequestTag`, IPAM pool, or tag-on-create) is **inexpressible / inert** against `CreateDefaultVpc`, so a constrained principal can mint a VPC the governance intended to block.
2. Prove the **documented IAM-fan-out bypass**: `CreateDefaultVpc` internally creates an internet gateway, subnets, route table + `0.0.0.0/0` route, security group, NACL and DHCP association **without** the caller holding (or despite a Deny on) `CreateInternetGateway`/`CreateSubnet`/`CreateRouteTable`/`CreateRoute`/`CreateSecurityGroup`.
3. Prove the **public-posture-restoration primitive**: after a defender deletes the default VPC as a hardening step, `CreateDefaultVpc` re-creates a `/16` with a public subnet per AZ, an IGW, and a `0.0.0.0/0`→IGW route in one unconstrained call — and it cannot be guardrailed per-VPC.
4. Prove the **ABAC-at-birth gap**: the created VPC (and its subnets/SG) are born **untagged** with no `aws:RequestTag`/`TagKeys` request context, defeating mandatory-tagging/ABAC admission controls.

## 2. Components, Assets, and Design

**Action.** `CreateDefaultVpc` (EC2 Query API, api-version 2016-11-15). Single-account, control-plane, mutating. One idempotent-ish call ("You cannot have more than one default VPC per Region") that provisions an entire default VPC.

**What one call creates** (default-vpc-components.html, verbatim):
- A VPC with a size `/16` IPv4 CIDR (`172.31.0.0/16`), up to 65,536 addresses.
- A size `/20` **default (public) subnet in each Availability Zone**.
- An **internet gateway**, attached to the VPC.
- A route in the **main route table**: `0.0.0.0/0` → internet gateway (plus `172.31.0.0/16` local).
- A **default security group**, associated with the VPC.
- A **default network ACL**, associated with the VPC.
- Association of the account's **default DHCP options set**.
- Default subnets have `mapPublicIpOnLaunch=true` ("a default subnet is a public subnet" — default-subnet.html / default-vpc.html "comes with a public subnet in each Availability Zone").

**Request surface.** Only `DryRun` (Boolean, optional). **No** CIDR, AZ, tag, IPAM, IPv6, or tenancy parameter — "You cannot specify the components of the default VPC yourself." Response = `requestId` + a `Vpc` object (`cidrBlock`, `dhcpOptionsId`, `instanceTenancy=default`, `isDefault=true`, `state=pending`, **`tagSet/>` empty**, `vpcId`).

**Identity.** SigV4 IAM, caller's own account. No role assumption, no cross-account input, no credential vending.

**Resource identifier shape.** Account-owned singleton per Region (`isDefault=true`). No caller-supplied id; no resource-by-id lookup.

**Authoritative IAM shape (service reference JSON):**
| Action | Resource types | Condition keys |
|---|---|---|
| `CreateDefaultVpc` | **(none)** | **`ec2:Region` only** |
| `CreateDefaultSubnet` | **(none)** | **`ec2:Region` only** |
| `CreateVpc` (scopable twin) | `vpc`, `ipam-pool`, `ipv6pool-ec2` | `vpc`: `aws:RequestTag/${k}`, `aws:TagKeys`, `ec2:Ipv4IpamPoolId`, `ec2:Ipv6IpamPoolId`, `ec2:VpcID`; `ipam-pool`: `aws:/ec2:ResourceTag` |
| `CreateSubnet` (scopable twin) | `subnet`, `vpc`, `ipam-pool` | `subnet`: RequestTag/TagKeys/Ipv4/Ipv6IpamPoolId/`ec2:SubnetID`; `vpc`: ResourceTag/`ec2:Tenancy`/`ec2:VpcID` |

```
  Caller (IAM principal, DryRun optional)
        | ec2:CreateDefaultVpc   [guard surface = ec2:Region ONLY]
        v
  ┌──────────────────────── ONE ACTION, internal fan-out ────────────────────────┐
  │  VPC /16  ──  Subnet /20 ×AZ (public, mapPublicIpOnLaunch=true)               │
  │     │                                                                         │
  │     ├── InternetGateway  (NO ec2:CreateInternetGateway invoked)              │
  │     ├── main RouteTable + 0.0.0.0/0 → IGW  (NO ec2:CreateRoute invoked)      │
  │     ├── default SecurityGroup  (NO ec2:CreateSecurityGroup invoked)         │
  │     ├── default NACL                                                         │
  │     └── default DHCP-options association                                     │
  │  >> "IAM policies do not apply to these actions because you do not perform   │
  │      these actions." (default-vpc-components.html Note)                      │
  └──────────────────────────────────────────────────────────────────────────────┘
```

## 3. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Constrained IAM principal (org SCP / Deny governs VPC creation) | VPC-creation governance boundary | `CreateDefaultVpc` not covered by any resource/tag/IPAM/VpcID condition key | A VPC is created that an equivalent Deny on `CreateVpc` (keyed on VpcID/RequestTag/IPAM/tenancy) would have blocked — the Deny never matches `CreateDefaultVpc` |
| Principal denied `CreateInternetGateway`/`CreateSubnet`/`CreateRoute`/`CreateSecurityGroup` | Those resource-creation boundaries | internal fan-out of `CreateDefaultVpc` bypasses the per-action IAM check | The IGW/subnet/route/SG exists after the call despite the explicit per-action Deny (documented behavior) |
| Attacker/insider with `CreateDefaultVpc` only | Account network-exposure posture (hardened by deleting default VPC) | one call restores `/16` + public subnet/AZ + IGW + `0.0.0.0/0` route | A new `isDefault=true` VPC with an IGW route to `0.0.0.0/0` reappears; EC2 launched into it gets an auto public IPv4 |
| Principal subject to mandatory-tagging / ABAC-at-birth admission | tag-governance boundary | no TagSpecification param, empty `tagSet`, no `aws:RequestTag`/`TagKeys` in request context | VPC (+ children) created with no tags; a `Deny … Null:aws:RequestTag/x:true` style gate cannot fire |
| any customer surface | AWS service plane | n/a | NONE expected — single-account, account-owned resource. If anything implicates AWS's fleet, HARD STOP. |

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `CreateDefaultVpc` | EC2 Query POST | Existing | **Yes** | Yes (ec2 endpoint) | principal with `ec2:CreateDefaultVpc` | **0 resource types, only `ec2:Region`**; `DryRun` only param; fan-out creates 7 child resource types |
| `CreateVpc` | Query | Existing | Yes | Yes | `ec2:CreateVpc` | richly scopable twin (VpcID/RequestTag/IPAM) — comparison baseline |
| `CreateDefaultSubnet` | Query | Existing | Yes | Yes | `ec2:CreateDefaultSubnet` | sibling un-scopable twin (same 0-resource/`ec2:Region` shape) |
| `DeleteVpc` | Query | Existing | Yes | Yes | `ec2:DeleteVpc` | the hardening move this action reverses |

Undocumented-knob sweep: none. The action takes no parameter that weakens auth/isolation — the weakness is the **absence** of parameters/keys, not a permissive value.

## 5. Recommended Areas of Focus

### Area 1 — Condition-key omission: VPC-creation governance is inexpressible against CreateDefaultVpc (Lens X + Lens S) — PRIORITY / CROWN
Background: `CreateVpc` carries resource type `vpc` with condition keys `aws:RequestTag/${k}`, `aws:TagKeys`, `ec2:Ipv4IpamPoolId`, `ec2:Ipv6IpamPoolId`, `ec2:VpcID`. Its functional twin `CreateDefaultVpc` carries **zero resource types and only `ec2:Region`** (confirmed in `ec2.json`).
Security Concern: an org/account that governs VPC creation via a Deny on `CreateVpc` keyed on any of those keys has written a control that is **structurally inert** against the default-VPC path — those keys never populate the request context for `CreateDefaultVpc`, so the Deny never matches and creation proceeds. The only available lever is `ec2:Region` + an all-or-nothing Allow/Deny of the action itself.
High-level Test Scenarios:
- **Claim:** A principal denied `CreateVpc` by a condition on `ec2:VpcID`/`aws:RequestTag`/`ec2:Ipv4IpamPoolId` can still create a VPC via `CreateDefaultVpc`. → **Oracle:** under a scoped role holding `CreateDefaultVpc` + a Deny on `CreateVpc` with those conditions, `CreateDefaultVpc` returns 200 and a new `isDefault=true` VPC appears. `iam:SimulatePrincipalPolicy` for both actions is the safe first oracle (the default-VPC path simulates Allow because the Deny's keys don't apply). → Preconditions: ability to create/simulate a scoped role. → Cost: low. → Severity: **High** (governance/Deny-bypass).
- **Claim:** There is no condition key by which an SCP could restrict *which* VPC `CreateDefaultVpc` creates (CIDR, tenancy, tag, IPAM). → **Oracle:** enumerate the action's condition keys in `ec2.json` — only `ec2:Region`; no CIDR/tenancy/tag/IPAM key exists → the restriction is inexpressible. Refute if a new key appears in the live policy simulator.
Doc evidence: service-reference `ec2.json` (`CreateDefaultVpc` → `ActionConditionKeys:["ec2:Region"]`, `Resources:[]`); API page "You cannot specify the components of the default VPC yourself." Severity-if-true: High.

### Area 2 — Documented IAM-fan-out bypass: one action provisions 7 resource types without their per-action permissions (Lens U + Lens X) — PRIORITY
Background: default-vpc-components.html states verbatim: *"Amazon creates the above resources on your behalf. IAM policies do not apply to these actions because you do not perform these actions. For example, if you have an IAM policy that denies the ability to call CreateInternetGateway, and then you call CreateDefaultVpc, the internet gateway in the default VPC is still created."*
Security Concern: `CreateDefaultVpc` is a **privilege-aggregation primitive** — a single grant internally performs the equivalent of `CreateVpc` + `CreateSubnet`×AZ + `CreateInternetGateway` + `AttachInternetGateway` + `CreateRoute`(0.0.0.0/0) + `CreateSecurityGroup` + NACL + DHCP association, **none of which are IAM-checked**. A least-privilege model that withholds (or Denies) IGW/subnet/route/SG creation is silently defeated. This is strictly broader than the CreateDefaultSubnet twin, which only re-creates subnets.
High-level Test Scenarios:
- **Claim:** A principal holding `ec2:CreateDefaultVpc` but explicitly **denied** `ec2:CreateInternetGateway` (and/or `CreateSubnet`, `CreateRoute`, `CreateSecurityGroup`) still ends up with those resources created. → **Oracle:** scoped role with that Allow+Deny set; after `CreateDefaultVpc`, `DescribeInternetGateways`/`DescribeRouteTables` show the IGW attached and the `0.0.0.0/0`→IGW route present. The doc asserts this outcome; confirm it holds and enumerate the full set of per-action Denies it bypasses. → Severity: **High** (least-privilege bypass; the mitigation is only "also Deny `CreateDefaultVpc`").
- **Adjacent:** verify the doc's prescribed mitigation is the *only* one — i.e. there is no narrower way (VPC BPA aside) to allow `CreateDefaultVpc` while blocking the internal IGW. Note the doc's own pointer to "Block public access to VPCs and subnets" (security-vpc-bpa.md) as the compensating control → test whether VPC BPA actually neutralizes the `0.0.0.0/0` route created here (does BPA override the default route, and is BPA itself guardable?).
Doc evidence: default-vpc-components.html Note (quoted). Severity-if-true: High.

### Area 3 — Public-posture restoration primitive (Lens U)
Background: Deleting the default VPC (and its public subnets + IGW) is a recognized account-hardening step. `CreateDefaultVpc` restores, in one unconstrained call, a `/16` with a **public** subnet per AZ, an IGW, and a `0.0.0.0/0`→IGW main-route-table route; instances launched there get an auto public IPv4 (`mapPublicIpOnLaunch=true`).
Security Concern: an attacker or drifting principal with only `CreateDefaultVpc` can re-open internet-facing network posture that a defender intentionally removed, and (Area 1) it cannot be guardrailed per-VPC.
High-level Test Scenarios:
- **Claim:** After `DeleteVpc` of the default VPC, a principal with only `CreateDefaultVpc` restores an internet-routable default VPC. → **Oracle:** `DescribeVpcs` shows `isDefault=true` again; `DescribeRouteTables` shows `0.0.0.0/0`→igw; a test ENI/instance in a default subnet receives a public IP. → Severity: **Medium–High** (posture regression; realized exposure depends on subsequent launches).
- **Adjacent (Lens L/abuse):** the "one default VPC per Region" rule is an existence constraint, not a rate limit — test the delete→create churn for any side effect (DHCP options re-association, ENI/route artifacts) but expect self-DoS only (out of scope).
Doc evidence: default-vpc.html, default-vpc-components.html route table, default-subnet.html public-subnet statement. Severity-if-true: Medium–High.

### Area 4 — ABAC-at-birth / mandatory-tagging gap (Lens I)
Background: no `TagSpecification` parameter; response shows empty `<tagSet/>`; the action exposes no `aws:RequestTag`/`aws:TagKeys` condition key (unlike `CreateVpc`'s `vpc` resource).
Security Concern: an admission control that requires tags at creation (`Deny CreateVpc where Null aws:RequestTag/CostCenter`) or an ABAC model keyed on birth tags is defeated — the default VPC and all its children are born untagged and no request-tag context exists to gate on.
High-level Test Scenarios:
- **Claim:** `CreateDefaultVpc` produces an untagged VPC that a RequestTag-mandating Deny cannot block. → **Oracle:** `SimulatePrincipalPolicy` with a `Null:aws:RequestTag/x` Deny → Allow for `CreateDefaultVpc`; the live call returns empty `tagSet`. → Severity: **Medium** (ABAC bypass; Low if tags aren't the access mechanism).
Doc evidence: API page (no TagSpecification, `<tagSet/>`); `ec2.json` (no tag keys on the action). Severity-if-true: Medium.

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Deny on `CreateVpc` (VpcID/RequestTag/IPAM) does not block default-VPC path | IAM condition-key coverage | the per-action condition keys on `CreateVpc` — show they don't apply to `CreateDefaultVpc` |
| Fan-out creates IGW/subnet/route/SG despite per-action Deny | internal provisioning | the per-action IAM checks (`CreateInternetGateway` etc.) — doc says they "do not apply" |
| Internet posture restored after hardening-delete | default VPC `0.0.0.0/0`→IGW route | VPC Block-Public-Access (security-vpc-bpa.md) — test whether it actually neutralizes the created route |
| Untagged resource at birth defeats tagging admission | tag governance | `aws:RequestTag`/`TagKeys` — show absent from the action |
| DryRun used as an existence/ownership signal | authz check | DryRun is caller-IAM only (false-positive trap) — do NOT treat as ownership oracle |

## 7. Out-of-Scope Risk Categories
- Cross-account / cross-tenant anything — single-account, account-owned singleton; no resource-by-id, no shared fleet (Lens A null).
- PassRole / credential vending / STS (B/C) — no role input.
- SSRF / upload / injection / KMS / attestation / token-validation (G/Q/F/H/W/FF) — no URL, blob, parser, key, or token in the surface.
- Shared-responsibility / AWS service-plane — not reached; HARD STOP if ever implicated.
- The internet exposure *itself* is a product default, not a vuln; the reportable issue is the **inability to govern** it via IAM (Areas 1–2), which is AWS-owned.
- Single-tenant self-DoS from delete/create churn.

## 8. Null hypotheses / doc gaps
- **Lens A (cross-tenant IDOR)** — null. Pages read: API_CreateDefaultVpc, default-vpc, default-vpc-components, default-subnet. No caller-supplied id, no foreign resource reachable; `isDefault` singleton is account-scoped.
- **Lens B/C (PassRole/vending)** — null. No role ARN or token parameter (API page: only `DryRun`).
- **Lens G/Q/F/K (SSRF/upload/injection/prompt)** — null. No dereferenced field, blob, parser, or LLM in the surface (API page request params = `DryRun` only).
- **Lens H/W/FF (KMS/attestation/JWT)** — null. No key/attestation/token surface.
- **Lens Y (transport/sig)** — null for this action beyond the EC2-endpoint-wide SigV2/`aws:SignatureVersion` observations already catalogued service-wide; nothing action-specific.
- **Lens AA (share/revoke)** — null. Not shareable (no RAM/launchPermission).
- **DryRun trap (noted, not a lead):** `DryRun` returns `DryRunOperation` vs `UnauthorizedOperation` — a **caller-IAM** oracle only, evaluated before resource resolution; it is NOT an ownership/existence oracle (false-positive trap per corpus Variant coverage).
- **Doc-external, hunter to re-verify:** whether VPC Block-Public-Access, once enabled, actually overrides the `0.0.0.0/0`→IGW route that `CreateDefaultVpc` creates (Area 2 adjacent) — not fully settled by the docs read; confirm live. WebSearch unavailable in this environment, so no external corroboration was attempted.

---
Reportability summary: Areas 1 & 2 are **AWS-owned structural defects** (condition-key omission on an action whose twin has the keys; a documented IAM-fan-out that bypasses per-action Denies) → Tier-2 Lens X/S/U, route `aws-security`. Severity: governance/Deny-bypass **High**; posture-restoration **Medium–High**; tag-gap **Medium**. Not customer footguns.
