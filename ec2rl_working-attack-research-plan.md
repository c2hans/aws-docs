# EC2Rescue for Linux (`ec2rl`) — Attack Research Plan

Source of leads: AWS EC2 User Guide — `ec2rl_working.html` (target), `ec2rl_install.html`, `ec2rl_moduledev.html`, `Linux-Server-EC2Rescue.html`; offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`; plus the public `awslabs/aws-ec2rescue-linux` GitHub repo and the `AWSSupport-TroubleshootSSH` SSM Automation runbook referenced by the docs. Online `.md` equivalents fetched to avoid local sync issues.
Status: **documentation-derived hypotheses only; nothing tested against a live account or instance.** Where behavior is only confirmable in source/runtime it is marked **doc-gap — confirm in source/live**.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- **This is not a classic multi-tenant AWS managed service.** `ec2rl` is an open-source CLI tool the customer **downloads and runs on their own instance, frequently as root**. The dominant trust boundaries are therefore: (a) the **software supply chain** (AWS S3 artifact → customer host); (b) the **local privilege boundary** (unprivileged local user / untrusted input ↔ root-running tool); (c) **untrusted data → code-execution** inside the tool (YAML module loader + CLI-arg interpolation); (d) **the tool's egress** (`upload` to an arbitrary URL, carrying collected diagnostics that may contain secrets); and (e) the **SSM-automation confused-deputy** path (`AWSSupport-TroubleshootSSH` runs the tool as root on your behalf).
- **HARD STOP (shared-responsibility line):** the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane**, stop, preserve evidence, and flag for AWS-Security disclosure. Do not pivot into AWS-owned buckets/keys. AWS-owned infra confirmed in source/docs and therefore **off-limits to probe**: the S3 bucket `ec2rescuelinux` (install artifacts); the hardcoded upload signing endpoint **`https://30yinsv8k6.execute-api.us-east-1.amazonaws.com/prod/get-signed-url`** (confirmed in `ec2rlcore/s3upload.py`); and the SSM automation's own execution context.
- **Code-review handoff:** `ec2rl` is open source (`awslabs/aws-ec2rescue-linux`). Many leads below are best confirmed by a source review (route to `code-review-deserialization`, `code-review-command-injection`, `code-review-ssrf`, `code-review-file-read-write`) rather than a live account.

---

## 1. Pentest Objectives (boundary-breach goals, stated as concrete outcomes)

1. Obtain **code execution as root** on an instance by getting `ec2rl` (run by an admin/automation) to load an attacker-influenced YAML module or to interpolate an attacker-controlled CLI argument into a module script.
2. Achieve **local privilege escalation** (unprivileged local user → root) by abusing the predictable, root-written output tree under `/var/tmp/ec2rl/` (symlink / TOCTOU / pre-created path).
3. **Exfiltrate collected diagnostics** (which can contain credentials/secrets harvested from the host) to an attacker-controlled destination via `ec2rl upload --support-url`/`--presigned-url`, or make the tool fetch an internal/link-local target.
4. **Subvert the software supply chain:** demonstrate that the documented install trusts an artifact whose integrity/authenticity anchor is co-located with the artifact (optional signature; hash and GPG key fetched from the same bucket/channel).
5. **Confused-deputy via automation / IAM:** make the `AWSSupport-TroubleshootSSH` runbook or the `--backup` path perform an EC2/sshd change using credentials/role the caller could not use directly.

---

## 2. Components, Assets, and Design

**What it is.** `ec2rl` ("EC2Rescue for Linux") is a command-line, open-source diagnostic/remediation tool with a library of **100+ modules**. Modules are **YAML files containing a BASH or Python script plus metadata**. It is installed and run *on a Linux EC2 instance by the instance's operator*, not a hosted service.

**Interfaces / entry points (all local CLI):**
- `./ec2rl help`, `./ec2rl list`, `./ec2rl help <module>` — introspection.
- `./ec2rl run` — run all modules (some require root → run with `sudo`).
- `./ec2rl run --only-modules=<name> --<arg>=<value>` — run a specific module with arguments (e.g. `--only-modules=dig --domain=amazon.com`).
- `./ec2rl run --backup=ami | allvolumes | <vol-id>` — create AMI / multi-volume snapshots / single-volume snapshot (calls EC2 control-plane APIs).
- `./ec2rl upload --upload-directory=<path> --support-url="<url>"` / `--presigned-url="<url>"` — HTTP upload of collected results.

**Processes / runtime:** Python tool (requires Python 2.7.9+ or 3.2+); module scripts run as **bash** or **python** subprocesses. `sudo: True` modules run **as root**. A custom YAML tag `!ec2rlcore.module.Module` drives object construction via a constructor in `module.py`.

**On-disk assets / identifiers (predictable paths):**
- `EC2RL_WORKDIR` = `/var/tmp/ec2rl` (main tmp dir).
- `EC2RL_RUNDIR` = `/var/tmp/ec2rl/<date&timestamp>` (all output).
- `EC2RL_GATHEREDDIR` = `/var/tmp/ec2rl/<date&timestamp>/mod_out/gathered/`.
- Module output logs: `/var/tmp/ec2rl/<timestamp>/mod_out/run/<module>.log`.
- Module library: `mod.d/*.yaml`.
- Install artifacts (S3, global predictable bucket `ec2rescuelinux`): `ec2rl.tgz`, `ec2rl.tgz.sha256`, `ec2rl.tgz.sig`, `ec2rl.key`.

**Identity / credentials:** no service identity of its own; it runs under the **invoking OS user** (often root) and, for `--backup`, uses the **instance's AWS credentials** (instance profile / IMDS — *doc-gap, confirm*). GPG key id `2FAE2A1C` (`ec2autodiag@amazon.com`) signs the tarball.

**Where untrusted data enters and is transformed (injection seams):**
- A **YAML module file** → PyYAML custom-tag constructor → instantiated Module object → its `content` script executed. (deserialization + exec seam)
- **CLI argument values** (`--period=`, `--times=`, `--domain=`, arbitrary `--<arg>=`) → interpolated into the module's bash/python `content` (the `ps.yaml` example interpolates `$times`/`$period` **unquoted** into `seq`/`sleep`). (command/argument-injection seam)
- **`--support-url` / `--presigned-url`** → tool performs an HTTP request to that URL carrying the results archive. (egress/SSRF/exfil seam)
- **Host data collected by modules** (syslog, package logs, config) → written into `EC2RL_RUNDIR` → later uploaded. (secret-harvest → exfil seam)
- **Downloaded install artifact** from `s3.amazonaws.com/ec2rescuelinux/` → executed. (supply-chain seam)

```
                 ┌─────────────────────────────────────────────┐
  AWS S3         │  s3.amazonaws.com/ec2rescuelinux/ (AWS-owned) │
 (service plane) │  ec2rl.tgz  .sha256  .sig  ec2rl.key          │
                 └───────────────┬─────────────────────────────┘
          curl over TLS (sig verification = OPTIONAL per docs)
                                 ▼
 ┌──────────────────────── Customer EC2 instance ───────────────────────┐
 │  operator/admin OR AWSSupport-TroubleshootSSH (SSM agent, as root)    │
 │        │ ./ec2rl run [--only-modules=X --arg=val] [--backup=...]      │
 │        ▼                                                              │
 │  ec2rl.py ──loads──> mod.d/*.yaml  (!ec2rlcore.module.Module tag)     │
 │        │                     │                                        │
 │        │  CLI args ─────────▶│ interpolated into content (bash/py)    │
 │        ▼                     ▼                                        │
 │  subprocess (bash/python, root if sudo:True) ── collects host data ──┐│
 │        │                                                             ││
 │        ▼ writes                                                      ▼│
 │  /var/tmp/ec2rl/<timestamp>/... (predictable, root-written)   host secrets│
 │        │                                                              │
 │        └── ./ec2rl upload --support-url / --presigned-url ──HTTP──▶ ? │
 └───────────────────────────────────────────────────────────────────────┘
                       (EC2 control plane: CreateImage/CreateSnapshot via instance creds)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Internet / MITM / DNS spoofer | Customer host (install) | `curl` of `ec2rl.tgz` from S3; signature verify is **optional**; `.sha256`/`.sig`/`.key` fetched from the **same** bucket/channel | A tampered tarball is accepted and executed because the only integrity anchor travels the same path as the artifact (no out-of-band pin) → **code exec as installer** |
| Unprivileged local user | root-running `ec2rl` | Predictable, root-written tree under `/var/tmp/ec2rl/<timestamp>/` | A pre-created path / symlink causes root to write/follow into an attacker-chosen location → **local root** |
| Attacker-supplied YAML module | `ec2rl` python process | `!ec2rlcore.module.Module` custom-tag load; `content` executed | Loading a crafted module instantiates an arbitrary object or runs attacker code **without** `safe_load`/sandbox → **code exec** |
| Attacker-controlled CLI arg value | module bash/python `content` | `--<arg>=<value>` interpolated (unquoted in the `ps` example) | A value like `--period='1;<cmd>'` runs `<cmd>` in the module shell (root if `sudo:True`) → **command injection** |
| `ec2rl upload` caller / tricked admin | arbitrary HTTP host / internal targets | `--support-url` / `--presigned-url` taken verbatim | The results archive is sent to an attacker host, or a request egresses to `169.254.169.254`/internal → **data exfil / SSRF** |
| Collected host diagnostics | the upload destination | modules gather syslog/config → archive → upload | Secrets harvested into `EC2RL_RUNDIR` leave the host inside the upload → **secret disclosure** |
| `AWSSupport-TroubleshootSSH` (SSM/AWS Support automation) | Customer instance (sshd, root) | Runbook installs & runs `ec2rl` as root, may modify sshd/auth | The automation performs a root/sshd change via a role the invoker could not use directly, or on an instance the invoker shouldn't reach → **confused deputy** |
| `ec2rl --backup` | EC2 control plane (CreateImage/CreateSnapshot) | instance credentials (*doc-gap*) | Backup action runs with credentials/permissions the local caller could not use directly, or over-broad IAM |
| **Any of the above** | **AWS service plane** (bucket `ec2rescuelinux`, SSM automation identity) | — | **HARD STOP.** Any AWS-owned credential/ARN/bucket write = disclosure event, not a test target. |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2rl run` (all) | local CLI | Existing | Yes (runs scripts; some remediate) | Local | Run all modules | No | Local OS user (root for `sudo:True` modules) | Remediation modules change system state |
| `ec2rl run --only-modules=X --arg=v` | local CLI | Existing | Yes | Local | Run one module w/ args | No | Local OS user | **Arg → script interpolation seam** |
| `ec2rl run --backup=ami\|allvolumes\|<vol>` | local CLI → EC2 API | Existing | **Yes (AWS resources)** | Local→control-plane | Create AMI/snapshots | No (local) | Local user + **instance creds (boto3 default chain, confirmed)** | `create_image`/`create_snapshot`; no published IAM policy |
| `ec2rl upload --support-url` | local CLI → HTTP | Existing | Yes (egress) | Local→Internet | Upload results (query→hardcoded API-GW signer) | No (local) | Local user | reads query only; short-URL path follows redirects |
| `ec2rl upload --presigned-url` | local CLI → HTTP(S3) | Existing | Yes (egress) | Local→arbitrary host | PUT results tarball | No (local) | Local user | **raw `requests.put`, `allow_redirects=True`, no host allowlist (confirmed)** |
| `ec2rl list` / `help` / `help <mod>` | local CLI | Existing | No | Local | Introspection | No | Local user | Low risk |
| Custom module load (`mod.d/*.yaml`, `!ec2rlcore.module.Module`) | file → YAML loader | Existing | Yes (exec) | Local | Define/run module | No | Local user (file author) | **Deserialization seam** |
| `AWSSupport-TroubleshootSSH` (SSM Automation) | SSM API | Existing | Yes (root/sshd) | External (SSM API) → instance | Install+run `ec2rl`, fix SSH | Yes (via SSM API w/ IAM) | SSM-authorized principals | **Confused-deputy / automation seam** — detail from subagent |
| Install fetch `s3.amazonaws.com/ec2rescuelinux/*` | HTTPS GET | Existing | No | External | Download tool+hash+sig+key | Yes | Anyone | **Supply-chain seam**; AWS-owned bucket = service plane |

**Undocumented/under-surfaced knobs to enumerate (source review):** full `--<arg>` space a module can consume (beyond `--period`/`--times`/`--domain`/`--backup`/`--perfimpact`); whether `--only-modules` / a module-path flag accepts an **arbitrary filesystem path** to a YAML file; `--perfimpact=true` gate semantics; any flag that changes `EC2RL_WORKDIR`/output path (→ feeds the tmp-path lead).

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — YAML module deserialization & script execution (Lens F / deserialization) — **PRIORITY** — *source-confirmed loader*

**Background.** Modules are YAML documents tagged `!ec2rlcore.module.Module`; the docs state the tag "tells the YAML parser which constructor to call when creating the object from the data stream" (constructor in `module.py`). The module's `content` is literal BASH/Python that the tool executes, possibly as root.

**Source-confirmed mechanism (`ec2rlcore/module.py`).** The loader is **`yaml.load(config_file, Loader=Loader)` — NOT `yaml.safe_load`** — where `Loader` is `yaml.CLoader`/`yaml.Loader`, and a custom constructor is registered: `yaml.add_constructor("!ec2rlcore.module.Module", module_constructor, Loader=Loader)`, whose `module_constructor` does `loader.construct_mapping(node, deep=True)` then `new_module.__init__(**values)`. Modules are enumerated **only** from `mod.d` under `CALLPATH` (`ec2rlcore/main.py`: `ModuleDir("{}/mod.d".format(...CALLPATH))`; `moduledir.py` `os.listdir` → `get_module()` for each `.yaml`). **No CLI flag to load a YAML module from an arbitrary path was found** — `--only-modules` only *selects by name* among files already present. (doc-gap: confirm no `--module-dir` override exists.)

**Security Concern.** `yaml.load` with a custom `Loader` is PyYAML's object-construction path (the generally-unsafe API family). The registered custom tag is the intended one, but using `yaml.load` rather than `safe_load` is a defect-prone posture. More importantly, because `content` is executed **by design** and modules run from a fixed on-disk directory, **the realistic attack is getting an attacker-controlled `.yaml` into `mod.d`** — via the supply-chain path (Area 5), an insecure/ world-writable install dir, or shared-tmp — after which the tool (frequently root, or the SSM runbook) parses and executes it.

**High-level Test Scenarios (falsifiable):**
- **Claim:** the loader honours object-construction tags → a module exercising the `yaml.load` path (custom-tag or `!!python/...` gadget, depending on loader strictness) runs code at parse time. **Oracle:** source confirms `yaml.load(...Loader=Loader)` (✔ confirmed); test a crafted module to see what tag classes the registered `Loader` accepts beyond `!ec2rlcore.module.Module`. Severity: **High (root RCE)**.
- **Claim:** `mod.d` (or the unpacked install tree) is attacker-writable / world-writable after the documented `tar -xzvf` extraction, letting a local user plant a module an admin/SSM later runs. **Oracle:** inspect post-extraction permissions of the install dir and `mod.d`; drop a benign-marker module and confirm it is picked up by `./ec2rl list`/`run`. **Confirm live** (extraction umask). Severity: **High** (local→root).
- **Claim:** `content` executes with no sandbox, inheriting root when `sudo:True`. **Oracle:** `ps.yaml` runs arbitrary bash as the invoking (root) user. Severity: **High**.

**Doc evidence:** `ec2rl_moduledev.html` (attribute table — `content`, `language: bash|python`, `sudo`; `!ec2rlcore.module.Module` → `module.py`; `ps.yaml`); source: `ec2rlcore/module.py`, `main.py`, `moduledir.py`. **Severity-if-true: High (root code execution / unsafe deserialization posture).**

### Area 2 — CLI-argument → module-script command injection (Lens F variant) — **PRIORITY** — *source-confirmed data flow*

**Background.** `./ec2rl run --only-modules=X --<arg>=<value>` passes argument values into module scripts. The shipped `ps.yaml` example interpolates `$times` and `$period` **unquoted** into `for i in $(seq 1 $times); do ps auxww; sleep $period; done`. The `dig` module takes `--domain=amazon.com` into a dig command.

**Source-confirmed mechanism (`ec2rlcore/options.py` + `module.py`).** argparse accepts **any** `--key=value` dynamically (`for dynamic_arg in unknown_args_list: ... self.parser.add_argument(dynamic_arg, ...)`); the only regex check (`re.match("[a-zA-Z0-9]", ...)`) applies to bare flag *names*, **never to the value after `=`**. The raw value is stored in `global_args`/`per_module_args`, then in `Module.__call__` copied verbatim into the subprocess environment: `envlist[option] = optionvalue` → `subprocess.check_output(command, env=envlist, ...)`. The subprocess uses an argv list (`shell=False`), so the injection is **not** at the Python layer — it is **inside the module's own bash script**, which interpolates the env var **unquoted** (`$(seq 1 $times)`, `dig $domain`, `sleep $period`). **No value sanitization/allowlist anywhere.**

**Security Concern.** Any caller who can invoke `ec2rl run --only-modules=… --<arg>=<value>` injects shell commands into the module context — **root for `sudo:True` modules**, and **root via the SSM runbook** (Area 6). Delivery does not require code changes, only control of a command line / automation parameter.

**High-level Test Scenarios:**
- **Claim:** `--period`/`--times` (or any arg) is interpolated unquoted → e.g. `--period='1; id > /tmp/pwn'` or `` --domain='`id`' `` executes the injected command. **Oracle (confirmed in source; validate live):** the injected command's side effect appears in output/filesystem. Severity: **High (root)** when the target module is `sudo:True`, else invoking-user level.
- **Claim:** `--domain=` in the `dig` module reaches the shell un-separated → shell metacharacters execute. **Oracle:** command side effect / malformed `dig` error reveals interpolation. Severity: **High/Medium**.
- **Claim:** there is **no allowlist/validation** on arbitrary `--<arg>=` values (✔ confirmed). **Oracle:** `options.py` dynamic-arg handling → `envlist`. Severity: **High**.

**Doc evidence:** `ec2rl_working.html` (`--only-modules`, `--domain=amazon.com`); `ec2rl_moduledev.html` (`ps.yaml` unquoted `$times`/`$period`; `required`/`optional`; env-var table); source: `ec2rlcore/options.py`, `module.py`. **Severity-if-true: High (command injection, root).**

### Area 3 — Local privilege escalation via predictable root-written output tree (Lens — local tmp/TOCTOU)

**Background.** Output always lands under the **fixed, world-known** base `/var/tmp/ec2rl/` with a `<date&timestamp>` subdir; `/var/tmp` is a world-writable sticky directory. When `ec2rl` runs as root (common; required by many modules and by the SSM runbook), it creates and writes files there.

**Source-confirmed mechanism (`ec2rlcore/main.py`).** `os.mkdir(WORKDIR)` then **`os.chmod(WORKDIR, 0o777)`** on `/var/tmp/ec2rl` — the comment says this is *intentional* ("read/writeable by all users... prevents permission issues when executed by root/sudo then a regular user"). The per-run `RUNDIR` (`WORKDIR/<ISO-timestamp>`) is `0o700`, but the **parent is world-writable** and no sticky bit is set by the code (it relies on `/var/tmp`'s own sticky bit, if present).

**Security Concern.** A **world-writable parent directory created/reused by root at a fixed, predictable path** is the classic precondition for symlink/TOCTOU local attacks. If any file creation under the tree (or reuse of a pre-existing `WORKDIR`) lacks `O_NOFOLLOW`/ownership checks, a local unprivileged user can pre-create or symlink paths so root writes/overwrites attacker-chosen files (`/etc/cron.d/*`, `authorized_keys`) → **local root**. Exploitability hinges on whether `/var/tmp` carries the sticky bit on the target OS and on the exact file-open flags.

**High-level Test Scenarios:**
- **Claim:** reuse of an attacker-pre-created/world-writable `/var/tmp/ec2rl` lets a non-root user influence what root writes (symlink/TOCTOU). **Oracle:** pre-create the dir or plant symlinks; observe root following them. **Confirm live** (sticky-bit + open flags). Severity: **High (LPE)**.
- **Claim:** gathered logs are readable by other local users before upload. **Oracle:** inspect mode bits under `mod_out/` (parent is 0777; RUNDIR 0700 — confirm leaf-file modes). Severity: **Medium (local info-disclosure)**.

**Doc evidence:** `ec2rl_moduledev.html` env-var table (fixed `/var/tmp/ec2rl` paths); source: `ec2rlcore/main.py` (`chmod 0o777` WORKDIR, `0o700` RUNDIR). **Severity-if-true: High (local root).**

### Area 4 — `upload` SSRF / arbitrary-destination data exfiltration (Lens G)

**Background.** `./ec2rl upload` tars `--upload-directory` (recursive tar of the full `/var/tmp/ec2rl/<timestamp>/` run output) and sends it to a URL given in `--support-url` or `--presigned-url`. USAGE.md itself warns the directory *"could contain sensitive data depending on modules run!"* — a confirmed carrier for harvested secrets.

**Source-confirmed mechanism (`ec2rlcore/s3upload.py`).** For `--presigned-url`: the user-supplied URL is PUT to **directly** — `requests.put(url=presigned_url, data=payload)` — with **no scheme/host allowlist, no private/link-local block, and default `allow_redirects=True`**. For `--support-url`: the code reads only the **query string** (`parse_qs`) and POSTs a signing request to the **hardcoded AWS endpoint** `30yinsv8k6.execute-api.us-east-1.amazonaws.com/prod/get-signed-url`; if the value has no query string it is treated as a short URL and resolved via `urlopen(...).geturl()` (**follows redirects**). The host of `--support-url`/`--presigned-url` is never validated against `amazonaws.com`.

**Security Concern.** `--presigned-url` is a documentation-confirmed **arbitrary-destination PUT of the full results tarball** with redirect-following and no SSRF guardrails — a data-exfiltration / SSRF-shaped primitive gated only by who controls the URL argument (a tricked admin, a malicious automation parameter, or an attacker who already has local exec from Areas 1–3 chaining to exfil).

**High-level Test Scenarios:**
- **Claim:** `--presigned-url` PUTs the full archive to an arbitrary attacker host (✔ confirmed in source). **Oracle:** point it at a controlled listener; observe the PUT with tarball bytes. Severity: **Medium–High (data exfil of harvested secrets)**.
- **Claim:** no block on link-local/private targets; `--presigned-url=http://169.254.169.254/...` egresses. **Oracle:** observe request. *Note:* reaching the tool's **own** IMDS is self-host (out of scope as a finding), but the unguarded-egress primitive is recorded. Severity: **Low–Medium**.
- **Claim:** `upload` follows HTTP redirects past any host expectation (✔ default `allow_redirects=True`; short-URL path uses `urlopen().geturl()`). **Oracle:** supply a redirecting URL; observe the followed hop. Severity: **Medium**.

**Doc evidence:** `ec2rl_working.html` upload section; `docs/USAGE.md` sensitive-data warning; source: `ec2rlcore/s3upload.py`. **Severity-if-true: Medium–High (exfil); SSRF primitive.** *(The hardcoded signing endpoint is AWS service plane — do not probe it; HARD STOP.)*

### Area 5 — Software supply-chain / install integrity (Lens Y transport + Lens EE predictable-name + Lens R artifact)

**Background.** Install = `curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz`, then unpack and run. Signature verification is explicitly **"(Optional)"**, and the integrity/authenticity material — `ec2rl.tgz.sha256`, `ec2rl.tgz.sig`, and even the GPG public key `ec2rl.key` — is downloaded from the **same bucket/channel** as the tarball. The bucket name `ec2rescuelinux` is a **global, predictable S3 name**.

**Security Concern.** The documented happy path trusts the artifact with no out-of-band anchor: an adversary who can tamper with the delivery (compromised mirror/proxy, TLS-stripping/MITM, or a cache) can replace the tarball **and** the `.sha256`/`.sig`/`.key` together, defeating the verification the docs already mark optional. The GitHub "bundled build" is a second, differently-trusted channel. (Bucket `ec2rescuelinux` is **AWS-owned → service plane → do not probe the bucket; this is a *doc/process* weakness to report, not a bucket to attack.**)

**High-level Test Scenarios (analysis/reporting, not live attack on AWS infra):**
- **Claim:** The docs present signature verification as optional and co-locate the hash, signature, and GPG key with the artifact, so integrity verification provides no MITM protection in the documented flow. **Oracle:** the four URLs share one origin; the verify step is under an "(Optional)" heading. Severity: **Low–Informational (AWS-authored doc/process weakness; Lens R/U-style — reportable because customers copy this flow verbatim)**.
- **Claim:** nothing pins TLS or forbids plaintext for the install fetch beyond default `https`. **Oracle:** doc review. Severity: **Informational**.
- **Null/HARD-STOP note:** do **not** attempt to claim/poison the `ec2rescuelinux` bucket or any AWS-owned name — that crosses the service plane.

**Doc evidence:** `ec2rl_install.html` — standard-build steps, "(Optional) Verify the signature", key id `2FAE2A1C`. **Severity-if-true: Low–Informational.**

### Area 6 — `--backup` IAM / confused-deputy + SSM-automation (`AWSSupport-TroubleshootSSH`) (Lens B / R / CC)

**Background.** `--backup=ami|allvolumes|<vol-id>` creates AMIs/snapshots via EC2 control-plane APIs, presumably using the instance's credentials. Separately, the `AWSSupport-TroubleshootSSH` SSM Automation runbook **installs and runs `ec2rl` as root** to "check or attempt to fix common issues that prevent an SSH connection" — i.e. it modifies sshd/auth state on your behalf.

**Source/doc-confirmed mechanism.** `ec2rlcore/backup.py` calls `boto3.client("ec2").create_image(...)` / `create_snapshot(...)` using boto3's **default credential chain** (instance profile / IMDS on EC2; raises `BackupNoCredsError` when absent). **No AWS-published scoped IAM policy for `ec2rl` backup exists** — required actions (`ec2:CreateImage`, `ec2:CreateSnapshot`, and the `Describe*` reads) are inferable from code only (doc-gap). The `AWSSupport-TroubleshootSSH` runbook (per its docs) **operates read-only by default**, installs EC2Rescue via `AWS-ConfigureAWSPackage` and runs it via `aws:runCommand` (SSM Agent → root-level), and in **offline** mode *"stops the instance and creates an AMI before attempting any operations"* (chains to `AWSSupport-ExecuteEC2Rescue` → ties to the backup/IAM surface). IAM: *"If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook"* (optional `AutomationAssumeRole`); AWS itself flags the log-upload S3 bucket as a confused-deputy/exfil risk (*"Make sure the bucket policy does not grant unnecessary read/write permissions…"*). No cross-account parameter is documented on this runbook page.

**Security Concern.**
- *Backup/IAM:* anyone with local exec (incl. via Areas 1/2) can call `create_image`/`create_snapshot` with the instance's credentials — creating an AMI/snapshot of the instance's volumes that the local attacker can then share out-of-account = **data exfiltration via the control plane**. Over-broad instance-profile permissions widen the blast radius; the absence of a published least-privilege policy makes over-provisioning likely.
- *Automation confused-deputy:* because the runbook runs `ec2rl` **as root via Run Command**, it is the highest-value **delivery vector for Areas 1–3** (a crafted module planted in `mod.d`, or an injected `--<arg>` value, reaching the runbook = root RCE in the SSM/automation context → potential service-plane adjacency → **HARD STOP the moment an AWS identity appears**).

**High-level Test Scenarios:**
- **Claim:** `ec2rl --backup` runs with over-broad instance-profile EC2 permissions and no published least-privilege policy (✔ no policy published; actions code-inferred). **Oracle:** enumerate the exact calls (`backup.py`); check the instance profile's actual grant. Severity: **Medium (local attacker leverages instance creds → snapshot/AMI exfil)**.
- **Claim:** the runbook's default-role-is-caller behavior or its `AWSSupport-ExecuteEC2Rescue` offline chain lets a caller reach instances / pass permissions they shouldn't. **Oracle:** runbook params, `AutomationAssumeRole`, the `ExecuteEC2Rescue` page (cross-account doc-gap). Severity: **High if cross-account**.
- **Chain:** module-in-`mod.d` or `--arg` injection (Area 1/2) delivered through the runbook → root RCE as the automation. Severity: rated at **chain end (High)**.

**Doc evidence:** `ec2rl_working.html` (`--backup`); `Linux-Server-EC2Rescue.html` + `automation-awssupport-troubleshootssh` runbook doc; source: `ec2rlcore/backup.py`, `main.py`. **Severity-if-true: Medium–High.**

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Unsafe YAML load → RCE at parse | Module loader (`module.py`, `!ec2rlcore.module.Module`) | Custom-tag constructor (should be `safe_load` + allowlisted tag only) |
| Attacker module in search path run by root | `mod.d/` / `--only-modules` | File placement / path trust (unstated) |
| CLI arg → shell injection | Module `content` arg interpolation | Arg validation / argv separation (unstated; `ps.yaml` is unquoted) |
| Symlink/TOCTOU on `/var/tmp/ec2rl` as root | Output tree | Safe file creation (O_NOFOLLOW, ownership check) — unstated |
| Collected-secret exfil to arbitrary URL | `ec2rl upload` | `--support-url`/`--presigned-url` host allowlist — unstated |
| SSRF to link-local/internal | `ec2rl upload` | Private-range block / redirect policy — unstated |
| Tampered install accepted | Install flow | GPG signature (**optional**) + sha256 (same-channel) |
| Over-broad backup IAM / cross-account automation | `--backup`, `AWSSupport-TroubleshootSSH` | Least-privilege policy / runbook IAM — **doc-gap** |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **IMDS on the instance itself** (`169.254.169.254`) reached from a tool running **on that same instance** — the tool already runs with host privileges; this is self-host, not a boundary breach. (An SSRF *primitive* in `upload` is still worth noting, but reaching your own IMDS is not a finding.)
- **A user steering their own tool** — an admin who intentionally runs a dangerous module/arg on their own instance is operating within their own trust zone. The in-scope shapes are where a **lower-privileged or remote/automation actor** influences what root runs.
- **Customer-authored modules** that the customer writes insecurely = customer footgun (out of scope). **AWS-shipped** modules / sample YAML / the documented install flow **are** in scope (AWS-authored, copied verbatim).
- **AWS-owned infrastructure:** the `ec2rescuelinux` S3 bucket and the SSM automation's own identity are the **service plane** — analyze the *documented process*, never probe/poison the bucket or assume the automation's role. HARD STOP on any AWS credential/ARN.
- Bugs in third-party reference material or the general GitHub ecosystem beyond the shipped tool.
- Single-tenant self-DoS (e.g. a `perfimpact` module slowing your own box).

---

## 8. Null hypotheses / doc gaps (pages checked)

- **Lens A/V/D (cross-tenant / network segmentation / data→control-plane):** **N/A.** Pages read: `ec2rl.html`(404 online)/`Linux-Server-EC2Rescue.html`, `ec2rl_working.html`, `ec2rl_install.html`, `ec2rl_moduledev.html`. `ec2rl` is a single-host CLI tool with **no multi-tenant fleet, no service account, no ENIs/VPC/control plane of its own** — there is no cross-tenant or network-isolation surface to breach. (True null, not an unexamined surface.)
- **Lens H/W/DD/FF/BB/CC-caching/token-validation:** **N/A** — no KMS/attestation gate, no caching layer, no JWT/OIDC token validation, no multi-parser HTTP routing in the tool. (CC *does* partially fire via the SSM-automation confused-deputy — see Area 6.)
- **Lens K (prompt injection):** **N/A** — no LLM/agent in the pipeline.
- **Lens P/Q (registration/upload-of-rich-content):** **N/A** for the tool itself (no onboarding, no server-side rendering of uploads); the `upload` path is covered under Area 4.
- **Source-confirmed by deep-dive (were doc-gaps, now closed):**
  1. Loader is `yaml.load(Loader=Loader)` not `safe_load`; modules load only from `mod.d` — **Area 1**.
  2. Arg→env→unquoted-bash flow with no value validation — **Area 2**.
  3. `WORKDIR /var/tmp/ec2rl` is `chmod 0o777`; `RUNDIR` `0o700` — **Area 3**.
  4. `--presigned-url` → raw `requests.put`, `allow_redirects=True`, no host allowlist; `--support-url` → hardcoded API-GW signer — **Area 4**.
  5. `--backup` uses boto3 default cred chain (`create_image`/`create_snapshot`) — **Area 6**.
- **Remaining doc-gaps to resolve before/with live hunting:**
  1. Whether any `--module-dir`/path override exists to load a YAML module from an arbitrary path (Area 1).
  2. Post-`tar -xzvf` permissions of the install tree and `mod.d`; leaf-file modes under `mod_out/`; whether `/var/tmp` carries the sticky bit + exact open flags (Areas 1, 3).
  3. Which shipped modules are `sudo:True` (root reach of injection) (Areas 1, 2).
  4. No AWS-published least-privilege IAM policy for `--backup`; the instance profile's actual grant (Area 6).
  5. `AWSSupport-ExecuteEC2Rescue` cross-account/assume-role parameters (Area 6).

---

*Plan generated by the `security-questionbuilder` skill from AWS documentation only. No live system was touched. Confirm the doc-gap items by source review of `awslabs/aws-ec2rescue-linux` (route: `code-review-deserialization`, `code-review-command-injection`, `code-review-file-read-write`, `code-review-ssrf`) before any authorized live validation.*
