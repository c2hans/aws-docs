# EC2 — "Grant permissions to attach an IAM role to an instance" — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/permission-to-pass-iam-roles.html` (`.md` twin fetched 2026-10-15) + corroborating `https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html` + AWS Service Authorization Reference (EC2 / IAM). Status: documentation-derived hypotheses only; nothing tested against a live account.

**Scope note / relationship to sibling plans.** This page is a single, thin **AWS-authored permissions/sample-policy page** — it defines the four actions a principal needs to launch-with / attach / replace / detach an instance profile, prints ONE example IAM policy, and adds a console caveat. It is therefore a **Lens R / S / B / EE / U** target almost exclusively (an uneditable, copy-verbatim artifact), not a network/parser/multi-tenant surface. It **COMPLEMENTS** [[iam-roles-for-amazon-ec2-attack-research-plan]] (which OWNS the broad instance-profile attach/replace/detach + IMDS-credential-vending privesc runtime surface, and already established that `iam:PassRole` IS enforced on all four code paths — the "Replace skips PassRole" myth is **refuted**, do not re-open it). This plan's distinct contribution is the **statement-by-statement audit of the printed example policy** and the **Note-vs-example least-privilege contradiction**. It does NOT restate the IMDSv2 / `ec2:RoleDelivery` / DHMC-confused-deputy material of the sibling plans ([[iam-policies-for-amazon-ec2-plan-note]], [[security-iam-awsmanpol-plan-note]], [[iam-policies-ec2-console-plan-note]]).

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **Primary safe oracle for every policy-scoping lead here is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** — it evaluates the printed artifact against a hypothetical request and touches **zero** resources. Escalate to a live scoped call (RunInstances + IMDS read) only with synthetic canary roles/instances in an authorized account.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (an AWS-fleet role, an AWS-owned instance profile), stop, preserve evidence, flag for AWS-Security disclosure.
- This is an **intra-account** privesc/sabotage surface (PassRole is same-account only — IAM doc Warning). Cross-account is explicitly out of band here; see §7.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes a hunter should try to produce, holding ONLY the example policy from this page (modeled under a scoped role, never the over-privileged tester):

1. **Non-admin → admin privilege escalation**: starting from the sample policy (+ a plausible companion grant such as `iam:CreateRole`/`iam:AttachRolePolicy`, or the mere existence of a privileged role whose name matches `DevTeam*`), obtain the credentials of a role more privileged than the holder, by passing it to an EC2 instance and harvesting it from IMDS.
2. **Intra-account cross-workload reach / sabotage**: attach, replace, or strip the instance profile of an EC2 instance owned by a *different* team/principal in the same account (the sample scopes the EC2 actions to `Resource:"*"` with no ownership condition).
3. **Demonstrate the omitted-condition-key gap**: show that the passed role is NOT pinned to the EC2 service (`iam:PassedToService`) nor to a specific instance (`iam:AssociatedResourceArn`), so the sample's `DevTeam*` role is passable far more broadly than "attach to one instance."
4. **Doc-integrity finding**: show the page's own **Note** ("specify the ARNs of specific IAM roles") is contradicted by the example it points to (a name-prefix wildcard + `Resource:"*"` EC2 actions with zero conditions).

---

## 2. Components, Assets, and Design

**What the page actually is:** a permissions prerequisite + one copy-verbatim example IAM policy. There is no service process, network interface, parser, or multi-tenant fleet on this page. The "assets" are IAM policy *statements* and the *roles/instance-profiles* they govern.

**The four governed actions (from the page):**
- `iam:PassRole` — permission (NOT an API call) that authorizes the caller to hand a role to EC2.
- `ec2:AssociateIamInstanceProfile` — attach a profile to a running instance that has none.
- `ec2:ReplaceIamInstanceProfileAssociation` — swap the profile on a running instance **in place, no reboot** (documented in sibling surface).
- `ec2:DisassociateIamInstanceProfile` — detach the profile from an instance.
- (`ec2:RunInstances` also appears in the example — launch-with-profile path.)
- (`iam:ListInstanceProfiles` — console-only addendum.)

**The printed example policy (the artifact under audit):**
```json
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
         "ec2:RunInstances",
         "ec2:AssociateIamInstanceProfile",
         "ec2:DisassociateIamInstanceProfile",
         "ec2:ReplaceIamInstanceProfileAssociation"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::123456789012:role/DevTeam*"
    }
  ]
}
```

**The data flow this policy unlocks (ASCII):**
```
 holder (sample policy)
    │ ec2:RunInstances / Associate / Replace  [Resource:"*", NO condition]
    ▼
 ANY EC2 instance in the account ──attaches──► instance profile ──wraps──► role matching DevTeam*
    │                                                                           │ (PassRole: prefix only,
    │ IMDS (169.254.169.254) /iam/security-credentials/<role>                   │  no PassedToService,
    ▼                                                                           │  no AssociatedResourceArn)
 temporary credentials of the DevTeam* role  ◄──────────────────────────────────┘
    │ (bypasses role's MaxSessionDuration — IMDS auto-refreshes)
    ▼
 holder now acts with that role's permissions
```

**Key design facts (grounding):**
- PassRole is **same-account only** (IAM doc Warning).
- PassRole is **checked on the CALLER** at the time the role ARN is supplied as a parameter (IAM doc: "The service then checks whether that user has the `iam:PassRole` permission").
- PassRole is scoped by the `Resource` element and optionally the `Condition` element (`iam:PassedToService`); the IAM doc's **own** examples use **name-prefix wildcards** (`EC2-roles-for-XYZ-*`, `RDS-*`) — so the `DevTeam*` prefix on this page is a sanctioned pattern, which is exactly what makes it exploitable when a prefix-matching privileged role exists or can be created.
- IAM doc **explicitly warns** that tag-based scoping of PassRole ("`ResourceTag` condition key ... does not have reliable results") is unreliable → the *only* reliable PassRole scoping is exact-ARN enumeration, which the sample does **not** do.

---

## 3. API / Interface Inventory

| Name | Method | Mutating | Authorized callers (per sample) | Scoping present in sample | Notes |
|---|---|---|---|---|---|
| `iam:PassRole` | permission (no API) | n/a | holder | `Resource: role/DevTeam*` **only** (no `iam:PassedToService`, no `iam:AssociatedResourceArn`) | NOT an API call → **no CloudTrail event for PassRole itself** |
| `ec2:RunInstances` | API | yes | holder | `Resource:"*"`, **no condition** | launch-with-profile; passes role via `IamInstanceProfile` param |
| `ec2:AssociateIamInstanceProfile` | API | yes | holder | `Resource:"*"`, **no condition** | attach profile to a running instance account-wide |
| `ec2:ReplaceIamInstanceProfileAssociation` | API | yes | holder | `Resource:"*"`, **no condition** | **in-place swap, no reboot**; stealthy |
| `ec2:DisassociateIamInstanceProfile` | API | yes | holder | `Resource:"*"`, **no condition** | strip profile account-wide (sabotage/DoS) |
| `iam:ListInstanceProfiles` | API | no | holder (console) | `Resource:"*"` (unscopable) | account-wide enumeration = recon oracle for targetable roles |

**Scoping facts — CONFIRMED from the AWS Service Authorization Reference (`list_ec2` / `list_iam`, 2026-10-15):**
- All three `*IamInstanceProfile` actions AND `RunInstances` anchor authz to the **`instance`** resource type only (ARN `arn:…:instance/${InstanceId}`). **No `instance-profile` or `iam-instance-profile-association` resource type exists in EC2** — so you can only scope these actions by *which instance* (not by *which association*). (EC2 does define a `role` resource type, but it is used only by the Nitro-Enclaves `*EnclaveCertificateIamRole` actions, never by instance-profile attach.)
- The `instance` resource type **does support `aws:ResourceTag/${key}` and `ec2:ResourceTag/${key}`** (plus `ec2:InstanceID`, `ec2:Region`, etc.) — so an **instance-ownership condition was fully available** on Associate/Replace/Disassociate but the sample **omits it** → Area 2.
- **Two distinct EC2 keys constrain which profile is attached, both omitted by the sample:** `ec2:InstanceProfile` ("ARN of an instance profile"; valid for RunInstances + all three attach actions) and `ec2:NewInstanceProfile` ("ARN of the instance profile *being attached*"; valid **only** for `AssociateIamInstanceProfile` + `ReplaceIamInstanceProfileAssociation` — **not** RunInstances, **not** Disassociate). This is the **key-name split / inert-Deny trap** (Lens S): a Deny written with `ec2:NewInstanceProfile` against RunInstances, or against Disassociate, is silently inert; cross-ref [[iam-roles-for-amazon-ec2-attack-research-plan]] §5A.
- `iam:PassRole` → resource type `role*` (required); condition keys = `aws:ResourceTag/${key}`, `iam:ResourceTag/${key}`, **`iam:AssociatedResourceArn`** (pin the role to the resource it's used on behalf of), **`iam:PassedToService`** (pin the service principal). Both scoping keys **confirmed to exist** and both **omitted** by the sample → Area 3.
- `iam:ListInstanceProfiles` → **no resource types and no condition keys** = fully unscopable account-wide enumeration → Area 6.
- **ResourceTag trap:** `aws:ResourceTag`/`iam:ResourceTag` ARE accepted condition keys for PassRole (the policy engine won't error), yet the IAM doc warns tag-based PassRole scoping "does not have reliable results" — so a customer who reaches for the obvious tag condition gets a policy that *validates* but does not reliably bind (fail-open-ish).

---

## 5. Recommended Areas of Focus

### AREA 1 — Role-name-prefix privilege escalation via the sample's `DevTeam*` PassRole (Lens R / EE / B / E) — **HIGH**
**Background.** The example scopes `iam:PassRole` to `arn:aws:iam::123456789012:role/DevTeam*` — a **name prefix**, not a specific role ARN. The IAM PassRole doc confirms prefix wildcards are the sanctioned idiom and warns, verbatim, "you should make sure that a user doesn't pass a role where the role has more permissions than you want the user to have."

**Security Concern.** A principal holding only this sample policy can pass **any** role whose name begins `DevTeam` to an instance and then read that role's live credentials from IMDS. If (a) a privileged role named `DevTeam…` already exists, or (b) the holder also has `iam:CreateRole`+`iam:AttachRolePolicy` (common in a dev account), the holder **mints `DevTeamAnything` with elevated/admin policies and escalates**. IMDS-vended creds also **bypass the role's `MaxSessionDuration`** (IMDS auto-refreshes) — cross-ref sibling §5A.

**High-level Test Scenarios (falsifiable):**
- **Claim:** The sample authorizes passing `role/DevTeamAdmin` (a hypothetical admin role) to an instance. → **Oracle:** `iam:SimulateCustomPolicy` with the exact sample JSON, action `iam:PassRole`, resource `arn:aws:iam::123456789012:role/DevTeamAdmin` → `allowed`. Repeat for `iam:PassRole` on `role/DevTeam` + `*` suffixes.
- **Claim:** With `iam:CreateRole` added, holder self-escalates. → **Oracle (live, canary only):** create `DevTeamCanary` with a scoped canary policy + EC2 trust policy, `RunInstances` with `IamInstanceProfile`, SSH/SSM to the instance, `curl http://169.254.169.254/latest/meta-data/iam/security-credentials/DevTeamCanary` → returns temp creds for the role the holder could not assume directly.
- **Claim:** The prefix also matches roles the admin never intended (e.g. a future `DevTeamBilling` with broad billing perms). → enumerate via `iam:ListInstanceProfiles` / `iam:ListRoles` (recon, Area 7).

**Preconditions / Cost.** Low. Simulate = free, no resources. Live PoC = 1 instance + 1 role (tear down).
**Severity-if-true.** Non-admin → admin = **High**. Reportable as a **Tier-2 weak AWS-authored sample** because the artifact is copy-verbatim and the page frames it as the least-privilege remedy (see Area 4).
**Stop condition.** The moment a prefix-matched role resolves to an **AWS-service-plane** identity → HARD STOP, do not read its creds.

### AREA 2 — `Resource:"*"` + zero condition on the three instance-profile actions = account-wide attach/replace/strip (Lens S / E / L) — **MEDIUM–HIGH**
**Background.** The first statement grants `AssociateIamInstanceProfile`, `ReplaceIamInstanceProfileAssociation`, `DisassociateIamInstanceProfile` (and `RunInstances`) on `Resource:"*"` with **no `Condition`**. The `instance` resource type for these actions **supports** `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:InstanceID` (instance-ownership scoping) and `ec2:InstanceProfile`/`ec2:NewInstanceProfile` (which-profile scoping) — the sample uses **none of them**, so both the *target instance* and the *attached profile* are unconstrained.

**Security Concern.** The holder can operate on the instance-profile association of **any EC2 instance in the account**, not just instances it created:
- **Attach** a `DevTeam*` role (Area 1) to a victim instance → if the holder can reach that instance's IMDS (e.g. it is a build host the holder can run code on), harvest the newly-attached role → cross-team reach.
- **Replace** the live profile on a victim instance **in place, no reboot** → stealthy swap (cross-ref sibling §5A "ReplaceIamInstanceProfileAssociation in-place").
- **Disassociate** / strip the profile from any instance → the instance's workload loses its credentials → **sabotage / availability DoS** on another team's service.

**High-level Test Scenarios:**
- **Claim:** The sample authorizes `ec2:AssociateIamInstanceProfile` against `instance/<some-other-teams-instance-id>`. → **Oracle:** `SimulateCustomPolicy`, action `ec2:AssociateIamInstanceProfile`, resource = a foreign instance ARN → `allowed` (because `Resource:"*"`). Contrast with a tightened variant that adds `aws:ResourceTag/Team` → should flip to `implicitDeny`, proving the gap is the missing condition, not the action.
- **Claim:** Replace/Disassociate are equally unconditioned. → same oracle for both actions.
- **Claim (defense-in-depth the sample skips):** adding `"Condition":{"ArnLike":{"ec2:NewInstanceProfile":"arn:aws:iam::123456789012:instance-profile/DevTeam*"}}` to the Associate/Replace grant would independently cap *which* profile can be attached (blunting Area 1's "attach an admin role" even if PassRole scoping is loose). → **Oracle:** show the un-conditioned sample allows attaching a profile wrapping `DevTeamAdmin`, while the `ec2:NewInstanceProfile`-conditioned variant denies a profile outside the prefix. Note the inert-Deny trap: the same key against RunInstances or Disassociate does nothing.
- **Refute path:** if the hunter's test account enforces an SCP/permission-boundary adding an instance tag condition, the sample's breadth is masked — note that the *sample as printed* is still the artifact-level defect.

**Preconditions / Cost.** Low (simulate). Live cross-team PoC needs a second canary instance under a different principal.
**Severity-if-true.** Intra-account cross-workload privesc/sabotage = **Medium–High** (High when chained with Area 1 to land an admin role on a reachable victim instance).
**Stop condition.** Do not strip/replace a profile on any instance you cannot prove is a canary; sabotage of a real workload is out of scope.

### AREA 3 — Omitted PassRole condition keys: `iam:PassedToService` and `iam:AssociatedResourceArn` (Lens B / S) — **MEDIUM (hardening/enabler)**
**Background.** The IAM PassRole doc names `iam:PassedToService` ("specify the service principal of the service to which a role can be passed") as the correct narrowing control. AWS also documents `iam:AssociatedResourceArn` to pin a passed role to the specific resource (instance) it is attached to. The example policy on this page uses **neither**.

**Security Concern.** Because the `DevTeam*` roles are passable without `iam:PassedToService: ec2.amazonaws.com`, the same grant lets the holder pass those roles to **any other PassRole-accepting service** (Lambda, CodeBuild, Glue, …), widening blast radius beyond "attach to an EC2 instance." Because there is no `iam:AssociatedResourceArn`, the role is not pinned to one instance ARN (the mechanism that would convert Area 2 from "any instance" to "one instance"). The three EC2 UserGuide permission pages teach **neither** key (cross-ref sibling §5A).

**High-level Test Scenarios:**
- **Claim:** Under the sample, `iam:PassRole` of `role/DevTeamX` to a **non-EC2** service principal is still allowed. → **Oracle:** `SimulateCustomPolicy` with `iam:PassedToService` set to e.g. `lambda.amazonaws.com` in the request context → `allowed` (sample has no condition to deny it). Then show a tightened sample adding `"Condition":{"StringEquals":{"iam:PassedToService":"ec2.amazonaws.com"}}` flips Lambda to deny.
- **Claim:** `iam:AssociatedResourceArn` is a valid PassRole condition key that *could* pin the role to one instance but is absent. → **CONFIRMED present** in the IAM Service Authorization Reference (PassRole condition keys = `aws:ResourceTag`, `iam:ResourceTag`, `iam:AssociatedResourceArn`, `iam:PassedToService`); the sample uses none of the scoping pair. A tightened sample pinning both — `iam:PassedToService=ec2.amazonaws.com` and `iam:AssociatedResourceArn=arn:…:instance/<id>` — would convert Area 1/2 breadth from "any role to any instance via any service" to "this role to this instance via EC2."

**Severity-if-true.** Hardening gap / enabler that sets the breadth of Areas 1–2 = **Medium**. Tier-2 (the AWS sample omits controls AWS documents elsewhere).

### AREA 4 — Note-vs-example least-privilege contradiction (Lens U — doc-guarantee vs artifact) — **LOW / INFORMATIONAL**
**Background.** The page's **Note** says: *"To follow the best practice of least privilege, specify the ARNs of **specific IAM roles** with iam:PassRole, as shown in the example policy below."* It presents the example as the least-privilege remedy.

**Security Concern.** The example does **not** specify specific role ARNs — it uses a **name-prefix wildcard** (`role/DevTeam*`, Area 1) — and it leaves `ec2:RunInstances` + all three instance-profile actions on `Resource:"*"` with **zero conditions** (Area 2). The artifact the Note cites as the least-privilege exemplar therefore violates the very bar the Note sets. A customer who copies it believing it is "least privilege" inherits Areas 1–3.

**High-level Test Scenarios:**
- **Claim:** The example contradicts the Note's "specify the ARNs of specific IAM roles". → **Oracle:** textual — prefix wildcard ≠ specific ARN; `Resource:"*"` on the EC2 actions ≠ least privilege. Self-evident from the page.
- Severity-if-true: **Informational / Low** (AWS-owned doc defect) — but worth filing because it propagates Areas 1–3 to every customer who trusts the "best practice" label.

### AREA 5 — PassRole is invisible to CloudTrail (Lens O — audit evasion enabler) — **LOW / INFORMATIONAL**
**Background.** IAM doc, verbatim: *"PassRole is not an API call ... no CloudTrail logs are generated for IAM PassRole."* Attribution requires correlating the enclosing `RunInstances` / `AssociateIamInstanceProfile` / `ReplaceIamInstanceProfileAssociation` event.

**Security Concern.** The escalation in Areas 1–2 leaves **no `PassRole` event**; a defender must notice the `ReplaceIamInstanceProfileAssociation` (in-place, no reboot — easy to miss) or `RunInstances` record and reason about which role was attached. This lowers the detection cost of the whole chain.

**Scenarios / Oracle.** Confirm no `PassRole` event appears for a role attach in CloudTrail; confirm the `Replace…`/`Run…` event does record the passed `IamInstanceProfile` ARN (so the signal exists, just not where a defender expects "PassRole").
**Severity:** Informational enabler (raises stealth of Areas 1–2).

### AREA 6 — `iam:ListInstanceProfiles` account-wide enumeration (Lens A/O — recon) — **LOW**
**Background.** The console addendum requires `iam:ListInstanceProfiles`, which (confirm via Service Authorization Reference) is `Resource:"*"`-only / unscopable.

**Security Concern.** It enumerates **every instance profile in the account**, revealing which privileged roles exist and are already wrapped in a profile — directly feeding target selection for Area 1 (which `DevTeam*`-matching or otherwise-passable profiles to go after).
**Oracle:** `SimulateCustomPolicy` shows `iam:ListInstanceProfiles` cannot be resource-scoped; live call returns all profiles.
**Severity:** Low (recon enabler).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Pass a more-privileged `DevTeam*` role, harvest its IMDS creds → privesc | `iam:PassRole` prefix in sample | The prefix `role/DevTeam*` + "specify specific role ARNs" Note (unenforced) |
| Attach/replace/strip profile on a foreign-owned instance | `ec2:*IamInstanceProfile` on `Resource:"*"` | None in the sample (no ownership/tag `Condition`) |
| Pass the `DevTeam*` role to a non-EC2 service | missing `iam:PassedToService` | `iam:PassedToService` documented but omitted from sample |
| Role not pinned to one instance | missing `iam:AssociatedResourceArn` | `iam:AssociatedResourceArn` documented but omitted |
| Escalation leaves no `PassRole` audit record | CloudTrail | "PassRole is not an API call" (by design — correlate enclosing event) |
| Enumerate privileged profiles to target | `iam:ListInstanceProfiles` | None (unscopable) |
| Doc claims the sample is least-privilege | the Note | Contradicted by the sample it cites |

---

## 7. Out-of-Scope Risk Categories
- **Cross-account PassRole** — PassRole is same-account only (IAM doc Warning); a cross-account bridge is a different role's trust policy, not this page.
- **Runtime "does Replace/Associate/RunInstances enforce PassRole" question** — already **resolved (yes, enforced on all four paths)** by [[iam-roles-for-amazon-ec2-attack-research-plan]]; do not re-open. This plan audits the *printed artifact*, not the enforcement path.
- **IMDSv2 / `ec2:RoleDelivery` / IMDS endpoint governance** — owned by the sibling plans; not on this page.
- **Customer-authored tightenings** — if a hunter's test account layers an SCP/permission boundary, that masks the sample's breadth but does not change the artifact-level defect.
- **A customer who edits the sample to use exact ARNs** — then it is their own composition; the finding is specifically about the **AWS-authored copy-verbatim example** (Tier-2).
- Any AWS-service-plane role surfacing behind a prefix match → **HARD STOP**, disclose.

## 8. Null hypotheses / doc gaps
Lenses that did **not** fire on this page, with the surface checked:
- **A (cross-tenant IDOR), C (credential vending/STS session scope), D/V (network/control-plane), F (injection/parser), G (SSRF), H (KMS), I (tagging ABAC runtime), J (OAuth), K (prompt injection), M (session interception), N (ARN migration), Q (upload), T (cross-service secret store), W (attestation), Y (transport/TLS/sig), AA (share/revoke lifecycle), BB (parser-differential), CC (upstream-context injection), DD (cache), FF (JWT/token)** — **N/A**. Checked: this is the single `permission-to-pass-iam-roles` page plus the IAM `id_roles_use_passrole` reference. There is no network interface, no server-side fetch field, no multi-tenant fleet, no parser, no token, no upload, no KMS/attestation surface, no cache, and no cross-account path on this page. (The IMDS credential-vending the chain *lands on* is runtime surface owned by the sibling plan, not introduced here.)
- **X (action-family parity)** — fired only to be **resolved**: PassRole enforcement parity across RunInstances/Associate/Replace/Disassociate is confirmed-equal by the sibling plan; the `ec2:NewInstanceProfile` vs `ec2:InstanceProfile` key-name split is the relevant Lens-S trap, cross-referenced in §3.
- **Doc gaps — RESOLVED** (Service Authorization Reference, `list_ec2`/`list_iam`, 2026-10-15): (1) the three `*IamInstanceProfile` actions anchor to the `instance` resource type, which **does** support `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:InstanceID` — ownership scoping was available and omitted; no `instance-profile`/association resource type exists. (2) `iam:AssociatedResourceArn` **and** `iam:PassedToService` are both confirmed valid `iam:PassRole` condition keys (both omitted by the sample). (3) `iam:ListInstanceProfiles` is confirmed resource-`*`-only with zero condition keys. (4) `ec2:NewInstanceProfile` is valid only for Associate/Replace; `ec2:InstanceProfile` for those plus RunInstances; neither for the sample — the key-name split is a live inert-Deny trap. Areas 2/3/6 are fully grounded.

---
Generated by the security-questionbuilder skill (documentation-only). All leads are falsifiable hypotheses with `iam:SimulateCustomPolicy` as the safe first oracle; nothing in this plan was tested against a live account.
