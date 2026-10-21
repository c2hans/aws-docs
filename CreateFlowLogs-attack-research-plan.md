# EC2 `CreateFlowLogs` — Attack Research Plan

**Source of leads:** `https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFlowLogs.html` (live, fetched 2026-10-20) + offline mirror `/work/aws-docs/docs/`:
`service-authorization/latest/reference/list_ec2.md` (IAM action/condition-key/resource-type detail), `AWSEC2/latest/APIReference/API_{CreateFlowLogs,DescribeFlowLogs,DeleteFlowLogs,FlowLog,DestinationOptionsRequest,TagFieldSpecificationRequest,GetFlowLogsIntegrationTemplate}.md`, and `vpc/latest/userguide/flow-logs-*.md` (basics, records, limitations, iam-role, slr, managed-policy, s3-permissions, s3-cmk-policy, s3-path, file-permissions, firehose, firehose-cross-account-delivery), plus `prescriptive-guidance/.../configure-vpc-flow-logs-for-centralization-across-aws-accounts.md` and `vpc/latest/tgw/flow-logs-api-cli.md`.

**Status:** documentation-derived hypotheses only. Nothing has been tested against a live AWS account. Every lead is a boundary that *might not hold* plus the exact observation that settles it.

---

## 0. How to use this document

- Each lead reads: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity-if-true → Stop condition.** Work in priority order (§5 is ordered). Look left and right for adjacent bugs.
- **HARD STOP:** the moment any evidence shows an identity / credential / ARN / account belonging to AWS's own service plane (e.g. the internal identity behind `vpc-flow-logs.amazonaws.com` or `delivery.logs.amazonaws.com`), stop, preserve evidence, and flag for AWS-Security disclosure. Do not probe further.
- **Scope discipline:** read-only / minimum-PoC. Confirm *existence* of a boundary gap, never exploit beyond it. Use synthetic canary buckets/log groups/VPCs you own across two in-scope accounts. Never read another real tenant's traffic data beyond the first byte of signal that proves the boundary broke.
- `DryRunOperation` is a **caller-IAM oracle only, NOT an ownership oracle** — it is evaluated before resource resolution (false-positive trap; see Lens A variant).

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)

1. **Exfiltrate network-topology intelligence to an attacker-chosen destination.** Prove that a principal holding a least-privilege `ec2:CreateFlowLogs` grant can direct captured traffic metadata (src/dst IP, ports, `account-id`, `instance-id`, instance/ENI **tag values**) to an S3 bucket / CloudWatch log group / Firehose stream the principal controls — including one in another account or outside the org — because **no `ec2:CreateFlowLogs` condition key constrains the destination.**
2. **Confused-deputy the log-delivery service.** Make `vpc-flow-logs.amazonaws.com` / `delivery.logs.amazonaws.com` assume a role or write to a resource that the calling principal could not have written to directly.
3. **Monitor a resource you do not own.** Enable flow logs on a VPC/subnet/ENI/TGW belonging to (or shared from) another tenant and receive its traffic records.
4. **Blind the defender (detection-evasion).** Delete or starve flow-log subscriptions, or exploit documented capture blind spots, so attacker traffic produces no durable record.
5. **Disclose configuration & role ARNs account-wide.** Use `DescribeFlowLogs` (region-only authz) to enumerate every flow log's destination and delivery-role ARN across the account.
6. **Side-effect resource creation / exhaustion.** Trigger auto-creation of the SLR + EventBridge Managed Rules via the Tags feature, or exhaust the 250-subscription-per-resource limit.

---

## 2. Components, Assets, and Design

**What `CreateFlowLogs` does.** Creates a *flow-log subscription* (`vpc-flow-log` resource, ARN `arn:aws:ec2:{region}:{account}:vpc-flow-log/{VpcFlowLogId}`) that captures IP-flow metadata for a monitored resource and **publishes it to a destination the caller names**. The subscription is immutable after creation (no Modify API — "you can't change its configuration … Instead … delete … and create a new one").

**Request inputs (attack-relevant):**
- `ResourceType` ∈ `VPC | Subnet | NetworkInterface | TransitGateway | TransitGatewayAttachment | RegionalNatGateway` + `ResourceId.N` (≤300; ≤25 for TGW) — **what to monitor**.
- `LogDestinationType` ∈ `cloud-watch-logs | s3 | kinesis-data-firehose` (default `cloud-watch-logs`), `LogDestination` (ARN of bucket / log-group / Firehose stream), `LogGroupName` (new-or-existing CWL group) — **where the data goes**.
- `DeliverLogsPermissionArn` — IAM role the service assumes to publish (required for CWL, and for cross-account Firehose). `DeliverCrossAccountRole` — role for cross-account publishing.
- `LogFormat` + `TagFieldSpecification.N` (resourceType ∈ `network-interface | instance | auto-scaling-group`, ≤3 specs, ≤2 tag keys each) — **the EC2-Tags enrichment feature** that writes resource **tag values** into each record.
- `TagSpecification.N`, `DestinationOptions` (`FileFormat plain-text|parquet`, `HiveCompatiblePartitions`, `PerHourPartition`), `MaxAggregationInterval` (60|600), `TrafficType` (`ACCEPT|REJECT|ALL`), `ClientToken`, `DryRun`.

**Assets / data sensitivity.** Flow-log records are a map of the victim's network: `srcaddr/dstaddr`, `pkt-srcaddr/pkt-dstaddr`, `srcport/dstport`, `protocol`, `account-id` (owner of source ENI), `instance-id`, `vpc-id`, `subnet-id`, `tcp-flags`, `flow-direction`, `pkt-src/dst-aws-service`, and (version 11) `instance-tag`, `interface-tag`, `asg-tag` **tag values** — which routinely carry owner, cost-center, environment, or secret-ish labels. Whoever controls the destination reads all of it.

**Identity / trust principals.**
- `ec2:CreateFlowLogs` — the caller's IAM identity (SigV4).
- `vpc-flow-logs.amazonaws.com` — service principal that assumes the customer **delivery role** (`DeliverLogsPermissionArn`) for CWL / cross-account Firehose.
- `delivery.logs.amazonaws.com` — the **log-delivery** service principal named in S3 bucket policies and Firehose cross-account roles.
- `AWSServiceRoleForVPCFlowLogs` (SLR) with managed policy `AWSVPCFlowLogsServiceRolePolicy` — auto-created **only** when a subscription uses Tag fields; manages EventBridge rules + reads tags (`tag:GetResources`, `autoscaling:DescribeTags`).

**Ownership split.** Three zones: **caller account** (creates subscription, chooses destination) · **monitored-resource owner** (may differ under RAM-shared subnets) · **destination owner** (may be a different account / org entirely). The service plane (`vpc-flow-logs` / `delivery.logs`) straddles all three and is the shared-responsibility line → **hard stop**.

```
                         ec2:CreateFlowLogs (caller IAM)
  Caller acct ───────────────────┬───────────────────────────────────────────────┐
     │  names: ResourceId(s)      │  names: LogDestination / DeliverLogsPermissionArn
     ▼                            ▼                                                 ▼
 [Monitored resource]       [VPC Flow Logs service plane]                   [Destination]
  VPC/Subnet/ENI/TGW/NATGW   vpc-flow-logs.amazonaws.com  ── assumes ──►  S3 bucket  (delivery.logs principal + bucket policy)
  (may be RAM-shared from    delivery.logs.amazonaws.com    delivery     CWL log group (same-acct only; LogGroupName free-choice)
   another account)          [SLR + EventBridge if Tags]    role         Firehose stream (same/cross-acct via role-chain)
                                                                          └─► records contain account-id, IPs, ports, instance-id, TAG VALUES
         ▲ no ec2:CreateFlowLogs condition key binds the destination ARN / type / log-group name
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller IAM (least-priv `ec2:CreateFlowLogs`) | Arbitrary destination (S3/CWL/Firehose), incl. cross-account | `LogDestination`/`LogGroupName`/`LogDestinationType` — **no condition key exists to constrain them** | A subscription is created whose destination the caller's IAM policy intended to forbid, and victim traffic metadata lands there → **topology exfiltration** |
| Caller IAM | Monitored resource it does not own (incl. RAM-shared subnet) | `ResourceId` + `ResourceType`; monitored-leg keys (`ec2:Vpc`, `ec2:SubnetID`, `ec2:NetworkInterfaceID`, `ec2:transitGatewayId`) *can* scope — but default `Resource:*` does not | Flow-log records for a resource owned by another team/account are delivered to the caller |
| Caller IAM | Delivery role (`DeliverLogsPermissionArn`) | `iam:PassRole` gated by `iam:PassedToService=vpc-flow-logs.amazonaws.com` + `iam:AssociatedResourceARN` | Service assumes a role the caller lacked `PassRole` for, or a role scoped to a different resource/account |
| `vpc-flow-logs` / `delivery.logs` service plane | Customer delivery role / destination resource | `sts:AssumeRole` (trust = service principal) / resource policy | Deputy writes to / assumes something the originating caller could not — SourceAccount/SourceArn only *recommended* |
| Caller / destination account | Another account's bucket or Firehose | S3 bucket policy (`delivery.logs` principal) / Firehose cross-account role-chain | Victim account's flow logs delivered into a bucket/stream without that account's genuine consent |
| Attacker traffic | Defender's monitoring | `DeleteFlowLogs` / 250-sub cap / documented capture blind spots (IMDS, Amazon DNS, …) | Security-relevant traffic produces no flow-log record |
| Any caller surface | AWS service-plane identity (`vpc-flow-logs`/`delivery.logs` internal creds/ARN/account) | — | **HARD STOP** — preserve evidence, disclose |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Ext-facing | Functionality | Callable from Internet | Authorized callers (IAM) | Notes |
|---|---|---|---|---|---|---|---|
| `CreateFlowLogs` | EC2 Query/SDK | **Yes** | Yes | Create flow-log subscription + destination | Yes | `ec2:CreateFlowLogs` (+`ec2:CreateTags`, `iam:PassRole→vpc-flow-logs.amazonaws.com`) | **Destination side has NO condition key.** Monitored-resource legs have keys; `vpc-flow-log*` leg has only `aws:RequestTag`/`aws:TagKeys`/`ec2:Region` |
| `DescribeFlowLogs` | EC2 Query/SDK | No | Yes | List all flow logs + their destinations/roles | Yes | `ec2:DescribeFlowLogs` — **no resource type, only `ec2:Region`** | Account-wide recon; returns `logDestination`, `deliverLogsPermissionArn`, `deliverCrossAccountRole`, `logGroupName`, `resourceId`, `logFormat` |
| `DeleteFlowLogs` | EC2 Query/SDK | **Yes** | Yes | Delete subscription(s) (disables monitoring) | Yes | `ec2:DeleteFlowLogs` on `vpc-flow-log*` (`aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Region`) | Scopable by tag — asymmetry vs Describe. Does **not** delete already-delivered data |
| `GetFlowLogsIntegrationTemplate` | EC2 Query/SDK | No (returns CFN text) | Yes | Generate Athena-integration CloudFormation | Yes | `ec2:GetFlowLogsIntegrationTemplate` | Inputs: `FlowLogId`, `ConfigDeliveryS3DestinationArn`, `IntegrateService`. No role input; generated template's IAM is undocumented. Not supported for TGW |

Undocumented/hidden-knob check: `RegionalNatGateway` `ResourceType` + `natgateway` IAM resource maps to "regional NAT gateway" (relatively new); `TagFieldSpecification`'s `auto-scaling-group` type silently requires an enabled CloudTrail trail + auto-creates EventBridge rules & SLR. `DestinationOptions.FileFormat=parquet` and `HiveCompatiblePartitions` change the on-disk path/parser.

---

## 5. Recommended Areas of Focus (ordered; one block per firing lens)

### AREA 1 — Destination is un-scopable in IAM (Lens S + B + U) — **CROWN**
**Background.** `CreateFlowLogs` names *both* a resource to monitor *and* a data destination. The IAM reference (`list_ec2.md`) shows the created `vpc-flow-log*` resource leg carries **only** `aws:RequestTag/${TagKey}`, `aws:TagKeys`, `ec2:Region`. There is **no condition key** for `LogDestination`, `LogDestinationType`, `LogGroupName`, `DeliverLogsPermissionArn`, or `DeliverCrossAccountRole`.
**Security Concern.** A policy author who grants `ec2:CreateFlowLogs` (even narrowly, e.g. only on a specific VPC via `ec2:VpcID`) **cannot** express "…but only deliver to *this* bucket / *this* log group." The destination is therefore caller-controlled and IAM-unconstrainable. Victim traffic metadata (IPs, ports, `account-id`, `instance-id`, tag values) can be aimed at any S3 bucket / CWL group / Firehose stream the caller can satisfy the *destination's* resource policy for — including an attacker-owned bucket that allows `delivery.logs.amazonaws.com`.
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* With an IAM policy that `Allow ec2:CreateFlowLogs` + `Deny` on every condition the author can write, a scoped principal can still create a subscription whose `LogDestination` is a bucket in **a second account** the principal controls, and records arrive there. → *Oracle:* records land in the attacker bucket; prove no `Deny` could have blocked it because no destination condition key exists. *Severity: High (cross-account topology exfil).*
- *Claim:* Same, delivering to a brand-new CloudWatch `LogGroupName` of the caller's choosing (CWL is same-account, so impact is intra-account data redirection / cost). → *Oracle:* new log group created and populated under a name the author's policy did not and could not whitelist.
- *Claim:* `simulate-principal-policy` for `ec2:CreateFlowLogs` returns `allowed` regardless of any destination-ARN context key, confirming the gap statically (safe first oracle). 
**Doc evidence.** `list_ec2.md` lines for `CreateFlowLogs` → `vpc-flow-log*` leg keys = {`aws:RequestTag`,`aws:TagKeys`,`ec2:Region`}; `API_CreateFlowLogs.html` destination params carry no IAM note. **Severity-if-true: High** (owner-to-fix: AWS — add a destination condition key; this is an IAM-expressiveness gap, in scope as a hardening/least-privilege-impossibility finding).
**Stop condition:** once one cross-account delivery is observed, stop — do not enumerate buckets or read beyond the first record.

### AREA 2 — Confused-deputy on the delivery/log-delivery service principals (Lens B)
**Background.** `vpc-flow-logs.amazonaws.com` assumes the customer `DeliverLogsPermissionArn`; `delivery.logs.amazonaws.com` writes to S3 under a bucket policy. The CWL delivery-role trust policy is a bare `sts:AssumeRole` for `vpc-flow-logs.amazonaws.com`; the docs only **recommend** adding `aws:SourceAccount`/`aws:SourceArn` ("We recommend…"). The auto-attached S3 bucket policy uses `aws:SourceArn = arn:aws:logs:{region}:{account}:*` — an **account/region-wide wildcard**, not flow-log-specific.
**Security Concern.** (a) If `ec2:CreateFlowLogs` does *not* actually enforce `iam:PassRole` on `DeliverLogsPermissionArn` at create time (the reference lists it only in a *sample* policy, not as a required dependency on the authoritative action row), a caller could pass any role whose trust allows `vpc-flow-logs.amazonaws.com`. (b) A delivery role whose trust omits `SourceAccount`/`SourceArn` can be driven by *another* account's flow log (classic confused deputy). (c) The S3 `SourceArn` wildcard means the bucket policy cannot pin a single flow log.
**High-level Test Scenarios:**
- *Claim:* `CreateFlowLogs` succeeds specifying a `DeliverLogsPermissionArn` the caller holds **no `iam:PassRole` for** → PassRole not enforced. *Oracle:* create succeeds + `deliverLogsStatus=SUCCESS`. *Refute:* `UnauthorizedOperation` citing PassRole.
- *Claim:* Account B's flow log can target a delivery role in Account B whose trust lacks `SourceAccount`, and that role writes to Account A's log group (deputy). *Oracle:* records from B's flow log appear under A's log group via the shared service principal.
- *Claim:* Because `SourceArn` is region-wide, a bucket intended for one flow log also accepts writes from a *second*, attacker-created flow log in the same account/region. *Oracle:* second flow log's records appear in the same bucket.
**Doc evidence.** `flow-logs-iam-role.md` ("We recommend … `aws:SourceAccount`/`aws:SourceArn` … to protect yourself against the confused deputy problem"); `flow-logs-s3-permissions.md` `SourceArn` wildcard; `firehose-cross-account-delivery.md` source role uses `iam:PassRole` + `iam:PassedToService` + `iam:AssociatedResourceARN` (so PassRole *is* wired for the Firehose case — test whether the CWL/base case matches). **Severity: High** (cross-account); Medium for the wildcard-pinning gap.

### AREA 3 — Monitoring a resource you don't own; RAM-shared-subnet cross-tenant capture (Lens A + V)
**Background.** Flow logs can be enabled on ENIs created by *other* AWS services (ELB/RDS/ElastiCache/Redshift/WorkSpaces/NAT/TGW) and the limitations page documents the shared-subnet case explicitly: *"you share a subnet (SubnetA) with another account (AccountB) … create a flow log subscription for SubnetA. If AccountB launches ECS tasks … your subscription receives traffic logs from those tasks."* AWS withholds **ECS metadata fields** and **tag-value fields** for the foreign account "due to security concerns" — **but the raw 5-tuple (IPs/ports/direction) is still captured.**
**Security Concern.** The subnet *owner* gains visibility into a *consumer* account's workload traffic patterns by design; the "security concerns" carve-out (suppressing ECS/tag fields) is a boundary worth probing — is the suppression actually enforced, or can a crafted `LogFormat`/`TagFieldSpecification` still surface AccountB's tag values? Also: can a principal with `Resource:*` `ec2:CreateFlowLogs` monitor *any* ENI/VPC/subnet in its own account (intra-account cross-team), including requester-managed service ENIs?
**High-level Test Scenarios:**
- *Claim:* Subnet owner's subscription over a RAM-shared subnet captures AccountB's instance↔internet 5-tuples. *Oracle:* records with AccountB's `account-id` and workload IPs. *Severity: High (cross-tenant metadata).* (Documented-as-designed → confirm scope, then stop; report the field-suppression bypass if any.)
- *Claim:* The ECS-field / tag-field suppression for foreign-owned resources can be bypassed (e.g. VPC/subnet-level subscription computes a field it shouldn't for AccountB). *Oracle:* a non-`-` ECS/tag value for an AccountB-owned resource. *Severity: High (Lens U enforcement gap).*
- *Claim:* `ec2:CreateFlowLogs` with `Resource:*` lets a low-priv principal flow-log an ENI of a sensitive workload in the same account it otherwise cannot read. *Oracle:* records delivered. *Severity: Medium (intra-account).*
**Doc evidence.** `flow-logs-basics.md` (service-ENI list); `flow-logs-limitations.md` (shared-subnet ECS/tag carve-outs "due to security concerns"). 

### AREA 4 — Peered-VPC / cross-account monitoring boundary: enforced or advisory? (Lens U + X)
**Background.** `flow-logs-limitations.md`: *"You can't enable flow logs for VPCs that are peered with your VPC unless the peer VPC is in your account."*
**Security Concern.** This is a stated isolation guarantee. Is it enforced by `CreateFlowLogs` (API rejects a peer VPC id owned by another account) or only by orchestration/prose? If the check keys on the *monitored* resource's owner, does naming the resource a different way (ARN vs bare id; a sub-resource) slip past it?
**High-level Test Scenarios:**
- *Claim:* `CreateFlowLogs ResourceType=VPC ResourceId=<peer-VPC-id-in-another-account>` is accepted. *Oracle:* 200 + a flow log that captures the peer VPC's traffic. *Refute:* `InvalidParameter`/authz error naming ownership. *Severity: High if accepted.*
- *Claim:* A validator divergence exists between `CreateFlowLogs` and `DescribeFlowLogs`/`DeleteFlowLogs` on how a foreign/invalid `resource-id` is classified (500 vs 400 vs AccessDenied) → enumeration oracle for peer resources. *Severity: Low–Medium.*
**Doc evidence.** `flow-logs-limitations.md` peered-VPC sentence.

### AREA 5 — EC2-Tags enrichment exfiltrates tag values + auto-creates privileged side-resources (Lens A/T + R + L)
**Background.** A custom `LogFormat` with version-11 fields (`instance-tag`, `interface-tag`, `asg-tag`) writes **resource tag values** into every record. Enabling this needs only `ec2:DescribeTags` and **auto-creates** the SLR `AWSServiceRoleForVPCFlowLogs` (policy `AWSVPCFlowLogsServiceRolePolicy`) **and EventBridge Managed Rules** "on the customer's behalf."
**Security Concern.** (1) **Disclosure:** combined with Area 1 (un-scopable destination), tag values — which often encode owner, environment, cost-center, or sensitive labels — are exfiltrated to the attacker destination; the enrichment widens what one `CreateFlowLogs` call leaks. (2) **IAM-artifact audit (Lens R/S):** `AWSVPCFlowLogsServiceRolePolicy` statement `AllowDescribeTagsOnAllEC2Resources` grants `tag:GetResources` + `autoscaling:DescribeTags` on **`Resource:"*"` with no condition** — an AWS-authored, uneditable managed policy reading *all* tags account-wide. (3) **Availability (Lens L/O):** docs warn "Do not manually delete these EventBridge Managed Rules. Doing so will result in large delays updating tag values" — a tamper/DoS lever on tag freshness.
**High-level Test Scenarios:**
- *Claim:* A single `CreateFlowLogs` with `TagFieldSpecification` on `instance` silently creates the SLR + EventBridge rules even for a caller who was not granted `iam:CreateServiceLinkedRole` explicitly. *Oracle:* SLR + rules exist post-call. *Severity: Low–Medium (side-effect privilege creation).*
- *Claim:* The `Resource:"*"`-unconditioned `tag:GetResources`/`autoscaling:DescribeTags` statement lets the SLR read tags on resources the subscription owner otherwise couldn't enumerate. *Oracle:* `SimulatePrincipalPolicy` on the SLR confirms account-wide tag read with no condition. *Severity: Medium (AWS-authored over-broad artifact → Tier-2 report).*
- *Claim:* Deleting the managed EventBridge rule (as a mischievous insider) stalls tag updates up to ~1h → stale/incorrect security tags in logs. *Oracle:* tag values freeze. *Severity: Low (integrity/availability).*
**Doc evidence.** `flow-log-records.md` v11 tag fields ("you need permission to call `ec2:DescribeTags` and `iam:CreateServiceLinkedRole`"); `flow-logs-slr.md`; `flow-logs-managed-policy.md` (`AllowDescribeTagsOnAllEC2Resources`, `Resource:"*"`, no condition); `flow-logs-limitations.md` (EventBridge-rule warning, 1h stale window).

### AREA 6 — `DescribeFlowLogs` account-wide recon (Lens A + O)
**Background.** `DescribeFlowLogs` has **no resource type** and only the `ec2:Region` condition key. It returns the full `FlowLog` object: `logDestination`, `logGroupName`, `deliverLogsPermissionArn`, `deliverCrossAccountRole`, `resourceId`, `logFormat`, `deliverLogsStatus/ErrorMessage`.
**Security Concern.** Any principal with `ec2:DescribeFlowLogs` (commonly bundled in read-only/analyst policies) can enumerate, across the whole account, every monitored resource, every destination bucket/log-group/stream, and every **delivery-role ARN** — a target list for Areas 1–2 and for broader role-abuse. Scoping is impossible (only region).
**High-level Test Scenarios:**
- *Claim:* A read-only principal recovers all delivery-role ARNs + destination ARNs account-wide. *Oracle:* `FlowLog` objects returned with those fields populated. *Severity: Low–Medium (recon / info-disclosure enabler).*
- *Claim:* `deliverLogsErrorMessage` ("Access error", "Rate limited") distinguishes misconfigured subscriptions → oracle for which delivery roles are under-permissioned (soft targets). *Severity: Low.*
**Doc evidence.** `API_DescribeFlowLogs.md` (no resource type, region-only); `API_FlowLog.md` (fields).

### AREA 7 — Detection-evasion: delete, starve, and blind-spot the monitor (Lens O + L)
**Background.** `DeleteFlowLogs` disables monitoring (and does **not** remove already-delivered data). There is a **250-subscription-per-resource-per-account** cap. The limitations page lists traffic that is **never captured**: to/from `169.254.169.254` (IMDS), Amazon DNS server, `169.254.169.123` (Time Sync), DHCP, ARP, default-router IP, endpoint-NIC↔NLB-NIC, Traffic-Mirroring *source*, and short-lived regional NAT gateways. Records may be silently **SKIPDATA**; VPC BPA logs omit `bytes`; default `dstaddr/srcaddr` can mask the real peer unless `pkt-*` fields are requested.
**Security Concern.** An attacker who can `DeleteFlowLogs` (tag-scopable, so a mis-tagged subscription is deletable) can blind a defender; one who can `CreateFlowLogs` can exhaust the 250-cap to block legitimate re-subscription. The documented blind spots (IMDS/DNS exfil channels) mean data exfil over those paths produces no flow-log evidence by design.
**High-level Test Scenarios:**
- *Claim:* A principal scoped to its own resources can `DeleteFlowLogs` a security-monitoring subscription whose tags it can match (or that lacks protective tags). *Oracle:* subscription gone, no new records. *Severity: Medium (detection-evasion enabler).*
- *Claim:* Creating 250 junk subscriptions on a VPC blocks the security team from adding theirs. *Oracle:* 251st create fails with the documented cap. *Severity: Low–Medium (availability of monitoring).*
- *Claim (informational):* Exfil via IMDS/Amazon-DNS leaves no flow-log record. *Oracle:* confirmed by the non-logged-traffic list. *Severity: Informational (raises severity of other findings as an enabler).*
**Doc evidence.** `flow-logs-limitations.md` (non-logged traffic, 250 cap, SKIPDATA, BPA `bytes` omission, `pkt-*` masking); `flow-logs-basics.md` ("Deleting a flow log does not delete any existing flow log data").

### AREA 8 — S3 delivery: auto-overwrite of bucket policy, fail-open delivery, predictable paths (Lens EE + U + Q-adjacent)
**Background.** `flow-logs-s3-permissions.md`: *"If the user creating the flow log owns the bucket and has `PutBucketPolicy`/`GetBucketPolicy` … we automatically attach the following policy … This policy overwrites any existing policy attached to the bucket."* The `HeadBucket` check is non-authoritative: *"The service still delivers VPC flow logs even if it can't confirm that the S3 bucket exists."* Object paths/filenames are deterministic (`AWSLogs/{account}/vpcflowlogs/{region}/{y}/{m}/{d}/{account}_vpcflowlogs_{region}_{flow-log-id}_{ts}_{hash}.log.gz`) with only an undocumented trailing `{hash}`.
**Security Concern.** (1) **Policy clobber:** triggering `CreateFlowLogs` toward a bucket you own with `PutBucketPolicy` silently **overwrites the entire existing bucket policy** — a foot-gun / possible privilege or deny-rule removal vector if a tool can be coerced into it. (2) **Fail-open delivery** to a non-confirmed bucket — a mistyped/pre-registered bucket name still receives logs (land-grab: pre-create a bucket matching a predictable name, Lens EE). (3) **Predictable keys** mean a reader with partial bucket access can locate specific flow logs by composing public identifiers.
**High-level Test Scenarios:**
- *Claim:* A `CreateFlowLogs` to a self-owned bucket replaces a pre-existing restrictive bucket policy wholesale. *Oracle:* prior policy statements gone after the call. *Severity: Medium.*
- *Claim:* Logs are delivered to a bucket name that did not exist at create time but is later created by an attacker (predictable-name land-grab). *Oracle:* records appear in the attacker-created bucket. *Severity: High if cross-account.*
- *Claim:* `aws/s3` managed key on a central bucket blocks cross-account delivery (documented 400) — confirming SSE-KMS-managed-key is an isolation control that *does* hold, i.e. a refute/boundary-holds result. 
**Doc evidence.** `flow-logs-s3-permissions.md`; `flow-logs-s3-path.md`; prescriptive-guidance pattern (`aws:SourceOrgID`, `aws/s3` cross-account caveat).

### AREA 9 — Cross-account Firehose role-chain & predictable role name (Lens B/C + EE)
**Background.** `firehose-cross-account-delivery.md`: source-account role carries `iam:PassRole`(→`delivery.logs.amazonaws.com`, conditioned on `iam:AssociatedResourceARN`) + `logs:CreateLogDelivery…` on `Resource:"*"` + `sts:AssumeRole` to `arn:aws:iam::{dest}:role/AWSLogDeliveryFirehoseCrossAccountRole`. The destination role **must be named with the `AWSLogDeliveryFirehoseCrossAccountRole` prefix**, grants `iam:CreateServiceLinkedRole` + `firehose:TagDeliveryStream` on `Resource:"*"`, and trusts the source role ARN.
**Security Concern.** This is the only role-assumption cross-account path (S3 is pure bucket-policy). (1) The **predictable destination role-name prefix** is a naming convention a workflow relies on — probe whether a destination account that *expects* such a role can be made to trust a source role it didn't intend (trust is pinned to a source role ARN, so likely holds — confirm). (2) `logs:*LogDelivery` and `firehose:TagDeliveryStream` on `Resource:"*"` are broad. (3) Confirm `iam:AssociatedResourceARN` actually pins the monitored resource (if mis-set to `*`, the source role can be reused for any resource).
**High-level Test Scenarios:**
- *Claim:* The source role's `iam:AssociatedResourceARN` can be satisfied for a resource other than the intended one if written with a wildcard. *Oracle:* PassRole succeeds for an unintended monitored resource. *Severity: Medium–High.*
- *Claim:* The destination `AWSLogDeliveryFirehoseCrossAccountRole`'s `Resource:"*"` `firehose:TagDeliveryStream` lets it tag streams beyond the intended one. *Oracle:* tag applied to an unrelated stream. *Severity: Medium.*
**Doc evidence.** `firehose-cross-account-delivery.md` (both role JSONs + trust policies).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Redirect victim traffic metadata to attacker destination | `CreateFlowLogs` LogDestination | **None in IAM** — no destination condition key (Area 1) |
| Pass a delivery role without `PassRole` | `DeliverLogsPermissionArn` | `iam:PassRole`+`iam:PassedToService` (verify enforced on base case, not just sample) (Area 2) |
| Confused-deputy via missing SourceAccount/SourceArn | delivery role trust / bucket policy | Only **recommended**, not enforced; S3 `SourceArn` wildcard (Area 2) |
| Monitor foreign / RAM-shared resource | `ResourceId`+`ResourceType` | monitored-leg condition keys (optional); ECS/tag suppression "due to security concerns" (Area 3) |
| Enable on peered VPC in another account | `CreateFlowLogs` VPC leg | Prose limitation "unless peer VPC is in your account" — enforcement unverified (Area 4) |
| Exfiltrate tag values / spawn SLR+rules | `LogFormat` v11 tag fields | `ec2:DescribeTags`+`iam:CreateServiceLinkedRole`; `AWSVPCFlowLogsServiceRolePolicy` `Resource:*` (Area 5) |
| Enumerate destinations/roles account-wide | `DescribeFlowLogs` | region-only authz, no resource scoping (Area 6) |
| Blind the defender | `DeleteFlowLogs` / 250 cap / blind spots | tag-scopable delete; hard cap; documented non-logged traffic (Area 7) |
| Clobber bucket policy / fail-open delivery | S3 delivery path | auto-overwrite; non-authoritative `HeadBucket` (Area 8) |
| Reuse source role across resources | Firehose cross-acct role-chain | `iam:AssociatedResourceARN` pin (verify not wildcarded) (Area 9) |

---

## 7. Out-of-Scope Risk Categories

- Shared storage/compute infra behind S3/CloudWatch Logs/Firehose themselves (shared-responsibility line).
- IMDS being unlogged on managed hosts — documented by-design blind spot, not a flaw.
- A customer writing their own over-broad `DeliverLogsPermissionArn` policy (customer-authored footgun) — **except** the AWS-authored `AWSVPCFlowLogsServiceRolePolicy` `Resource:*` statement, which **is** in scope (Tier-2, Area 5).
- Single-tenant self-DoS (exhausting your own 250-cap on your own VPC).
- Content of flow-log records as a product feature (what fields exist); only their *delivery boundary* is in scope.
- DNS-rebinding or SSRF — **no `CreateFlowLogs` field is a URL the service dereferences** (null hypothesis, §8).

## 8. Null hypotheses / doc gaps

- **Lens G (SSRF): N/A.** Pages read: `API_CreateFlowLogs.html`, `DestinationOptionsRequest`, `TagFieldSpecificationRequest`, `flow-logs-basics/records/limitations`. No field is a URL/host the service fetches/previews/renders; `LogDestination` is an AWS ARN validated as a destination, not fetched as content. No profile/branding/webhook field exists.
- **Lens F (translation/injection): N/A.** No customer input is transpiled to another language; `LogFormat` is a fixed `${field-id}` allowlist, not a template engine.
- **Lens K (prompt injection): N/A.** No LLM/agent in the pipeline.
- **Lens W (attestation), FF (JWT/OIDC), DD (cache), BB (canonicalization), CC (upstream-context): N/A** — no attestation gate, no token validation, no caching/authorizer/edge layer, single SigV4 authorizer.
- **Lens Q (upload): N/A** — no blob upload; `DestinationOptions`/`LogFormat` are enums/field-lists.
- **Lens H (KMS/enc-context): partial doc-gap.** `flow-logs-s3-cmk-policy.md` only says "use a customer-managed key ARN" and defers the actual key policy + encryption context to an external CloudWatch Logs page. **Confirm surface first**: whether `kms:EncryptionContext:aws:s3:arn` / `aws:SourceArn` can scope the CMK to the customer's own flow logs is undocumented here → open lead, not closed.
- **Lens X (modify-twin): N/A** — flow logs are immutable (no `ModifyFlowLogs`); the only lifecycle twins are Create/Delete, covered in Areas 1/7.
- **Doc gaps to resolve by live recon before relying on them:** (a) whether `ec2:CreateFlowLogs` enforces `iam:PassRole` on the *base/CWL* delivery role or only lists it in a sample policy (Area 2); (b) `GetFlowLogsIntegrationTemplate`'s generated CloudFormation IAM (undocumented — the Lambda/Athena role scope could be a Lens R target once the template text is inspected); (c) exact server-side validation of cross-account S3 consent (bucket policy only, per docs — no API handshake).

---

### Priority order for the hunter
**1** (Area 1, un-scopable destination — static-provable first via policy simulation) → **2** (confused-deputy / PassRole enforcement) → **3** (RAM-shared cross-tenant capture) → **5** (tag-value exfil + managed-policy `Resource:*`) → **4** (peered-VPC enforcement) → **9** (Firehose role-chain) → **6** (Describe recon) → **7** (detection-evasion) → **8** (S3 policy clobber / fail-open). Compose the chain: **Area 1 (destination) × Area 5 (tag enrichment) × Area 3 (foreign resource) = one `CreateFlowLogs` call exfiltrating another tenant's traffic + tag values to an attacker bucket** — rate at the chain's end (High/Critical if genuinely cross-account).
