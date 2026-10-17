# EC2Rescue for Linux (ec2rl) — Module Development & Execution — Attack Research Plan

Source of leads:
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2rl_moduledev.html (mirror: `docs/AWSEC2/latest/UserGuide/ec2rl_moduledev.md`) — **primary target**
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Linux-Server-EC2Rescue.html (overview)
- `docs/AWSEC2/latest/UserGuide/ec2rl_install.md`, `ec2rl_working.md` (install / run / upload)
- https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootssh.html and `…-executeec2rescue.html` (remote/SSM delivery)
- Public source repo the docs point to: https://github.com/awslabs/aws-ec2rescue-linux

Status: **documentation-derived hypotheses only; nothing tested against a live account or instance.** Several high-value leads require confirming implementation internals in the public repo — those are marked `impl-confirm`. Where the docs are silent on an internal, the lead is marked `doc-gap — confirm surface first`.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- **Scope note / what "a boundary" means here.** EC2Rescue for Linux is an *open-source tool that the customer runs on their own instance, as their own root*. A customer invoking `sudo ./ec2rl run` and getting root code-exec is **not** a vulnerability — they already have root. The boundaries that matter are the ones where a **lower-privileged or remote principal crosses into root on the instance**, or where **instance/account data crosses to somewhere it should not**:
  1. **local unprivileged user → root** (writable module dir, predictable temp path, parse-time deserialization, arg injection picked up by a `sudo` run);
  2. **remote IAM principal with limited SSM permissions → root code-exec on the instance** (the `AWSSupport-*` runbooks);
  3. **impaired-instance disk data → a helper instance / caller-chosen VPC** (offline remediation);
  4. **tool/module/software supply chain → root** (optional signature verification, AWS-owned S3 bucket, `software`/`package` download URLs);
  5. **any root-exec primitive → instance-profile credentials via IMDS → AWS account** (the escalation sink every primitive chains into).
- **HARD STOP:** the moment evidence implicates an **AWS-owned asset** — the `ec2rescuelinux` S3 bucket / signing key / SSM Distributor package pipeline, or the AWS-authored `AWSSupport-*` runbook definitions themselves — stop, preserve evidence, and route to **AWS-Security** disclosure. Those are the only "service-plane" assets in an otherwise self-hosted tool.

---

## 1. Pentest Objectives

Stated as concrete boundary-breach outcomes:

1. From a **non-root local user**, achieve code execution or arbitrary file write **as root** by influencing something a later `sudo ./ec2rl run` (or an SSM-driven root run) reads: a module file, the module directory, the `/var/tmp/ec2rl` workdir, a sourced `functions.bash`, or a CLI/SSM argument.
2. Cause **arbitrary code execution at YAML parse time** (not script-execution time) by crafting a module whose custom tag / embedded objects are constructed by an unsafe loader — triggerable merely by `./ec2rl list` / `help` / `run` enumerating `mod.d/`.
3. As an **IAM principal with only the documented minimal SSM permissions**, obtain root code-exec on a target instance, or make the automation act with privileges the caller does not hold (confused deputy on `AutomationAssumeRole`).
4. Via the **offline remediation** flow, read an impaired instance's **root-volume disk contents** from a helper instance or expose them in a caller-chosen subnet/VPC/S3 bucket.
5. Subvert the **download/verification chain** (optional GPG verification, the `ec2rescuelinux` bucket, `software`/`package` URLs) to run attacker code as root on the instance.
6. Exfiltrate collected diagnostic output (which may contain secrets) to an attacker-chosen destination via `ec2rl upload --support-url` / `--presigned-url`.
7. Chain any of the above into **theft of the instance's IAM role credentials** (IMDS `169.254.169.254`) → lateral movement into the AWS account.

---

## 2. Components, Assets, and Design

**The tool.** `ec2rl` — a Python 2.7.9+/3.2+ CLI (`ec2rl.py`) shipped as `ec2rl.tgz` (standard build) or a bundled build embedding a minimal Python. Runs on Amazon Linux / RHEL7+ / Ubuntu16.04+ / SLES12+. Invoked `./ec2rl run|list|help|upload`. Some modules require root; non-root users are told to `sudo ./ec2rl run`.

**Modules.** >100 YAML files (in `mod.d/`). Each is a single YAML document opening with the tag `--- !ec2rlcore.module.Module`, which per the docs "tells the YAML parser **which constructor to call** when creating the object from the data stream. You can find the constructor inside the `module.py` file." Key attributes:
- `content` — "The entirety of the script code." (bash or python per `language`); executed by the tool.
- `placement` — `prediagnostic | run | postdiagnostic` (lifecycle stage).
- `sudo` — "If the value is true, then the EC2Rescue for Linux logic only runs the module when the executing user has root access." (The module trusts the tool's root determination — `EC2RL_SUDO` — rather than re-checking.)
- `required` / `optional` — CLI arguments the module consumes; the example `ps` module interpolates them into the shell script as `$times` / `$period`, and the `dig` module takes `--domain=` → used as `$domain`.
- `software` / `package` — external executables the module needs and a URL/package pointer for obtaining them ("intended to specify software that is not installed by default"); the tool "ensures that these programs are present and executable before running the module."
- `constraint`, `distro`, `perfimpact`, `parallelexclusive` — gating/metadata. `perfimpact:true` modules are skipped unless `--perfimpact=true`.

**YAML parsing surface.** The docs explicitly teach custom YAML tags: `!ec2rlcore.module.Module` (invoke a Python constructor), `!!str` (force string), `|` literal scalar. The parser is constructed to call application code during load — this is the deserialization seam (see Lens F).

**Execution environment / env vars (doc-provided).**
- `EC2RL_CALLPATH` — path to `ec2rl.py`, "used to locate the lib directory and use vendored Python modules." (Library-resolution seam.)
- `EC2RL_WORKDIR` — default **`/var/tmp/ec2rl`** (predictable, shared, world-relevant temp path).
- `EC2RL_RUNDIR` — `/var/tmp/ec2rl/<date&timestamp>`; `EC2RL_GATHEREDDIR` — `…/mod_out/gathered/`.
- `EC2RL_SUDO` — "True if EC2Rescue for Linux is running as root." (Trusted by modules.)
- `EC2RL_INTERFACES` — "generated by `functions.bash` and is only available for modules that have sourced it" → modules `source functions.bash` (file-resolution seam).
- `EC2RL_NET_DRIVER`, `EC2RL_VIRT_TYPE` — derived from instance metadata.

**Delivery paths (who causes a root run).**
1. **Local:** owner runs `./ec2rl run` (`sudo` for root modules).
2. **Remote / SSM online:** `AWSSupport-TroubleshootSSH` → `aws:configurePackage` (`AWS-ConfigureAWSPackage`) installs EC2Rescue, then `aws:runCommand` runs a bash script that runs it as root on the managed instance.
3. **Remote / SSM offline:** `AWSSupport-TroubleshootSSH` → `AWSSupport-ExecuteEC2Rescue` — stops the impaired instance, creates an AMI, launches a **helper instance** in a caller-supplied `SubnetId` (or a newly-created VPC), attaches the impaired instance's root volume, and runs EC2Rescue against the mounted foreign volume. (Confirm exact steps — see §5 Lead V1 and subagent findings.)

**Install / integrity.** `curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz` over HTTPS; `ec2rl.tgz.sha256` from the **same** bucket; GPG verification against `ec2rl.key` + `ec2rl.tgz.sig` is an **"(Optional)"** step. Signing identity `ec2autodiag@amazon.com`, key `2FAE2A1C`.

**Results / upload.** `./ec2rl upload --upload-directory=… --support-url="<url from Support>"` or `--presigned-url="<S3 presigned>"`. Logs land under `/var/tmp/ec2rl/<timestamp>/mod_out/…` (predictable, may contain syslog, package lists, process dumps, and inadvertently secrets).

**Backup side-effect.** `./ec2rl run --backup=ami|allvolumes|vol-id` creates an AMI or EBS snapshots of attached volumes.

**Assets worth protecting:** root on the instance; the instance's IMDS/instance-profile credentials; the instance's and (offline) the *impaired* instance's disk contents; collected diagnostic data; the integrity of the AWS-published tool and signing key; the AWS-authored SSM runbook permission model.

**Identifiers:** module `name` (≤18 chars), the global S3 bucket name `ec2rescuelinux`, deterministic paths `/var/tmp/ec2rl[/<timestamp>]`, the SSM Distributor package name for EC2Rescue.

```
                         (optional GPG verify)
  s3://ec2rescuelinux/ec2rl.tgz ──HTTPS──▶ customer instance ── unpack ──▶ ec2rl.py
                                                                              │
   CLI/SSM args ──▶ --only-modules / --<arg> ──┐                             │ enumerates mod.d/
                                                ▼                             ▼
                                    ┌─────────────────────────────────────────────────┐
   mod.d/*.yaml ──(custom YAML)────▶│  YAML load  →  Module object (module.py ctor)     │  ← PARSE-TIME (Lens F)
   (writable dir? downloaded?)      │      content (bash/python)  +  $arg interpolation │  ← RUN-TIME as root if sudo
                                    └─────────────────────────────────────────────────┘
                                                │                         │
                 workdir /var/tmp/ec2rl ◀───────┘                         └──▶ source functions.bash / software,package URLs
                 (predictable; symlink/TOCTOU?)                                 (external fetch as root)
                                                │
                 ec2rl upload --support-url/--presigned-url ──▶ attacker-chosen URL (exfil)
                                                │
  ANY root exec ──▶ IMDS 169.254.169.254 ──▶ instance-profile creds ──▶ AWS account (escalation sink)

  Remote: AWSSupport-TroubleshootSSH ─(online)─▶ ConfigureAWSPackage install + runCommand(root)
                                     └(offline)─▶ AWSSupport-ExecuteEC2Rescue: stop instance → AMI →
                                                   helper instance in caller SubnetId → attach impaired
                                                   root volume → scan mounted foreign disk
```

---

## 3. Trust-Boundary Map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|---|
| TB1 | Local **non-root** user | root on the instance | a later `sudo ./ec2rl run` reads an attacker-influenced module file / `mod.d` dir / workdir / sourced file / arg | an unprivileged user causes **code exec or arbitrary file write as root** (writable `mod.d`, symlinked `/var/tmp/ec2rl`, attacker `functions.bash`) |
| TB2 | Untrusted **module YAML** (shared/downloaded/planted) | instance root — **at parse time** | custom constructor `!ec2rlcore.module.Module` / unsafe loader builds objects while enumerating `mod.d/` | merely running `./ec2rl list`/`help`/`run` **executes attacker code before any gating** |
| TB3 | Caller-controlled **CLI/SSM argument** | the root-run shell script | `required`/`optional` arg value interpolated into `content` (`$times`,`$domain`,…) | an arg value **breaks out of the intended command** → command injection (high value when the arg source ≠ the module author, e.g. SSM parameters) |
| TB4 | Remote **IAM principal** (minimal SSM perms) | root code-exec on the instance | `AWSSupport-TroubleshootSSH`/`-ExecuteEC2Rescue` install+run ec2rl as root | a principal **without direct instance/SSH access** obtains root on the instance, or the automation acts with privileges the caller lacks (confused deputy on `AutomationAssumeRole`) |
| TB5 | Offline **helper instance** / caller subnet | the **impaired instance's root-volume data** | runbook stops instance, snapshots, attaches impaired volume to a helper in caller `SubnetId`/new VPC | impaired-instance disk contents become **readable on a helper instance / in a caller-chosen network / S3 bucket** |
| TB6 | AWS-published **download / `software`/`package` URL** | instance root | `curl` over HTTPS (GPG **optional**); module-declared software fetch | a **tampered or substituted** tarball/software is executed as root (MITM, bucket/package takeover, skipped signature) |
| TB7 | `ec2rl upload` **destination URL** | collected diagnostic data | POST to `--support-url` / `--presigned-url` | diagnostic output (possibly containing secrets) is **sent to an attacker-chosen endpoint** |
| TB8 | **Any root-exec primitive** above | instance-profile credentials | root reads IMDS `169.254.169.254` | **instance IAM credentials stolen** → pivot into the AWS account (the escalation sink; rate chains at this severity) |
| TB9 | Customer surface | **AWS-owned** `ec2rescuelinux` bucket / signing key / SSM package / runbook defs | supply/distribution pipeline | **HARD STOP** — any evidence implicating these is an AWS-Security disclosure, not a customer finding |

---

## 4. API / Interface Inventory

| Name | Method/Form | New/Exist | Mutating | Internal/External | Functionality | Callable from | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2rl run` | CLI | Exist | Yes (runs code as root) | Local | Run all modules | local shell | local user (root for `sudo` modules) | reads every `mod.d/*.yaml` |
| `ec2rl run --only-modules=<name> --<arg>=<v>` | CLI | Exist | Yes | Local | Run specific module + args | local shell | local user | **arg values flow into `content`** (TB3) |
| `ec2rl list` / `help [module]` | CLI | Exist | No (but **parses** all modules) | Local | Enumerate/describe | local shell | local user | parse-time deserialization reachable here (TB2) |
| `ec2rl upload --support-url/--presigned-url` | CLI | Exist | No (egress) | Local→Internet | Upload results | local shell | local user | arbitrary-URL egress of logs (TB7) |
| `ec2rl run --backup=ami\|allvolumes\|vol-id` | CLI | Exist | Yes (AWS resources) | Local→AWS API | Create AMI/snapshots | local shell (needs instance creds) | instance IAM role | uses instance-profile creds |
| `mod.d/*.yaml` (module load) | File interface | Exist | Yes (indirectly) | Local FS | Define/execute modules | filesystem | whoever can write `mod.d` | **the primary planting surface** (TB1/TB2) |
| `source functions.bash` | File interface | Exist | Yes | Local FS | Shared bash helpers | filesystem | — | library-resolution seam (`EC2RL_CALLPATH`) |
| `AWS-ConfigureAWSPackage` (install EC2Rescue) | SSM Automation step | Exist | Yes | AWS→instance | Install distributor package | SSM | AutomationAssumeRole / caller | package-source trust (TB6) |
| `AWSSupport-TroubleshootSSH` | SSM Automation runbook | Exist | Yes | AWS (external) | Install+run ec2rl (online) / dispatch offline | SSM API | IAM principal w/ ssm perms | **"If no role is specified, …uses the permissions of the user that starts this runbook."** (TB4) |
| `AWSSupport-ExecuteEC2Rescue` | SSM Automation runbook | Exist | Yes | AWS (external) | Offline remediation (stop/AMI/helper/attach volume) | SSM API | IAM principal | cross-instance disk exposure (TB5) |
| Download endpoints `s3://ec2rescuelinux/{ec2rl.tgz,.sha256,.sig,.key}` | HTTPS GET | Exist | No | Internet | Obtain tool + integrity files | anyone | public | **GPG verify = optional**; sha256 same-origin (TB6/TB9) |

**Doc-planted leads kept verbatim:** install page labels signature verification **"(Optional)"**; the TroubleshootSSH doc warns operators to "Make sure the bucket policy does not grant unnecessary read/write permissions" for `S3BucketName`; "By default, the runbook operates in read-only mode" (a guarantee to test — Lens U); `AllowOffline` triggers the stop/AMI/attach path.

**Undocumented-knob hunt:** enumerate every `ec2rl` CLI flag and every module attribute the *reference* implies but prose omits — e.g. any flag that changes the module search path, the workdir, the loader behavior, or disables constraint/sudo gating; any `--<arg>` that a module passes to a shell unquoted. The delta between documented flags and `ec2rl --help` / argparse in `ec2rl.py` is a lead (`impl-confirm`).

---

## 5. Recommended Areas of Focus (priority order)

> **Implementation-confirmed status (public repo `awslabs/aws-ec2rescue-linux`, master).** Two subagents read the source and the full SSM runbook family. Net effect on priority: **Area 2 (local privesc) and Area 5 (offline cross-instance disk) are now CONFIRMED-risky from code/doc and lead the plan; Area 1 is real but gated behind a module-planting precondition; Area 3 is DOWNGRADED (the framework is injection-safe — risk is per-module bash quoting only).** Confirmed evidence is inlined per area.

### Area 1 — Parse-time deserialization via the custom module constructor (Lens F)
**Background.** The docs teach that `--- !ec2rlcore.module.Module` "tells the YAML parser which constructor to call," pointing at `module.py`.
**CONFIRMED (impl).** `ec2rlcore/module.py` does `yaml.add_constructor("!ec2rlcore.module.Module", module_constructor, Loader=Loader)` and `yaml.load(config_file, Loader=Loader)` where `Loader` is the base/`CLoader` — **not `SafeLoader`**. This is PyYAML's documented `yaml.load` RCE footgun: although only the `!ec2rlcore.module.Module` tag has a registered constructor, the non-safe loader will still honour a smuggled `!!python/object/apply:os.system [...]` tag in a module file, executing **at parse time** (during `./ec2rl list`/`help`/`run`, before `placement`/`sudo`/`constraint` gating). The constructor itself only does `construct_mapping(node, deep=True)` + `Constraint(...)`, so the parse-time gadget must come from the YAML, which means **an attacker must be able to supply/modify a `.yaml` file** that the tool enumerates.
**Security Concern.** This converts the "untrusted module source" problem into RCE: a module shared by a third party, downloaded, or dropped by a lower-privileged local user (→ Area 2) executes attacker code the instant anyone lists the module directory — as the invoker (root under `sudo`).
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* a module file in `mod.d/` containing a `!!python/object/apply:…` tag executes at parse during `./ec2rl list`. **Oracle:** place a benign side-effecting tag (touches a `/tmp` canary) in a lab `mod.d` file; confirm the canary appears on `list`, before any `run()`.
- *Claim:* the only precondition is file-supply, not script execution — so an untrusted/shared module is dangerous even if never "run." **Oracle:** canary fires under `list`/`help`, not just `run`.
**Doc evidence.** ec2rl_moduledev.html "Use YAML syntax" + attribute table; impl: `module.py` loader call. **Severity-if-true:** High (code exec as invoker on parse) — **but bounded by the module-planting precondition** (Area 2 for local; untrusted-module-source for remote). **Stop condition:** a parse-time side effect fires before `content` execution.

### Area 2 — Local privilege escalation: world-writable workdir + unchecked `mod.d` load (Lens E + Lens EE predictable path) — **CONFIRMED-risky; run first for local**
**Background.** Root modules run under `sudo ./ec2rl run`; the tool uses the **predictable, fixed** workdir `/var/tmp/ec2rl` and loads every `mod.d/*.yaml`.
**CONFIRMED (impl) — two distinct local-privesc primitives:**
1. **World-writable workdir, no symlink/ownership check.** `ec2rlcore/main.py::_setup_write_paths()` does `os.mkdir(WORKDIR)` then `os.chmod(WORKDIR, 0o777)` on `/var/tmp/ec2rl`, with **no `os.path.islink`/`O_NOFOLLOW`** guard, and **silently reuses** an existing path on `EEXIST`. `/var/tmp` is world-writable and the name is fixed/predictable. A non-root user who pre-creates `/var/tmp/ec2rl` as a **symlink** (or as a dir they own) before a `sudo ec2rl` run makes the root process `chmod 0o777` and write through it → arbitrary file write/overwrite as root. (The per-run `RUNDIR` is `0o700`, but the parent `WORKDIR` is the exposed hinge.)
2. **No ownership/permission check on module files before parse+exec.** `ec2rlcore/moduledir.py::ModuleDir.__init__` enumerates with `os.listdir(directory)`, filters only on `.yaml`/hidden prefix, and calls `module.get_module(path)` directly — **no `st_uid`/`st_mode` validation**. Safety reduces entirely to the install-time permissions of `mod.d`. If that directory is ever non-root-writable (unpacked under a user-writable path, group-writable, or a shared install), a dropped module gets **full parse-time RCE** as root via Area 1's non-safe loader.
**Security Concern.** Either primitive turns a local unprivileged user into root the next time `ec2rl` is run as root (an admin manually, or an SSM root run).
**High-level Test Scenarios:**
- *Claim:* pre-creating `/var/tmp/ec2rl` as a symlink to a root-owned target redirects root-written output / `chmod 0o777`s the target. **Oracle:** in a lab, `ln -s /target /var/tmp/ec2rl` as a non-root user, run `sudo ec2rl run`, observe the write/mode-change follow the link.
- *Claim:* a `mod.d` writable by the invoking non-root user yields root RCE on the next root run (chains Area 1). **Oracle:** confirm the unpacked default perms of `ec2rl-<ver>/mod.d`; drop a canary module; run as root.
**Doc evidence.** moduledev env-var table (`EC2RL_WORKDIR=/var/tmp/ec2rl`); impl: `main.py::_setup_write_paths`, `moduledir.py`. **Severity-if-true:** High (local non-root → root). **Stop condition:** a root-owned file write/exec driven by an unprivileged user.
**Note (CALLPATH sub-lead refuted):** the `ec2rl` launcher pins its dir via `BASEDIR="$(dirname "$(readlink -f "$0")")"` and the Python core does not `source functions.bash` from an env/CWD-derived path — so the `EC2RL_CALLPATH`/lib-sourcing privesc angle is **CONFIRMED-safe** at the framework level (shell-library sourcing lives inside individual bash modules, scoped to the module).

### Area 3 — Argument → shell injection in module `content` (Lens F) — **DOWNGRADED: framework-safe; per-module review only**
**Background.** The `ps`/`dig` examples read `--times=`/`--period=`/`--domain=` as `$times`/`$period`/`$domain` inside bash.
**CONFIRMED (impl) — NOT a framework shell-injection bug.** `module.py::run()` writes `self.content` **verbatim** to a `tempfile.NamedTemporaryFile()` and runs `subprocess.check_output(["/bin/bash", module_file.name], env=envlist, shell=False)`. CLI option values are passed purely as **environment variables** (`envlist[option] = str(value)`); `$domain` etc. are ordinary shell *variable expansions*, not Python-side string splicing. `options.py` does minimal validation (`re.match("[a-zA-Z0-9]", …)` only on bare positional tokens; `--domain=` values pass unchecked).
**Residual concern (per-module).** Injection is possible **only** if an *individual module's bash* uses an arg unsafely — unquoted `$domain` in `eval`/backticks/a command substitution. That is a code-review question against the ~100 shipped modules, not a framework defect, and self-injection by the owner is out of scope; it matters only where the arg source is lower-privileged than the executor (SSM parameter, wrapper).
**High-level Test Scenarios:**
- *Claim:* a shipped module uses an `--arg` value unquoted in a shell-eval context → injection. **Oracle:** grep the bundled `mod.d/*.yaml` `content` for unquoted `$`-expansions inside `eval`, backticks, `$( )`, or `sh -c`; test in a lab.
**Doc evidence.** moduledev example modules; impl: `module.py::run`, `options.py`. **Severity-if-true:** Medium (root command exec, per-module; higher only if an SSM/remote param feeds the arg). **Stop condition:** an injected command runs from an unquoted module arg.

### Area 4 — Remote root via the SSM runbooks: confused deputy & over-broad permissions (Lens B / R / S / U) — **CONFIRMED surface**
**Background.** The `AWSSupport-*` runbook family (Owner: Amazon) installs and runs EC2Rescue as root on a target instance. Members: `AWSSupport-TroubleshootSSH`, `AWSSupport-InstallEC2Rescue`, `AWSSupport-ExecuteEC2Rescue`, `AWSSupport-StartEC2RescueWorkflow`, `AWSSupport-RunEC2RescueForWindowsTool`.
**CONFIRMED (SSM docs):**
- **AutomationAssumeRole is optional on every runbook**, each carrying the identical sentence: *"If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook."* Nothing forces least-privilege scoping.
- **Low-priv → root.** `AWSSupport-InstallEC2Rescue`'s required perms are only `ec2:DescribeInstances`, `ssm:SendCommand`, `ssm:GetCommandInvocation`, `ssm:ListCommandInvocations`, `ssm:ListCommands` — **no EC2 admin, no documented instance-ownership/tag condition.** This set installs the EC2Rescue distributor package and runs it, which executes as **root** via SSM Agent. `AWSSupport-TroubleshootSSH`'s online path chains `aws:configurePackage` (install) → `aws:runCommand` (bash) with no additional root-capability gate.
- **PassRole wildcard prefix.** `AWSSupport-StartEC2RescueWorkflow`'s required-permissions JSON grants `iam:PassRole`, `iam:CreateRole`, `iam:AttachRolePolicy` scoped to `arn:aws:iam::{{account}}:role/AWSSupport-EC2Rescue-*` — a name-prefix wildcard (textbook confused-deputy risk if that prefix ever collides with / is reusable for a higher-privileged role), plus an `ec2:*` block on `"Resource": "*"`.
- **Guarantee to test (Lens U).** `AWSSupport-TroubleshootSSH`: *"By default, the runbook operates in read-only mode"* — prose, not IAM.
**Security Concern.** This is an AWS-authored primitive that converts coarse `ssm:*` rights into arbitrary **root code-exec on an EC2 instance** (and, offline, EBS/EC2 mutation) — the IAM-artifact audit (Lens R) is itself the attack surface.
**High-level Test Scenarios:**
- *Claim:* the minimal `AWSSupport-InstallEC2Rescue` permission set lets a principal with **no OS access and no EC2 admin** get root on any managed instance in the account → run-command-as-root is gated only by coarse `ssm:*`, not per-instance authz. **Oracle:** `iam:SimulatePrincipalPolicy` for `ssm:SendCommand`/`aws:configurePackage` against a foreign instance under exactly that policy; confirm no resource/tag condition.
- *Claim:* `iam:PassRole`/`CreateRole`/`AttachRolePolicy` on `AWSSupport-EC2Rescue-*` is abusable where that prefix collides with a pre-existing privileged role, or where the holder can create a role at that prefix with a broad policy. **Oracle:** audit the printed block statement-by-statement (Lens R/S); check for `PassedToService: ssm.amazonaws.com` absence and prefix-creation reachability.
- *Claim:* "read-only by default" is enforced only by orchestration → a caller setting `Action=FixAll`/`AllowOffline=true` mutates the instance. **Oracle:** trace the guarantee to a mechanism (Lens U).
**Doc evidence.** troubleshootssh.html + the per-runbook "Required IAM permissions" blocks; "uses the permissions of the user that starts this runbook"; "By default … read-only mode." **Severity-if-true:** High (remote → root; privesc). **Stop condition:** root on an instance the caller had no OS access to, under the minimal policy.

### Area 5 — Offline remediation: cross-instance disk exposure + caller-supplied code (Lens V / Lens A disclosure-timing) — **CONFIRMED**
**Background.** When online remediation fails or the instance is unmanaged, the offline flow runs via `AWSSupport-ExecuteEC2Rescue` / `AWSSupport-StartEC2RescueWorkflow`.
**CONFIRMED (SSM docs) — the literal step sequence:** stop the original instance → (optional) pre-backup AMI → `aws:runCommand` install EC2Rescue on a **helper instance** → `aws:executeAwsApi` **Detach the root volume from the provided instance** → **Attach that volume to the EC2Rescue helper instance as `/dev/sdf`** → sleep → `aws:runCommand` run a caller-supplied Bash script against the mounted foreign volume → detach → reattach to the original instance. Additional confirmed facts:
- **Encrypted root volumes are explicitly unsupported** → the impaired instance's root filesystem is mounted **unencrypted** on the helper.
- The **helper instance type** (`EC2RescueInstanceType`) and **subnet** (`SubnetId`, default `CreateNewVPC`/`SelectedInstanceSubnet`) are **caller-selectable**.
- `AWSSupport-StartEC2RescueWorkflow` takes a raw **`OfflineScript`** parameter (base64 Bash/PowerShell) run directly against the mounted disk, with documented env vars such as `EC2RESCUE_OFFLINE_SYSTEM_ROOT=/mnt/mount` — i.e. **caller-supplied arbitrary code executes with the victim's root disk already mounted.**
- **`S3BucketName`/`LogDestination`/`S3Prefix` are caller-supplied, optional, with only a soft warning** (*"Make sure the bucket policy does not grant unnecessary read/write permissions…"*) and **no documented AWS-side bucket-ownership/cross-account restriction**.
**Security Concern.** The offline flow is a sanctioned "mount a target instance's entire disk onto a caller-controlled instance, in a caller-chosen subnet, then run caller-supplied code and ship output to a caller-chosen bucket" primitive — a cross-instance data-exposure and potential exfil path for a principal who can invoke it.
**High-level Test Scenarios:**
- *Claim:* a caller choosing `SubnetId`/`EC2RescueInstanceType` + `OfflineScript` reads another instance's `/etc/shadow`/keys/app-secrets off the mounted `/dev/sdf` and egresses them (network of their chosen subnet, or the caller-chosen S3 bucket). **Oracle:** confirm the detach/attach-to-helper steps (done) and run a lab `OfflineScript` that reads the mounted root and writes to a bucket the assumed role controls.
- *Claim:* `S3BucketName`/`LogDestination` accepts an attacker-owned / cross-account bucket with no ownership check → log/credential exfil. **Oracle:** the soft-warning wording implies no enforcement; verify with a cross-account bucket.
- *Claim (Lens EE / HARD-STOP-adjacent):* the helper instance is provisioned by `aws:createStack` from a CloudFormation template at `arn:aws:s3:::awssupport-ssm.*` (wildcard bucket-name pattern) and the helper AMI owner is **undocumented** → is the template/AMI source confusable/spoofable in some partition/region? **Oracle:** resolve the exact template bucket + AMI owner; **if it implicates an AWS-owned bucket/AMI pipeline → HARD STOP + disclose (TB9).**
**Doc evidence.** automation-ec2rescue "How it works" ("attaches the original root volume to the helper instance"); `AWSSupport-StartEC2RescueWorkflow` steps (detach/attach `/dev/sdf`, `OfflineScript`, `EC2RESCUE_OFFLINE_SYSTEM_ROOT`); `AWSSupport-ExecuteEC2Rescue` (encrypted root unsupported); `SubnetId`/`S3BucketName` params. **Severity-if-true:** High (cross-instance data exposure / caller-code against a foreign disk). **Stop condition:** another instance's disk contents readable/egressed off-box; HARD STOP if AWS-owned template/AMI implicated.

### Area 6 — Supply-chain integrity: optional signature + predictable sources (Lens Y / Lens EE / Lens T)
**Background.** The tool is fetched with `curl` from `s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz`; the `sha256` lives in the **same** bucket; GPG verification is explicitly **"(Optional)."** Modules may declare `software`/`package` pointing at external download URLs, fetched/validated as root.
**Security Concern.** Because verification is optional and the hash is same-origin, integrity reduces to "trust TLS + trust the bucket." Any compromise of the distribution (bucket object overwrite, a MITM where TLS is stripped by a proxy, or a module's `software` URL) yields **code executed as root**. The `ec2rescuelinux` bucket, signing key, and SSM package are **AWS-owned (TB9 hard stop)**; the `software`/`package` URLs in *community/third-party* modules are the attacker-reachable part.
**High-level Test Scenarios:**
- *Claim:* a module's `software`/`package` fetch runs as root without pinned hash/signature → substitute the binary. **Oracle:** how the tool "ensures that these programs are present and executable" — does it download, and does it verify? (`impl-confirm`)
- *Claim:* the install flow proceeds without GPG verification and never warns at runtime → tampered `ec2rl.tgz` runs. **Oracle:** the "(Optional)" labelling; whether the bundled build or SSM package enforces a signature. **(If the lead points at the AWS bucket/key/package itself → HARD STOP, disclose.)**
- *Claim (CONFIRMED doc-gap, Lens Y/EE):* the SSM **distributor package** for EC2Rescue is **not documented to be signature-verified** (the Distributor docs say AWS packages are "published by Amazon" but assert no cryptographic signature check), and the offline helper's CloudFormation template loads from a **wildcard bucket pattern `arn:aws:s3:::awssupport-ssm.*`** → review whether the package/template source can be substituted. **(AWS-owned → HARD STOP + disclose if confirmed against the real pipeline.)**
**Doc evidence.** ec2rl_install.html ("(Optional) Verify the signature…", same-bucket sha256), ec2rl_moduledev `software`/`package` rows, distributor.md (no signature assertion). **Severity-if-true:** High (root via supply chain) — scope the *attacker-reachable* portion (third-party module URLs, proxy/MITM) vs the AWS-owned portion (disclose). **Stop condition:** attacker-substituted code runs as root.

### Area 7 — Result upload: arbitrary-destination exfil (Lens G / Lens T) — **CONFIRMED (user-trust-dependent)**
**Background.** `./ec2rl upload --support-url="<url>"` or `--presigned-url="<url>"` POSTs the gathered log directory to a URL.
**CONFIRMED (impl).** `ec2rlcore/s3upload.py` does `requests.put(url=presigned_url, data=payload)` with **no scheme/host allowlist** — a malicious `--presigned-url`/`--support-url` exfiltrates the diagnostic archive to any endpoint. This is a **user-supplied flag**, and the EC2Rescue FAQ already warns users to review output before uploading, so it is a CLI-trust / social-engineering dependency, **not an AWS-side doc gap or a remotely-forced primitive**.
**Security Concern.** Collected diagnostics routinely contain sensitive material (syslog, env, process args, package inventories, inadvertently keys). If the URL is attacker-influenced (a social-engineered "Support URL," a wrapper, or an SSM-parameter-fed value), data is exfiltrated.
**High-level Test Scenarios:**
- *Claim:* `--support-url`/`--presigned-url` accept any scheme/host → exfil to attacker host (confirmed in code; remaining question is whether any invocation path feeds the URL from a lower-privileged source). **Oracle:** trace whether any SSM runbook / wrapper sets the upload URL from caller-controlled input.
- *Claim:* collected output includes secrets by default (no redaction) raising impact. **Oracle:** what modules gather by default.
**Doc evidence.** ec2rl_working upload section; impl: `s3upload.py`. **Severity-if-true:** Medium (sensitive-data exfil; Low as a pure self-inflicted CLI footgun). **Stop condition:** log data reaches an attacker-chosen endpoint via a lower-privileged-controlled URL.

### Area 8 — Escalation sink: root → IMDS → instance credentials (kill chain)
**Background.** Every primitive in Areas 1–6 ends in code exec as root on the instance; an instance with an attached role exposes credentials at IMDS `169.254.169.254`.
**Security Concern.** The real blast radius of a *local/remote → root* bug is not the single host — it is the **instance-profile credentials** reachable from root, which pivot into the AWS account. Rate chained leads at this end-state.
**High-level Test Scenarios (chain, don't stop at entry):**
- Parse-time deser (Area 1) **or** writable-`mod.d` planting (Area 2) **or** SSM run-command (Area 4) → root → `curl http://169.254.169.254/latest/meta-data/iam/security-credentials/` → assume the instance role in the account.
- Offline flow (Area 5): helper instance's own role + the mounted impaired disk's stored credentials → account pivot.
**Oracle.** instance-role credentials retrieved and usable (in a lab/authorized account). **Severity:** inherits the account role's privilege — up to Critical. **Stop condition / HARD STOP:** if retrieved credentials or any reached ARN belong to **AWS's own fleet/service plane** (not the customer's instance role), stop and disclose.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Parse-time object construction from a module tag | `module.py` YAML constructor / loader | docs only describe `!ec2rlcore.module.Module` as intended; no stated loader-safety guarantee |
| Non-root plants a `sudo:true` module / writable `mod.d` | module loader | no documented ownership/permission check before load |
| Symlink/TOCTOU on `/var/tmp/ec2rl` during a root run | workdir creation | `EC2RL_WORKDIR` default is a fixed predictable path (no stated 0700/ownership assert) |
| Arg metachars injected into `content` | arg→script interpolation | none documented; examples interpolate raw `$var` |
| Minimal-`ssm:*` principal → root on arbitrary instance | `AWSSupport-TroubleshootSSH` | "Required IAM permissions" block; relies on caller's own perms if no AssumeRole |
| `iam:PassRole` of a privileged `AutomationAssumeRole` | runbook role model | no documented `PassedToService`/`SourceArn` constraint |
| "Read-only by default" bypass via `FixAll`/`AllowOffline` | runbook orchestration | prose guarantee only ("By default … read-only mode") |
| Impaired disk mounted on helper in caller subnet/bucket | `AWSSupport-ExecuteEC2Rescue` | operator warned to scope `S3BucketName` bucket policy manually |
| Tampered tool / `software` URL run as root | install + `software`/`package` | GPG verification labelled "(Optional)"; same-origin sha256 |
| Diagnostic exfil via `--support-url` | `ec2rl upload` | none documented (free-form URL) |
| Root → IMDS credential theft → account pivot | instance role | out-of-band; shared-responsibility |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **The owner running `ec2rl` as their own root.** A user who already has root on their instance executing module code / reading their own IMDS is expected behaviour, **not** a vulnerability. Every in-scope local lead must start from a **lower-privileged** actor crossing to root.
- **IMDS reachability itself on a managed host** (shared-responsibility; the credential-theft *chain* is in scope only as the severity-sink of a root-exec bug, not as a standalone finding).
- **Single-instance self-DoS / `perfimpact` resource use** triggered by the owner (not cross-tenant; EC2Rescue runs one customer's instance).
- **Customer-authored modules that are insecure by the customer's own choice** (a footgun in a module the customer wrote). *In scope:* the AWS-authored bundled modules and the AWS-authored SSM runbook permission blocks.
- **Bugs in third-party forks / community module repos** (except where a `software`/`package` URL is the delivery vector into a root run).
- **The AWS-owned `ec2rescuelinux` bucket, signing key, SSM Distributor package, and `AWSSupport-*` runbook definitions** — reachable only as a HARD-STOP disclosure (TB9), never to be actively exploited here.
- **No multi-tenant cross-account surface exists in the tool itself** — so classic cross-tenant IDOR (Lens A) does not fire; the nearest analogue is cross-*instance* disk exposure in the offline flow (Area 5), which is in scope.

---

## 8. Null Hypotheses / Lenses That Did Not Fire (pages checked)

- **Lens A (cross-tenant IDOR)** — N/A. Checked moduledev, working, install, overview, and the SSM runbook pages: EC2Rescue is a single-instance self-hosted tool with no tenant/resource-by-ID service API. The cross-*instance* disk analogue is captured in Area 5 (routed to Lens V) rather than A.
- **Lens H (KMS/encryption-context)** — N/A. No customer-managed-key, encryption-context, or per-resource-key mechanism in the tool docs (install/working/moduledev read). *Doc-gap:* the offline AMI/snapshot step may touch EBS encryption — confirm if it copies across KMS keys.
- **Lens I (tagging/ABAC)** — N/A for the tool; the `--backup` AMI/snapshot side-effect uses instance creds but ABAC is not the tool's access-control mechanism.
- **Lens J (OAuth/3P)**, **Lens K (prompt injection)**, **Lens N (namespace migration)**, **Lens P (identity proofing/registration)**, **Lens W (attestation)**, **Lens BB (canonicalization between security layers)**, **Lens DD (cache-key vs authz)**, **Lens FF (JWT/OIDC)** — N/A; no corresponding mechanism in any page read (moduledev, working, install, overview, troubleshootssh). No LLM, OAuth, token, auth-layer, cache, or attestation surface in a local diagnostic tool.
- **Lens L (DoS)** — mostly out of scope (single-instance, owner-triggered). The one keep: a malicious module YAML (zip-bomb-style deeply-nested structure) could hang the parser on anyone who lists it — folded into Area 1.
- **Lens M (shared-identifier)** — minor: predictable `/var/tmp/ec2rl` paths (folded into Area 2) and the presigned upload URL (Area 7); no session/jti/MagicLink surface.
- **Lens O (audit-log evasion)** — minor/enabler: locally-run modules produce no CloudTrail; only the SSM path is audited. Relevant as an enabler for Area 4, not a standalone finding.
- **Lens Q (file upload)** — reframed: the "uploaded blob" here is the **module YAML / `content` / `software`** planted into `mod.d` — covered by Areas 1–3 and 6; and the `ec2rl upload` egress — Area 7.
- **Lens X (action-family parity)** / **Lens AA (share/revoke)** — minor: `--backup=ami` default `launchPermission` should be private; confirm the backup AMI/snapshot is not shared. Low priority.
- **Lens CC (trusted-upstream-context)** — minor: modules trust the tool-set `EC2RL_SUDO`/`EC2RL_*` env ("You do not need to implement sudo checks"); if those env vars are attacker-settable before a root run it folds into Area 2.

### Doc gaps — status after implementation/doc recon (two subagents)
1. **Loader safety** — **RESOLVED:** `module.py` uses `yaml.load(..., Loader=Loader)` (non-safe) with a controlled `!ec2rlcore.module.Module` constructor; no `!!python/object/apply` registered, but a crafted module file still executes at parse → Area 1, gated by module-planting.
2. **`mod.d` + workdir perms / symlink** — **RESOLVED (risky):** `main.py` `os.mkdir`+`chmod 0o777` on `/var/tmp/ec2rl` with no `islink`/`O_NOFOLLOW` and `EEXIST`-reuse; `moduledir.py` `os.listdir`→`get_module` with no `st_uid`/`st_mode` check → Area 2.
3. **Arg→script interpolation** — **RESOLVED (framework-safe):** verbatim `content` to tempfile, `bash` with `shell=False`, args as env vars → Area 3 downgraded to per-module bash review.
4. **Offline steps / `SubnetId`/`S3BucketName` / helper-AMI** — **RESOLVED (steps confirmed); OPEN:** helper-AMI owner and CFN template source (`arn:aws:s3:::awssupport-ssm.*` wildcard) still need resolution → Area 5 Lens-EE sub-lead (HARD-STOP-adjacent).
5. **`software`/`package` fetch + upload URL** — **PARTIAL:** `s3upload.py` confirms no URL allowlist (Area 7); the `software`/`package` *download-and-verify* behaviour still needs code confirmation → Area 6 `impl-confirm`.
6. **OPEN:** SSM distributor-package signature verification — docs assert none; confirm against the real package pipeline (AWS-owned → disclose).
7. **OPEN:** whether `AWSSupport-EC2Rescue-*` role-name prefix is creatable/collidable by a low-priv holder → Area 4 PassRole lead.

> **Hunter note:** Work Areas 1→8 in order. Areas 1–3 are confirmable in a throwaway lab instance with the public tool; Areas 4–5 require an authorized AWS account and the `AWSSupport-*` runbooks; Area 6 touches AWS-owned infra — stay on the third-party-module / proxy portion and HARD-STOP + disclose on anything implicating the `ec2rescuelinux` bucket, signing key, or SSM package. Rate every local/remote→root chain at the Area-8 (account-credential) end-state, not the entry point.
