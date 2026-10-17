# EC2 Instance Stop / Force-Stop (Troubleshoot stuck `stopping`) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesStopping.html` (+ `.md`), and the adjacent pages it links/implies: `instance-stop-methods`, `Stop_Start`, `ec2-stop-protection`, `instance-terminate-methods`, `TroubleshootingInstancesShuttingDown`, `monitoring-system-instance-status-check`, `ec2-instance-lifecycle`, `terminating-instances`; API refs `API_StopInstances`, `API_AttachVolume`, `API_DetachVolume`, `API_CreateVolume`, `API_CreateSnapshot`, `API_CreateImage`, `API_ModifyInstanceAttribute`; Service Authorization Reference (EC2 action table, recovered via PDF/archive because the live page is a JS SPA); AWS-managed policy `AmazonEC2FullAccess`.
Status: **documentation-derived hypotheses only; nothing tested against a live account.** Mirror at `/work/aws-docs/docs/AWSEC2/latest/UserGuide` is missing the newest pages — online `.md` variants were used.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Most of this surface is **customer-plane IAM / data-integrity / least-privilege** rather than cross-tenant. The two highest-yield directions are (a) the **IAM granularity gap** around the *new* `SkipOsShutdown`/`Force` flags, and (b) the **in-account root-volume-swap** primitive the troubleshooting doc itself teaches.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the EBS/EC2 fleet decrypt identity, a shared Nitro host, cross-tenant data from a reclaimed host), stop, preserve evidence, flag for AWS-Security disclosure. Do **not** destroy data on, or force-stop, any instance you do not own in a test account.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Prove an admin cannot bound the data-destructive stop variants.** Show that any principal holding plain `ec2:StopInstances` can issue `Force` and/or `SkipOsShutdown` (irreversible cache-flush bypass → data loss) and that **no IAM condition key exists to deny those variants while allowing a normal stop.**
2. **Prove the integrity-interruption primitive.** Show that `SkipOsShutdown`/`Force` can abort an *in-progress* graceful stop (or hit a `running`/`pending` instance that is not stuck at all), poisoning the state-transition session so a subsequent clean stop still skips the flush → forced data loss/corruption on a healthy instance.
3. **Prove / refute the stop-protection-vs-force interaction.** Determine whether `--force`/`--skip-os-shutdown` honors `DisableApiStop` / `DisableApiTermination`, and enumerate the documented protection *exclusions* (scheduled events, Auto Scaling, OS-initiated shutdown) that a stop still passes through.
4. **Prove the in-account root-volume-swap read primitive.** Show that a principal with the shipped `AmazonEC2FullAccess` policy can `CreateSnapshot`→`CreateVolume`→`AttachVolume (as root)`→`StartInstances` against *another team's* instance/volume in the same account and read its root filesystem — with no guardrail in AWS's own baseline policy.
5. **Prove the shared/public-snapshot ingest + crash-consistent AMI leak paths**, and the status-check misread that bakes a compromised OS into a "clean" replacement AMI.
6. **Characterise detection gaps:** force/skip-shutdown stops carry no distinct CloudTrail `eventName`.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 control-plane API (SigV4) + console + CLI/PowerShell. Core actions on this page: `StopInstances` (flags `Force`, `SkipOsShutdown`, `Hibernate`, `DryRun`), `StartInstances`, `TerminateInstances`, `CreateImage`, `RunInstances`, `CreateSnapshot`, `CreateVolume`, `DetachVolume`, `AttachVolume`, `ModifyInstanceAttribute` (`DisableApiStop`/`DisableApiTermination`).

**What is a "resource" and its identifier shape.** `instance` ARN (id `i-...`), `volume` (`vol-...`), `snapshot` (`snap-...`), `image`/AMI (`ami-...`). All are account-scoped; EBS volumes & instances are **not** cross-account-shareable — only **snapshots and AMIs** are (public or per-account).

**Identity / privilege.** IAM principals via SigV4. Resource-level permission for the stop/attach actions is on the `instance*` (and `volume*`) ARN; the relevant data-destruction/data-read behavior is **not** separately permissioned.

**State machine (the heart of this page).**
```
                 StopInstances(Force=false, SkipOsShutdown=false)  → graceful OS shutdown (flush caches+metadata)
  running ──────▶ stopping ───────────────────────────────────────▶ stopped
     │  │           │
     │  │           └── stuck (underlying host/hw fault; failed SYSTEM status check)
     │  │                 │
     │  │                 └── StopInstances(Force=true) ───────────▶ stopped   [may skip flush; "post-stop writes
     │  │                                                                        to EBS volumes or other shared resources"]
     │  └── StopInstances(SkipOsShutdown=true)  ─ unconditional flush bypass ─▶ stopped  [NEW 2025-07-23; irreversible
     │                                                                                     for the current transition session]
     └── (CLI only) Force/Skip accepted from pending|running, NOT just stopping   ← console hides this
```

**Replacement / recovery pipeline the page teaches (second data-plane surface).**
```
stuck instance ──CreateImage(--no-reboot, crash-consistent)──▶ AMI ──RunInstances──▶ new instance
      │
      └─(alternate)─ CreateSnapshot(root vol) ─▶ CreateVolume ─▶ [DetachVolume root of a fresh instance]
                       ─▶ AttachVolume(recovered vol AS ROOT /dev/sda1) ─▶ StartInstances ─▶ read root fs
```

**[NEW] marker.** `SkipOsShutdown` for both stop **and** terminate launched **2025-07-23** (DocumentHistory). This is the least-reviewed surface on the page → Step-5 priority #1.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| IAM principal with `ec2:StopInstances` | integrity of an instance's filesystem / in-flight IO | `Force` / `SkipOsShutdown` flags | A data-destructive stop (flush bypass) executes with **no IAM condition able to deny only the destructive variants** → granularity gap confirmed. |
| Low-priv / wrong team principal in account A | **another team's** instance/volume in account A | `AmazonEC2FullAccess` (`ec2:*`, no Condition) → snapshot/attach-root chain | Booting or reading another workload's root filesystem (secrets/keys/config) under the attacker's control. |
| Caller controlling a `SnapshotId` | source account's data baked in a **shared/public snapshot or AMI** | `CreateVolume`/`RunInstances` from a shared/public snapshot/AMI | Reading cleartext data/secrets the source account failed to scrub; or re-sharing a derivative AMI. |
| EBS data-key decrypt path | customer CMK | `AttachVolume` → EBS service calls `kms:Decrypt` under the key policy | Decrypt succeeds under a key the *caller* lacks `kms:Decrypt` for because the key policy delegates to the EBS/EC2 service (cross-service reachability). |
| Any customer surface | **AWS service plane / shared Nitro host** | stuck-stop host fault, host reclaim, "post-stop writes to … other shared resources" | **HARD STOP** — any cross-tenant data, shared-host reach, or fleet identity. |

---

## 4. API / Interface Inventory

| Name | Mutating | Internet-callable | Authorized callers | Flags / notable params | Notes → lens |
|---|---|---|---|---|---|
| `StopInstances` | Yes | Yes | holder of `ec2:StopInstances` on `instance*` | `Force`, `SkipOsShutdown` **[NEW 2025-07-23]**, `Hibernate`, `DryRun` | No condition key gates Force/Skip. One `eventName` for all variants. → **S, U, X, O** |
| `TerminateInstances` | Yes | Yes | `ec2:TerminateInstances` | `Force`, `SkipOsShutdown` | "You can't terminate if termination protection is on" sits above the force-terminate method. → **U** |
| `ModifyInstanceAttribute` | Yes | Yes | `ec2:ModifyInstanceAttribute` | `DisableApiStop`, `DisableApiTermination` | Eventual-consistency on the protection attribute → race window. → **U** |
| `AttachVolume` | Yes | Yes | `ec2:AttachVolume` on `instance*`+`volume*` | `Device` = free-text (no root-device block) | Same-AZ required; **no cross-account path** (structural). → **A, X, H** |
| `DetachVolume` | Yes | Yes | `ec2:DetachVolume` | `Force` (detach) | → **A** |
| `CreateVolume` | Yes | Yes | `ec2:CreateVolume` | `SnapshotId`, `KmsKeyId`; condition key **`ec2:ParentSnapshot` exists but AWS policies don't use it** | Accepts shared/public snapshot. → **A, T, H** |
| `CreateSnapshot` | Yes | Yes | `ec2:CreateSnapshot` | captures full on-disk data | → **A, Q, T** |
| `CreateImage` | Yes | Yes | `ec2:CreateImage` | `NoReboot` (crash-consistent) | AWS's own recovery flow uses `--no-reboot`. → **Q, U** |
| `RunInstances` | Yes | Yes | `ec2:RunInstances` | launch from any readable AMI | ingest shared/public AMI. → **A, EE** |
| Console "Force stop instance" | Yes | Yes (console) | same IAM | **only shown when state == `stopping`** | Capability delta vs CLI/API. → **X, U** |

**Console-hidden knob (Step-3 sweep):** CLI/SDK accept `Force`/`SkipOsShutdown` from `pending`|`running`|`stopping`; the console only exposes "Force stop" in `stopping`. Documented (troubleshooting sub-page) but invisible from the console UI and absent from the main API-ref parameter description — the most-permissive path is the least-visible one.

---

## 5. Recommended Areas of Focus

### Area 1 — [NEW, PRIORITY] IAM granularity gap: no condition key can deny `Force` / `SkipOsShutdown` (Lens S / R / U)
**Background.** `SkipOsShutdown` (launched 2025-07-23) and `Force` are Boolean flags on `StopInstances`/`TerminateInstances`. Both bypass the graceful OS shutdown and, per AWS's own text, "might result in **data loss or corruption** … memory contents not flushed to disk … loss of in-flight IOs … skipped shutdown scripts."
**Security Concern.** The complete condition-key set for `ec2:StopInstances` is: `aws:ResourceTag/*`, `ec2:AvailabilityZone(Id)`, `ec2:CpuOptionsAmdSevSnp`, `ec2:EbsOptimized`, `ec2:InstanceAutoRecovery`, `ec2:InstanceBandwidthWeighting`, `ec2:InstanceID`, `ec2:InstanceMarketType`, `ec2:InstanceMetadataTags`, `ec2:InstanceProfile`, `ec2:InstanceType`, `ec2:ManagedResourceOperator`, `ec2:MetadataHttp*`, `ec2:PlacementGroup`, `ec2:Region`, `ec2:ResourceTag/*`, `ec2:RootDeviceType`, `ec2:Tenancy`. **Every key scopes *which instance*, not *how* it is stopped.** There is no `ec2:Force` / `ec2:SkipOsShutdown` condition key and no separate action. An admin can only allow-all-stops or deny-all-stops; they cannot grant "normal stop but never the data-destructive bypass."
**High-level Test Scenarios (falsifiable claims).**
- *Claim:* A principal granted only `ec2:StopInstances` (no extra permission) can set `SkipOsShutdown=true` and `Force=true` with no additional authz. → *Oracle:* `aws ec2 stop-instances --skip-os-shutdown --force` returns 200 under a scoped role holding exactly `ec2:StopInstances`; `DryRun` returns `DryRunOperation` (caller-IAM only — **not** a destructive confirmation). *Severity-if-true:* Medium (AWS-owned least-privilege granularity gap; a routine "operators may stop instances" grant silently includes an irreversible data-destruction capability).
- *Claim:* No `Condition` can be written that permits a normal stop and denies the skip/force variant. → *Oracle:* `iam:SimulateCustomPolicy` (safe, no resources touched) with every candidate key; show none keys on the flags.
**Doc evidence:** `API_StopInstances` Force/SkipOsShutdown field text; Service Authorization Reference EC2 action table. **Severity-if-true:** Medium (reportable AWS-owned granularity gap).

### Area 2 — [NEW, PRIORITY] Integrity interruption: force/skip aborts an in-progress graceful stop and poisons the session (Lens U / Business-logic / L)
**Background.** `instance-stop-methods` states: skip-os-shutdown "If used while a default stop with graceful OS shutdown is in progress, the graceful OS shutdown **will be bypassed**," and "Bypassing the graceful OS shutdown is **irreversible for the instance's current state transition session**. A subsequent default stop attempt during this session will not attempt a graceful OS shutdown." Force stop's data impact: "In rare cases, results in **post-stop writes to EBS volumes or other shared resources**."
**Security Concern.** A caller with `ec2:StopInstances` can (a) interrupt another operator's clean, in-flight shutdown and convert it to a flush-bypass → data loss on a healthy instance, and (b) poison the transition session so even a later *correct* `StopInstances` (no flags) skips the flush. The "other shared resources" post-stop-write phrasing is a documented write that outlives the stop — worth characterising for any cross-boundary effect.
**High-level Test Scenarios.**
- *Claim:* Issuing `SkipOsShutdown` during an in-progress graceful stop bypasses the flush already underway. → *Oracle:* in a test account, start a graceful stop with a long shutdown script, then issue skip-os-shutdown; observe the shutdown script did not complete / fs is dirty on next boot.
- *Claim:* After one skip-os-shutdown in a session, a subsequent plain stop also skips the flush. → *Oracle:* reproduce the documented "subsequent default stop … will not attempt a graceful OS shutdown."
- *Claim (HARD-STOP-gated):* "post-stop writes to … other shared resources" ever touch a resource outside the instance's own EBS volumes. → *Oracle:* observe writes to any resource not owned by the caller → **stop, disclose.**
**Doc evidence:** `instance-stop-methods` §Skip/§Force "Data impact". **Severity-if-true:** High if an attacker-triggerable data-loss on a healthy third-party-owned (same-account) instance; Low if purely self-inflicted on own instance.

### Area 3 — [PRIORITY] In-account root-volume-swap read primitive + unconditioned `AmazonEC2FullAccess` (Lens A / R / X)
**Background.** The page's "(Alternate) create a replacement instance" procedure explicitly instructs: snapshot the stuck instance's volumes → `CreateVolume` → detach a fresh instance's root → "**attach it to the new instance as its root volume**" → start. `AttachVolume`'s `Device` is free-text (no root-device restriction). The shipped AWS-managed policy `AmazonEC2FullAccess` is `{"Action":"ec2:*","Resource":"*"}` with **no `Condition`**.
**Security Concern.** Any principal holding `AmazonEC2FullAccess` (extremely common) can run the full `CreateSnapshot → CreateVolume → AttachVolume(as root) → StartInstances` chain against **any other team's instance/volume in the same account**, booting/reading that workload's root filesystem (SSH keys, app secrets, credentials baked on disk). AWS's own baseline grant provides zero guardrail even though `ec2:ResourceTag`, `ec2:InstanceID`, `ec2:ParentSnapshot` all exist and would scope it. This is an **AWS-authored, copy-verbatim artifact** → in scope (Tier-2), not a customer footgun.
**High-level Test Scenarios.**
- *Claim:* A role with only `AmazonEC2FullAccess` can snapshot and boot a foreign (same-account) root volume and read its data. → *Oracle:* under a scoped role holding exactly that managed policy, with synthetic canary data on a second "victim" instance you also own in a test account, complete the chain and read the canary from the attached root. Prove the managed policy — not a broader tester identity — authorized it.
- *Claim:* `ec2:ParentSnapshot` / `ec2:ResourceTag` could bound `CreateVolume`/`AttachVolume` but no AWS-managed policy uses them. → *Oracle:* `iam:SimulateCustomPolicy` showing a tag-scoped variant denies the cross-team attach while `AmazonEC2FullAccess` allows it.
**Doc evidence:** `TroubleshootingInstancesStopping` alternate procedure; `API_AttachVolume` (`Device` free-text, same-AZ only); `AmazonEC2FullAccess` JSON. **Severity-if-true:** Medium–High (cross-workload data reach within an account via an AWS-authored uneditable policy).

### Area 4 — Shared / public snapshot & AMI ingest + crash-consistent image leak (Lens A / T / Q / EE)
**Background.** `CreateVolume`/`RunInstances` accept any snapshot/AMI the caller can read, including cross-account-shared or public ones. AWS warns: sharing a snapshot gives "access to **all of the data** on the snapshot"; a shared-AMI recipient can "rebundle it and register it as their own." `CreateImage --no-reboot` yields "crash-consistent" images that exclude buffered/in-memory data — AWS's own recovery flow accepts this.
**Security Concern.** (a) Ingesting a shared/public snapshot/AMI leaks the source account's unscrubbed secrets; (b) a crash-consistent `--no-reboot` image of a running (or compromised) instance can bake inconsistent/sensitive state and is then re-shareable; (c) **predictable/public namespace** (public snapshots/AMIs) is a weak authenticity-filter surface (Lens EE / whoAMI-style) — a lookup that omits an `--owners`/owner filter can select an attacker-published image.
**High-level Test Scenarios.**
- *Claim:* `CreateVolume` from a snapshot *shared to* the caller boots and exposes the source account's on-disk data. → *Oracle:* with two test accounts you own, share a canary snapshot A→B, create+boot in B, read canary.
- *Claim:* a replacement-instance workflow that resolves an AMI by name/pattern without owner-pinning selects an attacker-registered AMI. → *Oracle:* confirm any name-based AMI lookup in the recovery runbook lacks `--owners amazon|self`.
**Doc evidence:** `ebs-modifying-snapshot-permissions`, `sharingamis-explicit`, `building-shared-amis`, `API_CreateImage` NoReboot text. **Severity-if-true:** Medium (data exposure, source-account-scrub-dependent); High only if cross-account occurs without the owner's intended share.

### Area 5 — Stop/termination protection vs force (Lens U)
**Background.** `DisableApiStop` "controls whether the instance can be stopped by using the console, CLI, or the API." Force/skip are the same `StopInstances` action plus flags — no documented separate code path. `instance-terminate-methods` states "You can't terminate an instance if termination protection is turned on" directly above the table that lists force-terminate. **But no page explicitly states that `--force` does not bypass `DisableApiStop`/`DisableApiTermination`** (doc gap). Documented protection *exclusions*: OS-initiated shutdown, scheduled retirement events, Auto Scaling scale-in/health termination; stop protection is unavailable for instance-store-root and Spot instances; the attribute is eventually consistent.
**Security Concern.** Confirm force/skip is a shutdown-execution modifier layered on top of normal authz (expected: it does **not** bypass protection), and that the documented exclusions + eventual-consistency window are the real gaps an attacker/operator leans on.
**High-level Test Scenarios.**
- *Claim:* `stop-instances --force` against an instance with `DisableApiStop=true` is refused exactly like a normal stop. → *Oracle:* on your own test instance, expect an error, not a stop. (Refute = High finding: force bypasses protection.)
- *Claim:* the eventual-consistency window on `ModifyInstanceAttribute(DisableApiStop)` lets a stop land after protection was "enabled." → *Oracle:* race enable→stop; observe the window.
**Doc evidence:** `ec2-stop-protection`, `Using_ChangingDisableAPITermination`, `instance-terminate-methods`. **Severity-if-true:** Critical if force bypasses protection (very unlikely by design); otherwise Low/Informational (documented exclusions).

### Area 6 — Detection gap: force/skip stops carry no distinct event name (Lens O)
**Background.** CloudTrail records one `eventName` = `StopInstances` for every flag combination; the only differentiator is nested `requestParameters` (`force`/`skipOsShutdown`). No `ForceStopInstances` action exists.
**Security Concern.** Detections keyed on `eventName` alone cannot distinguish a routine stop from a data-destructive force/skip stop; defenders must parse `requestParameters`. (EC2-specific worked-example log was not found → confirm field casing live.)
**High-level Test Scenarios.** *Claim:* `requestParameters.skipOsShutdown=true` / `requestParameters.force=true` appear in the `StopInstances` CloudTrail event and are the *only* signal. → *Oracle:* read a real CloudTrail event in a test account; confirm casing and presence. **Severity-if-true:** Low/Informational (detection-engineering enabler).

### Area 7 — Status-check misread bakes a compromised OS into the "clean" replacement (Lens U / incident-response)
**Background.** The page's "Important": create a replacement AMI **only if the stuck instance produces system status checks only**, because instance status checks mean the guest OS is bad and "the AMI [will copy] over an exact replica of the broken operating system."
**Security Concern.** System check = host fault; instance check = guest fault (possibly compromise). An operator who reads only the aggregate "impaired" status (not which of `StatusCheckFailed_System` vs `StatusCheckFailed_Instance` fired) can AMI a compromised guest and redeploy the backdoor as a golden image. Stuck-instance troubleshooting and compromise-forensics converge on the same `CreateImage` step.
**High-level Test Scenarios.** *Claim:* the only documented gate preventing compromise-propagation here is the status-check *type*. → *Oracle:* doc-confirmed; recommend runbook hardening (always branch on the specific failed-check metric). **Severity-if-true:** Informational→Medium as an IR-process pitfall.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Data-destructive stop usable without extra privilege | `StopInstances` Force/Skip | IAM — but **no condition key exists** to bound the flags |
| Interrupt in-progress graceful stop → forced data loss / session poisoning | stop state machine | "irreversible for the current session" wording (the gap, not a control) |
| Cross-team root-fs read via snapshot→attach-root | `AttachVolume`/`CreateVolume` + `AmazonEC2FullAccess` | resource-level IAM / tag scoping — **unused** by the shipped policy |
| Secret leak from shared/public snapshot/AMI ingest | `CreateVolume`/`RunInstances` | "share only with people you trust"; scrub-before-share guidance |
| Force bypassing stop/termination protection | `StopInstances --force` + `DisableApiStop` | attribute gate on the API action (expected to hold; explicit doc silent) |
| Cross-tenant / shared-host effect from a host-fault stuck stop | underlying Nitro host | Nitro isolation guarantees (general); **not addressed for this scenario** |
| Detection evasion of destructive stops | CloudTrail | `requestParameters` (no distinct `eventName`) |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Shared Nitro host infrastructure**, host-reclaim media sanitization, instance-store remanence between tenants — AWS service-plane; **HARD STOP** if ever reached. Not customer-testable from docs.
- **A customer destroying their own data** with force/skip on their own instance — intended behavior, self-inflicted, out of scope. (In scope only when the destructive capability reaches *another* principal's / team's instance, or the *granularity gap* itself.)
- **Customer-authored** over-broad IAM — footgun, out of scope. (`AmazonEC2FullAccess` is **AWS-authored** → in scope, Tier-2.)
- **IMDS on managed hosts**, DNS rebinding against private-only endpoints, product/feature-parity requests.
- **Billing "camp in stopping to avoid charges"** — unsupported by docs: `stopping` is a transient EC2-controlled fault state, not an attacker-reachable hold.

---

## 8. Null hypotheses / doc gaps (surfaces checked; confirm before trusting)
- **SSRF (Lens G):** N/A — read `TroubleshootingInstancesStopping`, `instance-stop-methods`, `Stop_Start`, `ec2-stop-protection`; no field the service dereferences server-side (no `*Url`/webhook/import). True null for this page set.
- **Prompt injection / LLM (Lens K):** N/A — no agent/LLM in this flow.
- **OAuth / 3P (Lens J), Attestation (Lens W), Canonicalization/parser-diff (Lens BB), Trusted-upstream-context (Lens CC), Cache-key (Lens DD), JWT (Lens FF):** N/A for this control-plane action set — no multi-parser edge, authorizer, cache, or token validation on this page.
- **Hibernate × Force/Skip interaction (Lens U) — DOC GAP:** no page states whether `Force`/`SkipOsShutdown` can combine with `Hibernate`, or what happens if force hits an instance mid-hibernation (partial/corrupt RAM-flush-to-EBS?). **Confirm live before relying.**
- **Shared-host cross-tenant blast radius (Lens V/L) — DOC GAP:** troubleshooting/lifecycle pages are written single-tenant; the stuck-stop host-fault scenario's effect on co-resident tenants is addressed only by general Nitro isolation claims, never in connection with this scenario. Treat as doc gap, **not** a confirmed vuln; **HARD STOP** on any cross-tenant observation.
- **Instance-store / host-reclaim remanence (Lens L) — DOC GAP:** docs describe data *loss* on forced terminate, not a documented secure-wipe/scrub-on-reclaim step; the specific Nitro scrubbing mechanics were not substantiated in this recon.
- **CloudTrail field casing (Lens O) — DOC GAP:** EC2-specific worked `StopInstances` example event not located; confirm `force`/`skipOsShutdown` casing live.
- **"Post-stop writes to … other shared resources" (Lens U/V) — DOC GAP:** AWS names this data-integrity risk but does not define "shared resources"; characterise live (benign EBS-only expected; **HARD STOP** if it reaches another tenant's resource).

---

### Kill-chain note
The sharpest chain here is **Area 3 → Area 2/1**: hold `AmazonEC2FullAccess` → snapshot a target workload's root volume (Area 3) *and* independently use the unbounded `SkipOsShutdown`/`Force` grant (Area 1) to force a dirty stop of the live target first, maximizing on-disk inconsistency/loss, then boot the recovered root to read residual secrets — a same-account cross-workload **integrity-then-confidentiality** chain, rated at the end state (Medium–High), all enabled by AWS-authored defaults with no condition-key guardrail.
