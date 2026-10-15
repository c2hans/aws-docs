# Requester-Managed Network Interfaces — Attack / Research Plan

> **Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requester-managed-eni.html`
> (verified online == offline mirror, byte-identical, 2026-10-15; `.md` and `.html` variants identical)
> **Method:** AWS `security-questionbuilder` (boundary-first). Documentation-only. No live calls were made.
> **Authoritative IAM source:** `./docs/service-authorization/latest/reference/list_ec2.md` (10,190 lines, grepped verbatim — line numbers cited inline).
> **Status:** This is the **page-level authoritative plan for the customer-VPC ↔ AWS-service-plane seam.** It develops at full depth the one-liner that `using-eni` lead #4 only flagged (Reset-on-requester-managed). It cross-references rather than duplicates: create-time Operator spoofing → `create-network-interface` Area 4; Modify/Reset attribute mechanics → `modify-network-interface-attributes`; grant teardown & describe oracle → `using-eni`; cross-VPC/shared-VPC MITM → `ec2-networking` hub.

---

## 0. TL;DR — the one sentence

> A **requester-managed network interface** is the data-plane foot that an AWS *service* (RDS, NAT gateway, PrivateLink interface endpoint, resource gateway) plants inside the customer's VPC. The page enumerates five operations the customer "can't" perform on it and three they can (view, tag, reset) — **but every one of those gates is a server-side allowlist that EC2 evaluates from the ENI's `requesterManaged` flag, and there is NO IAM condition key for that flag anywhere in the EC2 authorization reference.** The customer-side carve-outs that *are* permitted — `ResetNetworkInterfaceAttribute` (which forces `SourceDestCheck` back to `true`), `DeleteNetworkInterface` on a detached service ENI, and unconditioned tag writes — are therefore un-scopable integrity/availability/attribution primitives that reach across the shared-responsibility line into the AWS service plane. **Any confirmed effect on a requester-managed ENI is a HARD-STOP disclosure boundary: prove existence, preserve evidence, do not exploit.**

---

## 1. Components, Assets, and Design

### 1.1 What the page actually says (verbatim anchors)

- **Definition:** "A requester-managed network interface is a network interface that an AWS service creates in your VPC on your behalf. The network interface is associated with a resource for another service, such as a DB instance from Amazon RDS, a NAT gateway, or an interface VPC endpoint from AWS PrivateLink."
- **Considerations — the customer CANNOT:** Modify network interface attributes · Attach or detach · Associate or disassociate Elastic IP addresses · Assign or unassign private IP addresses · Specify the interface when launching an instance.
- **The carve-out:** "You can still reset network interface attributes, even though you can't modify them."
- **The customer CAN:** "view the requester-managed network interfaces in your account and you can add or remove tags."
- **Delete-detached lifecycle:** "When you delete the resource associated with a requester-managed network interface, the AWS service detaches the network interface and deletes it. If the service detached a network interface but didn't delete it, you can delete the detached network interface."
- **Trust-signal fields:** `Requester-managed` = "Indicates whether the network interface is managed by AWS." · `Requester ID` = "The alias or AWS account ID of the principal or service that created the network interface."
- **Recon CLI shipped on the page:** `aws ec2 describe-network-interfaces --filters "Name=requester-managed,Values=true"` → sample output leaks `VPC Endpoint Interface`, `Resource Gateway Interface` descriptions + `InterfaceType` (`interface`, `vpc_endpoint`).

### 1.2 Two concepts that look the same and are not (critical disambiguation)

`using-eni.html` documents them as **separate bullet entries linking to separate sub-pages**:

| Concept | Flag / field | Set by | Example | IAM key |
|---|---|---|---|---|
| **Requester-managed** (this page) | `requesterManaged`=true + **Requester ID** | an AWS **service** on your behalf | RDS DB instance, NAT gateway, PrivateLink interface endpoint, resource gateway | **none** (no `ec2:Requester*` key for this; only unrelated `ec2:RequesterVpc` peering key, L-grep) |
| **Managed** (adjacent) | `Managed`=true + **Operator**/`Principal` | a **service provider** (e.g. EKS Auto Mode) | EKS Auto Mode managed instance/ENI | `ec2:ManagedResourceOperator` ("presence of an EC2 operator provisioning a managed resource", L10111) |

> **Do not conflate them.** `ec2:ManagedResourceOperator` is the *only* IAM key in the neighbourhood and it keys on the **Operator/managed** concept, **not** on `requesterManaged`. Treating it as a lever over RDS/NAT/VPCE service ENIs is a near-miss trap. See Area 4.

### 1.3 Trust-boundary / ownership picture

```
         CUSTOMER ACCOUNT / VPC (customer owns)
   ┌──────────────────────────────────────────────────────┐
   │  subnet, route table, SG assignment, NACL  ← customer │
   │                                                        │
   │     ┌───────────── requester-managed ENI ───────────┐ │   SHARED-RESPONSIBILITY LINE
   │     │  requesterManaged = true                       │ │   ════════════════════════════
   │     │  Requester ID = <service alias / AWS acct id>  │◄┼───  AWS SERVICE PLANE
   │     │  attachment / IP / attrs  ← AWS service owns   │ │     (RDS / NAT GW / PrivateLink /
   │     └────────────────────────────────────────────────┘ │      resource-gateway fleet)
   │        ▲ customer-permitted ops on this object:          │
   │        │  describe · CreateTags/DeleteTags · Reset ·     │
   │        │  Delete(iff already detached)                   │
   └────────┼─────────────────────────────────────────────────┘
            │  ← every "can"/"cannot" decided server-side by EC2 reading requesterManaged;
               NO IAM condition key expresses it.
```

### 1.4 Assets

- **Integrity of the service ENI's `SourceDestCheck` attribute** (the only attribute Reset can touch) — matters for any service whose ENI forwards/translates traffic.
- **Availability of the service resource** behind the ENI (DB reachability, NAT path, PrivateLink endpoint, resource-gateway path).
- **Confidentiality of the service footprint** — which AWS/partner services run in the account's VPCs, their resource IDs, and the requester account IDs/aliases (via describe).
- **Tag-based control integrity** — cost allocation, the customer's own ABAC, and any service-side tag automation on the ENI.
- **The `requesterManaged` / `Requester ID` fields as a trust signal** consumed by customer tooling and humans ("this is AWS's, leave it alone").

---

## 2. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Customer IAM principal with broad `ec2:*NetworkInterface*` | AWS service plane's ENI object | `ResetNetworkInterfaceAttribute` on a `requesterManaged=true` ENI | Reset is **accepted** and flips `SourceDestCheck`→`true` on a service ENI → service forwarding/translation integrity altered from inside the customer account (**HARD STOP**) |
| Customer principal | AWS service's in-flight teardown | `DeleteNetworkInterface` during the service's detach-but-not-yet-deleted window | Customer deletes the service's ENI → service resource left referencing a destroyed ENI / inconsistent teardown (**HARD STOP**) |
| Customer principal | Service's ENI metadata | `CreateTags`/`DeleteTags` (unconditioned) | Customer removes/overwrites a tag the service set, or adds a tag that re-points the customer's own ABAC — on an object the customer is told it "can't manage" |
| Any read-capable principal (incl. cross-team) | Account-wide service topology | `DescribeNetworkInterfaces --filters requester-managed=true` | Full inventory of every RDS/NAT/VPCE/resource-gateway + their resource IDs + requester account IDs, with no resource-level IAM scoping |
| Customer principal creating own ENI | The `requesterManaged`/`Requester ID` trust signal | `CreateNetworkInterface` (`Operator` param) | **NULL** — no customer input sets these; `Operator` is "Reserved for internal use." (documented refutation; keep the describe-side trust-signal doubt only) |
| Customer-controlled network environment | Service ENI's data path | customer-owned route table / SG assignment / NACL around the service ENI | redirect/intercept of RDS/VPCE/NAT traffic — in-scope-by-design intra-account; cross-account only under shared-VPC (→ hub) |
| **Any customer surface** | **AWS's own fleet identity/plane** | any of the above landing on a service-owned object | **HARD STOP — preserve evidence, flag for disclosure, never exploit.** |

---

## 3. API / Interface Surface (IAM-authoritative)

| API | Mutating? | Resource type (required) | Condition keys available | Works on requester-managed ENI? | Notes (list_ec2.md) |
|---|---|---|---|---|---|
| `DescribeNetworkInterfaces` | no | — (no resource row) | `ec2:Region` only (unscopable) | **yes** (view permitted) | the shipped recon filter; account-wide, no ownership scoping |
| `ResetNetworkInterfaceAttribute` | **yes** | `network-interface*` | aws:ResourceTag, ec2:AvailabilityZone, **ec2:ManagedResourceOperator**, ec2:NetworkInterfaceID, ec2:Region, ec2:ResourceTag, ec2:Subnet, ec2:Vpc (**L9519**) | **YES — explicitly carved in by the page** | **NO `ec2:Attribute` key** (cannot scope by attribute) though the resource type *has* it (L9982). Only resets `SourceDestCheck`→`true` (API ref). |
| `ModifyNetworkInterfaceAttribute` | yes | `network-interface*` (4 rows) | per `modify-network-interface-attributes` plan | **NO — blocked server-side** | the "can't modify" guarantee. Reset is the bypass twin. |
| `DeleteNetworkInterface` | yes | `network-interface*` | aws:ResourceTag, ec2:ManagedResourceOperator, ec2:NetworkInterfaceID, ec2:Region, ec2:Subnet, ec2:Vpc (**L6088**) | **YES, iff already detached** | Description: "delete a **detached** network interface." Page: can delete if service detached-but-didn't-delete. |
| `AttachNetworkInterface` / `DetachNetworkInterface` | yes | — | — | **NO** | "can't attach or detach" |
| `AssociateAddress` / `DisassociateAddress` (L4712 / L7885) | yes | — | EIP-side scopable | **NO** | "can't associate/disassociate EIP" |
| `AssignPrivateIpAddresses` / `UnassignPrivateIpAddresses` (L—/L9696) | yes | — | — | **NO (claimed)** | "can't assign/unassign private IPs" — **Lens-X: are the IPv6 + Assign twins all blocked, or only the v4 pair the page names?** (Area 1b) |
| `CreateTags` / `DeleteTags` (L30/L1244) | yes (Tagging) | network-interface | **condition-key column BLANK on the generic rows** | **YES** (add/remove tags permitted) | unconditioned writes to a service object |
| `CreateNetworkInterface` | yes | — | `Operator` = "Reserved for internal use"; no `RequesterManaged`/`RequesterId` input | n/a | cannot mint a requester-managed ENI (Area 4 NULL) |

**Null / absent condition keys (grep-confirmed in `list_ec2.md`):**
- `requester-managed` / `RequesterManaged` / `RequesterId` → **0 hits.** No IAM key, no ABAC path, nothing — the flag is describe-filter-only.
- `ec2:Requester*` → only `ec2:RequesterVpc` (VPC-peering, unrelated).
- `ec2:Attribute` on the `ResetNetworkInterfaceAttribute` action row → absent (present on the resource type at L9982, not plumbed to Reset).

---

## 4. Boundary-Lens Catalog — Leads

Severity key: **S0** = hard-stop service-plane effect (prove existence only). Then Critical / High / Medium / Low. Every lead is a falsifiable claim with a doc anchor and a confirm/refute oracle.

### Area 1 — HEADLINE: Reset-but-not-Modify is an un-scopable integrity primitive against the service plane (Lens X / S / U) — **S0**

**Claim 1a.** The page's "you can still reset network interface attributes, even though you can't modify them" is not a benign nicety: `ResetNetworkInterfaceAttribute` *only* resets `SourceDestCheck`, and *only* forces it to `true` (API ref verbatim: "The source/destination checking attribute. Resets the value to `true`."). `SourceDestCheck=false` is mandatory for any ENI that forwards/translates traffic ("You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls." — `using-eni`). Therefore a customer principal that can call Reset on a **requester-managed** ENI belonging to a traffic-forwarding service resource can silently re-enable source/dest checking on the service plane's own interface and break the service's forwarding path — an **integrity + availability attack across the shared-responsibility line, launched entirely from inside the customer account.**
- **Mechanism:** page carve-out + `API_ResetNetworkInterfaceAttribute` (`SourceDestCheck`→true) + `using-eni` source/dest-check requirement + `ModifyNetworkInterfaceAttribute` blocked (L row) while Reset is allowed (L9519 lists the action against `network-interface*`).
- **Doc-gap to resolve first:** the NAT **gateway** basics page frames the NAT gateway as a managed construct, *not* an instance performing NAT, and does **not** say its own ENI needs `SourceDestCheck=false`. So the service classes where Reset→true actually causes breakage are undocumented. **Confirm-first:** on a canary account, enumerate requester-managed ENIs across RDS / NAT gateway / interface VPC endpoint / resource gateway and read each one's current `SourceDestCheck` value — any service ENI showing `SourceDestCheck=false` is a service that Reset could flip.
- **Confirm/refute oracle (S0 — EXISTENCE ONLY):** issue `ResetNetworkInterfaceAttribute --network-interface-id <requester-managed-eni> --source-dest-check` **against a canary-owned service resource you created**. (i) Does EC2 **accept** the call (no `requesterManaged`-based deny)? (ii) Does the ENI's `SourceDestCheck` flip to `true`? If yes to (i), the "can't modify" guarantee is bypassed via Reset regardless of (ii). **The moment acceptance is observed, STOP** — do not leave the attribute flipped, restore if the service doesn't self-heal, preserve evidence, flag for disclosure. Do **not** run this against any ENI whose `Requester ID` is an AWS service you did not provision.
- **Lens S corollary (why no admin can prevent it):** there is **no** condition key for `requesterManaged`, and Reset's action row carries **no `ec2:Attribute` key** (L9519) — so a customer security admin cannot write a policy that (a) denies Reset specifically on service-managed ENIs, nor (b) denies the `sourceDestCheck` attribute specifically. A role granted `ec2:ResetNetworkInterfaceAttribute` for legitimate self-managed ENIs inescapably also gets it on every service ENI in scope. **Severity: S0 (service-plane integrity) / Medium as a customer least-privilege footgun.**

**Claim 1b (Lens X twin-sweep).** The "cannot" list is phrased in high-level verbs ("Assign or unassign private IP addresses", "Associate or disassociate Elastic IP"). The server-side allowlist is only known to block the exact actions named. Does it also block every **twin / lower-level / newer** action that achieves the same effect — `AssignIpv6Addresses`, `UnassignIpv6Addresses`, `AssignPrivateIpAddresses` with `AllowReassignment`, `ModifyNetworkInterfaceAttribute` sub-paths exposed only in the API model (per `modify-network-interface-attributes`), `AssociateAddress` with `AllowReassociation=true`? If any twin slips the allowlist, the "cannot assign IPs / cannot associate EIP" guarantee is bypassed.
- **Oracle:** for each twin action, attempt against a canary requester-managed ENI; a non-deny proves a guarantee gap. **S0 if it mutates the service ENI.** Cross-ref the IP-takeover primitives in `using-instance-addressing`, `instance-secondary-ip-addresses`, `working-with-ipv6-addresses` — those found no source-owner checks on the assign family; the question here is whether the `requesterManaged` allowlist is the *only* thing standing between those primitives and a service ENI. **Severity: S0 / High.**

### Area 2 — Delete of a detached requester-managed ENI: premature-teardown race / orphan (Lens AA / L / S) — **S0 / High**

**Claim.** The page says if "the service detached a network interface but didn't delete it, you can delete the detached network interface," and `DeleteNetworkInterface`'s IAM description is literally "delete a **detached** network interface" (L6088). This opens a window: whenever an AWS service **transiently detaches** its ENI as part of a reconfiguration (RDS failover/scaling, VPCE AZ change, NAT gateway lifecycle), a customer with `ec2:DeleteNetworkInterface` can race in and delete the service's ENI before the service re-attaches or completes its own bookkeeping — leaving the service resource referencing a destroyed interface.
- **Mechanism:** page delete-detached sentence + L6088 description + `delete_eni.html` ("Deleting a network interface releases all attributes... and releases any private IP / EIP addresses").
- **Confirm/refute oracle (S0 — EXISTENCE ONLY):** on a canary, drive a service resource through a state that transiently detaches its requester-managed ENI (e.g. a controlled RDS/VPCE reconfiguration) and observe whether `DeleteNetworkInterface` is **accepted** during the detached window. Acceptance = the primitive exists; **do not** complete a delete that would damage a real resource — the existence of a non-deny is the finding. Preserve evidence, flag.
- **Lens S:** again no `requesterManaged` key → an admin cannot deny `DeleteNetworkInterface` only for service ENIs; broad network-admin roles cover them. **Also test:** does the customer get a distinct error on a *still-attached* service ENI vs a self-managed one (enumeration oracle for which services are mid-reconfiguration)? **Severity: S0 / High (service availability).**

### Area 3 — Unconditioned tag writes on a service-owned object (Lens I / O / U) — **Medium**

**Claim.** The page grants `CreateTags`/`DeleteTags` on requester-managed ENIs, and those actions' condition-key columns are **blank** on the generic rows (L30, L1244) — i.e. no scoping. So the customer can (a) **delete tags the service set** on its own ENI (breaking the service's tag-based automation or the customer's cost-allocation attribution), and (b) **add arbitrary tags** to a service ENI, which can re-point the customer's *own* `aws:ResourceTag`-based ABAC — e.g. tag a service ENI so it matches a `Delete`/`Reset`-allow condition the customer uses to self-scope, converting Areas 1/2 from "needs broad grant" to "works under a tag-scoped least-privilege policy."
- **Mechanism:** page ("add or remove tags") + blank condition-key cells on CreateTags/DeleteTags network-interface rows.
- **Oracle:** on a canary, (i) read a service ENI's tags, remove one, confirm removal persists (and whether the service restores it — Lens O: is there any service-side signal?); (ii) construct a customer policy that allows `ResetNetworkInterfaceAttribute` only on ENIs tagged `k=v`, then `CreateTags k=v` on a requester-managed ENI, then confirm Reset now passes the tag condition → **ABAC self-widening into Area 1 under a least-privilege policy.** **Severity: Medium (attribution/ABAC); becomes the enabler that lowers Area 1/2 preconditions).**

### Area 4 — Can a customer forge the requester-managed / Requester-ID trust signal? (Lens EE / U / X) — **largely NULL, one residual doc-gap**

**Refuted (document as null with evidence):** `CreateNetworkInterface` has **no** `RequesterManaged` or `RequesterId` request parameter; `requesterManaged` appears only in the *response* (always `false` for customer-created ENIs). The one schema element that resembles a backdoor, `Operator` (→ `ec2:ManagedResourceOperator`, L10111), is documented "Reserved for internal use." So a general customer principal **cannot mint an ENI that reports `requesterManaged=true`** or spoof a `Requester ID`. The create-side camouflage/self-protection primitive is closed. (Cross-ref `create-network-interface` Area 4 — same conclusion from the create page.)
- **Residual lead (Lens U/EE, Low, doc-gap):** `Requester ID` is "the alias or AWS account ID of the principal **or service** that created the network interface. If you created the network interface, this is your AWS account ID." So *your own* ENIs do carry a `Requester ID` = your account. Does any customer security tool / cleanup script treat "non-empty Requester ID" or "Requester-managed column present" as "AWS-owned, skip" without checking `requesterManaged=true` specifically? If so, an attacker's ordinary ENI (which legitimately has a Requester ID = the attacker's account) could be mis-skipped by sloppy tooling. This is a *consumer-of-the-field* question, not an EC2 defect — mark **doc-gap / tooling-dependent, Low.**
- **Inverse twist (Lens O, cross-ref):** the *adjacent* `managed` concept moves the other way — effective **2026-04-22**, EKS Auto Mode managed resources incl. ENIs are **hidden from `describe` list operations by default** while remaining "fully operational and billable." That is an audit-visibility / stealth-persistence / cost angle on the `managed` surface (not requester-managed). Owned by whatever plan covers EKS Auto Mode managed instances; noted here only to keep the two concepts' audit postures straight (requester-managed = **visible** recon oracle, Area 5; managed = **newly invisible**).

### Area 5 — The requester-managed describe filter as a cross-service recon oracle (Lens A / O) — **Medium (info-disclosure)**

**Claim.** The page itself ships `describe-network-interfaces --filters "Name=requester-managed,Values=true"`, and `DescribeNetworkInterfaces` has **no resource row / no resource-level condition keys** (only `ec2:Region`). So any read-capable principal — including a low-privilege or cross-team role — can enumerate, account-wide, **every** AWS service with a foot in the account's VPCs: the `Description` field leaks `vpce-…`, resource-gateway, RDS, and NAT gateway resource IDs; `InterfaceType` distinguishes `vpc_endpoint` vs `interface`; and `Requester ID` leaks the **AWS account IDs / service aliases of the requesters** (for PrivateLink, this reveals *which SaaS/partner services the account consumes* — a sensitive supply-chain signal).
- **Mechanism:** shipped CLI on the page + unscopable `DescribeNetworkInterfaces` (consistent with the sibling plans' finding that EC2 Describe actions are account-wide-unscopable).
- **Oracle:** a role with only `ec2:DescribeNetworkInterfaces` returns the full requester-managed inventory; confirm no tag/ARN/ownership scoping can restrict it (there is no resource row to attach a condition to). **Lens O:** does reading it emit anything to the services? No. **Severity: Medium** — same inert-ABAC shape as the corpus's other Describe oracles, but the net-new *content* is the complete AWS/partner service topology + requester account IDs. Cross-ref `using-eni` (which owns the general ENI Describe-oracle framing); this plan owns the **requester-managed-filter / service-topology-disclosure** specialization.

### Area 6 — The service ENI as a reachability seam the customer still surrounds (Lens D / V) — **thin pointer**

**Claim.** Even though the customer "can't manage" the requester-managed ENI itself, the customer **owns the network context around it**: the subnet, the route table, the security-group *assignment* (for VPCE the customer sets the endpoint SG), and the NACLs. So the customer can influence or intercept the data path to/from the service ENI (e.g. black-hole or redirect the RDS/VPCE/NAT path, or scope SGs to observe reachability). Intra-account this is in-scope-by-design (the customer owns their VPC). The seam only becomes a cross-account boundary under **shared VPC** (a *participant's* service ENI living in the *owner's* subnet, or vice-versa).
- **Oracle / scope:** cross-account MITM/redirect of a service ENI's path under shared VPC. **Defer the mechanism** to `using-eni` (cross-VPC attach / MITM) and the `ec2-networking` hub (shared-VPC isolation guarantees). Kept here only to close the coverage sweep. **Severity: deferred.**

---

## 5. Null Hypotheses (checked, with pages read)

- **Spoofing/minting a requester-managed ENI — NULL.** Read `API_CreateNetworkInterface` (no `RequesterManaged`/`RequesterId` input; `Operator` reserved-internal) + the target page. Closed. (Area 4.)
- **`ec2:ManagedResourceOperator` as a lever over RDS/NAT/VPCE service ENIs — NULL/trap.** Read L10111 + `using-eni` + `amazon-ec2-managed-instances`. It keys on the *Operator/managed* concept (EKS Auto Mode), a different attribute from `requesterManaged`. No overlap for RDS/NAT/PrivateLink.
- **Injection / translation-layer (Lens F), credential-vending (Lens C), PassRole (Lens B) — N/A on this page.** Read the target page, `using-eni`, `scenarios-enis`, `delete_eni`, `modify-network-interface-attributes`: the requester-managed surface exposes no customer-supplied data that a service parses here, no role ARN input, no STS path. These live in the owning services' own docs (RDS/PrivateLink), not in the ENI-management surface.
- **Reset resetting attributes other than `SourceDestCheck` — NULL.** `API_ResetNetworkInterfaceAttribute`: "You can specify only one attribute at a time," and the sole documented parameter is `SourceDestCheck`. No other attribute is resettable, so Reset's blast radius is exactly source/dest checking.

---

## 6. Prioritized Research Queue

| # | Lead | Lens | Severity | First action (confirm-first) |
|---|---|---|---|---|
| 1 | Reset→`SourceDestCheck=true` accepted on a service ENI (integrity/availability) | X/S/U | **S0** | Enumerate canary service ENIs' current `SourceDestCheck`; test Reset acceptance on a canary-owned one; STOP on accept |
| 2 | Twin-sweep: do IPv6/assign/associate twins bypass the "cannot" allowlist? | X | **S0 / High** | Attempt each twin against a canary requester-managed ENI; non-deny = gap |
| 3 | Delete-detached race during service reconfiguration | AA/L/S | **S0 / High** | Drive canary service to transient-detach; observe Delete acceptance in the window |
| 4 | Tag-write ABAC self-widening → lowers #1/#3 preconditions | I/O/U | Medium (enabler) | CreateTags to satisfy a self-scoped Reset/Delete condition; confirm |
| 5 | requester-managed describe = account-wide service-topology + requester-acct-ID oracle | A/O | Medium | Low-priv role runs the shipped filter; confirm no scoping possible |
| 6 | Requester-ID / Requester-managed-column trust-signal mis-consumption by tooling | EE/U | Low (doc-gap) | Review customer cleanup-tool logic (out-of-band) |
| — | Shared-VPC MITM of a service ENI path | D/V | deferred | → `using-eni` / `ec2-networking` hub |

---

## 7. HARD-STOP / Rules of Engagement (restate for the hunter)

- A `requesterManaged=true` ENI **is the AWS service plane.** Any confirmed effect on one (accepted Reset, accepted Delete, mutated attribute, torn-down service resource) is a shared-responsibility-line crossing: **prove existence with the minimum observation, preserve evidence, flag for disclosure, and STOP. Never exploit, escalate, iterate, or leave the service ENI in a mutated state.**
- Only ever test against **canary service resources you provisioned yourself** in an authorized account. Never touch an ENI whose `Requester ID` is a service/account you did not create.
- Reads (Area 5) are low-risk but still stop at *existence of the disclosure* — do not harvest a full production inventory.
- Honor the global 3600 s budget; this plan is a documentation-derived lead set, not an execution log.

---

## 8. Handoff Notes (for the next agent / orchestrator)

- **This plan is authoritative for the requester-managed (customer-VPC ↔ AWS-service-plane) seam.** Siblings own the depth cross-referenced above; do not re-derive:
  - create-time Operator spoofing & all-5-ENI-attributes-unscopable-at-create → `create-network-interface` plan (Area 4 there).
  - Modify/Reset attribute mechanics, the 4-row Modify resource model, `ec2:Attribute` audit → `modify-network-interface-attributes` plan.
  - General ENI lifecycle, grant teardown (`DeleteNetworkInterfacePermission`), cross-VPC attach/MITM, and the general Describe oracle → `using-eni` plan.
  - Shared-VPC isolation guarantees & EFA/SRD → `ec2-networking` hub.
  - IP-assignment takeover primitives the twin-sweep (#2) feeds into → `using-instance-addressing`, `instance-secondary-ip-addresses`, `working-with-ipv6-addresses`.
- **The single highest-value, lowest-ambiguity lead is #1** (Reset→SourceDestCheck=true on a service ENI): it is a documented carve-out, with a documented single-attribute effect, with a documented "forwarding needs it false" requirement, and **provably no IAM key to prevent it.** Confirm-first = read the current `SourceDestCheck` of real requester-managed ENIs; the subset with `false` are the exposed services.
- **IAM ground truth** is `list_ec2.md`, not the User Guide prose. The decisive nulls (no `requesterManaged` condition key, no `ec2:Attribute` on Reset's action row) are what make Areas 1–3 un-scopable rather than merely risky.
- Online == offline verified for the target page on 2026-10-15.
