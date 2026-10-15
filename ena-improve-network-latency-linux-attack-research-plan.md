# Improve network latency for Linux based EC2 instances — Attack / Research Plan

> **Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-improve-network-latency-linux.html
> (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ena-improve-network-latency-linux.md`).
> **Method:** `security-questionbuilder` skill — boundary-first, documentation-only; no live
> testing. Online `.html` and offline `.md` were diffed and are **byte-for-byte identical**
> (81 lines, both outbound link targets identical), including the two cross-service pointers.
> **Prepared:** 2026-10-15. Status: documentation-derived hypotheses only; nothing tested against a live account.

---

## 0 — How to use this document

This is a **guest-OS performance-tuning page**, not a control-plane feature page. It tells a Linux
operator how to lower network latency on *their own* EC2 instance by (1) reducing network hops
(cluster placement group / Dedicated Host), (2) tuning the Linux kernel (busy-poll sysctls,
C-states), and (3) tuning the ENA driver's interrupt moderation with `ethtool`. **It introduces
no AWS API, no IAM action, no condition key, no role, no URL the service dereferences, no uploaded
blob, and no tenant identifier.** The honest headline is therefore a *null*: the page exposes no
new control-plane or cross-tenant attack surface of its own.

Consequently the real, ownable surface is narrow and all low/informational:

1. **One AWS-authored download-and-apply artifact** (Area 5.1, Lens R/Q) — the `ENA_Linux_Best_Practices.rst`
   guide the page links on a *mutable* GitHub branch, which instructs root-level kernel/driver changes.
   This is the one lead a defender/supply-chain reviewer can act on. **Distinct** from the ENA Express
   sibling's `check-ena-express-settings.sh` (different repo).
2. **A guest-tuning-is-not-a-security-weakening bounded null** (Area 5.2, Lens U) — a per-tuning audit
   proving the recommended changes are security-neutral-to-positive, with the one microarchitectural
   caveat (C-state limiting) sharply bounded so it is not over-claimed.
3. **Two cross-service pointers** (Area 5.3) — cluster placement group (co-residency/topology) and
   Dedicated Host (tenancy) — whose security surface is **owned elsewhere** and only cross-referenced.

HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own
service plane (e.g. the Nitro card below the ENA driver), stop, preserve evidence, flag for
AWS-Security disclosure. No such surface is reachable through anything documented on this page.

---

## 1 — Pentest objectives

1. **Characterize the supply-chain artifact:** assess the `ENA_Linux_Best_Practices.rst`
   "download and apply as root" flow for branch-pinning / integrity controls (Area 5.1).
2. **Close the control-plane null:** prove no ENA interrupt-moderation / busy-poll / C-state / MTU /
   ring-buffer tuning on this page maps to any `ec2:` action or condition key (Area 5.2 / Area 8).
3. **Audit each tuning against security posture:** confirm the recommended guest changes do not
   weaken auth/encryption/access-control/logging, and bound the C-state microarchitectural caveat
   honestly (Area 5.2).
4. **Hand off the co-residency and tenancy angles** to their owning plans without re-deriving them
   (Area 5.3), and flag the Dedicated-Host corpus gap.
5. **Record the cross-tenant null** for the guest data path (Area 8) — Nitro per-instance ENA
   queue virtualization means disabling interrupt moderation is a self-DoS, not a shared-fleet one.

---

## 2 — Components, assets, and design

**Customer-facing interface.** None new. The entire page operates **inside the guest OS**:
`sysctl -w net.core.busy_read` / `net.core.busy_poll`; `ethtool -c`/`-C` against the ENA interface;
GRUB/kernel-cmdline C-state limits. Identity for all of it is **guest-OS root** (`sudo`), not SigV4 IAM.

**Processes / fleets behind it.** The guest-side **ENA kernel driver** (customer-owned; `ethtool -S`
counters, interrupt handling) and, below the logical ENI, the AWS **Nitro card** that generates the
receive interrupts. The Nitro card is **AWS service plane — out of scope / hard-stop** (Area 7).

**Accounts / VPCs.** Entirely within the customer's own instance. The two "reduce hops" options touch
the control plane only *by reference*:
- **Cluster placement group** (`placement-strategies.md#placement-groups-cluster`) — packs instances
  physically close in one AZ for low latency = **maximizes co-residency** (a topology/side-channel
  adjacency surface, owned elsewhere — Area 5.3).
- **Dedicated Host** (`dedicated-hosts-overview.md`) — a physical server dedicated to one account =
  single-tenant hardware tenancy (owned elsewhere — Area 5.3).

**Resource / identifier shape.** No new ID class. No ARN, no opaque ID, no tenant ID appears anywhere
on the page.

**Untrusted-data transforms.** None. The page parses no customer documents/URLs. The only outbound
URLs are **human-facing prose links** (the GitHub `.rst` guide, kernel.org docs, the AL2 User Guide) —
the service never fetches them, so there is no SSRF seam (Area 8, Lens G null).

**Secrets.** None generated or stored (Lens T null).

**ASCII design / data flow:**

```
   Customer instance (single tenant)                         AWS service plane (HARD STOP)
   ┌──────────────────────────────────────────────┐         ┌──────────────────────────────┐
   │  app ── socket ── TCP/UDP stack                │         │                              │
   │     ▲  busy_read / busy_poll (sysctl, root)    │         │                              │
   │  ENA kernel driver (customer-owned)            │         │                              │
   │     • interrupt moderation  (ethtool -C, root) │◄── RX interrupts ── Nitro card (AWS)   │
   │     • ring buffers / MTU    (ethtool, root)    │         │  per-instance virtualized    │
   │  CPU C-states (GRUB / kernel cmdline, root)    │         │  ENA queues (no shared surf.)│
   │  logical ENI ──────────────────────────────────┼─────────┤                              │
   └──────────────────────────────────────────────┘         └──────────────────────────────┘

   Control-plane references (NOT configured on this page — pointers only):
     Cluster placement group  →  co-residency / DescribeInstanceTopology   (owned by ec2-networking hub)
     Dedicated Host           →  ec2:Tenancy / host-resource actions        (no current corpus owner)

   AWS-authored artifact (download & apply as root):
     github.com/amzn/amzn-drivers .../ENA_Linux_Best_Practices.rst   (branch=master, no integrity ceremony)
```

---

## 3 — API / interface inventory

| Name | Type | Mutating | Facing | Identity | Control-plane? | Notes |
|---|---|---|---|---|---|---|
| `sysctl -w net.core.busy_read` / `busy_poll` | guest OS | yes (guest) | internal | guest root | **No** | low-latency busy-poll; CPU cost only |
| `ethtool -c {iface}` | guest OS | no | internal | guest root | **No** | read interrupt-moderation config |
| `ethtool -C {iface} adaptive-rx off rx-usecs 0 tx-usecs 0` | guest OS | yes (guest) | internal | guest root | **No** | disable interrupt moderation |
| C-state limit (`intel_idle.max_cstate=1 processor.max_cstate=1` via GRUB) | guest OS | yes (guest) | internal | guest root | **No** | per .rst / AL2 processor_state_control |
| ring-buffer / MTU (`ethtool -G`, `ip link set mtu`) | guest OS | yes (guest) | internal | guest root | **No** | implied by the .rst guide |
| Cluster placement group | control plane | — | external | SigV4 IAM | **ref only** | `CreatePlacementGroup` / `RunInstances --placement`; **owned by ec2-networking hub Cluster 3** |
| Dedicated Host | control plane | — | external | SigV4 IAM | **ref only** | `ec2:Tenancy` + host actions; **no current corpus owner (gap)** |
| `ENA_Linux_Best_Practices.rst` | GitHub artifact | no | external artifact | n/a | n/a | AWS-authored, mutable `master`, root instructions (Area 5.1) |

**Control-plane / IAM reachability — confirmed null.** A grep of the authoritative IAM reference
`/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` for
`interrupt | moderation | usecs | busy(_|)poll | cstate | c-state | ethtool | ring(-|)buffer | mtu | driver | ena`
returns **zero genuine hits** — the only `interrupt` matches are unrelated homonyms
(`CreateInterruptibleCapacityReservationAllocation`, `SendDiagnosticInterrupt`, Spot-interruption
keys). There is **no `ec2:EnaSupport` condition key** (the `enaSupport` *attribute* is reachable only
via the generic, value-blind `ec2:Attribute`/`ec2:Attribute/${AttributeName}` keys on
`ModifyInstanceAttribute` — a *different*, enhanced-networking-enablement surface this page never
touches). ⇒ every tuning on this page is **100% guest-OS**, with no `ec2:` action or condition key to
scope, allow, or deny it. (Note: `/work/aws-docs/list_ec2.md` 404s — always use the
`docs/service-authorization/latest/reference/` mirror path. See [[reference-aws-iam-service-auth-ref-url]].)

---

## 4 — Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Operator following AWS prose | Root shell on own instance | "see the ENA Linux Best Practices Guide" → operator fetches the `.rst` from a mutable branch and transcribes/applies its `sudo` commands | A tampered guide (repo/account compromise, MITM'd clone, malicious `master` commit) causing the operator to run attacker-chosen root commands = **supply-chain breach** (Area 5.1). Blast radius = operator's own instance. |
| Guest root | ENA driver interrupt behavior | `ethtool -C … rx-usecs 0` maximizes interrupt rate | Degraded availability of **the operator's own instance** only — Nitro virtualizes ENA queues per instance, so there is **no shared interrupt/queue surface to a co-tenant** = single-tenant self-DoS, **out of scope** (Area 5.2 / 8). |
| Guest root | CPU power/frequency state | C-state limiting keeps cores active, changes Turbo headroom | Theoretical frequency/power microarchitectural side-channel class — **not demonstrated** here; per-instance guest control behind the Nitro boundary. Bounded null, **not elevated** (Area 5.2). |
| IAM principal choosing placement | Physical co-residency of instances | `RunInstances` into a cluster placement group | Co-residency / topology adjacency (DescribeInstanceTopology oracle) — **owned by `ec2-networking-attack-research-plan.md` Cluster 3**, cross-ref only (Area 5.3). |
| IAM principal choosing tenancy | Single-tenant physical server | Dedicated Host allocation (`ec2:Tenancy`) | Tenancy isolation surface — **no current corpus owner (gap)**, cross-ref only (Area 5.3). |
| Customer instance | **AWS Nitro card / ENA termination** | RX interrupt generation below the logical ENI | **HARD STOP** — any identity/credential/packet from AWS's own service plane. No such surface reachable via this page (Area 7). |

---

## 5 — Recommended areas of focus (per firing lens)

### 5.1 — AWS-authored best-practices guide as a download-and-apply artifact (Lens R / Lens Q) — **PRIMARY (and only actionable) LEAD, Severity: Low**

**Background.** Line 13 of the page: *"For additional configuration guidance, see the
[ENA Linux Driver Best Practices and Performance Optimization Guide](https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/ENA_Linux_Best_Practices.rst) on GitHub."* The guide is AWS-authored
(repo `amzn/amzn-drivers`) and instructs the operator to apply a series of changes **as root**.

**Security Concern.** The link is pinned to the **mutable `master` branch**, *not* a tag or commit, even
though the repo publishes tagged releases. **No checksum, signature, or integrity ceremony** is
published anywhere in the chain (the AWS doc, the `.rst` itself, or the repo's security-policy stub).
The guide instructs root-level, security-adjacent changes confirmed to include:
`sudo ethtool -C … adaptive-rx off rx-usecs 0 tx-usecs 0`, `sudo ethtool -L combined N`,
`sudo ethtool -G rx 4096`, `sudo sysctl -w vm.min_free_kbytes=1048576`,
`echo 70 > /proc/sys/net/core/busy_read|busy_poll`, `echo 0 > /proc/sys/net/ipv4/tcp_sack`,
and GRUB `intel_idle.max_cstate=1 processor.max_cstate=1`.

**High-level test scenarios.**
- Treat the flow as functionally a "fetch guidance from a mutable branch → apply root commands"
  pattern. Because the content is **prose (`.rst`), not a piped install script**, the realistic worst
  case is "a tampered `master` commit convinces an operator to transcribe a malicious root command,"
  **not** a `curl | sudo bash` RCE — there is no network callback or binary execution implied.
- Confirm/refute oracle: diff `master` against the latest tagged release of the `.rst` over time; a
  guide whose "fix" commands change between a pinned release and `master` without the AWS doc updating is
  the supply-chain risk. **Refuted if** AWS pins the link to a tag/commit or publishes a release/checksum.
- **Re-flag immediately** if AWS ever converts this guide (or any linked helper) into a direct
  `curl … | sudo bash` one-liner — that upgrades the severity materially.

**Non-duplication:** this is a **distinct artifact** from the ENA Express sibling's
`check-ena-express-settings.sh`, which lives in a *different* repo entirely
(`amzn/amzn-ec2-ena-utilities/ena-express/`). The two supply-chain leads do not overlap; see
`ena-express-attack-research-plan.md` §5.3.

**Severity: Low** — AWS's own GitHub org; prose not an executable; self-instance blast radius; no
doc-level compensating control. Pure supply-chain residual (repo/account compromise or MITM'd clone).

### 5.2 — Guest tunings vs security posture, and the control-plane null (Lens U / Lens S) — **Severity: Null / Informational**

**Background.** The page recommends disabling interrupt moderation, enabling busy-polling, and limiting
C-states. A naive reviewer might treat "disable a default protection mechanism" as a weakening.

**Security Concern + resolution (per-tuning audit).** Each recommended change was traced to its effect
and its tenancy boundary:

| Tuning | Effect | Weakens / Neutral / Strengthens | Cross-tenant? | Verdict |
|---|---|---|---|---|
| `ethtool -C adaptive-rx off rx-usecs 0 tx-usecs 0` (disable interrupt moderation) | max interrupt rate, higher CPU overhead on RX path | Neutral (perf trade-off) | **No** — Nitro virtualizes ENA queues per instance; no shared interrupt/queue surface | Single-tenant self-DoS only → **out of scope** |
| `net.core.busy_read` / `busy_poll` (busy-poll) | socket layer polls device queue; higher CPU | Neutral | No | Self-inflicted CPU cost; null |
| C-state limiting (`max_cstate=1`) | cores stay active; changes Turbo Boost headroom | Neutral (perf trade-off); theoretical freq/power side-channel class | No (per-instance, behind Nitro) | **Bounded null** — a *theoretical* microarch side-channel category from general cloud literature, **no documented or Nitro-specific lead**; AWS frames the trade-off only vs the instance's *own* other vCPUs. **Not elevated.** |
| `tcp_sack=0` (from the `.rst`) | disables TCP selective ACK | **Strengthens** | n/a | Incidentally the mitigation posture for **SACK Panic (CVE-2019-11477 family)** — security-neutral-to-positive |
| ring buffers / MTU (`ethtool -G`, `ip link set mtu`) | buffer sizing | Neutral | No | perf tuning; null |

**None of these disable authentication, encryption, access control, or logging.** Combined with the
Section 3 **control-plane null** (no `ec2:` action/condition key governs any of them), the conclusion is
a documented, bounded null rather than a finding. Recorded to prevent over-claiming and to anchor the
C-state side-channel caveat honestly.

**Cross-check:** the Amazon Linux 2 `processor_state_control` page (linked for C-states) is **purely
guest-OS config** (GRUB edits, `grub2-mkconfig`, reboot, `/sys/.../no_turbo` toggle) — it introduces no
AWS API or control-plane surface either.

### 5.3 — Cross-service pointers (co-residency + tenancy) — **owned elsewhere; cross-ref only**

**Cluster placement group (line 22).** Recommending a *cluster* placement group to reduce hops packs
instances physically close in one AZ — i.e. it **maximizes co-residency**, which is a topology /
side-channel-adjacency surface (and a `DescribeInstanceTopology` co-residency confirmation oracle). The
real control plane here (`CreatePlacementGroup`, `RunInstances --placement`, and the **real** condition
keys `ec2:PlacementGroupStrategy` / `ec2:PlacementGroupName`, confirmed present in `list_ec2.md`) is
**owned by `ec2-networking-attack-research-plan.md`, "Cluster 3 — Placement/Topology/EFA/Enhanced-net."**
This page's "pack tight for latency" framing is a **research note to cross-link**, not a finding to add
here. Do not re-derive.

**Dedicated Host (line 23).** Recommending a Dedicated Host so instances share one physical server is a
single-tenant hardware-tenancy surface (`ec2:Tenancy` + host-resource-type actions). **No
`*dedicated-host*` / `*host*` attack-research plan currently exists in the corpus** — this is a genuine
**gap in the plan corpus**, not a defect on this page. Flagged for a future sibling; this page defers to
that (not-yet-existing) owner and should not grow a tenancy section.

---

## 6 — Threat-model test objectives (priority order)

| # | Threat / test case | Component | Documented mitigation to attack | Severity-if-true |
|---|---|---|---|---|
| 1 | Does the `ENA_Linux_Best_Practices.rst` flow lack branch-pinning / integrity controls, and could a mutable-`master` tamper reach an operator's root shell? | GitHub artifact (`amzn/amzn-drivers`) | None documented (prose link, no checksum/signature) | Low (self-instance supply chain) |
| 2 | Prove no `ec2:` action or condition key governs ENA interrupt moderation / busy-poll / C-state / MTU / ring buffers (null close). | `list_ec2.md` | n/a — guest-OS only | Informational (null) |
| 3 | Confirm each recommended tuning is security-neutral-to-positive; bound the C-state side-channel caveat as theoretical only. | guest OS | n/a | Informational (null) |
| 4 | Hand off co-residency (cluster placement group) and tenancy (Dedicated Host) to their owners; flag the Dedicated-Host corpus gap. | control plane (ref) | owned by `ec2-networking` hub / unowned | n/a (cross-ref) |
| 5 | Confirm the guest data-path cross-tenant null (interrupt disable = self-DoS, not shared-fleet). | ENA driver + Nitro | per-instance virtualized ENA queues | Informational (null) |

---

## 7 — Out-of-scope risk categories

- **AWS Nitro card / ENA SRD/termination plane** below the logical ENI — AWS service plane, **hard stop**.
- **Single-tenant self-DoS** from disabling interrupt moderation or over-busy-polling the operator's own
  instance — the operator harming only their own instance.
- **Theoretical microarchitectural side channels** from C-state/Turbo manipulation absent a demonstrated,
  Nitro-specific cross-tenant primitive — research-note only, not a finding on this page.
- **Co-residency / topology** surface of cluster placement groups — owned by
  `ec2-networking-attack-research-plan.md` Cluster 3.
- **Dedicated Host tenancy** surface — unowned corpus gap, deferred to a future sibling.
- **Third-party / human-facing prose links** (kernel.org, AL2 UG, the GitHub guide) — not server
  dereferenced; bugs in referenced repos are out of scope beyond the supply-chain framing of 5.1.
- No DNS/port/subdomain enumeration; HTTP/application + control-plane layer only; no destructive payloads.

---

## 8 — Null hypotheses and documentation gaps (consolidated)

| Hypothesis | Verdict | Pages / sources checked |
|---|---|---|
| Some ENA interrupt-moderation / busy-poll / C-state / MTU tuning on this page maps to an `ec2:` action or condition key | **REFUTED (CONFIRMED NULL)** — zero genuine hits; only unrelated `interrupt` homonyms | full grep of `docs/service-authorization/latest/reference/list_ec2.md` |
| `ec2:EnaSupport` is a condition key (a Deny on it would bind) | **REFUTED** — no such key; `enaSupport` is an *attribute* via generic value-blind `ec2:Attribute`, a different surface this page never touches | `list_ec2.md` |
| The page exposes a server-dereferenced URL (SSRF seam) — Lens G | **N/A** — the only outbound URLs (GitHub guide, kernel.org, AL2 UG) are human-facing prose links, never fetched by the service | full 81-line page text |
| Cross-tenant / IDOR surface — Lens A | **N/A** — no API, no object ID, no tenant id on the page | full page text |
| Role ARN / PassRole / confused deputy — Lens B | **N/A** — no role or ARN field | full page text |
| LLM / prompt-injection path — Lens K | **N/A** — no customer content fed to a model | full page text |
| Secret generation/storage — Lens T | **N/A** — no credential generated or persisted | full page text |
| JWT / OIDC token validation — Lens FF | **N/A** — no token/claims field | full page text |
| Disabling interrupt moderation is a cross-tenant / shared-fleet DoS | **REFUTED** — Nitro virtualizes ENA queues per instance; self-DoS only | `ena-improve-network-latency-linux.md`, Nitro/ENA architecture |
| Guest tunings weaken security posture | **REFUTED (bounded null)** — all neutral; `tcp_sack=0` incidentally strengthens (SACK Panic); C-state side-channel is theoretical/unbounded-here | per-tuning audit (`.cache/ena-latency-supplychain-tuning.md`) |
| The `.rst` guide is the same artifact as ENA Express's `check-ena-express-settings.sh` | **REFUTED** — different repo (`amzn/amzn-drivers` vs `amzn/amzn-ec2-ena-utilities`); distinct supply-chain lead | both GitHub repos |
| **Dedicated Host tenancy has a current corpus owner** | **DOC-GAP / CORPUS GAP** — no `*dedicated-host*`/`*host*` plan exists; defer to future sibling | `ls /work/aws-docs/*attack-research-plan.md` |

**Supporting memos (full detail):** `/work/aws-docs/.cache/ena-latency-supplychain-tuning.md`
(supply-chain + per-tuning audit) and `/work/aws-docs/.cache/ena-latency-controlplane.md`
(control-plane null + cross-ref ownership + null-lens sweep).

---

*Prepared with the `security-questionbuilder` skill, documentation-only, boundary-first. All confirmed
facts trace to the cited page/line or to the authoritative `list_ec2.md`; the plan claims no bug — it
documents a guest-config page whose only ownable surface is a low-severity supply-chain artifact and a
set of carefully-bounded nulls, with the richer co-residency/tenancy surfaces explicitly handed to their
owners. See [[reference-aws-iam-service-auth-ref-url]] and [[project-aws-research-plans]].*
