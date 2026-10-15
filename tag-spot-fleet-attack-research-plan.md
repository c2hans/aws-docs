# Spot Fleet *Tagging* — Attack Research Plan

**Source of leads:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tag-spot-fleet.html` ("Tag a new or existing Spot Fleet request and the instances and volumes it launches") and its immediate tagging neighborhood — `Using_Tags.html`, `ExamplePolicies_EC2.html` (anchors `#iam-example-taggingresources`, `#iam-example-runinstances-tags`), `spot-fleet-prerequisites.html` — reconciled against the **authoritative AWS IAM Service Authorization Reference** `https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html` (`list_ec2`, NOT the dead `list_amazonec2` slug).
Offline mirror: `/work/aws-docs/docs/**`. **Online `.md` twins cross-checked** (append `.md` to any `.html`): every audited page — `tag-spot-fleet`, `spot-fleet-prerequisites`, `create-spot-fleet`, `work-with-spot-fleets`, `Using_Tags`, `ExamplePolicies_EC2`, and the entire `list_ec2` actions/resource-types/condition-keys tables — was **byte-for-byte identical** offline vs online (differences limited to the mirror's `source_url` front-matter and trailing-whitespace noise). No sync gaps.
**Status:** Documentation-derived hypotheses only. **Nothing in this plan has been tested against a live AWS account.** It is the plan a hunter (e.g. `aws-vuln-hunter`) executes next.
**Produced by:** `security-questionbuilder` skill — orchestrator pass on the tagging page + two documentation-only subagents (IAM Service Authorization Reference verification; instance/volume tag-provenance across the role model).

> **Relationship to the sibling plans (read these first; this plan deliberately does NOT re-derive their leads).**
> - `spot-fleet-attack-research-plan.md` — the broad Spot Fleet plan (request lifecycle, SLRs, auto-scaling, KMS). Its **I1** notes the *under-tagging → ABAC-escape* angle.
> - `spot-fleet-prerequisites-attack-research-plan.md` — the permissions/IAM-artifact plan. It owns the **PassRole / confused-deputy / `TerminateInstances`-on-`*` / `RegisterTargets */*` / privesc-chain** leads (its R1–R6, P1–P3) and its **I1** also covers under-tagging.
> **Both siblings repeat the User-Guide claim "resource-level permissions are not supported for `spot-fleet-request`" as settled fact.** This plan's headline contribution (§5 **U1**) is that the **authoritative IAM reference contradicts that claim**, and works through what the contradiction means for tag governance either way. Everything here is scoped to the **tagging authorization model**; where a tagging lead touches the fleet role's broader powers, it cross-references the siblings rather than restating them.

---

## 0. How to use this document

- Each lead is a falsifiable claim: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in the priority order of §5. Look left and right for adjacent bugs.
- **Prefer the safe oracle first.** Every lead here is confirmable **before touching any live resource** with read-only `iam:GetPolicyVersion` / `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` and `aws ec2 … --dry-run`. The one empirical unknown that docs cannot settle — *does the `RequestSpotFleet`/`CreateTags` runtime actually accept or reject a resource-scoped `spot-fleet-request` policy?* — is resolved with a single `--dry-run` or a synthetic-canary call in an account you are authorized to test, torn down immediately.
- **This service runs entirely inside the customer's own account.** There is no multi-tenant service fleet, no customer-reachable data plane. The cross-tenant surface is therefore null; the value is **intra-account privilege / governance manipulation via the tag model**, plus **AWS-authored guidance that teaches an over-broad grant** (in-scope per the Lens R/U carve-out: the weak default ships in an AWS-published sample policy the customer is told to copy verbatim).
- **HARD STOP:** The only true AWS-service-plane identities in scope are `spotfleet.amazonaws.com`, `AWSServiceRoleForEC2SpotFleet`, and `AWSServiceRoleForEC2Spot`. Treat read-only. The moment any evidence shows a credential/ARN/account belonging to AWS's own fleet/service plane, **stop, preserve evidence, flag for AWS-Security disclosure.**

---

## 1. Pentest Objectives (concrete breach outcomes to attempt)

1. **Reconcile the doc-vs-reference contradiction (U1).** Determine empirically whether `ec2:CreateTags`/`ec2:RequestSpotFleet` scoped to `arn:…:spot-fleet-request/*` is **rejected at runtime** (User Guide claim) or **honored** (IAM reference claim). Either answer is a reportable AWS-owned defect — a dangerous over-grant taught by the docs, *or* a formally-advertised resource type/condition-key set the runtime silently refuses.
2. **Over-grant → ABAC self-widening (S1).** As a principal holding **only** the AWS-published tagging prerequisite policy (`ec2:CreateTags` + `ec2:RequestSpotFleet` on `Resource:"*"`), add/overwrite/remove an `aws:ResourceTag`-keyed tag on a resource the holder otherwise cannot manage, to **pass an ABAC Allow or strip a Deny / SCP / backup / cost-allocation tag** anywhere in the account.
3. **Tag-on-create governance bypass (U2).** Show that an IAM/SCP policy intended to *mandate* tags on fleet creation via `aws:RequestTag`/`aws:TagKeys` on `ec2:RequestSpotFleet`, or to gate `Cancel`/`Modify` via `aws:ResourceTag`, is **silently unenforceable** for Spot Fleet (either because the runtime rejects the resource scoping, or because the legacy API does not evaluate the resource).
4. **Fleet-role tag-provenance bypass (I1).** Show that tag keys/values a caller is **forbidden to apply directly** (by their own `aws:TagKeys`/`aws:RequestTag` conditions) are nonetheless stamped onto fleet-launched **instances/volumes** because the **assumed fleet role**, not the caller, performs the `CreateTags` — so the caller's ABAC tag restrictions do not propagate.
5. **Reserved-tag write boundary (I2).** Determine whether `ec2:CreateTags` can set the `aws:ec2spot:fleet-request-id` reserved/service tag key on an arbitrary instance — the gate on whether the sibling plans' SLR tag-presence `TerminateInstances` (prereq-plan R2 / broad-plan S1) becomes a *victim-instance-termination* primitive.

---

## 2. Components, Assets, and Design

**What this surface is.** The tag model for the legacy Spot Fleet (`RequestSpotFleet`) family. Three *distinct* tagging sub-flows, each with a different acting identity:

| Sub-flow | What is tagged | Who sets the tag (acting identity) | How specified |
|---|---|---|---|
| **Fleet-request tag-on-create** | the `spot-fleet-request` (`sfr-…`) | the **calling user** | `TagSpecifications` with `ResourceType:spot-fleet-request` inside `SpotFleetRequestConfig` |
| **Fleet-request tag-after** | existing `sfr-…` | the **calling user** | standalone `ec2:CreateTags` / console "Tags" tab |
| **Instance tag-on-launch** | fleet-launched `instance` | the **assumed fleet role** (`IamFleetRole` / SLR), *not* the user | `TagSpecifications` with `ResourceType:instance` in `LaunchSpecifications`, or the launch template |
| **Volume tag-on-launch** | fleet-launched `volume` (On-Demand only) | the **assumed fleet role** | launch template only ("Volume tagging in `LaunchSpecifications` is not supported"; "only … volumes attached to On-Demand Instances") |

**The split acting-identity is the entire security story of this page.** The user tags the *request*; the service role tags the *instances/volumes it launches on your behalf*. Any ABAC/tag condition on the **user's** policy governs only the first; the second runs under the role's policy.

**AWS-authored artifacts shipped on the tagging path (copy-verbatim, in-scope):**
- The **tagging prerequisite policy** (`tag-spot-fleet` → "Prerequisite"): `ec2:CreateTags` + `ec2:RequestSpotFleet` on `Resource:"*"`, **no condition** — the page says "For `Resource`, you **must** specify `"*"`."
- `AmazonEC2SpotFleetTaggingRole` (AWS-managed, v5) — recommended for `IamFleetRole`; its `ec2:CreateTags` on `*` is **unconditioned** (full artifact audit is prereq-plan R1 — cross-ref, not restated).
- The broader user sample policy on `spot-fleet-prerequisites` (unconditioned `ec2:CreateTags` on `*` alongside the fleet APIs).

**Authoritative IAM facts (from `list_ec2`, both offline + online, identical):**
- `spot-fleet-request` **IS a formal resource type:** ARN `arn:${Partition}:ec2:${Region}:${Account}:spot-fleet-request/${SpotFleetRequestId}`; condition keys `aws:RequestTag/${TagKey}`, `aws:ResourceTag/${TagKey}`, `aws:TagKeys`, `ec2:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:Attribute[/…]`.
- `ec2:RequestSpotFleet` lists `spot-fleet-request*` **as a REQUIRED resource type** (also `image`, `key-pair`, `launch-template`, `placement-group`, `security-group`, `snapshot`, `subnet`), with `aws:RequestTag`/`aws:TagKeys` condition keys on it.
- `ec2:CancelSpotFleetRequests` **requires** `spot-fleet-request*` (sole type); supports `aws:ResourceTag`/`ec2:ResourceTag`.
- `ec2:ModifySpotFleetRequest` **requires** `spot-fleet-request*`; supports `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Attribute`.
- `ec2:CreateTags` lists `spot-fleet-request` (optional) with `aws:RequestTag`, `aws:ResourceTag`, `aws:TagKeys`, `ec2:CreateAction`, `ec2:ResourceTag`. `ec2:DeleteTags` the same minus `ec2:CreateAction`.
- `ec2:DescribeTags` / `ec2:DescribeSpotFleetRequests`: no resource types (Resource `*` only), only `ec2:Region`.

→ **The IAM reference flatly contradicts the User Guide's "resource-level permissions are not currently supported for the `spot-fleet-request` resource … you must specify `"*"`."** That contradiction is lead **U1**.

```
 Caller (holds AWS tagging-prereq policy: CreateTags + RequestSpotFleet on "*")
   │
   │ (a) TagSpecifications[spot-fleet-request]  ── tagged by CALLER ───────────────┐
   │ (b) standalone CreateTags on sfr-/instance/volume/* ── tagged by CALLER ──────┤  governed by caller's (forced-"*") policy
   │                                                                               │  → aws:RequestTag/aws:TagKeys/ec2:CreateAction apply HERE only
   │ RequestSpotFleet(IamFleetRole, LaunchSpecifications[... TagSpecifications[instance]])
   ▼
 Spot Fleet control plane ── sts:AssumeRole ─► IamFleetRole / AWSServiceRoleForEC2SpotFleet
                                                   │ RunInstances + CreateTags on *  (role's OWN policy, UNCONDITIONED)
                                                   ▼
                               instance / volume tagged by the ROLE  ◄── caller's tag conditions do NOT run here (I1)
```

---

## 3. API / Interface Inventory (tagging-relevant)

| Name | Method | Mutating | Facing | Functionality | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ec2:CreateTags` | SDK/Query/CLI | **Yes** | External | Tag/overwrite tags on existing resources | Yes | Caller **and** fleet role **and** SLR | UG forces `Resource:"*"`; IAM-ref says scopable w/ `ec2:CreateAction`/`aws:RequestTag`. Overwrites existing values. |
| `ec2:DeleteTags` | SDK/Query/CLI | **Yes** | External | Remove tags from existing resources | Yes | Caller (via `*` grant) | Not on the UG prereq policy, but the forced `*` + ABAC-strip angle lives here (S1). |
| `ec2:RequestSpotFleet` (`TagSpecifications`) | SDK/Query | **Yes** | External | Create fleet request + tag-on-create (request & instances) | Yes | Caller w/ `RequestSpotFleet`+`PassRole` | IAM-ref: `spot-fleet-request*` **required**, `aws:RequestTag`/`aws:TagKeys` supported. `ResourceType` must be exactly `spot-fleet-request`/`instance` or the request **fails**. |
| `ec2:DescribeTags` | SDK/Query | No | External | List tags; `--filters resource-id/resource-type` | Yes | Caller; Resource `*` only | Cannot be resource-scoped (no resource types / only `ec2:Region`). |
| `ec2:DescribeSpotFleetRequests` | SDK/Query | No | External | Returns fleet config **including its tags** | Yes | Caller; Resource `*` only | Second path to read a fleet's tags. |

**Doc-flagged pointers kept verbatim:**
- `tag-spot-fleet`: "Resource-level permissions are not currently supported for the `spot-fleet-request` resource. If you specify `spot-fleet-request` as a resource, you will get an unauthorized exception when you try to tag the fleet." + "For `Resource`, you **must** specify `"*"`."
- `tag-spot-fleet`: "If you specify another value [for `ResourceType`], the fleet request will fail." (brittle validator)
- `spot-fleet-prerequisites`: "the differences in the permissions that are set for the user and the `IamFleetRole` might lead to **inconsistent tagging behavior** of instances in the fleet … **While we are working to fix this inconsistency** …" (AWS acknowledges a tagging-authz bug).
- `Using_Tags`: "**If tags cannot be applied during resource creation, we roll back the resource creation process.** … resources are either created with tags or not created at all" and "**Your resources are properly secured from creation** — tags are applied immediately … any tag-based resource-level permissions controlling the use of resources are immediately effective." (Lens U guarantee — written for the direct `RunInstances` caller, not the fleet-role path.)
- `ExamplePolicies_EC2` ("Surprise inconsistency"): for `spot-instances-request`, "this policy will not be evaluated if there are no … tags, so a non-tag Spot on Run request will succeed" — a documented precedent that Spot-family resource types bypass normal tag-conditional evaluation.

---

## 4. Boundary-lens catalog — firing lenses

(Lenses whose triggers are owned by the sibling plans — B/confused-deputy, R-artifact-audit of `TerminateInstances`/`RegisterTargets`, P-privesc-chain, H-KMS, auto-scaling L — are **not** restated here. Pages checked for each non-firing lens are named in §8.)

### Lens U — Documented-guarantee vs actual-enforcement / doc-vs-reference integrity  (HIGHEST YIELD — the headline)

**U1 — User-Guide "no resource-level permissions / must use `Resource:"*"`" contradicts the authoritative IAM reference.**
**Claim:** `tag-spot-fleet` instructs the customer to grant `ec2:CreateTags` + `ec2:RequestSpotFleet` on `Resource:"*"` and asserts resource-level permissions are "not supported" for `spot-fleet-request`. The IAM Service Authorization Reference contradicts this: `spot-fleet-request` is a formal resource type with an ARN and condition keys, `RequestSpotFleet` marks it **required**, and `CreateTags` lists it as a scopable resource type with `ec2:CreateAction`/`aws:RequestTag`. **At most one source is right, and either way AWS owns a defect:** (a) if the IAM reference is correct, the User Guide teaches an **unnecessary account-wide over-grant** (`CreateTags`/`RequestSpotFleet` on `*`) that could instead be scoped — a copy-verbatim AWS-published sample-policy footgun (in-scope, Lens R/U carve-out); (b) if the User Guide is correct, the IAM reference **advertises an ARN, a required-resource marker, and condition keys the runtime silently refuses**, so any policy/SCP author who scopes by them is **unknowingly running an inert or request-breaking policy**.
**Mechanism:** `tag-spot-fleet` "Prerequisite" + "Important" callout vs `list_ec2` actions/resource-types tables (quoted in §2). Reconciliation note [[reference-aws-iam-service-auth-ref-url]] warns the User-Guide prose can contradict the authoritative reference — this is a confirmed instance.
**Confirm/Refute oracle:** read-only first — `iam:SimulateCustomPolicy` with a policy scoping `ec2:CreateTags`/`ec2:RequestSpotFleet` to `arn:…:spot-fleet-request/*` and `--resource-arns` a concrete `sfr-` ARN → does the simulator return `allowed` (IAM-ref model holds) or `implicitDeny`? Then the **decisive empirical step**: one `aws ec2 request-spot-fleet --dry-run` under a canary principal whose policy is scoped to `spot-fleet-request/*` (not `*`), and one `aws ec2 create-tags --resources sfr-… --dry-run` likewise → `DryRunOperation` (accepted → UG wrong) vs `UnauthorizedOperation` (rejected → UG right). Treat `DryRun` as caller-IAM-only (per the broad plan's A-oracle note), so for `CreateTags` confirm with a real synthetic `sfr-` + scoped policy, torn down.
**Preconditions / Cost:** one canary IAM user/role; free to simulate; one or two dry-runs. **Severity-if-true:** branch (a) over-grant guidance = Medium (AWS-authored, account-wide `CreateTags`/`DeleteTags` blast radius — see S1); branch (b) doc-vs-reference inconsistency with governance impact = Low–Medium (Informational on the pure inconsistency, Medium if a customer builds a tag-governance control on the false capability). **Stop:** record which source wins; do not actually tag foreign resources.

**U2 — Mandatory-tag-on-create governance is unenforceable for the legacy fleet API.**
**Claim:** A common governance control is an IAM/SCP that *denies* a create unless `aws:RequestTag/<k>` is present (so every resource is born tagged). `Using_Tags` promises "resources are either created with tags or not created at all … properly secured from creation." For `ec2:RequestSpotFleet`, if U1 branch (b) holds (runtime ignores resource-level scoping on `spot-fleet-request`), that Deny **never binds** — and the documented "Surprise inconsistency" for the sibling `spot-instances-request` type ("not evaluated if there are no tags → a non-tag request succeeds") is direct precedent that the Spot family evaluates the resource only *when a tag is already present*, i.e. a request with **no** tags slips past a `RequestTag`-conditioned Deny. A fleet (and its launched instances) can thus be created **untagged** despite a mandatory-tagging policy.
**Mechanism:** `Using_Tags` guarantee; `ExamplePolicies_EC2` "Surprise inconsistency" precedent; `list_ec2` shows `RequestSpotFleet` *does* list `aws:RequestTag`/`aws:TagKeys` (so an author will reasonably try it) — the gap is whether evaluation fires on the empty-tag path.
**Confirm/Refute oracle:** `iam:SimulateCustomPolicy` for `RequestSpotFleet` with a `Deny … Condition: Null{aws:RequestTag/<k>: true}` or `StringNotEquals aws:RequestTag/<k>` under (i) a request context carrying the tag and (ii) one carrying none → if the no-tag case returns `allowed`, the mandatory-tag control fails open. Live: a canary `--dry-run request-spot-fleet` with no `TagSpecifications` under the Deny policy.
**Preconditions / Cost:** canary IAM; simulate + one dry-run. **Severity-if-true:** Medium (governance/compliance control silently fails open; untagged fleet resources also feed the broad-plan I1 ABAC-escape). **Owner-to-fix:** AWS (legacy-API tag-evaluation semantics).

### Lens S — Over-granted `CreateTags`/`DeleteTags` on `*` as an ABAC/governance manipulation primitive

**S1 — Forced `Resource:"*"` makes the tagging prereq a tag-write-anywhere primitive.**
**Claim:** Because the User Guide forces `ec2:CreateTags` on `Resource:"*"` (and the broader prereq policy adds it unconditioned), a holder of the Spot-Fleet "tagging" prerequisite can **create, overwrite, or (if `DeleteTags` is also present) remove tags on any taggable EC2 resource in the account**. Where the account uses tag-based access control, this is a privilege/governance primitive independent of Spot Fleet: (i) **ABAC self-widen** — set `aws:ResourceTag/<k>` on a target instance/volume/SG so a separate `aws:ResourceTag`-conditioned Allow now grants the holder access; (ii) **owner-tag spoof** — the AWS example `#iam-example-taggingresources` keys on `aws:ResourceTag/owner: ${aws:username}`, so a holder can stamp `owner=<self>` on a foreign resource to satisfy an owner-scoped policy; (iii) **protective-tag strip** — `DeleteTags` to remove a tag an SCP/`Deny`/backup/cost-allocation/`aws:ResourceTag`-Deny relies on. None of these touch Spot Fleet at all; the fleet docs are merely what provisioned the over-broad `CreateTags`.
**Mechanism:** `tag-spot-fleet` "you must specify `"*"`"; `spot-fleet-prerequisites` user policy (`ec2:CreateTags` on `*`, no condition); `ExamplePolicies_EC2 #iam-example-taggingresources` shows the exact `aws:ResourceTag/owner:${aws:username}` and `aws:RequestTag` ABAC patterns this bypasses; `list_ec2` confirms `CreateTags`/`DeleteTags` reach ~90 resource types incl. `instance`/`volume`/`security-group`.
**Confirm/Refute oracle:** `iam:SimulatePrincipalPolicy` for `ec2:CreateTags` + `--resource-arns <foreign-instance-ARN>` under a principal holding only the prereq policy → expect `allowed` (no ownership binding). Then, against a **self-owned canary** ABAC policy (`Allow ec2:StartInstances if aws:ResourceTag/team = X`), simulate: tag a canary instance `team=X` with the prereq policy, confirm the ABAC Allow now fires. **Do not** tag resources you do not own. **Severity-if-true:** Medium–High where tags *are* the access-control mechanism (ABAC-gated secret/instance/volume) — intra-account privilege manipulation. **Owner-to-fix:** shared — AWS owns the "must use `*`" guidance (U1); the customer owns the ABAC composition. **Reportable** as AWS-authored guidance that defeats least privilege, per the Lens R/U carve-out.

**S2 — `DescribeTags`/`DescribeSpotFleetRequests` cannot be tag/resource-scoped → tag read is all-or-nothing.**
**Claim:** `ec2:DescribeTags` and `ec2:DescribeSpotFleetRequests` carry **no resource types** (Resource `*` only, condition key `ec2:Region` alone), so a principal granted either reads **every** fleet/resource tag in the account — tags frequently carry sensitive metadata (owner emails, cost centers, environment, data-classification). There is no IAM way to restrict a user to "describe only *my* fleets' tags."
**Mechanism:** `list_ec2` — both actions list no resource types; `tag-spot-fleet` shows `describe-tags`/`describe-spot-fleet-requests` returning full tag sets.
**Confirm/Refute oracle:** `iam:SimulateCustomPolicy` attempting to scope `DescribeTags` to a resource ARN → `implicitDeny`/no effect (confirms unscopable). **Severity-if-true:** Low (intra-account info-exposure / least-privilege gap; account-partitioned, not cross-tenant). **Owner-to-fix:** AWS (action design).

### Lens I — Tagging / ABAC enforcement (tag-provenance; complements, does not restate, sibling I1)

**I1 — Fleet-role tag provenance bypasses the caller's `aws:RequestTag`/`aws:TagKeys` restrictions (forbidden-key *injection* onto instances/volumes).**
**Claim:** The siblings' I1 covers *under*-tagging (fleet launches instances **untagged** → they escape an ABAC Allow). This is the **inverse and arguably stronger** direction: because fleet-launched **instance/volume** tags are applied by the **assumed fleet role** (whose own `CreateTags` is unconditioned on `*`), a caller who is explicitly **denied** a tag key by their *own* policy (`aws:TagKeys` deny-list, or `aws:RequestTag/<k>` value constraint) can still cause those instances to be born carrying that forbidden key/value — by putting it in `LaunchSpecifications.TagSpecifications[instance]` or the launch template. The caller's tag conditions never run on the role's `CreateTags`. If the account's ABAC grants access on `aws:ResourceTag/<k>=<v>`, the caller injects `<k>=<v>` onto fleet instances they then control → access they could not have tagged their way into directly.
**Mechanism:** `tag-spot-fleet` ("Specify the tags for the instances in `LaunchSpecifications` … `ResourceType: instance`"); `spot-fleet-prerequisites` ("the `IamFleetRole`'s … `CreateTags` permission … inconsistent tagging behavior … we are working to fix this inconsistency") confirms the role, not the user, is the tagging identity; `Using_Tags` ABAC-from-tags framing; `ExamplePolicies_EC2` "Surprise inconsistency" precedent that Spot-family tag evaluation is irregular. The docs are **silent** on whether the caller's `aws:RequestTag`/`aws:TagKeys` context propagates into the role's `CreateTags` — the hypothesis is that it does not.
**Confirm/Refute oracle:** docs cannot settle propagation — this is the plan's primary **live** lead. Canary setup: principal P with `Deny ec2:CreateTags if aws:TagKeys contains "secret-access"` (or a value constraint) **and** `Allow ec2:RequestSpotFleet`+`PassRole`. P submits a fleet whose `LaunchSpecifications.TagSpecifications[instance]` sets `secret-access=true`. Oracle: `describe-instances`/`describe-tags` on the launched instance → if the tag **is present**, P bypassed its own restriction via the role (bug); if the request is rejected or the tag omitted, the restriction propagated (null). Pair with an `aws:ResourceTag/secret-access`-gated canary Allow to show end-to-end access gain. Tear down the fleet + instances.
**Preconditions / Cost:** canary account; one fleet launch (minimal `TargetCapacity`, immediate cancel-with-terminate). **Severity-if-true:** Medium–High where ABAC on launched instances is the access-control mechanism (caller escapes their own tag governance). **Owner-to-fix:** AWS (acknowledged tagging inconsistency). **Stop:** confirm tag presence; do not use any access the injected tag unlocks beyond proving the Allow fires.

**I2 — Reserved `aws:ec2spot:fleet-request-id` tag write boundary (gates sibling TerminateInstances primitive).**
**Claim:** The siblings' SLR `TerminateInstances` is conditioned only on **presence** of the service tag key `aws:ec2spot:fleet-request-id` (prereq-plan R2 / broad-plan S1). That is a cross-fleet-only self-impact **unless** a user can *set* that key on a victim instance — which would turn it into a "mark any instance for the SLR to terminate" primitive. `aws:`-prefixed tags are normally reserved and unsettable via `ec2:CreateTags`, but the forced-`*` `CreateTags` grant (S1) is exactly the capability that would attempt it.
**Mechanism:** reserved-tag namespace rules (`Using_Tags`); the forced-`*` grant (U1/S1); the SLR condition in the sibling plans.
**Confirm/Refute oracle:** `aws ec2 create-tags --resources <canary-instance> --tags Key=aws:ec2spot:fleet-request-id,Value=<some-sfr> --dry-run` under the prereq policy → `UnauthorizedOperation`/validation error (reserved-tag protection holds → the sibling primitive stays cross-fleet-only, Low) vs `DryRunOperation`/accepted (user can set it → victim-instance-termination primitive, Medium–High). **This single read-only-ish probe resolves the open question flagged as doc-gap #3 in `spot-fleet-attack-research-plan.md`.** **Severity-if-true:** Medium–High (feeds a destructive primitive). **Owner-to-fix:** AWS. **Stop:** on `DryRunOperation`, do not proceed to a real tag-set on any instance you do not own.

### Lens L — Tag quantity / value validation (low)

**L1 — Tag key/value limits & brittle `ResourceType` validator.** The page states a wrong `ResourceType` value makes "the fleet request **fail**" (whole-request abort), and volume tagging is silently unsupported in `LaunchSpecifications`. Probe: does an oversized/invalid tag set (50-tag limit, 128/256-char key/value, empty value, unicode/injection in key) produce a clean per-tag error or abort/partially-apply the fleet create (consistency gap)? Does the "fails" path leave a half-created fleet or orphaned instances (overlaps broad-plan O1)?
**Oracle:** read-only / canary `--dry-run request-spot-fleet` with malformed `TagSpecifications`. **Severity:** Low (input-validation / single-tenant resilience, within account). **Owner-to-fix:** AWS.

---

## 5. Recommended Areas of Focus (priority order)

1. **U1 — doc-vs-IAM-reference contradiction** (resource-level perms / forced `*`). Highest yield, mostly read-only (`SimulateCustomPolicy` + one/two `--dry-run`), and it corrects a premise both sibling plans inherited. Resolve which source wins first — it determines whether S1 (over-grant) or U2 (unenforceable governance) is the live impact.
2. **S1 — forced-`*` `CreateTags`/`DeleteTags` as an ABAC/governance-manipulation primitive.** Confirmable read-only with `SimulatePrincipalPolicy`; the account-wide tag-write blast radius is the concrete harm behind U1 branch (a).
3. **I1 — fleet-role tag-provenance bypass (forbidden-key injection).** The primary *live* lead; docs cannot settle propagation. Decisive canary fleet launch; high value where instance-ABAC is the control.
4. **U2 — mandatory-tag-on-create governance fails open** for the legacy fleet API (ties to broad-plan I1 under-tagging). 
5. **I2 — reserved-tag write boundary** — one cheap probe that *also* resolves the siblings' open doc-gap on whether their `TerminateInstances` lead escalates to victim instances.
6. **Lower:** S2 unscopable tag-read, L1 tag-validation / brittle `ResourceType`.

**Kill-chain to compose:** U1(b)/U2 (mandatory-tag Deny inert on `RequestSpotFleet`) → fleet created untagged **or** I1 (inject a forbidden `aws:ResourceTag` key via `LaunchSpecifications`, applied by the unconditioned fleet role) → account ABAC on `aws:ResourceTag/<k>` now grants the attacker-controlled instance access it was never meant to have → (if that access is itself a privileged role via the siblings' PassRole leads) escalate. Rate at the **end** of the chain. Hand the PassRole/privesc tail to `spot-fleet-prerequisites-attack-research-plan.md` (P1/B1) rather than re-deriving it here.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Scoped `spot-fleet-request` policy rejected (or inert) at runtime | `RequestSpotFleet`/`CreateTags` authz | UG: "must use `Resource:"*"`" vs IAM-ref: formal resource type + required marker (contradiction = the bug) |
| Account-wide tag write/overwrite/strip via forced-`*` grant | caller `ec2:CreateTags`/`DeleteTags` on `*` | None — UG forces `*`; no ownership condition on the taught policy |
| ABAC self-widen / owner-tag spoof | `aws:ResourceTag`/`${aws:username}` ABAC + forced-`*` CreateTags | ABAC Allow assumed the holder can't set the tag — forced-`*` breaks that assumption |
| Mandatory-tag-on-create Deny fails open | `RequestSpotFleet` tag evaluation | `Using_Tags` "created with tags or not at all" (promise) vs Spot "Surprise inconsistency" (reality) |
| Forbidden tag key injected onto fleet instances via role | `LaunchSpecifications.TagSpecifications` + fleet role `CreateTags` | Caller's `aws:TagKeys`/`aws:RequestTag` conditions — do NOT run on the role's call (hypothesis) |
| Set reserved `aws:ec2spot:fleet-request-id` on a victim instance | forced-`*` `CreateTags` + reserved-tag namespace | AWS reserved-`aws:`-prefix tag protection (test it holds) |
| Read all fleet/resource tags in account | `DescribeTags`/`DescribeSpotFleetRequests` | None — unscopable (Resource `*` only) |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-tenant / cross-account tag access** — Spot Fleet is single-account; `DescribeTags`/`CreateTags` are account-partitioned like all EC2. No multi-tenant tag store. (The one cross-account angle, confused-deputy `IamFleetRole`, belongs to the prereq plan's B1, not the tag model.)
- **`sfr-` enumeration** — IDs are ~122-bit UUID-class; not guessable (see broad plan A1). Tag reads still require account-local auth.
- **AWS's own service plane** — `spotfleet.amazonaws.com` + the SLRs are the shared-responsibility hard stop.
- **Customer-authored ABAC/tag policies** — a weak tag policy the customer wrote is their footgun. In scope here only because the **over-grant is taught by an AWS-published sample policy** the customer copies verbatim (U1/S1), and the tagging inconsistency is an **AWS-acknowledged bug** (I1).
- **IMDS / UserData on the launched instances** — the instances are the customer's own; relevant only when chained to a privileged role via the sibling PassRole leads.
- **The `TerminateInstances`/`RegisterTargets`/PassRole artifact audit** — owned by `spot-fleet-prerequisites-attack-research-plan.md`; this plan only contributes the I2 reserved-tag probe that gates its severity.

---

## 8. Null hypotheses / doc gaps (pages named)

- **Lens A (cross-tenant IDOR):** null for the tag surface — all tag APIs account-partitioned; `sfr-` non-enumerable. (Pages: `tag-spot-fleet`, `list_ec2` `DescribeTags`/`DescribeSpotFleetRequests` rows.)
- **Lens G (SSRF):** null — no tag field is a URL/host the service dereferences; tag keys/values are opaque strings. (Pages: `tag-spot-fleet`, `Using_Tags`.)
- **Lens Q (upload):** null — no file/blob upload on the tag path; `TagSpecifications` carries only key/value strings. (Pages: `tag-spot-fleet`, `create-spot-fleet`.)
- **Lens B / C / H / E / R-artifact-audit / auto-scaling-L / O:** **do fire for Spot Fleet but are owned by the two sibling plans** — cross-referenced, not restated (confused-deputy `IamFleetRole`, KMS grant, SLR/tagging-role `TerminateInstances`/`RegisterTargets`, privesc chain, orphaned-instance persistence). Pages: `spot-fleet-prerequisites`, the Batch `spot-fleet-roles-*` runbooks — audited in `spot-fleet-prerequisites-attack-research-plan.md`.
- **Lens K / P / F / D / V / M / N / W / Y / AA / BB / CC / DD / EE / FF:** no triggers on the tagging surface (no LLM/agent, no onboarding/OTP, no protocol translator, no network/ENI boundary, no bearer token, no namespace migration, no attestation, no customer-facing TLS endpoint, no share/revoke beyond the KMS grant in the siblings, no multi-parser request path, no upstream-asserted-identity header, no caching layer, no predictable-global-namespace resolution, no JWT/OIDC). Pages checked: `tag-spot-fleet`, `Using_Tags`, `ExamplePolicies_EC2`, `create-spot-fleet`, `work-with-spot-fleets`.

**Doc gaps requiring live/API confirmation (not resolvable from documentation):**
1. **(U1)** Does the `RequestSpotFleet`/`CreateTags` *runtime* accept a `spot-fleet-request`-scoped policy (IAM-ref) or reject it (User Guide)? → one `--dry-run` each.
2. **(U2)** Does a `RequestSpotFleet` with **no** `TagSpecifications` bypass an `aws:RequestTag`-conditioned Deny (Spot "Surprise inconsistency" generalizing to fleets)?
3. **(I1)** Do a caller's `aws:TagKeys`/`aws:RequestTag` conditions propagate into the fleet role's `CreateTags` on launched instances/volumes, or not? → canary fleet launch.
4. **(I2)** Can `ec2:CreateTags` set the reserved `aws:ec2spot:fleet-request-id` key on an arbitrary instance? → one `--dry-run` (also resolves sibling doc-gap #3).
5. Whether a malformed/oversized `TagSpecifications` aborts the whole fleet create vs per-tag error, and whether the abort orphans resources (L1; overlaps broad-plan O1).

---
*End of plan. Documentation-derived hypotheses only; nothing herein has been executed against a live AWS account. Companion to `spot-fleet-attack-research-plan.md` and `spot-fleet-prerequisites-attack-research-plan.md` — read those for the PassRole/confused-deputy/IAM-artifact depth this plan deliberately does not duplicate.*
