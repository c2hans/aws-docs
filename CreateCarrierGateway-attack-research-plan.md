# CreateCarrierGateway — Attack Research Plan

Source of leads: `API_CreateCarrierGateway.html`, `API_DeleteCarrierGateway.html`, `API_DescribeCarrierGateways.html`, `API_CarrierGateway.html`, `API_CreateRoute.html` (online + offline mirror), `service-authorization/.../list_ec2.md` (lines 5045–5049 Create, 5836–5840 Delete, 6702–6706 Describe, 5403–5407 CreateRoute, 9927 resource ARN), and AWS Wavelength Developer Guide `how-wavelengths-work.html`. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (or the telco/CSP carrier fleet), stop, preserve evidence, flag for AWS-Security disclosure.
- **Framing correction up front:** a carrier gateway is **single-account, single-VPC, not RAM-shareable** (resource carries `ownerId`; Describe is "describe one or more of *your* carrier gateways"). The headline risk here is **NOT cross-tenant IDOR**. It is **an intra-account IAM-scoping / network-isolation question**: the carrier gateway is a NAT bridge from a Wavelength-Zone VPC to the **4G/5G telecommunication carrier network and the public internet**, and the IAM surface around creating/routing/deleting it governs who can open or sever that bridge.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes a hunter should try to produce:
1. Attach a carrier gateway to a VPC that policy intended to keep off the carrier/internet, using a principal whose grant the operator *believed* was scoped (prove the VPC-selection guardrail is inert or absent).
2. From a principal scoped only to a route table, install a `0.0.0.0/0 → cgw-*` default route sending all Wavelength-subnet traffic to the carrier network/internet, with no IAM key able to forbid that target.
3. Create a carrier gateway tagged so the creator can later delete/modify it despite an ABAC deny (tag-on-create self-widen).
4. Delete a carrier gateway (or a route pointing at it) to blackhole a Wavelength Zone's egress — a DoS reachable without route-table write.
5. Enumerate every carrier gateway (and its `ownerId`/`vpcId`/tags) in the account from a principal the operator assumed could not (Describe has no resource-level authz).

---

## 2. Components, Assets, and Design

**Mechanism (not marketing).** A *carrier gateway* (`cgw-…`, ARN `arn:${Partition}:ec2:${Region}:${Account}:carrier-gateway/${CarrierGatewayId}`) is a VPC-attached gateway object, valid **only** for VPCs that contain a subnet in a **Wavelength Zone**. It performs **NAT** between Wavelength instance private IPs and **Carrier IP addresses** drawn from a *network border group* (e.g. `us-east-1-wl1-bos-wlz-1`) and is the egress/ingress point to the **telecommunication carrier (CSP) network** and the **public internet**.
- Inbound: traffic from the carrier network (4G/LTE/5G devices). **No inbound from the public internet** through the CGW.
- Outbound: to the carrier network and the internet.
- It is referenced as a **route target** in a route table (`0.0.0.0/0 → cgw-…`).

**Assets / identifiers.**
- `CarrierGatewayId` — server-assigned `cgw-` id (opaque, checksum-bearing — not attacker-fabricable).
- `ownerId` — account ID of the owner (returned by Describe).
- `state` — pending | available | deleting | deleted (API also filters `failed`).
- `TagSet`, `VpcId`.

**Trust zones.** Customer account/VPC (control of VPC networking) ↔ **AWS Wavelength Zone infrastructure** ↔ **telco carrier network (CSP)** ↔ **public internet**. The CGW is the object that bridges the first zone to the last three.

**ASCII pipeline (from the Wavelength guide routing example):**
```
[EC2 in Wavelength-Zone subnet] --(private IP)--> [Wavelength subnet route table]
      route: VPC_CIDR -> local
      route: 0.0.0.0/0 -> cgw-xxxx   <-- the bridge
                                  |
                          [Carrier Gateway]  (NAT: private IP -> Carrier IP from network border group)
                                  |
             +--------------------+--------------------+
             v                                         v
   [Telco carrier network: 4G/5G devices]     [Public internet]
```

**Control-plane API surface (all SigV4 EC2 Query API, `ec2-2016-11-15`):** `CreateCarrierGateway`, `DeleteCarrierGateway`, `DescribeCarrierGateways`. Routing is done with the generic `CreateRoute`/`ReplaceRoute`/`DeleteRoute` (CGW passed via the `CarrierGatewayId` route-target parameter). CloudFormation resource: `AWS::EC2::CarrierGateway` (VpcId + Tags).

**Mandatory coverage sweep result.** Pages read: the three CGW API pages, `API_CarrierGateway` data type, `API_CreateRoute`, the Wavelength `how-wavelengths-work` guide, and the IAM reference rows. No field here is a URL/URI/host the service dereferences (→ SSRF N/A), no upload/blob field (→ upload N/A), no identity-proofing code/gate (→ Lens P N/A), no crypto/attestation gate (→ H/W N/A), no JWT/token (→ FF N/A). The live surface is **three thin control-plane verbs + one shared route verb**, so the whole plan concentrates on IAM-scoping (R/S/I/X), network-isolation semantics (V/D), the Create→Route kill-chain, and lifecycle/DoS (L/AA).

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| IAM principal w/ `ec2:CreateCarrierGateway` | A specific customer VPC | CreateCarrierGateway(VpcId) | A CGW attached to a VPC the principal's policy was *written* to exclude (VPC-scoping key inert/absent) = breach of the intended guardrail |
| Wavelength-Zone subnet (data plane) | Telco carrier network + public internet | CGW NAT + `0.0.0.0/0 → cgw` route | Egress reaching the carrier/internet from a subnet the design intended to keep private, enabled by a route a route-table-scoped principal installed |
| IAM principal w/ `ec2:CreateRoute` (route-table scoped) | *Any* CGW as route target | CreateRoute(CarrierGatewayId) | Route created pointing at a CGW the principal could not restrict — no `ec2:CarrierGatewayId` key exists on CreateRoute |
| Creator of CGW | Later Delete/Modify ABAC gate | `aws:RequestTag` at create vs `aws:ResourceTag` at delete | Delete succeeds under a tag the creator themselves set = self-widen |
| Principal w/ `DeleteCarrierGateway` (no `DeleteRoute`) | Wavelength Zone egress availability | Delete CGW → dangling route becomes blackhole | Zone-wide egress outage with no route-table permission |
| Principal w/ `ec2:DescribeCarrierGateways` | All CGWs in account (ownerId/vpcId/tags) | Describe (Resource:\*, region-only) | Inventory of every CGW returned where operator believed it was ABAC-restricted |
| Any customer surface | **AWS Wavelength / CSP service plane** | — | **HARD STOP** — any CSP/AWS fleet identity, Carrier IP pool internals, or cross-account CGW = disclosure |

---

## 4. API / Interface Inventory

| Name | Method | New/Exist | Mutating | Int/Ext | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| CreateCarrierGateway | POST (Query) | Existing | **Yes** | External | Create CGW, bridge VPC→CSP/internet | Yes (SigV4) | Account principals w/ `ec2:CreateCarrierGateway` | **Two required legs:** `carrier-gateway*` (keys: `aws:RequestTag`, `aws:TagKeys`, `ec2:Region`) **and** `vpc*` (keys: `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag`, `ec2:Tenancy`, **`ec2:VpcID`**). `ClientToken` not a condition key. |
| DeleteCarrierGateway | POST (Query) | Existing | **Yes** | External | Delete CGW | Yes | Principals w/ `ec2:DeleteCarrierGateway` | `carrier-gateway*`; keys: `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag`. Dangling route → blackhole. |
| DescribeCarrierGateways | POST (Query) | Existing | No | External | List CGWs + ownerId/vpcId/tags | Yes | Principals w/ `ec2:DescribeCarrierGateways` | **No resource types (Resource:\*); only `ec2:Region`.** Filters incl. `owner-id`, `vpc-id`, `state`, `tag:`. No ABAC possible. |
| CreateRoute / ReplaceRoute / DeleteRoute | POST (Query) | Existing | **Yes** | External | Route `0.0.0.0/0 → CarrierGatewayId` | Yes | Principals w/ route-write | **CreateRoute authorizes only `route-table*`; keys bind the route table (`ec2:Vpc`, `ec2:RouteTableID`, tags) — NO key for the route TARGET and NO destination-CIDR key.** The CGW target is unconstrainable. |

Undocumented/console-hidden knob sweep: none weakening auth (no `authType`-style enum; CGW has no inbound-from-internet config by design). CloudFormation `AWS::EC2::CarrierGateway` only exposes `VpcId` + `Tags`.

---

## 5. Recommended Areas of Focus

### Area 1 — Create→Route kill-chain: unconditioned carrier/internet egress (Lens X + V + D) — PRIORITY
**Background.** The sole documented purpose of CreateCarrierGateway is to "provide CSP connectivity to VPC customers." Opening that bridge requires two steps: create the CGW, then point a route at it. Routing uses the generic `CreateRoute`, whose IAM authorizes **only the `route-table*` resource** with keys that describe the route *table* (`ec2:Vpc`, `ec2:RouteTableID`, tags) — there is **no `ec2:CarrierGatewayId` key and no destination-CIDR key** (list_ec2.md L5403–5406; API_CreateRoute `CarrierGatewayId` param).
**Security Concern.** A principal holding `ec2:CreateCarrierGateway` + `ec2:CreateRoute` (even scoped to one route table) can install `0.0.0.0/0 → cgw-*`, routing every Wavelength-subnet's traffic out to the telco carrier network and public internet. **No IAM policy can express "this route table may not default-route to a carrier gateway"** or "only to this specific CGW." Network isolation intended by the operator is not expressible in IAM.
**High-level Test Scenarios.**
- Claim: *A route-table-scoped principal can repoint a Wavelength subnet's default route to an arbitrary CGW.* → Oracle: `CreateRoute(RouteTableId=<scoped rt>, DestinationCidrBlock=0.0.0.0/0, CarrierGatewayId=<any cgw in acct>)` returns 200 and the route appears. → Refute: an `ec2:CarrierGatewayId`-style key denies it (it does not exist).
- Claim: *No condition key restricts which CGW / which destination a route may target.* → Oracle: `iam:SimulateCustomPolicy` on CreateRoute with every candidate key — confirm none scope the target.
**Doc evidence:** list_ec2.md L5403–5406; API_CreateRoute (`CarrierGatewayId`); Wavelength routing example (`0.0.0.0/0 → carrier-gateway-id`). **Severity-if-true:** High (intra-account network-isolation bypass / data-egress path to carrier+internet).

### Area 2 — CROWN: no condition key constrains the carrier/CSP exposure itself (Lens S + U)
**Background.** CreateCarrierGateway's `carrier-gateway*` leg offers only `aws:RequestTag`, `aws:TagKeys`, `ec2:Region`. The *decision to bridge a VPC to the carrier network* carries no key for the network border group, the Carrier IP pool, or any "may-connect-to-CSP" attribute.
**Security Concern.** Once a principal may create a CGW on a VPC, the resulting exposure (which CSP border group, what egress reach) is **unconditioned** — the only guardrail is the binary "may you create a CGW on this VPC at all," expressed on the *vpc* leg. There is no least-privilege middle ground.
**High-level Test Scenarios.**
- Claim: *No key limits the network border group / Carrier IP pool a CGW draws from.* → Oracle: enumerate CreateCarrierGateway keys via SimulatePrincipalPolicy; confirm absence.
- Claim (guarantee trace, Lens U): *The doc promise "provides CSP connectivity to VPC customers" is enforced only by holding the action on a VPC, nothing finer.* → trace to mechanism: it is IAM-action presence + the vpc leg keys, not any CSP-scoping condition.
**Doc evidence:** list_ec2.md L5047 (carrier-gateway leg keys); CGW description L5046. **Severity-if-true:** Informational→Medium (least-privilege expressiveness gap; AWS-owned key-coverage, not a customer footgun).

### Area 3 — VPC-selection scoping: `ec2:VpcID` vs `ec2:Vpc` key-name divergence (Lens S fail-open)
**Background.** CreateCarrierGateway's *vpc* leg scopes VPC selection with **`ec2:VpcID`** (capital-D id key), plus `ec2:Tenancy`, `ec2:ResourceTag`, `ec2:Region` (L5048). Most other VPC-child actions and the carrier-gateway *resource definition* (L9927/L5498) use **`ec2:Vpc`** (the ARN-parent key). These are two distinct IAM keys.
**Security Concern.** An operator who writes a policy `Condition: {StringEquals: {"ec2:Vpc": "...vpc/vpc-abc"}}` intending to confine CreateCarrierGateway to one VPC may find **`ec2:Vpc` is not offered on the create legs** — only `ec2:VpcID` is — so the condition is evaluated against an absent key and (depending on operator) **silently fails open**, allowing the CGW to be attached to *any* VPC. This is the catalog's "key that does not exist on this action / wrong key name → inert guardrail" shape (cf. `ec2:InterfaceType`, `ec2:Vpc`-binds-wrong-resource precedents in prior EC2 hunts).
**High-level Test Scenarios.**
- Claim: *A Deny/Allow written with `ec2:Vpc` does not constrain CreateCarrierGateway's VPC target; only `ec2:VpcID` does.* → Oracle: SimulateCustomPolicy, one policy keyed on `ec2:Vpc`, one on `ec2:VpcID`, against `CreateCarrierGateway` for two different VpcIds — confirm only `ec2:VpcID` changes the decision.
- Adjacent: confirm whether `ec2:VpcID` is value-validated (ARN vs bare id fail-open — a prior EC2 finding).
**Doc evidence:** L5048 (`ec2:VpcID` on create) vs L9927/L5498 (`ec2:Vpc` on resource). **Severity-if-true:** Medium (fail-open VPC scoping → Area-1 exposure on an unintended VPC).

### Area 4 — Tag-on-create self-widen + Create/Delete ABAC asymmetry (Lens I + X)
**Background.** CreateCarrierGateway accepts `aws:RequestTag`/`aws:TagKeys` on the carrier-gateway leg. DeleteCarrierGateway is gated by `aws:ResourceTag`/`ec2:ResourceTag` (L5839).
**Security Concern.** If the operator protects deletion with an ABAC condition (e.g. Deny Delete unless `ResourceTag/Protected=false`, or Allow Delete only when `ResourceTag/Team=${principal-team}`), the **creator sets that very tag at create time** → self-grants delete/modify authority the ABAC policy intended to withhold. Create-twin vs Delete-twin key asymmetry.
**High-level Test Scenarios.**
- Claim: *A principal can create a CGW with a tag that satisfies the delete-side ABAC gate it otherwise fails.* → Oracle: create with `TagSpecification` setting the gating key/value; then Delete succeeds. → Refute: tag-on-create is denied (no `aws:RequestTag` enforcement) or Delete re-checks an immutable attribute.
- Adjacent: can the creator also set `aws:TagKeys` to inject `aws:`-prefixed or reserved keys? Does tag validation bound this?
**Doc evidence:** L5047 (RequestTag on create) vs L5839 (ResourceTag on delete). **Severity-if-true:** Medium (ABAC bypass; High only if tags are the sole access-control mechanism).

### Area 5 — Delete → blackhole-route DoS (Lens L + AA revocation-completeness)
**Background.** DeleteCarrierGateway doc: *"If you do not delete the route that contains the carrier gateway as the Target, the route is a blackhole route."* Delete requires only the `carrier-gateway*` resource — **no route-table permission**.
**Security Concern.** A principal with `ec2:DeleteCarrierGateway` (scoped by tag, see Area 4 self-widen) but **no** `ec2:DeleteRoute`/route-table write can delete the CGW and leave every Wavelength-subnet default route a **blackhole** — a zone-wide egress outage. Revocation (delete) does not cascade to the dependent route reference; the stale route survives pointing at a deleted target. Also create/delete churn and the non-identity-bound `ClientToken` (idempotency, not a condition key → double-create race).
**High-level Test Scenarios.**
- Claim: *Deleting a CGW while a `0.0.0.0/0 → cgw` route exists silently blackholes the subnet with no route-table permission required.* → Oracle: delete; observe the route's state become `blackhole` and egress stop; confirm the deleting principal held no route write.
- Claim: *`ClientToken` is not identity-bound* → two concurrent creates with distinct tokens → duplicate CGWs (quota/DoS). Low.
**Doc evidence:** API_DeleteCarrierGateway "Important" note; L5838–5839. **Severity-if-true:** Medium intra-account DoS (High if the principal shouldn't control that prod/shared VPC's egress).

### Area 6 — DescribeCarrierGateways has no resource-level authz (Lens U + A recon)
**Background.** DescribeCarrierGateways lists **no resource types** (Resource:\* effectively) and only the `ec2:Region` condition key (L6704–6705). Filters include `owner-id`, `vpc-id`, `state`, `tag:`.
**Security Concern.** Any principal granted `ec2:DescribeCarrierGateways` can enumerate **every** CGW in the account, including `ownerId`, `vpcId`, and tags — there is **no way to ABAC-restrict Describe** to specific CGWs or tag sets. This is the standard EC2 Describe pattern (account-scoped, so not cross-tenant), but it is a recon surface that defeats any assumption that read access was confined.
**High-level Test Scenarios.**
- Claim: *A principal intended to see only tagged CGWs sees all of them.* → Oracle: SimulateCustomPolicy with `aws:ResourceTag` condition on DescribeCarrierGateways — confirm the key has no effect (not in the key list).
- Adjacent (Lens A oracle): does the `owner-id` filter ever return a foreign account's CGW, or is it strictly self-owned? Confirm Describe is account-bound server-side (expected null, but verify — do NOT exploit beyond existence).
**Doc evidence:** L6704–6706; API_DescribeCarrierGateways filters. **Severity-if-true:** Low/Informational (intra-account recon; account-scoped).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Route-write principal opens carrier/internet egress on any CGW | CreateRoute + CGW | CreateRoute has no target/CIDR key → mitigation absent |
| Policy author scopes CGW to one VPC with `ec2:Vpc` | CreateCarrierGateway vpc leg | Only `ec2:VpcID` offered → `ec2:Vpc` condition inert |
| Creator self-grants delete via tag-on-create | Create vs Delete ABAC | `aws:RequestTag` at create vs `aws:ResourceTag` at delete |
| CGW delete blackholes Wavelength Zone egress | DeleteCarrierGateway | No cascade to dependent route; no route perm needed |
| Read access confined to tagged CGWs | DescribeCarrierGateways | No resource-level key → cannot ABAC-restrict |
| Carrier/CSP exposure scoped per border group | CreateCarrierGateway | No border-group/Carrier-IP-pool condition key |

---

## 7. Out-of-Scope Risk Categories
- **Cross-account / cross-tenant CGW access** — carrier gateway is single-account, single-VPC, not RAM-shareable; `ownerId` + "describe your carrier gateways" ⇒ account-bound. (Confirm RAM-shareability once against the live RAM resource list before fully closing.)
- **The AWS Wavelength / CSP service plane** — any CSP fleet identity, Carrier IP pool internals, or telco-side reachability = **HARD STOP**, disclosure.
- `cgw-` ID enumeration — server-assigned, checksum-bearing → foreign ids not fabricable (genuine null).
- DryRun as an ownership oracle — caller-IAM only, evaluated before resource resolution (false-positive trap).
- Single-tenant self-DoS from create/delete churn beyond the blackhole case.
- IMDS / data-plane behavior on managed Wavelength hosts.

## 8. Null hypotheses / doc gaps
- **Lens A/N/EE (cross-tenant, migration, predictable-name):** NULL — single-account resource, server-assigned checksummed id, no global namespace, no dual ARN namespace. (Checked: all three CGW API pages, CarrierGateway data type, ARN format L9927.)
- **Lens G (SSRF):** NULL — no field the service dereferences. (Checked: Create/Delete/Describe API pages, CarrierGateway type, Wavelength guide — no `*Url`/`*Uri`/host/endpoint field.)
- **Lens Q (upload):** NULL — no blob/file/image field. (Checked: same pages + CFN `AWS::EC2::CarrierGateway` = VpcId+Tags only.)
- **Lens K/F (prompt/translation injection):** NULL — no LLM, no parser/translation layer; VpcId is an opaque id.
- **Lens H/W (KMS/attestation):** NULL — no encryption context or attestation gate on this action.
- **Lens P (proofing):** NULL — no registration/OTP/uniqueness gate. (Checked: Create API page.)
- **Lens B/C (PassRole/vending):** NULL — no role ARN input, no credential vending. CGW assumes no customer role.
- **Lens Y/BB/CC/DD/FF (transport, canonicalization, upstream-context, cache, JWT):** NULL for this SigV4 Query-API control-plane verb — no multi-parser request path, no token, no cache layer.
- **Doc gap:** the Wavelength guide describes CGW NAT and "inbound traffic from a carrier network" but does not specify whether a CGW's inbound carrier-side reach can be scoped per network border group — mark "doc-gap — confirm border-group scoping on the live control plane" (feeds Area 2).

---

### Priority order for the hunter
1. **Area 1** (Create→Route unconditioned egress — the real network-isolation bug, High).
2. **Area 3** (`ec2:Vpc` vs `ec2:VpcID` fail-open VPC scoping, Medium).
3. **Area 4** (tag-on-create self-widen → delete, Medium).
4. **Area 5** (blackhole-route DoS, Medium).
5. **Area 2** (no CSP/border-group key, Info→Medium, AWS-owned key coverage).
6. **Area 6** (Describe no ABAC, Low/recon).

Safe first oracle for every IAM lead: `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` (touches no resources). Escalate to a live scoped call only with a dedicated low-priv role and a canary Wavelength-opted VPC; tear down the CGW and any route immediately after.
