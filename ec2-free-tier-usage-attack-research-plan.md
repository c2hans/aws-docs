# Amazon EC2 Free Tier (and the backing AWS `freetier` service) — Attack Research Plan

Source of leads:
- Target page: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-free-tier-usage.html` (`.md` mirror `docs/AWSEC2/latest/UserGuide/ec2-free-tier-usage.md`)
- Backing service API: `docs/aws-cost-management/latest/APIReference/API_Operations_AWS_Free_Tier.md` + `API_freetier_*.md` (GetAccountActivity, GetAccountPlanState, GetFreeTierUsage, ListAccountActivities, UpgradeAccountPlan; types ActivityReward, ActivitySummary, DimensionValues, Expression, FreeTierUsage, MonetaryAmount)
- IAM authorization reference: `docs/service-authorization/latest/reference/list_freetier.md`
- Billing/account docs: `awsaccountbilling/latest/aboutv2/{tracking-free-tier-usage,using-free-tier-api,free-tier-plans,free-tier-plans-activities}.md`; `accounts/latest/reference/bcm-lite-free-tier{,-credits,-track}.md`
- EC2 attribute surface: `AWSEC2/latest/APIReference/{API_DescribeImages,API_DescribeInstanceTypes,API_Image,API_InstanceTypeInfo}.md` (`freeTierEligible` field + `free-tier-eligible` filter)

Status: **documentation-derived hypotheses only; nothing tested against a live account.** Online `.md` versions were cross-checked against the local mirror; where the mirror is thin a lead is marked *doc-gap*.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- This is a **billing / anti-abuse / usage-metering** surface, not a classic data plane. The highest-value boundaries are: (a) *who in an account can flip billing state*, (b) *cross-account/Organizations visibility of plan+usage data*, (c) *the free-credit issuance ("earn $100") anti-abuse flow*, and (d) *the authenticity of the `free-tier-eligible` attribute a victim's "find a free AMI/instance" workflow trusts*.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane** (the credit-granting / metering backend, a cross-customer reward ledger, an AWS-internal account id in a response), stop, preserve evidence, flag for AWS-Security disclosure. Do **not** attempt to actually mint credits, flip another tenant's plan, or farm real credits — confirm the *authorization/validation gap* with a single read/benign call and stop.
- **Money-touching caveat:** `UpgradeAccountPlan`, credit issuance, and account-closure are real billing-state mutations. Confirm reachability/authorization with the *least* side-effecting call possible (prefer `iam:SimulatePrincipalPolicy`, a `ValidationException`-inducing malformed call, or a read twin) before any state change. Never farm credits or close an account as "proof."

---

## 1. Pentest Objectives (boundary-breach goals, stated as concrete outcomes)

1. **Cross-account read:** from account A's credentials, read account B's Free Tier *usage* (`GetFreeTierUsage`), *plan state / remaining credit balance* (`GetAccountPlanState`), or *activity/reward records* (`GetAccountActivity`/`ListAccountActivities`) — any response carrying a `[0-9]{12}` `accountId` that is not the caller's is a breach.
2. **Unauthorized billing-state mutation:** cause `UpgradeAccountPlan` to change the plan of an account/project the caller should not control (another project under the same payer, the Organizations management account, or another account entirely), or to flip `PAID→FREE` ("downgrade" via an API named *Upgrade*).
3. **Free-credit abuse / anti-abuse bypass:** obtain the "$20 per activity / up to $100" reward **without** legitimately completing the activity, **replay** a completion, or **farm** credits at scale across many accounts in a way the documented one-per-new-customer limit should prevent.
4. **"You can't exceed your Free Tier limits" guarantee break (new-account plans):** drive real usage past the free limit on a *Free account plan* before the 3×/day metering catches it, i.e. incur usage AWS says cannot be incurred.
5. **Alert suppression / redirection:** change the Free Tier alert email (`PutFreeTierAlertPreference`) or opt an account out of alerts so a victim never learns they are being billed — enabling a stealth cost-overrun / denial-of-wallet.
6. **`free-tier-eligible` authenticity:** make a victim's documented "list the free AMIs / instance types" workflow (`describe-images`/`describe-instance-types --filters free-tier-eligible=true`) select or trust an **attacker-influenced** image/type.
7. **Metering/filter injection:** make `GetFreeTierUsage`'s `Expression` filter or the opaque `nextToken` reach data (another account's rows, backend errors) the caller's identity does not scope.

---

## 2. Components, Assets, and Design

**Customer-facing interfaces**
- **EC2 console widget** "EC2 Free Tier" box on the EC2 Dashboard (read-only usage display; "View Global EC2 resources", "View all AWS Free Tier offers"). Only shown to accounts <12 months old (pre-2025-07-15 accounts).
- **Billing/Cost Management console** "Free Tier" page; "Billing preferences → Alert preferences" (set alert email, opt in/out of alerts); "Explore AWS" / "Recommended actions" widgets; the new "AWS Settings" surface (bcm-lite) with credit balance + "Upgrade plan".
- **`freetier` service API** (`freetier-2023-09-07`, SDK/CLI `aws freetier …`): `GetAccountActivity`, `GetAccountPlanState`, `GetFreeTierUsage`, `ListAccountActivities`, `UpgradeAccountPlan`.
- **EC2 API** read filters: `DescribeImages` / `DescribeInstanceTypes` with `free-tier-eligible` filter; response fields `Image.freeTierEligible`, `InstanceTypeInfo.freeTierEligible`.

**Processes / backends behind it (inferred — doc-gap on internals)**
- A **metering/usage aggregation backend** that computes `actualUsageAmount`, `forecastedUsageAmount`, `limit` per service/usageType/region. Docs state usage **"is not updated in real time; it's updated three times a day."** → an eventually-consistent meter, not an inline gate.
- A **credit/reward ledger** that issues $100 signup credit and $20-per-activity rewards, and an **activity-completion verifier** that decides when an activity is `COMPLETED` and emits the reward.
- An **account-plan state machine** (`accountPlanType ∈ {FREE,PAID}`, `accountPlanStatus ∈ {NOT_STARTED,ACTIVE,EXPIRED}`) driving service-access gating ("Free account plans don't include … Savings Plans, Reserved Instances …") and automatic account **closure** after 6 months / credit depletion (90-day retention).
- An **`Expression` filter evaluator** for `GetFreeTierUsage` (Cost-Explorer-style AND/OR/NOT over `Dimensions{Key,Values,MatchOptions}`), and an opaque **`nextToken`** pagination cursor (len ≤ 8192, pattern `[\S\s]*`).

**Accounts / tenancy**
- Everything is **account-scoped with no resource ARNs and no condition keys** (see §4) — the only isolation is "the API acts on the caller's own account." That makes tenancy enforcement *entirely implicit* and the prime thing to test.
- **AWS Organizations** overlays this: management vs member accounts, "billing transfer" / bill-source vs bill-transfer accounts, pro forma vs chargeable. The new bcm-lite model has **"projects"** all sharing one plan type ("All projects that you own are under the same plan type").

**Identifiers / entropy**
- `accountId`: `[0-9]{12}` — appears in `UpgradeAccountPlan`/`GetAccountPlanState` **responses** (not request). Low entropy / enumerable as an identifier, though not accepted as input in any documented request.
- `activityId`: **fixed length 32, `[a-zA-Z0-9]+`** — accepted as **input** to `GetAccountActivity`. High entropy, but is it tenant-scoped or global?
- `nextToken`: opaque, ≤8192, `[\S\s]*` — tamperable cursor.

**Identity**
- SigV4 IAM. `GetFreeTierUsage` is additionally authorized by the **legacy** `aws-portal:ViewBilling` permission (dual-grant). Alert email + root user are relevant for the alert-redirection path.

**Untrusted-data entry points**
- `GetFreeTierUsage.filter` (nested `Expression`) and `nextToken` (both free-form strings into a backend query).
- `ListAccountActivities.filterActivityStatuses` / `languageCode` (enums).
- The alert **email address** (console/`PutFreeTierAlertPreference`).
- Server→client text fields `instructionsUrl`, `description`, `title` on activities (AWS-authored → rendered in console).
- The `free-tier-eligible` **attribute** on AMIs/instance types that `describe-*` workflows filter on.

```
                                 AWS service plane (HARD STOP)
                         ┌───────────────────────────────────────────┐
                         │  metering backend (3x/day)   credit/reward │
                         │  usage aggregator            ledger + activity verifier
                         │  account-plan state machine  closure job   │
                         └───────▲───────────────▲───────────▲────────┘
                                 │               │           │
  caller IAM principal ─ SigV4 ─┤               │           │
   (freetier:* / aws-portal:*)  │               │           │
        │                       │               │           │
        ├─ GetFreeTierUsage ────┘ (usage rows)   │           │
        ├─ GetAccountPlanState ─ (plan + remaining credits)  │
        ├─ Get/ListAccountActivities ────────────┘ (reward offers/status)
        ├─ UpgradeAccountPlan ── FREE|PAID ───────────────── (plan mutation; NO accountId input, NO condition keys)
        └─ Put/GetFreeTierAlertPreference (console-only; alert email)

  EC2 API: DescribeImages/DescribeInstanceTypes --filters free-tier-eligible=true
           -> trusts freeTierEligible boolean on (possibly shared/attacker) AMIs
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Account A IAM principal | Account B usage/plan/activity data | `freetier:*` read APIs (no resource scoping) | A response returns a `[0-9]{12}` `accountId ≠ A`, or B's usage/credit rows |
| Low-priv principal in account | Account/project billing posture | `UpgradeAccountPlan` (Write, no condition keys, no resource) | Plan flips for the account/all projects when the principal should not control billing |
| Org **member** / delegated principal | Org **management** account plan/usage | billing-transfer / payer linkage | Member call returns or mutates the management account's plan/credits |
| New customer | AWS **credit ledger** | activity-completion → `$20` reward | A reward credited without a genuine completion, or a completion replayed/farmed |
| Free-plan account | Real paid usage | metering is 3×/day, not inline | Usage incurred past the free limit on a plan AWS says "can't exceed" |
| Attacker | Victim's "find free AMI" workflow | `freeTierEligible` attribute + `--filters free-tier-eligible=true` | A victim-run describe selects/launches an attacker-controlled image marked free-tier-eligible |
| Caller | Metering query backend | `Expression` filter / `nextToken` | Backend error leaking internals, or rows outside caller's account returned |
| Attacker | Victim alert channel | `PutFreeTierAlertPreference` / Billing preferences | Alert email changed/opted-out so victim never sees overage |
| **Any customer surface** | **AWS service plane** (ledger/meter) | all of the above | **Any AWS-internal identity/account/credential surfaced = hard stop + disclosure** |

---

## 4. API / Interface Inventory

| Name | Method/Access | New? | Mutating | Internet-callable | Functionality | Authorized callers | Notes (→lens) |
|---|---|---|---|---|---|---|---|
| `GetFreeTierUsage` | Read | — | No | Yes (SDK/CLI) | Usage rows vs limits w/ `Expression` filter | `freetier:GetFreeTierUsage` **OR legacy `aws-portal:ViewBilling`** | Dual-grant legacy alias (→X); filter+nextToken injection (→F,A) |
| `GetAccountPlanState` | Read | New (2023-09-07) | No | Yes | Plan type/status, **remaining credit balance**, expiry | `freetier:GetAccountPlanState`; **no condition keys** | Credit balance disclosure; cross-acct (→A) |
| `GetAccountActivity` | Read | New | No | Yes | One activity by **`activityId` (32-char)**, reward, `instructionsUrl` | `freetier:GetAccountActivity`; no resource scoping | activityId-as-input → is it tenant-scoped? (→A,M) |
| `ListAccountActivities` | List | New | No | Yes | Available/earned reward activities + status | `freetier:ListAccountActivities` | Reward offers; status filter (→P) |
| `UpgradeAccountPlan` | **Write** | New | **Yes** | Yes | Set `accountPlanType FREE\|PAID` | `freetier:UpgradeAccountPlan`; **no condition keys, no resource ARN** | **No `accountId` in request** — acts implicitly; name "Upgrade" accepts `FREE` (downgrade) (→E,A,U) |
| `GetFreeTierAlertPreference` | Read (permission-only) | — | No | **Console-only — not invocable via any API** | Read alert email | `freetier:GetFreeTierAlertPreference` | Undocumented-knob delta (→Step-3 hidden knob) |
| `PutFreeTierAlertPreference` | Write (permission-only) | — | **Yes** | **Console-only** | Set alert email | `freetier:PutFreeTierAlertPreference` | Alert redirection/suppression (→M, denial-of-wallet) |
| `ec2:DescribeImages` (filter) | Read | — | No | Yes | `free-tier-eligible` filter; `Image.freeTierEligible` | `ec2:DescribeImages` | Authenticity of attribute on shared/public AMIs (→U,EE) |
| `ec2:DescribeInstanceTypes` (filter) | Read | — | No | Yes | `free-tier-eligible` filter; `InstanceTypeInfo.freeTierEligible` | `ec2:DescribeInstanceTypes` | AWS-computed; sanity-only (→U) |

**Undocumented/console-hidden knobs (Step-3 sweep):**
- `GetFreeTierAlertPreference` / `PutFreeTierAlertPreference` are **"defined … but not directly invocable through any API operation"** — IAM actions that gate a console-only email-set. A principal granted `freetier:PutFreeTierAlertPreference` (e.g. via a wildcard `freetier:*`) controls where overage alerts go. Enumerate whether any undocumented wire operation backs them.
- `UpgradeAccountPlan` accepts `accountPlanType=FREE` though it is named *Upgrade* — the most-permissive/unexpected enum value. Does anything warn, or is a silent **downgrade** PAID→FREE accepted (and what does that do to active paid resources / closure timer)?
- Verify the live model against `https://servicereference.us-east-1.amazonaws.com/v1/freetier/freetier.json` (linked from the IAM ref) for any action/field not in the prose docs.

**AWS plants the lead:** the target page explicitly tells users to run `describe-instance-types`/`describe-images` **with the `free-tier-eligible` filter** to decide what is free — making that attribute an authorization-adjacent input (→Area F).

---

## 5. Recommended Areas of Focus (one block per firing lens, priority-ordered)

### Area A — Billing-state mutation with zero scoping (`UpgradeAccountPlan`)  [Lens E, A, U, X]  — **TOP PRIORITY**
**Background:** `UpgradeAccountPlan` is the only **Write** action in the service. Its IAM entry has **no condition keys and no resource type** (`freetier` "does not support specifying a resource ARN"). The request body is **only** `{"accountPlanType":"FREE|PAID"}` — there is **no `accountId`**, so the target account is implicit from the caller's credentials, and the console path is a single "Upgrade account" click. In the new bcm-lite model, **"all projects that you own are under the same plan type"** and joining Organizations/Control Tower/APN *auto-upgrades* a free plan.
**Security Concern:** With no resource/condition scoping, the *only* control over "who may flip this account's billing plan (for all projects at once)" is whether a principal holds `freetier:UpgradeAccountPlan`. A broad grant (`freetier:*`, `billing:*`, an admin-ish role, or a wildcard in an AWS-managed/sample policy) silently confers the ability to (a) **downgrade PAID→FREE** — the enum accepts `FREE` despite the "Upgrade" name — potentially tripping the free-plan service restrictions / 6-month closure timer on a production account, or (b) **upgrade FREE→PAID** to escape the "can't exceed limits" guard and start incurring charges (denial-of-wallet). In Organizations, test whether a member/linked principal's call can reach the management/payer account's plan.
**High-level Test Scenarios:**
1. *Claim:* a `FREE` value is accepted by an API named *Upgrade* → **Mechanism:** `Valid Values: FREE | PAID`, Required. → **Oracle:** call returns 200 with `accountPlanType=FREE` on a PAID account (or `ValidationException` if blocked); observe whether paid resources/closure state change. → **Cost:** real billing-state change — prefer `SimulatePrincipalPolicy` first; only exercise on a disposable canary account. → **Severity:** downgrade of a prod account = High.
2. *Claim:* any principal with the action can flip the whole account though it is not "billing admin." → **Oracle:** under a scoped role holding **only** `freetier:UpgradeAccountPlan` (no other billing perms), the call succeeds → confirms action is the sole gate. → **Severity:** High (least-priv footgun promoted to real-mutation).
3. *Claim:* the call can be aimed at another account/project. → **Oracle:** craft a request adding `accountId`/`accountPlanType` for a foreign 12-digit id (undocumented param); member→management in an Org; a response `accountId ≠ caller`. → **Severity:** cross-account billing mutation = Critical.
**Doc evidence:** `API_freetier_UpgradeAccountPlan.md` (request/enum), `list_freetier.md` (no condition keys/resources), `bcm-lite-free-tier.md` ("all projects … same plan type"), `free-tier-plans.md` (auto-upgrade triggers).
**Severity-if-true:** High–Critical.
**Stop condition:** the moment a *foreign* account's plan state changes or a service-plane id appears — stop, preserve, disclose.

### Area B — Cross-account / Organizations read of plan, credit balance, usage & activities  [Lens A]
**Background:** `GetAccountPlanState` returns `accountPlanRemainingCredits` (a dollar balance), expiry, status; `GetFreeTierUsage` returns per-service usage; `Get/ListAccountActivities` return reward offers/status. **None** supports a resource ARN or condition key; isolation is purely "acts on caller's account." Docs note Organizations billing-transfer nuances (management vs linked/bill-source accounts can/can't see each other's Free Tier applications).
**Security Concern:** Because tenancy is implicit, the classic failure is an API that scopes by a request field or a payer linkage instead of the caller's credential — letting a member account read the management account's (or a sibling's) credit balance/usage, or vice-versa. The billing-transfer note is a documented place where visibility rules differ by account role → a parity gap is plausible.
**High-level Test Scenarios:**
- *Claim:* a member/linked principal can read the payer/management account's remaining credit balance or usage. → **Oracle:** `GetAccountPlanState`/`GetFreeTierUsage` from the member returns a balance/usage attributable to another account (response `accountId` mismatch, or values the member has no resources to explain). → **Severity:** cross-account billing-data disclosure = High.
- *Claim:* `GetAccountActivity` accepts another tenant's `activityId`. → **Mechanism:** `activityId` is **input** (32-char), "available to the customer" — is "the customer" enforced, or only existence? → **Oracle:** supply a well-formed activityId not belonging to the caller → `ResourceNotFoundException` (ownership enforced) vs 200 with foreign reward/`instructionsUrl` (IDOR). → **Severity:** cross-account activity/reward disclosure = Medium–High.
- *Error-oracle variant (Lens A):* diff `ResourceNotFoundException` vs `ValidationException` vs 200-empty across foreign vs malformed ids — an enumeration oracle for account/activity existence.
**Doc evidence:** `API_freetier_GetAccountPlanState.md`, `API_freetier_GetAccountActivity.md`, `tracking-free-tier-usage.md` (billing-transfer visibility note), `list_freetier.md`.
**Severity-if-true:** Medium–High (High if management-account credit balance).

### Area C — Free-credit issuance / activity-reward anti-abuse  [Lens P, U]
**Background:** New customers get **$100 signup + up to $100 earned** ($20 for each of 5 activities: launch EC2, Bedrock playground, create budget, Lambda web app, RDS db). Activities have states `NOT_STARTED→IN_PROGRESS→COMPLETED/EXPIRING`; a reward is granted "upon activity completion." `ActivityReward` is a union currently holding only `credit` (a `MonetaryAmount`).
**Security Concern:** This is the money-minting anti-abuse surface. The documented guard is "$100 … **regardless of your account plan** … completing activities" and an implicit *one-per-new-customer* / one-per-activity limit. Two breach shapes: (1) **completion forgery/replay** — can an account reach `COMPLETED` and collect $20 without genuinely performing the activity, or collect twice (replay, race two completions, toggle status)? (2) **farming** — scripted mass new-account creation to mint $100+credit each (identity-proofing bypass at signup). Also test whether `UpgradeAccountPlan` interacts with reward eligibility (e.g., re-trigger NOT_STARTED to re-earn).
**High-level Test Scenarios:**
- *Claim:* an activity can be marked COMPLETED without the underlying action, or a reward replayed. → **Mechanism:** states enumerated in `GetAccountActivity`/`ListAccountActivities`; reward "upon completion." → **Oracle:** completion credited (`accountPlanRemainingCredits` increases by $20) without the real resource existing, or a second $20 for the same activity. → **Severity:** credit theft from AWS = High (service-plane money — **hard-stop on confirmation; do not farm**).
- *Claim:* uniqueness ("one new customer") is bypassable. → **Oracle:** two accounts sharing the normalized identity/payment both receive the $100 — but **do not execute at scale**; stop at the first duplicate that proves the gap. → **Severity:** High.
- *Null-check:* confirm whether completion is verified server-side from real service telemetry (likely) vs client-assertable (bug). Mark *doc-gap* on the verifier internals.
**Doc evidence:** `bcm-lite-free-tier-credits.md`, `free-tier-plans-activities.md`, `free-tier-plans.md`, `API_freetier_ActivityReward.md`, `API_freetier_ListAccountActivities.md`.
**Severity-if-true:** High (reaches AWS credit ledger — treat as service-plane, hard stop).

### Area D — "You can't exceed your Free Tier limits" vs 3×/day metering  [Lens U, L, O]
**Background:** For post-2025-07-15 accounts the target page asserts **"You can't exceed your Free Tier limits."** Yet the same corpus states usage **"is not updated in real time; it's updated three times a day,"** and alerts fire at **85%** (and only after a resource exists). AWS Budgets alerting is a *notification*, not an inline quota.
**Security Concern:** The promised hard guarantee is enforced by an eventually-consistent meter plus email alerts — not an inline admission control. Between meter refreshes a Free-plan account may be able to **incur real, unbilled-but-chargeable usage past the limit** (spin up many free-eligible instances / burst usage faster than the 3×/day settle), contradicting the documented "can't exceed." The enforcement mechanism for the guarantee is the thing to trace: is it IAM/quota at launch time, or only post-hoc metering + closure?
**High-level Test Scenarios:**
- *Claim:* the "can't exceed" guarantee is advisory (post-hoc), not inline. → **Oracle:** on a Free-plan canary, launch usage exceeding a free limit within one metering window and observe whether the resource is admitted (guarantee broken) or refused at the control plane (guarantee real). → **Severity:** Low–Medium (self-inflicted cost / weak-guarantee), **unless** it enables cross-tenant resource exhaustion on shared free-tier infra (→escalate).
- *Claim (Lens O):* some usage/operation types are never reflected in the 3×/day meter → a blind spot a cost-abuser rides. → **Oracle:** a usageType present in billing but absent from `GetFreeTierUsage`/the trackable-services table. → **Severity:** Informational–Low (enabler).
**Doc evidence:** `ec2-free-tier-usage.md` ("can't exceed"; "updated three times a day"), `tracking-free-tier-usage.md` (85% alert, "only after you've created an instance").
**Severity-if-true:** Low–Medium (doc-vs-enforcement gap; AWS-owned claim worth filing).

### Area E — `free-tier-eligible` attribute authenticity (AMI/instance-type)  [Lens U authenticity-filter-omission, EE, A]
**Background:** The target page instructs users to **list free resources via `describe-images --filters free-tier-eligible=true`** and `describe-instance-types --filters free-tier-eligible=true`. `Image.freeTierEligible` / `InstanceTypeInfo.freeTierEligible` are booleans surfaced on *every* image, including shared/community AMIs.
**Security Concern:** This is the whoAMI shape: a documented discovery workflow that filters on an attribute **without an `--owners amazon` / authenticity constraint**. If `freeTierEligible` can be influenced on an attacker-published/shared AMI (or if a victim's automation trusts the flag and omits owner-pinning), the attacker's image can be selected by a "find a free AMI" script and launched with attacker code. For instance types the attribute is AWS-computed (sanity-only), but the AMI path is the real lead.
**High-level Test Scenarios:**
- *Claim:* `freeTierEligible=true` can appear on a non-AWS/shared image, or is attacker-settable at registration/share. → **Mechanism:** field is `Required: No` and present on all images; filter has no owner constraint. → **Oracle:** register/share an AMI and read its `freeTierEligible`; or find any `free-tier-eligible=true` image whose `OwnerId ≠ amazon/aws-marketplace`. → **Severity:** victim launches attacker AMI = High (if the attribute is attacker-controllable); otherwise refuted (AWS-computed, owner-pinned).
- *Guidance-gap (Lens U):* the doc's example omits owner-pinning → file as an AWS-owned hardening/doc defect even if the attribute itself is authentic. → **Severity:** Low (doc hardening).
**Doc evidence:** `ec2-free-tier-usage.md` (the two example commands), `API_Image.md`/`API_InstanceTypeInfo.md` (`freeTierEligible`), `API_DescribeImages.md` (`free-tier-eligible` filter).
**Severity-if-true:** High if attribute is attacker-controllable; else Low (guidance hardening).

### Area F — `Expression` filter & `nextToken` injection into the metering backend  [Lens F, A]
**Background:** `GetFreeTierUsage.filter` is a recursive `Expression` (AND/OR/NOT over `Dimensions{Key, Values[], MatchOptions[]}`), Cost-Explorer-style. `Values` are free strings; `nextToken` is opaque, ≤8192, pattern `[\S\s]*` (any bytes).
**Security Concern:** A customer-controlled nested expression and an opaque cursor are both fed to a backend query evaluator. Breach shapes: (a) **filter injection / unexpected `Key`/`MatchOptions`** values reaching the backend to leak internals or error-dump; (b) **`nextToken` tampering** — if the cursor encodes the account scope or an offset rather than being bound to the caller's identity, a forged/replayed token could page into another account's rows or trigger a backend error. (c) deeply-nested `Expression` (AND/OR/NOT recursion) → parser DoS.
**High-level Test Scenarios:**
- *Claim:* a malformed/overlong/foreign `nextToken` pages into unexpected data or dumps backend state. → **Oracle:** 200 with rows whose `service`/`region` the caller never used, or a `500 InternalServerException` leaking an internal message. → **Severity:** cross-account rows = High; error leak = Low.
- *Claim:* unexpected `Dimensions.Key`/`MatchOptions`/special-char `Values` reach the backend unescaped. → **Oracle:** differential errors / reflected internals vs `ValidationException`. → **Severity:** Low–Medium.
- *Claim:* deeply nested `Expression` → parser hang. → **Oracle:** latency/`500` as nesting depth grows. → **Severity:** single-tenant Low.
**Doc evidence:** `API_freetier_Expression.md`, `API_freetier_GetFreeTierUsage.md` (`nextToken` pattern `[\S\s]*`, len 8192).
**Severity-if-true:** High if cross-account via cursor; otherwise Low–Medium.

### Area G — Alert redirection / suppression → denial-of-wallet  [Lens M, O]
**Background:** `PutFreeTierAlertPreference` (console-only, Write) sets the email that receives "you exceeded 85% / exceeded Free Tier" alerts; overage emails otherwise go to the **root user**. Alerts can be opted out entirely (management accounts are opt-in).
**Security Concern:** A principal who can set the alert email or opt the account out can **blind the victim to cost overruns** — a stealth enabler for a denial-of-wallet attack (combine with Area A upgrade FREE→PAID or Area D exceed-limits). Because the action is permission-only and console-backed, a `freetier:*` wildcard grant confers it without the operator realizing.
**High-level Test Scenarios:**
- *Claim:* a non-root principal with `freetier:PutFreeTierAlertPreference` redirects/suppresses alerts. → **Oracle:** alert email changes to an attacker address / alerts disabled, confirmed by `GetFreeTierAlertPreference` and no email to root on overage. → **Severity:** Medium (enabler); High when chained with a cost-inflation primitive.
**Doc evidence:** `list_freetier.md` (permission-only Put/Get), `tracking-free-tier-usage.md` (alert email, opt in/out, root recipient).
**Severity-if-true:** Medium (High chained).

### Area H — Legacy-permission parity on `GetFreeTierUsage`  [Lens X]
**Background:** `GetFreeTierUsage` is authorized by **either** `freetier:GetFreeTierUsage` **or** the legacy `aws-portal:ViewBilling`. The two actions are different IAM strings governing the same read.
**Security Concern:** A policy that **denies `freetier:GetFreeTierUsage`** (e.g. to hide billing/usage from a role) is **bypassed** by any grant of the legacy `aws-portal:ViewBilling`, which many older roles/SCPs still carry. Classic twin-action authorization gap.
**High-level Test Scenarios:**
- *Claim:* a principal denied `freetier:GetFreeTierUsage` but granted `aws-portal:ViewBilling` still reads usage. → **Oracle:** `SimulatePrincipalPolicy` on both actions, then a live `get-free-tier-usage` call that succeeds despite the `freetier:` deny. → **Severity:** Low–Medium (usage/billing info disclosure; worth filing as a documented dual-grant trap).
**Doc evidence:** `list_freetier.md` (GetFreeTierUsage lists both IAM actions).
**Severity-if-true:** Low–Medium.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Flip another account's / all-projects' billing plan | `UpgradeAccountPlan` | Implicit caller-account scoping; action-only gate (no resource/condition) |
| Downgrade PAID→FREE on a prod account | `UpgradeAccountPlan` enum | `Valid Values FREE\|PAID` (no guard against FREE) |
| Member reads management account credit balance | `GetAccountPlanState` | Billing-transfer visibility rules (prose only) |
| IDOR on activity by foreign `activityId` | `GetAccountActivity` | "available to the customer" (ownership check unstated) |
| Mint/replay/farm $20 activity rewards | reward ledger / activity verifier | "upon completion", one-per-new-customer (unstated enforcement) |
| Exceed free limit before 3×/day settle | metering backend | "You can't exceed your Free Tier limits" (claim) |
| Launch attacker AMI via free-tier filter | `DescribeImages` `free-tier-eligible` | `freeTierEligible` attribute authenticity (no owner-pin in doc) |
| nextToken/filter crosses account scope | `GetFreeTierUsage` | Caller-identity binding of cursor (unstated) |
| Suppress/redirect overage alerts | `PutFreeTierAlertPreference` | Permission-only action; root-user recipient default |
| Deny-bypass via legacy billing perm | `GetFreeTierUsage` dual-grant | Separate `aws-portal:ViewBilling` grant |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Shared RDS/Aurora/EC2 hypervisor/metering infra internals** — the metering backend's implementation, cross-tenant isolation of AWS's own aggregation fleet. If a probe would reach it, it is a **hard-stop/disclosure**, not an in-scope test.
- **A customer steering their own billing** — a root/admin legitimately upgrading/downgrading *their own* account, or legitimately earning rewards by doing the activities, is intended behavior.
- **Customer-authored IAM footguns** — a customer who grants `freetier:*`/`billing:*` too broadly in *their own* policy is a least-privilege self-inflicted issue (only in scope if the broad grant ships in an **AWS-managed or AWS-published sample** policy — none observed in these docs; mark *doc-gap*, check AWS-managed billing policies separately).
- **Account-closure data loss** (6-month / 90-day retention) — product behavior, not a vuln, unless an attacker can *trigger* a victim's closure (that would route to Area A/C).
- **IMDS / instance-level issues on launched free-tier instances** — covered by EC2 instance-metadata plans, not this metering surface.
- **Real credit farming / real plan flips on live/third-party accounts** — never perform; confirm the authorization/validation gap and stop.
- **AWS Budgets / Cost Explorer internals** — separate services; only the Free Tier-specific alert wiring is in scope here.

---

## 8. Null Hypotheses / Doc Gaps
- **Lens B/C (PassRole / credential vending):** *Null — read `list_freetier.md`, all `API_freetier_*` operations, and the billing/account docs; the `freetier` service assumes no caller-passed role, vends no STS credentials, and accepts no role ARN. No PassRole/credential-vending surface.*
- **Lens G (classic SSRF):** *Mostly null — the only server-dereferenced field is `instructionsUrl` in an activity response, which is **AWS-authored** (not caller-supplied). No customer-supplied URL/host field exists in any request. Mark the `instructionsUrl`→console-render path as a minor stored-content/XSS check (Area C adjacency), not SSRF.* Checked: all 5 API operation request bodies, the alert-preference flow, the EC2 describe filters.
- **Lens H (KMS/encryption-context):** *N/A — no customer KMS key, encryption context, or key policy in any Free Tier doc read.*
- **Lens K (prompt injection):** *N/A — no LLM/agent in this metering/billing surface (the Bedrock *activity* is a link out, not part of this service).*
- **Lens Q (file upload):** *N/A — no upload field; the only blob adjacency is an AMI (Area E), handled as attribute authenticity.*
- **Lens V/D (network segmentation / data→control):** *N/A at the doc layer — no customer ENI/VPC/socket; all interaction is SigV4 API.*
- **Lens W / Y / BB / CC / DD / FF (attestation / TLS-sig / canonicalization / upstream-context / cache / JWT):** *No triggers in the Free Tier docs (no attestation gate, no documented multi-parser edge/authorizer chain, no JWT/OIDC, no documented authorizer-result caching). Mark **doc-gap** rather than hard-N/A for DD, because `GetFreeTierUsage` is a read AWS may cache in the console — low priority.*
- **Doc gaps to confirm against a live account before deep work:**
  - Does `UpgradeAccountPlan` accept any undocumented `accountId`/target param (check `freetier.json` service-reference)? Does it enforce "billing admin" vs plain action grant?
  - Is `GetAccountActivity`'s `activityId` tenant-scoped or global (ownership vs existence)?
  - Is the `nextToken` bound to the caller's identity/account, or does it encode account scope?
  - Is activity completion verified from real service telemetry (server-side) or assertable by the caller?
  - Can `freeTierEligible=true` ever appear on a non-AWS-owned image?
- **Priority recommendation for the hunter:** execute in the order **A → B → C → E → D → F → G → H**. Areas A, B, and C are where a *real cross-boundary / money* finding would live; D/E/F/G/H are hardening/parity/guidance leads. **C and any confirmed cross-account read in A/B touch the AWS service plane — confirm the gap with one benign call and HARD STOP for disclosure; do not exploit.**

---
*Generated by the `security-questionbuilder` skill against AWS documentation. Documentation-derived hypotheses only — no live AWS account was contacted.*
