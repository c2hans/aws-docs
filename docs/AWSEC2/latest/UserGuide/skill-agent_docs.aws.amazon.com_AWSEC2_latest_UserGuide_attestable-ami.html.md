# Attestable AMIs — Attack Research Plan

Source of leads: `docs.aws.amazon.com/AWSEC2/latest/UserGuide/attestable-ami.html` and its four child pages
(`build-sample-ami.html`, `al2023-isolated-compute-recipe.html`, `customize-sample-ami.html`, `create-pcr-compute.html`)
plus prerequisite `enable-nitrotpm-prerequisites.html`. Offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/*.md`
**re-validated live 2026-09-13** — offline == live, and there is **NO injected "see also / run this aws CLI" AI-agent block**
on any of these pages (consistent with the sibling NitroTPM-attestation hub finding).

Status: documentation-derived hypotheses only; nothing tested against a live account.

> **Scope relationship.** This page is the **build / provenance side** of the NitroTPM attestation trust chain. The
> *consumption / KMS-gate* side (attestation document validation, `kms:RecipientAttestation:NitroTPMPCR*`, fail-open on
> absent attestation, the AWS sample key policy that pins PCR4-only / PCR12=all-zeros) is covered in the sibling plan
> `skill-agent_..._nitrotpm-attestation.html.md` (crown jewels AF-1..AF-4) and its parent `nitrotpm-attack-research-plan.md`.
> **Do not re-hunt the KMS gate here** — this plan owns the questions that only the *build/measurement-provenance* pages raise.
> Where a lead depends on the enforced PCR set, it is stated as a *chain into* the KMS-gate plan.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's **own service plane**
  (the Nitro hypervisor's TPM-measurement path, the AL2023 mirror/package-signing infra, the KMS attestation verifier),
  stop, preserve evidence, flag for AWS-Security disclosure. Building an AMI in your own account is **customer-side** and
  is *not* a service-plane breach on its own.
- Priority order below is deliberate: the highest-yield lead (U-1, the "represents all contents" guarantee vs the
  actually-measured PCR set) is a **doc-vs-enforcement** claim that is testable purely from the measurement mechanics.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Break the "all contents" guarantee.** Produce two AMIs (or two booted states) that yield **identical enforced PCR
   measurements** but differ in code/data the doc claims is covered — i.e. an instance that **attests successfully to AWS
   KMS while running different application/root-filesystem content** than the reference image the policy author intended.
2. **Reference-measurement forgery / self-assertion.** Show that the `pcr_measurements.json` values are attacker-authored
   (locally computed by a public utility, never signed/notarised by AWS) and therefore prove nothing about image
   *provenance* — only self-consistency of whatever image the builder chose.
3. **Measurement ↔ actual-boot divergence.** Show that `edit_boot_install.sh` (the build-time script that *computes* the
   reference measurements) can emit measurements that do not correspond to the bytes that actually boot — or the reverse:
   a benign build whose measurements silently exclude an attacker-controllable region.
4. **AMI build supply chain.** Enumerate every external artifact the build pulls (KIWI image-description repo, `coldsnap`
   from GitHub, `aws-nitro-tpm-tools`, the AL2023 mirror `<repository>` endpoint, arbitrary customer `<packages>`/overlay/
   scripts) and identify which are unpinned / TOFU / MITM-able such that a compromised input yields a **still-attestable**
   backdoored AMI.
5. **AWS-authored artifact audit.** Audit the tutorial's IAM prerequisite block and the AWS-published sample image
   description for weak defaults a customer copies verbatim.

---

## 2. Components, Assets, and Design

**What the feature is (mechanism, not marketing).** An "Attestable AMI" is an ordinary EBS-backed AMI plus a set of
**reference PCR measurements** the *builder* computes and later pins into an AWS KMS key policy. At runtime, NitroTPM +
the Nitro hypervisor measure the instance's boot into TPM PCRs; KMS releases a key only if the live PCRs match the pinned
reference values (`kms:RecipientAttestation:NitroTPMPCR*`). This page governs **how the reference measurements and the
image are produced** — not how KMS enforces them.

**Build pipeline (all steps run inside the *customer's* account, on a customer EC2 instance):**

```
 AL2023 build instance (customer acct)
   │  dnf install kiwi-cli … aws-nitro-tpm-tools      ← AL2023 mirror + repo
   │  git clone awslabs/coldsnap ; cargo install       ← GitHub (unpinned)
   │  dnf install kiwi-image-descriptions-examples      ← AWS sample image description
   ▼
 KIWI NG `system build`  (XML image description: <repository>,<packages>,overlay tree /root/, scripts)
   │   builds UKI (.efi) + erofs root fs + dm-verity  → al2023*.raw
   │   edit_boot_install.sh  (auto-run post-bootloader):
   │        mount .raw loopback → locate UKI .efi → nitro-tpm-pcr-compute --image UKI.efi
   │        → ./image/pcr_measurements.json  { PCR4, PCR7, PCR12 }   ← SELF-ASSERTED, unsigned
   ▼
 coldsnap upload al2023*.raw  →  EBS snapshot   (ebs:PutSnapshotBlock, raw bytes)
   ▼
 ec2 register-image --tpm-support v2.0 --boot-mode uefi …  →  Attestable AMI
   ▼
 (later, out of scope here) launch → NitroTPM measures boot → KMS gate pins PCR4/7/12
```

**Assets / trust anchors:**
- **PCR4** — measures the Unified Kernel Image (UKI `.efi`: kernel + initrd + boot params, one signed binary).
- **PCR7** — UEFI Secure Boot state (the *only* PCR capable of per-tenant binding, via a customer-private SB cert — see
  sibling plan AF-1). Doc here does not require or describe customer SB keys for AL2023.
- **PCR12** — kernel command line. **This is the load-bearing link for the root filesystem**: dm-verity "calculates a hash
  of the filesystem blocks and stores it in the kernel command line," so the *only* thing that binds the erofs/dm-verity
  root-fs contents into the measurement chain is the dm-verity root hash **being present in the measured cmdline (PCR12)**.
- **`pcr_measurements.json`** — the reference measurements. Locally produced by the public `nitro-tpm-pcr-compute`. No AWS
  signature, no notarisation, no provenance binding to a specific account/image.
- **AWS-published sample image description** — `github.com/amazonlinux/kiwi-image-descriptions-examples` + AL2023 package
  `kiwi-image-descriptions-examples` (installed to `/usr/share/kiwi-image-descriptions-examples/al2023/attestable-image-example`).
- **Identity/roles:** none new. Build runs as the customer's IAM identity; tutorial requires `ebs:StartSnapshot/
  PutSnapshotBlock/CompleteSnapshot` on `arn:aws:ec2:*::snapshot/*` and `ec2:RegisterImage` on `*`.

**No multi-tenant service fleet is in this page's data path.** The build is single-account, single-tenant, on customer
compute. The *shared* surface (KMS attestation verifier, Nitro measurement path) is service-plane = hard stop, not a target.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| AMI builder (customer) | AWS KMS attestation gate (later consumer) | reference PCRs pinned into key policy | **Two images with identical PCR4/7/12 but different covered content both attest** = the "all contents" guarantee is false |
| `edit_boot_install.sh` (build script) | `pcr_measurements.json` (reference values) | build-time local compute of measurements | Measurements that do **not** correspond to the bytes that boot, or that omit an attacker-controllable region, are emitted and later accepted |
| External build inputs (GitHub, mirror, packages, overlay, scripts) | resulting AMI contents | KIWI `<repository>`/`<packages>`/overlay/`coldsnap`/`cargo install` | A tampered/unpinned input yields a backdoored image whose (recomputed) PCRs still match a pinned policy → **still-attestable backdoor** |
| dm-verity root hash | PCR12 (kernel cmdline) | hash stored in cmdline, cmdline measured | Root-fs content changed **without** changing the measured cmdline → root fs unmeasured → content swap attests clean |
| Reference measurements author | KMS key-policy author | PCR set chosen for the policy | PCR12 (and thus root fs) dropped / set to a sentinel in the policy → root fs entirely unbound (chains to sibling AF-3) |
| **any customer surface** | **AWS Nitro measurement path / KMS verifier / AL2023 signing infra** | — | **HARD STOP** — service plane |

---

## 4. API / Interface Inventory

This page exposes **no new EC2 control-plane API**. The build uses existing primitives; capture them for the hunter:

| Name | Method | Mutating | Ext-facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ec2:RegisterImage` | RegisterImage | yes | yes | register the AMI (`--tpm-support v2.0 --boot-mode uefi`) | yes (SigV4) | tutorial says grant on `*` (unconditioned) | UEFI + TPM path — `--uefi-data` blob parsing is a **separate** surface, see [[ami-boot-plan]]/[[uefi-secure-boot-plan]]; **no `ec2:BootMode`/`ec2:TpmSupport` condition key** to constrain it |
| `ebs:StartSnapshot` / `PutSnapshotBlock` / `CompleteSnapshot` | EBS direct APIs | yes | yes | `coldsnap upload` writes raw disk image bytes into a snapshot | yes | scoped `arn:aws:ec2:*::snapshot/*` | raw-bytes→snapshot→AMI primitive; identical to instance-store/S3-backed AMI path |
| `nitro-tpm-pcr-compute` | local CLI (`aws-nitro-tpm-tools`) | n/a | n/a (on-box) | compute reference PCR4/7/12 from a UKI `.efi` | n/a | anyone who has the binary (public repo) | **public + reproducible → PCRs are attacker-computable** |
| `nitro-tpm-attest` | local CLI | n/a | on-box | produce attestation at runtime | n/a | on-box | preinstalled into the sample AMI at `/usr/bin/` |

**Undocumented-knob sweep:** `register-image --tpm-support` accepts `v2.0`; there is **no documented IAM condition key**
(`ec2:TpmSupport`, `ec2:BootMode`) to force/deny TPM or UEFI at registration — cross-check the EC2 IAM reference (this is a
Lens-S "condition key does not exist" lead, mirroring the confirmed absence of `ec2:BootMode`/`ec2:UefiData` in the
sibling ami-boot plan). `nitro-tpm-pcr-compute` accepts only `--image` per docs — check the actual binary for hidden flags
(e.g. algorithm selection, PCR-index selection) that could produce weaker/partial measurements.

---

## 5. Recommended Areas of Focus (one block per firing lens)

### Area 1 — Lens U ⭐ CROWN JEWEL: "represents all of its contents" guarantee vs the actually-measured PCR set
**Background.** The page opens: *"An Attestable AMI is an AMI with a corresponding cryptographic hash that represents all
of its contents … calculated based on the entire contents of that AMI, including the applications, code, and boot
process."* But the reference measurements actually produced are exactly three PCRs: **PCR4 (UKI), PCR7 (Secure Boot),
PCR12 (kernel command line)** — nothing that directly hashes the root filesystem. The root-fs is bound **only
transitively**, and only if (a) dm-verity is used, (b) the dm-verity root hash lands in the kernel command line, and
(c) that command line is what feeds PCR12, and (d) the *consuming KMS policy actually pins PCR12*.

**Security Concern.** The doc's "entire contents … applications, code" is a *guarantee word* (Lens U trigger). Trace it
to the enforcing mechanism: it is **not** a single hash of the AMI; it is the dm-verity+UKI construction, which the doc
itself frames as optional "utilities … can be used." An AMI that does **not** use dm-verity (or whose overlay/writable
regions are outside the verity tree) has application/data content that is **unmeasured**, yet the page calls it an
"Attestable AMI." The guarantee is therefore **advisory / conditional**, not intrinsic to "Attestable AMI."

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** Two AMIs with the **same UKI** (identical PCR4) but **different root-filesystem content** can both produce
  the same enforced measurement set — because PCR4 measures only the UKI and the root-fs is bound only via the dm-verity
  root hash in the cmdline (PCR12). → **Confirm/Refute:** build image A and image B differing only in a `/usr/bin` binary;
  if the dm-verity root hash (and thus PCR12) changes, refuted for a PCR12-pinning policy; **if the KMS policy pins PCR4
  only** (sibling AF-3 confirmed the AWS sample does exactly this), image B attests clean → guarantee broken. → chains to
  sibling `nitrotpm-attestation` AF-3.
- **Claim:** An Attestable AMI built **without** dm-verity/erofs (the utilities are "can be used," not "must") still
  qualifies and attests, while its writable root-fs content is entirely unmeasured. → **Oracle:** the doc never makes
  dm-verity a *requirement* (see §"Requirements": only base OS / arch / NitroTPM / UEFI are required); confirm that
  `register-image --tpm-support v2.0` succeeds for a non-verity image and that its PCRs omit any root-fs binding.
- **Claim:** PCR12 = kernel command line is **attacker-adjustable at build** (it is customer-authored). An attacker who
  controls the build can choose a cmdline whose dm-verity root hash points at a benign tree, then serve different content
  at runtime via the ephemeral overlay (writes to `/etc`,`/var` are in-memory and *not* re-measured). → **Oracle:**
  post-boot in-memory modification is invisible to the boot-time PCRs → attestation reflects boot state only, not running
  state (see Area 4).

**Doc evidence:** attestable-ami.html §intro ("represents all of its contents … applications, code"); §Maintaining
("dm-verity … stores it in the kernel command line"); build-sample-ami.html `pcr_measurements.json` = {PCR4,PCR7,PCR12}.
**Severity-if-true:** Informational/Low as a pure doc-vs-mechanism inconsistency, **but Medium–High** because a customer
may build an **attestation/compliance control** on the false belief that "Attestable AMI" ⇒ all code is measured. AWS-owned
(the guarantee sentence and the sample recipe are AWS-authored). Reportable, Tier-2, route `aws-security`.

### Area 2 — Lens U / W: reference measurements are self-asserted (no provenance / notarisation)
**Background.** `pcr_measurements.json` is computed locally by `nitro-tpm-pcr-compute` (public, in `aws-nitro-tpm-tools`,
`sudo yum install`), during the customer's own build. AWS never signs, notarises, or records these values.

**Security Concern.** Attestation proves *"the running boot matches whatever PCRs the KMS-policy author pinned."* It does
**not** prove those PCRs correspond to any AWS-blessed or provenance-verified image. Because the compute utility is public
and deterministic, **any party can compute valid-looking reference measurements for any image they build**, including a
backdoored one. The "attestable" label conveys integrity-to-a-chosen-baseline, not authenticity-of-origin. This is the
build-side restatement of sibling AF-1 ("attestation authenticates code, not tenant").

**High-level Test Scenarios:**
- **Claim:** A malicious builder produces a backdoored AMI, computes its PCRs with the public tool, pins them, and the
  image attests exactly as cleanly as a benign one — there is no external check that the pinned values are "good." →
  **Oracle:** reproduce `nitro-tpm-pcr-compute --image UKI.efi` on two arbitrary UKIs; both yield well-formed
  measurements; nothing in the flow validates provenance. Refuted only if AWS is shown to cross-check the values
  server-side (docs show no such step).
- **Claim (chain):** combine with sibling AF-2 — `nonce`/`user_data` unused by the KMS gate and freshness undocumented →
  a replay of an old attestation for a *previously-benign* build could satisfy a policy after the on-disk image was
  swapped. (Verify in the sibling plan; noted here as the build-side enabler.)

**Doc evidence:** create-pcr-compute.html (public `sudo yum install aws-nitro-tpm-tools`, deterministic `--image` compute);
build-sample-ami.html step 6 (`pcr_measurements.json` produced locally, no signing).
**Severity-if-true:** Medium (design property AWS may consider intended). File as a documented-guarantee clarity gap +
support the sibling's AF-1 crown jewel.

### Area 3 — Lens Q / supply chain: still-attestable backdoor via tampered build inputs
**Background.** The build pulls, unpinned: the KIWI image-description sample (`amazonlinux/kiwi-image-descriptions-examples`
via GitHub and via the AL2023 package `kiwi-image-descriptions-examples`), `coldsnap` (`git clone awslabs/coldsnap` +
`cargo install --locked` — pins deps but not the checkout), `aws-nitro-tpm-tools`, and the AL2023 core repo through the
KIWI `<repository>` "mirror endpoint." Customize page invites arbitrary additional `<repository>` entries, `<packages>`,
overlay-tree files (`/root/`), and custom scripts (auto-detected/executed by KIWI, plus first-boot scripts).

**Security Concern.** Any of these inputs, if compromised or MITM'd, produces a backdoored image — and because the
reference measurements are recomputed **from that same tampered image**, the backdoor is **transparent to attestation**
(PCRs match the malicious build). The most sensitive input is **`edit_boot_install.sh`**: it is the code that *computes
the measurements*. A modified `edit_boot_install.sh` could (a) measure a different `.efi` than the one that actually boots,
or (b) narrow which regions are measured — creating a measurement↔content divergence that still yields a "valid"
`pcr_measurements.json`.

**High-level Test Scenarios:**
- **Claim:** The KIWI `<repository>` mirror endpoint / `git clone`s are fetched without pinned digests or enforced
  signature verification in the tutorial → a network-position or repo-compromise attacker injects a backdoored package
  that ships in the AMI, and the recomputed PCRs still match a pinned policy. → **Oracle (doc-only here):** confirm the
  tutorial specifies no digest/signature pinning for the GitHub clones and the mirror; confirm `dnf`/repo GPG posture of
  the sample description. Live confirm belongs to a build-lab, not a shared account.
- **Claim:** `edit_boot_install.sh` locates "the UKI (the `.efi` file)" heuristically and measures it; if two `.efi`s exist
  or the boot loader selects a different binary than the script measures, reference PCR4 ≠ actual boot PCR4 → either a
  benign fail-closed, **or** (worse) a crafted layout where the measured `.efi` is benign but the booted one is not. →
  **Oracle:** inspect the script's UKI-selection logic; test a two-UKI image.
- **Claim:** overlay tree (`/root/`) "overwrites existing files" **after** package install and (per customize page) is
  copied in — files added here that are *outside* the dm-verity tree or writable-overlay are unmeasured. → **Oracle:**
  map which build outputs are inside vs outside the verity root hash.

**Doc evidence:** build-sample-ami.html (steps 2–4: `git clone`, `cargo install`, `dnf install`, mirror `<repository>`);
customize-sample-ami.html (arbitrary repos/packages/overlay/scripts; `edit_boot_install.sh` "runs `nitro-tpm-pcr-compute`
… called immediately after the bootloader is installed").
**Severity-if-true:** customer-side supply-chain = normally **customer footgun / out-of-scope** for AWS; **but** the fact
that a tampered input remains *transparent to attestation* is a design observation supporting Area 1/2 (the "attestable"
label gives false assurance). The AWS-authored sample recipe's pinning posture is the reportable slice (Tier-2).

### Area 4 — Lens U: boot-time measurement vs runtime state ("Maintaining an Attestable State")
**Background.** The whole "Maintaining an Attestable State" section (erofs in-memory writes, return-to-boot-state) exists
because measurements are **point-in-time at boot**. Runtime memory/process state is never re-measured until a restart.
**Security Concern.** An attacker with code exec inside a *running* attested instance operates entirely below the
attestation horizon: the instance already released its KMS-sealed secret at boot, and in-memory changes (permitted by the
ephemeral overlay) are invisible until reboot — at which point they vanish (erofs) rather than being detected. So
"attestable" bounds *what booted*, not *what is running now*. **Test Scenario:** confirm no re-attestation/continuous
measurement is documented; confirm a released data key remains usable after in-memory tampering. **Doc evidence:**
§Maintaining ("measurements are based on its initial boot state"; overlay writes "lost when the instance is restarted").
**Severity:** Informational (inherent to measured-boot); relevant only as a scoping caveat for anyone treating attestation
as runtime integrity.

### Area 5 — Lens R / S: AWS-authored tutorial IAM prerequisite block
**Background.** build-sample-ami.html "Prerequisites" tells the customer to grant `ec2:RegisterImage` on **all resources**
(`Resource:"*"`, unconditioned) and the three `ebs:*Snapshot*` actions on `arn:aws:ec2:*::snapshot/*`.
**Security Concern.** `ec2:RegisterImage` unconditioned is a known lead: RegisterImage is the entry point for
UEFI `--uefi-data` blob parsing and for registering AMIs over arbitrary snapshots (see [[ami-boot-plan]],
[[s3-backed-ami-plan]]); there is **no `ec2:BootMode`/`ec2:TpmSupport`/`ec2:UefiData` condition key** to scope it (Lens S:
"condition key does not exist"). The `arn:aws:ec2:*::snapshot/*` grant (empty account field = the direct-EBS-API snapshot
namespace) plus `PutSnapshotBlock` is raw-write-to-snapshot.
**Test Scenario:** audit whether a principal holding *exactly* this tutorial policy can register AMIs / write snapshot
blocks beyond the intended build (it can — nothing scopes it). **Severity:** Low — this is a **customer-authored** tutorial
policy (footgun, largely out-of-scope), *unless* it is presented as a copy-verbatim "required" block, in which case it is a
Lens-R hardening note. No AWS-managed policy is shipped by this feature.

### Area 6 — Lens Q chain-out: RegisterImage / UEFI blob surface (pointer, not owned here)
The `register-image … --boot-mode uefi --tpm-support v2.0` step touches the same server-side UEFI/`--uefi-data` parsing and
Secure Boot trust-anchor surface analysed in [[ami-boot-plan]] and [[uefi-secure-boot-plan]] (crown jewels: attacker-authored
`--uefi-data` blob parsed server-side = hard stop; empty-PK/SetupMode anchor forgery). **Do not duplicate** — route any
RegisterImage/UEFI-blob hunting to those plans. Noted here only because the attestable-AMI flow reaches that surface.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Same PCRs, different covered content → attests clean | reference PCR set (PCR4/7/12) | "hash represents all of its contents" (Area 1) |
| Backdoored image with self-computed valid PCRs | `nitro-tpm-pcr-compute` / `pcr_measurements.json` | (none — self-asserted) (Area 2) |
| Tampered build input transparent to attestation | KIWI repos/packages/overlay/scripts, coldsnap | "isolated compute environment" sample recipe (Area 3) |
| Measurement ≠ actual boot via `edit_boot_install.sh` | build script UKI selection | erofs/dm-verity return-to-boot-state (Area 3) |
| Runtime tamper below attestation horizon | ephemeral overlay / boot-time PCRs | "Maintaining an Attestable State" (Area 4) |
| Unconditioned RegisterImage / no TPM/boot condition key | tutorial IAM prereq | least-privilege prose only (Area 5) |
| Root fs unmeasured w/o dm-verity | erofs/dm-verity "can be used" (optional) | dm-verity integrity claim (Area 1) |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **The AMI build is single-tenant, in the customer's own account, on customer compute.** No shared service fleet is in
  this page's data path → no cross-tenant IDOR/DoS surface here (Lenses A, D, V, L null on *this* page).
- **The KMS attestation gate itself** (fail-open on absent attestation, wildcard/all-zero PCR acceptance, `PutKeyPolicy`
  bogus-PCR validation) is owned by the sibling `nitrotpm-attestation` plan — not re-hunted here.
- **The AWS Nitro measurement path, the AL2023 package-signing/mirror infrastructure, and the KMS attestation verifier**
  are AWS service plane → **HARD STOP** if evidence points there.
- **Customer-authored** KIWI image descriptions / additional repos / overlay content / IAM policies = customer footgun,
  out of scope (Area 3/5 caveat: the AWS-*authored* sample recipe and any copy-verbatim "required" policy are the only
  reportable slices).
- **Third-party reference repos** (`osinside/kiwi`, `awslabs/coldsnap`, NixOS samples) — bugs in them are upstream, not AWS.
- User steering the reasoning/content of their *own* attested workload; IMDS on the built instance.

---

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens A/D/V/M/N/J/I/H/O/Y/AA/F/K/C/E — null on this page.** Pages read: attestable-ami, build-sample-ami,
  al2023-isolated-compute-recipe, customize-sample-ami, create-pcr-compute, enable-nitrotpm-prerequisites. No shared fleet,
  no cross-account share, no server-side URL-dereference field, no OAuth/3P, no wire-protocol translator, no LLM, no new
  ARN/namespace, no TLS/SigV2 statement, no tagging/ABAC control, no session-id routing.
- **Lens G (SSRF) — null:** no field on these pages that the *service* dereferences server-side (all fetches are
  build-time, from the customer's own instance, under the customer's control). Confirmed by reading all six pages.
- **Lens W (attestation gate) — fires but is OWNED BY THE SIBLING PLAN.** This page contributes only the *build-side*
  enablers (which PCRs exist, that they are self-asserted, that PCR12 is the sole root-fs binder). The fail-open / under-
  binding / `PutKeyPolicy`-validation questions live in `skill-agent_..._nitrotpm-attestation.html.md` (AF-1..AF-4).
- **Doc gaps to confirm before live work:**
  1. Is dm-verity/erofs a **requirement** or merely recommended for an "Attestable AMI"? (§Requirements omits them → likely
     optional → Area 1 core.)
  2. Does the **dm-verity root hash actually feed the measured PCR12**, or only an unmeasured cmdline region? (Not stated —
     pivotal for Area 1; confirm from `nitro-tpm-pcr-compute` behaviour, not prose.)
  3. Does AWS perform **any** server-side validation of `pcr_measurements.json` provenance? (Docs show none → Area 2.)
  4. Hidden flags on `nitro-tpm-pcr-compute` (PCR-index/algorithm selection) that could weaken measurement scope.
  5. Whether `register-image` enforces any `--tpm-support`/`--boot-mode` IAM condition key (EC2 IAM reference — expected
     absent, mirroring ami-boot).

## Related plans
[[nitrotpm-attestation-plan]] (KMS-gate side; AF-1..AF-4), [[nitrotpm-plan]] (parent), [[enclaves-existing-plans]],
[[ami-boot-plan]] / [[uefi-secure-boot-plan]] (RegisterImage `--uefi-data` blob + Secure Boot anchor), [[s3-backed-ami-plan]]
(raw-bytes→snapshot→AMI), [[aws-docs-see-also-injection]] (none present on these pages).
