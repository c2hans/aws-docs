# EC2 DescribeFleetHistory — Attack Research Plan
Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleetHistory.html (+ `.md` mirror); supporting shapes API_HistoryRecordEntry, API_EventInformation; IAM service-authorization ref `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (rows L6810-6826 DescribeFleetHistory/Instances/Fleets, L7404-7411 Spot twins, resource ARN L9941). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- This is a **read-only / List** action (IAM access level: List). The attack value is therefore concentrated in: (1) cross-tenant / cross-scope **read**, (2) **ABAC tag-scoping** that may silently fail, (3) **sibling-parity** enumeration paths, (4) **information disclosure** through free-form event descriptions, (5) **audit/retention blind spots**. Mutation lenses largely do not fire — see §8.
- **Priority:** settle **Area 2 (ABAC enforcement doc-contradiction)** first — it is settleable with one IAM policy + one API call and its outcome determines whether Areas 1/3/5 are real cross-fleet disclosure paths or same-account curiosities.
- **DryRun trap (from prior corpus):** `DryRun=true` is evaluated against caller IAM *before* resource resolution. A `DryRunOperation` response is **caller-IAM only and is NOT an ownership oracle**. Do not treat a DryRun success against a foreign FleetId as cross-tenant access.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Watch especially the `iamFleetRoleInvalid` event descriptions — if one ever surfaces an AWS-internal fleet role rather than the customer's role, stop.)

## 1. Pentest Objectives
1. Read the event history of a **fleet owned by another account/tenant** by naming its `FleetId` directly (cross-account IDOR on a resource-scoped List action).
2. Defeat a **tag-based (ABAC) scoping policy** that an admin applied to `DescribeFleetHistory`, either by (a) the List action silently ignoring resource-level permissions, or (b) reaching the same fleet metadata through an **unscoped sibling** (`DescribeFleets`, `DescribeFleetInstances`).
3. Extract **sensitive internal data** (instance IDs, IAM fleet-role identifiers, load-balancer targets, launch-spec/config detail, Spot-price internals) from `eventDescription` that other APIs would gate more tightly.
4. Replay a **pagination `NextToken`** minted for fleet A against a request naming fleet B (cross-resource token confusion).
5. Use the **48h retention / 30s delay** contract to make a security-relevant fleet change (deletion, role swap, scale event) invisible to a history-based detector.

## 2. Components, Assets, and Design
**Interface.** EC2 Query/JSON API action `DescribeFleetHistory`, EC2 service endpoint, SigV4 IAM auth. Non-mutating; IAM access level **List**.

**Request parameters.**
- `FleetId` (String, **required**) — the EC2 Fleet whose history is read. Caller-supplied identifier; this is the IDOR-relevant input.
- `StartTime` (Timestamp, **required**) — window start.
- `EventType` (String, optional) — `instance-change | fleet-change | service-error`.
- `MaxResults` (Integer, optional) / `NextToken` (String, optional) — pagination.
- `DryRun` (Boolean, optional) — permission probe (see DryRun trap above).

**Response / assets returned.**
- `fleetId`, `startTime`, `lastEvaluatedTime` (absent when `nextToken` present), `nextToken`, `requestId`.
- `historyRecordSet[]` → `HistoryRecordEntry{ eventType, timestamp, eventInformation }`.
- `EventInformation{ eventDescription (free-form String), eventSubType, instanceId }`.
  - `instanceId` present for `instanceChange` events → leaks instance IDs of the fleet's hosts.
  - `eventSubType` enumerates operational state incl. `iamFleetRoleInvalid` (role permission failures), `registerWithLoadBalancersFailed`, `allLaunchSpecsTemporarilyBlacklisted`, `launchSpecUnusable`, `spotInstanceCountLimitExceeded`, `spotFleetRequestConfigurationInvalid`, `active/deleted/deleted_running/deleted_terminating/expired/modify_in_progress/modify_succeeded/submitted/progress`.
  - `eventDescription` is free text that the docs repeatedly say carries "more information" about failures → the leak surface.

**Resource / identifier shape.**
- Fleet ARN: `arn:${Partition}:ec2:${Region}:${Account}:fleet/${FleetId}` — **account is embedded**, so resource-level IAM CAN bind ownership. `FleetId` is a high-entropy `fleet-<uuid>` value → **not enumerable** by brute force (pure-enumeration IDOR is a genuine null; cross-account access requires knowing/leaking the ID).
- Data retention: events are **delayed up to 30s** and **retained 48h**.

**Identity / roles.** SigV4 IAM principal. The fleet itself runs under an IAM fleet role (`iamFleetRole` for Spot/legacy; the launch-template-referenced instance profile for EC2 Fleet) — this role's *name/validity* can surface in event descriptions but the role credentials are not returned.

```
Caller (SigV4 IAM principal)
   │  DescribeFleetHistory(FleetId, StartTime, [EventType,NextToken,DryRun])
   ▼
EC2 control plane ── IAM authz on resource  arn:...:fleet/${FleetId}
   │                 (condition keys: ec2:ResourceTag, aws:ResourceTag, ec2:Region)
   ▼
Fleet event store (48h TTL, 30s ingestion delay)
   └── historyRecordSet[] { eventType, timestamp, EventInformation{desc, subtype, instanceId} }
```

## 3. Trust-Boundary Map
| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller account A | Fleet owned by account B | `FleetId` in request body; ARN is account-scoped | A reads B's `historyRecordSet` (any record for a fleet A does not own = breach) |
| Low-priv principal, tag-scoped by admin | Fleet *not* carrying the required tag | `ec2:ResourceTag` condition on `DescribeFleetHistory` | History returned for a fleet whose tag should have denied it = ABAC bypass |
| Low-priv principal denied history on fleet X | Same fleet X via a sibling action | `DescribeFleets` (no resource scoping) / `DescribeFleetInstances` | Fleet config / instance IDs obtained through the sibling the policy didn't cover |
| Holder of a `NextToken` for fleet A | Fleet B's event page | Opaque pagination token replayed with `FleetId=B` | B's records returned under a token minted for A = cross-resource token confusion |
| Any caller | AWS service-plane identity | `eventDescription` / `iamFleetRoleInvalid` text | An AWS-internal role/account/ARN appears in a description = HARD STOP, disclosure |

## 4. API / Interface Inventory
| Name | Method | Mutating | Ext-facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| **DescribeFleetHistory** | Query/JSON | No (List) | Yes | Events for one EC2 Fleet in a window | Yes (SigV4) | Principals with `ec2:DescribeFleetHistory` on `fleet*` | Required resource `fleet*`; keys `ec2:ResourceTag`,`aws:ResourceTag`,`ec2:Region` |
| DescribeFleetInstances | Query/JSON | No (List) | Yes | Running instances of a fleet | Yes | `fleet*` + same tag keys | Sibling leak path (instance IDs) |
| DescribeFleets | Query/JSON | No (List) | Yes | List one/many fleets + config | Yes | **No resource type**, only `ec2:Region` | **Cannot be tag-scoped** → account-wide enumeration path |
| DescribeSpotFleetRequestHistory | Query/JSON | No (List) | Yes | Events for a Spot Fleet request | Yes | `spot-fleet-request*` + tag keys | Twin of target (symmetric scoping); shares `EventInformation` model |
| DescribeSpotFleetRequests | Query/JSON | No (List) | Yes | List Spot Fleet requests | Yes | No resource type | Looser sibling (as DescribeFleets) |

Undocumented-knob check: no non-SDK/console-hidden parameter on this action; `EventType` enum is closed (3 values). No auth-weakening field accepted. Primary delta worth noting is the **IAM-reference delta**: singular history/instances actions are resource-scoped; the plural list actions are not.

## 5. Recommended Areas of Focus

### Area 1 — Cross-account / cross-scope history read (Lens A) — HIGHEST
Background: `FleetId` is caller-supplied and the fleet ARN embeds `${Account}`; `DescribeFleetHistory` requires resource type `fleet*`, which *implies* the control plane resolves and ownership-checks the fleet.
Security Concern: a resource-scoped List action can validate **existence** without validating **ownership**, or can honor a `fleet/*` wildcard grant across accounts.
High-level Test Scenarios (falsifiable):
- **Claim:** A principal in account A can retrieve `historyRecordSet` for a `FleetId` owned by account B. → **Mechanism:** ARN `arn:...:${Account}:fleet/${FleetId}`; action authorizes on `fleet*`. → **Oracle:** supply B's real FleetId from A with `ec2:DescribeFleetHistory` on `Resource:"*"`; any returned record = cross-account breach; `InvalidFleetId.NotFound`/`AccessDenied` = refute. → **Preconditions:** know B's FleetId (high-entropy UUID → must be leaked, e.g. from a shared CloudFormation output, a log, a cross-account role). → **Cost:** low. → **Severity-if-true:** Critical (cross-account data).
- **Claim (error oracle, Lens A variant):** the not-found vs access-denied vs 500 response differs enough to confirm *existence* of a foreign FleetId. → **Oracle:** compare responses for (a) well-formed nonexistent ID, (b) well-formed foreign-owned ID, (c) malformed ID; distinct codes/latency = enumeration oracle. → **Severity:** Low (ID is high-entropy; existence-only leak).
Doc evidence: request `FleetId` Required; IAM row L6810-6814; ARN L9941. Severity-if-true: Critical / Low.

### Area 2 — ABAC tag-scope silently ignored on a List action (Lens S / I / U) — SETTLE FIRST (gates Areas 1, 3, 5)
Background: the IAM row advertises `ec2:ResourceTag/${TagKey}` and `aws:ResourceTag/${TagKey}` on `DescribeFleetHistory`, so an admin may write a policy that only allows history reads on fleets tagged e.g. `team=web`.
**Doc-vs-doc contradiction (the key lead — Lens U):** the two AWS docs disagree about whether this is even possible.
- Service Authorization Reference (`list_ec2.md` L6810-6814) says `DescribeFleetHistory` requires resource `fleet*` **and supports `ec2:ResourceTag`/`aws:ResourceTag`** → implies enforced.
- EC2 User Guide `iam-policies-for-amazon-ec2.md` (L72-73, L351; confirmed on the live `.html`, not a sync artifact) states blanket: *"the Amazon EC2 `Describe*` API actions do not support resource-level permissions"* and *"the `Describe` actions do not support resource-level permissions, so you must specify them in a separate statement without conditions."*
Security Concern: if the User Guide is right, a tag-scoped `DescribeFleetHistory` policy is **advisory only** — the condition is silently ignored and every fleet's history is readable to any principal with the action on `ec2:Region`. This is settleable with **one IAM policy + one API call**, and its outcome gates Areas 1/3/5 (if ResourceTag is ignored, those become real cross-fleet disclosure paths rather than same-account curiosities). It may also fail *closed* and wrongly deny legitimate reads.
High-level Test Scenarios:
- **Claim:** a policy `Allow DescribeFleetHistory where ec2:ResourceTag/team = web` still returns history for a fleet tagged `team=db`. → **Oracle:** under a scoped role holding exactly that policy, call against a `team=db` fleet in the *same account*; records returned = ABAC bypass; `AccessDenied` = enforced. → **Severity:** High (ABAC is the access-control mechanism here).
- **Claim (binding):** does the condition bind the tag on the **queried fleet**, or on something else (Lens S "binds-wrong-resource" shape)? → **Oracle:** `iam:SimulatePrincipalPolicy` first (no resources touched), then a scoped live call with canary-tagged fleets. → **Severity:** High.
- **Claim (self-widen, Lens S):** can the scoped principal also `CreateTags` on a fleet to grant itself the gating tag? → route to CreateTags surface ([[ec2-createtags-surface]]); if yes the ABAC is self-defeating. → **Severity:** High.
Doc evidence: IAM row condition keys L6813. Severity-if-true: High.

### Area 3 — Sibling parity: unscoped bulk-list feeder (Lens X) — HIGH
Background: the EC2-Fleet and Spot-Fleet twins are actually **symmetric** (both `*History`/`*Instances` take an ID and are `fleet*`/`spot-fleet-request*`+ResourceTag scopable). The real split is **bulk-list vs per-ID**: `DescribeFleetHistory`/`DescribeFleetInstances` require `fleet*` and are tag-scopable; **`DescribeFleets` requires no resource type and carries only `ec2:Region`** (L6822-6826), as does `DescribeSpotFleetRequests` (L7410). The bulk-list actions cannot be tag-denied.
Security Concern: an admin who tag-scopes `DescribeFleetHistory` to contain a principal to its own team's fleets has **not** contained `DescribeFleets`, which lists *every* fleet in the account (IDs + config) and cannot be tag-denied. The principal enumerates all FleetIds via `DescribeFleets`, then — if Area 2 proves the history action also under-enforces — reads every fleet's history; even if Area 2 is enforced, `DescribeFleets` itself already leaks fleet configuration intra-account.
High-level Test Scenarios:
- **Claim:** a principal denied `DescribeFleetHistory` on all but its tagged fleets can still enumerate all fleet IDs and launch configs via `DescribeFleets`. → **Oracle:** scoped role with tag-limited history + plain `DescribeFleets`; `DescribeFleets` returns fleets outside the tag scope = parity gap. → **Severity:** Medium–High (intra-account least-privilege break; the sibling is AWS-defined, not customer-editable — the *scoping gap* is a documentation/consistency defect worth noting, the policy itself is customer-authored).
- **Claim (twin data-model reuse):** `DescribeSpotFleetRequestHistory` returns the *same* `EventInformation` structure — does any EC2-Fleet-created resource expose a parallel `spot-fleet-request` representation whose history is reachable under the (separately-scoped) Spot action? → **Oracle:** check whether a CreateFleet request in `instant`/`maintain` mode registers a describable spot-fleet-request. → **Severity:** Medium.
Doc evidence: L6810-6826, L7404-7411. Severity-if-true: Medium–High.

### Area 4 — Information disclosure via free-form event text (Lens A disclosure)
Background: `eventDescription` is an unbounded String the docs say carries "more information" for `allLaunchSpecsTemporarilyBlacklisted`, `spotFleetRequestConfigurationInvalid`, `launchSpecTemporarilyBlacklisted`, `registerWithLoadBalancersFailed`, `iamFleetRoleInvalid`; `instanceId` is returned for every `instanceChange`.
Security Concern: history read is a **List** action (coarse-grained), yet the content it returns (instance IDs, the identity/validity of the IAM fleet role, load-balancer registration targets, launch-spec/config detail, Spot-price internals) is information a more privileged `Describe*`/`iam:*` call would otherwise gate. Whoever can read history gets a cheap inventory + failure-reason oracle for the fleet.
High-level Test Scenarios:
- **Claim:** `eventDescription` for `iamFleetRoleInvalid` names the fleet role ARN / permission detail, usable to map the victim's IAM. → **Oracle:** induce/read such an event; inspect description for role ARN or policy detail. → **Severity:** Low–Medium (info leak; **HARD STOP if it ever names an AWS-internal role**).
- **Claim:** `instanceId` + description together reconstruct the fleet's instance inventory and scaling pattern for a principal who cannot `DescribeInstances` those instances. → **Oracle:** compare the set of instanceIds from history vs what `DescribeInstances` returns under the same scoped role. → **Severity:** Low–Medium.
- **Claim (config leak, doc-confirmed shape):** `eventDescription` carries launch-spec/pricing internals verbatim. → **Mechanism:** the sibling `DescribeSpotFleetRequestHistory` sample response (`API_DescribeSpotFleetRequestHistory.md` L130) shows `eventDescription = "m3.medium, ami-1ecae776, Linux/UNIX (Amazon VPC); old price: 0.0153, new price: 0.0153"` for a `price_update` event, and `EventInformation` is explicitly the shared type for both EC2 Fleet and Spot Fleet; `allLaunchSpecsTemporarilyBlacklisted`/`registerWithLoadBalancersFailed` say "see the description of the event" → instance types, AMIs, AZs, LB target ARNs land in free text. → **Oracle:** trigger such an event and diff the literal description against the account's real ARNs/config. → **Severity:** Low–Medium.
Doc evidence: API_EventInformation (eventDescription/eventSubType/instanceId); API_DescribeSpotFleetRequestHistory L130. Severity-if-true: Low–Medium.

### Area 5 — Pagination-token cross-resource replay (Lens A / M)
Background: `NextToken` is opaque; the docs do not state it is bound to the originating `FleetId`. Note the structural quirk: `lastEvaluatedTime` is *omitted* when `nextToken` is present.
Security Concern: if the token encodes a query cursor but the server trusts the token's embedded fleet scope instead of re-authorizing the `FleetId` on the continuation call, a token minted for fleet A (which the caller owns) could page fleet B's records — or vice-versa, pass `FleetId=B` with A's token.
High-level Test Scenarios:
- **Claim:** calling `DescribeFleetHistory(FleetId=B, NextToken=<token-for-A>)` returns A's (or B's) records without re-checking authorization on the *effective* fleet. → **Oracle:** mint a token on an owned fleet A, replay with a foreign/other FleetId B; inspect whether records returned correspond to A (token-trusted scope, authz skipped on continuation) or B (and whether B was authorized). → **Preconditions:** own one fleet, know one other FleetId. → **Severity:** High if continuation skips re-authz. → **Cost:** low.
Doc evidence: NextToken/lastEvaluatedTime response elements; Query-Requests pagination. Severity-if-true: High.

### Area 6 — Retention / delay as a detection blind spot (Lens O / U)
Background: "EC2 Fleet events are delayed by up to 30 seconds… available for 48 hours." The docs present `lastEvaluatedTime` as a completeness guarantee ("query by the last evaluated time and not miss a recorded event").
Security Concern: (a) any history-based detector has a hard **48h horizon** — a fleet deletion (`deleted`/`deleted_running`), role swap, or scale event older than 48h is unobservable here; (b) the 30s delay + lastEvaluatedTime contract is an ordering assumption — if an event is ingested out of order relative to a poller's `lastEvaluatedTime`, a detector can miss it (integrity gap in the stated guarantee).
High-level Test Scenarios:
- **Claim:** a `fleet-change` event (e.g. `deleted_running`) ages out of the 48h window, leaving no record via this API. → **Oracle:** confirm retention; cross-check whether the same event persists in CloudTrail/EventBridge (the doc points to EventBridge for monitoring) — if history is the only source, the blind spot is real. → **Severity:** Informational–Low (enabler; raises the value of audit-evasion chains).
- **Claim:** two events with timestamps straddling a poller's `lastEvaluatedTime` under the 30s delay can cause a gap. → **Oracle:** reason about ingestion-order vs timestamp-order from docs; flag as doc-gap if unspecified. → **Severity:** Low.
Doc evidence: API intro paragraph (30s/48h/lastEvaluatedTime). Severity-if-true: Low.

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account history read by FleetId | control-plane IAM authz on `fleet*` | Required resource type `fleet*` + account-scoped ARN (claim: ownership actually enforced) |
| ABAC tag-scope bypass / silent no-op | `ec2:ResourceTag` on List action | Resource-level permission enforcement for a Describe/List action |
| Unscoped sibling enumeration | `DescribeFleets` (no resource type) | None documented — the sibling is inherently account-wide |
| NextToken cross-resource replay | pagination continuation authz | Opaque token (claim: token re-binds/re-authorizes the FleetId) |
| Sensitive data in `eventDescription` | event store content | None (free-form string surfaced to any List-capable principal) |
| Detection evasion via 48h expiry | event store retention | 48h retention + EventBridge/CloudTrail as the durable source |

## 7. Out-of-Scope Risk Categories
- Mutation of fleet state (this action is read-only; mutation lives in CreateFleet/ModifyFleet/DeleteFleets — see [[ec2-createfleet-surface]], [[ec2-deletefleets-surface]]).
- Pure brute-force enumeration of `FleetId` (high-entropy UUID → infeasible; cross-account access requires a *leaked* ID, which is the in-scope path).
- Shared AWS fleet/host infrastructure, IMDS on managed hosts, product/feature gaps.
- DryRun used as an ownership oracle (known false-positive trap — see §0).
- A principal reading its *own* account's fleet history (intended behavior).

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens G (SSRF) — N/A:** read all request parameters (FleetId, StartTime, EventType, MaxResults, NextToken, DryRun); none is a URL/host/location the service dereferences. No profile/branding/import field exists on this action.
- **Lens Q (upload) — N/A:** no blob/file/image parameter; response content is JSON text only.
- **Lens B/C (PassRole / credential vending) — N/A as input:** no `roleArn`/credential-provider parameter. *But* `eventDescription`/`iamFleetRoleInvalid` can *reveal* the fleet role identity (covered under Area 4; hard-stop if AWS-internal).
- **Lens F (injection / parser) — thin:** the only server-parsed opaque input is `NextToken` (covered under Area 5 as token confusion, not a translation layer). No wire-protocol/SQL/BSON translation.
- **Lens K/H/W/T/EE/AA/N/V/D — N/A:** no LLM, no KMS/encryption-context, no attestation, no generated secret, no predictable namespace, no share/revoke, no namespace migration, no network-interface/control-plane reachability surface on a control-plane read action.
- **Lens BB/CC/DD/FF/Y — N/A:** this is a single-hop SigV4 Query API action — no front authorizer/WAF/router chain, no asserted-upstream identity header, no response/authz caching layer, no JWT/OIDC token validation. SigV4 signature-coverage gaps (UNSIGNED-PAYLOAD, presigned replay) do not apply to a standard signed Query request; noted as N/A.
- **Doc CONTRADICTION (not just a gap) — ABAC enforcement:** the Service Authorization Reference (tag-scopable) and the EC2 User Guide ("Describe* do not support resource-level permissions") directly disagree (Area 2) — this is the #1 lead; settle it live with one policy + one call before trusting ANY tag-scoped fleet-read policy.
- **Doc gap — NextToken binding:** the docs do NOT state whether `NextToken` re-authorizes the `FleetId` on continuation (Area 5) — confirm surface first.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
