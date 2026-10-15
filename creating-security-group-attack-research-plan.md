# CreateSecurityGroup (creating-security-group.html) — Attack Research Plan

Source of leads: offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/creating-security-group.md` (online twin `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-security-group.md` fetched 2026-10-15 — byte-identical, no drift), plus `ec2-security-groups.md`, `docs/vpc/latest/userguide/{vpc-share-limitations,security-group-sharing}.md`, and the authoritative IAM reference `docs/service-authorization/latest/reference/list_ec2.md` (grepped directly — the online copy truncates condition-key columns). Status: documentation-derived hypotheses only; nothing tested against a live account.

This is the **page-level, action-scoped deep-dive child** of the existing cluster plan `ec2-security-groups-privatelink-attack-research-plan.md`. That plan owns the whole security-groups + PrivateLink cluster (referencing / ABAC-on-rule / rule-contents-unscopable / `ec2:Vpc` binding / unshare / connection-tracking / endpoint policy). **This plan deliberately does NOT restate those eight areas — it cross-references them** and owns only what is specific to the *create* action `ec2:CreateSecurityGroup` and this one page: the insecure default-egress rule baked into every new SG, the create-time condition-key surface (what you can and cannot scope at birth), the immutable caller-chosen `GroupName`/`Description`, and the shared-VPC participant create path. It is the SG-create counterpart to the ENI-create sibling `create-network-interface-attack-research-plan.md` (same shared-VPC participant-creates-in-owner's-VPC shape) — cross-ref, do not re-derive.

## 0. How to use this document

- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.
- `list_ec2.md` line numbers below are from the author's read at research time (file ~10,190 lines; entries shift). Re-grep if the mirror is refreshed.
- The safe first oracle for every IAM-scoping lead here is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` — a condition key either applies to the action or it does not, settleable with **no resource created**. Escalate to a live scoped `create-security-group` call only with canary tags/VPCs.

## 1. Pentest Objectives

1. Determine whether an org can author a `CreateSecurityGroup` identity policy / SCP that forces every new SG to a safe baseline — specifically whether the **default outbound "allow all traffic" rule** can be prevented, or whether default-permissive egress is structurally unavoidable at create (forcing all such control into post-create Revoke + AWS Config/prose).
2. Enumerate exactly which properties of a new SG are IAM-scopable **at create time** vs inert, and prove the inert ones are inert (notably `ec2:SecurityGroupID`, which cannot exist before the call returns).
3. Determine whether the caller-chosen, **immutable** `GroupName` plus per-VPC name uniqueness creates a land-grab / shadow-resource pre-registration primitive against name-based automation (CloudFormation, scripts) in a shared or same VPC.
4. Determine whether a RAM-share **participant** can create security groups inside the **owner's** shared VPC, who owns the result, and whether the owner can clean it up — a persistent-foreign-resource and quota/limit question paralleling the ENI-create sibling.
5. Determine whether tag-on-create governance (`aws:RequestTag`/`aws:TagKeys`) is the only enforceable create-time ABAC lever and whether a mandatory-tag Deny fails open when `TagSpecifications` is omitted.

## 2. Components, Assets, and Design

**Customer-facing interface.** A single mutating EC2 control-plane action, `ec2:CreateSecurityGroup` (console "Create security group", CLI `aws ec2 create-security-group`, PowerShell `New-EC2SecurityGroup`, SDK, CloudFormation `AWS::EC2::SecurityGroup`). SigV4/IAM only; runs under the **caller's own identity** — no role is passed, no service-linked role, no STS, no server-side fetch. There is no data-plane component to this page; the SG it creates is enforced later at the ENI by the Nitro system (that enforcement surface is owned by the cluster plan's Area 6 / `ena-nitro-perf`).

**Request inputs (from the page + API):**
- `GroupName` (**required**, caller-chosen, **immutable after create** — "You can't change the name and description of a security group after it is created"). Must be unique within the VPC; cannot start with `sg-`; printable-ASCII limited.
- `Description` (**required**, caller-chosen, **immutable**).
- `VpcId` (which VPC the group is born into — the one create-time property with real IAM scoping, via the `vpc` resource row).
- `TagSpecification` (optional — the only create-time ABAC lever).

**What a new SG *is* at birth (the asset):** `security-group` — `arn:${Partition}:ec2:${Region}:${Account}:security-group/${SecurityGroupId}` (`sg-...`), bound to exactly one home VPC. **Documented default state (the headline asset property):** "New security groups start with **only an outbound rule that allows all traffic to leave the resource**. You must add rules to enable any inbound traffic or to restrict the outbound traffic." I.e. every new SG ships **inbound default-deny** (safe) but **outbound `0.0.0.0/0` + `::/0` allow-all** (permissive). Port 25 egress is throttled by AWS by default (`ec2-resource-limits.md#port-25-throttle`) — an AWS-plane control, not customer-expressible.

**Create-time IAM surface (authoritative, `list_ec2.md` L5446–5452):** `ec2:CreateSecurityGroup` requires **two** resource rows:
- `security-group*` → condition keys: `aws:RequestTag/${TagKey}`, `aws:TagKeys`, `ec2:Region`, `ec2:SecurityGroupID`.
- `vpc` → condition keys: `aws:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:Tenancy`, `ec2:VpcID`.

Note what is **absent**: no condition key for `GroupName`, none for `Description`, none for the default egress rule, and (on the `security-group*` row) **no `aws:ResourceTag`** (the SG does not yet exist to carry a tag). `ec2:SecurityGroupID` on the create row is structurally inert (see Area 2).

**Accounts/VPCs/ownership.** The only cross-boundary shape on *this* action is **shared-VPC create**: a RAM-share participant can create SGs in a subnet shared to it from an owner account (`vpc-share-limitations.md` L18, L50). The SG is owned by the **participant**; the VPC owner "can describe the security groups created by participants … cannot work with [them] in any other way" (L54). This is the SG twin of the ENI-create sibling's Area 2.

```
 caller (IAM principal)
      | ec2:CreateSecurityGroup  (own identity; no PassRole/SLR/STS)
      v
 [EC2 control plane] --scopes--> ec2:VpcID / ec2:Tenancy / ec2:ResourceTag(vpc)   <-- which VPC (REAL lever)
      |                           aws:RequestTag / aws:TagKeys (sg)               <-- tag-on-create (opt-in lever)
      |                           ec2:SecurityGroupID (sg)  == INERT at create
      v
 new sg-xxxx  (home VPC fixed; GroupName/Description caller-chosen + IMMUTABLE)
      |
      +-- default state: inbound DENY-ALL (safe)  /  outbound ALLOW-ALL 0.0.0.0/0+::/0 (permissive, AWS default)
      |
 shared-VPC case: participant creates sg in OWNER's VPC; participant owns it; owner can only Describe
```

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv IAM principal | A new SG's egress posture | `CreateSecurityGroup` leaves `0.0.0.0/0` allow-all egress with no create-time knob | An org that intends "no open egress" **cannot** author a `CreateSecurityGroup` policy/SCP that prevents it — the default is permissive and unconditionable at create = exfil-permissive baseline on every new SG |
| IAM policy author | "only create SGs for *my* resources" intent | `ec2:SecurityGroupID` present on the create row | A Deny/Allow keyed on `ec2:SecurityGroupID` at create is **inert** (id doesn't exist pre-call) → policy that looks scoped is vacuous |
| Participant account | Owner's shared VPC | `CreateSecurityGroup` with owner's shared `VpcId` | A participant-owned `sg-` lands in the owner's VPC; owner can Describe but not delete → persistent foreign resource / quota consumption / name land-grab |
| Attacker in same/shared VPC | Victim's name-based automation | Caller-chosen immutable `GroupName`, unique per VPC | Attacker pre-creates the `GroupName` a victim's CFN/script expects → victim's create collides/fails, or victim's by-name lookup resolves the attacker's SG |
| IAM principal subject to tag governance | Mandatory-tag Deny | `TagSpecification` optional on create | Create succeeds with **no** tags when policy intended `aws:RequestTag` to force them (Null-key fail-open) |
| Any customer surface | AWS service plane | — | Any AWS-owned identity/ARN/credential = HARD STOP |

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2:CreateSecurityGroup` | API/CLI/PS/CFN | Existing | Mutating | External | Create an SG in a VPC with name+description+optional tags | Yes | IAM-scoped: `security-group*` (RequestTag/TagKeys/Region/SecurityGroupID) + `vpc` (ResourceTag/Region/Tenancy/VpcID) | **No condition key for GroupName, Description, or the default egress rule.** `ec2:SecurityGroupID` inert at create. Areas 1–5. |
| `AuthorizeSecurityGroupEgress`/`Ingress` | API | Existing | Mutating | External | Add rules (incl. revoking the default egress to tighten it) | Yes | see cluster plan Area 2/3 | The *only* way to tighten the default egress is a **separate** post-create call → cluster plan owns rule-content unscopability. |
| `RevokeSecurityGroupEgress` | API | Existing | Mutating | External | Remove the default allow-all egress | Yes | `security-group*` scoped | Deferred to cluster plan; relevant here only as "the default is permissive until a second action fires." |

Doc-flagged focus sentence (verbatim, keep the pointer): *"New security groups start with only an outbound rule that allows all traffic to leave the resource. You must add rules to enable any inbound traffic or to restrict the outbound traffic."* — AWS plants the default-posture lead right there.

## 5. Recommended Areas of Focus

### Area 1 — The default allow-all egress rule is an AWS-baked permissive baseline with no create-time IAM knob (Lens U / R / S) — HEADLINE
**Background.** The page states every new SG begins with a single outbound rule allowing **all** traffic to all destinations (`0.0.0.0/0` + `::/0`), and only inbound is default-deny. Tightening egress requires a *separate* `RevokeSecurityGroupEgress` + narrower `AuthorizeSecurityGroupEgress` call.
**Security Concern.** An organization that wants "no SG may permit unrestricted egress" has **no mechanism at the create action** to enforce it: `list_ec2` gives `CreateSecurityGroup` no rule-content / egress / CIDR condition key (whole-doc grep for rule-content keys = 0; cross-ref cluster Area 3 which proves the same for the Authorize* actions). So the exfil-permissive default stands on every new SG for the window between create and a corrective Revoke — and if the principal is denied the Revoke/Authorize actions, permanently. This is an **AWS-authored insecure default** surfaced as a copy-paste expectation ("keep the default rule, which allows all outbound traffic" — the Console step 7 literally recommends keeping it) → Lens R/U, Tier-2 reportable framing (AWS owns the default, the customer cannot change it at create).
**High-level Test Scenarios.**
- Claim: *No `CreateSecurityGroup` policy or SCP can force new SGs to lack an open-egress rule.* → Oracle: `iam:SimulateCustomPolicy` for `ec2:CreateSecurityGroup` with every plausible egress-scoping condition key — confirm none exists / none denies based on resulting rules. Refute if any key (or an SCP pattern) blocks create based on the default rule.
- Claim: *There is a create→tighten race.* → Oracle: time-box between `CreateSecurityGroup` returning and the SG being associated to an ENI; during it, egress is open. Confirm by associating a canary instance immediately after create (before any Revoke) and observing outbound reachability.
**Doc evidence.** `creating-security-group.md` Considerations bullet 1 + Console step 7; `list_ec2.md` L5446–5452 (no rule-content key). **Severity-if-true.** Low–Medium as a hardening/guarantee gap (defense-in-depth; AWS-owned, uneditable default). Not a cross-tenant breach.

### Area 2 — `ec2:SecurityGroupID` is inert on the create action (Lens S — inert-key / attacker-chosen-value shape)
**Background.** The `security-group*` resource row for `CreateSecurityGroup` lists `ec2:SecurityGroupID` as a condition key. But the `sg-...` id is minted *by the service as the result of the call* — it does not exist when the authorization decision is made.
**Security Concern.** A policy author who writes `Condition: {StringEquals: {ec2:SecurityGroupID: sg-abc}}` (or a Deny on a set of ids) on `CreateSecurityGroup` will produce a statement that is **structurally un-satisfiable / vacuous at create** — the create either never matches (fail-closed, surprising) or the key resolves absent (fail-open depending on operator). This is the same class as the confirmed `ec2:InterfaceType`-is-not-a-real-key and `ec2:SecurityGroupID`-pre-existence shapes in the sibling plans: a condition key that *looks* like a lever but cannot bind at this action.
**High-level Test Scenarios.**
- Claim: *`ec2:SecurityGroupID` cannot constrain `CreateSecurityGroup`.* → Oracle: `SimulateCustomPolicy` with an Allow on `ec2:CreateSecurityGroup` conditioned on `ec2:SecurityGroupID` — observe whether any create is ever permitted (fail-closed) or whether the condition is ignored (fail-open). Either outcome proves the key is not a usable create-time lever.
- Corollary (positive): confirm the **real** create-time levers are exactly `ec2:VpcID`/`ec2:Tenancy`/`ec2:ResourceTag`(vpc) and `aws:RequestTag`/`aws:TagKeys`(sg) — i.e. you can bound *which VPC and with which tags* an SG is born, nothing else.
**Doc evidence.** `list_ec2.md` L5448 (`security-group*` row). **Severity-if-true.** Informational–Low (policy-author footgun / silent fail), but worth filing: a defender believes they scoped create and did not.

### Area 3 — Immutable caller-chosen `GroupName` + per-VPC uniqueness = land-grab / shadow-resource pre-registration (Lens EE / P / S)
**Background.** `GroupName` and `Description` are caller-supplied, **immutable after create** (page: "You can't change the name and description … after it is created"), and SG names must be **unique within a VPC**. No `GroupName` condition key exists on the create action.
**Security Concern.** Two distinct shapes:
- **(EE) Predictable-name pre-registration:** automation that references an SG **by name** (CloudFormation `GroupName` property, Terraform `name`, scripts doing `describe-security-groups --filters Name=group-name`) assumes it will create/own that name. If an attacker who can create SGs in the same VPC (same account cross-team, or a shared-VPC participant — Area 4) **pre-creates the expected `GroupName` first**, the victim's create fails on the uniqueness constraint (DoS on deploy), or the victim's by-name lookup resolves the **attacker's** SG (wrong-rules substitution — the attacker's SG may be wide-open or reference attacker SGs). Because the name is immutable, the squat is sticky.
- **(P) Uniqueness/dedup bypass variants:** does uniqueness normalize case / unicode / trailing whitespace, or can `MyApp` and `myapp` co-exist and confuse a case-insensitive by-name consumer? Can two concurrent creates race the uniqueness check (double-claim)?
**High-level Test Scenarios.**
- Claim: *An attacker can occupy a GroupName a victim's IaC will later try to create in the same VPC.* → Oracle: create `sg` named `X` in VPC V; attempt a second create of `X` in V → expect `InvalidGroup.Duplicate`. Confirms the DoS/land-grab precondition. Then test whether a `describe … Name=group-name=X` by the victim returns the attacker's `sg-id`.
- Claim: *Uniqueness is not normalization-safe.* → Oracle: create `X` then `x`/`X ` (trailing space)/unicode-homoglyph in the same VPC; a success is a confusion primitive.
**Doc evidence.** `creating-security-group.md` Console step 4 (immutability) + general per-VPC name uniqueness; `list_ec2.md` L5448 (no GroupName key). **Severity-if-true.** Medium where name-based automation trusts the resolved SG (wrong-rules substitution); Low as pure deploy-DoS. Cross-tenant only via the shared-VPC path (Area 4).

### Area 4 — A shared-VPC participant creates SGs inside the owner's VPC; the owner cannot clean them up (Lens A / EE / L — shared-VPC) 
**Background.** `vpc-share-limitations.md` L18 + L50: "participants can create network interfaces and **security groups** … in a shared VPC subnet"; the resources "count against the VPC quotas in the **participant** account." L54: "VPC owners can **describe** the security groups created by participants … **cannot work with** [them] in any other way." L52–53: participants cannot *use* the owner's default/non-shared SGs, but they can freely *create their own*.
**Security Concern.** This is the SG twin of the ENI-create sibling's Area 2. A participant account:
- creates participant-owned `sg-` objects inside the **owner's** VPC that the owner can see but **cannot delete or modify** → persistent foreign resources the owner cannot garbage-collect (parallels the un-deletable foreign ENI; combined, a participant can clutter/limit-exhaust the owner's VPC with SGs the owner is powerless over);
- can **name-squat** (Area 3) inside the owner's VPC namespace, since GroupName uniqueness is per-VPC and the VPC is the owner's → cross-account land-grab against the owner's or other participants' by-name automation;
- its SGs can **reference** other participants'/owner's SGs by `account-number/security-group-id` (L51) — chains into the cluster plan's Area 1 referencing/audit-blind-spot (cross-ref, do not re-derive).
**High-level Test Scenarios.**
- Claim: *Participant can create an SG in the owner's shared subnet that the owner cannot delete.* → Oracle (2-account canary): owner shares a subnet via RAM; participant `create-security-group --vpc-id <owner VPC>`; owner attempts `delete-security-group` → expect denial/no-op; owner `describe` shows it. Confirms persistent-foreign-resource.
- Claim: *Participant can exhaust the owner's per-VPC SG quota / land-grab names.* → Oracle: enumerate how participant-created SGs count against which account's quota (docs say participant's quota — verify) and whether name uniqueness blocks the owner's later same-name create.
**Doc evidence.** `vpc-share-limitations.md` L18/L50–54; `creating-security-group.md` Console step 5 ("choose the VPC"). **Severity-if-true.** Medium–High (cross-account persistent resource + name land-grab against owner automation). Needs 2-account canary — `DryRun` is caller-IAM only and cannot answer the ownership/cleanup question. Cross-ref `create-network-interface-attack-research-plan.md` Area 2.

### Area 5 — Tag-on-create is the only create-time ABAC lever and is opt-in (Lens I / S)
**Background.** The sole value-bearing create-time condition keys on the `security-group*` row are `aws:RequestTag/${TagKey}` and `aws:TagKeys` — populated only if the caller supplies `TagSpecification`. The `vpc`-row keys scope *where* the SG is born but not the SG's own attributes.
**Security Concern.** Mirror of the cluster plan's Area 2 (which covers the *rule* resource). If an org's governance Deny is `Deny CreateSecurityGroup unless aws:RequestTag/Owner exists`, does omitting `TagSpecification` cause a clean deny, or does the absent key fail the condition open? And can the principal that creates the SG also tag it with the very key an ABAC grant later reads (self-widen), given no `aws:ResourceTag` exists at create? This is the mandatory-tag fail-open + self-tagging-widening pair.
**High-level Test Scenarios.**
- Claim: *A mandatory-tag Deny on CreateSecurityGroup fails open when TagSpecifications is omitted.* → Oracle: `SimulateCustomPolicy` with `Deny … Condition {Null: {aws:RequestTag/Owner: true}}` vs `{StringNotEquals …}`; confirm which formulation actually blocks an untagged create (the classic `Null` vs value-match asymmetry).
- Claim: *The creator can set the tag key its own later ABAC access keys on.* → Oracle: create with `TagSpecification Owner=me`, then confirm an `aws:ResourceTag/Owner`-gated subsequent action (associate/authorize) now passes — self-grant.
**Doc evidence.** `list_ec2.md` L5448. **Severity-if-true.** Medium where tags *are* the access-control mechanism; else Low (governance footgun). Cross-ref cluster Area 2.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Open-egress default survives on every new SG; org cannot forbid at create | `CreateSecurityGroup` default rule | "You must add rules to … restrict the outbound traffic" (manual, post-create) + AWS Config/SCP out-of-band — **no create-time IAM key** |
| Policy keyed on `ec2:SecurityGroupID` at create is vacuous | create-row condition key | none — defender must know the key is inert and scope by VPC/tag instead |
| GroupName land-grab / wrong-SG-by-name substitution | immutable `GroupName`, per-VPC uniqueness | per-VPC uniqueness is the only guard; no owner-pinning for by-name lookups |
| Participant-created SG in owner's VPC un-deletable by owner | shared-VPC create | "VPC owners can describe … cannot work with [them] in any other way" (by design — the gap *is* the design) |
| Mandatory-tag governance bypass at create | `aws:RequestTag`/`TagKeys` | tag-on-create ABAC — enforced only if policy uses `Null`/`ForAllValues` correctly and `TagSpecification` cannot be omitted |

## 7. Out-of-Scope Risk Categories

- The **rule-authoring** actions (`Authorize*`/`Revoke*`/`ModifySecurityGroupRules`/`UpdateSecurityGroupRuleDescriptions*`), rule-content unscopability, security-group **referencing**, `AssociateSecurityGroupVpc` `ec2:Vpc` binding, cross-Org **unshare** revocation completeness, **connection-tracking** flow survival, and **PrivateLink** endpoint policy — all owned by `ec2-security-groups-privatelink-attack-research-plan.md`. Do not duplicate.
- Nitro-side **enforcement** of SG rules and the flow-cache guarantee gap — `ena-nitro-perf-attack-research-plan.md` + cluster Area 6.
- Port-25 egress throttle — AWS service-plane control, not customer-expressible.
- Customer-authored over-broad `CreateSecurityGroup` policies — least-privilege footgun (out of scope). The in-scope carve-out is the **AWS-authored default egress rule** (Area 1), which the customer cannot edit at create.
- Shared RDS/Grover/storage infra; IMDS on managed hosts; single-tenant self-DoS from creating many SGs in one's own VPC.

## 8. Null Hypotheses / Doc Gaps

- **Lens B/C (PassRole / credential vending) — NULL.** `CreateSecurityGroup` runs under the caller's own identity; no role ARN, no SLR, no STS, no `iam:PassRole` on the action (read `creating-security-group.md` all three tabs + `list_ec2.md` L5446–5452). 
- **Lens G (SSRF) — NULL.** No field on this action is dereferenced server-side; `VpcId`/`GroupName`/`Description`/tags are identifiers/strings, not fetched URLs (read the full page; Description is free text but is stored, not fetched/rendered server-side — if a downstream console/tool renders it unsanitized that is a consumer-side XSS lead, Lens Q/output-side, noted for a UI pass).
- **Lens F/H/K/M/W/Y/J/FF/N/BB/CC/DD/T — NULL** for this single mutating control-plane action (no parser/translation layer, no KMS, no LLM, no session id, no attestation, no TLS-floor claim on the action itself, no OAuth, no token validation, no namespace migration, no multi-parser request path, no upstream-asserted-identity header, no cache layer, no generated-secret persistence). Each checked against the page + IAM rows.
- **Lens Q (upload) — NULL on input;** flagged on **output** only: `Description`/`GroupName` are caller free-text stored and later rendered in consoles/third-party tools — a stored-content XSS/MIME question that belongs to whatever renders it, not to EC2. Mark "doc-gap — confirm the rendering surface before investing."
- **Doc gaps to settle before investing:** (a) exact `GroupName` uniqueness normalization (case/unicode/whitespace) — not stated on the page; (b) whether a mandatory-tag Deny formulation reliably blocks an untagged create — needs `SimulateCustomPolicy`; (c) shared-VPC SG quota accounting (docs say participant's quota — confirm) and the precise set of owner actions denied on a participant-created SG; (d) whether `ec2:SecurityGroupID` on create fails open or closed under each operator — needs the simulator.

See [[reference-aws-iam-service-auth-ref-url]], [[project-aws-research-plans]].
