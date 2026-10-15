# EC2 Spot Fleet — Lifecycle / Request-State Attack Research Plan

**Source of leads:** AWS EC2 User Guide, anchored on `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-states.html` (the Spot Fleet request **state machine**) and its lifecycle neighborhood (`work-with-spot-fleets`, `create-spot-fleet`, `modify-spot-fleet`, `cancel-spot-fleet`, `manage-spot-fleet`, `spot-fleet-automatic-scaling`, `spot-fleet-auto-scaling-IAM`, `tag-spot-fleet`, `spot-fleet-prerequisites`, `fleet-quotas`), the EC2 API Reference (`API_RequestSpotFleet`, `API_ModifySpotFleetRequest`, `API_CancelSpotFleetRequests`, `API_DescribeSpotFleetRequests`, `API_DescribeSpotFleetInstances`, `API_DescribeSpotFleetRequestHistory`), the IAM **Service Authorization Reference** (`https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html` — note: the legacy `list_amazonec2.html` slug now 302-redirects to a JS shell; use `list_ec2.html`/`list_ec2.md`), the AWS-managed policy `AWSEC2SpotFleetServiceRolePolicy` (v4) and `AmazonEC2SpotFleetTaggingRole`, and the KMS-grant runbook in `spot-fleet-prerequisites`.
Offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`. **Online `.md` twins cross-checked** (append `.md` to any `.html` page); `spot-fleet-states` and all lifecycle pages matched. No sync gaps found on the audited lifecycle pages.
**Status:** Documentation-derived hypotheses only. **Nothing in this plan has been tested against a live AWS account.** It is the plan a hunter (e.g. `aws-vuln-hunter`) executes next.
**Produced by:** `security-questionbuilder` skill — orchestrator pass on the state machine + 3 parallel documentation-only deep-analysis subagents (control-plane API/IAM-authz surface; revocation/orphan completeness; state-transition races / scaling-guardrail / quota DoS).

> **Relationship to the sibling plans.** This is the **lifecycle/state-machine companion** to `spot-fleet-attack-research-plan.md` (the broad Spot Fleet plan) in this directory, which itself leans on `ec2-fleet-attack-research-plan.md`. For the **IAM-artifact privilege-escalation** depth — SLR wildcard `iam:PassRole`, the copy-verbatim `aws-ec2-spot-fleet-tagging-role`'s unconditioned `RunInstances`/`TerminateInstances`/`CreateTags` on `*`, the cross-account `IamFleetRole` confused-deputy chain (`B1`), the user sample policy's optional `CreateRole`/`AttachRolePolicy` self-escalation block (`S3`), ELB target insertion (`S2`), and the Config-rule blind spot (`H1`) — **read the broad plan first; those leads are not re-derived here.** This plan concentrates on what the **state machine itself** (`submitted → active ⇄ modifying → cancelled_running/cancelled_terminating → cancelled`) exposes: lifecycle-API authorization scoping, state-transition integrity, revocation/orphan completeness, quota-driven DoS, and the forensic decay built into the `cancelled` state.

---

## 0. How to use this document

- Each lead is a falsifiable claim: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in the priority order of §5. Look left and right for adjacent bugs.
- **Prefer the safe oracle first.** Almost every lead here is confirmable **before touching a live resource** with `iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy`, read-only `iam:GetPolicyVersion` / `iam:GetRole` / `kms:ListGrants` / `ec2 describe-*` / `elbv2 describe-target-health` / `service-quotas get-service-quota`, and `aws ... --dry-run`. **Caveat (confirmed from the API docs):** `DryRun` on every Spot Fleet action checks **IAM permission only** (`DryRunOperation` vs `UnauthorizedOperation`), **not** request state or type — so a dry-run can *never* surface a state/type-precondition error. State-enforcement leads (SF-13, SF-14) therefore require a real call against a synthetic canary fleet in an account you are authorized to test; the call does not mutate if the service rejects it.
- **This service runs entirely inside the customer's own account.** There is no multi-tenant service fleet and no customer-reachable data plane. The lifecycle "service" is the control-plane API plus the service-linked roles that call `RunInstances`/`TerminateInstances`/`RegisterTargets`/`CreateTags` on your behalf. Classic **cross-tenant** surface is therefore thin (documented null in §8); the real value is **intra-account cross-team control-plane abuse**, **revocation-completeness gaps on AWS-authored artifacts**, and **lifecycle-driven DoS**.
- **HARD STOP:** The only true AWS-service-plane identities in scope are the service principal `spotfleet.amazonaws.com` and the service-linked roles `AWSServiceRoleForEC2SpotFleet`, `AWSServiceRoleForEC2Spot`, and `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest`. Treat them read-only. The moment any evidence shows you have reached, assumed, or extracted credentials/ARNs belonging to AWS's own fleet/service plane, **stop, preserve evidence, flag for AWS-Security disclosure.**

---

## 1. Pentest Objectives (concrete breach outcomes to attempt)

1. **Cross-team control-plane takeover of a fleet you do not own:** holding only AWS's documented Spot-Fleet-operator sample policy, **cancel-and-terminate** (or capacity-zero) another team's production `maintain` fleet, and **read its full config** (IamFleetRole ARN, subnets, AMIs, launch spec) — all within one account, with no IAM-native way for the victim team to stop you.
2. **Scaling-guardrail bypass:** as a principal granted the AWS auto-scaling sample policy, call `ec2:ModifySpotFleetRequest` **directly** to push a fleet's target capacity above the Application-Auto-Scaling-configured `MaxCapacity` (cost blowout) or to 0 (outage), bypassing the guardrail that lives only in Application Auto Scaling.
3. **Victim-fleet availability DoS via CloudWatch:** disable/delete the scale-out alarm or overwrite the scale-in alarm of a fleet you do not own, using the `cloudwatch:*` on `Resource:"*"` the auto-scaling sample policy grants.
4. **Account-wide Spot-Fleet DoS via quota exhaustion:** cheaply occupy the shared Region quota (1,000 fleets in `active`/`cancelled_running`) with `TargetCapacity=0` fleets so every other principal's new `RequestSpotFleet` auto-cancels on `submitted`.
5. **Durable decryption primitive via a surviving KMS grant:** confirm the SLR's CMK grant (including `CreateGrant`) is **not** retired when the fleet is cancelled/deleted or the SLR is deleted.
6. **Persistence + anti-forensics via `cancelled_running`:** cancel-without-terminate to orphan running (and still load-balanced, still fleet-tagged) instances, then let the request + its 48-hour history self-delete so EC2-native tooling can no longer reconstruct what the orphan was launched with.
7. **State-machine integrity:** confirm whether the "`maintain`-only / `active`-only" modify preconditions are server-enforced or prose-only, and whether concurrent modify/cancel on a `modifying` fleet races.

---

## 2. Components, Assets, and Design

**What it is.** Spot Fleet is a console-supported, API/CLI-drivable orchestration layer that launches and *maintains* a mixed Spot + On-Demand fleet in the **caller's own account/VPC**. It is the legacy twin of EC2 Fleet (`CreateFleet`), explicitly "legacy API with no planned investment." The request moves through a documented **state machine**; the states — not the launch spec — are this plan's subject.

**The state machine (verbatim from `spot-fleet-states`):**
- `submitted` — being evaluated; **"If a request would exceed your Spot Fleet quotas, it is canceled immediately."**
- `active` — validated; EC2 maintains target capacity; stays here "until it is modified or canceled."
- `modifying` — modification in flight; **only a `maintain` fleet reaches it**; "remains in this state until the modification is fully processed **or the request is canceled**."
- `cancelled_running` — request cancelled/deleted but **"existing instances continue to run until they are interrupted or terminated manually."**
- `cancelled_terminating` — request cancelled, instances terminating.
- `cancelled` — no running instances; **"The request is deleted two days after its instances are terminated."** (API ref: "deleted 48 hours after they are canceled and their instances are terminated.")

**Customer-facing interface.** SigV4 EC2 Query/SDK APIs + the EC2 console "Spot Requests" screen. No non-SDK/internal endpoint. No customer-reachable data plane.

**Identity / roles.** (Depth in the broad plan §2.)
- `AWSServiceRoleForEC2SpotFleet` (SLR, `AWSEC2SpotFleetServiceRolePolicy` v4) — launches/terminates/tags/registers instances on your behalf. Its `ec2:TerminateInstances` is on `Resource:"*"` conditioned only `StringLike ec2:ResourceTag/aws:ec2spot:fleet-request-id : "*"` (tag-**key presence**, any value). It has `RegisterTargets`/`RegisterInstancesWithLoadBalancer` but **no `Deregister*`**.
- `aws-ec2-spot-fleet-tagging-role` (customer-passed `IamFleetRole`; AWS-managed policy `AmazonEC2SpotFleetTaggingRole`) — copy-verbatim artifact; default trust has **no** `aws:SourceArn`/`aws:SourceAccount` (confused-deputy hardening is only *recommended*).
- `AWSServiceRoleForApplicationAutoScaling_EC2SpotFleetRequest` — modifies the fleet's target capacity on your behalf when auto-scaling is enabled.
- End-user operator principal — holds the **AWS-published sample policy** (`spot-fleet-prerequisites` and/or `spot-fleet-auto-scaling-IAM`), both using `Resource:"*"`. **Primary attack surface of this plan.**

**Resource identifiers.** Spot Fleet request IDs `sfr-` + 8-4-4-4-12 hex (UUIDv4-shaped, ~122-bit; **not enumerable** — inference from the uniform example format, not a documented guarantee). The IAM `spot-fleet-request` resource ARN is `arn:${Partition}:ec2:${Region}:${Account}:spot-fleet-request/${SpotFleetRequestId}`.

**Lifecycle-relevant knobs.** `TargetCapacity` / `OnDemandTargetCapacity` (plain integers, capped only by the 10,000 per-fleet quota), `ExcessCapacityTerminationPolicy` (`noTermination|default`), `TerminateInstances` (required boolean on cancel), `TerminateInstancesWithExpiration` + valid-from/valid-until window, instance **weighting** (fulfilled capacity is a float rounded **up**), and the auto-scaling min/max which lives in **Application Auto Scaling**, not EC2. `Context` on `RequestSpotFleet`/`ModifySpotFleetRequest` is documented only as **"Reserved."** — an undocumented field worth probing.

```
 Operator principal (AWS sample policy, Resource:"*")
   │  RequestSpotFleet ─────────────► submitted ──(quota exceeded)──► cancelled (immediate)
   │  (passes IamFleetRole ARN)             │ validated
   │                                        ▼
   │  ModifySpotFleetRequest ────────►   active  ⇄  modifying     (maintain type only)
   │  (direct — bypasses AAS min/max)       │
   │  CancelSpotFleetRequests ──────────────┤
   │     --terminate-instances ─────────────┼──► cancelled_terminating ──► cancelled ──(48h)──► DELETED
   │     --no-terminate-instances ──────────┴──► cancelled_running  ───────► (instances run on, orphaned,
   │                                                 still tagged aws:ec2spot:fleet-request-id,
   │                                                 still registered in target group, no managing fleet)
   │
   ├─ Application Auto Scaling ──► SLR modifies TargetCapacity within Min/MaxCapacity  (guardrail lives HERE, not in EC2)
   ├─ CloudWatch alarms (TargetTracking-sfr-<id>-AlarmHigh/Low)  ◄── auto-scaling sample policy: cloudwatch:* on *
   └─ KMS grant to SLR (Decrypt+Encrypt+GenerateDataKey+CreateGrant+ReEncrypt*)  ── no documented RetireGrant on cancel/delete
```

---

## 3. API / Interface Inventory (lifecycle actions)

Columns derived from the IAM Service Authorization Reference (`list_ec2.md`) and the API Reference. **The resource/condition-key column is the key correction over the broad plan** (see SF-2/SF-3).

| Name | Mutating | IAM resource type (required) | Condition keys supported | State/type precondition | Notes |
|---|---|---|---|---|---|
| `RequestSpotFleet` | Yes | `spot-fleet-request*` (+ image/key-pair/launch-template/subnet/etc. it references) | `aws:RequestTag`, `aws:TagKeys`, `ec2:Region` (creation action) | — | `IamFleetRole` passed in; `Context`=Reserved; quota-exceeded → immediate cancel |
| `ModifySpotFleetRequest` | Yes | `spot-fleet-request*` (+ launch-template/subnet if used) | `aws:ResourceTag/${k}`, `ec2:ResourceTag/${k}`, `ec2:Attribute`, `ec2:Attribute/${name}`, `ec2:Region` | **"only type `maintain`"** — prose only, no API error code | Also in auto-scaling policy; sets absolute `TargetCapacity` |
| `CancelSpotFleetRequests` | Yes | `spot-fleet-request*` | `aws:ResourceTag/${k}`, `ec2:ResourceTag/${k}`, `ec2:Region` | ≤100 per call, atomic ("exceed → none deleted") | `TerminateInstances` **required**; per-ID success/unsuccess split |
| `DescribeSpotFleetRequests` | No | **none (blank)** | **`ec2:Region` only** | — | **Cannot be resource-scoped at all** — returns full config of every fleet in account/region |
| `DescribeSpotFleetInstances` | No | `spot-fleet-request*` | `aws:ResourceTag/${k}`, `ec2:ResourceTag/${k}`, `ec2:Region` | single `sfr-` | *Can* be tag/ARN-scoped (unlike its sibling above) |
| `DescribeSpotFleetRequestHistory` | No | `spot-fleet-request*` | `aws:ResourceTag/${k}`, `ec2:ResourceTag/${k}`, `ec2:Region` | single `sfr-` | Events delayed ≤30 s, **retained 48 h** |
| `register-scalable-target` / `put-scaling-policy` (Application Auto Scaling) | Yes | AAS scalable-target | AAS keys | min/max set here | The **only** place the capacity guardrail is enforced |

**Doc-flagged pointers kept verbatim:** "Resource-level permissions are not currently supported for the `spot-fleet-request` resource … you will get an unauthorized exception when you try to tag the fleet" (`tag-spot-fleet`, about `ec2:CreateTags`) — **contradicts** the Service Authorization Reference's resource-type support for `Modify`/`Cancel`/`Describe*Instances`/`History` (→ SF-3). "If a request would exceed your Spot Fleet quotas, it is canceled immediately" (`spot-fleet-states`). "The request is deleted two days after its instances are terminated" (`spot-fleet-states`). "`Context` … Reserved." (`API_ModifySpotFleetRequest`/`API_RequestSpotFleet`).

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle (what proves it broke) |
|---|---|---|---|
| Operator principal (team A, sample policy) | Team B's `sfr-` fleet (same account) | `Modify`/`Cancel`/`DescribeSpotFleetRequests` on `Resource:"*"` | A `SimulatePrincipalPolicy` showing `allowed` for Cancel/Modify against team B's fleet ARN = **cross-team control-plane breach** (SF-1/SF-2) |
| Operator granted auto-scaling policy | Another fleet's registered capacity bound | direct `ModifySpotFleetRequest` (not via AAS) | Target capacity set outside the AAS `Min/MaxCapacity` = **guardrail bypass** (SF-5) |
| Operator granted auto-scaling policy | Another fleet's CloudWatch alarms | `cloudwatch:DeleteAlarms`/`PutMetricAlarm` on `*` | Deleting/overwriting `TargetTracking-sfr-<otherid>-*` = **victim availability DoS** (SF-6) |
| Any low-priv Spot-Fleet creator | Every other principal's ability to launch a fleet | shared Region quota + immediate-cancel-on-submit | Victim `RequestSpotFleet` auto-cancels while attacker holds 1,000 `TargetCapacity=0` fleets = **account-wide DoS** (SF-4) |
| Cancelled fleet (dead parent) | Still-running orphan instance + its CMK grant + its TG registration | missing teardown on `cancelled_running`/delete | Grant still in `kms:ListGrants`; instance still in `describe-target-health`; tag still present after request `NotFound` = **revocation-incompleteness** (SF-8/9/10) |
| Any Spot Fleet instance lifecycle | AWS's own fleet/service plane | SLR assumes `spotfleet.amazonaws.com` role | Any AWS-owned credential/ARN surfaced = **hard stop, disclose** |

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — Lifecycle-API authorization scoping (HIGHEST YIELD, read-only confirmable)
*Lenses S / U / A. The whole point of the state machine is reached through these six APIs; AWS's own sample policy makes them account-wide.*

**SF-1 — `DescribeSpotFleetRequests` cannot be IAM-scoped at all.**
**Claim:** Any principal holding `ec2:DescribeSpotFleetRequests` can read the **full configuration** (`IamFleetRole` ARN, subnet IDs, AMI IDs, launch specs, tags) of **every** Spot Fleet in the account/region; a security team **cannot** restrict it to "fleets I own" via IAM, because the action supports **no resource type** and only the `ec2:Region` condition key.
**Mechanism:** Service Authorization Reference `list_ec2.md` — `DescribeSpotFleetRequests` row has a **blank** "Resource types" cell and only `ec2:Region`; contrast `DescribeSpotFleetInstances`/`DescribeSpotFleetRequestHistory`, which require `spot-fleet-request*` and support `aws:ResourceTag`/`ec2:ResourceTag`. `API_DescribeSpotFleetRequests` takes an optional `SpotFleetRequestId.N` filter but **no owner filter** ("Describes your Spot Fleet requests").
**Confirm/Refute oracle:** `iam:SimulatePrincipalPolicy` for `ec2:DescribeSpotFleetRequests` while attempting a `Resource` ARN of one specific fleet → the scoping is a no-op, returns `allowed` regardless. Fully offline against the sample policy text; zero resources touched.
**Preconditions / Cost:** operator holds the sample read permission; one simulate. **Severity-if-true:** High (intra-account cross-team config disclosure; **no IAM-native mitigation** — only SCP/OU or a wrapper API). **Owner-to-fix:** AWS (missing resource-level support) + customer (SCP). **Stop:** read-only; do not pivot into the disclosed fleets.

**SF-2 — AWS's own sample policy grants account-wide Modify/Cancel despite ARN+tag scoping being available.**
**Claim:** `ec2:ModifySpotFleetRequest` and `ec2:CancelSpotFleetRequests` **do** support the `spot-fleet-request` resource type and `aws:ResourceTag`/`ec2:ResourceTag` conditions — yet the canonical, copy-pasteable sample policy in `spot-fleet-prerequisites` (and `spot-fleet-auto-scaling-IAM`) grants them on `Resource:"*"`. A shop that follows AWS's documented instructions verbatim gives any Spot-Fleet operator the power to **cancel-and-terminate or capacity-zero every other team's production fleet** in the account.
**Mechanism:** `list_ec2.md` shows the resource/condition-key support (table in §3); `spot-fleet-prerequisites` §"Grant permission to users" prints the `Resource:"*"` block with "grants a user the permissions required for most Spot Fleet use cases" and **no** scoped variant anywhere on the page. The only `spot-fleet-request/sfr-*` ARN scoping shown in the docs is in the tagging-role **trust** policy (confused-deputy mitigation), which constrains the *service*, not the operator.
**Confirm/Refute oracle:** `iam:SimulatePrincipalPolicy` with the verbatim sample policy as input, action `ec2:CancelSpotFleetRequests` / `ec2:ModifySpotFleetRequest`, resource = a *different* (synthetic) team's fleet ARN → expect `allowed`. Pure policy-artifact test, no live resources. Live confirmation (optional): a `--dry-run CancelSpotFleetRequests` naming a canary "other team" fleet returns `DryRunOperation` (auth passes).
**Preconditions / Cost:** sample policy attached; one simulate. **Severity-if-true:** High (intra-account cross-team, **control-plane blast radius** = mass termination, not just read). Not cross-account (confirmed no mechanism), so capped below Critical. **Owner-to-fix:** AWS-published sample policy is in scope per the Lens R carve-out (uneditable/copy-verbatim guidance) — recommend AWS ship a tag-scoped sample. **Stop:** confirm `allowed`; do not cancel a real foreign fleet.

**SF-3 — Doc-vs-doc contradiction: does resource-scoped Modify/Cancel actually work, or fail closed like CreateTags?** *(Lens U / X)*
**Claim:** `tag-spot-fleet` states resource-level permissions are **not** supported for `spot-fleet-request` ("you will get an unauthorized exception"), but that is demonstrated only for `ec2:CreateTags`. The Service Authorization Reference lists `spot-fleet-request*` as a **required** resource for `Modify`/`Cancel`/`DescribeSpotFleetInstances`/`History`. If, in reality, those actions **also** reject a resource-scoped ARN at runtime (as `CreateTags` does), then a customer who *tries* to harden away SF-2 by scoping the policy gets a fail-closed policy that breaks their tooling — pushing them back to `Resource:"*"`. That is a Lens-U "documented capability the service does not actually honor" gap and the mechanism that makes SF-1/SF-2 sticky.
**Mechanism:** the contradiction between `tag-spot-fleet` (unsupported) and `list_ec2.md` (supported) for the same resource type.
**Confirm/Refute oracle:** attach a canary policy scoping `ec2:ModifySpotFleetRequest` to one `spot-fleet-request/sfr-<canary>` ARN; `--dry-run ModifySpotFleetRequest` against (a) that fleet → expect `DryRunOperation`, (b) a different fleet → expect `UnauthorizedOperation`. If (a) returns `UnauthorizedOperation` too, the resource scoping is a no-op/fail-closed → confirmed Lens-U gap. Safe (dry-run, canary fleets).
**Severity-if-true:** Medium (doc-vs-reality; elevates SF-1/SF-2 to "no working fix exists"). **Owner-to-fix:** AWS.

### Area 2 — Scaling-guardrail bypass & CloudWatch DoS (auto-scaling path)
*Lens L / P / BB. The guardrail is in Application Auto Scaling; the raw EC2 lever and the alarms are granted account-wide alongside it.*

**SF-4 — Account-wide Spot-Fleet DoS via shared-quota exhaustion.**
**Claim:** The quota "fleets of type `maintain`/`request` in `active`, `deleted_running`/`cancelled_running` states = **1,000 per Region**" is **account-scoped, not per-principal**. A single low-priv principal can hold 1,000 `maintain` fleets at `TargetCapacity=0` (near-zero cost, explicitly supported) and thereby make **every other principal's** new `RequestSpotFleet` auto-cancel immediately on `submitted` ("If a request would exceed your Spot Fleet quotas, it is canceled immediately"). `cancelled_running` still counts toward the quota; only terminating the instances (`cancelled_terminating`) frees the slot — so the attacker never passes `--terminate-instances`.
**Mechanism:** `fleet-quotas` (the single Region-scoped 1,000 row + footnote that `cancelled_running` counts and `cancelled_terminating` does not); `API_ModifySpotFleetRequest` ("set the target capacity to 0"); `spot-fleet-states` `submitted` immediate-cancel sentence.
**Confirm/Refute oracle:** `service-quotas get-service-quota` (read-only) confirms the value is a single Region/account number with no per-principal partition. No live creation needed to validate the design claim; a defender refutes it only by finding an undocumented per-caller partition.
**Preconditions / Cost:** any principal with `RequestSpotFleet`; near-zero compute (TargetCapacity 0). **Severity-if-true:** High (intra-account, cross-team, cheap, deterministic availability DoS). **Owner-to-fix:** AWS (quota is per-account by design) + customer (SCP limiting fleet count). **Stop:** confirm the quota semantics read-only; do not actually exhaust a shared account.

**SF-5 — Direct `ModifySpotFleetRequest` bypasses the Application-Auto-Scaling min/max.**
**Claim:** The scaling floor/ceiling is enforced **only** by Application Auto Scaling's `RegisterScalableTarget` Min/MaxCapacity; EC2 does **not** cross-check `ModifySpotFleetRequest` against it. A holder of the auto-scaling sample policy (which grants `ec2:ModifySpotFleetRequest` on `Resource:"*"`) can set any fleet's `TargetCapacity` up to the 10,000 quota (cost blowout) or 0 (outage), silently overriding the owner's configured bounds.
**Mechanism:** `spot-fleet-automatic-scaling` ("scaling policies are created with Application Auto Scaling" — separate control plane, no EC2-side bound check documented); `API_ModifySpotFleetRequest` (`TargetCapacity` plain integer, no range beyond quota); `spot-fleet-auto-scaling-IAM` grants `ec2:ModifySpotFleetRequest` beside `application-autoscaling:*` on `*`.
**Confirm/Refute oracle:** `application-autoscaling describe-scalable-targets --service-namespace ec2` reads the configured bound; `SimulatePrincipalPolicy` confirms `ec2:ModifySpotFleetRequest` is unconditional and fleet-unscoped. Whether EC2 re-validates against the registered bound is **undocumented** → canary `maintain` fleet with a scalable target registered Min=1/Max=2, then real `ModifySpotFleetRequest --target-capacity 5`; if accepted → bypass confirmed.
**Severity-if-true:** High (cost/availability, intra-account cross-team because `Resource:"*"`). **Owner-to-fix:** AWS (missing `aws:CalledVia application-autoscaling.amazonaws.com` guard pattern) + customer.

**SF-6 — Cross-fleet CloudWatch alarm tampering.**
**Claim:** The auto-scaling sample policy grants `cloudwatch:PutMetricAlarm`/`DeleteAlarms`/`DisableAlarmActions`/`EnableAlarmActions` on `Resource:"*"`. A holder can **delete/disable** another fleet's scale-out alarm (starve it under load) or **overwrite** its scale-in alarm threshold to force premature termination — without any EC2/AAS permission on the victim fleet. The target-tracking page's only control is prose ("Do not edit or delete the CloudWatch alarms that Spot Fleet manages").
**Mechanism:** verbatim policy JSON in `spot-fleet-auto-scaling-IAM`; auto-named alarms `TargetTracking-sfr-<id>-AlarmHigh/Low`.
**Confirm/Refute oracle:** `cloudwatch describe-alarms --alarm-name-prefix TargetTracking-sfr-` (read-only enumeration) + `SimulatePrincipalPolicy` for `DeleteAlarms`/`PutMetricAlarm` against a foreign fleet's alarm ARN → `allowed`.
**Severity-if-true:** High (victim availability/cost DoS). **Owner-to-fix:** AWS (sample policy) + customer.

**SF-7 — Instance-weighting rounding defeats scale-in deterministically.** *(Lens L)*
**Claim:** AWS's own worked examples show integer round-**up** of fulfilled capacity can make a scale-in alarm fire yet take "no scaling action," pinning a fleet above target. An adversary who can induce the weighted-pool skew (e.g. by consuming the cheap low-weight pool elsewhere in the Region) can keep a victim's scale-in permanently defeated (cost).
**Mechanism:** `spot-fleet-automatic-scaling` "Considerations → Instance weighting" (the 30.1→30 and 12→10 examples, verbatim).
**Confirm/Refute oracle:** arithmetic replay against a target fleet's real weight config via read-only `describe-spot-fleet-requests` + `describe-spot-fleet-instances`; no live scaling needed.
**Severity-if-true:** Medium (cost abuse; root cause is the owner's own policy math per AWS docs, but worth flagging). **Owner-to-fix:** customer (policy tuning).

### Area 3 — Revocation / orphan completeness (`cancelled_running` and delete)
*Lens AA / U. The cancel transition is a revoke operation; test what it fails to tear down.*

**SF-8 — KMS grant to the SLR is never retired on cancel/delete, and includes `CreateGrant`.**
**Claim:** The documented encrypted-AMI/EBS runbook creates a KMS grant to `AWSServiceRoleForEC2SpotFleet` with operations `Decrypt Encrypt GenerateDataKey GenerateDataKeyWithoutPlaintext CreateGrant DescribeKey ReEncryptFrom ReEncryptTo`. **No** Spot Fleet doc instructs (or claims EC2 performs) `RetireGrant`/`RevokeGrant` on fleet cancel/delete — and the "delete the SLR" guidance addresses only the IAM role, not the grant. Per KMS semantics, deleting the grantee principal does **not** auto-retire a grant. Result: a durable `Decrypt`+`CreateGrant` capability on the customer CMK that outlives the fleet and its instances.
**Mechanism:** `spot-fleet-prerequisites` §"Grant access to CMKs …" (the `create-grant` command with `CreateGrant` in `--operations`); the paired teardown ("we recommend that you delete the … role") omits the grant; **doc silence** — `RetireGrant`/`RevokeGrant` appears nowhere in the Spot Fleet docs tree.
**Confirm/Refute oracle:** `kms:ListGrants --key-id <cmk>` before/after cancelling a fleet that used the CMK → grant for the SLR still listed = stale. Cross-check `iam:GetRole` for the SLR (even after manual deletion) against the surviving grant. Read-only.
**Preconditions / Cost:** a fleet that used a customer CMK; read-only list. **Severity-if-true:** High (durable decryption + sub-grant-minting primitive; "setup documented, teardown undocumented"). **Owner-to-fix:** shared — AWS (over-broad default operation set incl. `CreateGrant`; no teardown step) + customer. Cross-reference broad plan `H2` and `ec2-fleet-attack-research-plan.md` KMS section (same shape).

**SF-9 — Orphaned `cancelled_running` instances stay tagged; SLR termination authority keys on tag-key *presence*, not a live fleet.**
**Claim:** After cancel-without-terminate, instances keep running **and** keep the `aws:ec2spot:fleet-request-id` tag, while the SLR's `ec2:TerminateInstances` is conditioned only `StringLike ec2:ResourceTag/aws:ec2spot:fleet-request-id : "*"` (any value). So (a) the authorization boundary for "who may kill these" does **not** depend on the owning fleet still existing, and (b) any customer SCP/IAM policy keyed on *presence* of that tag (e.g. an exception for "managed fleet instances") is **inherited indefinitely** by instances no fleet manages.
**Mechanism:** `spot-fleet-states` `cancelled_running` text; `AWSEC2SpotFleetServiceRolePolicy` v4 statement (the `StringLike "*"` termination condition); `IAM id_tags` ("`aws:ec2spot:fleet-request-id` identifies the … request that launched the instance" — static, no TTL/cleanup).
**Confirm/Refute oracle:** `describe-tags --filters Name=resource-id,Values=<orphan>` shows the tag present while `describe-spot-fleet-requests --spot-fleet-request-ids <sfr>` returns NotFound (live resource, dead parent). Whether a *user* can set the `aws:`-prefixed reserved tag to mark a victim instance for SLR termination is the escalation question → test `ec2:CreateTags` with that key (expect denied/ignored for reserved prefix). Read-only + one denied-tag probe.
**Severity-if-true:** Medium–High (persistence/evasion; tag-keyed-policy inheritance). If the reserved tag turns out user-settable → victim-instance-termination primitive (Medium–High). **Owner-to-fix:** AWS (value-agnostic condition) + customer (don't key policy on tag presence).

**SF-10 — Load-balancer / target-group registration has no teardown path.** *(new vs broad plan)*
**Claim:** The SLR policy grants `RegisterTargets`/`RegisterInstancesWithLoadBalancer` but **no `DeregisterTargets`/`DeregisterInstancesFromLoadBalancer`** — by design the SLR **cannot** deregister. No cancel/`cancelled_running` doc mentions deregistration. Orphaned instances therefore **stay registered** in the target group and keep receiving production traffic with no managing fleet and no automated path to remove them.
**Mechanism:** `AWSEC2SpotFleetServiceRolePolicy` (register actions present, deregister absent); `spot-fleet-prerequisites` SLR permission list; silence in `cancel-spot-fleet`.
**Confirm/Refute oracle:** `elbv2 describe-target-health --target-group-arn <tg>` after a `--no-terminate-instances` cancel of a fleet with `LoadBalancersConfig` → target still `healthy`/registered. Read-only.
**Severity-if-true:** Medium–High (stale traffic routing to unmanaged instances; chains with SF-9 persistence and with broad-plan `S2` ELB insertion). **Owner-to-fix:** AWS (no deregister capability) + customer (manual cleanup).

### Area 4 — State-transition integrity & forensic decay
*Lens X / BB / O.*

**SF-11 — 48-hour deletion of the `cancelled` request erases the EC2-native launch-config trail.** *(Lens O)*
**Claim:** Once a request reaches `cancelled` and is deleted (2 days / 48 h after its instances terminate), both `DescribeSpotFleetRequests` (config: ImageId, IamFleetRole, launch spec) and `DescribeSpotFleetRequestHistory` (events, already only 48 h retained) become unresolvable — so "what AMI/role/user-data launched this now-orphaned instance?" can no longer be answered from EC2 Spot Fleet APIs alone. CloudTrail mitigates **only if** a trail/Lake is configured and retained; an IR team defaulting to the EC2 console loses the trail exactly on the attacker's cancel-and-wait clock.
**Mechanism:** `spot-fleet-states` ("deleted two days after its instances are terminated"); `API_DescribeSpotFleetRequests` ("deleted 48 hours after …"); `API_DescribeSpotFleetRequestHistory` ("events are available for 48 hours").
**Confirm/Refute oracle:** `describe-spot-fleet-request-history --spot-fleet-request-id <aged sfr>` on a request >2 days past termination → expect NotFound-class error; cross-check `cloudtrail lookup-events` for the same `spotFleetRequestId` to scope whether the gap is EC2-API-local or absolute. Read-only.
**Severity-if-true:** Medium (bounded, EC2-API-local forensic gap; a convenient anti-forensics timing coincidence for cancel-without-terminate). **Owner-to-fix:** customer (CloudTrail retention) — flag as IR assumption, not a bug.

**SF-12 — SLR-attributed events + sfr-id purge break the human-requester attribution chain.** *(Lens O)*
**Claim:** The fleet's `RunInstances`/`TerminateInstances`/`RegisterTargets`/`CreateTags` are logged in CloudTrail as actions by the SLR via `spotfleet.amazonaws.com`, not by the human who called `RequestSpotFleet`. The only documented join key back to the human is `spotFleetRequestId` in `requestParameters` — which is exactly what SF-11 purges at 48 h. Post-orphaning + purge, the "SLR did X for sfr-Y → human who created sfr-Y" pivot is broken in EC2-native tooling.
**Mechanism:** `monitor-with-cloudtrail` (generic "request made by another AWS service" + `userIdentity.invokedBy`); `manage-spot-fleet` (sfr-id is the join key); SF-11 purge. (SLR-attribution specifics inferred from documented general CloudTrail service-principal behavior, not a Spot-Fleet-specific example — verify first.)
**Confirm/Refute oracle:** `cloudtrail lookup-events` on `RunInstances` around a fleet's activity → inspect `userIdentity.invokedBy`/`arn` (expect SLR) and whether `requestParameters.spotFleetRequestId` persists in the record (the mitigating factor). Read-only.
**Severity-if-true:** Medium (expected SLR behavior, but a real audit-pivot decay). **Owner-to-fix:** customer (CloudTrail/Lake retention + query discipline).

**SF-13 — Modify/Cancel TOCTOU: no documented state-precondition error.** *(Lens X / BB)*
**Claim:** Neither `API_ModifySpotFleetRequest` (Errors section points only to Common Errors) nor the UserGuide enumerates a state-conflict error for calling `Modify` while a fleet is already `modifying`/`submitted`. The state page itself documents that `cancel` is permitted *during* `modifying` (`modifying → cancelled_*`). This implies a lost-update / inconsistent-target-capacity window if two `ModifySpotFleetRequest` (or modify+cancel) calls race on one `maintain` fleet.
**Mechanism:** `API_ModifySpotFleetRequest` Errors ("see Common Error Types"); `spot-fleet-states` `modifying` ("… or the request is canceled"); silence on modify-during-modifying in both twins.
**Confirm/Refute oracle:** two back-to-back real `ModifySpotFleetRequest` calls (dry-run cannot test state — it checks IAM only) on a canary mid-modify fleet; inspect `describe-spot-fleet-request-history` for interleaved vs serialized events. Canary fleet only.
**Severity-if-true:** Medium (same-owner self-inconsistency); High if a second principal with only `ec2:ModifySpotFleetRequest` can interleave competing modifies on a shared fleet (folds into SF-2's cross-team reach). **Owner-to-fix:** AWS.

**SF-14 — `maintain`-only / `active`-only modify gate is prose-only.** *(Lens U / P)*
**Claim:** "You can only modify a `maintain` fleet" is asserted in prose on two pages but has **no API error code**, so it is unknown from docs whether the gate is a real server-side state check or a console/client guard. If weak, a caller could flip a one-time (`request`) fleet's capacity/termination behavior outside its documented lifecycle.
**Mechanism:** `API_ModifySpotFleetRequest` ("You can only modify … type `maintain`" with no enumerated error); `spot-fleet-states`/`modify-spot-fleet` prose only.
**Confirm/Refute oracle:** real `ModifySpotFleetRequest` against a canary one-time (`type=request`) fleet → distinct `InvalidSpotFleetRequestState`-class error (enforced) vs silent success (weak). Dry-run won't reveal it (IAM-only). Canary fleet, call does not mutate if rejected.
**Severity-if-true:** Medium (lifecycle logic bypass, no privilege-boundary break). **Owner-to-fix:** AWS.

**SF-15 — Cancel per-ID response split as a state oracle; "deleted" vs "cancelled" wording.** *(Lens BB / low)*
**Claim:** `CancelSpotFleetRequests` returns per-ID `SuccessfulFleetRequests`/`UnsuccessfulFleetRequests` with `current`/`previousSpotFleetRequestState`. If IAM-deny vs state-conflict errors are distinguishable per item, a broadly-scoped caller could use the split to probe a fleet's state without `Describe*`. The docs also say "deleted" where the action is "cancel" (legacy-wording leftover) — a potential automation/parser confusion signal.
**Mechanism:** `API_CancelSpotFleetRequests` response shape + "if you exceed … no fleets are deleted" (atomic — rules out a count-overflow oracle).
**Confirm/Refute oracle:** `--dry-run` mixed batch (authorized + unauthorized + already-cancelled IDs) → observe whether per-ID differentiation leaks (dry-run tests the auth branch only). Safe.
**Severity-if-true:** Low (enumeration/oracle); multiplier on SF-13 if per-ID errors reveal transition timing. **Owner-to-fix:** AWS.

**Kill-chain to compose:** SF-2 (hold AWS sample policy → account-wide Cancel) → cancel a victim team's fleet **without** terminate (SF-9/SF-10: orphan instances stay running, tagged, and load-balanced) → the request + history self-delete at 48 h (SF-11/SF-12: EC2-native attribution of what the orphan is and who left it is gone) → the orphan keeps serving production traffic as an unmanaged, hard-to-attribute foothold. Rate at the end of the chain (persistence + cross-team disruption + anti-forensics), not the entry point. Separately, SF-8's surviving CMK grant is a durable decryption primitive independent of this chain.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Cancel/terminate another team's fleet; read its config | `Cancel`/`Modify`/`DescribeSpotFleetRequests` on `Resource:"*"` | ARN+tag scoping *available* for Modify/Cancel/DescribeInstances/History but **unused** by AWS's sample policy; **none** possible for `DescribeSpotFleetRequests` |
| Resource-scoped policy silently fails closed | Modify/Cancel resource-level support | Doc-vs-doc contradiction (`tag-spot-fleet` vs `list_ec2`) — enforcement unverified |
| Push capacity past AAS min/max; zero a fleet | direct `ModifySpotFleetRequest` | Min/max enforced only in Application Auto Scaling; no EC2-side `CalledVia` guard |
| Disable/overwrite a victim fleet's scaling alarms | `cloudwatch:*` on `*` in auto-scaling policy | Prose only ("don't edit the alarms") |
| Account-wide fleet-launch denial | shared Region quota + `submitted` immediate-cancel | None IAM-native; SCP limiting fleet count |
| Surviving CMK grant after cancel/delete | SLR KMS grant (incl. `CreateGrant`) | No documented `RetireGrant`; teardown covers only the role |
| Orphaned, still-tagged, still-load-balanced instances | `cancelled_running` + SLR (no `Deregister*`) | None (documented behavior); value-agnostic termination condition |
| EC2-native forensic/attribution decay | 48 h request+history deletion; SLR attribution | CloudTrail/Lake retention (customer-configured) |
| Modify race / one-time-fleet modify | state-transition gates | Prose-only preconditions; no enumerated state error |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-account / cross-tenant access to any `sfr-` fleet** — Spot Fleet runs wholly in the caller's account; EC2 account-partitioning protects these APIs as it does every `Describe*`/`Cancel*`. `sfr-` IDs are UUID-shaped (~122-bit) → **enumeration null** (SF-5 ID note is a multiplier only, and moot under `Resource:"*"`). All leads here are **intra-account cross-team**, not cross-tenant.
- **`sfr-` as a leaked capability** — never a bearer token; every call is SigV4-authed. (Lens M null.)
- **IMDS / UserData on the launched instances** — the instances are the customer's own; steering one's own instance boot/creds is not a boundary breach unless a *more-privileged* instance profile is attached (that chain lives in the broad plan `R1`/`S3`, not here).
- **Single-tenant self-DoS / cost churn from one's own quota** — bounded by the attacker's own bill, unless from compromised credentials (then SF-4/SF-6 griefing applies).
- **IAM-artifact privilege escalation, cross-account confused deputy, Config-rule blind spot** — covered in `spot-fleet-attack-research-plan.md` (`R1`/`R2`/`R3`/`S1`/`S2`/`S3`/`B1`/`H1`); not re-scoped here.
- **AWS's own service plane** — `spotfleet.amazonaws.com` and the three SLRs are the shared-responsibility line and a **hard stop**.
- **Customer-authored policies** — a weak policy the customer wrote is a footgun (out of scope). In scope here: the **AWS-published sample policies** (SF-2/SF-5/SF-6) and **AWS-managed SLR policy** (SF-8/SF-9/SF-10), which are copy-verbatim / uneditable.

---

## 8. Null hypotheses / doc gaps (pages checked)

- **Lens A (cross-tenant IDOR):** null for cross-account; the real finding is **intra-account unscopable grant** (SF-1) and **account-wide-by-default sample policy** (SF-2). Pages: `spot-fleet-states`, `manage-spot-fleet`, `list_ec2.md`, all five `API_*` pages.
- **Lens C (credential vending / STS session scope):** null — `IamFleetRole` is a static ARN; no session-policy/ProvidedContext/per-tenant role vending. Pages: `spot-fleet-prerequisites`, `API_RequestSpotFleet`.
- **Lens D / V (data-plane→control-plane / network segmentation):** null — no service-owned fleet, no control/storage ENI, no multi-tenant subnet; all instances live in the customer VPC. Pages: `work-with-spot-fleets`, `create-spot-fleet`.
- **Lens F (translation/wire-protocol injection):** null — plain EC2 Query/SDK, no translator. Pages: `API_RequestSpotFleet`, `API_ModifySpotFleetRequest`.
- **Lens G (SSRF):** null — no field the lifecycle APIs dereference server-side (no URL/webhook/logo/import); `ImageId`/`SubnetId`/`IamFleetRole` are AWS resource identifiers, not fetched locations. The launch-template `resolve:ssm:<ARN>` AMI alias is the one adjacent surface → see `ec2-fleet-attack-research-plan.md`. Pages checked: `create-spot-fleet`, `tag-spot-fleet`, `modify-spot-fleet`, `cancel-spot-fleet`.
- **Lens K (prompt injection):** N/A — no LLM/agent.
- **Lens M (shared-identifier interception):** null — `sfr-` always paired with SigV4; no presigned/one-time token. Pages: all `API_*`.
- **Lens N (ARN/namespace migration):** null — single legacy namespace, no dual-live migration. The `AmazonEC2SpotFleetRole`→`AmazonEC2SpotFleetTaggingRole` / `aws-ec2-spot-fleet-autoscale-role`→SLR migrations are role-name changes, not dual-live authz namespaces (see broad plan). Pages: `spot-fleet-prerequisites`, `spot-fleet-auto-scaling-IAM`.
- **Lens P (identity proofing / registration):** no onboarding/KYC/OTP. The nearest "gate" is the state-transition precondition → covered as SF-14 (workflow-gate enforcement) and SF-5 (guardrail bypass).
- **Doc gaps to confirm first:** SF-3 (does resource-scoped Modify/Cancel actually work?), SF-12 (SLR CloudTrail `userIdentity` specifics — inferred from general behavior), SF-14 (server-side vs console-only state gate), the **`Context` "Reserved"** field on `RequestSpotFleet`/`ModifySpotFleetRequest` (undocumented input surface — probe for accepted values / behavior). All marked "confirm surface first," not "N/A."

---

*End of plan. Downstream hunter (`aws-vuln-hunter`): start with SF-1/SF-2/SF-4/SF-8 — all confirmable read-only via `SimulatePrincipalPolicy`, `GetPolicyVersion`, `ListGrants`, and `get-service-quota` before any live fleet is created. Use `list_ec2.md` (not `list_amazonec2.html`) for the IAM reference.*
