# Enhanced Networking (Amazon EC2) — Attack Research Plan

Source of leads: `enhanced-networking.html` (hub) and its subtree — `enhanced-networking-ena.html`, `enabling_enhanced_networking.html`, `ena-express.html`, `ena-express-configure.html`, `ena-express-list-view.html`, `sriov-networking.html`, `monitoring-network-performance-ena.html`, `enhanced-networking-os.html`, driver-install/troubleshoot pages. Offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`. Live docs cross-checked 2026-09-13 (hub page identical online/offline; no injected AI-agent "See also" block on the hub — contrast [[aws-docs-see-also-injection]]).
Status: documentation-derived hypotheses only; nothing tested against a live account.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane — the **Nitro network-shaping / SRD routing / credit-accounting plane** is the shared-responsibility line here — stop, preserve evidence, flag for AWS-Security disclosure.
- **This is a thin spec/index hub.** The page itself has NO API, NO IAM action, NO condition key. Real control-plane surface is inherited from the *enabling* and *ENA-Express-configure* children. Most boundary lenses are genuine nulls (§8). Do not re-scope the whole EC2 instance/ENI surface here — route those to the sibling plans referenced inline. Concentrate fire on the 5 live angles in §5.

---

## 1. Pentest Objectives (boundary-breach goals)
1. Set/clear the enhanced-networking attributes (`enaSupport`, `sriovNetSupport`, `EnaSrdSpecification`) on an instance/ENI/AMI you do **not** own, or from a principal the org intended to bound.
2. Prove that a principal granted "enable enhanced networking" (`ec2:ModifyInstanceAttribute` / `ec2:ModifyNetworkInterfaceAttribute`) can reach a **different, higher-impact attribute** on the same API (userData → root code exec) — i.e. the grant is de-facto instance takeover.
3. Prove the org **cannot** enforce a posture ("ENA Express must be off in PCI subnets", "enhanced networking must stay on") because no value-level IAM condition key exists.
4. Reach another tenant's traffic/host via the shared **SRD / ENA Express** network fabric (co-residency, cross-AZ dynamic routing) — expected mostly out-of-scope/hard-stop, but confirm the isolation claim.
5. Compromise an instance via the driver **supply chain** (root compile of `amzn-drivers` from GitHub with no signature verification).

---

## 2. Components, Assets, and Design

**What enhanced networking is.** SR-IOV device virtualization exposing a virtual function NIC directly to the guest, via two mechanisms:
- **ENA** (Elastic Network Adapter) — up to 100 Gbps; all Nitro instances + a few Xen (H1, I3, G3, m4.16xlarge, P3, P3dn, R4). Gated by the instance/AMI boolean attribute **`enaSupport`** (`enaSupport`).
- **Intel 82599 VF** — up to 10 Gbps; C3/C4/D2/I2/M4(≠16xl)/R3. Gated by attribute **`sriovNetSupport`** (`sriov-networking.html`).
- **ENA Express** — AWS **Scalable Reliable Datagram (SRD)** transport layered on ENA; single-flow bandwidth 5→25 Gbps; dynamic multi-path routing + packet reorder + retransmit in the network layer. Configured per **attachment** via **`EnaSrdSpecification` {EnaSrdEnabled, EnaSrdUdpSpecification.EnaSrdUdpEnabled}**.

**Where untrusted data / config enters (the mutating surface, from the children):**
| Mechanism | API | Attribute / field | Where set |
|---|---|---|---|
| Enable ENA on instance | `ModifyInstanceAttribute` | `enaSupport` (bool) | `enabling_enhanced_networking.html` |
| Enable Intel VF on instance | `ModifyInstanceAttribute` | `sriovNetSupport` = `simple` | `sriov-networking.html` |
| Bake ENA into AMI | `RegisterImage` | `--ena-support` / `--sriov-net-support` | `enabling_enhanced_networking.html` |
| Configure ENA Express on attach | `AttachNetworkInterface` | `EnaSrdSpecification` | `ena-express-configure.html` |
| Configure ENA Express on live ENI attachment | `ModifyNetworkInterfaceAttribute` | `EnaSrdSpecification` | `ena-express-configure.html` |
| Read settings | `DescribeInstances` / `DescribeImages` / `DescribeNetworkInterfaces` | `enaSupport` / `EnaSrdEnabled` | list-view / test pages |
| In-guest driver | (no API) `git clone amzn-drivers`, compile as root, `depmod`, `dracut`, grub edit | — | `enabling_enhanced_networking.html` |

**Ownership / trust zones.**
- **Customer account** owns the instance, the ENI, the AMI, and the in-guest OS/driver. These are all customer resources — no AWS multi-tenant fleet sits in the data path (contrast managed-DB services).
- **AWS service plane** owns the SR-IOV virtual-function backing, the Nitro card that shapes traffic, and the **SRD routing fabric** that spreads a flow "across different AWS network paths." This is the hard-stop line.

**ASCII (control + data):**
```
 caller (IAM principal)
   │  ec2:ModifyInstanceAttribute {enaSupport|sriovNetSupport|userData|...}
   │  ec2:ModifyNetworkInterfaceAttribute {EnaSrdSpecification}
   ▼
 [EC2 control plane] ──sets attribute──► instance / ENI-attachment / AMI (CUSTOMER-owned)
                                              │
 guest OS ── ena/ixgbevf driver ──► SR-IOV VF ──► [Nitro card: shaping, credits] ──► [SRD fabric: multi-path route]  ◄── HARD STOP
                                                                                          │
                                                              peer EC2 instance (same/other AZ, same Region)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv IAM principal "may enable enhanced networking" | Same instance's **other** attributes | `ModifyInstanceAttribute` is one API for ~20 attributes incl. `userData` | Setting `userData` (or `instanceInitiatedShutdownBehavior`, `disableApiTermination`) through the grant meant only for `enaSupport` → next-boot root code exec = breach |
| IAM principal in acct A | Instance/ENI/AMI in acct B | resource id in request | `ModifyInstanceAttribute`/`ModifyNetworkInterfaceAttribute`/`RegisterImage` accepting a foreign id (expect NOT — id ownership-bound) |
| Org security admin (intent) | Enforce ENA/SRD posture | IAM condition key on the attribute *value* | No `ec2:EnaSupport`/`ec2:EnaSrdSupported` value key exists → posture unenforceable = governance breach (Lens S/U) |
| Customer instance on shared SRD fabric | Another tenant's flow/host | SRD dynamic multi-path routing across "different AWS network paths" | Any packet/read of another tenant's SRD traffic = **HARD STOP** service-plane breach |
| In-guest root (customer) | Instance integrity | `git clone` amzn-drivers → compile → load kernel module | A tampered/MITM'd driver source loaded as a kernel module (TOFU, no signature) |
| Instance A operator | Attachment lifecycle | `EnaSrd` "applies to the attachment; gone on detach/terminate" | A stale/re-created ENI inheriting or dropping SRD unexpectedly (state confusion) |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Ext-facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ModifyInstanceAttribute` | POST (Query) | **Yes** | Yes | set `enaSupport` / `sriovNetSupport` (+ userData, +18 others) | Yes | any IAM principal w/ the action | ⭐ multi-attribute workhorse; `ec2:Attribute` case-fail-open variant applies |
| `ModifyNetworkInterfaceAttribute` | POST | **Yes** | Yes | set `EnaSrdSpecification` on live ENI attachment | Yes | principal w/ action + ENI | ENA Express |
| `AttachNetworkInterface` | POST | **Yes** | Yes | attach ENI w/ `EnaSrdSpecification` | Yes | principal w/ action | cross-VPC scoping caveats → route to [[using-eni-plan]] |
| `RegisterImage` | POST | **Yes** | Yes | `--ena-support`/`--sriov-net-support` bakes attribute into AMI | Yes | principal w/ action | supply-chain into launched fleet → [[s3-backed-ami-plan]] / [[copying-amis-plan]] |
| `DescribeInstances` / `DescribeImages` / `DescribeNetworkInterfaces` | GET | No | Yes | read `enaSupport` / `EnaSrdEnabled` | Yes | principal w/ action | enumeration / posture-observability |

No `[NEW]` markers on the hub. No non-SDK/hidden endpoints on these pages. No AWS-managed policy, CFN, or SLR JSON printed anywhere in the subtree → Lens R does not fire on printed artifacts (but see §5 Area A cross-reference).

---

## 5. Recommended Areas of Focus (one block per firing lens)

### Area A — ⭐ `ModifyInstanceAttribute` is a de-facto instance-takeover grant (Lens B/E + variant, Lens X)
**Background.** The docs instruct the operator to enable ENA with a single call: `aws ec2 modify-instance-attribute --instance-id i-… --ena-support`. But `ModifyInstanceAttribute` is a *single API that mutates ~20 distinct instance attributes* — including `userData`, `instanceInitiatedShutdownBehavior`, `disableApiTermination`, `kernel`, `blockDeviceMapping`. IAM authorizes the **action**, not the **attribute**.
**Security Concern.** An org that grants `ec2:ModifyInstanceAttribute` so a team can "turn on enhanced networking" has almost certainly granted the ability to rewrite `userData`. On the next stop/start, `userData` runs as **root/SYSTEM** → full instance compromise. This is the confirmed corpus exemplar ([[launch-instances-plan]], memory: "non-PassRole actions that reach a role's live credentials"). The enhanced-networking runbook is a *plausible business reason* an over-broad `ModifyInstanceAttribute` grant exists.
**High-level Test Scenarios (falsifiable):**
- Claim: a role holding `ec2:ModifyInstanceAttribute` with no `ec2:Attribute` condition can set `userData` on the same instance it was meant to only `enaSupport`. → Oracle: `iam:SimulatePrincipalPolicy` for `ModifyInstanceAttribute` first (no resource touched); then, with a canary instance, set `userData` and confirm the base64 blob is stored via `DescribeInstanceAttribute --attribute userData`.
- Claim: an `ec2:Attribute`-scoped deny (`ec2:Attribute StringEquals userData`) is **inert / fails open** because the request field is PascalCase / the key is case-sensitive (documented variant, [[stop-start-plan]] / [[terminating-instances-plan]]). → Oracle: author a scoped role that Allows `ModifyInstanceAttribute` but Denies when `ec2:Attribute` = `userData`; attempt to set userData with varying case; a 200 proves fail-open.
**Doc evidence:** `enabling_enhanced_networking.html` (the `--ena-support` runbook). **Severity-if-true:** intra-account non-admin → root-on-instance = High (customer footgun, unless the enabling grant is in an AWS-authored artifact — none printed here, so route as least-priv guidance, not aws-security).
**Stop condition:** proven on one canary instance; do not iterate across instances.

### Area B — ⭐ No value-level IAM condition key governs the enhanced-networking attributes (Lens S / Lens U)
**Background.** Enhanced networking, Intel VF, and ENA Express are all boolean/enum *attribute values* (`enaSupport`, `sriovNetSupport=simple`, `EnaSrdEnabled`, `EnaSrdUdpEnabled`). The only documented IAM lever is the *action* (`ModifyInstanceAttribute`/`ModifyNetworkInterfaceAttribute`) plus the coarse `ec2:Attribute` key (attribute *name*, not value).
**Security Concern.** An org cannot write a policy that says "ENA Express (SRD) must be **off** on interfaces in a regulated subnet" or "enhanced networking must not be **disabled** on hardened AMIs," because there is no `ec2:EnaSupport` / `ec2:EnaSrdSupported` / `ec2:SriovNetSupport` **value** condition key. Same systemic gap as [[network-bandwidth-plan]], [[burstable-unlimited-mode-plan]], [[instance-optimize-cpu-plan]] (no CpuCredits/CoreCount value key), [[dedicated-hosts-maintenance-plan]]. Disabling `enaSupport` can also be a resilience/DoS lever: the docs warn enabling/disabling it "might render incompatible instances or operating systems unreachable."
**High-level Test Scenarios:**
- Claim: no IAM condition key exists to constrain the *value* of any enhanced-networking attribute. → Oracle: enumerate EC2 condition keys in the live Service Authorization Reference for `ModifyInstanceAttribute` / `ModifyNetworkInterfaceAttribute`; confirm only `ec2:Attribute` (name) is present, no value key. **Doc-gap: confirm at hunt time** (Service Authorization Reference fetch was inconclusive in this pass).
- Claim: `ec2:Attribute` cannot distinguish `EnaSrdSpecification` because ENA Express is set via `ModifyNetworkInterfaceAttribute`, whose attribute-key coverage differs. → Oracle: diff the condition-key set of the two APIs.
- Claim: toggling `enaSupport` off is a documented reachability/DoS lever with no fine-grained guard. → Oracle: doc-confirmed ("might render … unreachable"); severity = self-inflicted single-tenant (Low) unless a low-priv principal can do it to a shared/critical instance (then it's the Area A grant problem).
**Doc evidence:** `ena-express-configure.html`, `enhanced-networking-ena.html` (reachability warning). **Severity-if-true:** governance/enforceability gap = Informational–Low on its own; becomes the enabler for Area A. AWS-owned (the missing key), worth filing as Lens U.

### Area C — ENA Express / SRD shared-fabric isolation (Lens V / Lens L) — mostly HARD STOP, confirm the claim
**Background.** SRD "distributes packets for each network flow across **different AWS network paths**," dynamically reroutes on congestion, and reorders/retransmits in the network layer. This is a shared, AWS-owned transport fabric spanning AZs within a Region.
**Security Concern.** (1) Cross-tenant reach: can one tenant's SRD flow observe/inject into another's on the shared fabric, or use SRD path-probing as a co-residency/topology oracle? (2) Noisy-neighbour: single-flow burst 5→25 Gbps "up to the aggregate instance limit" on shared paths — can a tenant degrade a co-resident's SRD performance? (overlaps [[network-bandwidth-plan]] shared-burst-pool question and [[instance-topology-plan]] co-residency oracle).
**High-level Test Scenarios:**
- Claim: SRD provides no cross-tenant traffic isolation guarantee beyond standard VPC. → Oracle: **documentation-only for the isolation claim; any live packet-level cross-tenant test is HARD STOP** the moment it touches the SRD/Nitro plane. Confirm only whether the docs *assert* isolation (they do not explicitly) → mark as a doc-gap, route co-residency inference to [[instance-topology-plan]].
- Claim: SRD dynamic-routing timing is a covert/side channel for path or co-residency inference. → Oracle: theoretical; out-of-scope for active testing (Nitro plane).
**Doc evidence:** `ena-express.html` "How ENA Express works." **Severity-if-true:** cross-tenant on shared fabric = Critical **but hard-stop / AWS service plane** — do not weaponize; observe-and-flag only.

### Area D — Driver supply chain: root compile of `amzn-drivers` with no integrity check (Lens Q/F variant — supply chain, in-guest)
**Background.** For non-Amazon-Linux/Ubuntu distros, the runbook is: `git clone https://github.com/amzn/amzn-drivers`, compile, install the `ena` kernel module, `depmod`, rebuild `initramfs` (`dracut -f`), edit grub. All as root, in-guest.
**Security Concern.** TOFU: no signature/hash verification of the cloned source or the resulting kernel module is documented. A MITM on the clone, a compromised mirror, or a poisoned fork loaded by a copy-paste operator yields a **kernel-mode** implant. In-guest, customer-side — but AWS's runbook omits any integrity step (contrast a signed package). Similar shape to [[ec2rescue-linux-plan]] / [[ec2winutil-troubleshooting-plan]] TOFU supply chains.
**High-level Test Scenarios:**
- Claim: the documented driver-install flow has no integrity verification. → Oracle: doc review confirms (no gpg/sha step). Reportable as an insecure AWS-published runbook (Lens R variant — "AWS-published sample code insecure defaults"), Informational–Low (customer-executed, in-guest).
**Doc evidence:** `enabling_enhanced_networking.html` "RHEL, SUSE, CentOS" procedure. **Severity-if-true:** Low (documentation hardening), not a service-plane bug.

### Area E — Silent ENA-Express fallback & shaping/microburst monitoring blind spot (Lens U + Lens O)
**Background.** ENA Express "detects if ENA Express is operating on **both**" instances; on any mismatch (config, instance type, middleware box, cross-Region) "communication falls back to standard ENA transmission" — **silently**. Separately, the monitoring page states AWS shapes over-limit traffic by "queueing and then dropping packets," surfaced only via ENA driver metrics (CloudWatch import requires the CW agent + driver ≥2.2.10).
**Security Concern.** (1) Doc-vs-enforcement: an operator (or a compliance control) that *assumes* SRD/ENA-Express is active — e.g. for a latency SLA or a "traffic stays on SRD" assumption — has no hard signal it fell back to plain ENA. (2) Audit/evasion: microburst shaping/drops increment driver counters but not necessarily flat CloudWatch instance metrics → a blind spot that masks a saturation/DoS event (evasion enabler, per [[network-bandwidth-plan]]).
**High-level Test Scenarios:**
- Claim: ENA Express fallback is unobservable without polling `EnaSrdEnabled` + driver metrics. → Oracle: `DescribeNetworkInterfaces` shows the *config* bit but not the *live operating* state; confirm the gap. Informational.
- Claim: shaping drops during a microburst are invisible in default CloudWatch. → Oracle: doc-confirmed reliance on ENA driver counters. Informational (enabler).
**Doc evidence:** `ena-express.html` (fallback), `monitoring-network-performance-ena.html` (shaping). **Severity-if-true:** Informational.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| `ModifyInstanceAttribute` grant → userData root exec | EC2 control plane | IAM action-only authz; `ec2:Attribute` (name) key — test case-fail-open |
| Foreign instance/ENI/AMI attribute mutation (IDOR) | ModifyInstanceAttribute / ModifyNetworkInterfaceAttribute / RegisterImage | resource-id ownership binding (expected to hold) |
| Org cannot enforce ENA/SRD posture | IAM condition keys | (none exists — the gap under test) |
| Cross-tenant SRD traffic reach / co-residency oracle | SRD fabric | VPC isolation + Nitro (HARD STOP for active tests) |
| Poisoned driver kernel module | in-guest install runbook | none documented (TOFU) |
| Silent ENA-Express fallback / shaping blind spot | ENA Express + monitoring | driver metrics only (observability gap) |

---

## 7. Out-of-Scope Risk Categories
- **Nitro network-shaping, SRD routing fabric, credit-accounting plane** — AWS service plane; observe-and-flag only, never weaponize.
- Cross-tenant packet capture / injection on the SRD or SR-IOV fabric — hard stop.
- Single-tenant self-DoS (disabling `enaSupport` bricks your own instance; saturating your own bandwidth).
- In-guest OS/driver bugs a customer inflicts on their own instance (the RSS/`Set-NetAdapterRss` tuning, MTU, TCP-chimney config on `enhanced-networking-os.html`) — customer-owned config, not a boundary.
- Generic instance/ENI/AMI IDOR and cross-VPC ENI attach — covered by [[using-eni-plan]], [[prefix-eni-plan]], and the AMI plans; do not re-derive here.
- IMDS on managed hosts; DNS rebinding against private-only endpoints.

## 8. Null hypotheses / doc gaps
- **Lens A (IDOR):** `ModifyInstanceAttribute`/`ModifyNetworkInterfaceAttribute`/`RegisterImage` take an instance/ENI/AMI id that is expected ownership-bound (EC2 resource ids carry account binding). Null unless a validator-divergence twin surfaces — cross-reference [[copying-amis-plan]] existence-vs-ownership work. Checked: enabling + ena-express-configure pages.
- **Lens B/C (PassRole/credential vending):** no role ARN, no `PassRole`, no STS/session-scope field anywhere in the subtree. Null. (The privesc angle in Area A is *action-family reach*, not PassRole.) Checked: all children.
- **Lens G (SSRF):** no field the service dereferences server-side (the `git clone` URL is executed *in the guest by the customer*, not fetched by AWS). Null. Checked: enabling, ena-express, monitoring pages.
- **Lens H/W (KMS/attestation):** none. Null.
- **Lens J (OAuth/3P):** none. Null.
- **Lens R/S (printed IAM artifact):** NO AWS-managed policy, CFN, or SLR JSON printed in the subtree → no artifact to audit statement-by-statement. Lens S fires only as the *absence*-of-condition-key finding in Area B. Checked: all children (grep for `arn:aws:iam`, `AWS::IAM`, "managed policy" — none).
- **Lens Y (transport/sig):** the `git clone` is over HTTPS but unverified (Area D); no `http://` service endpoint, no SigV2 surface on these pages. Partial → folded into Area D.
- **Lens AA (share/revoke):** `RegisterImage --ena-support` propagates the attribute into an AMI that may later be shared — but share/revoke lifecycle belongs to [[sharing-amis-plan]]; here only note the attribute *inherits* into the AMI. Near-null.
- **Doc-gap — CONFIRM AT HUNT TIME:** exact EC2 IAM condition-key set for `ModifyInstanceAttribute` / `ModifyNetworkInterfaceAttribute` (Area B). Live Service Authorization Reference fetch was inconclusive in this documentation pass; the hunter must resolve it before rating Area B. Prior corpus strongly implies only `ec2:Attribute` (name) exists and no value key — treat as an open lead, not a closed null.
- **Doc-gap — SRD cross-tenant isolation** (Area C): the docs never state SRD's tenant-isolation model → confirm-surface-first, and only via documentation / topology inference, never active fabric testing.

---

### Priority order for the hunter
1. **Area A** (ModifyInstanceAttribute → userData privesc; case-fail-open) — highest concrete impact, live-confirmable with a scoped role + canary.
2. **Area B** (no value-level condition key) — cheap live confirm via Service Authorization Reference; enables Area A.
3. **Area D** (driver TOFU supply chain) — documentation finding, quick.
4. **Area E** (fallback / monitoring blind spot) — Informational enabler.
5. **Area C** (SRD shared fabric) — documentation/inference only; hard-stop on any active fabric test.
