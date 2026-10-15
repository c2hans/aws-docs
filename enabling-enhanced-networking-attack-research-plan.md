# Enable Enhanced Networking on Your Instance (`enabling_enhanced_networking.html`) — Attack Research Plan

Source of leads: the enable-procedure how-to page `enabling_enhanced_networking.html`
(offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/enabling_enhanced_networking.md`) +
the IAM Service Authorization Reference `list_ec2.md`
(`/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`, 10,190 lines) +
`iam-policies-for-amazon-ec2.md`. Status: documentation-derived hypotheses only; nothing tested
against a live account. **Offline==online byte-identical confirmed 2026-10-15** (markers: the two
`git clone https://github.com/amzn/amzn-drivers` occurrences L85/L182; the Windows
`https://s3.amazonaws.com/ec2-windows-drivers-downloads/ENA/Latest/AwsEnaNetworkDriver.zip` L288;
`Set-ExecutionPolicy -ExecutionPolicy Unrestricted` L293–294; the `70-persistent-net.rules`
paragraph L139).

## Relationship to the existing plans — READ THIS FIRST

This page is a **procedural how-to child** that is already a *source page* of two existing plans.
It is NOT fresh surface. This plan is a **tightly-scoped COMPLEMENT** that owns only the net-new
surface those two left uncaptured, and it **corrects one stale claim** in the hub plan. Execute the
two parent plans first; the three Areas below are *additions*, not replacements.

Already OWNED elsewhere — do **not** restate here:
- **`enhanced-networking-attack-research-plan.md` (hub)** — Area 1 ENA-Express `EnaSrdSpecification`
  three-path IAM-unscopability; Area 2 cross-team ENI SRD-state flip; Area 3 SRD vs inspection /
  Flow-Log silence; **Area 4/4b** `ModifyInstanceAttribute` single-attribute scopability +
  `ec2:Attribute/${AttributeName}` casing fail-open + Describe\*Attribute no-`ec2:Attribute`-key read
  oracle; **Area 5** irreversible `sriovNetSupport`/reachability-break `enaSupport` bricking primitive
  + `RegisterImage` AMI-level unguarded write-path; **Area 6** AWS-authored driver-install insecure
  defaults (the *separate* `ena-adapter-driver-install-upgrade-win.md` Windows download); Area 7
  metrics side-channel.
- **`enhanced-networking-ena-attack-research-plan.md` (ENA landing-page child)** — **Area N2 / Objective 1**
  owns the Windows enable procedure's `Set-ExecutionPolicy Unrestricted` + unpinned `…/ENA/Latest/…`
  checksum-free `install.ps1` fetch *on this very page* (quoted verbatim); N1 the ENA-Express
  cross-account/shared-subnet SRD doc contradiction; N3 `CreateImage` silent `enaSupport` inheritance;
  N4 "cannot be managed from the console" contradiction; **N5-a** the `ec2:Attribute` PascalCase-vs-
  lowerCamelCase casing trap; **N5-d** the `RegisterImage` "no narrow Deny to bake ENA/SRIOV into an
  AMI" gap; N5-b `DescribeInstances` region-only read oracle.

**What THIS plan owns (net-new only):**
- **Area 1** — the `70-persistent-net.rules` MAC-address AMI-propagation leak (fully untouched by both).
- **Area 2** — the *full multi-OS* driver-install supply-chain artifact set this page prints
  (unpinned `git clone` ×2, DKMS support-void, GRUB `net.ifnames=0` / Trusty `/dev/xvda`), plus a
  Lens-EE predictable-S3-bucket-name sliver. **Corrects** hub Area 6 R-2's stale doc-gap claim that
  "the in-scope UserGuide pages print no Linux `git clone`/`make install` sequence" — this page does,
  twice.
- **Area 3** — the EBS-vs-instance-store **enable-path fork** this page documents (L39): instance-store
  instances cannot be stopped, so `ModifyInstanceAttribute` is unavailable and `RegisterImage` is the
  *only* path — the strictly-weaker-scopable twin — and **no `ec2:InstanceState`-type condition key
  exists anywhere in `list_ec2.md`**, so the pervasive "must be STOPPED" guardrail is a runtime gate,
  not an IAM lever. Sharpens (does not restate) hub Area 5 / ENA N5-d.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- Safe first oracle for every IAM-scopability lead is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (no resource touched). `DryRunOperation` is caller-IAM-only, **NOT** an ownership/state oracle.
- Supply-chain / AMI-hygiene leads are **documentation-and-package-metadata inspection only** — never tamper with a live artifact, bucket, or shared AMI, and never fetch-and-run the installer to "confirm" it.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the SRD fabric, the Nitro card, a host-manager interface, or an AWS-owned distribution bucket's control plane), stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives (page-specific; additive to both parent plans)
1. Prove or refute that AWS's own copy-verbatim AMI-creation procedure bakes the **original builder
   instance's MAC address** into a derived AMI (via a retained `/etc/udev/rules.d/70-persistent-net.rules`)
   with **no control-plane enforcement** that the file was stripped — a cross-tenant hardware-identity
   disclosure + boot-DoS that propagates silently across every `launchPermission` share / AMI copy.
2. Audit the **full set** of AWS-authored, copy-verbatim driver-install commands this page prints for
   insecure defaults (Lens R): the two unpinned `git clone` of `amzn-drivers`, the DKMS
   support-agreement-voiding path, the GRUB `net.ifnames=0` edit — and the Lens-EE predictable-bucket
   angle on the Windows distribution path. **Correct** the hub plan's stale "no Linux git clone on any
   in-scope page" claim.
3. Characterize the **EBS-vs-instance-store enable-path fork** (page L39) as an IAM-governance asymmetry:
   instance-store instances are forced onto `RegisterImage` (the twin with *zero* attribute-scoping keys),
   and the ubiquitous "must be STOPPED" precondition is **not expressible as an IAM condition key** at all.

---

## 2. Components, Assets, and Design (page scope only)

**What this page is.** The step-by-step how-to for *enabling* enhanced networking on an existing
instance (or baking it into an AMI). It presents, per operating system:
- A **test** step (`describe-instances --query ...EnaSupport`; `EnaSupport=false` by default).
- An **enable** step that **forks on root-device type**:
  - **EBS-backed:** stop → `modify-instance-attribute --ena-support` (or `Edit-EC2InstanceAttribute -EnaSupport $true`) → start. Reversible via `--no-ena-support`.
  - **Instance-store-backed (L39):** *"You can't stop the instance to modify the attribute. Instead … register-image"* → `register-image --ena-support …` (or `Register-EC2Image -EnaSupport $true …`).
- A **driver-install** step (Linux: build `ena` from GitHub; Windows: fetch + run `install.ps1`).
- An **AMI-creation** step with the `70-persistent-net.rules` deletion warning.

**Assets touched.** Instance attribute `enaSupport` (reversible) / `sriovNetSupport` (one-way); AMI
attribute `enaSupport`/`sriovNetSupport` (inherited / `RegisterImage`-set); the derived **AMI blob**
(and anything inside its guest filesystem that survives into a share); the guest kernel (driver load).

**Identifiers.** `i-…`, `ami-…`. No new ID shape.

**Trust posture.** Everything the *driver* steps touch is guest-OS plane (the customer's own instance
fetches/builds); in scope only as a **Lens-R audit of AWS's instructions**, never as a service bug.
The MAC-leak (Area 1) is special: it is guest-filesystem content that **crosses the AMI-share control-
plane boundary** when the AMI is shared — so it is a propagation finding, not a pure guest-local one.

**ASCII (enable + propagation):**
```
                         ┌── EBS root ──▶ stop → ModifyInstanceAttribute(enaSupport) → start   [reversible]
instance (enaSupport?) ──┤
                         └── instance-store root ──▶ RegisterImage(--ena-support)   [L39: cannot stop]
                                                            │  (strictly fewer IAM keys than Modify)
CreateImage/RegisterImage ──▶ AMI ──(launchPermission share / CopyImage)──▶ consumer account
      │                                                                         │
      └─ if 70-persistent-net.rules NOT stripped ───────────────────────────▶ builder MAC baked in guest FS
                                                                                 + eth0 boot failure (DoS)
```

---

## 3. Trust-Boundary Map (page-specific rows; see parents for the SRD/ENI/attribute rows)

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| AMI builder (any account) | Every consumer of a shared/published AMI | `CreateImage`/`RegisterImage` with `70-persistent-net.rules` retained, then `launchPermission` share / `CopyImage` | A consumer's guest FS contains the **builder's** MAC address; and/or the consumer's `eth0` fails on first boot — an attribute of the *source* fleet leaks/propagates across the AMI-share boundary with no control-plane scrub (Lens Q/AA/U/O). |
| Operator following AWS's Linux enable runbook | Guest kernel (privileged `insmod`/initramfs) | `git clone …amzn-drivers` (HEAD, unpinned, no checksum) → compile → `dracut -f -v` | An unpinned/unverified source tree is compiled into the boot-time initramfs with no pin or signature step the runbook references (Lens R; first-party repo caps severity). |
| Any AWS account (hypothetical, future) | Any consumer still following the Windows URL | predictable global bucket name `ec2-windows-drivers-downloads` if ever released | A squatted first-party bucket name serves an attacker ZIP that `install.ps1` runs as Administrator with signing disabled (Lens EE; **theoretical** — AWS owns the bucket today). |
| Principal w/ `ec2:RegisterImage` (no `ec2:ModifyInstanceAttribute`) | Instance-store ENA/SR-IOV enablement | re-register the AMI with `--ena-support`/`--sriov-net-support` | ENA/SR-IOV enabled via the twin that carries **no `ec2:Attribute` key**, bypassing any Deny the admin keyed on `ModifyInstanceAttribute` (Lens X; mechanism owned by hub Area 5 / ENA N5-d — this row is the page-specific instance-store framing). |
| Any customer surface | AWS SRD fabric / Nitro card / AWS distribution-bucket control plane | — | **hard stop** disclosure. |

---

## 4. API / Interface Inventory (delta only — see parents for the full table)

| Name | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|
| `RegisterImage` (`--ena-support`/`--sriov-net-support`) | yes | yes | image owner / grantee | **Only** enable path for **instance-store** roots (page L39). `image*` row keys = `aws:RequestTag`, `aws:TagKeys`, `ec2:ImageID`, `ec2:Owner`, `ec2:Region` — **no `ec2:Attribute`** (`list_ec2.md:9319`). Strictly fewer keys than `ModifyInstanceAttribute`. Bake-in gap owned by hub Area 5 / ENA N5-d; **instance-store-fork framing owned here (Area 3)**. |
| `ModifyInstanceAttribute` (`--ena-support`/`--no…`/`--sriov-net-support`) | yes | yes | instance owner / grantee | EBS path; requires **STOPPED** (runtime gate). `instance*` row has `ec2:Attribute`/`ec2:Attribute/${AttributeName}` (`list_ec2.md:8808`) but **no `ec2:InstanceState` key exists anywhere** → the stop precondition is not IAM-expressible (Area 3). Scopability/casing owned by hub Area 4 / ENA N5-a. |
| `CreateImage` | yes | yes | instance owner / grantee | AMI-creation step where the `70-persistent-net.rules` warning attaches (Area 1). Silent `enaSupport` inheritance owned by ENA N3. |
| Guest driver fetch (`git clone`/`install.ps1`) | n/a (guest) | guest-initiated | local root / Administrator | Lens-R instruction audit only (Area 2). Windows `Set-ExecutionPolicy`/`Latest` fetch owned by ENA N2. |

No non-SDK / console-hidden control-plane knob is introduced by this page.

---

## 5. Recommended Areas of Focus (NET-NEW; additive to both parent plans)

### Area 1 — `70-persistent-net.rules`: builder MAC baked into a shared AMI (disclosure + boot-DoS, no control-plane scrub) [Lens Q / AA / U / O] — HEADLINE, fully net-new
**Background.** The page's AMI-creation step warns (L139, verbatim):
> *"If your instance operating system contains an `/etc/udev/rules.d/70-persistent-net.rules` file, you
> must delete it before creating the AMI. This file contains the MAC address for the Ethernet adapter of
> the original instance. If another instance boots with this file, the operating system will be unable to
> find the device and `eth0` might fail, causing boot issues. This file is regenerated at the next boot
> cycle, and any instances launched from the AMI create their own version of the file."*

**Security Concern.** The mitigation is **prose-only — "you must delete it"** — with no API-level,
build-tool-level, or `CreateImage`/`RegisterImage`-level check that the file was actually stripped before
the AMI write completes (confirmed: `CreateImage`/`RegisterImage` have no guest-filesystem-content
condition key; `list_ec2.md:5142–5147`/`9317–9321`). Two distinct harms, both propagating across the
AMI-share boundary:
- **(a) Cross-tenant hardware-identity disclosure (Lens Q/AA/O).** If the builder skips the manual
  deletion and the AMI is shared via `launchPermission` (cross-account) or published, the **original
  builder's MAC address** is baked into a guest file inside *every* instance a consumer launches, durable
  until the consumer's own first boot regenerates it. It is a zero-privilege, guest-readable oracle
  (`cat /etc/udev/rules.d/70-persistent-net.rules`) that lets a consumer correlate a shared/public AMI
  back to its originating fleet/vendor, and can confuse any **MAC-allowlist / NAC / MAC-bound licensing**
  control into treating a foreign MAC as legitimate.
- **(b) Availability / boot-DoS (Lens U).** Independent of sharing, a reused or cloned AMI that retains
  the file causes the *consumer's* `eth0` to fail to come up on first boot — AWS's own text: *"the operating
  system will be unable to find the device and `eth0` might fail, causing boot issues."* A publisher who
  forgets the step ships a latent boot failure to every downstream launcher.
- **(c) Lens-AA propagation.** The defect is baked into the blob, not per-launch runtime state, so one
  forgotten manual step propagates automatically and silently through every subsequent share / `CopyImage`.

**High-level Test Scenarios.**
- *Claim:* `CreateImage`/`RegisterImage` performs no guest-FS scrub or validation of `70-persistent-net.rules`
  before completing the AMI. → *Oracle:* `list_ec2.md` image-write rows carry only tag/ID/owner/region keys
  (confirmed, no content hook); on an **owned** builder instance, create an AMI *without* deleting the file
  and confirm the file survives into an instance launched from that AMI (`cat` the path). **Owned canaries only.**
- *Claim:* the retained MAC is readable by a consumer of a **shared** AMI. → *Oracle:* share the owned test
  AMI to a **second account you control**, launch there, read the file; confirm it holds the *builder's* MAC.
  Keep strictly within accounts you own; do not touch any third-party or public AMI.
- *Claim:* a retained file causes `eth0` boot failure on a differing-hardware target. → *Oracle:* document-level
  — AWS asserts it; a live reproduction is a destructive availability test, owned-canary only.

**Doc evidence.** `enabling_enhanced_networking.md:139`; `list_ec2.md:5142–5147` (`CreateImage` rows),
`9317–9321` (`RegisterImage` rows). **Severity-if-true:** Low–Medium — the disclosure is a MAC (low-sensitivity
identifier) and the modern Amazon Linux / Ubuntu HVM AMIs are already ENA-capable (exempted earlier on this
same page), narrowing this manual procedure — and its risk — to **legacy / "other Linux" / instance-store
custom-AMI builders**. Reportable as an AWS-authored *prose-only* mitigation with no enforcement, most
impactful for AMI marketplace/vendor publishers. **Confirmed net-new:** grep shows zero mentions of
"70-persistent"/"MAC address" in either parent plan.

### Area 2 — Full multi-OS driver-install supply-chain artifact set [Lens R / Y / EE] — net-new; CORRECTS hub Area 6 R-2
**Background.** The hub plan's Area 6 (R-2) explicitly recorded a doc-gap: *"the in-scope UserGuide pages
print **no** Linux `git clone`/`curl`/`make install` sequence."* **That is stale for this page.**
`enabling_enhanced_networking.md` prints the bare clone **twice** — once in the RHEL/SUSE/CentOS/"other Linux"
section (L85) and once in the Ubuntu-DKMS section (L182). This Area owns the Linux + non-Windows artifacts the
siblings never developed; the Windows `Set-ExecutionPolicy`/`…/ENA/Latest/…` finding is owned by ENA Area N2
and is **cross-referenced, not restated**.

**Security Concern (per artifact).**
- **R-A — unpinned `git clone amzn-drivers` (Low; corrects hub R-2).** *"`git clone https://github.com/amzn/amzn-drivers`"*
  → compile → `sudo depmod` → `dracut -f -v`. The repo is **first-party** (`github.com/amzn` = Amazon's org →
  in-scope Lens R, not a 3P exclusion), which caps severity, but the clone is to **HEAD of the default branch**
  with **no tag/release/commit-SHA pin** and **no signature/checksum step** before the source is compiled and
  forced into the boot-time initramfs as a privileged kernel module. The DKMS variant later tells the operator
  to rename the cloned directory to include "the version number … in the release notes" — but that rename
  happens *after* the unpinned clone, so even the DKMS path never checks out a tagged release; it just labels an
  untagged checkout with a version string taken on faith.
- **R-B — DKMS voids the support agreement (Low; net-new, zero prior mentions).** *"Using DKMS voids the support
  agreement for your subscription. It should not be used for production deployments … for testing and feedback
  purposes only."* Good disclosure hygiene by AWS, but it sits adjacent to and reuses the same unpinned clone
  plus a hand-authored `dkms.conf` whose `PACKAGE_VERSION="1.0.0"` is a copy-pasted example, not verified.
  Operator-footgun / support-posture note.
- **R-C — GRUB `net.ifnames=0` / Trusty `/dev/xvda` (Low/informational; net-new).** Disabling predictable NIC
  names and the Ubuntu-Trusty "install `grub` onto `/dev/xvda`, keep `/boot/grub/menu.lst`" step are
  connectivity/boot-continuity details, not security boundaries. Recorded for completeness; hub Area 6 mentions
  `net.ifnames=0` once in passing but never analyzes it, and the Trusty detail is unmentioned by both siblings.
- **EE sliver — predictable first-party S3 bucket name (Informational; theoretical).** The Windows path fetches
  from the global-namespace bucket `ec2-windows-drivers-downloads`. **Documentation-derived only, no probe:**
  *if* such a first-party distribution bucket name were ever deregistered/released, the predictable name becomes
  globally squattable, and any consumer still following this exact AWS-authored URL would fetch-and-run (as
  Administrator, with signing disabled per the same runbook — see ENA N2) an attacker ZIP — a classic Lens-EE
  predictable-name land-grab shape. **AWS owns and serves the bucket today → theoretical/informational.** Neither
  sibling's Lens-EE note covers bucket naming (sibling 1's EE-null is scoped to AMI `enaSupport` trust confusion).

**High-level Test Scenarios.**
- *Claim:* this page prints a bare, unpinned `git clone` of `amzn-drivers` with no verification step → the hub's
  "no Linux git clone on any in-scope page" is wrong. → *Oracle:* the two literal occurrences at L85/L182
  (present); the `amzn-drivers` README/RELEASENOTES does not instruct GPG-signed-tag checkout before `make`
  (follow-on fetch — the repo's *own* internal practices are a 3P-repo exclusion, but the *absence of a pin/verify
  step in AWS's referencing instruction* is in scope).
- *Claim (EE, doc-only):* the `Latest` Windows path is mutable/unversioned vs the pinned `…/x64/<version>/…` form,
  and the bucket name is predictable. → *Oracle:* contrast the two documented URL forms (do **not** probe the bucket).

**Doc evidence.** `enabling_enhanced_networking.md:85,182` (`git clone`), DKMS section (support-void), L139-adjacent
GRUB steps, L288/L293–294 (Windows — cross-ref ENA N2). **Severity-if-true:** Low across the board (first-party
source, HTTPS, no known compromise); value is **correcting the hub's stale claim** and completing the artifact
inventory. Report the unpinned-clone omission as an AWS-authored insecure default, not an active 3P trust breach.

### Area 3 — EBS-vs-instance-store enable-path fork: the only instance-store path is the weaker twin, and "must be STOPPED" is not IAM-expressible [Lens X / S / U] — net-new framing; sharpens hub Area 5 / ENA N5-d
**Background.** This page is where the enable procedure **forks on root-device type** (L39):
> *"If your instance is an instance store-backed instance, you can't stop the instance to modify the
> attribute. Instead … use the `register-image` command."*

EBS-backed → `ModifyInstanceAttribute --ena-support` (requires STOPPED). Instance-store → `RegisterImage
--ena-support` (no stop possible).

**Security Concern (two net-new observations; the RegisterImage *bake-in* gap itself is owned by hub Area 5 /
ENA N5-d — not restated).**
- **(a) The forced path is the strictly-weaker-scopable twin (Lens X).** `ModifyInstanceAttribute`'s `instance*`
  row carries `ec2:Attribute`/`ec2:Attribute/${AttributeName}` (`list_ec2.md:8808` — a per-attribute hook, even
  if its binding to `EnaSupport` is unconfirmed; see ENA N5-a). `RegisterImage`'s `image*` row carries **no
  `ec2:Attribute` key at all** (`list_ec2.md:9319` — only `aws:RequestTag`/`aws:TagKeys`/`ec2:ImageID`/`ec2:Owner`/
  `ec2:Region`). So the one path AWS *forces* onto instance-store instances is the twin an admin can govern
  **least**: there is no attribute-level lever on it whatsoever, and an admin who `Deny`s `ec2:ModifyInstanceAttribute`
  (believing they've blocked enhanced-networking enablement) leaves the `RegisterImage` path fully open for any
  instance-store workload.
- **(b) The ubiquitous "must be STOPPED" precondition is NOT an IAM condition key (Lens S/U).** The stop
  requirement appears throughout this page's EBS procedure, but **no `ec2:InstanceState`-type condition key
  exists anywhere in `list_ec2.md`** (confirmed absent from the master condition-key table at `list_ec2.md:10036`
  onward). The precondition is a **service-side runtime gate**, not IAM-expressible — so an admin **cannot** author
  a policy like "allow enabling ENA only on a stopped instance / only during a maintenance window / never
  re-trigger the one-way `sriovNetSupport`." Combined with the Area-5 irreversibility of `sriovNetSupport`, there
  is no state-aware IAM lever to constrain *when* the destructive flip may occur — only *whether* the principal
  holds the action at all.

**High-level Test Scenarios.**
- *Claim:* a principal with `ec2:RegisterImage` but denied `ec2:ModifyInstanceAttribute` can still enable ENA/SR-IOV
  on an instance-store workload via re-register. → *Oracle:* `iam:SimulateCustomPolicy` — the Deny on
  `ModifyInstanceAttribute` has no effect on `RegisterImage` (the key set doesn't overlap; `--ena-support` is not
  gated by any `RegisterImage` key). No live resource touched.
- *Claim:* no condition key lets an admin require the instance be stopped (or restrict to a maintenance window) for
  `ModifyInstanceAttribute`. → *Oracle:* grep the condition-key master table for any `InstanceState`/state key →
  zero; confirm the "must be STOPPED" rule is enforced only at call time, not by IAM.

**Doc evidence.** `enabling_enhanced_networking.md:39,45,50,60–68`; `list_ec2.md:8808` (Modify keys), `9319`
(RegisterImage keys), `10036`+ (condition-key master table, no state key). **Severity-if-true:** Low–Medium
(least-privilege / policy-completeness gap; the RegisterImage bake-in and `sriovNetSupport` irreversibility
severities are owned by hub Area 5 / ENA N5-d — this Area adds the instance-store-fork framing and the
no-state-key observation).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Builder MAC baked into a shared AMI (disclosure + boot-DoS) | `CreateImage`/`RegisterImage` + guest FS | **prose-only** "you must delete it"; no control-plane scrub/validation (Area 1) |
| Unpinned `git clone amzn-drivers` compiled into initramfs | guest driver build (Linux) | *none* — AWS text prints a bare clone, no pin/checksum; first-party repo (Area 2 R-A) |
| DKMS voids support agreement | guest driver build (Ubuntu) | AWS discloses it; reuses the unpinned clone (Area 2 R-B) |
| Predictable first-party distribution bucket (if ever released) | Windows `install.ps1` fetch | *none documented*; theoretical land-grab, AWS owns bucket today (Area 2 EE sliver) |
| Instance-store enablement via the weaker twin | `RegisterImage` | *none* — no `ec2:Attribute` key on `RegisterImage`; Deny on `ModifyInstanceAttribute` doesn't cover it (Area 3a) |
| No IAM lever to require STOPPED / a maintenance window | `ModifyInstanceAttribute` | *none* — no `ec2:InstanceState`-type key exists in EC2 (Area 3b) |

---

## 7. Out-of-Scope Risk Categories
- **Guest-OS driver fetch/build by the customer's own instance** — a guest/client fetch, not a server-side
  service-plane fetch (no SSRF role). In scope only as the Lens-R audit of AWS's *instructions* (Area 2). The
  `github.com/amzn/amzn-drivers` repo's own internal practices are a 3P-repo-behavior exclusion (Amazon-owned);
  the absence of a pin/verify step in AWS's referencing instruction is in scope.
- **The SRD transport fabric / Nitro card internals / IMDS on the managed host / an AWS distribution bucket's
  control plane** — AWS service plane; hard-stop disclosure, not a test target.
- **Single-tenant self-DoS** (bricking your *own* instance by enabling ENA on an incompatible kernel) — product
  behavior. The *cross-team* bricking primitive is owned by hub Area 5.
- **The Windows `Set-ExecutionPolicy Unrestricted` + `…/ENA/Latest/…` finding** — owned by ENA Area N2 /
  Objective 1; cross-referenced here, not re-filed.
- **ENA-Express / `EnaSrdSpecification`, `ModifyInstanceAttribute` scopability + casing, Describe\* read oracles,
  `RegisterImage` bake-in gap, `CreateImage` inheritance, "cannot be managed from the console", cross-account SRD**
  — all owned by the hub plan (Areas 1–7) and ENA plan (N1–N5). Execute those; do not re-file here.

---

## 8. Null hypotheses / doc gaps
- **Lens G (SSRF): NULL** — read the full page. Every URL/fetch (`install.ps1` zip, the two `git clone`s) is
  dereferenced by the customer's **own guest OS**, not by an EC2 control-plane fetch identity. No `*Url`/`*Uri`
  field the service fetches server-side.
- **Lens A (cross-tenant IDOR on the enable path): NULL** — the enable actions act on the caller's own
  instance/AMI; cross-account reach exists only via *deliberate* `launchPermission` AMI sharing (Area 1 is a
  propagation/hygiene finding on that consensual share, not an IDOR). ENA-Express cross-account is owned by ENA N1.
- **Lens EE (AMI `enaSupport` trust confusion): REFUTED** (per hub §8 / ENA N3) — enhanced-networking state is a
  functional/perf attribute, not a trust signal; no `RunInstances` consumer makes a security decision on it. The
  only EE angle this page adds is the **S3 bucket-name** sliver (Area 2), which is theoretical.
- **Lens H / W / FF / J / DD / CC / BB / N / P: NULL for this page** — no KMS/encryption-context, attestation gate,
  JWT/OIDC validation, OAuth linking, caching layer, multi-parser request path, namespace migration, or
  registration/proofing workflow. Page read in full.
- **Lens Q (AMI-as-blob hygiene): FIRES** — Area 1 (the MAC-leak), the one place this page introduces an
  untrusted-content-survives-into-a-share surface.
- **Open doc-gaps to confirm before investing:** (1) does any build tool / `CreateImage` option scrub
  `70-persistent-net.rules` (none found; confirm no EC2 Image Builder / cloud-init default silently handles it —
  if a managed builder does, Area 1 narrows further); (2) does the `amzn-drivers` README instruct a signed-tag
  checkout the AWS page omits (Area 2 R-A follow-on); (3) confirm via `iam:SimulateCustomPolicy` that a
  `ModifyInstanceAttribute` Deny leaves `RegisterImage --ena-support` Allowed (Area 3a).
- **Drift:** `enabling_enhanced_networking.md` re-verified offline==online **byte-identical 2026-10-15** (markers
  L85/L139/L182/L288/L293–294). `list_ec2.md` rows cited inline (8808 / 9319 / 10036+). Parent plans' hub/ENA
  claims cross-referenced as of their 2026-10-15 checks.
