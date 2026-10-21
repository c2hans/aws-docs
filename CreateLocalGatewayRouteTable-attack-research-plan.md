# CreateLocalGatewayRouteTable — Attack Research Plan

Source of leads: AWS EC2 API Reference `API_CreateLocalGatewayRouteTable.html` + `API_LocalGatewayRouteTable.html` + `API_DeleteLocalGatewayRouteTable.html`; IAM/Service-Authorization mirror `/work/list_ec2.md` (authoritative — online SAR is JS-rendered and returned empty, trust the mirror); Outposts userguide `routing.md`, `sharing-outposts.md`, `network-userguide/routing-domains.md`; CloudFormation `aws-resource-ec2-localgatewayroutetable.md`.
Status: **documentation-derived hypotheses only; nothing tested against a live account.** Outposts hardware required to confirm most leads.
Analyst note: This is the **container-creation** verb (the LGW *route table* itself), sibling to the route-level [[ec2-createlocalgatewayroute-surface]] plan (`/work/CreateLocalGatewayRoute-attack-research-plan.md`) and the CoIP chain ([[ec2-createcoipcidr-surface]], [[ec2-createcoippool-surface]]). Where the route-level plan's jewel was "no `ec2:Cidr` dest key," this container's jewel is **"no condition key for `Mode`, and `Mode` is immutable"** — a higher-leverage gap because `Mode` governs auto-propagation of *all* associated-VPC CIDRs, not one route.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **DryRun is NOT an ownership oracle** — it is evaluated on caller IAM before resource resolution (false-positive trap). Safe authz oracle = `iam:SimulatePrincipalPolicy` / `SimulateCustomPolicy`.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the Outpost-owner *service* account, the LGW control plane, a VIF/BGP control identity), stop, preserve evidence, flag for AWS-Security disclosure. Cross-**customer-account** reach on a shared Outpost is in-scope and reportable; the AWS fleet plane is the wall.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. As a principal holding a **tag/region-scoped** `CreateLocalGatewayRouteTable` grant, create a route table in a `Mode` the account's governance intended to forbid (e.g. force `direct-vpc-routing` when policy wanted `coip`, or vice-versa) — proving `Mode` is not IAM-constrainable.
2. As a **RAM consumer** of a shared LGW route table, associate a VPC and cause the consumer's (or another party's) VPC CIDRs to be advertised to the **owner's on-premises network** via BGP — a cross-account routing-exposure the consumer could not achieve directly.
3. Break the second-gen **routing-domain isolation** invariant ("a VPC is exclusively associated with one routing domain per Outpost") by creating/associating so a VPC bridges two domains.
4. Using only `DeleteLocalGatewayRouteTable` authority (no authority over the parent local-gateway), **tear down** a route table and blackhole an Outpost's on-prem connectivity (teardown asymmetry).
5. Enumerate another account's route tables, `ownerId`, `mode`, and `outpostArn` via region-only `Describe*` (cross-account recon on a shared Outpost).
6. Determine what `CreateLocalGatewayRouteTablePermission` (Permissions-management, no public API page) actually grants and whether it over-shares a route table to a service/principal without a scoping condition key.

---

## 2. Components, Assets, and Design

**What it is.** `CreateLocalGatewayRouteTable` creates the route-table *container* bound to one **local gateway** (`LocalGatewayId`, required) on an AWS Outposts rack. The route table is step 1 of a **routing domain**; it becomes active only once a **VIF group** and a **VPC** are associated (`routing.md` L8, `routing-domains.md` L39).

**Request parameters** (`API_CreateLocalGatewayRouteTable`):
- `LocalGatewayId` *(String, **required**)* — the parent local gateway. Owned by the AWS account associated with the Outpost (`routing.md` L8).
- `Mode` *(String, optional; `direct-vpc-routing | coip`)* — default `direct-vpc-routing`. **Mutually exclusive, immutable** (CFN "Update requires: Replacement", `aws-resource-ec2-localgatewayroutetable.md` L57). No `Modify*RouteTable` API exists (only `ModifyLocalGatewayRoute`, route-level).
- `TagSpecification.N` *(optional)* — tags on the new table.
- `DryRun` *(Boolean)*.

**Response / data type** (`LocalGatewayRouteTable`): `localGatewayId`, `localGatewayRouteTableId`, `localGatewayRouteTableArn` (len ≤1283), `mode`, `outpostArn`, `ownerId` (**owning account**), `state`, `stateReason`, `TagSet`.

**Mode semantics (the security-relevant knob):**
- **`direct-vpc-routing`** (default): the local gateway advertises the **private IPs of Outpost-subnet instances** to the on-premises network over **BGP**; no NAT; "does not support overlapping CIDR ranges" (`routing.md` L24-26). Advertisement limited to subnets that have a route targeting the LGW (L47).
- **`coip`**: a customer-owned IP pool is advertised instead; supports overlapping CIDR; requires EIP mapping (`routing.md` L96-100). CoIP addresses show as **propagated** routes.

**Ownership / sharing model:**
- The local gateway is **owned by the Outpost-owner account** (`routing.md` L8). "**Only the owner of the local gateway can modify the local gateway route table**" (prose-only, L8) and "**Only the owner of a local gateway can create local gateway route tables**" (`outposts-local-gateways.html`). → **route-table creation is owner-only; RAM consumers cannot create tables** (resolves a prior doc-gap).
- **RAM sharing** (`sharing-outposts.md`): owners share within their **AWS Organization**. For a shared **local gateway route table**, "Consumers with access to this resource can: (1) **Create and manage VPC associations** to a local gateway; (2) **View configurations** of local gateway route tables and virtual interfaces; (3) **Create a VPC subnet route where the target is a local gateway**" (L44-46, L94). Owners can view/modify/delete consumer-created resources; consumers "can't modify Outposts shared with them" and "can't share a resource shared with them."
- **Unshare behavior (doc-confirmed, feeds Area 2):** "When a shared local gateway route table is unshared, the consumer can no longer create new VPC associations to it. **Any existing VPC associations that the consumer created remain associated with the route table.**" — surviving cross-account state after revocation.
- **Second-gen routing domains** (`routing-domains.md`): up to **10 isolated routing domains**; a routing domain = (LGW Route Table ⊕ VIF Group) 1:1; "**VPCs are exclusively associated with one LGW routing domain per Outpost, preventing unintended cross-domain communication**" (L19); "A VPC can be associated with 1 LGW route table per Outpost" (L39).

**ASCII pipeline:**
```
                 Outpost-owner account (service-plane adjacent)
  ┌───────────────────────────────────────────────────────────┐
  │  local-gateway/${LGW-id}  (AWS-provisioned, owner-owned)    │
  │        │ CreateLocalGatewayRouteTable(Mode)                 │
  │        ▼                                                     │
  │  local-gateway-route-table/${rtb-id}  ─assoc─ VIF Group ──► BGP ──► on-premises net
  │        │                                                     │
  │        └─ VPC association ◄── (RAM consumer can create/manage)
  └───────────────────────────────────────────────────────────┘
        ▲ consumer accounts (same Org) via RAM: VpcAssociation + view configs
```

**Identity:** SigV4 IAM only. No URL/blob/token/role-ARN/KMS/LLM/authorizer/cache inputs on this verb → lenses G/Q/B/C/H/K/W/BB/CC/DD/FF largely null (see §8).

---

## 3. API / Interface Inventory

| Name | Mutating | Facing | IAM resource legs (required*) & condition keys | Authorized callers | Notes |
|---|---|---|---|---|---|
| **CreateLocalGatewayRouteTable** | yes | external | `local-gateway*` {aws:ResourceTag, ec2:Region, ec2:ResourceTag}; `local-gateway-route-table*` {aws:RequestTag, aws:TagKeys, ec2:Region} | LGW owner (prose L8) | **No key for `Mode`.** Created-resource leg has only tag/region. |
| DeleteLocalGatewayRouteTable | yes | external | `local-gateway-route-table*` {aws:ResourceTag, ec2:Region, ec2:ResourceTag} — **no `local-gateway` leg** | owner | Teardown asymmetry vs Create. Returns the deleted table obj. |
| CreateLocalGatewayRouteTableVpcAssociation | yes | external | `local-gateway-route-table*` {ResourceTag,Region}; `local-gateway-route-table-vpc-association*` {RequestTag,TagKeys,Region}; `vpc*` {ResourceTag,Region,**ec2:Tenancy,ec2:VpcID**} | owner **+ RAM consumer** | Consumer-facing cross-account seam. |
| DeleteLocalGatewayRouteTableVpcAssociation | yes | external | `local-gateway-route-table-vpc-association*` {ResourceTag,Region} | owner + consumer | |
| CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation | yes | external | `local-gateway-route-table*`, `...-vig-association*`, `local-gateway-virtual-interface-group*` | owner | Completes a routing domain. |
| DescribeLocalGatewayRouteTables | no | external | **no resource types**; {ec2:Region} only | all (incl. consumers of shares) | Returns `ownerId`, `mode`, `outpostArn`. Region-wide recon. |
| DescribeLocalGatewayRouteTableVpcAssociations / ...VirtualInterfaceGroupAssociations | no | external | none; {ec2:Region} | all | Recon. |
| **CreateLocalGatewayRouteTablePermission** | yes | **non-SDK** | `local-gateway-route-table*` {ResourceTag,Region,ResourceTag}; **Permissions-management** | ? | **No public `API_…` page (404).** IAM links to Outposts userguide. "Grants permission to **allow a service to access** a local gateway route table." Under-documented. |
| DeleteLocalGatewayRouteTablePermission / DescribeLocalGatewayRouteTablePermissions | yes/no | non-SDK | same / region-only | ? | Permission lifecycle; Describe is region-only List. |

**Undocumented-knob flags (Step-3 discipline):** `Mode` accepts two enum values with **no condition key** and **no console warning documented** — the operator cannot author an IAM guardrail distinguishing them. The entire `*RouteTablePermission` family is accepted by the control plane but has **no API-reference page** — exactly the "accepted by the API/SDK but not surfaced" shape that has yielded real findings.

---

## 4. Recommended Areas of Focus (one block per firing lens)

### Area 1 — `Mode` is unconstrainable by IAM and immutable (Lens S + Lens U) — **PRIORITY 1**
**Background.** `Mode` (`direct-vpc-routing | coip`) decides whether the LGW advertises **instance private IPs** or a **CoIP pool** to on-premises BGP. It is a flat request parameter.
**Security Concern.** The `CreateLocalGatewayRouteTable` IAM row exposes **no condition key for `Mode`** (created-resource leg = `aws:RequestTag`/`aws:TagKeys`/`ec2:Region` only). An org that wants "route tables on this Outpost must be CoIP (so only an owned, advertised address range leaves the building)" or conversely "must be DVR" **cannot express it** — any principal allowed to create a table picks the mode freely. Because `Mode` is **immutable** (CFN Replacement; no `Modify*RouteTable`), a mis-moded table can only be remediated by delete+recreate, which itself requires teardown (Area 4) and transiently blackholes connectivity.
**High-level Test Scenarios (falsifiable):**
- **Claim:** A `Deny` with `Condition:{StringNotEquals:{"ec2:…Mode":"coip"}}` on `CreateLocalGatewayRouteTable` has no effect because no such key exists. → **Oracle:** `iam:SimulateCustomPolicy` with a policy referencing any plausible mode key returns the request still **Allowed**; `aws ec2 create-local-gateway-route-table --mode direct-vpc-routing` succeeds under a scoped role that "denied" DVR. → **Severity:** Medium–High (governance-of-on-prem-advertisement gap; High when a compliance control assumes mode is enforceable).
- **Claim (chain):** Choosing `direct-vpc-routing` auto-advertises *every* associated VPC's Outpost-subnet private IPs to on-prem with **no per-route `CreateLocalGatewayRoute` call** → container-level bypass of the route-level controls documented in the sibling plan. → **Oracle:** after `CreateLocalGatewayRouteTable(direct-vpc-routing)` + VPC/VIF association, on-prem BGP receives the subnet prefixes without any `CreateLocalGatewayRoute` being authorized.

### Area 2 — RAM consumer VPC-association → cross-account on-prem advertisement (Lens A + Lens AA) — **PRIORITY 2**
**Background.** `sharing-outposts.md` L44-46/L94: a consumer with a shared LGW route table can "**create and manage VPC associations**" and "**view configurations**." The owner picked the (immutable) `Mode` at creation.
**Security Concern.** The owner controls `Mode`; the **consumer controls which VPC is associated**. In `direct-vpc-routing` the association causes the **consumer's** Outpost-subnet private IPs to be advertised into the **owner's on-premises** network (and makes the consumer's instances reachable from the owner's on-prem). The `vpc*` leg's `ec2:VpcID`/`ec2:Tenancy` keys are evaluated **in the consumer's own account against the consumer's VPC** — they bound *which of the consumer's own* VPCs, not whether this crosses into the owner's routing domain. No condition key ties the association to owner consent beyond the RAM grant itself.
**High-level Test Scenarios:**
- **Claim:** A RAM consumer associates its VPC to the owner's shared DVR route table and the consumer's CIDRs appear in the owner's on-prem BGP advertisement. → **Oracle:** consumer-side `CreateLocalGatewayRouteTableVpcAssociation` succeeds; owner-side `SearchLocalGatewayRoutes`/on-prem BGP shows the consumer prefixes. → **Preconditions:** shared LGW route table, same Org. → **Severity:** High (cross-account routing exposure); **stop** if evidence implicates the *owner service account* internals (disclose).
- **Claim (revocation completeness, Lens AA) — DOC-CONFIRMED:** `sharing-outposts.md` states that after unshare, "any existing VPC associations that the consumer created **remain associated** with the route table." So a consumer's VPC keeps advertising into the owner's on-prem BGP **after the owner revokes the share** — the consumer loses only the ability to create *new* associations, not the existing one. → **Oracle:** confirm the surviving association still forwards/advertises post-unshare and that only the owner (not the now-unshared consumer) can `DeleteLocalGatewayRouteTableVpcAssociation` to sever it. → **Severity:** High (cross-account routing persists past revocation; owner must take explicit teardown action).

### Area 3 — Routing-domain isolation invariant (Lens U + Lens A sub-resource isolation) — **PRIORITY 3**
**Background.** 2nd-gen racks promise "**VPCs are exclusively associated with one LGW routing domain per Outpost, preventing unintended cross-domain communication**"; "A VPC can be associated with 1 LGW route table per Outpost" (`routing-domains.md` L19, L39). Up to 10 isolated domains.
**Security Concern.** This "exclusive, one-domain-per-VPC" guarantee is stated as prose; the enforcing mechanism (the 1:1 VPC↔route-table constraint) is **not expressed in any condition key**. Creating an additional route table and (re)associating a VPC is exactly the manage-VPC-associations capability a consumer holds.
**High-level Test Scenarios:**
- **Claim:** A principal creates a second route table and associates a VPC already in another domain, or races two associations, defeating the "exactly one domain" invariant → cross-domain communication between on-prem segments that should be isolated. → **Oracle:** `DescribeLocalGatewayRouteTableVpcAssociations` shows one VPC in two domains, or traffic crosses VLAN/VIF boundaries documented as isolated. → **Severity:** High (segmentation breach on shared infra) — **doc-gap; confirm the server-side 1:1 enforcement first.**

### Area 4 — Create-vs-Delete teardown asymmetry (Lens X) — **PRIORITY 4**
**Background.** `CreateLocalGatewayRouteTable` requires authz on **both** `local-gateway*` **and** `local-gateway-route-table*`. `DeleteLocalGatewayRouteTable` requires **only** `local-gateway-route-table*` (`aws:ResourceTag`/`ec2:Region`/`ec2:ResourceTag`) — **no `local-gateway` leg.**
**Security Concern.** A principal with no authority over the parent local gateway (cannot create tables there) can still **delete** an existing table if it satisfies the table's tag/region. Deleting the table tears down the routing domain (VPC + VIF associations) and blackholes the Outpost's on-prem connectivity. Delete returns the full table object (minor disclosure). Cascade behavior to routes/associations is **undocumented** (doc-gap).
**High-level Test Scenarios:**
- **Claim:** `local-gateway`-denied + `local-gateway-route-table`-tag-allowed principal deletes a production route table. → **Oracle:** `SimulatePrincipalPolicy` shows Delete Allowed while Create is Denied on the same LGW; live delete transitions state to `deleting`. → **Severity:** Medium–High (availability / DoS on shared Outpost).
- **Adjacent:** confirm whether Delete **cascades** or fails closed when VPC/VIF associations exist — a cascade makes the DoS one-call.

### Area 5 — Tag-on-create self-widen into the ABAC gate (Lens I + Lens S) — **PRIORITY 5**
**Background.** The created-resource leg carries `aws:RequestTag`/`aws:TagKeys`; every downstream action (Delete, VpcAssociation, the Permission family, and route-level Create/Modify from the sibling plan) is gated on `ec2:ResourceTag`/`aws:ResourceTag`.
**Security Concern.** The creator sets the table's tags at creation via `TagSpecification`. If the org's control is "only act on tables tagged `team=netops`," the creator simply creates the table **with** `team=netops`, self-widening into every ResourceTag-gated downstream action. The Create row has no `ec2:CreateAction` listed to bind tag-on-create to the create context, and no key prevents the creator choosing an arbitrary governance tag.
**Test Scenario:** **Claim:** a principal restricted by `aws:RequestTag` can still choose the exact tag value that unlocks a ResourceTag-gated Delete/VpcAssociation. → **Oracle:** `SimulateCustomPolicy` — create-with-tag Allowed, then Delete gated on that tag Allowed. → **Severity:** Medium (High where ResourceTag *is* the access-control mechanism).

### Area 6 — `DescribeLocalGatewayRouteTables` region-wide recon → `ownerId` disclosure (Lens A) — **PRIORITY 6**
**Background.** `Describe*` for the route-table family has **no resource-type scoping**, only `ec2:Region`. Response includes `ownerId`, `mode`, `outpostArn`, `state`.
**Security Concern.** A consumer (or any principal with the Describe grant) enumerates **all route tables visible in the region**, learning foreign **`ownerId`**, Outpost ARNs, and mode — cross-account recon undocumented as sensitive. Feeds Areas 2–4 (which tables to associate/delete).
**Test Scenario:** **Claim:** a consumer lists route tables it does not own and reads `ownerId`/`outpostArn`. → **Oracle:** `describe-local-gateway-route-tables` returns foreign-owned entries with populated `ownerId`. → **Severity:** Low–Medium.

### Area 7 — `CreateLocalGatewayRouteTablePermission` family — confused-deputy / over-share (Lens AA + Lens B) — **PRIORITY 7 (doc-gap)**
**Background.** `CreateLocalGatewayRouteTablePermission` / `Delete…` / `Describe…` are **Permissions-management** actions with **no public API-reference page** (the `API_…html` 404s); the IAM entries link to the Outposts userguide. Description: "Grants permission to **allow a service to access** a local gateway route table."
**Security Concern.** This is a permission-granting primitive whose resource leg carries only `{ResourceTag, Region}` — **no principal/service/counterparty condition key** is documented. If it grants a service (or account) access to the route table without a scoping key, it is a confused-deputy / over-share seam: the grantee reach cannot be IAM-bounded by the operator, and `Describe…Permissions` is region-only (any caller can read who has been granted). Because the action is console-/RAM-internal and undocumented, it is under-tested.
**Doc blind-spot (confirmed by sweep):** these three actions exist **only** as one-line Service-Authorization entries — no API-reference page, no CLI-reference page, no Outposts user-guide prose, and the Outposts service-linked role `AWSServiceRoleForOutposts_{OutpostID}` does **not** call them (its documented policy is scoped to `ec2:Describe*`/`Create*NetworkInterface`/`*SecurityGroup*`). The **"service" these permission actions target is nowhere documented.** The phrasing "allow **a service** to access" (singular, not "consumer"/"account") mirrors `ec2:CreateNetworkInterfacePermission` (a service-principal grant), *not* RAM account-sharing.
**Test Scenarios (confirm surface first):**
- **Claim:** `CreateLocalGatewayRouteTablePermission` accepts a service/principal target with no validation that the operator could scope, over-granting route-table access. → **Oracle:** determine the actual parameters (SDK model / `aws ec2 create-local-gateway-route-table-permission help`); check whether a grantee can be named cross-account or as a wildcard service. → **Severity:** Medium–High if an unscopable grant; **route `aws-security` if it reaches the owner service plane** (HARD STOP).
- **Claim:** `Delete…Permission` has a vintage/teardown asymmetry (can revoke a permission the caller could not grant). → **Oracle:** compare the two IAM rows + live behavior.

---

## 5. Prioritized NEW / changed surface
1. **`Mode` unconstrainable + immutable (Area 1)** — the distinguishing gap of this verb; governs on-prem advertisement for all associated VPCs.
2. **RAM-consumer VPC-association cross-account advertisement (Area 2)** — the only consumer-facing mutation path; cross-account by design.
3. **Routing-domain isolation invariant (Area 3)** — 2nd-gen `[NEW]` feature, least-reviewed; prose-only isolation guarantee.
4. **Permission family (Area 7)** — non-SDK / no API page / Permissions-management = classic under-tested knob.
5. Teardown asymmetry (Area 4), ABAC self-widen (Area 5), recon (Area 6).

**Kill-chain to compose:** Area 6 (enumerate owner `ownerId`/tables, learn mode) → Area 2 (associate consumer VPC to a shared **DVR** table) → cross-account on-prem advertisement of consumer prefixes; **or** Area 1 (owner creates a DVR table) → Area 5 (self-tag) → sibling `CreateLocalGatewayRoute` (no `ec2:Cidr`) injects a more-specific ENI route → inbound interception with destination preserved (routing.md L164). Rate at the chain end (High).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Choose on-prem advertisement mode against policy | `Mode` param | None — no condition key; immutable (CFN Replacement) |
| Consumer advertises its VPC into owner's on-prem BGP | VpcAssociation (RAM) | "Only owner can modify the route table" (prose); RAM grant scope |
| Bridge two routing domains via a VPC | VpcAssociation / 2nd-gen domains | "VPC exclusively one routing domain per Outpost" (prose, routing-domains L19/39) |
| Delete route table without LGW authority | Delete IAM row | ResourceTag/Region gate only; no `local-gateway` leg |
| Self-tag into ABAC gate | TagSpecification + downstream ResourceTag | `aws:RequestTag` at create (creator-chosen) |
| Cross-account recon of `ownerId`/mode | Describe* | Region-only; no resource scoping |
| Over-share via Permission family | `*RouteTablePermission` | Undocumented; `{ResourceTag,Region}` only, no principal key |

---

## 7. Out-of-Scope Risk Categories
- AWS Outpost-owner **service plane** / LGW control plane / VIF-BGP control identities — **HARD STOP + disclose**.
- Shared Outpost **hardware/firmware**, the physical uplinks/LAGs/CNDs, and BGP peer devices (customer-owned on-prem gear).
- Single-tenant self-DoS (deleting your own route table).
- Customer-authored IAM policy footguns (only AWS-authored artifacts are in scope — none ship with this verb).
- IMDS / instance-level issues on Outpost instances (managed-host out-of-scope).
- BGP protocol attacks against the on-prem network beyond what a route/mode choice expresses.

---

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens G (SSRF) / Q (upload) / B,C (role-ARN/PassRole) / H (KMS) / K (LLM) / W (attestation) / Y (TLS/sig) / BB (canonicalization) / CC (upstream-context) / DD (cache) / FF (JWT):** NULL. Pages read: `API_CreateLocalGatewayRouteTable`, `API_LocalGatewayRouteTable`, `API_DeleteLocalGatewayRouteTable`, `list_ec2.md` rows, `routing.md`, `sharing-outposts.md`, `routing-domains.md`, CFN resource. The verb takes only `LocalGatewayId` + `Mode` enum + tags — no URL/blob/role/token/key/crypto/authorizer/cache/JWT input.
- **Lens EE (predictable-name land-grab):** NULL — `LocalGatewayId` is AWS-provisioned at rack install, not a predictable/global namespace the attacker can pre-claim.
- **Lens N (namespace migration):** NULL — single ARN form.
- **RESOLVED (was a gap):** RAM consumers **cannot** create route tables — "Only the owner of a local gateway can create local gateway route tables" (`outposts-local-gateways.html`). Consumer mutation on a shared table is limited to VPC-association + a subnet-route-to-LGW.
- **Open doc-gaps (confirm surface first, do not treat as closed):**
  1. The actual parameters and grantee-scoping of the **`*RouteTablePermission`** family (no API/CLI page; target "service" undocumented; not called by the Outposts SLR). **Top gap.**
  2. Whether `DeleteLocalGatewayRouteTable` **cascades** to routes/VPC/VIF associations or fails closed.
  3. Server-side enforcement of the **1:1 VPC↔routing-domain** invariant on 2nd-gen racks (routing-domains.md frames it as a hard constraint requiring you to "first delete the existing LGW Route Table and routing domain association" before re-pointing a VIF group — confirm IAM does not let a consumer-managed association bypass this).
  4. Whether a local gateway route can target an **ENI in a different account** than the table owner (genuinely silent — neither permitted nor forbidden; shared with the route-level plan).
  5. CloudTrail event shape for `CreateLocalGatewayRouteTable` / `Mode` selection.
  - *(Correct doc path for routing domains: `outposts/latest/network-userguide/routing-domains.html`; the `/userguide/` variant is a stub.)*
- **`ec2:Attribute/${AttributeName}`** is listed as *available* on the `local-gateway-route-table` resource but is **not consumed by any table-level verb** (it is used by route-level `ModifyLocalGatewayRoute`). A `Deny` keyed on `ec2:Attribute` to constrain table creation/mode would be inert — Lens S "key present on the resource but not evaluated by this action."

---
*Generated by the `security-questionbuilder` skill against AWS documentation only. No live AWS account was contacted.*
