# Troubleshoot an Unreachable EC2 Instance — Attack Research Plan

Source of leads: `docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-unreachable-instance.html`
(offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/troubleshoot-unreachable-instance.md`, 170 lines).
Cross-referenced pages: `ics-common.md` (Windows screenshots), `verify-if-automatic-recovery-occurred.md`,
`ec2-instance-reboot.md`, `Stop_Start.md`.
IAM authority: `docs/service-authorization/latest/reference/list_ec2.md` (offline, read statement-by-statement).
Managed-policy artifacts: `docs/aws-managed-policy/latest/reference/{ReadOnlyAccess,AmazonEC2ReadOnlyAccess,SecurityAudit,ViewOnlyAccess,AmazonEC2FullAccess}.md`.

**Status: documentation-derived hypotheses only. Nothing has been tested against a live AWS account.**
Live-vs-offline drift check (2026-09-14): live `.md` (167 lines) matches the offline mirror; the "Only the instance owner
can access the console output" guarantee is present in both (line 30). **No `## See also` / `agent-toolkit` prompt-injection
block on this page** in either copy (cf. [[aws-docs-see-also-injection]] — this page is clean).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- This is a **thin operational-troubleshooting page**. Its entire live attack surface is three EC2 APIs — `GetConsoleOutput`, `GetConsoleScreenshot`, `RebootInstances` — plus an AWS-service-plane-initiated *automatic instance recovery / host-failure* flow (mostly out of scope; see §7). Most catalog lenses are legitimate null hypotheses here (§8) — the leads that *do* fire are concentrated on **sensitive-data disclosure via read-grants** and **IAM condition-key / action-family enforcement gaps**.
- **The single highest-value lead is not an IDOR** (ownership is IAM-enforceable — see below) **but a confidentiality-scope gap:** these two "Read"-level APIs return the *rendered screen* and the *boot/console log* of an instance, and the AWS-managed `ReadOnlyAccess` policy grants both via an `ec2:Get*` wildcard.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the Console Screenshot Service fleet, the recovery/migration control plane, the Nitro serial subsystem), stop, preserve evidence, and flag for AWS-Security disclosure. Do **not** attempt to read another *account's* console output/screenshot beyond the minimum observation that proves a boundary broke.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes a hunter should try to produce:
1. **Read the console output or screenshot of an instance the caller does not own** (cross-account), despite the documented "Only the instance owner can access the console output" guarantee.
2. **Read the console output/screenshot of an instance the caller has no *intended* access to, from inside the same account**, by holding a broad AWS-managed "read-only" grant — proving that a "read-only" role leaks live screen contents and boot-log secrets.
3. **Reboot (or force-reboot) an instance without holding `ec2:RebootInstances`** — i.e., cause the guarded availability-impacting effect through a sibling action whose IAM control differs.
4. **Defeat a tag/attribute-based scoping policy** an admin wrote to restrict who can screenshot/console-read which instances — by exploiting an inert or wrong-binding condition key.
5. **Recover data (or observe residual state) after an automatic host-failure recovery / stop-start migration** that the customer believes is a clean re-host (data-remanence / integrity angle; see §7 for scope caveat).

---

## 2. Components, Assets, and Design

### What the page actually exposes
| Capability | API (IAM action) | Access level | What it returns / does |
|---|---|---|---|
| Get console output | `ec2:GetConsoleOutput` | **Read** | Linux: buffered kernel/console output posted around lifecycle transitions (start/stop/reboot/terminate). Windows: **last three system event-log errors**. Optional `--latest` returns **live serial console output** (Nitro-only). |
| Get instance screenshot | `ec2:GetConsoleScreenshot` | **Read** | **Base64-encoded JPG (≤100 KB) of the live/crashed screen** of a running instance. |
| Reboot instance | `ec2:RebootInstances` | **Write** | Resets an otherwise-unreachable instance (out-of-band; works even when SSH/RDP is dead). |
| (adjacent) Automatic instance recovery / host-failure re-host | *service-initiated* + `Stop_Start` / `CreateImage` flows | — | On unrecoverable host HW fault, AWS schedules a stop event (email) and may **migrate the instance to different hardware**; instance-store data is lost across stop/start. |

### Assets (what an attacker wants)
- **Screen contents** — a `GetConsoleScreenshot` JPG can show a Windows **logon screen with the account/username**, an unlocked desktop, an RDP/console session, an app displaying secrets, a recovery console, a BSOD/panic, or a "Sysprep/Getting-ready/Chkdsk" screen (`ics-common.md` enumerates exactly these). Direct confidentiality asset.
- **Boot/console log** — `GetConsoleOutput` frequently contains cloud-init/user-data echoes, service errors, tokens/paths printed to console, and (Windows) the last three system event-log errors. Secondary confidentiality asset.
- **Availability** — `RebootInstances` (and reboot-as-side-effect of `CreateImage`) is a disruption primitive.

### Design / trust model (from docs + IAM reference)
- The three APIs are **standard EC2 control-plane SigV4 calls**, each requiring the `instance*` resource type. The instance ARN is `arn:aws:ec2:<region>:<account-id>:instance/i-…` — **the account-id segment is in the ARN**, so IAM resolves the target instance to its owning account. This is the mechanism behind the "Only the instance owner can access the console output" guarantee: it is enforced by ARN-scoped IAM authorization, **not merely prose** (contrast with services where the "only owner" claim has no IAM anchor — here it does). → This is why cross-account IDOR (Lens A) is a *low-probability* lead, but the enforcement must still be confirmed for the **serial/`--latest`** path and the **screenshot** path independently (Lens X / U).
- `GetConsoleScreenshot` output is produced by an AWS-owned **Console Screenshot Service** (named verbatim in `ics-common.md`): "Console Screenshot Service returned the following." → a distinct backend fleet reading the guest's framebuffer. Any credential/identity from that fleet surfacing to the caller is a service-plane breach (hard stop).
- **No customer-supplied URL, upload, parser, translation layer, KMS key, role ARN, OAuth, or multi-tenant shared data-path** appears anywhere on this page or its adjacent pages → the injection/SSRF/PassRole/crypto families are genuine null hypotheses (§8), *after* the coverage sweep below.

```
Caller (SigV4 IAM principal)
   │  ec2:GetConsoleOutput / GetConsoleScreenshot / RebootInstances   (target = instance ARN w/ account-id)
   ▼
EC2 control plane ──(authz: instance ARN → owning account + condition keys)──► owning-account gate
   │                                                        │
   │ screenshot path                                        │ reboot path
   ▼                                                        ▼
Console Screenshot Service (AWS fleet)                 hypervisor reset (out-of-band; bypasses SG/NACL/SSH state)
   │ reads guest framebuffer → JPG
   ▼
base64 JPG back to caller
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `GetConsoleOutput` | GET (Query API) | Existing | No (Read) | External | Buffered console log; `--latest` → live serial (Nitro) | Yes | Principals with `ec2:GetConsoleOutput` on the instance ARN | **Two behaviors, one action** (buffered vs `--latest` serial) — parity untested. Doc: "Only the instance owner can access." |
| `GetConsoleScreenshot` | GET (Query API) | Existing | No (Read) | External | Base64 JPG of live screen | Yes | Principals with `ec2:GetConsoleScreenshot` on the instance ARN | **Carries `ec2:NewInstanceProfile` condition key that its siblings do NOT** (see Area 3). Returns rendered screen — direct confidentiality. |
| `RebootInstances` | POST (Query API) | Existing | **Yes (Write)** | External | Reset instance(s) | Yes | Principals with `ec2:RebootInstances` on instance ARN | **`CreateImage` reboots without this permission** (see Area 4). |
| Automatic instance recovery | n/a (service-initiated) | Existing | — | Internal (control plane) | Re-host on HW fault; `AWS_EC2_*_AUTO_RECOVERY_{SUCCESS,FAILURE}` Health events | No (customer only observes) | AWS | Verify via Health Dashboard / `StatusCheckFailed_System` CW metric. `ec2:InstanceAutoRecovery` condition key exists. |

**Undocumented/console-hidden knob to probe:** the `--latest` flag on `get-console-output` (serial console output) is documented in prose but has **no separate IAM action** — it rides `ec2:GetConsoleOutput`. Enumerate whether the AWS API model exposes any other parameter (e.g., a Windows-vs-Linux mode selector, an "all output" vs "buffered" selector) that changes *what data is returned* without changing the *authorization*.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller account A | Instance owned by account B | `GetConsoleOutput`/`GetConsoleScreenshot` with a foreign `i-…` id | **Receiving any console bytes / a non-empty JPG for an instance whose ARN account-id ≠ caller account = breach.** (Expected: `AccessDenied`/`InvalidInstanceID.NotFound`.) |
| Low-priv / "read-only" principal in account A | Any instance's screen + boot log in account A | `ec2:Get*` wildcard in `ReadOnlyAccess` grants `GetConsoleScreenshot`+`GetConsoleOutput` | **A principal whose grant is described as "read-only" retrieves a screenshot revealing on-screen credentials / a logon username, or a boot log containing secrets = confidentiality breach the artifact's own framing implies is prevented.** |
| Principal WITHOUT `ec2:RebootInstances` | Instance availability | `ec2:CreateImage` (reboots as a side effect unless `NoReboot`) | **An instance reboots under a principal that lacks `RebootInstances` = the reboot IAM control is bypassable via a sibling action.** |
| Admin's tag/attribute-scoping policy | Screenshot/console authorization | Condition key on `GetConsoleScreenshot` | **A `Deny`/`Allow` written against `ec2:NewInstanceProfile` (or a case-variant of an enum key) has no effect on screenshot calls = scoping policy fails open.** |
| Any customer surface | Console Screenshot Service fleet / recovery control plane / Nitro serial subsystem | screenshot render, `--latest` serial fetch, recovery migration | **Any AWS-fleet identity/credential/ARN surfacing to the caller = HARD STOP, service-plane breach.** |
| Instance on failed host | New host after auto-recovery / stop-start | control-plane migration | **Residual data from a prior tenant visible on the migrated-to host, or instance-store data recoverable when docs imply it is gone = remanence/integrity breach** (scope caveat §7). |

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — "Read-only" grant leaks live screen contents & boot-log secrets  ⭐ TOP / most actionable  (Lens R + U + S)
**Background.** `GetConsoleScreenshot` returns a base64 JPG of the instance's live screen; `GetConsoleOutput` returns kernel/console/boot output (Windows: last three system event-log errors). Both are IAM **Read**-level actions. `ics-common.md` confirms the screenshot can render a **logon screen exposing the username**, a recovery console, an unlocked desktop, etc.
**Security Concern.** The AWS-managed **`ReadOnlyAccess`** policy grants **`ec2:Get*`** (confirmed in `docs/aws-managed-policy/latest/reference/ReadOnlyAccess.md`), which *includes* `ec2:GetConsoleOutput` and `ec2:GetConsoleScreenshot`. Operators routinely attach `ReadOnlyAccess` to auditors, analysts, contractors, break-glass roles, and SIEM/observability integrations under the mental model that "read-only ⇒ cannot see instance internals." That model is **false**: the holder can screenshot every running instance in the account (harvesting on-screen credentials / usernames / session content) and dump boot/console logs. Because the weak breadth lives in an **AWS-authored, customer-uneditable managed policy**, it is in scope (Lens R, Tier 2) — not a customer footgun. Note the **inconsistency across AWS's own read-only artifacts**: `AmazonEC2ReadOnlyAccess` and `SecurityAudit` use `ec2:Describe*` (which does **not** include the console `Get*` actions), while account-wide `ReadOnlyAccess` uses the broader `ec2:Get*` — so the same "read-only" intent grants screen access in one policy and not another (Lens U doc-vs-artifact inconsistency).
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** A principal holding *only* `ReadOnlyAccess` can call `get-console-screenshot` on an arbitrary running instance and decode a JPG that reveals on-screen secrets / a logon username. → **Oracle:** under a scoped role holding exactly `ReadOnlyAccess` (never the over-privileged tester), `iam:SimulatePrincipalPolicy` for `ec2:GetConsoleScreenshot`/`ec2:GetConsoleOutput` returns **allowed**; escalate to a live call **only against a canary instance you own** and confirm a non-empty JPG/log is returned. → **Severity if true:** High (intra-account sensitive-data disclosure via AWS-managed wildcard; AWS-owned).
- **Claim:** The `ec2:Get*` wildcard makes `ReadOnlyAccess` grant future console-family read actions with no re-review. → **Oracle:** enumerate all `ec2:Get*` actions the reference lists as Read; confirm the console actions are in-set. → **Severity:** informational reinforcement of the above.
**Doc evidence:** page §"Instance console output" / §"Capture a screenshot"; `ics-common.md` logon-screen image; `ReadOnlyAccess.md` (`ec2:Get*`), `AmazonEC2ReadOnlyAccess.md`/`SecurityAudit.md` (`ec2:Describe*`).
**Preconditions:** ability to attach/assume a role scoped to exactly `ReadOnlyAccess`. **Cost:** minutes. **Stop condition:** confirmed a non-empty screenshot/log under the scoped role; do not iterate across instances.

### Area 2 — Cross-account console/screenshot read (documented "only the owner" guarantee)  (Lens A + U + X)
**Background.** The page asserts: *"Only the instance owner can access the console output."* The screenshot section does **not** restate this — a documentation asymmetry worth pinning.
**Security Concern.** The guarantee is (per the IAM reference) anchored in ARN-scoped authorization: the instance ARN embeds the owning account-id and all three actions require the `instance*` resource type with `ec2:InstanceID`/`ec2:ResourceTag` condition keys. So a naive cross-account read *should* fail closed. The residual risk is **enforcement parity across the variants**: (a) does the *screenshot* path enforce ownership identically to the *console-output* path (the doc only promises it for console output)? (b) does the **`--latest` serial console output** path (a different, Nitro serial subsystem) re-check ownership, or does it trust an instance-id resolved elsewhere? (c) is there any id-shape confusion (instance-id vs ARN vs a resolver) where authz checks one naming and the read acts on another?
**High-level Test Scenarios:**
- **Claim:** `GetConsoleScreenshot` on an instance-id owned by another account returns a JPG (screenshot path lacks the ownership check the console-output path has). → **Oracle:** call with a foreign canary instance-id from a second in-scope account; **any** returned image = breach. Expected refute: `InvalidInstanceID.NotFound` / `AccessDenied`. **HARD STOP** the instant a foreign screenshot is returned — capture the one image as evidence, do not enumerate.
- **Claim:** `GetConsoleOutput --latest` (serial) enforces ownership differently than the buffered mode. → **Oracle:** compare authz behavior of buffered vs `--latest` against a foreign id; a divergence (one denies, one returns data) is the finding.
- **Claim (validator-divergence oracle, Lens A variant):** the two APIs classify a foreign/nonexistent id differently (500 vs 400 vs NotFound vs AccessDenied), yielding an existence-enumeration oracle. → **Oracle:** diff status/latency for owned-valid / foreign-valid / nonexistent ids across both actions. → **Severity:** Low–Medium (enumeration), unless data is returned (then Critical).
**Doc evidence:** page line "Only the instance owner can access the console output"; `list_ec2.md` condition-key sets (identical `instance*` scoping for both console actions). **Severity if true:** cross-account screen/log read = **Critical**; enumeration oracle = Low–Medium. **Preconditions:** two in-scope accounts, a canary instance in each.

### Area 3 — `GetConsoleScreenshot`'s anomalous `ec2:NewInstanceProfile` condition key  (Lens S + U)
**Background.** In `list_ec2.md`, `GetConsoleScreenshot` lists a condition key its siblings **do not**: **`ec2:NewInstanceProfile`**. `GetConsoleOutput` and `RebootInstances` (same `instance*` resource, adjacent rows) carry `ec2:InstanceProfile` but **not** `ec2:NewInstanceProfile`. `ec2:NewInstanceProfile` is semantically for profile-*association* mutations (`AssociateIamInstanceProfile` / `ReplaceIamInstanceProfileAssociation`) — there is **no "new instance profile" input in a screenshot request** to populate it.
**Security Concern.** A condition key that cannot be populated by the request is **inert**: a policy author who writes `"Condition": {"StringEquals": {"ec2:NewInstanceProfile": "…"}}` (Allow or Deny) intending to scope who can screenshot which instances will get **fail-open** behavior — the Allow never matches (locking nobody out as intended) or, worse, a Deny silently never triggers. This is the classic Lens-S "condition key that is silently ignored / binds the wrong resource" shape. Whether the key is a genuine spurious entry in the reference or an actual (mis)wired key on the API is the open question.
**High-level Test Scenarios:**
- **Claim:** `ec2:NewInstanceProfile` has no effect on `GetConsoleScreenshot` authorization (it is inert for this action). → **Oracle:** author an identity policy allowing `ec2:GetConsoleScreenshot` only when `ec2:NewInstanceProfile` StringEquals a value; confirm via `SimulateCustomPolicy` that no realistic screenshot request context populates the key → the statement never authorizes (or a Deny never fires). Compare with `ec2:InstanceProfile`, which *is* populatable.
- **Claim (doc-vs-API integrity, Lens U):** the reference row for `GetConsoleScreenshot` is inconsistent with `GetConsoleOutput` for two read actions on the same resource that should be twins. → **Oracle:** diff the two condition-key lists (done: screenshot has `NewInstanceProfile`, output does not) and confirm against the live service-authorization page; file the inconsistency. → **Severity:** Informational/Low (AWS-owned doc/IAM-model defect; matters only if a customer builds a scoping control on the phantom key).
**Doc evidence:** `list_ec2.md` — `GetConsoleScreenshot` condition keys include `ec2:NewInstanceProfile`; `GetConsoleOutput`/`RebootInstances` do not. **Severity if true:** Low (fail-open scoping / doc-model defect). **Preconditions:** policy-simulation access.

### Area 4 — Reboot without `ec2:RebootInstances` via `CreateImage` side effect  (Lens X — action-family parity)
**Background.** The page frames reboot as the guarded availability action (`ec2:RebootInstances`, Write). But `list_ec2.md`'s `CreateImage` description states verbatim: *"This action can reboot instances as part of the image creation process, **even without RebootInstances permissions**. To prevent instance reboots during image creation, use the NoReboot parameter."*
**Security Concern.** The reboot capability — an availability-impacting effect the customer likely governs via `ec2:RebootInstances` — is reachable through `ec2:CreateImage` (default `NoReboot=false`) **without** holding `RebootInstances`. A principal granted image-creation for backup/AMI workflows can therefore reboot production instances at will, defeating any SCP/boundary that denies `RebootInstances`. This is the "sibling action achieves the guarded effect without the guarded permission" shape.
**High-level Test Scenarios:**
- **Claim:** A principal denied `ec2:RebootInstances` but allowed `ec2:CreateImage` can force a target instance to reboot by calling `create-image` with default `NoReboot`. → **Oracle:** on a canary instance you own, under a role that explicitly `Deny`s `RebootInstances` and `Allow`s `CreateImage`, call `create-image` (NoReboot omitted) and observe a reboot (state transition / uptime reset). → **Severity if true:** Medium (availability-control bypass; single-account). Note this is documented behavior — file as an enforcement/expectation gap, not a novel bug, unless it crosses accounts (it should not).
- **Adjacent (Lens O):** does the `CreateImage`-induced reboot emit the same CloudTrail/instance-event signal as an explicit `RebootInstances`, or is it attributable only to `CreateImage`? A reboot that logs as "CreateImage" is an attribution blind spot.
**Doc evidence:** `list_ec2.md` `CreateImage` description. **Severity if true:** Medium. **Preconditions:** canary instance; scoped role.

### Area 5 — Availability / disruption surface of `RebootInstances` + recovery interplay  (Lens L, lower)
**Background.** `RebootInstances` works **out-of-band** — it resets an instance whose SSH/RDP is dead, bypassing security-group/NACL/OS state. Automatic instance recovery re-hosts an instance on hardware fault.
**Security Concern.** `RebootInstances` is `instance*`-scoped and does **not** carry a `Force`/`SkipOsShutdown`-style attribute or an `ec2:Attribute`-value condition key, so there is no IAM lever to distinguish a graceful reboot from a hard reset (cf. the Stop/Start and Terminate plans' "no Force/SkipOsShutdown condition key" finding — same family). Repeated reboots, or a reboot racing an in-flight automatic recovery, is a same-account disruption primitive; it is **not** cross-tenant (a shared-fleet noisy-neighbor angle is absent from these docs).
**High-level Test Scenarios:**
- **Claim:** there is no condition key to restrict *how* a principal reboots (graceful vs forced) — the grant is all-or-nothing per instance. → **Oracle:** enumerate `RebootInstances` condition keys (done — only `instance*` scoping + tag/attribute/region keys, no reboot-behavior key); confirm no `ec2:*` key gates reboot semantics. → **Severity:** Low (least-privilege granularity gap; single-account availability).
**Doc evidence:** `list_ec2.md` `RebootInstances` condition keys. **Severity if true:** Low.

### Area 6 — Automatic instance recovery / host-failure re-host: data remanence & integrity  (data-protection lens, scope-gated)
**Background.** On unrecoverable host HW fault AWS schedules a stop event and may **migrate the instance to different hardware**; the page's recovery runbook notes **instance-store data is lost across stop/start** and must be backed up to EBS/S3 first. `verify-if-automatic-recovery-occurred.md` gives the Health-Dashboard events and the `StatusCheckFailed_System` metric.
**Security Concern.** Two angles: (a) **remanence** — when AWS migrates the instance to a *different* host, is the prior host's instance-store/local NVMe reliably wiped before the next tenant lands (the confidentiality guarantee is AWS-owned; a hunter can only observe from the guest, and the migrated-*to* host is the fresh one, so this is largely AWS's shared-responsibility side → see §7); (b) **integrity/availability expectation** — a customer who assumes automatic recovery is transparent may lose instance-store data or find a workload not auto-restarted (the page's Note warns of exactly this). This is an operational-integrity observation, not a boundary breach the hunter can force.
**High-level Test Scenarios:**
- **Claim:** instance-store contents survive an automatic recovery migration in a way the docs say they should not (or vice-versa — silently lost when the customer expected persistence). → **Oracle:** only observable by triggering/simulating a recovery on an owned canary and inspecting instance-store before/after; **cannot be forced by an attacker** → mark as monitoring/assurance, not an exploit.
**Doc evidence:** page §"Instance recovery when a host computer fails" + §"Instance appeared offline and unexpectedly rebooted"; `verify-if-automatic-recovery-occurred.md`. **Severity if true:** Low / informational (single-account). **Scope:** the cross-tenant remanence portion is AWS-service-plane — **out of scope / hard-stop** (§7).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Read another **account's** screenshot/console output | `GetConsoleScreenshot` / `GetConsoleOutput` | "Only the instance owner can access the console output" + ARN account-scoped IAM |
| Read any in-account instance's screen/log under a "read-only" grant | `ReadOnlyAccess` (`ec2:Get*`) | *(none — this is the gap)*; contrast `AmazonEC2ReadOnlyAccess`/`SecurityAudit` = `ec2:Describe*` |
| Screenshot-path ownership check weaker than console-output path | `GetConsoleScreenshot` vs `GetConsoleOutput` | shared `instance*` ARN scoping (verify parity) |
| `--latest` serial path bypasses buffered-path authz | `GetConsoleOutput --latest` (Nitro serial) | single `ec2:GetConsoleOutput` action gates both (verify) |
| Tag/attribute scoping policy fails open | `ec2:NewInstanceProfile` on `GetConsoleScreenshot` | condition-key must be populatable to enforce |
| Reboot without `RebootInstances` | `CreateImage` (NoReboot=false) | `NoReboot` parameter (opt-in, default reboots) |
| Forced vs graceful reboot indistinguishable in IAM | `RebootInstances` | *(none — no reboot-behavior condition key)* |
| Attribution: `CreateImage`-induced reboot logging | CloudTrail / instance events | CloudTrail records `CreateImage` (verify reboot is attributable) |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Cross-tenant data remanence on the underlying host** after automatic recovery / host-failure migration, and the wipe guarantee of the migrated-*from* host — this is AWS's shared-responsibility side; the guest can only observe the fresh host. **HARD STOP** if any prior-tenant data or AWS-fleet identity is observed.
- **The Console Screenshot Service fleet, the Nitro serial subsystem, and the recovery/migration control plane** — AWS service plane. Any credential/ARN from them = disclosure to AWS-Security, not a customer finding.
- **Single-account self-DoS via repeated reboot** — availability against one's own instances is out of scope (Area 5 is a least-privilege *granularity* note, not an exploit).
- **IMDS / in-guest content shown in a screenshot or console log** — the guest OS state is the customer's responsibility; the finding is the *disclosure across an IAM boundary*, not that the OS printed a secret to the console.
- **`ReadOnlyAccess` being broad in general** — only the specific, confirmed inclusion of the screen/log-reading `Get*` actions is in scope as a Lens-R artifact defect; a wholesale critique of the policy is not.
- No SSRF / injection / translation-layer / PassRole / KMS / OAuth / upload / multi-tenant-shared-data surface exists on this page (see §8).

---

## 8. Null Hypotheses / Doc Gaps
Lenses walked and recorded as non-firing, **with pages checked**:
- **Lens B/C (PassRole / credential vending):** N/A — no API on this page or in the three actions' IAM rows accepts a role ARN or vends a session. Checked: page, `list_ec2.md` rows for all three actions. *(Adjacent `CreateImage`/recovery do not pass roles here.)*
- **Lens F (translation/injection):** N/A — no customer input is parsed into a downstream language; the only "input" is an instance-id (ARN-validated) and the `--latest` flag. Checked: page, API inventory.
- **Lens G (SSRF):** N/A — no field the service dereferences/fetches; the screenshot is a framebuffer read, not a URL fetch. Checked: page, `ics-common.md`, screenshot section (no URL/media/location field).
- **Lens H/W (KMS / attestation):** N/A — no KMS key, encryption context, or attestation parameter on any action. Checked: `list_ec2.md` condition keys (only `ec2:CpuOptionsAmdSevSnp` appears as a generic instance key, unrelated to these calls' function).
- **Lens J (OAuth/3P):** N/A — no third-party linking. Checked: page.
- **Lens K (prompt injection):** N/A — no LLM/agent in the pipeline. Checked: page.
- **Lens P (identity proofing/registration):** N/A — no onboarding/verification/OTP gate. Checked: page.
- **Lens Q (upload):** N/A — no upload; the JPG is server-generated *output* (its disclosure risk is covered in Area 1, not upload-validation). Checked: page.
- **Lens Y (transport/signature):** N/A on-page — standard SigV4 EC2 API; no `http://` endpoint, no internal-hop cert claim on this page. (General EC2 transport posture is covered by sibling plans.)
- **Lens AA (share/revoke):** N/A — no share/grant/RAM/launchPermission on this page. Checked: page.

**Doc gaps to confirm on live surface first:**
1. Does `GetConsoleScreenshot` enforce instance-ownership identically to `GetConsoleOutput`? (The page promises "only owner" only for console *output*.) — confirm before running Area 2.
2. Does `GetConsoleOutput --latest` (serial) re-authorize independently of the buffered path? — confirm the serial subsystem's authz.
3. Is `ec2:NewInstanceProfile` on `GetConsoleScreenshot` a genuine (mis-wired) key or a reference artifact? — confirm against the live service-authorization JSON and via policy simulation (Area 3).

---

## Appendix — Reproduction pointers for the hunter
- Offline target: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/troubleshoot-unreachable-instance.md`
- IAM authority: `docs/service-authorization/latest/reference/list_ec2.md` — search `GetConsoleOutput` (row ~8227), `GetConsoleScreenshot` (~8233), `RebootInstances` (~9286), `CreateImage` (~5118).
- Managed policies: `docs/aws-managed-policy/latest/reference/ReadOnlyAccess.md` (`ec2:Get*` — **includes** console actions), `AmazonEC2ReadOnlyAccess.md` / `SecurityAudit.md` (`ec2:Describe*` — **excludes** them), `AmazonEC2FullAccess.md` (`ec2:*`).
- CLI: `aws ec2 get-console-output --instance-id i-… [--latest]`, `aws ec2 get-console-screenshot --instance-id i-…` (output base64 JPG), `aws ec2 reboot-instances --instance-ids i-…`, `aws ec2 create-image --instance-id i-… [--no-reboot|--reboot]`.
- Safe first oracle for every IAM lead: `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` under a role scoped to exactly the artifact — never the over-privileged tester. Escalate to a live call only against a canary instance you own.
- **Live-vs-offline drift (2026-09-14):** live `.md` == offline mirror; no `## See also` prompt-injection block on this page (unlike older instancetypes pages — [[aws-docs-see-also-injection]]).
