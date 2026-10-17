# Lens S/R audit — instance-type/hardware gating condition keys (EC2)

Scope: static documentation analysis only. No live AWS account touched. All citations
are to the offline mirror under /work/aws-docs/docs/ (cross-checked where noted) and
the EC2 Service Authorization Reference at
/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md (NOT
list_amazonec2 — mirror renames it).

================================================================================
## 1. Condition-key inventory relevant to instance-type/hardware gating
================================================================================

Source: list_ec2.md "## Condition keys for Amazon EC2" table (lines ~10036-10190),
cross-referenced against the per-action resource/condition-key rows for RunInstances
(line 9585-9609) and ModifyInstanceAttribute (line 8806-8811).

| Key | Type | Bound resource type(s) on RunInstances | Notes |
|---|---|---|---|
| `ec2:InstanceType` | String | `instance*` only | THE primary type-gating key. Not present on `image*`, `launch-template`, `network-interface*`, `subnet*`, `security-group*`, `key-pair`, `elastic-gpu`, `volume`, `snapshot` resource rows for the same action. |
| `ec2:Tenancy` | String (`default\|dedicated\|host`) | `instance*` | Hardware-isolation gate, same binding pattern as InstanceType. |
| `ec2:RootDeviceType` | String (`ebs\|instance-store`) | `instance*`, `image*` | |
| `ec2:PlacementGroup` | ARN | `instance*`, `placement-group` | |
| `ec2:InstanceAutoRecovery` | String | `instance*` | "whether the instance type supports auto recovery" — a per-type hardware capability, not independently settable by caller. |
| `ec2:InstanceBandwidthWeighting` | String | `instance*` | |
| `ec2:CpuOptionsAmdSevSnp` | String | `instance*` | SEV-SNP (confidential-compute hardware feature). |
| `ec2:EbsOptimized` | Bool | `instance*` | |
| `ec2:InstanceMarketType` | String | `instance*` | capacity-block / on-demand / spot. |
| `ec2:InstanceMetadataTags`, `ec2:MetadataHttpEndpoint`, `ec2:MetadataHttpPutResponseHopLimit`, `ec2:MetadataHttpTokens` | String/Numeric | `instance*` | IMDS posture keys; some instance families/features (NitroTPM, enclaves) interact with these but there is no family-scoped IMDS key. |
| `ec2:IsLaunchTemplateResource` | Bool | nearly every resource type in the RunInstances row-set, **including `instance*`** | "whether users are able to override resources that are specified in the launch template." Governs override, not the type value itself. |
| `ec2:LaunchTemplate` | ARN | nearly every resource type incl. `instance*`, `launch-template` | |
| `ec2:Owner`, `ec2:Public`, `ec2:ImageID`, `ec2:ImageType` | String/Bool | `image*` only | AMI-side gates; irrelevant to instance family but often conflated with it in sample policies (see Lens R §3). |
| `ec2:Region`, `ec2:AvailabilityZone[Id]` | String | nearly all resource rows | |
| `ec2:ManagedResourceOperator` | String | `instance*`, `launch-template`, `network-interface*`, `volume` | |

`ModifyInstanceAttribute` (line 8806) binds the identical key-set
(`ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:InstanceType`, `ec2:Tenancy`,
`ec2:RootDeviceType`, `ec2:PlacementGroup`, etc.) to its own `instance*` resource row —
structurally independent from the RunInstances row. A policy author must duplicate the
`ec2:InstanceType` condition on *both* actions; nothing in the docs cross-links them.

**Doc-confirmed absence** (checked by grepping the full list_ec2.md condition-key table,
line 10036-10190, and the whole file for case-insensitive hits):
- No `ec2:InterfaceType` key exists anywhere in list_ec2.md (0 hits). This is the
  already-confirmed corpus exemplar for failure shape (a); verified against the current
  mirror.
- No condition key for "Nitro version", "bare metal", "processor type"/"Graviton vs
  Intel vs AMD", or "accelerator type/count" exists. The only accelerator-adjacent key is
  `ec2:ElasticGpuType` (legacy Elastic Graphics, not Inferentia/Trainium/GPU instance
  families). `ec2:EnclaveOptions` is **not** a condition key — "enclave" only appears in
  action names (`AssociateEnclaveCertificateIamRole`, `DisassociateEnclaveCertificateIamRole`,
  `GetAssociatedEnclaveCertificateIamRoles`) and in the `ec2:Attribute` *valid-value* enum
  (`enclaveOptions`, see §2 below) — there is no standalone `ec2:AttributeEnclaveOptions`
  or similar key to Deny-gate enclave-capable families directly.

================================================================================
## 2. Known failure-shape audit
================================================================================

### (a) Nonexistent / silently-ignored key — CONFIRMED GENERALIZES

Mechanism: IAM does not reject unknown condition-key names at policy-validation time for
most operators; if the key is simply absent from the request context, operators like
`StringEquals`/`StringLike` evaluate to `false`, so a `Deny` keyed on a nonexistent key
never fires. list_ec2.md's condition-key table (§1) is the authoritative "does this key
exist" oracle.

- Confirmed exemplar re-verified: `ec2:InterfaceType` — 0 hits in list_ec2.md.
- New instance-type-adjacent cases a policy author could plausibly invent and get
  silently ignored, because none of these strings appear in list_ec2.md's key table:
  `ec2:BareMetal`, `ec2:Processor`, `ec2:NitroVersion`, `ec2:AcceleratorType`,
  `ec2:AcceleratorCount`, `ec2:EnclaveOptions`, `ec2:GpuCount`. Any `Deny` written
  against one of these (e.g. to block bare-metal `.metal` sizes or GPU families) is
  inert — the request is never evaluated against it and launch succeeds regardless of
  hardware class.
- Claim: a customer who tries to Deny bare-metal or GPU/accelerator instance families by
  condition key (rather than by `StringLike` on `ec2:InstanceType` itself) has written a
  no-op statement.
- Confirm/refute oracle: `iam-policy-simulator-api:SimulateCustomPolicy` (or
  `aws iam simulate-custom-policy`) with a policy containing
  `"Deny" / "ec2:RunInstances" / Condition: StringEquals {"ec2:BareMetal": "true"}` against
  action `ec2:RunInstances` with context key `ec2:InstanceType=c5.metal` — expect
  simulator to report `allowed` (Deny never matches) wherever an Allow exists elsewhere,
  proving the key is inert. This is a pure policy-syntax test; no live resource is
  created.
- Preconditions: customer must rely on a bespoke/hallucinated key instead of
  `ec2:InstanceType` + `StringLike`. Severity: **Medium** (requires an authoring mistake,
  but the mistake is easy to make precisely because AWS doesn't publish an exhaustive
  "here is every key that does NOT exist" list, and `.metal` sizes feel like they deserve
  their own key).

### (b) Case-sensitivity fail-open — CONFIRMED for `ec2:Attribute`, applies directly to instance-type changes

Mechanism, with exact citation:
`/work/aws-docs/docs/AWSEC2/latest/APIReference/API_ModifyInstanceAttribute.md` line 23:

> Valid Values: `disableApiTermination | instanceType | kernel | ramdisk | ...`

The wire-level `Attribute` parameter enum is **camelCase** (`instanceType`), because it's
the legacy Query-API string enum. But every other place the same concept is documented —
the named structured parameter in the same API doc (line 74, `**InstanceType**`), the SDK
parameter (`InstanceType=` in boto3/CLI), and the IAM doc's own worked example
(`iam-policies-for-amazon-ec2.md` lines 240-263, which only ever shows `ec2:Attribute`
tested against `Description`, never `instanceType`) — renders it **PascalCase**
(`InstanceType`). `StringEquals`/`StringLike` are case-sensitive on values.

- Claim: a policy author who writes
  `"Deny" / "ec2:ModifyInstanceAttribute" / Condition: StringEquals {"ec2:Attribute": "InstanceType"}`
  (the PascalCase form they see in every SDK/CLI reference and in the API doc's own
  parameter heading) produces a Deny that **never matches**, because the actual request
  context value of `ec2:Attribute` is the camelCase enum `instanceType`. The companion
  per-value key `ec2:Attribute/${AttributeName}` has the same exposure if the
  `${AttributeName}` segment is typed in the wrong case.
- Why this is instance-type-relevant specifically: this is the only documented path by
  which an *in-place* instance-type change (as opposed to a fresh `RunInstances`) is
  IAM-gated, and it is also the action an operator would use to implement the
  "self-widen" bypass in (e) below, so a case mistake here is doubly dangerous.
- Confirm/refute oracle: `SimulateCustomPolicy` on action `ec2:ModifyInstanceAttribute`
  with the Deny statement above and context key
  `ec2:Attribute = "instanceType"` (lowercase-first, the real runtime value) plus an
  Allow statement elsewhere granting the action unconditionally — expect simulator to
  return `allowed`, proving the Deny is bypassed. Re-run with
  `ec2:Attribute = "InstanceType"` to show the Deny *would* have worked if the case
  matched, isolating case-sensitivity as the sole variable.
- Doc gap flagged: neither `iam-policies-for-amazon-ec2.md` §"ec2:Attribute condition
  key" nor `API_ModifyInstanceAttribute.md` cross-references the other's casing
  convention or warns that the IAM-visible value is camelCase while the API parameter
  name is PascalCase. This omission is the proximate cause.
- Preconditions: policy author uses PascalCase by habit (very likely, since every other
  AWS reference surface they'd copy from PascalCases the field). Severity: **High** —
  for a customer who keys their entire "nobody may resize instances" control on this
  Deny, the condition IS the access-control mechanism and it is silently void.

Did **not** find evidence that `ec2:InstanceType`'s own *value* (`t3.micro` etc.) has a
documented case-sensitivity escape — the naming-convention doc
(`instance-type-names.md`) and every API example consistently lowercase the type string
on both the request side and any would-be policy-authoring side, so there's no
asymmetric casing convention to exploit the way there is for `ec2:Attribute`. Marked as
**doc gap, not a finding**: no document states whether the RunInstances/ModifyInstanceAttribute
APIs case-normalize an upper/mixed-case `InstanceType` string before launch (e.g. would
`T3.MICRO` be silently coerced to `t3.micro` and succeed) versus how IAM evaluates the
condition against the raw, pre-normalization request value. If the service is
case-tolerant on input but IAM evaluates pre-normalization, a `Deny` keyed on
`StringEquals {"ec2:InstanceType": "t3.micro"}` could theoretically be bypassed by
requesting `T3.MICRO`. No mirror or online doc confirms or refutes this either way —
recommend confirming via `SimulateCustomPolicy` plus a scoped dry-run `RunInstances`
(`DryRun=true`) in a lab account before treating this as more than a hypothesis.

### (c)/(d) Wrong-resource binding & statement override — CONFIRMED, with an AWS-authored sample as the vector (Lens R)

This is the strongest finding. AWS's own docs **acknowledge the general mechanism**:

`/work/aws-docs/docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md` lines 195-196
("Important" box):

> Many condition keys are specific to a resource, and some API actions use multiple
> resources. If you write a policy with a condition key, use the `Resource` element of
> the statement to specify the resource to which the condition key applies. If not, the
> policy may prevent users from performing the action at all...

That callout only warns about the *fail-closed* direction (over-broad Resource breaks
legitimate use). It does **not** warn about the *fail-open* direction: a second,
independent Allow statement whose `Resource` also happens to cover the same resource
(e.g. `instance/*`, or `"*"`) without the same condition will satisfy IAM's per-resource
OR-across-statements evaluation and nullify the narrow statement. Two of AWS's own
sample recipes in the same guide, read together exactly as presented, produce this.

**Sample A — "Instance types" recipe**
(`ExamplePolicies_EC2.md` lines 304-344, Allow variant):
```
Stmt1: Allow ec2:RunInstances on instance/*      Condition: StringEquals ec2:InstanceType in [t2.micro, t2.small]
Stmt2: Allow ec2:RunInstances on image/*, subnet/*, network-interface/*, volume/*, key-pair/*, security-group/*   (no condition)
```

**Sample B — "Launch templates" recipe**, same guide, same page, 548 lines later
(`ExamplePolicies_EC2.md` lines 862-878):
```
Stmt3: Allow ec2:RunInstances on Resource: "*"   Condition: ArnLike ec2:LaunchTemplate = arn:...:launch-template/lt-09477bcd97b0d310e
```
(and the `IsLaunchTemplateResource` variant at lines 884-908 is no safer — it only
constrains *override*, never `ec2:InstanceType`.)

- Claim: a customer who — as the guide's own "Topics" list at lines 219-227 invites, by
  presenting both as independent, composable recipes on the *same action* — adds Sample
  B's statement to a policy that already has Sample A's "cost control" statements,
  believing they've "additionally allowed a pre-approved launch template," has in fact
  **fully defeated the instance-type restriction**. `Stmt3`'s `Resource: "*"` matches the
  `instance*` resource the multi-resource `RunInstances` call touches, its only
  condition is on `ec2:LaunchTemplate`, and IAM's evaluation is OR across Allow
  statements: if the user launches via `lt-09477bcd97b0d310e` and that launch template
  (or an override in the same `RunInstances` call — `Stmt3` has no
  `IsLaunchTemplateResource` restriction at all) specifies e.g. `p4d.24xlarge`, `Stmt1`'s
  condition fails for the `instance` resource but `Stmt3` independently grants it. Net
  effect: cost-control statement is silently overridden by the launch-template statement,
  with no error, no log signal distinguishing it from a legitimate small launch.
- Confirm/refute oracle: `SimulateCustomPolicy` with the union of Stmt1+Stmt2+Stmt3 as
  the policy document, action `ec2:RunInstances`, context keys
  `ec2:InstanceType=p4d.24xlarge`, `ec2:LaunchTemplate=arn:...:launch-template/lt-09477bcd97b0d310e`,
  resource ARNs covering instance/image/subnet/etc. — expect `allowed`. Then remove Stmt3
  and re-run with the same context — expect `implicitDeny` on the `instance` resource,
  isolating Stmt3 as the sole cause of the bypass.
- Preconditions: customer adopts both AWS-published recipes (plausible — they're
  presented back-to-back as the canonical way to combine "control cost" with "allow
  launch templates"); no cross-reference between the two sections warns of the
  interaction. Severity: **High** — the condition key IS the access-control mechanism
  here, the bypass requires zero cleverness (just "use the allowed launch template"),
  and the vector is an AWS-authored sample policy, which per the engagement's Lens R
  framing is a **reportable Tier 2 finding** independent of any customer mistake.

**Separate wrong-resource/action-indirection instances (still shape (c)/(d), different
action rather than different statement):**

- `CreateFleet` (EC2 Fleet) — list_ec2.md line 5114, AWS's own action description:
  > "Resource-level permissions for this action do not include the resources specified
  > in a launch template. To specify resource-level permissions for resources specified
  > in a launch template, you must include the resources in the RunInstances action
  > statement."
  This is AWS stating in its own authorization reference that an `ec2:InstanceType`
  condition attached to `ec2:RunInstances` provides **no coverage** for instances
  launched by `ec2:CreateFleet` referencing a launch template — a structurally different
  action with a structurally different (and weaker) resource-level permission model for
  the same underlying launch template. `CreateFleet`'s own `instance*` resource row
  (line 5118) does list `ec2:InstanceType`, but only for instances specified as explicit
  `Overrides` in the `CreateFleet` request itself — not for the type baked into the
  referenced launch template, per the quoted caveat.
- `RequestSpotInstances` / `RequestSpotFleet` — list_ec2.md lines 9465-9480: resource
  types are only `image` and `key-pair`; there is **no `instance*` resource row and no
  `ec2:InstanceType` key anywhere in either action's condition-key list**. A policy that
  restricts instance types exclusively via `ec2:RunInstances` + `ec2:InstanceType`
  provides **zero** protection against the same principal calling
  `ec2:RequestSpotInstances`/`RequestSpotFleet` for any instance type — these actions
  cannot be instance-type-gated via resource-level IAM conditions at all, per the
  authorization reference.
- Autoscaling cross-service indirection — `/work/aws-docs/docs/service-authorization/latest/reference/list_autoscaling.md`
  line 850-851: `autoscaling:InstanceType` / `autoscaling:InstanceTypes` are a wholly
  separate condition-key namespace. Per AWS's own description (line 851):
  > "Filters access based on the instance types present as overrides to a launch
  > template for a mixed instances policy. Use it to qualify which instance types can be
  > explicitly defined in the policy"
  i.e. it only sees types declared as `Overrides` in a `MixedInstancesPolicy`, not a type
  baked natively into the referenced launch template — the same LT-origin blind spot as
  `CreateFleet` above, independently confirmed in a second service's docs. Compounding
  this: Auto Scaling launches instances via its own service-linked role, not the calling
  principal's credentials, so an `ec2:RunInstances`-scoped `ec2:InstanceType` restriction
  on the human/role never even enters the evaluation for ASG-driven launches — classic
  confused-deputy/action-indirection bypass of an instance-type cost-control policy.
- Confirm/refute oracle for this cluster: `SimulateCustomPolicy` against
  `ec2:RequestSpotInstances` (and separately `autoscaling:CreateAutoScalingGroup`) using
  only the customer's `ec2:RunInstances`-scoped policy — expect `implicitDeny` is NOT
  returned (i.e., the action is either unrestricted or governed by a completely
  different, likely-absent, condition set), demonstrating the restriction doesn't carry
  over. Severity: **High** where cost/hardware control is the stated compliance
  requirement, since these are standard, commonly-granted EC2 actions (Spot, Fleet, ASG)
  that most "launch instances" roles also carry.

### (e) Self-widen

- `ec2:InstanceType` is not itself a tag the launching principal controls, so the
  literal "set the attribute you're gated on" pattern doesn't apply to the `RunInstances`
  statement directly. But the **adjacent-action** version applies squarely: AWS's sample
  library (§(c)/(d) above) only ever shows the `ec2:InstanceType` condition attached to
  `ec2:RunInstances`. `ec2:ModifyInstanceAttribute` exposes the **identical**
  `ec2:InstanceType` key on its own `instance*` resource row (list_ec2.md line 8806) but
  no sample policy in `ExamplePolicies_EC2.md` demonstrates gating it. A customer who
  copies only the RunInstances recipe and separately grants
  `ec2:ModifyInstanceAttribute` (needed for ordinary admin tasks — stop/start, SG
  changes, etc.) without re-adding the `ec2:InstanceType` condition has left a
  stop → `ModifyInstanceAttribute(InstanceType=...)` → start path that fully self-widens
  past the launch-time cost/hardware cap, using an action whose IAM Attribute-name casing
  pitfall is described in (b) above if they *did* try to gate it and mistyped the case.
- Confirm/refute oracle: `SimulateCustomPolicy` on `ec2:ModifyInstanceAttribute` with the
  customer's actual combined policy (RunInstances recipe + whatever
  ModifyInstanceAttribute grant they have for routine admin) and context
  `ec2:InstanceType=p4d.24xlarge` — expect `allowed` unless the customer independently
  duplicated the condition.
- Severity: **Medium-High**, contingent on the customer's actual ModifyInstanceAttribute
  grant shape (common in practice; AWS's own "Modify a stopped instance" workflow doc,
  referenced from `API_ModifyInstanceAttribute.md` line 12, actively encourages using
  this action to change instance type on stopped instances, with no accompanying IAM
  guidance to mirror the launch-time restriction).

================================================================================
## 3. Lens R — AWS-authored sample policy audit summary
================================================================================

File: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md` (source URL
`https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.html`).

| Section (anchor) | Lines | Claims to restrict | Bypass present? |
|---|---|---|---|
| "AMIs" (`iam-example-runinstances-ami`) | 229-301 | Which AMI may be launched | Not instance-type scoped; out of scope but shares the same multi-resource pattern (Resource list covers instance/*, volume/*, etc. with no condition — correct here only because AMI restriction is encoded via `Resource` ARN enumeration, not a `Condition`, on the `image*` row.) |
| "Instance types" Allow variant | 304-344 | Launch only t2.micro/t2.small | **Self-consistent in isolation** — correct use of per-resource binding (condition tied to `instance*` row only). No bypass *on its own*. |
| "Instance types" Deny variant | 348-386 | Same, via Deny | Also self-consistent in isolation (an explicit Deny on any one resource in a multi-resource action kills the whole request, so scoping the Deny to `instance/*` is sufficient and correct). |
| "Launch templates" (3 variants) | 852-990 | Allow launch via a specific/any launch template, optionally without override | **Composability bypass**: none of the three variants carries any `ec2:InstanceType` condition. Combining any of them with the "Instance types" statements above (as the guide's flat structure invites) produces the Stmt1/Stmt2/Stmt3 override documented in §2(c)/(d). This is the Tier 2 finding. |
| "Work with launch templates" (manage the LT object itself) | 1624-1681 | Who may edit/delete launch templates | Separately gated by tag (`Purpose=Testing`), but note: whoever can call `CreateLaunchTemplateVersion`/`ModifyLaunchTemplate` on an approved LT can edit *its* instance type, which is then inherited for free by anyone holding the "Launch templates" Allow statement above — a second self-widen path once LT-authoring and LT-launching permissions are split across different "least privilege" roles without realizing the dependency. |

No sample policy in the mirror explicitly combines "Instance types" + "Launch templates"
into one hardened policy that also pins `ec2:InstanceType` inside the launch-template
branch (e.g. via `StringEquals` on `ec2:InstanceType` alongside `ec2:LaunchTemplate` in
the same statement) — such a combined, safe pattern is not documented anywhere found,
which is itself a documentation gap: AWS doesn't show customers the fix for the
composability trap its own two recipes create.

================================================================================
## 4. Answer to the specific "t3.* StringLike" question
================================================================================

For a policy using `"StringLike": {"ec2:InstanceType": "t3.*"}` on `ec2:RunInstances`
`Resource: instance/*`, the documented bypasses are:

1. **Launch templates with no matching `IsLaunchTemplateResource`/`InstanceType`
   constraint in the same or a sibling statement** (§2 c/d) — if any other Allow
   statement grants `RunInstances` on `instance/*` (or `"*"`) keyed only on
   `ec2:LaunchTemplate`/`ec2:IsLaunchTemplateResource`, that statement independently
   satisfies the `instance` resource for any type the launch template specifies or the
   caller overrides to, regardless of the `t3.*` `StringLike`.
2. **`ec2:RequestSpotInstances` / `ec2:RequestSpotFleet`** — no `ec2:InstanceType` key
   exists for these actions at all (list_ec2.md 9465-9480); the `t3.*` restriction simply
   doesn't apply if the principal also holds either of these actions.
3. **`ec2:CreateFleet`** — explicitly documented (list_ec2.md line 5114) to not apply
   resource-level permissions to launch-template-specified resources; only `Overrides`
   entries in the `CreateFleet` call itself are checked against `ec2:InstanceType`.
4. **`autoscaling:CreateAutoScalingGroup`** (and `UpdateAutoScalingGroup` with a
   `MixedInstancesPolicy`) — separate `autoscaling:*` condition-key namespace,
   `autoscaling:InstanceTypes` only inspects `Overrides`, not the LT-native type; launches
   execute under the ASG service-linked role, not the caller's own `ec2:RunInstances`
   permissions, so the `t3.*` condition on the human/role is never evaluated.
5. **Attribute-based instance-type selection** (`InstanceRequirements` on `RunInstances`/
   `CreateFleet`/`RequestSpotFleet`/ASG `MixedInstancesPolicy`) — resolves to a *set* of
   concrete instance types at launch time server-side, not a caller-supplied
   `InstanceType` string in the request; `ec2:InstanceType` as a request-context key is
   designed around an explicit `InstanceType` parameter, and no document in the mirror
   describes how/whether the resolved type from `InstanceRequirements` is exposed to the
   `ec2:InstanceType` condition key for evaluation. **Marked as a doc gap** — flagging
   for confirmation rather than asserting it as a bypass: searched
   `API_InstanceRequirements.md`, `ec2-fleet-attribute-based-instance-type-selection.md`,
   and `iam-policies-for-amazon-ec2.md` for any statement that `ec2:InstanceType` is (or
   is not) populated from `InstanceRequirements`-resolved launches; none found either way.
   If it is not populated, a `StringLike "t3.*"` condition would never match and the
   resource-level check would fail *closed* (blocking the whole launch) rather than open
   — so this would be an availability bug for the customer rather than a security bypass,
   unless the customer's statement structure makes the absence of a match equivalent to
   "falls through to a broader unconditioned sibling Allow" as in §2(c)/(d), in which case
   it becomes a bypass by the same override mechanism, not by anything specific to
   `InstanceRequirements`.
6. **`ec2:ModifyInstanceAttribute` post-launch** (§2 e) — the `t3.*` restriction is a
   launch-time check only; nothing in the sample library proposes mirroring it onto
   `ModifyInstanceAttribute`, so stop/resize/start is a standard self-widen path if that
   action is granted elsewhere without its own `ec2:InstanceType` condition.

================================================================================
## 5. Summary table of leads
================================================================================

| # | Claim | Key evidence | Oracle | Severity |
|---|---|---|---|---|
| 1 | Hallucinated hardware-class keys (bare-metal/Nitro/accelerator/enclave) are silently inert in Deny statements | list_ec2.md condition-key table has no such keys (0 hits) | SimulateCustomPolicy, Deny never fires | Medium |
| 2 | `ec2:Attribute` PascalCase vs camelCase mismatch voids Deny on `ModifyInstanceAttribute` instance-type changes | API_ModifyInstanceAttribute.md line 23 (`instanceType` enum) vs line 74 (`InstanceType` param) | SimulateCustomPolicy with `ec2:Attribute=instanceType` context | High |
| 3 | AWS's own "Instance types" + "Launch templates" sample recipes, combined as the guide presents them, let the launch-template statement silently override the instance-type cap | ExamplePolicies_EC2.md lines 304-386 vs 862-990 | SimulateCustomPolicy union-policy test, with/without Stmt3 | High (Tier 2 — AWS sample weakness) |
| 4 | `CreateFleet` resource-level perms explicitly exclude launch-template-specified resources | list_ec2.md line 5114 (AWS's own text) | Simulate/launch-template CreateFleet vs RunInstances comparison | High |
| 5 | `RequestSpotInstances`/`RequestSpotFleet` have no `ec2:InstanceType`/`instance*` row at all | list_ec2.md 9465-9480 | SimulateCustomPolicy shows no implicitDeny path tied to type | High |
| 6 | `autoscaling:InstanceType(s)` is a separate namespace, blind to LT-native type, and ASG launches via service-linked role bypass the caller's RunInstances restriction entirely | list_autoscaling.md lines 472/478/826/850-851 | SimulateCustomPolicy on autoscaling:CreateAutoScalingGroup | High |
| 7 | `ec2:ModifyInstanceAttribute` shares the `ec2:InstanceType` key but no AWS sample shows gating it; stop/resize/start self-widens past the RunInstances cap | list_ec2.md line 8806; API_ModifyInstanceAttribute.md line 74; absence in ExamplePolicies_EC2.md | SimulateCustomPolicy on customer's actual ModifyInstanceAttribute grant | Medium-High |
| 8 (doc gap, not asserted) | Whether `InstanceRequirements`-resolved (attribute-based) launches populate `ec2:InstanceType` for condition evaluation | No statement found in InstanceRequirements/attribute-based-selection/IAM docs | N/A — needs AWS clarification or lab test | Unknown |
| 9 (doc gap, not asserted) | Whether `ec2:InstanceType`'s *value* comparison is case-normalized relative to the raw API input | No statement found in instance-type-names.md, API_RunInstances.md, or IAM policy doc | SimulateCustomPolicy + DryRun RunInstances with mixed-case type | Unknown |
