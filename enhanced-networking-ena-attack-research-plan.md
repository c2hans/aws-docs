# EC2 Enhanced Networking with ENA (`enhanced-networking-ena.html`) — Attack Research Plan

Source of leads: the ENA landing page `enhanced-networking-ena.html` + its own child set
(`test-enhanced-networking-ena.html`, `enabling_enhanced_networking.html`, `ena-queues.html`,
`troubleshooting-ena.html`, `troubleshoot-ena-driver.html`, `ena-driver-releases-windows.html`,
`ena-adapter-driver-install-upgrade-win.html`) + `API_EnaSrdSpecification.md`. Cross-checked against
the IAM Service Authorization Reference `list_ec2.md` (offline mirror
`/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`). Status: documentation-derived
hypotheses only; nothing tested against a live account. Offline==online byte-identical confirmed for the
target page 2026-10-15 (markers: `enaSupport` L52, SHA-2 L54, "cannot be managed from the Amazon EC2
console" L55).

## Relationship to the existing hub plan — READ THIS FIRST

This is a **page-level deep-dive child of the existing `enhanced-networking-attack-research-plan.md`**
(the `enhanced-networking.html` hub + all children umbrella), which is itself a page-level child of the
`ec2-networking` hub plan. That hub plan already OWNS, and this plan deliberately does **not restate**:

- **Area 1** — ENA Express `EnaSrdSpecification` IAM-unscopable-by-value + three-path (`ModifyNetworkInterfaceAttribute`/`AttachNetworkInterface`/`RunInstances`) action-family-parity gap [Lens S/X/U].
- **Area 2** — cross-team flip of a victim ENI's ENA-Express state [Lens S/A intra-account].
- **Area 3** — SRD multipath vs in-path inspection + VPC-Flow-Log/Traffic-Mirroring silence [Lens V/O].
- **Area 4 / 4b** — `ModifyInstanceAttribute` single-attribute scopability + `ec2:Attribute/${AttributeName}` casing fail-open (`enaSupport` vs `userData`); `DescribeInstanceAttribute`/`DescribeImageAttribute` carry **no `ec2:Attribute` key at all** → "read enaSupport" grant reads `userData` [Lens S/O/A].
- **Area 5** — irreversible `sriovNetSupport` enablement + reachability-break `enaSupport` as a bricking primitive; `RegisterImage` AMI-level unguarded write-path [Lens L/U/X].
- **Area 6** — AWS-authored driver-install insecure defaults (the `ena-adapter-driver-install-upgrade-win.md` Step-2 `.../ENA/Latest/` download, no checksum) [Lens R].
- **Area 7** — ENA / ENA-Express metrics as a side-channel/oracle [Lens O/L].

**This plan owns only the net-new surface the ENA landing page + its specific children introduce that the
hub plan left uncaptured or stated at summary level**, and it **reconciles two findings against the hub
plan** (Area N1 reopens the hub's Lens-A-NULL verdict; Area N2 sharpens the hub's Area 6). If you are the
hunter: execute the hub plan's Areas 1–7 first; the three Areas below are *additions*, not replacements.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right.
- Safe first oracle for IAM-scopability leads is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (no resource touched). `DryRunOperation` is caller-IAM-only, NOT an ownership oracle.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the SRD transport fabric, the Nitro card, a host-manager interface), stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives (page-specific; additive to the hub plan's objectives)
1. Prove or refute that AWS's own copy-verbatim Windows **enable procedure** (`enabling_enhanced_networking.md`) instructs the operator to **disable PowerShell script-signing enforcement** (`Set-ExecutionPolicy Unrestricted`) in order to run a script fetched over a **mutable, unversioned, checksum-free** S3 URL with local-Administrator rights — a reportable AWS-authored insecure default (Lens R).
2. Resolve the **`ena-express.md` vs `API_EnaSrdSpecification.md` contradiction** on SRD reachability scope (same-Region narrative vs "same subnet within the same account, **or in different accounts**" API-ref text), and determine whether a **shared-subnet / VPC-sharing** participant can establish SRD with the VPC owner's (another account's) instance — i.e. whether ENA Express has a documented **cross-account** data path the hub plan's Lens-A-NULL verdict did not account for.
3. Characterize the ENA landing page's **prerequisite + "cannot be managed from the console"** framing as an availability/audit asymmetry: the destructive attribute-flip is forced onto the API/CLI path, below any console-only guardrail.

---

## 2. Components, Assets, and Design (page scope only)

**What this page is.** The ENA enablement landing page. Enhanced networking has three enable mechanisms
(parent `enhanced-networking.html`): **ENA** (instance+AMI attribute `enaSupport`, reversible), **Intel
82599 VF** (`sriovNetSupport="simple"`, one-way/irreversible), and **ENA Express** (per-attachment
`EnaSrdSpecification`, SRD transport). This page is the ENA + ENA-Express entry point; its own children are
the **test** (`describe-instance-attribute`/`DescribeInstances .EnaSupport`), **enable procedure**
(stop → `modify-instance-attribute --ena-support` → start), **queues**, and **troubleshooting + Windows
driver** pages.

**Control-plane surface touched by this page's children.**
- `ec2:ModifyInstanceAttribute --ena-support` / `--no-ena-support` (reversible), `--sriov-net-support simple` (one-way) — requires instance **STOPPED**.
- `ec2:DescribeInstances` / `ec2:DescribeInstanceAttribute` / `ec2:DescribeImages` (`.EnaSupport` read).
- `ec2:RegisterImage --ena-support` (instance-store AMI); **`CreateImage` silent inheritance** of `enaSupport` from the source instance (net-new owner — see Area N3).
- ENA queue count reconfiguration (console/CLI/PowerShell) — also requires instance STOPPED, value a power of 2, ≤ vCPU count.
- Guest-OS driver fetch/install (Windows `install.ps1` from S3; Linux delegated to `github.com/amzn/amzn-drivers`).

**Identifiers.** `i-…`, `ami-…`, `eni-…`. No new ID shape vs the hub plan.

**Prerequisites section (the page's own body, L50–55).** Nitro-based instance; internet connectivity;
**"you should back that data up now by creating an AMI … Updating the ENA kernel driver and enabling the
`enaSupport` attribute might render incompatible instances or operating systems unreachable"**; Windows
Server 2008 R2 SP1 needs the **SHA-2 code-signing support update**; management via **CloudShell / CLI /
PowerShell only — "Enhanced networking cannot be managed from the Amazon EC2 console."**

---

## 3. Trust-Boundary Map (page-specific rows; see hub plan for the SRD/ENI rows)

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Operator following AWS's Windows enable runbook | Local-Admin code execution on the guest | `Set-ExecutionPolicy Unrestricted` + run `install.ps1` from mutable `…/ENA/Latest/…zip`, no checksum | A substituted/tampered zip at that unpinned path executes as Administrator with signing enforcement disabled — AWS-authored instruction is the enabler (Lens R; guest-side but copy-verbatim). |
| Account B instance (shared subnet participant) | Account A instance's SRD transport | ENA Express enabled both ends, same subnet, `API_EnaSrdSpecification` "or in different accounts" | SRD session established across the account boundary where the user-facing `ena-express.md` narrative never says cross-account is possible (Lens U doc-integrity; reopens hub Lens-A-NULL). |
| Principal with `ModifyInstanceAttribute`+`Stop/StartInstances` (no console) | Victim stopped instance availability | Off-console `--ena-support`/`--sriov-net-support` flip during a stop window | A console-only SCP / click-through / session guardrail is bypassed because the destructive step has no console path (Lens O/U asymmetry; destructive detail owned by hub Area 5). |

---

## 4. API / Interface Inventory (delta only — see hub plan §4 for the full table)

| Name | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|
| `CreateImage` | yes | yes | instance owner / grantee | Silently **inherits** `enaSupport` from source instance → AMI (net-new owner, Area N3; `RegisterImage` AMI path owned by hub Area 5). |
| ENA queue-count config | yes | yes (console **and** CLI/PS) | instance owner / grantee | Console-manageable — contradicts the page's "cannot be managed from the console" blanket claim (Area N4). Requires STOPPED. |
| Windows `install.ps1` fetch | n/a (guest) | guest-initiated | local Admin | Fetched from unpinned `…/ENA/Latest/…`, run after `Set-ExecutionPolicy Unrestricted` (Area N2). |

No non-SDK/console-hidden control-plane knob is introduced by this page beyond the hub plan's `EnaSrdSpecification` three-path finding.

---

## 5. Recommended Areas of Focus (NET-NEW; additive to hub Areas 1–7)

### Area N1 — ENA Express reachability-scope contradiction & the undocumented cross-account SRD path [Lens U / A] — PRIMARY, reconciles hub Lens-A-NULL
**Background.** The user-facing concept page `ena-express.md` says: *"With ENA Express, you can communicate
between two EC2 instances in the same Availability Zone or across Availability Zones **within the same
Region**"* — stating **no subnet restriction and no account scope**. The API reference
`API_EnaSrdSpecification.md` states something materially narrower-and-broader: *"With ENA Express, you can
communicate between two EC2 instances **in the same subnet within the same account, or in different
accounts**. Both sending and receiving instances must have ENA Express enabled."*
**Security Concern.** (a) **Doc-integrity (Lens U):** the security-relevant constraint ("same subnet") and
the cross-account capability appear **only** in the API reference, not in the page a customer actually
reads to understand the feature — a customer building an isolation assumption on the concept page is
misled. (b) **Reopens the hub plan's Lens-A-NULL verdict.** The hub plan declared cross-tenant IDOR NULL
for ENA Express partly because *"nothing describes SRD … granting cross-VPC/cross-account reach"* (hub §8,
line 112). `API_EnaSrdSpecification.md` **does** describe a cross-account path ("or in different accounts")
— the canonical case being a **shared subnet (VPC sharing)** where two accounts own instances in one
subnet. The hub's NULL should be downgraded to **"doc-gap — confirm the shared-subnet cross-account SRD
establishment path before closing."**
**High-level Test Scenarios.**
- *Claim:* two instances owned by **different accounts** in one **shared subnet**, both with ENA Express enabled, establish an SRD session (not just standard-ENA fallback). → *Oracle (owned canaries, two accounts you control, one shared subnet):* `ethtool -S eth0 | grep ena_srd_tx_pkts` increments on cross-account flows; `ena_srd_mode` reports SRD active. Keep strictly within accounts you own.
- *Claim:* enabling SRD across the account boundary does **not** grant any reach standard ENA wouldn't (SG/NACL still evaluated per `ena-nitro-perf.md`). → *Oracle:* a Deny SG rule still drops the SRD flow; SRD rides the normal socket/TCP-UDP stack (distinct from EFA OS-bypass — do NOT treat as transferable).
- *Claim (Lens U):* the "same subnet" constraint is enforced, not advisory — enabling SRD between two instances in **different** subnets silently falls back to standard ENA with no error. → *Oracle:* SRD counters stay zero across-subnet.
**Doc evidence.** `ena-express.md` "How ENA Express works"; `API_EnaSrdSpecification.md` ("same subnet within the same account, or in different accounts"). **Severity-if-true:** doc-integrity inconsistency = Low/Informational (AWS-owned, worth filing — a customer could build an isolation/compliance assumption on the concept page's silence); a *provable* cross-account reach beyond standard ENA (SG not evaluated on the SRD path) would be High — but the architecture (SG/ACL still evaluated by the Nitro card) makes "SRD is just a faster transport for already-permitted flows" the likely outcome. **Mark doc-gap — confirm the shared-subnet establishment behavior first.**

### Area N2 — AWS's Windows ENABLE runbook disables script-signing to run a checksum-free fetched installer [Lens R] — PRIMARY, sharpens hub Area 6
**Background.** The hub plan's Area 6 audited the dedicated driver page `ena-adapter-driver-install-upgrade-win.md`
(Step 2: download from `…/ENA/Latest/AwsEnaNetworkDriver.zip`, no checksum). This Area owns a **second,
independent, and sharper instance** on a *different* page in the ENA landing page's own child set.
**Security Concern (net-new).** `enabling_enhanced_networking.md`'s **Windows enable procedure** itself
instructs: download the latest driver from
`https://s3.amazonaws.com/ec2-windows-drivers-downloads/ENA/Latest/AwsEnaNetworkDriver.zip` (the **mutable,
unversioned `Latest` alias** — same anti-pattern as hub Area 6, no SHA256/Authenticode/signed-manifest step
referenced), extract, and run `install.ps1`. It then **compounds** the fetch with an explicit
signing-enforcement downgrade: *"If you get an execution policy error, set the policy to `Unrestricted` (by
default it is set to `Restricted` or `RemoteSigned`). In a command line, run `Set-ExecutionPolicy
-ExecutionPolicy Unrestricted`, and then run the `install.ps1` PowerShell script again."* `Unrestricted`
permits **any unsigned script, including freshly internet-downloaded ones, to run with no warning** — and
the doc offers **no narrower alternative** (`Bypass` for a single `-Scope Process` session, unblocking the
specific file, or local signing). The script runs as **local Administrator**. So AWS's copy-verbatim enable
runbook pairs (i) an unpinned, integrity-unverified artifact with (ii) a global, persistent disabling of
the OS control that would otherwise refuse to run it — a Lens-R insecure-default stack that is strictly
worse than hub Area 6's single finding.
**High-level Test Scenarios.**
- *Claim:* no AWS-published checksum/signed manifest is referenced by `enabling_enhanced_networking.md`'s Windows flow, and `Set-ExecutionPolicy Unrestricted` is machine-scoped (persists beyond the install) rather than `-Scope Process`. → *Oracle (doc + package-metadata inspection only, no live tamper):* confirm the page text (present), confirm the zip at the `Latest` path ships no sibling `.sha256`/signed manifest the runbook cites, and confirm the AWS text uses bare `Set-ExecutionPolicy Unrestricted` with no `-Scope`. The *omission* of a verification step and the use of the broadest policy value are themselves the defect.
- *Claim:* the mutable `Latest` alias allows a downgrade/substitution window a pinned `…/x64/<version>/…` path (used by the version-history table) would not. → *Oracle:* contrast the two documented URL forms; the "fastest"/default-presented one is the unpinned one.
**Doc evidence.** `enabling_enhanced_networking.md` Windows section (download `…/ENA/Latest/…`; `Set-ExecutionPolicy -ExecutionPolicy Unrestricted`); cross-ref hub Area 6 / `ena-adapter-driver-install-upgrade-win.md` Step 2. **Severity-if-true:** Medium (AWS-authored copy-verbatim admin install: unpinned + unverified artifact + signing enforcement disabled). **Reportable** precisely because it is AWS-published instruction, not a customer footgun. Partially mitigated by 64-bit Windows kernel-mode driver-signature enforcement (would reject an unsigned `.sys`) and HTTPS transport — **residual risk is the `install.ps1` script layer**, which signing enforcement normally protects and this runbook explicitly disables.

### Area N3 — `CreateImage` silently inherits `enaSupport` → AMI (inheritance twin of the RegisterImage write-path) [Lens X / U]
**Background.** The hub plan's Area 5 owns `RegisterImage` as the unguarded **explicit** AMI write-path for
`enaSupport`/`sriovNetSupport`. This Area owns the **implicit** path on this page's own enable procedure.
**Security Concern.** `enabling_enhanced_networking.md` states, once per OS section (near-verbatim):
*"The AMI inherits the enhanced networking `enaSupport` attribute from the instance. Therefore, you can use
this AMI to launch another instance with enhanced networking enabled by default."* Inheritance is
**silent** — no step re-declares or re-confirms the attribute at `CreateImage` time for EBS-backed images;
it simply carries forward to every instance launched from that AMI. Combined with hub Area 5's finding that
**no `ec2:Attribute` value key governs the attribute on any image write-path**, a principal who can
`CreateImage` from a source instance that has `enaSupport` (or the one-way `sriovNetSupport`) set
**propagates that attribute to the fleet with no IAM lever to forbid it**. For `enaSupport` this is benign
(reversible, perf-only); for an image whose source carried `sriovNetSupport=simple` it propagates an
**irreversible** attribute, broadening the hub Area 5 bricking blast radius to launch-from-AMI.
**Lens-EE check — REFUTED (confirmed):** `enaSupport` is a functional/perf attribute, **not** a trust
signal; no documented `RunInstances` consumer makes a security decision on an AMI's `enaSupport` value
(unlike owner-id / `imdsSupport`). Worst case = degraded perf / unreachability, already covered by hub
Area 5. Recorded to close out the whoAMI-style angle.
**High-level Test Scenarios.**
- *Claim:* `CreateImage` from an `enaSupport`-enabled instance yields an AMI whose `.EnaSupport` is true with no attribute re-declaration. → *Oracle:* `describe-images --query "Images[].EnaSupport"` on the new AMI returns the inherited value; no `ec2:Attribute` key on `CreateImage`/`RegisterImage` can have forbidden it (`iam:SimulateCustomPolicy`).
**Doc evidence.** `enabling_enhanced_networking.md` (inheritance sentence, each OS section); `test-enhanced-networking-ena.md` L50–77 (`.EnaSupport` AMI read); cross-ref hub Area 5. **Severity-if-true:** Low–Medium (least-privilege / policy-completeness gap; propagation of an ungovernable attribute; irreversible only on the `sriovNetSupport` variant).

### Area N4 — "Cannot be managed from the console" blanket claim is contradicted by queue config + forces the destructive step off-console [Lens U / O]
**Background.** The target page asserts (L55): *"Enhanced networking cannot be managed from the Amazon EC2
console."* Subagent-confirmed procedural reality:
- The `enaSupport` **attribute toggle** step in `enabling_enhanced_networking.md` indeed offers **no console option** (only `modify-instance-attribute` / `Edit-EC2InstanceAttribute`), while the surrounding **stop/start** steps *do* offer the console — substantiating the claim for the toggle.
- BUT `ena-queues.md` L629 says the **ENA queue count** *is* set *"[u]sing the AWS Management Console, AWS CLI, or PowerShell … this setting appears under each Network interface"* — a part of "enhanced networking" that **is** console-manageable, contradicting the blanket statement.
**Security Concern.** Two angles: (a) **Lens U doc-integrity** — the absolute "cannot be managed from the
console" is false for queue count; a reader cannot rely on it. (b) **Lens O/U control-asymmetry** — the
*destructive* attribute flip (`--ena-support`/`--sriov-net-support`, the Area-5 bricking primitive) is
architecturally forced onto the API/CLI path, **below** any defense-in-depth that assumes console actions
get an extra confirmation, MFA prompt, or console-session SCP (`aws:ViaAWSConsole`-style). The control point
a defender might rely on for "sensitive instance changes get a console click-through" simply does not exist
for the one step that can brick the instance — not because an attacker disabled it, but by design.
**High-level Test Scenarios.**
- *Claim:* `modify-instance-attribute --ena-support`/`--sriov-net-support` has no console equivalent, so a console-only guardrail does not cover the destructive step. → *Oracle:* enumerate the EC2 console instance-settings UI; confirm `enaSupport`/`sriovNetSupport` is absent while queue-count is present. (Documentation + console enumeration; no mutation.)
- *Claim:* the page's blanket "cannot be managed from the console" is contradicted by queue-count config. → *Oracle:* `ena-queues.md` L629 (present) vs `enhanced-networking-ena.md` L55 (present) — a direct textual contradiction.
**Doc evidence.** `enhanced-networking-ena.md` L55; `ena-queues.md` L629–635; `enabling_enhanced_networking.md` (stop/start offer console, toggle does not). **Severity-if-true:** Informational/Low (AWS-owned doc inconsistency + a design-level audit/guardrail asymmetry; the destructive-primitive severity itself is owned by hub Area 5).

### Area N5 — IAM condition-key audit sharpenings (SAR `list_ec2.md` + live `servicereference` JSON, 2026-10-15) [Lens S] — sharpens hub Areas 1 & 4, corrects one premise
**Method note.** Confirmed against both the offline SAR mirror `list_ec2.md` (10,190 lines) and the fresh
live machine-readable reference `https://servicereference.us-east-1.amazonaws.com/v1/ec2/ec2.json`; both
agree on every point. The live HTML/.md SAR page truncates before the Actions table (reproduced the task's
warning) — the offline mirror + JSON are authoritative. `grep -c -i "enasupport|sriovnetsupport|enasrd"`
over the full SAR → **0** → there is **no dedicated `ec2:EnaSupport`/`ec2:SriovNetSupport`/`ec2:EnaSrdSupported`
condition key anywhere in EC2's 145 service-wide keys**; the only lever is the generic
`ec2:Attribute` / `ec2:Attribute/${AttributeName}` pair (scopes attribute *name*, never the boolean *value*).

**N5-a — the casing trap is AWS-authored, inside ONE API page [sharpens hub Area 4b].** The hub plan's
Area 4b framed `ec2:Attribute/${AttributeName}` casing fail-open as `enaSupport` vs `userData`. The sharper,
doc-grounded instance: `API_ModifyInstanceAttribute.md` documents the generic `Attribute` request field's
valid values in **lowerCamelCase** (`enaSupport | sriovNetSupport | ebsOptimized | …`, L23) — **but** also
states the generic `Attribute=…&Value=…` path is restricted to `kernel|ramdisk|userData|…` only (L106–109),
so `EnaSupport` can **only** be set via its dedicated **PascalCase** top-level parameter (`EnaSupport.Value=true`,
L150–160). The User Guide's `ec2:Attribute` condition-key examples (`iam-policies-for-amazon-ec2.md:203–265`)
use the **PascalCase parameter-name** form. **Nowhere is the exact runtime-populated string for `ec2:Attribute`
spelled out per attribute.** An admin who models a Deny on the lowerCamelCase enum (`"ec2:Attribute":
"enaSupport"`) rather than the PascalCase name (`"EnaSupport"`) risks a Deny that **silently never matches**
under default case-sensitive `StringEquals` — a fail-open driven directly by AWS using two casing conventions
for the same concept on the same page. *Oracle:* `iam:SimulateCustomPolicy` with each casing against a
`ModifyInstanceAttribute --ena-support` request context; the one that fails to Deny is the trap. **Doc-grounded
hypothesis, unverified live; Tier-2 doc-clarity candidate.**

**N5-b — `DescribeInstances` is a region-only, fully-unscopable read oracle for ENA/SRIOV state [clean Lens S].**
`DescribeInstances` (`list_ec2.md:6996–7000`; JSON confirms no `Resources` array, `actionConditionKeys:
['ec2:Region']`) has a **blank resource-type cell and supports only `ec2:Region`** — no resource-level or
attribute-level IAM scoping at all. Its response returns `enaSupport`/`sriovNetSupport`. **A principal with
`ec2:DescribeInstances` in a region reads ENA/SRIOV (and ENI/addressing) state for every instance in that
region regardless of tags, ownership, or any boundary.** This is sharper than hub Area 4 (which addressed
`DescribeInstanceAttribute`/`DescribeImageAttribute` lacking `ec2:Attribute`): `DescribeInstances` can't even
be *instance*-scoped. (Caveat: this is a long-standing EC2-wide limitation, not ENA-specific — likely not a
*new* finding to AWS, but load-bearing for any "who can read enaSupport" boundary claim.)

**N5-c — `EnaSrdSpecification` value-scoping gap has a precise mechanism [sharpens hub Area 1].** The hub
Area 1 said ENA-Express config is unscopable-by-value. The mechanism: `ModifyNetworkInterfaceAttribute`'s
`network-interface*` row **does** carry `ec2:Attribute`/`ec2:Attribute/${AttributeName}` (`list_ec2.md:8969`),
so an admin can Deny `"ec2:Attribute": "EnaSrdSpecification"` wholesale — but `EnaSrdSpecification`
(`API_EnaSrdSpecificationRequest.md:13–21`) is a **multi-field object** (`EnaSrdEnabled` boolean **plus**
nested `EnaSrdUdpSpecification`). The User Guide states `ec2:Attribute/${AttributeName}` **cannot** be used
on multi-property objects (the `LaunchPermission`-style exclusion, `iam-policies-for-amazon-ec2.md:208`). So
there is **no documented way to condition on `EnaSrdEnabled=true` vs `false`** — only all-or-nothing on the
whole struct. *Oracle:* `iam:SimulateCustomPolicy` with `"ec2:Attribute/EnaSrdSpecification"` value conditions
→ expect no value-level match.

**N5-d — PREMISE CORRECTION for Area N3 / hub Area 5: `ModifyImageAttribute` CANNOT touch ENA/SRIOV at all.**
`API_ModifyImageAttribute.md:10,14,21–23` — the `Attribute` parameter's valid values are only
`description | imdsSupport | launchPermission`; L14 explicitly says to enable `SriovNetSupport` you must
enable it on an instance and **create an AMI from the instance**. So `ec2:Attribute` on `ModifyImageAttribute`
(real, `list_ec2.md:8803`) is **irrelevant to ENA/SRIOV** — those flags are set **only** at `RegisterImage`
time (one-way for `SriovNetSupport`), and `RegisterImage`'s `image*` row carries **no `ec2:Attribute` and no
ENA/SRIOV key of any kind** (`list_ec2.md:9319`; JSON `['aws:RequestTag/${TagKey}','aws:TagKeys','ec2:ImageID',
'ec2:Owner']`). **Net:** there is **no narrow IAM/SCP construct to Deny "register/bake an AMI with
`EnaSupport=true`/`SriovNetSupport=simple`"** — the only options are Deny `RegisterImage` wholesale or Deny
`CreateImage`/`RunInstances` on specific ENA/SRIOV-enabled *source* instances (indirect, incomplete). Given
`SriovNetSupport` irreversibility, this is a real customer footgun (architecturally consistent — these are
creation params, not "attribute modifications" — but under-documented as a limitation). This confirms and
scopes Area N3's "no `ec2:Attribute` key governs the attribute on any image write-path."

**N5-e — `RunInstances` has no ENA/SRIOV param or key at all [closes a would-be gap].** Full key inventory of
all 17 `RunInstances` resource rows: no `ec2:Attribute`, no ENA/SRIOV/EnaSrd key. Consistent with
`RunInstances` having no `EnaSupport`/`SriovNetSupport` *input* parameter (grep of `API_RunInstances.md`:
`enaSupport` appears only in a *response* example) — ENA/SRIOV is purely inherited from the AMI/instance
attribute, not a launch-time choice. Note the **contrast**: the IMDS launch-time toggles
(`ec2:MetadataHttpTokens`/`ec2:MetadataHttpEndpoint`/`ec2:MetadataHttpPutResponseHopLimit`) **do** exist on the
`RunInstances` `instance` row — AWS *does* ship condition keys for other security-relevant launch toggles, so
the absence for network-adapter type is a deliberate design consequence (nothing to scope), not an oversight.
**Severity:** N5 overall = Low/Informational per item, but N5-a (casing) and N5-d (RegisterImage bake-in gap)
are the two reportable Tier-2/footgun candidates; the rest are boundary-claim ground-truth for the hunter.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account SRD on a shared subnet | ENA Express attachment | `ena-express.md` silent on cross-account; `API_EnaSrdSpecification` admits it; SG/ACL still evaluated per `ena-nitro-perf.md` (Area N1) |
| Windows enable runbook disables script-signing for a checksum-free installer | `enabling_enhanced_networking.md` Windows flow | *none* — AWS text instructs `Set-ExecutionPolicy Unrestricted` + unpinned `Latest` fetch, no verification step (Area N2) |
| AMI silently inherits enhanced-networking attribute | `CreateImage` | no `ec2:Attribute` value key on any image write-path (hub Area 5); inheritance is automatic (Area N3) |
| Console-only guardrail misses the destructive attribute flip | EC2 console vs CLI | "cannot be managed from the console" forces the flip off-console; queue-count IS console-managed (Area N4) |
| `ec2:Attribute` Deny silently never matches (casing) | `ModifyInstanceAttribute` | *none* — AWS docs mix lowerCamelCase enum (`enaSupport`) and PascalCase param (`EnaSupport`); case-sensitive `StringEquals` fail-open (Area N5-a) |
| No narrow Deny for baking ENA/SRIOV into an AMI | `RegisterImage` | *none* — no `ec2:Attribute`/ENA key on the image row; `ModifyImageAttribute` can't touch it; `SriovNetSupport` irreversible (Area N5-c/d) |

---

## 7. Out-of-Scope Risk Categories
- **Guest-OS driver fetch/build by the customer's own instance** — a guest/client fetch, not a server-side service-plane fetch (no SSRF role). In scope only as the Lens-R audit of AWS's *instructions* (Area N2), not as a service bug. The `github.com/amzn/amzn-drivers` repo's own internal practices are out of scope (Amazon-owned, but still a 3P-repo-behavior exclusion); the absence of a verification step in AWS's referencing instructions is in scope.
- **The SRD transport fabric / Nitro card internals / IMDS on the managed host** — AWS service plane; hard-stop disclosure, not a test target.
- **Single-tenant self-DoS** (bricking your *own* instance by enabling ENA on an incompatible kernel; exhausting your own pps/bandwidth/queue allowance) — product behavior. The *cross-team* bricking primitive is owned by hub Area 5.
- **Performance/feature-parity gaps** (ENA Express not cross-AZ in São Paulo/Bahrain/UAE; not in Local Zones; queue count power-of-2 / ≤vCPU limits) — availability facts, not vulnerabilities.
- Everything in hub Areas 1–7 — execute from the hub plan, do not re-file here.

---

## 8. Null hypotheses / doc gaps
- **Lens G (SSRF): NULL** — read `enhanced-networking-ena.md`, `enabling_enhanced_networking.md`, `test-enhanced-networking-ena.md`, `ena-queues.md`, both troubleshooting pages, both Windows driver pages. Every URL/fetch (`install.ps1` zip, `git clone`) is dereferenced by the customer's **own guest OS**, not by an EC2 control-plane fetch identity. No `*Url`/`*Uri` field the service fetches server-side.
- **Lens H / W / FF / J / DD / CC / BB / EE / N / P / Q: NULL for this page set** — no KMS/encryption-context, attestation gate, JWT/OIDC validation, OAuth linking, caching layer, multi-parser request path, namespace migration, registration/proofing workflow, or untrusted file upload the *service* parses (driver blobs are guest-loaded). EE (AMI trust-confusion on `enaSupport`) specifically REFUTED in Area N3. Pages checked: the full ENA child set named above.
- **Lens A (cross-tenant for ENA Express): downgraded from the hub's NULL to DOC-GAP** — see Area N1. The hub plan's NULL was premised partly on "nothing describes cross-account reach"; `API_EnaSrdSpecification.md` describes a shared-subnet cross-account path. Confirm the establishment behavior (and that SG/ACL still gate it) before closing. Still distinct from the EFA OS-bypass RDMA cross-tenant lead (owned by the `ec2-networking` hub) — ENA Express SRD rides the normal socket/TCP-UDP stack and remains SG-evaluated per `ena-nitro-perf.md`.
- **Lens U (console-manageability claim): contradiction confirmed** — Area N4.
- **Open doc-gaps to confirm before investing:** (1) shared-subnet cross-account SRD establishment + whether SG/ACL is evaluated on that path (Area N1); (2) whether AWS publishes a checksum/signed manifest the Windows runbook omits, and the scope/persistence of `Set-ExecutionPolicy Unrestricted` (Area N2); (3) whether `CreateImage` ever offers an attribute override (Area N3).
- **Mirror-hygiene observation (SUSPECTED PROMPT INJECTION — recorded, not acted on):** the offline UserGuide tree contains leftover non-doc artifacts — `skill-agent_docs.aws.amazon.com_*.html.md` files and a `/work/aws-docs/.cache/ena-*-findings.md` set — some carrying agent-directed text ("HARD STOP", "disclose if observed"). These are prior-run working files, not AWS documentation; a naive grep of the corpus could surface their instruction-shaped text as if it were AWS prose. All findings in this plan are drawn only from genuine `source_url: https://docs.aws.amazon.com/…` pages. Flag to the mirror owner.
- **Drift:** `enhanced-networking-ena.md`, `ena-express.md`, `API_EnaSrdSpecification.md`, `enabling_enhanced_networking.md`, `ena-queues.md`, `test-enhanced-networking-ena.md` re-verified against the offline mirror 2026-10-15; the target page confirmed offline==online byte-identical. Troubleshooting/driver pages carry an inherited no-drift check — re-fetch if a claim becomes load-bearing.
