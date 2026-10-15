# Build the Sample Attestable AMI — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/build-sample-ami.html` (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/build-sample-ami.md`, **byte-identical online==offline 2026-10-15**). Supporting pages: `nitrotpm-attestation-document-content.md` (PCR semantics), the IAM Service Authorization Reference (`list_ec2`/`list_ebs`), and the public repos `github.com/amazonlinux/kiwi-image-descriptions-examples` + `github.com/awslabs/coldsnap`.
Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Scope — this plan is the BUILD / SUPPLY-CHAIN / MEASUREMENT-GENERATION complement of the NitroTPM cluster.** It is the page *before* the RegisterImage runbook: it is where the Attestable AMI is **built from source** and where the **reference PCR measurements are first generated**. It OWNS: (1) the AMI build supply chain (KIWI NG, dnf packages, `coldsnap`/cargo, the two GitHub repos, `edit_boot_install.sh`); (2) the **build-time reference-measurement generation** point and its reproducibility; (3) this page's **IAM prerequisite block** (`ebs:*` snapshot direct-APIs + `ec2:RegisterImage` on `*`); (4) the `coldsnap` **EBS-direct-API** snapshot-creation path; (5) the page's **isolation / immutability guarantees** ("removes all interactive access"; dm-verity/erofs). It CROSS-REFERENCES and does **not** restate:
> - RegisterImage register-time co-parameters (`--tpm-support`/`--boot-mode`/`--uefi-data`/`--imds-support` all IAM-ungatable; foreign-snapshot provenance laundering) → `enable-nitrotpm-support-on-ami-attack-research-plan.md` (Areas 1–5).
> - KMS attestation gate, PCR under-binding (AWS example pins `NitroTPMPCR12` to 96 hex zeros), replay/freshness, CRL-disabled, COSE alg-pin, key-family confusion → `nitrotpm-attestation-attack-research-plan.md` (A1–A8).
> - `DescribeImages` unscopable read oracle / "verify = read a self-asserted flag" / whoAMI / console blind spot → `verify-nitrotpm-support-on-ami-attack-research-plan.md`.
> - `GetInstanceTpmEkPub`, launch prerequisites, BitLocker, instance-type change → the NitroTPM hub + `enable-nitrotpm-prerequisites` + `retrieve-ekpub` plans.
> All are children of the EC2 Security hub (NitroTPM = Area 2).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **The safe first oracle for every IAM-scoping lead is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** — no resource is created and a condition key is either wired to an action or it is not. Escalate to a live scoped call only with synthetic canary data.
- **`--dry-run` is caller-IAM-only** (evaluated before resource resolution) — it is NOT a provenance/ownership oracle. A foreign-resource question needs a real 2-account canary.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the Nitro hypervisor signing path, the NitroTPM device, AWS's attestation CA/KDS), stop, preserve evidence, flag for AWS-Security disclosure. The attestation *signing* chain is AWS-owned and out of scope — only the customer-authored measurement/policy/supply-chain inputs are in scope here.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Attestation-identity break:** produce an AMI/instance that yields PCR4/PCR7/PCR12 measurements **matching a victim's Attestable-AMI reference measurements** without being the victim's trusted build — so it passes a KMS attestation policy keyed on those PCRs (the "untrusted AMI with matching measurements" case AWS itself warns about). The build page is where the reproducible inputs live.
2. **Supply-chain injection:** cause the built Attestable AMI (or the operator's build host) to execute attacker-controlled code via an unpinned/unverified build dependency (dnf package, cargo crate, GitHub repo, `edit_boot_install.sh`), such that the "isolated / immutable" AMI ships a backdoor while still producing attestable measurements.
3. **IAM over-grant abuse:** show that a principal holding **only** this page's AWS-authored prerequisite block (`ebs:StartSnapshot`/`PutSnapshotBlock`/`CompleteSnapshot` on `ec2:*::snapshot/*` + `ec2:RegisterImage` on `*`) can do more than build its own AMI — e.g. register an AMI from a snapshot it does not own, or write snapshot blocks in a way the ec2 control-plane equivalent would gate.
4. **Isolation-guarantee violation:** reach an "isolated" instance built from this description through a path the "removes all interactive access" claim overlooks (SSM, user-data, cloud-init, Nitro-level serial console), or tamper with the "immutable" filesystem.

## 2. Components, Assets, and Design

**What the page actually does.** It is an AWS-authored tutorial that turns a **public source recipe** into an **"Attestable AMI"** — a NitroTPM-measured, dm-verity/erofs-immutable, interactive-access-stripped AL2023 image. Flow:

```
 Operator (root on an AL2023 EC2 build host)
   │  dnf install kiwi-cli, aws-nitro-tpm-tools, veritysetup, erofs-utils, cargo, git     [supply chain #1]
   │  git clone awslabs/coldsnap ; cargo install --locked coldsnap                         [supply chain #2]
   │  dnf install kiwi-image-descriptions-examples  → /usr/share/.../attestable-image-example [supply chain #3]
   ▼
 KIWI NG `system build --description attestable-image-example --target-dir ./image`
   │   builds AL2023 rootfs (erofs read-only + dm-verity hash tree), installs
   │   nitro-tpm-pcr-compute + nitro-tpm-attest into /usr/bin/, removes SSH / EIC / serial
   │   └── runs edit_boot_install.sh (ROOT, build time): loopback-mount ./image/*.raw,
   │        locate UKI (.efi), run nitro-tpm-pcr-compute → ./image/pcr_measurements.json
   ▼  ./image/al2023*.raw   +   ./image/pcr_measurements.json {PCR4, PCR7, PCR12, SHA384}
 coldsnap upload *.raw  ──(EBS direct APIs: StartSnapshot/PutSnapshotBlock/CompleteSnapshot)──►  snap-xxxx
   ▼
 aws ec2 register-image --tpm-support v2.0 --boot-mode uefi --architecture {x86_64|arm64}
        --block-device-mappings ...SnapshotId=snap-xxxx  ──►  ami-xxxx  (Attestable AMI)
   ▼
 (later) instance launched from ami-xxxx → NitroTPM measures boot → Attestation Document (PCR4/7/12)
         → consumer's KMS attestation policy decides whether to vend secrets         [owned by attestation sibling]
```

**Assets:**
- **The reference PCR measurements** (`pcr_measurements.json`: PCR4/PCR7/PCR12, SHA384). These are the *identity* a downstream KMS/attestation policy trusts. **They are a deterministic function of public inputs** (public KIWI image description + public base AL2023 + public `nitro-tpm-pcr-compute`). PCR4 = boot-manager/boot-binary measured chain; PCR7 = hash of the UEFI Secure Boot policy (**builder-chosen** certificate per the UEFI-data path); PCR12 = hash of the kernel command line. (`nitrotpm-attestation-document-content.md`.)
- **The built `.raw` image** → becomes an EBS snapshot → the AMI. Integrity of the AMI == integrity of the whole build supply chain.
- **The NitroTPM tools baked into `/usr/bin/`** (`nitro-tpm-pcr-compute`, `nitro-tpm-attest`) — present on every launched instance.
- **The AWS-authored IAM prerequisite block** — a copy-verbatim artifact (Lens R).

**Identity / trust model:** The AMI is built entirely under the **operator's own account/identity** (no service-linked role, no PassRole on this page). The *attestation* trust is **measurement-based, not identity-based** — the Attestation Document and the PCRs carry **no account/owner field** (established in the attestation + enable siblings). This is the central design fact every lead below leans on: **"this exact code" is provable; "built by this account" is not.**

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Public source recipe (anyone) | A victim's attestation identity | Reproducible PCR4/PCR12 from public KIWI recipe + builder-chosen PCR7 | An attacker-built AMI produces PCR4/7/12 **equal to a victim reference set** and passes a KMS policy keyed on them (no account binding) |
| Build dependency origin (crates.io / dnf repo / GitHub) | The built "immutable/isolated" AMI | `cargo install`, `dnf install`, `git clone`, `edit_boot_install.sh` run as root | Attacker-controlled code lands in the AMI (or on the build host) while measurements still validate |
| Principal holding only the prereq IAM block | Snapshots / AMIs it does not own | `ebs:*` on `ec2:*::snapshot/*`; `ec2:RegisterImage` on `*` | The principal registers an AMI from, or writes blocks into, a snapshot it does not own; or the `*` grant authorizes more than "build my own AMI" |
| EBS direct-data-plane API (`ebs:PutSnapshotBlock`) | Snapshot bytes | coldsnap `upload` | A snapshot is created/populated via `ebs:*` under conditions the `ec2:CreateSnapshot` control-plane path would scope differently (Lens X) |
| Network / management plane | An "isolated, no-interactive-access" instance | SSM / user-data / cloud-init / Nitro serial console | Reaching a shell/command channel on an instance the doc says has "all interactive access removed" |
| **Any customer surface** | **AWS Nitro hypervisor signing / NitroTPM device / attestation CA** | — | **HARD STOP** — AWS service plane, out of scope |

## 4. API / Interface Inventory

| Name | Method | Mut/Non | Int/Ext | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ebs:StartSnapshot` | EBS direct API | Mutating | External | Begin a new snapshot for block upload | Yes (SigV4) | prereq block: `ec2:*::snapshot/*` | Data-plane cousin of `ec2:CreateSnapshot` — **Lens X**; check KMS/tag/ownership keys |
| `ebs:PutSnapshotBlock` | EBS direct API | Mutating | External | Write a 512 KiB block + checksum into a pending snapshot | Yes | prereq block | Writes raw image bytes; integrity rides a caller-supplied checksum |
| `ebs:CompleteSnapshot` | EBS direct API | Mutating | External | Seal the snapshot | Yes | prereq block | — |
| `ec2:RegisterImage` | SDK | Mutating | External | Register AMI from snapshot w/ `--tpm-support v2.0`, `--boot-mode uefi` | Yes | prereq block grants on **`*`** | Register-time co-params owned by `enable-nitrotpm` sibling; **the `*` scope is this page's own Lens-R/S lead** |
| `coldsnap upload` | CLI (3P awslabs tool) | — | — | Wraps the three `ebs:*` calls | — | — | `cargo install --locked` from a cloned git repo — supply chain |
| `nitro-tpm-pcr-compute` | local binary (`aws-nitro-tpm-tools`) | — | — | Generates `pcr_measurements.json` at build time | — | — | Self-asserted reference measurements; baked into AMI |
| `kiwi-ng system build` | CLI | — | — | Builds the image from the description | — | — | Runs `edit_boot_install.sh` as root |

No non-SDK/console-hidden control-plane knob is introduced on this page (the hidden-knob surface for RegisterImage lives in the `enable-nitrotpm` sibling). The *under-tested* surface here is the **3P/local tooling** (coldsnap, kiwi-ng, nitro-tpm-pcr-compute) and the **direct EBS APIs**, which hunters skip because they aren't the obvious `ec2:*` control plane.

## 5. Recommended Areas of Focus

### Area 1 — Reference measurements are a function of public, UNPINNED inputs, with no owner binding, generated by the image's own tool (Lens U / W / EE)  — PRIMARY
*(Repo-confirmed by supply-chain subagent against `amazonlinux/kiwi-image-descriptions-examples/al2023/attestable-image-example/{appliance.kiwi,edit_boot_install.sh,README.md}`.)*

**Background.** The value of an Attestable AMI is that PCR4/PCR7/PCR12 "describe exactly what code an instance will execute." A consumer builds a KMS/attestation policy that vends secrets only to instances presenting those PCRs. **This page makes the entire input set public and unpinned:** a public KIWI description, a public base (AL2023), and a public measurement tool (`nitro-tpm-pcr-compute`). PCR4 (boot-manager code) / PCR12 (kernel command line) derive from the measured UKI; PCR7 (Secure Boot policy) is **builder-chosen** (UEFI-data cert path, `enable-nitrotpm` Area 2). The Attestation Document carries **no account/owner field** (attestation sibling).

**Security Concern — three repo-confirmed facts, pulling in different directions.**
1. **Unpinned recipe ⇒ NOT bit-reproducible, which cuts the naive bypass but exposes a verifier footgun.** `appliance.kiwi` sources packages from `https://cdn.amazonlinux.com/al2023/core/mirrors/**latest**/$basearch/mirror.list` with `<namedCollection name="core"/>` + `<namedCollection name="ami-minimal"/>` — **no NEVRA snapshot / no lockfile.** The measured UKI components (kernel, dracut, systemd-boot) float with the mirror, so **two honest builds on different dates legitimately produce different PCR4/PCR7**. Consequence: an attacker cannot trivially reproduce a *specific victim's historical* PCR set from the public recipe alone (**this partially REFUTES the simplest form of attestation-A1**) — BUT it also means a verifier who pins a policy to a PCR value is pinning to a value that AWS's own recipe will *drift away from on the next rebuild*, so either the policy breaks on legitimate rebuilds or the operator loosens it. The real defect is the **absence of any owner/account binding** (fact 2), not reproducibility per se.
2. **No cryptographic owner binding at generation.** `nitro-tpm-pcr-compute` writes `pcr_measurements.json` as **plain unsigned JSON** to the builder's local disk; nothing ties it to an account or AMI id. The "trust" that a PCR set == "AWS's intended workload" lives entirely in the verifier's out-of-band choice to trust an (AMI-id, PCR) pair — exactly the binding the attestation sibling's A1 is about. The build page is where that unbound value is born.
3. **The reference generator is the image's OWN just-built copy, measuring its own UKI.** `edit_boot_install.sh` runs `sudo "$root_mount/usr/bin/nitro-tpm-pcr-compute" --image <UKI> | tee pcr_measurements.json` — i.e. the tool that produces the "reference" is the dnf-installed copy **inside the artifact it is measuring**, with no external/host-vetted cross-check. Measurer and measured come from the same pipeline (chains to Area 4).

**Also found (doc defects):** (a) **PCR count disagreement** — the AWS page's sample JSON lists PCR4/PCR7/**PCR12**, but the upstream repo README/prose says the tool computes only **PCR4 and PCR7** (no PCR12). Which PCRs the public tool actually emits is unresolved — a sharp doc-gap feeding the attestation sibling's PCR-binding leads. (b) No AWS page formally defines PCR4/7/12 TCG semantics (the subagent's PCR4=boot-mgr / PCR7=SB-policy / PCR12=cmdline mapping is systemd-stub convention, *not* AWS-stated — treat as hypothesis to confirm against the NitroTPM device behavior).

**High-level Test Scenarios.**
- **Claim:** Backdoor placed in a region NOT folded into the measured UKI (rootfs content, or the ephemeral overlay — see Area 5) yields PCR4/7/12 **identical** to a clean build → attested-but-trojaned AMI. → *Oracle:* determine exactly what bytes `nitro-tpm-pcr-compute --image <UKI.efi>` hashes (UKI only, per the script's `--image` arg) vs the full erofs root; a payload outside the UKI defeats "describes exactly what code runs." → *Severity:* High–Critical. **This is the strongest surviving form of the bypass given fact 1.**
- **Claim:** A verifier pins a KMS policy to PCR4/12 and it is satisfied by *any* AL2023 attestable build of the same vintage (not just the trusted builder's), because PCR7 is unpinned/builder-chosen. → *Oracle:* cross-ref attestation A1/A2 (AWS example pins `NitroTPMPCR12` to 96 hex zeros). **Build-side owned here; KMS-policy side → attestation plan.**
- *Cost:* build-time only. *Stop condition:* UKI-vs-rootfs measurement scope resolved and the PCR12 doc-disagreement documented; do not attack a live victim KMS policy (route to attestation plan + authorization).

### Area 2 — AWS-authored IAM prerequisite block: `ec2:RegisterImage` on `*` abandons available scoping (Lens R / S)  — HIGH, Tier-2 reportable
*(Authoritative: IAM-audit subagent read `list_ec2.md` RegisterImage row 30040–30072 + `list_ebs.md` full catalog.)*

**Background.** The page prints a **copy-verbatim** permission block the customer attaches as-is: `ebs:CompleteSnapshot`/`StartSnapshot`/`PutSnapshotBlock` on `arn:aws:ec2:*::snapshot/*`, and `ec2:RegisterImage` on **`*`**. A weak default here is AWS's defect, not a customer footgun → disclosure **Tier 2**.

**Security Concern — corrected against the authoritative reference.**
1. **`ec2:RegisterImage` on `*` discards real, available scoping.** The RegisterImage action has **two** resource rows: `image*` (required) with keys `aws:RequestTag`/`aws:TagKeys`/`ec2:ImageID`/**`ec2:Owner`**/`ec2:Region`, and `snapshot` (optional, the source) with ten keys incl. **`ec2:Owner`**, `ec2:SnapshotID`, `ec2:ParentVolume`, `ec2:SnapshotTime`, `ec2:VolumeSize`. So AWS *could* have published a sample scoped e.g. `Condition:{StringEquals:{ec2:Owner:<account-id>}}` on the snapshot resource to pin "only self-owned snapshots may be registered." The blanket `Resource:"*"` abandons **every** one of these levers. This is a **completeness defect, not an inaccuracy** — the ARN shapes the sample uses are canonical.
2. **CORRECTION to my earlier draft — the `::` empty-account field is NOT an over-grant.** `arn:aws:ec2:${Region}::snapshot/${SnapshotId}` (and `.../image/${ImageId}`) is the **canonical AWS-defined ARN shape**; EC2/EBS snapshot & image ARNs *never* carry an account segment regardless of author. The genuinely unused lever in the `ebs:*` grant is the **region wildcard** (`ec2:*` → could be `arn:aws:ec2:us-east-1::snapshot/*`), which the sample leaves open. Do not report `::` as a finding.
3. **`ec2:SnapshotID` exists** (snapshot row) — but note **`ebs:SnapshotId` does NOT exist** as a condition key in the EBS catalog (corrects an earlier key-name assumption; see Area 3).

**High-level Test Scenarios.**
- **Claim:** A principal holding only the prereq block can `register-image` from a **foreign/shared** snapshot id and set `--tpm-support v2.0` → provenance-laundering into an "attestable" AMI. → *Oracle:* `SimulateCustomPolicy` proves the IAM allow (the `*` grant trivially permits it); a 2-account canary (share a snapshot, register from the other account) proves whether the *service* enforces snapshot ownership beyond IAM. **`--dry-run` is caller-IAM-only, NOT a provenance oracle.** → *Severity:* Med–High. Cross-ref `enable-nitrotpm` Area 4 (which owns the foreign-snapshot-provenance depth; `ec2:Owner` on the snapshot row is the one positive control).
- **Claim:** AWS could have scoped the sample but used `*`. → *Oracle:* diff sample vs the enumerated `list_ec2`/`list_ebs` key columns above. → *Severity:* Low–Med (AWS-authored over-grant, Tier-2).
- *Stop condition:* IAM allow + unused scoping shown via Simulate; live foreign-snapshot register is the escalation (canary + authorization).

### Area 3 — The `coldsnap` / EBS-direct-API path is architecturally less constrainable than its control-plane cousin (Lens X / H)
*(Authoritative: IAM-audit subagent, `list_ebs.md` full catalog vs `list_ec2.md` CreateSnapshot 15906–15946.)*

**Background.** `coldsnap upload` creates the snapshot via the **EBS direct APIs** (`StartSnapshot`→`PutSnapshotBlock`→`CompleteSnapshot`), **not** `ec2:CreateSnapshot`. Both land the same resource type via different services with different authorization schemas.

**Security Concern — repo/reference-confirmed asymmetry (not just "might differ").**
1. **The entire `ebs` service defines exactly ONE resource type — `snapshot` — and SIX condition keys total:** `aws:RequestTag`, `aws:ResourceTag`, `aws:TagKeys`, `ebs:Description`, `ebs:ParentSnapshot`, `ebs:VolumeSize`. By contrast `ec2:CreateSnapshot` requires **two** resource types — `snapshot*` **and `volume*`** — and the volume row carries `ec2:VolumeID`, `ec2:ParentVolume`, and crucially **`ec2:Encrypted`**. So the control plane lets an admin gate snapshot creation by **source-volume identity and encryption posture**; the direct-API trio has **no volume-binding key at all**, and its `ebs:Description`/`ebs:VolumeSize` are *caller-supplied request params*, not derived facts. The bytes-first data-plane API is **architecturally less constrainable than its control-plane cousin, independent of how the policy is written** — a clean Lens-X finding, Tier-2 (AWS-schema-owned).
2. **No KMS key-pinning on the direct API (Lens H).** The EBS catalog contains **zero** KMS-related condition keys — no `kms:KeyId`, no via-service binding. Per this reference there is **no IAM mechanism to restrict which KMS key a caller uses for an encrypted direct-API snapshot** (caveat: KMS key-policy-side grants may constrain out-of-band — outside this page's surface).
3. **Measurement/upload decoupling.** `pcr_measurements.json` is computed on the **local `.raw`**; the snapshot is uploaded by a *separate* coldsnap step. Nothing binds the uploaded snapshot bytes to the measured `.raw`.

**High-level Test Scenarios.**
- **Claim:** The `ebs:*` trio cannot be scoped by source-volume or encryption, so the prereq grant is strictly broader than any achievable `ec2:CreateSnapshot` policy. → *Oracle:* the enumerated key delta above (already established at reference level). → *Severity:* Med, Tier-2.
- **Claim:** The distributed `pcr_measurements.json` need not match the shipped AMI (self-asserted reference). → *Oracle:* reason through the launch path — the NitroTPM re-derives PCRs **at launch** from the actual boot, so a mismatched upload yields *different* PCRs (fails attestation) rather than a silent bypass; this likely **closes the "swap bytes after measuring" variant to NULL**. The residual real issue is that the operator *distributes* a reference that is cryptographically unbound to the AMI (ties to Area 1 fact 2). → *Severity:* Low–Med.
- *Stop condition:* key delta + measure-vs-launch binding resolved at doc level.

### Area 4 — Build supply chain: the `git clone` is inert, host-side installs are unverified, and the measurer rides in the measured image (Lens R / EE / Q)  — HIGH
*(Repo-confirmed by supply-chain subagent — `appliance.kiwi`, `add-gpg-key.sh`, `edit_boot_install.sh`, crates.io sparse index for `coldsnap`.)*

**Background.** The build installs, as root: host `dnf` packages (`kiwi-cli`, `python3-kiwi`, `aws-nitro-tpm-tools`, `kiwi-image-descriptions-examples`, `cargo`, `git`), a cargo crate, and the KIWI recipe; then `kiwi-ng system build` runs `edit_boot_install.sh` as root. The built AMI is marketed as isolated/immutable and its measurements are downstream-trusted.

**Security Concern — repo-confirmed, with two of my earlier hypotheses CORRECTED.**
1. **`cargo install --locked coldsnap` IGNORES the `git clone` — HEADLINE.** The doc says `git clone awslabs/coldsnap && cd coldsnap && cargo install --locked coldsnap`. `cargo install <name>` (no `--path .`) **always resolves from crates.io, not the working directory** — confirmed `coldsnap` is published on crates.io (sparse index: real metadata, recent `pubtime`). So **the clone is functionally inert**: the installed binary is whatever is *latest on crates.io at install time*, with **no version pin** (`--locked` only locks that version's transitive deps, not `coldsnap` itself). The doc gives the *appearance* of installing a reviewed/cloned artifact while trusting the newest public-registry publish → Lens-EE registry/namespace-takeover + unpinned-version exposure feeding an attested AMI's upload tool. **High.**
2. **CORRECTION — in-IMAGE RPMs ARE GPG-checked.** `appliance.kiwi` sets `<rpm-check-signatures>true</rpm-check-signatures>` + repo `package_gpgcheck="true"`, and `add-gpg-key.sh` pins the AL2023 GPG key. So packages baked *into the image* (incl. `aws-nitro-tpm-tools`, `veritysetup`, `systemd-boot`) **are** signature-verified — my earlier "no signature verification" hypothesis is **REFUTED for the in-image path.**
3. **…but the HOST-side `dnf install aws-nitro-tpm-tools` / `kiwi-image-descriptions-examples` (run directly on the build EC2, not inside the KIWI build) has no shown gpgcheck posture** — relies on the host's `/etc/yum.repos.d` config, which neither doc displays (doc-gap). This matters because of fact 4.
4. **The reference-measurement generator rides inside the artifact it measures.** `edit_boot_install.sh` runs `sudo "$root_mount/usr/bin/nitro-tpm-pcr-compute"` — the **guest image's own freshly-installed copy**, as root, on the build host, with no external cross-check. A compromised `aws-nitro-tpm-tools` (host repo or mirror) therefore gets **root on the build host** *and* can emit **attacker-chosen `pcr_measurements.json`** — forging the "reference" the whole attestation trust rests on. Single biggest trust-chain observation (chains to Area 1 fact 3).
5. **Un-auditable package sets:** `<namedCollection name="core"/>` + `ami-minimal` pull package sets not enumerated in the repo (live in AL2023 metadata) — a reviewer cannot fully audit the installed list from the repo alone. No SBOM / SLSA provenance / reproducible-build attestation anywhere (doc-gap).
6. **`edit_boot_install.sh` doc-vs-reality discrepancy:** the AWS page says the script "mounts the raw disk image to a loopback device"; the actual script does **no mount** — it only `findmnt`s the mount KIWI already created. Minor, but shows the AWS summary doesn't match the public artifact (confidence signal for Area 1's reproducibility leads).

**High-level Test Scenarios.**
- **Claim (headline):** The upload tool actually installed is an unpinned crates.io latest, not the cloned commit → registry compromise / malicious transitive dep lands in the build-host toolchain. → *Oracle:* already confirmed at doc/registry level; the live angle is auditing `coldsnap`'s current crates.io dep tree. → *Severity:* High.
- **Claim:** A compromised host-side `aws-nitro-tpm-tools` yields build-host root + forged `pcr_measurements.json`. → *Oracle:* confirm host `gpgcheck` default for the serving repo; trace the root invocation in `edit_boot_install.sh`. → *Severity:* High.
- *Preconditions:* influence over crates.io `coldsnap`, the host dnf repo/mirror, or the build host. *Stop condition:* each component's resolution + verification posture documented. **Do not publish a typosquat or tamper with any repo/registry.**

### Area 5 — Isolation / immutability guarantees: stronger than stated on the admin channels, weaker on the ones the page never mentions (Lens U)
*(Repo-confirmed by supply-chain subagent — `appliance.kiwi` `<ignore>` list + kernel cmdline + `fstab.script`/`chrony.d`.)*

**Background.** The page asserts the image "removes all interactive access (SSH, EC2 instance connect, serial console) to create an isolated compute environment" and uses "dm-verity and erofs configurations for filesystem immutability."

**Security Concern — repo config shifts the picture both ways (my SSM/cloud-init hypothesis is REFUTED).**
1. **Admin channels: actually stripped MORE than the page states (positive, but a doc-gap).** `appliance.kiwi` `<ignore>`s not only `openssh-server` + `ec2-instance-connect` but also **`amazon-ssm-agent`, `cloud-init`, `cloud-init-cfg-ec2`, `update-motd`.** So SSM Session Manager **and all user-data/cloud-init execution are gone** — my earlier "SSM/user-data may be a residual channel" lead is **REFUTED**. The AWS page understates its own hardening (never mentions SSM/cloud-init removal) → doc-gap, not a bug.
2. **Serial console — login removed, but a boot-log info-disclosure residual the claim doesn't address.** Kernel cmdline: `console=ttyS0 rd.shell=0 systemd.getty_auto=false rd.kiwi.verity_options=panic-on-corruption`. `rd.shell=0` + `systemd.getty_auto=false` → no login/rescue shell on any console (claim holds for *shell* access even if a customer enables the account-level EC2 Serial Console). BUT `console=ttyS0` remains → **kernel/dmesg boot output is still routed to the serial device** — a residual information-disclosure channel the "removes all interactive access … serial console" phrasing silently covers up. → *Severity:* Low (info-disclosure).
3. **dm-verity is detect-and-PANIC, not write-prevention.** `verity_blocks="all"` + `panic-on-corruption` → tampered blocks are *detected* and crash the guest kernel; it does **not** prevent a privileged actor with block-device access from writing. "Immutability" = (a) erofs root is read-only + integrity-checked, and (b) `overlayroot_write_partition="false"` → the runtime write overlay is **non-persistent** (vanishes on reboot, never touches the verity base). So **runtime writes ARE possible, just ephemeral** — the page spells out neither the detect-vs-prevent distinction nor the ephemeral-overlay reality (doc-gap). Chains to Area 1 (a payload in the ephemeral overlay or any un-measured region is attested-clean until reboot).
4. **Uncovered paths the page never scopes:** no host firewall (**`firewalld` is `<ignore>`d** → guest has zero local packet filtering; network isolation is 100% on SG/NACL — an undiscussed tradeoff); **IMDS exposure unaddressed** (ties to `enable-nitrotpm` Area 3 — the register command omits `--imds-support v2.0` → launched instances default IMDSv1-capable; SSRF→cred-theft precondition on an "attestation-grade" image); no statement that the guarantees cover only *administrative* channels, not the workload itself. Minor extra hardening present but unmentioned: `/boot/efi` `ro,nosuid,nodev,noexec`; chrony `cmdport 0`.

**High-level Test Scenarios.**
- **Claim:** The dm-verity/erofs guarantee covers only the measured erofs base; the ephemeral overlay + any un-measured region are runtime-writable and (per Area 1) possibly un-attested. → *Oracle:* map partition/verity scope vs what the UKI measures. → *Severity:* Low–Med, chains to Area 1 Critical variant.
- **Claim:** `console=ttyS0` leaks boot/dmesg to a serial channel the "no interactive access" claim implies is closed. → *Oracle:* cmdline already confirmed; verify what a customer-enabled EC2 Serial Console actually surfaces. → *Severity:* Low.
- **Claim:** No `--imds-support v2.0` → IMDSv1-capable attestation-grade instance. → *Oracle:* owned by `enable-nitrotpm` Area 3; cross-ref only. 
- *Stop condition:* each sub-claim traced to the repo config or marked doc-gap (most already are).

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Attacker reproduces identical PCR4/PCR12 from public recipe + chosen PCR7 → passes a victim attestation policy | Reference measurements / NitroTPM | "PCRs describe exactly what code runs" (measurement-as-identity) — no account binding |
| Register a `--tpm-support v2.0` AMI from a foreign/shared snapshot | `ec2:RegisterImage` + prereq block | `ec2:RegisterImage` on `*` (sample abandons `ec2:Owner`/tag scoping) |
| `ebs:*` data-plane path reaches/creates snapshots differently than `ec2:CreateSnapshot` | EBS direct APIs / coldsnap | `ec2:*::snapshot/*` wildcard; condition-key delta vs control plane |
| Backdoored dependency (cargo crate / dnf pkg / repo / `edit_boot_install.sh`) baked into attested AMI | Build supply chain | None stated on page (no pinning/signature verification shown) |
| Compromised `nitro-tpm-pcr-compute` emits attacker-chosen `pcr_measurements.json` | aws-nitro-tpm-tools | Self-asserted build artifact; dnf gpgcheck posture (unstated) |
| Reach "isolated" instance via SSM / user-data / Nitro serial console | AL2023 image description | "removes all interactive access (SSH, EIC, serial console)" |
| Tamper writable/unmeasured region of an "immutable" AMI | dm-verity / erofs | "filesystem immutability" (root only?) |

## 7. Out-of-Scope Risk Categories
- **The AWS attestation signing chain** — the Nitro hypervisor signature over the Attestation Document, the NitroTPM device, AWS's attestation CA/KDS/CRL endpoints. **HARD STOP** if evidence reaches any of these.
- The **KMS attestation-policy mechanics** (PCR under-binding, replay/freshness, CRL-disabled, COSE alg-pin, key-family confusion) — owned by `nitrotpm-attestation-attack-research-plan.md`; chain into it, don't re-derive.
- RegisterImage **register-time co-parameters** (`--tpm-support`/`--boot-mode`/`--uefi-data`/`--imds-support` IAM-ungatability) — owned by `enable-nitrotpm-support-on-ami-attack-research-plan.md`.
- The **read/verify path** (`DescribeImages` unscopable oracle, "verify = self-asserted flag") — owned by `verify-nitrotpm-support-on-ami-attack-research-plan.md`.
- **IMDS on a self-built host**, single-tenant self-DoS, and least-privilege footguns a customer inflicts on a policy **they** authored (the prereq block is AWS-authored → in scope; a customer's own tightening is not).
- Bugs in the **third-party reference repos themselves** (KIWI NG upstream, coldsnap as a project) except where AWS's published tutorial tells the customer to run them unpinned (that composition is in scope as Lens R).

## 8. Null hypotheses / doc gaps
- **Lens G (SSRF):** NULL — checked target page + build flow. No field the service dereferences server-side: `ImageLocation` is not used here; `coldsnap upload` reads a local `.raw`; GitHub/crates URLs are client-side `git clone`/`cargo` fetches by the operator, not a service-side fetch. (The `--uefi-data` fetch question is the `enable-nitrotpm` sibling's, routed to Lens W there.)
- **Lens B/C (PassRole / vending):** NULL — no role ARN is passed anywhere on this page; the build runs under the operator's own identity, no SLR.
- **Lens A (cross-tenant IDOR on output):** NULL for the primary flow — `register-image` creates a **caller-owned** `ami-`; the foreign-input variant (register from a snapshot you don't own) is captured as Area 2/`enable-nitrotpm` Area 4, not a read-by-foreign-id.
- **Lens F (translation/wire injection):** NULL — no customer-input→downstream-language translator on this page.
- **Lens H (KMS):** partial — encrypted-snapshot key selection on `ebs:StartSnapshot` is folded into Area 3; the AMI copy/re-encryption path is owned by `data-protection` R2.
**RESOLVED by subagents (2026-10-15):**
- (3) `edit_boot_install.sh` contents/privs — RESOLVED (Area 4 fact 4 + the no-mount discrepancy).
- (4b) `cargo install --locked coldsnap` — RESOLVED: ignores the clone, installs unpinned crates.io latest (Area 4 fact 1).
- (4a) In-image dnf gpgcheck — RESOLVED: in-image RPMs ARE signature-checked; only the **host-side** install posture is still unshown (Area 4 facts 2–3).
- (5) SSM / user-data / cloud-init — RESOLVED: all `<ignore>`d → REFUTED as residual channels; residuals are instead `console=ttyS0` dmesg + no `firewalld` + IMDS (Area 5).
- (6) `ebs:*` vs `ec2:CreateSnapshot` delta — RESOLVED: `ebs` has only a `snapshot` resource + 6 keys, no `volume`/`ec2:Encrypted`/KMS equivalent (Area 3). The `::` ARN is canonical, NOT an over-grant (Area 2 correction).

**STILL OPEN (highest value, settle first):** (1) exact bytes feeding **PCR4/PCR12** (UKI only, per `--image <UKI.efi>`, vs full rootfs) — decides the unmeasured-region backdoor (Area 1 primary). (2) **PCR12 existence disagreement** — AWS page sample lists PCR4/7/12; upstream repo README says the tool emits only PCR4/7 (Area 1). (2b) Formal AWS definition of PCR4/7/12 TCG semantics — none found (Area 1). (7) Host-side `dnf` gpgcheck default for the repo serving `aws-nitro-tpm-tools` (Area 4 fact 3). (8) Live foreign-snapshot `register-image` provenance enforcement beyond IAM (Area 2; needs 2-account canary, deferred-depth to `enable-nitrotpm` Area 4).

---
*Companion to the NitroTPM cluster: `nitrotpm-attestation`, `enable-nitrotpm-support-on-ami`, `enable-nitrotpm-prerequisites`, `verify-nitrotpm-support-on-ami`, `verify-nitrotpm-support-on-instance`, `retrieve-ekpub`, `nitrotpm-instance`, and the `nitrotpm` hub (EC2 Security Area 2). This plan owns the build / supply-chain / measurement-generation surface.*
