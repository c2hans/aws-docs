# EC2 DescribeFlowLogs — Attack Research Plan

Source of leads: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeFlowLogs.html (+ .md twin), API_FlowLog.html, API_DestinationOptionsResponse / API_TagFieldSpecificationResponse, and the EC2 IAM action reference (`list_ec2.md`). Twin of the already-analyzed `CreateFlowLogs-attack-research-plan.md` and `DeleteFlowLogs-attack-research-plan.md` — **read all three together; this is the RECON leg of that family.** Status: documentation-derived hypotheses only; nothing tested against a live account.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment a `DescribeFlowLogs` call returns a flow log (`fl-…`), destination ARN, or delivery-role ARN belonging to an account that is **not yours**, stop, preserve evidence, flag for AWS-Security disclosure. The `vpc-flow-log` ARN is account-scoped and **not RAM-shareable** — any cross-account read is a service-plane breach, not a feature.

## 1. Pentest Objectives
1. Determine whether `DescribeFlowLogs` can be **meaningfully scoped** by IAM to a subset of flow logs (resource, destination, team) — or whether any grant is account-wide. (Primary; expected answer from docs: account-wide.)
2. Determine what **sensitive topology** a single unconstrained `DescribeFlowLogs` call discloses, and how that output seeds the exfil/blinding chain in the Create/Delete twins.
3. Determine whether the **Describe/Delete scoping inversion** gives a least-privilege reviewer false assurance (recon unscopable, destruction scopable).
4. Probe parity: does `DescribeFlowLogs` enforce the same account-ownership as sibling/legacy/cross-service reads of the same metadata (Lens X), and does a foreign `FlowLogId.N` ever resolve (service-plane oracle).
5. Confirm null hypotheses (no SSRF/injection/upload/PassRole-at-read/KMS surface on a pure read action).

## 2. Components, Assets, and Design

**Interface.** EC2 Query/SDK API `DescribeFlowLogs` (action `ec2:DescribeFlowLogs`). Read-only, **non-mutating**, external-facing, SigV4 IAM. Classified **List** in the IAM reference.

**Request parameters** (all optional):
- `FlowLogId.N` — array of flow-log IDs, **max 1000**.
- `Filter.N` — `deliver-log-status`, `log-destination-type`, `flow-log-id`, `log-group-name`, `resource-id`, `traffic-type`, `tag:<key>`, `tag-key`.
- `MaxResults` / `NextToken` — pagination.
- `DryRun` — boolean; caller-IAM check only (**not an ownership oracle** — evaluated before resource resolution).

**Response — `flowLogSet[]` of `FlowLog`**, each item disclosing (verbatim fields):
- `flowLogId` (`fl-…`), `resourceId` (the monitored `vpc-`/`subnet-`/`eni-` ID), `flowLogStatus` (`ACTIVE`), `creationTime`, `trafficType` (`ACCEPT|REJECT|ALL`), `maxAggregationInterval`.
- `logDestination` (full **S3/Firehose ARN**), `logDestinationType` (`cloud-watch-logs|s3|kinesis-data-firehose`), `logGroupName` (CWL group name).
- `deliverLogsPermissionArn` (**the CWL delivery IAM role ARN**), `deliverCrossAccountRole` (**the cross-account publish role ARN**), `deliverLogsStatus` (`SUCCESS|FAILED`), `deliverLogsErrorMessage` (`Rate limited` / `Access error` / `Unknown error`).
- `logFormat` (the exact record template, incl. which fields are captured).
- `destinationOptions` (`DestinationOptionsResponse`: FileFormat, HiveCompatiblePartitions, PerHourPartition for S3).
- `TagFieldSpecificationSet[]` (`TagFieldSpecificationResponse`, 1–3 items) — **the instance/interface tag KEYS being exported into records** (v11 Amazon-EC2-Tags enrichment feature).
- `TagSet[]` — the flow log's own tags.

**Asset = the account's complete flow-log topology.** The response is a pre-attack map: every destination, every delivery-role ARN, every monitored resource, and which tags leak into records — all from one call, no per-resource authz.

**Design (recon position in the family):**
```
DescribeFlowLogs (THIS)  --->  enumerate: destinations + delivery roles + monitored resources + tag-field specs + delivery errors
        |                                           |
        v                                           v
  CreateFlowLogs (exfil new capture to attacker     DeleteFlowLogs (blind the SIEM-feeding
  dest; reuse discovered delivery role)             flow log discovered here)
```

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `DescribeFlowLogs` | POST (Query/SDK) | Existing | **No** | External | Enumerate flow logs + full config/status | Yes (SigV4) | Any principal w/ `ec2:DescribeFlowLogs` in region | **List class; NO resource type; `ec2:Region` only** (list_ec2.md ~L6828). Discloses `deliverLogsPermissionArn`, `deliverCrossAccountRole`, `logDestination`. |
| `CreateFlowLogs` | POST | Existing | Yes | External | Create capture → destination | Yes | `ec2:CreateFlowLogs` (`aws:RequestTag`/`TagKeys` only) | Twin plan. Destination un-scopable. |
| `DeleteFlowLogs` | POST | Existing | Yes | External | Teardown (forward-blind) | Yes | `ec2:DeleteFlowLogs` (tag-scopable) | Twin plan. **Scoping inversion vs Describe.** |

**Undocumented-knob sweep:** no auth/isolation-weakening enum here (read action). The only "hidden" surface is the set of **Filter.N** keys — all documented. `DryRun` is the one caller-controlled boolean; see Lens A variant on the DryRun trap.

## 4. Boundary-lens catalog results

### FIRES — Lens S / I — Condition-key scoping semantics (PRIMARY, Medium→High enabler)
- **Claim:** `ec2:DescribeFlowLogs` **cannot be scoped** to a subset of flow logs; any grant is account-wide enumeration of every flow log's full config.
- **Mechanism:** IAM reference lists `ec2:DescribeFlowLogs` as **List** class with **no resource type** and only `ec2:Region` as a condition key (`list_ec2.md` ~L6828). No `aws:ResourceTag`, no `ec2:LogDestination`, no monitored-resource key (`ec2:Vpc`/`ec2:Subnet`/`ec2:NetworkInterfaceID`). The `Filter.N`/`FlowLogId.N` request params are caller-controlled **output filters**, not authz boundaries.
- **Confirm/Refute oracle:** under a role whose policy attempts `Condition: {StringEquals: {aws:ResourceTag/team: X}}` on `ec2:DescribeFlowLogs`, the call still returns flow logs **without** that tag → scoping is inert. Confirm first with `iam:SimulateCustomPolicy` (no resources touched); the sim will show the condition key not applicable to the action.
- **Preconditions:** a scoped role. Cost: minutes. **Severity: Medium** standalone; **High as an enabler** — it is the unscopable recon that feeds Create-exfil and Delete-blinding.
- **Stop condition:** confirmed inert, or a condition key unexpectedly bites (refutes — document the key).

### FIRES — Lens X — Describe/Delete scoping INVERSION & cross-service parity (High-value reviewer trap)
- **Claim:** A least-privilege reviewer who scopes the *destructive* `ec2:DeleteFlowLogs` by tag gets false assurance, because the *recon* `ec2:DescribeFlowLogs` sibling is unconstrainable — the attacker maps every flow log (incl. the SIEM one) before deleting.
- **Mechanism:** asymmetry in `list_ec2.md`: `DeleteFlowLogs` = Write, resource `vpc-flow-log*`, keys `aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Region` (tag-scopable, ~L5890); `DescribeFlowLogs` = List, no resource type, `ec2:Region` only (~L6828). Recon unscopable, destruction scopable — **the inversion of the usual expectation.**
- **Cross-service parity sub-claim:** the *same* metadata (destinations, delivery roles) is reachable via the destination services — `logs:DescribeLogGroups`, `s3:ListBucket`, `firehose:ListDeliveryStreams`, and CloudTrail `CreateFlowLogs` events. Does a principal **denied** `ec2:DescribeFlowLogs` still reconstruct the topology from those cousins? (Expected: partially yes — the delivery-role ARN and `logFormat` are EC2-only, but destination existence leaks via the storage service.)
- **Oracle:** (inversion) a role with tag-scoped Delete + broad Describe enumerates a flow log it cannot delete, proving the recon/destroy mismatch. (parity) reconstruct ≥1 destination ARN via a destination-service read while `ec2:DescribeFlowLogs` is denied.
- **Severity:** inversion = **Medium–High** (least-priv footgun that is AWS-shaped, not customer-authored — the missing resource type is AWS's IAM-model defect). Parity leak = Low–Medium.

### FIRES — Lens A — Info-disclosure / enumeration oracle / cross-account (recon payload + hard-stop probe)
- **Claim 1 (intra-account disclosure):** one `DescribeFlowLogs` call hands an attacker the full exfil/blinding toolkit: every `logDestination`, both delivery-role ARNs (`deliverLogsPermissionArn`, `deliverCrossAccountRole`), `logFormat` (reveals whether sensitive fields like `pkt-srcaddr`/`account-id`/tag values are captured), `TagFieldSpecificationSet` (which tag KEYS leak into records), and `deliverLogsErrorMessage` (`Access error` flags a misconfigured/assumable delivery role).
  - **Oracle:** the returned `deliverLogsPermissionArn` is then used to seed Lens B/C probing in the Create twin (can I reuse/assume this role; is its trust policy's SourceArn pinned). Severity of the *disclosure itself*: **Low–Informational**; value is as chain fuel.
- **Claim 2 (cross-account — HARD STOP probe):** supplying a **foreign/fabricated `fl-` ID** in `FlowLogId.N` returns that flow log's config.
  - **Mechanism:** `vpc-flow-log` ARN is account-scoped and not RAM-shareable (Delete-twin: cross-account REFUTED by design). `FlowLogId.N` takes up to 1000 IDs — a batch blind-fabrication oracle **iff** `fl-` IDs lack an embedded checksum (open doc-gap).
  - **Oracle:** any foreign `fl-` returning a `FlowLog` item (not empty, not `InvalidFlowLogId.NotFound`) = **service-plane breach → HARD STOP.** Expected result: empty/NotFound (genuine null — correct).
- **Claim 3 (differential-error / DryRun trap):** test whether `FlowLogId.N` with a nonexistent vs an existent-but-foreign ID yields distinguishable errors (existence oracle). Note: `DryRun` is **caller-IAM only, evaluated before resource resolution — NOT an ownership oracle** (false-positive trap; do not treat a `DryRunOperation` success as "the flow log exists/is mine").
- **Severity:** Claim 1 Informational-as-enabler; Claim 2 Critical-if-true + hard stop; Claim 3 Low.

### FIRES — Lens O — Audit-log / recon stealth
- **Claim:** `DescribeFlowLogs` is a List/read call that **precedes** the destructive family actions and is itself low-signal; an attacker maps the whole flow-log estate with one CloudTrail `DescribeFlowLogs` (read-event, often not alerted on) before any mutation.
- **Mechanism:** read actions default to CloudTrail management-event *read* category, which many detections exclude. The Delete twin notes the mutation is logged — but the recon that targets it may not be alerted.
- **Oracle:** confirm `DescribeFlowLogs` emits only a read-category CloudTrail event; measure whether a SIEM rule exists for it (environment-dependent). Severity: **Informational** (enabler).

### FIRES — Lens U — Shared-subnet / shared-VPC ownership disclosure (doc-gap)
- **Claim:** In a RAM-shared subnet, a **participant** account can `DescribeFlowLogs` and see the flow log the **VPC owner** created on the shared VPC/subnet (or vice-versa), disclosing the owner's destination + delivery-role ARNs across the share boundary.
- **Mechanism:** flow logs can be created on a shared subnet (Create twin: shared-subnet capture is by-design). Who *owns* the resulting flow log — the VPC owner or the participant — and whether the non-owner can `Describe` it is **not stated in the docs** (open doc-gap in both twins). `resourceId` of a shared subnet is visible to both parties.
- **Oracle:** from a participant account, `DescribeFlowLogs` filtered by the shared `resource-id`; if the owner's `fl-` + its `deliverLogsPermissionArn` appear, that is a cross-account disclosure across the RAM boundary → evaluate as High / possible hard stop depending on whether it crosses the service plane or merely two customer accounts sharing by consent.
- **Severity:** **doc-gap — confirm surface first.** If a participant reads the owner's delivery-role ARN: High.

### NULL hypotheses (pages checked)
- **Lens G (SSRF):** NULL. Checked request params + FlowLog response — `DescribeFlowLogs` **dereferences nothing**; `logDestination`/`deliverLogsPermissionArn` are strings *returned*, never fetched. No server-side fetch on a read path.
- **Lens B/C (PassRole/vending) at read time:** NULL. No role is passed or assumed by `DescribeFlowLogs`; it only *reveals* the ARNs that Create/Delete-time PassRole probing (twin plans) will target. (The disclosure is the chain link, not a vuln here.)
- **Lens F / Q / K (injection / upload / prompt):** NULL. No parser, no blob, no LLM — read of structured metadata. `Filter.N`/`tag:<key>` values are server-side output filters, not a backend query seam exposed to the caller.
- **Lens H / T (KMS / secret reachability):** NULL for Describe. It does not return KMS key IDs or secret material; destination-bucket SSE/KMS config is a destination-service concern (CWL/S3 page), not exposed here.
- **Lens L (DoS):** NULL/out-of-scope. `MaxResults`/`FlowLogId.N`≤1000 are bounded; no attacker-amplifiable parse.

## 5. Recommended Areas of Focus (priority order)
1. **Lens S/I — prove Describe is unscopable** (SimulateCustomPolicy, then scoped-role live read). Foundation for the whole family's least-priv story.
2. **Lens X — Describe/Delete inversion** demonstration under a tag-scoped-delete role. Highest reviewer-impact, AWS-owned IAM-model defect.
3. **Lens A Claim-2 — foreign `fl-` fabrication batch** (up to 1000 IDs) as a service-plane hard-stop probe + resolve the `fl-`-checksum doc-gap.
4. **Lens U — shared-subnet flow-log ownership disclosure** (resolve the doc-gap; this is the only path to a genuine cross-account read via Describe).
5. **Lens A Claim-1 — chain fuel**: feed discovered `deliverLogsPermissionArn`/`deliverCrossAccountRole` into the Create-twin confused-deputy/assume-role probes.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Account-wide recon under a "scoped" role | `ec2:DescribeFlowLogs` IAM | Claimed least-privilege scoping — attack the **absence of a resource type** |
| Recon/destroy scoping inversion | Describe vs Delete IAM rows | Tag-scoped Delete gives false assurance — attack via unscopable Describe |
| Cross-account flow-log read | `FlowLogId.N` foreign IDs | ARN account-scoping + (unverified) `fl-` checksum |
| Shared-subnet owner disclosure | participant vs VPC owner | RAM participant visibility — **unspecified in docs** |
| Delivery-role ARN harvest → confused deputy | `deliverLogsPermissionArn` field | SourceArn trust-policy pinning (Create twin) — attack the disclosure that enables it |
| Low-signal recon before mutation | CloudTrail read category | Read-event logging — attack detection-coverage gap |

## 7. Out-of-Scope Risk Categories
- The **content** of flow-log records (that is the destination service's data plane — S3/CWL/Firehose), reached via the destination, not via Describe.
- Shared S3/CWL/Firehose storage infra and their KMS defaults (shared-responsibility / destination-service owned).
- Single-tenant self-inflicted least-privilege footguns **in a customer-authored policy** (the inversion is in-scope only because the missing resource type is AWS's IAM-model definition).
- IMDS/Amazon-DNS/TimeSync/DHCP/ARP flow-log blind spots (a capture-coverage gap of the feature, not a Describe bug).
- DryRun as an ownership/existence oracle (known false-positive trap — explicitly out).

## 8. Null hypotheses / doc gaps
- **Null:** SSRF, PassRole-at-read, injection, upload, prompt, KMS/secret, DoS — all NULL with pages named in §4.
- **Doc-gap 1:** Do `fl-` flow-log IDs embed a checksum? Determines whether the `FlowLogId.N`≤1000 batch is a viable blind cross-account fabrication oracle or a genuine null.
- **Doc-gap 2:** In a RAM-shared subnet, who **owns** the flow log and can a non-owner `DescribeFlowLogs` read it? Shared by both the Create and Delete twins; the single highest-value unknown for Describe.
- **Doc-gap 3:** Does `DescribeFlowLogs` list flow logs on resources **shared into** the account (e.g. transit gateways, shared subnets) — i.e. is the returned set keyed on resource-visibility or on flow-log-owner-account?

---
*Twin of `CreateFlowLogs-attack-research-plan.md` (exfil leg) and `DeleteFlowLogs-attack-research-plan.md` (blinding leg). This is the recon leg; chain findings across all three.*
