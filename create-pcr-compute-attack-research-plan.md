# `create-pcr-compute` (nitro-tpm-pcr-compute utility) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-pcr-compute.html` (offline mirror `docs/AWSEC2/latest/UserGuide/create-pcr-compute.md`, **byte-identical to the online `.md` twin, verified 2026-10-15, no drift**). Supporting pages read: `nitrotpm-attestation-document-content.md`, `prepare-attestation-service.md`, `nitrotpm-attestation.md`, `attestation-attest.md`, `attestable-ami.md`, `al2023-isolated-compute-recipe.md`, `build-sample-ami.md`, `customize-sample-ami.md`; IAM reference `docs/service-authorization/latest/reference/list_kms.md` and `list_ec2.html`.
Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **This is the measurement-GENERATOR deep-dive of the NitroTPM/Attestable-AMI cluster.** It is a tightly-scoped COMPLEMENT to its siblings and must not restate them. It owns the one page that defines *how the reference measurements are produced and what they structurally can and cannot contain*. The downstream KMS-gate authz logic, the all-zeros PCR12 smoking gun, the AMI build pipeline/supply chain, and the overlay-forgery mechanics are OWNED elsewhere and only cross-referenced here:
> - `attestable-ami-attack-research-plan.md` — build/measurement **root cause** of reproducibility (A1); erofs/dm-verity one-hop commitment framing.
> - `nitrotpm-attestation-attack-research-plan.md` — the **KMS-gate** level: A1 reproducible-PCR bypass, **A2 all-zeros PCR12** (confirmed smoking gun), A3 ImageSha384; CRL/alg-pin.
> - `customize-sample-ami-attack-research-plan.md` — **CONFIRMED measurer hashes UKI-only not erofs**, overlay overwrites measurer pre-self-measure (forged refs), KIWI `package_gpgcheck` default=false, `<ignore>` not a deny-list.
> - `build-sample-ami-attack-research-plan.md` — supply chain: `cargo install` ignores git-clone (unpinned crates.io), `<rpm-check-signatures>true`, KIWI script matrix (`editbootinstall` = build-host root, not chrooted), register/snapshot IAM prereqs.
> - `enable-nitrotpm-support-on-ami-attack-research-plan.md` / `al2023-isolated-compute-recipe-attack-research-plan.md` — `--uefi-data=attacker` PCR7; ephemeral-overlay-NOT-measured (W1).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Most oracles here are **static / offline** (build two UKIs and compare the tool's output; `objdump`/`ukify` a `.efi`; `iam:SimulateCustomPolicy` on a KMS key policy) — this page has **no live AWS call of its own**.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the Nitro attestation signer, a KMS fleet key), stop, preserve evidence, flag for AWS-Security disclosure. The KMS-decryption-bypass *end* of the kill chain (reading a victim's keys) must only ever be exercised with your own canary KMS key and canary secrets — never a third party's.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Produce two materially-different Attestable images whose `nitro-tpm-pcr-compute` output (PCR4/PCR7/PCR12) is byte-identical** — proving the reference measurement is an identity *collision*, not an identity. (Measurement-vs-identity gap.)
2. **Show that the three values the tool emits do not commit the running root filesystem, the ephemeral overlay, first-boot code, or any secondary volume** — i.e. a backdoored-but-attested image passes a KMS gate authored from this tool's output.
3. **Show that the root-of-trust generator itself (`aws-nitro-tpm-tools`) is installed with no documented signature verification on the build host**, so a tampered/MITM'd tool emits attacker-chosen "reference" values for any image.
4. **Show the emitted JSON is an unsigned, self-asserted artifact** with no binding to the image, the account, or the Nitro platform — hand-copied into a KMS policy.
5. **Show AWS's documented PCR7-only Secure-Boot path pins a coarse, image-independent value** — attesting "Secure Boot was on", not "this image booted".

> Objectives 1/2/5 are the AWS-authored measurement-semantics defects this plan OWNS. The *consequence* (cross-account KMS key access by an attested backdoored instance) is the kill-chain END owned by `nitrotpm-attestation`; rate chained leads at that end.

---

## 2. Components, Assets, and Design

**What this page is:** documentation for a single local CLI, `nitro-tpm-pcr-compute`, shipped in the RPM `aws-nitro-tpm-tools`, that reads a Unified Kernel Image (`UKI.efi`) and prints reference PCR measurements as JSON. It is run at **AMI build time** on a **customer-owned EC2 build instance** (`build-sample-ami.md:29`). There is **no AWS API, no IAM action, no service endpoint, no ARN on this page** (full-read confirmed; `customize-sample-ami-attack-research-plan.md:62` corroborates "no AWS API on this page … no cross-tenant surface").

**The utility (verbatim surface):**
- Install: `sudo yum install aws-nitro-tpm-tools` → binaries in `/usr/bin` (`create-pcr-compute.md:15-21`). The sample image also auto-installs it *into the built image* (`:10`; `build-sample-ami.md:10` — both `nitro-tpm-pcr-compute` and `nitro-tpm-attest`).
- Invocation: `/usr/bin/nitro-tpm-pcr-compute --image {{UKI.efi}}` — the UKI is the **only** required input, "Required for Standard boot and UEFI" (`:28-37`).
- Output (the entire output surface):
  ```
  { "Measurements": { "HashAlgorithm": "SHA384 { ... }",
      "PCR4": "{{…}}", "PCR7": "{{…}}", "PCR12": "{{…}}" } }
  ```
  — exactly three PCRs + a hash-algorithm string, no signature, no account/image id (`:42-49`; identical in `build-sample-ami.md:76-83`).

**What each emitted PCR actually measures** (authoritative, `nitrotpm-attestation-document-content.md` + `list_kms.md:740-794`):
- **PCR4** = boot-manager code / "all the binaries executed by its UEFI environment … the single boot binary hash can describe exactly what code an instance will execute" (`…content.md:25`; KMS: "boot loader and additional drivers … loaded by the boot loader").
- **PCR7** = "a hash of the instance's UEFI Secure Boot policy" / "Secure Boot state" (`…content.md:26`; KMS `list_kms.md:762`).
- **PCR12** = "hash of the command line passed to the UEFI boot binary … Required in conjunction with PCR4 for standard boot" (`…content.md:29`; KMS: "kernel command line, system credentials and system configuration images").
- **NOT emitted:** PCR0/1 (AWS-controlled firmware, "always contain constant values", `…content.md:11`), PCR2/3/5/6, PCR8–15 (except 12), PCR16(Debug), PCR23. KMS exposes `kms:RecipientAttestation:NitroTPMPCR0–23` + `ImageSha384` — **24 pins available, the tool gives you 3.**

**Measurement input scope (CONFIRMED by siblings):** the measurer is only ever pointed at the UKI binary (`…/EFI/BOOT/$EFI_BINARY`), never the erofs rootfs (`customize-sample-ami-attack-research-plan.md:95,220`). UKI = kernel + initrd + boot params as one immutable binary (`al2023-isolated-compute-recipe.md:10`). The erofs read-only root is protected by **dm-verity, a separate mechanism** (`al2023-isolated-compute-recipe.md:12`, `attestable-ami.md:16`); the runtime overlay (`/etc`,`/run`,`/var`) is **in-memory, never measured** (`al2023-isolated-compute-recipe.md:14`).

```
                         BUILD HOST  (customer-owned EC2, build-host root)
 public recipe (GitHub) ─────────────┐
 unpinned AL2023 mirror pkgs ─────────┤→ KIWI NG build → raw disk ─→ UKI.efi ──┐
 overlay tree (/root/) ───────────────┘   (editbootinstall, LAST disk step)    │
 aws-nitro-tpm-tools RPM (yum, no doc'd gpg) → /usr/bin/nitro-tpm-pcr-compute ──┤
                                                                                ▼
                                          nitro-tpm-pcr-compute --image UKI.efi
                                                                                │ (deterministic SHA384, no secret, no API)
                                                                                ▼
                                   pcr_measurements.json  {PCR4, PCR7, PCR12}  ── hand-copied ──┐
                                                                                                ▼
   RUNTIME (any account):  Attestable instance ─ NitroTPM attestation doc ─→  KMS key policy  (StringEqualsIgnoreCase
                                                                              kms:RecipientAttestation:NitroTPMPCR4/7/12)
                                                                                                │ match → Decrypt/GenerateDataKey allowed
                                                                                                ▼  [cross-account END — owned by nitrotpm-attestation]
```

**The seam this page defines:** the *reference* side of the attestation equality check is manufactured here, by a builder-controlled tool, over a builder-controlled artifact, with no provenance on either, emitting exactly 3 of 24 possible pins. Every KMS gate downstream is only as strong as this generator's coverage.

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `nitro-tpm-pcr-compute --image <UKI.efi>` | local CLI | Existing (NitroTPM GA tooling) | No (read+print) | **Local only** | Hash a UKI → PCR4/7/12 JSON | **No** | anyone with the RPM + a UKI file | No AWS call; deterministic; no secret/nonce/account input |
| `yum install aws-nitro-tpm-tools` | pkg install | Existing | Yes (host fs) | Local (pulls from AL2023 repo) | Install the generator (+`nitro-tpm-attest`) | repo fetch only | build-host root | **No GPG guidance on this page** |
| `edit_boot_install.sh` | KIWI build hook | Existing | Yes (writes `pcr_measurements.json`) | Local, **build-host root, NOT chrooted** | Locates UKI, runs the measurer | No | KIWI NG during build | doc'd on `build-sample-ami.md:12`, `customize-sample-ami.md:46`; cross-ref build/customize plans |

**Downstream authz keys (not on this page, but the consumer of its output):** `kms:RecipientAttestation:NitroTPMPCR4`, `:NitroTPMPCR7`, `:NitroTPMPCR12` on KMS `Decrypt`/`GenerateDataKey`/`GenerateDataKeyPair`/`GenerateRandom`/`DeriveSharedSecret` (`prepare-attestation-service.md:13-15`, `attestation-attest.md:8-10`). **`list_ec2.html` contains ZERO PCR/attestation/`TpmSupport` keys** — the entire measurement→authz binding lives in KMS, nothing in EC2.

**Undocumented/console-hidden knob sweep:** the tool exposes a single documented flag (`--image`). Undocumented flags/output fields (e.g. whether it can emit PCR0-3 or accept a non-UKI target, whether `HashAlgorithm` is selectable) are a **doc-gap lead** — enumerate `nitro-tpm-pcr-compute --help` / strings on the real binary (W4).

---

## 4. Boundary-lens catalog — firing lenses

### Area 1 — [HEADLINE, Lens W + U] The tool structurally emits only 3 of 24 PCRs → under-binding is baked into the generator
**Background.** A KMS attestation gate is only as strong as the set of PCRs it pins, and a policy author pins the values this tool hands them. The tool emits **exactly PCR4, PCR7, PCR12** and cannot emit PCR0/1/2/3/5/6/8-11/13-15 (`create-pcr-compute.md:42-49`). KMS defines 24 `NitroTPMPCR0–23` keys (`list_kms.md`), so a conscientious author who "pins everything the tool gives me" still leaves 21 registers free.
**Security Concern.** PCR4 (boot binary), PCR7 (Secure Boot *policy*), PCR12 (kernel cmdline) commit the **boot chain up to and including the UKI** and *nothing about the running root filesystem, the ephemeral overlay, first-boot/runtime code, or any secondary EBS volume* (`customize-sample-ami-attack-research-plan.md:95` CONFIRMED measurer hashes UKI-only; `al2023-isolated-compute-recipe.md:14` overlay in-memory, never measured). Nothing in the tool's output or page warns the operator what is omitted. A verifier therefore equates "these 3 PCRs match" with "my trusted image is running" — a false equivalence.
**High-level Test Scenarios (falsifiable):**
- **Claim:** Two Attestable images with the **same UKI** but **different erofs rootfs/overlay content** produce **identical** PCR4/7/12 → the KMS gate cannot distinguish a clean image from a backdoored one. → **Oracle:** build UKI-identical images A (clean) and B (malicious payload added via overlay tree, *not* altering the UKI), run `nitro-tpm-pcr-compute --image` on each; identical triple = collision confirmed. → **Precondition:** the rootfs change does not alter the UKI cmdline (see Area 2). → **Severity-if-true:** High (feeds cross-account KMS bypass END owned by `nitrotpm-attestation`).
- **Claim:** The decisive question — **does the erofs/dm-verity root hash reach the UKI embedded cmdline (→ PCR12) before `--image` runs?** If NOT, rootfs changes are entirely attested-invisible; if yes, only *rootfs-baked* changes are bound (runtime overlay still invisible). This is left OPEN in both the customize (`:97,224`) and attestable siblings. → **Oracle (static):** `objdump -s -j .cmdline UKI.efi` / `ukify inspect` — look for `roothash=` / `rd.verity` / `usrhash=` tokens in the embedded `.cmdline` section. Presence → rootfs bound via PCR12; absence → attested-invisible rootfs. → **Severity-if-true (absence):** High; this single static check decides the blast radius of Area 1 and W1.
- **Claim:** A KMS policy authored from this tool's output cannot pin firmware/platform/OS-runtime registers because the tool never produces them → under-binding is non-remediable with the documented tooling alone. → **Oracle:** `iam:SimulateCustomPolicy` on the `prepare-attestation-service.md:19-44` example — confirm only PCR4/7/12 are conditioned.
**Doc evidence:** `create-pcr-compute.md:42-49,28`; `nitrotpm-attestation-document-content.md:11,14-15,24`; `list_kms.md:740-794`. **Severity-if-true:** High (AWS-authored tool + sample defect, Tier-2 reportable). **Stop:** once a measurement collision is demonstrated offline; do not exercise the live KMS decrypt against any non-canary key.

### Area 2 — [Lens W, sharp] The documented PCR7-only Secure-Boot path pins an image-independent value
**Background.** `prepare-attestation-service.md:13` tells authors: *"Use PCR4 and PCR12 measurements for standard boot **or PCR7 measurements for Secure Boot**."* The tool emits PCR7 as a standalone value, inviting a PCR7-only gate for Secure-Boot images.
**Security Concern.** PCR7 = "hash of the instance's UEFI **Secure Boot policy** / Secure Boot **state**" (`…content.md:26`, `list_kms.md:762`) — a function of the enrolled keys/policy, **not** of which image booted. Every image signed under the same Secure Boot key set yields the **same PCR7**. A gate pinning only `NitroTPMPCR7` therefore attests "Secure Boot is on with policy X" and authorizes **any** image under that policy — including an attacker's.
**High-level Test Scenarios:**
- **Claim:** Two different Attestable images signed under the same UEFI Secure Boot keys produce identical PCR7 → a PCR7-only KMS gate is satisfied by both. → **Oracle:** build two images differing in UKI/rootfs but same SB signing key; compare the tool's PCR7 field; `SimulateCustomPolicy` a PCR7-only policy against both attestation docs (or reason from the equality). → **Severity-if-true:** High (image-independent authz on the AWS-recommended Secure-Boot shortcut).
**Doc evidence:** `prepare-attestation-service.md:13`; `nitrotpm-attestation-document-content.md:26`; `list_kms.md:762`. **Severity-if-true:** High. **Stop:** at demonstrated PCR7 equality.

### Area 3 — [Lens R/Q/U, supply chain] The root-of-trust generator is installed with no documented signature verification
**Background.** `create-pcr-compute.md:15-19` installs the measurer with a bare `sudo yum install aws-nitro-tpm-tools` — **no GPG key, no `--enablerepo`/signature guidance, no checksum** anywhere on the page. The tool that *manufactures the reference measurements* is itself an unverified-on-this-page download.
**Security Concern.** If the build host's dnf/yum config has `gpgcheck` off for the repo serving this package (default is **undocumented on this page**; KIWI's *in-image* per-repo `package_gpgcheck` default is `false` per `customize-sample-ami-attack-research-plan.md:126`), a tampered or MITM'd `aws-nitro-tpm-tools` emits **attacker-chosen** PCR4/7/12 for *any* UKI. The reference measurements would then describe an image the attacker never built, or make a backdoored image produce "clean" values — a root-of-trust inversion. This compounds the sibling-owned finding that the measurer is the image's own *overwritable in-image copy* (`customize-sample-ami-attack-research-plan.md:95` overlay overwrites `root/usr/bin/nitro-tpm-pcr-compute` before it self-measures). **Both the install source and the in-image copy are untrusted; this page owns the install-source half.**
**High-level Test Scenarios:**
- **Claim:** The build-host `yum install aws-nitro-tpm-tools` performs no signature verification by default on a stock AL2023 build host → a substituted RPM is accepted silently. → **Oracle:** on an AL2023 instance, inspect the repo definition serving the package for `gpgcheck=` and whether a signing key is pre-imported; attempt install of a locally-rebuilt unsigned `aws-nitro-tpm-tools`. → **Severity-if-true:** High (forged reference measurements for arbitrary images; AWS-authored install instruction omits the control). → **This is single-tenant/customer-side supply chain — not cross-tenant.**
- **Claim:** No provenance/signing check is performed on the UKI *before* `--image` hashes it → the measurer trusts whatever `.efi` it is handed. → **Oracle:** feed an unsigned/foreign UKI to the tool; it still emits a measurement. → **Severity-if-true:** Medium (measurement of an unverified artifact; by-design but undocumented).
**Doc evidence:** `create-pcr-compute.md:15-19,35-37`; `al2023-isolated-compute-recipe.md:10`. **Severity-if-true:** High (install) / Medium (UKI provenance). **Stop:** at confirmation of the default gpgcheck posture.

### Area 4 — [Lens U] The emitted measurement is an unsigned, self-asserted artifact
**Background.** The tool's entire output is a plain-stdout JSON of three hex strings + `"HashAlgorithm": "SHA384 { ... }"` (`create-pcr-compute.md:42-49`). There is **no signature over the JSON, no account id, no image id, no Nitro-platform attestation of the generator**, and the values are hand-copied into a KMS policy (`prepare-attestation-service.md:19-44`).
**Security Concern.** Nothing binds the reference JSON to the image it supposedly describes or to the account that built it. Combined with determinism (A1, owned by attestable/nitrotpm siblings — **cross-ref, not restated**), anyone holding (or rebuilding, from the public recipe) a target's UKI can **pre-compute the exact PCR values a victim's KMS policy pins, using the same official public RPM as an offline oracle**. The generator is the forgery tool.
**High-level Test Scenarios:**
- **Claim:** `HashAlgorithm` is self-asserted and the only algorithm is SHA384; a verifier that trusts the JSON's stated algorithm/structure has no cryptographic assurance the values came from a genuine build. → **Oracle:** inspect output; confirm no signature/MAC field exists. → **Severity-if-true:** Low–Informational (artifact-integrity gap; the real integrity must come from the live NitroTPM attestation doc + KMS, not this JSON).
- **Claim (recon/forgery enabler):** the public `aws-nitro-tpm-tools` RPM lets an attacker reproduce a victim's PCR4/7/12 offline given the victim's (public-recipe-derived) UKI, with zero AWS round-trip. → **Oracle:** rebuild the public sample image twice on independent hosts; byte-compare the tool's output. → **Severity-if-true:** High *as the entry of the kill chain whose END is cross-account KMS access* (rate at the END; END owned by `nitrotpm-attestation` A1). → **HARD STOP** before touching any non-canary KMS key.
**Doc evidence:** `create-pcr-compute.md:42-49`; `nitrotpm-attestation.md:23-25`. **Severity-if-true:** Low (artifact) → High (chained). **Stop:** at offline reproduction.

### Area 5 — [Lens W, cross-ref to A2] A verifier may pin a dead/all-zeros PCR12
**Background.** AWS's canonical example policy pins `kms:RecipientAttestation:NitroTPMPCR12` to **96 hex zeros** (`prepare-attestation-service.md:38`) — the TPM's uninitialized/never-extended value. This smoking gun is **OWNED by `nitrotpm-attestation-attack-research-plan.md` A2 (lines 99-109)** and is only referenced here.
**Security Concern (this page's angle only).** The tool *does* emit a real PCR12 for a standard-boot UKI, yet AWS's example discards it for all-zeros — a mismatch between what the generator produces and what the sample pins. A verifier copying the example gets a PCR12 condition that matches **any** instance whose PCR12 is unextended, i.e. an under-binding the generator's output would have prevented. → **Oracle:** diff the tool's PCR12 for the sample image against the example policy's `{{000…}}`; `SimulateCustomPolicy` to confirm the zero-condition is satisfiable. → **Severity-if-true:** High (but **report under A2**; this plan contributes the generator-vs-sample mismatch observation only).
**Doc evidence:** `prepare-attestation-service.md:37-38`; `create-pcr-compute.md:42-49`. **Severity:** High (deduplicate into A2). **Stop:** immediately — hand to the attestation plan.

---

## 5. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| UKI-identical / rootfs-different image collision | measurer output | "the single boot binary hash can describe exactly what code an instance will execute" (`…content.md:25`) — attack: it describes the boot binary, not the rootfs |
| rootfs/overlay attested-invisible (dm-verity hash not in cmdline) | PCR12 coverage | implied one-hop commitment erofs→roothash→cmdline→PCR12 (unconfirmed, `attestable-ami` plan) |
| PCR7-only Secure-Boot gate authorizes any same-policy image | PCR7 semantics | `prepare-attestation-service.md:13` offers PCR7-only as a valid path |
| Forged reference via tampered/unsigned `aws-nitro-tpm-tools` | build-host install | none shown on page (`:15-19` bare `yum install`) |
| Forged reference via overlay-overwritten in-image measurer | in-image `/usr/bin` copy | OWNED by `customize-sample-ami` Area 4 — cross-ref |
| Offline pre-computation of a victim's pinned PCRs | public RPM determinism | OWNED by `attestable-ami` A1 / `nitrotpm-attestation` A1 — cross-ref |
| All-zeros PCR12 pin satisfiable by unextended TPM | KMS example policy | OWNED by `nitrotpm-attestation` A2 — cross-ref |

---

## 6. Out-of-Scope Risk Categories
- **Cross-tenant / cross-account primitives on THIS page** — none exist. The tool is a local CLI on a **customer-owned build instance** (`build-sample-ami.md:29`); no AWS API, IAM action, or network endpoint. The cross-account *consequence* (a victim KMS key vending to an attested-but-backdoored instance) is the kill-chain END owned by `nitrotpm-attestation` and must be tested only against canary keys.
- **The live NitroTPM attestation document, its Nitro-signer, and KMS's validation of it** — AWS service plane. **HARD STOP** on any evidence reaching the signer or a fleet key.
- **Customer-authored KMS key policy least-privilege choices** — a customer who pins only PCR7, or copies the all-zeros example, is partly a customer footgun; the **AWS-authored** defects (tool emits only 3 PCRs; the sample pins all-zeros; the install omits signature guidance) are the in-scope, Tier-2-reportable parts.
- **The AMI build pipeline supply chain beyond the tool install** (`cargo install` unpinned, KIWI gpgcheck, overlay-overwrites-measurer, `<ignore>` deny-list) — OWNED by `build-sample-ami` / `customize-sample-ami`.
- **PCR4-via-`--uefi-data` injection / Secure-Boot `.ps1`** — OWNED by `enable-nitrotpm-support-on-ami`.
- **Single-tenant self-DoS, IMDS on the build host, DNS rebinding** — out of scope.

---

## 7. Null hypotheses / doc gaps (pages named)
- **Lens A (IDOR) — NULL.** Read `create-pcr-compute.md` in full: no resource id, no tenant id, no API returning a resource. Local CLI only.
- **Lens G (SSRF) — NULL.** The only input is a local `UKI.efi` file path; no field the service dereferences, fetches, or renders. Read full page + `build-sample-ami.md`/`customize-sample-ami.md` — the only network action is `yum`/`dnf` package fetch (→ Area 3 supply chain, not SSRF).
- **Lens B/C/E (PassRole/vending/RBAC) — NULL on this page.** No role ARN, no AssumeRole, no SLR; runs under the operator's own identity (`customize-sample-ami-attack-research-plan.md:62`). Build-sample-ami's `ebs:*`/`ec2:RegisterImage` prereqs gate *later* steps, not the measurer.
- **Lens F (injection) — doc-gap.** The tool is a native binary parsing an attacker-influenceable `.efi`; a malformed/oversized UKI could crash or mis-measure it. Not described in docs → "doc-gap — confirm the binary's parser behavior offline" (fuzz `--image` with truncated/oversized/non-PE inputs). Single-tenant; Low unless it yields a forged measurement.
- **Lens Q (upload) — partial, folded into Area 1/3.** The `.efi` is the "blob"; its parsing is the surface. No cross-tenant file path.
- **Lenses H/I/J/M/N/O/V/X/Y/AA/BB/CC/DD/EE/FF — NULL** (read full page): no CMK-at-create, no tagging, no OAuth, no session id, no namespace migration, no audit surface, no network segmentation, no action-twin, no transport/TLS endpoint, no share/revoke, no multi-parser request path, no upstream-context header, no cache, no predictable global name, no token/JWT on this local-CLI page.
- **Open doc-gaps carried (settle before investing):**
  1. **Does the dm-verity root hash reach the UKI cmdline (→ PCR12) before `--image` runs?** (Area 1) — the single most load-bearing unknown; static `objdump`/`ukify` of a real `.efi` settles it.
  2. **Default `gpgcheck` posture of the build-host repo serving `aws-nitro-tpm-tools`** (Area 3) — not stated on this page.
  3. **The tool's full flag/output surface** (does `--help` expose a way to emit more/other PCRs or select the hash algorithm?) — enumerate on the real binary (undocumented-knob sweep).
  4. **Whether the deployed sample emits PCR12 at all vs the example pinning all-zeros** (Area 5 / A2) — generator-vs-sample mismatch.

---
*Cross-references:* `attestable-ami` (A1 root cause), `nitrotpm-attestation` (A1 KMS gate, A2 all-zeros, A3 ImageSha384), `customize-sample-ami` (UKI-only measurer, overlay-overwrites-measurer, KIWI gpgcheck), `build-sample-ami` (cargo/rpm supply chain, build-host-root script matrix), `enable-nitrotpm-support-on-ami` (`--uefi-data` PCR7), `al2023-isolated-compute-recipe` (W1 ephemeral-overlay-not-measured). See [[reference-aws-iam-service-auth-ref-url]].
