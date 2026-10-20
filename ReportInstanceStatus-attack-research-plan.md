# EC2 `ReportInstanceStatus` — Attack Research Plan

Source of leads:
- Target page: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReportInstanceStatus_section.html (CLI / PowerShell code examples)
- API reference: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReportInstanceStatus.html
- Status-check model: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html
- Scheduled events / retirement: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html
- Authorization facts: AWS service reference JSON (`servicereference.us-east-1.amazonaws.com/v1/ec2/ec2.json`), parsed 2026-10-20.
- Offline mirror: `/work/aws-docs/`

**Status: documentation-derived hypotheses only. Nothing has been tested against a live AWS account.** This plan is produced with the `security-questionbuilder` method (boundary-first). It names where the `ReportInstanceStatus` boundary *might* not hold and exactly how a hunter would confirm or refute it.

---

## 0. How to use this document

- Each lead reads: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows customer feedback reaching an identity/credential/ARN/account belonging to **AWS's own service plane** (e.g. the internal health/accuracy model performing an automated action against a host, or any AWS-fleet identity), stop, preserve evidence, and flag for AWS-Security disclosure. Do not escalate.
- **This is a read-mostly, low-blast-radius API by design** (see §1). The whole plan therefore hinges on one question: *is the documented "feedback is advisory telemetry, scoped to running instances" model actually enforced at the ownership boundary, or is `InstanceId.N` trusted?* Everything else is secondary.
- Use only synthetic/canary instances you own in the two authorized test accounts. Never report status for an instance you cannot account for.

---

## 1. Components, Assets, and Design

**What the action is.** `ReportInstanceStatus` submits *customer feedback* about an instance's health ("ok" or "impaired", with reason codes). Per the API reference it is explicitly **advisory telemetry**:

> "Amazon EC2 collects this information to improve the accuracy of status checks."
> "**Use of this action does not change the value returned by DescribeInstanceStatus.**"

So the documented design decouples this write from any customer-observable state: it does **not** flip the public status, and (per the scheduled-events page) "Scheduled events are managed by AWS. **You can't schedule events for your instances.**" The feedback is a one-way signal into an AWS-internal accuracy model.

**Customer-facing interface.** Standard EC2 Query/SigV4 API over HTTPS (`https://ec2.amazonaws.com/?Action=ReportInstanceStatus&...&AUTHPARAMS`). Exposed in all SDKs, the CLI (`aws ec2 report-instance-status`), and PowerShell (`Send-EC2InstanceStatus` — a legacy cmdlet name for the same action, both V4 and V5 Tools).

**Request shape (the asset surface):**

| Parameter | Type | Required | Role in boundary analysis |
|---|---|---|---|
| `InstanceId.N` | Array of strings | **Yes** | **The identifier the caller supplies** — the IDOR hinge. Instance IDs are `i-` + 17 hex chars (e.g. `i-0598c7d356eba48d7`): high entropy, not trivially enumerable. |
| `Status` | String enum `ok \| impaired` | **Yes** | The feedback polarity. |
| `ReasonCode.N` | Array of enum | **Yes** | `instance-stuck-in-state \| unresponsive \| not-accepting-credentials \| password-not-available \| performance-network \| performance-instance-store \| performance-ebs-volume \| performance-other \| other`. Free-form only via `other` + `Description`. |
| `Description` | String | No | **Deprecated**, but still accepted — free text stored as telemetry. Untrusted-content seam if an operator/tool later renders it. |
| `StartTime` / `EndTime` | Timestamp | No | Reported health window. |
| `DryRun` | Boolean | No | IAM-permission probe only (see trap in Lead A2). |

**Response:** `requestId` + `return` (boolean true on success). No resource payload returned — so there is **no direct read primitive** here; any cross-tenant signal is an *oracle* (accept vs error), not data exfiltration.

**Precondition stated in docs:** "The instance must be in the `running` state." This is itself a server-side check against the named instance — a potential state oracle.

**Identity / ownership model.** SigV4 IAM. The only documented scoping is IAM. There is **no documented statement** that the API validates the caller's *account ownership* of each `InstanceId.N` beyond existence + running-state — this absence is the central lead, not a reassurance.

**Authorization facts (authoritative, from the EC2 service reference JSON):**
- `ec2:ReportInstanceStatus` — access level **Write**. Supports resource type **`instance`** with condition keys: `ec2:AvailabilityZoneId`, `ec2:InstanceBandwidthWeighting`, `ec2:InstanceID`; action condition key `ec2:Region`.
  - **Notably absent:** `ec2:ResourceTag/*` and `aws:ResourceTag/*`. **Tag-based ABAC cannot scope this action.** (→ Lens S)
- `ec2:DescribeInstanceStatus` (read twin) — supports **no** resource types at all (wildcard only); only `ec2:Region`. (→ Lens X asymmetry)

**Mandatory coverage sweep (pages checked, per Step-1 discipline):**
- `API_ReportInstanceStatus` — no URL/URI/host/endpoint/location field → **Lens G (SSRF) N/A**; no file/blob/upload field → **Lens Q N/A**; no role ARN / credential field → **Lens B/C N/A**; no KMS/encryption-context field → **Lens H N/A**; no tagging operation in this action → **Lens I N/A**.
- `monitoring-system-instance-status-check`, `monitoring-instances-status-check_sched` — no prompt/LLM/agent, no OAuth/3P, no session token, no attestation, no cache/authorizer layer → Lenses **K (see caveat below), J, M, W, BB, CC, DD, EE, FF N/A**.
- The one non-generic transport fact is the standard EC2 endpoint; per-API transport analysis is out of scope (service-wide, not this action).

---

## 2. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller's IAM principal (account A) | An instance owned by **account B** | `InstanceId.N` is a caller-supplied body field; authz must bind it to account A | **A success (`return=true`) — or any response that distinguishes B's running instance from a nonexistent one — when reporting an instance account A does not own is a cross-account boundary breach (integrity/enumeration).** |
| Low-privilege principal in account A (tag-scoped) | Any instance in account A | IAM policy keyed on `aws:ResourceTag` cannot gate `ReportInstanceStatus` (no such condition key) | A tag-ABAC-only policy fails to restrict which instances the principal can report on — intra-account scoping gap. |
| Customer feedback (any tenant) | AWS internal status-check **accuracy model** / automated remediation | "collects this information to improve the accuracy of status checks" | **Any evidence that submitted feedback produces an automated action (scheduled event, host migration, hardware-degraded flag, retirement) — especially against another tenant — crosses into AWS's service plane. HARD STOP + disclose.** |
| Caller-supplied `Description` free text | AWS internal feedback-triage tooling / operator view | Deprecated-but-accepted free string stored as telemetry | Stored content later rendered/interpreted by an internal tool = indirect-injection seam (doc-gap; unobservable externally). |

Canonical boundary that is **the hard stop:** *any customer surface ↔ AWS's own service plane.* Because the documented purpose of this API is to feed an AWS-internal model, over-aggressive confirmation of the "poisoning" leads risks touching that plane. Keep those leads at the **existence-oracle** level and stop.

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ReportInstanceStatus` | POST (Query) | Existing (legacy; `2016-11-15`) | **Write** (telemetry submit; does **not** mutate customer-observable state) | External-facing | Submit ok/impaired feedback + reason codes for one or more instances | Yes (SigV4) | Any principal with `ec2:ReportInstanceStatus` | Array param → batch; running-state precondition; `Description` deprecated. |
| `Send-EC2InstanceStatus` (PowerShell) | — | Legacy alias | same | External | Same action, different name surface | Yes | same | Legacy cmdlet name — check parity (Lens X). |
| `DescribeInstanceStatus` (twin, for oracle calibration) | POST (Query) | Existing | Non-mutating (Read) | External | Returns status + scheduled events | Yes | `ec2:DescribeInstanceStatus` | No resource-level perms; use as the "what account A can already see" baseline. |

Undocumented-knob sweep: the only enum surfaces are `Status` (`ok|impaired`) and `ReasonCode` (9 values). The API-ref **Example 2 uses `ReasonCode` values `instance-performance-network` and `instance-performance-disk` that are NOT in the valid-values list** — a doc defect worth a one-line Informational report (Lens U doc-vs-doc), and a hint to test whether the server silently accepts invalid/legacy reason codes.

---

## 4. Recommended Areas of Focus

Priority order: **A (cross-tenant ownership) → U (guarantee-vs-enforcement / impact) → X (twin parity) → S (IAM scoping) → L/O/K (abuse, logging, stored content).**

### Area A — Cross-account ownership enforcement on `InstanceId.N` (Lens A — PRIMARY)

**Background.** `InstanceId.N` is a caller-controlled body field naming the target resource. Nothing in the docs states the action verifies account ownership beyond existence and running-state. This is the exact "resource named by a caller-supplied field; is authz bound to the credential or to the field?" IDOR shape.

**Security Concern.** If authz checks only *existence*/*running-state* (or only caller IAM via `DryRun`-style evaluation) and not *ownership*, account A can submit health feedback about account B's instances.

**High-level Test Scenarios (falsifiable claims):**
- **A1 — Cross-account report acceptance.** *Claim:* `ReportInstanceStatus(InstanceId=<account-B running instance>, Status=impaired)` returns `return=true` for a caller in account A. *Mechanism:* no documented ownership check on this action's own page; `InstanceId.N` is attacker-chosen. **Calibration — expected refute:** the EC2 API family documents its ownership convention on the analogous `DescribeInstanceImageMetadata` page — *"If you specify ... an instance that you do not own, an error (`InvalidInstanceID.NotFound`) is returned."* If `ReportInstanceStatus` follows the family pattern, a foreign running instance should return `InvalidInstanceID.NotFound` (ownership enforced via account-scoped existence) → **lead refuted**. *Oracle:* `return=true`, or ANY response other than `InvalidInstanceID.NotFound`/`AccessDenied` (e.g. `IncorrectInstanceState`, a 500, or success) for a foreign running ID = breach, because it proves the action resolved a resource outside the caller's account. Compare against a known-owned control instance (should succeed) and a random nonexistent ID (should `InvalidInstanceID.NotFound`). *Preconditions:* two authorized accounts; a running canary in each. *Cost:* minutes. *Severity-if-true:* **High** (cross-account write/telemetry) — escalates toward Critical **only** if chained to a provable automated effect (Area U → then HARD STOP). *Stop:* the moment acceptance is confirmed; do **not** spam further reports.
- **A2 — DryRun false-positive trap (refute-first).** *Claim:* `DryRun=true` on a foreign instance returning `DryRunOperation` proves nothing about ownership. *Mechanism:* DryRun is evaluated on caller IAM **before resource resolution** (per skill's documented trap). *Oracle:* treat `DryRunOperation` as "I hold `ec2:ReportInstanceStatus`", never as "I can target this instance". Confirm A1 with a **non-DryRun** call. *Severity:* N/A (methodology guard).
- **A3 — Existence / running-state enumeration oracle.** *Claim:* the error taxonomy distinguishes (a) foreign **running** instance, (b) foreign **stopped** instance (`IncorrectInstanceState`), (c) nonexistent (`InvalidInstanceID.NotFound`), (d) malformed (`InvalidInstanceID.Malformed`) — giving a cross-account state oracle. *Mechanism:* docs require "running" state → a state check runs against the named instance; distinct errors leak its state. **Key refute condition:** if ownership is enforced account-scoped (per A1 calibration), a foreign instance returns `InvalidInstanceID.NotFound` in *every* state → **no state leak, lead refuted**. The oracle only survives if a foreign ID yields state-dependent errors (`IncorrectInstanceState` for a stopped foreign instance), which would mean the existence/state check runs *before* the ownership check — that ordering is the real finding. *Oracle:* send the same foreign ID while the owner toggles it running↔stopped and diff error code / latency / 500-vs-400-vs-200 behavior. *Preconditions:* a foreign instance you can toggle (collaborating test account) to calibrate. *Cost:* low. *Severity-if-true:* **Low–Medium** — bounded by instance-ID entropy (17 hex chars ≈ non-enumerable), so this is a *confirmation* oracle for a known ID, not a discovery primitive. Note any **embedded-checksum** in the instance ID that would make fabricating a foreign ID impossible (genuine null result).
- **A4 — Batch partial-success oracle.** *Claim:* a single call mixing one owned + one foreign `InstanceId` reveals per-ID handling (atomic reject vs partial accept vs per-ID error map). *Oracle:* response/error granularity distinguishes which IDs were accepted = per-ID existence oracle + confirms whether ownership is enforced per-element. *Severity:* Low–Medium.

### Area U — Documented guarantee vs actual enforcement / impact (Lens U — determines severity of Area A)

**Background.** Two explicit guarantees: (1) "does not change the value returned by `DescribeInstanceStatus`"; (2) scheduled events are "managed by AWS. You can't schedule events for your instances." These make the action *look* harmless. The research question is whether those guarantees fully hold, because they are the only thing bounding Area A's severity.

**Documented impact ceiling (confirmed doc-dead-end).** A documentation sweep of the retirement, auto-recovery, and status-check pages found **no documented path** from customer-submitted feedback to any automated action. Retirement is driven *only* by AWS hardware detection — *"An instance is scheduled to be retired when AWS detects irreparable failure of the underlying hardware"* (`instance-retirement.html`). Automatic recovery triggers *only* on a failed **system** status check — *"Automatic instance recovery ... does not operate if only the instance status check fails"* (`ec2-instance-recover.html`) — and system checks are AWS-telemetry-driven, never customer-feedback-driven. **Conclusion for the hunter:** per docs, Area A tops out at **High** (cross-account telemetry write), and the "feedback → victim availability" escalation (U2) is a *doc-gap hypothesis only* — if it were ever confirmed it immediately crosses into AWS's service plane (HARD STOP).

**Security Concern.** If sufficient `impaired` feedback — especially cross-tenant (Area A) — can influence the internal accuracy model enough to trigger an automated action (a scheduled `system-reboot`/`instance-stop`/`instance-retirement`, a host-degraded flag, or a migration), then cross-account false reporting becomes a **victim availability attack**, and the path reaches AWS's service plane.

**High-level Test Scenarios:**
- **U1 — Status immutability.** *Claim:* after reporting `impaired`, `DescribeInstanceStatus` for the same (owned) instance is unchanged. *Oracle:* diff `InstanceStatus`/`SystemStatus`/`Events` before vs after; any change refutes guarantee (1). *Severity-if-true:* Medium (doc-vs-behavior) → High if the induced change is an event the attacker did not own.
- **U2 — No induced scheduled event (bounded, HARD-STOP-gated).** *Claim:* repeated/varied `impaired` feedback on an **owned canary** never induces a scheduled event or migration. *Oracle:* poll `DescribeInstanceStatus[].Events` on the owned canary over time. **If an event appears that correlates with your feedback, STOP** — you are at the service-plane boundary; preserve evidence, do not attempt it cross-account, and flag for disclosure. *Severity-if-true:* **Critical** (customer feedback → automated remediation). *Precondition:* owned instances only; never probe this against a foreign instance.
- **U3 — Reason-code validation strictness.** *Claim:* the server accepts reason codes outside the published enum (the doc's own Example 2 uses `instance-performance-disk`, not in valid-values). *Oracle:* submit an out-of-enum reason code on an owned instance; `return=true` vs `InvalidParameterValue`. *Severity:* **Informational** (doc defect / loose validation). Also file the doc-example inconsistency to `aws-security` docs owner (Lens U doc-vs-doc, AWS-owned).

### Area X — Twin / legacy-alias authorization parity (Lens X)

**Background.** The write action `ReportInstanceStatus` supports `instance`-level IAM scoping; the read twin `DescribeInstanceStatus` supports **none** (wildcard only). The PowerShell `Send-EC2InstanceStatus` is a legacy alias for the same action.

**Security Concern.** Divergent validators across sibling/legacy surfaces give enumeration oracles or unequal ownership enforcement.

**High-level Test Scenarios:**
- **X1 — Validator divergence (Report vs Describe).** *Claim:* for a foreign/nonexistent/malformed `InstanceId`, `ReportInstanceStatus` and `DescribeInstanceStatus` return different error codes/strictness, forming a cross-API confirmation oracle. *Oracle:* diff the two actions' responses on identical foreign IDs. *Severity:* Low (enumeration-only).
- **X2 — Legacy-cmdlet parity.** *Claim:* `Send-EC2InstanceStatus` enforces the same ownership/validation as the raw API. *Oracle:* run both paths against the same foreign ID; any looser behavior on the legacy path is the lead. *Severity:* mirrors Area A if it diverges.

### Area S — IAM condition-key scoping gap (Lens S)

**Background.** `ec2:ReportInstanceStatus` is gateable only by `ec2:InstanceID`, `ec2:AvailabilityZoneId`, `ec2:InstanceBandwidthWeighting`, `ec2:Region` — **not** by `ec2:ResourceTag`/`aws:ResourceTag`.

**Security Concern.** A customer who governs instance access with tag-based ABAC (the AWS-recommended pattern) *cannot* scope this action by tag. A least-privilege policy written as "allow EC2 actions only on instances tagged `team=X`" silently leaves `ReportInstanceStatus` ungated across the whole account.

**High-level Test Scenarios:**
- **S1 — Tag-ABAC inert.** *Claim:* a policy allowing `ec2:ReportInstanceStatus` with `Condition: StringEquals aws:ResourceTag/team=X` does not restrict the action (condition key not evaluated for this action) — either it errors at author time or is simply ineffective. *Oracle:* `iam:SimulatePrincipalPolicy` / `SimulateCustomPolicy` first (no resources touched); confirm the tag condition does not deny an untagged/other-team instance. *Severity:* **Low–Medium** (intra-account least-privilege gap; it is a *customer-authored* policy, so a footgun rather than an AWS defect — but worth documenting because the condition-key omission is AWS-owned surface). *Note:* `ec2:InstanceID` scoping does work, so the mitigation exists but is coarse.

### Area L / O / K — Abuse volume, logging, stored content (lower priority)

- **L1 — Batch / rate abuse & model poisoning (cross-tenant integrity).** *Claim:* an array of many `InstanceId` + high request rate lets one tenant flood `impaired` feedback. *Concern:* if feedback feeds a *shared* accuracy model, mass false reporting could degrade signal quality for others. *Mechanism / limits:* `ReportInstanceStatus` is **not individually listed** in the EC2 API throttling reference, so it falls into the generic **"Mutating actions"** bucket (documented bucket ≈ 50 tokens, refill 5/sec; over-limit → `RequestLimitExceeded`). The `InstanceId.N` array has **no documented maximum count** (doc-gap). *Oracle:* confirm the per-call array cap empirically on owned instances; any cross-tenant integrity effect → service plane → HARD STOP. *Severity:* cross-tenant integrity = High if provable; single-tenant = out of scope.
- **O1 — CloudTrail coverage.** *Claim:* `ReportInstanceStatus` is recorded as a management (write) event. *Oracle:* check CloudTrail for the event after an owned-instance call; a missing record is an attribution gap. *Severity:* Informational (enabler).
- **K1 — `Description` stored-content seam.** *Claim:* the deprecated `Description` free text is stored and later rendered in an internal triage tool/console without sanitization (indirect stored-injection/XSS into an AWS-operator surface). *Oracle:* **not externally observable** — doc-gap; flag as a design question for AWS, do not attempt active confirmation. *Severity:* unknown / doc-gap.

---

## 5. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Report status for another account's instance (A1) | `ReportInstanceStatus` authz | Account-ownership binding of `InstanceId.N` (undocumented — assumed, must verify) |
| Enumerate foreign instance existence/state via error taxonomy (A3/A4/X1) | Report vs Describe error paths | Uniform error responses; high instance-ID entropy |
| Induce an automated remediation/event via feedback (U2) | Internal accuracy model | "does not change DescribeInstanceStatus"; "events managed by AWS, you can't schedule" |
| Bypass tag-based least-privilege (S1) | IAM condition-key coverage | `ec2:InstanceID`-based scoping (tag scoping unavailable) |
| Poison shared accuracy model by volume (L1) | Feedback ingestion | Throttling / per-account isolation of the signal (doc-gap) |
| Legacy-alias parity (X2) | `Send-EC2InstanceStatus` | Same server-side authz as the raw action |

---

## 6. Out-of-Scope Risk Categories

- **Single-tenant self-impact.** Reporting bogus status on your *own* instances, or self-DoS via your own feedback — out of scope.
- **The internal accuracy model itself.** How AWS's ML/health model works is service-plane; probing it beyond the owned-instance immutability check (U1) and the gated stop-on-first-signal check (U2) is a HARD STOP.
- **Generic EC2 endpoint transport/TLS/SigV4** — service-wide, not specific to this action.
- **IMDS / in-guest behavior** on managed infra.
- **Customer-authored IAM least-privilege choices** beyond noting the `ec2:ResourceTag` omission (S1) — the condition-key *omission* is AWS-owned surface (worth a note); the policy a customer writes around it is their own footgun.
- **DNS rebinding / network-layer** — no fetch primitive exists here.

---

## 7. Null Hypotheses / Doc Gaps

**Lenses that did NOT fire (pages checked named per Step-1 discipline):**
- **G (SSRF) — N/A.** Read `API_ReportInstanceStatus`; no field is a URL/URI/host/endpoint/location the service dereferences. Only `InstanceId`, enums, timestamps, and a deprecated free-text `Description`.
- **Q (upload) — N/A.** No file/blob/image/attachment field.
- **B / C (PassRole / credential vending) — N/A.** No role ARN, no STS/session, no credential-provider field.
- **H (KMS), I (tagging op), J (OAuth/3P), M (session id), N (namespace migration), V (network seg), W (attestation), Y (per-API transport), AA (share/revoke), BB/CC/DD (edge/parser/cache/upstream-context), EE (predictable-name), FF (JWT) — N/A** for a single SigV4 Query action with no corresponding mechanism; checked the API ref + the two status-check user-guide pages.
- **K (prompt injection) — mostly N/A**, except the `Description` stored-content seam (K1) which is a doc-gap, not a confirmable lead.

**Doc gaps (confirm surface before relying on these):**
- `ReportInstanceStatus`'s **own API page does not state** account-ownership behavior/error. The EC2 family convention — `InvalidInstanceID.NotFound` for "an instance that you do not own" — is documented on the analogous `DescribeInstanceImageMetadata` page, so ownership is *likely* enforced account-scoped, but this must be confirmed for this action specifically (Area A1). Treat as open until observed.
- The **exact downstream use** of the collected feedback is undocumented, and a full sweep of the retirement / auto-recovery / status-check pages found **no documented link** from feedback to any automated action → the U-area "availability" ceiling is a doc-gap hypothesis and a HARD-STOP-gated probe, not a supported severity.
- **Per-call `InstanceId.N` array cap** is undocumented; request-rate throttling is only inferable (generic "Mutating actions" bucket, `RequestLimitExceeded`), not a named limit for this action.
- Whether the server **rejects out-of-enum reason codes** (the API doc's own Example 2 uses invalid `instance-performance-network` / `instance-performance-disk`) is unconfirmed.
- Whether `Description` (deprecated) is still accepted/stored and where it surfaces.
- No legacy/deprecated *action* alias exists beyond the CLI (`report-instance-status`) and PowerShell (`Send-EC2InstanceStatus`) wrappers (checked).

---

## Appendix — Authoritative facts captured (for the next agent)

- Action: `ec2:ReportInstanceStatus`, access level **Write**, API version `2016-11-15`.
- Required params: `InstanceId.N` (array), `Status` (`ok|impaired`), `ReasonCode.N` (9-value enum). Optional: `Description` (deprecated), `StartTime`, `EndTime`, `DryRun`.
- Response: `requestId`, `return` (bool) — **no resource data returned**.
- Documented preconditions/guarantees: instance must be **running**; action **does not change `DescribeInstanceStatus`**; purpose is to "improve the accuracy of status checks."
- IAM: resource type `instance`; condition keys `ec2:AvailabilityZoneId`, `ec2:InstanceBandwidthWeighting`, `ec2:InstanceID`, `ec2:Region`. **No `ec2:ResourceTag`/`aws:ResourceTag`.**
- Twin `ec2:DescribeInstanceStatus`: **no** resource-level permissions (wildcard only).
- Legacy alias: PowerShell `Send-EC2InstanceStatus` (Tools V4 + V5); CLI `aws ec2 report-instance-status`. No older EC2-Classic-era action name found.
- Scheduled events are AWS-managed; customers cannot schedule them. Event types: `instance-stop`, `instance-retirement`, `instance-reboot`, `system-reboot`, `system-maintenance`.
- Impact sweep (confirmed doc-dead-end): retirement = *"AWS detects irreparable failure of the underlying hardware"* (`instance-retirement.html`); auto-recovery triggers only on a failed **system** status check and *"does not operate if only the instance status check fails"* (`ec2-instance-recover.html`). Neither names customer feedback as an input.
- Throttling: not individually listed → generic "Mutating actions" bucket (~50 token / 5-per-sec); over-limit error `RequestLimitExceeded`. No documented `InstanceId.N` max count.
