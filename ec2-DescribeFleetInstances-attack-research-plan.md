# EC2 DescribeFleetInstances — Attack Research Plan
Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFleetInstances.html (+ .md mirror), API_ActiveInstance, API_DescribeFleets, API_Filter; Service Authorization Reference `list_ec2.md` L6816-6826 (verified 2026-10-22). Sibling plan: `ec2-DescribeFleetHistory-attack-research-plan.md`. Status: documentation-derived hypotheses only; nothing tested against a live account.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- This is a **read-only (IAM access level: List), non-mutating, single-hop SigV4 Query API.** There is no write primitive, no URL fetch, no upload, no role input, no LLM, no KMS, no parser-of-attacker-blobs. The entire attack surface is **information disclosure via authorization gaps** on a resource-by-ID describe + its **sibling-authorization asymmetry**. Calibrate severity accordingly: the realistic ceiling here is cross-tenant/cross-account metadata disclosure and an ABAC-containment bypass, not RCE.
- HARD STOP: the moment any returned `instanceId`, `spotInstanceRequestId`, role name, or account belongs to AWS's own service plane (e.g. a fleet owned by an AWS-internal account, an `AWSServiceRoleForEC2Fleet`-managed resource outside your tenant), stop, preserve evidence, flag for AWS-Security disclosure.

## 1. Pentest Objectives
1. Read the running-instance set (`instanceId`, `instanceType`, `spotInstanceRequestId`, `instanceHealth`) of an **EC2 Fleet owned by another account** by naming its `FleetId` directly → cross-account IDOR.
2. Prove that a tag-scoped IAM policy intended to **contain** which fleets a principal may introspect is **advisory / silently ignored** on this Describe action → ABAC-containment bypass (the #1 lead; it gates leads 2/3).
3. Prove the **sibling-authorization asymmetry**: a `fleet*`+ResourceTag-scoped grant on `DescribeFleetInstances`/`DescribeFleetHistory` does **not** constrain `DescribeFleets`, which is unscoped → account-wide fleet enumeration feeder that also returns instance-bearing fleet config.
4. Prove a **continuation-token (NextToken) cross-resource replay** or a **Filter.N** parsing/oracle weakness leaks data the caller's FleetId authorization should have gated.
5. Establish whether a successful `DescribeFleetInstances` call against a non-owned/foreign fleet produces a **log record** (detection blind-spot).

## 2. Components, Assets, and Design
**Mechanism (not marketing).** `DescribeFleetInstances` is a single AWS-region-scoped Query/SDK call against the EC2 control plane. It takes one **required `FleetId`** (singular — unlike `DescribeFleets`, which takes `FleetId.N` plural or none), optional `Filter.N` (documented filter: `instance-type`), `MaxResults`/`NextToken` for pagination, and `DryRun`. It returns `activeInstanceSet` = array of `ActiveInstance`, plus `fleetId`, `nextToken`, `requestId`.

- **Customer-facing interface:** SigV4-signed HTTPS to the regional `ec2.<region>.amazonaws.com` endpoint (Query API `Action=DescribeFleetInstances`, service version `2016-11-15`), or any SDK. No non-SDK/internal endpoint surfaced.
- **Resource & identifier shape:** the resource is an **EC2 Fleet**, ARN `arn:${Partition}:ec2:${Region}:${Account}:fleet/${FleetId}` (account embedded in ARN; `list_ec2.md` resource `fleet`). `FleetId` is high-entropy `fleet-<uuid-like>` → **not brute-enumerable**; a cross-account read requires a *leaked/known* FleetId, not guessing. This makes pure-enumeration IDOR a genuine null and shifts the real risk to **known-ID cross-account reads** and **the unscoped sibling feeder** that hands out FleetIds.
- **Response assets (what leaks on a successful call):** per instance — `instanceId`, `instanceType`, `spotInstanceRequestId`, `instanceHealth` (`healthy|unhealthy`). The `ActiveInstance` object's doc note says it "Describes a running instance in a **Spot Fleet**," i.e. the type is shared with Spot Fleet — a cross-feature reuse worth noting. List "is refreshed periodically and might be out of date."
- **Identity:** SigV4 IAM principal only. No session cookie, JWT, SCRAM, or credential chaining. TTL per the caller's STS/long-term creds.
- **Instant-fleet carve-out (design seam):** doc Note — "`DescribeFleetInstances` does **not** support fleets of type `instant`. Instead, use `DescribeFleets`, specifying the `instant` fleet ID." So the running instances of an *instant* fleet are only reachable through `DescribeFleets` (which returns `FleetData` incl. instance info and is **unscoped**). This is a documented split of one logical capability (enumerate a fleet's instances) across two APIs with **different resource-level-permission support** → Lens X.

```
 caller (SigV4 IAM principal)
     │  Action=DescribeFleetInstances & FleetId=fleet-xxxx  (singular, required)
     ▼
 EC2 control plane  ──(authz: ec2:DescribeFleetInstances on fleet* + ResourceTag? / existence?)──▶ Fleet record
     │  returns activeInstanceSet[ {instanceId, instanceType, spotInstanceRequestId, instanceHealth} ], nextToken
     ▼
 caller
      ▲ sibling feeder: DescribeFleets (UNSCOPED — ec2:Region only) enumerates FleetIds + FleetData for the whole account/region,
        AND is the ONLY path to an instant fleet's instances.
```

## 3. API / Interface Inventory
| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `DescribeFleetInstances` | Query/SDK GET-style | Existing | **No** (List) | External | Running instances of ONE EC2 Fleet | Yes (regional EC2 endpoint) | IAM principals w/ `ec2:DescribeFleetInstances`; resource `fleet*` + `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Region` | **FleetId required & singular.** Instant fleets NOT supported. Returns instance IDs + spot request IDs. |
| `DescribeFleets` | Query/SDK | Existing | No (List) | External | One/all EC2 Fleets (`FleetData`) | Yes | `ec2:DescribeFleets` — **NO resource type, `ec2:Region` only → NOT tag-scopable** | Sibling feeder (Lens X). Only path to instant-fleet instances. |
| `DescribeFleetHistory` | Query/SDK | Existing | No (List) | External | Event history of ONE fleet | Yes | `fleet*` + ResourceTag (same as this action) | Symmetric scoped sibling; leaks instance IDs in free-text `eventDescription`. See sibling plan. |

Undocumented-knob sweep: request params are exactly `DryRun`, `Filter.N`, `FleetId`, `MaxResults`, `NextToken`. Only one documented filter key (`instance-type`) — probe whether the service silently accepts **additional** EC2 filter keys (e.g. `instance-health`, `instance-id`, tag filters) that the reference does not list; an accepted-but-undocumented filter widens the readable/queryable projection (Step-3 "console-hidden knob" move, applied to the Query API's filter grammar).

## 4. Recommended Areas of Focus

### Area 1 — ABAC containment is advisory on EC2 Describe* (Lens S / I / U) — **#1, gates Areas 2–3**
Background: `list_ec2.md` L6816-6820 says `DescribeFleetInstances` supports resource type `fleet*` with condition keys `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, `ec2:Region` — i.e. an admin can seemingly write a policy that lets a principal introspect **only fleets tagged X**. But the EC2 User Guide `iam-policies-for-amazon-ec2` (sibling plan cite: L72-73 / L351) states blanket that **EC2 `Describe*` actions do NOT support resource-level permissions** and must be granted in a separate statement **without conditions**. Direct contradiction.
Security Concern: a tag-scoped `DescribeFleetInstances` policy an admin believes *contains* a principal to its own fleets may be **silently ignored**, granting account-wide introspection of every fleet's running instances.
High-level Test Scenarios:
- **Claim:** A policy allowing `ec2:DescribeFleetInstances` with `Condition: StringEquals aws:ResourceTag/team = A` still succeeds when called against a fleet tagged `team=B` (condition ignored). → **Mechanism:** Service-Auth-Ref says scopable; User-Guide says Describe* is unconditioned. → **Oracle:** under a scoped role, call against a `team=B` fleet; `200` + `activeInstanceSet` = condition ignored (bug); `UnauthorizedOperation` = enforced (refuted). → **Preconditions:** 1 IAM policy + 2 fleets differently tagged. → **Cost:** minutes. → **Severity:** Medium (intra-account containment bypass; High if the policy is the *sole* control over sensitive-tenant fleet visibility in a multi-team account).
Doc evidence: `list_ec2.md` L6816-6820 vs `iam-policies-for-amazon-ec2`. Severity-if-true: Medium. **Stop condition:** once enforced-vs-ignored is settled, record it — it determines whether Area 2's cross-account read is even reachable under a scoped role.

### Area 2 — Cross-account read by known FleetId: ownership vs existence (Lens A)
Background: resource is `fleet*` with an account-embedded ARN, but the API accepts a bare `FleetId` string. Authorization on a resource-scoped List action must bind the FleetId to the **caller's account**, not merely to the fleet's **existence**.
Security Concern: if authz validates existence/format but not cross-account ownership, a principal who learns a foreign `FleetId` (from a shared CloudFormation template, a leaked support case, a cross-account log, CloudTrail in an org sink, or a mis-shared tag export) reads another account's running-instance inventory.
High-level Test Scenarios:
- **Claim:** `DescribeFleetInstances(FleetId=<account-B's fleet>)` called by account-A creds returns `activeInstanceSet` rather than an access/does-not-exist error. → **Mechanism:** singular bare-ID input; ARN carries account but input does not. → **Oracle:** `200` with foreign instance IDs = cross-account IDOR (Critical, likely HARD STOP if the fleet is AWS-owned); `InvalidFleetId.NotFound`/`UnauthorizedOperation` = refuted. → **Preconditions:** two accounts you control + a known foreign FleetId. → **Cost:** low. → **Severity:** cross-account data access = Critical.
- **Error-oracle variant (Lens A additions):** compare responses for (a) well-formed foreign FleetId, (b) malformed FleetId, (c) nonexistent-but-well-formed FleetId. Distinct **500-InternalError vs 400-Malformed vs `NotFound` vs `AccessDenied`** codes/latencies form an **existence/enumeration oracle** across the tenant boundary even if the full read is blocked. Note the **embedded-checksum defense**: if FleetIds carry a checksum, a *fabricated* foreign ID can't pass format validation → pure-enumeration is a genuine null; only *leaked* IDs matter.
- **DryRun trap (do NOT misread):** `DryRun=true` returns `DryRunOperation` on permission success — this is **caller-IAM only, evaluated before resource resolution, NOT an ownership oracle.** A `DryRunOperation` on a foreign FleetId proves nothing about cross-account access. See [[ec2-multiresource-action-failopen-scoping]].
Doc evidence: API_DescribeFleetInstances request params; `list_ec2.md` fleet ARN. Severity-if-true: Critical (cross-account) / Low-Med (enumeration oracle only).

### Area 3 — Sibling-authorization asymmetry & instant-fleet delegation (Lens X) — **crown jewel**
Background: three APIs expose a fleet's instances/config: `DescribeFleetInstances` (`fleet*`+ResourceTag, this action), `DescribeFleetHistory` (`fleet*`+ResourceTag), and `DescribeFleets` (**no resource type, `ec2:Region` only — cannot be tag-scoped**). The doc Note additionally routes **instant-fleet instances exclusively through `DescribeFleets`**.
Security Concern: an admin who tag-scopes `DescribeFleetInstances` (per Area 1) to contain a principal has **not** contained `DescribeFleets`, which returns `FleetData` for every fleet in the region and is the only way to read an instant fleet's instances. The containment the admin believes they built leaks around the unscoped sibling.
High-level Test Scenarios:
- **Claim:** A principal granted *only* tag-scoped `DescribeFleetInstances` + `DescribeFleets` can enumerate **all** fleet IDs and instance-bearing `FleetData` account-wide via `DescribeFleets` despite the `DescribeFleetInstances` tag scope. → **Mechanism:** `list_ec2.md` L6822-6826 — `DescribeFleets` has no resource leg. → **Oracle:** `DescribeFleets` (no FleetId arg) returns fleets tagged outside the principal's allowed tag = scoping escape (expected-but-confirm); then feed a discovered foreign FleetId back into `DescribeFleetInstances` to test Area 1. → **Severity:** account-wide enumeration = High as an enabler; the pair is the realistic kill chain (enumerate via unscoped sibling → read via per-ID action).
- **Instant-fleet delegation claim:** for an *instant* fleet, `DescribeFleetInstances` is documented unsupported but `DescribeFleets` returns its instances — does `DescribeFleets`' instance-level data honor the **same** account/tag authorization the per-fleet action would, or a looser one? Validator-divergence between the two APIs naming the same instances. → **Oracle:** compare the authz outcome of reading one instant fleet's instances via each path.
Doc evidence: Note on both API pages; `list_ec2.md` L6816-6826. Severity-if-true: High (containment bypass / enumeration feeder).

### Area 4 — NextToken continuation re-authorization & Filter.N (Lens A / M, Lens F)
Background: `MaxResults`/`NextToken` paginate; `Filter.N` accepts `instance-type`.
Security Concern (NextToken, Lens A/M): if the opaque continuation token encodes fleet/offset state and the service does **not** re-authorize the FleetId (and the caller) on the continuation request, a token could be replayed or tampered to continue a listing against a resource the caller no longer/never should access. Classic "authz at page 1, trust the token thereafter."
High-level Test Scenarios:
- **Claim:** A `NextToken` minted for `FleetId=X` continues to return instances when replayed with a different/absent FleetId, or after the caller's access to X is revoked. → **Oracle:** mint token for X, revoke access or swap FleetId, replay; continued `activeInstanceSet` = continuation-trust bug. → **Severity:** Medium-High (session/continuation IDOR). → **Note:** doc-gap on token contents; mark "confirm surface first."
- **Filter.N (Lens F, low):** `Filter.N` claims only `instance-type`. **Claim:** the service accepts undocumented filter keys or malformed filter values without clean rejection. → **Oracle:** supply `instance-id`, `tag:*`, `instance-health`, oversized/odd values; a 500 or an honored undocumented filter = parsing/projection gap. → **Severity:** Low (query grammar is server-side enum matching, not a SQL/translation layer; injection-to-backend is implausible but the accepted-undocumented-filter case widens the readable projection).
Doc evidence: request params (`Filter.N`, `NextToken`, `MaxResults`), Pagination reference. Severity-if-true: Low-Medium.

### Area 5 — Disclosure payload sensitivity & audit completeness (Lens A-disclosure, Lens O/U)
Background: a successful call returns `instanceId`, `spotInstanceRequestId`, `instanceType`, `instanceHealth`; list "might be out of date."
Security Concern: (a) if Areas 1-3 yield any over-broad read, the leaked `instanceId`/`spotInstanceRequestId` are directly actionable identifiers for follow-on reconnaissance of the target tenant's compute inventory; `spotInstanceRequestId` ties the fleet to Spot-feature resources (cross-feature pivot). (b) Audit: is a **List** action against a foreign/scoped fleet recorded in CloudTrail at all, and does it capture the FleetId + result count — or is this a detection blind-spot for the cross-account read in Area 2?
High-level Test Scenarios:
- **Claim:** A `DescribeFleetInstances` call that returns another account's instances produces **no CloudTrail record in the victim's account** (describe calls are logged in the *caller's* trail, not the resource owner's). → **Oracle:** inspect both accounts' trails after an Area-2 read. → **Severity:** Informational/Low on its own, but an **enabler** that raises the effective severity of any confirmed Area-2/3 read (silent cross-account recon).
Doc evidence: API_ActiveInstance fields; CommonErrors. Severity-if-true: Low (enabler).

## 5. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account read by known FleetId | `DescribeFleetInstances` authz | Resource `fleet*` ARN carries account; authz must bind FleetId to caller account, not existence |
| Tag-scope silently ignored on Describe* | IAM evaluation for this action | `list_ec2.md` claims `fleet*`+ResourceTag scopability (contradicted by User Guide) |
| Containment escape via unscoped `DescribeFleets` | Sibling API | `DescribeFleets` has `ec2:Region` only — no resource leg |
| Instant-fleet instance read diverges in authz | `DescribeFleets` vs `DescribeFleetInstances` | Doc Note delegates instant fleets to `DescribeFleets` |
| NextToken continuation not re-authorized | Pagination | Opaque token; re-authz behavior undocumented |
| Undocumented/malformed Filter.N accepted | Filter grammar | Reference lists only `instance-type` |
| Silent cross-account recon (no victim log) | CloudTrail | Describe logged in caller's trail only |

## 6. Out-of-Scope Risk Categories
- Pure brute-force FleetId enumeration — IDs are high-entropy `fleet-<uuid>`; a genuine null absent a leaked ID.
- RCE / memory-safety / injection-to-backend — no attacker-controlled parser, no translation layer, no blob upload on this read-only action.
- IMDS on managed hosts; shared fleet-host compute; the running instances themselves (their security is a separate surface — this action only *names* them).
- Mutation of fleets/instances — not reachable from this action (List only); see `CreateFleet`/`DeleteFleets`/`ModifyFleet` surfaces.
- Any customer self-inflicted least-privilege footgun in a *customer-authored* policy (the Area-1 contradiction is in scope **only** because the weak/contradictory guidance is **AWS-authored** documentation an admin follows verbatim).
- A user reading their **own** fleet's instances (intended functionality).

## 7. Null hypotheses / doc gaps
- **G (SSRF):** N/A — no field is dereferenced/fetched server-side. Checked: full request param list (DryRun/Filter.N/FleetId/MaxResults/NextToken) — none is a URL/host/location.
- **Q (upload):** N/A — no blob/file/image input or server-rendered output. Checked: request params + `ActiveInstance` response (scalar IDs/enums only).
- **B / C (PassRole / vending):** N/A — no role ARN input, no STS/session-policy/credential-vending. Checked: request params.
- **H / W (KMS / attestation):** N/A — no key input, no encryption context, no `Recipient`/PCR. Checked: request + response.
- **K (prompt injection):** N/A — no LLM/agent/GenAI in path.
- **FF / M (JWT / session token):** N/A — SigV4 IAM only; no JWT/OIDC/Cognito; `NextToken` is the only opaque token (covered as Lens A/M continuation, Area 4).
- **Y (transport/sig):** N/A at the doc level — standard regional SigV4 HTTPS endpoint; no `http://`, no documented sig-version weakness. (Generic SigV4-coverage probing applies to all EC2 Query APIs, not specific to this one.)
- **V / D (network segmentation / control-plane escape):** N/A — control-plane API, no customer data-plane network vantage, no ENI model.
- **BB / CC / DD (parser-differential / upstream-context / cache):** N/A — single parser, single hop, no authorizer-in-front, no documented authz/result caching. (If EC2 fronts this with request-router caching internally, that is undocumented — doc-gap, not a lead.)
- **EE (predictable-name land-grab):** N/A — FleetId is service-assigned high-entropy, not a caller-chosen global name.
- **AA / N (share-revoke / namespace migration):** N/A — no share/unshare op, no dual-ARN migration for this action.
- **T (cross-service secret reachability):** N/A — action generates/persists no secret.
- **P (proofing/registration):** N/A — no onboarding/verification/OTP workflow.
- **Doc-gaps to confirm-surface-first:** NextToken contents & re-authz behavior (Area 4); whether undocumented Filter.N keys are accepted (Area 4); whether EC2 records this List against a *foreign* fleet in the resource owner's CloudTrail (Area 5). The Area-1 ABAC contradiction is a **documentation** contradiction that only a live IAM test settles.
```
