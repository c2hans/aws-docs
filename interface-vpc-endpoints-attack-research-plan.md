# Interface VPC Endpoints (EC2 / AWS PrivateLink) — Attack & Research Plan

> **Target doc:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html
> **Offline mirror:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/interface-vpc-endpoints.md` (verified offline == online, verbatim, no drift, 2026-10-15)
> **Authoritative IAM source:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (~10,190 lines)
> **Method:** `security-questionbuilder` skill (6-step boundary-first). This is a **falsifiable-hypothesis research plan**, not a list of confirmed bugs. All reasoning is documentation-only; no live AWS plane was touched. A hunter executes and confirms/refutes each lead later.

---

## §0 — How to use this plan

This plan **complements** the existing sibling `ec2-security-groups-privatelink-attack-research-plan.md`:

- The **sibling owns**: PrivateLink *default posture* framing from the SG chapter, the CloudTrail/CloudWatch **logging gap** (its Area 7), and *raises* the sample-policy `ec2:Encrypted` Deny-completeness question (its Objective 5). The sibling treats PrivateLink from the security-group vantage.
- **This plan owns** the dedicated interface-endpoint surface the sibling does not reach: the `ec2:Vpce*` **condition-key scopability** audit, the **Create-vs-Modify scoping asymmetry**, the **unconstrained free-form endpoint `PolicyDocument`**, **private-DNS override + verification**, the `aws:SourceVpce` **absence doc-gap**, and the **null hypotheses** (no PassRole, no Org key).
- **Area 8 below EXTENDS (does not duplicate) the sibling's Objective 5**: the sibling asks "is the two-statement Deny complete?"; this plan answers it with a 6-escape-path enumeration + a fail-open-polarity finding. Hunters should read both; the sibling is the owner of record for the sample-policy lead, this plan is the deepened enumeration.

Each lead uses the skill's shape: **Claim → Mechanism (doc evidence w/ file:line) → Confirm/Refute oracle → Preconditions / Cost / Severity-if-true.** A clean refutation is a complete, correct result — several leads below are explicit **null hypotheses** and are expected to refute.

**HARD STOP:** any evidence pointing at AWS's own service plane (an AWS-fleet ARN/account/credential, a cross-tenant hop into AWS infrastructure) is a disclosure-grade breach — preserve evidence, stop, do not exploit beyond existence.

---

## §1 — Objectives

1. Determine whether an admin can **bound what a delegated principal does with VPC endpoints** using only IAM condition keys — i.e. is the `ec2:Vpce*` family sufficient to express a least-privilege endpoint policy, or are there scoping holes.
2. Determine whether the **Create-time scoping controls survive Modify** (create-benign-then-widen).
3. Determine whether the **endpoint `PolicyDocument` itself** can be constrained by any IAM mechanism (can an org force a *minimum* endpoint policy?).
4. Determine whether **private-DNS override** of `com.amazonaws.{region}.ec2` enables a split-horizon / interception surface, and whether its verification gate is sound.
5. **Extend the sibling's Objective 5**: enumerate every unencrypted-volume path the AWS sample endpoint policy fails to deny, and characterize its missing-key fail-open polarity.
6. Record the audit-log-evasion lead (owned by sibling Area 7) with a cross-reference, and the confirmed **null hypotheses** so the surface is provably swept.

---

## §2 — Components, Assets, and Design

### Mechanism (from the target page, verbatim-sourced)
- **Interface endpoint** for the EC2 control-plane API, service name **`com.amazonaws.{region}.ec2`** (`interface-vpc-endpoints.md:20`). Backed by an ENI in the customer subnet with a private IP; traffic to the EC2 API never leaves the AWS network / needs no IGW/NAT (`:8`).
- **Endpoint policy** = a **resource-based IAM policy attached to the endpoint** (`:27`). **Default = full access** to the EC2 API (`:27`). It is an **intersection/restricting** layer, not an additive grant: `vpc/latest/privatelink/vpc-endpoints-access.md:10` — "An endpoint policy does not override or replace identity-based policies or resource-based policies." The caller's identity policy must independently allow the action.
- **Private DNS**: enabling private DNS makes the standard public EC2 API hostname (`ec2.{region}.amazonaws.com`) resolve, *inside the VPC*, to the endpoint ENI via a hidden AWS-managed private hosted zone — split-horizon DNS. Toggled by `PrivateDnsEnabled` (an `ec2:Attribute` on Modify; see §4 Area 3).
- **Audit caveat** (`interface-vpc-endpoints.md:34-35`): *"When a non-default policy is applied to an interface VPC endpoint for Amazon EC2, certain failed API requests, such as those failing from `RequestLimitExceeded`, might not be logged to AWS CloudTrail or Amazon CloudWatch."*

### Assets
- The EC2 **control-plane API reachability** from inside a VPC (the whole point of the endpoint).
- The **endpoint policy** (who-can-do-what through this pipe).
- The **private DNS binding** of the canonical EC2 API hostname.
- Endpoint resource identifiers: `vpce-*` (vpc-endpoint), `vpce-svc-*` (vpc-endpoint-service).

### API inventory (endpoint-relevant; from `list_ec2.md`)
| Action | Mutating | Resource type(s) | Scoping keys present | Notes |
|---|---|---|---|---|
| `CreateVpcEndpoint` | yes | `vpc-endpoint`, `vpc-endpoint-service`, subnet, sg, route-table | **VpceServiceName, VpceServiceOwner, VpcePrivateDnsPreference, VpcePrivateDnsSpecifiedDomains, VpceServiceRegion, VpceMultiRegion** (list_ec2.md:5767-5776) | positive controls DO exist at create |
| `ModifyVpcEndpoint` | yes | `vpc-endpoint` | **`ec2:Attribute` only** (incl. `PrivateDnsEnabled`, `PolicyDocument`) | **none of the Vpce* create keys apply** |
| `DeleteVpcEndpoints` | yes | `vpc-endpoint` | ResourceTag/Region | |
| `DescribeVpcEndpoints` | no | **(no resource type)** | **`ec2:Region` only** | **unscopable read oracle** |
| `CreateVpcEndpointServiceConfiguration` | yes | `vpc-endpoint-service` | PrivateDnsName-related | provider-side |
| `ModifyVpcEndpointServicePrivateDnsName` | — | — | — | **DOES NOT EXIST in list_ec2.md** — do not reference it; the real items are the condition key `ec2:VpceServicePrivateDnsName` and the unrelated instance action `ModifyPrivateDnsNameOptions` |
| `StartVpcEndpointServicePrivateDnsVerification` | yes | `vpc-endpoint-service` | — | provider domain-ownership proof |

`ec2:Vpce*` condition-key family defined at `list_ec2.md:10175-10182`.

### Trust-boundary map
| From (actor) | To (resource) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Delegated IAM principal (intended least-priv) | VPC endpoint config | `CreateVpcEndpoint` / `ModifyVpcEndpoint` | Principal creates/modifies an endpoint the admin's condition keys were meant to forbid (wrong service, wrong DNS pref, over-broad policy) |
| In-VPC caller | EC2 control-plane API | endpoint ENI + private DNS | Caller reaches/escalates EC2 API actions the endpoint policy was meant to deny |
| Org admin | member-account endpoint policy content | (none expressible in `ec2:*`) | Member attaches a wide-open `PolicyDocument`; org has no `ec2:` key to force a floor (SCP/RCP only) |
| Endpoint operator | canonical EC2 API hostname resolution in VPC | private-DNS override | API traffic silently redirected/observed through an attacker-influenced endpoint |

---

## §4 / §5 — Firing-lens Areas (NEW surface, prioritized)

### Area 1 — `ec2:Vpce*` condition-key coverage: can an endpoint policy be bounded? (Lens S, U) — **PRIORITY**
- **Claim:** An admin *can* restrict a delegated principal to creating endpoints only for approved services with approved private-DNS posture, because `CreateVpcEndpoint` carries `VpceServiceName`, `VpceServiceOwner`, `VpcePrivateDnsPreference`, `VpcePrivateDnsSpecifiedDomains`, `VpceServiceRegion`, `VpceMultiRegion` (`list_ec2.md:5767-5776, 10175-10182`). **This refines the naive "VPC endpoints are unscopable" assumption — a positive control that is rarely applied.**
- **Mechanism:** the six keys above are real and resolve to the `vpc-endpoint`/`vpc-endpoint-service` rows.
- **Confirm/Refute oracle:** in a test account, attach a policy allowing `CreateVpcEndpoint` only when `ec2:VpceServiceName` matches `com.amazonaws.*.ec2`; confirm a create for a *different* service name is denied. **Then test the string-match semantics** (case, wildcard, partial) — a `StringEquals` vs `StringLike` mismatch is a bypass.
- **Severity:** the hole is a least-privilege footgun (lower), unless combined with Area 2/3.

### Area 2 — Create-vs-Modify scoping asymmetry (Lens S, U) — **PRIORITY / HEADLINE**
- **Claim:** The Area-1 controls are **defeated by `ModifyVpcEndpoint`**, which carries **none** of the `Vpce*` keys — only `ec2:Attribute`. A principal constrained at create can create a benign endpoint, then **modify** it toward a forbidden state (swap `PolicyDocument`, toggle `PrivateDnsEnabled`) with the create-time guardrails inert.
- **Mechanism:** `ModifyVpcEndpoint` block in `list_ec2.md` lists only `ec2:Attribute` (+ generic Region/ResourceTag); the `VpceServiceName/Owner/PrivateDnsPreference` keys are absent from its block.
- **Confirm/Refute oracle:** with an identity scoped by Area-1 keys and also granted `ModifyVpcEndpoint`, create an approved endpoint, then `ModifyVpcEndpoint --policy-document <wide-open>` and/or `--private-dns-enabled`. If the modify succeeds, the create-time scoping is bypassable. **Also test `ec2:Attribute` case-sensitivity**: `StringEquals ec2:Attribute "PolicyDocument"` vs an API that accepts `policyDocument`/`Policy` casing → missing-key / case fail-open (see cross-ref to `changing-security-group` ec2:Attribute casing lead in memory).
- **Severity:** High if confirmed — it collapses the only expressible endpoint-scoping control.

### Area 3 — Private-DNS toggle via `ec2:Attribute` only (Lens S, V, D) — **PRIORITY**
- **Claim:** Whether an endpoint hijacks in-VPC resolution of the canonical EC2 API hostname (`PrivateDnsEnabled`) is gatable **only** through `ec2:Attribute` on `ModifyVpcEndpoint` — a case-sensitive string match with the classic fail-open modes — and there is **no dedicated boolean condition key** for private-DNS-enabled on Modify.
- **Mechanism:** `PrivateDnsEnabled` is modeled as a value of `ec2:Attribute`, not its own key; `VpcePrivateDnsPreference` exists only on *Create* (`list_ec2.md:5775`), not Modify.
- **Confirm/Refute oracle:** attempt `ModifyVpcEndpoint` with `PrivateDnsEnabled=true` under a policy that `Deny`s `ec2:Attribute = PrivateDnsEnabled`; vary casing. If a casing variant evades the Deny, fail-open confirmed. **Split-horizon consequence:** confirm whether enabling private DNS on an attacker-influenced endpoint can shadow `ec2.{region}.amazonaws.com` for the whole VPC (data-plane callers silently routed through an endpoint whose policy the attacker controls).
- **Severity:** High (silent redirection of control-plane API calls for every in-VPC principal).

### Area 4 — Unconstrained free-form endpoint `PolicyDocument` (Lens U, R) — **PRIORITY**
- **Claim:** **No `ec2:` condition key reaches into the content of the endpoint `PolicyDocument`.** An org/admin cannot force a *minimum* endpoint policy (e.g. "must Deny `ec2:*` to non-org principals") via EC2 IAM — the document is opaque free-form JSON to the authz layer. The documented **default is full access** (`interface-vpc-endpoints.md:27`), so an endpoint created/modified with no explicit restriction is wide open by design.
- **Mechanism:** `PolicyDocument` is a value of `ec2:Attribute` (presence-gatable, not content-gatable); no `ec2:VpcePolicy*` content key exists in `list_ec2.md`.
- **Confirm/Refute oracle:** search `list_ec2.md` for any key constraining policy *content* (expected: none). Confirm that the only org-level floor is an SCP/RCP (`aws:*`/`ec2:Attribute` presence), not an EC2 content key. If no content key exists, the claim holds (a hardening gap, AWS-design-level).
- **Severity:** Hardening/least-privilege gap; elevate if combined with Area 2 (modify toward wide-open).

### Area 5 — `aws:SourceVpce` / `aws:SourceVpc` enforcement vs documentation (Lens U, D) — PRIORITY MED
- **Claim:** The target page never tells the reader that resource owners can require traffic to arrive **through a specific endpoint** using `aws:SourceVpce`/`aws:SourceVpc`/`aws:VpcSourceIp` global keys — a doc-gap that leads customers to believe the endpoint policy is their only lever.
- **Mechanism:** these are *global* condition keys (not in `list_ec2.md`'s EC2-specific table); the EC2 page is silent on them while they are the actual mechanism for "lock this S3/API access to my VPCe."
- **Confirm/Refute oracle:** confirm the keys exist globally and are honored by EC2 API resource policies; confirm the target page omits them. Documentation completeness lead, not an exploit.
- **Severity:** Doc-gap (customer-footgun), low direct severity.

### Area 6 — `DescribeVpcEndpoints` unscopable read oracle (Lens A, S)
- **Claim:** `DescribeVpcEndpoints` has **no resource type** and only `ec2:Region` — it cannot be scoped to a subset of endpoints. Any principal granted it enumerates **all** endpoints in the account/region, including their policies and private-DNS state.
- **Mechanism:** the action's block in `list_ec2.md` lists no resource ARN row, only `ec2:Region`.
- **Confirm/Refute oracle:** attempt to write a policy restricting `DescribeVpcEndpoints` to one `vpce-*`; confirm it cannot be expressed (no resource row). Account-scoped, not cross-account — matches the family-wide unscopable-Describe pattern (cross-ref memory `describe-keys`, `verify-nitrotpm`).
- **Severity:** Low (intra-account recon oracle), consistent with EC2 Describe-family.

### Area 7 — Audit-log evasion on non-default policy (Lens O) — **CROSS-REF: SIBLING OWNS**
- **Claim:** Applying a non-default endpoint policy can cause **certain failed requests (e.g. `RequestLimitExceeded`) to not be logged to CloudTrail/CloudWatch** (`interface-vpc-endpoints.md:34-35`) — a defender-blinding property that an attacker can deliberately induce (attach a restrictive policy, then drive throttle-failing probes that go unlogged).
- **Owner of record:** `ec2-security-groups-privatelink-attack-research-plan.md` **Area 7 / Objective 5**. Not re-analyzed here beyond noting the exact doc sentence and that the gap is *attacker-inducible*, not merely incidental.
- **Confirm/Refute oracle:** attach a non-default policy; generate throttle/limit failures through the endpoint; diff CloudTrail/CloudWatch for the missing events.
- **Severity:** Medium (detection evasion). See sibling for full treatment.

### Area 8 — Sample endpoint-policy `ec2:Encrypted` Deny-completeness (Lens R, U, S) — **EXTENDS SIBLING OBJECTIVE 5**
> The sibling *raises* "is the two-statement Deny complete?"; this is the deepened answer. The sibling remains owner of record; this area is the enumeration contribution.

The AWS-shipped sample (`interface-vpc-endpoints.md:46-83`) claims (`:45`) it "denies permission to create unencrypted volumes or to launch instances with unencrypted volumes." That framing is **false** in two independent ways:

**8a — Six escape paths the two-statement Deny never reaches.** The Deny names only `ec2:CreateVolume` and `ec2:RunInstances`. The following unencrypted-volume paths are **not denied**:
- `CreateFleet` **via launch-template `BlockDeviceMapping`** — `CreateFleet`'s `volume` row carries `ec2:Encrypted` (`list_ec2.md:5122`) but **only for inline override volume params**, per its own caveat (`list_ec2.md:5114`): resource-level perms "do not include the resources specified in a launch template." A fleet whose unencrypted volume comes from a referenced template escapes.
- `RequestSpotFleet`, `RequestSpotInstances` — **carry no `ec2:Encrypted` key at all** (verified: token absent from each action's full block). Cannot be gated even if added to the Deny.
- `ImportSnapshot`, `ImportImage`, `CopyImage` — **no `ec2:Encrypted` key** (verified). These are the "bring/duplicate your own unencrypted disk" paths; un-gatable by this key.
- (Lower risk, also absent from the Deny but *do* carry the key: `RestoreSnapshotFromRecycleBin`/`RestoreSnapshotTier`/`RestoreVolumeFromRecycleBin`, lines 9552/9558/9564.)
- Full `ec2:Encrypted`-carrying action roster captured for the hunter: AttachVolume(4873), CopySnapshot(4999), CopyVolumes(5005), CreateFleet(5122), CreateSnapshot(5455), CreateSnapshots(5462), CreateTags(5562/5585), CreateVolume(5745 snapshot /5746 volume), DeleteVolume(6441), DescribeSnapshotAttribute(7377), DescribeVolumeAttribute(7581), DetachVolume(7743), Disable/EnableFastSnapshotRestores(7797/8050), EnableVolumeIO(8141), ImportInstance(8666), ImportVolume(8684), Lock/UnlockSnapshot(8708/9711), ModifyInstanceAttribute(8810), ModifySnapshotTier(9014), ModifyVolume(9126), ModifyVolumeAttribute(9132), RunInstances(9603), FIS InjectVolumeIOLatency(9886)/PauseVolumeIO(9898); key def at `list_ec2.md:10075`.

**8b — Fail-open polarity on a missing/not-reported key.** The sample uses `Deny ... Bool { ec2:Encrypted: "false" }`. Per IAM's generic rule (`IAM/latest/UserGuide/reference_policies_elements_condition.md:93,98`): *"A context key that is not present in the request is considered a mismatch"* — so if `ec2:Encrypted` is **absent** from the request context, the Deny **does not fire**, and Statement 1's blanket `Allow ec2:*` lets the action through. Present-and-false matches; **absent never matches.** The companion doc `ExamplePolicies_EC2.md:467-487` ships the **inverse polarity** for the same goal — `Allow ... Bool ec2:Encrypted = "true"` — which **fails closed** on a missing key. The sample on the target page chose the fail-**open** polarity and gives the reader **no `Null`-guard** (`reference_policies_elements_condition.md:101` recommends exactly a `Null` check to defend against this) and **no cross-reference** to the inverse pattern. Whether `ec2:Encrypted` is populated from the literal `Encrypted` API param or from the *resolved* encryption state (incl. account-level EBS-encryption-by-default) is **not documented anywhere in the EC2/EBS doc set** — a doc-gap the hunter must resolve empirically.
- **Confirm/Refute oracle:** through an endpoint carrying the sample policy, launch via `RequestSpotInstances`/`CreateFleet`(template)/`ImportSnapshot` with an unencrypted volume; confirm the Deny does not fire. Separately, issue a `CreateVolume`/`RunInstances` that **omits** the `Encrypted` param under account EBS-encryption-by-default and observe whether the Deny evaluates (tests 8b).
- **Severity:** the policy is AWS-authored and copy-verbatim; a weak default in it is AWS's defect (Lens R). Medium — a customer who copies it believes they have closed all unencrypted paths and has not. Note the service-side backstop (`ebs/.../ebs-encryption.md:12-13`: with encryption-by-default on, "you can't create unencrypted snapshots") independently mitigates *some* paths — so this is a defense-in-depth/false-assurance finding, not necessarily an exploitable unencrypted-volume outcome in every account.

---

## §6 — Threat-model summary

| # | Area | Lens | Boundary | Severity-if-true | Priority |
|---|---|---|---|---|---|
| 2 | Create-vs-Modify asymmetry | S/U | delegated-principal → endpoint config | High | **P0** |
| 3 | Private-DNS toggle `ec2:Attribute`-only + split-horizon | S/V/D | in-VPC caller → control-plane API | High | **P0** |
| 4 | Free-form `PolicyDocument` uncontrollable | U/R | org → member endpoint policy | Hardening (High w/ #2) | **P1** |
| 1 | `Vpce*` key coverage (positive control) | S/U | delegated-principal → endpoint | Least-priv footgun | **P1** |
| 8 | Sample-policy Deny escapes + fail-open polarity | R/U/S | copy-verbatim artifact | Medium (false assurance) | **P1** |
| 7 | Audit-log evasion (sibling-owned) | O | attacker → detection | Medium | **P2** |
| 5 | `aws:SourceVpce` doc-gap | U/D | customer understanding | Doc-gap | **P2** |
| 6 | `DescribeVpcEndpoints` unscopable | A/S | intra-account recon | Low | **P3** |

---

## §7 — Out of scope / HARD STOP
- No live AWS plane touched in building this plan. Hunter stays within the two authorized test sessions, synthetic/canary data only.
- Any AWS-fleet ARN/account/credential surfaced via an endpoint = disclosure-grade; preserve evidence and stop.
- Provider-side endpoint-*service* mechanics (`vpce-svc-*`, `StartVpcEndpointServicePrivateDnsVerification` TXT domain-ownership proof) are noted but secondary — the target page is a *consumer* page; deep provider analysis belongs to a PrivateLink-service-specific plan.
- Security groups on the endpoint ENI: owned by the SG sibling plan; not re-analyzed.

## §8 — Null hypotheses (surface provably swept)
- **Lens B (PassRole / confused deputy): NULL.** No endpoint action (`CreateVpcEndpoint`/`ModifyVpcEndpoint`/Delete/Describe) accepts a role ARN the service assumes; `iam:PassRole` does not appear on any VPC-endpoint action in `list_ec2.md`. Pages checked: target page, `CreateVpcEndpoint`/`ModifyVpcEndpoint` blocks in `list_ec2.md`.
- **Org-scoping (`aws:PrincipalOrgID`/`aws:ResourceOrgID`): NULL at the EC2-key layer.** Not in `list_ec2.md`; org floors on endpoint policy content are expressible **only** via SCP/RCP, not an EC2 condition key. (Feeds Area 4.)
- **`ModifyVpcEndpointServicePrivateDnsName`: DOES NOT EXIST.** Prior briefing artifact; the real items are the key `ec2:VpceServicePrivateDnsName` and the unrelated `ModifyPrivateDnsNameOptions`. Do not cite the nonexistent action.
- **Lens F (translation/injection), Lens Q (blob parsing): N/A** — the consumer endpoint page exposes no parser/translation layer or uploaded-blob field; checked the full target page and the API inventory above.
- **Lens Y (transport/TLS): not analyzed here** — endpoint traffic is AWS-internal TLS; no TLS-config knob on the consumer page. Marked doc-gap-not-pursued rather than null.

---
*Generated by the security-questionbuilder method (documentation-only). Complements `ec2-security-groups-privatelink-attack-research-plan.md`. 2026-10-15.*
