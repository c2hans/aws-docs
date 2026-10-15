# EC2 Placement **Strategies** — Attack Research Plan (page-level CHILD of the Placement Groups HUB)

Source of leads: `AWSEC2/latest/UserGuide/placement-strategies.html` (the per-strategy deep page:
Cluster / Partition / Spread / Precision-time) + its tightly-coupled sibling
`configure-ec2-ntp.html` (the precision-time / PHC detail page the strategy page links to) +
the IAM Service Authorization Reference `list_ec2.md`. Status: **documentation-derived
hypotheses only; nothing tested against a live account.** Offline mirror == online `.md`
for `placement-strategies.md` (129 lines) and `configure-ec2-ntp.md` verified 2026-10-15.

**Relationship to the hub.** This is a **page-level CHILD / COMPLEMENT** of
`/work/aws-docs/placement-groups-attack-research-plan.md` (the HUB). It does **not** restate
the hub's crown-jewel surface. It **DEFERS**, by explicit cross-reference:
- cross-account co-residency core + topology `nn-` side-channel → **HUB Area 1** (HARD STOP) and the `ec2-instance-topology` plan A6;
- RAM/`PutResourcePolicy` sharing lifecycle, org-leave orphaning, unshare completeness → **HUB Area 2**;
- the unscopable `DescribePlacementGroups` read oracle + "can't view instances you don't own" → **HUB Area 3**;
- the full PG-action IAM condition-key map, "can't mandate a PG", stale strategy enum → **HUB Area 4**;
- the `spread`/`partition` "isolation is availability-not-security" framing correction → **HUB Area 5**;
- predictable PG-name land-grab + name-only-condition footgun → **HUB Area 6**;
- 500-PG quota + `ModifyInstancePlacement` forced-stop sabotage → **HUB Area 7**;
- Outpost placement groups (NULL / single-tenant) → **HUB Area 8**;
- On-Demand Capacity Reservation *inside* a cluster PG → the existing `cr-cpg-attack-research-plan.md`.

It **OWNS** the net-new, strategy-specific surface the hub only summarised: the precision-time
PHC / nanosecond-timestamp capability (**newest, least-reviewed feature — the headline**), the
cluster-PG network-performance differential as a membership/co-residency *inference* oracle, the
cross-VPC/cross-account flat high-bisection segment, the partition-visibility + specific-partition
targeting knobs, the precision-time **parent deletion-lock** cross-reference, and the documented
stop/start **physical-migration** primitive.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- `iam:SimulateCustomPolicy`/`SimulatePrincipalPolicy` is the safe first oracle for any condition-key claim (no resources touched). Several leads here are **guest-side / data-plane** measurements (throughput, PHC reads, packet timestamps) that need a canary instance pair, NOT an API call — note this per lead.
- **HARD STOP (inherited from the hub):** the moment evidence shows cross-**account** physical co-residency *confirmed* (a `nn-` topology node, a PHC/clock correlation, or a throughput/latency signature shared with a foreign account), or any identity/credential/ARN/account belonging to AWS's own service plane / placement engine / Nitro time source, stop, preserve evidence, flag for AWS-Security disclosure. **The precision-time timers in Area 1 are a side-channel *amplifier* for exactly this trigger — treat any cross-tenant use as HARD-STOP territory.**

## 1. Pentest Objectives (strategy-page-specific; co-residency *core* lives in the hub)
1. Determine whether the **nanosecond-resolution PHC clock + hardware packet timestamping** granted by a precision-time PG constitutes a high-resolution timer / shared-clock **side-channel amplifier** that sharpens co-residency detection or microarchitectural timing attacks against a co-resident tenant (feeds HUB Area 1).
2. Use the documented **cluster-PG network-performance differential** (10 Gbps single-flow in-group vs 5 Gbps out) as a **membership / physical-proximity inference oracle** that needs **no `Describe*` permission at all** — a pure data-plane measurement a shared-PG consumer could run against the owner.
3. Characterise the cross-VPC / cross-account **high-bisection "same segment" fabric** a shared cluster PG places instances on: is per-tenant L2/L3 network isolation enforced on that segment, or can co-resident cross-account instances observe each other (ARP/broadcast/multicast/latency)?
4. Abuse the **precision-time parent deletion-lock** (`--parent-group-id`): can a principal pin a *victim's* precision-time PG against deletion by creating a child cluster PG that references it, with no ownership authz on the parent reference (griefing / resource-lock)?
5. Use **partition visibility** ("you can see which instances are in which partitions") + **specific-partition launch** to disclose or co-target the owner's partition placement in a *shared* partition PG (defeat the owner's correlated-failure isolation, or achieve chosen-partition adjacency).
6. Weaponise the documented **stop→start "might migrate them to hardware that has capacity"** behaviour as the physical-relocation "re-roll" step of a co-location loop (chains to HUB Area 1 / `ec2-instance-topology` A6).
7. Probe the **"legacy access"** carve-out where PHC/enhanced-time is reachable **without** a precision-time PG in named regions/families — a documented bypass of the placement-group gate (Lens U/X).

## 2. Components, Assets, and Design (net-new vs hub)

**The four strategies, re-read for the mechanism this page adds over the hub summary:**

- **Cluster** — "a logical grouping of instances within a single Availability Zone. **Instances are not isolated to a single rack.** A cluster placement group **can span peered VPCs** in the same Region. Instances … enjoy a **higher per-flow throughput limit** … placed in the **same high-bisection bandwidth segment** of the network." Enhanced-networking instances get **up to 10 Gbps single-flow in-group vs 5 Gbps out-of-group**. May specify a **`--parent-group-id`** → a precision-time PG. Recommends an On-Demand CR in the PG (→ `cr-cpg`). *Asset: a shared, high-bandwidth, physically-adjacent network segment; a measurable in/out differential; a parent cross-reference.*
- **Partition** — ≤7 partitions/AZ (2 with Dedicated Instances); spans multiple AZs; **"offers visibility into the partitions — you can see which instances are in which partitions"**; can **"launch instances into a specific partition"**; **Capacity Reservations do NOT reserve capacity** here. *Asset: an intra-group placement-disclosure surface + a chosen-partition targeting knob.*
- **Spread** — rack-level (Regions + Outposts) vs host-level (Outposts only); ≤7 running/AZ; not for Dedicated Instances; **CRs do NOT reserve capacity**. *Mostly availability — defers to HUB Area 5.*
- **Precision time** — "places instances on supported hardware with **direct access to high-precision time sources in AWS infrastructure**." Grants: enhanced local NTP (any OS); **PTP Hardware Clock (PHC) device — Linux only**; **hardware packet timestamping for nanosecond-resolution network measurements — Linux only.** Can be a **parent** of a cluster PG; **"you can't delete a precision time placement group that is a parent of a cluster placement group."** *Asset: the newest feature + a nanosecond timer surface.*

**Precision-time mechanism (from `configure-ec2-ntp.md`, net-new depth):**
- PHC is **"part of the AWS Nitro System"**, exposed via the **ENA driver** (`ENA_PHC_INCLUDE=1`, `phc_enable=1`) as a kernel PTP device named **`ena-ptp-<PCI slot>`**, symlinked `/dev/ptp_ena`. The clock is **tied to the ENA ethernet controller PCI slot** (per-NIC), sourcing from the host/infrastructure time source. Resolution observed in docs: **nanosecond** (`+184ns [+198ns] +/- 5032ns`, Stratum 0). `ethtool -T` exposes **`hardware-receive`** packet timestamping.
- **"Legacy access"** carve-out: PHC + enhanced time are reachable **WITHOUT a precision-time PG** in named regions (US-East-1/2, AP-Malaysia/Thailand/Tokyo, EU-Stockholm; NYC Local Zone) for named families (M7a/g/i, R7a/g/i, I8g/ge). ⇒ the "placement group grants access" story has a documented exception.
- Supported families: Gen7+ (M7/C7/R7/… through M9g/C9g/R9g/X8/I8). All AWS Commercial Regions.

**Enforcement reality (net-new).** Everything above is enforced by the **EC2 placement engine +
Nitro (service plane)**. The guest-side capabilities (throughput ceiling, PHC device, packet
timestamps, partition visibility) are **data-plane observables with no IAM grain** — a shared-PG
consumer who holds *zero* `Describe*` permissions can still measure them. That is the core shift
this child plan adds to the hub's IAM-centric analysis.

```
  consumer account B (shared cluster PG)                owner account A
  ┌───────────────────────────┐                        ┌───────────────────────────┐
  │ instance (own)            │  ===10Gbps single-flow==│ instance (own)            │
  │ /dev/ptp_ena  (ns clock)  │   same high-bisection    │ /dev/ptp_ena (same host    │
  │ ethtool -T hw-receive ts  │   "segment", not rack-   │  Nitro time source?)       │
  └───────────────────────────┘   isolated, spans peered└───────────────────────────┘
          │ measure: throughput / RTT / PHC offset / pkt-ts            ▲
          └──── co-residency / proximity INFERENCE (no Describe) ──────┘   HUB Area 1 amplifier
```

## 3. API / Interface Inventory (strategy-specific knobs; full map in HUB §3)

| Interface | Where | New/Existing | Mutating? | Notes (strategy-specific) |
|---|---|---|---|---|
| `CreatePlacementGroup --strategy precision-time` | CLI/API | Existing | Yes | creates the timer-granting PG; returns ARN+name+id |
| `CreatePlacementGroup --strategy cluster --parent-group-id <precision-time-pg>` | CLI/API | Existing | Yes | **parent cross-reference**; parent not a resource row on this action (HUB F3) → **authz-invisible** |
| `RunInstances --placement GroupId=…[,PartitionNumber=N]` | CLI/API | Existing | Yes | launch into a **specific partition** (partition PG); no IAM key for `PartitionNumber` (HUB F2) |
| `DeletePlacementGroup` (precision-time parent) | CLI/API | Existing | Yes | **blocked while it is a parent of a cluster PG** → deletion-lock lead (Area 4) |
| guest `/dev/ptp_ena` / `ethtool -T` / `chronyc` | **data plane** | Existing | No (read) | nanosecond clock + hw packet RX timestamps — **no IAM grain**, Linux only |
| guest TCP single-flow throughput / RTT | **data plane** | Existing | No | 10 vs 5 Gbps differential = membership oracle — **no IAM grain** |
| `DescribePlacementGroups` partition/instance membership | API | Existing | No | partition visibility; scoping deferred to HUB Area 3 |
| `AttachResourcesToPlacementGroup` / `DetachResourcesFromPlacementGroup` | CLI/API | Existing | Yes | **Access level = "Permissions management, Write"** (list_ec2); keys = Name/Strategy only — move an instance in/out of a PG post-launch; adjacency re-roll adjunct to Area 6 |

## 4. Recommended Areas of Focus (net-new only)

Priority order. Each: Background → Security Concern → Test Scenarios → Doc evidence → Severity.

---

### Area 1 — Precision-time PG: nanosecond PHC clock + hardware packet timestamping as a co-residency / timing side-channel **amplifier** (HEADLINE — newest feature, least-reviewed)

**Background.** A precision-time PG grants a Linux guest a **nanosecond-resolution PTP Hardware
Clock** (`/dev/ptp_ena`, part of the Nitro System, sourced from a shared "high-precision time
source in AWS infrastructure") and **hardware packet RX timestamping** (`ethtool -T` →
`hardware-receive`). Historically AWS and other hypervisors have **deliberately coarsened
guest-accessible timers** because high-resolution timers are the enabling primitive for cache /
microarchitectural timing side-channels and for co-residency detection. This feature
re-introduces a precise, hardware-backed clock *and* nanosecond network timestamps to the guest,
and is explicitly recommended to be combined with a **cluster** PG (via `--parent-group-id`),
i.e. with intentional physical packing.

**Security concern.** (a) Does the PHC behave as a **shared-host fingerprint** — do two instances
on the *same physical host* observe a correlated/identical PHC phase, offset, `ena-ptp-<PCI slot>`
identity, or drift signature that an instance on a *different* host does not, giving a
**co-residency confirmation oracle** that needs no `DescribeInstanceTopology` and no `Describe*`
IAM at all? (b) Does nanosecond RX packet timestamping sharpen a **network timing side-channel**
against a co-resident tenant (RTT / inter-packet-gap measurement precise enough to leak a
neighbour's activity), i.e. convert the hub's "co-residency exists" into "co-residency is
*measurable to nanoseconds* and *information-leaking*"? (c) In a cross-account **shared cluster
PG whose parent is a precision-time PG**, both tenants get this timer on physically-adjacent
hardware — the amplifier and the proximity ship together. This is the HUB Area 1 kill-chain with
a far sharper measurement instrument.

**High-level test scenarios.** (Guest-side canary measurements — NOT API calls.)
- Two canary instances **in the same precision-time (or precision-parented cluster) PG**, same account: compare `/dev/ptp_ena` phase/offset, `chronyc sources` PHC0 sample, and `ena-ptp-<PCI slot>` naming; repeat for a pair **forced apart** (spread PG / different AZ). Any pair-distinguishable signature = a co-residency oracle. If a correlation holds **across an account boundary** in a shared cluster PG → **HARD STOP**.
- Measure achievable RX-timestamp resolution / clock-read latency; assess whether it is precise enough to mount a known cache-timing or interrupt-timing side channel against a co-resident VM (characterise the *primitive*, do not exploit a neighbour).
- Confirm whether the PHC/time source is **per-instance virtualised** vs **host-shared read-only** (docs say "direct access to high-precision time sources in AWS infrastructure" + "part of the Nitro System" — ambiguous; the answer decides whether it is a shared resource at all).

**Doc evidence.** `placement-strategies.md` l.112–122 ("direct access to high-precision time
sources," PHC + "hardware packet timestamping for nanosecond-resolution network measurements,
Linux only"); `configure-ec2-ntp.md` ("PHC is part of the AWS Nitro System," `/dev/ptp_ena`,
`ena-ptp-<PCI slot>`, Stratum 0 `+184ns`, `ethtool -T hardware-receive`); cluster `--parent-group-id`
l.27.

**Severity.** Side-channel *primitive* characterisation = Informational→Medium on its own;
**High–Critical and HARD STOP** if it yields a *confirmed cross-account* co-residency signal or a
cross-tenant information leak. Frame carefully: on your **own** instances the timer is a feature
(single-tenant = OOS); the finding is the **cross-tenant observability** it enables.

---

### Area 2 — Cluster-PG network-performance differential (10 Gbps in-group vs 5 Gbps out) = membership / physical-proximity **inference oracle** with no IAM grain

**Background.** The page states, verbatim: *"Instances within a cluster placement group can use
up to 10 Gbps for single-flow traffic. Instances that are not within a cluster placement group can
use up to 5 Gbps for single-flow traffic."* Plus "same high-bisection bandwidth segment" and
"higher per-flow throughput limit." This is a **documented, deterministic, guest-observable**
difference keyed on cluster-PG co-membership / physical proximity.

**Security concern.** Two instances can **determine whether they share a cluster PG / are
physically adjacent purely by measuring achievable single-flow throughput** (and RTT) between
them — **no `DescribePlacementGroups`, no topology API, no IAM permission** required. In a
cross-account **shared** cluster PG, this lets a consumer *confirm* proximity to the owner's
instances (or to a co-consumer's) from the data plane alone, bypassing the hub's "can't view
instances you don't own" (HUB Area 3) and the IAM-scoped topology read — because this signal is
not mediated by any API. It is the cheapest co-residency *inference* in the whole PG surface.

**High-level test scenarios.** (Guest-side; needs ≥2 canary instances.)
- Measure single-flow TCP throughput + RTT between a pair **in the same cluster PG** vs a pair **not** in one (same AZ); confirm the ~10 vs ~5 Gbps step and any latency floor is a reliable binary membership signal.
- In a 2-account shared cluster PG, as consumer B measure flow performance to A-owned endpoints (where reachable via the documented VPC peering) and infer proximity; if it discloses physical adjacency across the account boundary → feed HUB Area 1 (and HARD STOP if it confirms a *specific* co-resident foreign host).

**Doc evidence.** `placement-strategies.md` l.48 (10 vs 5 Gbps), l.19 ("same high-bisection
bandwidth segment," "higher per-flow throughput limit"), `share-placement-group.md` ("use VPC
peering … get the full latency benefits offered by shared cluster placement groups").

**Severity.** Intra-account self-measurement = Informational. **Medium–High** as a *cross-account*
proximity-inference oracle inside a consented share (amplifies HUB Area 1); the no-IAM-grain
property is the reportable structural point.

---

### Area 3 — Cross-VPC / cross-account "same segment" fabric: is per-tenant network isolation enforced on the shared high-bisection segment?

**Background.** Cluster PGs are explicitly **"not isolated to a single rack,"** place instances in
the **"same high-bisection bandwidth segment of the network,"** and **"can span peered VPCs in the
same Region."** The share page adds: *"You can use VPC peering to connect instances owned by
separate AWS accounts and get the full latency benefits offered by shared cluster placement
groups."* So a cross-account shared cluster PG + VPC peering intentionally places **two accounts'
instances on one low-latency, high-bisection segment.**

**Security concern.** On that shared segment, is per-tenant L2/L3 isolation still fully enforced,
or does the "same segment / not rack-isolated / high-bisection" design relax any boundary that is
normally present between unrelated instances? Specifically: can a cross-account co-resident
instance observe the other via **ARP / broadcast / multicast / link-local**, unexpectedly low-level
reachability, or MAC/neighbour visibility that would not exist off the segment? (The hub's Area 1
is about *placement observability*; this is about *network-plane reachability* on the fabric the
packing creates — Lens V network-segmentation, specific to the cluster strategy's "same segment"
wording.)

**High-level test scenarios.** In a 2-account shared cluster PG with peered VPCs, from consumer B's
instance probe the segment for any neighbour-visibility primitive the normal VPC model forbids
(broadcast/multicast delivery, ARP of a non-peered neighbour, link-local reach, promiscuous
capture). Any packet from an A-owned instance that the standard VPC isolation model says is
unreachable = a breach → **HARD STOP** (cross-account), preserve evidence.

**Doc evidence.** `placement-strategies.md` l.19 ("not isolated to a single rack," "same
high-bisection bandwidth segment," "span peered VPCs"); `share-placement-group.md` VPC-peering /
"full latency benefits" sentence.

**Severity.** Cross-account L2/L3 leakage on the shared segment = **High–Critical** if confirmed;
most likely a documented-negative (standard VPC isolation holds regardless of placement) — record
as refuted if so. Needs a 2-account canary.

---

### Area 4 — Precision-time **parent deletion-lock** via `--parent-group-id` (griefing / resource-lock) + unauthz parent cross-reference

**Background.** A cluster PG may name a precision-time PG as **parent** at create
(`--parent-group-id`). The page states, verbatim: *"You can't delete a precision time placement
group that is a parent of a cluster placement group."* The hub (Area 4 / F3) already established
that `CreatePlacementGroup` exposes a **single resource-type row (the created PG)** → the **parent
reference is authz-invisible**: no IAM check on the referenced parent PG.

**Security concern.** This child develops the hub's note into a concrete **lifecycle lock**: if a
principal can create a cluster PG whose `--parent-group-id` points at a precision-time PG **it does
not own** (e.g. one **RAM-shared** to it, or — if the parent reference is validated by neither
ownership nor existence — any guessed/named PG), then creating that child **pins the parent against
deletion** indefinitely. The owner's `DeletePlacementGroup` on the parent fails for a reason the
owner cannot see or control (the locking child is in another account). A **cross-account /
cross-team denial-of-deletion** griefing primitive, and an **AA-style stranded cross-reference**.

**High-level test scenarios.**
- `iam:SimulateCustomPolicy` + API: create a cluster PG with `--parent-group-id` set to a precision-time PG owned by a *different* team/account (first a shared one, then an un-shared/guessed one); confirm (a) whether the parent reference is authz-checked for ownership/existence at all (HUB F3), and (b) whether the parent's `DeletePlacementGroup` is then blocked.
- Confirm the error surfaced to the parent owner on delete — does it name the locking child (info-leak of a foreign resource) or fail opaquely?
- Check whether unsharing/deleting the child cleanly releases the lock (revocation completeness, Lens AA).

**Doc evidence.** `placement-strategies.md` l.27 (`--parent-group-id`), l.128 ("can't delete a
precision time placement group that is a parent of a cluster placement group"); `delete-placement-group.md`
**corroborates verbatim**: "You can't delete a placement group that is a parent of a cluster
placement group. Delete the cluster placement groups first." + "Before you can delete a placement
group, it must contain no instances." HUB Area 4 / F3 (parent reference authz-invisible on
`CreatePlacementGroup`).

**IAM confirmed (list_ec2, subagent-verified 2026-10-15):** there is **NO "parent placement group"
condition key** anywhere in the EC2 reference (`grep -i "parent placement|ParentPlacement"` → 0;
the only `Parent*` keys are `ec2:ParentSnapshot`/`ec2:ParentVolume`, EBS-only). `CreatePlacementGroup`
exposes only `aws:RequestTag`, `aws:TagKeys`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`,
`ec2:Region` on a **single required `placement-group*` resource row (the group being created)** —
**the `--parent-group-id` reference is on no resource row and no condition key**. ⇒ it is
**impossible to write an IAM policy that restricts which parent a principal may attach a child to.**
This upgrades the parent cross-reference from "likely authz-invisible" (hub hypothesis) to
**confirmed IAM-unscopable**; the only open question is runtime behaviour (ownership/existence
validation of the named parent in the control plane).

**Severity.** Cross-account deletion-lock = **Medium–High** (griefing / resource-lock, uneditable
by victim); unauthz parent cross-reference = **confirmed structural gap** (Med); parent-name
info-leak in the delete error = Low–Med. Precondition: whether a non-owned PG can be named as
parent (the open runtime question).

---

### Area 5 — Partition **visibility** + specific-partition **targeting** in a shared partition PG

**Background.** Partition PGs *"offer visibility into the partitions — you can see which instances
are in which partitions,"* intended to be shared with topology-aware apps (HDFS/HBase/Cassandra),
and you can *"launch instances into a specific partition."* There is **no IAM condition key for
partition number** (HUB F2).

**Security concern.** (a) In a **shared** partition PG, does the partition-membership visibility
disclose which partition the **owner's** instances occupy — i.e. placement disclosure across the
account boundary, in tension with the share page's "can't view instances … not owned by you" (HUB
Area 3)? Even the *partition structure / per-partition occupancy counts* leaking is a placement
side-channel. (b) Can a consumer **launch into a specific partition** chosen to **co-locate with**
(or deliberately **collide the hardware isolation of**) the owner's partition — defeating the
owner's correlated-failure isolation guarantee from inside a consented share, with no IAM key able
to restrict which partition a consumer targets?

**High-level test scenarios.** 2-account shared partition PG: as consumer B, enumerate partition
membership/occupancy visible to you and diff for owner-side (A) placement leakage; attempt
`RunInstances … PartitionNumber=N` into a partition occupied by A and observe whether B can
co-target A's partition. Intra-account: confirm no IAM key constrains `PartitionNumber`.

**IAM confirmed (list_ec2, subagent-verified 2026-10-15):** there is **NO partition-number
condition key** — `grep "PlacementGroupPartition|PartitionNumber"` → 0; "partition" exists in the
reference only as one of the three *values* of the `ec2:PlacementGroupStrategy` string key
("cluster, spread, or partition"). `RunInstances` carries `placement-group` as a **NON-required**
resource row (no `*`, unlike `image*`/`instance*`/`subnet*`) with keys `ec2:PlacementGroupName`,
`ec2:PlacementGroupStrategy`, `ec2:Region`, `ec2:ResourceTag`, `ec2:LaunchTemplate`,
`ec2:IsLaunchTemplateResource` — **none expresses *which partition number* the launch targets.**
⇒ an admin can require a specific PG (by name/strategy) but **cannot restrict which partition** a
consumer launches into. Confirmed structural gap, not merely a doc-gap.

**Doc evidence.** `placement-strategies.md` l.68 (partition visibility, "share this information"),
partition-targeting prose; HUB F2 (no partition-number key — now IAM-confirmed above);
`share-placement-group.md` "can't view instances … not owned by you".

**Severity.** Cross-account partition-placement disclosure = **Medium–High** if it leaks owner-side
placement; chosen-partition co-targeting inside a share = Medium (availability/isolation of a
consented party). Defers the generic Describe-oracle scoping to HUB Area 3.

---

### Area 6 — Documented stop→start **physical-migration** primitive as the co-location "re-roll" step

**Background.** The page states that on a capacity error you should *"stop and start all of the
instances in the placement group … Starting the instances might migrate them to hardware that has
capacity"* and that a stopped→started instance "still runs in the placement group." The classic
academic co-residency placement attack relies on repeatedly launching / stop-starting to **re-roll
physical placement** until adjacency to a target is achieved.

**Security concern.** This is an AWS-documented, customer-triggerable **physical remapping** lever.
Combined with HUB Area 1 (observe co-residency via topology/PHC/throughput) + CR influence
(`cr-cpg`), it supplies the **"influence / retry"** step of a guided co-location loop: observe →
re-roll (stop/start all) → re-observe, inside a cluster PG, optionally in a shared cross-account
PG. Not a bug in itself; it is the mobility primitive that makes Area 1/2's observability
*actionable*.

**High-level test scenarios.** In a cluster PG, measure how much stop/start-all changes the
`nn-`/PHC/throughput co-residency signature (does it reliably re-place onto different hardware?);
assess whether iterated re-rolls converge toward a chosen neighbour. Keep strictly within the
attacker's own account unless a *consented* cross-account share exists; **HARD STOP** on any
confirmed foreign-account adjacency.

**Doc evidence.** `placement-strategies.md` cluster rules ("stop and start all … might migrate them
to hardware that has capacity"; stop/start "still runs in the placement group").

**Severity.** Enabler, Informational→Medium standalone; inherits HUB Area 1 severity when chained
(High–Critical cross-account, HARD STOP).

---

### Area 7 — "Legacy access" carve-out: PHC/enhanced-time reachable **without** a precision-time PG (Lens U/X parity gap)

**Background.** `configure-ec2-ntp.md` documents that in **named regions** (US-East-1/2,
AP-Malaysia/Thailand/Tokyo, EU-Stockholm; NYC Local Zone) and for **named families** (M7a/g/i,
R7a/g/i, I8g/ge) the enhanced Amazon Time Sync Service **and the PHC device remain accessible
WITHOUT a precision time placement group** ("legacy access").

**Security concern.** The strategy page frames the precision-time PG as *the* gate to these
capabilities ("Launch your supported instance in a placement group with the `precision-time`
strategy to reach a higher-accuracy NTP source"), but a documented **legacy path grants the same
nanosecond PHC + packet-timestamp primitive with no placement-group membership at all** in those
regions/families. Any Area-1 side-channel reasoning that assumes "precision-time PG membership" as
a precondition (for detection, scoping, or an operator control keyed on the PG) **fails open** on
those instances. This is a Lens U (gate-vs-reality) / Lens X (two paths to one capability, only one
gated) note worth filing against the doc, and it widens the Area-1 blast radius beyond PG members.

**High-level test scenarios.** On a legacy-access region+family instance **not** in any PG, confirm
`/dev/ptp_ena` + `ethtool -T hardware-receive` are present (capability reachable off the PG path);
desk-check that no PG-keyed control/detection would catch its use.

**Doc evidence.** `configure-ec2-ntp.md` "Note … remain accessible without a precision time
placement group in the following regions and for the specific instance families" + the region/family
lists.

**Severity.** Low (doc/clarity + Area-1 scope-widening); AWS-owned doc note.

## 5. Threat Model Test Objectives
| # | Threat / Test Case | Area | Component | Documented mitigation to attack | Status |
|---|---|---|---|---|---|
| S1 | PHC phase/offset/`ena-ptp` identity distinguishes co-resident vs non-co-resident pairs (co-residency oracle) | 1 | `/dev/ptp_ena`, chrony PHC0 | none (guest-side, no IAM grain) | doc-gap — **HARD STOP if cross-account** |
| S2 | ns packet timestamping enables a cross-tenant network/timing side channel | 1 | `ethtool -T hardware-receive` | none | doc-gap |
| S3 | 10-vs-5 Gbps single-flow step = binary cluster-PG membership / proximity signal | 2 | guest TCP throughput | none (no API mediates it) | doc-gap — cross-account amplifier |
| S4 | Cross-account L2/L3 leakage on the shared high-bisection segment | 3 | cluster "same segment" + VPC peering | standard VPC isolation (assumed) | doc-gap — likely refuted; **HARD STOP if confirmed** |
| S5 | `--parent-group-id` pins a foreign/precision-time parent against deletion | 4 | `CreatePlacementGroup` parent ref | single resource-row → parent authz-invisible; **NO parent condition key exists (list_ec2 confirmed)** | **confirmed IAM-unscopable** — griefing lock; runtime-ownership open |
| S6 | Parent-of-cluster delete error leaks the locking child's identity | 4 | `DeletePlacementGroup` on parent | — | doc-gap |
| S7 | Shared partition PG discloses owner-side partition placement | 5 | partition visibility | "can't view instances not owned by you" (HUB Area 3) | doc-gap |
| S8 | Consumer co-targets owner's partition via `PartitionNumber` | 5 | `RunInstances PartitionNumber` | **NO partition-number IAM key (list_ec2 confirmed)**; "partition" is only a strategy *value* | **confirmed structural gap** |
| S9 | Stop/start-all reliably re-rolls physical placement (co-location loop step) | 6 | cluster capacity-retry behaviour | — (documented behaviour) | enabler |
| S10 | Legacy-access path grants PHC/enhanced-time with no PG (gate fail-open) | 7 | `configure-ec2-ntp` legacy carve-out | PG framed as the gate | doc note (Lens U/X) |

## 6. Out-of-Scope Risk Categories (strategy-page-specific)
- **Single-tenant** use of the PHC / enhanced time / 10 Gbps throughput on your **own** instances — a feature, not a finding. Only the **cross-tenant observability** these enable is in scope.
- `spread`/`partition` "physical isolation defeated" treated as a *security* break — it is an **availability** property within your own account (HUB Area 5); only crosses into scope at an account boundary (→ HUB Area 1 / Area 5 here).
- Co-residency, topology `nn-` disclosure, sharing lifecycle, Describe-oracle, name-squat, 500-PG quota, `ModifyInstancePlacement` sabotage, Outpost — **owned by the HUB** (Areas 1/2/3/6/7/8); do not re-derive.
- On-Demand CR inside a cluster PG — owned by `cr-cpg-attack-research-plan.md`.
- The EC2 placement engine's / Nitro time source's internal implementation (service plane) — observe/confirm only; **HARD STOP** on service-plane evidence.
- NTP/PHC guest-OS configuration bugs (chrony, ENA driver) — third-party / guest-OS, OOS.

## 7. Null hypotheses / doc gaps

**Lenses fired (net-new here):** V (network-segmentation / side-channel — Areas 1/2/3, the dominant
lens for this page), A (cross-account disclosure — Areas 2/4/5), AA (parent cross-ref lifecycle lock
— Area 4), U/X (gate-vs-reality legacy carve-out — Area 7; stale strategy enum → HUB Area 4), L
(stop/start re-roll enabler — Area 6).

**Explicit NULL hypotheses (pages named per skill discipline):**
- **Lens G (SSRF):** N/A — no URL/endpoint/callback the service dereferences on `placement-strategies.md` or `configure-ec2-ntp.md`. (The link-local `169.254.169.123`/`fd00:ec2::123` NTP endpoints are **guest-dialed outbound to a fixed AWS address**, not a customer-supplied fetch target — not an SSRF seam. Note the 1024 PPS link-local aggregate cap as an availability aside only.)
- **Lens Q (upload/blob):** N/A — no file/blob/image surface.
- **Lens F (translation/injection):** N/A — no parser/translation layer; `--parent-group-id`/`PartitionNumber` are typed IDs/ints.
- **Lens B/C (PassRole / credential-vending):** N/A — no role-ARN input, no STS/session seam on these knobs.
- **Lens K (prompt/LLM), W (attestation/enclave), FF (JWT), BB/CC/DD (edge/parser/cache/upstream-context):** N/A — no LLM, no PCR/enclave gate, no bearer-JWT, no multi-parser edge path on this page.
- **Lens R (sample-policy audit):** N/A on this page — `placement-strategies.md` prints no IAM JSON (the share-page "Required permissions" two-action list is a HUB Area 2 item).

**Top open doc-gaps carried for the hunter (priority order):**
1. **(Area 1, HARD STOP-adjacent)** Is the precision-time PHC a **host-shared** clock whose phase/offset/identity correlates across co-resident instances (→ a no-IAM co-residency oracle), and is its ns resolution a usable cross-tenant timing side-channel? Needs a canary pair ± co-residency.
2. **(Area 2)** Is the 10-vs-5 Gbps single-flow step a **reliable binary** cluster-PG-membership / proximity signal measurable cross-account in a shared PG? Needs ≥2 canary instances.
3. **(Area 4)** IAM-unscopability of `--parent-group-id` is now **settled** (no parent condition key exists). Remaining runtime question: can it name a **non-owned** precision-time PG (shared or guessed), and does that **block the parent's deletion** (cross-account resource-lock)? Does the delete error leak the child?
4. **(Area 5)** IAM-unscopability of partition targeting is now **settled** (no partition-number key exists). Remaining runtime question: does a **shared** partition PG disclose the **owner's** partition placement to a consumer, and can a consumer **co-target** the owner's partition via `PartitionNumber`?
5. **(Area 3)** Does the cluster "same high-bisection segment" + VPC peering relax any cross-account L2/L3 isolation? (Expect refuted; confirm.)
6. **(Area 7)** Does the legacy-access path grant PHC/enhanced-time with **no PG**, fail-opening any PG-keyed control/detection in those regions/families?

**Corpus facts confirmed this pass (list_ec2, subagent-verified 2026-10-15; supersede any earlier
WebFetch paraphrase):** `ec2:PlacementGroupName` (String), `ec2:PlacementGroupStrategy` (String,
values cluster/spread/partition), `ec2:PlacementGroup` (**ARN**, filters by the PG an instance/CR
belongs to — carried by `ModifyInstancePlacement` instance-row / `CreateCapacityReservation` /
`ModifyInstanceNetworkPerformanceOptions`) all EXIST. **No parent-PG key, no partition-number key**
exist. `DeletePlacementGroup`/`ModifyInstancePlacement` DO carry condition keys + resource rows
(an earlier WebFetch paraphrase wrongly said they had none — discarded). `placement-groups-limitations-general.html`,
`describe-instance-placement.html` **do not exist** (302→index); their content lives in
`placement-groups.html` and `change-instance-placement-group.html` respectively. 500-PG/Region cap.
`change-instance-placement-group.md`: instance must be `stopped` to change its PG.

**Confirmed negative / framing results (do not re-chase):** `spread`/`partition` "isolation" is
availability-not-tenant-security within one account (HUB Area 5); the NTP link-local endpoints are
not an SSRF seam (fixed outbound AWS address); single-tenant timer/throughput use is OOS. All
cross-account paths in this plan inherit the hub's precondition that the **owner must have
initiated a RAM/CR share first** — these are *consented-neighbour* amplifiers, not arbitrary-victim
reaches.
