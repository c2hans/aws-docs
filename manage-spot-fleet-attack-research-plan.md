# EC2 Spot Fleet — "Describe / Manage (read side)" — Attack Research Plan

**Source of leads:** AWS EC2 User Guide page `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-spot-fleet.html` (title in the live doc: *"Describe a Spot Fleet request, its instances, and event history"*; markdown twin `manage-spot-fleet.md`); the EC2 **API Reference** pages `API_DescribeSpotFleetRequests`, `API_DescribeSpotFleetInstances`, `API_DescribeSpotFleetRequestHistory`, `API_SpotFleetRequestConfigData`, `API_SpotFleetLaunchSpecification`, `API_HistoryRecord`, `API_EventInformation`; the IAM **Service Authorization Reference** `https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html` (markdown twin `list_ec2.md`; the legacy slug `list_amazonec2.html` is dead — 302 to a JS shell — use `list_ec2`); the related monitoring page `fleet-monitor.html` (EventBridge). All offline `.md` cross-checked against the online `.md` twin on 2026-10-14.

**Status:** documentation-derived hypotheses only. Nothing has been tested against a live AWS account.

**Scope of THIS plan (read side) and its siblings (do not duplicate — cross-reference).** `manage-spot-fleet.html` is the *describe/read how-to* page. This plan therefore **owns the read/describe/history-disclosure surface** and the **read-side authorization-scopability asymmetry** across the three `Describe*` actions. It deliberately does **not** re-derive the mutation, IAM-artifact, PassRole, SLR-launch, tagging, or lifecycle-decay leads already owned by the siblings in this directory:
- `spot-fleet-attack-research-plan.md` — overview; **owns lead A1** ("resource-by-ID APIs on `Resource:"*"`") and the SLR/Config-rule deltas.
- `spot-fleet-states-attack-research-plan.md` — state machine; **owns the 48 h / `cancelled`→`deleted` decay and the IR-blind-spot leads**, and *first noted the describe-action condition-key asymmetry in passing*. This plan promotes that asymmetry to a first-class, fully-developed thesis.
- `spot-fleet-prerequisites-attack-research-plan.md` — PassRole / confused-deputy / IAM-artifact audit.
- `tag-spot-fleet-attack-research-plan.md` — tag-on-create ABAC-widening, forced `Resource:"*"` CreateTags.
- `create-spot-fleet-attack-research-plan.md` — request construction / SLR-launch guardrail bypass.
- `modify-ec2-fleet-attack-research-plan.md`, `delete-fleet-attack-research-plan.md`, `ec2-fleet-attack-research-plan.md` — EC2 Fleet (non-Spot) analogues.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **Posture note (reused from the memory-backed fleet backbone):** EC2 Spot Fleet is a **single-account / delegation-centric** service. The `Describe*` APIs carry an **API-level owner filter** ("Describes **your** Spot Fleet requests") and the request IDs are **high-entropy UUIDs** (`sfr-` + a 8-4-4-4-12 UUID, e.g. `sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`). So the high-value target here is **NOT** classic cross-tenant/cross-account IDOR (that is a documented null — see §8); it is **intra-account over-exposure and the inability to least-privilege-scope the read surface** — i.e. an ABAC/tag Deny that silently does not bind, and a recon-grade information disclosure that no IAM condition can fence.
- **DryRun trap (reused variant):** all three `Describe*` support `DryRun`. `DryRunOperation` vs `UnauthorizedOperation` reflects **caller IAM only**, evaluated *before* resource resolution — it is **not** an ownership oracle. Do not treat a `DryRunOperation` success as proof you can read a specific fleet.
- **HARD STOP:** the moment evidence shows an identity / credential / ARN / account belonging to AWS's own service plane (e.g. a response leaking a fleet SLR session or an AWS-owned account id), stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Prove the read-scopability gap is real and exploitable intra-account:** demonstrate that a principal whose policy *intends* to restrict Spot Fleet visibility to its own team (by resource ARN or by `aws:ResourceTag`) can nonetheless enumerate **every** Spot Fleet request configuration in the region via `DescribeSpotFleetRequests` — including other teams' `IamFleetRole` ARNs, AMI IDs, launch-spec user-data, and subnet/SG IDs — because that action honours **no** resource type and **no** tag condition key.
2. **Prove the ABAC Deny is inert / unauthored-able on the list action:** show there is no policy an admin can write that scopes `DescribeSpotFleetRequests` by tag or resource (only by `ec2:Region`), so "read only fleets tagged team=X" is **impossible** for the richest read action while being possible for its two drill-down twins — a Lens S/X parity hole.
3. **Quantify the recon disclosure:** enumerate exactly which sensitive fields each read API returns and show the aggregate (role ARN + launch spec + user-data + network placement) is a complete blueprint of the account's launch posture, available to any `DescribeSpotFleetRequests` holder.
4. **Confirm the Lens-X lower-level-cousin reach:** show that even where `DescribeSpotFleetInstances` *is* tag-scopable, the same fleet-launched instances remain readable through non-fleet cousins (`DescribeInstances`, `DescribeSpotInstanceRequests`) that the fleet tag never gates.
5. **Confirm the read-side detection/decay blind spot** (cross-reference, don't re-derive): history is 48 h-retained and 30 s-delayed, so the read surface itself cannot answer "what launched this orphaned instance" after the decay clock — see the states plan.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** SigV4 EC2 Query/SDK API and the EC2 console "Spot Requests" view. Three read actions are the whole surface of this page:
- `DescribeSpotFleetRequests` — list + full configuration of the caller's Spot Fleet requests.
- `DescribeSpotFleetInstances` — the running instances backing one `sfr-` request.
- `DescribeSpotFleetRequestHistory` — the time-ordered event log of one `sfr-` request.

**Resource & identifier shape.** The resource is `spot-fleet-request`, ARN `arn:${Partition}:ec2:${Region}:${Account}:spot-fleet-request/${SpotFleetRequestId}`. `SpotFleetRequestId` = `sfr-` + a v4-shaped UUID → **high entropy, not enumerable**; console IDs begin `sfr-`.

**What the read surface discloses (information-disclosure inventory).** From `API_SpotFleetRequestConfigData` (returned by `DescribeSpotFleetRequests`):
- `iamFleetRole` — **the fleet IAM role ARN** (names the delegation principal; feeds the PassRole/privesc leads in the prerequisites sibling).
- `launchSpecifications[]` (`SpotFleetLaunchSpecification`) and/or `launchTemplateConfigs[]` — **ImageId (AMI), KeyName, UserData, SecurityGroups, SubnetId, IamInstanceProfile, InstanceType, SpotPrice, Monitoring, EbsBlockDevice/Snapshot, AddressingType** — i.e. the full launch blueprint including any secrets a developer baked into `UserData`.
- `loadBalancersConfig` — **ELB names / target-group ARNs** the fleet registers into.
- `context`, `clientToken`, `onDemandMaxTotalPrice`, `allocationStrategy`, `targetCapacity`, `fulfilledCapacity`, `spotMaintenanceStrategies`, `tagSpecifications`.

From `DescribeSpotFleetInstances`: `instanceId`, `spotInstanceRequestId`, `instanceType`, `instanceHealth`.

From `DescribeSpotFleetRequestHistory` → `HistoryRecord{eventType ∈ instanceChange|fleetRequestChange|error|information, timestamp, eventInformation{eventSubType, instanceId, eventDescription}}`. `eventDescription` is a free-text field that can echo **instance IDs, launch errors, and configuration/role failure detail**. Events are **delayed ≤30 s** and **retained 48 h** only.

**Accounts / trust zones.** All three actions resolve only within the caller's account/region (API-level owner filter). There is **no** service-account/data-plane boundary exposed on the read path; the relevant boundary is **intra-account identity ↔ fleet-configuration data**, policed (or not) by IAM resource/condition scoping.

```
caller (SigV4 principal in account A)
      │  ec2:DescribeSpotFleetRequests        (NO resource type, only ec2:Region)  ─┐
      │  ec2:DescribeSpotFleetInstances       (spot-fleet-request*, aws/ec2:ResourceTag) │  all three
      │  ec2:DescribeSpotFleetRequestHistory  (spot-fleet-request*, aws/ec2:ResourceTag) │  owner-filtered
      ▼                                                                                   │  to account A
  Spot Fleet control plane ── returns ──► config (role ARN, launch spec, user-data, ...) ─┘
                                          instances, 48h event history
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Any IAM principal in account A holding `ec2:DescribeSpotFleetRequests` | Every Spot Fleet request config in the region (incl. other teams') | List action with **no** resource type / tag condition key, only `ec2:Region` | A principal whose policy *intended* a tag/resource restriction reads a fleet config it does not own/tag → **the intended ABAC/resource boundary did not bind** |
| Admin authoring a least-privilege read policy | A scoped-by-tag `DescribeSpotFleetRequests` grant | IAM policy condition evaluation | **No policy exists** that scopes the action below region (only `ec2:Region` is honoured) → the scoping boundary is **unauthorable** |
| Caller tag-scoped on `DescribeSpotFleetInstances` | The same fleet-launched instances via `DescribeInstances`/`DescribeSpotInstanceRequests` | Lower-level cousin actions not gated by the fleet's tag | Enumerating the fleet's instances through a cousin the fleet tag never binds → **parity hole around the scoped twin** |
| Caller | AWS service plane | (none exposed on read path) | Any AWS-owned account/ARN/credential in a response → **HARD STOP, disclose** |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `DescribeSpotFleetRequests` | SDK/Query | Existing (legacy API) | No | External | List + **full config** of **your** fleets | Yes | Caller (owner-filtered) | **No resource type; only `ec2:Region` condition key.** `SpotFleetRequestId.N` **optional**; no owner-filter param; `MaxResults`/`NextToken`. Returns `iamFleetRole`, launch spec, user-data, SG/subnet, LB config. |
| `DescribeSpotFleetInstances` | SDK/Query | Existing | No | External | Instances backing one `sfr-` | Yes | Caller | **`SpotFleetRequestId` required.** Resource `spot-fleet-request*`; condition keys `aws:ResourceTag`, `ec2:ResourceTag`, `ec2:Region`. Returns instance/spot-request IDs, health. |
| `DescribeSpotFleetRequestHistory` | SDK/Query | Existing | No | External | 48 h event log of one `sfr-` | Yes | Caller | **`SpotFleetRequestId` + `StartTime` required.** `EventType` filter. Resource `spot-fleet-request*`; same tag condition keys. ≤30 s delay, **48 h** retention. |

**Doc-flagged lead planted by AWS:** the page opens with *"Spot Fleet uses a **legacy API with no planned investment**. We recommend using EC2 Fleet or an Auto Scaling group instead."* A frozen, no-investment API is exactly where authorization-parity drift (Lens X) and un-modernised condition-key coverage persist — treat the "legacy, unmaintained" banner as a pointer, not boilerplate.

**Undocumented/console-hidden knob check:** the console "Spot Requests" view surfaces only the caller's own `sfr-` rows and offers no tag/resource filter affecting authorization; the API's `SpotFleetRequestId.N` being optional (list-all) is the SDK-only superset of the console. The absence of any owner/account/tag parameter on `DescribeSpotFleetRequests` is itself the lead (nothing lets you *narrow* authorization below region).

---

## 5. Recommended Areas of Focus

### Area 1 — Read-scopability asymmetry: the richest read action is unscopable (PRIMARY) — Lens S + X + U
**Background.** The IAM Service Authorization Reference (`list_ec2.md`, verbatim 2026-10-14) assigns the three sibling read actions **unequal** scoping:
- `DescribeSpotFleetRequests` → **Resource types: _(blank)_**, **Condition keys: `ec2:Region` only**.
- `DescribeSpotFleetInstances` → **Resource types: `spot-fleet-request*`**, **Condition keys: `aws:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`**.
- `DescribeSpotFleetRequestHistory` → **Resource types: `spot-fleet-request*`**, **Condition keys: `aws:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`**.

**Security Concern.** The one action that needs **no** `sfr-` ID (it lists *all* of the caller's fleets) and returns the **most** sensitive data (role ARN, launch spec, user-data) is the one that **cannot be restricted by resource ARN or by tag** — only by region. An admin can tag-scope the two drill-down twins (`...Instances`, `...RequestHistory`) but **cannot author any policy** that grants "read only the fleet configs my team tagged `team=X`." Granting `ec2:DescribeSpotFleetRequests` at all is a region-wide, account-wide read of every fleet's launch blueprint. This is simultaneously:
- **Lens S** — a condition key (`aws:ResourceTag`) that is **not evaluated** for this action, so a `Condition` keyed on it is inert; a `StringNotEquals aws:ResourceTag/team` Deny will have a *missing key* at evaluation → either over-denies (fail-closed, breaking legitimate use) or, with `...IfExists`, is skipped (fail-open) — **there is no middle "scope to my team" setting**.
- **Lens X** — an action-family parity divergence: three reads on one resource, one unchecked.
- **Lens U** — if any User-Guide / IAM-tutorial prose implies Spot Fleet read access is tag-restrictable in general, that guarantee is **false for `DescribeSpotFleetRequests`**; trace the promise to the (missing) mechanism.

**High-level Test Scenarios (falsifiable claims).**
- **Claim:** A principal with `Allow ec2:DescribeSpotFleetRequests` + a `Condition {StringEquals aws:ResourceTag/team: X}` can still list fleets tagged `team=Y`. **Oracle:** the call returns `team=Y` configs (the condition did not bind because the key is absent from the request context). **Refute** if the call is `UnauthorizedOperation`/empty, proving the key *is* honoured (contradicts the reference).
- **Claim:** No policy scopes `DescribeSpotFleetRequests` below region. **Oracle:** `iam:SimulateCustomPolicy` for `ec2:DescribeSpotFleetRequests` with a `spot-fleet-request/<id>` resource and a `aws:ResourceTag` condition → simulation shows the condition/resource is **not applicable** (allowed regardless of resource/tag, denied only by region mismatch). This is a **documentation-safe oracle (no live fleet touched)** and should be the first confirmation step.
- **Claim:** The twins *are* scopable, proving the asymmetry (control). **Oracle:** `SimulateCustomPolicy` for `DescribeSpotFleetInstances` with the same tag condition → condition **is** applicable / can deny. The delta between the two simulations *is* the finding.

**Doc evidence:** `list_ec2.md` action rows for the three describes (resource-type + condition-key cells quoted above); `API_DescribeSpotFleetRequests` ("Describes your Spot Fleet requests", `SpotFleetRequestId.N` optional). **Severity-if-true:** **Medium** (intra-account least-privilege ceiling + inert ABAC on a read; raises toward **High** where ABAC is the account's *sole* intended tenancy/team isolation mechanism and the data disclosed includes credentials in `UserData`). **Owner-to-fix:** AWS (the condition-key coverage of an AWS action is AWS's; this is not a customer-authored artifact). **Stop condition:** once the simulate delta (twins scopable, list action not) is shown, the boundary verdict is settled — do not iterate across regions.

### Area 2 — Recon-grade information disclosure via the config read — Lens A (disclosure) + Lens O enabler
**Background.** `DescribeSpotFleetRequests` returns `SpotFleetRequestConfigData` for every fleet: `iamFleetRole` ARN, full `launchSpecifications`/`launchTemplateConfigs` (ImageId, KeyName, **UserData**, SecurityGroups, SubnetId, IamInstanceProfile), `loadBalancersConfig` (ELB/target-group ARNs), `context`.
**Security Concern.** Combined with Area 1 (unscopable), any read-capable principal obtains a complete map of the account's compute launch posture: which IAM roles are passed to fleets (feeds the PassRole/privesc chain in the prerequisites sibling), which AMIs and subnets/SGs are in use (network recon), and **any secret a developer base64-embedded in `UserData`** (a recurring real-world footgun). `DescribeSpotFleetInstances`/`...RequestHistory` then pivot each `sfr-` to live `instanceId`s and error text.
**High-level Test Scenarios.**
- **Claim:** `UserData` in a launch spec is returned in cleartext (base64) to any `DescribeSpotFleetRequests` holder. **Oracle:** a response field `launchSpecifications[].userData` present and decodable. **Severity-if-true:** inherits the secret's value — **High** if a credential is recoverable; else **Low–Medium** info-leak.
- **Claim:** `iamFleetRole` ARNs disclosed by this read enumerate the account's fleet-delegation roles for targeting. **Oracle:** distinct role ARNs returned → cross-reference the prerequisites plan's PassRole leads (do not re-run them here).
- **Claim:** `eventDescription` free-text in history echoes config/instance internals. **Oracle:** AWS's own sample response for a `price_update` sub-event returns `eventDescription: "m3.medium, ami-1ecae776, Linux/UNIX (Amazon VPC); old price: 0.0153, new price: 0.0153"` — i.e. the free-text field embeds **instance type, AMI ID, platform, and spot prices**; `instanceId` is additionally populated for `instanceChange` events (`launched`/`terminated`). Error sub-types (`iamFleetRoleInvalid`, `spotFleetRequestConfigurationInvalid`, `registerWithLoadBalancersFailed`, …) carry further config/role detail in the description. **Cross-reference the states plan's 48 h decay lead — do not re-derive.**

**Doc evidence:** `API_SpotFleetRequestConfigData`, `API_SpotFleetLaunchSpecification`, `API_EventInformation`. **Severity-if-true:** **Low–Medium** standalone (intra-account recon), **High** if `UserData` yields a credential. **Stop condition:** confirming the fields are returned is the finding; do not harvest actual secret values beyond a single existence PoC on canary data.

### Area 3 — Lower-level cousin reach around the scoped twin — Lens X (cousin parity)
**Background.** Even where `DescribeSpotFleetInstances` is tag-scopable (Area 1), the instances it enumerates are ordinary EC2 instances and backing Spot Instance requests, reachable by `ec2:DescribeInstances` and `ec2:DescribeSpotInstanceRequests` — actions that are **not** gated by the `spot-fleet-request` tag.
**Security Concern.** A customer who tag-scopes fleet *reads* to achieve team isolation gains nothing if the launched instances remain enumerable through the cousins by their own filters/tags. The isolation claimed via the fleet-tag path leaks through the instance-tag path.
**High-level Test Scenarios.**
- **Claim:** The instance set returned by a tag-denied `DescribeSpotFleetInstances` is still enumerable via `DescribeInstances` (filter `tag:aws:ec2spot:fleet-request-id`) with no fleet-tag condition applying. **Oracle:** the same `instanceId`s appear via the cousin while the fleet path denies. **Severity-if-true:** **Medium** (parity/least-priv hole, intra-account). **Stop condition:** one matched instance id via the cousin settles it.

### Area 4 — Transport / signature-coverage sanity on the read path — Lens Y (secondary, likely null)
**Background/Concern.** The three reads are SigV4 EC2 Query over the regional HTTPS endpoint. Check only for a documented downgrade/enforcement gap.
**High-level Test Scenarios.**
- **Claim:** there is no service-specific way to require TLS/signature floor beyond the account-wide `aws:SecureTransport`/`aws:SignatureVersion` global keys. **Oracle:** `list_ec2.md` shows no transport condition key on these actions (expected). **Severity:** Informational. Likely **null** — recorded for coverage.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Tag/resource `Condition` on `DescribeSpotFleetRequests` is inert → account-wide fleet-config read | IAM authz for the list action | The *supposed* ABAC/resource scoping of Spot Fleet reads (false for this action — only `ec2:Region`) |
| No authorable policy scopes the list read below region | IAM policy model | "Least privilege" / tag-based team isolation claims |
| `UserData`/role-ARN/launch-spec disclosure to any read principal | `SpotFleetRequestConfigData` response | Confidentiality of launch configuration & embedded secrets |
| Cousin actions enumerate fleet instances around the scoped twin | `DescribeInstances`/`DescribeSpotInstanceRequests` | The tag scoping applied to `DescribeSpotFleetInstances` |
| Read surface cannot answer post-decay forensics | history 48 h retention | *(owned by states plan — cross-ref only)* |

---

## 7. Out-of-Scope Risk Categories (state as confidently as in-scope)
- **Cross-account / cross-tenant IDOR on the read APIs** — treated as a near-null (see §8): `DescribeSpotFleetRequests` is explicitly owner-filtered ("Describes **your**…") and all `sfr-` IDs are high-entropy UUIDs, so there is no enumeration path to a foreign fleet. For the two ID-required drill-downs the cross-account outcome is doc-silent (see §8 doc-gap), but gated behind the same unguessable UUID — not a practical cross-tenant path.
- **Mutation, PassRole, SLR-launch guardrail bypass, tag-on-create ABAC widening, lifecycle decay** — owned by the sibling plans; do not re-test here.
- **Service-plane / shared-fleet reach** — the Spot Fleet read path exposes no AWS-owned data-plane; any such leak is a HARD-STOP disclosure item, not a routine lead.
- **IMDS / user-data on the launched instances themselves** — that is the customer's instance posture (and the create/SLR-launch plan's territory), not the read-API surface.
- **Single-tenant self-DoS via large `MaxResults`/pagination** — product behaviour, out of scope.
- **Customer-authored least-privilege mistakes** — only the AWS-owned *inability to scope* (Area 1) is in scope; a customer over-granting `DescribeSpotFleetRequests` to everyone is their footgun.

---

## 8. Null Hypotheses / Doc Gaps (pages checked)
- **Lens A (cross-tenant IDOR): near-NULL, with one scoped doc-gap.** Checked `manage-spot-fleet.md`, `API_DescribeSpotFleetRequests/Instances/RequestHistory`, and the sub-object pages (`SpotFleetRequestConfig(Data)`, `SpotFleetLaunchSpecification`, `ActiveInstance`, `HistoryRecord`, `EventInformation`). The possessive "**your**" owner-filter language is documented **only** on `DescribeSpotFleetRequests`; `DescribeSpotFleetInstances` and `DescribeSpotFleetRequestHistory` are phrased "the specified Spot Fleet[,] request", require a caller-supplied `SpotFleetRequestId`, and the docs are **silent on what happens if that ID belongs to another account** (none of the three pages document a cross-account `AuthFailure`/`UnauthorizedOperation` behaviour). Those two actions **do** carry a `spot-fleet-request*` resource type + `aws:ResourceTag`/`ec2:ResourceTag` in `list_ec2.md`, which implies IAM resource-level ownership scoping — but that is inference, not an explicit doc statement. Net: the real finding is intra-account (Area 1); cross-account is gated behind an unguessable UUID so it is not a practical path, **but** "does `DescribeSpotFleetInstances`/`...RequestHistory` validate ownership of a supplied `sfr-` or only existence" is a legitimate (low-probability, UUID-bounded) confirm-oracle for a hunter who ever obtains a foreign `sfr-` out-of-band (logs, shared config, `eventDescription` leak). The embedded-UUID defense is why this is near-null rather than open.
- **Lens B/C (PassRole/credential vending): N/A here.** No role-ARN *input* on the read path; the role ARN is *output* (Area 2 disclosure). PassRole leads belong to the prerequisites/create siblings — cross-referenced, not restated.
- **Lens G/Q (SSRF / upload): NULL.** Checked all three API pages and `manage-spot-fleet.md` — no field the service dereferences or any blob upload on the read path.
- **Lens H/W (KMS / attestation): N/A** on the read path.
- **Lens O (audit): deferred.** The 48 h/30 s history-decay blind spot is real but **owned by `spot-fleet-states-attack-research-plan.md`** (its O-leads); cited in Area 2, not re-derived.
- **Lens Y (transport): likely NULL** (Area 4) — no service-specific transport condition key; recorded for coverage.
- **Doc gap:** the IAM reference marks the twins' resource type `spot-fleet-request*` (asterisk = resource type required for the action). The exact runtime behaviour of a `DescribeSpotFleetRequests` policy carrying an inert `aws:ResourceTag` condition (over-deny vs skip) is **evaluation-semantics-dependent** and must be confirmed by `iam:SimulateCustomPolicy` before any live call — marked as the first, documentation-safe oracle in Area 1.

---

*Companion to the six existing `*-spot-fleet*` / `*-fleet*` plans in `/work/aws-docs/`. This plan is the read/describe-surface member of the set; it reconciles and promotes the describe-action condition-key asymmetry first noted by the states plan into a fully-developed Lens S/X/U thesis, and inventories the read-API information disclosure, while explicitly deferring mutation, IAM-artifact, PassRole, tagging, and lifecycle-decay leads to their owning siblings.*
