# Customize the Sample Attestable AMI — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/customize-sample-ami.html` (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/customize-sample-ami.md`, **byte-identical online==offline 2026-10-15**). Supporting: `build-sample-ami.md` (the base build this page modifies), the KIWI NG upstream docs this page links (`repository_setup.html`, `packages.html`, `shell_scripts.html`), the real recipe `github.com/amazonlinux/kiwi-image-descriptions-examples` (`al2023/attestable-image-example/`), and the NitroTPM attestation/enable/verify siblings.
Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Scope — this plan is the CUSTOMIZATION complement of the Attestable-AMI / NitroTPM cluster.** `build-sample-ami` owns the *base* build pipeline, measurement-generation mechanism, the IAM prerequisite block, the coldsnap/EBS-direct path, and the base isolation config. **This page is where the customer is explicitly invited to MODIFY that base** — add repositories, add/remove packages, drop files into the overlay tree, and add auto-executed custom scripts. So this plan OWNS exactly the delta: **how each customization interacts with (a) the in-image package-signature guarantee, (b) the "removes all interactive access / isolated compute" guarantee, (c) the attestation measurement coverage (what the reference PCRs actually fold in), and (d) build-time + first-boot code execution.** It CROSS-REFERENCES and does **not** restate:
> - The base supply chain (KIWI/dnf/coldsnap/cargo/`edit_boot_install.sh`), the measurement-generation mechanism and its reproducibility, the `ebs:*`/`ec2:RegisterImage` IAM prereq block → **`build-sample-ami-attack-research-plan.md`** (Areas 1–5).
> - KMS attestation gate, PCR under-binding, `NitroTPMPCR12`=all-zeros, replay/CRL/COSE → **`nitrotpm-attestation-attack-research-plan.md`** (A1–A8).
> - RegisterImage register-time co-params (`--tpm-support`/`--boot-mode`/`--uefi-data`/`--imds-support` IAM-ungatability; foreign-snapshot provenance) → **`enable-nitrotpm-support-on-ami-attack-research-plan.md`**.
> - `DescribeImages` unscopable read oracle / "verify = read a self-asserted flag" → **`verify-nitrotpm-support-on-ami-attack-research-plan.md`**.
> - `GetInstanceTpmEkPub`, launch prerequisites, BitLocker, instance-type change → the NitroTPM hub + `enable-nitrotpm-prerequisites` + `retrieve-ekpub` plans.
> All are children of the EC2 Security hub (NitroTPM = Area 2).

> **Central design fact inherited from the cluster (every lead leans on it):** an Attestable AMI's trust is **measurement-based, not identity-based** — the Attestation Document and PCR4/7/12 carry **no account/owner field** (established in `build-sample-ami` §Design + the attestation sibling). "This exact boot code is provable; built-by-this-account is not." **Customization is the operator's lever to change what gets measured — and therefore the lever to put code in a place attestation never looks.**

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- This page introduces **no new AWS API, IAM policy, role, or network interface** — it is pure KIWI-recipe guidance. So the firing lenses are **U (guarantee-vs-enforcement), W (attestation coverage), EE (predictable-path overwrite/land-grab), Q (untrusted content baked into the measured image), R/Y (supply-chain / transport of custom repos)**. The classic API/IAM/tenant lenses (A/B/C/D/E/F/H/I/J/…) are **null here and deferred to the siblings** — see §8, which names the pages checked.
- **The safe first oracle for a measurement-scope question is NOT a live KMS call** — it is a *build-time* experiment: build two images differing only in a customization, run `nitro-tpm-pcr-compute`, and diff the emitted PCRs. No victim resource is touched.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the Nitro hypervisor signing path, the NitroTPM device, AWS's attestation CA/KDS), stop, preserve evidence, flag for AWS-Security disclosure. The attestation *signing* chain is AWS-owned and out of scope — only the customer-authored measurement/recipe/supply-chain inputs are in scope.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Attested-but-backdoored image (headline):** apply a *documented, invited* customization (an added package, an overlay file, a first-boot script) that lands attacker/operator code into an image which **still produces PCR4/7/12 equal to a clean reference** (or whose reference the operator ships), so the image passes a downstream KMS attestation policy while running code the "attestable" posture implies is absent.
2. **Measurer forging via overlay overwrite:** use the overlay tree's documented "existing files are overwritten" behavior to replace `/usr/bin/nitro-tpm-pcr-compute` (or boot inputs) *before* `edit_boot_install.sh` self-measures, so the shipped `pcr_measurements.json` is attacker-chosen.
3. **Signature-guarantee defeat via custom repo:** add a `<repository>` (as the page invites) that is unsigned and/or `http://`, re-opening the per-repo GPG check the base recipe closed, so an unsigned/MITM'd package is baked into the attested AMI.
4. **Isolation-guarantee undo:** re-introduce an interactive-access package (`openssh-server`, `amazon-ssm-agent`, `cloud-init`) via `<packages>`, defeating the page's sibling "removes all interactive access … isolated compute environment" claim — and determine whether that change is reflected in the attestation at all.
5. **Stealth build-host code-exec:** drop a correctly-named KIWI script into the recipe directory so it auto-executes at build (host-root for the non-chrooted hooks) **with no reference in `appliance.kiwi`**, defeating a reviewer who audits only the image-description file.

## 2. Components, Assets, and Design

**What the page actually does.** It is AWS-authored guidance for editing the public KIWI NG image description (`appliance.kiwi` + its directory) that `build-sample-ami` builds into an Attestable AMI. Four invited customization surfaces, each a seam into the measured/isolated artifact:

```
 appliance.kiwi  (the KIWI image description — customer edits it)
 ├── <repository …>        ← "Repository management": add other repos; sample uses AL2023 core mirror endpoint
 │        │                   (per-repo package_gpgcheck / http-vs-https / NEVRA pinning = supply-chain posture)
 ├── <packages>            ← "Package management": ADD packages (install into AMI) or REMOVE/uninstall them
 │        │                   (re-add openssh/ssm/cloud-init? remove veritysetup/erofs/nitro-tpm tools?)
 ├── overlay tree  root/   ← "Adding files and directories": copied into rootfs AFTER packages;
 │        │                   "New files are added and existing files are OVERWRITTEN"
 │        │                   (overwrite the measurer / boot files / authorized_keys / systemd units)
 └── <scripts by filename> ← "Adding custom scripts": KIWI auto-detects+executes by name, NO explicit reference;
                              run "during the image build process OR AT FIRST BOOT of the image"
   │
   ▼  kiwi-ng system build  →  erofs read-only root + dm-verity + UKI(.efi)
   │     └── edit_boot_install.sh (ROOT, build host): runs image's OWN /usr/bin/nitro-tpm-pcr-compute
   │          → ./image/pcr_measurements.json {PCR4, PCR7, PCR12, SHA384}        [reference identity]
   ▼  coldsnap upload → snapshot → register-image --tpm-support v2.0 → Attestable AMI
   ▼  (later) launch → NitroTPM measures boot → Attestation Document → consumer KMS policy vends secret
```

**Assets (what customization puts at risk):**
- **The reference PCR measurements** (`pcr_measurements.json`). What they *fold in* is the crux: if a customization lands in a measured region the PCRs change (a clean-pinned verifier rejects); if it lands in an **un-measured** region (first-boot runtime, ephemeral overlay, non-root volume, or a rootfs region the measurer doesn't hash) the image is **attested-clean but modified**. This page is the invited way to choose that region.
- **The in-image package-signature guarantee** — established per-repo in the base recipe (`rpm-check-signatures=true` + per-repo `package_gpgcheck="true"`, `build-sample-ami` Area 4 fact 2). Adding a repo is the invited way to re-open it.
- **The "isolated / no interactive access" posture** — enforced by package *omission* (`<ignore>` of openssh-server/ec2-instance-connect/amazon-ssm-agent/cloud-init/update-motd/firewalld, `build-sample-ami` Area 5). Adding packages is the invited way to undo it.
- **The build host (operator root)** and **the measurer binary** — both reachable by overlay-overwrite and by auto-detected scripts.

**Identity / trust model:** everything here runs under the **operator's own account/identity** at build time (no SLR, no PassRole, no AWS API on this page). There is **no cross-tenant surface on this page** — the breach boundaries are (i) *recipe-author/supply-chain → the attested artifact's measurement/isolation guarantee* and (ii) *build dependency/overlay/script → build-host root + forged reference*. The downstream cross-account consequence (a victim KMS policy vending to an attested-but-backdoored image) lives in the attestation sibling; this page owns the *input* that makes it possible.

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Recipe author / anyone who can influence the recipe directory | The attested AMI's "describes exactly what code runs" guarantee | Add package / overlay file / first-boot script landing in an **un-measured** region | A documented customization lands code in the booted image while PCR4/7/12 are **unchanged** from a clean build (or the operator ships the matching reference) → attested-but-modified |
| Overlay tree (`root/`) | The measurer `/usr/bin/nitro-tpm-pcr-compute` + boot files | "existing files are **overwritten**", copied before `edit_boot_install.sh` self-measures | Overlay-placed binary at the measurer's path is the one that generates `pcr_measurements.json` → attacker-chosen reference |
| Custom `<repository>` origin | The attested image's package set | `dnf` install from a repo whose `package_gpgcheck`/transport the customer sets | An unsigned or `http://`-fetched package is baked into the AMI (signature guarantee was per-repo, re-opened by the add) |
| Added `<packages>` | The "no interactive access / isolated" guarantee | `dnf install openssh-server`/`amazon-ssm-agent`/`cloud-init` | A shell/SSM/user-data channel exists on an image the sibling page says has "all interactive access removed" |
| Correctly-named script in the recipe dir | Build-host root (operator) + the artifact | KIWI auto-detect-by-filename, **no reference in `appliance.kiwi`** | A script runs at build (host-root for non-chrooted hooks) or first boot, invisible to a reviewer auditing only `appliance.kiwi` |
| **Any customer surface** | **AWS Nitro signing / NitroTPM device / attestation CA** | — | **HARD STOP** — AWS service plane, out of scope |

## 4. API / Interface Inventory

**No AWS SDK/console/control-plane API is introduced on this page.** The "interfaces" are all KIWI NG recipe elements (operator-side, build-time). Listed for completeness; the control-plane surface (`ebs:*`, `ec2:RegisterImage`) is owned by `build-sample-ami` §4.

| Name | Type | Mut/Non | Int/Ext | Functionality | Notes |
|---|---|---|---|---|---|
| `<repository>` element | KIWI recipe | — (build-time) | operator-side | Declares a dnf repo to install from | Per-repo `package_gpgcheck`, URL transport, NEVRA pinning = supply-chain posture (Area 3) |
| `<packages>` element | KIWI recipe | — | operator-side | Install (or `<package>`-remove) software into the AMI | Re-add interactive-access pkgs / remove integrity tooling (Areas 1, 6) |
| Overlay tree `root/` | KIWI directory | — | operator-side | Files copied verbatim into rootfs after packages; **overwrites existing** | Overwrite measurer/boot/authorized_keys (Area 4) |
| Custom scripts (`config.sh`, `config-overlay.sh`, `config-host-overlay.sh`, `pre_disk_sync.sh`, `disk.sh`, `images.sh`, `post_bootstrap.sh`, editbootinstall `*.sh`, …) | KIWI auto-detect-by-filename | — | operator-side / build-host | Run during build (chrooted or host-root per type) or at first boot | No explicit reference in `appliance.kiwi` (Area 5) |
| `nitro-tpm-pcr-compute` | local binary (in image) | — | — | Generates `pcr_measurements.json` from image content | Self-measures; overwritable via overlay (Area 4) |

The **under-tested surface** is exactly this operator/build-time tooling — hunters skip it because it is not an `ec2:*` control-plane call, yet it is where the attested artifact's integrity is actually decided.

## 5. Recommended Areas of Focus

### Area 1 — Invited customizations can put code in a region attestation never measures (Lens U / W) — PRIMARY / HEADLINE
**Background.** The whole value proposition is that PCR4/7/12 "describe exactly what code an instance will execute," and a consumer builds a KMS policy that vends secrets only to instances presenting a trusted PCR set. **This page explicitly invites the operator to add packages, drop files into the rootfs, and add scripts** — i.e. to change what the image runs. The load-bearing question (carried **OPEN** from `build-sample-ami` Area 1 / §8 #1): **what does `nitro-tpm-pcr-compute --image <UKI.efi>` actually fold in — only the UKI (kernel+initrd+cmdline), or the full erofs rootfs via the dm-verity root hash embedded in the kernel cmdline (→ PCR12)?**

**NEW EVIDENCE (subagent 2026-10-15, from `edit_boot_install.sh` + repo README):**
- **CONFIRMED — the measurer is only ever pointed at the UKI file.** The actual invocation is `sudo "$root_mount/usr/bin/nitro-tpm-pcr-compute" --image "$efi_mount/EFI/BOOT/$EFI_BINARY"` — it hashes the UKI binary, **never the erofs rootfs or any other file**. Its own doc header: *"locates the UKI (kiwi.efi) … calculates PCR4 and PCR7 values."*
- **CONFIRMED — the example repo's tool/README emit `PCR4` + `PCR7` only; NO `PCR12` field.** The AWS `build-sample-ami.md` page's example JSON *does* show PCR12. **The PCR12 disagreement is now confirmed by direct comparison**, not just inferred — the thing a verifier might pin (PCR12, to catch rootfs change) may not be produced by the tool at all.
- **CONFIRMED — package add/remove changes erofs content → changes the dm-verity root hash** (recipe sets `verity_blocks="all"` = full coverage). **DOC-GAP — whether that root-hash change propagates into any *measured* PCR is NOT stated anywhere.** The roothash-into-UKI-cmdline injection (standard dracut `dracut-kiwi-verity` pattern) is plausible but **unconfirmed in any AWS or KIWI doc**, and the static `kernelcmdline` in `appliance.kiwi` contains no roothash literal.

**Security Concern — the evidence tilts hard toward the Critical branch; resolve the one remaining link.**
1. **If the erofs root hash does NOT reach a measured PCR (strongly supported — the tool demonstrably hashes only the UKI):** a package added via `<packages>` (e.g. `openssh-server`) or a backdoor binary / `authorized_keys` dropped in the overlay tree lands in the booted rootfs but **does not change the measured PCRs** → the image is **attested-identical to a clean build while carrying attacker/operator-added code**. Realizes the "untrusted AMI with matching measurements" case AWS itself warns about, now via a *documented* customization. **Critical.** Reinforced by the `<ignore>`-is-not-a-deny-list finding (Area 6): re-adding `openssh-server` is a trivial unguarded `<package>` line.
2. **If the root hash IS folded (via a cmdline value embedded in the UKI before measurement):** a rootfs-landing customization *changes* the UKI → changes PCR4 → a clean-pinned verifier rejects. This branch REFUTES the package/overlay bypass. Surviving vector = any region excluded **by construction**: (a) **first-boot scripts** (Area 2, CONFIRMED outside build-time measurement), (b) the **ephemeral runtime overlay**, (c) a **non-root / secondary EBS volume**, (d) data pulled at runtime. Severity High (attestation TOCTOU).

**High-level Test Scenarios.**
- **Claim:** Build image A (clean) and image B (A + `openssh-server` in `<packages>`, or a backdoor file in `root/`); `nitro-tpm-pcr-compute` emits **identical** PCRs for both. → *Oracle:* the build-time two-build diff — **no live KMS, no victim**. Given the CONFIRMED UKI-only hashing, the decisive sub-question is purely *does the erofs roothash land in the UKI's embedded cmdline before `--image` is run?* Inspect the built UKI's embedded cmdline (`objdump`/`ukify` the `.efi`) for a `roothash=`/`rd.verity` value → if absent, Case 1 confirmed (Critical). → *Severity:* Critical if match.
- **Claim:** A verifier pins PCR12 (per AWS's example JSON) but the deployed tool emits only PCR4/7 → the pinned PCR is never populated, or populated as all-zeros (cross-ref attestation sibling A2: `NitroTPMPCR12`=all-zeros). → *Oracle:* confirm the running tool's emitted PCR set vs the KMS policy's pinned set. → *Severity:* High (verifier binding a dead PCR).
- *Cost:* build-time + static UKI inspection only. *Stop condition:* roothash-in-UKI-cmdline link resolved and the two-build PCR diff recorded; **do not attack a live victim KMS policy** — route the downstream vend to the attestation plan + authorization.

### Area 2 — "At first boot" custom scripts = un-measured runtime code on an attestation-grade instance (Lens U / W / K-adjacent) — HIGH
**Background.** The page: *"you can include your own custom scripts … to perform tasks or configurations during the image build process **or at first boot of the image**."* NitroTPM measures the **boot** (into PCRs) and the attestation document is a **boot-state snapshot** (`build-sample-ami` Area 6: attestation = boot-state only, in-memory/runtime changes never re-extend PCRs = TOCTOU).

**Security Concern.** Code that runs **at first boot** executes *after* the boot measurement that the Attestation Document captures. So any first-boot script (whether operator-added or slipped in by a supply-chain/overlay attacker) is **runtime code the attestation can never reflect** — the instance presents a trusted PCR set and *then* runs the script. This is the invited, documented form of the TOCTOU: the page tells customers first-boot scripting is a supported customization, with no caveat that first-boot code is outside the attested measurement. Chains Area 1 Case 2 (the surviving un-measured vector) + `build-sample-ami` Areas 5/6.

**NEW EVIDENCE (subagent 2026-10-15):**
- **CONFIRMED — first-boot code is NOT measured into the reference PCRs.** `nitro-tpm-pcr-compute` runs **once, at build time**, over the static UKI, before the AMI ever launches. Anything that runs only at instance first-boot executes *after* measured boot has already extended PCR4/PCR7 from that static UKI → first-boot code is not folded into those PCRs (confirmed logically from the single build-time invocation).
- **DOC-GAP / contradiction — "at first boot" is NOT a KIWI build-script mechanism.** The subagent walked the full KIWI `shell_scripts.html` matrix: *every* auto-detected script hook (`post_bootstrap.sh`, `config.sh`, `config-overlay.sh`, `config-host-overlay.sh`, `images.sh`, `pre_disk_sync.sh`, `disk.sh`, `editbootconfig`, `editbootinstall`) is a **build-time** hook (chrooted during build or host-side during disk assembly). **None run "at first boot of the running instance."** AWS's exact sentence — *"to perform tasks or configurations during the image build process or at first boot of the image"* — is **unsubstantiated by any cited KIWI script type.** The only plausible real mechanism (INFERRED, not doc-confirmed) is a **systemd unit placed via the overlay tree** (the recipe already uses exactly this for `set-hostname-imds.service` via `root/etc/systemd/system/…` + `config.sh`'s `systemctl preset`). This makes Area 2 and Area 4 (overlay) the **same primitive**: "first boot" = an overlay-placed systemd unit = un-measured runtime code.

**High-level Test Scenarios.**
- **Claim:** An overlay-placed systemd unit (the recipe's own `set-hostname-imds.service` pattern) runs on the launched instance while the reference PCRs remain the clean set → attested instance executes un-measured code. → *Oracle:* reproduce the recipe's `root/etc/systemd/system/…` + `systemctl preset` pattern with an attacker payload; confirm it is a first-boot/runtime unit not folded into any build-time PCR (CONFIRMED by construction). → *Severity:* High (defeats "describes exactly what code runs" for everything after boot).
- **Claim:** AWS's "or at first boot" guidance has no mechanism in the linked KIWI docs and no measurement caveat. → *Oracle:* doc read (CONFIRMED — unsubstantiated + no caveat). → *Severity:* Low as a doc-defect, High as the enabler. 
- *Stop condition:* overlay-systemd first-boot path reproduced at build/launch level; measurement exclusion already CONFIRMED.

### Area 3 — A custom `<repository>` re-opens the per-repo signature guarantee; `http://` and unpinned allowed (Lens R / Y / U / EE) — HIGH
**Background.** `build-sample-ami` Area 4 fact 2 established that packages baked **into the image** are GPG-verified **because the base recipe sets** `<rpm-check-signatures>true` + per-repo `package_gpgcheck="true"` and `add-gpg-key.sh` pins the AL2023 key. Signature enforcement is therefore **per-repository configuration**, not a global invariant. This page: *"you can add references to other repositories from which to install your required software"* and links KIWI `repository_setup`.

**NEW EVIDENCE (subagent 2026-10-15, from KIWI `repository_setup.html` + `appliance.kiwi`):**
- **CONFIRMED — the KIWI per-repo default is `package_gpgcheck="false"`** (verbatim: *"If not set, the default value is `false`."*) and `repository_gpgcheck` likewise defaults to `false`. The sample closes this only because it **explicitly** sets `package_gpgcheck="true"` on its sole repo plus `customize="add-gpg-key.sh"` (injects `gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-amazon-linux-2023`) and the global `<rpm-check-signatures>true`.
- **A customer-added `<repository>` therefore defaults to UNSIGNED-per-repo** unless the operator replicates all three settings — and the AWS page's add-a-repo guidance says nothing about any of them.
- **DOC-GAP — the precedence between global `rpm-check-signatures="true"` and a per-repo `package_gpgcheck="false"` is NOT stated** in the KIWI doc (it documents the two switches independently, not their interaction). So whether the global flag still forces a check on an unconfigured repo, or the per-repo default wins, is unresolved — a decisive sub-question for severity.
- **CONFIRMED — `http://` (and `ftp://`) repo URLs are accepted** (verbatim: *"http://URL or https://URL or ftp://URL"*).

**Security Concern.** Three sub-concerns, now evidence-backed:
1. **Signature re-opening (default-insecure):** an added repo installs **unsigned** packages into the attested image unless the operator explicitly sets `package_gpgcheck="true"` — the KIWI default is `false`, the integrity guarantee the base recipe closed is per-repo, and the AWS page invites the add with no caveat. (Lens R/U — AWS-authored invitation + insecure-default = Tier-2.)
2. **Cleartext transport (Lens Y):** a custom `http://` repo → MITM of the package stream into an "attestable" build. The base sample's own repo already uses a floating `mirrors/latest` endpoint (unpinned NEVRA, `build-sample-ami` Area 1 fact 1) — so even the shipped default lacks version pinning; a custom repo compounds it.
3. **Namespace/land-grab (Lens EE):** a custom repo + a package name shadowing a base package or a `<namedCollection>` dependency → attacker package selected, subject to repo priority/cost (dnf resolution). Owner-pinning is the operator's job; the page gives no guidance.

**High-level Test Scenarios.**
- **Claim:** A `<repository>` added per the page's guidance, lacking `package_gpgcheck="true"`, installs an unsigned package into the AMI. → *Oracle:* resolve the global-vs-per-repo precedence DOC-GAP (build with global `rpm-check-signatures="true"` + a repo at `package_gpgcheck` default + an unsigned package; observe whether the install is rejected). → *Severity:* High if the unsigned package is baked in (unsigned code into attested image).
- **Claim:** An `http://` custom repo (CONFIRMED accepted) allows MITM of the package stream. → *Severity:* High on the attestation path.
- *Preconditions:* operator follows the page's add-a-repo guidance (AWS-authored invitation + CONFIRMED insecure default → Tier-2, not a pure customer footgun). *Stop condition:* precedence DOC-GAP resolved. **Do not stand up a malicious repo against anyone else's build.**

### Area 4 — Overlay tree "existing files are overwritten" → overwrite the self-measurer before it measures (Lens EE / Q / U) — HIGH / HEADLINE supply-chain
**Background.** The page: *"The overlay tree directory … files and directories … will be copied directly into the root filesystem … **copied into the image after all the packages have been installed. New files are added and existing files are overwritten.**"* `build-sample-ami` Area 1 fact 3 / Area 4 fact 4: `edit_boot_install.sh` runs the image's **own freshly-installed** `/usr/bin/nitro-tpm-pcr-compute` (as root) to generate the reference `pcr_measurements.json` — measurer and measured come from the same pipeline.

**NEW EVIDENCE (subagent 2026-10-15, from KIWI `shell_scripts.html` + `edit_boot_install.sh` source):**
- **CONFIRMED — the phase ordering holds.** Overlay-tree copy happens in the **prepare** phase (early): `config.sh` *"runs at the end of the [prepare step] and after … the overlay tree directory has been applied."* `editbootinstall` (= `edit_boot_install.sh`'s role) is *"called as the very last step of the disk build, after the bootloader has been installed."* So the overlay tree is already in the root tree **before** the measurer runs.
- **CONFIRMED — `edit_boot_install.sh` executes the binary at the overwritable path.** Its invocation is `sudo "$root_mount/usr/bin/nitro-tpm-pcr-compute" …` — it runs whatever binary occupies `/usr/bin/nitro-tpm-pcr-compute` **in the just-built root partition**, i.e. the overlay-overwritten copy if one was placed there. **The measurer-overwrite mechanism is logically confirmed.**

**Security Concern.** The overlay copy overwrites existing files, happens **after package install**, and (CONFIRMED) **precedes** the `editbootinstall` measurer run. A file placed at **`root/usr/bin/nitro-tpm-pcr-compute`** in the overlay tree **overwrites the measurer**, and the overwritten (attacker/operator-chosen) binary is the one `edit_boot_install.sh` then runs → the shipped reference measurements are **attacker-chosen** (forged to match whatever payload the image actually carries). Adjacent overwrite targets (Lens Q/EE — the overlay occupies predictable, build-trusted paths): systemd units (= the Area 2 first-boot primitive), the UKI/boot inputs, `authorized_keys`, PAM/sshd config if SSH is re-added. This is the **sharpest, most invited build-poisoning primitive on the page** — the overlay is unreviewed-by-construction ("copied directly … existing files overwritten"), and nothing on the page warns that it can overwrite the measurement toolchain.

**High-level Test Scenarios.**
- **Claim:** `root/usr/bin/nitro-tpm-pcr-compute` in the overlay tree replaces the dnf-installed measurer, and `edit_boot_install.sh` runs the replacement → forged `pcr_measurements.json`. → *Oracle:* phase ordering CONFIRMED; build with a stub measurer in the overlay and observe the emitted JSON matches the stub's output. → *Severity:* High–Critical (forges the reference the entire attestation trust rests on; chains to the attestation sibling's A1 "reproducible-measurement bypass" — this is the *build-poisoning* input to it).
- **Claim:** The overlay can overwrite boot/isolation files (sshd config, systemd units) to undo hardening while — per Area 1 — possibly not changing PCRs. → *Oracle:* overwrite + two-build PCR diff. → *Severity:* High.
- *Stop condition:* phase ordering + measurer-overwrite behavior resolved at doc/repo level, or via a local build-only experiment. **No live victim.**

### Area 5 — Custom scripts auto-executed by filename, with no reference in `appliance.kiwi` = review blind spot + build-host root (Lens R / Q) — MEDIUM
**Background.** The page: *"KIWI NG automatically detects and executes the scripts if they are named correctly and placed in the correct location, **without the need to explicitly reference them in the image description file**."* `build-sample-ami` Area 4: KIWI auto-execs by filename; the `edit_boot_install.sh`/editbootinstall hook and `config-host-overlay.sh` run **NOT chrooted = build-host root**; others (`config.sh`, `config-overlay.sh`) run chrooted in the image.

**NEW EVIDENCE (subagent 2026-10-15, full `shell_scripts.html` matrix):** chrooted vs host, per script —
`post_bootstrap.sh`, `config.sh`, `config-overlay.sh`, `images.sh`, `pre_disk_sync.sh` = **chrooted**; `disk.sh` = chrooted into the virtual disk; **`config-host-overlay.sh` = NOT chrooted / host (but docker/oci `delta_root="true"` builds only)**; **`editbootconfig` and `editbootinstall` = NOT chrooted / host (oem disk builds only).** For this sample (an **oem disk build**), the host-root hook that actually fires is **`editbootinstall` (`edit_boot_install.sh`)** — which is *also* the measurer-running script (Area 4). `config-host-overlay.sh` likely does **not** apply to this build type (delta_root-only) — note the discrepancy rather than assume it runs.

**Security Concern.**
1. **Review blind spot (CONFIRMED mechanism):** scripts are detected by *filename* and *"without the need to explicitly reference them in the image description file."* A reviewer auditing only `appliance.kiwi` **will not see them**. A supply-chain actor who can drop a correctly-named file into the recipe directory (or a malicious example recipe) gets **auto-execution at build time with zero reference in the audited file** — a stealthy code-exec/measurer-forge primitive (chains Area 4: the host-root `editbootinstall` can rewrite `pcr_measurements.json` directly).
2. **Build-host root (CONFIRMED):** `editbootinstall` runs NOT chrooted = build-host root; a malicious `edit_boot_install.sh` (or a same-named drop-in) escapes the image sandbox onto the operator's build EC2.
3. **Scope caveat:** scripts the *operator themselves* author into *their own* recipe are a customer footgun (lower severity). The in-scope angle is the **AWS-authored invitation + auto-detect-by-filename design** that makes a *slipped-in* or *example-provided* script invisible — Lens-R/U, because AWS's tutorial promotes a build pattern with no "audit scripts by filename, not just the description" caveat.

**High-level Test Scenarios.**
- **Claim:** A correctly-named host-level script (`edit_boot_install.sh`/`editbootinstall`) in the recipe dir runs as build-host root with no entry in `appliance.kiwi`. → *Oracle:* matrix CONFIRMED; demonstrate a drop-in script executing at build without an `appliance.kiwi` reference. → *Severity:* Medium (build-host root, preconditioned on recipe-dir write / malicious example).
- *Stop condition:* matrix documented (done); demonstrate the no-reference auto-exec.

### Area 6 — Package REMOVAL can silently strip integrity/measurement controls (Lens U) — LOW–MEDIUM
**Background.** The page: *"You can also use the `<packages>` element to uninstall or delete specific software packages."*

**NEW EVIDENCE (subagent 2026-10-15):** the base recipe's "zero operator access" is enforced purely by `<ignore>` entries — CONFIRMED list: `openssh-server`, `amazon-ssm-agent`, `cloud-init`, `cloud-init-cfg-ec2`, `update-motd`, `ec2-instance-connect` (+ `firewalld` under a separate comment). **CONFIRMED — `<ignore>` only suppresses a package from being *pulled in as a dependency*; it is NOT a block/deny-list.** A customer `<packages>` section with `<package name="openssh-server"/>` simply tells `dnf` to install it like any other package. **CONFIRMED — no doc-stated or recipe-enforced guardrail exists against re-adding the stripped packages** (nothing in `appliance.kiwi`, `config.sh`, `add-gpg-key.sh`, the README, or the AWS page prevents it). This is the mechanism behind Area 1's "re-add interactive access" case and sharpens it: the isolation guarantee is a *soft default*, trivially and unguardedly reversible.

**Security Concern.** Two directions:
1. **Re-add (undo isolation):** `<package name="openssh-server"/>` (or `amazon-ssm-agent`/`cloud-init`/`ec2-instance-connect`) re-introduces the exact interactive-access channel the sibling page claims is removed — unguarded, and (per Area 1) possibly without changing the measured PCRs. Chains Area 1.
2. **Remove (strip integrity):** removing `veritysetup`/`erofs-utils`, the measurer tooling, or other hardening produces an image that may still *appear* to be an Attestable AMI build but has weakened/absent integrity enforcement. The page gives no load-bearing-package list.

**High-level Test Scenarios.**
- **Claim:** `<package name="openssh-server"/>` in a customer `<packages>` block installs sshd into the image despite the base `<ignore>` — CONFIRMED by KIWI semantics; the open question is whether it moves the measured PCRs (→ Area 1 experiment). → *Severity:* High if PCR-invisible (attested image with a live shell).
- **Claim:** Removing a verity/erofs package yields a build that still registers `--tpm-support v2.0` but lacks runtime integrity. → *Oracle:* build with the package removed; observe build success + posture. → *Severity:* Low–Medium (footgun; AWS-authored insofar as the page invites removal with no load-bearing list).
- *Stop condition:* re-add PCR-visibility settled with Area 1; which removals break vs silently weaken documented.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Added package / overlay file lands code in an un-measured region → attested-identical to clean build | `<packages>` / overlay tree vs `nitro-tpm-pcr-compute` scope | "PCRs describe exactly what code runs" (measurement-as-identity; scope unspecified on page) |
| First-boot custom script runs after boot measurement → un-measured runtime code | custom scripts "at first boot" | Attestation = boot-state only (no page caveat) |
| Custom `<repository>` without `package_gpgcheck` / over `http://` → unsigned pkg in attested AMI | `<repository>` | Per-repo signature config (base recipe only; page invites add w/o caveat) |
| Overlay overwrites `/usr/bin/nitro-tpm-pcr-compute` before self-measure → forged reference | overlay tree | "existing files are overwritten" (no caveat it can hit the measurer) |
| Re-add `openssh-server`/`amazon-ssm-agent`/`cloud-init` → interactive access on "isolated" image | `<packages>` | Sibling claim "removes all interactive access … isolated compute environment" |
| Correctly-named script auto-executed, unreferenced in `appliance.kiwi` → stealth build-host root | custom scripts | "automatically detects and executes … without … explicitly reference" (promoted, not warned) |
| Remove integrity/measurement package → weakened but still "attestable" image | `<packages>` remove | None stated |

## 7. Out-of-Scope Risk Categories
- **The AWS attestation signing chain** — Nitro hypervisor signature, NitroTPM device, AWS attestation CA/KDS/CRL. **HARD STOP** on any evidence reaching these.
- **KMS attestation-policy mechanics** (PCR under-binding, all-zero/`NitroTPMPCR12`, replay/freshness, CRL-disabled, COSE alg-pin) — owned by `nitrotpm-attestation-attack-research-plan.md`; chain into it, don't re-derive.
- **The base build pipeline, measurement-generation mechanism, coldsnap/EBS-direct path, and the `ebs:*`/`ec2:RegisterImage` IAM prerequisite block** — owned by `build-sample-ami-attack-research-plan.md`. This plan only adds the *customization delta*.
- **RegisterImage register-time co-parameters** and **foreign-snapshot provenance** — owned by `enable-nitrotpm-support-on-ami-attack-research-plan.md`.
- **The read/verify path** (`DescribeImages` oracle, "verify = self-asserted flag") — owned by `verify-nitrotpm-support-on-ami-attack-research-plan.md`.
- **Bugs in KIWI NG upstream itself** (parser, overlay engine) — in scope only where AWS's published tutorial *invites* an unpinned/unsigned/unreviewed composition (that composition is Lens R/U here).
- **A least-privilege or integrity footgun a customer inflicts on a recipe THEY authored** — out of scope. BUT the **sample recipe** and the **page's own invitations** (add-a-repo with no gpgcheck caveat; first-boot scripting with no measurement caveat; overlay-overwrite with no measurer caveat) are **AWS-authored** → in scope as Lens R/U, **Tier-2** reportable.
- **IMDS on the self-built host, single-tenant self-DoS.**

## 8. Null hypotheses / doc gaps
Pages checked for triggers: `customize-sample-ami.md` (the full target page — all four sections: Repository/Package/Files/Scripts), cross-read against `build-sample-ami.md` and the KIWI docs this page links.
- **Lens A / cross-tenant IDOR:** NULL — this page exposes no resource-by-id API, no tenant/customer id, no shared service account. Everything is operator-local build-time recipe editing. (Downstream cross-account consequence lives in the attestation sibling.)
- **Lens B / C (PassRole / credential vending):** NULL — no role ARN, no STS, no SLR anywhere on this page; build runs under the operator's own identity.
- **Lens D / V (data→control plane / network segmentation):** NULL — no ENI, VPC, control plane, or network interface introduced; the page is pre-launch build guidance.
- **Lens G (SSRF):** NULL — checked all four sections. Every fetch the page implies (`dnf` from a `<repository>`, `git`/`cargo` in the base build, KIWI pulling packages) is **operator/build-host-side**, not a value the *AWS service* dereferences server-side. No `*Url`/`*Uri`/webhook/validation field exists on this page. (The `--uefi-data` fetch question belongs to `enable-nitrotpm`.) 
- **Lens F / H / I / J / M / N / O / T / AA / BB / CC / DD / FF:** NULL — no translation layer, KMS key field, tagging API, OAuth/3P link, session id, namespace migration, audit-log surface, secret-persistence location, share/revoke operation, multi-parser request path, upstream-identity header, cache layer, or JWT/token validation is present on this prose page. All are deferred to the siblings where the corresponding mechanism actually lives.
- **Lens Q (upload):** FIRES as "untrusted content baked into the measured image" (overlay files + scripts) — covered in Areas 4/5 (there is no HTTP upload endpoint; the "upload" is the operator placing files in the recipe, so it is Lens-Q *content-trust*, not a web-upload parser).
- **Lens L (DoS):** low — a maliciously large overlay / zip-bomb package could bloat the build or the AMI, but it is a single-tenant build-time self-DoS (operator's own build host); not developed.

**RESOLVED by subagent (2026-10-15):**
- ✅ **KIWI build phase ordering** (Area 4) — overlay copy = prepare phase (early); `editbootinstall` = very last step of disk build. Overlay precedes the measurer. **Measurer-overwrite mechanism CONFIRMED.**
- ✅ **KIWI per-repo `package_gpgcheck` default** (Area 3) — **`false`**. Added repos are unsigned-per-repo unless explicitly set to `true`. `http://`/`ftp://` repos accepted.
- ✅ **KIWI "first boot" mechanism** (Area 2) — **no KIWI build-script hook runs at instance first-boot; AWS's "or at first boot" claim is unsubstantiated.** Plausible real mechanism = overlay-placed systemd unit (= Area 4 primitive). First-boot code CONFIRMED outside the build-time static-UKI measurement.
- ✅ **Measurer scope — the tool only ever hashes the UKI file** (`--image …/EFI/BOOT/$EFI_BINARY`), never erofs. Package add/remove changes erofs + dm-verity roothash (CONFIRMED), but whether that reaches a measured PCR is still open (below).
- ✅ **`<ignore>` is not a deny-list** (Area 6) — re-adding stripped packages is a trivial unguarded `<package>` line.

**STILL OPEN (settle first, highest value):**
1. **Does the erofs dm-verity root hash reach a measured PCR?** (Area 1 — the one remaining link.) The tool hashes only the UKI; the question is whether `dracut-kiwi-verity` injects the roothash into the UKI's embedded cmdline **before** `--image` runs. **Oracle:** `objdump`/`ukify` the built `.efi` and look for a `roothash=`/`rd.verity` literal in the embedded cmdline. Absent → added packages/overlay files are **attested-invisible** (Critical). Present → rootfs changes move PCR4 (High via first-boot/ephemeral residual only). *This single static inspection decides the headline severity.*
2. **Global `rpm-check-signatures="true"` vs per-repo `package_gpgcheck="false"` precedence** (Area 3) — does the global flag still force a check on an unconfigured custom repo, or does the per-repo default win? Decides whether added-repo packages are truly unsigned.
3. **PCR12 existence/semantics** — the example repo's tool emits PCR4/7 only; AWS's `build-sample-ami` example JSON shows PCR12. Does the deployed tool emit PCR12, and does it carry the verity roothash (vs the attestation sibling's A2 all-zeros finding)? A verifier pinning PCR12 may be pinning a dead/zero register.

---
*Companion to the NitroTPM / Attestable-AMI cluster: `build-sample-ami` (base build/supply-chain/measurement — this plan's primary sibling), `attestable-ami`, `nitrotpm-attestation`, `enable-nitrotpm-support-on-ami`, `enable-nitrotpm-prerequisites`, `verify-nitrotpm-support-on-ami`, `verify-nitrotpm-support-on-instance`, `retrieve-ekpub`, `nitrotpm-instance`, and the `nitrotpm` hub (EC2 Security Area 2). This plan owns the **customization delta** — how added repos/packages/overlay-files/scripts interact with the signature, isolation, and attestation-measurement guarantees.*
