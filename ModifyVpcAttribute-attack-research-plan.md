# EC2 `ModifyVpcAttribute` (VPC DNS / NAU Attribute Control Surface) — Attack Research Plan

**Source of leads:** Target doc page `https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ModifyVpcAttribute_section.html` (SDK/CLI + PowerShell code example) plus the mechanism it exercises. Fetched live from `docs.aws.amazon.com` on 2026-10-19 (both `.html` and `.md` variants) and cross-checked against the offline mirror at `/work/aws-docs`. The target example page itself was **absent** from the local mirror (a sync gap — read online only); the EC2 API reference (`API_ModifyVpcAttribute`, `API_DescribeVpcAttribute`, `API_ModifyVpcPeeringConnectionOptions`), the VPC User Guide DNS pages, and the Service Authorization Reference (`list_ec2.md`) were verified online == mirror.
**Status:** documentation-derived hypotheses only; **nothing has been tested against a live AWS account.** This is the plan a hunter executes later against an account they are authorized to test.
**Analysis:** 4 passes — primary surface (this doc + API refs), IAM/condition-key enforcement deep-dive, DNS availability/blast-radius deep-dive, action-family-parity/cross-account deep-dive (3 subagents + main agent synthesis).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to AWS's **own service plane**, stop, preserve evidence, flag for AWS-Security disclosure. *Note: this surface is entirely account-scoped VPC configuration + IAM — no service-plane reach is expected. If one appears, it is a surprise worth stopping for.*
- **Methodology caveat used throughout:** `DryRun` on these actions is a caller-IAM pre-flight check (`DryRunOperation` vs `UnauthorizedOperation`) evaluated **before** resource-state resolution. It is **not** an ownership/existence oracle. Only non-dry-run outcomes are valid oracles on this surface.
- **Condition-key casing caveat:** several leads turn on the exact string EC2 synthesizes into the `ec2:Attribute` / `ec2:Attribute/${AttributeName}` context keys for a *named-boolean* action (this action has no generic `Attribute`+`Value` request pair, unlike `ModifyImageAttribute`). AWS documents no worked example for this action; bisecting the real runtime string is itself a deliverable.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Cross-account VPC attribute mutation** — flip `enableDnsSupport`/`enableDnsHostnames` on a VPC owned by *another account* by naming its `vpc-…` id → Critical if it succeeds. *(Expected to fail — per-account `vpc` resource-ARN model — but it is the headline objective the IDOR/enumeration leads probe around.)*
2. **Silent Deny-bypass via condition-key semantics** — achieve a DNS-attribute change that a reasonable, correctly-intentioned customer `Deny` (keyed on `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:VpcID`, or `ec2:Tenancy`) was written to block, because the key is case-mismatched, value-unpinnable, or never populated for this action. **This is the primary research thrust.**
3. **Low-privilege → account-wide DNS outage** — as a principal holding only `ec2:ModifyVpcAttribute` (no compute/network delete rights), disable name resolution for an entire production VPC with one synchronous call, breaking PrivateLink private DNS, Route 53 private hosted zones, EFS/RDS/MSK/OpenSearch/EKS name resolution.
4. **AWS-managed-policy blast-radius** — show a principal holding a common AWS-managed policy (`NetworkAdministrator`, `PowerUserAccess`, `AmazonEC2FullAccess`) wields `ec2:ModifyVpcAttribute` unconditionally on `Resource:"*"`, defeating any assumption that the policy name implies VPC scoping.
5. **Cross-account peering DNS confused-deputy** — via the adjacent `ModifyVpcPeeringConnectionOptions`, have one account toggle DNS-resolution exposure affecting the peer without the peer's consent.
6. **ABAC self-widening** — a principal with broad `ec2:CreateTags` on VPCs sets the very tag a `ModifyVpcAttribute` ABAC `Allow` keys on, self-escalating into attribute-modify rights.

---

## 2. Components, Assets, and Design

**What this is.** The target page is a *code example* (AWS CLI + Tools for PowerShell V4/V5) for the EC2 control-plane action **`ModifyVpcAttribute`**, which sets three VPC-level boolean attributes. There is no new service, no fleet, no data plane, no parser, no untrusted-content path — the request carries only a `vpc-…` id and one `AttributeBooleanValue {Value: bool}`. The attack surface is the **VPC DNS/NAU attribute control cluster** and, dominantly, its **IAM authorization semantics** and **availability blast radius**.

**Customer-facing interface.** EC2 Query/JSON control-plane API over HTTPS (`ec2.<region>.amazonaws.com`), API version `2016-11-15`, SigV4 IAM auth. Also reachable via `Edit-EC2VpcAttribute` (PowerShell) and `modify-vpc-attribute` (CLI). No non-SDK/internal endpoints; no console-hidden auth-weakening knob found (all three attributes are console-exposed).

**The three attributes (assets):**
| Attribute (API field, PascalCase) | Prose/console name (camelCase) | Default | Effect of `false` |
|---|---|---|---|
| `EnableDnsSupport` | `enableDnsSupport` | `true` | Route 53 Resolver (169.254.169.253 / VPC+2) stops resolving Amazon-provided private DNS; PrivateLink private DNS + Route 53 private hosted zones break |
| `EnableDnsHostnames` | `enableDnsHostnames` | `false` (`true` for default VPC) | instances with public IPs get no public DNS hostname |
| `EnableNetworkAddressUsageMetrics` | `enableNetworkAddressUsageMetrics` | (off) | NAU CloudWatch metric stops emitting (monitoring only; quota enforcement unaffected) |

Constraints (doc-stated): *"You cannot modify the DNS resolution and DNS hostnames attributes in the same request"*; *"You can only enable DNS hostnames if you've enabled DNS support."* If **at least one** of the two DNS attributes is `false`, Amazon-provided private/public DNS resolution fails VPC-wide.

**Resource & identifier shape.** Resource = EC2 **VPC**, ARN `arn:${Partition}:ec2:${Region}:${Account}:vpc/${VpcId}`. `VpcId` = `vpc-` + 8 or 17 **lowercase hex** chars — no documented checksum, but the ARN is **account-scoped**, so a foreign id is confirmable-if-known, not cross-account actionable. Casing is not a realistic sub-vector for the id itself (always lowercase hex).

**Identity / privilege.** Pure SigV4 IAM, standard per-account evaluation. No roles assumed, no STS vending, no credential chaining, no hidden admin identity, no multi-tenant shared fleet. Authorization is: (identity policy ∧ SCP ∧ permission boundary) on action `ec2:ModifyVpcAttribute`, resource `vpc*`.

**Asset at risk = availability (name resolution) + policy-enforcement integrity.** There is no spend, no data exfil, no cross-tenant fleet here. The crown jewels are (a) *account-wide DNS availability* (one call can break it) and (b) the *correctness of a customer's own guardrail policy* (whether a Deny they wrote actually fires).

**ASCII surface map:**
```
                          ┌──────────────────────────────────────────────────────────┐
  IAM principal ──SigV4──►│ EC2 control plane (ec2.<region>.amazonaws.com, 2016-11-15) │
  (caller in account A)   │                                                            │
                          │  ModifyVpcAttribute        [vpc* , Write]                  │
                          │    └─ VpcId + one of {EnableDnsSupport|EnableDnsHostnames| │
                          │        EnableNetworkAddressUsageMetrics}=AttributeBoolean  │
                          │    cond keys: ec2:Attribute, ec2:Attribute/${AttrName},    │
                          │               ec2:VpcID, ec2:Tenancy, ec2:Region, *:Tag    │
                          │  DescribeVpcAttribute      [vpc* , List]  (NO ec2:Attribute)│
                          │  ModifyVpcPeeringConnectionOptions [vpc-peering-conn*,Write]│
                          │    └─ Allow(Egress)DnsResolutionFromRemoteVpc  ──► ACCOUNT B│
                          └───────────────────────────┬──────────────────────────────┘
                                                       │ sets enableDnsSupport=false
                                                       ▼
   ┌───────────────────────────── blast radius (account A, VPC-wide) ─────────────────────────────┐
   │ Route 53 Resolver 169.254.169.253 ─► SERVFAIL ─► PrivateLink private DNS, R53 private hosted  │
   │ zones, EFS mount DNS, RDS/Aurora/MSK/OpenSearch/EKS-CoreDNS endpoint resolution all FAIL.     │
   │ EXCEPTION: S3/DynamoDB *gateway* endpoints use route-table + prefix-list, NOT DNS → unaffected│
   └──────────────────────────────────────────────────────────────────────────────────────────────┘
   Adjacent write paths: CreateTags(vpc) → self-widen ABAC;  default VPC ships hostnames=true.
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internet-callable | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ModifyVpcAttribute` | EC2 Query/JSON | Existing | **Mutating (Write)** | Yes (SigV4) | set DNS/NAU attrs on a VPC | holders of `ec2:ModifyVpcAttribute` on `vpc*` | resource-scopable; carries `ec2:Attribute`/`…/${AttributeName}`; **primary target** |
| `DescribeVpcAttribute` | EC2 Query/JSON | Existing | Non-mutating (List) | Yes | read one of the three attrs | holders of `ec2:DescribeVpcAttribute` on `vpc*` | **no `ec2:Attribute`** → reads not attribute-scopable (Lens X) |
| `ModifyVpcPeeringConnectionOptions` | EC2 Query/JSON | Existing | **Mutating** | Yes | toggle DNS-resolution-from-remote-VPC per side | holders on `vpc-peering-connection*` | **cross-account** two-party DNS surface; `ec2:AccepterVpc`/`ec2:RequesterVpc` |
| `ModifySubnetAttribute` | EC2 Query/JSON | Existing | Mutating | Yes | subnet-level attrs | `subnet*` | sibling; adds `ec2:Vpc` (binds subnet's *home* VPC — Lens S variant b) |
| `CreateTags` (on `vpc`) | EC2 Query/JSON | Existing | Mutating | Yes | tag a VPC | `ec2:CreateTags` gated by `aws:RequestTag`/`ResourceTag` | **ABAC self-widening vector** feeding lead 6 |
| `ModifyVpcTenancy` | EC2 Query/JSON | Existing | Mutating | Yes | change VPC instance tenancy | `vpc*` | **control** action for the `ec2:Tenancy` null-key test |

Doc-flagged leads to keep verbatim: API reference — *"You cannot modify the DNS resolution and DNS hostnames attributes in the same request"* and *"You can only enable DNS hostnames if you've enabled DNS support."* No `[NEW]`/preview marker on this surface. No non-SDK/console-hidden parameter discovered (the delta between SDK model and console is empty for these three attributes).

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller in account A | VPC in account B | `ModifyVpcAttribute(VpcId=foreign)` | **Any 200/`return:true` mutating a VPC the caller's account does not own = Critical breach.** (Expected: `UnauthorizedOperation`/not-found; ARN is account-scoped.) |
| Caller in account A | existence of a foreign `vpc-…` | error differential (`InvalidVpcID.NotFound` vs `UnauthorizedOperation` vs validation 400) | A reliable not-found-vs-denied-vs-malformed differential that confirms a foreign VPC id = enumeration oracle (Low). |
| Low-priv intra-account principal | account-wide name resolution | one `ModifyVpcAttribute …=false` call | **Account-wide DNS outage from a principal lacking any delete/compute right = availability breach** (least-privilege blast radius). |
| Customer-authored `Deny` policy | IAM enforcement engine | `ec2:Attribute`/`${AttributeName}`/`ec2:VpcID`/`ec2:Tenancy` condition-key evaluation | **A correctly-intentioned Deny evaluates inert and the blocked change succeeds = enforcement-semantics breach (AWS-owned).** |
| Account A (one peering side) | Account B's DNS exposure | `ModifyVpcPeeringConnectionOptions` | One side toggling remote-VPC DNS resolution behavior **without the other account's separate action** = cross-account confused-deputy. |
| Shared-VPC participant | owner's VPC attributes | RAM share | Participant *modifying* the owner's VPC attrs = breach (docs say owner-only); participant *describing* them is by-design. |
| Holder of `ec2:CreateTags(vpc)` | `ModifyVpcAttribute` ABAC grant | self-set the gating tag | Holder tags an unowned VPC with the gating key then modifies it = ABAC self-widening (Medium). |
| Any customer surface | **AWS service plane** | — | **Hard stop.** None expected — VPC config is account-scoped. Any AWS-owned identity/ARN appearing = stop + disclose. |

---

## 5. Recommended Areas of Focus (ordered)

### 5.1 IAM / Condition-Key Enforcement (Lens R/S/U) — **PRIMARY**

> The dominant real surface. `ec2:ModifyVpcAttribute` is `vpc*`-scoped with condition keys `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:VpcID`, `ec2:Tenancy`, `ec2:Region`, `aws:/ec2:ResourceTag`. Several of these are plausibly *inert for this action*, so a customer guardrail silently fails open. AWS documents **no** worked condition example for this action.

**Lead S-1 — `ec2:Attribute` case-sensitivity / undocumented-value fail-open.**
→ **Claim:** A customer `Deny` on `ec2:ModifyVpcAttribute` keyed on `ec2:Attribute` with `StringEquals` and the console/prose casing (`enableDnsSupport`) is silently inert — the disable still succeeds — because the exact string EC2 synthesizes for this *named-boolean* action is undocumented (the only AWS example, `ModifyImageAttribute` → `"Description"`, is a different request shape with a generic `Attribute`/`Value` pair, which `ModifyVpcAttribute` lacks).
→ **Mechanism:** UserGuide *Identity-based policies for Amazon EC2* §attribute-key (only `ModifyImageAttribute` example, capitalized `Description`); `API_ModifyVpcAttribute` has no generic `Attribute` param; IAM *condition operators* ref: `StringEquals` = "Exact matching, case sensitive". Every documented `ec2:ModifyVpcAttribute` grant (UserGuide VPC examples, `vpc-policy-examples.md`, code-library) uses `Resource:"*"` with **no** `Condition`.
→ **Confirm/Refute oracle:** In the authorized account, attach `Allow ec2:ModifyVpcAttribute Resource:*` + `Deny … Condition StringEquals {"ec2:Attribute":"enableDnsSupport"}`; call `ModifyVpcAttribute(EnableDnsSupport={Value:false})`. If it **succeeds**, Deny was inert. Bisect the real runtime string by re-running with `StringEqualsIgnoreCase` and candidate values `EnableDnsSupport` / `DnsSupport` / `enableDnsSupport` / `ENABLEDNSSUPPORT`; corroborate with `DecodeAuthorizationMessage` on the variant that *does* deny.
→ **Preconditions / Cost:** disposable VPC; one call per casing candidate. `DryRun` not usable (need allow/deny outcome).
→ **Severity-if-true:** **Medium — AWS-owned enforcement-semantics defect** (no doc tells the customer which string to write), not a customer footgun. Reportable.

**Lead S-2 — `ec2:Attribute/${AttributeName}` cannot value-pin, and the `${AttributeName}` casing is undocumented.**
→ **Claim:** A customer cannot express "may set `enableDnsSupport=true` but never `false`" (the key tests *which attribute is touched*, not the boolean value, because the VPC attribute is a boolean toggle, not a string like `ModifyImageAttribute`'s `Description`). Separately, whether the suffix must be PascalCase `EnableDnsSupport` or camelCase `enableDnsSupport` is unconfirmed for this action → same silent-miss risk as S-1 at the key-name level.
→ **Mechanism:** `ec2:Attribute/${AttributeName}` = "Filters access by an attribute being set on a resource" (presence, not value); only example pins a *string* value. UserGuide says condition **key names** are case-insensitive, but is silent on whether that extends to the dynamic `${AttributeName}` suffix.
→ **Confirm/Refute oracle:** (a) value-pin: `Deny … Bool {"ec2:Attribute/EnableDnsSupport":"false"}` then call with `Value:false` — success confirms it gated only presence. (b) casing: repeat the presence-based Deny with suffix `enableDnsSupport` vs `EnableDnsSupport` vs `DnsSupport`; compare allow/deny.
→ **Preconditions / Cost:** disposable VPC, handful of calls.
→ **Severity-if-true:** Medium for the casing half (AWS-owned); the value-pin limitation itself is an inherent key-design limit — **informational**, listed so the hunter doesn't waste time writing a value-pin policy.

**Lead R-3 — AWS-managed policies grant `ec2:ModifyVpcAttribute` unconditionally.**
→ **Claim:** `AdministratorAccess`, `PowerUserAccess`, `AmazonEC2FullAccess`, and the `job-function/NetworkAdministrator` policy all grant `ec2:ModifyVpcAttribute` on `Resource:"*"` with **no `Condition`** — any holder can flip DNS/NAU on *any* VPC in the account, defeating any assumption the policy name implies VPC scoping.
→ **Mechanism (verbatim):** `AmazonEC2FullAccess` v5 → `{"Action":"ec2:*","Resource":"*"}`; `PowerUserAccess` v12 → `NotAction:[iam:*,organizations:*,account:*] Resource:*` (ec2:* falls through); `AdministratorAccess` → `Action:* Resource:*`; `NetworkAdministrator` v16 Sid `AllowDefaultNetworkAdminActions` lists `ec2:ModifyVpcAttribute`, `Resource:"*"`, no Condition — bundled with non-destructive network actions and *without* `ec2:TerminateInstances`/`ec2:DeleteVpc` (so a "network ops" role gets DNS-kill power without destroy-compute power).
→ **Confirm/Refute oracle:** doc-only confirmation via `iam:GetPolicyVersion` on each managed ARN (read-only, zero blast radius) — check for a `Condition` on the statement containing `ec2:ModifyVpcAttribute`/`ec2:*`. Behavioral confirmation: attach `NetworkAdministrator` to a disposable principal, call `ModifyVpcAttribute` on a VPC it has no tag relationship to, confirm success.
→ **Preconditions / Cost:** none for doc-only; one disposable principal + VPC for behavioral.
→ **Severity-if-true:** **Medium-High, Tier-2 in-scope** — AWS-authored, copy-verbatim artifact; standard/expected but a legitimate, falsifiable blast-radius fact. Route `aws-security` only as a precise "policy grants more than its name implies" note.

**Lead S-4 — `ec2:VpcID` resource-ID-family caveat (uncertain binding).**
→ **Claim:** A `Deny` keyed solely on `ec2:VpcID` (without matching `Resource`-ARN scoping) is assumed to fire for `ModifyVpcAttribute`, but `ec2:VpcID` belongs to the documented `ec2:{Resource}ID` family that for *creation* actions "always resolves to `*` at runtime" if the specific value is used. `ModifyVpcAttribute` is absent from AWS's avoid-with list, so by **negative inference** it should bind — but this is never stated positively.
→ **Mechanism:** UserGuide §"ec2:ResourceID condition keys" (the resolve-to-`*` caveat; only `ec2:VpcID – CreateVpc` listed); `list_ec2.md:10173` links `ec2:VpcID` to that same family anchor. Also the "Important" multi-resource-statement note (a resource-specific key in a mixed statement without `…IfExists` can falsify the whole condition for unrelated resources).
→ **Confirm/Refute oracle:** `Deny … Resource:"*" StringEquals {"ec2:VpcID":"vpc-AAAA"}`; call on `vpc-AAAA` (expect deny) and `vpc-BBBB` (expect allow). If AAAA is **not** denied, the negative inference fails → reportable. (VPC ids are lowercase-hex, so no casing sub-vector — note explicitly to save hunter time.)
→ **Preconditions / Cost:** two disposable VPCs, two calls.
→ **Severity-if-true:** Low/informational if it behaves as documented; Medium if it silently resolves to `*` like `CreateVpc`. **Uncertain — pending oracle.**

**Lead S-5 — `ec2:Tenancy` is a vacuously-false, never-populated key for this action.**
→ **Claim:** `ec2:Tenancy` is attached to the `vpc` resource type as a blanket bundle inherited by *every* `vpc*` action; `ModifyVpcAttribute`'s request carries no tenancy field, so a `Deny … StringEquals {"ec2:Tenancy":"dedicated"}` meant to protect dedicated-tenancy VPCs never fires (StringEquals on an absent context key = no match → falls through to `Allow`).
→ **Mechanism:** `list_ec2.md` — identical condition bundle on `ModifyVpcAttribute` (9135-9139) and `DescribeVpcAttribute` (7602-7606), confirming it's resource-type-level not action-tailored; glossary (10165) phrases `ec2:Tenancy` generically; IAM ref: absent key → condition values do not match.
→ **Confirm/Refute oracle:** `Deny … StringEquals {"ec2:Tenancy":"dedicated"}` + `Allow …`; call `ModifyVpcAttribute` on a `dedicated`-tenancy VPC → success confirms inert. **Control:** the same Deny shape on `ec2:ModifyVpcTenancy` (which *does* carry tenancy) should legitimately fire.
→ **Preconditions / Cost:** one dedicated-tenancy VPC (small extra cost) + two calls.
→ **Severity-if-true:** **Medium** — documented, syntactically-valid key a reasonable customer expects to gate this action, silently never engaging. Enforcement-applicability gap.

---

### 5.2 DNS Availability / Blast-Radius (Lens L/U/D) — **PRIMARY (impact)**

**Lead L-1 — one call collapses VPC-wide name resolution across many AWS services.**
→ **Claim:** A single `ModifyVpcAttribute … EnableDnsSupport={Value:false}` (or hostnames=false) stops the Route 53 Resolver from resolving Amazon-provided hostnames for the whole VPC, and jointly breaks Route 53 **private hosted zones**, **PrivateLink** interface-endpoint private DNS, **EFS** DNS mounts, and resolution of **RDS/Aurora/MSK/OpenSearch/EKS-CoreDNS** endpoints.
→ **Mechanism:** `API_ModifyVpcAttribute` ("…the Amazon provided DNS service…is not enabled"); `AmazonDNS-concepts` Rules ("If at least one of the attributes is set to false…The Route 53 Resolver cannot resolve Amazon-provided private DNS hostnames…for a private hosted zone…or private DNS with interface VPC endpoints (AWS PrivateLink), you must set both…to true"); `Route53/hosted-zone-private-considerations` ("must set…enableDnsHostnames, enableDnsSupport…to true"); `privatelink/interface-endpoints` (same); `efs/…mount-fs-mount-cmd-dns-name` ("must have both DNS Resolution and DNS Hostnames enabled"); `opensearch…/vpc`; `msk-connect-dns-attributes` + `…dns-failure-handling`. AWS's **own Support runbooks** treat this as a known root cause: `AWSSupport-ValidateRdsNetworkConfiguration`, `AWSSupport-TroubleshootEKSDNSFailure` (branches on `GetVpcDnsSettings`; disabled ⇒ terminal), `AWSSupport-TroubleshootMSKClusterConnection`. **Exception (refuting it as in-radius):** S3/DynamoDB *gateway* endpoints route via route-table + managed prefix list, not DNS — `vpc-endpoints-s3` lists DNS only as a consideration for *private DNS on top of* the gateway endpoint.
→ **Confirm/Refute oracle:** owned account — `describe-vpc-attribute` before/after; from an in-VPC instance `nslookup` a private-DNS name, an `efs-id.efs.<region>.amazonaws.com`, and a PHZ name → expect SERVFAIL/timeout against 169.254.169.253 post-flip; confirm gateway-endpoint S3 traffic unaffected.
→ **Preconditions / Cost:** only `ec2:ModifyVpcAttribute` on the target `vpc*`; one call, no quorum/undo-delay.
→ **Severity-if-true:** **High (customer availability / least-privilege framing)** — see L-2 for the actor model. Not a "bug" in AWS's sense (documented design), but a real low-priv→high-impact blast-radius fact. **Doc-gaps:** ElastiCache/Redshift/ECS-awsvpc DNS-dependency sentences not located in the mirror — verify live before asserting.

**Lead L-2 — single-API, synchronous, guardrail-free availability primitive.**
→ **Claim:** A principal holding *only* `ec2:ModifyVpcAttribute` (no `TerminateInstances`/`DeleteVpc`/`DeleteSubnet`) can break an entire production VPC's resolution in one synchronous call — no confirmation, quorum, or undo-delay — and `NetworkAdministrator` is a real role shape granting exactly that without destroy-compute rights.
→ **Mechanism:** `API_ModifyVpcAttribute` Response = single boolean `return` (no async `State`/pending-modification model, unlike `ModifyDBInstance`); `NetworkAdministrator` v16 grants the action on `Resource:"*"` alongside non-destructive actions only.
→ **Confirm/Refute oracle:** attach a policy granting only `ec2:ModifyVpcAttribute` (+ read-only Describe*); confirm the flip returns `return:true` immediately and the same principal gets `AccessDenied` on `TerminateInstances`/`DeleteVpc`. Time reversion: re-enable and measure seconds-to-resolution-restored.
→ **Preconditions / Cost:** one disposable principal + VPC. Actor model that makes it in-scope (not "self-DoS"): a broad-but-not-admin network operator, or a compromised CI/automation role scoped "only" to `ModifyVpcAttribute` for NAU toggling and abused for the DNS attribute.
→ **Severity-if-true:** High for the least-privilege/availability angle; explicitly **not** a confirmed bug. **Doc-gap:** no stated propagation delay for *re-enabling* (vs EFS's 90-s new-mount-target note, interface-endpoint "few minutes") — the outage-window-after-fix is a live-test question.

**Lead L-3 — two-call constraint & enable-ordering dependency (operational).**
→ **Claim:** "Cannot modify both DNS attributes in one request" + "can only enable hostnames if support is enabled" create a remediation gotcha: an operator re-enabling hostnames first (before support) may get an error, prolonging an incident.
→ **Mechanism:** `API_ModifyVpcAttribute` both-field notes.
→ **Confirm/Refute oracle:** from both-false, call `EnableDnsHostnames=true` first → observe reject vs silent-accept-but-inert; test whether the "at least one false ⇒ resolver fails" effect already takes hold after only the first disable (i.e., the "inconsistent window" is just the normal single-false state, not a novel race).
→ **Severity-if-true:** Low — incident-response friction, not a security primitive. **Doc-gap:** no stated intra-attribute eventual-consistency window across AZs/resolvers.

**Lead U-6 — `enableNetworkAddressUsageMetrics=false` as monitoring-evasion.**
→ **Claim:** Disabling NAU metrics removes a CloudWatch capacity signal (masking an approaching availability cliff for operators relying on NAU alarms) but does **not** disable the underlying NAU quota enforcement.
→ **Mechanism:** `network-address-usage` describes NAU as a monitoring/quota-planning metric; quota enforcement ("API calls fail…") is described independently of metric surfacing.
→ **Confirm/Refute oracle:** disable the metric, drive NAU toward quota → confirm (a) the `NAU` CloudWatch metric stops emitting while (b) `RunInstances`/`AttachNetworkInterface` still fail with `NetworkAddressUsageLimitExceeded` at quota.
→ **Severity-if-true:** Low — alarm-visibility loss, not a control bypass. **Doc-gap:** whether metric absence is total or display-only (`vpc-cloudwatch` not fully re-read).

---

### 5.3 Action-Family Parity & Cross-Account DNS (Lens X/A/AA/B/I)

**Lead X-1 — read/write condition-key asymmetry (`DescribeVpcAttribute` lacks `ec2:Attribute`).**
→ **Claim:** A customer can (attempt to) attribute-scope *writes* but cannot attribute-scope *reads* — `DescribeVpcAttribute` has no `ec2:Attribute`/`${AttributeName}` key, so a role meant only to read DNS settings can also read `enableNetworkAddressUsageMetrics`, with no policy carve-out possible. *(The earlier-suspected modify/describe enum mismatch does NOT hold — both APIs expose all three attributes; the asymmetry is purely IAM granularity.)*
→ **Mechanism:** `list_ec2.md` — `DescribeVpcAttribute` (7602) cond keys omit `ec2:Attribute`; `ModifyVpcAttribute` (9135) includes it. `API_DescribeVpcAttribute` ValidValues = all three.
→ **Confirm/Refute oracle:** grant `ec2:DescribeVpcAttribute` on `vpc*` with the tightest possible condition; confirm there is no way to deny `Attribute=enableNetworkAddressUsageMetrics` reads specifically.
→ **Severity-if-true:** Low (read of a boolean config flag; documented capability gap, no state change).

**Lead B-2 — cross-account peering DNS confused-deputy (`ModifyVpcPeeringConnectionOptions`).**
→ **Claim:** In a cross-account peering, a principal holding `ec2:ModifyVpcPeeringConnectionOptions` on `vpc-peering-connection*` **without** an `ec2:AccepterVpc`/`ec2:RequesterVpc` condition may be able to set the *other* side's `AllowDnsResolutionFromRemoteVpc`, altering the peer account's DNS-resolution exposure without that account's action. Docs phrase "each owner must initiate a separate request" as an operational rule, not an explicitly-stated server-side ownership check.
→ **Mechanism:** `list_ec2.md:9197` row (resource `vpc-peering-connection*`, keys incl `ec2:AccepterVpc`/`ec2:RequesterVpc`/`ec2:Attribute`); `API_ModifyVpcPeeringConnectionOptions` accepts both `Accepter`+`Requester` options in one call; `vpc-peering-dns` ("owner of the requester VPC must modify the requester…options") states the requirement without describing the enforcement layer.
→ **Confirm/Refute oracle:** two owned accounts, accepted peering; from account A (requester) with a grant lacking the `*Vpc` condition, attempt to set `AccepterPeeringConnectionOptions.AllowDnsResolutionFromRemoteVpc=true`. If accepted, A unilaterally changed B's side → confused-deputy. If server rejects regardless of IAM, drops to doc-clarity gap.
→ **Preconditions / Cost:** existing cross-account peering; a plausibly-misconfigured grant (omitting the two optional condition keys).
→ **Severity-if-true:** **Medium-High if confirmed** (one account makes the other's private DNS resolvable without consent); informational if the service enforces side-ownership server-side.

**Lead I-3 — ABAC self-widening via `ec2:CreateTags`.**
→ **Claim:** If a customer gates `ModifyVpcAttribute` with an ABAC `Allow` (`aws:ResourceTag/dns-admin=true`) **and** separately grants broad `ec2:CreateTags` on VPCs without an `aws:RequestTag`/`aws:TagKeys` restriction, the holder can self-set `dns-admin=true` on any VPC and then modify it.
→ **Mechanism:** `ModifyVpcAttribute` supports `aws:ResourceTag`/`ec2:ResourceTag` (9138); `CreateTags(vpc)` is gated only by existing/requested tags; AWS's own `access_tags` example shows `CreateTags` must be deliberately constrained with `aws:RequestTag`/`aws:TagKeys` to prevent arbitrary tag writes.
→ **Confirm/Refute oracle:** principal with ABAC `ModifyVpcAttribute` + unconstrained `CreateTags(vpc)`; `CreateTags(dns-admin=true)` on an unadministered VPC then `ModifyVpcAttribute` → success confirms self-widening. Also test whether tagging is denied (bounding blast radius).
→ **Severity-if-true:** **Medium** — escalation from "can tag VPCs" to "can modify VPC DNS," but only under a customer-authored policy combination (misconfiguration-amplification, not an AWS-side defect). Flag as a least-privilege warning.

**Lead AA-4 — shared-VPC owner-only enforcement layer (by-design, one open question).**
→ **Claim:** Per `vpc-share-limitations` ("Participants cannot modify VPCs or their related attributes. Only the VPC owner can. Participants can describe VPCs, their attributes…"), modify is owner-only and participant describe is by-design. The open question: is "owner-only" enforced by IAM account/ownership match (hard) or a service business-rule atop IAM (soft, possibly bypassable via a resource-based/delegated-admin grant path)?
→ **Confirm/Refute oracle:** in a RAM-shared VPC, grant a participant principal `ec2:ModifyVpcAttribute` on the shared VPC's ARN and confirm it is denied regardless (hard) — vs any path where it evaluates true (reportable).
→ **Severity-if-true:** Low/by-design for the main claim; the enforcement-layer question is a doc-clarity + defense-in-depth check.

**Lead U-5 — default VPC DNS-posture guarantee.**
→ **Claim:** A default VPC ships with `enableDnsSupport=true` and `enableDnsHostnames=true` as an inherent property (`AmazonDNS-concepts`: hostnames default `false` "unless the VPC is a default VPC"; `default-vpc` "settings to enable DNS resolution"). Instances in a brand-new default VPC are DNS-hostname-resolvable by default — a baseline other leads (peering requires both-true) depend on.
→ **Confirm/Refute oracle:** `DescribeVpcAttribute` on a freshly auto-created default VPC → both true with no customer action; a `false` would refute the guarantee.
→ **Severity-if-true:** Low (documented/expected; baseline-assumption note).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation being attacked |
|---|---|---|
| Deny bypass via `ec2:Attribute` casing/undocumented value | IAM eval of `ModifyVpcAttribute` | condition key `ec2:Attribute` (no worked example for this action) |
| Deny inert via never-populated `ec2:Tenancy` | IAM eval | resource-type-bundled condition key |
| Uncertain `ec2:VpcID` binding (resolve-to-`*`) | IAM eval | `ec2:{Resource}ID` family caveat |
| Value-pin impossibility `ec2:Attribute/${AttributeName}` | IAM eval | presence-only condition key |
| Unconditional managed-policy grant | `NetworkAdministrator`/`PowerUserAccess`/`AmazonEC2FullAccess`/`AdministratorAccess` | AWS-authored policy `Resource:"*"` no Condition |
| Account-wide DNS outage, one low-priv call | `ModifyVpcAttribute` + Route 53 Resolver | synchronous single-boolean action, no quorum/undo |
| Cross-account peering DNS toggle | `ModifyVpcPeeringConnectionOptions` | "each owner initiates separate request" (enforcement layer unstated) |
| ABAC self-widening | `CreateTags(vpc)` → `ModifyVpcAttribute` | `aws:RequestTag`/`aws:TagKeys` not required by default |
| Cross-account VPC mutation / enumeration | `ModifyVpcAttribute(VpcId=foreign)` | per-account `vpc` resource-ARN model |
| NAU monitoring-evasion | `enableNetworkAddressUsageMetrics` | NAU quota enforcement independent of metric surfacing |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **AWS service-plane / shared infra** — the Route 53 Resolver fleet (169.254.169.253), the EC2 control plane itself, shared RDS/Aurora/Grover/storage. Hard stop + disclose on any AWS-owned identity/ARN.
- **Single-tenant self-inflicted DoS** where the actor legitimately holds admin and intends the change — only in scope when the actor is a *bounded* principal (narrow network role / compromised scoped automation) causing disproportionate account-wide impact.
- **Customer-authored weak policies** as footguns (least-privilege is the customer's problem) — EXCEPT where the weak default is in an **AWS-managed/copy-verbatim artifact** (Lead R-3) which IS in scope.
- **DNS rebinding / resolver behavior against private-only endpoints**; IMDS on managed hosts; product/feature-parity gaps.
- **The target page is a code example** — SDK language bindings (PowerShell V4/V5, CLI) are thin wrappers; no injection/parser/deserialization surface exists in them (scalar id + boolean only).

---

## 8. Null Hypotheses / Doc Gaps (lenses checked that did NOT fire)
Pages checked across this surface: the target example page, `API_ModifyVpcAttribute`/`API_DescribeVpcAttribute`/`API_ModifyVpcPeeringConnectionOptions`/`API_AttributeBooleanValue`, `vpc-dns`/`AmazonDNS-concepts`/`vpc-dns-updating`, `vpc-share-limitations`/`vpc-sharing-share-subnet-working-with`, `default-vpc`, `network-address-usage`, `service-authorization/list_ec2.md`, UserGuide `iam-policies-for-amazon-ec2`, `vpc-policy-examples`, and the AWS-managed-policy JSON for the four policies above.

- **Lens C (credential vending / session scope)** — N/A: no STS `AssumeRole`, no session policy, no role ARN input, no credential chaining on this action.
- **Lens D/V (data-plane→control-plane / network segmentation)** — N/A as a *reachability* lens: this is a pure control-plane API; there is no customer-reachable data path or ENI hop here. (The *effect* on the Route 53 Resolver is covered as availability, not as a reachable boundary.)
- **Lens F (translation/injection) & memory-safety** — N/A: inputs are a scalar `vpc-…` id and a boolean; no parser/translator/wire protocol.
- **Lens G (SSRF)** — N/A: no field the service dereferences/fetches. The `169.254.169.253` link-local is the resolver *the VPC uses*, not a URL this API fetches. (Checked all three attribute params + the example page — no `*Url`/`*Uri`/fetch field.)
- **Lens K (prompt injection)** — N/A: no LLM/agent.
- **Lens M (shared-identifier interception)** — N/A: no session id / presigned URL / one-time token.
- **Lens N (namespace migration)** — N/A: single stable action, API version `2016-11-15`, no dual-live ARN/namespace.
- **Lens P (identity proofing / registration)** — N/A: no onboarding/OTP/uniqueness/KYB gate.
- **Lens Q (file/rich-content upload)** — N/A: no blob/upload/media field.
- **Lens T (cross-service secret reachability)** — N/A: this action generates/persists no secret.
- **Lens W (attestation-conditioned authz)** — N/A: no `kms:RecipientAttestation`/PCR surface.
- **Lens Y (transport / signature)** — N/A beyond generic EC2 endpoint TLS + SigV4 (no `http://` endpoint, no SigV2 acceptance, no internal-hop cert claim specific to this action).
- **Lens BB/CC/DD (canonicalization / upstream-context / cache-key)** — N/A: single-parser SigV4 control-plane call; no authorizer/WAF/CDN/cache in front; no authz-decision caching documented.
- **Lens EE (predictable-name land-grab)** — N/A: VPC ids are server-assigned, not a claimable global/predictable namespace.
- **Lens FF (JWT/OIDC token confusion)** — N/A: SigV4 only.
- **Lens A (cross-tenant IDOR)** — **fires weakly**: kept as Objective 1 + enumeration oracle, but the `vpc` resource ARN is account-scoped, so cross-account mutation is expected to fail; the realistic A-surface here is the error-differential enumeration oracle (Low), not data access.
- **Lens O (audit-log evasion)** — minor: `ModifyVpcAttribute` is a standard CloudTrail management event; no documented operation/error path that escapes logging. Note only as an enabler. **(Confirm the event is emitted for failed/dry-run calls.)**

**Key doc gaps blocking full resolution without a live account:**
1. The exact string EC2 populates into `ec2:Attribute` / `ec2:Attribute/${AttributeName}` for this *named-boolean* action (no AWS worked example for any non-`Attribute`/`Value`-pair action) — S-1/S-2 cannot be settled from docs alone.
2. Propagation delay for *re-enabling* the DNS attributes (outage-window-after-fix) — undocumented.
3. ElastiCache/Redshift/ECS-awsvpc explicit "requires VPC DNS resolution" sentences not located in the mirror — verify live.
4. Shared-VPC "owner-only" enforcement layer (IAM-hard vs service-business-rule) — unstated.

---

*End of plan. All leads are documentation-derived hypotheses; none has been tested against a live AWS account. A hunter executing this must use an account they are authorized to test, synthetic/disposable VPCs, and must hard-stop + preserve evidence if any AWS service-plane identity/ARN appears.*
