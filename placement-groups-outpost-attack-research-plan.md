# Placement Groups on AWS Outposts — Attack Research Plan

> **Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups-outpost.html
> (offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/placement-groups-outpost.md`)
> **Service:** Amazon EC2 — placement groups, Outpost sub-surface
> **Plan type:** page-level **CHILD / COMPLEMENT** of `placement-groups-attack-research-plan.md` (the EC2 placement-groups HUB).
> **Built with:** `security-questionbuilder` skill (6-step boundary-first method).
> **Offline/online drift:** `placement-groups-outpost.md` and `sharing-outposts.md` are byte-identical offline vs. live (2026-10-15, verified by two subagents). **CAVEAT:** the online `list_ec2.md` IAM Service Authorization Reference is **truncated** mid-"Actions" and never reaches the condition-key table — the **offline** `list_ec2.md` (10,190 lines) is authoritative for all IAM-key claims below.

---

## 0. Relationship to the hub plan — THIS PLAN CORRECTS A WRONG NULL

The hub plan (`placement-groups-attack-research-plan.md`) files the Outpost page as **Area 8 — NULL / out-of-scope**, reasoning:

> "an Outpost is provisioned/billed to a single owning account; `list_outposts.md` has no sharing action; self-co-residency only, not a security boundary."

**That verdict is factually wrong**, on two independent counts proven in this plan:

1. **The hub checked the wrong resource.** The `outposts:` *service* API genuinely has no `ShareOutpost` action (hub was right about that narrow fact) — but Outpost sharing does not live there. It lives in **AWS RAM** (`ram:CreateResourceShare`) and in **EC2's resource-policy actions** (`ec2:PutResourcePolicy` / `ec2:DeleteResourcePolicy`). Checking `list_outposts.md` for a share action and concluding "not shareable" is a false negative.
2. **Outpost placement groups ARE multi-account by design.** Multiple distinct AWS accounts can land instances on the *same physical Outpost hardware* via at least three independent RAM share units — and one of them (`ec2:PlacementGroup`) is shareable to accounts **outside** the owner's organization.

**Headline correction:** A shared Outpost placement group is a **genuine, physically-bounded, multi-account co-residency surface** — arguably the *strongest* cross-tenant co-residency primitive in the entire placement-groups family, because the physical pool is a handful of racks/hosts at one customer site (not a Region-scale pool), so forced co-residency is near-deterministic rather than probabilistic.

This plan **owns** the Outpost-specific net-new surface and **defers** everything the hub already covers (see §8). It does not restate hub Areas 1–7.

---

## 1. Pentest Objectives

Confirm or refute, from documentation, that:

- **O1 (headline).** Two *different* AWS accounts can place EC2 instances onto the *same physical Outpost* (owner's on-prem rack/host) via RAM sharing — and that this is reachable **cross-organization** through placement-group sharing, not only within-org. → Lens A, V, U.
- **O2.** The host-vs-rack `SpreadLevel` sub-dimension (net-new on this page) has **no IAM condition-key representation**, so an administrator cannot author a policy that pins or restricts it. → Lens S.
- **O3.** The placement-group / instance-launch / subnet-creation code path has **no `ec2:OutpostArn` scoping**, so an admin cannot restrict *which Outpost* a role may build a PG on, launch onto, or carve a subnet in — even though `ec2:OutpostArn` exists and is used for Capacity-Reservation and snapshot actions. → Lens S, U.
- **O4.** **Unshare is incomplete by design**: after the owner revokes a share, the consumer's instances/subnets/volumes survive, remain modifiable, and the consumer can **launch new instances** onto a surviving subnet — a cross-account foothold that persists on the owner's physical hardware past revocation. → Lens AA.
- **O5.** The **owner is an asymmetric super-tenant** over consumer resources on a shared Outpost (can view/modify/delete them) — *except* instances consuming shared Capacity Reservations — and whether the stated consumer↔consumer isolation ("can't view or modify resources owned by other consumers") actually holds on shared physical hardware. → Lens U, A.
- **O6.** The spread-PG capacity ceiling (= physical host/rack count) is a **shared, hard, cross-account exhaustion ceiling** and simultaneously a **physical-topology disclosure oracle** (PG capacity reveals the owner's host/rack count). → Lens L, A/topology.

**Severity ceiling:** cross-**account/organization** co-residency on physical on-prem hardware = **Critical**. Any evidence the surface reaches **AWS's own fleet/service plane is a HARD STOP** — preserve evidence, flag for disclosure, do not proceed.

---

## 2. Components, Assets, and Design

### 2.1 What the page actually introduces

`placement-groups-outpost.md` is short (28 lines) and says four load-bearing things:

1. "You can create placement groups on Outposts **that you have created in your account**." (The page assumes single-account framing — this is exactly the assumption the sharing docs break.)
2. **Net-new sub-dimension:** "When you create a placement group with a **spread** strategy on an Outpost, you can choose to have the placement group spread instances across **hosts or racks**. Spreading instances across hosts allows you to use a spread strategy with a single-rack Outpost."
3. **Capacity considerations (physical-count disclosure):** "A **rack-level** spread PG can hold as many instances as you have **racks**… A **host-level** spread PG can hold as many instances as you have **hosts**."
4. **3-step procedure:** (a) create a subnet on the Outpost; (b) create a PG *in the associated Region* (host- or rack-level spread); (c) launch an instance into the PG, choosing the Outpost subnet.

### 2.2 The mechanism the page omits (pulled from linked/sibling docs)

- **`SpreadLevel` API parameter** (`API_CreatePlacementGroup.md` lines 50–56): `SpreadLevel: host | rack`, `Required: No`; "`host` — You can use `host` only with Outpost placement groups." `API_PlacementGroup.md` line 49: "**Only** Outpost placement groups can be spread across hosts." Describe-side filter `spread-level` (`host|rack`) exists (`API_DescribePlacementGroups.md` line 29).
- **The PG is a *Regional* resource** (step 2 says "in the associated Region of the Outpost"), but the *hardware* it governs is the on-prem Outpost. So the PG object lives in the Region's control plane while its placement decisions bind physical on-prem hosts/racks. Ownership of the PG object and ownership of the hardware can diverge across accounts.
- **Outpost RAM sharing** (`sharing-outposts.md`, verified byte-identical offline/online): owner shares Outpost resources with consumers in the **same AWS organization**; "This allows other consumers to use Outpost sites, configure VPCs, and **launch and run instances on the shared Outpost**." Shareable units (verbatim): Allocated Dedicated Hosts, Capacity Reservations, CoIP pools, Local gateway route tables, Outposts, S3 on Outposts, Sites, **Subnets** ("Launch and run EC2 instances in subnets").
- **Placement-group RAM sharing** (`share-placement-group.md`, per subagent): `ec2:PlacementGroup` is shareable to **"Specific AWS accounts inside or outside of its organization"** — i.e. **cross-org**. Consumer "must specify a shared placement group by **ID**, not by name." Required perms: `ec2:PutResourcePolicy`, `ec2:DeleteResourcePolicy`.
- **AZ-ID consistency** (`sharing-outposts.md` §Sharing across Availability Zones): AZ *names* are randomized per account; the **AZ-ID** (`use1-az1`) is "a unique and consistent identifier … the same location in every AWS account." → the physical locator a cross-account attacker uses to confirm two accounts' resources are co-located.

### 2.3 Assets

- **Primary asset:** physical compute capacity (hosts/racks) in a single-site Outpost deployment, co-occupied by multiple AWS accounts' instances.
- **The co-residency relationship itself** (which account's instance sits on which physical host/rack) — a side-channel/targeting asset.
- **The owner's physical topology** (host count, rack count) — disclosed indirectly by spread-PG capacity limits.
- **Consumer-created subnets/volumes/instances** that survive unshare.

### 2.4 Identifiers & entropy

- `pg-...` placement-group IDs; shared PGs referenced **by ID** cross-account.
- `op-...` Outpost IDs; `os-...` site IDs; `subnet-...`; `cr-...` Capacity Reservation IDs; `h-...` Dedicated Host IDs.
- **AZ-ID** (`use1-az1`) — stable cross-account physical locator.

### 2.5 ASCII design (shared Outpost)

```
   Owner account (A)                         Consumer account (B)  [same org OR, for PG-share, ANY account]
   ┌──────────────────────┐                  ┌──────────────────────┐
   │ creates Outpost op-…  │   AWS RAM share  │ accepts share        │
   │ creates subnet on OP  │ ───────────────▶ │ launches EC2 into    │
   │ creates PG pg-… (host/│  (Outpost|Subnet │  shared subnet / PG  │
   │   rack spread)        │   |CapRes|PG)    │  by ID               │
   └─────────┬────────────┘                  └──────────┬───────────┘
             │                                          │
             ▼                                          ▼
   ╔═══════════════════════════════════════════════════════════════╗
   ║   ONE physical Outpost at owner's site  (few racks / hosts)     ║  ← the trust boundary that
   ║   ┌─────rack 1─────┐ ┌─────rack 2─────┐  …                      ║    the page silently assumes
   ║   │ host  host host│ │ host  host host│                         ║    does not exist
   ║   │ [A-inst][B-inst]│ │ [B-inst][A-inst]│   ← cross-account      ║
   ║   └────────────────┘ └────────────────┘      CO-RESIDENCY       ║
   ╚═══════════════════════════════════════════════════════════════╝
             ▲ owner = super-tenant over B's resources (except CR-consuming instances)
             ▲ control plane: PG object lives in the associated Region; hardware is on-prem
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Consumer account B | Owner A's physical Outpost host/rack | RAM-shared Outpost/Subnet/CapRes/**PlacementGroup** → `RunInstances` into shared subnet/PG by ID | **An instance owned by B running on the same physical host/rack as A's instance is the intended-but-dangerous state; the breach is any read of A's (or another consumer's) instance data/memory/metadata, or any co-residency side-channel, from B's co-resident instance.** |
| Consumer B (cross-**org**, outside A's AWS Organization) | Owner A's physical Outpost | `ec2:PlacementGroup` RAM share "inside or outside of its organization" + launch-by-ID | **A non-org account placing an instance onto A's on-prem hardware at all** — the org boundary the Outpost sharing prose implies ("within your organization") does NOT hold for PG sharing. |
| Consumer B (post-unshare) | Surviving subnet/instances on A's Outpost | Owner removes RAM share; consumer resources "are not deleted" | **B launching a NEW instance onto A's physical Outpost after A revoked the share** = surviving-access-after-revoke. |
| Consumer B | Another consumer C's resources on same Outpost | Shared physical substrate | Doc asserts "Consumers can't view or modify resources owned by other consumers" — **any view/modify of C's resource by B is a breach of a stated guarantee.** |
| Owner A | Consumer B's CR-consuming instances | Owner super-tenant powers | Doc asserts owner **cannot** modify "instances that consumers launch into Capacity Reservations that they have shared" — **owner modifying/terminating such an instance is a breach of the one stated owner limit.** |
| IAM admin (owner org) | "which Outpost / which spread level" policy intent | `CreatePlacementGroup`/`RunInstances`/`CreateSubnet`/`ModifyInstancePlacement` | **No `ec2:OutpostArn` and no SpreadLevel key on these actions → the admin's intended restriction is silently unexpressible; any role with the bare action reaches every Outpost.** |
| Any customer | AWS service/fleet plane | — | **HARD STOP** — any AWS-owned identity/ARN/host reached via this surface: preserve, flag, stop. |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internet-callable | Authorized callers | Outpost/spread scoping keys | Notes |
|---|---|---|---|---|---|---|---|
| `CreatePlacementGroup` | SDK | Existing (SpreadLevel enum extended for Outpost) | **Yes** | Yes | account principals w/ action | **NONE** — only `aws:RequestTag`, `aws:TagKeys`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region` (offline `list_ec2.md` 5370–5374). **No `ec2:OutpostArn`, no SpreadLevel key.** | `SpreadLevel: host\|rack`, Required:No. `ec2:PlacementGroupStrategy` only sees cluster/spread/partition (not even precision-time) — no host/rack sub-value. |
| `RunInstances` (placement-group row) | SDK | Existing | **Yes** | Yes | all account principals | `placement-group` row (line 9596): `ec2:PlacementGroupName/Strategy`, `ec2:LaunchTemplate`, tags, Region. **No `ec2:OutpostArn` on ANY of RunInstances' 13 resource rows.** | The actual co-residency action. Launch into shared subnet + shared PG by ID. |
| `ModifyInstancePlacement` | SDK | Existing | **Yes** | Yes | account principals | placement-group row (8873–8878): same keys as Create; **no `ec2:OutpostArn`.** | Moves an instance between hosts/racks within a group — host/rack retarget unscopable. |
| `CreateSubnet` (on Outpost) | SDK | Existing | **Yes** | Yes | account principals / Outpost consumers | lines 5477–5482: **no `ec2:OutpostArn`.** | Step 1 of the procedure; the subnet is the launch anchor that survives unshare. |
| `DescribePlacementGroups` | SDK | Existing | No | Yes | account principals | has `spread-level` **filter** (`host\|rack`) but Describe scoping is the hub's unscopable-read-oracle concern (Area 3). | Reveals spread-level + capacity → topology disclosure. |
| `ram:CreateResourceShare` / `ec2:PutResourcePolicy` | SDK | Existing | **Yes** | Yes | resource owner | — | The share mechanism. PG share reaches **cross-org**. |
| `ec2:DeleteResourcePolicy` / RAM disassociate | SDK | Existing | **Yes** | Yes | resource owner | — | Unshare — **incomplete by design** (see §5 Area 4). |
| `DescribeInstanceTopology` | SDK | Existing | No | Yes | account principals | — | `nn-` node side-channel — **owned by `ec2-instance-topology` plan**; cross-ref only. AZ-ID is the Outpost analogue of the physical locator. |

**Undocumented/console-hidden knob:** `SpreadLevel=host` on a *non-Outpost* (regional) spread PG — the API says "host only with Outpost PGs," but **no doc states the runtime behavior** (hard reject vs. silent coercion to rack vs. accepted-and-ignored). `API_CreatePlacementGroup.md` Errors section (82–85) has no SpreadLevel-specific entry. → open question for the hunter (§7-Q7). `ParentGroupId`/`PartitionCount` are real request params with **no** IAM key either.

---

## 5. Recommended Areas of Focus (firing lenses)

### Area 1 — Cross-account / cross-ORG co-residency on physical Outpost hardware **[Lens A + V — HEADLINE, Critical, HARD-STOP class]**

- **Claim.** Two different AWS accounts can place EC2 instances on the same physical Outpost host/rack; a consumer instance can then reach another account's instance (owner's or another consumer's) via the shared physical substrate (memory, local network, side-channel), breaking tenant isolation.
- **Mechanism (doc evidence).** `sharing-outposts.md:8` "launch and run instances on the shared Outpost"; `:56-58` Subnets consumer can "Launch and run EC2 instances"; `share-placement-group.md` PG shareable "inside **or outside** of its organization," launch "by ID"; `placement-groups-outpost.md:12` spread places instances "across hosts or racks" of the one physical Outpost. Physical pool is a few racks at one site → co-residency is near-deterministic, unlike Region-scale cluster PGs (hub Area 1).
- **Confirm/Refute oracle.** (a) Instance in account B lands on the same AZ-ID + Outpost as account A's instance (confirm via AZ-ID `use1-az1` match + `DescribeInstanceTopology`/`nn-` node equality — cross-ref hub Area 1 / `ec2-instance-topology` plan). (b) **Breach** = any read of A's data/metadata/memory, or a working cross-instance side-channel, from B's co-resident instance. (c) **Cross-org breach** = B is in a *different* AWS Organization than A and still lands on A's hardware (PG-share path only).
- **Preconditions.** Owner shares Outpost/subnet (org-only) OR placement group (any account). Consumer accepts share, launches by ID.
- **Severity.** Cross-account on physical on-prem hardware = **Critical**. Cross-org amplifies (no org trust assumption). **If the co-resident "neighbor" turns out to be AWS's own fleet → HARD STOP.**
- **Stop condition.** Co-residency confirmed + one isolation-breach oracle fires → stop, document, do not escalate/exfiltrate.

### Area 2 — Host-vs-rack `SpreadLevel`: a placement knob with zero IAM representation **[Lens S — net-new, Medium–High]**

- **Claim.** An administrator cannot write any IAM policy that pins, requires, or forbids `SpreadLevel=host` vs `rack`; the sub-dimension is invisible to authorization.
- **Mechanism.** Subagent grep of full offline `list_ec2.md` (10,190 lines): **zero** matches for `SpreadLevel`/`spread-level`/`host-level`/`rack-level`/`PartitionCount`/`ParentGroupId`. Only PG keys that exist: `ec2:PlacementGroup`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy` (lines 10131–10133) — and `PlacementGroupStrategy` resolves only to cluster/spread/partition, never the host/rack sub-value. `CreatePlacementGroup`/`ModifyInstancePlacement` carry none.
- **Confirm/Refute oracle.** Author a Deny-unless-`SpreadLevel=rack` policy — **there is no condition key to express it** → refutes any claim that host-level spread can be governed. Confirm by API: a role restricted only by `ec2:PlacementGroupStrategy=spread` can still freely choose `host` level.
- **Severity.** Medium–High. The host-level choice (and `host` reachable only on Outposts) is a security-relevant placement decision (determines whether a consumer's instances pack onto fewer physical hosts) that is wholly outside policy control. This **extends** the hub Area 4 statement "no IAM key exists for … spread level" with the verbatim confirmation and the specific actions.

### Area 3 — No `ec2:OutpostArn` on the PG/launch/subnet path = unscopable "which Outpost" **[Lens S + U — net-new, Medium–High]**

- **Claim.** `ec2:OutpostArn` exists as a real EC2 condition key, but is **absent** from `CreatePlacementGroup`, every `RunInstances` resource row, `CreateSubnet`, and `ModifyInstancePlacement` — so an admin cannot restrict which Outpost a role builds a PG on, launches onto, or carves a subnet in. The scoping surface is inconsistent: it was wired to Capacity-Reservation and snapshot/image actions but never to the placement-group / instance-launch / subnet code path.
- **Mechanism.** Subagent mapped all 20 `OutpostArn` occurrences: present on `CreateCapacityReservation(BySplitting)`, `Copy/CreateSnapshot(s)`, `CreateImage`/`RegisterImage`, `RequestSpot*`, billing-ownership actions, and the `capacity-reservation`/`snapshot` resource types (offline lines listed in §4). **Absent** from `CreatePlacementGroup` (5370–5374), `RunInstances` (all 13 rows, incl. placement-group 9596), `CreateSubnet` (5477–5482), `ModifyInstancePlacement` (8873–8878).
- **Confirm/Refute oracle.** Try to author `CreatePlacementGroup` + condition `ec2:OutpostArn = <specific op->` — the key is not evaluated for this action → any role with bare `CreatePlacementGroup`/`RunInstances` reaches **every** Outpost the account can see, including shared-in ones. Compare against `CreateCapacityReservation`, where the same condition *does* restrict.
- **Severity.** Medium–High. Combined with Area 1, a least-privilege intent ("this role may only build PGs on our dev Outpost") is silently unenforceable; a compromised/over-broad role can target any shared Outpost. **This is an AWS-owned IAM-surface defect (asymmetric key coverage), reportable on its own.**

### Area 4 — Unshare is incomplete: surviving cross-account foothold after revoke **[Lens AA — net-new, High]**

- **Claim.** After the owner revokes the RAM share, the consumer retains a working foothold on the owner's physical Outpost: existing instances/subnets/volumes survive, stay modifiable, and the consumer **can launch NEW instances** onto a surviving consumer-created subnet. Revocation is not self-sufficient — it requires an out-of-band request to the consumer.
- **Mechanism (verbatim).** `sharing-outposts.md:131-135`: "Subnets, volumes, or instances that the consumer created during the shared period **are not deleted** and the consumer can continue to: **Access and modify these resources. Launch new instances on an existing subnet that the consumer created.** To prevent the consumer from … launching new instances on your Outpost, **request that the consumer delete their resources.**" Also `:137` local gateway route-table VPC associations survive unshare.
- **Confirm/Refute oracle.** After owner issues `DeleteResourcePolicy`/RAM disassociate, consumer calls `RunInstances` into the surviving subnet → **success = breach** (new workload placed on owner's physical hardware post-revocation, with no owner action able to stop it short of asking the consumer to self-delete).
- **Severity.** High. A revoked tenant keeps *and can grow* its presence on your physical hardware; the only documented remediation is social (ask them to delete). Compare hub Area 2 (sharing-lifecycle completeness) and `efa`/`eni` revoke-doesn't-sever findings — this is the Outpost-physical-hardware instance of surviving-access-after-revoke.
- **Stop condition.** One post-unshare `RunInstances` success demonstrates the gap → stop.

### Area 5 — Owner super-tenant asymmetry + the CR-consuming-instance exception **[Lens U + A — net-new, Medium (owner-side) / High (if consumer-isolation claim breaks)]**

- **Claim(s).** (a) The owner can view/modify/**delete** resources that consumers create on a shared Outpost — a broad asymmetric super-tenant power the page never warns consumers about. (b) The one documented exception — "owners **can't** modify instances that consumers launch into Capacity Reservations that they have shared" — is a hard, testable limit; owner modifying/terminating such an instance is a breach of a stated guarantee. (c) The symmetric consumer-isolation claim ("Consumers **can't** view or modify resources owned by other consumers or by the Outpost owner") is a stated boundary to test directly.
- **Mechanism (verbatim).** `sharing-outposts.md:10` "With the exception of instances that consume Capacity Reservations, owners can also view, modify, and delete resources that consumers create on shared Outposts. Owners can't modify instances that consumers launch into Capacity Reservations that they have shared." `:12`/`:176` consumer-isolation claim.
- **Confirm/Refute oracle.** (b) Owner attempts `ModifyInstanceAttribute`/`TerminateInstances` on a consumer instance consuming a shared CR → **success = breach of the stated owner limit**. (c) Consumer B attempts to view/modify consumer C's instance/subnet on the same Outpost → **any success = breach of the consumer-isolation guarantee** (Lens A on shared physical substrate). (a) Document the super-tenant power as a consumer-trust hazard (owner can delete consumer workloads — a griefing/availability lever, and a confidentiality concern if "view" includes instance metadata/console/volume access).
- **Severity.** (a) Medium (consumer-trust hazard, by-design but under-disclosed). (b)(c) High if either stated boundary breaks. **Cross-check capability claims against the EC2 control-plane API** — the doc asserts owner powers "using AWS Organizations"; verify the actual API path and whether CR-exception enforcement is real or prose-only.

### Area 6 — Spread-PG capacity ceiling = shared exhaustion limit + physical-topology disclosure **[Lens L + A — net-new, Low–Medium]**

- **Claim.** (a) A spread PG's capacity equals the owner's physical host/rack count — so the PG capacity error/limit **discloses the owner's physical topology** (how many hosts/racks the Outpost has) to any account that can create/launch into a spread PG on it. (b) The physical host/rack pool is a hard, small, **shared** ceiling; one account (owner or a consumer) filling the hosts denies placement to all others on that Outpost.
- **Mechanism (verbatim).** `placement-groups-outpost.md:15-16` "A rack-level spread PG can hold as many instances as you have **racks** … A host-level spread PG can hold as many instances as you have **hosts** in your Outpost deployment." Physical pool is finite and single-site.
- **Confirm/Refute oracle.** (a) Launch into a spread PG until capacity error → the max instance count = host (or rack) count = topology leak. (b) Fill hosts from one account → co-tenant `RunInstances` fails with insufficient-capacity = cross-account availability DoS on physical hardware.
- **Severity.** Low–Medium. Topology disclosure is a recon aid for Area 1 targeting; the exhaustion is a cross-account availability lever bounded by the (small) physical pool. Compare hub Area 7 (PG resource exhaustion) — this is the physically-bounded, cross-account-amplified Outpost variant. Note: `service quotas apply per individual account` (`sharing-outposts.md:192`) governs API quotas, **not** the shared physical pool — so per-account quotas do **not** prevent the shared-pool exhaustion.

---

## 6. Threat Model Test Objectives (hunter checklist)

1. **O1/Area1:** Stand up owner (A) + consumer (B) accounts; share Outpost/subnet (org path) AND placement group (cross-org path); from B launch by ID; confirm AZ-ID + `nn-` co-residency with A; attempt one isolation-breach oracle. **HARD STOP if neighbor is AWS fleet.**
2. **Area1 cross-org:** Prove the PG share reaches a B that is *outside* A's AWS Organization (the share-placement-group "inside or outside of its organization" claim).
3. **Area2:** Demonstrate no IAM policy can constrain `SpreadLevel` (author attempt fails; `host`-level freely chosen under a `strategy=spread`-only grant).
4. **Area3:** Demonstrate `ec2:OutpostArn` condition is ignored on `CreatePlacementGroup`/`RunInstances`/`CreateSubnet`/`ModifyInstancePlacement` but honored on `CreateCapacityReservation` (asymmetry).
5. **Area4:** Owner unshares; consumer still launches a NEW instance onto the surviving subnet (post-revoke foothold).
6. **Area5b:** Owner attempts to modify/terminate a consumer's CR-consuming instance (should fail per doc — confirm the limit is enforced, not prose).
7. **Area5c:** Consumer B attempts to view/modify consumer C's resources on the same Outpost (should fail per doc — confirm isolation holds on shared substrate).
8. **Area6:** Launch-to-capacity to read off host/rack count (topology leak) and to deny a co-tenant's placement (shared-pool DoS).
9. **Q7 (doc-gap):** Determine runtime behavior of `SpreadLevel=host` on a non-Outpost spread PG (reject vs silent-coerce vs accept-ignore) — undocumented in all four pages.

---

## 7. Open questions / doc-gaps

- **Q-A.** Does `SpreadLevel=host` on a *regional* (non-Outpost) spread PG hard-reject, silently coerce to `rack`, or accept-and-ignore? No doc states it; `API_CreatePlacementGroup.md` Errors (82–85) has no SpreadLevel entry. (→ §6 step 9.)
- **Q-B.** For the **PG-share cross-org** path (Area 1), does the consumer still need an *independent* grant to launch into a subnet on the Outpost, or does PG-sharing-by-ID alone suffice? Subagent read the procedure as "PG-share is a parallel, sufficient RAM grant *provided* the consumer also has a path to launch into a subnet on that Outpost" — the exact minimal grant set is a doc-gap worth pinning before the hunter builds the harness.
- **Q-C.** Does the owner's "view/modify/delete consumer resources" super-power (Area 5a) extend to reading instance **volume contents / console / memory**, or only metadata-level modify/delete? The prose doesn't delimit "view."
- **Q-D.** Is the consumer↔consumer isolation (Area 5c) enforced by VPC/account boundaries (likely holds) or merely asserted? Test, don't assume.

---

## 8. Out-of-scope / deferred to siblings (do NOT restate)

- **Co-residency side-channel via `DescribeInstanceTopology` `nn-` nodes** → `ec2-instance-topology-attack-research-plan.md` (hub Area 1 cross-refs it). This plan uses AZ-ID + topology only as a *confirmation oracle* for Area 1.
- **Generic cluster-PG cross-tenant co-residency in a Region** → hub Area 1.
- **PG sharing lifecycle (share/accept/revoke) in general** → hub Area 2; this plan owns only the Outpost-physical-hardware unshare-incompleteness (Area 4).
- **Unscopable `DescribePlacementGroups` read oracle** → hub Area 3.
- **General placement-knob IAM scoping gaps** → hub Area 4; this plan owns the Outpost/SpreadLevel-specific confirmations (Areas 2–3).
- **spread/partition = availability-not-security** framing → hub Area 5.
- **PG name squatting (names are account-scoped; shared PGs referenced by ID)** → hub Area 6. (Note: by-ID cross-account reference *mitigates* name squat for shared PGs — minor corroboration, no new finding.)
- **Generic PG resource exhaustion (500/Region)** → hub Area 7; this plan owns the physically-bounded Outpost variant (Area 6).
- **Zero EC2 org condition keys** (`aws:PrincipalOrgID`/`ResourceOrgID`/`ResourceOrgPaths` = 0 hits in `list_ec2.md`) → established across all EC2 plans; relevant here because "within your organization" (Outpost/subnet share) is a **RAM/SCP** boundary, never an EC2 resource-level condition — and the PG-share path doesn't even claim org-scoping.
- **Capacity Reservations on Outposts** detail (shareable via RAM; "can't use CR groups on an Outpost") → `capacity-reservations-outposts.md`; referenced here only as a secondary share unit (Area 1) and the owner-exception source (Area 5b).
- **S3 on Outposts, CoIP pools, local gateway route tables** sharing → separate Outpost surfaces, not placement-group-relevant (noted for completeness).

---

## 9. Null hypotheses (lenses checked, not firing)

Pages checked for triggers: `placement-groups-outpost.md`, `create-placement-group.md`, `sharing-outposts.md`, `capacity-reservations-outposts.md`, `launch-instance.md` (Outpost UG), `API_CreatePlacementGroup.md`, `API_PlacementGroup.md`, `API_DescribePlacementGroups.md`, `list_ec2.md` (offline, full).

- **Lens B (confused deputy / PassRole):** N/A — no role-ARN-as-input field on any PG/Outpost launch action on these pages.
- **Lens C (credential vending / session scope):** N/A — no STS/session-policy/token-vending surface on these pages.
- **Lens D (data→control-plane escape):** N/A at the doc layer — the Outpost's service-link/control VPC is AWS-managed and not described here; any such escape = HARD STOP territory, not a PG-page lead.
- **Lens F (injection/translation):** N/A — no customer-input→downstream-language transform on this page.
- **Lens G (SSRF / server-side dereference):** N/A — read the full page + the 3-step procedure + `create-placement-group.md`; every link (`order-outpost-capacity`, `launch-instance`, `create-subnet`, `create-placement-group`) is navigation, no field the service fetches/renders.
- **Lens Q (blob/upload parsing):** N/A — no uploaded artifact on these pages.
- **Lens P (gate before privileged change):** partial — the RAM share-accept invitation is a mutual-consent gate; covered under hub Area 2 (sharing lifecycle), not re-owned here.
- **Lens T (secret storage):** N/A — no service-generated secret on these pages.
- **Lens E (RBAC/priv-esc), K, W, BB–FF, etc.:** N/A for this page (named).
- **Lens O (observability/forensics):** Informational — spread-PG capacity errors and launch events are ordinary EC2 management events; co-residency recon (AZ-ID, topology, capacity probing) looks like normal `Describe`/`RunInstances` activity → low detectability, noted as a defender blind spot but not a standalone finding here.

**Firing lenses:** A, V, S, U, AA, L (+ O informational). The headline is Lens A/V (cross-account/cross-org co-residency on physical Outpost hardware) — the surface the hub plan wrongly closed as NULL.
