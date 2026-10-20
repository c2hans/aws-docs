---
title: EC2 `ResetInstanceAttribute` — Attribute Security Semantics (Area: area_attribute_semantics)
status: documentation-derived hypotheses only — nothing tested against a live AWS account
---

# EC2 `ResetInstanceAttribute` — Attribute Security Semantics Research Plan

**Target doc page:** `https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ResetInstanceAttribute_section.html` (local mirror: `docs/ec2/latest/devguide/example_ec2_ResetInstanceAttribute_section.md`), plus the API it exercises.

**Sources read (all local mirror, byte-checked against the API-reference wording — no live calls):**
- `docs/AWSEC2/latest/APIReference/API_ResetInstanceAttribute.md`
- `docs/ec2/latest/devguide/example_ec2_ResetInstanceAttribute_section.md` (CLI + PowerShell examples)
- `docs/AWSEC2/latest/APIReference/API_ModifyInstanceAttribute.md`
- `docs/AWSEC2/latest/APIReference/API_DescribeInstanceAttribute.md`
- `docs/AWSEC2/latest/UserGuide/Using_ChangingDisableAPITermination.md`
- `docs/AWSEC2/latest/UserGuide/Using_ChangingInstanceInitiatedShutdownBehavior.md`
- `docs/AWSEC2/latest/UserGuide/ec2-stop-protection.md`
- `docs/vpc/latest/userguide/VPC_NAT_Instance.md`
- `docs/vpc/latest/userguide/work-with-nat-instances.md` (step 5, "Disable source/destination checks")
- `docs/config/latest/developerguide/ec2-enis-source-destination-check-enabled.md`
- `docs/linux/al2/ug/UserProvidedKernels.md` (HVM GRUB vs PV-GRUB, fallback-kernel semantics, `describe-instance-attribute --attribute kernel` / `modify-instance-attribute --kernel` example)
- `docs/AWSEC2/latest/UserGuide/instancedata-data-retrieval.md` (userData modify requires stopped instance)
- `docs/service-authorization/latest/reference/list_ec2.md` (action rows + condition-key table for `ResetInstanceAttribute`, `ModifyInstanceAttribute`, and the global `ec2:Attribute` / `ec2:Attribute/${AttributeName}` key definitions)
- `docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md` (`#attribute-key` section — worked examples of `ec2:Attribute` / `ec2:Attribute/${AttributeName}`)
- House framing reused (not duplicated) from `/work/aws-docs/ModifyInstanceCreditSpecification-attack-research-plan.md` and `/work/aws-docs/RebootInstances-attack-research-plan.md` (userData → IMDS → instance-profile-role privesc is a **confirmed exemplar** elsewhere; this document maps only what the **Reset** half contributes/omits, and the one asymmetry unique to this action pair).

**Status:** documentation-derived hypotheses only. Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions/Cost → Severity-if-true.** Unsettled items are marked "doc-gap — confirm surface first."

**Methodology caveat (repeated from sibling plans):** `DryRun` on any of these three actions reflects only the caller's **identity-policy** authorization (`DryRunOperation` vs `UnauthorizedOperation`), evaluated **before** resource-state/ownership resolution. It is not an ownership or state oracle — never treat a `DryRunOperation` success against someone else's instance as proof the real call will succeed.

---

## 0. What `ResetInstanceAttribute` actually is

Per `API_ResetInstanceAttribute.md`: *"Resets an attribute of an instance to its default value. To reset the `kernel` or `ramdisk`, the instance must be in a stopped state. To reset the `sourceDestCheck`, the instance can be either running or stopped."* `Attribute` is **Required**, `Valid Values: kernel | ramdisk | sourceDestCheck` — a 3-value enum, no `Value` parameter (you cannot choose what it resets *to*; only AWS's notion of "default" applies). Request shape is minimal: `InstanceId` + `Attribute` + `DryRun`. Response is boolean `return`. There is no batch array (unlike `ModifyInstanceCreditSpecification`'s `InstanceCreditSpecification.N`) — one instance, one attribute, per call.

The devguide CLI/PowerShell examples (`example_ec2_ResetInstanceAttribute_section.md`) show exactly this 3-value set for the CLI, but the **PowerShell V4 and V5 examples show five**: `sriovNetSupport`, `ebsOptimized`, `sourceDestCheck`, `disableApiTermination`, `instanceInitiatedShutdownBehavior` — two of which (`sriovNetSupport`, `ebsOptimized`) aren't even in `ModifyInstanceAttribute`'s reset-adjacent semantics the same way, and two (`disableApiTermination`, `instanceInitiatedShutdownBehavior`) are safety-relevant attributes whose "default" has direct security meaning. **This is the doc-vs-reference discrepancy named in the brief — Area 5 below.**

---

## 1. Area 1 — `sourceDestCheck` reset as a NAT/router/firewall outage primitive (Lens L — availability)

**Claim:** A principal holding only `ec2:ResetInstanceAttribute` (no `ec2:ModifyInstanceAttribute`, no `ec2:StopInstances`) can silently break packet forwarding for an entire VPC subnet by resetting `sourceDestCheck` on a NAT instance / router / firewall / VPN appliance back to its default (`true`), on a **running** instance, with no state-change precondition.

**Mechanism (doc evidence):**
- `API_ResetInstanceAttribute.md`: *"To reset the `sourceDestCheck`, the instance can be either running or stopped."* — no stop required, unlike kernel/ramdisk.
- Same page: *"The `sourceDestCheck` attribute controls whether source/destination checking is enabled. The default value is `true`... This value must be `false` for a NAT instance to perform NAT."*
- `work-with-nat-instances.md` step 5 (`#EIP_Disable_SrcDestCheck`): *"Each EC2 instance performs source/destination checks by default... However, a NAT instance must be able to send and receive traffic when the source or destination is not itself. Therefore, you must disable source/destination checks on the NAT instance."* The same page frames this as mandatory console step 5 of 7 in the NAT-instance build — i.e., it is load-bearing infrastructure configuration, not a cosmetic flag.
- `ec2-enis-source-destination-check-enabled.md` (AWS Config managed rule) exists specifically to detect ENIs with this check disabled going **out of compliance** (`NON_COMPLIANT` when disabled) for ENI types `lambda | aws_codestar_connections_managed | branch | efa | interface | quicksight` — confirming AWS treats this attribute as a security/compliance-relevant control surface in its own right, watched by automated guardrails. (Note: the Config rule's resource type is `AWS::EC2::NetworkInterface`, and `ResetInstanceAttribute` acts on the **instance**, not a named ENI — see "Preconditions" below for the multi-ENI caveat.)
- A NAT instance's whole function is to be "the source or destination of traffic it receives" that is not addressed to it — exactly what `sourceDestCheck=true` forbids. Resetting to default `true` is **the single cheapest API call that defeats this**, requiring neither `DryRun` evasion nor any secondary action.

**Confirm/Refute oracle:**
1. Launch a working NAT-instance topology per `work-with-nat-instances.md` (private-subnet instance routes 0.0.0.0/0 through the NAT instance; `sourceDestCheck=false` on the NAT instance's primary ENI). Confirm forwarding works (e.g., `curl` from the private instance succeeds).
2. As a second, separately-scoped IAM principal holding **only** `ec2:ResetInstanceAttribute` on the NAT instance's ARN (no `ec2:ModifyInstanceAttribute`, no stop/start rights), call `ResetInstanceAttribute(InstanceId=<nat>, Attribute=sourceDestCheck)` against the **running** NAT instance.
3. Immediately re-test forwarding from the private instance; also call `DescribeInstanceAttribute(Attribute=sourceDestCheck)` to confirm the flag flipped to `true`.
4. Oracle: forwarding breaks (private subnet loses internet/on-prem reachability) with a single unprivileged-for-anything-else API call, and `DescribeInstanceAttribute` shows the flip, timestamped to the `ResetInstanceAttribute` CloudTrail event.
5. Secondary oracle (multi-ENI edge case — doc-gap): `API_ModifyInstanceAttribute.md`'s **Note** states that modifying security groups on a multi-ENI instance via `ModifyInstanceAttribute` "can result in an error" and recommends `ModifyNetworkInterfaceAttribute` instead for ENI-scoped fields. `ResetInstanceAttribute` has no analogous documented caveat for `sourceDestCheck` on a multi-ENI instance — confirm whether `ResetInstanceAttribute(sourceDestCheck)` resets the check on the **primary** ENI only, or is rejected/ambiguous on an instance with secondary ENIs (the NAT how-to's own step 5 separately re-does the same action "If the NAT instance has a secondary network interface" via the ENI's own attribute page — implying the instance-level attribute and the ENI-level attribute are not the same knob once a second ENI exists). **doc-gap — confirm surface first.**

**Preconditions/Cost:** One IAM grant (`ec2:ResetInstanceAttribute` on the instance ARN — Write access level per `list_ec2.md`), zero cost to the caller, one API call, no `DryRun` needed since there's no "wrong instance" ambiguity once the ARN is known/authorized. No stop/reboot required — the outage is instantaneous and silent (no console warning, no CloudTrail-adjacent alarm by default).

**Severity-if-true:** **High (availability).** A single low-privilege action — one that a policy author might grant believing "it only resets to AWS defaults, how dangerous can that be" — causes a full routing/NAT/firewall outage for every resource behind that instance, with no secondary approval and no built-in blast-radius limiter (no batch cap matters here; cutting off one NAT instance can be an entire subnet or VPC's egress). This is a textbook "innocuous-sounding action name hides a security-relevant default" finding, in the same family as Area 1 of the `ModifyInstanceCreditSpecification` plan (action name gives no signal of blast radius) but for **availability** rather than cost.

---

## 2. Area 2 — `kernel` / `ramdisk` reset and boot integrity (Lens L — availability/integrity, stopped-instance precondition)

**Claim:** On a **stopped** PV (paravirtual) instance, `ResetInstanceAttribute(Attribute=kernel|ramdisk)` can revert a custom-kernel/ramdisk configuration to the AMI's registered default AKI/ARI, potentially producing an instance that fails to boot the OS the operator expects (incompatible kernel/initrd pairing) or that silently loses a security-relevant custom kernel (e.g., a hardened/patched kernel swapped in for compliance reasons).

**Mechanism (doc evidence):**
- `API_ResetInstanceAttribute.md`: kernel/ramdisk reset **requires stopped state** — the one documented precondition difference from `sourceDestCheck`.
- `API_ModifyInstanceAttribute.md` `Kernel`/`Ramdisk` params: *"We recommend that you use PV-GRUB instead of kernels and RAM disks"* — AWS flags this whole attribute pair as legacy/fragile.
- `UserProvidedKernels.md`: PV-GRUB "chain loads the kernel specified by your image's `menu.lst` file"; **"You can't specify an Amazon ramdisk image (ARI) when using a PV-GRUB AKI"** (a kernel/ramdisk **combination** constraint — resetting one without the other could produce an invalid combination); and *"Having a fallback kernel enables the instance to boot even if the new kernel isn't found"* — implying boot failure is a real, anticipated failure mode of kernel mismanagement, and the AMI's own `kernel`/`ramdisk` IDs (the "default" that Reset reverts to) are exactly the registered AKI/ARI pairing the current running config may have deliberately diverged from.
- The same page's worked CLI example (`describe-instance-attribute --attribute kernel` → `modify-instance-attribute --kernel <aki>` → `stop` → `modify` → `start`) demonstrates that a kernel change is itself a routine, expected operational action requiring a stop/start cycle — `ResetInstanceAttribute` collapses the "set to a specific known-good AKI" step into "set to whatever the AMI's registration default is," which the caller does not choose and may not know in advance.

**Confirm/Refute oracle:**
1. Launch a PV instance from an AMI with a known default `kernel`/`ramdisk` (AKI/ARI) registered; confirm via `DescribeInstanceAttribute(Attribute=kernel)` / `(Attribute=ramdisk)`.
2. Modify the instance's `kernel` (and/or `ramdisk`) to a different, deliberately-chosen value via `ModifyInstanceAttribute` while stopped (per the `UserProvidedKernels.md` worked example), confirm it boots.
3. As a principal holding only `ec2:ResetInstanceAttribute`, stop is still required (so this principal also needs `ec2:StopInstances`/`ec2:StartInstances`, or acts on an already-stopped instance) — call `ResetInstanceAttribute(Attribute=kernel)` then start the instance.
4. Oracle: `DescribeInstanceAttribute` shows the AMI-default AKI restored; instance either boots (if the default AKI is PV-GRUB-compatible — likely for modern AMIs) or fails to come up / comes up running the "wrong" (default, not operator-intended) kernel — either outcome is a documented-mechanism integrity/availability deviation from operator intent.
5. Edge case worth flagging as **doc-gap**: does `ResetInstanceAttribute(ramdisk)` succeed independently when `kernel` is a PV-GRUB AKI that (per `UserProvidedKernels.md`) "can't specify an ARI"? I.e., is there an inconsistent-combination state reachable only via Reset (reset ramdisk to a non-empty AMI-default ARI while kernel stays PV-GRUB)? **doc-gap — confirm surface first.**

**Preconditions/Cost:** Requires `ec2:ResetInstanceAttribute` plus the ability to get the instance into `stopped` state (either the caller also holds `ec2:StopInstances`/`StartInstances`, or they act during a maintenance window someone else created). Narrower blast radius than Area 1 (affects one instance's bootability, not a whole subnet's forwarding) — classified as **legacy-surface** risk since PV/kernel-ID instances are a shrinking minority of the fleet (most modern AMIs use HVM+GRUB, which per `UserProvidedKernels.md` doesn't use the `kernel`/`ramdisk` *instance attribute* mechanism at all).

**Severity-if-true:** **Medium** (availability/integrity, scoped to legacy PV fleets; not a cross-tenant or credential-reach issue — self-inflicted on the instance's own boot path, but still a real "one low-privilege action breaks a running production box the next time it's rebooted" footgun, and one an owner may not expect from a word like "Reset").

---

## 3. Area 3 — Twin-parity map: what Reset reaches vs. what only Modify/Describe reach (Lens X)

**Background.** `ResetInstanceAttribute`'s write surface is a strict, tiny subset of `ModifyInstanceAttribute`'s. Per the reference pages:

| Attribute | `ResetInstanceAttribute` (sets to AMI/account default) | `ModifyInstanceAttribute` (sets to caller-chosen value) | `DescribeInstanceAttribute` (read) |
|---|---|---|---|
| `kernel` | Yes (stopped only) | Yes (stopped only), to **any** AKI value | Yes |
| `ramdisk` | Yes (stopped only) | Yes (stopped only), to **any** ARI value | Yes |
| `sourceDestCheck` | Yes (running or stopped) | Yes, to `true`/`false` | Yes |
| `userData` | **No** (not in Reset's enum) | Yes — `SecureBlobAttributeValue`, base64, "changes the instance's user data" (stopped only per `instancedata-data-retrieval.md`) | Yes — `userData` is a response element |
| `groupSet` (security groups) | **No** | Yes — `GroupId.N` **"Replaces the security groups of the instance"** (full replace, not merge) | Yes — `groupSet` is a response element |
| `blockDeviceMapping` (`DeleteOnTermination`) | **No** | Yes — per-volume `DeleteOnTermination`, default `true` if unspecified on a fresh set | Yes (`blockDeviceMapping` response element) |
| `disableApiTermination` | **Not in API reference's enum** (`kernel\|ramdisk\|sourceDestCheck` only) — **but shown in the devguide PowerShell examples** | Yes — `AttributeBooleanValue`; default (unset) is **`false`/disabled** per `Using_ChangingDisableAPITermination.md`: *"By default, termination protection is disabled for your instance."* | Yes |
| `instanceInitiatedShutdownBehavior` | **Same discrepancy as above** | Yes — default is **`stop`** per `Using_ChangingInstanceInitiatedShutdownBehavior.md`: *"By default, when you initiate a shutdown... the instance stops."* | Yes |
| `disableApiStop` | **No** (not in any of the three enums) | Yes (`DisableApiStop`) | Yes |

**Claim A (kill-chain already fully owned by Modify, Reset adds nothing there):** The confirmed userData→IMDS→instance-profile-role privesc chain (documented pattern in the sibling `RebootInstances`/credit-spec plans and directly supported here by `ModifyInstanceAttribute`'s `UserData` param + `instancedata-data-retrieval.md`'s "modify user data... instance must be stopped" note) is **not reachable via `ResetInstanceAttribute` at all** — `userData` is absent from Reset's 3-value enum. A principal with only `ec2:ResetInstanceAttribute` (even unconditioned) cannot plant user-data code. **This is a refutation worth stating explicitly so a hunter doesn't waste time probing it**: Reset is not a backdoor into the Modify-side privesc surface; it is a narrower, different-shaped risk (availability/integrity on 2-3 attributes, not code-execution).

**Claim B (the one place Reset *does* intersect a safety-relevant default — the PowerShell discrepancy, Area 5 below):** *if* `disableApiTermination` and `instanceInitiatedShutdownBehavior` are in fact resettable (per the PowerShell examples, contra the API reference's documented enum), then `ResetInstanceAttribute` would let a caller **strip termination protection** (reset `disableApiTermination` to its default `false`) and/or **reset shutdown behavior to `stop`**, without ever calling `ModifyInstanceAttribute` and without choosing an arbitrary value (they can't set `disableApiTermination=true`, only reset it toward `false`-by-default) — i.e., Reset could only ever be used to **weaken** these two protections, never to strengthen them, because "default" for both is the permissive setting. That asymmetry (Reset == one-way ratchet toward weaker security posture for exactly the two attributes whose default happens to be insecure) is the crux of Area 5's severity.

**Claim C (IAM condition-key asymmetry — new finding from this pass, not covered in sibling plans):** `list_ec2.md`'s per-action condition-key rows show:
- `ModifyInstanceAttribute` → `instance*` resource row's condition keys **include** `ec2:Attribute` and `ec2:Attribute/${AttributeName}`.
- `ResetInstanceAttribute` → `instance*` resource row's condition keys **do NOT include `ec2:Attribute` or `ec2:Attribute/${AttributeName}` at all** (verified: the full list is `aws:ResourceTag/${TagKey}`, `ec2:AvailabilityZone`, `ec2:AvailabilityZoneId`, `ec2:CpuOptionsAmdSevSnp`, `ec2:EbsOptimized`, `ec2:InstanceAutoRecovery`, `ec2:InstanceBandwidthWeighting`, `ec2:InstanceID`, `ec2:InstanceMarketType`, `ec2:InstanceMetadataTags`, `ec2:InstanceProfile`, `ec2:InstanceType`, `ec2:ManagedResourceOperator`, `ec2:MetadataHttpEndpoint`, `ec2:MetadataHttpPutResponseHopLimit`, `ec2:MetadataHttpTokens`, `ec2:ProductCode`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:RootDeviceType`, `ec2:Tenancy` — no `Attribute` key anywhere in that row).
- `iam-policies-for-amazon-ec2.md` (`#attribute-key`) confirms `ec2:Attribute` is exactly the mechanism for filtering **which named attribute** an action targets (its own worked example: `Deny` `ec2:ModifyImageAttribute` when `ec2:Attribute: "Description"`), i.e., it is the per-field scoping lever a policy author would reach for to write *"allow resetting `sourceDestCheck` but never `kernel`/`ramdisk`"* or vice versa.

**Claim C stated as a hypothesis:** Because `ResetInstanceAttribute` has no `ec2:Attribute`/`ec2:Attribute/${AttributeName}` condition key documented, an IAM policy author who grants `ec2:ResetInstanceAttribute` to a principal (scoped only by instance ARN/tag, as the row permits) **cannot carve out "may reset sourceDestCheck, may not reset kernel/ramdisk"** (or any sub-split of the 3-value enum) the way they demonstrably can for `ModifyInstanceAttribute`'s much larger enum. The grant is necessarily all-three-or-none at the IAM layer, despite the three attributes having materially different blast radii (Area 1's subnet-wide NAT outage vs. Area 2's single-instance boot risk). This is a **real, documentable scoping gap**, not a doc-gap — the absence is directly verifiable from the SAR table rows cited above (re-confirm the live rendered table matches the local mirror before relying on it further, since SAR tables are sometimes JS-rendered on `.html` and only reliable via `.md`/raw fetch per the `RebootInstances` plan's own methodology note).

**Confirm/Refute oracle for Claim C:** Write an IAM policy granting `ec2:ResetInstanceAttribute` on an instance ARN with `Condition: {"StringEquals": {"ec2:Attribute": "sourceDestCheck"}}` (mirroring the `iam-policies-for-amazon-ec2.md` worked Deny example, but as an Allow-scoping Condition) and test whether it actually constrains the call to `sourceDestCheck` only (expected: the condition key is either silently ignored/not evaluated — i.e. the policy allows all three regardless — or IAM policy validation/evaluation itself errors on an undocumented key for this action, both of which confirm no real per-attribute scoping exists for Reset). Compare against the identical pattern on `ModifyInstanceAttribute`, which `iam-policies-for-amazon-ec2.md` shows *does* work.

**Severity-if-true:** **Medium.** Not a cross-tenant or credential-exfil bug — a least-privilege authoring gap that AWS's own SAR table structurally cannot close for this action today. Relevant to Area 1/2's severity: an operator who wants to grant "may fix a security-group-adjacent sourceDestCheck mistake" without also granting "may un-boot my custom-kernel fleet" has no IAM-native way to do so.

---

## 4. Area 4 — `DescribeInstanceAttribute` as the pre-flight/read-twin, and what it discloses

**Background.** `DescribeInstanceAttribute` reads any one of `instanceType | kernel | ramdisk | userData | disableApiTermination | instanceInitiatedShutdownBehavior | rootDeviceName | blockDeviceMapping | productCodes | sourceDestCheck | groupSet | ebsOptimized | sriovNetSupport | enaSupport | enclaveOptions | disableApiStop` — a superset of both Reset's and (almost) Modify's enums, explicitly including `userData` (full bootstrap script disclosure — the confirmed-elsewhere secrets-in-userData vector) and `groupSet` (security-group membership recon).

**Claim:** A principal who can `DescribeInstanceAttribute(userData)` on an instance can read any secrets/bootstrap material embedded in user data (the standard "don't put secrets in userData" anti-pattern) **without** ever needing `ModifyInstanceAttribute` or `ResetInstanceAttribute` — this is a pure-read reconnaissance primitive that pairs naturally with the Area 3 Claim A kill-chain (read userData for recon → if ModifyInstanceAttribute is also held, overwrite userData for persistence/privesc) but stands alone as an info-disclosure concern even without any Reset/Modify rights.

**Mechanism:** `API_DescribeInstanceAttribute.md` `userData` response element: *"The user data. Type: AttributeValue object."* No redaction, no separate "sensitive" ACL tier distinct from the generic `ec2:DescribeInstanceAttribute` action.

**Confirm/Refute oracle:** Launch an instance with userData containing a canary secret string (never a real credential). As a principal with only `ec2:DescribeInstanceAttribute` (no Modify/Reset), call `Attribute=userData` and confirm the canary is returned verbatim (base64-decoded by the caller). This is expected-to-succeed (documented, not a bug) — the value of testing it is characterizing exactly what else sits in the same IAM action's reach (e.g., does one `ec2:DescribeInstanceAttribute` grant implicitly reach all 16 sub-attributes with a single IAM allow, including `groupSet`, with no per-attribute Describe-side condition key either — same Claim-C-shaped question, worth checking against `list_ec2.md`'s `DescribeInstanceAttribute` row as a fast follow.) **doc-gap — confirm whether DescribeInstanceAttribute's SAR row has the same `ec2:Attribute` condition-key absence as Reset; not yet checked in this pass.**

**Severity-if-true:** Informational/Low standalone (documented, expected behavior) — High as a chain-link if combined with secrets-in-userData (customer anti-pattern, not an AWS defect) or with Modify-side userData-rewrite privesc (AWS's documented, confirmed-elsewhere exemplar).

---

## 5. Area 5 — The doc-vs-API-reference discrepancy on valid `Attribute` values (Lens U — undocumented knob)

**Claim:** The EC2 **API Reference** for `ResetInstanceAttribute` states the `Attribute` parameter's `Valid Values` are strictly `kernel | ramdisk | sourceDestCheck` — a closed 3-value enum, presumably enforced server-side with `InvalidParameterValue` (or similar) for anything else. The **devguide code-example page for the same action** (`example_ec2_ResetInstanceAttribute_section.md`), specifically its **Tools for PowerShell V4 and V5** tabs, show five `Reset-EC2InstanceAttribute -Attribute` examples: `sriovNetSupport`, `ebsOptimized`, `sourceDestCheck`, `disableApiTermination`, `instanceInitiatedShutdownBehavior` — two values present in neither the API reference's enum nor even `ModifyInstanceAttribute`'s broader enum in the same shape (`sriovNetSupport`/`ebsOptimized` *are* in Modify's enum; `disableApiTermination`/`instanceInitiatedShutdownBehavior` *are* in Modify's enum too — so all five are "real" EC2 instance-attribute names, just not members of the 3-value set the Reset API Reference says is valid).

**Mechanism (doc evidence):** Direct textual contradiction between two AWS-owned pages for the identical API action:
- `API_ResetInstanceAttribute.md` line: `Valid Values: kernel | ramdisk | sourceDestCheck`
- `example_ec2_ResetInstanceAttribute_section.md` PowerShell V4/V5 tabs: five `Reset-EC2InstanceAttribute` examples covering a superset.

Three explanations are possible, each with different security weight, and docs alone cannot disambiguate them:
1. **Stale/wrong example page** — the PowerShell cmdlet reference itself hasn't actually supported those extra values in years (the cmdlet's parameter validation may independently reject them; the devguide page may just be copy-pasted from an older cmdlet surface). → No security relevance, pure doc-quality bug.
2. **The service actually accepts more attribute names than the reference documents**, and the reference's enum is simply incomplete (the service historically supported resetting `sriovNetSupport` — it has "no way to disable" per `ModifyInstanceAttribute`'s own `SriovNetSupport` note ("There is no way to disable enhanced networking with the Intel 82599 Virtual Function interface at this time"), making a *Reset* path to disable it a materially different, more powerful primitive than Modify offers for that one attribute — worth flagging specifically). → Real undocumented-surface risk: an action whose server-side acceptance is broader than its documented/IAM-reasoned-about enum is exactly the shape of bug that defeats "I read the docs and scoped my Deny to the 3 values I was told are possible."
3. **The SDK/CLI/PowerShell layer silently translates** an unsupported `Attribute` value into a different, supported wire call (e.g., routes to `ModifyInstanceAttribute` with a default-valued payload instead of literally calling `ResetInstanceAttribute` on the wire) — in which case the PowerShell examples are not lying about *capability* but are misleading about *mechanism*, and the actual IAM action invoked (and thus the actual permission checked) differs from what `ec2:ResetInstanceAttribute`-only grant holders would expect.

**Confirm/Refute oracle:**
1. From a scoped test principal, call the raw EC2 Query API directly (bypassing SDKs) with `Action=ResetInstanceAttribute&Attribute=disableApiTermination` and `Attribute=sriovNetSupport` against a self-owned instance. Record the raw HTTP response: a clean `InvalidParameterValue`-class error settles explanation (1)/(3) partially (server rejects it outright → the API Reference's enum is authoritative on the wire, and the PowerShell examples are simply wrong/stale — doc-quality bug, not a security finding).
2. If the raw call succeeds, capture the CloudTrail event: does it log `eventName: ResetInstanceAttribute` with the extra attribute, or does it show a translated `ModifyInstanceAttribute` call underneath (confirms/refutes explanation 3)?
3. Separately, run the actual `Reset-EC2InstanceAttribute -Attribute disableApiTermination` PowerShell cmdlet (Tools for PowerShell, matching the exact devguide example) against a self-owned canary instance with termination protection enabled, and observe whether protection is stripped — this is the directly actionable version of Claim B from Area 3 and should be tested together.
4. If any path confirms the service genuinely resets `disableApiTermination`/`instanceInitiatedShutdownBehavior` under the `ec2:ResetInstanceAttribute` IAM action (not `ec2:ModifyInstanceAttribute`): that means a security team that denies `ec2:ModifyInstanceAttribute` entirely (believing it fully locks termination-protection posture) while permitting `ec2:ResetInstanceAttribute` (believing — per the API Reference — it only touches `kernel|ramdisk|sourceDestCheck`) would have an **undocumented bypass** that strips termination protection via the "harmless" action. This is the single highest-value confirm/refute item in this whole document because it directly contradicts the primary API reference's own stated contract.

**Preconditions/Cost:** Zero extra cost beyond the CLI/PowerShell tooling already shown in AWS's own example page; trivially cheap to test with two authorized test accounts/instances.

**Severity-if-true:** **High** if explanation (2) or (3) holds for `disableApiTermination`/`instanceInitiatedShutdownBehavior` specifically (silent termination-protection-strip bypass under an IAM action an operator reasonably believes is narrowly scoped to 3 harmless values) — **Low/doc-quality-only** if explanation (1) holds (stale example, server-side enum is authoritative). **This entire area is "doc-gap — confirm surface first"** by design; it is the one hypothesis in this document that cannot be resolved by reading further documentation, only by the oracle above.

---

## 6. Area 6 — Reset mid-operation / resilience (Lens L)

**Claim:** Calling `ResetInstanceAttribute(sourceDestCheck)` against an instance **while it is actively mid state-transition** (e.g., immediately after `StopInstances` is issued but before the instance reaches `stopped`, or immediately after `StartInstances` but before `running`) may race against the instance's own networking-stack initialization, producing either a clean reject, a queued-and-applied-later change, or (worst case) a window where the attribute briefly disagrees between the EC2 control-plane's view and the hypervisor/ENI's enforced state.

**Mechanism:** No doc evidence either confirms or denies this — `API_ResetInstanceAttribute.md` documents only the two steady-state preconditions ("stopped" for kernel/ramdisk; "running or stopped" for sourceDestCheck) and says nothing about transitional states (`stopping`, `pending`, `shutting-down`). This is analogous to the `RebootInstances` plan's Area 6 (async multi-AZ default-rollout race) and `ModifyInstanceCreditSpecification`'s Area 6, but for instance-attribute state rather than account defaults.

**Confirm/Refute oracle:** Issue `StopInstances` then immediately (same second) issue `ResetInstanceAttribute(sourceDestCheck)` without waiting for `stopped`; repeat for `StartInstances`→`ResetInstanceAttribute(kernel)` (expected to fail cleanly since kernel requires `stopped`, per docs — confirms the precondition is actively enforced, not just advisory) and for `StopInstances`→immediate`ResetInstanceAttribute(sourceDestCheck)`→immediate `StartInstances` (does the reset "stick" through the transition, or get silently dropped/overridden by boot-time ENI state restore?). Record exact error codes (`IncorrectInstanceState` expected) vs. any silent success-but-no-effect outcome.

**Severity-if-true:** Low–Medium (resilience/consistency characterization, no new privilege boundary crossed — valuable mainly to rule out a "the precondition check is advisory, not enforced" finding, which would matter for Area 2's kernel/ramdisk stopped-state requirement specifically).

---

## 7. Null hypotheses / lenses checked that did not fire

- **Lens B/C (PassRole, credential vending)** — N/A for `ResetInstanceAttribute` itself: no `roleArn`/`PassRole`/profile field anywhere in its request shape. (The userData/IMDS privesc chain lives entirely on the `ModifyInstanceAttribute` side, per Area 3 Claim A — confirmed absent from Reset.)
- **Lens G (SSRF)** — N/A. No URL/host/webhook field in any of the three actions' request parameters.
- **Lens F (parser/translation injection)** — N/A for the 3 documented values; the *only* open question in this family is Area 5 (does the service accept more values than documented — a validation-boundary question, not a parser-injection one).
- **Cross-account reach** — not analyzed as a presumed-broken claim here (out of scope for this attribute-semantics area); `InstanceId` is a single scalar with the same per-account-ARN model discussed in the `RebootInstances` plan — assume it holds unless a hunter finds otherwise elsewhere.
- **Batch/multi-item oracle (Lens A oracle variant)** — N/A; `ResetInstanceAttribute` takes exactly one `InstanceId`, no array, so the `ModifyInstanceCreditSpecification`-style per-item error-differential oracle doesn't apply here.

---

## 8. Priority order for a downstream hunter

1. **Area 5** (doc-vs-reference discrepancy, `disableApiTermination`/`instanceInitiatedShutdownBehavior` resettability) — resolves whether a documented-as-narrow action is actually a termination-protection-strip bypass. Highest severity-if-true, cheapest to test, and the only item that *requires* live confirmation rather than more reading.
2. **Area 1** (`sourceDestCheck` reset → NAT/router outage on a running instance, no stop needed) — highest confidence-of-mechanism (directly and repeatedly stated across 3 independent AWS pages), concrete availability blast radius.
3. **Area 3 Claim C** (`ec2:Attribute` condition-key absence on Reset's SAR row) — a real, already-fully-documented (no live test needed to establish the gap itself, though the Confirm/Refute oracle should still verify IAM evaluates it as expected) least-privilege scoping limitation feeding directly into Area 1/2's "can an operator even mitigate this with IAM" question.
4. **Area 2** (`kernel`/`ramdisk` reset → PV boot integrity) — real but narrower (legacy PV fleet only), still worth a cheap confirm.
5. **Area 4 / Area 6** — lower-priority characterization and resilience items; useful completeness, not headline findings.
