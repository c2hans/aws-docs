# EC2 `CreateNatGateway` — Attack Research Plan
Source of leads: `API_CreateNatGateway.html/.md` (online + mirror), `service-authorization/.../list_ec2.md` detailed row (CreateNatGateway @5318; also DeleteNatGateway / AssociateNatGatewayAddress / DisassociateNatGatewayAddress / Assign/UnassignPrivateNatGatewayAddress), `vpc/.../nat-gateways-regional.md`. Status: **documentation-derived hypotheses only; nothing tested against a live account.** Companion family memos: `[[ec2-associatenatgatewayaddress-surface]]`, `[[ec2-assignprivatenatgatewayaddress-surface]]`, `[[ec2-ip-assignment-family-and-eni-scoping]]`.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop.
- Work in priority order; look left and right for adjacent bugs in the NAT-gateway address family (the child Assign/Associate actions share the scoping gaps).
- **HARD STOP:** regional NAT gateway **automatic mode** is an AWS-operated control loop (auto-manages IPs + AZ expansion). The moment evidence touches an AWS-fleet identity/ARN/account driving that loop, stop, preserve evidence, flag `aws-security`.

## 1. Pentest Objectives (boundary-breach goals)
1. From a scoped `ec2:CreateNatGateway` grant intended to confine NAT gateways to specific subnets/AZs/VPCs, **create a NAT gateway outside that intended placement** (subnet/AZ/VPC/connectivity the author believed they had denied).
2. **Attach an attacker-chosen public egress identity** (EIP) to a NAT gateway serving workloads the attacker does not own, changing/adding the outbound source IP for everything behind it (allowlist/IP-reputation defeat).
3. Establish an **internet egress path (public NAT gateway)** from a position the org intended to be private-only.
4. **Self-widen** a tag-ABAC-scoped grant via tag-on-create.
5. Create a NAT gateway **ENI inside another account's shared subnet** (VPC-sharing boundary).

## 2. Components, Assets, and Design
- **Interface:** EC2 Query/SDK action `CreateNatGateway` (SigV4, control-plane, mutating, external-facing, callable by any principal holding the action). Idempotency via `ClientToken` (≤64 ASCII).
- **What it builds:** a NAT gateway (`nat-0{17hex}`, high-entropy) plus **a network interface it creates in the target subnet** with a private IP from the subnet range. Public NATGW → associates an EIP (public source IP); private NATGW → private-only, routed via TGW/VGW.
- **Resource / identifier shapes:** `natgateway` (created, account-scoped ARN), `subnet` (zonal input), `vpc` (regional input), `elastic-ip` (allocation-id / public-ip), ENI (derived). No URL/blob/parser/secret/role/token inputs.
- **Request parameters (API):** `SubnetId` (zonal), `VpcId` + `AvailabilityMode=zonal|regional` + `AvailabilityZoneAddress.N` (**NEW** regional), `ConnectivityType=public|private`, `AllocationId` + `SecondaryAllocationId.N` (public EIPs), `PrivateIpAddress` + `SecondaryPrivateIpAddress.N` + `SecondaryPrivateIpAddressCount` (1–31, private), `TagSpecification.N`, `DryRun`, `ClientToken`.
- **Trust zones:** customer account/VPC (resource owner) ↔ AWS NAT service-plane (regional automatic control loop that auto-provisions AZs/EIPs) ↔ shared-VPC owner account (if subnet is RAM-shared). The NAT gateway's EIP set **is the shared public egress identity** of every workload routed to it.

ASCII (zonal vs regional authz surface):
```
zonal:    caller --CreateNatGateway--> [natgateway*]+[subnet(SubnetId)]+[elastic-ip(AllocationId)]
          scopable by: SubnetID / AZ / Vpc (subnet leg) + AllocationId / PublicIp (eip leg)
regional: caller --CreateNatGateway--> [natgateway*]+[vpc(VpcId)]        (NO subnet leg)
          scopable by: VpcID only  -->  subnet/AZ-level Deny is INERT  <-- (Lead R1)
          then AWS auto-expands across AZs + auto-associates EIPs (service-plane loop)
```

## 3. API / Interface Inventory (authz legs — authoritative)
`CreateNatGateway` — Write. Four resource legs (only `natgateway*` is required):

| Leg | Req? | Condition keys | Note |
|---|---|---|---|
| `natgateway*` | yes | `aws:RequestTag/${k}`, `aws:TagKeys`, `ec2:Region` | **tag/region only** — created resource not scopable by content |
| `elastic-ip` | if EIP given | `aws:ResourceTag`, `ec2:AllocationId`, `ec2:Domain`, `ec2:PublicIpAddress`, `ec2:Region`, `ec2:ResourceTag` | rich: can pick WHICH EIP |
| `subnet` | zonal only | `aws:ResourceTag`, `ec2:AvailabilityZone`, `ec2:AvailabilityZoneId`, `ec2:Region`, `ec2:ResourceTag`, `ec2:SubnetID`, `ec2:Vpc` | rich — **absent for regional** |
| `vpc` | regional | `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag`, `ec2:Tenancy`, `ec2:VpcID` | VpcID scoping |

Undocumented/under-surfaced knobs to probe: `AvailabilityMode=regional` (changes which legs appear → authz-surface delta), `ConnectivityType` (**no condition key exists for it**), `AvailabilityZoneAddress.N` (regional manual-mode EIP placement, no AZ/EIP-binding key).

Family (route adjacent bugs): `DeleteNatGateway`, `AssociateNatGatewayAddress`/`Disassociate…` (public EIP half — see memo), `AssignPrivateNatGatewayAddress`/`Unassign…` (private IP half — see memo), `AttachApplianceToNatGateway` (perm-only, Network Firewall confused-deputy — see memo).

## 4. Trust-Boundary Map
| From | To | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Scoped caller | subnet/AZ placement policy | `AvailabilityMode=regional` drops the subnet leg | A NATGW created with no subnet resource in request → a `Deny` keyed on `ec2:SubnetID`/`ec2:AvailabilityZone` never evaluates = **regional create succeeds where zonal is denied** |
| Scoped caller | egress identity of others' workloads | associate attacker EIP at create to a NATGW others route to | outbound source IP for co-routed workloads changes/adds to attacker-chosen EIP |
| Scoped caller | "private-only" egress posture | `ConnectivityType=public` with no condition key | a **public** NATGW (internet egress) created under a grant meant to permit NAT only |
| Tag-ABAC-scoped caller | own grant's scope | `aws:RequestTag` tag-on-create + `CreateTags` | principal self-applies the gating tag → self-widen |
| Participant account | VPC-owner's subnet | create NATGW ENI in RAM-shared subnet | a NATGW ENI lands in another account's subnet/AZ |
| Any caller | AWS NAT service plane | regional automatic-mode control loop | **HARD STOP** — AWS-fleet identity drives AZ expansion/EIP auto-association |

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area R1 — Regional mode drops the subnet authz leg (Lens S + X + U; **NEW surface, top priority**)
**Background:** `AvailabilityMode=regional` is new. Zonal create carries a `subnet` leg with `ec2:SubnetID`, `ec2:AvailabilityZone`, `ec2:AvailabilityZoneId`, `ec2:Vpc`. The regional path takes `VpcId` instead and **"you do not need to specify any subnets"** (`nat-gateways-regional.md`; CLI `--vpc-id … --availability-mode regional`) — so the subnet resource is **absent from the request** and the regional leg only offers `ec2:VpcID`/`ec2:Tenancy`.
**Security Concern:** Any policy that confines NAT-gateway creation to specific subnets or AZs via `ec2:SubnetID` / `ec2:AvailabilityZone` on the `subnet` leg is **inert for a regional NATGW** — those keys never populate, so (depending on the author's `Deny`-vs-`Allow` construction) creation either fails open or the subnet/AZ restriction silently does not apply. A caller denied "create NATGW only in subnet-X" can create a regional NATGW spanning the whole VPC's AZs.
**High-level Test Scenarios:**
- Claim: *A `Deny` on `CreateNatGateway unless ec2:SubnetID IN {approved}` does not stop a regional create.* → Oracle: with a role carrying that Deny, `create-nat-gateway --vpc-id <v> --availability-mode regional` returns a `natGateway` (vs `AccessDenied` for the zonal form in a non-approved subnet).
- Claim: *`ec2:AvailabilityZone` restrictions are bypassed by regional auto-expansion* — the service later expands into AZs the policy would deny (≤60 min), with no per-AZ IAM check.
- Claim: *An `Allow` written only for the zonal shape (subnet leg) breaks for regional* (fail-closed variant) OR *an `Allow` on `natgateway*`+`vpc` with broad VpcID lets regional create anywhere in the VPC.*
**Doc evidence:** `list_ec2.md` CreateNatGateway legs; `nat-gateways-regional.md` ll.33–35, 61, 73. **Severity-if-true:** Medium–High (placement-control bypass; High on a shared VPC where egress identity is co-tenant).

### Area R2 — No EIP↔placement binding key: egress-identity placement is uncontrollable (Lens S + A/V)
**Background:** The `elastic-ip` leg has rich selector keys (`ec2:AllocationId`, `ec2:PublicIpAddress`, `ec2:Domain`) and the `subnet` leg has `ec2:SubnetID`/`ec2:Vpc` — but **no condition key correlates WHICH EIP with WHICH subnet/VPC/NATGW.** Same shape as the family crown jewel (`[[ec2-associatenatgatewayaddress-surface]]`): the EIP set is the shared public egress identity.
**Security Concern:** A two/three-leg grant ("create NATGW with EIP A, in subnet B") authorizes **any allowed combination** — EIP A in a different allowed subnet, or a different allowed EIP in subnet B. If subnet B hosts workloads the attacker does not own (shared/misconfigured route table), the attacker sets the outbound source IP those workloads egress from → defeats downstream IP allowlists / reputation, enables EIP-release→next-tenant hand-off scavenging.
**High-level Test Scenarios:**
- Claim: *A grant scoped to allocation `eipalloc-X` and subnet `subnet-Y` also permits `eipalloc-X` on `subnet-Z`* (no cross-leg binding). Oracle: both creates succeed.
- Claim: *`ConnectivityType` has no condition key, so "only private NAT" is inexpressible* — a grant meant for private NAT can create a **public** NATGW (internet egress). Oracle: `--connectivity-type public` succeeds under a policy intended to deny internet egress (no `ec2:ConnectivityType` key exists to deny it).
**Doc evidence:** `list_ec2.md` leg table; `API_CreateNatGateway` `AllocationId`/`ConnectivityType` (no condition key). **Severity-if-true:** High on shared egress; Medium intra-account.

### Area R3 — Tag-on-create ABAC self-widen (Lens I + S)
**Background:** The required `natgateway*` leg's only non-region keys are `aws:RequestTag/${k}` + `aws:TagKeys`. Tag ABAC is therefore the *only* way to scope the created resource.
**Security Concern:** If the author gates creation on `aws:RequestTag/team = X` (or later use on `ec2:ResourceTag`), a principal who also holds `CreateTags` (or supplies the tag at create) self-satisfies the gate → self-widen. Standard EC2 tag-on-create footgun, but here it is the **sole** resource-scoping mechanism for the created NATGW.
**Oracle:** with a role allowed `CreateNatGateway` only when `aws:RequestTag/team=X` and also `CreateTags`, create with `TagSpecification team=X` then retag — the resource escapes the intended ABAC fence. **Severity:** Medium (unless tag is the access-control mechanism → High).

### Area R4 — Shared-VPC / cross-account subnet placement (Lens A + V)
**Background:** VPC sharing (RAM) lets a participant account create resources in the owner's shared subnet. CreateNatGateway places an **ENI in the target subnet**.
**Security Concern:** Can a participant create a NATGW (ENI + egress) inside the VPC-owner's shared subnet, giving the participant control of an egress appliance physically in the owner's network segment, or influencing the owner's AZ footprint? Does the `subnet`/`vpc` leg's `ec2:Vpc`/`ec2:VpcID` evaluate to the shared VPC (owner-scoped) so the owner can/can't deny it?
**Oracle:** as a VPC-sharing participant, `create-nat-gateway --subnet-id <shared-subnet>` succeeds and the NATGW ENI lands in the owner's subnet. **Severity:** High if it crosses the account boundary with egress control; else Medium. Note: `natgateway` ARN is `${Account}`-scoped and `nat-0{17hex}` is high-entropy → direct cross-account IDOR on the created id is a **null** (see §8).

### Area R5 — Regional automatic-mode service-plane loop (Lens U / B — bounded, HARD-STOP-adjacent)
**Background:** Automatic mode: "AWS automatically manages IP addresses and Availability Zone expansion." Expansion triggered by ENI presence in an AZ (≤60 min); IAM-ungated (from `[[ec2-assignprivatenatgatewayaddress-surface]]`).
**Security Concern:** A principal with only ENI-launch permission (no `natgateway*` perm) can **trigger** expansion/auto-EIP-association → cost/footprint/routing influence without holding the NAT action. The zonal→regional "reuse IPs" conversion **deletes the zonal NATGW first (releasing EIPs) then recreates** with no atomic hand-off ("resets existing connections") → an EIP-reassignment/scavenging race window.
**Oracle:** observe expansion/EIP association occurring with no `CreateNatGateway`/`AssociateNatGatewayAddress` call in CloudTrail by the triggering principal. **Severity:** Medium (cost/footprint); the control loop itself is AWS-operated — **do not probe the loop's identity; HARD STOP if it surfaces an AWS-fleet credential.**

### Area R6 — DeleteNatGateway / resilience teardown (Lens L + X)
**Background:** Deleting a NATGW / converting modes resets connections; private family `Unassign` can strip secondary IPs collapsing NAT port capacity (child-action memo).
**Security Concern:** Is `DeleteNatGateway` scopable finer than tag/region? Can a cross-team principal delete or mode-convert a shared NATGW (availability teardown / egress-IP churn)? **Oracle:** `DeleteNatGateway` on a foreign-but-same-account shared NATGW succeeds with only tag/region scoping. **Severity:** High on shared egress (cross-team DoS); else out-of-scope self-DoS.

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Regional create bypasses subnet/AZ Deny | `AvailabilityMode` leg selection | `ec2:SubnetID`/`ec2:AvailabilityZone` on subnet leg (inert when leg absent) |
| Attacker EIP on co-tenant egress | elastic-ip + natgateway legs | `ec2:AllocationId`/`PublicIpAddress` (no cross-leg binding) |
| Public NATGW under private-only intent | `ConnectivityType` | none (no condition key) |
| Tag-ABAC self-widen | `natgateway*` RequestTag | `aws:RequestTag`/`aws:TagKeys` + CreateTags denial |
| Cross-account subnet ENI | shared VPC | `ec2:Vpc`/`ec2:VpcID` + RAM share config |
| Ungated AZ expansion / EIP auto-assoc | regional automatic loop | (AWS-operated; no customer IAM key) |

## 7. Out-of-Scope Risk Categories
- The regional **automatic-mode control loop** internals (AWS-operated service plane — HARD STOP).
- Single-tenant self-DoS (deleting your own NATGW; draining your own secondary IPs).
- Shared VPC/NAT **product-design** choices (egress sharing is a feature); only the *authz-enforcement gap* is in scope.
- IMDS / data-plane of instances behind the NATGW.
- Customer-authored least-privilege footguns (in scope ONLY if an AWS-managed/sample policy ships the weak default — see §8 Lens R).
- Direct cross-account IDOR on `nat-0{17hex}` ids (high-entropy, account-scoped ARN, `DryRun` = caller-IAM only, **not** an ownership oracle).

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens G (SSRF), F (injection/parser), K (prompt), Q (upload), H (CMK), T (secret), W (attestation), J (OAuth), M (session), FF (JWT), DD (cache), CC (upstream-context), BB (canonicalization), Y (transport/sig)** — **NULL.** Checked: `API_CreateNatGateway.md` (no URL/blob/parser/role/token/secret field; all inputs are ids, IPs, enums, tags) and `nat-gateways-regional.md`. No server-side dereference, no parsed content, no credential generation, no token/signature surface.
- **Lens B/C (PassRole/vending)** — NULL at create (no role ARN input; no credential vended). Regional loop assumes AWS-side identity only (HARD STOP, not a customer-reachable PassRole).
- **Lens A cross-account** — effectively NULL (account-scoped ARN, high-entropy id, no ID-in-body-vs-path divergence); the live A/V surface is the **shared-VPC** path (R4), not id enumeration.
- **Lens R (AWS-authored IAM artifact)** — **doc-gap, confirm first.** No NATGW-specific AWS-managed/sample policy is printed; `nat-gateway-working-with.md` points to generic `security-iam.md`. If a hunter finds `AmazonVPCFullAccess` (or similar) granting `CreateNatGateway`/`AssociateNatGatewayAddress` on `Resource:*` unconditioned, pull the actual JSON (`GetPolicyVersion`) and audit — route Tier-2 per `[[ec2-ip-assignment-family-and-eni-scoping]]`.
- **Lens AA (revoke lifecycle)** — partial: covered via R5 conversion gap and R6; no explicit share/unshare on NATGW itself.
```

🤖 Generated with [Claude Code](https://claude.com/claude-code)
