# Identity-based policies for Amazon EC2 — Attack / Research Plan

**Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html`
**Offline mirror:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md` (22073 bytes)
**Authoritative action/key reference:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (NOT `list_amazonec2` — that slug 404s; see note §7)
**Date:** 2026-10-15
**Skill:** security-questionbuilder (boundary-first research-plan generator)
**Drift check:** live `.md` fetch byte-identical to offline mirror for this page (both subagents independently confirmed). No online/offline drift.

---

## §0 — Scope & relationship to existing plans (READ FIRST)

This page is the **canonical reference for EC2 IAM condition-key *evaluation semantics*** — not a feature API. It has no mutating API surface of its own; it teaches *how* conditions resolve, fail open, and bind to resources. This plan is therefore a **mechanism-level COMPLEMENT**, not a duplicate, of the cluster hub:

> **`/work/aws-docs/ec2-security-iam-attack-research-plan.md`** (the `security-iam` cluster HUB) already covers this page at summary level:
> - **S1** — `ec2:ResourceID` fail-open (summarized there; this plan OWNS the full mechanism + 14-pair list — see §5 Area 1)
> - **S2** — `ec2:Attribute` LaunchPermission exclusion (this plan OWNS the case-sensitivity *value* fail-open extension — Area 4)
> - **C1** — Describe* needs a separate statement (cross-ref only; Area 6)
> - **C4 / S3 / #6** — ABAC tag self-widen, prose-only, no enforcing JSON (cross-ref; Area 6 + the tagging-child finding)
> - **#2** — AmazonEC2FullAccess → ModifyInstanceAttribute userData → IMDS cred theft (Critical) — lives in hub, NOT restated here
> - **F8** — ModifyInstanceMetadataOptions "no conditions" doc defect = FALSE (lives in hub)

**Rule for the downstream hunter:** do not re-file S1/S2/C1/C4/#2/F8 as new. This plan supplies the *evaluation-semantics depth* those hub entries point at, plus **two net-new findings** the hub does not contain (Area 3 `AssociateSecurityGroupVpc` unscopability; Area 4 `ec2:Attribute` value case-sensitivity fail-open). Trust `list_ec2.md` over User-Guide prose wherever they disagree.

**Boundary posture:** 100% documentation analysis. Every oracle below is **`iam:SimulateCustomPolicy`** — a non-mutating IAM API that honors EC2's documented resolve-to-`*` and `IfExists` logic. No EC2 service-plane action is required to confirm any lead. **HARD STOP** rule unchanged: if any confirmation path touches AWS's own service plane, stop and flag.

---

## §1 — Components, Assets, and Design

- **Customer-facing interface:** IAM policy JSON authored by customers and attached to EC2 principals. The "mechanism" is the IAM policy evaluation engine as *specialized for EC2 condition keys*.
- **Asset under protection:** the *intended* authorization boundary a customer believes their condition expresses (e.g., "only this VPC", "only this AMI", "only non-public images"). The vulnerability class on this page is **the gap between what a policy reads like and what it actually enforces** — a false-sense-of-restriction class, not a direct data breach.
- **Resource identifier shapes referenced:** `ec2:{Resource}ID` keys (ImageID, InstanceID, SnapshotID, VolumeID, VpcID, …), VPC ARNs, SG ARNs, instance ARNs (`ec2:SourceInstanceARN`), AMI attributes.
- **Identity provenance key:** `ec2:SourceInstanceARN` — injected by STS at role-session creation when the session originates on an EC2 instance (trusted-upstream context, Lens CC).
- **Transforms / seams:** none in the data sense; the "transform" is **policy text → IAM decision**, and every documented quirk in that transform is a seam where the author's intent and the engine's behavior diverge.

**Pinned citations (offline line numbers):**
- L155 — "Condition keys are not case-sensitive" (applies to the *key name only*)
- L196 — `...IfExists` Important note (fail-open semantics)
- L208 — `ec2:Attribute` supports only primitive/single-Value AttributeValue; **cannot** be used with the LaunchPermission object of ModifyImageAttribute
- L270 — `ec2:{Resource}ID`: non-`*` value "always resolves to `*` during runtime"
- L298–311 — the full 14-pair recommended-avoid key/action list
- L338 — `ec2:SourceInstanceARN` = ARN of the originating instance
- L355 — ABAC tag-circumvention warning (must explicitly Deny tag add/remove)
- L378 — DryRun → `DryRunOperation` vs `UnauthorizedOperation`
- L385 — `DecodeAuthorizationMessage`

---

## §2 — Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller holding an under-scoped Allow | A resource the author believed was pinned by `ec2:{Resource}ID` | Create-action where the key silently resolves to `*` | `SimulateCustomPolicy` returns `allowed` for *any* ID, not just the typed one |
| Caller | A resource an author tried to **block** via `Deny ec2:{Resource}ID = x` | Deny condition resolves to `*` → never matches literal → never fires | Deny proven inert: same decision for pinned vs different ID |
| Caller re-homing a security group | A **destination** VPC outside the approved set | `AssociateSecurityGroupVpc` — `ec2:Vpc` binds to SG's *home* VPC, not destination; `vpc*` resource carries only `ec2:VpcID`/`ec2:Tenancy` | Deny keyed on `ec2:Vpc` allows association into any destination VPC |
| Policy author | The resource dimension that mattered | `StringEqualsIfExists` + a multi-resource action where the key is absent on one resource → condition true | `allowed` for a disallowed resource while policy "reads as" scoped |
| Caller sharing an AMI public | `LaunchPermission` object (Add/Remove/Group=all) | `ec2:Attribute` can't gate multi-property objects | Only `ec2:Public`/`ec2:Owner`/Resource-ARN can gate; attribute-value condition is a no-op on the sharing call |
| Any principal | Account-wide read (Describe*) | Describe* actions carry no resource/ownership-scoping keys | account-wide enumeration confirmed unscopable |
| EC2 instance role session | A policy keyed on `ec2:SourceInstanceARN` | STS-injected, non-spoofable at IAM layer | **No IAM-layer breach**; real boundary is IMDS/SSRF hardening (out of doc scope) |

---

## §3 — Interface surface (semantics, not APIs)

This page documents **condition-key behaviors**, each of which is a question generator:

| Mechanism | Doc line | Mutating? | Failure class | Routed to |
|---|---|---|---|---|
| `ec2:{Resource}ID` resolve-to-`*` | L270, L298–311 | n/a (policy) | silent no-op / Deny-inert fail-open | Area 1 |
| `...IfExists` key-absent → true | L196 | n/a | fail-open on multi-resource actions | Area 2 |
| `ec2:Vpc` binds to SG home VPC | L161–181 | n/a | wrong-resource binding | Area 3 |
| `AssociateSecurityGroupVpc` key set | list_ec2 L4795–4799 | mutating | **unscopable destination VPC** (net-new) | Area 3 |
| `ec2:Attribute` LaunchPermission exclusion | L208 | n/a | ungateable high-impact object | Area 4 |
| key-name vs **value** case-sensitivity | L155 | n/a | **value fail-open** (net-new) | Area 4 |
| `ec2:SourceInstanceARN` provenance | L338 | n/a | sound (Informational) | Area 5 |
| Describe* unscopable | — | non-mutating | account-wide read | Area 6 |
| DryRun not an ownership oracle | L378 | non-mutating | trap (not an oracle) | Area 6 |
| `DecodeAuthorizationMessage` | L385 | non-mutating | info disclosure | Area 6 |
| ABAC self-widen (`ec2:CreateAction`/`aws:RequestTag`/`aws:TagKeys`) | L355 + tagging child | mutating | tag-based privilege self-widen | Area 6 |

---

## §4 — NEW / changed surface to concentrate fire

Two findings are **net-new** (not in the hub) and should be filed first:

1. **Area 3** — `AssociateSecurityGroupVpc` / `DisassociateSecurityGroupVpc` destination VPC is unscopable by the page's own `ec2:Vpc` teaching pattern. Confirmed in `list_ec2.md` L4795–4799: `ec2:Vpc` sits only on the `security-group*` resource; the `vpc*` resource carries only `ec2:VpcID`/`ec2:Tenancy`. The flagship example (L161–181) teaches a control that silently fails to bound the destination.
2. **Area 4** — `ec2:Attribute` *value* case-sensitivity fail-open. L155 disclaims only the *key name*; `StringEquals` on the *value* is case-sensitive (vs `StringEqualsIgnoreCase`), and the API populates the value PascalCase (`Description`, `ImdsSupport`). A lowercase Deny silently never matches.

---

## §5 — Boundary-lens findings (the leads)

### Area 1 — `ec2:{Resource}ID` silent resolve-to-wildcard  [Lens S / U — HIGH on Deny lists]
**Claim:** A policy that pins a create-action to a specific resource ID via `ec2:ImageID`/`InstanceID`/`SnapshotID`/`VolumeID`/… does **not** restrict to that ID; it silently authorizes *any* ID. On the Deny side the intended block never fires (fail-open).
**Mechanism (doc):** L270 — "If you specify a different value, the condition always resolves to `*` during runtime." Full 14 key/action pairs, L298–311 (verbatim from subagent): `ec2:DhcpOptionsID`→CreateDhcpOptions; `ec2:ImageID`→CopyImage/CreateImage/ImportImage/RegisterImage; `ec2:InstanceID`→RunInstances/ImportInstance; `ec2:InternetGatewayID`→CreateInternetGateway; `ec2:NetworkAclID`→CreateNetworkAcl; `ec2:NetworkInterfaceID`→CreateNetworkInterface; `ec2:PlacementGroupName`→CreatePlacementGroup; `ec2:RouteTableID`→CreateRouteTable; `ec2:SecurityGroupID`→CreateSecurityGroup; `ec2:SnapshotID`→CopySnapshot/CreateSnapshot/CreateSnapshots/ImportSnapshots; `ec2:SubnetID`→CreateSubnet; `ec2:VolumeID`→CreateVolume/ImportVolume; `ec2:VpcID`→CreateVpc; `ec2:VpcPeeringConnectionID`→CreateVpcPeeringConnection.
**Key subtlety:** these keys name the resource *being created*, not a source input — so pinning a literal is semantically meaningless and the engine degrades it to `*`. They are **not deprecated** (list_ec2 still lists them, e.g. `image` resource type keys L4849/4951, CreateImage/RegisterImage L4992/L5144) — they are *inert for these specific create pairings*. A trap, not a removed feature.
**Confirm/Refute oracle:** `iam:SimulateCustomPolicy` with the target Allow/Deny statement, `ActionNames: ["ec2:CopyImage"]`, `ec2:ImageID` omitted from `ContextEntries`, against (i) requested image = pinned id, (ii) requested image = a different id. Identical decisions ⇒ condition proven inert. A real discriminating control shows (ii) denied/not-allowed.
**Severity:** Medium-High for over-scoped Allow (false sense of pinning); **High** for Deny block-lists (intended block silently never applies; true blast radius = any ID). Cross-ref hub **S1**.

### Area 2 — `...IfExists` documented fail-open  [Lens S / U — HIGH when stacked with Area 3]
**Claim:** On a multi-resource action, `StringEqualsIfExists` on a key that is absent for one of the resources makes the condition evaluate **true** for that resource — the scoping silently never applies to the dimension that mattered, while the policy reads as scoped.
**Mechanism (doc):** L196 Important note — without `IfExists` the condition "fails for the resources to which the condition key does not apply"; AWS instructs authors to add `IfExists` to avoid that. Authoritative semantics `reference_policies_elements_condition_operators.md` L529: "If the key is not present, evaluate the condition element as true."
**Breach scenario (stacks with Area 3):** `Allow ["ec2:AuthorizeSecurityGroupIngress","ec2:AssociateSecurityGroupVpc"]`, `Resource:*`, `Condition: StringEqualsIfExists {"ec2:Vpc":"<approved-vpc>"}`. For the `vpc*` resource of `AssociateSecurityGroupVpc`, `ec2:Vpc` is absent → true unconditionally → destination-VPC scoping is a no-op.
**Oracle:** `SimulateCustomPolicy` on the combined action set, `ResourceArns` = disallowed-VPC arn + SG arn, supply `ec2:Vpc` only in the SG context; an `allowed` decision for the disallowed VPC confirms fail-open.
**Severity:** Medium standalone; High stacked with Area 3 (silent, review-invisible control bypass).

### Area 3 — `ec2:Vpc` wrong-binding + `AssociateSecurityGroupVpc` unscopable destination  [Lens S / U — NET-NEW, Medium-High]
**Claim:** The page's flagship `ec2:Vpc` example (scope SG-rule changes to one VPC) does **not** extend to the SG-relocation action: a security group that currently lives in the approved VPC can be re-homed into *any* destination VPC the caller can reach, without violating a `Deny` keyed on `ec2:Vpc`.
**Mechanism (doc + reference):** Flagship example L161–181 (`ec2:Vpc` on Authorize/Revoke SG ingress/egress, `security-group/*`). In `list_ec2.md`: Authorize/Revoke carry `ec2:Vpc` only on `security-group*` (L4888–4898, L9573–9583). `AssociateSecurityGroupVpc` (L4795–4799) is **two-resource**: `security-group*` → `ec2:SecurityGroupID`,`ec2:Vpc` (L4797); `vpc*` → `ec2:Tenancy`,`ec2:VpcID` **not** `ec2:Vpc` (L4798). `ec2:Vpc` therefore only ever resolves to the SG's *home* VPC, never the destination. Blocking the destination requires `ec2:VpcID` on the `vpc*` resource — a different key the page never teaches.
**Oracle:** `SimulateCustomPolicy`, `ActionNames:["ec2:AssociateSecurityGroupVpc"]`, `ResourceArns`=[SG arn, target-VPC arn], two `ContextEntries` sets: (a) `ec2:Vpc`=SG home VPC (matches), target VPC arbitrary; (b) same but target VPC = disallowed. Both `allowed` ⇒ Deny inert w.r.t. destination.
**Severity:** Medium-High — defense-in-depth bypass enabling lateral SG movement across VPC trust boundaries without tripping the written condition. **NET-NEW — not in hub.** (Also test `DisassociateSecurityGroupVpc` for the symmetric gap.)

### Area 4 — `ec2:Attribute` LaunchPermission exclusion + value case-sensitivity fail-open  [Lens S / U — Medium; value fail-open NET-NEW]
**Claim A (hub S2, depth here):** `ec2:Attribute` cannot gate the `LaunchPermission` object of `ModifyImageAttribute` (public-AMI sharing), because it only supports primitive / single-`Value` AttributeValue objects. The realistic levers are Resource-ARN scoping + **`ec2:Public`/`ec2:Owner`** (confirmed present on `ModifyImageAttribute`, list_ec2 L8800–8803: `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:ImageID`, `ec2:ImageType`, `ec2:Owner`, `ec2:Public`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:RootDeviceType`).
**Claim B (NET-NEW):** L155 disclaims case-sensitivity for the *key name only*. The page's own Deny example (L247–263) uses `StringEquals {"ec2:Attribute":"Description"}` — `StringEquals` is **value-case-sensitive**. An author who writes `"description"` (lowercase), assuming key insensitivity extends to values, gets a Deny that silently never matches the API-populated PascalCase value (`Description`, `ImdsSupport` per L208) → fail-open.
**Oracle:** `SimulateCustomPolicy` with the L247–263 Deny unmodified, `ec2:Attribute="Description"` vs `="description"`. `allowed` for lowercase + `denied` for exact-case ⇒ value-case fail-open proven non-mutatingly.
**Severity:** Medium (single-key, easy to fix once known; but LaunchPermission ungateability is a real coverage gap for accidental AMI public-sharing). Cross-ref hub **S2**.

### Area 5 — `ec2:SourceInstanceARN` trust model  [Lens CC — Informational / null]
**Determination:** **Sound at the IAM layer — not caller-asserted.** `reference_policies_condition-keys.md` L836: injected "whenever the role session is created by an Amazon EC2 instance" (STS/IAM provenance, grouped with `aws:SourceIdentity`/`aws:PrincipalArn`). An attacker cannot set an arbitrary value in-request. **Caveat:** it only identifies which instance's session signed the request — it does **not** detect credential theft; stolen Instance-B IMDS creds correctly carry Instance B's real ARN. The real boundary is IMDS/SSRF hardening, which is **out of documentation scope** and a separate non-doc finding.
**Oracle:** cannot be force-injected via `ContextEntries` by an outside caller in production — spoofability is refuted at the policy layer. Any attempt to override it to a foreign ARN only reflects the actual session value.
**Severity:** Informational (confirms key is sound). Flag only if paired with an IMDS-exfil primitive (hunter follow-up, not this plan).

### Area 6 — Account-wide read, DryRun trap, info disclosure, ABAC self-widen  [Lens A / U / I — cross-ref hub]
- **Describe\* unscopable** (account-wide read theme): Describe actions carry no resource/ownership-scoping condition keys — enumeration is account-wide by design. Cross-ref hub **C1** (Describe needs its own statement).
- **DryRun is NOT an ownership oracle** (L378): a `DryRunOperation` response proves *permission*, not *resource existence/ownership* — do not treat distinct DryRun responses as an IDOR oracle. (Trap flagged so the hunter doesn't mis-file it.)
- **`DecodeAuthorizationMessage`** (L385): decodes the encoded authorization-failure message → reveals policy/context detail; minor info-disclosure lever, note only.
- **ABAC tag self-widen** (L355 + child page): see below. Cross-ref hub **C4/#6**.

### Area 6b — `supported-iam-actions-tagging.md` child — NOT a thin page  [Lens I — Medium composability]
Child: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/supported-iam-actions-tagging.md` (109 lines). Real semantics, keep in active set:
- **`ec2:CreateAction`** (L12/34/62) gates which create-action's embedded `ec2:CreateTags` sub-check applies; **`aws:RequestTag`** (L80–90) enforces specific request tags; **`aws:TagKeys`** (L91–101, `ForAllValues`/`ForAnyValue`).
- `ec2:CreateTags` is only separately authz-checked **when tags are present** in the create request / launch template (L70/72) — no tags supplied ⇒ `CreateTags` permission never consulted.
- **No bypass of a standalone `CreateTags` Deny** via RunInstances-embedded tagging (embedded spec still triggers the same check, L10/72) — a blanket Deny still fires. **The real hazard is the inverse:** an Allow scoped only by `ec2:CreateAction=RunInstances` with no `aws:RequestTag`/`aws:TagKeys` lets a user apply **arbitrary tag keys/values at launch** — including ABAC keys (`aws:ResourceTag/environment=production`, main page L345–348) — enabling tag-based privilege/ABAC-bypass self-widen (create → self-tag to match an ABAC Allow). Main page L355 explicitly warns operators to Deny tag add/remove on ABAC resources "otherwise … a user to circumvent your restrictions."
- Case-sensitivity note (child L107) mirrors Area 4: "the condition key is not case-sensitive and the condition value is case-sensitive" — recommends `aws:TagKeys` over case folding.
**Oracle:** `SimulateCustomPolicy` with `RunInstances` + conditional `CreateTags` (child L17–40), `ContextEntries` supplying `aws:RequestTag/environment=production` at launch with no `aws:RequestTag` restriction → `allowed` demonstrates the self-widen is live absent `aws:RequestTag`/`aws:TagKeys`.
**Severity:** Medium (composability hazard — needs a second ABAC-gated resource policy; doc flags the mitigation). Doc-gap verdict: **not thin**, keep in active analysis.

---

## §6 — Prioritized lead ranking

| # | Lead | Lens | Severity | New? | Oracle |
|---|---|---|---|---|---|
| 1 | `ec2:{Resource}ID` Deny block-list silently inert (fail-open) | S/U | **High** | hub S1 (depth here) | SimulateCustomPolicy, two IDs |
| 2 | `AssociateSecurityGroupVpc` destination VPC unscopable | S/U | Med-High | **NET-NEW** | SimulateCustomPolicy, 2 context sets |
| 3 | `IfExists` fail-open stacked on multi-resource action | S/U | High (stacked) | hub-adjacent | SimulateCustomPolicy combined set |
| 4 | `ec2:Attribute` value case-sensitivity fail-open | S/U | Medium | **NET-NEW** | SimulateCustomPolicy, case variants |
| 5 | `ec2:Attribute` LaunchPermission ungateable (use ec2:Public) | S/U | Medium | hub S2 (depth) | key-set confirmed in list_ec2 |
| 6 | ABAC tag self-widen via unconstrained CreateTags-at-launch | I | Medium | hub C4 (depth) | SimulateCustomPolicy w/ RequestTag |
| 7 | Describe* account-wide / DryRun-not-oracle / DecodeAuthMessage | A/U | Low-Info | hub C1 | n/a (doc) |
| 8 | `ec2:SourceInstanceARN` sound at IAM layer | CC | Info/null | — | refuted (not spoofable) |

---

## §7 — Null hypotheses, traps, and notes

- **DryRun is not an IDOR oracle** (L378) — permission signal only; do not enumerate resources with it.
- **`ec2:SourceInstanceARN` spoofing — REFUTED** at the IAM layer (STS-injected provenance, Area 5). Only relevant chained with an IMDS/SSRF exfil primitive (non-doc).
- **Reference-URL trap:** the live page still links `ec2:` keys to `.../list_amazonec2.html`, which 404s / redirects to a JS shell. Use **`list_ec2.md`** — the only working authoritative reference. (Memory: [[reference-aws-iam-service-auth-ref-url]].)
- **Trust order:** where User-Guide prose and `list_ec2.md` disagree, trust `list_ec2.md` (it is the authoritative action→resource→condition-key table).
- No cross-tenant / cross-account breach is directly expressible from this page alone — the class here is **false-sense-of-restriction within an account** (Lens U), which becomes cross-boundary only when the mis-scoped action (SG re-homing, AMI public-share, ABAC self-widen) is itself cross-boundary.

---

## §8 — Handoff for the next agent

- **Everything here is confirmable non-mutatingly** via `iam:SimulateCustomPolicy`. No EC2 mutating call is needed. HARD STOP still applies if any path reaches AWS's own service plane.
- **File leads #2 and #4 as net-new** (not in the hub). Leads #1/#5/#6/#7 are depth for existing hub entries S1/S2/C4/C1 — attach, don't duplicate.
- **Still unread in this cluster** (doc-gap, lower priority): `ExamplePolicies_EC2.md` (62594 b — likely more insecure-sample JSON, Lens R), `security-iam-awsmanpol.md` (15811 b — AWS-managed-policy audit, Lens R, overlaps hub #2). The tagging child (`supported-iam-actions-tagging.md`) is now READ and folded in (Area 6b).
- **Hub to update:** consider back-linking `ec2-security-iam-attack-research-plan.md` S1/S2 to this plan for the full mechanism + 14-pair list.
