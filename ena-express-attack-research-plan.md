# EC2 ENA Express (AWS SRD) — Attack / Research Plan

> **Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express.html
> (+ siblings `ena-express-configure.html`, `ena-express-list-view.html`,
> `monitoring-network-performance-ena.html`).
> **Method:** `security-questionbuilder` skill — boundary-first. Documentation-only; no live
> testing was performed. Online (`.html`→`.md`) and offline mirror
> (`/work/aws-docs/docs/AWSEC2/latest/UserGuide/`) were diffed and are **verbatim-identical**
> on all security-relevant content.
> **Prepared:** 2026-10-15.

---

## 0 — How to use this plan

ENA Express is a **transport-layer accelerator**, not an access-control feature. It toggles
whether a network interface's eligible TCP/UDP flows ride AWS's **Scalable Reliable Datagram
(SRD)** multipath transport (packet fan-out across AWS network paths + receiver-side reordering
+ SRD-level retransmit; single-flow bandwidth 5→25 Gbps) instead of standard ENA. Both the
sender and receiver must independently opt in, in the same Region; on any mismatch it silently
falls back to standard ENA. Nothing about it changes security-group, NACL, VPC, subnet, or
routing enforcement, and the docs never claim it does.

Because of that, **the highest-value findings here are not cross-tenant breaks** — the honest
null hypothesis (Area 8) is that ENA Express grants no reach a caller didn't already have. The
real surface is three narrower things, each confirmed from docs:

1. **An IAM policy-authoring gap** (Area 5.1) — the one lead a defender can act on today.
2. **Observability / detection-posture gaps** (Area 5.2) — what Flow Logs / Traffic Mirroring
   *cannot* see once SRD is on, and a documented live-migration side-channel counter.
3. **A download-and-run-as-root AWS-authored helper script** (Area 5.3) — low severity, but a
   real supply-chain artifact AWS ships in the prose.

A hunter should read Areas 2–4 to load the mechanism, then execute Area 6's test objectives in
priority order. Several leads are **owned by sibling plans** and only cross-referenced here (see
the non-duplication note below) — do not re-derive them.

**Non-duplication / ownership map (read before starting):**

| Fact / lead | Owner plan | This plan |
|---|---|---|
| `EnaSrdSpecification` as a post-hoc `ModifyNetworkInterfaceAttribute` knob; generic `ec2:Attribute`/`ec2:Attribute/${AttributeName}` name-vs-value distinction; attachment-scoped silent-revoke lifecycle | `modify-network-interface-attributes-attack-research-plan.md` §5.7 | cross-ref only |
| EFA (Elastic Fabric Adapter) OS-bypass RDMA cross-tenant frame-injection — **also "SRD"-branded but a distinct device, driver, and trust model** | `ec2-networking-attack-research-plan.md` Lead [3] / Cluster 3 | explicitly distinguished, Area 7 |
| Generic ENI create/attach/detach/modify/reset mechanics not specific to EnaSrd | `using-eni-*`, `create-network-interface-*`, `modify-network-interface-attributes-*` | cross-ref only |
| `ena_srd_eligible_tx_pkts` vs `ena_srd_tx_pkts` divergence as a live-migration side-channel | `.cache/ena-driver-monitoring-findings.md` (O/L-4) | re-stated as 5.2-B2 because it is ENA-Express-specific and load-bearing here |

**This plan OWNS:** the ENA Express feature as a whole; the three-write-path IAM condition-key
parity gap (Attach / RunInstances / Modify); both-ends-opt-in fallback semantics as a
non-primitive; the SRD observability blind spot vs Flow Logs / Traffic Mirroring; the
`check-ena-express-settings.sh` supply-chain surface; and the consolidated null hypotheses.

---

## 1 — Pentest objectives

1. **Prove or refute the IAM parity gap:** can a principal enable SRD on an attachment via a
   write path (`AttachNetworkInterface` / `RunInstances`) that an attribute-name Deny on
   `ModifyNetworkInterfaceAttribute` was supposed to prevent? (Area 5.1 — the actionable one.)
2. **Characterize the detection blind spot:** confirm whether VPC Flow Logs and Traffic
   Mirroring can observe SRD multipath/reorder/retransmit, or whether they only ever see the
   reassembled logical flow. (Area 5.2-B1.)
3. **Characterize the live-migration side channel:** confirm whether the eligible-vs-actual TX
   counter divergence is a reliable guest-visible oracle for host maintenance. (Area 5.2-B2.)
4. **Assess the helper-script supply chain:** evaluate the "download and run" + "run the emitted
   fix commands as root" flow for integrity controls. (Area 5.3.)
5. **Close the cross-tenant null hypothesis** for ENA Express specifically, without conflating it
   with EFA. (Area 8.)

---

## 2 — Components, assets, and design

**Customer-facing interface.** No new endpoint. ENA Express is a boolean-pair attribute
(`EnaSrdSpecification { EnaSrdEnabled: bool, EnaSrdUdpSpecification { EnaSrdUdpEnabled: bool } }`)
carried on the EC2 control plane (SigV4 IAM), plus a guest-OS data path (the standard ENA driver
/ socket / TCP-UDP stack — SRD is engaged *below* the socket API, transparent to the app) and a
console surface ("Manage ENA Express" dialog with **Enable** / **Enable UDP** checkboxes).

**Processes / fleets behind it.** AWS's own network backbone ("different AWS network paths") and
the Nitro card / ENA device that terminates SRD reorder+retransmit below the guest's logical ENI.
These are AWS-service-plane and are **out of scope / hard-stop** (Area 7). The guest-side ENA
kernel driver and `ethtool -S` counters are customer-owned.

**Accounts / VPCs.** Entirely within the customer account/VPC. SRD operates between two
customer instances that *already* have standard EC2 networking reachability to each other, in
the **same Region**. There is no documented service-account, data-plane-account, or shared-fleet
multi-tenancy exposed to the customer through this feature (contrast EFA — Area 7).

**Resource / identifier shape.** The setting is **attachment-scoped**, not ENI-scoped: it lives
on `NetworkInterfaces[].Attachment.EnaSrdSpecification` and is dropped when the ENI is detached
or the instance terminated (even though the ENI object persists). Identifiers in play are
ordinary `eni-…` / `i-…` / `eni-attach-…` — not a new ID class.

**Identity.** SigV4 IAM on the control-plane actions; guest-OS root for the `ethtool`/driver
counters and the helper script.

**Untrusted-data transforms.** None in the classic injection sense — ENA Express does not parse
customer documents/URLs. The only "transform" is SRD packet fan-out + reassembly, which is the
observability lead (Area 5.2), not an injection seam.

**ASCII design / data flow:**

```
   Customer account / VPC (same Region, both ends opt in)
   ┌─────────────────────────────┐              ┌─────────────────────────────┐
   │  Instance A (sender)        │              │  Instance B (receiver)       │
   │  app ── socket ── TCP/UDP   │              │   TCP/UDP ── socket ── app   │
   │        │                    │              │        ▲                     │
   │   ENA driver (EnaSrdEnabled)│              │  ENA driver (EnaSrdEnabled)  │
   │   logical ENI  ◄── Flow Logs / Traffic Mirroring tap here (sees reassembled flow only)
   └────────┼────────────────────┘              └────────┼────────────────────┘
            │  SRD below the ENI abstraction:             ▲
            │  fan-out across N AWS paths + reorder + retransmit
            ▼                                             │
   ┌───────────────────────  AWS backbone (SERVICE PLANE — HARD STOP)  ───────────────────────┐
   │   path 1 ─┐                                                                               │
   │   path 2 ─┼──►  reorder/retransmit terminated on Nitro/ENA device at receiver             │
   │   path N ─┘                                                                               │
   └───────────────────────────────────────────────────────────────────────────────────────────┘

   Control plane (SigV4 IAM):  AttachNetworkInterface | RunInstances | ModifyNetworkInterfaceAttribute
                               ──► set EnaSrdSpecification       DescribeInstances / DescribeNetworkInterfaces ──► read it
```

---

## 3 — API / interface inventory

| Name | Method | Mutating | Facing | Sets/Reads EnaSrd | `ec2:Attribute`? | Resource-scopable? | Notes |
|---|---|---|---|---|---|---|---|
| `AttachNetworkInterface` | SigV4 | yes | external | **sets** (attach-time) | **No** (line 4861) | tag/ENI/Subnet/VPC/AZ | implicit attach; no attribute-name gate |
| `RunInstances` | SigV4 | yes | external | **sets** (launch-time, `NetworkInterfaces[].EnaSrdSpecification`) | **No** (line 9595) | RequestTag/ENI/Subnet/VPC/AZ | wizard + launch template |
| `ModifyNetworkInterfaceAttribute` | SigV4 | yes | external | **sets** (post-hoc) | **Yes** (line 8969) | same + attribute-name | only path with an attribute-name gate |
| `DescribeInstances` | SigV4 | no | external | **reads** | n/a | **No — region only** | unscopable read oracle |
| `DescribeNetworkInterfaces` | SigV4 | no | external | **reads** | n/a | **No — region only** | unscopable read oracle |
| `ModifyInstanceAttribute` | SigV4 | yes | external | — (no EnaSrd field) | Yes | instance keys | has `ec2:Attribute` but no EnaSrd param — irrelevant to SRD |
| `CreateNetworkInterface` | SigV4 | yes | external | **no** (EnaSrd not accepted) | No | ENI/Region | SRD not settable at ENI-create time |
| Console "Manage ENA Express" | HTTPS | yes | external | sets | — | — | **premise "no console surface" REFUTED** |
| `ethtool -S eth0` SRD counters | guest OS | no | internal | reads driver counters | — | — | `ena_srd_*`; side-channel source (5.2-B2) |
| `check-ena-express-settings.sh` | GitHub | no | external artifact | — | — | — | AWS-authored, "download and run" (5.3) |

**Line references** are into
`/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (the authoritative
"Actions defined by Amazon EC2" per-action table — **not** the earlier non-authoritative "API
operations" cross-reference section). Note: the path `/work/aws-docs/list_ec2.md` 404s; use the
`docs/service-authorization/latest/reference/` mirror path.

**Hidden-knob sweep result:** `grep -ni "EnaSrd|InterfaceType|NetworkCard|ec2:Srd" list_ec2.md`
→ **0 hits for all four.** No condition key of any name inspects the SRD boolean *value*, and
`ec2:InterfaceType` does not exist as an EC2 condition key — so a Deny keyed on it is silently
inert (Lens S). The console-hidden-knob premise is **refuted** for ENA Express (it is fully
console-manageable); the genuine delta is the opposite — the API is *fully* exposed, but the IAM
*condition surface* governing it is thin and asymmetric.

---

## 4 — Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| IAM principal with Attach/Run perms | ENI attachment's SRD transport mode | `AttachNetworkInterface` / `RunInstances` set `EnaSrdSpecification` with **no attribute-name condition key** | Enabling SRD on an attachment that an attribute-name Deny on `ModifyNetworkInterfaceAttribute` was meant to forbid = **policy-bypass breach** (Area 5.1) |
| Any IAM principal with `Describe*` in a Region | SRD state of **every** ENI/instance in that Region | `DescribeInstances`/`DescribeNetworkInterfaces` carry only `ec2:Region` | Reading SRD config for a resource the principal can't name/tag-scope = **unscopable read oracle** (Area 5.1) |
| Defender relying on Flow Logs / Traffic Mirroring | SRD multipath / reorder / retransmit layer | Monitoring taps the **logical ENI**, above SRD reassembly | Any SRD path-level behavior invisible to a complete flow-log/mirror record = **detection-posture gap** (Area 5.2-B1) |
| Unprivileged-ish guest reader | Host maintenance events (live migration / live server update) | `ethtool -S` eligible-vs-actual TX divergence | Guest inferring a host-side maintenance window from the counter gap = **side-channel disclosure** (Area 5.2-B2) |
| Operator following AWS prose | Root shell on own instance | "download and run" `check-ena-express-settings.sh` + run emitted `sudo` fix commands | A tampered script/output executing attacker-chosen commands as root = **supply-chain breach** (Area 5.3) |
| Customer instance | **AWS backbone / Nitro SRD termination** | SRD fan-out + reorder below the ENI | **HARD STOP** — any identity/credential/packet from AWS's own service plane reached via this path; preserve evidence, flag for disclosure (Area 7) |

---

## 5 — Recommended areas of focus (per firing lens)

### 5.1 — IAM condition-key parity gap across the three write paths (Lens S / Lens X) — **PRIMARY ACTIONABLE LEAD, Severity: Medium**

**Claim:** A defender who tries to govern who may enable SRD by denying the *attribute name* on
`ModifyNetworkInterfaceAttribute` (`ec2:Attribute: "enaSrdSpecification"`, the generic mechanism
in `iam-policies-for-amazon-ec2.md`) gets **no protection at all** against the identical setting
being applied through `AttachNetworkInterface` or `RunInstances`, because those actions'
`network-interface*` resource rows **do not carry `ec2:Attribute` / `ec2:Attribute/${AttributeName}`
at all**.

**Mechanism (doc evidence, confirmed by sub-analysis of `list_ec2.md`):**
- `ModifyNetworkInterfaceAttribute` `network-interface*` row (line 8969) carries
  `ec2:Attribute` **and** `ec2:Attribute/${AttributeName}`.
- `AttachNetworkInterface` `network-interface*` row (line 4861): `aws:ResourceTag`,
  `ec2:AvailabilityZone`, `ec2:ManagedResourceOperator`, `ec2:NetworkInterfaceID`, `ec2:Region`,
  `ec2:ResourceTag`, `ec2:Subnet`, `ec2:Vpc` — **no `ec2:Attribute`.**
- `RunInstances` `network-interface*` row (line 9595): `aws:RequestTag`, `aws:TagKeys`,
  `ec2:AssociatePublicIpAddress`, `ec2:AuthorizedService`, `ec2:AvailabilityZone`,
  `ec2:IsLaunchTemplateResource`, `ec2:LaunchTemplate`, `ec2:ManagedResourceOperator`,
  `ec2:NetworkInterfaceID`, `ec2:Region`, `ec2:Subnet`, `ec2:Vpc` — **no `ec2:Attribute`.**
- **No condition key anywhere inspects the EnaSrd *value*** (0 hits for `EnaSrd`/`ec2:Srd`), so
  even the Modify path can only gate *which attribute name* is touched, never the true/false
  being written. All three paths are value-blind; only Modify is attribute-name-aware.

**Confirm/Refute oracle:** Fully resolvable by reading the IAM reference (done — asymmetry
confirmed across all three actions). Live confirmation: with a role allowed `AttachNetworkInterface`
but under a policy that `Deny`s `ModifyNetworkInterfaceAttribute` on
`ec2:Attribute/${AttributeName} == enaSrdSpecification`, enable SRD via attach-time
`--ena-srd-specification 'EnaSrdEnabled=true'` and read it back via `DescribeNetworkInterfaces`.
Success proves the Deny is bypassable. (A tag/ENI/Subnet/VPC-scoped Deny on the *action itself*
is the only effective control — not an attribute-name Deny.)

**Also test (unscopable read oracle):** `DescribeInstances` / `DescribeNetworkInterfaces` have
**blank required-resource-type and only `ec2:Region`** (lines ~6998 / ~7220) — a principal with
Describe in a Region can read SRD state for every ENI/instance in that Region regardless of
ownership or tag. There is no resource-level lever to restrict who reads SRD config.

**Preconditions / cost:** Zero privilege to *discover* (pure IAM-reference read). To exploit,
only whatever Attach/Run perms a "network admin" role already holds — such roles are commonly
granted broadly without anyone realizing they carry SRD-enable authority the Modify-path Deny
doesn't cover.

**Severity: Medium** — policy-completeness / least-privilege footgun, not a cross-tenant break.
Matters wherever an org treats "no ENA Express" (e.g. to keep east-west traffic in a documented,
inspectable transport mode — see 5.2) as a compliance control and tries to enforce it with an
attribute-name Deny.

> Cross-ref: the *post-hoc reconfiguration* framing of the Modify path and the attachment-scoped
> silent-revoke lifecycle are owned by `modify-network-interface-attributes-attack-research-plan.md`
> §5.7 — not restated here.

### 5.2 — SRD observability / detection-posture gaps (Lens O)

**B1 — Flow Logs / Traffic Mirroring are blind to the SRD layer. Severity: Medium (detection gap).**
`grep -rli 'ena express|EnaSrd|ena_srd|SRD|scalable reliable datagram'` across the entire VPC
doc tree (`flow-logs-*.md`, `flow-log-records.md`, `flow-logs-limitations.md`, all of
`mirroring/*.md`) → **zero hits.** Flow Logs record at the **logical ENI**
(`flow-logs-basics.md`), i.e. *post*-SRD-reassembly; no field in `flow-log-records.md` indicates
SRD path, retransmit count, or reorder. Traffic Mirroring taps the ENI similarly
(`traffic-mirroring-network-limitations.md` discusses only ENA checksum-offload truncation, not
SRD). **Oracle (live, out of scope here):** compare flow-log 5-tuple/packet counts and a mirrored
capture for an SRD-eligible flow vs the same flow with ENA Express disabled; check for
reorder/retransmit artifacts or multipath fan-out an inline IDS would miss or double-count. A
defender relying on Flow Logs/Mirroring as a *complete* path-level record is working from an
incomplete view — flagged as an architectural blind spot, **not** a demonstrated evasion
technique (no doc evidence of exploitability).

**B2 — Eligible-vs-actual TX divergence is a documented guest-visible host-maintenance oracle.
Severity: Low/Informational.** `monitoring-network-performance-ena.md` states the gap between
`ena_srd_eligible_tx_pkts` and `ena_srd_tx_pkts` "can also fall into this gap **during live
migrations or live server updates**" — an explicit AWS-documented causal link between a
guest-readable `ethtool -S eth0` counter and a host-side maintenance event AWS does not otherwise
disclose in real time. **Oracle (live, out of scope):** poll both counters at short intervals; a
sustained divergence spike *uncorrelated* with `ena_srd_resource_utilization` nearing 100% is
attributable (per AWS's own text) to a live-migration / host-update window. AWS itself tempers
this ("you can ignore occasional minor differences… when your instance establishes a connection
to another instance for SRD traffic") — i.e. the signal is noisy. Discloses only *that* the host
is being maintained, not any other tenant's data; CPU steal-time / clock-skew are long-known,
lower-friction equivalents. Novel enough to record; not alarming absent a demonstrated attacker
use (e.g. timing an action to a migration window).

> This is the same underlying counter owned by `.cache/ena-driver-monitoring-findings.md` (O/L-4);
> re-stated here because it is ENA-Express-specific and directly load-bearing for this plan's
> observability theme.

**A4 — UDP MTU / PMTUD blackhole (minor). Severity: Low/Informational.** ena-express.md: "Newly
established TCP connections automatically clamp the MSS… but UDP traffic still requires a lower
MTU." An operator who enables ENA Express UDP without lowering the UDP-path MTU can get silent
fragmentation / black-holing — compounded if NACLs/SGs block the ICMP "fragmentation needed"
messages PMTUD depends on. Self-inflicted DoS of the operator's own flow only; no cross-party
impact. Recorded as an operational caveat the docs don't explicitly flag.

### 5.3 — AWS-authored settings-check script (Lens R / Lens Q — download-and-run supply chain)

**A1 — "Download and run" against a mutable branch, no integrity ceremony. Severity: Low.**
ena-express.md links `https://github.com/amzn/amzn-ec2-ena-utilities/blob/main/ena-express/check-ena-express-settings.sh`
— pinned to `main`, not a tag/commit/release. No checksum, signature, or hash is published; the
doc frames it as a turnkey "download and run." Functionally a curl-pipe-to-root pattern for
anyone who scripts the fetch+exec rather than reading it. **Mitigations:** it is AWS's own GitHub
org; the script is read-only (it *emits* `sudo` commands, does not run them); blast radius is the
customer's own instance. Residual risk is pure supply chain (repo/account compromise or MITM'd
clone) with no doc-level compensating control. **Refuted if** AWS adds a signed release / documented
checksum / commit-pinning.

**A2 — Two-stage trust: operator must also run the emitted `sudo` commands. Severity: Low.**
"…outputs the exact commands to fix any issues it finds" (e.g. `sudo ip link set {interface} mtu
8900`). The doc gives no guidance to review emitted commands before running them as root — the
whole flow (download → run → run the output) is framed as a turnkey fix. A compromised or buggy
script could emit a destructive/malicious command string the operator is implicitly told to trust.
Additive to A1 (trust the logic *and* the output), same self-instance blast radius.

**A3 — Best-practices tuning is NOT a security weakening. Severity: Null/Low (refuted).** The
`ENA_Linux_Best_Practices.rst` recommendations (`tcp_sack=0` — incidentally the SACK-Panic DoS
mitigation, so security-neutral-to-positive; `busy_read/busy_poll=70`; larger ring buffers,
bounded 256–16K rx / 256–1K tx; `max_cstate=1`) are latency/throughput tuning with CPU/memory
cost on the customer's own instance. None disable auth, encryption, access control, or logging.
Recorded as a bounded null to prevent over-claiming.

---

## 6 — Threat-model test objectives (priority order)

1. **[Medium — do first, no live account needed for the doc half]** Confirm the 5.1 IAM parity
   bypass: attribute-name Deny on `ModifyNetworkInterfaceAttribute` vs SRD-enable via
   `AttachNetworkInterface` / `RunInstances`. Then confirm `Describe*` is region-only unscopable.
2. **[Medium]** Live-characterize 5.2-B1: is any SRD path/reorder/retransmit behavior observable
   in Flow Logs or a Traffic-Mirror capture, or only the reassembled logical flow?
3. **[Low/Info]** Live-characterize 5.2-B2: is the eligible-vs-actual TX divergence a
   reliable-enough live-migration oracle to be useful, given AWS's own noise caveat?
4. **[Low]** Review `check-ena-express-settings.sh` at a pinned commit; diff `main` over time;
   assess whether emitted fix commands can be influenced by attacker-controlled instance state
   the script reads (5.3-A1/A2).
5. **[Null-closing]** Attempt and document the absence of any cross-tenant SRD reach primitive
   (Area 8) — explicitly separate from EFA (Area 7).

---

## 7 — Out of scope / hard stops

- **AWS backbone + Nitro/ENA SRD termination** (the "different AWS network paths", reorder, and
  retransmit machinery) is AWS service plane. Any identity, credential, ARN, or packet observed
  originating from it is a **HARD STOP** — preserve evidence, cease, flag for disclosure. No such
  surface is reachable through any documented ENA Express interface.
- **EFA (Elastic Fabric Adapter) OS-bypass RDMA** is a *different feature* that is also
  "SRD"-branded. Its cross-tenant frame-injection lead is owned by
  `ec2-networking-attack-research-plan.md` Lead [3] / Cluster 3. **Do not treat an EFA finding as
  transferable to ENA Express or vice versa** — ENA Express SRD rides inside the standard
  ENA/socket/TCP-UDP stack on ordinary ENIs and remains subject to normal SG/VPC enforcement; EFA
  bypasses the guest kernel entirely on dedicated EFA devices. Re-derive separately if testing EFA.
- No DNS/port/subdomain enumeration; HTTP/application + control-plane layer only.
- No destructive payloads; read-only PoC / dummy values only.

---

## 8 — Null hypotheses and documentation gaps (consolidated)

| Hypothesis | Verdict | Pages checked |
|---|---|---|
| No IAM condition key scopes the EnaSrd enable/disable **value** | **CONFIRMED TRUE** | `list_ec2.md` full-file grep (`EnaSrd`/`ec2:Srd` → 0 hits) |
| `ec2:InterfaceType` / `NetworkCard` condition keys exist (a Deny on them would bind) | **REFUTED** (0 hits — any such Deny is silently inert, Lens S) | `list_ec2.md` |
| ENA Express is not surfaced in the EC2 console | **REFUTED** — full "Manage ENA Express" dialog exists | `ena-express-configure.md` + `-list-view.md` Console tabs; `enhanced-networking-ena.md:55` shown to refer to a *different* feature |
| `AttachNetworkInterface` carries the same attribute-name gate as Modify | **REFUTED** — it carries none; so does `RunInstances` | `list_ec2.md` lines 4861 / 8969 / 9595 |
| Flow Logs / Traffic Mirroring docs state how SRD traffic is captured | **SILENT** (no statement either way → detection gap) | all `docs/vpc/latest/userguide/flow-logs-*.md`, `docs/vpc/latest/mirroring/*.md`, `monitoring-network-performance-ena.md` |
| ENA Express provides a cross-tenant reach primitive distinct from standard EC2 networking | **NOT SUPPORTED** (both-ends-opt-in; same-Region; silent fallback on mismatch; no SG/VPC/routing override claimed) — null, distinct from EFA | `ena-express.md`, `-configure.md`, `-list-view.md` (all, in full) |
| Best-practices tuning weakens security posture | **REFUTED** (null) | `ENA_Linux_Best_Practices.rst` |
| SRD per-instance connection-memory cap translates into a documented cross-tenant backbone noisy-neighbor effect | **BOUNDED NULL** — `ena_srd_resource_utilization` is explicitly per-instance memory; no shared-backbone capacity metric exposed | `monitoring-network-performance-ena.md`, `ena-express.md` |
| Middlebox requirement is a *security* control | **REFUTED** — it is a compatibility/eligibility requirement; docs silent on behavior when violated, but architecture ("two cooperating ENA drivers", not a tunnel) is consistent with "SRD doesn't engage", not "bypasses the appliance" | `ena-express.md`, `-configure.md` |

**Residual verification gap:** `ena-express-list-view.md` was read offline in full and
field-name-cross-checked against `list_ec2.md`, but (being read-only/non-mutating) was not
independently re-fetched online — low risk, flagged for completeness.

---

*Prepared with the `security-questionbuilder` skill, documentation-only, boundary-first. All
confirmed facts are traceable to the cited page/line; all live-test items are explicitly marked
out-of-scope for this doc-only pass.*
