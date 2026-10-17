# EC2 Instance Termination (Troubleshoot `shutting-down` / force-terminate) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesShuttingDown.html` (+ `.md`), and the adjacent pages it links/implies: `instance-terminate-methods`, `terminating-instances`, `how-ec2-instance-termination-works`, `Using_ChangingDisableAPITermination`, `Using_ChangingInstanceInitiatedShutdownBehavior`, `preserving-volumes-on-termination`, `troubleshooting-launch` (#instance-terminates-immediately), `ec2-instance-lifecycle`, `Stop_Start`, `ec2-auto-scaling-instance-protection`, `as-instance-termination`, `spot-fleet-prerequisites`, `ec2-fleet-prerequisites`, `spot-instance-termination-notices`, `rebalance-recommendations`; API refs `API_TerminateInstances`, `API_ModifyInstanceAttribute`; the AWS Service Authorization Reference EC2 action/condition-key table (`list_ec2.html` — **note the filename is `list_ec2.html`, NOT `list_amazonec2.html`, which 302-redirects to a JS SPA dead end**); AWS-managed policy `AutoScalingServiceRolePolicy`; SLRs `AWSServiceRoleForAutoScaling` / `AWSServiceRoleForEC2SpotFleet` / `AWSServiceRoleForEC2Fleet`.
Status: **documentation-derived hypotheses only; nothing tested against a live account.** The `/work/aws-docs/docs` mirror is missing the newest (July-2025) termination pages — online `.md` variants were used throughout.
Companion plan: `TroubleshootingInstancesStopping-attack-research-plan.md` (the stop/force-stop sibling). The IAM-granularity-gap, in-account root-volume-swap, and shared/public-snapshot leads there are the stop-side mirror of this plan; a hunter should run both together — the `Force`/`SkipOsShutdown` flags are the **same primitive on `TerminateInstances`**.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The highest-yield directions are (a) the **IAM granularity gap** around the *new* (July 2025) `Force`/`SkipOsShutdown` terminate flags — **confirmed by an exhaustive 148-key condition-key sweep**; (b) the **guest→control-plane termination** path via `InstanceInitiatedShutdownBehavior=terminate`, which `disableApiTermination` explicitly does **not** block; (c) the **`DeleteOnTermination` same-account sleeper primitive**; and (d) the **unconditioned (`Resource:"*"`) terminate capability** of the Auto Scaling / Fleet service-linked roles reachable by cross-team scale-in.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the EC2/EBS fleet, a shared Nitro host, reclaimed-host data, a `aws.ec2`-sourced control signal), stop, preserve evidence, flag for AWS-Security disclosure. Do **not** terminate, force-terminate, or destroy data on any instance you do not own in an authorized test account. Terminate is **permanent and irreversible** (doc warning, `instance-terminate-methods`) — every destructive oracle below must use synthetic canary instances/volumes you own.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Prove an admin cannot bound the data-destructive terminate variants.** Show any principal holding plain `ec2:TerminateInstances` can set `Force` and/or `SkipOsShutdown` (irreversible graceful-shutdown bypass → unflushed FS caches/metadata, lost in-flight IO, skipped shutdown scripts) and that **no IAM condition key exists to deny only the destructive variants** while allowing a normal terminate.
2. **Prove the guest→control-plane termination boundary.** Show that a principal with only OS/guest shell (no EC2 IAM) can drive the control plane to `terminate` the instance (destroying `DeleteOnTermination=true` volumes) when `InstanceInitiatedShutdownBehavior=terminate`, and that `disableApiTermination` does **not** block it — a two-tier privilege crossing.
3. **Prove the `DeleteOnTermination` sleeper primitive.** Show a same-account principal can silently flip `DeleteOnTermination=true` on another team's attached data volume via `ModifyInstanceAttribute`, so a later (legitimate-looking) terminate destroys that data — the destructive act and the weaponization act are temporally decoupled.
4. **Prove / refute force-vs-termination-protection.** Determine whether `--force`/`--skip-os-shutdown` honors `disableApiTermination` (expected: yes, by shared code path — but **never explicitly stated for the force path**; doc gap), and enumerate the documented protection *exclusions* an operator/attacker leans on.
5. **Prove the cross-team auto-termination blast radius.** Show that a principal holding broad `autoscaling:SetDesiredCapacity`/`UpdateAutoScalingGroup` (no `ec2:TerminateInstances` at all) can drive scale-in on another team's ASG, and the SLR's unconditioned `Resource:"*"` terminate carries it out.
6. **Characterise detection gaps:** force/skip terminate carries no distinct CloudTrail `eventName`; a guest-initiated terminate may not surface as a `TerminateInstances` call attributed to any principal.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 control-plane API (SigV4) + console + CLI/PowerShell. Core actions on this page: `TerminateInstances` (flags `Force`, `SkipOsShutdown`, `DryRun`), `ModifyInstanceAttribute` (`DisableApiTermination`, `InstanceInitiatedShutdownBehavior`, `BlockDeviceMapping.DeleteOnTermination`), `DescribeInstances` (`StateReason`), plus the auto-scaling control plane (`autoscaling:*`, Spot/EC2 Fleet) acting via service-linked roles.

**What is a "resource" and its identifier shape.** `instance` ARN (id `i-...`), `volume` (`vol-...`), `snapshot` (`snap-...`), `image`/AMI (`ami-...`), `AutoScalingGroup` (name/ARN). All account-scoped. EBS volumes & instances are **not** cross-account-shareable (snapshots/AMIs are). The destructive flags are **request parameters**, not separately-permissioned sub-resources.

**Identity / privilege.** IAM principals via SigV4 for the control plane. A *second, lower* privilege tier matters here: a **guest/OS shell** on the instance (no AWS IAM) can trigger a terminate via `InstanceInitiatedShutdownBehavior`. A *third* tier is **AWS service principals** (`autoscaling.amazonaws.com`, `spotfleet.amazonaws.com`, EC2-Fleet SLR) that terminate "on your behalf."

**Four documented termination methods** (`instance-terminate-methods`): default / terminate-with-skip-OS-shutdown / force / force-with-skip-OS-shutdown. `Force` = "attempt a default termination first; if the instance fails to terminate, then forcibly terminate" (a *fallback-escalation*, not an unconditional skip). `SkipOsShutdown` = "bypass the graceful OS shutdown" (independent boolean, combinable with `Force`).

**State / trigger machine (heart of this page).**
```
  running ──TerminateInstances(default)──▶ shutting-down ──(graceful OS shutdown: flush FS caches+metadata)──▶ terminated
     │  │        │
     │  │        └── stuck in shutting-down > several hours ──▶ EC2 forcibly terminates (AWS-side)
     │  │
     │  ├── TerminateInstances(SkipOsShutdown=true) ─ graceful-shutdown bypass ─▶ terminated   [NEW 2025-07-23]
     │  ├── TerminateInstances(Force=true) ─ default-then-forcible fallback ─────▶ terminated   [NEW 2025-07-31]
     │  │        (console button ONLY shown when state == `stopping`; CLI/SDK accept it from more states)
     │  │
     │  └── (guest) `shutdown -h` / `poweroff`  with InstanceInitiatedShutdownBehavior=terminate ─▶ terminated
     │             (NOT blocked by disableApiTermination; instance-store-root ALWAYS terminates on guest shutdown)
     │
     └── AWS Auto Scaling / EC2 Fleet / Spot Fleet SLR ──TerminateInstances(Resource:"*")──▶ terminated
                (scale-in / health-check replacement / AZ rebalance / Spot interruption / Capacity-Block end)
```
On terminate: all `DeleteOnTermination=true` EBS volumes are **permanently deleted**; all instance-store data is **permanently lost** (`instance-terminate-methods` warning).

**[NEW] markers (DocumentHistory, UserGuide).** `SkipOsShutdown` for terminate = **2025-07-23**; `Force` terminate = **2025-07-31**. Both ship in the same ~1-week window → least-reviewed surface on the page → Step-5 priority #1/#2.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| IAM principal with `ec2:TerminateInstances` | integrity of an instance's filesystem / in-flight IO | `Force` / `SkipOsShutdown` flags | A data-destructive terminate executes with **no IAM condition key able to deny only the destructive variants** → granularity gap (confirmed from the 148-key sweep). |
| **Guest/OS shell** (no AWS IAM) | EC2 control-plane terminate + `DeleteOnTermination` volume destruction | `shutdown`/`poweroff` with `InstanceInitiatedShutdownBehavior=terminate` | A guest with zero IAM terminates the instance and destroys EBS data; `disableApiTermination` does **not** block it (verbatim doc exclusion). |
| Same-account principal B (wrong team) | another team's **attached data volume** destruction-on-terminate | `ModifyInstanceAttribute` `BlockDeviceMapping.DeleteOnTermination=true` | B flips the flag on A's volume ("owned by the caller" = account-level only), later terminate destroys A's data. |
| Principal holding only `autoscaling:*` (no `ec2:TerminateInstances`) | another team's running instances | lower desired-capacity / metric manipulation on a shared ASG → SLR terminates | A's instances terminated by `AWSServiceRoleForAutoScaling` (`Resource:"*"`) at B's command, with no terminate grant on B. |
| Caller / 3P service | `aws-ec2-spot-fleet-tagging-role` | confused-deputy on a non-SLR role whose trust policy lacks `aws:SourceArn`/`SourceAccount` by default | Spot Fleet acting under a role the caller should not be able to invoke cross-account. |
| Any customer surface | **AWS service plane / shared Nitro host** | stuck-terminate host fault, host reclaim, Spot capacity reclaim, `aws.ec2` control signals | **HARD STOP** — any cross-tenant data, shared-host reach, or fleet identity. |

---

## 4. API / Interface Inventory

| Name | Mutating | Internet-callable | Authorized callers | Flags / notable params | Notes → lens |
|---|---|---|---|---|---|
| `TerminateInstances` | Yes | Yes | holder of `ec2:TerminateInstances` on `instance*` | `Force` **[NEW 2025-07-31]**, `SkipOsShutdown` **[NEW 2025-07-23]**, `DryRun`, up to 1000 IDs | No condition key gates Force/Skip; one `eventName` for all variants. → **S, R, U, X, O** |
| `ModifyInstanceAttribute` | Yes | Yes | `ec2:ModifyInstanceAttribute` | `DisableApiTermination`, `InstanceInitiatedShutdownBehavior`, `BlockDeviceMapping.DeleteOnTermination` | "volume must be owned by the caller" (account-level). Eventual consistency. → **A, S, U** |
| `DescribeInstances` | No | Yes | `ec2:DescribeInstances` | returns `StateReason` (`Code`/`Message`) | Termination-reason strings (`Client.VolumeLimitExceeded`, `Client.InternalError` for KMS) are an info/enumeration surface. → **A, H, O** |
| Console "Force terminate instance" | Yes | Yes (console) | same IAM | **button only shown when state == `stopping`**; "Skip OS shutdown" checkbox region-gated | Capability delta vs CLI/SDK — console-only guardrails are bypassable. → **X, U** |
| `terminate-instance-in-auto-scaling-group` | Yes | Yes | `autoscaling:TerminateInstanceInAutoScalingGroup` | ignores EC2 termination protection & scale-in protection | documented scale-in-protection bypass. → **E, U** |
| `autoscaling:SetDesiredCapacity` / `UpdateAutoScalingGroup` | Yes | Yes | `autoscaling:*` holder | drives scale-in → SLR terminates | cross-team blast radius if `Resource:"*"`. → **A, E, B** |
| Auto Scaling / Spot Fleet / EC2 Fleet SLRs | Yes | n/a (service) | the service principal only | `ec2:TerminateInstances` with **`Resource:"*"`, no Condition** | unconditioned fleet terminate; correctness is service-side logic only. → **B, E, R** |

**Console-hidden knob (Step-3 sweep):** CLI/SDK accept `Force` from `running`/`pending`/`stopped`; the console only exposes "Force terminate" in `stopping` (and the "Skip OS shutdown" checkbox only where regionally rolled out). The **most-permissive path is the least-visible one** — a break-glass/change-management process that assumes "console-only = safe" is bypassable via CLI/SDK.

---

## 5. Recommended Areas of Focus

### Area 1 — [NEW, PRIORITY] IAM granularity gap: no condition key can deny `Force` / `SkipOsShutdown` terminate (Lens S / R / U) — CONFIRMED from docs
**Background.** `Force` (2025-07-31) and `SkipOsShutdown` (2025-07-23) are boolean request parameters on `TerminateInstances`. Both bypass the graceful OS shutdown; AWS's own text: terminate is "permanent and irreversible … EBS volumes configured to be deleted on termination are also permanently deleted … instance store data is permanently lost," and skip-OS-shutdown means FS caches/metadata are not flushed and in-flight IO is lost.
**Security Concern.** An exhaustive sweep of the Service Authorization Reference (`list_ec2.html`) found the full `ec2:TerminateInstances` condition-key set to be: `aws:ResourceTag/*`, `ec2:AvailabilityZone(Id)`, `ec2:CpuOptionsAmdSevSnp`, `ec2:EbsOptimized`, `ec2:InstanceAutoRecovery`, `ec2:InstanceBandwidthWeighting`, `ec2:InstanceID`, `ec2:InstanceMarketType`, `ec2:InstanceMetadataTags`, `ec2:InstanceProfile`, `ec2:InstanceType`, `ec2:ManagedResourceOperator`, `ec2:MetadataHttp*`, `ec2:PlacementGroup`, `ec2:ProductCode`, `ec2:Region`, `ec2:ResourceTag/*`, `ec2:RootDeviceType`, `ec2:Tenancy`. A case-insensitive grep of the whole 148-key EC2 table for `force`/`skip`/`shutdown`/`enforce` returned **zero** matches. **Every key scopes *which* instance, not *how* it is terminated.** No `ec2:Force` / `ec2:SkipOsShutdown` key and no separate action exist — an admin can only allow-all or deny-all terminates; least-privilege cannot express "normal terminate but never the data-destructive bypass."
**High-level Test Scenarios (falsifiable claims).**
- *Claim:* A principal granted only `ec2:TerminateInstances` can set `Force=true`/`SkipOsShutdown=true` with no extra authz. → *Oracle:* `aws ec2 terminate-instances --force --skip-os-shutdown` returns 200 under a scoped role holding exactly `ec2:TerminateInstances`, against a canary instance you own; `DryRun` returns `DryRunOperation` (caller-IAM only — **not** a destructive confirmation). *Severity:* Medium (AWS-owned least-privilege granularity gap; a routine "operators may terminate" grant silently includes an irreversible data-destruction capability).
- *Claim:* No `Condition` permits a normal terminate and denies the skip/force variant. → *Oracle:* `iam:SimulateCustomPolicy` (safe, no resources touched) with a `Deny` keyed on a hypothetical `ec2:Force` — the simulator ignores the undefined key, confirming absence. *Severity:* High for the gap narrative.
**Doc evidence:** `API_TerminateInstances` Force/SkipOsShutdown fields; `list_ec2.html` condition-key table. **Severity-if-true:** Medium (reportable AWS-owned granularity gap).

### Area 2 — [PRIORITY] Guest→control-plane termination; `disableApiTermination` does NOT block it (Lens E / Business-logic / U) — HIGH
**Background.** `Using_ChangingInstanceInitiatedShutdownBehavior`: "when you initiate a shutdown from an EBS-backed instance (using `shutdown` or `poweroff`), the instance stops. You can change this … so the instance terminates instead by changing the `InstanceInitiatedShutdownBehavior` attribute." `Using_ChangingDisableAPITermination` (verbatim exclusion): "The `DisableApiTermination` attribute doesn't prevent you from terminating an instance by initiating shutdown from the instance … when the `InstanceInitiatedShutdownBehavior` attribute is set to `terminate`." `ec2-instance-lifecycle`: "Operating system shutdown commands **always** terminate an instance with an instance store root volume" (no attribute to disable, no stop possible).
**Security Concern.** A principal with only a **guest/OS shell** (compromised app, user-data/SSM script, a lower trust tier with no AWS IAM) can drive the control plane to terminate the instance and destroy `DeleteOnTermination=true` EBS volumes — crossing from OS tier into a control-plane state change — and the one guardrail AWS markets against accidental termination (`disableApiTermination`) explicitly does not apply. The realistic chain is two-stage: (a) any principal with `ec2:ModifyInstanceAttribute` sets `InstanceInitiatedShutdownBehavior=terminate` (or it is already so), then (b) a *separate* guest-only actor triggers it.
**High-level Test Scenarios.**
- *Claim:* On a protected (`disableApiTermination=true`) EBS-backed instance with `InstanceInitiatedShutdownBehavior=terminate`, `shutdown -h now` from inside the guest terminates it while a `TerminateInstances` API call is still rejected with the protection error. → *Oracle:* on your own canary instance, observe state → `shutting-down`/`terminated` from the guest command while the API refuses; confirm the exclusion. *Severity:* High (guest-tier → control-plane data-destruction, not blocked by the protection control).
- *Claim:* An instance-store-root canary terminates on any guest `shutdown`, with no attribute able to prevent it. → *Oracle:* reproduce; `halt` must NOT terminate (ruling out false positive — doc: `halt` places CPU in HLT, instance keeps running). *Severity:* Medium–High.
**Doc gap:** none of the pages state whether a guest-initiated terminate appears in CloudTrail as `TerminateInstances`, or to which principal it is attributed — confirm live for the detection-evasion angle.
**Doc evidence:** `Using_ChangingInstanceInitiatedShutdownBehavior`, `Using_ChangingDisableAPITermination`, `ec2-instance-lifecycle`, `Stop_Start`. **Severity-if-true:** High.

### Area 3 — [PRIORITY] `DeleteOnTermination` same-account sleeper primitive (Lens A / S / U) — HIGH
**Background.** `API_ModifyInstanceAttribute`: "Modifies the `DeleteOnTermination` attribute for volumes that are currently attached. **The volume must be owned by the caller.** If no value is specified … the default is `true` and the volume is deleted when the instance is terminated." `preserving-volumes-on-termination` default table shows a foot-gun: a **data volume attached at launch via CLI defaults to `Delete`** (console defaults to Preserve). The attribute is modifiable on a running instance (no stop required for `DeleteOnTermination`).
**Security Concern.** "Owned by the caller" is **account-level** — the doc states no instance-ownership / tag / team check tying the volume to the instance's owner. In an org where many engineers hold broad `ec2:ModifyInstanceAttribute`, a second-team principal can silently flip `DeleteOnTermination=true` on another team's attached data volume. The destructive effect is deferred to the *next* terminate (which may be legitimate/unrelated), decoupling the weaponization from the damage → a quiet pre-positioning / sleeper primitive that evades point-in-time detection.
**High-level Test Scenarios.**
- *Claim:* Principal B (same account, generic `ec2:ModifyInstanceAttribute`, no resource-tag scoping) can set `DeleteOnTermination=true` on Principal A's instance's data volume. → *Oracle:* under two scoped roles you own in a test account, B runs `modify-instance-attribute --instance-id <A's instance> --block-device-mappings '[{"DeviceName":"/dev/xvdb","Ebs":{"DeleteOnTermination":true}}]'`; confirm 200 with no instance-ownership check; then terminate and confirm the (canary-data) volume is destroyed. *Severity:* High (silent same-account cross-team data-destruction primitive).
- *Claim:* `aws:ResourceTag`/`ec2:ResourceTag` *could* scope this but a typical broad grant does not. → *Oracle:* `iam:SimulateCustomPolicy` showing a tag-scoped variant denies the cross-team modify while a plain `ec2:ModifyInstanceAttribute` allows it.
**Doc gap:** the EC2 IAM "actions/resources/condition-keys" scoping specifically for the `BlockDeviceMapping`/`DisableApiTermination` sub-attributes of `ModifyInstanceAttribute` was not fully resolved — confirm whether resource-level conditions can bound it.
**Doc evidence:** `API_ModifyInstanceAttribute`, `preserving-volumes-on-termination`. **Severity-if-true:** High.

### Area 4 — Force / Skip vs termination protection; documented exclusions (Lens U) — mostly refute, enumerate gaps
**Background.** `instance-terminate-methods` places "**Note** You can't terminate an instance if termination protection is turned on" directly above the four-method table (default/skip/force/force+skip), implying it applies to all. But `API_TerminateInstances` documents the protection-check and the force/skip logic as **separate, never-cross-referenced** paragraphs, and `Using_ChangingDisableAPITermination` never mentions `Force`/`SkipOsShutdown` at all. Documented protection **exclusions** (verbatim): OS-initiated shutdown with `InstanceInitiatedShutdownBehavior=terminate` (Area 2); scheduled retirement events ("Enabling termination protection does not prevent AWS from terminating the instance when there is a scheduled event"); Auto Scaling unhealthy/scale-in ("does not prevent Amazon EC2 Auto Scaling from terminating an instance when the instance is unhealthy or during scale-in events"); **Spot Instances cannot be protected at all** ("You can't enable termination protection for Spot Instances").
**Security Concern.** Confirm force/skip is a shutdown-execution *modifier* layered on normal authz (expected: it does **not** bypass protection — but this is inference from general boilerplate, never explicitly asserted for the force code path → genuine doc gap). The real operational gaps are the enumerated exclusions + the attribute's eventual consistency.
**High-level Test Scenarios.**
- *Claim:* `terminate-instances --force --skip-os-shutdown` against an instance with `disableApiTermination=true` is refused exactly like a normal terminate. → *Oracle:* on your own canary, expect `OperationNotPermitted`/protection error, not a terminate. *Severity:* **Critical if refuted** (force bypasses the marketed guardrail → data-loss primitive defeats accidental-termination protection); Low/Informational if it holds.
- *Claim:* an eventual-consistency window on `ModifyInstanceAttribute(DisableApiTermination=true)` lets a terminate land just after protection was "enabled." → *Oracle:* race enable→terminate on a canary; observe the window.
**Doc evidence:** `instance-terminate-methods`, `terminating-instances`, `Using_ChangingDisableAPITermination`, `API_TerminateInstances`. **Severity-if-true:** Critical (bypass) / else Informational.

### Area 5 — Cross-team auto-termination blast radius; SLR over-privilege (Lens A / E / B / R) — HIGH if confirmed
**Background.** Target page: EC2 Auto Scaling, EC2 Fleet, or Spot Fleet "scale your computing resources automatically … To stop … set its capacity to 0 or delete it." The `AutoScalingServiceRolePolicy` (managed, fetched in full) grants `ec2:TerminateInstances` (among Run/Start/Stop) with **`Resource:"*"` and no `Condition`**; trust = `autoscaling.amazonaws.com` only. Spot Fleet / EC2 Fleet SLRs are authored identically ("request, launch, terminate … on your behalf"). Scale-in happens on dynamic-policy metric change **or** manual desired-capacity decrease (`as-instance-termination`). `ec2-auto-scaling-instance-protection` lists scale-in-protection exclusions verbatim: health-check replacement, Spot interruption, Capacity-Block end, `terminate-instance-in-auto-scaling-group`, and manual console/CLI/API termination.
**Security Concern.** The IAM layer imposes **no boundary** on the SLR terminate — correctness depends entirely on the service's own which-instance-belongs-to-which-ASG logic (confused-deputy-adjacent). An ASG is an account/region-scoped resource; membership/blast-radius lives in ASG state, not in IAM on the *calling* principal. A principal with broad `autoscaling:SetDesiredCapacity`/`UpdateAutoScalingGroup` (`Resource:"*"`), holding **no** `ec2:TerminateInstances`, can shrink another team's ASG (or influence a shared CloudWatch metric a target-tracking policy consumes) and have the SLR terminate that team's instances.
**High-level Test Scenarios.**
- *Claim:* Principal B with only `autoscaling:SetDesiredCapacity`/`UpdateAutoScalingGroup` (`Resource:"*"`) can shrink Team A's ASG and cause A's instances to be terminated by the SLR. → *Oracle:* in an authorized multi-principal test account, grant B exactly that, lower A's ASG desired capacity, confirm A's canary instances terminate — with B holding no terminate permission. *Severity:* High (same-account lateral availability/data-destruction via a shared control-plane resource).
- *Claim:* `terminate-instance-in-auto-scaling-group` and manual API termination are documented bypasses of scale-in protection. → *Oracle:* doc-confirmed; verify the protected canary still terminates via these paths.
**Doc gap:** whether `autoscaling:UpdateAutoScalingGroup`/`SetDesiredCapacity`/`SetInstanceProtection` support resource-level (`Resource` ARN) scoping that a well-run account *could* use to prevent the cross-team path — resolve against the Auto Scaling Service Authorization Reference before rating mitigability.
**Doc evidence:** `TroubleshootingInstancesShuttingDown` auto-scaling section, `AutoScalingServiceRolePolicy`, `as-instance-termination`, `ec2-auto-scaling-instance-protection`, `spot-fleet-prerequisites`, `ec2-fleet-prerequisites`. **Severity-if-true:** High (confirmed live); Medium–High as a structural design fact.

### Area 6 — Spot Fleet confused-deputy on the tagging role (Lens B)
**Background.** `spot-fleet-prerequisites` has an explicit "Cross-service confused deputy prevention" section: "We recommend that you use the `aws:SourceArn` and `aws:SourceAccount` global condition context keys in the `aws-ec2-spot-fleet-tagging-role` trust policy" — framed as **optional hardening**, implying the console-wizard-generated trust policy trusts `spotfleet.amazonaws.com` **without** these keys by default. EC2 Fleet's prerequisites page has **no** equivalent callout (its role is a true SLR, assumable only by the service) — a doc asymmetry worth noting.
**Security Concern.** The `aws-ec2-spot-fleet-tagging-role` is a customer-created (non-SLR) role whose default trust policy lacks source-scoping; AWS deems the confused-deputy risk real enough to warn. User `iam:PassRole` is narrow (scoped to the role ARN pattern) and does not itself grant terminate power — the SLR does the terminating.
**High-level Test Scenarios.**
- *Claim:* the console-wizard-created `aws-ec2-spot-fleet-tagging-role` trust policy omits `aws:SourceArn`/`aws:SourceAccount` by default. → *Oracle:* create it via the wizard in a sandbox, inspect the generated trust policy. *Severity:* Medium (AWS-acknowledged hardening gap; needs live confirmation of the default).
**Doc evidence:** `spot-fleet-prerequisites` §Cross-service confused deputy prevention. **Severity-if-true:** Medium.

### Area 7 — "Instance terminates immediately": KMS / StateReason surface (Lens H / A / O)
**Background.** `troubleshooting-launch` #instance-terminates-immediately lists causes an instance goes `pending`→`terminated`: EBS volume limits exceeded; a **corrupted EBS snapshot**; **root EBS volume encrypted and the caller lacks permission to the KMS key**; **an AMI block-device snapshot encrypted and the caller lacks KMS access**; an S3-backed AMI missing an `image.part.*` part. The reason is read from `StateReason` (`Code`/`Message`, e.g. `Client.VolumeLimitExceeded: Volume limit exceeded`, `Client.InternalError: Client error on launch` = KMS access failure).
**Security Concern.** (a) The KMS-access-on-launch dependency is a cross-service reachability touchpoint (`CreateVolume`/`RunInstances` → EBS calls `kms:Decrypt` under the key policy) — route to the companion plan's EBS/KMS leads (Lens T/H). (b) `StateReason` strings differ by failure class — a potential low-value **enumeration/info oracle** (does a cross-account/shared encrypted snapshot or AMI yield a distinguishable `Client.InternalError` vs not-found?). (c) `StateReason` is retrievable by any `ec2:DescribeInstances` holder.
**High-level Test Scenarios.**
- *Claim:* launching from a shared/public encrypted snapshot/AMI without KMS grant yields a distinguishable `Client.InternalError` immediate-terminate, usable to confirm the resource exists + is encrypted. → *Oracle:* with two test accounts you own, share a canary encrypted snapshot without the key grant, launch, read `StateReason`. *Severity:* Low–Informational (info-leak oracle); escalates only if it reveals another account's resource existence/attributes.
**Doc evidence:** `troubleshooting-launch` #troubleshooting-launch-internal; `volume_limits`. **Severity-if-true:** Low–Informational.

### Area 8 — Detection gap: force/skip terminate carries no distinct event name (Lens O)
**Background.** `Force`/`SkipOsShutdown` are request parameters of the single `TerminateInstances` action — there is no `ForceTerminateInstances` operation. By AWS's universal CloudTrail convention, the expected shape is `eventName: TerminateInstances` with nested `requestParameters.force` / `requestParameters.skipOsShutdown`.
**Security Concern.** Detections keyed on `eventName` alone cannot distinguish a routine terminate from a data-destructive force/skip terminate; a guest-initiated terminate (Area 2) may not surface as a principal-attributed `TerminateInstances` at all.
**High-level Test Scenarios.** *Claim:* `requestParameters.force`/`skipOsShutdown` are the only CloudTrail differentiators; confirm exact JSON key casing. → *Oracle:* read a real CloudTrail event in a test account (the EC2 CloudTrail-logging doc page 404'd during recon — casing is **unconfirmed**; do not ship a detection rule on inferred casing). **Severity-if-true:** Medium (detection-engineering enabler).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Data-destructive terminate usable without extra privilege | `TerminateInstances` Force/Skip | IAM — but **no condition key exists** to bound the flags (confirmed) |
| Guest-tier → control-plane terminate + EBS destruction | `InstanceInitiatedShutdownBehavior=terminate` | `disableApiTermination` — explicitly **does not** block this path |
| Same-account cross-team data destruction (deferred) | `ModifyInstanceAttribute DeleteOnTermination` | resource-level IAM / tag scoping — **not required** by the API ("owned by the caller" = account-level) |
| Force bypassing termination protection | `TerminateInstances --force` + `disableApiTermination` | protection attribute gate (expected to hold; **never explicitly stated for the force path**) |
| Cross-team auto-termination via shared ASG / metric | `autoscaling:SetDesiredCapacity` + SLR terminate | ASG resource-level IAM — **mitigability unconfirmed**; SLR terminate is `Resource:"*"` |
| Confused deputy on Spot Fleet tagging role | `aws-ec2-spot-fleet-tagging-role` trust policy | `aws:SourceArn`/`SourceAccount` — **optional, not default** |
| KMS-less launch immediate-terminate as info oracle | `RunInstances`/`StateReason` | key-policy access control (fail-closed by design) |
| Detection evasion of destructive / guest terminates | CloudTrail | `requestParameters` only (no distinct `eventName`); guest path attribution unknown |
| Cross-tenant / shared-host effect from stuck-terminate host fault, Spot reclaim | underlying Nitro host / EC2 capacity plane | Nitro isolation (general); **HARD STOP** if reached |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Spot interruption / rebalance signal spoofing** — the 2-minute notice and rebalance recommendation are emitted server-side by `aws.ec2` (EventBridge + read-only IMDS path `/latest/meta-data/spot/instance-action`); non-AWS principals cannot publish under the reserved `aws.ec2` source. Service-plane; **HARD STOP** / out of scope here (IMDS-response forgery is a different surface).
- **Shared Nitro host** infrastructure, host-reclaim media sanitization, instance-store remanence between tenants, Spot capacity reclaim internals — AWS service-plane; **HARD STOP** if ever reached. Not customer-testable from docs.
- **A customer destroying their own data** with force/skip on their own instance — intended, self-inflicted. In scope only when it reaches *another* principal's/team's instance or the *granularity gap* itself.
- **Customer-authored** over-broad IAM — footgun, out of scope. (The AWS-managed `AutoScalingServiceRolePolicy`/SLRs are **AWS-authored** → in scope, Tier-2.)
- **IMDS on managed hosts**, DNS rebinding against private-only endpoints, product/feature-parity requests.
- **Billing "camp in `shutting-down` to avoid charges"** — unsupported by docs: billing stops *at* `shutting-down`, but `shutting-down` is a transient EC2-controlled state, not an attacker-held hold; EC2 forcibly terminates a stuck instance after several hours. No attacker-reachable billing primitive.

---

## 8. Null hypotheses / doc gaps (surfaces checked; confirm before trusting)
- **SSRF (Lens G):** N/A — read `TroubleshootingInstancesShuttingDown`, `instance-terminate-methods`, `terminating-instances`, `Using_ChangingDisableAPITermination`, `troubleshooting-launch`; no field the service dereferences server-side (no `*Url`/webhook/import/fetch). True null for this page set.
- **Prompt injection / LLM (Lens K):** N/A — no agent/LLM in this flow.
- **Untrusted upload (Lens Q):** N/A — no upload/parse field on this surface (snapshot/AMI ingest is covered in the companion stop plan's Area 4).
- **OAuth/3P (Lens J), Attestation (Lens W), Canonicalization/parser-diff (Lens BB), Trusted-upstream-context (Lens CC), Cache-key (Lens DD), JWT (Lens FF), Transport/TLS (Lens Y):** N/A for this control-plane action set — no multi-parser edge, authorizer, cache, token, or custom transport on this page.
- **Force-vs-`disableApiTermination` (Lens U) — DOC GAP:** general "can't terminate if protected" boilerplate is never re-asserted for the force code path; `API_TerminateInstances` documents protection-check and force/skip as unrelated paragraphs. Confirm live (Area 4) — Critical if a bypass exists.
- **Guest-initiated terminate CloudTrail attribution (Lens O) — DOC GAP:** no page states whether an OS-initiated terminate appears as `TerminateInstances` or to which principal — confirm live.
- **`ModifyInstanceAttribute` sub-attribute IAM scoping (Lens S) — DOC GAP:** whether resource-level/tag conditions can bound `DeleteOnTermination`/`DisableApiTermination`/`InstanceInitiatedShutdownBehavior` sub-attributes specifically — resolve against `list_ec2.html` action detail.
- **Auto Scaling resource-level permission support (Lens A/E) — DOC GAP:** whether `autoscaling:SetDesiredCapacity`/`UpdateAutoScalingGroup` support `Resource` ARN scoping (needed to rate Area 5 mitigability) — resolve against the Auto Scaling Service Authorization Reference.
- **CloudTrail field casing (Lens O) — DOC GAP:** EC2 CloudTrail-logging doc page 404'd; `force`/`skipOsShutdown` key casing unconfirmed — do not ship a detection rule on inference.
- **Stuck-terminate host-fault cross-tenant blast radius (Lens V/L) — DOC GAP:** troubleshooting/lifecycle pages are single-tenant; the "stuck > several hours, EC2 forcibly terminates" host-fault scenario's effect on co-resident tenants is addressed only by general Nitro isolation. Treat as doc gap, **not** a confirmed vuln; **HARD STOP** on any cross-tenant observation.

---

### Kill-chain note
The sharpest chain here is **Area 3 → Area 1/2**: a same-account wrong-team principal silently flips `DeleteOnTermination=true` on a target workload's data volume (Area 3, deferred/undetected), then either (a) uses the unbounded `Force`/`SkipOsShutdown` grant (Area 1) to force a dirty terminate that maximizes on-disk loss, or (b) if lacking `ec2:TerminateInstances`, drives a shared-ASG scale-in (Area 5) so the SLR terminates the target — the destructive flag it pre-set now permanently deletes the data. A same-account **pre-position-then-trigger** integrity-and-availability chain, rated at the end state (High), all enabled by AWS-authored defaults (no condition-key guardrail on the flags, account-level-only ownership on `DeleteOnTermination`, `Resource:"*"` on the fleet SLRs). Independently, **Area 2** is a standalone High: a guest-tier compromise with zero AWS IAM destroys EBS data through a control-plane path the marketed protection control does not cover.
