# Attestable AMIs (EC2 NitroTPM measured-boot image build) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/attestable-ami.html` and its four child pages — `build-sample-ami.html`, `al2023-isolated-compute-recipe.html`, `customize-sample-ami.html`, `create-pcr-compute.html` (all fetched live as `.md` twins 2026-10-15, byte-consistent with the offline mirror). Supporting: `enable-nitrotpm-prerequisites.html`, `nitrotpm.html`; the public build artifacts GitHub `amazonlinux/kiwi-image-descriptions-examples` (recipe dir `al2023/attestable-image-example`: `appliance.kiwi`, `edit_boot_install.sh`, `README.md` — fetched via raw.githubusercontent.com) and `awslabs/coldsnap`; KIWI NG docs (`osinside.github.io/kiwi`); IAM Service Authorization Reference `list_ec2.html` (EC2 control plane, 35,512 lines) and `list_ebs.html` (title "Actions, resources, and condition keys for **Amazon Elastic Block Store**" — the EBS **Direct APIs** table). `systemd.io/TPM2_PCR_MEASUREMENTS/` (PCR12 corroboration). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Slug note (save for citation):** EBS Direct APIs = `service-authorization/latest/reference/list_ebs.html`. `list_amazonelasticblockstore.html` is a **dead** meta-refresh stub → do not cite. (Mirrors the existing `list_ec2` vs dead `list_amazonec2` rule.)

> **Scope & sibling coordination.** This page is the **AMI-BUILD / reproducible-measurement / measurement-scope / KIWI-recipe / PCR-compute / build-pipeline-IAM** layer of the NitroTPM chapter. It is the *root-cause* source material behind the attestation plan's headline A1 ("reproducible-measurement bypass"), which that plan develops only at the **KMS-gate** level and explicitly defers the build/measurement side. This plan therefore **OWNS**: (a) *why* the reference measurements are reproducible/forgeable (public recipe + public `nitro-tpm-pcr-compute` + measurement = deterministic function of the UKI, zero owner entropy); (b) **what the measurement actually covers and when** (UKI only → rootfs bound transitively via dm-verity-hash-in-cmdline → PCR12; boot-time-only, not runtime); (c) the build-pipeline supply chain (KIWI NG, `coldsnap`, the GitHub recipe, floating `mirror.list/latest`, dnf); (d) build-time root code execution (KIWI auto-script + overlay tree); (e) the AWS-authored **build-sample-ami Prerequisites IAM artifact** and the EBS **direct-API** (`ebs:*`) data-plane write path; (f) the self-referential-measurement poisoned-build finding; (g) the "isolated compute / no operator access" guarantee as a build-choice-not-enforced control.
>
> **Explicitly DEFERS (cross-ref, do not restate):**
> - KMS verifier gate / PCR under-binding / **nonce/replay** / COSE / cert-chain → `nitrotpm-attestation-attack-research-plan.md` (Areas 1–6). (Subagent could not confirm nonce usage this pass — left to that plan.)
> - `RegisterImage` posture `--tpm-support`/`--boot-mode`/`--uefi-data`/`--imds-support` being IAM-ungatable, and **registering `--tpm-support v2.0` from a snapshot you don't own** → `enable-nitrotpm-support-on-ami-attack-research-plan.md` (Areas 1–5). This plan adds only the **EBS direct-API** write-path cousin + the IAM-artifact audit.
> - `GetInstanceTpmEkPub` EK-as-identity, whoAMI AMI-name land-grab depth, BitLocker "original instance only" → `nitrotpm-attack-research-plan.md` (hub).
> - Enablement launch prerequisites / instance type list → `enable-nitrotpm-prerequisites-attack-research-plan.md`.

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (§5); look left and right for adjacent bugs.
- Doc-only oracles are preferred (read the IAM reference; `iam:SimulateCustomPolicy`; read the public recipe; diff two local `pcr_measurements.json`). Live tests are marked **[hunter step]** and are not run here.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (Nitro Hypervisor signing keys, AWS internal attestation PKI, AWS build-fleet identity), stop, preserve evidence, flag for AWS-Security disclosure.

## 1. Pentest Objectives (concrete boundary-breach goals)
1. Determine whether the **reference measurements** (PCR4/7/12) that gate an attestation-conditioned KMS key are **reproducible by any party** from public inputs — i.e. the measurement proves *which code booted*, not *who owns/built the AMI* — so an attacker who can reach a broadly-scoped attestation-gated key can satisfy its PCR gate without ever possessing the victim's secret. **[Subagent B: CONFIRMED from docs — zero per-account/instance/build entropy in the measurement input surface.]**
2. Determine the **true measurement scope and timing**: whether PCRs cover application/rootfs content directly or only transitively, and whether attestation reflects *runtime* state or only *boot* state — so a verifier's "trusted" verdict can be mapped to what is actually proven.
3. Determine whether a **poisoned build toolchain** yields an AMI **and** reference measurements that are mutually self-consistent, so the poisoning is invisible to downstream attestation.
4. Determine whether the AWS-published **build Prerequisites IAM block** (`ebs:StartSnapshot`/`PutSnapshotBlock`/`CompleteSnapshot` on `arn:aws:ec2:*::snapshot/*` + `ec2:RegisterImage` on `*`) over-grants, and whether the EBS **direct-API** path can write into / register from a snapshot the principal does not own. **[Subagent A: CONFIRMED IAM offers no ownership condition on either path.]**
5. Determine whether **build-time code execution** (KIWI auto-executed scripts, overlay-tree overwrite) is a stealthy injection seam.
6. Determine whether the **"isolated compute / no operator access"** property is enforced by any AWS mechanism or is only a build-time package-exclusion choice.

## 2. Components, Assets, and Design

**What an Attestable AMI is.** An AMI with a corresponding SHA-384 hash set (PCR4/PCR7/PCR12) that "represents all of its contents … generated during the AMI creation process" (`attestable-ami.html`). Requirements: base OS AL2023 or NixOS; `x86_64`/`arm64`; **NitroTPM enabled** (`--tpm-support v2.0`); **UEFI boot mode**. **[Lens U tension — see Area 1: the "all of its contents" framing is a one-hop commitment, not a direct content measurement.]**

**Build pipeline (this plan's surface):**
```
[Public GitHub recipe: amazonlinux/kiwi-image-descriptions-examples
   dir al2023/attestable-image-example]  (installed via `dnf install kiwi-image-descriptions-examples`)
   │  appliance.kiwi: systemd_boot UEFI, erofs read-only root (lz4hc), verity_blocks="all",
   │     literal kernelcmdline "console=ttyS0 rd.shell=0 systemd.getty_auto=false
   │        rd.kiwi.verity_options=panic-on-corruption",  repo source = mirror.list/LATEST (floating)
   │     EXCLUDES openssh-server, cloud-init(+cfg-ec2), amazon-ssm-agent, ec2-instance-connect,
   │        amazon-chrony-config, update-motd  (isolated-compute recipe)
   ▼
[ sudo kiwi-ng system build ]  → ./image/al2023*.raw
   │  erofs rootfs → dm-verity hash tree over ALL blocks → root hash → embedded in kernel cmdline
   │     (dracut-kiwi-verity) → UKI (kiwi.efi) assembled WITH that cmdline
   │  THEN KIWI auto-runs edit_boot_install.sh (editbootinstall hook, NOT chrooted = build-host root):
   │     renames kiwi.efi → EFI/BOOT/BOOTX64.EFI, removes /EFI/Linux + /EFI/systemd (UKI = sole boot app),
   │     runs `nitro-tpm-pcr-compute --image UKI.efi`  →  ./image/pcr_measurements.json {PCR4,PCR7,PCR12}
   ▼
[ coldsnap upload ./image/al2023*.raw ]  (EBS DIRECT APIs: ebs:StartSnapshot/PutSnapshotBlock/CompleteSnapshot)
   ▼ SNAPSHOT id    ← NOTE: pcr_measurements.json is NEVER an input past this point
[ aws ec2 register-image --tpm-support v2.0 --boot-mode uefi --architecture … \
     --block-device-mappings …SnapshotId=$SNAPSHOT ]      ← no digest/measurement parameter exists
   ▼
[ "Attestable AMI" (name e.g. attestable_isolated_al2023_ami) ]
   ▼ launch → nitro-tpm-attest → Nitro-signed attestation doc {PCR4,PCR7,PCR12}  (BOOT-TIME values)
   ▼
[ AWS KMS Decrypt gated by kms:RecipientAttestation:NitroTPMPCR4/7/12 == pinned values ]   (deferred to attestation plan)
```

**Measurement input chain (Subagent B, confirmed):**
`erofs content → dm-verity root hash (verity_blocks="all") → kernel cmdline → UKI → PCR12`. `nitro-tpm-pcr-compute` reads **only** the UKI (`--image UKI.efi`); it never reads the erofs partition. PCR mapping: **PCR4** = boot-application code (here the UKI, since `edit_boot_install.sh` makes it the sole boot app); **PCR7** = Secure Boot policy/variable state (TCG-convention inference — *no AWS page enumerates PCR semantics; residual doc-gap*); **PCR12** = kernel command line, which carries the dm-verity root hash (confirmed via `attestable-ami.html` + `systemd.io/TPM2_PCR_MEASUREMENTS/`).

**Tooling / processes:**
- `nitro-tpm-pcr-compute` (RPM `aws-nitro-tpm-tools`, `yum install`): build-time; sole input the UKI; output `pcr_measurements.json`. **No AWS round-trip** → measurement is a client-side deterministic hash; nothing AWS-side authenticates it against the image.
- `nitro-tpm-attest` (guest): runtime attestation request (deferred to attestation plan).
- `kiwi-ng`: open-source image builder; **auto-executes scripts by filename convention** and the `editbootinstall` hook **not chrooted** (build-host root).
- `coldsnap` (awslabs): installed `git clone … && cargo install --locked coldsnap` (git **default branch**, not a tag); raw image → EBS snapshot via EBS direct APIs.

**Assets:** UKI/`.efi`; `pcr_measurements.json` (the reference the KMS policy pins); the EBS snapshot (`snap-…`); the registered AMI; the dm-verity root hash (in the UKI cmdline). None carries per-owner secret entropy.

**Trust zones:** customer build account vs **any other party who can run the identical public recipe** (→ identical measurements) vs AWS Nitro root of trust. The build account splits: whoever controls the **image-description source** (repo/CI) vs whoever runs `kiwi-ng` (build-host root).

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Any AWS account (attacker) | Victim's attestation-gated KMS key | Build identical public recipe → identical PCR4/7/12 → attestation doc satisfies the key policy's PCR conditions | A party who never held the victim's secret obtains a successful `Decrypt`; the only residual binding is the key policy **Principal** (owned by attestation A1) |
| Attacker with in-memory runtime foothold on a legit instance | Attestation-gated secret | PCRs are boot-time-only; in-memory compromise never re-extends them | Instance keeps producing the "trusted" PCR set and keeps passing the KMS gate while no longer trustworthy (Area 6) |
| Offline snapshot/volume tamperer | Rootfs integrity | PCR computation never reads erofs; dm-verity verifies lazily on-read | Instance attests with correct PCRs + obtains KMS secrets **before** the tampered block is read and panics (Area 7 window) |
| Image-description author / CI contributor | Build-host root | KIWI auto-executes a correctly-named script / overlay-tree overwrite during build | A file dropped into the recipe dir runs as root on the build host (`edit_boot_install.sh` runs **not chrooted**) with no reference in `appliance.kiwi` |
| Compromised dependency (recipe repo / coldsnap main / added dnf repo / floating mirror) | AMI boot content **and** its reference measurements | Both produced by the same build run | Poisoned image whose `pcr_measurements.json` matches it exactly → attestation reports "trusted"; no cross-check detects it |
| Holder of the build Prerequisites policy | An EBS snapshot / registered AMI | `ebs:PutSnapshotBlock` on `::snapshot/*` (no account segment, no ownership condition key) + `ec2:RegisterImage` on `*` | IAM poses zero obstacle to writing into / registering from a non-owned snapshot; only ID-secrecy + an **undocumented** service-side pending/ownership check stand in the way (Area 2) |
| Persistence via separate non-root EBS volume | Reboot-surviving state | Non-root volumes are outside the attested boot chain entirely | Data persists across reboot with zero PCR impact and no dm-verity involvement (Area 7) |
| Customizer | "isolated compute / no operator access" guarantee | Re-add an excluded package / add a listener | A still-"attestable" AMI that exposes remote/operator access (Area 5) |
| Any customer surface | AWS Nitro signing / build fleet | — | **HARD STOP** — service plane |

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2:RegisterImage` | SDK | Existing | Yes | External | Snapshot → AMI, sets `--tpm-support v2.0` | Yes | sample grants on `*`, no Condition | **5 image + 10 snapshot condition keys exist & are unused**; `ec2:TpmSupport`=**0 hits** (absent); `ec2:BootModeOverride` wired to `CreateImage` only, not RegisterImage (Lens X parity gap). Posture-ungatability depth → enable-nitrotpm-support |
| `ebs:StartSnapshot` | SDK (EBS **direct**) | Existing | Yes | External | begin direct-upload snapshot | Yes | sample grants on `arn:aws:ec2:*::snapshot/*` | ARN has **no account segment by design**; 6 condition keys, **none** ownership-bearing |
| `ebs:PutSnapshotBlock` | SDK (EBS **direct**) | Existing | Yes | External | write a 512 KiB block + SHA-256 | Yes | same | the image-content ingress; structurally weaker twin of `ec2:` control-plane snapshot actions |
| `ebs:CompleteSnapshot` | SDK (EBS **direct**) | Existing | Yes | External | finalize snapshot | Yes | same | |
| `nitro-tpm-pcr-compute` | build-host CLI | **New** | No (local) | — | PCR4/7/12 from a UKI | No | build-host user | **no server call** → root cause of reproducibility; sole input the UKI |
| `nitro-tpm-attest` | guest CLI | **New** | No | — | request Nitro-signed attestation doc | No | guest | runtime path, deferred |
| `kiwi-ng system build` | host CLI | — | local | — | build raw image, auto-run scripts | No | build-host root | code-exec seam |
| `coldsnap upload` | host CLI | — | Yes (calls `ebs:*`) | External | raw → EBS snapshot | — | build-host creds | wraps the EBS direct APIs |

**No undocumented control-plane knob is introduced by these pages.** The security-interesting delta is that the measurement is produced by a **client-side utility with no AWS round-trip**, and `pcr_measurements.json` is **never** an input to `RegisterImage` or any `ebs:*` API — measurement and snapshot content are fully decoupled (Area 2 / Area 3).

## 5. Recommended Areas of Focus (priority order)

### Area 1 — Reference measurements are reproducible public-boot-byte hashes; measurement ≠ identity, and "all contents" is a one-hop commitment [HEADLINE] (Lens W / U / EE)
**Background.** The reference measurements are produced by `nitro-tpm-pcr-compute` — a **public** utility — over a UKI built from a **public** recipe. **Subagent B confirmed from docs + the GitHub recipe:** the measurement input surface has **zero** per-account, per-instance, per-build-identity, or secret input (`create-pcr-compute.html`: sole required input `UKI.efi`; `edit_boot_install.sh` passes only `--image`; `appliance.kiwi` cmdline is a fixed literal with no templated variables). PCR4=boot-app (the UKI), PCR7=Secure Boot policy (TCG inference — doc-gap), PCR12=kernel cmdline carrying the dm-verity root hash.
**Security Concern.** Two parties who build the same recipe revision against the same package set land on **byte-identical** PCRs. The attestation binds to *what booted*, not *who owns/built it*; the only residual access binding is the KMS key-policy `Principal` (attestation A1). **Lens U sub-finding (confirmed):** `attestable-ami.html`'s claim that the hash "represents all of its contents … including the applications, code" is a **one-hop commitment**, not a direct measurement — `nitro-tpm-pcr-compute` never reads the erofs root FS; rootfs enters only as `erofs → dm-verity root hash → cmdline → UKI → PCR12`. Any rootfs change therefore *either* breaks dm-verity at boot *or* changes PCR12 — it can never silently pass — but the framing overstates what is directly measured.
**High-level Test Scenarios.**
- *Claim:* building the public recipe in two unrelated accounts yields byte-identical `pcr_measurements.json`. **Oracle [hunter step]:** build in two accounts (or one account + a local KIWI build), `diff`. Equal = reproducible.
- *Caveat to pre-empt a false refutation (Subagent B):* `appliance.kiwi`'s repo source is `mirror.list/latest` (**floating**). Two builds weeks apart may diverge in PCR because AL2023 shipped a new kernel/systemd-boot/dracut — this is *public, explicable* drift, **not** owner-specific entropy, so it does not refute the headline. Pin package versions when comparing.
- *Chain:* reproducible measurement → satisfies a broadly-`Principal`'d attestation-gated key (attestation A1) → decrypt a secret never earned. **Rate at the chain end.**
**Severity-if-true:** High–Critical (gate-bypass enabler). The *measurement-is-not-identity* fact is a design property to document; the exploitable half lives at the KMS `Principal`.

### Area 2 — Build Prerequisites IAM artifact + EBS direct-API ownership gap (Lens R / S / X) [CONFIRMED doc-only]
**Background.** `build-sample-ami.html` ships a **copy-verbatim** Prerequisites block: `ebs:CompleteSnapshot`/`StartSnapshot`/`PutSnapshotBlock` on `arn:aws:ec2:*::snapshot/*` + `ec2:RegisterImage` on **all resources**, no `Condition`.
**Confirmed findings (Subagent A, line-cited to `list_ec2.html` / `list_ebs.html`):**
- **`RegisterImage` over-grant (Tier-2):** the action supports resource type `image*` (5 keys incl. `ec2:ImageID`, `ec2:Owner`) and `snapshot` (10 keys incl. `ec2:SnapshotID`, `ec2:Owner`, `ec2:ParentVolume`). The sample uses **none** → the identity can register **any AMI from any snapshot ARN it can name**. AWS could have scoped to "images named `attestable_isolated_al2023_ami*` from a snapshot I own" and chose not to.
- **`--tpm-support` is un-gatable:** `ec2:TpmSupport` = **0 hits** in the entire 35,512-line EC2 reference (absent, not merely undocumented). → defer the posture-ungatability headline to enable-nitrotpm-support; this plan records the grep-confirmed absence.
- **Lens X parity gap:** `ec2:BootModeOverride` exists but is wired to **`CreateImage` only**, *not* `RegisterImage` — the sibling control-plane action can be boot-mode-gated; the one in this tutorial cannot.
- **EBS direct-API ownership gap:** the `ebs:` `snapshot` ARN template has **no `${Account}` segment** (literal `::`) — this is the canonical shape, same on EC2's own snapshot resource type, *not* a loose sample. The real gap is the **condition-key set**: the 6 keys available to all `ebs:*` snapshot actions are tag/metadata-only (`aws:RequestTag`, `aws:ResourceTag`, `aws:TagKeys`, `ebs:Description`, `ebs:ParentSnapshot`, `ebs:VolumeSize`) — **no `ec2:Owner`, no `aws:ResourceAccount`/`aws:PrincipalAccount`** (all 0 hits). Contrast: the `ec2:` control-plane snapshot resource type **does** carry `ec2:Owner`/`ec2:ParentVolume`/`ec2:Encrypted`. So the `coldsnap` write path is the **structurally weaker twin** — IAM cannot scope it to "snapshots I started" even if AWS wanted to.
- **The real backstop is undocumented (Lens U doc-gap):** the only non-IAM obstacle to writing blocks into a non-owned snapshot is (a) knowing its `snap-` ID (longer-ID entropy — *not re-confirmed in-session, flag before relying*) and (b) a service-side "snapshot must be `pending`"/ownership check that is **not expressible as, nor visible in, the SAR at all**.
**Oracle.** `iam:SimulateCustomPolicy` with the exact artifact: `ec2:RegisterImage` against `ec2:SnapshotID = snap-<not-mine>` → `allowed`; `ebs:PutSnapshotBlock` against a foreign `::snapshot/*` ARN → `allowed`. Both prove IAM poses no obstacle (no live call needed). **[hunter step]** probe `StartSnapshot`/`PutSnapshotBlock` against a discoverable non-owned (e.g. second-account) snapshot id → expect `AccessDenied`/`ResourceNotFound` from the *service's internal* check, confirming the control lives outside IAM.
**Severity.** `RegisterImage` over-grant = **Medium–High, Tier-2 (AWS-authored artifact — route for disclosure)**; EBS ownership gap = Medium (IAM gives no defence-in-depth; exploitability gated by the undocumented backstop).

### Area 3 — Supply chain + self-referential measurement: a poisoned build attests "trusted" (Lens R-variant / EE / U)
**Background.** The tutorial installs/runs, several as **root**, multiple **unpinned** components: `coldsnap` from `git clone … && cargo install --locked` (= git **default branch**; `--locked` pins only `Cargo.lock`), the `kiwi-image-descriptions-examples` dnf package, and the recipe's own **floating `mirror.list/latest`** package source (Subagent B). Customization permits arbitrary added `<repository>` endpoints.
**Security Concern.** Compromise of **any** input (recipe-repo PR, `coldsnap` main, an added dnf repo, the floating mirror, a KIWI script) poisons the AMI's boot content. **Decisive twist:** the *same* build run also runs `nitro-tpm-pcr-compute`, so a poisoned image and its `pcr_measurements.json` are **mutually self-consistent**. Attestation only ever proves "this instance matches the measurements computed over this image"; it can **never** detect that the image itself was poisoned at build time. The measurement is self-referential, not an independent AWS-side integrity assertion.
**High-level Test Scenarios.**
- *Claim:* `coldsnap` cloned from an unpinned default branch. **Oracle:** `build-sample-ami.html` step 3 (no `--branch`/tag). **Severity:** build-host compromise = High.
- *Claim:* recipe + packages referenced by latest, not a pinned commit/version. **Oracle:** repo + `appliance.kiwi` `mirror.list/latest`.
- *Claim:* a poisoned build's measurements validate against the poisoned image. **Oracle:** by construction; document as an attestation-scope limitation feeding the attestation plan's threat model.
**Owner note.** AWS-authored tutorial mandating unpinned root installs = **Tier-2 reportable**; a customer's own recipe choices = footgun.

### Area 4 — Build-time root code execution via KIWI auto-scripts & overlay-tree clobber (Lens K / Q)
**Background.** `customize-sample-ami.html`: KIWI "automatically detects and executes the scripts if they are named correctly … **without the need to explicitly reference them**." The overlay tree (`/root/`) is "copied directly into the root filesystem … **existing files are overwritten**." Auto-executed names: `config.sh`, `images.sh`, `post_bootstrap.sh`, `config-overlay.sh` (chrooted), `config-host-overlay.sh` (**not** chrooted), `pre_disk_sync.sh`, `disk.sh`, plus the `editbootinstall` hook `edit_boot_install.sh` which runs **not chrooted = on the build host as root** (and is exactly the script that runs `nitro-tpm-pcr-compute`).
**Security Concern.** Anyone who can drop a correctly-named file into the image-description dir or overlay tree gets **root code execution during build** — invisible to a reviewer scanning `appliance.kiwi` (no XML reference). Overlay overwrite allows silent clobber of trusted files, **including `edit_boot_install.sh` / the measurement tooling itself** → feeds Area 3. Trigger: a shared/collaborative recipe, a CI build, or a repo an attacker can PR.
**High-level Test Scenarios.**
- *Claim:* a file named `config.sh`/`edit_boot_install.sh` added to the recipe dir executes as root at build with no XML declaration. **Oracle:** KIWI "User-Defined Scripts" doc + `customize-sample-ami.html`.
- *Claim:* overlay files silently overwrite image files incl. the attestation tooling. **Oracle:** `customize-sample-ami.html` overlay section.
**Owner note.** The auto-exec convention is upstream KIWI, but AWS's tutorial normalizes an unreviewed-script workflow and the host-root `edit_boot_install.sh` hook — flag as a hardening/doc gap.

### Area 5 — "Isolated compute / no operator access" is a build choice, not an enforced control (Lens U)
**Background.** `al2023-isolated-compute-recipe.html` achieves the guarantee by **excluding packages** (openssh-server, cloud-init/cloud-init-cfg-ec2, amazon-ssm-agent, ec2-instance-connect, amazon-chrony-config, update-motd) + disabling serial console via kernel cmdline. Stated property: "removes all interactive access … to create an isolated compute environment."
**Security Concern.** Enforced *only* by omission. A customizer who re-adds an excluded package or opens a listener silently reintroduces remote/operator access while the AMI stays a valid "Attestable AMI." Nuance (confirmed via Area 1 chain): such a change **does** alter PCR12 (package set → erofs → root hash → cmdline), so the posture *is* attested through the root hash — but only against a verifier that pins the *isolated* recipe's exact PCRs. A verifier pinning the attacker's own PCRs accepts the SSH-enabled image. The guarantee's real enforcer is the PCR pin, not the exclusion.
**High-level Test Scenarios.**
- *Claim:* an "Attestable AMI" can be built with SSH re-enabled and still attest (to its own PCRs). **Oracle:** attestation validates whatever PCRs the UKI yields; SSH-on changes PCR12 but does not *fail*. **Severity:** Low–Medium (guarantee-scope clarity).
- *Claim:* in-guest agent removal does not change the AWS-managed control-plane reachability of the instance. **Oracle:** the recipe describes only in-guest removal. **Severity:** Informational.

### Area 6 — Attestation reflects BOOT state only, not runtime state (Lens U) [CONFIRMED, exact quote]
**Background (Subagent B, exact AWS quote).** `attestable-ami.html` "Maintaining an Attestable State": *"An instance's measurements are based on its **initial boot state**. Any software or code changes made to the instance after launch **and that persist after restarts** will change the instance's measurement **after restarts** … the instance will no longer be able to successfully attest to AWS KMS **after the instance restarts**."*
**Security Concern.** PCR4/7/12 are fixed at boot and never re-extended during the instance's life. An **in-memory-only** runtime compromise (code exec into the running kernel/userspace that never writes a reboot-surviving location and never triggers a restart) changes **no** measured PCR. The instance keeps producing a Nitro-signed doc with the original "trusted" PCRs, and `kms:RecipientAttestation:NitroTPMPCR*` keeps being satisfied — a classic TOCTOU: "this boot's software measured X" is proven, "this instance is *currently* running only X" is not.
**High-level Test Scenarios.**
- *Claim:* an in-memory runtime modification leaves PCRs (and thus KMS access) unchanged for the life of the boot. **Oracle [hunter step, owner-only, no cross-tenant access]:** launch from the AMI, baseline `nitro-tpm-attest | aws kms generate-random --recipient AttestationDocument=…` (the repo README's own harness), apply an in-memory-only change (edit a running process/library in place, no disk write), re-run → confirm identical PCRs + still-successful KMS call.
**Severity.** High — central guarantee-vs-enforcement gap: attestation-gated key release does not protect against a runtime exploit that avoids reboot. **Cross-ref:** the KMS-side consequence (what the verifier should additionally require, e.g. freshness/short lease) is attestation-plan territory; the *measurement-is-boot-time-only* fact is owned here.

### Area 7 — Offline root-volume tamper: DoS + lazy-verification window + non-root-volume persistence (Lens U / L)
**Background (Subagent B).** `appliance.kiwi` sets the literal kernel param `rd.kiwi.verity_options=panic-on-corruption`. dm-verity verifies **lazily, per-block-on-read**, not eagerly at mount.
**Security Concern.**
- *Offline rootfs tamper = DoS, not PCR-visible bypass:* editing erofs blocks offline changes **no** PCR (computation never reads erofs; UKI/cmdline untouched) and does not change the committed root hash → any read of a tampered block → kernel panic. Fail-closed on *content*, but…
- *Lazy-verification timing window (flag as top live-test):* if the tampered blocks are in a rarely-read path, the instance can **complete boot, attest with correct PCRs, obtain KMS-released secrets, and only panic later** when that block is finally read. So "attestation succeeded" is **not** proof that 100% of the rootfs was validated at that instant — only the UKI/cmdline/root-hash chain + blocks-read-so-far.
- *Reboot-surviving persistence outside the attested chain:* a **separate, non-root EBS volume** is not measured and not dm-verity-protected — nothing in the docs/recipe covers additional attached volumes. Data there persists across reboot with zero PCR impact (the erofs + in-memory overlay design closes the overlay channel for `/etc` `/run` `/var`, but not this one).
**High-level Test Scenarios.**
- *Claim:* a rarely-read erofs region can be tampered offline so the instance attests + gets secrets before panicking. **Oracle [hunter step]:** flip bytes in a rarely-read erofs region of a copied root snapshot, boot, attest immediately (confirm PCRs match + KMS succeeds), then force a read of the region → confirm panic. Bounds the window.
- *Claim:* a non-root volume gives reboot-surviving persistence with no PCR impact. **Oracle [hunter step]:** attach a second EBS volume, write, reboot, confirm data persists + PCRs unchanged.
**Severity.** Medium (DoS confirmed from docs) → High if the lazy-verification window is confirmed live (attestation-gated secrets obtainable before storage-tamper detection fires).

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation / status |
|---|---|---|
| Reproduce victim PCRs from the public recipe (gate-forgery root cause) | `nitro-tpm-pcr-compute` + public recipe | **CONFIRMED** zero owner entropy; "hash represents all contents" is one-hop |
| In-memory runtime compromise keeps passing the KMS gate | boot-time PCRs | **CONFIRMED** by AWS's own "after restarts" scoping (Area 6) |
| Offline rootfs tamper → attest + get secrets before panic | dm-verity lazy on-read | window plausible; **top live-test** (Area 7) |
| Persistence via non-root EBS volume | attested chain scope | outside measurement + dm-verity entirely (Area 7) |
| Register any AMI from any snapshot ARN; write into non-owned snapshot | RegisterImage `*` + `ebs:*` | **CONFIRMED** no IAM ownership condition (Area 2) |
| `--tpm-support` / boot-mode ungatable on RegisterImage | IAM | **CONFIRMED** `ec2:TpmSupport`=0 hits; BootModeOverride=CreateImage-only |
| Poison a build input → self-consistent poisoned measurements | coldsnap/recipe/floating-mirror/KIWI | unpinned root installs; measurement from same run (Area 3) |
| Root code-exec at build via auto-script/overlay | KIWI NG build | auto-detected/executed; overlay overwrites (Area 4) |
| Re-add excluded access, remain "attestable" | isolated-compute recipe | exclusion-only; attested only vs the pinning verifier (Area 5) |

## 7. Out-of-Scope Risk Categories
- The KMS attestation gate itself, PCR under-binding, **nonce/replay** (unconfirmed this pass), COSE/cert-chain → attestation sibling.
- `RegisterImage` posture-ungatability *headline* depth, `--uefi-data` PCR7 ownership, snapshot-provenance-at-RegisterImage headline → enable-nitrotpm-support sibling.
- Nitro Hypervisor signing keys / AWS build-fleet identity / internal PKI → **HARD STOP**, service plane.
- A customer's *own* custom recipe weakening its *own* isolation — in scope **only** where the weak default ships in AWS's published recipe/tutorial/IAM block.
- KIWI NG / coldsnap upstream code bugs — out of scope except where AWS's tutorial mandates an unsafe usage pattern.
- IMDS on these managed hosts; single-tenant self-DoS.

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens A (cross-tenant IDOR):** no multi-tenant resource-by-id API on these build pages; the cross-account angle is *measurement reproducibility* (Area 1), not IDOR. Checked all 5 pages.
- **Lens G (SSRF):** the only URL-like inputs (recipe GitHub URL, coldsnap git URL, `<repository>` dnf endpoints) are build-host client fetches, not a service-side dereference. N/A (checked customize-sample-ami repository-management + build-sample-ami steps).
- **Lens B/C (PassRole/vending):** no role-ARN input on these pages; build-host uses the caller's own creds. N/A.
- **Lens EE (AMI-name land-grab):** `register-image` resolves its snapshot by caller-supplied `SnapshotId`, not by name, so the tutorial's own flow is **not** name-squattable (snapshot-ID guessing is entropy-mitigated). Residual **downstream** lead (whoAMI-shaped, speculative): any consumer later resolving `attestable_isolated_al2023_ami` by `Name` filter **without `--owners self`** could hit an attacker-published public AMI of the same predictable literal name. Not demonstrated in the fetched pages → log as confirm-before-use, defer land-grab depth to hub.
- **Doc gaps to confirm first [hunter steps]:** (1) longer-ID snapshot entropy (not re-confirmed in-session); (2) **AWS publishes no PCR-semantics table** — PCR4/PCR7 mapping is TCG-convention inference (PCR12 is confirmed); pin via a live `nitro-tpm-pcr-compute` run swapping only the `.cmdline` section to see which PCR moves; (3) the exact `dracut-kiwi-verity` cmdline parameter that carries the root hash is a packaging internal not visible in the public recipe; (4) whether `kms:RecipientAttestation:NitroTPMPCR*` includes a nonce → attestation sibling; (5) the service-side pending/ownership check behind `ebs:*` is undocumented — probe behavior for the real backstop.
