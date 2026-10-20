# EC2 `ModifyInstanceCreditSpecification` (Burstable-Credit Control Surface) — Attack Research Plan

**Source of leads:** Target doc page `https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyInstanceCreditSpecification_section.html` (SDK/CLI code example) plus the mechanism it exercises, fetched live from `docs.aws.amazon.com` on 2026-10-19 and cross-checked against the offline mirror at `/work/aws-docs` (the target example page itself was **absent** from the local mirror — a sync gap — and was read online only; the IAM SAR and AWS-managed-policy JSON were verified online == mirror, byte-for-byte).
**Status:** documentation-derived hypotheses only; nothing has been tested against a live AWS account. This is the plan a hunter executes later.
**Analysis:** 3 passes — primary surface (this doc), authorization/IAM deep-dive, billing/resilience/state-machine deep-dive.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Severity → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to AWS's **own service plane**, stop, preserve evidence, flag for AWS-Security disclosure. *Note: this surface is entirely account-scoped billing/state — no service-plane reach is expected here; if one appears, it is a surprise worth stopping for.*
- **Methodology caveat used throughout:** `DryRunOperation` is a caller-IAM pre-flight check evaluated **before** resource-state resolution. It is **not** an existence or ownership oracle. Only non-dry-run per-item error codes are valid oracles on this surface.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Cross-account credit mutation** — flip the `CpuCredits` mode of a burstable instance owned by *another account* via `ModifyInstanceCreditSpecification` (naming its `i-…` id directly) → Critical if it succeeds. *(Expected to fail — EC2's per-account instance-ARN model — but it is the headline objective and the thing the batch/error-oracle leads probe around.)*
2. **Cross-account existence enumeration** — use the batch per-item error differential (`InvalidInstanceID.NotFound` vs `IncorrectInstanceState` vs whole-call `UnauthorizedOperation`) to confirm whether a known foreign `i-…` id exists.
3. **Intra-account cost-ceiling removal / financial DoS** — as a principal who should not control cost posture, flip instances (or the account/region default) to `unlimited` and drive surplus charges (`CPUSurplusCreditsCharged`).
4. **Tag-guardrail evasion** — achieve a credit change the per-instance tag Deny was meant to block, via the account-level default action or the launch path.
5. **AWS-managed-policy privilege-reach** — show a principal holding a conceptually-"operational" AWS-managed policy (`job-function/SystemAdministrator`) wields the unscopeable account-wide default-credit action.
6. **State/accounting edge cases** — surplus-charge timing via rapid `unlimited↔standard` toggling; T2 launch-credit stripping as griefing; async multi-AZ rollout race.

---

## 2. Components, Assets, and Design

**What this is.** The target page is a *code example* (AWS CLI + PowerShell) for the EC2 control-plane action **`ModifyInstanceCreditSpecification`**, which sets the CPU-credit billing mode (`standard` | `unlimited`) of a **burstable performance instance** (families T2, T3, T3a, T4g, T8i). There is no new service here — the attack surface is the **burstable-credit control API cluster** and its IAM/billing semantics.

**Customer-facing interface.** EC2 Query/JSON control-plane API over HTTPS (`ec2.<region>.amazonaws.com`), SigV4 IAM auth. No data-plane, no network fleet, no parser, no untrusted-content path — the request carries only scalar `i-…` ids and the enum string `standard|unlimited`.

**Resource & identifier shape.** The resource is an EC2 **instance**, ARN `arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}`. `InstanceId` = `i-` + 17 hex chars, **no documented checksum** (a fabricated foreign id is cheap to try; a *real* foreign id is confirmable-if-known, not enumerable blind). `CpuCredits` ∈ {`standard`,`unlimited`} (case-sensitive per docs). `ModifyDefaultCreditSpecification` names no instance — only `InstanceFamily` ∈ {`t2`,`t3`,`t3a`,`t4g`} + `CpuCredits`.

**Identity / privilege.** Pure SigV4 IAM. No roles assumed, no STS vending, no credential chaining, no hidden admin identity. Authorization is per-account standard IAM evaluation.

**Asset at risk = money + (minor) performance posture.** `unlimited` removes the baseline CPU throttle; sustained >baseline burst is billed at a flat per-vCPU-hour surplus rate. The account-level default governs **every future** burstable launch in a region+family. There is no spend-cap/quota/approval parameter anywhere in the API — the only gate on cost is IAM.

**ASCII surface map:**
```
                         ┌─────────────────────────────────────────────┐
 IAM principal ──SigV4──►│ EC2 control plane (ec2.<region>.amazonaws)   │
 (caller in account A)   │                                             │
                         │  ModifyInstanceCreditSpecification  [instance* scoped, Write]
                         │      └─ InstanceCreditSpecification.N[{InstanceId, CpuCredits}]
                         │  DescribeInstanceCreditSpecifications [no resource, List]
                         │  ModifyDefaultCreditSpecification   [NO resource, Region-only, Write]
                         │      └─ InstanceFamily + CpuCredits  ──► account+region default
                         │  GetDefaultCreditSpecification      [no resource, Read]
                         └───────────────┬─────────────────────────────┘
                                         │ sets billing mode
                                         ▼
                      Burstable instance (T2/T3/T3a/T4g/T8i) ── unlimited ──► surplus charges ($)
                                         ▲                                   (CPUSurplusCreditsCharged)
          also set at create via RunInstances.CreditSpecification (aws:RequestTag path)
          twin surfaces: CFN AWS::EC2::{Instance,LaunchTemplate}.CreditSpecification;
                         WorkSpaces-Instances CreditSpecificationRequest (wraps EC2)
```

---

## 3. API / Interface Inventory

| Name | Method | New/Exist | Mutating | Int/Ext | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ModifyInstanceCreditSpecification` | POST (Query) | Existing | **Mutating** | External | Set `standard`/`unlimited` on running/stopped burstable instance(s), **batch array** | Yes (signed) | IAM `ec2:ModifyInstanceCreditSpecification`, **instance*-scopable** (tag/type/tenancy) | Target action. `ClientToken`+`DryRun`. Partial-failure response split. |
| `ModifyDefaultCreditSpecification` | POST | Existing | **Mutating** | External | Set account+region **default** per family | Yes | IAM `ec2:ModifyDefaultCreditSpecification`, **NO resource type — `ec2:Region` only** | **Unscopeable.** Async, ≤5 min all-AZ. Rate-limited: once/5 min, 4×/24 h. |
| `GetDefaultCreditSpecification` | POST | Existing | Non-mut | External | Read account/region default | Yes | IAM, no resource type, `ec2:Region` | Read. |
| `DescribeInstanceCreditSpecifications` | POST | Existing | Non-mut | External | Read per-instance credit mode | Yes | IAM `ec2:Describe…`, **no resource type — tenant-wide read** | Non-burstable id → returns `standard` (no error). Terminated instances linger ≤~1 h. No-IDs → returns all `unlimited`. |
| `RunInstances` (`CreditSpecification`) | POST | Existing | Mutating | External | Set credit mode **at launch** | Yes | IAM `ec2:RunInstances`, `aws:RequestTag` (not `ResourceTag`) | Create-half of the same control. Twin path for guardrail evasion. |
| `ModifyInstanceAttribute` | POST | Existing | Mutating | External | **No `creditSpecification` attribute** | Yes | IAM | **Not a twin — refuted** (enum has no credit value). |

**Undocumented/hidden-knob sweep:** No console-hidden auth-weakening parameter found. The salient "knob" is a *semantic* one: there is **no `ec2:CpuCredits`/`ec2:CreditSpecification` condition key** — the dangerous value (`unlimited`) cannot be gated by IAM, only the resource can.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| IAM principal in account A | Burstable instance in **account B** | `ModifyInstanceCreditSpecification` naming B's `i-…` directly | A credit change applied to a B-owned instance (per `DescribeInstanceCreditSpecifications` + CloudTrail). **Expected to fail**; if it succeeds = Critical, HARD-STOP-adjacent. |
| Batch item lacking authz | Other items / foreign id existence | Per-item vs top-level error handling | A foreign/unauthorized `i-…` returns `IncorrectInstanceState` (service resolved it) vs `InvalidInstanceID.NotFound` (truly absent) → **cross-account existence oracle**. |
| Principal denied per-instance Modify (tag Deny) | Account+region credit default | `ModifyDefaultCreditSpecification` (no resource/tag context) | Default flips to `unlimited` despite a per-instance tag Deny → **tag-guardrail evasion**, every future launch inherits it. |
| Principal w/ `ec2:ModifyInstanceCreditSpecification` but no cost mandate | The instance owner's bill | Single synchronous Write, no spend-cap | `CPUSurplusCreditsCharged` rises, traceable in CloudTrail to a credit flip the owner didn't request → **intra-account cost DoS**. |
| Holder of AWS-managed `SystemAdministrator` | Account-wide credit posture | `ec2:Modify*` wildcard (unconditioned) in the managed policy | Principal with only that policy calls `ModifyDefaultCreditSpecification` successfully → **AWS-authored over-grant**. |
| `RunInstances` caller during ≤5 min rollout | AZ-level default consistency | Timing race | New instance's mode disagrees with post-rollout `GetDefaultCreditSpecification` → race to dodge/force a default. |
| Any customer surface | **AWS service plane** | — | **None expected** — pure account-scoped billing/state. Any service-plane credential = HARD STOP. |

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — AWS-managed-policy over-grant: `SystemAdministrator` reaches the unscopeable default (Lens R + E + S) — HIGHEST VALUE
**Background:** `ModifyInstanceCreditSpecification` is properly scopable to an instance ARN (supports `ec2:ResourceTag`, `ec2:InstanceType`, `ec2:Tenancy`, etc.), but `ModifyDefaultCreditSpecification` has **no resource type at all** — its only condition key is `ec2:Region`, so it cannot be constrained by tag/instance/family in any permission boundary or SCP-equivalent beyond region.
**Security Concern:** The AWS-managed `job-function/SystemAdministrator` policy (ARN `arn:aws:iam::aws:policy/job-function/SystemAdministrator`, verified v12, online==mirror) is an otherwise-curated explicit allowlist that drops in a bare **`"ec2:Modify*"`, `Resource:"*"`, no `Condition`**. This silently grants both `ModifyInstanceCreditSpecification` (any instance, any tag) **and** the unscopeable `ModifyDefaultCreditSpecification` to anyone holding what reads as an "operational," not "cost-control," role. Because the default action has no tag dimension, a security team that notices the wildcard **cannot** contain it with per-instance tag boundaries. This is AWS-authored and copy-attached verbatim → **in scope, Tier-2 disclosure, not a customer footgun.**
**High-level Test Scenarios:**
- Attach **only** `job-function/SystemAdministrator` to a scoped canary principal. Confirm `ModifyDefaultCreditSpecification(InstanceFamily=t3, CpuCredits=unlimited)` succeeds and `ModifyInstanceCreditSpecification` succeeds against an instance the principal does not own/tag. Prove under the scoped role (never the over-privileged tester). `iam:SimulatePrincipalPolicy` is the safe first oracle.
- Also check `AmazonEC2FullAccess` (`ec2:*`) and `PowerUserAccess` (`NotAction` excludes only iam/organizations/account) as the ceilings — expected, documented for completeness.
**Doc evidence:** SAR `list_ec2.html` rows for both actions; `aws-managed-policy/latest/reference/SystemAdministrator.html` (`ec2:Modify*` line). **Severity-if-true:** Medium–High (intra-account account-wide cost blast radius inside a managed policy; `ModifyDefaultCreditSpecification` portion is uncontainable by tags). **Stop:** once the scoped-role call succeeds, that is the PoC.

### Area 2 — Intra-account cost-ceiling removal / financial DoS (Lens L + A)
**Background:** `unlimited` lets an instance spend surplus credits beyond baseline; sustained >baseline is billed at a flat per-vCPU-hour rate (`unlimited-mode-concepts.html`: *"billed for the additional usage at a flat additional rate per vCPU-hour"*). There is **no quota, approval, MFA, or spend-cap** in the API — only IAM gates it.
**Security Concern:** A principal holding `ec2:ModifyInstanceCreditSpecification` (e.g., via an over-broad `ec2:Modify*`), without being the cost owner, can flip instances to `unlimited` and drive unbounded surplus charges. The action name gives a policy author no signal it is cost-unbounding. There is **no `ec2:CpuCredits` condition key** to Deny the dangerous *value* — the guardrail can only be written against the resource, not the setting.
**High-level Test Scenarios:**
- Flip a canary instance to `unlimited`; drive CPU >baseline; observe `CPUSurplusCreditBalance` / `CPUSurplusCreditsCharged` rise, correlated via CloudTrail to the `ModifyInstanceCreditSpecification` event the owner did not request.
- Confirm no `ec2:CpuCredits`/`ec2:CreditSpecification` key exists in `list_ec2.html` condition-key table (anchor `list_ec2-policy-keys`) → a native "block unlimited" Deny is impossible; only an SCP/Config-rule proxy on tags works.
**Doc evidence:** `burstable-performance-instances-unlimited-mode-concepts.html` (surplus billing, triggers); SAR condition-key table (absence of a value key). **Severity-if-true:** Medium–High (intra-account cost DoS; a design-level guardrail gap, AWS-owned since no value key exists). **Stop:** one owner-unauthorized flip with a measurable `CPUSurplusCreditsCharged` delta.

### Area 3 — Account/region default: blast radius + tag-guardrail evasion, bounded by a rate limit (Lens A + S + U)
**Background:** One `ModifyDefaultCreditSpecification` call sets the default for **all future** burstable launches of one family in a region (*"All new burstable performance instances in the account launch using the default credit option"*). It is async, all-AZ within 5 min, and **rate-limited: once per rolling 5-min period, ≤4× per rolling 24 h** (how-to page "Consideration" callout).
**Security Concern:** Because the action is unscopeable (Area 1), a principal **denied** per-instance Modify by a tag Deny can still flip the account-wide default to `unlimited` — a durable, tag-condition-immune cost-posture persistence mechanism. The rate limit caps *repeated* flapping but a single call still changes the default until reverted (within the same 4/day budget).
**High-level Test Scenarios:**
- Grant `ModifyDefaultCreditSpecification`, Deny `ModifyInstanceCreditSpecification` on all tagged instances. Confirm the default flip succeeds despite the Deny; launch a new `t3.micro` with no `--credit-specification` and confirm it comes up `unlimited`.
- Probe the rate limit: 2 calls <5 min apart (same family/region) → is the 2nd throttled, and with what code? (The specific error is **undocumented** — doc-gap; `Errors` points only to `CommonErrors`.) Attempt a 5th change in 24 h.
**Doc evidence:** `API_ModifyDefaultCreditSpecification.html`; `burstable-performance-instances-how-to.html` rate-limit callout; SAR (no resource type). **Severity-if-true:** Medium–High (uncontainable account-wide default flip evading the one scoping mechanism the sibling supports). **Stop:** default flip succeeds under the instance-level Deny.

### Area 4 — Cross-account targeting & batch existence-enumeration oracle (Lens A, oracle variant)
**Background:** The request is a **batch array** of `{InstanceId, CpuCredits}`; the response splits `successfulInstanceCreditSpecificationSet` vs `unsuccessfulInstanceCreditSpecificationSet`. The documented per-item error enum is **only**: `InvalidInstanceID.Malformed | InvalidInstanceID.NotFound | IncorrectInstanceState | InstanceCreditSpecification.NotSupported` (`API_UnsuccessfulInstanceCreditSpecificationItemError.html`) — notably **no `UnauthorizedOperation`/`AccessDenied`** code in the per-item set.
**Security Concern:** This asymmetry creates an ambiguous IAM-boundary seam. Two questions: (a) Does naming a **foreign-account** `i-…` ever mutate it (expected No — Objective 1)? (b) Does an authz-denied/foreign id fold into the unsuccessful set as `InvalidInstanceID.NotFound` (fused with genuinely-absent → **no leak**), or produce a different code / top-level failure? If a *real* foreign-owned id returns `IncorrectInstanceState` (service resolved + read state) while a *fabricated* id returns `InvalidInstanceID.NotFound`, that differential is a **cross-account existence oracle** (confirm-a-known-id, not blind-enumerate, since ids have 17 hex chars/no checksum).
**High-level Test Scenarios (needs 2 tester-owned accounts — synthetic canary, no third-party boundary):**
- Batch of {owned burstable id, syntactically-valid nonexistent id, real id in a 2nd tester account}. Compare per-item codes and whether one bad/foreign id fails the **whole** call (masking the legitimate item = minor availability finding, not a leak).
- Compare against `DescribeInstanceCreditSpecifications` quirks: a non-burstable id silently returns `standard` (no error) and terminated instances linger ≤~1 h — map these as additional differential-response signals.
**Doc evidence:** `API_ModifyInstanceCreditSpecification.html` (response split), `...ItemError.html` (4-value enum), `API_DescribeInstanceCreditSpecifications.html` (non-burstable→standard, terminated-linger). **Severity-if-true:** Low–Medium (existence-only, no data/control; capped to confirming suspected ids). **Stop:** once the code differential is characterized. **This is the top doc-gap — not answerable from docs alone.**

### Area 5 — State-transition / billing-trigger abuse (Lens A/P)
**Background:** `unlimited→standard` **immediately charges** `CPUSurplusCreditBalance`; `standard→unlimited` carries over `CPUCreditBalance` and (for T2) **strips launch credits every transition**. The per-instance Modify action has **no documented rate limit** (docs say "at any time") — unlike the default action.
**Security Concern:** Rapid `standard↔unlimited` toggling could force surplus settlement at a chosen moment (e.g., before a billing boundary), or repeatedly strip a shared T2 instance's launch credits as an availability/performance **griefing** primitive (no billing needed). Open question whether toggling produces double/under-charge accounting edge cases exploitable at scale (an AWS revenue-integrity concern).
**High-level Test Scenarios:**
- Script N toggles on a canary vs an untoggled control under identical load; diff `CPUSurplusCreditsCharged` for over/under-charge.
- Confirm whether launch credits are stripped on **every** `standard→unlimited` transition (per doc) or once per lifetime. Probe for any undocumented per-instance throttle (`RequestLimitExceeded`/`Throttling`).
**Doc evidence:** `unlimited-mode-concepts.html` ("What happens to credits when switching"; three surplus-charge triggers). **Severity-if-true:** Low–Medium (self/intra-account; higher only if a systemic under-charge is found → report to AWS). **Stop:** accounting delta characterized.

### Area 6 — Async multi-AZ rollout race (Lens L/U)
**Background:** `ModifyDefaultCreditSpecification` is async; *"if instances are launched during this operation, they might not get the new credit option until the zone is updated"* — up to 5 min, no per-AZ visibility API (only `GetDefaultCreditSpecification` polling).
**Security Concern:** During the window AZs disagree. A caller can **race** a `RunInstances` into a not-yet-updated AZ to grab the old default — e.g., dodge a just-tightened `standard` default to obtain `unlimited` even when direct Modify is IAM-denied; or automation silently gets a stale mode (reads as a service defect).
**High-level Test Scenarios:** Issue the default change, then poll `GetDefaultCreditSpecification` while launching across AZs (no `--credit-specification`); record per-instance AZ/timestamp/resulting mode; a mismatch vs the already-"updated" account value is the race signal.
**Doc evidence:** `API_ModifyDefaultCreditSpecification.html` (async/5-min/all-AZ paragraph). **Severity-if-true:** Medium (documented, self-heals ≤5 min, no tenant crossing). **Stop:** one documented AZ/account-value mismatch.

### Area 7 — Idempotency `ClientToken` scope & collision (Lens M)
**Background:** `ClientToken` = ≤64 ASCII, **Regional** idempotency; same token+same params → no-op success; same token+different params → `IdempotentParameterMismatch` (`Run_Instance_Idempotency.html`). The `InstanceId` is a parameter inside the array.
**Security Concern:** The token is not documented as principal-bound. CloudTrail logs request parameters (incl. `ClientToken`). Question: is the idempotency store per-principal or per-account within a region? If per-account, a principal observing another's `ClientToken` could replay with matching params for a silent no-op "success" (low impact — the effect already happened; an info-disclosure-via-CloudTrail angle). Any cross-principal *suppression* is blocked by `IdempotentParameterMismatch` whenever the instance id differs → no divergent-state risk here.
**High-level Test Scenarios:** Two same-account principals, same token, different instance ids → expect `IdempotentParameterMismatch`, confirm no silent suppression. Test per-principal vs per-account scoping via CloudTrail correlation.
**Doc evidence:** `Run_Instance_Idempotency.html` (Regional type, mismatch error). **Severity-if-true:** Low (doc-gap: token scoping boundary unstated). **Stop:** scoping boundary characterized.

### Area 8 — Action-family / cross-service twin parity (Lens X) — mostly refuted, one open adjacency
**Background/Concern:** Verify no sibling path achieves the credit change that a per-instance Deny blocks.
- `ModifyInstanceAttribute` — **refuted**: enum has no `creditSpecification` value; cannot be a bypass.
- `RunInstances.CreditSpecification` — **expected asymmetry, not a flaw**: authorized via `aws:RequestTag` (not `ec2:ResourceTag`), so a `ResourceTag`-keyed Deny on Modify does not cover a brand-new `unlimited` launch unless the Deny is also written against `RunInstances`/`aws:RequestTag`. Flag as a least-priv authoring footgun (Low).
- **Open adjacency — cross-service wrappers:** `CreditSpecification`/`CreditSpecificationRequest` also appears in **WorkSpaces-Instances** (`API_CreateWorkspaceInstance` / `API_CreditSpecificationRequest`) and **CloudFormation** (`AWS::EC2::Instance` / `AWS::EC2::LaunchTemplate` `CreditSpecification`). Question: do these wrappers let a caller set `unlimited` under a *different* IAM action (`workspaces-instances:*`, CFN role) than `ec2:ModifyInstanceCreditSpecification`/`ec2:RunInstances`, bypassing an EC2-scoped Deny? (Found via mirror grep; worth a parity check.)
**Doc evidence:** `API_ModifyInstanceAttribute.html` enum; `RunInstances` `CreditSpecification` param; mirror grep hits under `workspaces-instances/` and `AWSCloudFormation/.../creditspecification`. **Severity-if-true:** Low (footgun) → Medium if a cross-service wrapper genuinely evades an EC2-action Deny. **Stop:** parity confirmed/refuted per path.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account credit flip | `ModifyInstanceCreditSpecification` | Per-account instance-ARN IAM model (`list_ec2.html` instance resource type) |
| Cross-account existence enumeration | Batch per-item errors | 4-value error enum with no authz code (`…ItemError.html`) — test if authz fuses into NotFound |
| Intra-account cost DoS | `unlimited` mode | IAM only — **no spend-cap, no `ec2:CpuCredits` value key** (SAR) |
| Tag-guardrail evasion | `ModifyDefaultCreditSpecification` | None by tag — action is resource-less, `ec2:Region`-only (SAR) |
| AWS-managed over-grant | `job-function/SystemAdministrator` | Policy's own `ec2:Modify*` wildcard, `Resource:*`, no Condition |
| Surplus-charge timing / launch-credit strip | state transitions | Per-instance action has no documented rate limit |
| Rollout race | async default, ≤5 min | `GetDefaultCreditSpecification` polling (only consistency check) |
| Idempotency replay/suppression | `ClientToken` | `IdempotentParameterMismatch` on differing params (Regional scope) |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Cross-account instance mutation assumed-broken** — out of scope to assume; EC2's per-account instance-ARN model applies. It is an Objective to *test*, not a presumed finding.
- **Customer-authored over-broad IAM** (a customer who writes their own `ec2:Modify*`) — Low / least-privilege footgun, out of scope. *(The `SystemAdministrator` case is **in scope** precisely because AWS authored it — Area 1.)*
- **Single-tenant self-inflicted billing surprise** — Low / out of scope.
- **IMDS / host internals of the managed instance** — not reachable from this control API; out of scope.
- **Service-plane / shared-fleet reach** — none exists on this surface; HARD STOP if it ever appears.
- **DNS rebinding / network lenses** — N/A, no server-side fetch or network namespace here.

---

## 8. Null hypotheses / doc gaps (lenses that did not fire, with pages checked)

**Lenses N/A (triggers absent — pages checked):**
- **B / C (PassRole, credential vending, STS session scope)** — N/A. No `roleArn`/`PassRole`/`AssumeRole`/`ProvidedContext` on any of the 4 actions. Checked all API-reference pages + `Run_Instance_Idempotency`.
- **D / V (data→control plane, network segmentation, ENI)** — N/A. Pure control-plane API; no ENI/VPC/socket/host process. Checked API refs + unlimited-mode concepts.
- **F (translation-layer / wire-protocol / parser injection)** — N/A. Only scalar `i-…` ids and a 2-value enum; no parser/translator. Checked `InstanceCreditSpecificationRequest`.
- **G (SSRF)** — N/A. No field the service dereferences/fetches. Checked the target example page + all 4 API refs + how-to + unlimited-mode concepts — no `*Url`/`*Uri`/webhook/import/domain-validation field.
- **H / W (KMS / encryption-context / attestation)** — N/A. No KMS key, encryption context, or PCR/attestation parameter. Checked API refs.
- **J (OAuth / 3P linking)** — N/A. No 3P integration. Checked how-to.
- **K (prompt injection / LLM)** — N/A. No LLM/agent/GenAI in pipeline. Checked all target pages.
- **P (identity proofing / registration)** — N/A as a workflow; nearest trigger (`ClientToken`) handled under Lens M (Area 7). Checked how-to + idempotency page.
- **Q (file / rich-content upload)** — N/A. No upload/blob/image/attachment field. Checked API refs.
- **T (cross-service secret reachability)** — N/A. The action generates/persists no secret. Checked API refs + how-to.
- **Y (transport/TLS/sig)** — generic EC2 HTTPS+SigV4; no action-specific transport claim; Low/not specific. Checked API refs.
- **AA (share/revoke lifecycle)** — N/A. The account default is not a cross-account share; no `launchPermission`/RAM/grant. Checked `ModifyDefaultCreditSpecification`.
- **N, BB, CC, DD, EE, FF** — N/A. No namespace migration, multi-parser/authorizer edge, trusted-upstream header, caching layer, predictable-name land-grab, or JWT/OIDC validation on this surface. Checked target example page + API refs.
- **O (audit-log evasion)** — minimal: these are standard CloudTrail-logged control-plane calls; no action-specific logging gap documented. Informational.
- **R / S partial** — **fired** (Area 1/3): the *AWS-managed* `SystemAdministrator` policy is the artifact. No sample IAM-policy JSON / CFN / runbook block is printed on the burstable-credit *doc* pages themselves (checked target example + how-to + 4 API refs), so the Lens-R artifact is the managed policy, resolved via `aws-managed-policy` reference.

**Highest-priority doc gaps requiring live confirmation (hunter closes these first):**
1. **Mixed-authorization batch behavior** of `ModifyInstanceCreditSpecification` (Area 4) — decides whether a cross-account existence oracle exists. Undocumented.
2. **Per-instance rate limit** on `ModifyInstanceCreditSpecification` toggling (Area 5) — docs say "at any time," no number. Undocumented.
3. **`ClientToken` scoping** — per-principal vs per-account within a region (Area 7). Idempotency page states only "Regional."
4. **Error code returned when hitting the `ModifyDefaultCreditSpecification` rate limit** (Area 3) — not in the documented `CommonErrors`.
5. **Cross-service wrapper parity** — whether WorkSpaces-Instances / CFN `CreditSpecification` paths evade an EC2-action Deny (Area 8).

---

### Key pages for the hunter to re-verify (online; swap `.html`→`.md` for markdown)
- Target: `ec2/latest/devguide/example_ec2_ModifyInstanceCreditSpecification_section.html` (CLI/PowerShell example — **absent from local mirror**)
- `AWSEC2/latest/APIReference/API_ModifyInstanceCreditSpecification.html`, `API_InstanceCreditSpecificationRequest.html`, `API_UnsuccessfulInstanceCreditSpecificationItem.html` / `...Error.html`
- `AWSEC2/latest/APIReference/API_ModifyDefaultCreditSpecification.html`, `API_GetDefaultCreditSpecification.html`, `API_DescribeInstanceCreditSpecifications.html`, `Run_Instance_Idempotency.html`
- `AWSEC2/latest/UserGuide/burstable-performance-instances-unlimited-mode-concepts.html`, `...-how-to.html` (rate-limit callout)
- `service-authorization/latest/reference/list_ec2.html` (action rows; condition-key table — note correct path is `list_ec2`, not `list_amazonec2`)
- `aws-managed-policy/latest/reference/{SystemAdministrator,AmazonEC2FullAccess,AmazonEC2ReadOnlyAccess,PowerUserAccess}.html`
