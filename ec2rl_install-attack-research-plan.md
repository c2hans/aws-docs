# EC2Rescue for Linux — *Install page* — Attack Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2rl_install.html (offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2rl_install.md`).
**Source of leads:** the target page + sibling pages `Linux-Server-EC2Rescue.html` (overview), `ec2rl_working.html` (run/upload), `ec2rl_moduledev.html` (module dev); the AWS-authored SSM Automation runbook `AWSSupport-TroubleshootSSH` (referenced by the install page) and the `AWSSupport-*EC2Rescue*` runbook family; the public distribution bucket `s3://ec2rescuelinux`; and the open-source repo `awslabs/aws-ec2rescue-linux`.
**Status:** documentation-derived hypotheses only. **Nothing has been tested** against a live account, instance, the distribution bucket, or any runbook. Every lead requires live PoC confirmation on a disposable, in-scope target.

> **Scope note / relationship to the broader plan.** A broad whole-subsystem plan already exists at `Linux-Server-EC2Rescue-attack-research-plan.md` (covers module RCE, upload exfil, `--backup` over-privilege). **This document is scoped to the *install page* surface specifically:** (1) the **software supply chain** that delivers `ec2rl.tgz`, (2) the **optional GPG/sha256 verification gate** the page documents, and (3) the **`AWSSupport-TroubleshootSSH` install path** — the only part of the install page that crosses an AWS/account trust boundary. Module-execution and upload/backup leads are cross-referenced but owned by the broader plan.

---

## 0. How to use this document
- Each lead reads: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work Section 5 in priority order; look left and right for adjacent bugs.
- **HARD STOP / disclosure:** The distribution bucket `s3://ec2rescuelinux` and the `AWSSupport-*` runbooks are **AWS-owned service-plane artifacts.** The moment evidence shows the bucket is claimable/writable by a non-AWS principal, or a runbook's AWS-managed role grants more than its purpose needs, **stop, preserve evidence, and route to AWS Security — do not exploit.** Likewise if any credential/ARN/account belonging to AWS's own fleet appears.
- What this target **IS**: a client-side, open-source diagnostic tool the customer downloads from a **public S3 bucket** and runs **inside their own EC2 Linux instance, frequently as root**. It is **not** a multi-tenant managed service — classic cross-tenant IDOR / credential-vending / control-ENI lenses do **not** fire on the *install* flow. The install-page value is: **supply-chain integrity**, **signature-gate integrity**, and the **AWS-authored SSM runbook** that installs+drives it remotely.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Supply-chain RCE:** Obtain code execution on an instance that follows the documented `curl …/ec2rl.tgz` install, by controlling, tampering with, or taking over the `ec2rescuelinux` distribution or its transport — *without* the user's **optional** GPG step catching it.
2. **Signature-gate defeat:** Produce a substituted artifact + key + signature set that the documented verification flow accepts as a **"Good signature"**, or that the user is trained to accept despite the warnings the doc itself prints.
3. **Cross-instance / over-privileged install via SSM:** Through `AWSSupport-TroubleshootSSH` (and the `*EC2Rescue*` workflow family), install/run against an instance the caller should not touch, read another volume's data via a helper-instance attach, or abuse the runbook's `AutomationAssumeRole` / `PassRole` / output-bucket parameters to cross an account or instance boundary.
4. **Tarball-unpack abuse:** Use a malicious `ec2rl.tgz` (only reachable after objective 1/2) to write outside the unpack directory via path-traversal/absolute/symlink entries during `tar -xzvf`.

---

## 2. Components, Assets, and Design

**Mechanism (not marketing):**
- **Distribution origin** — `https://s3.amazonaws.com/ec2rescuelinux/` (path-style, **global-namespace** S3 bucket `ec2rescuelinux`). Four objects: `ec2rl.tgz` (the tool), `ec2rl.tgz.sha256` (integrity hash), `ec2rl.key` (publisher GPG public key), `ec2rl.tgz.sig` (detached GPG signature). **All four are served from the same origin/bucket.**
- **Alternate origin** — the **bundled build** and full source are on GitHub `awslabs/aws-ec2rescue-linux` (third-party-hosted open source).
- **Install actor** — a shell on a "working Linux instance", running `curl` **anonymously** (no AWS identity). Unpack via `tar -xzvf`; the tool then typically runs **as root** (`sudo`, `EC2RL_SUDO`).
- **Verification gate (OPTIONAL)** — `sha256sum -c ec2rl.tgz.sha256` (integrity only, same-origin hash) and the GPG flow: `gpg2 --import ec2rl.key` → `gpg2 --verify ./ec2rl.tgz.sig`. The publisher identity is `ec2autodiag@amazon.com <EC2 Rescue for Linux>`; primary-key fingerprint `E528 BCC9 0DBF 5AFA 0F6C C36A F780 4843 2FAE 2A1C`; sig dated 2018-07-12.
- **Remote install driver (AWS-authored)** — SSM Automation runbook **`AWSSupport-TroubleshootSSH`**: "installs EC2Rescue for Linux and then uses the tool to check or attempt to fix common issues that prevent a remote connection to a Linux machine through SSH." Related family: `AWSSupport-StartEC2RescueWorkflow`, `AWSSupport-ExecuteEC2Rescue` (detach impaired root volume → attach to a **helper instance**).

**Identity / privilege model:** no tenants, no login on the install path. Trust is OS-level (root vs non-root) and, for the SSM path, the automation's IAM role. Supply-chain "trust" rests entirely on an **optional** signature whose key is fetched from the **same bucket** as the artifact it signs.

**ASCII pipeline (install surface):**
```
   (1) SUPPLY CHAIN                              (verify = OPTIONAL, same-origin key)
   s3://ec2rescuelinux/{ec2rl.tgz,.sha256,.sig,.key} --curl(anon,https)--> instance disk
   GitHub awslabs/aws-ec2rescue-linux (bundled build) --------------------> instance disk
                 |                                   |
                 | tar -xzvf ec2rl.tgz               | gpg2 --verify (optional; warns "not certified")
                 v                                   v
   (2) ./ec2rl ...  (runs as root) ---> [module exec / upload / backup : see broader plan]

   (3) REMOTE INSTALL PATH (AWS-authored automation)
   caller --SSM StartAutomationExecution--> AWSSupport-TroubleshootSSH
             (AutomationAssumeRole?, InstanceId param) --RunCommand--> target instance
                                                        \--installs ec2rl from s3://ec2rescuelinux
```

**Mandatory coverage sweep — pages checked for lens triggers:**
- Target `ec2rl_install.md`; siblings `Linux-Server-EC2Rescue.md`, `ec2rl_working.md`, `ec2rl_moduledev.md`; online runbook pages (see §5C).
- URL/dereferenced-field fields on the install page: the four `s3.amazonaws.com/ec2rescuelinux/*` download URLs, the `www.gnupg.org` and GitHub links, the runbook hyperlink. (→ Lens Y/EE, and Lens G only insofar as the SSM path fetches server-side.)
- Upload-blob / pointer fields: none on the *install* page itself (`--support-url`/`--presigned-url` live on `ec2rl_working` → owned by broader plan; noted in §7).
- Gates before privileged state change: the **optional** sha256 + GPG verification before running a root tool. (→ Lens U/P — the central install-page lead.)
- IAM policy JSON / managed policies / runbook permission blocks: none on the install page; the `AWSSupport-TroubleshootSSH` runbook doc is the artifact to resolve (→ Lens R/S, §5C).
- Secrets generated/persisted: none on install.
- Security guarantees asserted: the whole "(Optional) Verify the signature" section asserts authenticity/integrity protection — trace to the mechanism (→ Lens U, §5B).

---

## 3. API / Interface Inventory (install surface)

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `GET s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz` | HTTPS GET | Existing | Non-mut (read) | External | Download tool tarball | Yes (public, anon) | Anyone | Path-style, global-namespace bucket. Primary supply-chain object. |
| `GET …/ec2rl.tgz.sha256` | HTTPS GET | Existing | Non-mut | External | Integrity hash | Yes (anon) | Anyone | Same origin → integrity, not authenticity. |
| `GET …/ec2rl.key` | HTTPS GET | Existing | Non-mut | External | Publisher GPG pubkey | Yes (anon) | Anyone | Trust root fetched from the thing it protects. TOFU. |
| `GET …/ec2rl.tgz.sig` | HTTPS GET | Existing | Non-mut | External | Detached signature | Yes (anon) | Anyone | Same origin as artifact + key. |
| GitHub `awslabs/aws-ec2rescue-linux` (bundled build) | HTTPS GET | Existing | Non-mut | External | Bundled build + source | Yes | Anyone | 3P-hosted; out-of-scope code, in-scope as a trust source. |
| SSM `StartAutomationExecution(DocumentName=AWSSupport-TroubleshootSSH, …)` | SigV4 API | Existing | **Mutating** | External | Install + run ec2rl on a target instance | Yes (IAM) | Caller + `AutomationAssumeRole` | **Primary trust-boundary surface** — see §5C. Takes `InstanceId`, assume-role, likely output-bucket params. |

**Undocumented/hidden-knob note:** the install page does not expose runbook parameters; enumerate them from the SSM runbook reference and the SDK model (`ssm:GetDocument AWSSupport-TroubleshootSSH`) — the delta between console-exposed and API-accepted parameters (esp. any that choose the assume-role, output bucket, or install source) is a lead.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Anonymous internet client | `s3://ec2rescuelinux` objects | Anonymous HTTPS GET | A non-AWS principal can **write/replace** an object, or **claim the bucket name** (any region/partition) → every doc-following install is RCE. **Hard stop + disclose on any hit.** |
| Network path (client ↔ S3) | the tarball bytes | TLS transport | A downgrade/MITM that substitutes `ec2rl.tgz` and the user skipped GPG (it's optional) → RCE. |
| Published artifact | user's trust decision | Optional GPG/sha256 gate | A substituted {tarball+key+sig} triple (same origin) yields **"Good signature"**, or the user accepts despite the doc-printed `not certified`/`no ultimately trusted keys` warnings → tampered tool run as root. |
| Malicious `ec2rl.tgz` | instance filesystem | `tar -xzvf` | An archive entry writes **outside** the unpack dir (abs path / `../` / symlink) → arbitrary file write as the unpacking user (often root). |
| SSM caller ↔ `AutomationAssumeRole` | the automation workflow | `StartAutomationExecution` (role optional → falls back to caller perms) | A low-priv caller drives the workflow with elevated perms, or passes an `AutomationAssumeRole` they lack `iam:PassRole` for. See §5C. |
| SSM caller | target EC2 instance (by free-text `InstanceId`) | online `aws:runCommand` / offline detach-attach | Install/run/stop reaches an instance the caller does not own (no ownership condition; `Resource:"*"` samples). See §5C. |
| **Impaired instance's root volume** | **helper instance + caller `OfflineScript`** | offline path detaches root EBS → attaches to helper → runs caller base64 script | **Arbitrary caller code reads/exfiltrates another instance's disk** (`/etc/shadow`, SSH keys, secrets) from the mounted volume. Critical. See §5C. |
| automation IAM role | `awssupport-ssm.*` S3 (CFN template/zip) | wildcard-scoped `GetObject` + `CreateRole`/`PassRole` | A non-AWS principal occupying an `awssupport-ssm.*` name feeds an attacker CFN/IAM policy → confused-deputy privesc. **Hard-stop/disclose on any claimability evidence.** |
| Any customer surface | **AWS service plane** (`ec2rescuelinux` bucket, `AWSSupport-*` managed roles) | — | **Hard stop.** Any AWS-fleet credential/ARN/ownership proof → preserve evidence, disclose, do not exploit. |

---

## 5. Recommended Areas of Focus

<!-- ORDER: A (supply-chain takeover) and B (signature gate) are the install-page core; C (SSM runbook) is the cross-boundary path; D (tarball) is conditional on A/B. -->

### 5A. Supply-chain: distribution-origin integrity & name takeover  — PRIORITY 1
**Background:** The documented install is a single anonymous `curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz`. The bucket `ec2rescuelinux` is a **global-namespace, path-style** S3 bucket. All four supply-chain objects (tarball, sha256, key, sig) are served from this one origin.
**Security Concern:** If any non-AWS principal can write to, or ever claim, this bucket name (in any region/partition, or after any lifecycle/release event), they serve malicious `ec2rl.tgz` to **every** customer who follows the docs — a mass supply-chain RCE, executed as root. The same-origin key+sig means an origin compromise also defeats the signature.
**High-level Test Scenarios (falsifiable):**
- **Claim:** The bucket name `ec2rescuelinux` is not owner-pinned in docs and could be claimable if ever released. **Mechanism:** doc hardcodes `s3.amazonaws.com/ec2rescuelinux/*`; nothing states the owning account. **Oracle:** (read-only) confirm current ownership via `aws s3api get-bucket-location`/HEAD **without mutating**; a `404 NoSuchBucket` in any partition where the doc URL is still published = claimable land-grab (Lens EE / "whoAMI/Bucket-Monopoly" shape). **DO NOT create the bucket.** **Severity:** Critical (+ hard stop/disclose). **Stop:** on any evidence the bucket is unowned/writable.
- **Claim:** Object-level write is possible (bucket ACL/policy misconfig). **Oracle:** read-only policy/ACL inspection only; any `PutObject` allow for a non-AWS principal = Critical. **Never attempt a write.**
**Doc evidence:** install-page step 1; the `s3.amazonaws.com/ec2rescuelinux/` origin. **Severity-if-true:** Critical.

### 5B. Signature-/integrity-gate integrity (Lens U + P)  — PRIORITY 2
**Background:** The page devotes a whole section to verification but labels it **"(Optional)"**, and its own example output prints `WARNING: This key is not certified with a trusted signature!` and `no ultimately trusted keys found`.
**Security Concern:** The gate is (1) optional, (2) rooted in a key fetched from the **same bucket** as the artifact (no independent trust anchor), and (3) documented in a way that **trains users to accept the exact warning** that would flag a substituted key. There is no emphasized out-of-band step to verify the fingerprint `E528…2A1C` against an independent AWS channel. The sha256 is same-origin too → integrity, not authenticity.
**High-level Test Scenarios (falsifiable):**
- **Claim:** A substituted `{ec2rl.tgz, ec2rl.key, ec2rl.tgz.sig}` triple produced by an attacker who controls the origin yields `Good signature from "ec2autodiag@amazon.com"`, because trust is TOFU on the same-origin key. **Mechanism:** doc imports `ec2rl.key` from the bucket and verifies against it; no independent fingerprint check is mandated. **Oracle:** in a lab, import an attacker key named identically, sign a tampered tarball, run the documented `gpg2 --verify` → observe "Good signature" with the same warnings the doc says to ignore. **Severity:** High (defeats the only authenticity control).
- **Claim:** The doc's guidance causes users to proceed past the warning that actually matters. **Mechanism:** the page explains the `not certified` / `no ultimately trusted keys` warnings as benign ("In an ideal world you would visit an AWS office…"). **Oracle:** doc-review finding — the happy path never pins the fingerprint OOB. **Severity:** Low–Informational (AWS-owned doc-safety gap; raises severity of 5A).
- **Claim:** Because verification is "(Optional)", the modal install skips it entirely. **Oracle:** step-2 is parenthetical "(Optional)". **Severity:** enabler for 5A (High when chained).
- **Claim:** The `sha256sum -c` step gives users **false authenticity confidence** — it is a *non-optional-looking* step but the hash is fetched from the **same bucket** as the tarball, so it proves transit-integrity only, not origin/publisher authenticity. **Mechanism:** `curl -O …/ec2rl.tgz.sha256` then `sha256sum -c` from the same origin. **Severity:** Medium (misplaced confidence; not an independent control).
- **Claim (bundled build, Lens U):** The **bundled build** path has even weaker first-party verification coverage — the AWS page shows **no inline sha256/GPG steps**, only *"For a link to the download and a list of limitations, see [EC2Rescue for Linux] on github."* Users of lower-Python-version systems (the bundled build's audience) get verification guidance only from the third-party-maintained GitHub page. **Oracle:** doc-review — the AWS-owned page carries no verification for the bundled artifact family (`ec2rl-bundled.tgz*`, same `ec2rescuelinux` bucket). **Severity:** Medium (coverage gap, same root exposure, smaller population).
**Doc evidence:** "(Optional) Verify the signature…" section; the printed WARNING block; "In this case, the website is an Amazon Web Services website." (sole basis offered for trusting the key); bundled-build "see … on github" sentence. **Severity-if-true:** High (chained with 5A); Informational–Medium standalone. **Owner-to-fix:** AWS (doc + distribution design).

### 5C. `AWSSupport-TroubleshootSSH` runbook — IAM/automation trust boundary  — PRIORITY 2
**Background:** The install page points to this AWS-authored SSM Automation runbook as the remote way to "install EC2Rescue for Linux and then use the tool" against a Linux instance over SSM. It has two paths:
- **Online** (instance is SSM-managed): `aws:configurePackage` (`AWS-ConfigureAWSPackage`) installs the `AWSSupport-EC2Rescue` Distributor package → `aws:runCommand` runs EC2Rescue **on the target instance under the target's own instance-profile identity** (not the automation role).
- **Offline** (`AllowOffline=true`, `Action=FixAll`, instance unmanaged): chains `aws:executeAutomation` → **`AWSSupport-ExecuteEC2Rescue`** → **`AWSSupport-StartEC2RescueWorkflow`**, which: deploys a fresh CFN stack (new VPC/subnet/IGW, a `AWSSupport-EC2Rescue-*` Lambda + **IAM role + instance profile**), launches a **helper instance**, **stops the impaired instance, detaches its root EBS volume, attaches it to the helper**, then `aws:runCommand` runs the **caller-supplied base64 `OfflineScript`** against the mounted volume (chroot to `EC2RESCUE_OFFLINE_SYSTEM_ROOT`), then reattaches/restarts and tears down.

**Security Concern:** This is the only install path that crosses an AWS/account trust boundary. The offline path physically mounts one instance's disk into a fresh, **caller-influenced** compute environment and runs **arbitrary caller code** against it. The published sample IAM policies are AWS-authored artifacts admins copy verbatim (Lens R/S) and use `Resource:"*"` / name-prefix wildcards with no ownership condition.

**High-level Test Scenarios (falsifiable, priority order):**
- **Claim (Critical):** The offline chain executes arbitrary caller code against another instance's full root filesystem. **Mechanism:** `AWSSupport-StartEC2RescueWorkflow`'s `OfflineScript` is *"(Required) Base64 encoded script to run against the helper instance… chroot to an offline Linux root volume and perform an offline remediation"* — fully caller-authored, run with the original root volume mounted. **Oracle:** with an `AutomationAssumeRole` scoped only for "SSH troubleshooting," run `AllowOffline=true`+`Action=FixAll` against an `InstanceId` the operator does not administer, supplying an `OfflineScript` that reads `/etc/shadow`/SSH host keys from the mounted volume. Exfil to a canary bucket = breach. **Severity:** Critical (confidentiality/integrity of any instance reachable by `InstanceId`/`UnreachableInstanceId`). **Stop:** if evidence points at AWS's own fleet, hard-stop + disclose.
- **Claim (High):** No IAM resource/tag condition scopes *which* instances an `AutomationAssumeRole` holder can target. **Mechanism:** every published sample policy across `TroubleshootSSH`/`ExecuteEC2Rescue`/`StartEC2RescueWorkflow` uses `Resource:"*"` for EC2/SSM actions; `InstanceId`/`UnreachableInstanceId` are free-text, no ownership-tag validation. **Oracle:** as a caller authorized only to run this runbook, pass the `InstanceId` of another team's instance (same account) and see if stop/backup/detach proceeds. **Severity:** High (cross-team blast radius; stops/mutates out-of-scope instances).
- **Claim (Critical if enforcement gap / Low if doc gap):** `iam:PassRole` is load-bearing (`AutomationAssumeRole` is accepted as a parameter) but **never listed** in `TroubleshootSSH`'s "Required IAM permissions" block (only buried in `StartEC2RescueWorkflow`'s deeper policy). **Oracle:** start `TroubleshootSSH` passing an `AutomationAssumeRole` the caller lacks `iam:PassRole` for — silent acceptance = real escalation; rejection = doc omission that drives admins to over-grant `iam:PassRole:*`. **Severity:** Critical (gap) / Low (doc-only).
- **Claim (Critical→Info):** The CFN template/Lambda-zip fetch is scoped by a **bucket-name wildcard** `arn:aws:s3:::awssupport-ssm.*/*.template` + `*.zip`, combined with `iam:CreateRole`/`PutRolePolicy`/`AttachRolePolicy`/`PassRole` scoped only by name-prefix `AWSSupport-EC2Rescue-*` (not by policy *content*). **Oracle (read-only):** determine whether `awssupport-ssm.<suffix>` is an AWS-reserved prefix partition-wide or a mere convention; confirm `GetObject` source-bucket owner is always an AWS account in CloudTrail. **Any evidence a non-AWS principal can occupy an `awssupport-ssm.*` name = Critical confused-deputy (attacker CFN/IAM content) + hard-stop/disclose.** Otherwise Informational. **Lens:** EE + R.
- **Claim (High):** The freshly-provisioned helper role `AWSSupport-EC2Rescue-*` gets policies attached from an **undisclosed, unversioned** CFN template (`iam:PutRolePolicy`/`AttachRolePolicy` with no content constraint in docs). **Oracle:** diff the actual deployed template (real-run CloudTrail `CreateStack` params) vs minimal need. **Severity:** High if over-broad; Medium doc-gap.
- **Claim (Medium):** Collected logs (`S3BucketName`/`LogDestination`) and pre/post-rescue **AMIs** are left with no automation-enforced access control — only advisory text (*"The AMI will persist after the automation completes. It is your responsibility to secure access… or delete it."*). **Oracle:** run with backups on + a broad bucket policy; check resulting AMI/log object permissions. **Severity:** Medium–High (persistent disk/diagnostic copies leak via downstream misconfig; note the flow requires an **unencrypted** root volume).
- **Claim (Medium):** `Action=CheckAll` (read-only default) and `Action=FixAll` (mutating, runs EC2Rescue fix modules as root on the box) require the **same** documented IAM set — a diagnostics-only operator can flip to live remediation with no extra grant. **Oracle:** confirm a check-only caller can set `Action=FixAll` and succeed. **Severity:** Medium.
- **Claim (Medium, Lens U/supply-chain tie-in):** The **automated** install path (`AWS-ConfigureAWSPackage` / `AWSSupport-EC2Rescue` Distributor package) documents **no** signature/integrity check, in contrast to the manual page's detailed (optional) GPG flow. **Oracle:** inspect the Distributor package signing manifest (live, out-of-scope here) — confirms whether Distributor signing supersedes GPG or a gap exists. **Severity:** Medium (undocumented = the doc-review finding).

**Doc-gaps (confirm surface first):** CFN template content never shown (can't audit helper-role policy statement-by-statement); no `iam:PassRole` `iam:PassedToService` condition examples; no ownership/tag resource constraints in any of the 4 sample policies; no failure/rollback semantics if `OfflineScript` hangs (orphaned attached volume?); no statement on whether helper SSM-agent/CloudWatch logs capture `OfflineScript` output from the mounted volume.
**Sources:** `automation-awssupport-troubleshootssh.html`; mirror `automation-awssupport-{executeec2rescue,startec2rescueworkflow,installec2rescue}.md`, `automation-ec2rescue.md`. (`AWSSupport-TroubleshootConnectivityToRDS` is **not** referenced by this family — ruled out.)
**Severity-if-true:** Critical (offline-path cross-instance data exposure + arbitrary code on mounted volume).

### 5D. Malicious-tarball unpack (Lens Q) — PRIORITY 3 (conditional on 5A/5B)
**Background:** Install step: `tar -xzvf ec2rl.tgz`, typically as root.
**Security Concern:** Only reachable if 5A/5B succeed, but then a crafted archive with absolute paths, `../` traversal, or symlink entries writes outside `ec2rl-<version>/` on extraction.
**High-level Test Scenarios:**
- **Claim:** `tar -xzvf` of an attacker tarball writes to an arbitrary path (e.g. `/etc/cron.d/`, `~/.ssh/authorized_keys`). **Oracle:** lab extraction of a poisoned tarball → file appears outside the expected dir. **Severity:** High (arbitrary write as root) — but gated on origin control, so inherits 5A.
**Doc evidence:** install-page step 5. **Severity-if-true:** High (chained).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Replace `ec2rl.tgz` at origin → mass RCE | `s3://ec2rescuelinux` | Bucket is AWS-owned & write-protected (unverified) |
| Bucket-name land-grab if released | S3 global namespace | None documented (name hardcoded) |
| Substituted key+sig accepted as "Good signature" | GPG verify flow | OOB fingerprint trust (not emphasized; TOFU same-origin) |
| User skips optional verification | Install procedure | Verification is "(Optional)" — no enforcement |
| MITM/downgrade on download | TLS to S3 | HTTPS URL (no documented pin/HSTS note) |
| Path-traversal tarball unpack | `tar -xzvf` | None documented |
| Cross-instance install/read via SSM | `AWSSupport-TroubleshootSSH` | AutomationAssumeRole + IAM (audit §5C) |

---

## 7. Out-of-Scope Risk Categories
- **Module-execution RCE, `--backup` over-privilege, upload exfil (`--support-url`/`--presigned-url`)** — these live on `ec2rl_working.html` / `ec2rl_moduledev.html`, owned by `Linux-Server-EC2Rescue-attack-research-plan.md`. Cross-referenced, not re-tested here.
- **Code bugs in the `awslabs/aws-ec2rescue-linux` repo** — third-party reference code; read for trust-model understanding only, not a live PoC target here.
- **A root user attacking their own instance** — the tool runs as root by design; a user with root subverting their own box is not a boundary crossing.
- **IMDS on the managed/customer instance** — in the customer's own trust zone.
- **Actively probing / mutating the live `ec2rescuelinux` bucket** — read-only ownership reasoning only; any write attempt is prohibited (and any claimability evidence is a hard-stop disclosure, not an exploit).

## 8. Null hypotheses / doc gaps
- **Cross-tenant IDOR / credential vending / control-ENI (Lens A/C/D/V):** N/A for the *install* flow — read `ec2rl_install`, `Linux-Server-EC2Rescue`, `ec2rl_working`; no multi-tenant fleet, no per-tenant resource IDs, no service-owned ENI on the install path.
- **Prompt injection / LLM (Lens K):** N/A — no LLM/agent in the install flow.
- **KMS / attestation (Lens H/W):** N/A — no CMK or attestation on install.
- **SSRF (Lens G):** doc-gap — the only server-side fetch is the SSM runbook pulling the package under the automation's identity; covered as a supply-chain tie-in in §5C, not an independent SSRF.
- **Runbook internals (§5C):** partially resolved from the online + mirror runbook docs. Remaining doc-gaps are enumerated at the end of §5C (CFN template content, PassRole conditions, resource/tag scoping, failure semantics, helper-log capture) — confirm those surfaces first.
- **Verbatim-quote caveat:** the bundled-build GitHub README detail (`ec2rl-bundled.tgz*` URLs) was retrieved via a summarizing fetch and should be re-validated with a raw read before being cited as an exact quote. The `awslabs/aws-ec2rescue-linux` source itself is third-party reference code — read for trust-model understanding, not a live PoC target.
