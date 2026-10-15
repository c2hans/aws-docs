# Modify a Spot Fleet request (`ModifySpotFleetRequest`) — Attack Research Plan

Source of leads:
- User Guide: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-spot-fleet.html` (+ `.md` twin) — the target page.
- API Reference: `https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest.html` (+ `API_LaunchTemplateConfig.md`).
- IAM Service Authorization Reference (authoritative, offline + online): `list_ec2.md` lines 9017–9020 (ModifySpotFleetRequest), 9999 (spot-fleet-request resource ARN), 5119 (launch-template resource).
- AWS-managed SLR policy JSON: `AWSEC2SpotFleetServiceRolePolicy` v4 (offline mirror `docs/aws-managed-policy/latest/reference/AWSEC2SpotFleetServiceRolePolicy.md`).

Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Companion plan — read the siblings, do not re-derive them.** This plan owns the **modify-time (`ModifySpotFleetRequest`) mutation surface** of an *already-existing* Spot Fleet. It deliberately complements, and cross-references rather than restates:
> - `create-spot-fleet-attack-research-plan.md` — create/request-construction (SLR-launch guardrail bypass at `RequestSpotFleet` time, launch-spec injection). **This plan is the modify-time analog**: the same primitives re-triggered against a *live* fleet, plus the launch-spec *swap* that only exists at modify time.
> - `spot-fleet-prerequisites-attack-research-plan.md` — owns the PassRole/confused-deputy/IAM-artifact depth (`TerminateInstances` on `*`, `RegisterTargets */*`, the privesc chain). This plan cites it for the artifact detail it does not restate.
> - `spot-fleet-states-attack-research-plan.md` — owns the lifecycle/state-machine (`active`/`modifying`/`cancelled_running`). This plan cites it for the `modifying`-state race window.
> - `tag-spot-fleet-attack-research-plan.md` — owns tag/ABAC authz on the `spot-fleet-request` resource. This plan defers all tag-mutation leads to it and only consumes its conclusions.
> - `delete-fleet-attack-research-plan.md`, `ec2-fleet-attack-research-plan.md`, `modify-ec2-fleet-attack-research-plan.md` — the EC2-Fleet equivalents. **`modify-ec2-fleet` §5.1/5.2 is the closest cousin**: `ModifyFleet` as a launch/terminate primitive routing around `RunInstances`/`PassRole`/`TerminateInstances`, and the console-hidden `LaunchTemplateConfig` redirect. The Spot-Fleet analog below reaches the *same* oracles through the *legacy* API.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The highest-value Spot/EC2-Fleet leads are **intra-account privilege escalation via AWS-authored, uneditable managed IAM artifacts, PassRole/confused-deputy, and identity-policy-guardrail bypass on service-linked-role (SLR)-initiated launches/terminations** — not classic cross-tenant IDOR (the `sfr-` id is a full UUID → not fabricable/enumerable).
- **Prove every IAM lead under a scoped role holding *exactly* the artifact under test** (`iam:SimulatePrincipalPolicy` first — touches nothing — then a live scoped call with canary data). Never prove with the over-privileged tester.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the SLR's own session, an AWS-owned instance), stop, preserve evidence, flag for AWS-Security disclosure.
- Always cross-check the offline `.md` against the online `.md` twin (append `.md` to the `.html` URL) to avoid sync drift.

---

## 1. Pentest Objectives (concrete breach outcomes to attempt)
1. **Launch an instance with an IAM role (instance profile) the caller cannot `iam:PassRole`** by swapping the launch template/overrides into a live fleet via `ModifySpotFleetRequest` + a capacity increase — the SLR does the `RunInstances`+`PassRole`.
2. **Terminate EC2 instances the caller is explicitly denied `ec2:TerminateInstances` on**, by decreasing target capacity with `ExcessCapacityTerminationPolicy=default` so the SLR terminates them.
3. **Bypass an identity-policy `RunInstances` guardrail** (IMDSv2-required, instance-type/tenancy/instance-profile restrictions) by driving the launch through the SLR at modify time.
4. **Modify a Spot Fleet request owned by another principal/tenant** by naming its `sfr-` id, if resource-level permission is not enforced.
5. **Defeat an ABAC/condition-key scoping** written against `ModifySpotFleetRequest` (`ec2:ResourceTag`, `ec2:Attribute`) — case-sensitivity fail-open, tag-presence-vs-ownership, launch-template-scope omission.
6. **Cost / quota exhaustion**: drive a huge target-capacity increase (mass Spot/On-Demand launch) or forced mass termination against a fleet, as a self-DoS or (if cross-account modify works) a victim-DoS.
7. **Act on a fleet the docs say is immutable** (one-time / non-`maintain`, or non-`active` state) if the precondition is console-only, not API-enforced.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** SigV4 EC2 query/JSON API action `ec2:ModifySpotFleetRequest` (SDK/CLI `modify-spot-fleet-request`, PowerShell `Edit-EC2SpotFleetRequest`). Console route: **Spot Requests → Actions → Modify target capacity** — the console exposes **only** target capacity + On-Demand portion + a "Terminate instances" checkbox. The API accepts strictly more (see §4).

**Request parameters (API Reference).**
- `SpotFleetRequestId` (**required**, String) — e.g. `sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE` → `sfr-` + full UUID (128-bit) → **not enumerable/fabricable**.
- `TargetCapacity` (Integer) — new total fleet size. Increase ⇒ SLR launches more Spot (per allocation strategy) / On-Demand. Decrease ⇒ cancels open requests, optionally terminates running instances. Can be set to `0`.
- `OnDemandTargetCapacity` (Integer) — On-Demand portion.
- `ExcessCapacityTerminationPolicy` (String; **valid values `noTermination | default`**) — on decrease, whether to terminate running instances. Supported only for `maintain` fleets.
- `LaunchTemplateConfig.N` (Array of `LaunchTemplateConfig`) — **the launch template and overrides.** "You can only use this parameter if you specified a launch template (`LaunchTemplateConfigs`) in your Spot Fleet request." **Not surfaced in the console or the User-Guide prose; only in the API Reference.**
- `Context` (String, "**Reserved.**") — undocumented/internal field accepted by the API.
- Response: `return=true` boolean + `requestId` only (no resource echo).

**Processes / actors behind the interface.**
- **Caller identity** (IAM principal) — authorizes `ec2:ModifySpotFleetRequest`.
- **EC2 Spot Fleet service** + its **service-linked role** (`AWSServiceRoleForEC2SpotFleet`, policy `AWSEC2SpotFleetServiceRolePolicy` v4) — the SLR, *not the caller*, performs the resulting `RunInstances`, `RequestSpotInstances`, `PassRole`, `CreateTags`, `TerminateInstances`, `RegisterTargets`.
- **Launch template(s)** referenced by `LaunchTemplateConfig` — a *separately-owned* resource whose `$Latest`/`$Default`/explicit version resolves at launch time and carries the instance profile, user-data, AMI, SG, subnet, IMDS options.

**Assets.** Running EC2 instances (compute + any instance-profile credentials they receive); the Spot Fleet request object; the launch template contents; the SLR's own trust (the hard-stop service-plane boundary).

**Identity model.** Single-account, delegation-centric. The caller delegates launch/terminate authority to the SLR. **The caller's own identity-policy condition keys do NOT bind SLR-initiated actions** (see §5.1/§5.2 — the backbone finding) — only SCPs bind the SLR.

**Resource identifier shape.** `arn:${Partition}:ec2:${Region}:${Account}:spot-fleet-request/${SpotFleetRequestId}` (list_ec2 line 9999).

```
 Caller (IAM principal)
   │  ec2:ModifySpotFleetRequest  (authz checks: spot-fleet-request* [required], launch-template [optional])
   │   params: TargetCapacity↑↓ / OnDemandTargetCapacity / ExcessCapacityTerminationPolicy / LaunchTemplateConfig.N(hidden) / Context(reserved)
   ▼
 Spot Fleet service  ──assumes──►  AWSServiceRoleForEC2SpotFleet  (AWSEC2SpotFleetServiceRolePolicy v4)
   │                                   ├─ ec2:RunInstances          Resource:*  NO Condition      ← capacity increase
   │                                   ├─ ec2:RequestSpotInstances  Resource:*  NO Condition
   │                                   ├─ iam:PassRole              Resource:*  Cond: PassedToService=ec2.amazonaws.com(.cn)
   │                                   ├─ ec2:CreateTags            instance/* spot-instances-request/* spot-fleet-request/* volume/*
   │                                   ├─ ec2:TerminateInstances    Resource:*  Cond: StringLike ec2:ResourceTag/aws:ec2spot:fleet-request-id = "*"  ← capacity decrease (default policy)
   │                                   └─ elasticloadbalancing:RegisterTargets  arn:...:*/*
   ▼
 EC2 data plane: launches / terminates instances in the caller's account using the (possibly just-swapped) launch template
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller lacking `iam:PassRole` for role R | An EC2 instance running **with role R** | `ModifySpotFleetRequest LaunchTemplateConfig.N` → template referencing R's instance profile → capacity↑ → SLR `RunInstances`+`PassRole` | An instance exists carrying instance-profile R, launched by the SLR, that the caller could not have passed directly. **Privilege escalation.** |
| Caller explicitly denied `ec2:TerminateInstances` | Running instances tagged `aws:ec2spot:fleet-request-id` | `ModifySpotFleetRequest TargetCapacity↓ ExcessCapacityTerminationPolicy=default` → SLR `TerminateInstances` | Instances the caller is denied to terminate are terminated. **Guardrail bypass / destructive.** |
| Caller with an identity-policy `RunInstances` guardrail (IMDSv2/instance-type/tenancy) | New fleet instances | Capacity↑ relaunch runs under the SLR's unconditioned `RunInstances` | A launched instance violates the caller's own `RunInstances` condition (e.g. IMDSv1 allowed). **Policy-bypass.** |
| Caller / tenant A | Spot Fleet request owned by B (`sfr-...`) | `ModifySpotFleetRequest SpotFleetRequestId=<B's id>` | A's call mutates B's fleet (capacity/launch-template). **Cross-principal mutation** (requires knowing B's UUID). |
| Policy author's ABAC Deny (`ec2:ResourceTag`/`ec2:Attribute` on modify) | The modify action | Case/tag-presence mismatch between the written condition and the populated key | Modify succeeds against a resource the Deny intended to block. **ABAC fail-open.** |
| Any customer surface | **AWS's own service plane** (the SLR's session, AWS-owned fleet host) | — | Any AWS-owned identity/credential/ARN surfaced. **HARD STOP — preserve & disclose.** |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ModifySpotFleetRequest` | SigV4 EC2 API | Existing (legacy, "no planned investment") | **Yes** | External | Change target/On-Demand capacity; optionally swap launch template; set excess-termination policy | Yes | `ec2:ModifySpotFleetRequest` holders | **Legacy API.** Required resource `spot-fleet-request*`; optional `launch-template`. |
| └ param `LaunchTemplateConfig.N` | — | Existing | Yes | External | Replace the launch template + overrides on a live fleet | Yes | same | **Console-hidden / UG-prose-hidden** knob → §5.2 |
| └ param `Context` | — | Existing | ? | External | "Reserved." | Yes | same | Undocumented; probe for behavior → §5.6 |
| └ param `ExcessCapacityTerminationPolicy` | — | Existing | Yes (terminate) | External | `default` = terminate excess; `noTermination` = keep | Yes | same | Terminate side → §5.3 |
| `RequestSpotFleet` | SigV4 | Existing | Yes | External | Create fleet | Yes | `ec2:RequestSpotFleet` | **Owned by `create-spot-fleet` plan** |
| `CancelSpotFleetRequests` | SigV4 | Existing | Yes | External | Cancel fleet (`terminateInstances` flag) | Yes | `ec2:CancelSpotFleetRequests` | **Owned by `delete-fleet` plan** |
| SLR actions (`RunInstances`, `RequestSpotInstances`, `PassRole`, `CreateTags`, `TerminateInstances`, `RegisterTargets`) | internal | Existing | Yes | Internal (SLR identity) | Launch/terminate/tag/register on caller's behalf | No (SLR-only) | `AWSServiceRoleForEC2SpotFleet` | **The actual action surface** — see §5.1–§5.3 |

**IAM authorization facts (authoritative, `list_ec2.md`):**
- `ModifySpotFleetRequest` (lines 9017–9020) is **Write**, requires resource `spot-fleet-request*`, and *optionally* accepts resource `launch-template` (no asterisk).
  - On the `spot-fleet-request*` resource: condition keys `aws:ResourceTag/${TagKey}`, **`ec2:Attribute`**, **`ec2:Attribute/${AttributeName}`**, `ec2:Region`, `ec2:ResourceTag/${TagKey}`.
  - On the `launch-template` resource: condition keys `aws:ResourceTag/${TagKey}`, **`ec2:ManagedResourceOperator`**, `ec2:Region`, `ec2:ResourceTag/${TagKey}` (line 9019).
- `spot-fleet-request` resource ARN: `arn:${Partition}:ec2:${Region}:${Account}:spot-fleet-request/${SpotFleetRequestId}` (line 9999).
- SLR policy `AWSEC2SpotFleetServiceRolePolicy` v4 — key statements (verbatim):
  - `ec2:RunInstances`, `ec2:RequestSpotInstances`, `ec2:DescribeImages/Subnets/InstanceStatus` → `Resource:["*"]`, **no Condition**.
  - `iam:PassRole` → `Resource:["*"]`, Condition `StringEquals iam:PassedToService ∈ {ec2.amazonaws.com, ec2.amazonaws.com.cn}`.
  - `ec2:TerminateInstances` → `Resource:"*"`, Condition `StringLike "ec2:ResourceTag/aws:ec2spot:fleet-request-id":"*"` (**matches the tag KEY's presence with ANY value**).
  - `ec2:CreateTags` → `instance/*`, `spot-instances-request/*`, `spot-fleet-request/*`, `volume/*`.
  - `elasticloadbalancing:RegisterTargets` → `arn:aws:elasticloadbalancing:*:*:*/*`.

---

## 5. Recommended Areas of Focus (priority order)

### 5.1 `ModifySpotFleetRequest` is a **launch/terminate primitive that routes around the caller's `RunInstances`/`PassRole`/`TerminateInstances` controls** — **P0** (Lens B/E + variant, Lens X, Lens R/S)

**Background.** When `TargetCapacity`/`OnDemandTargetCapacity` is increased, "the Spot Fleet launches the additional Spot Instances" (UG + API ref). The launch is performed by the **SLR**, whose policy grants `ec2:RunInstances`/`ec2:RequestSpotInstances` on `Resource:"*"` with **no Condition** and `iam:PassRole` on `Resource:"*"` gated only by `iam:PassedToService=ec2.amazonaws.com`. This is the fleet-services **backbone finding** (shared with `create-spot-fleet` §backbone and `spot-fleet-prerequisites`): a customer's *identity-policy* `RunInstances` condition keys (`ec2:MetadataHttpTokens`/IMDSv2, `ec2:InstanceType`, `ec2:InstanceProfile`, `ec2:Tenancy`, `ec2:AssociatePublicIpAddress`, …) **do not propagate** to SLR-initiated launches. The modify-time novelty is that this re-fires against a **live, already-authorized** fleet, and the trigger (`ec2:ModifySpotFleetRequest`) is a *different, narrower* permission than `ec2:RunInstances`.

**Security Concern.** A principal holding **only** `ec2:ModifySpotFleetRequest` (+ `ec2:DescribeSpotFleetRequests`) on an existing `maintain` fleet can cause N new instances to launch **without holding `ec2:RunInstances` at all**, and bypass any identity-policy launch guardrail the org believes it has enforced. This parallels the confirmed `ec2:ModifyInstanceAttribute(userData)` exemplar (a non-PassRole action reaching a role's live launch spec) and `modify-ec2-fleet` §5.1.

**High-level Test Scenarios.**
1. **Claim:** a role with `ec2:ModifySpotFleetRequest` but *explicitly denied* `ec2:RunInstances` can still cause launches. → **Oracle:** scoped role increases `TargetCapacity` by K; observe K new instances appear launched by the SLR (`DescribeSpotFleetInstances`), while a direct `RunInstances` from the same role returns `AccessDenied`. → **Sev: High.**
2. **Claim:** an identity-policy guardrail `Deny RunInstances if ec2:MetadataHttpTokens != required` does not apply to the modify-triggered relaunch. → **Oracle:** fleet whose launch template sets `HttpTokens=optional`; capacity↑; new instance has IMDSv1 enabled despite the caller's Deny. → **Sev: High** (IMDSv2 bypass → downstream SSRF-to-credentials exposure).
3. **Claim (chain to 5.2):** combined with a launch-template swap, the relaunch passes an instance profile the caller cannot `PassRole`. → see §5.2.

**Doc evidence.** UG "the Spot Fleet launches the additional Spot Instances according to the allocation strategy"; SLR policy v4 (`RunInstances`/`RequestSpotInstances` `Resource:*` no Condition; `PassRole` `Resource:*`).
**Preconditions.** An existing `maintain` fleet the principal can modify; Spot/On-Demand capacity + vCPU quota headroom. **Cost.** Spot/On-Demand instance-hours. **Severity-if-true.** High (privilege/guardrail bypass; Critical only if it reaches the service plane — hard stop).
**Stop condition.** Once one guardrail-violating instance is observed, stop; do not scale further. Tear down (set capacity back to original, terminate canaries).

---

### 5.2 Console-hidden `LaunchTemplateConfig.N` on `ModifySpotFleetRequest` → **launch-spec redirect → PassRole-less role / AMI / user-data injection on a LIVE fleet** — **P0** (Lens B/E, Step-3 hidden-knob, Lens U)

**Background.** The API accepts `LaunchTemplateConfig.N` ("The launch template and overrides") on modify, but **the console and the User-Guide prose expose only target capacity** — a textbook "the control-plane API accepts more than the console surfaces" delta (the skill's hidden-knob discipline; the exact shape of `modify-ec2-fleet` §5.2). `list_ec2` confirms `launch-template` is an accepted (optional) resource type on `ModifySpotFleetRequest`, so the parameter is a real authorizable surface, not a no-op.

**Security Concern.** If `LaunchTemplateConfig.N` lets a caller **swap or override the launch template** on a fleet (changing AMI, user-data, **instance profile / IAM role**, SG, subnet) and the subsequent capacity-increase relaunch runs it under the SLR's unconditioned `RunInstances`+`PassRole`, then the modify caller injects a launch spec they could never have launched directly — **the SLR passes any `ec2.amazonaws.com`-trusting role for them.** The caller never needs `iam:PassRole`.

**High-level Test Scenarios.**
1. **Claim:** `ModifySpotFleetRequest` accepts a `LaunchTemplateConfig` naming a launch template / version the caller does not own or is not scoped to. → **Oracle:** modify a fleet, supplying a template that references instance-profile `AdminInstanceProfile`; capacity↑; a new instance launches with that profile, retrievable via IMDS. The caller holds **no** `iam:PassRole`. → **Sev: High (intra-account privesc to the role's permissions).**
2. **Claim:** the `launch-template` resource authz is **not** enforced (the Modify policy was scoped only on `spot-fleet-request`, leaving `launch-template` at implicit `*`). → **Oracle:** scoped role with `ModifySpotFleetRequest` on `spot-fleet-request/<id>` but no explicit `launch-template` grant still swaps in an arbitrary template. (list_ec2 marks `launch-template` **optional/non-required** → a policy that only grants the required `spot-fleet-request*` resource may leave the template unrestricted.) → **Sev: High.**
3. **Claim ($Latest/$Default late-binding):** supplying a template version `$Latest` (or editing the template after the modify) binds the AMI/profile **at relaunch time**, so a later `CreateLaunchTemplateVersion` + capacity bounce injects new content without a second `ModifySpotFleetRequest`. → **Oracle:** point fleet at `lt-xxx:$Latest`; publish a new version with a malicious instance profile; set capacity 0→K; new instance uses the new version. → **Sev: High** (persistence / deferred injection).
4. **Claim (LaunchSpecifications vs LaunchTemplateConfigs mismatch):** the API says `LaunchTemplateConfig` is usable *only* if the fleet was created with a launch template; probe the error path when the fleet used inline `LaunchSpecifications` — does the API reject cleanly, silently ignore, or accept and corrupt state? → **Oracle:** modify a `LaunchSpecifications`-created fleet with `LaunchTemplateConfig.N`; observe reject vs partial-apply. → **Sev: Medium (state-confusion / validator gap).**

**Doc evidence.** API Reference `LaunchTemplateConfig.N` param; `list_ec2` line 9019 (`launch-template` resource + `ec2:ManagedResourceOperator`); SLR `PassRole Resource:*`.
**Preconditions.** A modifiable `maintain` fleet created with a launch template; a target instance profile/role trusting `ec2.amazonaws.com`. **Cost.** instance-hours. **Severity.** High (Critical if the passed role or launched instance reaches AWS's service plane — hard stop).
**Stop condition.** One instance observed with the injected profile = PoC. Stop; do not use the vended credentials beyond proving they exist; tear down.

> **Cross-ref:** `spot-fleet-prerequisites` owns the full `iam:PassRole Resource:*` confused-deputy analysis and the `TerminateInstances`-on-`*` / `RegisterTargets */*` privesc chain. This lead consumes those conclusions; it does **not** restate them. `create-spot-fleet` owns the equivalent injection at *create* time — the modify path is distinct because it mutates an **already-approved** fleet and needs only `ec2:ModifySpotFleetRequest`.

---

### 5.3 Terminate-side guardrail bypass: `ExcessCapacityTerminationPolicy=default` → SLR terminates instances the caller is denied — **P1** (Lens X, Lens R/S)

**Background.** On a capacity decrease with `ExcessCapacityTerminationPolicy=default`, "the Spot Fleet terminate[s] Spot Instances until the size of the fleet reaches the new target capacity" — performed by the SLR, whose `ec2:TerminateInstances` is granted on `Resource:"*"` with Condition `StringLike "ec2:ResourceTag/aws:ec2spot:fleet-request-id":"*"`. **The condition binds the *presence* of the tag key with ANY value (`"*"`), not ownership of a specific fleet** — the canonical Lens-S "presence-not-ownership" shape.

**Security Concern.** `ModifySpotFleetRequest` is a **terminate primitive** reachable without `ec2:TerminateInstances`, mirroring §5.1's launch side. Two sub-concerns:
1. A principal denied `ec2:TerminateInstances` can still destroy fleet instances by shrinking the fleet.
2. The SLR's termination grant does **not** pin the *specific* `fleet-request-id` value — the IAM boundary alone would permit terminating **any** instance carrying the `aws:ec2spot:fleet-request-id` tag key (set by *any* Spot Fleet in the account). The service's internal logic presumably filters to the modified fleet; the **IAM artifact does not enforce that filter** → audit whether a decrease on fleet A can reach instances tagged for fleet B (e.g. via tag manipulation, or a logic gap).

**High-level Test Scenarios.**
1. **Claim:** a role with only `ec2:ModifySpotFleetRequest` (denied `ec2:TerminateInstances`) terminates running instances by decreasing capacity with `default`. → **Oracle:** two canary instances in fleet; decrease capacity by 2 with `ExcessCapacityTerminationPolicy=default`; both terminated with a Spot interruption notice. Direct `TerminateInstances` from the role → `AccessDenied`. → **Sev: High (destructive, authz bypass).**
2. **Claim (tag-presence over-grant):** because the SLR's `TerminateInstances` condition keys on tag *presence*, an instance that acquired the `aws:ec2spot:fleet-request-id` tag key (any value) is in-scope for SLR termination. → **Oracle:** audit via `iam:SimulatePrincipalPolicy` on a scoped copy of the SLR policy whether termination is bounded by the specific fleet id or only the tag key; then, read-only, check whether the service passes the specific id. **Do not actually terminate another fleet's instances.** → **Sev: Medium–High (over-broad AWS-authored grant; reportable as a Tier-2 AWS artifact defect).**
3. **Claim (`noTermination` ⇒ silent capacity drift):** with `noTermination`, the fleet keeps running instances above the new target and "not replace any ... interrupted" — does accounting drift leave orphaned instances / open requests that outlive the fleet record? → cross-ref `delete-fleet` and `spot-fleet-states`. → **Sev: Low–Medium.**

**Doc evidence.** UG considerations ("Spot Instance interruption notice"); API ref `ExcessCapacityTerminationPolicy` valid values; SLR policy `TerminateInstances` Condition.
**Preconditions.** A `maintain` fleet with running instances. **Cost.** negligible (termination). **Severity.** High (destructive guardrail bypass); the tag-presence over-grant is a Tier-2 AWS-authored-artifact finding (route `aws-security`).
**Stop condition.** One denied-termination observed = PoC. Never terminate a resource outside the canary fleet you created.

---

### 5.4 Resource-level / condition-key scoping on `ModifySpotFleetRequest` — enforcement & fail-open — **P1** (Lens A, Lens I, Lens S + variants)

**Background.** `list_ec2` marks `spot-fleet-request*` **required** on `ModifySpotFleetRequest`, with condition keys `aws:ResourceTag`, `ec2:ResourceTag`, `ec2:Region`, **`ec2:Attribute`**, **`ec2:Attribute/${AttributeName}`**. So, contrary to the Spot-Fleet User-Guide's blanket "resource-level permissions are not supported for `spot-fleet-request`" claim (see `tag-spot-fleet` lead U1 and the project memory — the UG prose contradicts the authoritative reference), a policy **can** scope modify to specific fleets by ARN/tag. The question is whether that scoping is actually enforced and whether its condition keys can be bypassed.

**Security Concern.** Three concrete fail-open shapes:
1. **`ec2:Attribute` case-sensitivity fail-open (confirmed-class variant).** The skill records `ec2:Attribute` as a confirmed case-sensitivity fail-open exemplar: a Deny written against a lowercase attribute value is inert when the key is populated with the PascalCase request field. If an org writes `Deny ModifySpotFleetRequest if ec2:Attribute StringEquals "targetcapacity"` (or similar), is the key populated as `TargetCapacity`/`targetCapacity`, defeating the Deny?
2. **Tag-presence vs ownership** (`ec2:ResourceTag/K:"*"` matches any value → any tagged fleet passes). Does a tag-scoped modify grant bind the *value* or just the key?
3. **Resource-level enforcement actually honored?** Does a role scoped to `spot-fleet-request/<id-A>` get `AccessDenied` when modifying `<id-B>` — or is resource-level permission silently not enforced (the UG's own "not supported" claim, if taken as an implementation statement, would predict a *fail-open*)?

**High-level Test Scenarios.**
1. **Claim:** modify is **not** resource-scoped despite `list_ec2` listing `spot-fleet-request*` as required. → **Oracle:** role allowed `ModifySpotFleetRequest` only on `arn:...:spot-fleet-request/<A>`; attempt to modify `<B>`; **Confirm = success (fail-open, contradicts reference), Refute = AccessDenied.** → **Sev: Medium–High** (ABAC/least-priv control is advisory, not enforced) + an **Informational doc-vs-reference contradiction** (Lens U) worth filing.
2. **Claim:** `ec2:Attribute` populated with a different case than a Deny expects → Deny bypass. → **Oracle:** author a scoped-copy Deny on the attribute value; `SimulatePrincipalPolicy` with each casing; a casing that still Allows confirms fail-open. → **Sev: Medium.**
3. **Claim:** which `AttributeName` values does `ec2:Attribute/${AttributeName}` actually populate for modify (targetCapacity? excessCapacityTerminationPolicy? launchTemplateConfig?) — is `launchTemplateConfig` *not* among them, so a Deny keyed on attributes cannot block the §5.2 redirect? → **Oracle:** CloudTrail / Simulate behavior across each param. → **Sev: Medium (blind-spot in the enforceable condition surface).**

**Doc evidence.** `list_ec2` lines 9019–9020, 9999; project memory on the UG-vs-reference contradiction. **Preconditions.** Ability to author/attach a scoped test role (own test account). **Cost.** none (Simulate) → minimal. **Severity.** Medium–High. **Stop condition.** First confirmed fail-open per sub-claim.

> **Cross-ref:** all **tag-mutation** leads (forcing `Resource:"*"` CreateTags, fleet-role tag-provenance, mandatory-tag fail-open) belong to `tag-spot-fleet-attack-research-plan.md`. This lead only consumes the authz facts; route any tag-write PoC to that plan.

---

### 5.5 Cost / quota exhaustion & capacity-accounting abuse — **P2** (Lens L)

**Background.** `TargetCapacity`/`OnDemandTargetCapacity` are unbounded integers in the API; an increase triggers immediate mass launch via the SLR. A decrease to a very small value forces mass termination. There is no documented per-call ceiling on the delta.

**Security Concern.** `ModifySpotFleetRequest` is a single call that can swing a fleet's instance count arbitrarily — a cost-amplification / vCPU-quota-exhaustion lever, and (if §5.4 cross-account modify holds) a victim-DoS lever.

**High-level Test Scenarios.**
1. **Claim:** a single modify to a very large `TargetCapacity` launches up to the On-Demand/Spot vCPU quota, incurring cost / starving the account. → **Oracle:** increase to a large value in a test account; observe launch burst until quota; note whether any throttle/warning exists. → **Sev: Low–Medium (self-DoS / cost); High only if cross-account modify (§5.4) is confirmed.**
2. **Claim:** rapid alternating increase/decrease (capacity flapping) churns launches/terminations, amplifying cost and interruption notices to co-tenant workloads behind shared ELB targets. → **Oracle:** flap capacity; measure launch/terminate churn. → **Sev: Low (single-tenant).**

**Doc evidence.** UG scale-up/scale-down behavior; API integer params. **Severity.** Low–Medium (single-tenant self-DoS is largely out-of-scope unless cross-account). **Stop condition.** Observe the behavior once; do not sustain cost.

---

### 5.6 State preconditions, `modifying`-state race, `Context` reserved param, and audit — **P3** (Lens P, Lens U, Lens O, Step-3 hidden-knob)

**Background.** "You can only modify a Spot Fleet request of type `maintain`" and "You can't modify a one-time Spot Fleet request"; "while ... being modified, it is in the `modifying` state." The console enforces the `maintain` precondition via UI; the API's enforcement and the race window are the question.

**Security Concern / Scenarios.**
1. **Claim (precondition is console-only):** the API accepts `ModifySpotFleetRequest` against a `one-time`/non-`maintain` or non-`active` (cancelling) fleet. → **Oracle:** call modify on a one-time fleet / a fleet in `cancelled_running`; Confirm = accepted/partial-apply, Refute = clean `UnsupportedOperation`. → **Sev: Low–Medium (state-machine integrity; cross-ref `spot-fleet-states`).**
2. **Claim (`modifying`-state race):** concurrent `ModifySpotFleetRequest` calls, or a modify racing a `CancelSpotFleetRequests`, produce inconsistent capacity/launch-template state or double-launch. → **Oracle:** fire two modifies (different `LaunchTemplateConfig`) simultaneously; inspect which template the relaunch uses. → **Sev: Medium (TOCTOU → §5.2 injection window).** Cross-ref `spot-fleet-states`.
3. **Claim (`Context` reserved):** the "Reserved" `Context` string param is accepted and reaches an internal consumer (injection / internal-routing signal). → **Oracle:** send structured/oversized `Context` values; observe acceptance, error differential, or any reflected/logged effect. → **Sev: Informational→Medium if it influences internal handling.**
4. **Claim (audit gaps):** the SLR-initiated launches/terminations triggered by modify are attributed to the SLR, not the modify caller — does CloudTrail link the `ModifySpotFleetRequest` to the resulting `RunInstances`/`TerminateInstances` so the human operator is accountable? → **Oracle:** diff CloudTrail events after a modify-driven launch; check caller attribution. → **Sev: Low–Informational (enabler for §5.1–§5.3 deniability).**

**Doc evidence.** UG considerations; API ref ("only ... type `maintain`", `modifying` state, `Context` Reserved). **Severity.** Low–Medium. **Stop condition.** Characterize each behavior once.

---

### Kill-chain candidates (rate at the end of the chain)
- **§5.2 → §5.1 → service-plane credentials:** `ModifySpotFleetRequest LaunchTemplateConfig.N` (swap to a template with a privileged instance profile + `HttpTokens=optional`) → capacity↑ → SLR `RunInstances`+`PassRole` launches it → IMDSv1-reachable role credentials for a role the caller could never pass. **End severity: High (Critical + HARD STOP if the role or instance reaches AWS's own plane).**
- **§5.3 (terminate) + §5.4 (cross-fleet tag-presence) :** if a modify-driven termination is bounded only by the SLR's tag-*presence* condition and the service's id-filter can be subverted, a decrease on an attacker fleet reaches another fleet's instances. **End severity: High (cross-workload destruction).** — audit-only until the IAM/service-filter boundary is understood; do not terminate foreign instances.
- **§5.2 ($Latest late-binding) → persistence:** point the fleet at `lt-xxx:$Latest`, then inject via `CreateLaunchTemplateVersion` + a capacity bounce with no further `ModifySpotFleetRequest` — a durable re-infection primitive surviving a single-point remediation.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Launch instance with un-passable IAM role via modify-time template swap | `ModifySpotFleetRequest LaunchTemplateConfig.N` + SLR `PassRole Resource:*` | `iam:PassedToService=ec2.amazonaws.com` is the *only* `PassRole` guard; no `aws:SourceArn`, no caller-PassRole check |
| Launch bypassing identity-policy `RunInstances` guardrails (IMDSv2/type/tenancy) | SLR `RunInstances Resource:* no Condition` | None at identity-policy layer (only SCPs bind the SLR) |
| Terminate instances without `ec2:TerminateInstances` | `ExcessCapacityTerminationPolicy=default` + SLR `TerminateInstances` | SLR `TerminateInstances` Condition keys on tag *presence* only |
| Modify another fleet by id | `SpotFleetRequestId` + resource-level authz | `spot-fleet-request*` required per `list_ec2` (UG prose claims unsupported — contradiction to test) |
| ABAC Deny bypass via `ec2:Attribute` casing | Modify condition keys | `ec2:Attribute` case-sensitivity (known fail-open class) |
| Cost/quota blast via unbounded `TargetCapacity` | capacity params | No documented per-call delta ceiling |
| Modify a non-`maintain`/non-`active` fleet | state precondition | "only ... type `maintain`" — API enforcement unverified |
| SLR action attribution to the modify caller | CloudTrail | SLR identity performs the launch/terminate |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **IMDS presence on managed hosts** per se — only *in scope* as the §5.1/§5.2 chain where the *caller's own guardrail* is bypassed; the existence of IMDS on EC2 is not a bug.
- **Single-tenant self-DoS / self-inflicted cost** (§5.5) — out of scope unless a confirmed cross-account modify (§5.4) makes it a victim-DoS.
- **Customer-authored** least-privilege footguns (a customer writing an over-broad `ModifySpotFleetRequest` grant on themselves). **In scope only** the AWS-authored, uneditable `AWSEC2SpotFleetServiceRolePolicy` defaults (§5.1–§5.3), which route `aws-security` as Tier-2.
- **Shared EC2/Spot capacity-pool contention** (noisy-neighbor at the Spot market level) — AWS-owned infra, out of scope.
- **Tag-mutation PoCs** — owned by `tag-spot-fleet-attack-research-plan.md`; **create-time** injection — owned by `create-spot-fleet`; **lifecycle/state** depth — owned by `spot-fleet-states`; **cancel/delete** — owned by `delete-fleet`. This plan references, does not re-execute, them.
- **The hard stop:** any AWS service-plane identity/credential/ARN/account → stop, preserve, disclose.

---

## 8. Null Hypotheses / Doc Gaps (lenses that did not fire, pages checked)
- **Lens G (SSRF):** N/A — pages checked: `modify-spot-fleet.html`, `API_ModifySpotFleetRequest.html`. `ModifySpotFleetRequest` has **no field the service dereferences** (no URL/URI/endpoint/webhook); the only "pointer" is the `LaunchTemplateConfig` reference, which is an EC2 resource id, not a server-side fetch. (The AMI/user-data inside the template is a §5.2 injection concern, not SSRF.)
- **Lens H (KMS/encryption-context):** deferred — EBS/volume encryption in the swapped launch template could involve a CMK, but modify does not take a key parameter; cross-ref `create-spot-fleet` for launch-spec KMS leads.
- **Lens J (OAuth/3P):** N/A — no third-party integration on this surface.
- **Lens K (prompt injection):** N/A — no LLM/agent in the modify path.
- **Lens Q (file upload):** N/A — no blob upload; `LaunchTemplateConfig` is structured JSON, not an uploaded file.
- **Lens Y (transport/sig):** standard SigV4 EC2 endpoint; no modify-specific transport weakness documented. Generic SigV4 coverage leads (presigned replay etc.) are not applicable to this synchronous mutating call. **doc-gap:** internal SLR→EC2 hop auth is undocumented (not customer-reachable).
- **Lens A cross-tenant IDOR:** **genuine partial-null** — `sfr-<UUID>` (128-bit) is **not enumerable or fabricable**, so blind cross-tenant discovery fails; the residual IDOR risk (§5.4) is *known-id* resource-level-permission enforcement, not guessing.
- **Lens D/V (network segmentation):** N/A for the modify API itself (control-plane call); any data→control-plane reach belongs to the *launched instance's* posture (cross-ref `create-spot-fleet`).
- **Doc gap flagged:** the exact set of `AttributeName` values populated into `ec2:Attribute/${AttributeName}` for `ModifySpotFleetRequest` (does it cover `launchTemplateConfig`?) is **not documented** → §5.4 scenario 3 must confirm the enforceable-condition surface empirically before trusting an attribute-based Deny. Marked "doc-gap — confirm surface first."
