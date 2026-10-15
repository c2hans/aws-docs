# AL2023 Isolated-Compute Recipe (Sample Image Description) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/al2023-isolated-compute-recipe.html` (= `.md` twin; offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/al2023-isolated-compute-recipe.md`). Supporting pages read in full: `isolate-data-operators.html` (parent / best-practices), `attestable-ami.html` (hub), `build-sample-ami.html`, `customize-sample-ami.html`, `create-pcr-compute.html`, `working-with-isolated-amis.html`; plus `nitrotpm-attestation-document-content.html`, `prepare-attestation-service.html`, `nitrotpm-attestation.html`, serial-console pages, IMDS pages, SSM `setup-instance-permissions`, EC2 Instance Connect `API_SendSSHPublicKey` / `connect-with-ec2-instance-connect-endpoint`, `set-time`/`configure-ec2-ntp`, `nitrotpm-attestation-document-validate`, and `docs.kernel.org/.../verity.html`.
Verified offline == online 2026-10-15 (byte-identical content; only `---source_url---` frontmatter differs).
Status: documentation-derived hypotheses only; nothing tested against a live account.

> **Relationship to existing sibling plans (do NOT re-derive — cross-reference).** This page is the **sample image-description recipe** child of the *Attestable AMI* hub. The attestation/KMS/measurement core is already owned by:
> - `attestable-ami-attack-research-plan.md` — AMI-build/measurement root-cause (reproducible-measurement zero-owner-entropy, RegisterImage `*` + ebs-direct no-ownership-key, boot-time-only TOCTOU, KIWI build-host-root code-exec, dm-verity lazy-verify window).
> - `build-sample-ami-attack-research-plan.md` — build/supply-chain (cargo-install ignores git-clone unpinned crates.io, measurer rides in measured image, PCR4/7/12-vs-4/7 disagreement, ebs:* vs ec2:CreateSnapshot, SSM/cloud-init stripped).
> - `nitrotpm-attestation-attack-research-plan.md` — attestation-doc/KMS-verifier (A1 reproducible-PCR bypass, A2 AWS-example PCR12=all-zeros, A3 ImageSha384 3rd family, CRL-off/alg-pin).
> - `nitrotpm-*`, `enable-nitrotpm-*`, `verify-nitrotpm-*`, `retrieve-ekpub` — NitroTPM lifecycle / read-path / EK.
>
> **This plan owns only the recipe-content surface** — the 4 image characteristics (UKI / erofs+dm-verity / ephemeral overlay / remote-access-removal) read as *security guarantees*, their enforcement gaps, and the completeness gap of the AWS-authored sample vs its own parent's best-practices list. Where a lead is really an attestation-core concern, it is a pointer, not a restatement.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- This is a **guarantee-dense, API-sparse** security-chapter page: it introduces **no new mutating EC2 API**. Dominant lenses are **U** (doc-guarantee-vs-enforcement + completeness), **W** (attestation coverage), **R** (AWS-authored copy-verbatim sample under-delivery), **X** (control-plane twin surviving an in-guest removal). A/B/C/E/F/G/H/J/M/N/BB/CC/DD/FF are null here (see §8) — the resources are the *customer's own* AMI/instance, so there is **no cross-tenant customer-testable primitive on this page**.
- Most leads are settleable **read-only**: `iam:SimulateCustomPolicy` for IAM-expressibility, `DescribeInstanceMetadataOptions`/`DescribeSerialConsoleAccess`/`get-image-attribute imdsSupport` for posture, and a single synthetic canary instance from the sample AMI for the runtime overlay/measurement questions.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the NitroTPM/KMS attestation verifier internals), stop, preserve evidence, flag for AWS-Security disclosure. The Nitro "zero operator access" property (`isolate-data-operators.html` → `no-aws-operator-access` whitepaper) is an **out-of-scope AWS-infra guarantee** — do not probe it.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes to pursue (all intra-account / within the customer's own trust zone — the recipe's threat model is the customer's *own operators*, not another tenant):
1. **Defeat the "trusted state" guarantee at runtime without changing attestation** — mutate the live `/etc`/`/var` overlay of a booted isolated instance such that the workload processes attacker-influenced config/binaries while the instance still produces PCR4/7/12 identical to the clean reference AMI and KMS attestation keeps succeeding.
2. **Reach a removed access channel through its surviving control-plane twin** — attach the Nitro serial console, or deliver/read user-data via IMDS, on an instance the recipe claims has "no remote access."
3. **Recover live instance-role credentials from in-guest code** via the IMDS endpoint the recipe never hardens (the real "operator ↔ instance" bridge the isolation claim omits).
4. **Show the AWS-authored sample, copied verbatim, under-delivers vs its own parent best-practices** (no in-instance firewall, no API-call restriction) and silently ships IMDSv1-capable.
5. **Attest a divergent/malicious image** by exploiting that reference measurements are builder-asserted with no AWS-side re-measurement (pointer to attestable-ami / build-sample-ami plans).

---

## 2. Components, Assets, and Design

**What this is.** A KIWI NG *image description* (XML `appliance.kiwi` + overlay tree + `edit_boot_install.sh`) that AWS ships as `kiwi-image-descriptions-examples` (GitHub `amazonlinux/kiwi-image-descriptions-examples`) to build an **Attestable AMI** for an *isolated compute environment* — a confidential-compute-style box whose stated goal (`isolate-data-operators.html`) is that **even the customer's own operators cannot reach the instance or its data**.

**The four asserted characteristics (each is a security *guarantee* to trace to a mechanism):**
1. **UKI (Unified Kernel Image) signed boot** — one immutable signed binary = kernel + initrd + boot params. Measured as **PCR4** (boot-manager binary hash) and its cmdline as **PCR12**; UEFI Secure Boot policy = **PCR7**.
2. **Read-only root fs** — `erofs` + `dm-verity`. dm-verity root hash lives in the kernel cmdline (→ inside the signed UKI → PCR12). Verifies blocks **lazily on-access**, fail-closed.
3. **Ephemeral overlay** — in-memory writable overlay for `/etc`, `/run`, `/var`; wiped on **reboot** ("returns to original trusted state"). **Not on the dm-verity device; not an input to `nitro-tpm-pcr-compute`.**
4. **Disabled remote access** — 7 methods, 6 removed by *omitting a package*, serial console by *kernel cmdline param*: SSH (`openssh-server`), user-data (`cloud-init`,`cloud-init-cfg-ec2`), chrony (`amazon-chrony-config`), MOTD (`update-motd`), SSM (`amazon-ssm-agent`), EC2 Instance Connect (`ec2-instance-connect`), serial console (kernel param).

**Build/measurement pipeline (owned by build-sample-ami / attestable-ami plans — summarized for context):**
```
customer EC2 build host (AL2023)
  └─ dnf install kiwi-cli python3-kiwi ... aws-nitro-tpm-tools   (AL2023 repo)
  └─ git clone awslabs/coldsnap ; cargo install --locked coldsnap (unpinned)
  └─ dnf install kiwi-image-descriptions-examples                 (sample recipe)
  └─ kiwi-ng system build --description .../attestable-image-example
        ├─ installs packages into erofs root (dm-verity)
        ├─ builds signed UKI (.efi)
        └─ edit_boot_install.sh → nitro-tpm-pcr-compute --image UKI.efi
              → ./image/pcr_measurements.json {PCR4,PCR7,PCR12}   ← BUILDER-ASSERTED
  └─ coldsnap upload *.raw → EBS snapshot (ebs:PutSnapshotBlock)
  └─ aws ec2 register-image --tpm-support v2.0 --boot-mode uefi   (NO --imds-support)
→ reference measurements pasted into KMS key policy (kms:RecipientAttestation:PCRn)
→ instance boots → NitroTPM attests PCRs → KMS Decrypt/GenerateDataKey gated on match
```

**Assets:** the attested "trusted boot state"; the data the KMS attestation gate protects; the instance-role credentials served by IMDS; the builder's UEFI signing keys (PK/KEK/db).

**Identity / roles on *this* page:** none introduced. Build-time IAM (`ebs:StartSnapshot/PutSnapshotBlock/CompleteSnapshot` on `snapshot/*`, `ec2:RegisterImage` on `*`) is owned by the build-sample-ami plan.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| In-guest code (workload / dropped binary) | Attested "trusted state" | Writes to the in-memory overlay `/etc`,`/var` not covered by PCR4/7/12 | Runtime overlay is modified **and** `nitro-tpm-attest` still yields clean PCR4/7/12 → KMS attestation succeeds against the *reference* AMI values |
| In-guest code | Instance-role credentials / launch secrets | IMDS `169.254.169.254` (recipe never hardens; AMI registered without `--imds-support v2.0`) | A GET to `/latest/meta-data/iam/security-credentials/<role>` or `/latest/user-data` returns live creds / operator-set user-data from inside the "isolated" box |
| Customer operator (control plane) | "Removed" serial console | `ec2:EnableSerialConsoleAccess` (account) + `ec2-instance-connect:SendSerialConsoleSSHPublicKey` (IAM) — Nitro virtual UART, independent of guest kernel param | A serial-console **attach** succeeds on an instance whose AMI "disabled" it (even if the port is silent) |
| Customer operator (control plane) | "Removed" user-data execution | user-data still delivered via IMDS at launch regardless of cloud-init removal | User-data provided at `RunInstances` is retrievable in-guest → one-way operator→instance channel the "elimination" claim denies |
| Compromised/malicious builder | Third-party attestation consumer | Reference PCRs are builder-asserted; no AWS re-measurement; standard-boot path has no signature check | A divergent image produces PCRs the builder places into a KMS policy and attests cleanly (pointer: attestable-ami / nitrotpm-attestation) |
| AWS Nitro host ↔ instance | — | "Zero operator access" (Nitro) | **OUT OF SCOPE / HARD STOP** — AWS-infra guarantee, do not probe |

---

## 4. API / Interface Inventory
This page defines **no API**. The security-relevant interfaces it implies (and that the plan tests) are posture reads and one build/register action, all owned elsewhere; listed here only so the hunter has the handles:

| Name | Mutating | Internet-callable | Role here | Notes |
|---|---|---|---|---|
| `GetInstanceMetadata` (IMDS HTTP, in-guest `169.254.169.254`) | No | No (link-local) | Credential/user-data exfil surface the recipe omits | IMDSv2 token optional unless hardened |
| `ec2:DescribeInstanceMetadataOptions` / `ModifyInstanceMetadataOptions` | — / Yes | Yes | Confirms AMI/instance IMDS posture | Recipe never sets it |
| `ec2:DescribeSerialConsoleAccess` / `EnableSerialConsoleAccess` / `DisableSerialConsoleAccess` | — / Yes | Yes | Serial-console control plane surviving the kernel param | Account-level, default disabled |
| `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | Yes | Yes | Serial-console attach grant | Gated on instance ARN |
| `ec2:RegisterImage` (`--imds-support`, `--tpm-support`, `--boot-mode`) | Yes | Yes | Build-time; sample omits `--imds-support v2.0` | Owned by build-sample-ami plan |
| `nitro-tpm-pcr-compute --image UKI.efi` (in-guest build tool) | No | No | Produces builder-asserted PCR4/7/12 | Input is **UKI only** |
| `nitro-tpm-attest` (in-guest, preinstalled `/usr/bin/`) | No | No | Runtime attestation document generation | — |

No `[NEW]` marker or "testing should focus on" sentence on the page. The whole *Attestable AMI* feature is recent/under-reviewed surface → §5 priority.

---

## 5. Recommended Areas of Focus

### Area W1 — Ephemeral overlay is outside the attestation measurement (HEADLINE) — Lens W / U
**Background.** PCR reference measurements are produced by `nitro-tpm-pcr-compute --image {{UKI.efi}}` (`create-pcr-compute.html`) → **PCR4** (boot-manager binary = the UKI), **PCR7** (Secure Boot policy), **PCR12** (UKI cmdline, which carries the dm-verity root hash). The ephemeral overlay for `/etc`,`/run`,`/var` is, per `attestable-ami.html`, "stored in memory and lost when the instance is restarted" — it is **not on the dm-verity block device and is not an input to the PCR utility.**
**Security Concern.** The recipe sells the overlay as "ensuring the system returns to its original trusted state." That is a **persistence** guarantee (a reboot wipes tampering), **not a runtime-integrity** guarantee. Measurement happens once, at boot, over the UKI. Any in-guest primitive that writes attacker-controlled content into the writable overlay (`/etc/<svc>.conf`, a binary under `/var`, an `LD_PRELOAD` shim, a systemd drop-in) changes what the workload *actually runs with for the entire boot* while PCR4/7/12 — and therefore the KMS attestation decision — remain identical to the clean reference AMI.
**High-level Test Scenarios (falsifiable):**
- **Claim:** On a running sample-AMI instance, modifying `/etc` or dropping a binary in `/var` does not change the attestation document's PCR4/7/12. → **Oracle:** `nitro-tpm-attest` before and after the overlay write returns identical PCR4/7/12; a KMS key gated on the *reference* values still authorizes `Decrypt` after the write. Confirmed if equal → "trusted state" ≠ "runtime integrity."
- **Claim:** The overlay write survives until reboot (not until the next read), so a long-lived boot runs tampered state indefinitely while continuously attesting clean. → **Oracle:** overlay change persists across an attestation call and across a workload request cycle, cleared only by `reboot`.
- Adjacent: is there any guest-side runtime integrity control (IMA/EVM, a periodic re-measure) the recipe could have included and did not? (Recipe/customize pages name none → doc-gap/omission.)
**Doc evidence:** `create-pcr-compute.html` (`--image UKI.efi` only); `nitrotpm-attestation-document-content.html` (PCR4/7/12 definitions, all boot-time); `attestable-ami.html` (overlay in memory). **Severity-if-true:** High (defeats the practical meaning of "attested trusted state" for the workload's live config/code; measure-at-boot is by design, but the recipe's prose over-promises). **Stop condition:** once equal-PCR-after-overlay-write is shown on one canary, the claim is settled — do not escalate into the KMS verifier internals (HARD STOP).

### Area U-IMDS — IMDS is never hardened or even mentioned (HEADLINE #2) — Lens U / R
**Background.** Grep of the entire Attestable-AMI doc cluster (`al2023-isolated-compute-recipe`, `attestable-ami`, `isolate-data-operators`, `build-sample-ami`, `customize-sample-ami`, `working-with-isolated-amis`, `create-pcr-compute`) returns **zero** matches for IMDS / metadata / 169.254 / credential. The sample `register-image` in `build-sample-ami.html` sets `--tpm-support v2.0 --ena-support` but **omits `--imds-support v2.0`** → the AMI carries no default IMDSv2 enforcement, no hop-limit tightening, no `HttpEndpoint=disabled`; IMDSv1 remains usable unless the account/launch layer separately enforces it (`configuring-instance-metadata-options.html` precedence: launch > account > AMI).
**Security Concern.** The recipe's own threat model (`isolate-data-operators.html`: "preventing even your own operators from accessing the EC2 instance", "ensure only trusted software and code") treats *all in-guest code as the thing to contain*. Yet IMDS — the one in-guest HTTP endpoint that hands any process the **live instance-role credentials** (`iam/security-credentials/<role>`) and the operator-set **user-data** — is left wide and undiscussed. For a confidential-compute box, IMDS is the real "operator/credential ↔ instance" bridge, and the recipe closes SSH/SSM/EIC/serial while leaving this open.
**High-level Test Scenarios:**
- **Claim:** An instance from the sample AMI responds to IMDSv1 (token-less) GETs and returns role credentials to any in-guest process. → **Oracle:** `curl http://169.254.169.254/latest/meta-data/iam/security-credentials/` with no token succeeds; `DescribeInstanceMetadataOptions` shows `HttpTokens=optional`. 
- **Claim:** There is no AMI-level backstop because `--imds-support` was never set. → **Oracle:** `aws ec2 describe-images --image-id <sample> --query 'Images[].ImdsSupport'` is empty.
- Chain: Area W1 overlay write or any SSRF-shaped bug in the workload → IMDS → instance-role creds → blast-radius escape from the "isolated" box (rate at the end of the chain).
**Doc evidence:** absence across the cluster; `build-sample-ami.html` register-image command; `instance-metadata-security-credentials.html`; `instancedata-data-retrieval.html`. **Severity-if-true:** High (credential-exfil surface omitted from a design whose stated purpose is in-guest containment; AWS-authored sample ships IMDSv1-capable). **Owner-to-fix:** shared — AWS owns the insecure sample default (Lens R, reportable Tier-2); customer owns per-launch hardening.

### Area U-COMPLETE — AWS-authored sample under-delivers vs its own parent best-practices — Lens R / U
**Background.** `isolate-data-operators.html` lists **five** best practices for an isolated-compute AMI: (a) remove all interactive access; (b) ensure only trusted software/code; (c) **configure a network firewall within the instance to block access**; (d) read-only/immutable storage; (e) **restrict instance access to authenticated, authorized, and logged API calls.**
**Security Concern.** The AL2023 sample recipe — the reference implementation a customer copies "as a starting point" (`build-sample-ami.html`) — implements only **(a)** (the 7-row removal table) and **(d)** (UKI/erofs/dm-verity/overlay). **(c)** (in-instance firewall) and **(e)** (API-call restriction) appear nowhere in the recipe, `build-sample-ami`, or `customize-sample-ami`; **(b)** has no allowlist/provenance process. A verbatim copy therefore satisfies 2–3 of AWS's own 5 points with **no in-page warning** that (c)/(e) are left to the customer.
**High-level Test Scenarios:**
- **Claim:** An instance built from the sample recipe has no host firewall restricting inbound/outbound. → **Oracle:** no `nftables`/`iptables` ruleset present; outbound to arbitrary hosts (incl. IMDS, incl. internet) is unrestricted.
- **Claim:** Nothing in the recipe restricts which API calls the instance role can make / logs them. → **Oracle:** instance role usable for arbitrary AWS calls from in-guest; no logging config shipped.
- **Claim:** The gap is silent (no "you must still add (c) and (e)" callout). → **Oracle:** text review of the three pages.
**Doc evidence:** `isolate-data-operators.html` 5-point list vs recipe/build/customize content. **Severity-if-true:** Moderate–High (AWS-authored copy-verbatim artifact that under-delivers against its own documented best-practice list; reportable as a hardening/doc defect, **not** a customer footgun because the sample is AWS-shipped).

### Area X-SERIAL — Serial-console removal is in-guest only; Nitro attach survives — Lens X / U
**Background.** The recipe disables serial console "through kernel command line parameter" — i.e. no `console=ttyS0`, hence no boot output and (with no getty / no password OS user) no login. But EC2 Serial Console attach is a **separate control plane**: account-level `ec2:EnableSerialConsoleAccess`/`DisableSerialConsoleAccess` (default disabled) + IAM `ec2-instance-connect:SendSerialConsoleSSHPublicKey` on the instance ARN, over a Nitro virtual UART that `configure-access-to-serial-console.html` says is "independent of the instance VPC … does not use the instance security group or the subnet network ACL." Nothing in the AMI disables the account setting or revokes the IAM action.
**Security Concern.** The single "Serial Console: Disabled" row reads as "the AMI closes this channel." It closes **login**, not **attach**. If an operator re-enables account-level serial access for any other fleet, isolated-compute instances become attachable at the Nitro level with only the kernel param (an in-guest config) as the backstop — exactly the "even your own operators" boundary the chapter is about.
**High-level Test Scenarios:**
- **Claim:** `send-serial-console-ssh-public-key` + SSH to the serial endpoint **attaches** to a sample-AMI instance (even if the port is silent). → **Oracle:** connection establishes (TCP/handshake to `*.oneclickv2-proxy.ec2.aws.dev` succeeds) where the recipe implies the channel is gone.
- **Claim:** The kernel param blocks guest login but not attach. → **Oracle:** attach yields a connected-but-blank port (no getty, no password user) — confirming removal is login-only.
- Doc-gap: can early UEFI/firmware output (pre-cmdline, no GRUB on direct-UKI boot) reach ttyS0 for an attached operator? Not documented either way → mark "doc-gap, confirm on canary."
**Doc evidence:** recipe table serial-console row; `configure-access-to-serial-console.html`; `ec2-serial-console-prerequisites.html`. **Severity-if-true:** Medium (requires a privileged operator position — account enable + IAM — so intra-account/operational; the sharp value is the false sense that the AMI itself closed it).

### Area U-USERDATA — "Eliminates the ability to provide user data" is false; IMDS still delivers it — Lens U
**Background.** Recipe table: removing cloud-init "Eliminates the ability for operators to provide user data to instances and run boot-time scripts." Cloud-init removal stops *execution*; user-data is still **delivered** at launch and retrievable at `http://169.254.169.254/latest/user-data` (`instancedata-data-retrieval.html`: "It is up to the instance to interpret and act on user data").
**Security Concern.** The claim conflates *provide* with *execute*. An operator can still set user-data at `RunInstances`/`ModifyInstanceAttribute`; any in-guest process (the workload, a re-added agent, an SSRF-shaped bug — chains to Area U-IMDS) can read it → a one-way operator→instance channel the "elimination" wording denies.
**High-level Test Scenarios:** **Claim:** user-data set at launch is readable in-guest on a sample-AMI instance despite cloud-init removal. → **Oracle:** `curl .../latest/user-data` returns the operator-set blob. **Severity-if-true:** Low–Moderate (doc-imprecision + residual channel; elevated when chained with the un-hardened IMDS of Area U-IMDS).

### Area R-BUILD — Reference measurements are builder-asserted with no AWS re-measurement (pointer) — Lens R / EE / U
**Background / Security Concern.** The sample is built on a customer EC2 host with customer-controlled tooling; `nitro-tpm-pcr-compute` is run **by the builder** and emits `pcr_measurements.json` with no AWS-side independent re-measurement before `register-image` or before the PCRs are placed into a KMS policy. UKI signing uses **customer-generated** PK/KEK/db (`create-ami-with-uefi-secure-boot.html`); the **standard-boot path (PCR4/PCR12)** that `prepare-attestation-service.html`'s example KMS policy actually uses has **no signature check at all — only measurement.** Supply chain is unpinned (`cargo install coldsnap`, `dnf` sample package, GitHub clone). ⇒ "reproducible measurement = trustworthy" is false: a compromised build self-certifies.
**This is OWNED by** `attestable-ami` (reproducible-measurement zero-owner-entropy, build-host-root code-exec, dm-verity lazy-verify), `build-sample-ami` (unpinned supply chain, measurer-rides-in-image, PCR4/7/12-vs-4/7), and `nitrotpm-attestation` (A1 reproducible-PCR bypass, A2 PCR12=all-zeros, A3 ImageSha384). **Do not re-run those tests here.** Recipe-specific angle only: the sample's overlay-tree (`/root/`) and auto-executed custom scripts (`customize-sample-ami.html`) are additional build-time injection points that ride into the measured image. **Severity-if-true:** Critical **if** the build/KMS-policy pipeline is compromised (defeats the attestation purpose) — but gated on build-pipeline access, hence a pointer. **Stop condition:** on any evidence touching the NitroTPM/KMS verifier itself → HARD STOP.

### Area U-TIME — Chrony removal: scope-limited, time-integrity side effects (DOC-GAP) — Lens U / L
**Background.** Recipe claims removing `amazon-chrony-config` "Disables the chrony command port … Prevents operators from running chrony commands." AWS docs scope the change to the **command port**, not full NTP removal; whether a bare `chronyd` still syncs on AL2023 without the config package is **not stated** (DOC-GAP).
**Security Concern.** If time sync is in fact lost: `set-time.html` documents that clock drift causes AWS to **reject signed (SigV4) requests**; `nitrotpm-attestation-document-validate.html` shows the attestation document carries a `timestamp` and optional `nonce` whose freshness policy is left to the consumer. PCR measurements themselves are not time-dependent, but drift can break TLS cert validation and any consumer-side attestation freshness check.
**High-level Test Scenarios:** **Claim:** a sample-AMI instance still synchronizes time (chronyd runs without the config). → **Oracle:** check clock sync state on a canary. **Severity-if-true:** Low (as scoped — command-port only) / Moderate (if full NTP is actually lost → signed-request + attestation-freshness failures).

### Area X-VERITY — dm-verity verifies lazily, not eagerly at boot (minor) — Lens X / U
**Background.** dm-verity root hash → kernel cmdline → UKI → PCR12 at boot, but blocks are verified **on-access** (`docs.kernel.org/.../verity.html`: "all hashes will be verified on-demand during disk access"), failing I/O (or `panic_on_corruption`) on mismatch.
**Security Concern.** "Booted and attested" ≠ "entire root fs verified now" — it is "verifiable on access, fail-closed if tampered." Not a PCR bypass; relevant only to anyone assuming full-image verification completes at boot. Cross-ref `attestable-ami` plan's dm-verity lazy-verify window. **Severity-if-true:** Low–Medium (fail-closed; availability/assumption nuance, not a read/mutate breach).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Runtime overlay tamper undetected by attestation | ephemeral overlay vs PCR4/7/12 | "returns to original trusted state" (reboot-persistence, NOT runtime integrity) |
| In-guest credential/user-data exfil via IMDS | IMDS 169.254.169.254 | *(none — recipe never mentions IMDS; AMI has no `imds-support`)* |
| Serial-console attach on a "disabled" instance | Nitro virtual UART / `EnableSerialConsoleAccess` | kernel cmdline param (in-guest login only) |
| User-data delivery despite cloud-init removal | IMDS user-data path | "Eliminates the ability … to provide user data" (false — execution only) |
| Sample under-delivers vs 5 best practices | recipe vs `isolate-data-operators` | best-practices list (c) firewall, (e) API restriction — not implemented |
| Self-certifying malicious build | `nitro-tpm-pcr-compute` / register-image | reproducible measurement (builder-asserted, no AWS re-measure) — *pointer* |
| Time drift breaks signed/attestation freshness | chrony removal | "disables the chrony command port" (scope-limited; NTP state doc-gap) |
| Lazy dm-verity verification window | dm-verity on erofs | fail-closed on-access I/O verification |

---

## 7. Out-of-Scope Risk Categories
- **AWS Nitro "zero operator access"** (`isolate-data-operators.html` → whitepaper): AWS-infra guarantee. HARD STOP on contact.
- **NitroTPM / KMS attestation verifier internals** — service plane; HARD STOP (route to AWS-Security).
- **Cross-tenant / cross-account** anything — null on this page (resources are the customer's own AMI/instance; AMI/snapshot sharing is owned by the nitrotpm/verify-nitrotpm/attestable-ami plans).
- **Build-time IAM artifact audit** (`ebs:*` snapshot perms, `RegisterImage *`) — owned by `build-sample-ami` / `attestable-ami` plans.
- **Customer-authored hardening gaps** (a customer who edits the sample and leaves IMDS open on *their* fork) — footgun, out of scope; but the **AWS-shipped sample's** defaults (Areas U-IMDS, U-COMPLETE) are **in scope** (Lens R, AWS-authored artifact).
- **Single-tenant self-DoS**, generic KIWI/upstream-package CVEs, DNS rebinding against link-local IMDS.

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens A/IDOR — N/A.** Checked recipe + parent + hub + build/customize/working-with pages: every resource (the AMI, the instance, the overlay, the PCRs, the KMS key) is the **customer's own**; no shared service account, no resource-by-foreign-id, no tenant id in any field. No cross-tenant primitive exists on this page.
- **Lens B/C/E — N/A on this page.** No PassRole/role-ARN/STS/session field; the only roles are build-time IAM (owned by build-sample-ami) and the instance role reachable via IMDS (covered under Lens U, not B).
- **Lens F — N/A.** No translation/wire-protocol/parser layer; this is an image recipe.
- **Lens G/SSRF — N/A as a service-side-fetch.** The only URLs on the page are documentation hyperlinks (osinside.github.io/kiwi, kernel.org); no field the *service* dereferences. The in-guest IMDS reachability is a Lens-U omission + a chain target, not a server-side-fetch field. (Build-time dnf/git/cargo fetches = supply chain → Area R-BUILD, owned by build-sample-ami.)
- **Lens H/KMS — pointer only.** The attestation-gated KMS key (`kms:RecipientAttestation:PCRn`) is owned by `nitrotpm-attestation` (A1/A2/A3, CRL/alg-pin). Not re-derived here.
- **Lens Q/upload — reframed.** Overlay-tree files and auto-run custom scripts are **build-time injection**, routed to Area R-BUILD / supply chain, not a runtime upload surface.
- **Lens AA/revoke-completeness — pointer.** Stale reference measurements lingering in a KMS key policy after an AMI update (old vulnerable image still attests) is owned by `working-with-isolated-amis` (and its "update your KMS key policy to the new reference measurements" step). Flagged here as a chain enabler.
- **Lens J/M/N/BB/CC/DD/FF — N/A.** No OAuth/3P, no session-id/presigned token, no namespace migration, no multi-parser request path, no upstream-asserted-identity header, no caching layer, no JWT/OIDC on these pages.
- **DOC-GAPs to settle on a canary before investing:** (1) reboot-preserves-identical-PCR is *inferred* from reboot's absence from the stop/start/RVR list in `working-with-isolated-amis.html` — not affirmatively stated; (2) whether `chronyd` still syncs without `amazon-chrony-config` (Area U-TIME); (3) early-UEFI/firmware output on ttyS0 pre-cmdline on direct-UKI boot (Area X-SERIAL); (4) whether any guest-side runtime integrity control exists that the recipe omits (Area W1).
