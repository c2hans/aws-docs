# EC2 DescribeFleets — Attack Research Plan
Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleets.html (+ API_FleetData, API_DescribeFleetError, API_DescribeFleetsInstances, API_LaunchTemplateAndOverridesResponse); Service Authorization Reference `list_ec2.md` L6822-6826 (offline mirror, verified online). Status: documentation-derived hypotheses only; nothing tested against a live account.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. `AWSServiceRoleForEC2Fleet`, an internal role surfaced in an `errorMessage`), stop, preserve evidence, flag for AWS-Security disclosure.
- **DryRun trap:** `DryRun=true` returns `DryRunOperation`/`UnauthorizedOperation` on **caller IAM only**, evaluated *before* resource resolution — it is NOT an ownership oracle. Do not treat a DryRun success as proof of access to a specific fleet.

## 1. Pentest Objectives (concrete breach outcomes)
1. **Account-wide fleet enumeration despite a tag-scoped policy** — read `fleetId` + full launch config of EC2 Fleets the caller was intended to be restricted away from, because `DescribeFleets` accepts no resource-level/ABAC scoping (only `ec2:Region`).
2. **Cross-account fleet read** — return another account's `FleetData` by supplying its `FleetId` (ownership-vs-existence on a List action).
3. **Sensitive config/identity disclosure** — recover launch-template specs (AMI, IAM instance profile, subnets, user-data pointer), launched `instanceIds`, and free-text `errorMessage` internals from the response, enabling downstream targeting or service-plane leak.
4. **Pagination/continuation re-authorization gap** — reuse a `NextToken` across identity/filter context to read items a fresh authorized call would not return.

## 2. Components, Assets, and Design
- **Interface:** EC2 Query API (SigV4, `Action=DescribeFleets`, API version 2016-11-15), public regional endpoint, Internet-reachable. SDK-surfaced (CLI/boto3/etc.).
- **Operation class:** read-only. Service Authorization Reference access level = **List**.
- **Resource:** EC2 Fleet. ARN `arn:${Partition}:ec2:${Region}:${Account}:fleet/${FleetId}` (account embedded). `FleetId` is high-entropy `fleet-<uuid>` → **not brute-enumerable** (pure-guessing IDOR is a genuine null; cross-account requires a *leaked* ID).
- **Request params:** `FleetId.N` (opt), `Filter.N` (activity-status | excess-capacity-termination-policy | fleet-state | replace-unhealthy-instances | type), `MaxResults`, `NextToken`, `DryRun`. **Behavioral quirk:** `instant`-type fleets are omitted from the response *unless* their `FleetId` is explicitly named — a listing-completeness asymmetry (Lens O).
- **Response — `fleetSet[] FleetData`** (the asset being disclosed). Notable fields:
  - `launchTemplateConfigs[]` → `LaunchTemplateAndOverridesResponse`: launch-template id/version + overrides (AMI/`ImageId`, `SubnetId`, `IamInstanceProfile`, instance type, etc.) — full launch spec.
  - `fleetInstanceSet[]` (`DescribeFleetsInstances`, `instant` only): `instanceIds[]`, `instanceType`, `lifecycle`, `platform`, `launchTemplateAndOverrides`.
  - `errorSet[]` (`DescribeFleetError`, `instant` only): `errorCode`, **`errorMessage` (free String)**, `launchTemplateAndOverrides`, `lifecycle`.
  - `tagSet[]`, `targetCapacitySpecification`, `spotOptions`/`onDemandOptions`/`reservedCapacityOptions`, `type`, `fleetState`, `activityStatus`, `validFrom/validUntil`, `createTime`, `clientToken`.
  - **`context` — "Reserved."** (undocumented field; doc-gap, probe what it reflects).
- **Ownership model:** a fleet (esp. `maintain`) is backed by the service-linked role `AWSServiceRoleForEC2Fleet` which launches/replenishes instances asynchronously — service-plane identity; any surfacing of it is a HARD STOP.

```
caller (SigV4 IAM principal)
        │  Action=DescribeFleets  (List; only ec2:Region conditionable)
        ▼
  EC2 control plane ──reads──► Fleet records (account-owned, fleet-<uuid>)
        │                         ├─ launchTemplateConfigs (AMI/profile/subnet/overrides)
        │                         ├─ fleetInstanceSet (instanceIds)      [instant only]
        └─ returns fleetSet[] ───►└─ errorSet.errorMessage (free text)   [instant only]
```

## 3. API / Interface Inventory
| Name | Method | Mutating | Facing | Functionality | From Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| DescribeFleets | SigV4 Query | No (List) | External | Describe one/all EC2 Fleets | Yes | any principal w/ `ec2:DescribeFleets` | **No resource type; only `ec2:Region`** — cannot be tag/ARN-scoped |
| DescribeFleetInstances | SigV4 | No | External | Per-fleet instances | Yes | `fleet*` + ResourceTag scopable | sibling — *is* scopable (asymmetry) |
| DescribeFleetHistory | SigV4 | No | External | Per-fleet event history | Yes | `fleet*` + ResourceTag scopable | sibling — *is* scopable; see [[ec2-describefleethistory-surface]] |
| CreateFleet | SigV4 | Yes | External | Create fleet (launch) | Yes | composite launch | see [[ec2-createfleet-surface]] |

**Undocumented/hidden knob:** response field `context` = "Reserved." — not surfaced in prose; confirm whether it is ever populated and with what (reflected input vs internal metadata).

## 4. Trust-Boundary Map
| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Restricted intra-account principal (tag-scoped on sibling APIs) | All fleets in the account | `DescribeFleets` with no FleetId → bulk list | Returns a `fleetId`/config the admin's tag scope intended to hide — **DescribeFleets being unscopable is the boundary breach** |
| Caller in account A | Fleet owned by account B | `FleetId.N` naming a foreign fleet | Response returns B's `FleetData` instead of empty/`InvalidFleetId.NotFound` |
| Any caller | Launch-spec / instanceIds / error internals | Response `FleetData` sub-objects | Recovering AMI/profile/subnet/user-data pointer, live `instanceIds`, or internal detail in `errorMessage` |
| Any customer surface | AWS service plane | `errorMessage` / `context` / role refs | Any `AWSServiceRoleForEC2Fleet` or AWS-internal ARN/account surfaced = **HARD STOP** |

## 5. Recommended Areas of Focus (firing lenses, priority order)

### AREA 1 — ABAC/resource-scoping gap: DescribeFleets is structurally unscopable (Lens S / X / U) — **TOP PRIORITY**
**Background:** The Service Authorization Reference row for `ec2:DescribeFleets` lists **no resource type (none required)** and **only `ec2:Region`** as a condition key (`list_ec2.md` L6824-6826). Its per-fleet siblings `DescribeFleetInstances` and `DescribeFleetHistory` *are* scopable by `fleet*` + `aws:/ec2:ResourceTag` (L6810-6820).
**Security Concern:** An operator who tag-scopes the per-fleet siblings (believing fleet visibility is contained) has **not** contained `DescribeFleets` — a restricted principal can bulk-list every fleet in the account and read full launch configs. This is also the feeder that defeats the high-entropy-ID defense: it hands the caller the `fleetId`s needed to then call the scoped per-fleet APIs. Additionally (cross-check, Lens U): the EC2 User Guide `iam-policies-for-amazon-ec2.md` asserts blanket that "EC2 `Describe*` actions do not support resource-level permissions" — settle whether any attempt to tag-scope a Describe is silently ignored (advisory) vs rejected.
**High-level Test Scenarios:**
- Claim: *A principal allowed `ec2:DescribeFleets` but Deny'd/omitted on tagged fleets still sees all fleets.* → Oracle: attach a policy that attempts `Condition: ec2:ResourceTag` or a `Resource: arn:...:fleet/...` restriction on `DescribeFleets`; observe whether it is rejected at policy save, silently ignored, or enforced. A full `fleetSet[]` returned under a would-be-restrictive policy confirms the gap.
- Claim: *No condition key exists to constrain DescribeFleets beyond region.* → Confirm by enumerating accepted keys; a `fleet/*`-scoped Allow produces `AccessDenied` on the whole action (not per-fleet filtering) or is a no-op.
**Doc evidence:** `list_ec2.md` L6822-6826; sibling rows L6810-6820. **Severity-if-true:** Medium–High (intra-account containment bypass; High where fleet visibility is the intended isolation control). Settleable with 1 policy + 1 call — **gates Areas 2 & 4**.

### AREA 2 — Cross-account fleet read by FleetId (Lens A: ownership-vs-existence)
**Background:** `DescribeFleets` resolves `FleetId.N`. The ARN embeds account, but the action has no owner/condition binding beyond region.
**Security Concern:** Does the action validate that the named `FleetId` is **owned by the caller's account**, or only that it **exists**? A `request`/`maintain` fleet omitted from a caller's list might still be fetchable by direct ID.
**High-level Test Scenarios:**
- Claim: *Supplying a foreign-account `FleetId` returns its `FleetData`.* → Oracle: with a known second-account `fleet-<uuid>` (leaked/shared, not guessed), call `DescribeFleets --fleet-ids`. Breach = foreign `FleetData`; refute = `InvalidFleetId.NotFound`/empty.
- Error-differential oracle (Lens A variant): compare response for (a) nonexistent ID, (b) malformed ID, (c) existing-foreign ID — distinct `InvalidFleetId.NotFound` vs `InvalidFleetId.Malformed` vs `200 empty` forms an existence oracle across the account boundary.
**Preconditions:** a leaked foreign `FleetId` (IDs are high-entropy → not brute-forceable; pure enumeration = null). **Severity-if-true:** cross-account = High–Critical. **Stop:** if response contains any service-plane identity.

### AREA 3 — Response disclosure surface (Lens A-disclosure / K-adjacent / service-plane HARD STOP)
**Background:** `FleetData` returns launch configs, `instanceIds` (instant), tags, and a **free-text `errorMessage`**; `context` is "Reserved."
**Security Concern:** The response concentrates downstream-targeting intel and may leak internals:
- `launchTemplateConfigs` / `launchTemplateAndOverrides`: AMI id, `IamInstanceProfile`, `SubnetId`, instance type — a map for lateral-movement/privesc targeting (chains to [[ec2-createfleet-surface]] / [[ec2-associate-iam-instance-profile-surface]]).
- `fleetInstanceSet.instanceIds`: live instance IDs for `instant` fleets.
- **`errorMessage` (free String):** per the sibling-corpus (`eventDescription` leaks), free-text error fields historically carry role names, invalid-IAM-role detail, and internal descriptors. An AWS-internal role/ARN here = **HARD STOP + disclosure**.
- `context` "Reserved.": probe whether it reflects caller input (→ stored/echo concern) or internal data.
**High-level Test Scenarios:** enumerate every field actually populated on a real fleet; grep `errorMessage` for role ARNs / internal hostnames / account IDs not the caller's; verify `context` content.
**Doc evidence:** API_FleetData, API_DescribeFleetError (`errorMessage`), API_DescribeFleetsInstances (`InstanceIds`). **Severity-if-true:** Low on its own (own-account intel); **Critical** if service-plane identity surfaces.

### AREA 4 — NextToken / pagination re-authorization (Lens A / M)
**Background:** `MaxResults` + opaque `NextToken` continuation; `DescribeFleets` common pagination.
**Security Concern:** Is the continuation token bound to the original caller identity, region, and filter set — or does it encode a server-side cursor that, when replayed, returns items without re-evaluating authorization/filters?
**High-level Test Scenarios:**
- Claim: *A `NextToken` minted under one filter/identity context returns items outside that context when replayed.* → Oracle: obtain a token, then replay it with altered `Filter.N` / from a differently-scoped principal; breach = items the second context should not see, or filter not re-applied on the continuation page.
**Severity-if-true:** Medium (depends on Area 1/2 outcome). **Precondition:** gated by whether scoping exists at all (Area 1).

### AREA 5 — Listing-completeness / detection blind-spot (Lens O / U)
**Background:** `instant` fleets are **omitted unless their FleetId is explicitly specified** (documented in both DescribeFleets and FleetData). `activityStatus`/`fleetState` enumerations exist.
**Security Concern:** A monitoring/inventory control built on `DescribeFleets` (no FleetId) silently misses all `instant` fleets → an attacker who launches via `instant` fleets evades a fleet-inventory-based detection. Also: does a deleted/`deleted_running` fleet's config remain readable, creating a post-deletion disclosure window?
**High-level Test Scenarios:** confirm a known `instant` fleet is absent from a no-FleetId call; confirm it appears only when named; confirm visibility of `deleted*`-state fleets.
**Severity-if-true:** Low–Informational (detection evasion / enabler).

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Tag-scoped principal bulk-lists all fleets | IAM authz on DescribeFleets | "resource-level permissions" / ABAC — **absent for this action** (only ec2:Region) |
| Cross-account read via FleetId | Fleet resolver | ARN account binding — verify enforced, not just existence |
| Launch-spec/instanceId/errorMessage leak | FleetData response | shared-responsibility; no documented redaction of free-text error fields |
| Service-plane role/ARN in errorMessage | errorMessage free String | none documented → HARD STOP if hit |
| NextToken replay across context | pagination | token binding to identity/filter — unstated (doc gap) |
| instant-fleet inventory evasion | response omission rule | documented behavior, not a mitigation → detection gap |

## 7. Out-of-Scope Risk Categories
- Pure brute-force enumeration of `fleet-<uuid>` IDs (high entropy — genuine null; cross-account read needs a *leaked* ID, not a guessed one).
- Mutating fleet actions (CreateFleet/ModifyFleet/DeleteFleets) — separate plans ([[ec2-createfleet-surface]], [[ec2-deletefleets-surface]]).
- A customer self-authoring an over-broad `ec2:DescribeFleets` grant (customer footgun) — *except* the structural unscopability in Area 1, which is an AWS-owned property of the action and is in scope.
- IMDS on managed fleet hosts; shared EC2 control-plane infra; single-tenant self-DoS.
- `DryRun` as an ownership oracle (false-positive trap — caller-IAM only).

## 8. Null hypotheses / doc gaps
- **Lens G (SSRF) — NULL.** Read DescribeFleets + FleetData + all sub-structs; no field the service dereferences/fetches (read-only describe; `resolve:ssm` lives on the *create* path, not here).
- **Lens Q (upload) — NULL.** No blob/file input or output.
- **Lens B/C (PassRole/vending) — NULL for this action.** DescribeFleets takes no role ARN and vends no credentials (the `AWSServiceRoleForEC2Fleet` coupling lives on CreateFleet/maintain lifecycle, not on read).
- **Lens F / K / FF / W / H / T / N / V / D / BB / CC / DD / AA / Y — NULL.** Single-hop SigV4 read: no translator/parser, no LLM, no JWT/OIDC, no attestation, no KMS context, no persisted-secret, no namespace migration, no network segmentation hop, no multi-parser routing, no upstream-context header, no caching knob, no share/revoke, no transport-floor claim specific to this action.
- **Lens I (tagging) — partial/NULL:** `tagSet` is returned but DescribeFleets does not mutate tags; relevance is only that tags here cannot be used to scope the action (folded into Area 1).
- **Doc gap:** `context` field = "Reserved." — behavior undocumented; probe before concluding. `NextToken` binding semantics undocumented → Area 4 is a doc-gap lead, confirm surface live first.
```
