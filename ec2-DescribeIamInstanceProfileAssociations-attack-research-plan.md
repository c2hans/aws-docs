# EC2 `DescribeIamInstanceProfileAssociations` — Attack Research Plan

**Source of leads:**
- Target page: `https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeIamInstanceProfileAssociations.html` (mirror: `docs/AWSEC2/latest/APIReference/API_DescribeIamInstanceProfileAssociations.md`) — online fetch confirmed consistent with mirror, no sync drift.
- Response data type: `docs/AWSEC2/latest/APIReference/API_IamInstanceProfileAssociation.md` (+ `API_IamInstanceProfile.md`, `API_Filter.md`).
- Write-twin API refs: `API_{ReplaceIamInstanceProfileAssociation,AssociateIamInstanceProfile,DisassociateIamInstanceProfile}.md`, `CommonErrors.md`, `CommonParameters.md`.
- Authorization reference: `docs/service-authorization/latest/reference/list_ec2.md` — Describe action-with-resources row **L6864**; write twins at Associate **L4749**, Disassociate **L7915**, Replace **L9401**; condition-key defs `ec2:InstanceProfile` L10096 / `ec2:NewInstanceProfile` L10117.
- IAM/EC2 user guide: `iam-roles-for-amazon-ec2.md`, `permission-to-pass-iam-roles.md`, `ExamplePolicies_EC2.md`, `attach-iam-role.md`, `monitor-with-cloudtrail.md`, IMDS pages.
- **Sibling plan (the privesc write path this Describe feeds):** `/work/aws-docs/ReplaceIamInstanceProfileAssociation-attack-research-plan.md`. This document deliberately does **not** re-derive the Replace/Associate privesc mechanics — it covers the *recon/read* half and the chain hand-off.

**Status:** documentation-derived hypotheses only. **Nothing tested against a live AWS account.** Each item is a boundary that *might not hold* plus the exact observation that would settle it.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5).
- **What this API is.** `DescribeIamInstanceProfileAssociations` is a **read-only (access level: List), intra-account reconnaissance primitive.** It returns, for the whole account, the map of `instanceId → instance-profile ARN → association state`. It mutates nothing. Its security weight is almost entirely **(a) that it cannot be least-privilege-scoped** and **(b) that it is the enumeration step that makes write-twin privilege escalation (`ReplaceIamInstanceProfileAssociation`) targetable.** The headline question: *"can a low-privileged principal in a shared account map every other workload's instance→role binding, with no IAM mechanism able to stop it?"*
- **Safe-oracle discipline:** the first oracle for every scoping lead is **`iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy`** (touches no resources). A live `describe-iam-instance-profile-associations` call is itself read-only and non-mutating, so it is a safe confirmation step under a scoped canary principal — but **do not** chain into the write twin on any real resource; that belongs to the sibling plan under synthetic canaries only.
- **HARD STOP / out of scope:** the moment any evidence shows an identity, credential, ARN, or account belonging to **AWS's own service plane** (an `aws:ec2-instance` instance-identity role, a service-linked-role credential, an AWS-owned fleet account) — **stop, preserve evidence, flag for AWS-Security disclosure.** This is an intra-account read API; cross-tenant isolation is **not** its risk class (see Section 7/8). A clean/negative result is a correct result.

---

## 1. Pentest Objectives (concrete boundary-breach goals)

1. **Unscopable account-wide recon.** From a principal holding **only** `ec2:DescribeIamInstanceProfileAssociations`, enumerate the instance→profile→role bindings of **instances/teams the principal has no other access to**, and show that **no IAM policy can narrow the result to the caller's own instances** (no resource type, only `ec2:Region`). **Breach = a least-privilege read grant that is structurally account-wide.**
2. **Recon-to-privesc chain hand-off.** Show that the Describe output supplies every input the write-twin privesc (`Replace…`) needs — a target `associationId`, the current profile ARN, and the `instanceId` — i.e. the Describe is the targeting oracle for the kill chain documented in the sibling plan.
3. **Doc-guarantee vs enforcement ("your associations").** The API description says it describes "**your** IAM instance profile associations"; test whether "your" is enforced as *the caller's* (it is not — it is *the account's*), making the word advisory.
4. **Error / validator-divergence enumeration oracle.** Probe whether passing a well-formed-but-foreign or malformed `AssociationId` / `Filter` yields a distinguishing response (NotFound vs empty vs 500) that the write twins do not, forming an existence oracle broader than the write path's.
5. **Low-visibility recon.** Confirm whether the call is a CloudTrail *read-only management event* that typical detections do not alert on, so the enumeration step of a privesc chain is effectively silent.

---

## 2. Components, Assets, and Design

**What the API does.** Returns `iamInstanceProfileAssociationSet` — an array of `IamInstanceProfileAssociation` objects. Each object (API_IamInstanceProfileAssociation.md):
- `associationId` — opaque `iip-assoc-<17 hex>` (e.g. `iip-assoc-08049da59357d598c`), ~68-bit random, **no embedded ownership checksum**; opacity is not an access boundary. This is the exact handle `Replace`/`Disassociate` consume.
- `iamInstanceProfile` — `IamInstanceProfile{ arn, id }`: the **full ARN of the attached instance profile** (e.g. `arn:aws:iam::123456789012:instance-profile/AdminProfile` in AWS's own sample response) and its `AIPA…` id. **This is the sensitive disclosure** — it names the privileged profile attached to each instance.
- `instanceId` — the instance the profile is attached to.
- `state` — `associating | associated | disassociating | disassociated`.
- `timestamp` — when the association was made.

**Request inputs (all optional, read-only):**
- `AssociationId.N` — array of association ids to narrow to.
- `Filter.N` — fixed filter set: `instance-id`, `state` (`associating|associated|disassociating`). No free-form/field-name filters → no translation-layer surface.
- `MaxResults` (5–1000) + `NextToken` — standard pagination.
- Standard `AUTHPARAMS` (SigV4) + optional `DryRun` (common param).

**Authoritative IAM facts (confirmed, `list_ec2.md` L6864):**
- **Resource types: *(none)*.** **Condition keys: `ec2:Region` only.** Access level: **List.**
- Consequence: the IAM statement for this action can be written **only** as `Action: ec2:DescribeIamInstanceProfileAssociations, Resource: "*"` (optionally gated by region). There is **no** `instance*` resource type, **no** `aws:ResourceTag`/`ec2:ResourceTag`, **no** `ec2:InstanceID`, **no** `ec2:InstanceProfile`. It is structurally impossible to scope the read to a subset of instances/profiles/tags.
- **Sharp asymmetry with the write twin** (`Replace…`, L9401): Replace is scoped by `instance*` + ~20 condition keys (`aws:ResourceTag`, `ec2:InstanceID`, `ec2:InstanceProfile`, `ec2:NewInstanceProfile`, …). So an org can tightly scope *who may change* a binding, but **cannot** scope *who may read* every binding. The read side is the weakest-privilege, widest-blast-radius member of the family.

**Trust zones (single customer account):**
- **Calling IAM principal** — bounded only by whether it holds the action (region-gated at most).
- **Every instance / profile / role in the account** — their binding metadata is readable by any holder.
- **AWS service plane** — out of scope / HARD STOP.

```
caller principal ──(ec2:DescribeIamInstanceProfileAssociations, Resource:* , region-gated only)──▶ EC2 control plane
                                                                                                        │ returns, ACCOUNT-WIDE:
                                                                                                        ▼
                         { instanceId , instance-profile ARN , associationId , state } × every instance
                                                                                                        │ feeds targeting for
                                                                                                        ▼
                         ReplaceIamInstanceProfileAssociation(associationId, high-priv profile)  ──▶  IMDS creds
                              [ see sibling plan — end-of-chain privesc; rate chain at its end ]
```

**Mandatory coverage sweep (pages opened):** target API ref; `IamInstanceProfileAssociation` + `IamInstanceProfile` + `Filter` data types; `CommonParameters.md`/`CommonErrors.md`; authorization-reference Describe row + the three write-twin rows + the two instance-profile condition-key defs; `iam-roles-for-amazon-ec2.md` (cred-TTL note, instance-identity role); `permission-to-pass-iam-roles.md` + `ExamplePolicies_EC2.md` (sample policies — Lens R, Section 5.4); CloudTrail page. **No** server-side-fetched URL field, upload/blob, OAuth/3P link, translation layer, multi-tenant shared fleet, customer KMS key, token/JWT, attestation gate, caching layer, or predictable global namespace appears on this surface (null hypotheses enumerated in Section 8 with the pages checked).

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `DescribeIamInstanceProfileAssociations` | Query/SigV4 (`ec2.amazonaws.com`) | Existing (2016-11-15) | **Non-mutating (List)** | External-facing | List instance↔profile associations, account-wide | Yes (public EC2 endpoint) | Any principal with `ec2:DescribeIamInstanceProfileAssociations` — **cannot be resource-scoped** | Returns profile ARN + instanceId + associationId. **ec2:Region is the ONLY condition key.** |
| `ReplaceIamInstanceProfileAssociation` | Query/SigV4 | Existing | Mutating (Write) | External | Swap profile on a running instance by `associationId` | Yes | `instance*`-scopable + `iam:PassRole` | Write twin; consumes the Describe's `associationId`. **See sibling plan.** |
| `AssociateIamInstanceProfile` | Query/SigV4 | Existing | Mutating (Write) | External | Attach profile by `instanceId` | Yes | `instance*`-scopable + `iam:PassRole` | Sibling. |
| `DisassociateIamInstanceProfile` | Query/SigV4 | Existing | Mutating (Write) | External | Detach by `associationId` | Yes | `instance*`-scopable | Sibling; also consumes the Describe's `associationId`. |

No `[NEW]` markers; no non-SDK/console-hidden parameters on this action (the request surface is 4 optional filters/paging knobs). Undocumented-knob sweep: the only enum is the `state` filter value set, which matches the response `state` valid values — no permissive hidden value.

---

## 4. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Low-priv principal (holds only the Describe) | Every instance→profile→role binding in the account | `Resource:"*"` grant (no scoping possible) | **Reading the profile ARN / instanceId of an instance the principal cannot otherwise touch is the designed behavior — the "breach" is that least-privilege cannot prevent it; confirm no IAM construct narrows it.** |
| Read-only operator | Privesc targeting data | Describe output → `associationId`/profile ARN | The Describe output is sufficient to select a `Replace` target; proving the hand-off completes the recon→privesc chain (end-of-chain severity per sibling plan). |
| Caller request context | AWS service plane | (none — intra-account read) | Any profile ARN / account id belonging to AWS's own fleet appearing in output = HARD STOP, preserve + disclose. |

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### 5.1 — [PRIMARY] Condition-key scoping: an unscopable account-wide read (Lens S + Lens U)
**Background.** In `list_ec2.md` (L6864) the action has **no resource types** and **only `ec2:Region`**. Its write twin `Replace` (L9401) is scoped by `instance*` and ~20 keys. The API prose calls the result "**your** IAM instance profile associations."
**Security Concern.** "Your" is enforced as **the account's**, not **the caller's**. There is no `aws:ResourceTag`, `ec2:InstanceID`, or resource ARN to pin the read to a team/workload subset. Any principal granted the action — including a nominally least-privilege read-only role — can enumerate **every** instance's attached instance-profile ARN account-wide. In a shared/multi-team account this is a cross-team visibility break that IAM **cannot** remediate short of denying the action entirely.
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** No IAM policy can restrict `DescribeIamInstanceProfileAssociations` to a tag/ARN subset. → **Oracle:** `iam:SimulateCustomPolicy` with a policy attempting `Condition: aws:ResourceTag` or a `Resource: arn:…:instance/i-xxx` on this action — the condition/resource is **ignored** (the action authorizes on `*`); a scoped-canary principal still returns *all* associations. **Confirm = full account result despite the scoping attempt.**
- **Claim:** The profile ARN disclosed per instance reveals privileged-role naming usable for the Replace chain. → **Oracle:** output contains `instance-profile/AdminProfile`-style ARNs for instances outside the caller's scope.
- **Doc-vs-enforcement:** trace the word "your" to a mechanism; there is none → **advisory-only guarantee** (Lens U), AWS-owned, worth noting even at Informational if a customer builds a containment assumption on it.
**Doc evidence:** `list_ec2.md` L6864 (no resource type, `ec2:Region` only); API ref "Describes **your** IAM instance profile associations." **Severity-if-true:** intra-account cross-team recon = **Medium** on its own (Low→Medium least-privilege-containment gap); **High as the enabling step of the Replace privesc chain (§5.2).**
**Stop condition:** once the full-result-despite-scoping behavior is shown under a scoped canary, stop — do not iterate across every instance.

### 5.2 — [PRIMARY] Recon→privesc chain hand-off (Lens B/X chain; rate at end-of-chain)
**Background.** The sibling plan's kill chain is: `Replace…`(swap privileged profile) → IMDS → STS creds for a role the caller was never granted. That chain needs a **target** `associationId`, the instance's **current** profile ARN, and the **instanceId**. This Describe supplies all three in one unprivileged call.
**Security Concern.** Denying/scoping the *write* actions does not deny the *targeting* data. An attacker who has (or later obtains) a scoped `Replace` can pre-select the highest-value instance (e.g. one already bound to an admin-ish profile, or a stopped instance) purely from Describe output; an attacker *without* Replace still gains a full inventory for lateral-movement planning.
**High-level Test Scenarios:**
- **Claim:** Describe output is a sufficient targeting oracle for `Replace`. → **Oracle:** every `associationId` returned is directly accepted by `ReplaceIamInstanceProfileAssociation` / `DisassociateIamInstanceProfile` (same opaque handle, no extra lookup). **Confirm from docs:** both write twins take `AssociationId` as their primary/only instance handle (sibling plan §2–§3).
- **Claim:** The read provides reconnaissance the write-side IAM scoping was meant to compartmentalize. → chain lead: Describe (unscopable, §5.1) + a tag-scoped Replace that the attacker's team *does* hold → attacker enumerates account-wide to find an in-scope-for-Replace instance whose profile can be upgraded.
**Doc evidence:** sibling plan; `API_ReplaceIamInstanceProfileAssociation.md` / `API_DisassociateIamInstanceProfile.md` (AssociationId input). **Severity-if-true:** **High–Critical at end of chain** (privilege escalation to a role the caller lacks) — but the Describe is only the *recon enabler*; the escalation proof lives in the sibling plan and must use synthetic canaries.
**Stop condition:** establishing the hand-off (Describe id → Replace accepts it) is the deliverable here; the live privesc PoC is the sibling plan's scope.

### 5.3 — Error / validator-divergence & enumeration oracle (Lens A variant)
**Background.** `AssociationId.N` and `Filter=instance-id` let the caller probe specific ids. IDs are intra-account and have no ownership checksum.
**Security Concern.** Even intra-account, a distinguishing response for a *known* id vs an *unknown/foreign-format* id can confirm the existence/state of a specific instance's association, and a divergent validator vs the write twins (e.g. Describe returns empty where Replace returns `InvalidAssociationID.NotFound`) is a low-grade oracle.
**High-level Test Scenarios:**
- **Claim:** A nonexistent/malformed `AssociationId` returns a distinguishing error vs a well-formed-but-absent one. → **Oracle:** compare responses for `iip-assoc-<valid-format-random>` (likely empty set / `InvalidAssociationID.NotFound`) vs a syntactically bad id (likely `InvalidAssociationID.Malformed` / 400) vs a real id (item returned). Record the 200-empty vs 400 vs NotFound split.
- **Claim:** `Filter=instance-id=i-<foreign>` confirms whether a specific instance has/lacks an association without any instance-level permission. → **Oracle:** association returned for an instance the caller cannot `DescribeInstances`.
- **Caveat (false-positive trap):** `DryRun` evaluates caller-IAM only *before* resource resolution — **not** an ownership oracle; do not treat a `DryRunOperation` success as evidence an association exists.
**Doc evidence:** `CommonErrors.md`; request params (AssociationId.N, Filter). **Severity-if-true:** **Low–Medium** (intra-account existence/state oracle; subsumed by §5.1's full-enumeration capability).
**Stop condition:** record the error-code split once; do not enumerate the id space.

### 5.4 — AWS-authored IAM-artifact audit (Lens R) — **CONFIRMED from docs**
**Background.** Because the action cannot be resource-scoped (§5.1), *every* managed/sample policy granting it necessarily grants account-wide association visibility on `Resource:"*"`. The authored root cause is explicit in `iam-policies-for-amazon-ec2.md`: **L73** "*Currently, the Amazon EC2 Describe\* API actions do not support resource-level permissions*" and **L351** "*the `Describe` actions do not support resource-level permissions, so you must specify them in a separate statement without conditions.*" AWS's own guidance structurally forces the scoped-write / unscopable-read asymmetry.
**Security Concern.** A customer attaching an AWS-managed policy inherits unscopable account-wide instance→role mapping; where the same policy also grants the write twin + `iam:PassRole`, recon and privesc are co-located in one copy-verbatim/uneditable artifact → **Tier-2 reportable** (not a customer footgun).
**Confirmed inventory (documentation, resolve live with `iam:GetPolicyVersion`):**
- **Pure read, Describe alone on `Resource:"*"`** (unscopable account-wide enumeration, no write): `ViewOnlyAccess` (explicit action, `Resource:"*"`), `ReadOnlyAccess` + `AmazonEC2ReadOnlyAccess` (via `ec2:Describe*`). These are how the recon primitive rides silently into nominally least-privilege read roles.
- **`AmazonEC2FullAccess`** (`ec2:*`): Describe **+ all three write twins** in one policy — but **no `iam:PassRole`** (caller must hold it separately). Recon+write co-located; privesc still needs an external PassRole.
- **`AWSQuickSetupManagedInstanceProfileExecutionPolicy`** — **the full kit in one managed policy:** Describe + `ec2:AssociateIamInstanceProfile` (scoped to `instance/*` with `ec2:InstanceProfile`/`ec2:NewInstanceProfile`) + **two condition-scoped `iam:PassRole` statements** (`iam:PassedToService`). Highest-value Lens R target — audit whether the `PassRole`/`NewInstanceProfile` scoping actually bounds the role set, or a prefix/service-condition lets a holder attach a more-privileged role.
- **Refuted doc-gap:** `AmazonSSMManagedInstanceCore` / `AmazonSSMFullAccess` / `AmazonSSMAutomationRole` do **not** grant it — the headline SSM-instance policy is *not* a source of this grant.
- **AWS sample policies (`ExamplePolicies_EC2.md`, "Work with IAM roles", `#iam-example-iam-roles`):** both Example 1 (L1483–1511) and Example 2 (L1524–1546) isolate `ec2:DescribeIamInstanceProfileAssociations` into its **own `Resource:"*"` statement** alongside tag/ARN-scoped write twins and a **prefix-wildcard `iam:PassRole`** (`role/DevTeam*`, `role/TestRole-*`). Prose L1473 is the authored rationale: "*Replacing or detaching an IAM role requires an association ID, therefore the policy also grants … `ec2:DescribeIamInstanceProfileAssociations`.*" Same shape in `systems-manager/.../quick-setup-assume-role.md` `SsmOnboardingInlinePolicy` (L51–89). → **This confirms the §5.1+§5.2 chain is AWS's *documented recommended* bundling: a scoped write that is useless without the unscopable read, so the read is granted on `*`.** Route the `role/TestRole-*` / `role/DevTeam*` prefix-PassRole analysis to the sibling plan's crown-jewel lead (prefix-wildcard PassRole → attach `TestRole-admin`).
- **Doc contradiction worth filing (Lens U):** `permission-to-pass-iam-roles.md` ("Grant permissions to attach an IAM role to an instance") lists required actions as `iam:PassRole` + Associate/Disassociate/Replace (+ console `iam:ListInstanceProfiles`) but **omits `ec2:DescribeIamInstanceProfileAssociations`** — even though Replace/Disassociate are unusable without it. The inconsistency with `ExamplePolicies_EC2.md` likely drives operators to over-grant it bundled in `ReadOnlyAccess` rather than scope it per-workflow.
**Doc evidence:** cited inline (managed-policy mirrors, `ExamplePolicies_EC2.md`, `iam-policies-for-amazon-ec2.md` L73/L351, `permission-to-pass-iam-roles.md`). **Severity-if-true:** read-only artifacts = Informational–Low (unscopable recon); `AWSQuickSetupManagedInstanceProfileExecutionPolicy` recon+write+PassRole kit = **High** if the PassRole/NewInstanceProfile scoping is defeatable → `aws-security` Tier-2.
**Stop condition:** statement-level confirmation of the actual live JSON (`GetPolicyVersion`); prove privesc only under a principal holding *exactly* the artifact, with synthetic canaries (sibling plan).

### 5.5 — Audit-log visibility of the recon step (Lens O)
**Background.** The call is a read-only management event.
**Security Concern.** Read/List events are logged by CloudTrail but are frequently excluded from alerting; the enumeration step of a privesc chain can run silently, and there is no data-plane equivalent an attacker must trip.
**High-level Test Scenarios:**
- **Claim:** `DescribeIamInstanceProfileAssociations` appears in CloudTrail as a read-only management event and produces no distinct security signal. → **Oracle:** confirm the event name/readOnly flag in `monitor-with-cloudtrail` docs; note it as a detection-gap enabler (not a standalone finding).
**Doc evidence:** `monitor-with-cloudtrail.md`. **Severity-if-true:** **Informational** (raises severity of §5.2 as an enabler).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Unscopable account-wide read of instance→profile→role map | IAM authorization of the action | "Describes **your** associations" + `ec2:Region`-only condition key — test that no scoping mechanism exists (§5.1) |
| Describe output used to target `Replace` privesc | Cross-action chain | Write-twin `instance*`/`PassRole` scoping — test that it does **not** cover the read targeting data (§5.2) |
| Existence/state oracle via AssociationId/Filter | Request validator | Opaque ids, common error types — test for validator divergence vs write twins (§5.3) |
| Weak AWS-authored read/privesc artifact | AWS-managed & sample policies | Documented least-privilege intent — audit actual JSON (§5.4) |
| Silent recon | CloudTrail | Read-only management-event logging — test detection gap (§5.5) |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-account / cross-tenant isolation.** Instance-profile associations are **account-local**; this API returns only the caller's account's data. There is no shared-fleet/multi-tenant surface here — do **not** pursue cross-tenant IDOR against it.
- **The write/privesc PoC itself.** Attaching a privileged profile and reading IMDS creds is the **sibling plan's** scope (`ReplaceIamInstanceProfileAssociation-attack-research-plan.md`), to be proven only with synthetic canary roles/instances.
- **AWS service plane.** Instance-identity role (`aws:ec2-instance`), SLR credentials, AWS-owned fleet accounts → **HARD STOP + disclose.**
- **IMDS on fully-managed hosts; single-tenant self-DoS; customer-authored over-broad policies** (footgun, not a defect).
- **Pagination "DoS."** `MaxResults` 5–1000 + `NextToken` is standard; no resource-exhaustion surface.

---

## 8. Null Hypotheses / Doc Gaps (lens + pages checked)

- **Lens A (cross-tenant IDOR): NULL.** Account-local read; no tenant/customer id input. (Checked: API ref request params, data types — only AssociationId/Filter/paging; no cross-account id.) Residual A-*variant* (intra-account existence oracle) retained as §5.3.
- **Lens C (credential vending/session): NULL.** No STS/session-policy/ProvidedContext/token input. (Checked: request params, CommonParameters.)
- **Lens D / V (data→control plane / network segmentation): NULL.** Pure control-plane read API; no ENI/VPC/socket surface. (Checked: API ref, no network fields.)
- **Lens E (RBAC privesc) / B (PassRole): NULL *on this action*.** No role ARN input, non-mutating. The PassRole/privesc risk lives on the write twins — captured as the chain §5.2 and in the sibling plan.
- **Lens F (injection/translation): NULL.** `Filter` is a fixed enum (`instance-id`, `state`), no free-form field-name/value reaching a backend language; no parser/wire-protocol surface. (Checked: `API_Filter.md`, request params.)
- **Lens G (SSRF) / Q (upload): NULL.** No URL/URI/location field the service dereferences; no blob/upload. (Checked: all request params, data types, examples — no `*Url`/`*Uri`/location/file field.)
- **Lens H (KMS/enc-context) / W (attestation): NULL.** No KMS key or attestation parameter. (Checked: request params.)
- **Lens I (tagging/ABAC): NULL *as a control*.** The action supports **no** tag condition key at all (that is precisely §5.1's finding) — ABAC cannot be applied, so there is no ABAC bypass to test; recorded as the scoping gap, not an ABAC lead.
- **Lens J (OAuth/3P) / K (prompt-injection) / FF (JWT/token): NULL.** No 3P linking, LLM, or bearer-token validation on this surface. (Checked: API ref, CommonParameters.)
- **Lens M (session interception): NULL.** No session/presigned/one-time-token identifier.
- **Lens N (namespace migration): NULL.** Single stable action name/API version (2016-11-15); no dual-live ARN/prefix.
- **Lens L (DoS): NULL / out of scope.** Standard pagination (§7).
- **Lens T (cross-service secret reachability): NULL.** The action generates/persists no secret.
- **Lens Y (transport/signature): standard SigV4 EC2 endpoint** — no action-specific weakness documented; defer to service-wide transport posture (not re-derived here).
- **Lens AA (share/revoke), BB (canonicalization), CC (upstream-context), DD (cache-key), EE (predictable-name): NULL.** No share/grant, no multi-parser front/origin split, no asserted-upstream-identity header, no cached authz decision, no predictable global namespace on this read action. (Checked: API ref, auth reference — the action has no resource/share/cache/edge surface.)
- **Doc gaps:** exact CloudTrail `readOnly`/event-name entry for this action (confirm against `monitor-with-cloudtrail` + CloudTrail event history); the precise set of AWS-managed policies carrying it (resolving via `GetPolicyVersion` — §5.4, subagent in progress). Marked "confirm first," not N/A.

---

## 9. Priority Summary

1. **§5.1 Unscopable account-wide read** (Lens S/U) — the defining property; confirm no IAM scoping possible.
2. **§5.2 Recon→privesc chain hand-off** (Lens B/X) — Describe is the targeting oracle for the sibling plan's Replace privesc; rate at end-of-chain **High–Critical**.
3. **§5.4 AWS-authored artifact audit** (Lens R) — managed/sample read policies carry it on `Resource:*`; Tier-2 if co-located with write-twin+PassRole.
4. **§5.3 Enumeration/validator oracle** (Lens A) — Low–Medium.
5. **§5.5 Audit-log visibility** (Lens O) — Informational enabler.
