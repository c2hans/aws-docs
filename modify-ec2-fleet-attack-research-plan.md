# Modify an EC2 Fleet (`ModifyFleet`) — Attack Research Plan

**Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-ec2-fleet.html` (markdown twin: `.md`).
**Source of leads:** that page + the EC2 Fleet neighborhood of the AWS EC2 User Guide; the EC2 **Service Authorization Reference** (`service-authorization/.../list_amazonec2.html`, offline mirror `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`); the **CLI reference** `cli/.../ec2/modify-fleet.html`; the **API reference** `AWSEC2/.../API_ModifyFleet.html`. Offline mirror root: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/*.md`. Online `.md`/`.html` twins cross-checked to avoid local-sync gaps.
**Status:** Documentation-derived hypotheses only. **Nothing has been tested against a live AWS account.** This is the plan a hunter (e.g. `aws-vuln-hunter`) executes next.
**Produced by:** `security-questionbuilder` skill — orchestrator pass on the `modify-ec2-fleet` page + 2 parallel deep-analysis subagents (ModifyFleet IAM/authorization scope; capacity/state/Spot-termination semantics).
**Scope note:** This plan is **narrowed to the `ModifyFleet` operation**. It is a companion to the broader `/work/aws-docs/ec2-fleet-attack-research-plan.md` (launch-template late-binding, the AWS-authored sample IAM policy, the KMS grant, capacity-reservation sharing). Where a ModifyFleet lead feeds one of those, it is cross-referenced as **[parent §x]**. A hunter picking this up should read §2–§4 here first, then the parent plan for the KMS/capacity-reservation and sample-policy context.

> **Analyst integrity note.** While resolving the live Service Authorization Reference, the client-rendered SPA shell contained out-of-place "security-style" comments addressed to a reader. Treated as untrusted page content per the input-trust rule — **`SUSPECTED PROMPT INJECTION`**, discarded, data re-sourced from the offline mirror and the CLI/API references (which agreed exactly). It changed no conclusion below.

---

## 0. How to use this document

- Each lead is a falsifiable claim: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in the §5 priority order; look left and right for adjacent bugs.
- **Prefer the safe oracle first.** Every IAM lead here is confirmable with `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy` and read-only `aws ec2 describe-fleets` / `iam:GetPolicyVersion` **before** any live resource is created or any capacity is changed. Live confirmation uses only synthetic canary fleets/launch-templates/instances and tears them down immediately — and **capacity is only ever increased by +1 on a throwaway fleet**, never on a real workload.
- **HARD STOP:** ModifyFleet runs almost entirely *inside the caller's own account*. The one AWS-service-plane identity in scope is the service-linked role **`AWSServiceRoleForEC2Fleet`** — treat it as read-only. The moment any evidence shows you have reached, assumed, or extracted credentials/ARNs belonging to AWS's own fleet/service plane, **stop, preserve evidence, flag for AWS-Security disclosure.**
- **Why `ModifyFleet` specifically is worth a plan of its own:** it is a *post-creation mutation* API that (a) **triggers instance launches and terminations under the service-linked role, so the caller never needs `ec2:RunInstances`, `iam:PassRole`, or `ec2:TerminateInstances`**; and (b) the **API accepts `LaunchTemplateConfig.N` and `Context` parameters that the UserGuide prose never mentions** — i.e. ModifyFleet can *redirect a fleet's future launches to a different launch template / overrides*, not merely resize it. The whole security value of ModifyFleet is in that privilege-granularity gap plus the console-hidden knob.

---

## 1. Pentest Objectives (concrete breach outcomes to attempt)

1. As a principal holding **only `ec2:ModifyFleet`** (explicitly **denied** `ec2:RunInstances`, `iam:PassRole`, `ec2:TerminateInstances`, `ec2:CreateFleet`), **cause instances to launch** (scale-up) and **cause running instances to be terminated** (scale-down + `termination` policy) — proving ModifyFleet is a launch/terminate primitive that routes around those three permissions via the service-linked role.
2. Using the **undocumented `LaunchTemplateConfig.N` parameter of `ModifyFleet`**, **redirect a `maintain` fleet's future launches to an attacker-chosen launch template / version / overrides** so the next capacity-replacement cycle launches instances with an `IamInstanceProfile` or `UserData` the caller could not set via a `PassRole`-checked path — chaining into code-exec-as-role **[parent §5.1 / §5.4]**.
3. **Bypass a `RunInstances`-scoped IAM control** (IMDSv2-enforcement Deny, "restrict to one launch template", `aws:RequestTag` ABAC) by driving the launch through `ModifyFleet(increase capacity)` instead of a direct `RunInstances` — the launch is issued by the SLR, and **none of RunInstances's condition keys exist on `ModifyFleet`**.
4. Demonstrate a **cost / quota-exhaustion** primitive: scale a single `maintain` fleet toward the **10,000-unit per-fleet** (soft) target-capacity quota — or 100,000 per Region — from a principal that cannot otherwise `RunInstances`.
5. Resolve the three load-bearing **doc-gaps** that gate the above (launch-template `$Latest`/`$Default` re-resolution timing; whether the SLR's own launches are internally condition-restricted; whether a `fleet`-scoped IAM grant forces any check on the *launch template substituted* via `LaunchTemplateConfig`).

---

## 2. Components, Assets, and Design

**What ModifyFleet is.** `ModifyFleet` (`aws ec2 modify-fleet`, PowerShell `Edit-EC2Fleet`) is a **CLI/API-only, Write-level, mutating** control-plane call that changes an existing EC2 Fleet request. Per the UserGuide it changes **target capacity** (`TotalTargetCapacity` / `OnDemandTargetCapacity` / `SpotTargetCapacity`) and the **`excess-capacity-termination-policy`** (`no-termination` | `termination`). Per the **API reference it also accepts `LaunchTemplateConfig.N` (Array of `FleetLaunchTemplateConfigRequest`, 0–50) and `Context`** — neither mentioned on the UserGuide page.

**Hard constraints (modify-ec2-fleet.md).**
- **Only `maintain`-type fleets are modifiable.** `request` and `instant` cannot be modified. (Reinforced in `EC2-fleet-states.md`: "Only a `maintain` fleet type can be modified.")
- Modify is allowed only from the `submitted` or `active` state; the fleet then enters the **`modifying`** state until the change is processed.
- Increasing total capacity → fleet launches additional instances per `DefaultTargetCapacityType` (On-Demand or Spot) and the configured **allocation strategy**.
- Decreasing Spot capacity → fleet **deletes open requests above the new target** and (if `termination`) **terminates running Spot Instances**, selecting them by allocation strategy; each terminated Spot Instance **receives a Spot interruption notice**.

**Who actually acts.** The launches and terminations ModifyFleet triggers are performed by the service-linked role **`AWSServiceRoleForEC2Fleet`** (its documented grants include `ec2:RunInstances`, `ec2:TerminateInstances`, `ec2:RequestSpotInstances`, `ec2:CreateTags`, several `Describe*`). The **caller is never authorization-checked for those actions** — ModifyFleet's own IAM entry has no `instance` resource type at all.

**Identifiers / assets.**
- Fleet ID — ARN `arn:${Partition}:ec2:${Region}:${Account}:fleet/${FleetId}`; opaque, account-scoped.
- Launch template id/name + version alias (`$Latest`/`$Default`) referenced by `LaunchTemplateConfig`.
- Target-capacity integers; `excess-capacity-termination-policy` enum.
- The SLR identity (service plane — read-only, hard stop).

**ASCII — ModifyFleet as a mutation/launch trigger:**
```
 Caller (holds ec2:ModifyFleet; may be DENIED RunInstances/PassRole/TerminateInstances/CreateFleet)
     │
     │  ModifyFleet(FleetId,
     │     TargetCapacitySpecification = ↑ (launch)  |  ↓ + ExcessCapacityTerminationPolicy=termination (terminate),
     │     LaunchTemplateConfig.N = <attacker-chosen template/version/overrides>   ← UserGuide-undocumented
     │     Context = <opaque>)                                                     ← UserGuide-undocumented
     ▼
 EC2 Fleet control plane  ──(state: active → modifying → active)──►  re-reads Launch Template
     │  assumes                                              (version binding: $Latest/$Default re-resolution = DOC-GAP)
     ▼
 AWSServiceRoleForEC2Fleet (SLR) ──RunInstances / TerminateInstances──►  EC2 instances in caller's account
                                   (caller holds none of those perms)        │
                                                                             └─ IamInstanceProfile creds via IMDS
                                                                                (IMDSv2 Deny on RunInstances NOT re-applied here)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Holder of `ec2:ModifyFleet`, **denied `ec2:RunInstances` + `iam:PassRole`** | A new EC2 instance running an `IamInstanceProfile` | `ModifyFleet(↑TargetCapacity)` → SLR issues `RunInstances` | An instance launches (and its profile creds become readable via IMDS) when the caller's own `RunInstances`/`PassRole` is `AccessDenied` |
| Holder of `ec2:ModifyFleet`, **denied `ec2:TerminateInstances`** | Running instances in the fleet | `ModifyFleet(↓TargetCapacity, ExcessCapacityTerminationPolicy=termination)` → SLR issues `TerminateInstances` | Instances terminate (Spot ones emit an interruption notice) when the caller's own `TerminateInstances` is `AccessDenied` |
| Holder of `ec2:ModifyFleet`, **no launch-template-write / PassRole** | Any launch template + overrides the fleet will launch next | `ModifyFleet(LaunchTemplateConfig.N = attacker template/version/overrides)` — UserGuide-undocumented param | Next capacity-replacement cycle launches instances with a profile/user-data the caller could not set via a PassRole-checked path |
| Caller IAM-restricted via `ec2:RunInstances` conditions (`ec2:LaunchTemplate`, IMDSv2 Deny, `aws:RequestTag`) | Launches outside that allowlist | Launch driven through `ModifyFleet(↑capacity)`; actual `RunInstances` is the SLR's; **no RunInstances condition keys exist on `ModifyFleet`** | A launch succeeds via ModifyFleet with properties the equivalent direct `RunInstances` denies (e.g. `HttpTokens=optional`) |
| Holder of `ec2:ModifyFleet` on `Resource:"*"` | Every `maintain` fleet in the account | `ModifyFleet` carries only `fleet*` (required) + optional `image`/`launch-template`/`subnet` resource types | A ModifyFleet against a fleet the holder does not "own"/tag succeeds (account-wide reach from a wildcard grant) |
| Low-privilege insider | Account's running capacity / On-Demand spend | `ModifyFleet(↑TargetCapacity)` up to 10,000/fleet, 100,000/Region (soft quotas) | Mass instance launch / quota exhaustion attributable to a ModifyFleet by a principal with no `RunInstances` |

**Hard-stop boundary:** any customer surface ↔ AWS's own service plane (the SLR's live credentials). Read-only only (`GetPolicyVersion`, `GetRole`).

---

## 4. API / Interface Inventory

| Name | Mutating | Facing | Functionality | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `ModifyFleet` | yes (Write) | external | Change `maintain` fleet: capacity, `ExcessCapacityTerminationPolicy`, **`LaunchTemplateConfig.N`**, **`Context`** | yes (SigV4) | principal with `ec2:ModifyFleet` | **Prime target.** Resource-scopable to `fleet/${FleetId}`; **no `instance` resource type**, so no `RunInstances`/IMDS/PassRole/Terminate condition keys apply. UserGuide documents only 2 of its parameters. |
| `DescribeFleets` / `DescribeFleetInstances` / `DescribeFleetHistory` | no | external | Read fleet config/state/instances/events (recon for which fleet to modify + which template it tracks) | yes | caller | Account-scoped. The recon that targets a ModifyFleet. |
| `CreateFleet` | yes | external | Create fleet (compare path) | yes | caller | Twin of ModifyFleet for the launch-trigger bypass (parent plan). |
| `DeleteFleets` | yes | external | Delete fleet (+ optionally terminate) | yes | caller | Alternate terminate primitive. |
| SLR launch/terminate (internal) | yes | internal | `RunInstances`/`TerminateInstances` the SLR performs on ModifyFleet's behalf | no | `ec2.amazonaws.com` only | Service plane — **read-only / hard stop.** Whether its own launches are internally condition-restricted is a doc-gap. |

**`ModifyFleet` IAM facts (Service Authorization Reference, mirror `list_ec2.md`):**
- Access level **Write**; required resource type **`fleet*`** (ARN `…:fleet/${FleetId}`).
- Condition keys on `fleet`: `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:Region`.
- Optional resource types: `image`, `launch-template`, `subnet` — **none carry `ec2:LaunchTemplate` or `ec2:IsLaunchTemplateResource`.**
- **No `instance` resource type** → none of `ec2:MetadataHttpTokens` / `ec2:MetadataHttpEndpoint` / `ec2:MetadataHttpPutResponseHopLimit` / `aws:RequestTag` (RunInstances controls) are expressible on `ModifyFleet`.

**Console-hidden knob (Step-3 lead, verbatim):** `API_ModifyFleet` request parameters = `Context`, `DryRun`, `ExcessCapacityTerminationPolicy`, `FleetId` (required), **`LaunchTemplateConfig.N`** (0–50, Required: No), `TargetCapacitySpecification`. The UserGuide `modify-ec2-fleet` page documents **only** `target-capacity-specification` and `excess-capacity-termination-policy`. `LaunchTemplateConfig` and `Context` are **accepted by the API/CLI but never surfaced in the UserGuide prose** — the exact "reference accepts but prose docs do not" delta the method says to hunt.

---

## 5. Recommended Areas of Focus (priority order)

Priority = (privilege-granularity gap confirmable with the safe oracle) > (console-hidden launch-template redirect → privesc) > (RunInstances-control bypass via the modify path) > (cost/availability DoS) > (doc-vs-reality / audit).

### 5.1 ModifyFleet is a launch/terminate primitive that routes around `RunInstances` / `PassRole` / `TerminateInstances` — **P0**
**Background:** The instance launches (scale-up) and terminations (scale-down + `termination`) that ModifyFleet triggers are performed by `AWSServiceRoleForEC2Fleet`, not the caller. ModifyFleet's IAM entry has **no `instance` resource type**, so the caller is never authorization-checked for `RunInstances`, `iam:PassRole`, or `TerminateInstances`.
**Security Concern (Lens E / X):** A principal granted only `ec2:ModifyFleet` — and *explicitly denied* `RunInstances`, `PassRole`, and `TerminateInstances` — can still (a) cause instances to launch and (b) **force-terminate running instances** (availability impact), both without the permission that nominally governs those actions. This is a privilege-granularity gap: ModifyFleet silently confers launch+terminate.
**High-level Test Scenarios:**
- `SimulatePrincipalPolicy`: confirm the scoped principal is `ALLOW ec2:ModifyFleet` on the fleet ARN, `DENY ec2:RunInstances` / `iam:PassRole` / `ec2:TerminateInstances`.
- Canary (throwaway `maintain` fleet, target 1): as that principal, `ModifyFleet(TotalTargetCapacity=2)` → confirm a 2nd instance launches. Then `ModifyFleet(TotalTargetCapacity=1, ExcessCapacityTerminationPolicy=termination)` → confirm an instance is terminated. Both succeeding = breach of the granularity assumption.
- Record whether the terminated instance emits a Spot interruption notice (expected for Spot).
**Doc evidence:** `modify-ec2-fleet.md` (termination behavior + capacity considerations); `ec2-fleet-prerequisites.md` SLR grant list; `list_ec2.md` ModifyFleet row (no `instance` resource type). **Severity-if-true:** High (unprivileged launch + forced-termination availability primitive inside the account). **Stop condition:** +1/−1 on a canary fleet only; never touch a real workload's capacity.

### 5.2 Console-hidden `LaunchTemplateConfig` on ModifyFleet → launch-template redirect → PassRole-less role injection — **P0**
**Background:** The API/CLI accept `LaunchTemplateConfig.N` on `ModifyFleet`, but the UserGuide page documents only capacity + termination policy. So ModifyFleet can **re-point a `maintain` fleet at a different launch template / version / set of overrides**, which the next capacity-replacement cycle will launch.
**Security Concern (Lens U + B + parent §5.1/§5.4):** A holder of `ec2:ModifyFleet` with **no launch-template-write and no `iam:PassRole`** could swap in a template (or version/override) carrying an arbitrary `IamInstanceProfile` and/or `UserData`, and have the SLR launch instances as that role — code-exec-as-role with no PassRole-checked path. Because the `launch-template` resource type on ModifyFleet is **optional (not required)**, a policy scoped only to the `fleet` ARN may not force any check against the specific launch-template ARN being substituted.
**High-level Test Scenarios:**
- Confirm the surface: `aws ec2 modify-fleet help` / API model — does `--launch-template-configs` on ModifyFleet accept `Overrides` with `IamInstanceProfile` / `UserData` / `MetadataOptions`, or only instance-type/subnet/price/weighting? **(doc-gap — resolve first.)** If overrides are limited to selection knobs, the redirect still works by pointing at a *different launch template* the attacker authored.
- `SimulatePrincipalPolicy` for `ec2:ModifyFleet` with `Resource` scoped to `fleet/X` only → confirm it does **not** also require/evaluate the launch-template ARN condition.
- Canary: fleet tracking benign template A → `ModifyFleet(LaunchTemplateConfig = template B with a privileged/instrumented profile)` → trigger a replacement → confirm new instance carries B's profile. Terminate immediately.
**Doc evidence:** `API_ModifyFleet.md` (`LaunchTemplateConfig.N`); `modify-ec2-fleet.md` (silent on it); `list_ec2.md` (launch-template optional on ModifyFleet); parent plan §5.1/§5.4. **Severity-if-true:** Critical (intra-account privilege escalation to an arbitrary role; cross-account if the injected role is trusted elsewhere). **Stop condition:** sandbox/canary only; stop the moment a non-synthetic profile would be assumed.

### 5.3 `RunInstances`-scoped controls bypassed by driving the launch through ModifyFleet — **P1**
**Background:** AWS's governance controls (IMDSv2-enforcement Deny, "restrict to one launch template" via `ec2:LaunchTemplate`/`ec2:IsLaunchTemplateResource`, `aws:RequestTag` ABAC) are written against `ec2:RunInstances` and evaluated against the **calling** principal. ModifyFleet's launch is issued by the SLR, and **none of those condition keys exist on `ModifyFleet`** (no `instance` resource type).
**Security Concern (Lens X — twin-path parity):** The IMDSv2 Deny that stops a direct `RunInstances {HttpTokens:optional}` does not re-apply when the same launch is produced by `ModifyFleet(↑capacity)` tracking a template whose `MetadataOptions.HttpTokens=optional`. Likewise a "launch only from template A" restriction is defeated by substituting template B via §5.2. This re-arms IMDSv1 → SSRF-to-IMDS credential theft on the launched instance.
**High-level Test Scenarios:** Attach each sample control to a scoped principal. Perform the restricted launch once directly (`RunInstances` → expect `AccessDenied`) and once via `ModifyFleet(↑capacity)` on a fleet whose template violates the control (breach if the instance launches with the forbidden property). Verify the launched instance's IMDS/tag state matches the forbidden config.
**Doc evidence:** parent plan §5.3; `list_ec2.md` (absence of RunInstances condition keys on ModifyFleet); `ec2-fleet-prerequisites.md` (SLR issues RunInstances). **Severity-if-true:** High (undermines IMDSv2 / template / tag governance; chains to credential theft).

### 5.4 Cost / quota-exhaustion and capacity-accounting drift via ModifyFleet — **P2**
**Background:** `fleet-quotas.md`: target capacity **per fleet = 10,000**, **per Region = 100,000** (both soft `¹` quotas, increasable). ModifyFleet sets target capacity directly. Capacity Rebalance (`ec2-fleet-capacity-rebalance.md`) does **not** count rebalance-flagged instances toward fulfilled capacity and can run "until fulfilled capacity is double target capacity," and a scale-in does **not** terminate rebalance-flagged instances ("You need to manually terminate these instances").
**Security Concern (Lens L / U):** A principal with only `ec2:ModifyFleet` can drive a single `maintain` fleet toward 10,000 units → mass launch / On-Demand quota exhaustion / cost impact, without `RunInstances`. Separately, the Capacity-Rebalance accounting divergence means actual running capacity can diverge from the nominal target by up to 2×, an operational-drift primitive (not framed as a security issue in docs). Single-account, so primarily an insider/least-privilege-footgun and self-DoS — rated accordingly.
**High-level Test Scenarios:** On a canary fleet, confirm ModifyFleet accepts a large target (bounded by the quota) from a principal lacking `RunInstances` — assert via `DescribeFleets` without actually launching thousands (set target slightly above current by 1 and read the pending launch intent, or use `DryRun` if supported). Confirm the rebalance scale-in leaves excess instances running per the documented example.
**Doc evidence:** `fleet-quotas.md`; `ec2-fleet-capacity-rebalance.md`. **Severity-if-true:** Medium (cost/availability via a permission that doesn't look like a launch permission); Low where it is pure self-DoS. **Stop condition:** never actually scale into real quota; +1 and read intent only.

### 5.5 State-machine concurrency & doc-vs-reality / audit — **P3 (informational, enablers)**
- **`modifying`-state concurrency (doc-gap):** `modify-ec2-fleet.md` names only `submitted`/`active` as valid *starting* states; `EC2-fleet-states.md` describes `modifying` but **says nothing about overlapping ModifyFleet calls** — rejected, queued, or raced? A TOCTOU window between "read target" and "apply target" during `modifying` is unconfirmed. Resolve before claiming any race.
- **`$Latest`/`$Default` re-resolution timing (doc-gap, gates §5.2/§5.3):** no fleet page states whether a `maintain` fleet re-resolves the launch-template version at each new-instance launch or pins it at `CreateFleet`. ModifyFleet is the cleanest *trigger* to test this, since §5.2 can also substitute the config directly.
- **SLR internal condition-restriction (doc-gap, service plane / read-only):** `security-iam-awsmanpol.md` links out to the managed-policy reference rather than printing `AWSEC2FleetServiceRolePolicy` inline — whether the SLR's own `RunInstances` is internally conditioned (e.g. only from fleet-owned templates) is unconfirmed. Resolve with read-only `iam:GetPolicyVersion`; **do not** exercise the SLR.
- **Audit:** ModifyFleet on a `maintain` fleet is expected to emit EventBridge/CloudTrail (only `maintain` is modifiable, and EventBridge covers `maintain`/`request`), so the §5.2 redirect is *not* in the "instant fleets emit no events" blind spot — note this as a defender advantage, and confirm the EventBridge event actually records the substituted `LaunchTemplateConfig`.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Launch instances with only `ec2:ModifyFleet` (no RunInstances/PassRole) | ModifyFleet → SLR launch path | SLR grant model; ModifyFleet has no `instance` resource type (so no RunInstances-side gate on the caller) |
| Force-terminate running instances with only `ec2:ModifyFleet` (no TerminateInstances) | ModifyFleet(↓capacity, termination) → SLR terminate | `excess-capacity-termination-policy`; allocation-strategy selection — no caller TerminateInstances check |
| Redirect fleet to attacker launch template / overrides | ModifyFleet `LaunchTemplateConfig.N` (UserGuide-undocumented) | None documented; launch-template resource type is *optional* on ModifyFleet |
| IMDSv2 / template / tag control bypass via the modify launch path | ModifyFleet vs RunInstances condition-key parity | IMDSv2 Deny / `ec2:LaunchTemplate` / `aws:RequestTag` on RunInstances (absent on ModifyFleet) |
| Cost/quota exhaustion by scaling a maintain fleet | ModifyFleet target capacity vs fleet quotas | 10,000/fleet, 100,000/Region soft quotas (no per-principal launch gate) |
| Account-wide fleet reach from a wildcard grant | `ec2:ModifyFleet` `Resource:"*"` | `fleet/${FleetId}` resource-level + `ec2:ResourceTag` scoping (available but often unused) |
| Overlapping ModifyFleet race in `modifying` state | Fleet state machine | None documented (doc-gap) |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-tenant / cross-account IDOR on fleets or instances** — N/A: a fleet, its instances, and the SLR all live in the caller's own account; `ModifyFleet` targets a `fleet/${FleetId}` in the caller's account. (Cross-account trust lives in the *KMS grant* and *shared capacity reservation* surfaces — see parent plan §5.5/§5.6, not reachable through ModifyFleet itself.)
- **AWS service-plane / SLR live credentials** — hard stop; read-only (`GetPolicyVersion`, `GetRole`) only.
- **Single-tenant self-DoS / cost footguns** a caller inflicts on *their own* fleet via legitimate capacity knobs — out of scope *except* where a principal that provably lacks `RunInstances`/`TerminateInstances` achieves launch/terminate/cost impact through ModifyFleet (that is the in-scope granularity gap, §5.1/§5.4).
- **Customer-authored** least-privilege mistakes (an over-broad `ec2:ModifyFleet` the customer wrote) — a footgun, lower priority; the in-scope defect is that ModifyFleet *structurally* lacks the condition keys to express the control (§5.3).
- **SSRF, wire-protocol/translation injection, prompt injection, attestation gating, canonicalization/parser-differential, cache-key divergence, trusted-header injection, JWT/token validation** — N/A for this surface (see §8).

---

## 8. Null Hypotheses / Doc Gaps (lenses that did not fire, pages checked)

- **Lens A (cross-tenant IDOR):** N/A — `modify-ec2-fleet.md`, `manage-ec2-fleet.md`, `EC2-fleet-states.md`, `list_ec2.md`: ModifyFleet targets a `fleet` ARN in the caller's own account; no multi-tenant resource. The intra-account "wildcard grant → any fleet" reach (§5 trust map) is a scoping risk, not a cross-tenant bug.
- **Lens F (injection/translation):** N/A — ModifyFleet inputs are integers (`TargetCapacitySpecification`), an enum (`ExcessCapacityTerminationPolicy`), structured `LaunchTemplateConfig`, and an opaque `Context` token; no free-text query language or parser. Checked `API_ModifyFleet` + CLI reference.
- **Lens G (SSRF):** N/A — reviewed `modify-ec2-fleet.md`, `API_ModifyFleet`, CLI reference; no URL/URI/webhook/callback field the service dereferences on behalf of this call.
- **Lens H (KMS/encryption-context):** not reachable *through ModifyFleet* — any CMK use happens inside the SLR's downstream launch; the KMS-grant over-scope lead lives in parent plan §5.5.
- **Lenses K / W / BB / CC / DD / FF (prompt-injection / attestation / canonicalization / trusted-header / cache-key / token-validation):** N/A — no LLM/agent, no enclave/`kms:RecipientAttestation`, no authorizer/WAF/CDN/cache layer, no JWT/OIDC in front of this SigV4 control-plane API.
- **Lens O (audit):** `maintain` is the only modifiable type and is covered by EventBridge/CloudTrail → ModifyFleet is **not** in the "`instant` emits no events" blind spot; confirm the event records the substituted `LaunchTemplateConfig` (§5.5).

**Load-bearing doc-gaps to resolve before calling anything confirmed:**
1. Does a `maintain` fleet re-resolve `$Latest`/`$Default` **per new-instance launch**, or pin the version at `CreateFleet`? (gates §5.2/§5.3) — no fleet page states it; grep of the mirror for `$Latest`/`$Default` near fleet docs returned zero hits.
2. Does `ModifyFleet`'s `LaunchTemplateConfig.Overrides` accept `IamInstanceProfile` / `UserData` / `MetadataOptions`, or only selection knobs (instance type / subnet / price / weighting)? (decides whether §5.2 needs an attacker-authored template vs an inline override) — resolve from the `FleetLaunchTemplateConfigRequest` / `FleetLaunchTemplateOverridesRequest` API model.
3. Is the SLR's own `RunInstances` internally condition-restricted (e.g. to fleet-owned templates)? (gates §5.2/§5.3 severity) — `AWSEC2FleetServiceRolePolicy` not printed inline; resolve with read-only `iam:GetPolicyVersion`.
4. Are overlapping `ModifyFleet` calls in the `modifying` state rejected, queued, or raced? (gates any §5.5 TOCTOU claim) — no concurrency language in `EC2-fleet-states.md`.
5. On a `TotalTargetCapacity`/`OnDemandTargetCapacity` decrease with `termination`, are **On-Demand** instances force-terminated and, if so, by what selection rule? The per-strategy termination list in `modify-ec2-fleet.md` is written only in Spot terms. (refines §5.1 severity for On-Demand)

---

### Kill-chain candidates (rate at the end of the chain)
- **Recon** (`DescribeFleets`/`DescribeFleetInstances` → find a `maintain` fleet and the privileged `IamInstanceProfile` its template carries) → **§5.2** (`ModifyFleet` `LaunchTemplateConfig` substitutes a template/override, or §5.1 scales up to force a fresh launch) → **code-exec as that profile's role** via IMDS → if that role can read a CMK or reach a shared Capacity Reservation, chain into **parent §5.5 / §5.6**. **End severity: Critical** (intra-account privesc, potentially cross-account via KMS/CR trust), achieved from a principal holding only `ec2:ModifyFleet`.
- **§5.3 IMDSv2 downgrade** (ModifyFleet-driven launch tracking `HttpTokens=optional`) → IMDSv1 reachable → SSRF-to-IMDS credential theft of the launched role. **End severity: High.**
