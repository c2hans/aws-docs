# Attack / Research Plan — Enhanced networking with the Intel 82599 VF interface (`sriov-networking.html`)

> **Skill:** `security-questionbuilder` (6-step boundary-first method). **Target:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sriov-networking.html` (offline twin `docs/AWSEC2/latest/UserGuide/sriov-networking.md`, 460 lines). **Status:** documentation-derived hypotheses only; nothing tested against a live account. **Drift:** offline == online **byte-identical** re-verified 2026-10-15 (typo L290, persistent-net L309, SourceForge/2.16.4 L242/244, no-disable L128, AMI-inherits L181/307/449, EC2Launch password reset L356, kernel-upgrade revert L248). IAM facts confirmed against `docs/service-authorization/latest/reference/list_ec2.md` (ModifyInstanceAttribute `instance*` L8808; RegisterImage `image*`/`snapshot` L9319; ResetInstanceAttribute L9516; DescribeInstanceAttribute L6924).

---

## §0 — Scope note / relationship to sibling plans (read first)

This page is a **thin, legacy, guest-OS-configuration page** for the *Intel 82599 Virtual Function* (`ixgbevf`) enhanced-networking path on **Xen-based** instance families (C3, C4, D2, I2, M4-non-16xl, R3). Its control-plane surface is **three EC2 actions** — `ModifyInstanceAttribute --sriov-net-support`, `RegisterImage --sriov-net-support`, and the `DescribeInstanceAttribute`/`DescribeImages` read verification — plus guest-side driver install.

**This surface is already substantially OWNED by two sibling plans. This plan is a page-level COMPLEMENT, not a restatement:**

- **`enhanced-networking-attack-research-plan.md`** (the hub) **OWNS** the primary mechanisms and must be read as the authority for:
  - **Area 4** — `ec2:Attribute`/`ec2:Attribute/${AttributeName}` casing fail-open on `ModifyInstanceAttribute` (`instance*` L8808). The sub-attribute Deny that fails open (`userData` lowercase-vs-PascalCase) → privesc. **Do not re-derive here.**
  - **Area 5** — the `RegisterImage` **unguarded twin** (zero `ec2:Attribute` on `image*`/`snapshot`, L9319); `ModifyImageAttribute` enum = `description|imdsSupport|launchPermission` (excludes `sriovNetSupport` — `API_ModifyImageAttribute.md` L14/L23 confirms inheritance/RegisterImage is the ONLY AMI path); the **irreversible-enable bricking** primitive against a stopped victim; the read-oracle via `DescribeInstanceAttribute` (no `ec2:Attribute` key, L6924) returning `userData`.
- **`enabling-enhanced-networking-attack-research-plan.md`** OWNS the **instance-store fork** framing (RegisterImage is the *only* enable path for instance-store roots) and the **no-`ec2:InstanceState` key** gap (the "must be STOPPED" precondition is not IAM-expressible).
- **`troubleshooting-ena-attack-research-plan.md`** OWNS the `enaSupport`/`ResetInstanceAttribute`-can't-reset / iam-policies casing-contradiction baseline.

**What THIS plan uniquely owns** (net-new, SR-IOV-page-specific, not covered by the siblings — see §4):
1. **Driver-image supply chain is distinct from ENA's** — SR-IOV instructs **SourceForge** (`ixgbevf`, Linux) and **Intel.com** (Windows, `pnputil` INF-install), not GitHub. (Lens Q)
2. **The `70-persistent-net.rules` stale-MAC AMI boot footgun** (L309) — a derived-AMI availability hazard **present only in this page's "Other Linux" procedure**.
3. **The kernel-upgrade silent driver-revert** (L248) — rebuilding/upgrading the kernel can silently revert to the distro `ixgbevf` and brick the box at next reboot.
4. **A confirmed doc-integrity defect** — the `--sriov-net-support` long-flag is split across a mis-placed line-continuation in the "Other Linux" `modify-instance-attribute` sample (L290). (Lens U doc-integrity)
5. **The SR-IOV irreversibility is confirmed in THREE places** and is a *stronger* hazard than `enaSupport` (which is reversible). This plan sharpens the hub's Area 5 with the Xen/PV-specific "unreachable" framing.

ResetInstanceAttribute (L9516) carries **no `ec2:Attribute` key** and its resettable set is `kernel|ramdisk|sourceDestCheck` only → **`sriovNetSupport` cannot be reset** — confirms the hub's "no undo" from the IAM side as well as the API side.

---

## §1 — Components, Assets, and Design

**Customer-facing interface.** EC2 control-plane APIs (SigV4) only — the page states twice (`ixgbevf-requirements`, hub): *"Enhanced networking cannot be managed from the Amazon EC2 console."* Guest-side configuration happens over the customer's own SSH/RDP session.

**Assets.**
- **Instance attribute `sriovNetSupport`** — value `simple` when enabled; **one-way** (no disable API). Set via `ModifyInstanceAttribute` (requires STOPPED for EBS-backed) or inherited at launch from the AMI.
- **AMI attribute `sriovNetSupport`** — set via `RegisterImage --sriov-net-support simple`, or inherited when an AMI is created from an instance that has it. **Propagates to every instance launched from the AMI** ("enabled by default").
- **Guest driver artifacts** — `ixgbevf` kernel module (Linux, from SourceForge, compiled in-guest) / Intel 82599 VF NDIS driver (Windows, from Intel.com, `pnputil`-installed). `initramfs`/`dracut`, GRUB (`net.ifnames=0`), `/etc/udev/rules.d/70-persistent-net.rules`.
- **Windows local administrator password** — reset as a side effect of the EC2Launch `InitializeInstance.ps1 -Schedule` step the page instructs (L356).

**Identity / ownership.** All three actions are same-account EC2 resource ops. There is **no cross-tenant data plane** on this page — SR-IOV is a NIC-passthrough performance feature; a VF is bound to one instance. Cross-tenant IDOR (Lens A) is a **null hypothesis** here (see §6).

**Design pipeline (guest-config, not a service pipeline):**
```
 operator SSH/RDP ─► guest OS ─► download driver (SourceForge / Intel.com, HTTP)
                                    │
                                    ▼  compile+install ixgbevf / pnputil INF
                              initramfs + GRUB net.ifnames=0 + depmod
                                    │
 operator local shell ─► StopInstances ─► ModifyInstanceAttribute --sriov-net-support simple  (ONE-WAY)
                                    │                           └─(or)─► RegisterImage --sriov-net-support simple  (AMI, zero ec2:Attribute key)
                                    ▼
                              StartInstances ─► (if PV / incompatible kernel) UNREACHABLE, no undo
```

---

## §2 — Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Cross-team principal w/ broad `ModifyInstanceAttribute` + `Stop/StartInstances` | Victim team's **stopped** instance (same account) | `--sriov-net-support simple` (one-way) | Instance's `sriovNetSupport` flips to `simple` **irreversibly**; a PV/incompatible instance is unreachable on next boot — an availability change the victim's admin cannot undo and did not consent to. |
| Principal w/ `ec2:RegisterImage` but denied `ModifyInstanceAttribute` | AMI `sriovNetSupport` | `register-image --sriov-net-support simple` | AMI carries `simple` though a Deny was keyed on the Modify path — `image*` row has **no `ec2:Attribute` key** (L9319). Propagates to every downstream instance. *(mechanism owned by hub Area 5 — cross-ref)* |
| Principal w/ "read ENA state" grant (`ec2:DescribeInstanceAttribute`) | Victim instance `userData` | `describe-instance-attribute --attribute userData` | Base64 userData (bootstrap secrets) returned by a grant that cannot be scoped to `sriovNetSupport` — no `ec2:Attribute` key on the read path (L6924). *(owned by hub Area; cross-ref)* |
| In-guest operator following the page | SourceForge / Intel.com over the network | HTTP(S) download of a kernel module / NDIS driver that is then compiled+loaded as root | A tampered/MITM'd `ixgbevf` tarball or Intel ZIP executes in-kernel / in-driver-store. **No checksum, no signature pin, no pinned URL** in the page. *(net-new — §4 Area A)* |
| AMI builder following "Other Linux" | Every instance launched from the derived AMI | AMI created with stale `/etc/udev/rules.d/70-persistent-net.rules` | Derived instances fail to find `eth0` → boot issues (self-inflicted DoS baked into a shared/published AMI). *(net-new — §4 Area B)* |

**Canonical boundaries present:** intra-account cross-team (irreversible attribute / RegisterImage bake-in). **Absent:** customer↔service-account, data↔control plane, credential-vending — none appear on this page.

---

## §3 — API / interface surface

| Name | Mutating | Ext-facing | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|
| `ModifyInstanceAttribute` (`--sriov-net-support simple`) | yes | yes | set instance `sriovNetSupport` | instance holder | `instance*` row (L8808) has `ec2:Attribute`/`ec2:Attribute/${AttributeName}` + many instance keys; **casing fail-open = hub Area 4**. EBS-backed requires STOPPED; **no `ec2:InstanceState` key** (= enabling-ENA plan). `sriovNetSupport` **NOT** reversible. |
| `RegisterImage` (`--sriov-net-support simple`) | yes | yes | set AMI `sriovNetSupport` | image owner / grantee | `image*` keys = `aws:RequestTag`,`aws:TagKeys`,`ec2:ImageID`,`ec2:Owner`,`ec2:Region`; **no `ec2:Attribute`** (L9319). **Only** AMI enable path (ModifyImageAttribute enum excludes it). Bake-in gap = hub Area 5. |
| `ModifyImageAttribute` | yes | yes | — | image owner | enum `description\|imdsSupport\|launchPermission` — **cannot** set `sriovNetSupport` (`API_ModifyImageAttribute.md` L14/L23). Its `ec2:Attribute` keys are structurally irrelevant to enhanced networking. |
| `ResetInstanceAttribute` | yes | yes | reset instance attr to default | instance holder | **no `ec2:Attribute` key** (L9516); resettable set = `kernel\|ramdisk\|sourceDestCheck`. **Cannot reset `sriovNetSupport`** → confirms no IAM-side undo. |
| `DescribeInstanceAttribute` (`--attribute sriovNetSupport`) | no | yes | read instance attr | instance holder | **no `ec2:Attribute` key** (L6924) → cannot be scoped to one attribute; `--attribute userData` works identically = read oracle (hub Area). |
| `DescribeImages` (`--query Images[].SriovNetSupport`) | no | yes | read AMI attr | per image visibility | bulk read; standard. |

**Doc-flagged focus sentence (verbatim, L128):** *"There is no way to disable the enhanced networking attribute after you've enabled it."* — the lead AWS plants on this page.

---

## §4 — Boundary-lens catalog (net-new leads this page owns)

### Area A — Driver supply chain: SourceForge (`ixgbevf`) + Intel.com (Windows), unpinned, in-kernel/driver-store (Lens Q)
**Background.** For "Other Linux", the page (L242) instructs: *"Download the source for the `ixgbevf` module on your instance from Sourceforge at `https://sourceforge.net/projects/e1000/files/ixgbevf%20stable/`"*, then *compile and install* it as a kernel module (L246), run `depmod`, rebuild `initramfs`. For Windows (L340-end), it links **six Intel.com download pages** per Server version and instructs `pnputil -i -a …\vxn6Xx64.inf` to add the driver to the **driver store** (and for 2008 R2, rename `PROWinx64Legacy.exe`→`.zip`, extract, `pnputil -a …vxn62x64.inf`).

**Security Concern (net-new — distinct from the hub's GitHub-ENA framing).** This is a **documented instruction to fetch third-party code and load it into the kernel / Windows driver store** with:
- **no checksum, no GPG/Authenticode signature verification step, no pinned version/URL** printed on the page;
- a plaintext-capable mirror (SourceForge project files redirect through arbitrary mirror hosts) → classic MITM / mirror-compromise seam;
- a **version-fragility trap** the page itself flags (L244): *"Versions of `ixgbevf` earlier than 2.16.4, including version 2.14.2, do not build properly…"* — operators under build pressure may grab an arbitrary "newer" tarball from a look-alike link.
- *Claim:* the page's driver-acquisition flow has no integrity control, so a MITM/typosquat/mirror-compromise of the SourceForge tarball or the Intel ZIP yields root-in-kernel / SYSTEM-in-driver-store on the following instances. → *Oracle:* static — show the page prescribes download→compile/`pnputil`→load with zero verify step; demonstrate the SourceForge files endpoint serves over mirrors without a published hash. (Threat-model/doc lead; **no live download**.)
- **Severity-if-true:** High *if* an operator network is interposable (supply-chain RCE in guest), but this is a **customer-responsibility hardening gap in AWS guidance**, not an AWS service defect — frame accordingly.

### Area B — `70-persistent-net.rules` stale-MAC → derived-AMI boot DoS (Lens U, availability; net-new)
**Background (L309, "Other Linux" only).** *"If your instance operating system contains an `/etc/udev/rules.d/70-persistent-net.rules` file, you must delete it before creating the AMI. This file contains the MAC address … If another instance boots with this file, the operating system will be unable to find the device and `eth0` might fail, causing boot issues."*

**Security Concern.** A **manual, easily-skipped** pre-AMI cleanup step whose omission bakes a **boot-breaking artifact** into the AMI. If that AMI is then **shared or published** (RAM / `launchPermission` / Marketplace), every launcher inherits a NIC that fails to come up — a propagating availability footgun, and a plausible **griefing/sabotage** vector for an insider who bakes a "golden" image with the rules file left in on purpose.
- *Claim:* an AMI created from an SR-IOV-enabled "Other Linux" instance without deleting `70-persistent-net.rules` produces instances whose `eth0` fails at boot. → *Oracle:* owned canary — build such an AMI, launch, observe `eth0` failure / no network; **owned resources only, do not publish.**
- **Severity-if-true:** Medium (shared/published-AMI availability; insider sabotage framing). Net-new; not in any sibling plan.

### Area C — Kernel-upgrade silent driver-revert → unreachable (Lens AA irreversible-state-adjacent; net-new)
**Background (L248, Warning).** *"If you compile the `ixgbevf` module for your current kernel and then upgrade your kernel without rebuilding the driver … your system might revert to the distribution-specific `ixgbevf` module at the next reboot. This could make your system unreachable if the distribution-specific version is incompatible with enhanced networking."*

**Security Concern.** This couples **routine patching** (a `yum update`/`apt upgrade` an automated patch pipeline runs unattended) with an **unreachability outcome on an instance whose `sriovNetSupport` is one-way-enabled**. The irreversibility (Area D) means the only exits are a compatible rebuild (needs console/serial access) or restore-from-AMI. A principal who merely enables `sriovNetSupport` and then lets normal patching proceed can leave a victim stranded — the DoS "arms" at enable-time and "fires" on an unrelated later reboot.
- *Claim:* an SR-IOV-enabled instance with a self-compiled `ixgbevf` becomes unreachable after a kernel upgrade that is not accompanied by a driver rebuild. → *Oracle:* owned canary — compile driver, `yum update` kernel, reboot, observe reversion+unreachability. **Destructive; owned canary only.**
- **Severity-if-true:** Medium (latent availability landmine; compounds Area D).

### Area D — SR-IOV irreversibility is strictly worse than `enaSupport` (sharpens hub Area 5)
**Background.** `sriovNetSupport` has **no disable path at all**, confirmed in THREE independent docs: `sriov-networking.md` L128; `API_ModifyInstanceAttribute.md` L96; `API_RegisterImage.md` L113. Unlike `enaSupport` (reversible via `--no-ena-support`), there is no API, no `ResetInstanceAttribute` enum entry (L9516), and no state-aware condition key ("allow enabling once, never re-trigger"). The Xen/PV legacy base makes the "unreachable" outcome far more likely than on modern Nitro ENA instances (L112 Warning; L457 Troubleshooting: *"If you enable enhanced networking for a PV instance or AMI, this can make your instance unreachable."*).

**Security Concern.** One low-privilege-sounding call (`modify-instance-attribute --sriov-net-support simple`) against a **stopped** victim is **permanent and unrepairable via API**, gated only by ownership-style keys (`ec2:InstanceID`/tag) — **no value-level key** can express "may set simple but not here." The AMI twin (`RegisterImage`, Area 5) has **broader blast radius** and bypasses any Modify-path Deny. This plan **defers the full mechanism to hub Area 5**; it owns the **Xen/PV-legacy "unreachable" amplification + the three-source irreversibility confirmation**.
- **Severity-if-true:** Medium–High (intra-account cross-team DoS; irreversible). Cross-ref hub Area 5 oracle (owned-canary destructive test).

### Area E — Windows EC2Launch admin-password reset side effect (Lens O / operational; cross-ref hub)
**Background (L356).** The page instructs running `InitializeInstance.ps1 -Schedule`, then warns: *"The administrator password will reset when you enable the initialize instance EC2 Launch script. You can modify the configuration file to disable the administrator password reset…"*

**Security Concern.** A page about *network tuning* instructs a step that **rotates the local administrator credential** as a side effect — an operator following it verbatim can lock out existing admin access / invalidate stored creds, and the opt-out is a buried config edit. Owned/flagged by hub supply-chain area; recorded here for page-completeness.
- **Severity-if-true:** Low–Medium (operational lockout / credential-handling surprise).

### Area F — Doc-integrity defect: split `--sriov-net-support` flag in "Other Linux" sample (Lens U doc-integrity)
**Background (L290).** The "Other Linux" `modify-instance-attribute` sample has a **mis-placed line continuation**:
```
aws ec2 modify-instance-attribute \
    --instance-id {{i-1234567890abcdef0}} -\
    -sriov-net-support simple
```
The Amazon Linux (L167) and Windows (L436) samples are correct (`… \` then `--sriov-net-support simple`). Here the `--` is broken as `-\`+`-sriov…`.

**Security Concern.** Functionally the backslash-newline re-joins to `--sriov-net-support` so a verbatim paste still works, but it is a **confirmed copy-editing defect in a security-relevant, one-way command**, and any reader who "fixes" the odd `-\` by hand can produce `-sriov-net-support` (single dash → unknown-option error) or mis-split. Low-severity doc-integrity marker; useful as a **freshness/ья canary** for future drift checks.
- **Severity-if-true:** Low (doc hygiene).

---

## §5 — Prioritization (NEW / changed surface)

1. **Area D (SR-IOV irreversible bricking, Xen/PV)** — highest intra-account impact; cross-ref hub Area 5 for the full IAM-unscopability + RegisterImage twin. **Confirm first** whether any state-aware/value-level key exists (it does not, per L8808 enumeration) — this is the load-bearing claim.
2. **Area C (kernel-upgrade silent revert)** — latent, arms-at-enable/fires-later DoS; compounds Area D.
3. **Area A (SourceForge/Intel supply chain)** — High-if-interposable but customer-responsibility; frame as AWS-guidance hardening gap.
4. **Area B (persistent-net stale-MAC AMI)** — shared/published-AMI availability + insider-sabotage.
5. **Area E / Area F** — operational / doc-integrity completeness.

**Fire concentration:** the net-new value of this page over the hub is Areas A–C (guest-OS/supply-chain/patching hazards the hub's control-plane-centric Areas 4–5 do not cover) + the Xen/PV amplification of the irreversibility. Everything control-plane (casing, RegisterImage twin, read oracle, no-InstanceState-key) is **already owned** — a hunter should execute those from the hub/enabling plans, not re-open them here.

---

## §6 — Explicit null hypotheses (pages checked)

- **Lens A (cross-tenant IDOR): NULL** — read `sriov-networking.md` in full (460 L) + hub `enhanced-networking.md`. SR-IOV is a single-instance NIC-passthrough performance attribute; no API returns another tenant's `sriovNetSupport` and no shared-fleet VF handoff is documented. (Matches hub Lens A null.)
- **Lens B/C (PassRole / credential vending): NULL** — no role-ARN/token/credential input anywhere on the page.
- **Lens D (data→control escape): NULL** — no control ENI / host-service / storage-plane surface; guest-only + SigV4 control APIs.
- **Lens EE (AMI trust confusion on `sriovNetSupport`): REFUTED** (inherited from hub subagent-2) — enhanced-networking state is a functional/perf attribute, not a trust signal; no `RunInstances` consumer makes a security decision on it. Worst case = degraded perf / unreachability (= Area D).
- **Lens F (injection): NULL** — no customer-input-to-downstream-language transform on this page.

---

## §7 — Confirm items / open questions for the hunter

1. **(load-bearing, Area D)** Confirm via `iam:SimulateCustomPolicy` that no condition key on `ModifyInstanceAttribute`/`instance*` can distinguish "set `sriovNetSupport=simple`" from any other attribute write at the **value** level, and that there is no state-transition key — i.e. the irreversible-enable cannot be IAM-fenced except by ownership/tag. (Doc evidence: L8808 key list; corroborate against `iam-policies-for-amazon-ec2.md` casing claim — the hub flags this contradiction as needing empirical settling.)
2. **(Area A)** Confirm the SourceForge `e1000/ixgbevf stable` files endpoint publishes no checksum/signature and redirects through third-party mirrors (static OSINT; no download).
3. **(Area B)** Confirm whether `CreateImage`/`RegisterImage` perform **any** warning or scrub of `70-persistent-net.rules` (the page says the operator must do it manually → almost certainly not; verify no console/API guard).
4. **Drift canary:** the L290 flag-split typo (Area F) is a cheap offline==online freshness check — if it is ever fixed, re-fetch the whole page.

---

## §8 — Deliverable summary

A **page-level complement** to the `enhanced-networking` hub plan. It defers all control-plane mechanisms (casing fail-open, RegisterImage unguarded twin, DescribeInstanceAttribute read oracle, no-`ec2:InstanceState`-key, Reset-can't-undo) to the hub / enabling-enhanced-networking / troubleshooting-ena plans, and **uniquely owns**: the SourceForge+Intel.com **supply-chain** seam (Area A), the `70-persistent-net.rules` **stale-MAC derived-AMI DoS** (Area B), the **kernel-upgrade silent driver-revert** latent DoS (Area C), the Xen/PV **amplified irreversibility** (Area D, sharpening hub Area 5), the Windows **EC2Launch password-reset** operational surprise (Area E), and a confirmed **doc-integrity defect** (Area F). Cross-tenant/credential/injection/data-plane lenses are explicit nulls (pages named). No live testing performed; destructive confirm items are flagged owned-canary-only.
