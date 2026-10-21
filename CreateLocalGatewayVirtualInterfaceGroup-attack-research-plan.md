# CreateLocalGatewayVirtualInterfaceGroup — Attack Research Plan

Source of leads:
- API: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLocalGatewayVirtualInterfaceGroup.html (mirror: `docs/AWSEC2/latest/APIReference/API_CreateLocalGatewayVirtualInterfaceGroup.md`)
- Sibling API (the VIFs that go *into* the group): API_CreateLocalGatewayVirtualInterface.html
- Response obj: API_LocalGatewayVirtualInterfaceGroup.html
- IAM authoritative: `docs/service-authorization/latest/reference/list_ec2.md` (summary L596-599; detail L5300-5304 create; L6034-6038 delete; ARNs L9973-9974). **NOTE: online Service Authorization Reference 404s intermittently for this family — trust the offline mirror, cross-check online where reachable.**
- Concept: https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html

Status: **documentation-derived hypotheses only; nothing tested against a live account.** This action requires a physical AWS Outposts rack to exercise — surface is doc-confirmed but a live hunter needs an Outpost (ideally 2nd-gen, which has the customer-driven VIF/BGP APIs).

Sibling/family plans already written (reuse their context): `CreateLocalGatewayRouteTable-attack-research-plan.md`, `CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation-attack-research-plan.md`, `CreateLocalGatewayRoute-attack-research-plan.md`, `CreateLocalGatewayRouteTableVpcAssociation-attack-research-plan.md`, `CreateCoipCidr`/`CreateCoipPool` plans. This action is the **root of that chain** — it mints the physical-uplink container that everything downstream binds to.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **DryRun is a caller-IAM oracle only, NOT an ownership oracle** — it is evaluated before resource resolution. Do not use it to probe x-account ownership. Safe ownership oracle = `iam:SimulatePrincipalPolicy`.
- **HARD STOP:** the physical BGP/VIF plane terminates on AWS-installed Outposts networking hardware and (for the Region-bound data path) AWS's service link. The moment evidence shows you can (a) influence an **AWS-owned** local gateway / VIF belonging to another account's rack, or (b) reach AWS's own service-plane/control-plane via a crafted VIF/BGP session, **stop, preserve evidence, flag for AWS-Security disclosure.** BGP route injection toward live on-prem is destructive — model it, do not fire it blind.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Set a BGP identity (local/peer ASN) or peering target that IAM cannot restrict** → stand up a rogue/ unexpected BGP session from the Outpost to an on-prem device of the attacker's choosing.
2. **Tear down a VIF group** (physical-uplink container) a principal is denied from *creating* → on-prem connectivity blackhole for the whole local gateway (denial-of-resilience).
3. **Create a VIF group on a local gateway the principal does not own** (RAM-shared / shared-tag) → cross-account manipulation of another account's physical uplink.
4. **Chain** VIF group → VIF (peer IP/ASN/VLAN) → RTB↔VIF-group association (routing domain) → LocalGatewayRoute → steer a victim CIDR onto an attacker-chosen uplink = targeted on-prem traffic interception/exfil.
5. Confirm the **doc-vs-API capability gap** (concepts page says "AWS creates the VIFs and VIF group"; the API lets the *customer* create them with full BGP config) does not leave an unguarded path.

---

## 2. Components, Assets, and Design

**What it is.** `CreateLocalGatewayVirtualInterfaceGroup` (EC2 Query API, `ec2-2016-11-15`) creates a **VIF group** on an Outposts **local gateway (LGW)**. Per the Outposts UG a VIF group is a *logical grouping of VIFs*, and a VIF "sets up VLAN, IP, and BGP connectivity between an Outposts networking device and an on-premises networking device." The VIF group is the container that carries the **local BGP ASN** for that uplink; the member VIFs carry the **peer** side (peer IP, peer ASN, VLAN, LAG).

**Generation gap (important).** The concepts page still describes the **1st-gen** model — *"AWS creates one VIF for each LAG and adds both VIFs to a VIF group"* (an AWS responsibility). But the API reference exposes **customer-driven** `CreateLocalGatewayVirtualInterfaceGroup` + `CreateLocalGatewayVirtualInterface` with `OutpostLagId` (a LAG abstraction) and full BGP params — this is the **2nd-generation Outposts racks** model where the *customer* configures the physical uplink and BGP. The security guarantees written for the AWS-managed 1st-gen model (AWS owns BGP config) do not transfer. Treat the whole customer-driven path as new surface.

**Request params (create VIF group):**
| Param | Type | Req | Notes |
|---|---|---|---|
| `LocalGatewayId` | String | **Yes** | the LGW to attach the group to |
| `LocalBgpAsn` | Integer | No | local-side BGP ASN (2-byte) |
| `LocalBgpAsnExtended` | Long | No | extended 32-bit local BGP ASN |
| `TagSpecification.N` | Array | No | tag-on-create |
| `DryRun` | Boolean | No | IAM-only check |

**Sibling — CreateLocalGatewayVirtualInterface (the VIF that joins the group):**
`LocalAddress`(req), `LocalGatewayVirtualInterfaceGroupId`(req), `OutpostLagId`(req), `PeerAddress`(req), `PeerBgpAsn`(opt), `PeerBgpAsnExtended`(opt), `Vlan`(req), `TagSpecification`, `DryRun`. → **the entire BGP peering target (peer IP, peer ASN, VLAN, local IP) is set here.**

**Response obj (`LocalGatewayVirtualInterfaceGroup`):** `configurationState` (`pending|incomplete|available|deleting|deleted`), `localBgpAsn`, `localBgpAsnExtended`, `localGatewayId`, `localGatewayVirtualInterfaceGroupArn` (len ≤1283), `localGatewayVirtualInterfaceGroupId`, `LocalGatewayVirtualInterfaceIdSet.N`, `ownerId`, `TagSet`. **`ownerId` is returned → `Describe*` leaks owning account + topology.** No `Modify*` API exists → reconfigure = delete + recreate.

**Resource identifiers.** Opaque service-assigned IDs (`lgw-vif-grp-…`, `lgw-…`, `lgw-vif-…`). ARN: `arn:${Partition}:ec2:${Region}:${Account}:local-gateway-virtual-interface-group/${Id}`.

**Ownership model (concepts, doc-verified).** "AWS creates a local gateway for each Outposts rack… owned by the AWS account associated with the Outposts rack." "An Outposts rack supports a single local gateway." "**Only the owner of a local gateway can create local gateway route tables.**" The LGW/RTB are **RAM-shareable** across accounts in an org (consistent with the broader LGW family — see sibling plans). A **routing domain** = RTB ↔ VIF-group association.

```
 attacker IAM principal (same acct, or RAM-consumer acct?)
        │  CreateLocalGatewayVirtualInterfaceGroup(LocalGatewayId, LocalBgpAsn=?)   ← local ASN, no IAM key
        ▼
   ┌──────────────┐  CreateLocalGatewayVirtualInterface(group, PeerAddress, PeerBgpAsn, Vlan, OutpostLagId)  ← peer target, no IAM key
   │  VIF GROUP   │────────────────▶  VIF(s)  ══BGP/VLAN══▶  on-prem networking device  (physical, customer LAN)
   └──────┬───────┘
          │  CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation  (= routing domain)
          ▼
   ┌──────────────┐  CreateLocalGatewayRoute(dest CIDR → this VIF group)   ← no ec2:Cidr key (sibling plan)
   │  ROUTE TABLE │────────────────▶  steers Outpost-subnet / VPC traffic onto the uplink above
   └──────────────┘
```
The physical hardware + AWS service link are **below** this API's boundary = HARD STOP zone.

---

## 3. API / Interface Inventory

| Name | Mutating | Ext-facing | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|
| **CreateLocalGatewayVirtualInterfaceGroup** | **Yes** | Yes (SDK/CLI) | create VIF group + set local BGP ASN | IAM: 2 legs (see §4) | **no cond key on `LocalBgpAsn*`** |
| CreateLocalGatewayVirtualInterface | Yes | Yes | add VIF (peer IP/ASN/VLAN/LAG) to group | IAM: 3 legs | **no cond key on peer params** |
| DeleteLocalGatewayVirtualInterfaceGroup | Yes | Yes | delete the group | IAM: 1 leg (group only) | asymmetry vs create (Lens X) |
| DeleteLocalGatewayVirtualInterface | Yes | Yes | delete a VIF | IAM: 1 leg | |
| DescribeLocalGatewayVirtualInterfaceGroups | No | Yes | list groups (+`ownerId`, VIF ids, ASN) | — | region-only filterable; x-acct leak? |
| DescribeLocalGatewayVirtualInterfaces | No | Yes | list VIFs (peer config) | — | leaks peer IP/ASN/VLAN |

CloudFormation resource `AWS::EC2::LocalGatewayVirtualInterfaceGroup` exists (mirror `aws-resource-ec2-localgatewayvirtualinterfacegroup.md`) → confirm whether it exposes the same ungated BGP params to a stack-launch role.

---

## 4. Authoritative IAM (from mirror `list_ec2.md`)

**CreateLocalGatewayVirtualInterfaceGroup** (detail L5300-5304) — **2 required resource legs:**
- `local-gateway*` → `{aws:ResourceTag/${k}, ec2:Region, ec2:ResourceTag/${k}}`  *(the LGW being attached to — scopable only by tag/region)*
- `local-gateway-virtual-interface-group*` (the new resource) → `{aws:RequestTag/${k}, aws:TagKeys, ec2:Region}`  *(tag-on-create)*
- Access level: Write. **NO condition key for `LocalBgpAsn` / `LocalBgpAsnExtended`. NO owner/account key. NO `ec2:Attribute`.**

**CreateLocalGatewayVirtualInterface** (detail L5293-5298) — **3 required legs:** `local-gateway-virtual-interface*` {RequestTag,TagKeys,Region}; `local-gateway-virtual-interface-group*` {ResourceTag,Region,ResourceTag}; `outpost-lag*` {ResourceTag,Region,ResourceTag}. **NO condition key for `PeerAddress`, `PeerBgpAsn*`, `LocalAddress`, `Vlan`.**

**DeleteLocalGatewayVirtualInterfaceGroup** (detail L6034-6038) — **1 leg:** `local-gateway-virtual-interface-group*` {aws:ResourceTag, ec2:Region, ec2:ResourceTag}.

**ARNs** (L9973-9974): `local-gateway-virtual-interface` and `local-gateway-virtual-interface-group` expose only `{aws:RequestTag, aws:ResourceTag, aws:TagKeys, ec2:Region, ec2:ResourceTag}`. No BGP/ASN/peer/VLAN-valued keys anywhere in the family.

---

## 5. Recommended Areas of Focus (one block per firing lens)

### Area 1 — BGP identity (local & peer ASN, peer IP, VLAN) is inexpressible in IAM  [Lens S + U, CROWN, High]
**Background.** The VIF group carries `LocalBgpAsn`/`LocalBgpAsnExtended`; the member VIF carries `PeerAddress`/`PeerBgpAsn*`/`Vlan`/`LocalAddress`. Together these fully define the BGP session the Outpost establishes toward an on-prem device.
**Security Concern.** **None of these values has a corresponding IAM condition key.** An administrator who grants `ec2:CreateLocalGatewayVirtualInterfaceGroup` (+ `…VirtualInterface`) scoped by tag/region **cannot** express "only ASN 64512" or "only peer 10.0.0.0/8 / VLAN 100." A permitted principal can set an **arbitrary local ASN** and point a VIF at an **arbitrary peer IP/ASN** — standing up an unexpected or rogue BGP session, impersonating a BGP identity, or (if the on-prem side peers loosely) injecting/withdrawing routes. This mirrors `CreateCustomerGateway` (BgpAsn inexpressible) and `AssociateRouteServer` (no PeerAddress/Asn key → BGP hijack) in the same corpus.
**High-level Test Scenarios.**
- **Claim:** a role allowed to create VIF groups can set any `LocalBgpAsn`, including one that collides with / impersonates the on-prem network's expected ASN. → **Oracle:** create two groups with different ASNs under a tag-scoped role; both succeed = IAM cannot bound the value. → Sev High.
- **Claim:** a VIF can be created toward an attacker-chosen `PeerAddress` with a crafted `PeerBgpAsn`, no allowlist. → **Oracle:** `CreateLocalGatewayVirtualInterface` with a peer IP outside any sanctioned range returns 200 / `configurationState: pending`. → **STOP before the session actually peers to live on-prem** — existence of acceptance is the PoC.
- **Claim:** there is **no BGP authentication (MD5/TCP-AO) parameter** in the API → no way to require authenticated peering. → **Oracle:** confirm param absence in API model (done, doc-confirmed). File as missing-control.
**Doc evidence.** API params `LocalBgpAsn`/`PeerBgpAsn`/`PeerAddress`/`Vlan`; IAM detail L5293-5304 (no matching keys). Severity-if-true: **High** (on-prem routing-identity manipulation; Critical if it reaches another account's rack or AWS service link — HARD STOP).

### Area 2 — Create-vs-Delete leg asymmetry → tear-down the physical uplink you can't build  [Lens X, High]
**Background.** Create requires the `local-gateway*` leg **plus** the new-group leg. Delete requires **only** the `local-gateway-virtual-interface-group*` leg. No `Modify*` exists.
**Security Concern.** A Deny/scope written on the `local-gateway` resource (e.g. "you may not create VIF groups on the prod LGW") does **not** constrain Delete, which never references `local-gateway`. A principal who can reach the group by its tag can **delete the VIF group** — removing the container for all member VIFs → drops the BGP sessions → **on-prem connectivity blackhole for the entire local gateway** (one LGW per rack). No Modify means the only reconfigure path is delete+recreate, so a delete-only principal is purely destructive.
**High-level Test Scenarios.**
- **Claim:** a role denied `CreateLocalGatewayVirtualInterfaceGroup` on LGW-A (via the local-gateway leg) can still `Delete` the group if it matches the group's `aws:ResourceTag`. → **Oracle:** `SimulatePrincipalPolicy` both actions under the scoped role: create=Deny, delete=Allow. → Sev High (denial-of-resilience).
- **Claim:** deleting the group cascades to drop member VIFs / the routing-domain association (resilience loss beyond the group itself). → **Oracle:** doc/`configurationState`→`deleting`; confirm whether Delete is blocked while VIFs/associations exist or forces cascade.
**Doc evidence.** IAM detail L5300-5304 (create 2 legs) vs L6034-6038 (delete 1 leg). Severity-if-true: **High**.

### Area 3 — No LGW↔VIF-group pairing/ownership key; shared-tag + self-widen  [Lens S/I, Med-High]
**Background.** Create's only control over *which* LGW is `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Region` on `local-gateway`. The new group is governed by `aws:RequestTag`/`aws:TagKeys` (tag-on-create).
**Security Concern.** You cannot express "VIF-group may only be created on LGW-X" except via a shared tag value — so in any environment where multiple LGWs (or a shared-tag convention) exist, an allowed principal can attach a VIF group to **any tag-matching LGW**. And because the creator chooses the new group's tags (`aws:RequestTag`), it can pick a tag value that its **own future `aws:ResourceTag`-keyed Delete** (Area 2) will match → **self-widen** the blast radius / guarantee its own teardown path.
**High-level Test Scenarios.**
- **Claim:** a tag-scoped create role can self-assign a group tag that satisfies a separate `ec2:ResourceTag`-gated Delete grant. → **Oracle:** create with `TagSpecification` = the gating tag; then Delete allowed. → Sev Med-High.
- **Claim:** no key binds a specific group to a specific LGW → any permitted LGW accepts a new group. → **Oracle:** policy analysis; confirm absence of a `local-gateway`-id/pairing key. → Sev Med.
**Doc evidence.** IAM ARNs L9973-9974; detail L5300-5304. Severity-if-true: Medium (High where tags are the sole access mechanism).

### Area 4 — RAM-shared local gateway → cross-account VIF-group create/delete  [Lens A/AA, TOP GAP, High→Critical if x-acct]
**Background.** LGWs and LGW route tables are RAM-shareable across an org (family-wide; see sibling plans). The concepts page states route-table creation is owner-only — **but is silent on who may create/delete VIF groups and VIFs.** `Describe*` returns `ownerId` + VIF ids + ASN → x-account topology disclosure.
**Security Concern.** Create keys on `local-gateway` *ResourceTag* — if the LGW is RAM-shared and the consumer can tag-match it (or the share conveys the resource into the consumer's policy evaluation), a **consumer account may create a VIF group / VIF on the owner's physical gateway**, injecting a BGP session the owner never configured. Delete needs only the group leg → a consumer who can reach the group could tear it down. The owner-only guarantee is documented **only for route tables**, leaving VIF-group/VIF authorship a doc-gap.
**High-level Test Scenarios.**
- **Claim:** a RAM-consumer principal can `CreateLocalGatewayVirtualInterfaceGroup`/`…VirtualInterface` against the owner's shared LGW. → **Oracle:** from the consumer account, `SimulatePrincipalPolicy` / minimal create; a 200 or Allow on the owner's `lgw-…` = cross-account physical-uplink write. → **HARD STOP + disclosure if confirmed** (crosses account boundary on AWS-owned hardware).
- **Claim:** `DescribeLocalGatewayVirtualInterfaceGroups`/`…Interfaces` from a consumer leaks the owner's `ownerId`, BGP ASNs, peer IPs. → **Oracle:** describe from consumer; non-empty foreign result. → Sev Med (disclosure), enabler for the above.
**Doc evidence.** concepts "owned by the AWS account associated with the rack"; "Only the owner … can create local gateway route tables" (VIF-group creation *not* so qualified); response `ownerId`. Severity-if-true: **Critical** (x-account physical-uplink control).

### Area 5 — Routing-domain kill chain (compose with siblings)  [chain, rate at end = High-Critical]
**Background.** This action is step 1 of: VIF group (local ASN) → `CreateLocalGatewayVirtualInterface` (peer IP/ASN/VLAN, attacker-chosen) → `CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation` (binds group to an RTB = a *routing domain*) → `CreateLocalGatewayRoute` (no `ec2:Cidr` key per sibling plan; static > propagated) → steer a victim CIDR onto the attacker's VIF group.
**Security Concern.** An attacker who holds the (tag-scoped, BGP-value-unconstrained) create permissions across the family can **stand up a parallel uplink to an attacker-controlled on-prem peer and repoint a victim destination CIDR onto it** — targeted interception/exfil of Outpost↔on-prem traffic (private-IP mode preserves dest IP, no NAT). Because no step exposes a value-level condition key (ASN, peer IP, CIDR), IAM cannot break the chain mid-way; only server-side owner-enforcement can.
**High-level Test Scenarios.**
- **Claim:** the four creates can be issued end-to-end under one tag-scoped role with no value-level Deny stopping them. → **Oracle:** `SimulatePrincipalPolicy` the whole chain; all Allow = chain is IAM-unbreakable. → **Model the on-prem interception; do not fire route injection at live infrastructure.**
**Doc evidence.** this API + sibling plans. Severity-if-true: **High-Critical** (data-plane interception).

### Area 6 — Doc-vs-capability gap (1st-gen prose vs 2nd-gen customer BGP APIs)  [Lens U, Low-Info, AWS-owned]
**Background.** Concepts page: *"AWS creates the virtual interfaces (VIFs) and a VIF group"* listed under **AWS responsibilities**; "Your responsibilities" lists only route-table / VPC-association / VIF-group-association. Yet `CreateLocalGatewayVirtualInterfaceGroup` + `CreateLocalGatewayVirtualInterface` are customer-callable with full BGP config (2nd-gen Outposts).
**Security Concern.** A customer/operator reading the concepts page will believe BGP/VIF config is AWS-managed and un-attackable, and may build a compliance/attestation assumption on it — while the API in fact lets any suitably-permitted principal configure the physical uplink's BGP. The security model written for the managed path does not cover the self-service path.
**Oracle.** Pure doc-vs-API inconsistency (already confirmed from the two pages). File as Informational/Low to AWS-docs; it *raises* the priority of Areas 1–5 because the self-service surface is under-documented. Severity: Low-Informational (AWS-owned).

### Area 7 — Network-segmentation / data-path reachability  [Lens V, scoping only]
**Background.** "The local gateway can also provide a data plane path back to the AWS Region … traverses from the Outpost, through the local gateway, and to your private local gateway LAN segment … private path back to the AWS service endpoints." Control plane always uses the service link.
**Security Concern (bounded).** A crafted VIF/BGP session could attempt to influence the Region-bound data path or reach the service link. **This is the HARD-STOP frontier** — the service link and AWS endpoints are AWS's service plane. Model only; any confirmed reach = disclosure. Not a free-fire area.
**Severity-if-true:** Critical + HARD STOP (service-plane reach).

---

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Set arbitrary local/peer BGP ASN, peer IP, VLAN | VIF group + VIF | *(none in IAM — no value-level condition key)* |
| Delete a VIF group a principal can't create | Delete action | tag-scoped `aws:ResourceTag` only (Create's local-gateway leg does not apply) |
| Attach VIF group to a non-intended LGW | Create | `aws:ResourceTag`/`ec2:ResourceTag` on `local-gateway` (no id/pairing key) |
| Cross-account create/delete on RAM-shared LGW | Create/Delete | "owned by the account associated with the rack"; route-table-only owner statement (VIF-group gap) |
| Self-widen via tag-on-create → own Delete path | Create `TagSpecification` | `aws:TagKeys`/`aws:RequestTag` (does not prevent choosing the gating tag) |
| End-to-end routing-domain interception chain | VIF group→VIF→assoc→route | server-side owner enforcement only; no value-level IAM keys anywhere |
| Rogue BGP session reaches AWS service link / Region path | data plane | service link / AWS endpoints = service plane (HARD STOP) |

---

## 7. Out-of-Scope Risk Categories
- Shared Outposts physical networking hardware, the AWS service link, and AWS-owned local gateways belonging to other accounts' racks — **HARD STOP / disclosure**, not free testing.
- Single-tenant self-DoS (deleting your *own* VIF group / exhausting your own VIF-group or 10-routing-domain quota).
- Customer-authored IAM policies that are merely over-broad (customer footgun) — in scope **only** if a weak default ships in an AWS-managed/sample artifact.
- Actual BGP route injection / withdrawal against live on-premises infrastructure (destructive — model, do not execute).
- IMDS, host-level, and physical attacks on the Outpost rack.

## 8. Null hypotheses / doc gaps
- **G (SSRF), B/C (PassRole/vending), H (KMS), K (LLM), Q (upload), W (attestation), DD (cache), CC (upstream-context), FF (JWT), N (namespace), BB (canonicalization), M (session-id):** N/A — checked the create + sibling VIF API pages, the VIF-group object schema, and the IAM detail; this is a 2-opaque-ID + BGP-integer + tag routing verb. No URL/blob/role-ARN/KMS-key/token/LLM/cache/JWT/upstream-header field anywhere.
- **T (secret reachability):** weak — no generated secret persisted; **but** note there is **no BGP MD5/TCP-AO auth parameter** in the API at all (missing control, filed under Area 1), so there is no secret to misplace.
- **O (audit):** relevant but low — confirm CloudTrail captures `CreateLocalGatewayVirtualInterfaceGroup`/`…VirtualInterface` with the BGP params, and whether a silent delete+recreate (no Modify) is distinguishable in the trail. Enabler, not a standalone finding.
- **EE (predictable-name land-grab):** N/A — IDs are service-assigned opaque, not a global/predictable namespace.
- **Open doc gaps requiring live/surface confirmation first:** (1) who (owner vs RAM-consumer) may create/delete VIF groups and VIFs — concepts page only states route-table creation is owner-only [Area 4, TOP]; (2) whether Delete cascades or is blocked while VIFs/associations exist [Area 2]; (3) whether 2nd-gen customer-driven BGP is gated server-side beyond IAM [Areas 1,5]; (4) CloudFormation `AWS::EC2::LocalGatewayVirtualInterfaceGroup` param exposure; (5) quota on VIF groups per LGW / per routing domain.
```
