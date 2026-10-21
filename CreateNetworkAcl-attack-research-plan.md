# EC2 `CreateNetworkAcl` — Attack Research Plan

**Source of leads:** Local mirror `/work/aws-docs` + live `docs.aws.amazon.com`. Anchor page: `https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkAcl.html` (and `.md`). Primary evidence:
- `docs/AWSEC2/latest/APIReference/` : `API_CreateNetworkAcl.md`, `API_CreateNetworkAclEntry.md`, `API_ReplaceNetworkAclAssociation.md`, `API_ReplaceNetworkAclEntry.md`, `API_DeleteNetworkAcl.md`, `API_NetworkAcl.md`, `API_TagSpecification.md`
- `docs/service-authorization/latest/reference/list_ec2.md` (authoritative IAM action/condition-key/resource tables — lines **5326–5330** CreateNetworkAcl rows; **9977** network-acl ARN; **10022** vpc ARN)
- `docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md` (lines **270, 302, 310** — `ec2:{Resource}ID` resolve-to-`*` rule; `ec2:NetworkAclID`/`ec2:VpcID` membership)
- `docs/vpc/latest/userguide/` : `vpc-network-acls.md`, `default-network-acl.md`, `custom-network-acl.md`, `network-acl-associations.md`, `amazon-vpc-limits.md`
- **Sibling plan (read it — full-family coverage):** `/work/aws-docs/ReplaceNetworkAclEntry-attack-research-plan.md` covers the entry/association/delete actions; this plan goes deep on the **creation** action and cross-references rather than duplicating.

**Status:** Documentation-derived hypotheses only. Nothing tested against a live AWS account. Every lead is falsifiable with a stated oracle; a hunter must confirm empirically in an authorized, disposable account.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order (§5). Look left and right for adjacent bugs in the NACL family.
- **Scope reality.** `CreateNetworkAcl` is a **mutating, control-plane** EC2 action. It creates one empty, *non-default*, *unassociated* custom NACL inside a VPC the caller names. Creation alone changes **no** firewall posture (a custom NACL denies-all but affects nothing until associated — `default-network-acl.md`, `custom-network-acl.md`). Its security value is therefore (a) as **step 1 of a subnet-firewall-rewrite kill chain**, (b) **IAM authorization-granularity / least-privilege scoping gaps** unique to the create path, and (c) **tag-on-create ABAC self-widening**. The `network-acl` ARN embeds the account (`arn:${Partition}:ec2:${Region}:${Account}:network-acl/${NaclId}`, line 9977) → **cross-account is a genuine null hypothesis** (§8).
- **HARD STOP:** the instant any evidence shows an identity/credential/ARN/account belonging to AWS's **own service plane**, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected for this pure customer-plane action, but the rule stands.)
- **Read-only / dummy-data discipline:** confirm the existence of a gap, never exploit beyond it. Operate only in a disposable test VPC you own, with synthetic subnets, and tear down every NACL/association/tag you create.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **VPC-scoping escape at create:** Prove a principal the policy author intended to confine to one VPC can `CreateNetworkAcl` in a *different* same-account VPC because the only create-time VPC key is `ec2:VpcID` (string on the `vpc*` leg) — and a policy that reuses the family's `ec2:Vpc` (ARN) pattern, or writes it on the wrong leg, silently fails to scope.
2. **Resource-ID pre-scoping no-op:** Prove that `ec2:NetworkAclID` on `CreateNetworkAcl` cannot pin the created NACL's ID (it resolves to `*` at runtime), so a policy that tries to constrain *which* NACL may be created is vacuous.
3. **Tag-on-create ABAC self-widening:** Prove that `TagSpecification` on `CreateNetworkAcl` lets a caller stamp a governance/gating tag onto the NACL **at birth**, so the fresh NACL immediately satisfies a downstream `aws:ResourceTag`-gated `CreateNetworkAclEntry` / `ReplaceNetworkAclAssociation` — ABAC defeated without ever calling `CreateTags`.
4. **Kill-chain step 1:** Prove that `CreateNetworkAcl` + `CreateNetworkAclEntry` + `ReplaceNetworkAclAssociation` (no entry-edit permission on any *existing* NACL required) lets a principal mint a fully-permissive NACL and swap a sensitive subnet onto it — reshaping that subnet's firewall while holding zero authority over the subnet's original NACL.
5. **Creation-time anti-abuse integrity:** Determine whether `aws:RequestTag`/`aws:TagKeys` gating at create is default-safe (it is opt-in), and whether the `ClientToken` idempotency path can be abused to confuse automation (replay returns a prior NACL).
6. **Quota / self-DoS mapping:** Document the 200-NACLs-per-VPC default quota as a single-tenant self-DoS ceiling (out of scope, recorded for completeness).

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 Query/JSON API over HTTPS (`https://ec2.<region>.amazonaws.com/`), SigV4 IAM auth, API version `2016-11-15`. Reached via CLI (`aws ec2 create-network-acl`), PowerShell (`New-EC2NetworkAcl`), all SDKs, console. **No** non-SDK/internal endpoint in this family.

**The managed asset created.** A **network ACL (NACL)** — a stateless, subnet-level, ordered packet filter (ingress set + egress set, lowest-number-first, first-match-wins, uneditable implicit final deny at rule 32767/32768). `CreateNetworkAcl` always produces a **non-default** NACL (`<default>false</default>` in the sample response), initially **empty of customer rules** (only the implicit final-deny pair for IPv4 and IPv6) and **unassociated** with any subnet.

**Request parameters (the entire create surface):**
- `VpcId` **(required)** — the VPC to create the NACL in. Account-bounded.
- `TagSpecification.N` (optional) — tags to assign to the new NACL *at creation* → **the ABAC primitive** (§5 Area 3).
- `ClientToken` (optional) — idempotency token (§5 Area 5).
- `DryRun` (optional) — permission probe; returns `DryRunOperation`/`UnauthorizedOperation`. **Treat as caller-IAM-only, NOT an ownership/existence oracle** (evaluated before resource resolution).

**Exact IAM authorization shape (`list_ec2.md:5326–5330`):**

| Required leg | Resource ARN | Condition keys available on this leg |
|---|---|---|
| `network-acl*` (the resource *being created*) | `arn:${Partition}:ec2:${Region}:${Account}:network-acl/${NaclId}` | `aws:RequestTag/${TagKey}`, `aws:TagKeys`, **`ec2:NetworkAclID`**, `ec2:Region` |
| `vpc*` (the *source* VPC) | `arn:${Partition}:ec2:${Region}:${Account}:vpc/${VpcId}` | `aws:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:Tenancy`, **`ec2:VpcID`** |

Decisive design facts:
- **`ec2:NetworkAclID` on `CreateNetworkAcl` resolves to `*` at runtime** (`iam-policies-for-amazon-ec2.md:270`: "If you specify a different value, the condition always resolves to `*` during runtime"; line 302 lists `ec2:NetworkAclID – CreateNetworkAcl` in this class). You cannot constrain *which* NACL id is created.
- **The `network-acl*` leg exposes no `ec2:Vpc` and no `ec2:ResourceTag`** for this action (the resource doesn't exist yet). VPC confinement is only expressible on the **`vpc*` leg via `ec2:VpcID`** (a *string* key), **not** `ec2:Vpc` (the ARN key used by the sibling actions `CreateNetworkAclEntry`/`ReplaceNetworkAclEntry`). A policy author who standardises on `ec2:Vpc` across the family mis-scopes create.
- **Tag gating at create is opt-in** via `aws:RequestTag`/`aws:TagKeys` on the `network-acl*` leg; absent those conditions, the caller chooses tags freely.

**Pipeline (control-plane only):**

```
Principal (SigV4) ──► EC2 API frontend ──► IAM authz ──► NACL store
                                             │  (authorizes by: action +
                                             │   vpc* leg [ec2:VpcID / VPC tags] +
                                             │   network-acl* leg [RequestTag/TagKeys];
                                             │   CANNOT pin created NaclId → ec2:NetworkAclID=*)
                                             ▼
                         new non-default, empty, UNASSOCIATED NACL  (benign until...)
                                             │
            ┌────────────────────────────────┴───────────────────────────────┐
            ▼ CreateNetworkAclEntry (rule content IAM can't bound)             ▼ ReplaceNetworkAclAssociation (swap subnet)
       permissive allow 0.0.0.0/0:*                                   subnet's effective firewall = attacker NACL
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Principal intended to be confined to VPC-A | A different same-account VPC-B | `CreateNetworkAcl` whose VPC leg is scoped (or mis-scoped) by `ec2:VpcID`/`ec2:Vpc` | A NACL is created in VPC-B under a policy the author believed confined creation to VPC-A. |
| Policy author's intent ("only NACL `acl-X`") | Actual created-resource scope | `ec2:NetworkAclID` condition on `CreateNetworkAcl` | Create succeeds for *any* new id — the condition resolved to `*`. |
| Principal with downstream `aws:ResourceTag`-gated NACL mutation | The ABAC gate | `TagSpecification` on `CreateNetworkAcl` (stamp gate tag at birth) | A freshly-created NACL already carries the gating tag → passes a gate it was never meant to satisfy, with no `CreateTags` call. |
| Principal with **no** authority over subnet S's current NACL | Subnet S's effective firewall | `CreateNetworkAcl` → `CreateNetworkAclEntry` → `ReplaceNetworkAclAssociation` | Subnet S's packet filter is replaced by an attacker-minted NACL. |
| Principal in account X | VPC `vpc-*` in account Y | `CreateNetworkAcl` with foreign `VpcId` | **Genuine null** — the `vpc*` leg ARN embeds the account; a foreign VPC id will not resolve. Record, do not pursue. |
| Any customer surface | AWS service plane | — | **HARD STOP** if ever reached. Not expected here. |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Facing | Required IAM resource(s) | Content/ID-scopable? | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| **CreateNetworkAcl** *(target)* | Query/SDK | **Yes** | External | `network-acl*` **and** `vpc*` | VPC-leg only via `ec2:VpcID`; **created id NOT scopable** (`ec2:NetworkAclID`→`*`) | `ec2:CreateNetworkAcl` | Tag-on-create (`TagSpecification`); `ClientToken` idempotent. Produces empty, non-default, unassociated NACL. |
| CreateNetworkAclEntry | Query/SDK | **Yes** | External | `network-acl*` | **No rule-content key** (allow/deny/CIDR/port/proto/ruleNumber all unconstrainable) | `ec2:CreateNetworkAclEntry` | Conds: `aws:ResourceTag`,`ec2:NetworkAclID`,`ec2:Region`,`ec2:ResourceTag`,`ec2:Vpc`. See sibling plan Area 1. |
| ReplaceNetworkAclAssociation | Query/SDK | **Yes** | External | `network-acl*` **and** `subnet*` | n/a | `ec2:ReplaceNetworkAclAssociation` | Swaps a subnet's NACL. Chain terminus (step 3). See sibling plan Area 2/4b. |
| ReplaceNetworkAclEntry / DeleteNetworkAclEntry / DeleteNetworkAcl | Query/SDK | **Yes** | External | `network-acl*` | No rule-content key | respective `ec2:*` | Covered in sibling plan. |
| DescribeNetworkAcls | Query/SDK | No | External | none (only `ec2:Region`) | n/a | `ec2:DescribeNetworkAcls` | No resource-level read scoping; account-bounded. Sibling plan F2. |

No `[NEW]` markers, no non-SDK/internal endpoint, no undocumented auth-weakening enum. The create action's value is the **authorization-granularity delta** and its **kill-chain position**, not surface discovery.

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — Create→Entry→Associate kill chain: mint-and-swap a subnet firewall *(highest value; Lens X + kill chain)*
**Background.** Three independent IAM actions, each coarsely authorized, compose into full control of a subnet's effective firewall without ever touching the subnet's *original* NACL: `CreateNetworkAcl` (mint an empty NACL in the VPC), `CreateNetworkAclEntry` (write rules — IAM cannot bound their content, sibling Area 1), `ReplaceNetworkAclAssociation` (point subnet S at the new NACL, sibling Area 2).
**Security Concern.** A least-privilege design that carefully locks down `ReplaceNetworkAclEntry`/`DeleteNetworkAclEntry` on the *production* NACLs does nothing if the same principal holds the three creation/association verbs: it simply builds a parallel permissive NACL and re-points the subnet. Creation looks innocuous in a policy review ("they can only *create* NACLs") precisely because an unassociated NACL is inert — the danger is latent until the association verb fires.
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* A principal holding exactly `ec2:CreateNetworkAcl`, `ec2:CreateNetworkAclEntry`, `ec2:ReplaceNetworkAclAssociation` (scoped only by VPC/region, no authority over subnet S's current NACL) can give subnet S a NACL that allows `0.0.0.0/0` on all ports inbound+outbound. → *Oracle:* in an owned test VPC, run the three calls; `DescribeNetworkAcls` shows subnet S associated with the attacker NACL and the permissive rule present. → *Severity:* **High** (effective subnet-firewall takeover within the account).
- *Claim:* The reverse — create an all-deny NACL and swap a subnet onto it — is a one-principal **availability** attack on that subnet (DoS), again without entry-edit rights on the original.
**Doc evidence:** `list_ec2.md:5326–5336, 9419–9429`; `API_CreateNetworkAcl.md`, `API_CreateNetworkAclEntry.md`, `API_ReplaceNetworkAclAssociation.md`; sibling plan Areas 1–2. **Stop condition:** once one end-to-end chain succeeds in an owned VPC, the composition is proven; do not enumerate rule variants.

### Area 2 — VPC-scoping at create: `ec2:VpcID` (string) not `ec2:Vpc` (ARN) *(Lens S)*
**Background.** The only create-time VPC confinement key is **`ec2:VpcID`** on the `vpc*` leg (`list_ec2.md:5329`; `iam-policies-for-amazon-ec2.md:310` lists it as a resource-result key for `CreateVpc`). The sibling family actions (`CreateNetworkAclEntry`, `ReplaceNetworkAclEntry`) scope by **`ec2:Vpc`** (the ARN key). A policy author standardising on one pattern across the family will use the wrong key for create.
**Security Concern.** Two concrete traps: (2a) a policy that reuses `ec2:Vpc` (ARN) to confine `CreateNetworkAcl` writes a key **not evaluated** for this action → no confinement (fail-open to all same-account VPCs). (2b) `ec2:VpcID` is a *resource-ID result* key class — confirm whether, for `CreateNetworkAcl`, it genuinely pins the *source* VPC or (like `ec2:NetworkAclID`) degrades to `*`; the "source resource vs resulting resource" distinction in `iam-policies-for-amazon-ec2.md:270` is the hinge (VpcId is a *source* input here, so it *should* bind — but this must be verified, not assumed).
**High-level Test Scenarios:**
- *Claim (2a):* A policy `Allow ec2:CreateNetworkAcl` with `Condition: {StringEquals: {ec2:Vpc: arn:...:vpc/vpc-A}}` still permits creating a NACL in vpc-B. → *Oracle:* `iam:SimulatePrincipalPolicy` for `CreateNetworkAcl` on the vpc-B ARN under that policy → `allowed`; then a live scoped call on owned vpc-B confirms. → *Severity:* **Low–Medium** (least-privilege scope broader than written).
- *Claim (2b):* A policy using `ec2:VpcID: vpc-A` on the vpc leg correctly denies creation in vpc-B (i.e., VpcID binds the source) — refuting 2b. If instead create in vpc-B succeeds, the source-VPC key also degrades → scoping of create is **unexpressible**, raising severity to Medium.
**Doc evidence:** `list_ec2.md:5329`; `iam-policies-for-amazon-ec2.md:270, 302, 310`. **Stop:** one simulate+live result per sub-case.

### Area 3 — Tag-on-create ABAC self-widening at birth *(Lens I / S — create-path-specific)*
**Background.** `CreateNetworkAcl` accepts `TagSpecification.N` and exposes `aws:RequestTag/${TagKey}` + `aws:TagKeys` on the `network-acl*` leg (`list_ec2.md:5328`). Downstream NACL mutations (`CreateNetworkAclEntry`, `ReplaceNetworkAclEntry`, `ReplaceNetworkAclAssociation`) can be gated on `aws:ResourceTag/${TagKey}`.
**Security Concern.** If an org gates NACL mutation on e.g. `aws:ResourceTag/Env=sandbox` but does **not** constrain `CreateNetworkAcl` with an `aws:RequestTag`/`aws:TagKeys` condition, a caller can create a NACL **already carrying `Env=sandbox`** via `TagSpecification` — the resource satisfies the downstream gate from the moment it exists. Unlike the sibling plan's Area 5 (which needs a separate `CreateTags` call on an existing NACL), this variant needs **no** `CreateTags` permission at all: the gate is self-satisfied at birth. It also sidesteps any `aws:TagKeys` lock on `CreateTags`, because the tag enters through the create verb, not the tagging verb.
**High-level Test Scenarios:**
- *Claim:* With `CreateNetworkAcl` unconstrained by `aws:RequestTag`/`aws:TagKeys`, and `CreateNetworkAclEntry`/`ReplaceNetworkAclAssociation` gated on `aws:ResourceTag/Env=sandbox`, a caller creates `acl-new` with `TagSpecification Env=sandbox` and then mutates/associates it — the gate never blocks. → *Oracle:* run the sequence in an owned account; the entry write on the self-tagged NACL that would be denied on an untagged NACL succeeds. → *Severity:* **Medium** (ABAC bypass → effectively unscoped NACL provisioning; **High** where that tag is the sole control separating prod from sandbox NACLs and feeds the Area 1 chain).
- *Adjacent:* confirm whether `aws:RequestTag` enforcement at create (deny create unless a required tag/value is present) is the intended mitigation, and whether it is actually applied in any AWS-authored sample policy (cross-ref sibling plan Area 3 HyperPod artifact — it grants `CreateNetworkAcl` on `Resource:"*"` with **no** condition, so the mitigation is absent there).
**Doc evidence:** `list_ec2.md:5328`; `API_CreateNetworkAcl.md` (TagSpecification); sibling plan Area 3/5. **Stop:** once the self-tag-at-birth → downstream-gate-pass chain succeeds once.

### Area 4 — `ec2:NetworkAclID` pre-scoping is a no-op at create *(Lens S — silent condition-key degradation)*
**Background.** `iam-policies-for-amazon-ec2.md:270` states the `ec2:{Resource}ID` keys used with a *creating* API "specify the resulting resource" and "if you specify a different value, the condition always resolves to `*`"; line 302 lists `ec2:NetworkAclID – CreateNetworkAcl`.
**Security Concern.** A policy author who writes `Condition: {StringEquals: {ec2:NetworkAclID: acl-approved}}` on `CreateNetworkAcl` believing it limits *which* NACL can be created is wrong — the key resolves to `*`, so creation of **any** NACL is permitted. The false sense of constraint is the defect (an auditor may sign off a policy that is actually unscoped on the created resource).
**High-level Test Scenarios:**
- *Claim:* `CreateNetworkAcl` with `ec2:NetworkAclID` pinned to a specific id still permits creating a NACL (which necessarily gets a different, AWS-assigned id). → *Oracle:* `SimulatePrincipalPolicy` → `allowed` regardless of the pinned id; live create confirms a differently-id'd NACL is produced. → *Severity:* **Low** (documented-but-surprising scoping ceiling; informational hardening note).
**Doc evidence:** `iam-policies-for-amazon-ec2.md:270, 302`; `list_ec2.md:5328`. **Stop:** one simulate result settles it.

### Area 5 — `ClientToken` idempotency & creation anti-abuse robustness *(Lens P / U — low)*
**Background.** `CreateNetworkAcl` accepts a `ClientToken` for idempotency (`API_CreateNetworkAcl.md`). A replayed token returns the originally-created NACL rather than creating a new one.
**Security Concern (open questions, doc-silent on edge behaviour):** (a) Can a caller influence or collide another automation's idempotency result by replaying/guessing a `ClientToken`, causing a workflow to associate a subnet to an unexpected (prior) NACL? Tokens are caller-chosen free strings — collision within one account's automation is plausible if tokens are non-random. (b) Does idempotency scope to the *account* or to the *principal* — can principal B replay principal A's token to retrieve A's NACL id (an intra-account disclosure/confusion oracle)? (c) Creation quota: 200 NACLs per VPC (`amazon-vpc-limits.md`) — mass creation is a **single-tenant self-DoS**, recorded as out-of-scope.
**High-level Test Scenarios:**
- *Claim:* Replaying a `ClientToken` previously used by a different same-account principal returns that principal's NACL id/details. → *Oracle:* principal A creates with token T; principal B (holding `CreateNetworkAcl`) replays token T → observe whether B receives A's `networkAclId`. → *Severity:* **Low** (intra-account info/automation confusion; not a cross-account boundary).
**Doc evidence:** `API_CreateNetworkAcl.md` (ClientToken, idempotency); `amazon-vpc-limits.md`. **Stop:** one replay observation per sub-case.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Mint-and-swap: build a permissive NACL and re-point a subnet onto it | CreateNetworkAcl → CreateNetworkAclEntry → ReplaceNetworkAclAssociation | IAM per-action resource scoping — but the three verbs are independent and creation is inert-looking (Area 1) |
| Create a NACL in a VPC the policy meant to exclude | CreateNetworkAcl + `ec2:Vpc` (wrong key) / `ec2:VpcID` | Only `ec2:VpcID` is evaluated at create; `ec2:Vpc` is not wired to this action (Area 2) |
| Satisfy a downstream `aws:ResourceTag` gate by tagging the NACL at birth | CreateNetworkAcl `TagSpecification` | `aws:RequestTag`/`aws:TagKeys` exist but are opt-in and often omitted (Area 3) |
| Pre-authorize a specific created NACL id | CreateNetworkAcl + `ec2:NetworkAclID` | Key silently resolves to `*` — constraint is vacuous (Area 4) |
| Confuse automation / disclose a peer principal's NACL via idempotency | CreateNetworkAcl `ClientToken` | Idempotency scoping undocumented for edge cases (Area 5) |
| Exhaust the 200-NACL/VPC quota | CreateNetworkAcl | Adjustable quota; single-tenant self-DoS only (out of scope, §7) |
| Create a NACL in a foreign account's VPC | CreateNetworkAcl | `vpc*` leg ARN embeds account → foreign id won't resolve (null, §7) |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-account** NACL creation via a foreign `vpc-*` id — the `vpc*` leg ARN embeds the account (`list_ec2.md:10022`). Genuine null; do not pursue.
- **Customer-authored over-broad policies** (a customer granting `ec2:CreateNetworkAcl` on `Resource:"*"`) — a customer least-privilege footgun, out of scope. *Carve-out:* the **AWS-authored** SageMaker HyperPod prerequisites policy that grants the full NACL mutation set (including `CreateNetworkAcl`) on `Resource:"*"` with no condition **is** in scope — see sibling plan **Area 3** (Tier-2 disclosure, route `aws-security`). Do not re-file; reference it.
- **Single-tenant self-DoS** — mass NACL creation vs the 200/VPC quota (`amazon-vpc-limits.md`). Record only.
- **IMDS/DNS/DHCP/ECS-metadata/Time-Sync non-filtering** — a *consequence* of any NACL (the created one included) that matters only when chained with an exfil finding; documented platform behaviour, not a create-action defect (sibling plan Area 7).
- **Injection / memory-safety / SSRF / upload / KMS / OAuth / JWT / cache / canonicalization / attestation / prompt-injection classes** — **no corresponding surface** in `CreateNetworkAcl` (no URL/blob/role-ARN/token/parser/LLM/encryption input). See §8 with pages checked.

---

## 8. Null Hypotheses / Doc Gaps (lenses that did not fire — pages checked named)

- **Lens A (cross-tenant IDOR):** null for cross-account (both legs' ARNs embed the account, `list_ec2.md:9977, 10022`). Intra-account cross-VPC reach is possible only via an over-broad / mis-scoped policy → surfaced as Areas 1–2, not a server authz defect. Checked: `CreateNetworkAcl` action rows + both resource-type rows.
- **Lens B/C (PassRole / credential vending):** N/A — no role-ARN/token/session input. Checked: `API_CreateNetworkAcl.md` request parameters (VpcId, TagSpecification, ClientToken, DryRun only).
- **Lens G (SSRF):** N/A — no field dereferenced server-side (no URL/URI/host/endpoint). Checked: `API_CreateNetworkAcl.md` request params.
- **Lens Q (upload):** N/A — no blob/file/image parameter. Checked: same page.
- **Lens K (prompt injection):** N/A — no LLM/agent in pipeline.
- **Lens H/W (KMS / attestation):** N/A — no encryption-context/KMS/PCR surface.
- **Lens J/FF (OAuth / JWT):** N/A — pure SigV4.
- **Lens BB/CC/DD (canonicalization / trusted-upstream header / cache):** N/A — single EC2 API hop, no authorizer/CDN/proxy chain.
- **Lens EE (predictable-name land-grab):** N/A — the created NACL id is AWS-assigned `acl-*` (`API_CreateNetworkAcl.md` sample response `acl-5fb85d36`), not a customer/global namespace; no "created on first use by name" behaviour. (Note: `ec2:NetworkAclID`→`*` means the caller cannot even choose the id — Area 4.)
- **Lens AA (share/revoke):** N/A — **no RAM/sharing capability for NACLs** exists in the mirror (no `network-acl-sharing.md`; contrast `security-group-sharing.md`). A created NACL cannot be shared cross-account.
- **Lens Y (transport/sig):** inherits standard EC2 endpoint TLS/SigV4; nothing `CreateNetworkAcl`-specific. Not pursued.
- **Doc gaps to confirm empirically first:** (i) whether `ec2:VpcID` genuinely binds the *source* VPC at create (Area 2b — the source-vs-result-resource distinction in `iam-policies-for-amazon-ec2.md:270` implies it should, but it is uncited for this specific action); (ii) the account-vs-principal scope of `ClientToken` idempotency (Area 5 — doc-silent). Mark both "doc-gap — confirm surface first."

---

### Appendix — Kill-chain note
`CreateNetworkAcl` is the *quiet* first move. Area 3 (self-tag at birth) satisfies any `aws:ResourceTag` gate on the entry/association verbs; Area 1 then mints a permissive NACL (rule content IAM cannot bound — sibling Area 1) and `ReplaceNetworkAclAssociation` swaps a sensitive subnet onto it; if a compromised host sits in that subnet, exfil proceeds via IMDS/DNS/metadata regardless of any residual deny (sibling Area 7). Rate at the chain end: **effective subnet-firewall takeover within the account = High.** The create action's distinctive contribution is that policy reviewers under-weight it — "can only create NACLs" reads as harmless, which is exactly why it is the softest entry to the chain.
