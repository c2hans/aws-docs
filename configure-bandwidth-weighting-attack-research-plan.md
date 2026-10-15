# EC2 Configure Bandwidth Weighting — Attack Research Plan

> **Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-bandwidth-weighting.html
> **Offline mirror:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/configure-bandwidth-weighting.md`
> **IAM authority:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`
> **API refs read:** `API_ModifyInstanceNetworkPerformanceOptions.md`, `API_LaunchTemplateNetworkPerformanceOptionsRequest.md`, `API_RequestLaunchTemplateData.md`, `aws-properties-ec2-launchtemplate-networkperformanceoptions.md`
> **Scope note:** single-account EC2, direct **caller-identity** control-plane actions (NOT a Fleet SLR page — the Fleet SLR-non-propagation backbone applies only as a *cross-reference*, §4 Lens B). This is the **configuration / how-to ACTION page** for the mechanism whose *capacity concepts* are owned by the sibling plan `ec2-instance-network-bandwidth-attack-research-plan.md`. **Primary firing lenses: S (condition-key scoping/enforcement semantics), U (documented guarantee vs enforcement), B/X (launch-template late-binding + action-family parity), O (silent Write mutation / no native event), L (self-affecting EBS-IOPS degradation under `vpc-1`).**
> **Drift check:** target page online == offline, **byte-identical, verified 2026-10-15** (two independent subagent fetches). `list_ec2` reference offline-authoritative; online byte-parity for its rows **unverifiable** (WebFetch truncates the HTML before the condition-key tables — a known limitation, not drift evidence).
> **Relationship to sibling (de-dup contract):** the sibling `ec2-instance-network-bandwidth` plan is a **concepts/capacity-governor** page and **owns** burst-pool cross-tenant contention (Lens L headline), the guest-only telemetry gap for *bandwidth-exhaustion* (Lens O), the baseline-sustainability guarantee (Lens U), the resource-less `*AwsNetworkPerformance*` actions, and SRD/ENA-Express isolation. **This plan does NOT re-litigate those.** This plan **owns the configuration-action layer** and **resolves/sharpens the sibling's carried-open questions**: sibling Lead #6 (new-value-vs-current-value at Modify time) and sibling Lead #5 (stop/start credit reset, which this page's Stopped-state precondition makes concrete).

---

## 0. TL;DR — where the boundaries might not hold

1. **[S — HEADLINE, resolves sibling Lead #6] `ec2:InstanceBandwidthWeighting` is listed on the `instance*` *resource* row of `ModifyInstanceNetworkPerformanceOptions` (list_ec2 L8867–8871) — so it most plausibly matches the instance's CURRENT weighting, not the NEW value in the call.** If so, a policy intended to pin an instance to `default`/`ebs-1` by writing `Deny … Condition {StringEquals ec2:InstanceBandwidthWeighting: vpc-1}` **fails to prevent the Modify that *sets* `vpc-1`** — it only blocks Modifies on instances *already* at `vpc-1`. The author's intent ("this instance must never become vpc-1") is silently defeated. Docs never state request-vs-resource semantics → **the single highest-value live-canary question.** (See §4 Lens S, Lead #1.)

2. **[S / B — HEADLINE] The launch-template body is an IAM blind spot for weighting.** `CreateLaunchTemplate` (L5253–5257) and `CreateLaunchTemplateVersion` (L5258–5262) carry **no `ec2:InstanceBandwidthWeighting` key** — only tag/region keys. A principal who can author an LT version can bake `BandwidthWeighting=vpc-1` (via `LaunchTemplateNetworkPerformanceOptionsRequest`) into `$Latest` with **zero IAM lever to constrain the value**, and the weighting condition key is **absent from the RunInstances `launch-template` resource row** (L9593) — it exists only on the resulting `instance*` row (L9591). Combined with `$Latest`/`$Default` late-binding, this is the classic "author the template, let a different principal/SLR consume it" redirect. (§4 Lens B/X, Lead #2.)

3. **[U / L — self-affecting workload-integrity knob, NET-NEW vs sibling] `vpc-1` silently degrades achievable EBS IOPS.** The page states verbatim that `vpc-1` can cause "**lower IOPS for EBS volumes if you reach the EBS bandwidth limit before … the IOPS limit**" (example: an instance normally doing 240,000 IOPS @16 KiB). Weighting is doc-asserted **self-affecting only** ("combined bandwidth … does not change"), so this is **not** a cross-tenant resource grab — it is a **workload-integrity / availability knob**: whoever controls the weighting (directly, or via LT late-binding in #2) can quietly throttle a victim instance's storage throughput without touching EBS at all, invisibly to EBS-centric monitoring. (§4 Lens L/U, Lead #3.)

4. **[O — silent Write mutation] A weighting change emits NO native EventBridge event and NO dedicated CloudWatch metric.** `ModifyInstanceNetworkPerformanceOptions` is a Write-level management action (CloudTrail-logged by default), but it is **absent from the EC2 EventBridge native event catalog** (`automating_with_eventbridge.html`), and the current value is readable **only by polling `DescribeInstances` → `NetworkPerformanceOptions.BandwidthWeighting`**. `DescribeInstances` is itself **unscopable** (L6996–6999: blank resource type, `ec2:Region` only). Drift-detection pipelines keyed to EventBridge have a blind spot for this mutation. (§4 Lens O, Lead #4.)

5. **[U — availability-precondition] Modify requires the instance in `Stopped` state, asserted ONLY in UserGuide prose, never in the API contract.** `API_ModifyInstanceNetworkPerformanceOptions.md` documents no state precondition and no specific error ("see Common Error Types"). The gate means re-weighting a running victim **requires forcing a stop first** — the weighting attack carries a built-in availability-disruption prerequisite, and the stop/start cycle re-grants max network-I/O credits (sibling Lead #5), chaining the two pages. (§4 Lens U, Lead #5.)

6. **[S — inert-boilerplate audit] `ec2:Attribute` and `ec2:Attribute/${AttributeName}` are listed on the Modify row but are probably inherited boilerplate.** They may let an operator *believe* they can scope the attribute (`Condition ec2:Attribute/… `) when the control is actually inert for this dedicated action — a false-sense-of-security hardening gap. (§4 Lens S, Lead #6.)

7. **[Doc-integrity] The console walkthrough asserts "the AMI must be based on `Arm` architecture," contradicting the same page's own supported-instance-types table** (which lists x86 families C8a/M8a/R8a, C8i/M8i/R8i/X8i, *-flex). Nothing in `run-instances`/`modify-instance-network-performance-options`/LT object docs enforces an architecture restriction → a documentation defect, not a real constraint. Flagged so a hunter does not build a hypothesis on a non-existent Arm gate. (§4 Lens U-doc, Lead #7.)

---

## 1. Components, Assets, and Design

### What the page actually describes
A **per-instance configuration knob** — `BandwidthWeighting ∈ {default, vpc-1, ebs-1}` — that shifts the *baseline* bandwidth split between the networking path and the EBS path **without changing the combined total**. `default` = balanced; `vpc-1` = favour networking (reduces EBS baseline → possible IOPS loss); `ebs-1` = favour EBS (reduces network baseline). Three ways to set it:

- **Launch-time, inline:** `RunInstances --network-performance-options BandwidthWeighting=vpc-1|ebs-1` (`RequestLaunchTemplateData.NetworkPerformanceOptions` is the same object when inline).
- **Launch-time, via launch template:** `LaunchTemplateNetworkPerformanceOptionsRequest.BandwidthWeighting` baked into an LT version (console "Advanced details → Instance bandwidth configuration"); also a CloudFormation property `AWS::EC2::LaunchTemplate NetworkPerformanceOptions` (`Update requires: No interruption`).
- **Post-launch:** `ModifyInstanceNetworkPerformanceOptions --instance-id --bandwidth-weighting …` — **requires the instance `Stopped`**.

Read-back: `DescribeInstances … NetworkPerformanceOptions.BandwidthWeighting` (poll-only; `--filters Name=network-performance-options.bandwidth-weighting,Values=vpc-1`).

Supported only on specific 8th/9th-gen families (M8/C8/R8/X8 + M9/C9/R9 variants, both x86 and Graviton).

### Assets at stake
- **A victim instance's effective EBS IOPS / storage throughput** (workload-integrity + availability asset) — degradable by flipping it to `vpc-1`, with no EBS-side signal.
- **A victim instance's effective internet-gateway / local-gateway egress ceiling** (border bandwidth) — scales *with* the weighted baseline ("50% of baseline or 5 Gbps"), so an SCP/guardrail reasoning about a fixed per-type egress cap is invalidated when weighting changes.
- **The weighting configuration itself** (an integrity/compliance asset) — mutable by a Write action with weak/ambiguous IAM scoping and no native event.
- **The launch-template body** (a late-binding config asset) — the weighting value baked into it is ungoverned by any condition key.

### Identity / control surface
Direct SigV4 IAM caller identity. Mutating: `RunInstances`, `CreateLaunchTemplate`/`CreateLaunchTemplateVersion`, `ModifyInstanceNetworkPerformanceOptions`, (`ModifyInstancePlacement` carries the key but does not change weighting — inert here). Read: `DescribeInstances`, `DescribeLaunchTemplateVersions`.

### ASCII — where the configuration-layer boundaries live
```
  Principal P ──RunInstances --network-performance-options──┐
       │                                                     ▼
       │                                            ┌──────────────────┐
       ├─CreateLaunchTemplateVersion(vpc-1)──►  LT $Latest  ──consume──►│  instance        │
       │   (NO ec2:InstanceBandwidthWeighting key              (SLR/   │  weighting=vpc-1 │
       │    on CreateLT* or on RunInstances LT row)            Fleet/  │                  │
       │                                                        ASG)   └────────┬─────────┘
       │                                                                        │ vpc-1 ⇒ lower
       └─ModifyInstanceNetworkPerformanceOptions ──(requires Stopped)──►        ▼ achievable
            key on instance* RESOURCE row ⇒ matches CURRENT value?       EBS IOPS (self, silent)
            (gates new value? ← sibling Lead #6, UNRESOLVED in docs)
                                                                         No EventBridge event;
                                                                         read only via DescribeInstances
                                                                         (unscopable, ec2:Region only)
```

---

## 2. Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Principal denied `vpc-1` via a resource-key Deny | An instance it is allowed to Modify | `ModifyInstanceNetworkPerformanceOptions` where the key matches **current** not **requested** weighting | The Modify **succeeds** in setting `vpc-1` on an instance that was `default` — proving the Deny only blocked already-`vpc-1` instances (intent defeated) |
| LT author (no weighting-scoping key) | A consumer principal / SLR that launches from `$Latest` | `CreateLaunchTemplateVersion` bakes `BandwidthWeighting`; RunInstances LT row has no key | A launch picks up a weighting the consumer's own identity policy would have forbidden inline |
| Operator who flips a victim to `vpc-1` | Victim's EBS IOPS / workload | Weighting is self-affecting; `vpc-1` reduces EBS baseline | Victim's achievable IOPS drops with **no EBS metric change and no EventBridge event** |
| Operator changing weighting | Audit / drift-detection pipeline | Write action with no native event; poll-only read | A weighting change produces **only** a CloudTrail record (if enabled) — nothing fires in an EventBridge-keyed detector |
| Attacker needing to re-weight a running victim | Victim availability | Modify requires `Stopped` | The attack **forces a stop** first (availability disruption as a precondition) + stop/start re-grants max network-I/O credits (→ sibling) |

---

## 3. API / interface surface (configuration subset of `list_ec2`)

| Name | Mutating | Resource row(s) | Weighting-relevant condition keys | Notes |
|---|---|---|---|---|
| `ModifyInstanceNetworkPerformanceOptions` | yes (Write) | `instance*` (L8867–8871) | `ec2:InstanceBandwidthWeighting` (on the resource row), `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, + full generic instance set | **The page's primary action.** Requires `Stopped` (UG prose only). Key on resource row ⇒ **current-value match suspected** (Lead #1). |
| `RunInstances` | yes | `instance*` (L9591) carries key; `launch-template` (L9593) and `network-interface*` (L9595) do **NOT** | `ec2:InstanceBandwidthWeighting` **only** on `instance*` | Inline `--network-performance-options`. Key absent from LT row ⇒ LT-sourced value ungoverned at the LT seam (Lead #2). |
| `CreateLaunchTemplate` | yes | `launch-template*` (L5253–5257) | **none** (`aws:RequestTag`, `aws:TagKeys`, `ec2:Region` only) | No lever on the baked `BandwidthWeighting` value. |
| `CreateLaunchTemplateVersion` | yes | (L5258–5262) | **none** (`aws:ResourceTag`, `ec2:ManagedResourceOperator`, `ec2:Region`, `ec2:ResourceTag`) | Same gap for a new version → `$Latest` redirect. |
| `ModifyInstancePlacement` | yes | `instance*` (L8876), `dedicated-host` (L8875), `placement-group` (L8877) | `ec2:InstanceBandwidthWeighting` on `instance*` | **Inert for weighting** — does not change it (corrects prior note: key row is L8876, not L8873). Listed for completeness. |
| `DescribeInstances` | no (List) | *(blank — unscopable)* (L6996–6999) | `ec2:Region` only | Poll-only read oracle for current weighting; **cannot be scoped** to instances or weighting values. |
| `DescribeLaunchTemplateVersions` | no | *(see list_ec2)* | — | Read-back of the baked LT value for drift detection. |

**`ec2:InstanceBandwidthWeighting` — exact definition (list_ec2 L10089):** `Filters access by the bandwidth weighting of an instance | String`. Values: `default | vpc-1 | ebs-1`. Appears on the shared `instance`-resource key set service-wide (ModifyInstanceMetadataOptions, StartInstances, SendDiagnosticInterrupt, ReportInstanceStatus, the `instance` ARN row ~L9949, etc.), but is a *meaningful request/resource control* only on `RunInstances`, `ModifyInstanceNetworkPerformanceOptions`, `ModifyInstancePlacement`. The def's doc anchor (`#imageId-key`) is a copy-paste artifact — cosmetic.

**Console-hidden / under-surfaced knob check:** the generic LT pages (`create-launch-template.html`, `launch-instances-from-launch-template.html`) contain **zero** mention of "bandwidth" — the knob exists in the LT body (`LaunchTemplateNetworkPerformanceOptionsRequest.BandwidthWeighting`, CloudFormation `NetworkPerformanceOptions`) but is surfaced only from the weighting page. An operator reviewing LT docs would not know the field is settable there. This asymmetry is the Lens-B/X seed (Lead #2).

---

## 4. Boundary-lens catalogue (fired + null, pages named)

### Lens S — Condition-key scoping & enforcement semantics  **[PRIMARY — FIRES]**
- **Trigger:** a real request/resource key (`ec2:InstanceBandwidthWeighting`) on a Write action; generic `ec2:Attribute*` keys; a launch-template authoring path.
- **Fired finding A (resolves sibling Lead #6 as far as docs allow):** the key is listed on the **`instance*` resource row** of `ModifyInstanceNetworkPerformanceOptions` (L8867–8871), not as a documented request key. AWS resource-row keys conventionally match the resource's **current** attribute. **Hypothesis (falsifiable):** a `Deny` with `Condition {StringEquals: {ec2:InstanceBandwidthWeighting: "vpc-1"}}` blocks Modifies on instances *currently* `vpc-1` but **does not block setting `vpc-1`** on a `default` instance → the "never let this become vpc-1" intent is silently defeated. **Oracle:** attach that Deny; attempt `modify-instance-network-performance-options --bandwidth-weighting vpc-1` on a `default` instance — if it succeeds, request-value is **not** gated. **Severity:** Medium (hardening-bypass / policy-intent defeat). **Confidence:** Med — doc-silent, strong IAM-convention prior.
- **Fired finding B (LT authoring gap):** `CreateLaunchTemplate`/`Version` carry **no** weighting key → the value baked into an LT is ungoverned by IAM. **Oracle:** author an LT version with `vpc-1` under a policy that denies `vpc-1` inline on RunInstances; confirm the LT create succeeds. **Severity:** Medium (feeds Lens B redirect, Lead #2).
- **Fired finding C (inert boilerplate):** `ec2:Attribute` / `ec2:Attribute/${AttributeName}` on the Modify row are likely inherited from the shared `ModifyInstanceAttribute`-style template, not action-specific. **Oracle:** craft `Condition {ec2:Attribute/… }` on `ModifyInstanceNetworkPerformanceOptions`; confirm whether it is evaluated at all (policy-sim + live). **Severity:** Low (false-sense-of-security). **Confidence:** Med.

### Lens B — Confused deputy / late-binding via launch template  **[FIRES — net-new vs sibling]**
- **Trigger:** LT body carries `NetworkPerformanceOptions`; `$Latest`/`$Default` late-binding; Fleet/ASG/Spot consume LTs under `AWSServiceRoleForEC2Fleet`, which calls `ec2:RunInstances` on the caller's behalf (`ec2-fleet-prerequisites.md`).
- **Claim:** An identity-policy condition on `ec2:InstanceBandwidthWeighting` restricting the **caller** is **not** evaluated against the SLR's internal `RunInstances` when a Fleet/ASG launches from an LT — standard SLR behavior, but **nowhere stated on the bandwidth pages**. A principal who can edit `$Latest` on an LT referenced by a Fleet/ASG can flip the weighting of every future instance in that group without ever calling a weighting action directly, and without tripping the caller-side condition. → **Mechanism:** RunInstances `launch-template` row has no weighting key (L9593); `LaunchTemplateNetworkPerformanceOptionsRequest.BandwidthWeighting` exists; `$Latest` re-resolves per launch. → **Oracle:** point an ASG/Fleet at an LT; bump `$Latest` to `vpc-1`; confirm new instances launch `vpc-1` despite a caller-side Deny. → **Severity:** Medium–High (ungoverned fleet-wide weighting drift / workload degradation). → **Confidence:** Med (SLR non-propagation is well-established; this surface is doc-silent).
- **Cross-ref:** this is the *configuration-layer instance* of the Fleet SLR-non-propagation backbone catalogued across the Fleet plans; it is **net-new** here because the weighting field specifically is the payload.

### Lens U — Guarantee vs enforcement  **[FIRES]**
- **Claim 1 (Stopped-state precondition is prose-only):** the `Stopped` requirement lives only in UG prose; the API contract documents no precondition and no named error. → **Oracle:** call `ModifyInstanceNetworkPerformanceOptions` on a *running* instance; observe whether it errors (and with what code) or silently no-ops. → **Severity:** Low (correctness/robustness) but it is the **availability precondition** for any re-weighting attack (must force a stop). → **Chain:** stop/start re-grants max network-I/O credits — **sibling Lead #5**; a rapid stop→re-weight→start loop both re-weights *and* farms burst credits.
- **Claim 2 (border-bandwidth scaling vs fixed-cap assumptions):** the internet-/local-gateway multi-flow ceiling is "**50% of the baseline bandwidth of the configured option or 5 Gbps**" and scales with the weighted baseline (page example: 40→50 Gbps baseline moves border 20→25 Gbps). Any SCP/guardrail/capacity-plan treating per-type egress as fixed is **invalidated** when weighting changes. → **Oracle:** compare measured border egress at `default` vs `vpc-1`. → **Severity:** Low–Medium (guardrail-assumption break).

### Lens L — Resource effect (self-affecting EBS-IOPS degradation)  **[FIRES — net-new framing vs sibling]**
- **Trigger:** page states `vpc-1` "**might reduce the achievable IOPS due to the adjusted EBS baseline bandwidth limit**" (240,000 IOPS @16 KiB example); "combined bandwidth … does not change."
- **Claim:** weighting is a **self-affecting workload-integrity knob**, not a cross-tenant resource grab (the sibling owns the cross-tenant *burst-pool* story). Whoever controls the weighting (directly, or via Lens-B LT late-binding) can throttle a victim instance's **own** EBS IOPS silently — the degradation shows on EBS performance but **not** on any EBS *configuration* and not on any native event. → **Oracle:** `fio`/`iostat` on an EBS volume at `default` vs `vpc-1`, large I/O size, instance at/near EBS bandwidth limit; confirm IOPS drop with volume config unchanged. → **Severity:** Medium (stealth workload degradation; availability/integrity). → **Confidence:** High that the effect exists (documented); Med on exploitable magnitude.
- **Explicit non-claim:** "combined bandwidth … does not change" **refutes** any theory that weighting lets one instance claim more of the shared host pool. Cross-tenant contention is **burst** only → **DEFER to sibling Lens L headline.** Do not duplicate.

### Lens O — Detection / audit evasion  **[FIRES]**
- **Claim:** `ModifyInstanceNetworkPerformanceOptions` emits **no native EventBridge event** (absent from `automating_with_eventbridge.html` catalog) and **no dedicated CloudWatch metric**; current value is readable **only** by polling `DescribeInstances.NetworkPerformanceOptions.BandwidthWeighting`, and `DescribeInstances` is **unscopable** (L6996–6999). A weighting change is a silent Write mutation visible only in CloudTrail (if enabled/reviewed). → **Oracle:** change weighting; confirm nothing fires in an EventBridge rule and no metric appears; confirm detection requires polling or CloudTrail log review. → **Severity:** Medium as a force-multiplier on Leads #2/#3 (the degradation is both effective and event-less). → **Confidence:** High (confirmed from the event catalog + list_ec2).
- **Distinct from sibling Lens O:** the sibling owns the *guest-only ENA allowance-counter* telemetry gap for bandwidth **exhaustion**; this owns the *control-plane no-event* gap for the weighting **change action**. Complementary, not duplicate.

### Lens U-doc — Documentation integrity  **[FIRES — low severity, flagged to prevent a dead-end]**
- The console walkthrough's "AMI must be based on `Arm` architecture" sentence contradicts the same page's supported-types table (x86 families C8a/M8a/R8a, C8i/M8i/R8i/X8i, *-flex listed). No API/CLI/LT doc enforces architecture. → **Disposition:** documentation defect; **do not** hypothesize an Arm-only enforcement gate. A hunter should confirm x86 support via `describe-instance-types`/`run-instances` if it ever matters, but no research time should be spent treating Arm as a real constraint.

### Lenses explicitly NULL (triggers absent — pages named)
- **A (cross-tenant IDOR / disclosure):** NULL. Checked target page, `API_ModifyInstanceNetworkPerformanceOptions`, `DescribeInstances`. All actions are instance-scoped within the caller's own account; instance IDs are same-account; no resource is "revealed after a step." No cross-account naming. `DescribeInstances` is unscopable but returns only the caller's own instances (standard EC2 account isolation).
- **C (credential vending / session scope):** NULL — no STS/token/role-ARN input on any weighting action. Checked all action rows.
- **D (data→control-plane escape):** NULL — no control ENI / host-service surface on this config page. (Burst/SRD data-plane concerns are the sibling's.)
- **E (RBAC privilege escalation):** NULL — no role model, no hidden admin identity on this page.
- **F (translation-layer / injection):** NULL — the only input is a 3-value enum (`default|vpc-1|ebs-1`); no customer-string→downstream-language transform. (Enum fail-open is covered as the Lens-S/ec2:Attribute audit, Lead #6.)
- **G (SSRF):** NULL — no field the service dereferences. Checked target + LT object docs; `BandwidthWeighting` is an enum, no URL/URI/endpoint/location field anywhere.
- **P (gate before privileged change):** the `Stopped` precondition is the only gate and it is a state gate, not an identity/OTP/uniqueness gate → covered under Lens U, not P. No consent/code/one-per-account gate exists. NULL for P proper.
- **Q (blob parsing):** NULL — no upload/attachment/document input.
- **R (shipped IAM/CFN sample policy):** NULL on the UG page (no printed IAM JSON). The CloudFormation `NetworkPerformanceOptions` property is a resource-config snippet, not a policy artifact. `iam-policies-for-amazon-ec2.html` omits the key entirely (noted as a doc-gap under Lens S).
- **T (generated secret storage):** NULL — the feature generates/persists no secret, key, or credential.

---

## 5. Prioritised leads (NEW / highest-signal first)

| # | Lens | Lead | Confirm/refute oracle | Severity-if-true | Confidence |
|---|---|---|---|---|---|
| 1 | S | `ec2:InstanceBandwidthWeighting` on the Modify **resource** row gates **current** not **requested** value → a `Deny vpc-1` fails to prevent *setting* vpc-1 (resolves sibling Lead #6) | Attach the Deny; `modify … --bandwidth-weighting vpc-1` on a `default` instance → success = request-value not gated | Medium (policy-intent defeat / hardening bypass) | Med (doc-silent; strong IAM prior) |
| 2 | B/X | LT body bakes `BandwidthWeighting` with **no** scoping key (CreateLT* + RunInstances LT row); `$Latest` late-binding + Fleet/ASG SLR consumption bypass the caller-side weighting condition | Author LT `vpc-1` under a caller policy denying `vpc-1`; launch via ASG/Fleet from `$Latest`; new instances come up `vpc-1` | Medium–High (ungoverned fleet-wide weighting drift) | Med (SLR non-propagation established; surface doc-silent) |
| 3 | L/U | `vpc-1` silently reduces achievable EBS IOPS (self-affecting); stealth workload degradation with no EBS-config change and no event | `fio`/`iostat` at `default` vs `vpc-1`, large I/O size near EBS BW limit; IOPS drops, volume config unchanged | Medium (stealth availability/integrity) | High effect / Med magnitude |
| 4 | O | Weighting change = silent Write mutation: no EventBridge event, no metric, poll-only unscopable read | Change weighting; confirm no event fires, detection needs CloudTrail/poll | Medium (force-multiplier on #2/#3) | **High (confirmed)** |
| 5 | U | `Stopped`-state precondition is prose-only; forces a stop (availability) + stop/start re-grants max network-I/O credits | Call Modify on a running instance (error vs no-op?); rapid stop→re-weight→start loop | Low alone / chains to sibling #5 | Med |
| 6 | S | `ec2:Attribute`/`ec2:Attribute/${AttributeName}` on the Modify row are likely inert boilerplate (false sense of scoping) | Policy-sim + live: does a `Condition ec2:Attribute/…` evaluate for this action? | Low (hardening false-positive) | Med |
| 7 | U-doc | **DEFER/FLAG** — "AMI must be Arm" console sentence contradicts the x86-inclusive supported-types table; documentation defect, not a real gate | — | — | Doc defect — do not build a hypothesis on it |

**Doc-gaps to resolve before/at hunt time:** (a) request-vs-resource semantics of `ec2:InstanceBandwidthWeighting` on Modify (Lead #1 — the big one); (b) whether the EC2-Fleet "resource-level perms don't cover LT-named resources" caveat (list_ec2 ~L5114) formally extends to RunInstances-via-LT (Lead #2); (c) whether `ec2:Attribute*` is enforced for this action (Lead #6); (d) the Modify-on-running-instance error contract (Lead #5); (e) online byte-parity of the `list_ec2` rows (WebFetch truncation — offline treated authoritative).

---

## 6. Hunter preconditions & scope guardrails
- **Leads #1, #5, #6** are confirmable with **one instance the researcher owns** + IAM policy-simulator / a scoped test principal — no cross-tenant target, no co-residency. Lead #1 is the priority and is cheap: a single Deny policy + one Modify attempt settles it.
- **Lead #2** needs an LT + an ASG or EC2 Fleet in the researcher's own account + a second scoped principal — all synthetic.
- **Lead #3** needs an instance with an EBS volume and a load generator (`fio`); measure IOPS at `default` vs `vpc-1`. Self-contained, single-account.
- **Lead #4** is confirmable from the control plane alone (change weighting, watch for events).
- **Hard stops:** this is single-account, caller-identity EC2 — no cross-account weighting path exists in docs; do not attempt one. If any Modify/launch surfaces an identity, ARN, or role belonging to AWS's own service plane (e.g. the Fleet SLR's internal calls expose a service-plane credential), **stop, preserve evidence, flag for AWS-Security disclosure.** Use only synthetic canary instances/volumes; tear down every resource created.

## 7. What could not be fully tested from docs
- **Lead #1 semantics** — request-vs-resource evaluation of `ec2:InstanceBandwidthWeighting` on Modify: docs are silent everywhere (`list_ec2`, `iam-policies-for-amazon-ec2.html`, API ref). Live canary only.
- **Lead #2** — whether the LT resource-level-permissions caveat formally applies to RunInstances-via-LT for this field: documented only for EC2 Fleet. Live canary.
- **Lead #3 magnitude** — achievable IOPS degradation is instance-type- and workload-dependent; docs give one illustrative example only.
- **Lead #5** — Modify-on-running error contract and whether stop/start truly resets the network-I/O-credit bucket (sibling notes this is *not* explicitly stated either way). Empirical.
- **`list_ec2` online byte-parity** — WebFetch truncates the HTML before the condition-key tables; offline mirror treated authoritative per task instructions.

## 8. Cross-references
- **Sibling (concepts/capacity):** `ec2-instance-network-bandwidth-attack-research-plan.md` — owns burst-pool cross-tenant contention (Lens L headline), guest-only ENA telemetry gap (Lens O), baseline-sustainability guarantee (Lens U), resource-less `*AwsNetworkPerformance*` actions, SRD/ENA-Express. **This plan resolves that plan's Lead #6 (→ my Lead #1) and makes its Lead #5 concrete (→ my Lead #5 Stopped-state chain).** Reciprocal note should be added there.
- **Fleet SLR-non-propagation backbone:** my Lead #2 is the configuration-layer instance of the backbone catalogued across the EC2-Fleet plans (the weighting field is the net-new payload).
- **Parent hub:** `ec2-networking` hub plan (networking-wide IAM-scoping-gap theme).
- **IAM authority (`list_ec2.md`):** `ec2:InstanceBandwidthWeighting` def @L10089; `ModifyInstanceNetworkPerformanceOptions` @L8867–8871 (`instance*`, Write); `ModifyInstancePlacement` key @L8876 (corrects prior @L8873); `RunInstances` key on `instance*` @L9591 (absent from `launch-template` @L9593 and `network-interface*` @L9595); `CreateLaunchTemplate` @L5253–5257 / `CreateLaunchTemplateVersion` @L5258–5262 (no weighting key); `DescribeInstances` @L6996–6999 (unscopable); `ec2:Attribute`/`ec2:Attribute/${AttributeName}` @L10051–10052; EC2-Fleet LT caveat ~L5114.

---
*Online == offline verified byte-identical 2026-10-15 for the target page (two independent fetches). `list_ec2` reference offline-authoritative (online truncation prevents row-level byte-parity confirmation — a tool limitation, not drift).*
