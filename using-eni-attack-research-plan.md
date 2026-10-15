# Elastic Network Interfaces (`using-eni.html`) — Attack / Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html
**Scope of this plan:** the ENI *resource itself* — its lifecycle (create / attach / detach / delete), its attributes (SourceDestCheck, DeleteOnTermination, Groups, Description), cross-account grants (network-interface permissions), and the attach/detach topology. The page's child pages: `network-interface-attachments.html`, `requester-managed-eni.html`, `scenarios-enis.html`, `modify-network-interface-attributes.html`, `delete_eni.html`, `ec2-prefix-eni.html`, `create-network-interface.html`.
**Authoritative IAM source:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (= `list_ec2.html`). Line numbers below are from that file.
**Drift check:** online twin (`using-eni.md`, `network-interface-attachments.md`) fetched 2026-10-15 — **byte-identical to the offline mirror. No drift.**
**Skill:** `security-questionbuilder` (6-step boundary-lens method).

> **Position in the EC2-Networking plan family.** This is a page-level child of the **`ec2-networking` hub** plan, in **cluster 2 (ENI / Secondary-Networks)**. It is the *ENI-resource* plan. It does **not** re-derive IP-assignment attacks — those are owned by siblings and are referenced, not duplicated:
> - **`using-instance-addressing-attack-research-plan.md`** — secondary private-IPv4 cross-ENI/cross-account takeover via `AssignPrivateIpAddresses`+`AllowReassignment`; EIP ride-along.
> - **`instance-secondary-ip-addresses-attack-research-plan.md`** — `UnassignPrivateIpAddresses` → EIP auto-disassociation collateral (unscopable twin of `DisassociateAddress`).
> - **`working-with-ip-addresses-attack-research-plan.md`** — launch-time IPv4 assignment, `ec2:AssociatePublicIpAddress` (RunInstances-NI-row only).
> - **`config-windows-multiple-ip-attack-research-plan.md`** — Windows guest static-binding ↔ control-plane split-brain.
> **Secondary Networks** (`eni-sn.html` cluster) is carried here only as a cross-ref lead (§4 Lens V/L); it deserves its own page plan.

---

## 0. TL;DR — Ranked leads

| # | Lead | Lens | Severity (if true) | Confidence |
|---|---|---|---|---|
| 1 | `DeleteNetworkInterfacePermission` cannot be scoped by `ec2:AuthorizedUser` / `ec2:AuthorizedService` / `ec2:Permission` while `CreateNetworkInterfacePermission` can — and its resource type is not even `*required`. A grantor policy that safely scopes *who you may grant to* cannot scope *whose grant you may revoke*. | X, AA, S | MED-HIGH (cross-account grant teardown / DoS; grant-management integrity) | HIGH (IAM-confirmed) |
| 2 | `AttachNetworkInterface` **instance** resource row carries **no `ec2:Vpc` / `ec2:Subnet` key** — cross-VPC same-account attach (a documented feature) cannot be IAM-fenced to "ENI's VPC must equal instance's VPC". | A, S, V | MED-HIGH (bridge isolated VPCs; data exfil path) | HIGH (IAM-confirmed + UG-confirmed feature) |
| 3 | **No value-level condition key** exists for the attributes that convert an ENI into a NAT/router/firewall transit point: `ec2:SourceDestCheck`, `ec2:DeleteOnTermination`, `ec2:NetworkCardIndex`, `ec2:DeviceIndex`, `ec2:InterfaceType` are **all 0-hit** in `list_ec2.md`. `ModifyNetworkInterfaceAttribute` can be scoped only to the attribute **name** (`ec2:Attribute`), never its **value** → granting `sourceDestCheck` modify = granting MITM-enablement with no governable guardrail. | S, U, D | MED-HIGH (chained with #2 = cross-VPC MITM transit node) | HIGH (IAM-confirmed) |
| 4 | `ResetNetworkInterfaceAttribute` is callable on **requester-managed ENIs** where `Modify` is blocked (UG line 18: "You can still reset… even though you can't modify them"), AND `Reset` carries **no `ec2:Attribute` key at all** (@9519) while `Modify` does (@8966) → an attribute-name-scoped Modify policy is silently bypassable via Reset. | X, S | MED (integrity / reset-to-default on resources you can't otherwise touch) | HIGH (IAM + UG confirmed) |
| 5 | `DescribeNetworkInterfaces` / `DescribeNetworkInterfacePermissions` have **zero resource-level scoping** — account-wide topology + cross-account grant-list disclosure oracle; also the recon primitive for leads #1–#4. | A, O | MED (full intra-account topology + grant disclosure) | HIGH (IAM-confirmed) |
| 6 | Public-IPv4 **persistence** footgun: an instance that has a secondary ENI or an EIP-associated secondary private IP **keeps its public IP across stop/start** (UG line 59). A dangling/forgotten secondary ENI silently pins a reputation-bearing address. | U | LOW-MED (dangling public-IP persistence; chains to dangling-DNS in sibling EIP/addressing plans) | HIGH (UG-confirmed) |
| 7 | **Force detachment** can (a) prevent instance metadata from reflecting the detach and (b) block re-attach on the same index until instance restart (attachments.md line 124) → integrity-of-truth + targeted index-DoS. | O, U, L | LOW-MED | HIGH (UG-confirmed) |
| 8 | Secondary Networks (secondary-network ENIs) lack SG/NACL/Flow-Logs equivalents → observability/segmentation gap. **Deferred to a dedicated Secondary-Networks plan.** | V, O | (defer) | MED (fragment-noted) |
| 9 | Secondary-network / prefix-delegation quota exhaustion; prefix-uniqueness TOCTOU. | L, P | LOW | MED |

**Null / N/A lenses (pages checked):** B, C, E, F, G, Q, T — see §4 null section. Each names the pages read.

---

## 1. Components, Assets, and Design

### What the ENI is
An *elastic network interface* (`eni-<17hex>`) is a logical VPC networking component — "a virtual network card" — that holds a bundle of **attributes that follow it across attach/detach/reattach** (UG line 8): primary + secondary private IPv4, primary + secondary IPv6, one EIP per private IPv4, one public IPv4, security groups, a MAC address, a **source/destination check flag**, and a description. Moving an ENI "redirects network traffic from the original instance to the new instance" — the ENI *is* a portable identity + reachability token.

### Resource / identifier shapes
- **ENI:** `eni-<17hex>` — has an IAM resource type `network-interface` with ARN; scopable by `ec2:Vpc`, `ec2:Subnet`, `ec2:AvailabilityZone`, `ec2:ResourceTag`, etc.
- **Attachment:** `eni-attach-<17hex>` — **no IAM ARN resource type.** `DetachNetworkInterface` takes only `--attachment-id`; authz is on the ENI, not a first-class attachment resource. (Enumerability note: 17-hex is not brute-forceable, but attachment IDs are returned wholesale by the unscopable `DescribeNetworkInterfaces` — see lead #5.)
- **Network-interface permission:** cross-account/cross-service grant object created by `CreateNetworkInterfacePermission`; names an `AwsAccountId` **or** an `AwsService` + a `Permission` (`INSTANCE-ATTACH` | `EIP-ASSOCIATE`).
- **Requester-managed ENI:** created by an AWS service (RDS, NAT GW, PrivateLink endpoint, ELB, Lambda, WorkSpaces) *in your VPC on your behalf*; you can tag/view/**reset** but not modify/attach/detach/assign-IP.
- **Managed ENI:** managed by a service provider (EKS Auto Mode); `Managed=true`; not customer-modifiable.

### Identity / privilege levels
SigV4 IAM only. Relevant principals: the ENI owner (account), a *grantee* account/service named in a network-interface permission, and AWS service principals behind requester-managed/managed ENIs.

### Where untrusted influence enters
Not a parser/translation surface. The "untrusted input" here is **IAM-authorized API calls whose parameters select *values* (attribute values, target instance, device/card index, grantee) that no condition key can constrain** — i.e. the attack surface is *authorization completeness*, not injection.

### Connection diagram (implied pipeline)
```
                         ec2:CreateNetworkInterfacePermission (scopable: AuthorizedUser/Service/Permission)
  Account A (owner) ───────────────────────────────────────────────► grant object ──► Account B / AWS service
        │                                                                   ▲
        │ ec2:DeleteNetworkInterfacePermission  (NOT scopable by those keys; resource not *required)   # LEAD 1
        │
        │ ENI (eni-…) attributes follow the card ──► attach ──► Instance
        │        SourceDestCheck / DeleteOnTermination / Groups / Description
        │        (ModifyNetworkInterfaceAttribute: name-scopable, NOT value-scopable)                   # LEAD 3
        │        (ResetNetworkInterfaceAttribute: NO ec2:Attribute key; works on requester-managed)     # LEAD 4
        │
        └ AttachNetworkInterface ──► instance in SAME or DIFFERENT VPC (same acct, same AZ)             # LEAD 2
                 instance row has NO ec2:Vpc/ec2:Subnet key → no "same-VPC" fence
```

---

## 2. Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Account A principal (grantor) | A grant object naming account B | `Create`/`Delete`NetworkInterfacePermission | Revoking/altering a grant you should not control, or granting beyond policy, with the *same* ENI permission a bounded policy intended → **grant-management integrity break** (lead #1). |
| Low-priv principal in account A | Instance in a *different* VPC of account A | `AttachNetworkInterface` (cross-VPC, same AZ) | An ENI from isolated VPC-X ends up on an instance in VPC-Y despite a policy meant to keep attach within one VPC → **VPC-isolation fence cannot be expressed** (lead #2). |
| Principal with `Modify`/`Reset` on an ENI | The traffic-forwarding posture of that ENI | Disable `sourceDestCheck` | ENI becomes a transit/NAT/router/firewall node for traffic it is neither source nor dest of; no condition key could have blocked the *value* → **MITM-enablement ungoverned** (lead #3; UG line 72 + scenarios line 38). |
| Principal blocked from `Modify` on a requester-managed/managed ENI | That same ENI's attributes | `ResetNetworkInterfaceAttribute` | Resetting an attribute on an ENI you were explicitly denied `Modify` on → **modify-deny bypass via reset** (lead #4; UG requester-managed line 18). |
| Any read principal | Whole-account ENI topology + cross-account grant list | `DescribeNetworkInterfaces` / `…Permissions` | Enumerating every ENI/attachment/grant in the account with no resource scoping → **topology + grant disclosure oracle** (lead #5). |
| ENI owner | A public IPv4 the owner believes is released on stop | Secondary-ENI/secondary-EIP persistence | Public IP survives stop/start because a forgotten secondary ENI pins it → **dangling reputation address** (lead #6; UG line 59). |
| Operator forcing a detach | Instance metadata + the device index | `Force detachment` | Metadata does not reflect the detach / index stays blocked until restart → **truth + availability break** (lead #7; attachments line 124). |
| Customer surface | **AWS service plane** (requester-managed/managed ENIs) | Any attempt to reach the service principal behind a requester-managed ENI | Any identity/credential/ARN belonging to AWS's own fleet = **HARD STOP; preserve evidence; flag for disclosure.** |

---

## 3. API / interface surface inventory

Line numbers = `list_ec2.md`. "Value-scopable" = a condition key constrains the *value* of the attribute/parameter, not merely the target resource.

| API | Mut? | Resource type(s) (`*`=required) | Key condition keys present | Gap / note |
|---|---|---|---|---|
| `CreateNetworkInterface` @5357 | Y | subnet\*, security-group, network-interface\* | ec2:Subnet, ec2:Vpc, ec2:AvailabilityZone, tag keys | Baseline; well-scopable. |
| `AttachNetworkInterface` @4858 | Y | **instance** (no `*`? std set), network-interface\* | network-interface row: ec2:Vpc/ec2:Subnet; **instance row: NO ec2:Vpc/ec2:Subnet** | **LEAD 2** — cannot require instance.VPC == ENI.VPC. |
| `DetachNetworkInterface` | Y | network-interface (attachment has no ARN type) | ENI-level only | Authz on ENI; attachment id not a resource. Force-detach side effects → **LEAD 7**. |
| `DeleteNetworkInterface` @6088 | Y | network-interface\* | tag/Vpc/Subnet | Standard. |
| `ModifyNetworkInterfaceAttribute` @8966 | Y | network-interface\*, **security-group** | **ec2:Attribute**, ec2:Attribute/${AttributeName}; (sg row: ec2:SecurityGroupID, ec2:Vpc) | Attribute **name**-scopable only. SG swap is partly scopable; **sourceDestCheck/deleteOnTermination value NOT** → **LEAD 3**. |
| `ResetNetworkInterfaceAttribute` @9519 | Y | network-interface\* | **NONE** (no ec2:Attribute) | **LEAD 4** — un-narrowable; works on requester-managed. |
| `CreateNetworkInterfacePermission` @5364 | Y (Permissions mgmt) | network-interface\* | **ec2:AuthorizedUser, ec2:AuthorizedService, ec2:Permission** | Grantor can scope *who* / *what*. |
| `DeleteNetworkInterfacePermission` @6094 | Y (Permissions mgmt) | network-interface (**not `*required`**) | **NONE of AuthorizedUser/Service/Permission** | **LEAD 1** — asymmetry; cannot scope which grant is revoked. |
| `DescribeNetworkInterfaces` | N | — | none (resource "\*") | **LEAD 5** — account-wide. |
| `DescribeNetworkInterfacePermissions` | N | — | none | **LEAD 5** — grant-list oracle. |
| `AssignPrivateIpAddresses` / `UnassignPrivateIpAddresses` / `Assign…Ipv6…` | Y | network-interface\* | **no ec2:PrivateIpAddress / Ipv6Address / AllowReassignment key** | **DEFERRED** to `using-instance-addressing` + `instance-secondary-ip-addresses` siblings. |
| `(Dis)AssociateAddress` (EIP↔ENI) | Y | — | — | **DEFERRED** to EIP-cluster plans. |
| `ec2:AssociatePublicIpAddress` (launch-time) | — | RunInstances NI row only | — | **DEFERRED** to `working-with-ip-addresses` sibling. |

**Confirmed 0-hit condition keys in `list_ec2.md`** (grep): `ec2:SourceDestCheck`=0, `ec2:DeleteOnTermination`=0, `ec2:NetworkCardIndex`=0, `ec2:DeviceIndex`=0, `ec2:InterfaceType`=0. (For contrast: `ec2:Attribute/`=129 hits, `ec2:AuthorizedUser`=8, `ec2:Permission`=8.) ⇒ there is **no value-level governance** for the attributes/parameters that decide whether an ENI forwards foreign traffic, auto-deletes, lands on a given card/device index, or is of a given interface type.

**Undocumented/console-hidden knob sweep:** `--device-index` and the network-card selector are CLI/API/console-exposed but have no condition key — a caller picks card index 0 reassignment / any device index with no IAM lever (ties to lead #3's `ec2:DeviceIndex`/`ec2:NetworkCardIndex`=0). No `authorizerType:NONE`-class hidden auth-weakening enum on this surface.

---

## 4. Boundary-lens catalog — firing lenses

### Lens X — Action-family parity  ★ LEAD 1 (headline)
**Claim:** A policy that lets a principal manage cross-account attach grants *safely* (scoped by grantee account/service and permission type) cannot prevent that principal from **revoking grants it did not create / should not touch**, because `DeleteNetworkInterfacePermission` (@6094) exposes **none** of `ec2:AuthorizedUser` / `ec2:AuthorizedService` / `ec2:Permission` that `CreateNetworkInterfacePermission` (@5364) exposes — and `Delete`'s `network-interface` resource type is **not even `*required`**, so even ENI-ARN scoping is weaker.
**Mechanism (doc evidence):** `list_ec2.md` @5364 vs @6094, side-by-side rows. Both are "Permissions management, Write".
**Confirm/Refute oracle:** In a policy that grants `Create` scoped to `ec2:AuthorizedUser = <partner-acct>`, add `Delete` — observe that no equivalent condition can bind `Delete` to that same grantee; a principal can revoke a *different* account's INSTANCE-ATTACH grant (teardown of a legitimately-shared ENI → attach failure / DoS of the partner's workload). Doc-confirmable today; live-confirm = call `DeleteNetworkInterfacePermission` on a permission created for another account under an IAM policy that scoped `Create` tightly.
**Preconditions / Cost / Severity:** needs `Delete…Permission` in the principal's policy; low cost; **MED-HIGH** (cross-account grant teardown / DoS, grant-management integrity). **Stop:** existence of the asymmetry + one revoke of a non-self-created grant = confirmed; do not enumerate other accounts' grants.

### Lens A / S / V — Cross-VPC attach has no VPC fence  ★ LEAD 2 (headline)
**Claim:** A low-privileged principal can attach an ENI living in an *isolated* VPC-X to an instance in VPC-Y of the **same account** (documented feature, same AZ), and no IAM policy can require "attach only within the ENI's own VPC," because `AttachNetworkInterface`'s **instance** resource row (@4858) carries **no `ec2:Vpc`/`ec2:Subnet`** key (only the `network-interface` row does).
**Mechanism (doc evidence):** UG `network-interface-attachments.md` line 42 (console: "same VPC … or in a different VPC that you own … multi-homed instances across VPCs with different networking and security configurations") + `scenarios-enis.md` line 48 ("launch an EC2 instance in one VPC and attach a secondary ENI from a different VPC … You can't create multi-homed instances across VPCs in different AWS accounts") + `list_ec2.md` @4858 instance-row key absence.
**Confirm/Refute oracle:** Author a Deny/Allow pair intending "ENIs may only attach to instances in the same VPC"; show it is inexpressible — the only levers (`network-interface` row `ec2:Vpc`, or the instance's own tags) cannot relate the two resources. Live-confirm = attach a VPC-X ENI to a VPC-Y instance; packets now bridge the two otherwise-unpeered VPCs (scenarios line 51 explicitly markets this as "overcome CIDR overlaps between two VPCs that can't be peered").
**Preconditions / Cost / Severity:** `AttachNetworkInterface` + an instance in a second VPC, same AZ; low cost; **MED-HIGH** (deliberate VPC-isolation bypass / data path between segmented environments; a prod↔dev or DMZ↔internal bridge). **Stop:** one cross-VPC attach observed = confirmed.

### Lens S / U / D — No value-level key for traffic-forwarding attributes  ★ LEAD 3 (headline)
**Claim:** Granting `ModifyNetworkInterfaceAttribute` for the `sourceDestCheck` attribute is equivalent to granting the ability to turn any reachable ENI into a NAT/router/firewall transit node, and this **cannot be constrained to a safe value**, because `ec2:SourceDestCheck` does not exist as a condition key (0 hits) and `ec2:Attribute` scopes only the attribute *name*. Same gap for `deleteOnTermination` (tamper: make a victim ENI auto-delete on instance terminate — 0-hit `ec2:DeleteOnTermination`), and for which `--device-index`/network-card an attach targets (0-hit `ec2:DeviceIndex`/`ec2:NetworkCardIndex`).
**Mechanism (doc evidence):** UG `using-eni.md` line 72 ("You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls"); `scenarios-enis.md` line 38 (appliances "configure the additional interfaces with their own … security groups, and source/destination checking"); `list_ec2.md` @8966 (name-only `ec2:Attribute`) + the 0-hit grep for the value keys.
**Confirm/Refute oracle:** Try to write an IAM policy that allows `Modify` of `description` but denies `sourceDestCheck` → shows `ec2:Attribute/${AttributeName}` *can* separate names (so a careful author can block it) **but** once `sourceDestCheck` is allowed at all, no key can pin the value to `true` (enabled) → the moment it's granted, MITM-enablement is granted. **Chain with LEAD 2:** cross-VPC-attach an ENI, then disable its sourceDestCheck → a cross-VPC transit/MITM node. Live-confirm = disable sourceDestCheck and route a third instance's traffic through it.
**Preconditions / Cost / Severity:** `Modify` on the ENI (or Reset per lead #4); low cost; **MED-HIGH** when chained with #2. **Stop:** policy-inexpressibility shown + one sourceDestCheck disable = confirmed.
**Nuance (fair to the mechanism):** `ec2:Attribute/${AttributeName}` *does* let a disciplined author exclude `sourceDestCheck`/`groupSet` from a Modify grant — the defect is that the *default* framing ("grant Modify") silently includes it, and `Reset` (lead #4) has no such lever at all.

### Lens X / S — Reset bypasses Modify-deny & is un-narrowable  ★ LEAD 4
**Claim:** A principal explicitly denied `ModifyNetworkInterfaceAttribute` (including on a **requester-managed** ENI they can't modify at all) can still call `ResetNetworkInterfaceAttribute` to force an attribute to default, and no `ec2:Attribute` key can narrow *which* attribute Reset touches (@9519 carries no condition keys).
**Mechanism (doc evidence):** UG `requester-managed-eni.md` line 18 — "You can still reset network interface attributes, even though you can't modify them"; `list_ec2.md` @9519 (no `ec2:Attribute`) vs @8966 (has it).
**Confirm/Refute oracle:** With a policy that Allows `Reset` but Denies `Modify` on an ENI, reset `sourceDestCheck` (default = enabled) or `groupSet`/`description`/`deleteOnTermination` → an attribute changes on a resource the principal was denied `Modify` on; on a requester-managed ENI this reaches an AWS-service-owned-config object (note the **hard-stop** boundary — reset-to-default of *your-side* config is in-scope; anything that perturbs the AWS service's own plane is a stop-and-flag).
**Preconditions / Cost / Severity:** `Reset` granted while `Modify` denied; low cost; **MED** (integrity / deny-bypass). **Stop:** one reset under a Modify-deny = confirmed. Do **not** probe the service-plane side of a requester-managed ENI.

### Lens A / O — Unscoped describe = topology + grant oracle  ★ LEAD 5
**Claim:** `DescribeNetworkInterfaces` and `DescribeNetworkInterfacePermissions` return every ENI, attachment id, IP, SG, MAC, requester-id, and **cross-account grant** in the account with no resource-level scoping, giving a full intra-account topology map and the enumeration substrate for leads #1–#4.
**Mechanism (doc evidence):** both actions carry resource "*" with no ARN resource type / tag scoping in `list_ec2.md`; `requester-managed-eni.md` CLI example shows `--filter requester-managed` surfacing service-owned ENIs and their `Requester ID`.
**Confirm/Refute oracle:** a read-only principal lists all ENIs/permissions it does not own-by-tag; distinct not-found vs access-denied behavior is not even needed because everything is returned.
**Preconditions / Cost / Severity:** any `Describe*` grant; trivial; **MED** (recon / topology + grant disclosure, no mutation). **Stop:** one unscoped listing = confirmed.

### Lens U — Public-IP persistence footgun  LEAD 6
**Claim:** An instance owner who believes "public IP is released on stop" is wrong whenever the instance has a secondary ENI or an EIP-associated secondary private IP — the public IPv4 persists across stop/start (UG line 59), so a forgotten secondary ENI silently pins a reputation-/allowlist-bearing address.
**Mechanism (doc evidence):** `using-eni.md` line 59 verbatim; `network-interface-attachments.md` line 27 ("If the public IPv4 address on your instance is released, it does not receive a new one if there is more than one network interface attached").
**Confirm/Refute oracle:** stop/start an instance with a secondary ENI; observe public IP retained. Chains to **dangling-DNS** themes owned by the EIP/addressing sibling plans.
**Severity:** **LOW-MED** (persistence / dangling address, not isolation break). **Stop:** one retained-IP observation.

### Lens O / U / L — Force-detachment integrity & index DoS  LEAD 7
**Claim:** `Force detachment` can leave instance metadata not reflecting the detach and block re-attach on the same device index until the instance is restarted (attachments.md line 124) → a truth-of-state break (metadata lies) plus a targeted availability denial (index locked).
**Mechanism (doc evidence):** `network-interface-attachments.md` line 124 verbatim.
**Confirm/Refute oracle:** force-detach, then (a) read instance metadata and see the stale ENI, and/or (b) attempt re-attach on the same index and observe rejection pre-restart.
**Severity:** **LOW-MED** (integrity + localized DoS). **Stop:** either effect observed once.

### Lens V / L — Secondary Networks segmentation/observability  LEAD 8 (DEFERRED)
**Claim (carried from the ENI fragment):** Secondary-network ENIs lack SG/NACL/Flow-Logs equivalents → a segment with no filtering and no flow visibility. **This belongs to a dedicated Secondary-Networks (`eni-sn.html`) page plan — do not resolve here.** Pointer only.

### Lens L / P — Quota exhaustion & prefix TOCTOU  LEAD 9
- **L:** secondary-network / prefix-delegation per-ENI and per-instance limits (network cards up to 32 on p5.48xlarge; prefix ranges) are capacity knobs; exhausting them is an intra-account noisy-neighbor DoS. LOW.
- **P:** prefix-delegation uniqueness has a documented auto/manual assignment path (`ec2-prefix-eni.html`) — a classic allocate-vs-assign TOCTOU window if two callers race the same prefix. LOW; doc-gap on the exact atomicity guarantee — mark "confirm surface first."

### Null hypotheses (pages checked — not blind skips)
- **Lens B (confused deputy / PassRole):** N/A for the ENI resource APIs — read `using-eni.md`, `network-interface-attachments.md`, `create-network-interface.md`, `requester-managed-eni.md`; **no API here takes a caller-supplied role ARN the service assumes.** (PassRole lives on `RunInstances`/launch-template, out of this page's scope.)
- **Lens C (credential vending / session scope):** N/A — no STS/session-policy/token-as-input on these APIs (pages above).
- **Lens E (RBAC priv-esc via hidden identity):** N/A on this page — no built-in admin identity for ENIs; the Reset/Modify asymmetry is captured under Lens X/S (lead #4) instead.
- **Lens F (translation/wire-protocol injection):** N/A — ENI APIs are structured SigV4 calls, no customer-string → downstream-language transform. Checked all ENI child pages.
- **Lens G (SSRF / server-dereferenced URL):** N/A — read all ENI pages incl. requester-managed and attachments; **no field the service fetches/unfurls** (`Description` is free-text but never dereferenced). Note the `Description` free-text field as a stored-value oracle only (shows up in `Describe` for other readers), not SSRF.
- **Lens Q (uploaded-blob parse):** N/A — no blob/file input on ENI APIs.
- **Lens T (generated secret persistence):** N/A — ENIs generate no customer secret/key persisted to SSM/Secrets Manager.

---

## 5. NEW / changed surface — where to concentrate fire

- **Highest net-new value vs the EC2-Networking hub:** leads #1 (Delete-permission asymmetry), #2 (cross-VPC attach fence gap), #3 (no value-level traffic-attribute keys) — all three are **authorization-completeness** findings provable from `list_ec2.md` *today* with no live account, then one-shot confirmable.
- **`[NEW]`-style features on the page:** **Managed network interfaces** (EKS Auto Mode, `Managed=true`) and the expanded **Network cards** table (now up to 32 NICs on p5.48xlarge, 17 on p6-b300/p6e-gb200) — these widen lead #3's `ec2:NetworkCardIndex`-has-no-key gap and the lead #9 exhaustion surface. Managed ENIs also widen the **hard-stop** service-plane boundary (treat like requester-managed).
- **AWS-planted lead:** UG line 72 states the operational *requirement* to disable sourceDestCheck for NAT/router/firewall — that sentence is exactly where the lead #3 MITM primitive is planted.

---

## 6. Hard stops / scope discipline for the downstream hunter
- Requester-managed and **managed** ENIs sit on the **AWS service plane**. Resetting *your-side* config is in-scope; the instant any probe would retrieve or perturb an AWS-fleet identity/credential/ARN or the service's own config → **STOP, preserve evidence, flag for disclosure.** Do not enumerate or touch the service principal behind them.
- Cross-**account** is only reachable here via network-interface *permissions* (leads #1) and never via direct attach (scenarios line 48: "You can't create multi-homed instances across VPCs in different AWS accounts"). Keep cross-account tests to the grant surface; one revoke/one grant proves the point — do not sweep other accounts' grants.
- All confirms are **existence/one-shot**: one asymmetry, one cross-VPC attach, one sourceDestCheck disable, one reset-under-deny, one unscoped list. Do not iterate, enumerate, or exploit beyond the single proof.

## 7. Open doc-gaps to confirm against a live account
1. Does `DeleteNetworkInterfacePermission` succeed on a permission the caller did **not** create (lead #1 live confirm)? Doc says resource type not `*required`; behavior must be observed.
2. Exact atomicity of prefix allocate-vs-assign (lead #9 P).
3. Whether `ResetNetworkInterfaceAttribute` on a **requester-managed** ENI returns a permission error like detach does (attachments line 95) or silently resets your-side fields (lead #4) — UG line 18 says reset is allowed; the service-plane boundary makes this a careful, stop-ready test.

## 8. Cross-references (do not duplicate — defer)
- IP assignment / takeover / EIP ride-along → `using-instance-addressing-attack-research-plan.md`, `instance-secondary-ip-addresses-attack-research-plan.md`, `working-with-ip-addresses-attack-research-plan.md`.
- Windows guest static-binding split-brain on reassignment → `config-windows-multiple-ip-attack-research-plan.md`.
- Secondary Networks SG/NACL/Flow-Log gap (lead #8) → future `eni-sn` page plan.
- Hub overview, cluster cross-cutting themes → `ec2-networking` hub plan.
