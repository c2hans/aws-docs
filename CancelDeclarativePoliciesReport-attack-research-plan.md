# CancelDeclarativePoliciesReport (EC2 Declarative Policies Account-Status Report) — Attack Research Plan

Source of leads:
- https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CancelDeclarativePoliciesReport.html (target)
- API_StartDeclarativePoliciesReport.html, API_DescribeDeclarativePoliciesReports.html, API_GetDeclarativePoliciesReportSummary.html, API_DeclarativePoliciesReport.html
- Service Authorization Reference (offline): `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (the four `*DeclarativePolicies*` actions + `declarative-policies-report` resource type)
- AWS-managed SLR policy (offline): `/work/aws-docs/docs/aws-managed-policy/latest/reference/DeclarativePoliciesEC2Report.md`
- Organizations User Guide: orgs_manage_policies_declarative_status-report.html (online, JS-rendered — key prerequisites captured from the Start API page instead; **confirm the exact required `ec2:`/`organizations:`/`s3:` permission list from this page before hunting — doc-gap**)

Status: **documentation-derived hypotheses only; nothing tested against a live account.** This action is part of a feature GA'd 2024-11-30 (SLR policy creation date); SLR policy edited 2026-07-03 (v2) — recent/under-reviewed surface (Step-5 priority).

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the `report.declarative-policies-ec2.amazonaws.com` / `ec2.amazonaws.com` fleet identity), stop, preserve evidence, flag for AWS-Security disclosure.
- **DryRun trap (apply throughout):** every action here accepts `DryRun`. `DryRunOperation` vs `UnauthorizedOperation` is a **caller-IAM-only** signal, evaluated *before* resource resolution. It is **NOT** an ownership/existence oracle for a `ReportId` — do not treat a `DryRunOperation` result as proof a report exists or is yours.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Scope-escalation at creation:** a principal intended to report on one account/OU generates a report for the **entire org root** (`r-...`), enumerating every member account's security posture — because no `TargetId`/org-scoping condition key exists.
2. **Compliance-control denial:** a principal holding only `ec2:CancelDeclarativePoliciesReport` (not Start) repeatedly cancels the org's single in-flight status report (reports take "several hours"; "only one report per organization at a time"), denying the governance/compliance reporting function.
3. **Unscoped enumeration + metadata disclosure:** a low-privileged principal lists all reports (ReportIds, S3 bucket/prefix, TargetId, status) via `DescribeDeclarativePoliciesReports` despite an ABAC scheme intended to isolate reports.
4. **Access-wall bypass via S3:** the org-wide posture CSV is read directly from the S3 bucket by a principal denied the EC2 report-read APIs, using the deterministic object path.
5. **ABAC defeat:** the `aws:ResourceTag`-gated Cancel/GetSummary controls are defeated because the creating action (`Start`) cannot enforce `aws:RequestTag` (tag-on-create gap).

---

## 2. Components, Assets, and Design

**What it is.** EC2 "Declarative Policies account status report" — an EC2 API family that generates an org-wide CSV of the current state of every account-level attribute that a *declarative policy* can enforce (IMDS defaults, serial-console access, image/snapshot block-public-access, allowed-images settings, VPC block-public-access, account VPC encryption control). Declarative policies are an **AWS Organizations** governance feature; the report is the "are my accounts actually in the baseline state" audit artifact.

**Interface.** EC2 Query/SDK API (`ec2-2016-11-15`), SigV4 IAM. Four actions:
- `StartDeclarativePoliciesReport` — Write. Inputs: `S3Bucket` (req), `S3Prefix` (opt), `TargetId` (req: root `r-ab12` / OU `ou-...` / account `123456789012`), `TagSpecification.N`, `DryRun`. Returns `reportId`.
- `CancelDeclarativePoliciesReport` **(TARGET)** — Write. Inputs: `ReportId` (req), `DryRun`. Returns `return` (bool). Only works while status=`running`.
- `DescribeDeclarativePoliciesReports` — List. Inputs: `ReportId.N` (opt), `MaxResults`, `NextToken`, `DryRun`. Returns `reportSet[]` (DeclarativePoliciesReport: reportId, status, s3Bucket, s3Prefix, targetId, startTime, endTime, TagSet).
- `GetDeclarativePoliciesReportSummary` — Read. Inputs: `ReportId` (req), `DryRun`. Returns attributeSummarySet, numberOfAccounts, numberOfFailedAccounts, s3Bucket, s3Prefix, targetId, start/endTime.

**Accounts / trust zones.**
- **Management account / delegated administrators** — the only callers allowed to `Start` (per Start API prereqs). The report ARN account = this account.
- **Member accounts** — subjects of the report (posture is read from each via the SLR).
- **AWS service plane** — two service principals: `ec2.amazonaws.com` (trusted-access identity) and `report.declarative-policies-ec2.amazonaws.com` (used as `aws:CalledViaLast` for the S3 PutObject delivery). **Hard-stop boundary.**
- **Customer S3 bucket** — governed by S3 IAM + bucket policy, a *different* reachability than the EC2 API that created the report.

**Resource & identifier.** `arn:${Partition}:ec2:${Region}:${Account}:declarative-policies-report/${DeclarativePoliciesReportId}`. Report-ID entropy/shape **undocumented → doc-gap** (enumerability unknown; check for embedded checksum). Report is Region-scoped (bucket must be same Region as the request). One report per org at a time.

**Untrusted-data entry / sink.** `S3Bucket` + `S3Prefix` are caller-controlled free-text that become an S3 object path: `s3://BUCKET/PREFIX/ec2_TARGETID_REPORTID_YYYYMMDDTHHMMZ.csv`.

```
                 Organizations trusted access (ec2.amazonaws.com)
                                    |
 [mgmt / delegated admin] --Start(TargetId=root/OU/acct, S3Bucket)--> EC2 control plane
                                    |                                      |
                                    |                 reads posture via SLR DeclarativePoliciesEC2Report
                                    |                 (ec2:Get*/Describe* Resource:* across member accts)
                                    v                                      v
                 report generated asynchronously (hours) -----> PutObject to customer S3
                   (delivery uses CALLER creds, aws:CalledViaLast =            bucket (deterministic path)
                    report.declarative-policies-ec2.amazonaws.com)
     Describe/GetSummary/Cancel  <---- ReportId ---->  (gated differently per action; see §4)
```

---

## 3. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| IAM principal in mgmt acct scoped (intent) to 1 OU | whole-org posture | `Start(TargetId=r-...)` with no org-scoping condition key | A report for a TargetId outside the principal's intended scope is generated — scope is caller-chosen and IAM-unconstrainable |
| Low-priv principal w/ Cancel only | org's in-flight report | `Cancel(ReportId)` flips running→cancelled | A compliance report the caller did not start is cancelled; repeated cancels keep the org from ever completing a report |
| Low-priv principal w/ Describe | all reports' metadata | `Describe` has no resource type / no ResourceTag gate | Caller enumerates ReportIds + S3 location + TargetId for reports an ABAC policy intended to hide |
| Principal denied EC2 report-read APIs | org posture CSV | `s3:GetObject` on deterministic path | Reading the CSV from S3 after being denied `GetDeclarativePoliciesReportSummary`/`Describe` |
| Report creator (controls S3Bucket/Prefix) | another account's / another prefix's S3 objects | caller-supplied bucket name (global ns) + free-text prefix in object path | Report delivered into a bucket/prefix the creator should not write, or overwriting an existing object |
| Any caller | AWS service-plane identity (`report.declarative-policies-ec2.amazonaws.com`) | `aws:CalledViaLast` delivery / trusted-access principal | **HARD STOP** — any credential/ARN of this principal surfacing |
| Member account / non-delegated principal | mgmt-account report resource | `Cancel`/`Describe`/`GetSummary` with report ARN | A non-management, non-delegated-admin caller affects/reads a report (parity gap vs the Start restriction) |

---

## 4. API / Interface Inventory + the central scoping asymmetry

| Action | Access | Resource type (required?) | Condition keys (from IAM ref) | Mutating | Callable by |
|---|---|---|---|---|---|
| `StartDeclarativePoliciesReport` | Write | **NONE** | **`ec2:Region` only** | Yes (creates) | mgmt acct / delegated admins (per API prereqs) |
| `CancelDeclarativePoliciesReport` **(target)** | Write | `declarative-policies-report*` | `aws:ResourceTag/${k}`, `ec2:ResourceTag/${k}`, `ec2:Region` | Yes | **not restated in docs — parity question** |
| `DescribeDeclarativePoliciesReports` | List | **NONE** | **`ec2:Region` only** | No | not restated |
| `GetDeclarativePoliciesReportSummary` | Read | `declarative-policies-report*` | `aws:ResourceTag/${k}`, `ec2:ResourceTag/${k}`, `ec2:Region` | No | not restated |
| `CreateTags` → `declarative-policies-report` | Tagging | `declarative-policies-report` | `aws:RequestTag`, `aws:ResourceTag`, `aws:TagKeys`, `ec2:CreateAction`, `ec2:Region`, `ec2:ResourceTag` | Yes | — |

**The asymmetry is the finding generator (Lens S/X/I):**
1. **No `TargetId`/org-scoping key anywhere.** You cannot author an IAM policy restricting *which* root/OU/account a principal may report on. `Start` is scopable only by `ec2:Region`.
2. **`Start` has no resource type and no `aws:RequestTag`/`aws:TagKeys`** — even though it accepts `TagSpecification.N`. So **tag-on-create cannot be enforced**: you cannot require a report be tagged, nor deny specific tag keys, at creation.
3. **Cancel & GetSummary are gated by `aws:ResourceTag`/`ec2:ResourceTag`** — but per (2) the creator controls whether the report carries any tag. An ABAC Deny keyed on a resource tag **fails open for untagged reports** and can be **self-widened** via `CreateTags` (which *does* accept `aws:RequestTag`).
4. **Describe has no resource type and no ResourceTag key** — it is **un-scopable per report**. Any holder lists every report's ReportId + S3 location + TargetId + status.

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — Un-constrainable report scope (TargetId) [Lens S / U, HIGH-priority least-privilege gap]
**Background.** `Start` creates an org-wide posture report for a caller-chosen `TargetId` (root / OU / account). The IAM reference shows `Start` carries **only `ec2:Region`** — no `TargetId`, no org/OU condition key.
**Security Concern.** AWS's own model says the report "scope is determined by the specified TargetId … or the entire AWS Organization." There is **no mechanism to bind a principal to a subset of the org**. A delegated administrator (or an IAM role in the management account granted `ec2:StartDeclarativePoliciesReport`) intended to audit one OU can set `TargetId=r-...` and enumerate the security posture (IMDS enforcement, public-access-block states, serial-console, VPC encryption) of **every account in the organization** — a high-value recon map of org-wide misconfiguration.
**High-level Test Scenarios.**
- Claim: *A principal whose policy grants `ec2:StartDeclarativePoliciesReport` cannot be restricted to a single OU/account.* → Oracle: no `Deny` can be written that blocks `TargetId=r-...` while allowing `TargetId=ou-...`; confirm with `iam:SimulateCustomPolicy` that no condition key references TargetId. Refute if a `TargetId`-like key exists in the live IAM model (doc may lag).
- Claim: *The posture summary exposes org structure.* → `GetDeclarativePoliciesReportSummary` returns `numberOfAccounts`/`numberOfFailedAccounts` and `attributeSummarySet` for the whole target → confirms org-wide read from one call.
**Doc evidence.** list_ec2.md Start block (`ec2:Region` only); Start API "scope … entire AWS Organization." **Severity-if-true:** Medium–High (least-privilege gap on a governance control; AWS-owned if considered a missing condition key — Tier-2 style, route `aws-security`). **Stop:** once the simulate shows no scoping key.

### Area 2 — Compliance-report denial via Cancel (the target action) [Lens L / X, HIGH]
**Background.** Only one report per org can run at a time; a report takes "several hours." `Cancel` flips `running→cancelled` and requires only the `declarative-policies-report` resource + optional `ResourceTag`/`Region`.
**Security Concern.** A principal holding `ec2:CancelDeclarativePoliciesReport` on `declarative-policies-report/*` (a natural wildcard grant) but **not** `Start` can cancel the organization's in-flight compliance report. Combined with Area 4 (Describe enumerates live ReportIds), the attacker needs no prior knowledge. Repeated/timed cancellation (cancel each new report shortly before the multi-hour completion) can **permanently deny** the org a completed status report — defeating a control auditors/Config/GuardRail workflows may depend on, with minimal footprint.
**High-level Test Scenarios.**
- Claim: *Cancel authorizes on `declarative-policies-report/*` without proving the caller started the report.* → Oracle: with a scoped role holding only Cancel (+Describe) on `*`, cancel a report started by a different principal; success = authz checks IAM+existence, not creator-identity.
- Claim: *Cancel's management/delegated-admin restriction is NOT enforced (parity gap).* → The Start API explicitly restricts callers to mgmt/delegated admins; Cancel's API page does **not** restate it. Oracle: a non-delegated principal in the management account (or a delegated-admin scoped elsewhere) successfully cancels. Route to Area 6.
- Adjacent: does cancelling mid-run still **bill**/leave a partial object? Does `error`/`cancelled` free the "one per org" lock immediately (enabling rapid re-cancel churn)?
**Doc evidence.** Cancel API "only cancel while running"; Start API "only one report per organization … at a time"; list_ec2.md Cancel block. **Severity-if-true:** cross-principal cancellation of a shared org control = High (integrity/availability of a compliance artifact). **Stop:** one confirmed cancel of a non-owned running report.

### Area 3 — ABAC defeat via tag-on-create gap + self-widening CreateTags [Lens I / S, MEDIUM–HIGH]
**Background.** Cancel/GetSummary are gated by `aws:ResourceTag`/`ec2:ResourceTag`, suggesting ABAC isolation (e.g. "only cancel reports tagged team=X"). But `Start` cannot enforce `aws:RequestTag`/`aws:TagKeys` (no resource type on the action), and `CreateTags` on the report **does** accept `aws:RequestTag`.
**Security Concern.** (a) **Fail-open on untagged:** a report created with no tags is not matched by a `aws:ResourceTag`-conditioned Deny → the control is bypassed by simply not tagging. (b) **Self-widen:** a holder of `CreateTags` can set the very tag an ABAC Allow keys on, then Cancel/GetSummary. (c) **Request-time gate absent:** you cannot force "every report must be tagged owner=${aws:username}".
**High-level Test Scenarios.**
- Claim: *A `Deny Cancel unless aws:ResourceTag/team == X` is inert against an untagged report.* → Oracle: Start a report without TagSpecification; confirm the Deny does not match (SimulateCustomPolicy with no resource tag).
- Claim: *A principal can `CreateTags` the report to satisfy its own ABAC Allow, then Cancel/GetSummary.* → Oracle: tag then act, under a scoped role.
**Doc evidence.** list_ec2.md: Start = no resource type/no RequestTag; Cancel/GetSummary = ResourceTag keys; CreateTags→declarative-policies-report accepts aws:RequestTag. **Severity-if-true:** Medium (High where ResourceTag is the sole access control). **Stop:** one confirmed untagged-bypass or self-tag-then-act.

### Area 4 — Unscoped report enumeration / metadata disclosure [Lens A, MEDIUM]
**Background.** `DescribeDeclarativePoliciesReports` has **no resource type and only `ec2:Region`** (Access level: List). It returns each report's `reportId`, `status`, `s3Bucket`, `s3Prefix`, `targetId`, times, tags.
**Security Concern.** It cannot be scoped per report. Any principal with the action learns: every live/complete ReportId (feeds Area 2 Cancel and Area 5 S3 read), the **exact S3 bucket+prefix** where posture CSVs land, and the **TargetId** (org/OU/account structure). This is the enumeration oracle that removes the "attacker must guess ReportId" precondition from every other lead.
**High-level Test Scenarios.**
- Claim: *A principal denied GetSummary/Cancel by ResourceTag can still list all reports (ReportId + S3 location + TargetId) via Describe.* → Oracle: scoped role with only `ec2:DescribeDeclarativePoliciesReports` returns the full `reportSet`.
- Adjacent (differential-error oracle): does `DescribeDeclarativePoliciesReports` with a **foreign/garbage ReportId.N** return empty vs error vs 500 — enumeration/existence oracle? Check for embedded checksum making fabricated IDs impossible (genuine-null candidate).
**Doc evidence.** list_ec2.md Describe block (no resource type); DeclarativePoliciesReport data type. **Severity-if-true:** Medium (metadata/structure disclosure + enabler). **Stop:** confirmed full-list under a report-scoped Deny.

### Area 5 — Posture CSV reachable via S3, bypassing the EC2 access wall [Lens T, MEDIUM–HIGH]
**Background.** The completed report is an org-wide posture CSV at a **deterministic path** `s3://BUCKET/PREFIX/ec2_TARGETID_REPORTID_YYYYMMDDTHHMMZ.csv`. Access is then governed by **S3 IAM / bucket policy**, not EC2 IAM.
**Security Concern.** A principal **explicitly denied** `ec2:GetDeclarativePoliciesReportSummary`/`Describe` can still read the full report if they hold `s3:GetObject` on the delivery bucket — the EC2-layer access control is silently bypassed at the storage layer. Bucket+prefix+TargetId come free from Area 4; the timestamp is the only unknown and is enumerable/listable. The CSV is **more** sensitive than the EC2 summary (per-account, per-attribute status across the whole org).
**High-level Test Scenarios.**
- Claim: *A role denied the EC2 report-read APIs reads the CSV via `s3:GetObject`.* → Oracle: prove the EC2 Deny + the S3 Allow in one run under a scoped role (canary report).
- Claim: *The object path is predictable enough to fetch without `ListBucket`.* → Oracle: reconstruct path from Describe output + reasonable timestamp window.
- Adjacent: is the delivered object encrypted with a CMK the reader lacks, or SSE-S3 (readable by any `s3:GetObject` holder)? Does report deletion/cancel cascade to the S3 object, or does a stale CSV linger (data outliving the control)?
**Doc evidence.** Describe/GetSummary "download it from the S3 bucket"; Start API S3 path structure. **Severity-if-true:** Medium–High (org posture disclosure bypassing intended EC2 wall; owner-to-fix shared — AWS owns delivery default, customer owns bucket IAM). **Stop:** one CSV read under an EC2-denied role.

### Area 6 — Action-family authorization parity: Start-restricted, siblings silent [Lens X, MEDIUM–HIGH]
**Background.** `Start` documents "can only be called by the management account or delegated administrators." The Cancel/Describe/GetSummary API pages **do not restate** any caller restriction.
**Security Concern.** If the mgmt/delegated-admin gate is enforced only on `Start` (the write that triggers trusted-access + org traversal) and the sibling read/cancel actions rely solely on standard IAM against the report ARN, then a principal who is **not** a delegated admin — but has the EC2 action and reaches the report ARN (same account) — can Cancel (Area 2) or read metadata/summary (Areas 4–5) without the org-level gate the feature's design implies.
**High-level Test Scenarios.**
- Claim: *A non-delegated-admin principal in the management account can Cancel/Describe/GetSummary.* → Oracle: call each under such a principal; success = parity gap.
- Claim: *A delegated admin scoped (by org) to OU-A can Cancel/read a report whose TargetId is OU-B / root.* → Oracle: cross-OU delegated-admin action succeeds (chains with Area 1's no-TargetId-key).
**Doc evidence.** Start API prereqs vs silent Cancel/Describe/GetSummary pages. **Severity-if-true:** High if a non-admin affects/reads an org-wide report. **Stop:** one confirmed sibling call by a caller the Start gate would reject.

### Area 7 — S3 delivery confused-deputy / predictable-name write [Lens B / EE / R, audit + MEDIUM]
**Background.** The AWS-published sample bucket policy grants `s3:PutObject` to a specific `identity_ARN` with `Condition StringEquals aws:CalledViaLast report.declarative-policies-ec2.amazonaws.com`. Delivery uses the **caller's** credentials via CalledVia, not a service role.
**Security Concern / Scenarios.**
- Claim: *`S3Prefix` free-text enables path control into unintended key space* (e.g. prefix `../`-style or a prefix pointing at another team's area in the same bucket). → Oracle: Start with a crafted `S3Prefix`; inspect resulting object key. Severity: Low–Medium (own-bucket; High only if it overwrites a sibling's object the caller couldn't otherwise write).
- Claim: *`S3Bucket` (global namespace) lets a report be delivered to a bucket the caller doesn't own but which carries the delivery policy with a loose principal* (confused-deputy). → Oracle: name a victim bucket whose policy allows `*`/broad principal + the CalledVia condition; write lands cross-account. The sample pins `identity_ARN`, so refute unless a customer copies it with a wildcard principal.
- Claim (EE): *Pre-create the predictably-named bucket the mgmt account will use on regional expansion / first use.* → doc-gap; only if any auto-bucket naming exists.
- **Lens R audit — SLR policy `DeclarativePoliciesEC2Report` (v2, 2026-07-03):** grants 8 **read-only** `ec2:Get*/Describe*` account-posture actions on `Resource:*`, attached to a service-linked role, customer-uneditable. Statement-by-statement: no mutating action, no `iam:PassRole`, no data-plane write → **no privesc path**; `Resource:*` is unavoidable (account-setting Gets have no resource-level ARN). **Near-null for Lens R privesc.** Note for follow-up: diff v1→v2 (what attribute coverage was added 2026-07-03) and confirm the SLR's trust policy only trusts `ec2.amazonaws.com`.
**Doc evidence.** Start API sample S3 policy + path; managed-policy md. **Severity-if-true:** confused-deputy cross-account write = High (only if a customer bucket policy is loose); prefix misuse = Low–Medium; SLR = Informational.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Report scope cannot be IAM-bound to an OU/account | `Start` TargetId | (none — no TargetId condition key) |
| Cross-principal cancellation of org's in-flight report | `Cancel` | `declarative-policies-report` resource + ResourceTag (no creator-identity check) |
| Perma-deny completed report (cancel-churn) | `Cancel` + "one per org" lock | report-run uniqueness lock |
| ABAC Deny inert on untagged report / self-widen | `Start`(no RequestTag) + `CreateTags` | `aws:ResourceTag` on Cancel/GetSummary |
| Full report enumeration incl. S3 location + TargetId | `Describe` (no resource type) | `ec2:Region` only |
| Posture CSV read bypassing EC2 APIs | S3 delivery object | bucket policy / S3 IAM (separate from EC2 IAM) |
| Non-admin / cross-OU sibling calls | Cancel/Describe/GetSummary | mgmt/delegated-admin gate (documented only on Start) |
| Confused-deputy S3 write | `S3Bucket`/`S3Prefix` + CalledVia | `aws:CalledViaLast` condition + pinned `identity_ARN` in sample policy |
| Service-plane identity exposure | `report.declarative-policies-ec2.amazonaws.com` | **HARD STOP — disclosure** |

---

## 7. Out-of-Scope Risk Categories
- The SLR `DeclarativePoliciesEC2Report`'s `Resource:*` on read-only account-setting Gets — unavoidable, read-only, no privesc → **not** a finding (noted as Lens R near-null).
- A **customer-authored** loose S3 bucket policy (wildcard principal) is a customer footgun; only the AWS-published sample's correctness is in scope.
- Single-tenant self-DoS (an admin cancelling their own org's report) — the in-scope variant is cross-principal / non-creator cancellation.
- Declarative-policy *enforcement* behavior on member accounts (that is the Organizations policy engine, a different surface).
- IMDS/attribute values themselves (the report merely reports them).
- Correctness of the report CSV contents (product accuracy, not a security boundary).

## 8. Null hypotheses / doc gaps
- **ReportId entropy/shape — doc-gap.** Enumerability (Area 2/4/5) hinges on whether ReportIds are guessable and whether a foreign/fabricated ID is rejected by an embedded checksum. Confirm the ID pattern from a live `Start` response or the IAM ARN resource-id regex before relying on guessing.
- **Exact required IAM permission list — doc-gap.** The Organizations `orgs_manage_policies_declarative_status-report` page (the authoritative "required IAM permissions" source) is JS-rendered and was not retrievable offline/online here. Confirm the full `ec2:`/`organizations:`/`s3:` set and whether `organizations:` permissions (e.g. delegated-admin registration) gate Cancel/Describe/GetSummary — this directly settles Area 6 (parity).
- **Caller restriction on Cancel/Describe/GetSummary — doc-gap** (only Start restates it). Area 6 is the test.
- **Cross-account IDOR (Lens A pure form) — likely null:** the report ARN embeds the creating (management) account and Region; a member-account caller naming that ARN is a standard cross-account denial. Treated as bounded, not a lead, unless the service resolves ReportId globally ignoring the ARN account (worth a single confirm during Area 6).
- **Lenses that did not fire:** F (no translation/parser — CSV is service-generated output, not attacker-parsed input), K (no LLM/agent), W (no attestation), Y/BB/CC/DD/FF (no HTTP edge/authorizer/cache/JWT layer — this is plain SigV4 EC2 API), V/D (no customer ENI/data-plane), H (no customer CMK on the EC2 action; revisit only via Area 5's S3 SSE). Each checked against the four API pages + IAM reference; marked null because the mechanism is absent, not unexamined.

---
**Chain to watch (end-to-end, rate at the end-severity):** Area 4 (Describe → ReportId + S3 bucket/prefix + TargetId, unscoped) → Area 2 (Cancel that ReportId → deny org compliance report) **and/or** Area 5 (read the posture CSV from S3 bypassing the EC2 wall). Entry is a List permission; end is org-wide posture disclosure + compliance-control denial.
