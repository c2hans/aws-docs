# ENA Express "Review settings" (list/view) page — Attack & Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express-list-view.html
("Review ENA Express settings for your EC2 instance")
**Offline mirror:** `./aws-docs/.../ena-express-list-view.md`
**Service:** Amazon EC2 — Enhanced networking / ENA Express (AWS Scalable Reliable Datagram, SRD)
**Date:** 2026-10-15
**Method:** `security-questionbuilder` (boundary-first threat modeling, Lens catalog A–FF)

---

## §0 How to use this plan (orientation for the next agent)

This page is a **thin, read-only "view your settings" page**. Its entire documented purpose is
to show a reader the `Attachment.EnaSrdSpecification` state of a network interface via three read
paths (Console, AWS CLI, PowerShell). It defines **no new write API** and **no new data-plane
mechanism**. Everything genuinely *new* that this page contributes to the attack surface is on the
**read / view / disclosure** axis — so **that is the niche this plan owns**, and it deliberately
does **not** re-litigate what the siblings already own.

**Sibling-plan ownership map — read this before adding anything here (avoid duplication):**

| Surface | Owning plan | What it owns |
|---|---|---|
| `EnaSrdSpecification` **write-side** scoping; 0-hit `EnaSrd` condition-key grep; `ec2:Attribute/${AttributeName}` case-sensitivity fail-open class; console-hidden/API-only modify knob | `modify-network-interface-attributes-attack-research-plan.md` **§5.7** | Full write-side analysis |
| SRD multipath vs flow-log / traffic-mirror silence; metrics oracle; **ENA Express `EnaSrdSpecification` unscopable 3-path parity (Area 1)**; cross-account "or in different accounts" doc-contradiction (Objective 2) | `enhanced-networking-ena-attack-research-plan.md` **Area 1 / 3 / 7, Obj 2** | Hub-level ENA/SRD analysis + the `.cache/ena-express-findings.md` scratch file (5 leads, 4 facts) |
| EFA/SRD OS-bypass **cross-tenant frame-injection mechanism** (the *actual* fabric-reach consequence) | `ec2-networking-attack-research-plan.md` (hub) **Lead #3** | Cross-tenant SRD/RDMA fabric reach (hard-stop territory) |
| Unscoped `DescribeNetworkInterfaces` / `...Permissions` as account-wide topology + grant-list oracle | `using-eni-attack-research-plan.md` **Lead 5** | General unscoped-Describe oracle |
| ENI attachment lifecycle (EnaSrdSpecification lost on detach/terminate) | `network-interface-attachments-attack-research-plan.md` | Attachment lifecycle |
| `Requester ID` requester-managed trust-signal field (distinct from `OwnerId`/`InstanceOwnerId`) | `requester-managed-eni-attack-research-plan.md` **Area 4 / Lead 6** | Creator-identity for AWS-service ENIs |

**What THIS plan owns (net-new niche):**
1. The ENA Express **read page as an unscopable, account-wide SRD-posture recon oracle** — who has/hasn't SRD and SRD-UDP enabled — and the fact that *no* IAM condition key narrows *which* ENIs/instances a describe-only caller may read (Lead R1).
2. **`OwnerId` / `InstanceOwnerId` disclosure** — the same read that leaks SRD posture always leaks the owning account ID in the same response object; net-new, not covered by any sibling (Lead R2).
3. **Three-read-path parity + the legacy fourth path** — `describe-instances`, `describe-network-interfaces`, `Get-EC2NetworkInterface`, and the legacy `DescribeNetworkInterfaceAttribute` — all identically unscoped (Lens X non-finding, stated for completeness) (Lead R3).
4. **Kill-chain stage-1 framing** — this read page is the reconnaissance that *feeds* the sibling-owned config (modify §5.7) and data-plane (enhanced-networking-ena / hub #3) leads. It is the "which targets are worth attacking" selector.
5. A small set of **data-plane doc-gaps surfaced while reading the companion pages** (SRD cross-AZ fabric enforcement, UDP/MTU gap, noisy-neighbor DoS, peer-detection) — recorded here with explicit pointers to the owning plans, **not** claimed as this page's own (Leads D-A … D-D).

**Confirmation posture:** documentation-only here. The safe scopability oracle is
`iam:SimulateCustomPolicy` (shows whether a condition key is even *evaluated*). `DryRunOperation`
is caller-IAM-only — **not** an ownership oracle. **HARD STOP:** anything that would require
observing Nitro-card-to-Nitro-card SRD signaling or the shared inter-AZ fabric is **AWS's own
service plane** — preserve evidence, flag for disclosure, do not test.

---

## §1 Components, Assets, and Design

**Customer-facing interface (this page):** three read methods against one data structure.
- **Console:** instance / network-interface detail → "ENA Express" field.
- **AWS CLI:** `aws ec2 describe-instances` and `aws ec2 describe-network-interfaces` → `Attachment.EnaSrdSpecification`.
- **PowerShell:** `Get-EC2NetworkInterface` → `.Attachment.EnaSrdSpecification`, and the documented
  example output also prints `OwnerId: 111122223333` and `InstanceOwnerId: 111122223333`.

**The data structure being read:**
```
Attachment.EnaSrdSpecification = {
    EnaSrdEnabled: bool,
    EnaSrdUdpSpecification: { EnaSrdUdpEnabled: bool }
}
```
`EnaSrdSpecification` is a property of a **network-interface attachment** (not the ENI itself) —
it is lost on detach/terminate (see `network-interface-attachments` plan).

**Processes / fleets behind it:** the SRD transport is implemented in **Nitro hardware** (the guest
driver only *reads back* `ena_srd_mode` / `ena_srd_*_pkts` counters; it does not implement SRD).
This is the service-plane hard stop.

**Accounts / VPCs:** normal case = caller's own account. The disclosure question (Lead R2) is
whether a describe call can ever return an `OwnerId`/`InstanceOwnerId` **different** from the
caller's account (shared-VPC / Outposts / cross-account-attach), turning the oracle into an
external-account enumeration primitive.

**Resource & identifier shape:** ENI IDs (`eni-…`), instance IDs (`i-…`), account IDs
(12-digit). SRD posture is a boolean pair per attachment.

**Identity:** SigV4 IAM. Relevant actions: `ec2:DescribeInstances`,
`ec2:DescribeNetworkInterfaces`, `ec2:DescribeNetworkInterfaceAttribute` (read);
`ec2:ModifyNetworkInterfaceAttribute`, `ec2:AttachNetworkInterface`, `ec2:RunInstances`,
`ec2:CreateNetworkInterface` (write — deferred to siblings).

**Where untrusted data enters:** nowhere on this page — it is a pure read page. No server-side
fetch, no upload, no parser. (Lenses G/Q/K/F declared N/A below with pages checked.)

---

## §2 Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv describe-only principal (Team A) | SRD posture of **every** ENI/instance in the account (Team B, C, …) | `ec2:DescribeNetworkInterfaces` / `DescribeInstances` with no scopable resource row | Reading `EnaSrdSpecification` of an ENI the caller has no tag/ownership relationship to = unscopable account-wide recon oracle |
| Describe-only principal | Owning account ID of an interface | `OwnerId` / `InstanceOwnerId` in the same response | A response returning an `OwnerId` ≠ caller's account = cross-account account-ID enumeration |
| Reader of SRD posture | Sibling-owned write path (modify §5.7) | posture read → pick a target → flip `EnaSrdEnabled` | Recon → config-change is a kill chain; this page is stage 1 only |
| Any customer surface | Nitro SRD fabric / inter-AZ shared paths | SRD multipath transport | **HARD STOP** — any observation of Nitro-to-Nitro signaling or another tenant's in-flight SRD packet is a service-plane breach; preserve + flag |

---

## §3 API / interface surface

| Name | Mutating? | Facing | Returns `EnaSrdSpecification`? | Authorized callers | Scopable? | Notes |
|---|---|---|---|---|---|---|
| `ec2:DescribeInstances` | No | External | Yes (`.Reservations[].Instances[].NetworkInterfaces[].Attachment.EnaSrdSpecification`) | any principal w/ the action | **No** — resource row blank, `ec2:Region` only (L6996–7000) | account-wide read oracle |
| `ec2:DescribeNetworkInterfaces` | No | External | Yes (`.NetworkInterfaces[].Attachment.EnaSrdSpecification`) | any principal w/ the action | **No** — resource row blank, `ec2:Region` only (L2162–2166 / L7218–7222) | account-wide read oracle; also leaks `OwnerId`/`InstanceOwnerId` |
| `ec2:DescribeNetworkInterfaceAttribute` (legacy) | No | External | **Doc-gap** — does `--attribute attachment` surface SRD? not stated | any principal w/ the action | **No** — resource row blank, `ec2:Region` only (L2150–2154 / L7206–7210) | redundant oracle *if* it exposes the field; dead end if not |
| PowerShell `Get-EC2NetworkInterface` | No | External | Yes | wraps `DescribeNetworkInterfaces` | same as above | documented example prints `OwnerId`/`InstanceOwnerId` |

No `[NEW]` write API on this page. No non-SDK/console-hidden knob on the **read** path (the hidden
knobs live on the write path — owned by modify §5.7 / create-network-interface).

---

## §4 Boundary-lens findings

### Lead R1 — Unscopable, account-wide SRD-posture recon oracle (Lens A read-oracle / Lens S)  — **PRIMARY, net-new**
**Claim:** Any principal holding `ec2:DescribeNetworkInterfaces` or `ec2:DescribeInstances` can read
the `EnaSrdEnabled` / `EnaSrdUdpEnabled` posture of **every** ENI/instance in the account; there is
**no IAM condition key** to restrict *which* interfaces/instances a caller may describe.
**Mechanism (exact rows in `list_ec2.md`):**
- `DescribeNetworkInterfaces` — resource-table L2162–2166 (blank Condition key / value); action-list L7218–7222: `Resource types (*required):` **blank**, `Condition keys: [ec2:Region]` only.
- `DescribeInstances` — L6996–7000: resource row **blank**, `Condition keys: [ec2:Region]` only.
- `DescribeNetworkInterfaceAttribute` — L2150–2154 / L7206–7210: same shape, `ec2:Region` only.
- **Root cause (confirmed):** `grep -i "enasrd|ena-srd|ena_srd" list_ec2.md` → **0 hits**. No `ec2:EnaSrd*`
  condition key exists anywhere in the EC2 IAM reference — on read **or** write. SRD state is not an IAM-evaluable dimension.
**Confirm/Refute oracle:** `iam:SimulateCustomPolicy` with a `Deny` scoped by `aws:ResourceTag` /
`ec2:ResourceTag` / ARN on `DescribeNetworkInterfaces` — the condition is **never evaluated** (no
resource-type row to attach it to), so the simulate returns `allowed`. Live-safe: a role granted
only `ec2:DescribeNetworkInterfaces` (no tag/ARN condition possible) reads `Attachment.EnaSrdSpecification`
for an ENI it has no ownership/tag relationship to.
**Framing — intra-account cross-team recon:** SRD/UDP enablement is a performance/cost/throughput
signal (and in some fleets a security-posture signal — SRD changes the L4 transport path). A
low-privileged read-only role in one team enumerates every other team's SRD rollout state
account-wide, with no lever for a security admin to narrow it.
**Relationship to siblings:** this is the **ENA-SRD-specific instantiation** of
`using-eni-attack-research-plan.md` **Lead 5** (general unscoped-Describe oracle) — file it as a
sub-bullet of that lead's evidence set, scoped to the `EnaSrdSpecification` field, and note it
**extends** that lead to `DescribeInstances` and the legacy `DescribeNetworkInterfaceAttribute`,
which that plan does not analyze.
**Severity:** Medium (structural EC2 Describe-family least-privilege gap; `Resource:"*"` is the only
shape IAM supports here — does **not** cross the account boundary unless Lead R2 confirms cross-account `OwnerId`).

### Lead R2 — `OwnerId` / `InstanceOwnerId` disclosure riding the same read (Lens U / Lens A)  — **net-new**
**Claim:** The read that leaks SRD posture **always** leaks the owning account ID of the
ENI/instance in the same response object.
**Mechanism:** the page's own PowerShell example prints `OwnerId: 111122223333` and
`InstanceOwnerId: 111122223333`; the same `OwnerId` field is present in `describe-network-interfaces`
JSON generally (standard EC2 schema). Live-fetch of the page 2026-10-15 confirms **no drift** — both
fields still in the example.
**Cross-ref (confirmed net-new):** checked `requester-managed-eni`, `using-eni`,
`network-interface-attachments` plans — none analyze `OwnerId`/`InstanceOwnerId` as a disclosure
field. `requester-managed-eni` analyzes the **different** `Requester ID` field (creator identity for
AWS-service-planted ENIs), not `OwnerId`/`InstanceOwnerId` (the account that *owns* the resource).
**Open question (doc-gap — the escalation hinge):** can a describe on a **requester-managed** or
shared / cross-account-attached ENI return an `OwnerId`/`InstanceOwnerId` **different** from the
caller's account (VPC-sharing / Outposts / cross-account attach)? The IAM reference does not speak to
response semantics — settle live. **If yes**, Lead R1 becomes a (still Region-scoped-only)
**cross-account account-ID enumeration** primitive: a describe-only caller maps which external
accounts own interfaces attached in a shared VPC alongside their SRD posture.
**Severity:** Low standalone (account IDs are low-sensitivity); **raises Lead R1 to Medium-High** if
the cross-account `OwnerId` return is confirmed.

### Lead R3 — Three-read-path parity + legacy fourth path (Lens X — parity *non-finding*, for completeness)
**Claim:** `DescribeInstances`, `DescribeNetworkInterfaces`, and the legacy
`DescribeNetworkInterfaceAttribute` scope **identically** (Region-only, no resource type) — there is
no stricter-vs-looser validator twin to exploit here.
**Mechanism:** line citations in Lead R1; all show `Condition keys: [ec2:Region]`, resource row blank.
**Residual doc-gap:** whether `DescribeNetworkInterfaceAttribute --attribute attachment` actually
surfaces `EnaSrdSpecification` as a queryable attribute is **not stated** in the IAM reference (it
governs authorization, not response shape) and is not verifiable offline. Confirm live with
`aws ec2 describe-network-interface-attribute --attribute attachment` against a canary SRD-enabled ENI.
- If it does **not** expose SRD → the legacy path is a dead end for the recon oracle (narrows R1).
- If it does → an additional unscoped path, identical shape — redundant oracle, no new severity.
**Severity:** Informational (parity confirmed) / Low if the legacy path also exposes the field.

### Lead C1 — Write-side scopability (deferred, with one net-new doc-gap) (Lens S / Lens R)
**Claim:** None of `ModifyNetworkInterfaceAttribute`, `AttachNetworkInterface`, `RunInstances`,
`CreateNetworkInterface` carry an `ec2:EnaSrd*` key; the only generic lever is
`ec2:Attribute` / `ec2:Attribute/${AttributeName}` on `ModifyNetworkInterfaceAttribute`'s
`network-interface*` row (L8969) — the `instance*` row (L8968) does **not** carry it; the other
three actions carry **no** `ec2:Attribute` key at all (`AttachNetworkInterface` L4858–4862,
`RunInstances` L9585–9594+, `CreateNetworkInterface` L5357–5362).
**Defers to:** `modify-network-interface-attributes-attack-research-plan.md` **§5.7** (full write-side
analysis: 0-hit `EnaSrd` grep, `ec2:Attribute/${AttributeName}` case-sensitivity fail-open class,
cross-tenant mechanism deferred to the hub).
**Net-new doc-gap this plan contributes (flag, do not close):** is `EnaSrdSpecification` (or
`ena-srd-specification`) even a value that `ec2:Attribute/${AttributeName}` recognizes? The IAM
reference's `ec2:Attribute` row (~L10051) only links to
`iam-policies-for-amazon-ec2.html#attribute-key` for the enumerated `AttributeName` values — and
that enumeration is **not present** in the offline `list_ec2.md` mirror, so it cannot be
grep-confirmed whether `EnaSrdSpecification` is in the documented allowed-value set at all, or whether
(being a newer non-SDK-era network-interface param alongside `AssociatePublicIpAddress` /
`EnablePrimaryIpv6` / `AssociatedSubnetId.N`) it was simply never added. **If it is absent from the
enum, the lever doesn't merely fail-open on casing — it does not exist for this attribute at all**,
and a policy author cannot even *attempt* to scope it. **Confirm:** write a Deny on
`ec2:Attribute/${AttributeName} = EnaSrdSpecification` (+ lower/camelCase variants) and
`iam:SimulateCustomPolicy` against a `ModifyNetworkInterfaceAttribute` call setting
`EnaSrdSpecification`. **Severity:** Medium control-gap (Tier-2, inherited from the sibling plan).

### Data-plane leads surfaced while reading companion pages (owned elsewhere — pointers only)

These came out of reading `ena-express.md`, `efa.md`, `monitoring-network-performance-ena.md`,
`network_mtu.md` in full. They are **not** this read-page's own surface — recorded here with
explicit ownership pointers so the next agent sees them in one place.

- **Lead D-A — SRD cross-AZ shared-fabric, enforcement layer never named (Lens V/D).** `ena-express.md`
  states SRD deliberately crosses AZs within a Region ("distributes packets … across different AWS
  network paths") — the *opposite* of EFA's explicit "can't cross AZs or VPCs, not routable" posture
  (`efa.md`) — yet **no page names the mechanism confining one tenant's multipath flow from
  another's** on that shared fabric. The sibling ENA page (`enhanced-networking-ena.md`) has **zero**
  mentions of "security group / isolat* / tenant / cross-account". **HARD STOP** — only resolvable by
  observing Nitro-to-Nitro traffic = service plane. File as **doc-gap, surface unconfirmed**.
  → **Owned by** `ec2-networking-attack-research-plan.md` **hub Lead #3** (extend it from EFA's RDMA
  device to the SRD inter-AZ fabric specifically) and `enhanced-networking-ena` Area 3.
- **Lead D-B — UDP has no automatic MTU accommodation for SRD headers; TCP does (Lens F).**
  `ena-express.md`: TCP auto-clamps MSS, "**UDP traffic still requires a lower MTU**." No page
  (`network_mtu.md` grepped — 0 SRD mentions) states the SRD header byte-overhead or what happens to
  an oversized UDP datagram once SRD silently activates (fragment? drop? per-packet demote?).
  **Reachable without Nitro access** — two cooperating ENA-Express instances, send UDP at the
  1500/9001 boundary, watch `ena_srd_tx_pkts` vs `ena_srd_eligible_tx_pkts` + packet capture.
  Severity Low/Medium (availability/correctness, not confidentiality). → **Owned by**
  `enhanced-networking-ena` (new sub-lead; it owns the SRD data-plane surface).
- **Lead D-C — `ena_srd_resource_utilization` is a shared per-instance budget: same-tenant / SG-peer
  noisy-neighbor DoS (Lens L).** `monitoring-network-performance-ena.md`: utilization is "the number
  of concurrent SRD connections a single instance can hold … As utilization approaches 100% … ENA
  Express falls back from SRD to standard ENA … possibility of dropped packets increases." A second
  SG-permitted peer opening many SRD-eligible flows degrades the victim's **unrelated** flows.
  **Reachable without Nitro access** (reachability-only test, no cross-tenant primitive). Severity
  Medium (documented availability primitive; silent degradation surfaced only via the metric).
  → **Owned by** `enhanced-networking-ena` / `fleet-quotas`-style resilience framing.
- **Lead D-D — SRD peer "detection" is undocumented, below the guest driver (Lens U).** `ena-express.md`
  says SRD "detects if ENA Express is operating on both" ends — mechanism never expanded, distinct
  from the `EnaSrdSpecification` control-plane bit, runs on the Nitro card. **HARD STOP**; and since
  `EnaSrdSpecification` is already proven self-scoped (one party can't set the peer's flag), there is
  **no guest-reachable spoof primitive** even in principle. Near-null; record as doc-completeness note.
  → **Owned by** hub Lead #3 / `enhanced-networking-ena` Obj 2.
- **Complement to the flow-log blind spot (Lens O):** the metrics that are a victim's *only* way to
  detect its own silent SRD fallback require **driver ≥ 2.8** (`ena-express.md`). An instance on an
  older driver has **no first-party visibility** into whether it has silently fallen back — a narrower
  **self-observability** gap distinct from the third-party IDS/flow-log blind spot. → **Owned by**
  `enhanced-networking-ena` Area 7 (metrics oracle), as a complement to its Lead 2.

---

## §5 Kill-chain framing — where this page sits

```
  [STAGE 1 — THIS PLAN]                    [STAGE 2 — modify §5.7]        [STAGE 3 — hub #3 / enhanced-networking-ena]
  Unscopable account-wide read     ──►     Flip EnaSrdEnabled on     ──►  SRD transport change / fabric reach
  (R1): enumerate every ENI's              a chosen target ENI             (HARD STOP — service plane)
  SRD/UDP posture + OwnerId (R2)           (write-side, unscopable)
  → pick the highest-value target
```
This page is the **reconnaissance selector**: it tells an attacker *which* interfaces are worth the
stage-2 config change and the stage-3 data-plane work. On its own it is Medium (least-privilege
recon). Its value is as the enumeration front-end to the sibling-owned write and data-plane leads.

---

## §6 Prioritized leads

| # | Lead | Lens | Severity | Confirm cost | Owner |
|---|---|---|---|---|---|
| R1 | Unscopable account-wide SRD-posture recon oracle | A/S | Medium (→Med-High w/ R2) | Low (SimulateCustomPolicy) | **this plan** (sub-bullet of using-eni Lead 5) |
| R2 | `OwnerId`/`InstanceOwnerId` disclosure; cross-account? | U/A | Low → Med-High if cross-acct | Low (one describe) | **this plan** |
| C1 | `ec2:Attribute/${AttributeName}` may not list `EnaSrdSpecification` at all | S/R | Medium | Low (SimulateCustomPolicy) | modify §5.7 (+ this doc-gap) |
| R3 | Legacy `DescribeNetworkInterfaceAttribute` surfaces SRD? | X | Info/Low | Low (one CLI call) | **this plan** |
| D-C | `ena_srd_resource_utilization` noisy-neighbor DoS | L | Medium | Med (2 instances) | enhanced-networking-ena |
| D-B | UDP/SRD-header MTU gap | F | Low/Med | Med (2 instances) | enhanced-networking-ena |
| D-A | SRD cross-AZ fabric enforcement unnamed | V/D | Info (Crit if ever shown live) | **HARD STOP** | hub #3 |
| D-D | SRD peer-detection unauthenticated-looking | U | Info (near-null) | **HARD STOP** | hub #3 |

---

## §7 Confirmation playbook (safe, documentation-authorized next steps)

1. **R1 (scopability):** `iam:SimulateCustomPolicy` — Deny `DescribeNetworkInterfaces` on
   `aws:ResourceTag`/ARN; expect `allowed` (condition not evaluated). Then a describe-only role reads
   an unrelated ENI's `EnaSrdSpecification`.
2. **R2 (disclosure):** one `describe-network-interfaces` on a shared-VPC / requester-managed ENI;
   inspect whether `OwnerId`/`InstanceOwnerId` ≠ caller's account.
3. **R3 (legacy path):** `aws ec2 describe-network-interface-attribute --attribute attachment` on a
   canary SRD-enabled ENI; does the response carry `EnaSrdSpecification`?
4. **C1 (attribute-name enum):** `iam:SimulateCustomPolicy` with Deny on
   `ec2:Attribute/${AttributeName}=EnaSrdSpecification` (+ case variants) against a
   `ModifyNetworkInterfaceAttribute` setting it; confirm whether the key engages at all.
5. **D-B / D-C (data-plane, non-hard-stop):** two cooperating ENA-Express instances with synthetic
   canary traffic; `ethtool -S | grep ena_srd` + packet capture. **Stop immediately** if any
   observation would require Nitro-internal visibility.

**Do NOT** attempt D-A / D-D confirmation — they require service-plane (Nitro/fabric) observation.

---

## §8 Null hypotheses (pages checked)

- **Lens B/C (PassRole / credential vending):** N/A — read `ena-express-list-view.md`,
  `ena-express-configure.md`; no role-ARN or credential-vending field on this surface.
- **Lens G (SSRF / server-side deref):** N/A — read `ena-express-list-view.md`,
  `ena-express.md`, `ena-express-configure.md`; no field the service fetches/renders. Pure read page.
- **Lens Q (upload/parse):** N/A — no blob/attachment field on any ENA Express page checked.
- **Lens K (injection):** N/A — read page, no server-side interpreter.
- **Lens F (translation/wire):** fires only on the SRD *data plane* (Lead D-B), not this read page.
- **Lens E (RBAC priv-esc):** N/A on the read page; write-side owned by modify §5.7.
- **Lens S "wrong-resource-bound / silently-overridden-sibling":** N/A for the Describe actions (no
  resource row to misbind); applies only write-side (owned by sibling).
- **Lens U (guarantee vs enforcement):** fires as D-A/D-D (data-plane fabric), owned by hub/ENA plans.

---

## Appendix — evidence anchors
- `list_ec2.md`: DescribeNetworkInterfaces L2162–2166 / L7218–7222; DescribeInstances L6996–7000;
  DescribeNetworkInterfaceAttribute L2150–2154 / L7206–7210; ModifyNetworkInterfaceAttribute
  network-interface* row L8969 (instance* row L8968 lacks `ec2:Attribute`); AttachNetworkInterface
  L4858–4862; RunInstances L9585–9594+; CreateNetworkInterface L5357–5362; `ec2:Attribute` row ~L10051.
- `grep -i "enasrd|ena-srd|ena_srd" list_ec2.md` → 0 hits (no SRD condition key, read or write).
- Target page live-fetched 2026-10-15: **no drift** vs offline mirror; PowerShell example still prints
  `OwnerId: 111122223333` / `InstanceOwnerId: 111122223333`.
- Companion pages read in full: `ena-express.md`, `efa.md`, `monitoring-network-performance-ena.md`,
  `network_mtu.md` (last grepped 0 SRD mentions).
