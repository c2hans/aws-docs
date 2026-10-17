# EC2 "Troubleshoot an Unreachable Instance" (Console Diagnostics + Instance Recovery) — Attack Research Plan

Source of leads:
- Primary page: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshoot-unreachable-instance.html (`.md` mirror)
- Child/linked pages: `ics-common.md` (common Windows screenshots), `ec2-instance-reboot.md`, `verify-if-automatic-recovery-occurred.md`, `ec2-instance-recover.md`, `instance-configuration-recovery.md`, `cloudwatch-recovery.md`, `schedevents_actions_reboot.md`, `Stop_Start.md`, `how-ec2-instance-stop-start-works.md`
- IAM: https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html  **(NOTE: the older `list_amazonec2.html` URL now 302-redirects to the reference index — use `list_ec2.html`)**
- API/CLI refs: `API_GetConsoleOutput.html`, `API_GetConsoleScreenshot.html`, `cli/.../get-console-output.html`, `cli/.../get-console-screenshot.html`
- CloudWatch: `AmazonCloudWatch/latest/monitoring/UsingAlarmActions.html`

**Status: documentation-derived hypotheses only. Nothing has been tested against any live AWS account.** This plan is for a downstream authorized hunter (`aws-vuln-hunter`) to execute in a two-account test lab.

---

## 0. How to use this document

- Each lead is written as: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity / credential / ARN / account belonging to AWS's own service plane (e.g. the "Console Screenshot Service" backend fleet, a recovery-migration host identity, the CloudWatch SLR's underlying principal), **stop, preserve evidence, and flag for AWS-Security disclosure.** Do not escalate.
- **The prime target of this page is a confidentiality boundary, not an availability one.** `GetConsoleOutput` returns raw boot/kernel console buffers (routinely containing cloud-init output, user-data secrets, kernel env dumps); `GetConsoleScreenshot` returns a JPG of the live screen (Windows logon screens, any app displaying secrets). A single confirmed cross-account read of either = **Critical**. Treat the ownership check as the one boundary that matters most.
- **Testability gate (read before planning IDOR work):** instance IDs are `i-` + 17 lowercase hex chars (~2^68), randomly generated, with **no documented checksum/pattern**. Blind cross-account enumeration is **not** feasible. Every cross-tenant lead below presumes a *known/leaked* foreign instance ID (from a shared AMI's logs, a public snapshot, a leaked screenshot/log, a support artifact, a shared-VPC/RAM relationship, or a misconfigured service that echoes its own instance ID). Acquire the ID out-of-band; do not burn time brute-forcing.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **Read another account's instance console output or screenshot** by naming its instance ID to `GetConsoleOutput` / `GetConsoleScreenshot` — the direct contradiction of the page's "Only the instance owner can access" guarantee. (Critical)
2. **Reach the shared "Console Screenshot Service" backend** in a way that returns, or discloses the existence of, a capture belonging to another tenant. (Critical)
3. **Confirm or refute** that the "only owner" guarantee is enforced by a service-side account-ownership check (not merely by the caller's own IAM policy), and identify any edge case where it is not applied (shared-VPC/RAM-launched instances, Outposts, Local Zones, License-Manager cross-account AMI). (Critical if it fails)
4. **Cause a state change through a "Read"-classified action** — specifically `GetConsoleScreenshot` with `WakeUp=true` sending a keystroke to wake a standby instance — proving a read-only-auditor role can mutate instance state. (Medium)
5. **Reboot / stop / recover an instance without holding the corresponding `ec2:*Instances` permission**, via a CloudWatch alarm "recover/reboot/stop" action executed by the `AWSServiceRoleForCloudWatchEvents` SLR (confused-deputy / least-privilege-review bypass). (Medium–High)
6. **Determine whether `GetConsoleOutput`/`GetConsoleScreenshot` calls are recorded in CloudTrail** as management events — i.e. whether reading another's (or one's own) secrets-bearing console data is a silent, un-audited reconnaissance primitive. (High if unlogged)
7. **Confirm the recovery/host-migration path preserves the documented "identical instance" guarantee** without creating an IMDS/instance-profile credential-confusion window. (Medium–High if it diverges)

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 control-plane APIs over HTTPS/SigV4 (public, internet-reachable): `GetConsoleOutput`, `GetConsoleScreenshot`, `RebootInstances`, plus the console routes **Actions → Monitor and troubleshoot → {Get system log | Get instance screenshot}**. No non-SDK/internal endpoint is exposed on this page; all three are standard SDK actions.

**Backend processes/fleets.**
- A named shared backend — **"Console Screenshot Service" / "Instance Console Screenshot Service"** (named verbatim in `ics-common.md`: *"Console Screenshot Service returned the following."*). It renders a JPG from the instance's video framebuffer, size-capped at 100 kb, and is **not** available on bare-metal, NVIDIA GRID, Graviton/Arm, Windows-on-Outposts, Windows-on-Local-Zones, or in AP (Thailand) / Mexico (Central) / GovCloud. The exclusion list is itself a design statement: screenshot capture is a hypervisor-mediated capability of the Nitro/Xen host, not of the guest.
- The console-output buffer is captured by the host/hypervisor "shortly after an instance transition state (start, stop, reboot, terminate)"; `Latest=true` (serial console output) is **Nitro-only**.
- **Recovery / migration control plane:** simplified automatic recovery and CloudWatch action-based recovery (the latter driven by the service-linked role `AWSServiceRoleForCloudWatchEvents`) migrate an unavailable instance to new hardware. Stop/Start also migrates to a new host on Start.

**Assets (what an attacker wants).**
- The **console-output buffer** — base64 text; routinely leaks cloud-init logs, user-data secrets, kernel panics with environment dumps, Windows "last three system event log errors."
- The **screenshot JPG** — on-screen content: Windows logon screen (reveals usernames), recovery/boot screens, and anything a running app renders (dashboards, tokens, secrets).
- The ability to **reboot/wake/recover** an instance (integrity/availability).

**Identity.** SigV4 IAM principal. Both diagnostic actions are IAM **Access level = "Read"**; `RebootInstances` is **Write**. All three support the `instance` resource type and a rich condition-key set (see §3/§4). Instance ARN: `arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}` — the account ID is embedded in the ARN; EC2 instances have **no resource-based (cross-account) policy** mechanism.

**Resource identifier shape.** `i-` + 17 hex (~2^68), random, **no documented checksum** → not blind-enumerable (see §0 testability gate).

**ASCII flow:**
```
  Caller (IAM principal, account B)
        │  SigV4: GetConsoleOutput / GetConsoleScreenshot(WakeUp) / RebootInstances
        ▼
  EC2 control plane  ──[ownership check: ARN account == caller account?]──►  (THE boundary under test)
        │                                                   │
        │ (screenshot)                                      │ (reboot / recover)
        ▼                                                   ▼
  "Console Screenshot Service"  ◄── shared multi-tenant ──►  Hypervisor / Nitro host
        │  renders JPG from framebuffer                      │  captures console buffer; migrates on recover/stop-start
        ▼                                                     ▼
  base64 JPG (≤100kb) back to caller               recovered instance on NEW host (same id/IP/metadata)

  [CloudWatch alarm "recover/stop/reboot" action] ──via SLR AWSServiceRoleForCloudWatchEvents──► EC2 mutating call
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `GetConsoleOutput` | GET/POST (SigV4) | Existing | **No** (Read) | External | Yes | "Only the instance owner" (prose); IAM `instance*` resource-level supported | `InstanceId` (req), `Latest` (bool, Nitro-only), `DryRun`. Returns base64 `output` + `timestamp`. |
| `GetConsoleScreenshot` | GET/POST (SigV4) | Existing | **No per IAM (Read)**, but `WakeUp=true` sends a keystroke → de-facto mutating | External | Yes | instance owner (NOT restated on this page — see Lens U); IAM `instance*` supported | `InstanceId` (req), `WakeUp` (bool, side-effecting), `DryRun`. Returns base64 JPG `imageData` (≤100kb). Unsupported on metal/GRID/Graviton/Win-Outposts/Win-LocalZones; absent in AP-Thailand/MX-Central/GovCloud. |
| `RebootInstances` | POST (SigV4) | Existing | **Yes** (Write) | External | Yes | instance owner | Resource `instance*`; cross-account structurally blocked (account-scoped ARN, no resource policy). "Reboot migration" knob affects whether a reboot during a pending `system-reboot` event changes hardware. |
| `ModifyInstanceMaintenanceOptions` `--auto-recovery {default\|disabled}` | POST | Existing | Yes | External | Yes | instance owner | Enables/disables simplified automatic recovery per instance. |
| `ModifyInstanceMaintenanceOptions` `--reboot-migration {default\|disabled}` | POST | Existing | Yes | External | Yes | instance owner | Controls hardware migration on user reboot during a pending `system-reboot` event. |
| CloudWatch alarm **"recover/reboot/stop/terminate" action** | (CloudWatch) | Existing | Yes (indirect EC2 mutation) | External config, internal execution | Yes (to configure) | Configurer needs `cloudwatch:PutMetricAlarm` + `iam:CreateServiceLinkedRole`; **executed by `AWSServiceRoleForCloudWatchEvents`, not the configurer's identity** | Confused-deputy surface — see Lens D/U lead D1. |

**Undocumented/console-hidden knob review:**
- `GetConsoleScreenshot.WakeUp` is documented but **packs a mutating keystroke into a "Read"-classified action** — an IAM access-level-taxonomy mismatch (Lens U/X lead U3).
- `GetConsoleOutput.Latest` is console-hidden-ish (the console "Get system log" button maps to default buffered output; `Latest` serial output is CLI/API-only and Nitro-only) — a potential authorization-parity delta between the two output modes (Lens X lead X1).
- IAM reference shows `ec2:NewInstanceProfile` as a condition key for `GetConsoleScreenshot` but **not** for `GetConsoleOutput`. That key semantically belongs to instance-profile-association actions; its presence on a read-only screenshot action looks like an AWS doc-generation/templating artifact (Lens U lead U4 — low impact, but it undermines blind trust in the reference table's fidelity).

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller IAM principal (account B) | Another account's (A) instance console data | `GetConsoleOutput`/`GetConsoleScreenshot` with A's instance ID | **Returning the base64 output/JPG for an instance whose ARN account ≠ caller's account is a hard cross-tenant breach (Critical).** `InvalidInstanceID.NotFound` = boundary holds. |
| Caller | Shared "Console Screenshot Service" backend | Screenshot render request | **Any response that discloses or returns a capture for a tenant other than the caller is a breach.** Reaching the backend fleet's own identity/host = HARD STOP, service-plane. |
| Caller with blanket `Resource:"*"` grant | Instances the caller does not own but is network-adjacent to | shared-VPC/RAM subnet, Outposts/Local Zone, License-Manager cross-account AMI | **A console read succeeding against an instance the caller "hosts" (network) but does not own is a breach** — the page's "owner" sentence never addresses these shared cases. |
| Read-only auditor role (`ec2:GetConsoleScreenshot` only) | Instance power/wake state | `WakeUp=true` keystroke | **A measurable state change (instance wakes) from a "Read"-only grant is a boundary break between the Read taxonomy and actual effect.** |
| Principal lacking `ec2:RebootInstances`/`StopInstances`/`TerminateInstances` | Its own-account instances' lifecycle | CloudWatch alarm action via `AWSServiceRoleForCloudWatchEvents` SLR | **An instance reboot/stop/terminate occurring for a principal explicitly denied the EC2 action = confused-deputy / least-privilege-review bypass.** |
| Instance (data plane) | New host after recovery/migration | automatic recovery / stop-start migration | Mostly AWS service plane. **In-scope slice:** an IMDS credential that remains valid against the vacated host, or a dual-validity window, after migration. |
| Any customer surface | AWS service plane (screenshot fleet, migration host, SLR principal) | — | **Any AWS-owned identity/credential/ARN = HARD STOP, preserve evidence, disclose.** |

---

## 5. Recommended Areas of Focus (ordered — highest-value first)

### Area 1 — Cross-tenant console-data disclosure (`GetConsoleOutput` / `GetConsoleScreenshot`)  [Lens A + Lens U]
**Background.** Both actions take a bare `InstanceId` string and return instance-specific secrets-bearing data (console buffer / screen JPG). The page asserts *"Only the instance owner can access the console output"* — but states **no enforcement mechanism** (no IAM feature, no API error code, no CloudTrail reference). Because EC2 instances have no resource-based policy, the "owner" scoping can only be a **service-side EC2 control-plane account check**; the caller's own IAM policy cannot be what stops cross-account access.

**Security Concern.** If that service-side check is missing, misapplied, or has an edge case (shared-VPC/RAM-launched instance, Outposts, Local Zone, License-Manager cross-account AMI, a legacy/alternate ID form), a caller holding a blanket `Action: ec2:GetConsole*, Resource: "*"` grant could read another account's console output/screenshot — a direct credentials/secrets exfiltration.

**High-level Test Scenarios (falsifiable claims):**
- **A1 (Critical).** Claim: `GetConsoleOutput` returns account A's console buffer when called by account B with A's instance ID. → Mechanism: bare prose guarantee, no cited mechanism; `instance` ARN embeds account but caller policy can't enforce it. → Oracle: two-account lab, B calls with A's *known* instance ID (not guessed). Success/data = Critical breach; `InvalidInstanceID.NotFound` = holds. Distinguish `NotFound` (ownership/existence check fired) vs `Malformed` (format only) vs `UnauthorizedOperation` (caller IAM only — does **not** prove ownership). → Preconditions: known foreign instance ID. → Stop: on any returned data, HARD STOP, disclose.
- **A2 (Critical).** Same as A1 for `GetConsoleScreenshot` → `imageData`. Note the page does **not** restate "only owner" for screenshot (Lens U asymmetry) — test whether screenshot enforces the same ownership gate as output.
- **A3 (High).** Claim: a shared-VPC/RAM relationship breaks the "owner" assumption — the subnet-**owner** account can read console output/screenshot of an instance a **participant** account launched into the shared subnet (or vice-versa). → Mechanism: `ics-common`/troubleshoot pages are silent on RAM; RAM shares the subnet, not the instance. → Oracle: RAM shared-subnet two-account lab; the non-owning network-owner calls both APIs on the participant's instance. Any data returned = High.
- **A4 (Informational, gating).** Claim: cross-tenant IDOR is only testable with a leaked ID (2^68, no checksum). → Oracle: confirm no `Pattern`/checksum in the botocore/SDK model for `InstanceId`; if none, scope all A-leads to leak-based ID acquisition, not enumeration.

**Doc evidence:** troubleshoot-unreachable-instance.html "Instance console output" sentence; `list_ec2.html` (`instance*` resource type, no cross-account resource policy); `API_GetConsoleOutput/Screenshot.html` (`InstanceId: Type String`, no Pattern).  **Severity-if-true: Critical (A1/A2), High (A3).**

### Area 2 — "Only owner" guarantee vs actual enforcement + ownership-check error oracle  [Lens U + Lens A variant]
**Background.** The guarantee is prose with no named backstop. AWS's own IAM reference even carries a plausible fidelity bug (the `ec2:NewInstanceProfile` key on a read-only screenshot action), so the reference table should not be trusted blindly.

**Security Concern.** The gap between a stated guarantee and an uncited enforcement path is the single most useful lead. Separately, differential error responses can form an existence oracle across tenants even if data is not returned.

**High-level Test Scenarios:**
- **U1 (Critical if it fails).** Trace the enforcement: in the authorized lab, confirm the ownership check is service-side by showing a correctly-scoped caller still cannot read a foreign instance even with `Resource:"*"`. Document the exact mechanism AWS never states.
- **U2 (Low–Medium, Lens A oracle).** Claim: `NotFound` vs `Malformed` vs `UnauthorizedOperation` vs a 500/InternalError differ by whether a foreign instance *exists*, forming a cross-tenant existence oracle. → Oracle: compare responses/latency for (a) a non-existent ID, (b) a real foreign ID, (c) a malformed ID. A divergence that confirms existence of a foreign instance = Low–Medium info leak.
- **U4 (Informational).** Report the `ec2:NewInstanceProfile`-on-`GetConsoleScreenshot` reference artifact to AWS as a doc-vs-model inconsistency (Lens U doc-vs-API).

**Doc evidence:** troubleshoot page; `list_ec2.html` condition-key tables.  **Severity-if-true: Critical (U1 refutation), else Informational–Medium.**

### Area 3 — `DryRun` and CloudTrail: silent reconnaissance of secrets-bearing data  [Lens O]
**Background.** Neither the IAM reference, CLI docs, nor API reference states whether `GetConsoleOutput`/`GetConsoleScreenshot` calls are logged as CloudTrail management events (the `logging_using_cloudtrail` page redirected/was unretrievable during recon). `DryRun=true` is documented as a zero-side-effect permission check.

**Security Concern.** If these reads are **not** CloudTrail-logged, an insider or a compromised over-scoped role can repeatedly pull console secrets with no audit trail. Note the skill's warning: **`DryRun` is evaluated as caller-IAM only, before resource resolution — it is NOT an ownership oracle.** So `DryRun` cannot by itself confirm cross-account access (correcting a tempting but false assumption); its value here is only as a low-noise *permission/existence* probe if CloudTrail treats DryRun events differently.

**High-level Test Scenarios:**
- **O1 (High if absent).** Call both APIs, then inspect CloudTrail Event History / a trail for `GetConsoleOutput`/`GetConsoleScreenshot` eventNames within the delivery window. Absent = undocumented audit gap (High — silent recon of secrets); present = expected baseline (Informational).
- **O2 (Medium, contingent on O1).** Determine whether `DryRunOperation` responses are logged with less detail than real calls, enabling low-and-slow permission probing.

**Doc evidence:** absence in `logging_using_cloudtrail.html` (unretrievable); `API_*` DryRun boilerplate.  **Severity-if-true: High (unlogged reads).**

### Area 4 — `WakeUp` keystroke: state change via a "Read"-classified action  [Lens U + Lens X]
**Background.** `GetConsoleScreenshot.WakeUp=true` "acts as keystroke input and wakes up an instance that's in standby/sleep mode" — yet the action's IAM Access level is **Read**.

**Security Concern.** A "read-only auditor" role built on AWS's Read/Write access-level taxonomy, or a change-control exemption that trusts "Read" actions as inert, is wrong: this action can alter instance power state.

**High-level Test Scenarios:**
- **X2 (Medium).** Grant a role only `ec2:GetConsoleScreenshot`; call with `WakeUp=true` against a standby instance; oracle = instance measurably wakes despite a Read-only grant. → Severity: Medium (unexpected state change; compliance/change-control relevance).

**Doc evidence:** `API_GetConsoleScreenshot.html` WakeUp; `list_ec2.html` Access level = Read.  **Severity-if-true: Medium.**

### Area 5 — Output-mode authorization parity (`Latest`/serial vs buffered)  [Lens X]
**Background.** `GetConsoleOutput` default returns the buffered post-transition output; `Latest=true` returns live serial console output (Nitro-only) and is CLI/API-only (not the console button).

**Security Concern.** Two data-retrieval modes behind one action may not share identical authorization/ownership handling, especially the newer Nitro-only serial path.

**High-level Test Scenarios:**
- **X1 (High if divergent).** Claim: the `Latest=true` serial path applies a different (weaker) ownership/validation check than the default buffered path. → Oracle: run Area-1 cross-tenant tests separately with and without `Latest=true`; a divergence (one refuses, one returns data) = High. Also compare error behavior for Nitro vs non-Nitro targets.

**Doc evidence:** troubleshoot page ("latest serial console output... only supported on Nitro-based instances").  **Severity-if-true: High.**

### Area 6 — CloudWatch alarm action confused-deputy (lifecycle mutation without `ec2:*Instances`)  [Lens D + Lens U]
**Background.** CloudWatch alarm "recover/reboot/stop/terminate" actions execute via the SLR `AWSServiceRoleForCloudWatchEvents`; configuring one requires `cloudwatch:PutMetricAlarm` + `iam:CreateServiceLinkedRole` — the docs never state the configurer also needs the matching `ec2:*Instances` permission.

**Security Concern.** A principal explicitly **denied** `ec2:RebootInstances`/`StopInstances`/`TerminateInstances` may still drive those lifecycle actions on same-account instances by wiring an alarm, because the EC2 call at trigger time is made by the SLR, not the configurer. This is a same-account least-privilege-review bypass many customers miss.

**High-level Test Scenarios:**
- **D1 (Medium–High).** Create an IAM principal with `cloudwatch:PutMetricAlarm` + `cloudwatch:SetAlarmState` + `iam:CreateServiceLinkedRole`, explicit **Deny** on `ec2:RebootInstances`/`StopInstances`/`TerminateInstances`. Configure a stop/reboot alarm action; force ALARM via `set-alarm-state`; observe whether the instance action fires. CloudTrail should attribute the EC2 call to the SLR. → Severity: Medium–High (same-account privesc / policy-bypass path; not cross-tenant).

**Doc evidence:** `UsingAlarmActions.html`; `cloudwatch-recovery.md`.  **Severity-if-true: Medium–High.**

### Area 7 — Recovery/migration integrity & IMDS credential continuity  [Lens U + Lens V, mostly scoping]
**Background.** Simplified auto-recovery and CloudWatch recovery migrate an unavailable instance to new hardware, preserving instance ID / IPs / EIP / metadata / placement group / EBS / AZ; RAM and (for CloudWatch recovery) instance-store data are lost. Docs call the recovered instance "identical to the original."

**Security Concern (in-scope slice only).** "Instance metadata preserved" implies the instance-profile/IAM-role association survives, but the docs never state whether IMDS-issued **temporary credentials** are reissued on migration or whether old creds retain validity — a potential dual-validity window.

**High-level Test Scenarios:**
- **V1 (Medium–High if divergent).** Record IMDSv2 temp-credential `AccessKeyId`/expiry before and after a controlled recovery (e.g. via AWS Fault Injection Service if system-check-failure injection is supported); check for continued validity of pre-migration creds or a dual-validity window. → Severity: Medium–High (credential-confusion window) / Medium (reliability).
- **V2 / H2-sanity (Critical if it fails, expected to hold).** Confirm `RebootInstances`/`StopInstances`/`StartInstances` cannot be invoked cross-account (account-scoped ARN, no resource policy) — expect `InvalidInstanceID.NotFound`. Also confirm a tenant cannot trigger another tenant's recovery (CloudWatch per-instance metrics are account-namespaced; re-check if **cross-account observability / OAM** links are configured in the target env — OAM was not analyzed in recon and is a flagged follow-up).

**Doc evidence:** `ec2-instance-recover.md`, `instance-configuration-recovery.md`, `cloudwatch-recovery.md`, `verify-if-automatic-recovery-occurred.md`.  **Severity-if-true: Medium–High (V1); V2 expected to hold.**

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account read of console buffer (A1) | `GetConsoleOutput` | "Only the instance owner can access the console output" (prose, mechanism uncited) |
| Cross-account read of screen JPG (A2) | `GetConsoleScreenshot` / Console Screenshot Service | Owner-scoping (not even restated for screenshot) |
| Shared-VPC/RAM/Outposts ownership edge case (A3) | both diagnostic APIs | none documented for shared cases |
| Cross-tenant existence oracle via error/latency (U2) | both diagnostic APIs | undifferentiated error handling assumed |
| Unaudited secrets recon (O1) | CloudTrail integration | assumed management-event logging (unconfirmed in docs) |
| State change via Read-labeled action (X2) | `GetConsoleScreenshot.WakeUp` | IAM Access level "Read" taxonomy |
| Output-mode authz divergence (X1) | `GetConsoleOutput.Latest` serial path | single IAM action gates both modes |
| Lifecycle mutation w/o `ec2:*Instances` (D1) | CloudWatch alarm action + SLR | `iam:CreateServiceLinkedRole` requirement (no `ec2:*Instances` named) |
| IMDS credential continuity across migration (V1) | automatic recovery | "recovered instance identical to original" (prose) |
| Cross-account reboot/recover trigger (V2) | `RebootInstances` / CloudWatch metrics | account-scoped ARN; account-namespaced metrics |

---

## 7. Out-of-Scope Risk Categories (state confidently to keep the hunter off shared infra)

- **Physical host wiping / instance-store data remanence between tenants** after stop/start/migration. The vacated host's local-disk sanitization (Nitro decommissioning, NVMe secure-erase) is AWS service-plane internals with no customer-reachable boundary and no public docs. **Out of scope.**
- **Hypervisor / live-migration internals** of reboot-migration, simplified auto-recovery, CloudWatch recovery, and stop-start (destination-host selection, state transfer, ENI/EBS re-attach at the Nitro layer). **Out of scope — AWS service plane.**
- **The "Console Screenshot Service" fleet's own identity/credentials/hosts.** Reaching them is a **HARD STOP** (service plane), not an in-scope target.
- **IMDS on fully-managed hosts** as a general class — except the specific documented-guarantee-vs-behavior credential-continuity question in V1.
- **Single-tenant self-DoS** — e.g. disabling reboot-migration and self-rebooting in place to keep a degrading host alive (`schedevents_actions_reboot.md`); a customer footgun on their own instance, Informational only.
- **Customer-authored IAM policy footguns** (e.g. a customer choosing `Resource:"*"` for `ec2:GetConsole*`). The resource-level/condition-key support exists, so a weak policy is customer-authored → out of scope as a finding (but a *service-side* ownership-check failure under such a policy is Area 1, in scope).
- **DNS rebinding against private-only endpoints; product/feature-parity gaps.**

---

## 8. Null Hypotheses / Doc Gaps / Lenses That Did Not Fire

- **Resource-level-IAM "gap" — NULL (debunked).** A common hunter assumption that `GetConsole*` are `Resource:"*"`-only is **false**: `list_ec2.html` shows both support the `instance` resource type plus ~22 condition keys (`aws:ResourceTag`, `ec2:ResourceTag`, `ec2:InstanceID`, `ec2:Region`, `ec2:Tenancy`, etc.). Customers *can* write tag/ARN-scoped least-privilege policies. Do not file this as a finding.
- **Blind cross-tenant enumeration — NULL.** 2^68 random IDs, no documented checksum → not brute-forceable; IDOR leads require a leaked ID (noted at every A-lead).
- **Lens B/C (PassRole / credential vending) — N/A.** Checked the troubleshoot page, reboot page, recovery pages, and `list_ec2.html` condition keys for these three actions: none accept a role ARN or vend credentials. (The CloudWatch SLR path is covered under Lens D, Area 6, not here.)
- **Lens F (translation/injection), Lens K (prompt injection) — N/A.** No parser/translator/LLM in this surface. Console output is read-only buffered text returned verbatim; screenshot is a service-generated JPG. Checked troubleshoot + ics-common pages.
- **Lens G (SSRF) — N/A.** Checked troubleshoot, ics-common, reboot, recovery pages: no field the service dereferences/fetches (no URL/URI/webhook/callback). `WakeUp` is a keystroke, not a fetch.
- **Lens Q (upload/rich-content) — mostly N/A, one render-side note.** No upload field on this surface. The screenshot JPG is **server-generated** (not attacker-supplied), so classic upload-parsing attacks don't apply; however the console *renders* the base64 JPG — if a hunter later finds the guest can influence the rendered bytes and the console mis-sets content-type, revisit for a render-side (Lens Q output) angle. Marked low-priority, surface-confirm-first.
- **Lens H (KMS/encryption-context), I (tagging/ABAC mutation), J (OAuth), M (shared-id interception), N (namespace migration), P (registration/proofing), R/S (shipped IAM-artifact audit), T (cross-service secret reachability), W (attestation), Y (transport/sig), AA (share/revoke), BB (canonicalization), CC (upstream-context), DD (cache-key), EE (predictable-name), FF (JWT) — did not fire for this page's surface.** No IAM policy JSON / managed policy / CFN / runbook is shipped on these pages (R/S); no secret is generated and persisted (T); no attestation gate, no multi-parser request path, no token validation. These were checked by reviewing the primary + child pages and the three actions' IAM-reference rows; none presented the respective lens triggers. If the downstream environment introduces OAM cross-account observability, shared-VPC/RAM, or Outposts, re-open Lens A (A3) and V2.
- **Doc gap — CloudTrail logging behavior for `GetConsoleOutput`/`GetConsoleScreenshot` is unconfirmed** (`logging_using_cloudtrail.html` redirected/unretrievable during recon). This directly powers Area 3 (O1) and must be resolved by live observation or a corrected doc URL — "doc-gap, confirm surface first."
- **Doc gap — IMDS temporary-credential continuity across recovery/migration is unstated** (`ec2-instance-recover.md` lists "metadata preserved" but not credential reissuance). Powers Area 7 (V1).

---

### Priority summary for the hunter
1. **Area 1 (A1/A2)** — cross-tenant console read (Critical) — *needs a leaked foreign instance ID + 2-account lab.*
2. **Area 1/2 (A3/U1)** — shared-VPC/RAM & enforcement-mechanism confirmation (High/Critical).
3. **Area 3 (O1)** — CloudTrail coverage of the diagnostic reads (High if unlogged).
4. **Area 5 (X1)** — `Latest` serial vs buffered authz parity (High if divergent).
5. **Area 6 (D1)** — CloudWatch SLR confused-deputy (Medium–High).
6. **Area 4 (X2)**, **Area 7 (V1)** — Read-labeled `WakeUp` mutation; IMDS credential continuity (Medium).
7. **Area 7 (V2)** — cross-account reboot/recover sanity (expected to hold; cheap confirm).
