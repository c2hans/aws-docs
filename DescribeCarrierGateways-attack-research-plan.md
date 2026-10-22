# DescribeCarrierGateways — Attack Research Plan
Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeCarrierGateways.html (+ `.md` twin); CarrierGateway object API_CarrierGateway.html; IAM reference `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` L1652-1657 (summary) & L6702-6706 (action detail). Family twins: `CreateCarrierGateway-attack-research-plan.md`, `DeleteCarrierGateway-attack-research-plan.md`. Status: documentation-derived hypotheses only; nothing tested against a live account.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- This is a **read-only List verb** — the recon/enumeration end of the Carrier Gateway kill-chain. Its value as a target is almost entirely as an **enabler** (it feeds unforgeable `cgw-` IDs and account-wide inventory into the destructive twins) and as a **least-privilege expressibility gap** (you cannot scope it). Rate it accordingly: on its own it is Low/Info; its weight is in the chain.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected here — single-account control-plane read.)

## 1. Pentest Objectives
1. Determine whether a principal holding **only** `ec2:DescribeCarrierGateways` can enumerate **every** carrier gateway in the account (all `ownerId`/`vpcId`/`state`/tags) with no resource-level or ABAC constraint possible — i.e. confirm the read is account-wide and unscopable.
2. Determine whether this read can cross a tenant boundary (read another account's carrier gateways). Expected NULL — confirm and close.
3. Determine whether the `CarrierGatewayId.N` input or the differential error/validator behavior provides an **enumeration oracle** for `cgw-` IDs (that then feed Delete/Create → route kill-chain).
4. Determine the **least-privilege ceiling**: can a policy author restrict this read to a specific VPC, tag, or set of carrier gateways — or only to a Region?

## 2. Components, Assets, and Design
- **Interface:** EC2 Query/JSON API `DescribeCarrierGateways`, action version `ec2-2016-11-15`, SigV4 IAM, reachable at the public regional `ec2.<region>.amazonaws.com` endpoint. SDK-surfaced (not hidden/non-SDK).
- **Mutating?** No — read-only. **Access level:** `List`.
- **Resource:** a carrier gateway (`cgw-...` ID) — a VPC-attached NAT bridge from a Wavelength-Zone subnet to the 4G/5G telco carrier (CSP) network + public internet. Single-account, single-VPC, **NOT RAM-shareable** (the object carries an `ownerId`; the API describes "your carrier gateways"). `cgw-` IDs are server-assigned and checksummed → **not client-fabricable**.
- **Request parameters (verbatim):** `CarrierGatewayId.N` (array, optional), `DryRun` (bool), `Filter.N` (optional; names: `carrier-gateway-id`, `state`, `owner-id`, `tag:<key>`, `tag-key`, `vpc-id`), `MaxResults` (5–1000), `NextToken`.
- **Response (verbatim):** `carrierGatewaySet` (array of CarrierGateway), `nextToken`, `requestId`.
- **CarrierGateway object fields:** `carrierGatewayId` (String), `ownerId` (String — AWS account ID of owner), `state` (`pending|available|deleting|deleted`), `TagSet.N` (Tags), `vpcId` (String). **No carrier-IP / network-border-group / CSP-endpoint field is exposed.**
- **Identity/roles:** caller IAM principal only. No role assumption, no credential vending, no tokens, no server-side fetch, no blob/upload, no LLM. No service-account / data-plane split touched by a read.

```
caller (IAM principal, SigV4)
      │  ec2:DescribeCarrierGateways   (condition key: ec2:Region ONLY; Resource: * ; no resource types)
      ▼
EC2 control plane ──► returns carrierGatewaySet for ALL cgw in (account, region)
                      each item: cgw-id | ownerId | vpcId | state | tags
      │ (unforgeable cgw- IDs + account-wide inventory)
      ▼  feed into ──►  DeleteCarrierGateway (single carrier-gateway leg, no VPC scoping, no route perm)
                        └─► dangling 0.0.0.0/0→cgw route = blackhole = zone-wide egress DoS
```

## 3. API / Interface Inventory
| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| DescribeCarrierGateways | POST (Query) | Existing | **No (read)** | External | Enumerate the account's carrier gateways + attributes | Yes (regional EC2 endpoint) | Any principal with `ec2:DescribeCarrierGateways` — **no resource-level authz; only `ec2:Region`** | Filters: carrier-gateway-id/state/owner-id/tag/tag-key/vpc-id. Pagination MaxResults 5–1000 + NextToken. `DryRun` = caller-IAM check only. |

Undocumented/hidden-knob sweep: no auth-weakening enum or hidden parameter — `DryRun`, filters, and pagination are the full input surface. `owner-id` as a *filter* is a convenience over the caller's own set, not a cross-account selector (see Area 2).

## 4. Boundary-lens catalog — findings

### Area 1 — No resource-level authorization on the read (CROWN / primary lead) — Lens S + Lens U + Lens A
**Background:** `DescribeCarrierGateways` in the IAM reference (L6702-6706) lists **no resource types** (`Resource:"*"` only) and **`ec2:Region` as its sole condition key**; Access level `List`. The Create twin, by contrast, authorizes two legs (`carrier-gateway*` + `vpc*` incl. `ec2:VpcID`) and Delete authorizes a `carrier-gateway*` leg with `ec2:ResourceTag`.
**Security Concern:** A principal granted `ec2:DescribeCarrierGateways` can enumerate **every** carrier gateway in the account and read each one's `ownerId`, `vpcId`, `state`, and full `TagSet` — and **no policy can narrow this**. There is no `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Vpc`/`ec2:VpcID`/`carrier-gateway` resource key available on the action, so ABAC and per-VPC/per-tag confinement are **inexpressible** (Lens S: "key does not exist for this action" fail-open). A "read-only Wavelength operator for VPC X" cannot be built; the grant is all-or-region.
**High-level Test Scenarios:**
- **Claim:** A caller with only `ec2:DescribeCarrierGateways` (no tag/VPC condition) returns CGWs it has no business reading. → **Oracle:** under a scoped role holding exactly that action with an attempted `Condition {ec2:ResourceTag/...}` or `{ec2:Vpc}`, `iam:SimulateCustomPolicy` shows the condition is **ignored** (not evaluated) and the call is allowed account-wide; a live call returns the full `carrierGatewaySet`. → Severity-if-true: **Low (intra-account least-priv expressibility gap / recon primitive)**; this is an EC2-family-wide pattern (Describe-* rarely resource-scoped), so file as a documented hardening observation, not a novel bug.
- **Claim:** The inventory this read yields (unforgeable `cgw-` IDs + `vpcId`) is the recon that arms the Delete-blackhole DoS. → See Area 5 kill-chain.
**Doc evidence:** list_ec2.md L6704 "Resource types (*required):" empty; L6705 "Condition keys: ec2:Region". Severity-if-true: Low-Info standalone; enabler for Medium/High chain.

### Area 2 — Cross-tenant / cross-account read — Lens A (expected NULL, confirm & close)
**Background:** API title: "Describes one or more of **your** carrier gateways." Object carries `ownerId`; carrier gateways are single-account, single-VPC, and **not RAM-shareable**. `owner-id` is offered as a *filter* over the returned set.
**Security Concern:** Could the `owner-id` filter or a crafted foreign `CarrierGatewayId.N` cause the service to return a **different** account's carrier gateway (existence-vs-ownership confusion)?
**High-level Test Scenarios:**
- **Claim:** Supplying `Filter owner-id=<victim account>` or `CarrierGatewayId.N=<victim cgw->` returns the victim's carrier gateway. → **Oracle:** response includes a `carrierGatewaySet` item whose `ownerId` ≠ caller account. → **Expected refute:** the service scopes the query to the caller's account first; `owner-id` filters only within the caller's own set; a foreign/valid-but-not-owned `cgw-` returns empty or `InvalidCarrierGatewayID.NotFound`. → **Checksum defense:** `cgw-` IDs are checksummed+server-assigned, so a *fabricated* foreign ID cannot pass validation — a genuine null, not an untested gap. Severity-if-true: **Critical** (cross-account disclosure) — but **predicted NULL**. Confirm once, then close.
**Doc evidence:** API intro "your carrier gateways"; API_CarrierGateway `ownerId`; CreateCarrierGateway memory (not RAM-shareable). Severity-if-true: Critical (but NULL-expected).

### Area 3 — ID / validator enumeration oracle — Lens A (oracles) + Lens X
**Background:** `CarrierGatewayId.N` accepts an arbitrary array of IDs. EC2 Describe-* siblings vary in how they treat an unknown/malformed ID (500 InternalError vs 400 Malformed vs 200-empty vs `*.NotFound`).
**Security Concern:** Does passing a malformed vs well-formed-but-nonexistent vs foreign-but-valid `cgw-` ID produce **distinguishable** responses that confirm the existence of a carrier gateway the caller can't otherwise see — an enumeration oracle feeding the Delete/Create→Route chain?
**High-level Test Scenarios:**
- **Claim:** `cgw-<foreign valid>` returns a different error/latency than `cgw-<nonexistent well-formed>` than `cgw-<malformed>`. → **Oracle:** diff the three response codes/bodies/timings (`InvalidCarrierGatewayID.Malformed` vs `.NotFound` vs empty set vs 200). A consistent **existence** signal across an account boundary = oracle. → **Refute:** checksum rejects fabricated IDs at parse → only malformed-vs-notfound distinction remains, which does not cross tenants. Severity-if-true: **Low-Medium** (enumeration only; the valuable IDs are same-account where you can already List).
**Doc evidence:** CarrierGatewayId.N param; family checksum property (memory). Severity-if-true: Low-Medium.

### Area 4 — Pagination / NextToken scoping — Lens A/M (NULL-expected)
**Background:** `MaxResults` 5–1000 + opaque `NextToken`.
**Security Concern:** Is `NextToken` a signed/account-bound continuation, or does a token minted in one context resolve data in another (token replay / cross-principal continuation)?
**High-level Test Scenarios:**
- **Claim:** A `NextToken` from account/region/principal A, replayed by B, continues A's result set. → **Oracle:** B's paginated response returns A's `cgw-` items. → **Expected refute:** EC2 pagination tokens are opaque and re-scoped to the caller's identity+region per request; the token encodes position, not authorization. Severity-if-true: High (but NULL-expected — standard EC2 pagination). Confirm cheaply alongside Area 2.
**Doc evidence:** MaxResults/NextToken params. Severity-if-true: High (NULL-expected).

### Area 5 — Chained lead: recon → destructive twin (kill-chain framing) — Lens A→L/AA
**Background:** This read supplies the two inputs the destructive twins need and cannot otherwise safely obtain: the set of valid, unforgeable `cgw-` IDs and the `vpcId` each is attached to.
**Security Concern:** `DeleteCarrierGateway` authorizes a **single `carrier-gateway*` leg with no VPC key** (cannot be confined to a VPC) and needs **no route permission**; deleting a CGW that a `0.0.0.0/0→cgw` route still targets leaves a **blackhole** = zone-wide egress outage (doc "Important" note on Delete). A principal with Describe + Delete (but not Create/route perms) can therefore recon-then-blackhole every Wavelength CGW in the account.
**High-level Test Scenarios:**
- **Claim:** Describe enumerates all `cgw-` IDs; Delete (no VPC scoping) blackholes each. → **Oracle:** (safe, in a canary account only) List returns IDs; a canary CGW with a canary dependent route, deleted, leaves a dangling route — repair immediately. → Severity-if-true: **Medium-High (cross-workload egress DoS within the account)**; Describe's role is the **enumeration entry**. Full exploit spec lives in `DeleteCarrierGateway-attack-research-plan.md` Area 1.
**Doc evidence:** Delete twin memory/plan; this page's `carrierGatewaySet` inventory. Severity-if-true: Medium-High (chain end).

## 5. Recommended Areas of Focus (priority order)
1. **Area 1** — confirm the read is account-wide and unscopable (Simulate first, then live List). Fast, high-certainty, documents the EC2-family least-priv ceiling.
2. **Area 5** — the kill-chain the read enables; the real impact lives at the Delete end.
3. **Area 3** — ID/validator oracle (cheap diff; likely bounded by checksum).
4. **Area 2 & 4** — cross-tenant read and token replay: confirm NULL cheaply and close, so the hunter doesn't revisit.

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Read all account CGWs with an unscopable grant | IAM action `ec2:DescribeCarrierGateways` | `ec2:Region`-only condition; no resource types (confirm the absence is real, not a doc omission) |
| Cross-account read via `owner-id` filter / foreign `cgw-` | EC2 control plane | "your carrier gateways" account scoping + `cgw-` checksum |
| Existence enumeration via differential error | `CarrierGatewayId.N` validator | uniform error/empty-set behavior |
| Cross-principal pagination continuation | `NextToken` | opaque, identity+region re-scoped per request |
| Recon→blackhole DoS | Describe + DeleteCarrierGateway | Delete `carrier-gateway*` leg; dependent-route "Important" note |

## 7. Out-of-Scope Risk Categories
- Cross-tenant data access via shared AWS infra (CGW is single-account, not RAM-shareable — no shared fleet reachable through a read).
- IMDS / host-level concerns (managed control-plane API; no customer-reachable host).
- Single-tenant self-DoS from the caller deleting its own resources (the in-scope DoS is **cross-workload within the account**, via the Delete twin).
- Customer-authored least-privilege footguns — note that Area 1's unscopability is a **documented AWS family pattern** (Describe-* actions are rarely resource-scoped), so it is a hardening observation, not an AWS-authored-artifact defect.

## 8. Null hypotheses / doc gaps
- **Lens B/C (PassRole / credential vending):** NULL — read verb; no `roleArn`/credential/token input. Pages checked: this API page, CarrierGateway object, list_ec2.md action entry.
- **Lens G (SSRF) / Lens Q (upload) / Lens F (injection) / Lens K (prompt) / Lens H/W (KMS/attestation) / Lens T (secret storage):** NULL — no URL/host field, no blob, no translation layer, no LLM, no key/secret field anywhere in the request or response. Pages checked: API_DescribeCarrierGateways, API_CarrierGateway, API_Filter.
- **Lens Y/BB/CC/DD/FF (transport/canonicalization/upstream-context/cache/JWT):** NULL — single SigV4-authenticated control-plane read, no multi-parser/edge/cache/token-validation hop in the documented path.
- **Lens I (tagging):** partial — `tag`/`tag-key` are read **filters** only (no mutation); tag-based ABAC is *inexpressible* here (folds into Area 1, Lens S), not a tag-write surface.
- **Doc gap:** the IAM reference shows an empty resource-types list for this action; confirm live (Simulate) that no undocumented resource-level condition is silently enforced — treat the empty list as "confirm surface" rather than proven, though the EC2 Describe-* family makes account-wide the strong default.
- **`DryRun` is caller-IAM only, NOT an ownership oracle** (evaluated before resource resolution) — do not use it to probe Area 2/3.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
