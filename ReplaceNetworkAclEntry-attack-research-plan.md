# EC2 Network ACL (ReplaceNetworkAclEntry) API Family — Attack Research Plan

**Source of leads:** Local mirror `/work/aws-docs` + live `docs.aws.amazon.com`. Anchor page: `https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReplaceNetworkAclEntry_section.html` (a thin CLI/PowerShell code-example). Primary evidence pulled from:
- `docs/AWSEC2/latest/APIReference/API_ReplaceNetworkAclEntry.md`, `API_CreateNetworkAcl.md`, `API_CreateNetworkAclEntry.md`, `API_DeleteNetworkAcl.md`, `API_DeleteNetworkAclEntry.md`, `API_ReplaceNetworkAclAssociation.md`, `API_DescribeNetworkAcls.md`, `API_NetworkAcl.md`, `API_NetworkAclEntry.md`, `API_NetworkAclAssociation.md`
- `docs/service-authorization/latest/reference/list_ec2.md` (authoritative IAM action/condition-key/resource tables)
- `docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md`, `supported-iam-actions-tagging.md`
- `docs/vpc/latest/userguide/` : `vpc-network-acls.md`, `nacl-rules.md`, `default-network-acl.md`, `custom-network-acl.md`, `create-network-acl.md`, `network-acl-associations.md`, `amazon-vpc-limits.md`, `vpc-policy-examples.md`
- `docs/sagemaker/latest/dg/sagemaker-hyperpod-prerequisites-iam.md` (AWS-authored sample policy)

**Status:** Documentation-derived hypotheses only. Nothing has been tested against a live AWS account. Each lead is falsifiable with a stated oracle; a hunter must confirm empirically in an authorized account.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5). Look left and right for adjacent bugs.
- **Scope reality:** this is an EC2 control-plane **mutating** API family that edits a *subnet-level stateless packet filter*. The `network-acl` ARN (`arn:${Partition}:ec2:${Region}:${Account}:network-acl/${NaclId}`) embeds the account → **cross-account resource access via a foreign `NetworkAclId` is architecturally bounded and is treated here as a genuine null hypothesis** (Section 8). The live-value leads are therefore (a) IAM authorization-granularity / least-privilege gaps, (b) one AWS-authored sample policy weakness, and (c) robustness/guarantee-vs-enforcement questions.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to AWS's **own service plane**, stop immediately, preserve evidence, and flag for AWS-Security disclosure. (Not expected for this pure customer-plane API family, but the rule stands.)
- **Dummy-data / read-only discipline:** confirm existence of a boundary gap, never exploit beyond it. Mutating NACL rules changes live firewall posture — a hunter must operate only in a disposable test VPC it owns, with synthetic subnets, and must restore/tear down every rule and ACL it creates.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **IAM rule-content escape:** Prove that a principal authorized to `ec2:ReplaceNetworkAclEntry`/`CreateNetworkAclEntry` on a specific NACL can write a rule the policy author intended to forbid (e.g., flip a `deny` to `allow`, open `0.0.0.0/0` on all ports) — i.e., that IAM cannot bound rule *content*.
2. **Second-path firewall change:** Prove that a principal denied entry-edit on a NACL can still change a subnet's effective firewall via `ReplaceNetworkAclAssociation` (re-point to a permissive NACL) — the "govern one action, miss the twin" gap.
3. **Silent condition-key no-op:** Prove that `ec2:NetworkAclID` on `CreateNetworkAcl`, and a single-`Condition` `ec2:Vpc` block on `ReplaceNetworkAclAssociation`, do not scope as a naïve policy author would expect.
4. **ABAC self-widening:** Prove that a principal with tag-gated NACL-mutation + `ec2:CreateTags` on `network-acl` can self-stamp the gating tag and defeat the ABAC boundary.
5. **AWS-authored artifact weakness:** Confirm the shipped SageMaker HyperPod prerequisites policy grants the full NACL mutation surface on `Resource:"*"` with no condition (an uneditable/copy-verbatim AWS defect → Tier 2 disclosure).
6. **Reserved-rule robustness:** Determine whether `ReplaceNetworkAclEntry` accepts `RuleNumber` 32767 (the internal/implicit final-deny band) and can overwrite the default deny with an allow.
7. **Defense-evasion mapping:** Document that no NACL rule can block IMDS/DNS/DHCP/ECS-metadata/Time-Sync egress (relevant to any "lock the subnet with NACL" assumption).

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 Query/JSON API over HTTPS (`https://ec2.<region>.amazonaws.com/`), SigV4 IAM auth, API version `2016-11-15`. Reached via CLI (`aws ec2 replace-network-acl-entry`), PowerShell (`Set-EC2NetworkAclEntry`), all language SDKs, console. No non-SDK/internal API in this family.

**The managed asset: a stateless subnet packet filter.** A **network ACL (NACL)** is an ordered set of numbered ingress rules + a separate ordered set of egress rules, evaluated lowest-number-first, first-match-wins, with an uneditable implicit final deny (`*` ≈ rule 32767). NACLs are **stateless** (`vpc-network-acls.md:42`). A subnet has exactly one NACL at a time; the default NACL allows all, a custom NACL denies all until populated and until explicitly associated (`default-network-acl.md:8`, `create-network-acl.md:19`).

**Resource identifiers.**
- `network-acl` → `acl-xxxxxxxx` / `acl-0ea1f54ca7EXAMPLE`; ARN `arn:${Partition}:ec2:${Region}:${Account}:network-acl/${NaclId}` (`list_ec2.md:9977`). Account-scoped.
- association → `aclassoc-xxxxxxxx` (opaque; **not** a standalone IAM resource — no ARN, authorized via its subnet + NACL).
- A *rule/entry* is **not** an addressable resource: it is identified only by (`NetworkAclId`, `Egress`, `RuleNumber`) tuple and carries `CidrBlock`/`Ipv6CidrBlock`/`Protocol`/`PortRange`/`Icmp`/`RuleAction`.

**Identity / ownership.** Pure SigV4 IAM. No service account, no multi-tenant shared fleet, no data plane, no credential vending, no LLM, no uploads, no URLs dereferenced, no KMS. All boundaries are **intra-account IAM authorization boundaries** between principals/teams/VPCs in one account, plus the account boundary itself (enforced by the ARN).

**Pipeline (control-plane only):**

```
Principal (SigV4) ──► EC2 API frontend ──► IAM authorization ──► NACL store
                                               │                     │
                 (authorizes by: action +      │                     ▼
                  network-acl ARN/ID/tag/VPC;   │        rule set (ingress/egress), association(subnet)
                  CANNOT authorize by rule      │                     │
                  content: allow/deny/CIDR/     │                     ▼
                  port/proto/rulenumber)        └──────► data-plane enforcement at subnet edge (stateless)
```

The decisive design fact: **authorization granularity stops at the NACL object; it does not reach rule content.**

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Principal scoped to NACL *object* | Rule *content* of that NACL | `ReplaceNetworkAclEntry`/`CreateNetworkAclEntry` | Writing a rule the policy intended to forbid (allow 0.0.0.0/0 all-ports) succeeds — IAM never saw the content. **Confirmed-by-docs gap (F5); live test = demonstrating no policy can stop it.** |
| Principal denied entry-edit on NACL-A | Subnet's effective firewall | `ReplaceNetworkAclAssociation` (re-point subnet to permissive NACL-B) | Subnet firewall changes without any `*NetworkAclEntry` permission. |
| Principal with tag-gated mutation + `CreateTags` | The ABAC gating tag | `CreateTags` on `network-acl` then satisfy `aws:ResourceTag` condition | Self-stamping the gate tag onto a foreign (same-account) NACL, then mutating it. |
| Naïve policy author's intent | Actual runtime scoping | `ec2:NetworkAclID` on `CreateNetworkAcl`; single `ec2:Vpc` `Condition` on multi-resource `ReplaceNetworkAclAssociation` | The condition resolves to `*` / skips a resource leg → broader than written. |
| Principal in account X | NACL `acl-*` in account Y | Any NACL action with a foreign `NetworkAclId` | **Genuine null** — ARN embeds account; foreign ID won't resolve. Record, do not pursue. |
| Any NACL rule (deny-all egress) | IMDS/DNS/DHCP/ECS-metadata/Time-Sync | Data-plane | Traffic to these egresses regardless of rule → NACL is not an exfil control (by design, documented). |
| Any customer surface | AWS service plane | — | **HARD STOP** if ever reached. Not expected here. |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Facing | Required IAM resource(s) | Content-scopable? | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| ReplaceNetworkAclEntry | Query/SDK | **Yes** | External | `network-acl*` | **No** (F5) | IAM w/ `ec2:ReplaceNetworkAclEntry` | Conds: `aws:ResourceTag`,`ec2:NetworkAclID`,`ec2:Region`,`ec2:ResourceTag`,`ec2:Vpc`. Doc omits the 1–32766 RuleNumber constraint that Create states. |
| CreateNetworkAclEntry | Query/SDK | **Yes** | External | `network-acl*` | **No** (F5) | `ec2:CreateNetworkAclEntry` | RuleNumber doc constraint 1–32766; 32767–65535 "reserved for internal use". |
| DeleteNetworkAclEntry | Query/SDK | **Yes** | External | `network-acl*` | partial (no rule-content key) | `ec2:DeleteNetworkAclEntry` | Removing a deny rule = opening traffic. |
| ReplaceNetworkAclAssociation | Query/SDK | **Yes** | External | `network-acl*` **and** `subnet*` | n/a | `ec2:ReplaceNetworkAclAssociation` | Two required resources, each exposing `ec2:Vpc` → multi-resource condition pitfall (F3). Idempotent. |
| CreateNetworkAcl | Query/SDK | **Yes** | External | `network-acl*` **and** `vpc*` | n/a | `ec2:CreateNetworkAcl` | Uses `ec2:VpcID` (string) on the `vpc*` leg, **not** `ec2:Vpc` (ARN). `ec2:NetworkAclID` here resolves to `*` at runtime (F4). Supports tag-on-create. |
| DeleteNetworkAcl | Query/SDK | **Yes** | External | `network-acl*` | n/a | `ec2:DeleteNetworkAcl` | Can't delete default NACL or one with associations. |
| DescribeNetworkAcls | Query/SDK | No | External | **none** (only `ec2:Region`) | n/a | `ec2:DescribeNetworkAcls` | **No resource-level read scoping** (F2). `owner-id` filter + `ownerId` field returned are own-account only. |

No `[NEW]` markers, no non-SDK/internal endpoints, no undocumented auth-weakening enum in this family. The entire attack value is in the *authorization-granularity delta* and *guarantee-vs-enforcement*, not in surface discovery.

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — IAM cannot constrain NACL rule content *(highest value; anchor finding)*
**Background.** `ReplaceNetworkAclEntry`/`CreateNetworkAclEntry` set `RuleAction` (allow|deny), `CidrBlock`/`Ipv6CidrBlock`, `Protocol`, `PortRange`, `RuleNumber`, `Egress`. IAM authorizes only on the `network-acl` object (tag/ID/VPC/region).
**Security Concern.** A full sweep of all ~140 EC2 condition keys (`list_ec2.md:10036-10190`) found **no** key for `RuleAction`, `CidrBlock`, `Ipv6CidrBlock`, `PortRange`, `Protocol`, `RuleNumber`, or `Egress`; the only CIDR-shaped keys (`ec2:InsideTunnelCidr*`) are VPN-only and not wired to NACL actions. So once a principal is authorized against a NACL ARN, they may write **any** rule into it.
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* A least-privilege policy intending "this role may only tighten NACL `acl-X` (add denies), never open it" cannot be expressed. → *Oracle:* author the most restrictive IAM policy you can for `ec2:ReplaceNetworkAclEntry` on `acl-X`; confirm it still permits `RuleAction=allow, Cidr=0.0.0.0/0, Protocol=-1`. Refuted only if some condition key blocks it. → *Severity:* Medium (customer least-privilege ceiling; High where a compliance control assumed rule-shape restriction is enforceable).
- *Claim:* `DeleteNetworkAclEntry` lets the same principal remove a protective deny rule, opening traffic, with the same coarse authorization.
**Doc evidence:** `list_ec2.md:5332-5336, 9425-9429, 10036-10190`; `API_ReplaceNetworkAclEntry.md:15-65`. **Severity-if-true:** Medium–High. **Stop condition:** once you demonstrate no policy expresses the content restriction, the gap is proven; do not enumerate every rule combination.

### Area 2 — Twin-action parity: entry-rewrite vs. re-association *(Lens X)*
**Background.** Two independent IAM actions change a subnet's effective firewall: `ec2:ReplaceNetworkAclEntry` (rewrite rules in place) and `ec2:ReplaceNetworkAclAssociation` (swap the subnet onto a different NACL). They have **distinct required resource-type sets** (`network-acl*` only vs. `network-acl*`+`subnet*`).
**Security Concern.** A policy that locks down rule edits on a specific NACL does nothing to the association action; a principal holding only `ReplaceNetworkAclAssociation` can re-point the subnet to a permissive/default NACL and achieve the same effect.
**High-level Test Scenarios:**
- *Claim:* Deny `ec2:ReplaceNetworkAclEntry` + `ec2:*NetworkAclEntry` on subnet S's NACL, but leave `ec2:ReplaceNetworkAclAssociation` → the subnet's firewall can still be fully changed. → *Oracle:* with that policy, `ReplaceNetworkAclAssociation` succeeds re-pointing S to a permissive NACL. → *Severity:* Medium–High (control bypass of the intended restriction).
- Also test the reverse twin: `DeleteNetworkAclEntry` as an unprotected sibling of `ReplaceNetworkAclEntry`.
**Doc evidence:** `list_ec2.md:9419-9429`; `API_ReplaceNetworkAclAssociation.md:8`. **Severity-if-true:** Medium–High. **Stop:** once both-paths divergence is shown on a single policy.

### Area 3 — AWS-authored sample policy ships full NACL mutation on `Resource:"*"` *(Lens R — in-scope, Tier 2 disclosure)*
**Background.** `sagemaker-hyperpod-prerequisites-iam.md:134-292`, Sid `AmazonVPCFullAccess`, grants `ec2:CreateNetworkAcl`, `ec2:CreateNetworkAclEntry`, `ec2:DeleteNetworkAcl`, `ec2:DeleteNetworkAclEntry`, `ec2:ReplaceNetworkAclAssociation`, `ec2:ReplaceNetworkAclEntry` (+ ~110 other EC2 actions) under a single `"Resource":"*"` with **no** `Condition`.
**Security Concern.** This is a customer-facing "copy this policy" prerequisites artifact. A principal that holds it can rewrite/replace **any** NACL in the account (all VPCs, all subnets), i.e., open or sever any subnet's firewall account-wide — far beyond provisioning one HyperPod cluster. Because the artifact is AWS-authored and copied verbatim, a weak default here is AWS's defect, not a customer footgun.
**High-level Test Scenarios:**
- *Claim:* A role holding only the HyperPod prerequisites policy can `ReplaceNetworkAclEntry` on a NACL unrelated to any HyperPod resource. → *Oracle:* `iam:SimulatePrincipalPolicy` for `ec2:ReplaceNetworkAclEntry` on an arbitrary account NACL ARN under a principal carrying exactly that policy → `allowed`. (Safe, no resources touched; escalate to a live scoped call only on canary NACLs you own.)
**Doc evidence:** `sagemaker-hyperpod-prerequisites-iam.md:134-292`. **Severity-if-true:** Medium–High (over-broad AWS-authored grant → route `aws-security`, Tier 2). **Stop:** Simulate-allow is sufficient proof.

### Area 4 — Condition-key scoping semantics pitfalls *(Lens S)*
**Background & Concern.** Three documented traps:
- **(4a) `ec2:NetworkAclID` on `CreateNetworkAcl` resolves to `*` at runtime** — `iam-policies-for-amazon-ec2.md:267-311` enumerates `ec2:NetworkAclID`–`CreateNetworkAcl` among `ec2:{Resource}ID` keys that "must specify `*`; a different value resolves to `*`". A policy pre-authorizing a specific future NACL ID is silently unscoped.
- **(4b) Multi-resource `ec2:Vpc` on `ReplaceNetworkAclAssociation`** — the key is exposed on **both** the `network-acl*` and `subnet*` legs. Per the `iam-policies-for-amazon-ec2.md:195-196` "Important" box, a single `Condition` without per-`Resource` partitioning either blocks the action entirely or, with `...IfExists`, silently skips the VPC check on the un-anchored leg → "scope to one VPC" weaker than intended.
- **(4c) `CreateNetworkAcl` VPC-scoping uses `ec2:VpcID` (string) not `ec2:Vpc` (ARN)** — a policy reusing the `ec2:Vpc` ARN pattern from the other five actions writes a key not evaluated for `CreateNetworkAcl`.
**Oracle.** For each: construct the "obvious" policy a careful author would write, then show (via `SimulatePrincipalPolicy` + a live scoped call on owned resources) that the effective scope is broader than the author's intent (the create succeeds in a VPC the policy meant to exclude / the association succeeds across a VPC leg the `ec2:Vpc` block meant to pin).
**Doc evidence:** `iam-policies-for-amazon-ec2.md:159-196, 267-311`; `list_ec2.md:5326-5330, 9419-9423, 10172`. **Severity-if-true:** Low–Medium (least-privilege scoping weaker than written). **Stop:** one demonstration per sub-case.

### Area 5 — ABAC self-widening via CreateTags/DeleteTags on network-acl *(Lens I / S)*
**Background.** NACL-mutation can be tag-gated (`aws:ResourceTag/${TagKey}`). `CreateTags`/`DeleteTags` on the `network-acl` resource type expose `aws:RequestTag`/`aws:TagKeys` but these are **opt-in**; tagging-condition enforcement is not default-safe.
**Security Concern.** A principal with (a) `ReplaceNetworkAclEntry` gated on `aws:ResourceTag/Env=prod` and (b) `ec2:CreateTags` on `network-acl*` *without* an `aws:RequestTag`/`aws:TagKeys` restriction can stamp `Env=prod` onto an arbitrary same-account NACL it can address, then satisfy its own gate.
**Oracle.** With such a policy: `CreateTags Env=prod` on a NACL that lacked it, then `ReplaceNetworkAclEntry` succeeds where it would have been denied before tagging. **Preconditions:** both actions held; CreateTags not locked by `aws:TagKeys`. **Doc evidence:** `list_ec2.md:5543` (CreateTags network-acl row), DeleteTags network-acl row; `supported-iam-actions-tagging.md:75-107`. **Severity-if-true:** Medium (ABAC bypass → effectively unscoped mutation). **Stop:** once the self-tag → mutate chain succeeds once.

### Area 6 — Reserved rule number / final-deny robustness *(Lens U / F robustness)*
**Background.** `CreateNetworkAclEntry` constrains `RuleNumber` to 1–32766, reserving 32767–65535 "for internal use" (`API_CreateNetworkAclEntry.md:69`). `ReplaceNetworkAclEntry`'s page states no range and no reference to the reserved band (`API_ReplaceNetworkAclEntry.md:62-65`); the implicit final-deny is observed at rule 32767/32768 (`API_CreateNetworkAcl.md:88-114`).
**Security Concern (open question — documentation is silent).** It is undetermined from docs whether `ReplaceNetworkAclEntry` enforces the 1–32766 bound or would accept `RuleNumber=32767` and overwrite the implicit final deny with an `allow`, defeating default-deny semantics.
**Oracle.** On a disposable owned NACL: `ReplaceNetworkAclEntry RuleNumber=32767 RuleAction=allow` → if accepted and the effective final rule becomes allow, the default-deny guarantee is bypassable; if rejected (`InvalidParameterValue`/similar), null. No action-specific error is documented (all pages defer to Common Errors), so this must be tested. **Severity-if-true:** Medium (single-account firewall-posture integrity). **Stop:** one accept/reject observation settles it.

### Area 7 — Defense-evasion / guarantee-vs-enforcement mapping *(Lens U / O — informational)*
**Background.** NACLs are stateless (need explicit ephemeral-port allows) and **cannot filter** IMDS (169.254.169.254), Route 53 Resolver DNS (VPC+2), DHCP, EC2/ECS instance & task metadata, Windows license activation, Time Sync, or reserved router IPs (`vpc-network-acls.md:46-55`).
**Security Concern.** Any control or finding that assumes "a deny-all-egress NACL contains a compromised instance / blocks exfil" is wrong for these channels by design — relevant when chaining with an SSRF/metadata finding elsewhere. Also: rule ordering is pure first-match (`nacl-rules.md:11`), so an attacker who can insert a *low-numbered* allow overrides any higher-numbered operator deny (Area 1 consequence).
**Oracle.** Documentation-confirmed; for a hunt, demonstrate IMDS reachable from an instance in a subnet whose NACL denies all egress. **Severity:** Informational / Low (enabler; raises severity of a chained exfil finding). **Stop:** mapping is the deliverable.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Open a locked-down subnet by editing rule content under a "restrictive" policy | ReplaceNetworkAclEntry / CreateNetworkAclEntry | IAM resource/tag/VPC scoping — **but no rule-content condition key** (F5) |
| Bypass entry-edit restriction by swapping the subnet's NACL | ReplaceNetworkAclAssociation | Separate IAM action; policies often govern only the entry action (Area 2) |
| Account-wide NACL rewrite from a copy-verbatim AWS policy | HyperPod `AmazonVPCFullAccess` Sid | None — `Resource:"*"`, no Condition (Area 3) |
| Pre-authorize a specific created NACL ID | CreateNetworkAcl + `ec2:NetworkAclID` | Key silently resolves to `*` (Area 4a) |
| Pin association to one VPC with a single ec2:Vpc condition | ReplaceNetworkAclAssociation | Multi-resource condition pitfall; needs per-Resource statements (Area 4b) |
| Satisfy a tag gate by self-tagging the NACL | CreateTags on network-acl | `aws:RequestTag`/`aws:TagKeys` exist but are opt-in (Area 5) |
| Overwrite the implicit final deny (rule 32767) with allow | ReplaceNetworkAclEntry | Input-range validation (documented only on Create) — unverified on Replace (Area 6) |
| Exfiltrate via IMDS/DNS/ECS-metadata despite deny-all NACL | data-plane | NACLs structurally cannot filter these (Area 7) |
| Read another principal's/team's NACLs | DescribeNetworkAcls | No resource-level read scoping; account-bounded only (Area 4/F2) |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-account NACL access** via a foreign `acl-*` id — the `network-acl` ARN embeds the account; a foreign id will not resolve. Genuine null, do not pursue.
- **Customer-authored over-broad policies** (e.g., a customer writing `ec2:ReplaceNetworkAclEntry` on `Resource:"*"`) — a customer least-privilege footgun, out of scope. (The AWS-*authored* HyperPod policy in Area 3 is the carve-out and **is** in scope.)
- **Single-tenant self-DoS** — the documented batched add/delete race (`nacl-rules.md:27`) and rule-quota exhaustion (`amazon-vpc-limits.md:64-65`, default 20/direction adjustable to 40, 200 NACLs/VPC). Record only.
- **IMDS on managed hosts, DNS/DHCP/Time-Sync non-filtering** — documented platform behavior, not a NACL defect (informational enabler only, Area 7).
- Memory-safety / wire-protocol / injection / SSRF / upload / KMS / OAuth / JWT / cache / attestation classes — **no corresponding surface** in this family (see Section 8 null hypotheses with pages checked).

---

## 8. Null Hypotheses / Doc Gaps (lenses that did not fire — pages checked named)

- **Lens A (cross-tenant IDOR):** null for cross-account (ARN embeds account, `list_ec2.md:9977`). *Intra-account* cross-VPC/cross-team reach IS possible but only via an over-broad `Resource:"*"` policy — surfaced as Areas 1–3, not a server authz defect. Checked: all six action rows + `DescribeNetworkAcls`.
- **Lens G (SSRF):** N/A — no field in any of the 10 NACL API pages is dereferenced server-side (no URL/URI/host/endpoint/webhook/import). Checked: all `API_*NetworkAcl*.md` request-parameter sections.
- **Lens Q (upload):** N/A — no blob/file/image/attachment parameter. Checked: same pages.
- **Lens K (prompt injection):** N/A — no LLM/agent in pipeline.
- **Lens B/C (PassRole / credential vending):** N/A — no role-ARN/token/session input in any NACL action. Checked: request params of all six.
- **Lens H/W (KMS / attestation):** N/A — no encryption-context/KMS/PCR surface.
- **Lens J/FF (OAuth / JWT):** N/A — pure SigV4.
- **Lens DD/BB/CC (cache / canonicalization / trusted-upstream header):** N/A — single EC2 API hop, no authorizer/CDN/proxy chain in this family.
- **Lens EE (predictable-name land-grab):** N/A — NACL ids are AWS-assigned `acl-*`, not a customer/global namespace; no "created on first use by name" behavior. Checked: `CreateNetworkAcl` + resource-type table.
- **Lens AA (share/revoke):** N/A — **no RAM/sharing capability for NACLs** exists in the mirror (contrast: `security-group-sharing.md` exists, no `network-acl-sharing.md`). Checked: `vpc` userguide file listing.
- **Lens Y (transport/sig):** inherits standard EC2 endpoint TLS/SigV4; nothing NACL-specific. Not pursued.
- **Doc gaps to confirm empirically first:** (i) whether `ReplaceNetworkAclEntry` enforces the 1–32766 `RuleNumber` bound (Area 6 — doc silent); (ii) whether NACL↔subnet association is hard-bounded to the same VPC (no explicit prose guarantee for this action, unlike the explicit same-VPC/Region statement AWS wrote for security groups at `security-group-assoc.md:16` — architecturally implied by fixed `vpcId` fields but uncited). Mark both "doc-gap — confirm surface first."

---

### Appendix — Kill-chain note
The sharpest chain here is **Area 2 → Area 1**: a principal intended to be read-only-ish but holding `ReplaceNetworkAclAssociation` (e.g., via the Area 3 wildcard policy) re-points a sensitive subnet onto an attacker-controlled permissive NACL (Area 2), whose rule content IAM cannot bound (Area 1), fully opening the subnet — then, if a compromised host sits there, exfil proceeds via IMDS/metadata regardless of any residual deny (Area 7). Rate at the chain end: effective account-wide subnet-firewall control = **High** within the account.
