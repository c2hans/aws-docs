# EC2 "Manage the IPv4 addresses for your EC2 instances" — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/working-with-ip-addresses.html` (offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/working-with-ip-addresses.md`), plus the authoritative IAM reference `service-authorization/latest/reference/list_ec2.md` and the shared-VPC pages `AWSEC2/.../using-vpc.md` + `vpc/latest/userguide/vpc-share-limitations.md` + `vpc/.../subnet-public-ip.md`. Status: **documentation-derived hypotheses only; nothing tested against a live account.** Online `.md` twins verified byte-identical to offline for every quoted sentence on 2026-10-15 (no drift).

**Position in the corpus.** This is a **page-level deep-dive child of the EC2 Networking hub** (`ec2-networking-attack-research-plan.md`) and a **sibling of `using-instance-addressing-attack-research-plan.md`** (the IP-addressing *concept* page). This page is the **launch-time IPv4 assignment operational how-to**: assign a *public* IPv4 at launch, assign a *private* IPv4 at launch, view IPs via `describe-instances`/IMDS. It **owns the launch-time assignment surface** and **cross-references, does not restate**, the sibling/hub leads it links to.

### Explicitly deferred to siblings (do NOT re-develop here)
- **Secondary private-IPv4 reassignment / `AssignPrivateIpAddresses … AllowReassignment` cross-ENI / cross-account takeover** → `using-instance-addressing-attack-research-plan.md` Area 1 (the target page links to `managing-network-interface-ip-addresses.md` + `instance-secondary-ip-addresses.md` only for the *after-launch* unassign/assign step; that deep surface is the sibling's).
- **Ephemeral auto-assigned public-IPv4 pool reuse / dangling-DNS hijack** → sibling Area 3. (This page's §"public IP at launch" adds only the pool/device-index-0 mechanics; the reuse-prohibition prose lives in `using-instance-addressing.md:54`, confirmed by subagent — nothing new at the launch step.)
- **Link-local (169.254.169.254 IMDS) SG/NACL non-filtering** → sibling Area 4. This page's §"View IPv4 via IMDS" is a verbatim IMDSv2/v1 `local-ipv4`/`public-ipv4` retrieval walkthrough; the metadata-service threat surface is the sibling's. (See §7.)
- **Elastic IP cross-account transfer (no dest-account key), `AllocateAddress` address-value squatting** → hub `ec2-networking-attack-research-plan.md` cluster 1.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The dominant finding type on this page is **Lens S/U** — *"the guardrail the operator would reach for is not expressible on this action,"* plus one **Lens A/V cross-account shared-VPC** seam. There is **no cross-tenant data-read primitive native to this page** beyond the unscopable Describe oracle; keep severity honest.
- **IAM oracle first:** every "unexpressible key" claim is settleable with `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` — **no resources created**. Escalate to a live scoped call only with synthetic canary data in an authorized account.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the Nitro/host side of any link-local service, Amazon's public-IPv4 pool internals), stop, preserve evidence, flag for AWS-Security disclosure. The host/Nitro side of IMDS is a disclosure boundary, never a test target.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Force public internet exposure of an instance against the controlling party's intent** — as a shared-VPC *participant*, override the *owner's* `MapPublicIpOnLaunch=false` and get a routable public IPv4 in the owner's subnet (A/V).
2. **Prove the public-IP-at-launch guardrail is unenforceable as commonly written** — a Deny on `ec2:AssociatePublicIpAddress` that is silently inert because of the multi-resource `Resource:"*"` evaluation pitfall (S/U).
3. **Prove no policy can pin or forbid which private IPv4 a launch requests** — `ec2:PrivateIpAddress` does not exist (S/U).
4. **Cross-tenant private-IP collision / pre-emption in a shared subnet** — grab a hardcoded internal-service private IP before the intended workload launches → DoS or address-confusion (L/A, doc-gap).
5. **Intent-vs-outcome divergence via the existing-ENI-at-index-0 rule** — the explicit `--associate-public-ip-address` override silently no-ops and defers to the owner's hidden subnet attribute (U/BB).
6. **Account-wide IP/metadata enumeration** via unscopable `DescribeInstances` (A read oracle).

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 control-plane API `RunInstances` (CLI `run-instances`) with the launch-time addressing parameters:
- `--associate-public-ip-address` (bool) — request/suppress an auto-assigned public IPv4 on the device-index-0 ENI; **overrides** the subnet default.
- `--private-ip-address` / `--private-ip-addresses` — request a *specific* primary private IPv4 from the subnet CIDR (or let EC2 pick).
Plus the subnet-level default `MapPublicIpOnLaunch` set via `ModifySubnetAttribute` (CLI `modify-subnet-attribute`; VPC console "Enable auto-assign public IPv4 address"), and the read path `DescribeInstances` + IMDS (`http://169.254.169.254/latest/meta-data/{local,public}-ipv4`).

**Assets.**
- A routable **public IPv4** (internet exposure of a workload) — assigned from *Amazon's shared pool*, "not associated with your AWS account."
- A specific **private IPv4** within a subnet CIDR (identity other workloads may hardcode: internal DNS `.2`, app service IPs, etc.).
- The **subnet `MapPublicIpOnLaunch` attribute** — a one-flag exposure default for *every* instance launched into the subnet.
- Instance inventory (public/private IPs, IAM-instance-profile ARN, metadata) readable via `DescribeInstances`.

**Ownership split / trust zones.**
- Single account: caller identity governs launch; `MapPublicIpOnLaunch` and the launch override are both the caller's.
- **Shared VPC (RAM-shared subnet):** the **subnet OWNER** exclusively controls the subnet attribute (`MapPublicIpOnLaunch`); the **PARTICIPANT** (different account) launches instances into it but owns only ENIs it creates. This is the only cross-account trust boundary on this page.

```
             ┌──────────────────── Subnet OWNER account ───────────────────┐
             │  Subnet (RAM-shared)   attribute: MapPublicIpOnLaunch=false  │  (owner-only writable)
             └──────────────▲───────────────────────────────┬──────────────┘
                            │ describe-only                  │ governs default
   PARTICIPANT account      │                                ▼
   run-instances ───────────┴──> instance / ENI(idx0) ──> public IPv4? (Amazon pool)
     --associate-public-ip-address  (override, acts on participant's own ENI, NOT the subnet)
     --private-ip-address 10.x.y.z  (specific primary private IP, no value-level IAM key)
```

---

## 3. API / Interface Inventory

| Name | Method | Mut? | Ext-facing | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `RunInstances` | API/CLI/SDK | Mutating | Yes | Launch; carries `AssociatePublicIpAddress`, `PrivateIpAddress[]` | identity-policy holders | **Only EC2 action carrying `ec2:AssociatePublicIpAddress`** (list_ec2 count-3). Caller identity governs (no SLR on direct RunInstances). |
| `ModifySubnetAttribute` | API/CLI | Mutating | Yes | Set subnet `MapPublicIpOnLaunch` (+IPv6 attr) | subnet owner only (in shared VPC) | No dedicated `ec2:MapPublicIpOnLaunch` key; only generic `ec2:Attribute`/`ec2:Attribute/${AttributeName}`. |
| `AssignPrivateIpAddresses` | API/CLI | Mutating | Yes | Assign secondary private IPv4 (after launch) | ENI owner | Deep surface owned by `using-instance-addressing` sibling; cited here only for the symmetric private-IP-value key gap. |
| `DescribeInstances` | API/CLI | Non-mut | Yes | Read instances incl. public/private IPs, profile ARN | any grantee | **Unscopable** — resource types blank, only `ec2:Region`. Account-wide read oracle. |
| IMDS `GET /meta-data/{local,public}-ipv4` | HTTP (link-local) | Non-mut | from instance | Read instance's own IPs | on-box processes | Link-local; threat surface owned by sibling Area 4. |

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Shared-VPC participant (acct B) | Owner (acct A) subnet exposure intent | `--associate-public-ip-address` at launch overriding owner `MapPublicIpOnLaunch=false` | Participant's instance gets a routable public IPv4 in the owner's `=false` subnet → owner's documented subnet-level exposure default is overridden by a party who cannot write the attribute. |
| Shared-VPC participant (acct B) | Another tenant's expected private IPv4 (acct A or C) | `--private-ip-address 10.x.y.z` at launch in the shared subnet | B's launch succeeds holding an IP that A's config hardcodes → A's later launch fails (DoS) or silently gets a different IP (address-confusion). |
| Guardrail author (any) | The intended "no public IP at launch" control | Deny `ec2:AssociatePublicIpAddress` written against `Resource:"*"` without `…IfExists`/NI-scoping | A `RunInstances` with `--associate-public-ip-address` still succeeds → the Deny was inert (evaluated only against the network-interface element). |
| Any grantee of `ec2:DescribeInstances` | Every instance in the Region | Describe with no resource/tag scoping | Reading IPs + instance-profile ARN of instances the caller does not own/tag. |
| Any customer surface | AWS service plane (Amazon public-IPv4 pool, Nitro/IMDS host) | — | **HARD STOP** — any AWS fleet identity/pool internal reached = disclosure, preserve + flag. |

---

## 5. Recommended Areas of Focus

### Area 1 — `ec2:AssociatePublicIpAddress` is `RunInstances`-only AND silently inert under the common multi-resource Deny shape (Lens S/U) — HEADLINE
**Background.** The only IAM lever that governs "does this launch get a public IPv4" is the condition key `ec2:AssociatePublicIpAddress` (Bool, def `list_ec2.md:10050`). Subagent confirmed it appears exactly **3 times in all of `list_ec2.md`**: its definition, the generic `network-interface` key catalogue (`:9982`), and **only one action — `RunInstances`** — and there only on the **`network-interface*` resource row** (`:9595`), **not** on the `instance*` (`:9591`) or `subnet*` (`:9602`) rows. No other EC2 action (`CreateNetworkInterface :5357-5362`, `ResetNetworkInterfaceAttribute :9519-9523`) carries it.
**Security Concern.** The key *is* expressible — but `RunInstances` is a **multi-resource action** and the key binds only the `network-interface` element. A guardrail author who writes a `Deny` with `ec2:AssociatePublicIpAddress=true` but a `Resource:"*"` (or any resource set that includes elements for which the key is undefined) hits AWS's own documented pitfall: for request elements where the condition key is **not present**, the condition does not match and the statement **may silently fail to apply** unless `…IfExists` logic and NI-scoped resources are used correctly. The result: an operator believes "no public IPs at launch" is enforced, but a plain `--associate-public-ip-address` launch succeeds.
**High-level Test Scenarios.**
- **Claim:** a `Deny {Action: RunInstances, Condition: Bool ec2:AssociatePublicIpAddress=true}` with `Resource:"*"` is inert → **Oracle:** `iam:SimulateCustomPolicy` for `RunInstances` with the public-IP request context against that policy returns **allowed**, while the same Deny scoped to `arn:…:network-interface/*` returns **denied**. Settles entirely offline (no resource created).
- **Claim:** the key cannot be used to require IMDSv2-style hardening of exposure elsewhere — it exists on **no other action**, so there is no way to forbid public IP on any path other than `RunInstances` (e.g. a later attribute flip). → **Oracle:** grep confirms count-3; simulate on `CreateNetworkInterface`/`ResetNetworkInterfaceAttribute` → key ignored.
- **Variant (Lens S case-sensitivity / Bool-vs-Null):** test whether a `Null`/`…IfExists` vs plain `Bool` Deny differ in matching when the request omits the flag (default-subnet `=true` path).
**Doc evidence.** `list_ec2.md:10050, :9595, :9982`; AWS multi-resource-action condition guidance. Target page `working-with-ip-addresses.md:19,36`.
**Severity-if-true.** Guardrail-bypass / least-privilege-enforcement gap = **Medium** (High if the exposed workload is sensitive and the operator relied on the inert Deny as the sole control). Not AWS-authored artifact → customer-footgun unless the inert-match behavior is itself the defect; the *key-is-NI-row-only* fact is informational-to-AWS.

### Area 2 — No condition key constrains the **private-IPv4 value** at launch (Lens S/U) — HEADLINE
**Background.** The page documents `--private-ip-address` to request a *specific* primary private IPv4 (`working-with-ip-addresses.md:57`).
**Security Concern.** Subagent grep: **`ec2:PrivateIpAddress` / `ec2:PrivateIp*` does not exist anywhere in `list_ec2.md`.** `RunInstances` `instance*`/`network-interface*`/`subnet*` rows (`:9591/:9595/:9602`) carry no IP-value key; `AssignPrivateIpAddresses` (`:4700-4704`) likewise. An admin **cannot** author a policy that pins which private IPv4 a launch may request, nor forbid specifying one at all. (This is **symmetric** across the launch path and the secondary-assign path — a precision guard: it is *not* a Lens-X asymmetry; both lack the key.)
**High-level Test Scenarios.**
- **Claim:** "only let this role launch into subnet X but never let it claim the subnet's `.10` reserved service IP" is inexpressible → **Oracle:** `SimulateCustomPolicy` shows no key available to discriminate the requested address; the subnet can be scoped (`ec2:Subnet`/`ec2:SubnetID`, see Area 3) but the address within it cannot.
- Chains into Area 4 (collision/pre-emption): because the value is un-gated, nothing in IAM stops a caller from targeting a *specific* address.
**Doc evidence.** `working-with-ip-addresses.md:57`; `list_ec2.md:9591,9595,9602,4700-4704` (keys enumerated verbatim by subagent); absence confirmed by grep.
**Severity-if-true.** Enforcement-gap = **Low–Medium** standalone (an admin cannot bound address selection); **Medium–High** when chained to the shared-subnet collision primitive (Area 4).

### Area 3 — Shared-VPC participant overrides owner's public-IP intent / owner silently controls participant exposure (Lens A / V / U cross-account) — HEADLINE cross-account
**Background.** In a RAM-shared subnet, **only the owner can modify the subnet or its attributes; participants can only *describe* them** (`vpc-share-limitations.md:57`). Participants may run instances into the shared subnet and control IP associations on **ENIs they own** (`using-vpc.md:49`, `vpc-share-limitations.md:43`). The launch-time override (`--associate-public-ip-address`) acts on the **participant's own ENI/instance**, not on the subnet object.
**Security Concern.** Two directional seams, both arising from the *composition of three pages* (no single page warns about either):
- **(a) Participant forces exposure against owner intent.** Owner sets `MapPublicIpOnLaunch=false` to keep the shared subnet private. A participant passes `--associate-public-ip-address` at launch and — because the override is an ENI-scoped control the participant legitimately holds, with no documented carve-out for shared subnets — obtains a routable public IPv4 in the owner's "private" subnet. The owner cannot prevent this via the subnet attribute (the only knob they own).
- **(b) Owner silently governs participant exposure.** If the participant omits the flag, whether their workload is internet-exposed is decided entirely by an attribute they can *describe* but never *set* — a cross-account control-influence over the participant's security posture.
**High-level Test Scenarios.**
- **Claim (a):** participant launch with `--associate-public-ip-address` into owner's `MapPublicIpOnLaunch=false` shared subnet yields a public IPv4 → **Oracle:** `describe-instances` on the participant's instance shows `PublicIpAddress` populated despite owner `=false`. Two-account (owner + participant RAM-share) canary required; DryRun is caller-IAM-only and cannot answer (evaluated before placement).
- **Claim (b):** participant launch without the flag inherits owner's attribute → **Oracle:** flip owner `MapPublicIpOnLaunch` true/false between two participant launches, observe participant exposure track the owner's setting.
- Is there any owner-side IAM/SCP that *can* forbid participant public-IP override in the owner's subnet? (Area 1 says the `ec2:AssociatePublicIpAddress` Deny lives in the *participant's* identity policy — the owner cannot impose it; worth confirming no RAM/resource-policy lever exists.)
**Doc evidence.** `vpc-share-limitations.md:43,57`; `using-vpc.md:49,50,52`; `working-with-ip-addresses.md:19,23`. Online==offline verified.
**Severity-if-true.** Participant-forced public exposure of a workload in an owner's intended-private shared subnet = **Medium–High** (internet exposure crossing an account's documented control boundary; High if it enables inbound reach the owner's segmentation assumed impossible — pair with SG/NACL posture).

### Area 4 — Cross-tenant private-IP collision / pre-emption in a shared subnet (Lens L / A, doc-gap)
**Background.** `--private-ip-address` lets a caller request a specific address; EC2 otherwise "select[s] an **available** IP address" (`using-instance-addressing.md:38`). For *multi-address* single-ENI requests, "the entire operation fails if one of the IP addresses can't be assigned" (`using-instance-addressing.md:145`).
**Security Concern.** **Doc-gap (subagent-confirmed):** none of the launch/shared-VPC pages state (i) whether private-IP uniqueness is enforced **cross-account at the shared-subnet level**, (ii) the error returned on a caller-specified collision, or (iii) whether a participant can **pre-emptively grab** a specific address another tenant's config hardcodes (internal DNS, app service IP) before that workload launches — causing the victim launch to fail (DoS) or silently receive a different IP (hardcoded-config confusion). The word "available" *implies* already-assigned addresses are rejected (arguing against silent takeover), but cross-account scoping of that check is never stated.
**High-level Test Scenarios.**
- **Claim:** participant B can hold a specific private IP in a shared subnet that participant/owner A expects → **Oracle:** B launches (or `assign-private-ip-addresses` on a B-owned ENI) at `10.0.0.53`; then A launches requesting `10.0.0.53` — observe A's launch **fail** (DoS primitive) or **get a different IP** (confusion). Any of those two outcomes confirms the cross-tenant collision primitive. Requires owner+participant canary.
- **Refute path:** if B's request for an in-use address is itself rejected and A always wins, the primitive is null — record as a clean negative.
**Doc evidence.** `working-with-ip-addresses.md:57`; `using-instance-addressing.md:38,145`; silence across `using-vpc.md`/`vpc-share-limitations.md`.
**Severity-if-true.** Cross-tenant DoS / address-confusion on a shared subnet = **Medium–High** (High if it reliably breaks a victim's hardcoded internal dependency). Standalone single-account = Low (self-inflicted).

### Area 5 — Existing-ENI-at-index-0 silently disables the public-IP override and defers to the owner's hidden subnet attribute (Lens U / BB intent-vs-outcome)
**Background.** `working-with-ip-addresses.md:23`: *"you cannot override the subnet setting using the auto-assign public IP feature if you specify an existing network interface for device index 0"* (and no auto-assign at all with >1 ENI).
**Security Concern.** A participant who pre-creates their **own** ENI (satisfying `using-vpc.md:49` "participants must own any network interfaces they specify") in the owner's shared subnet and attaches it at index 0 finds their explicit `--associate-public-ip-address` **silently ignored** — exposure reverts to the owner's `MapPublicIpOnLaunch`, which the participant can only describe. Intent (the flag) and outcome (owner's hidden setting) diverge with no error. The **cross-account bypass is foreclosed** (participants cannot specify the *owner's* ENI), so this is an integrity/clarity seam, not a privilege break — but the interaction is never discussed in one place.
**High-level Test Scenarios.**
- **Claim:** launch with self-owned existing ENI at idx0 + `--associate-public-ip-address` → public-IP assignment follows owner's subnet attribute, flag no-ops → **Oracle:** instance exposure matches `MapPublicIpOnLaunch`, not the flag; no API error raised for the ignored flag.
- Confirm attaching a foreign/owner ENI at idx0 is rejected (ownership rule holds) — expected clean negative; records that the bypass path is closed.
**Doc evidence.** `working-with-ip-addresses.md:23`; `using-vpc.md:49`; `vpc-share-limitations.md:43`.
**Severity-if-true.** **Low–Informational** (silent-override confusion → mis-set exposure expectation); elevate only if it causes an operator to believe a workload is private when it is public (or vice-versa).

### Area 6 — Subnet `MapPublicIpOnLaunch` has no dedicated condition key; only the easily-missed generic `ec2:Attribute` escape hatch (Lens S)
**Background.** `ModifySubnetAttribute` (`list_ec2.md:9024-9028`) requires `subnet*` and supports `aws:ResourceTag`, `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:AvailabilityZone(Id)`, `ec2:Region`, `ec2:ResourceTag`, `ec2:SubnetID`, `ec2:Vpc`. Subagent grep: **no `ec2:MapPublicIpOnLaunch` key exists.**
**Security Concern.** To forbid an operator from turning on auto-assign-public-IP at the subnet level, an admin must use the generic `ec2:Attribute`/`ec2:Attribute/${AttributeName}` keys (a `Deny` on `ec2:Attribute=MapPublicIpOnLaunch`, or `ec2:Attribute/MapPublicIpOnLaunch=true`). AWS documents these generic keys primarily via a `ModifyImageAttribute`/`Description` example — a boolean VPC exposure setting is **not** an obvious place an author would reach for them, so the control is *present but easily missed*. Also test the Lens-S **case-sensitivity fail-open** variant: a Deny written against a lowercase/mismatched attribute-name casing may be inert against the PascalCase request field.
**High-level Test Scenarios.**
- **Claim:** `Deny ec2:Attribute=MapPublicIpOnLaunch` on `ModifySubnetAttribute` actually blocks the flip → **Oracle:** `SimulateCustomPolicy` denies; confirm the exact attribute-name string the key populates (empirically verify, since the doc names it only via the Image example). If casing/name mismatch leaves it inert → fail-open finding.
**Doc evidence.** `list_ec2.md:9024-9028`; `subnet-public-ip.md:25,30`; absence of dedicated key by grep.
**Severity-if-true.** **Low** (control exists, just non-obvious); **Medium** only if a casing/name mismatch makes the intended Deny silently inert (Lens-S fail-open).

### Area 7 — `DescribeInstances` is an unscopable account-wide IP/metadata read oracle (Lens A)
**Background.** The page's "view the primary IPv4" step uses `describe-instances`. `list_ec2.md:6996-7000`: `DescribeInstances` has **blank required-resource-type**, condition keys **only `ec2:Region`**, Access=List.
**Security Concern.** Any principal granted `ec2:DescribeInstances` enumerates **every** instance in the allowed Region(s) account-wide — public/private IPs, IAM-instance-profile ARN, and adjacent metadata — with **no** tag/ARN/ownership scoping possible ("Describe\* actions do not support resource-level permissions"). This is the **same inert-ABAC read-oracle shape** the corpus has repeatedly logged (`manage-spot-fleet`'s `DescribeSpotFleetRequests`, the hub's `DescribeNetworkInterfaces`, CR `DescribeCapacityReservations`). Intra-account cross-team over-exposure + recon that feeds Areas 3/4 (locate target private IPs to collide with; confirm which instances have public IPs).
**High-level Test Scenarios.**
- **Claim:** a role scoped (by tag) to one team's instances can still read all instances' IPs → **Oracle:** `SimulateCustomPolicy` shows any `aws:ResourceTag` condition on `DescribeInstances` is ignored (no resource type to bind). Confirm live only with read-only canary.
**Doc evidence.** `list_ec2.md:6996-7000`.
**Severity-if-true.** Intra-account cross-team info-disclosure / recon enabler = **Low–Medium** (not cross-account; a least-privilege ceiling, inherent to Describe\*).

### Lens-X note (parity)
`RunInstances`' `network-interface*` row (`:9595`) uniquely carries `ec2:AssociatePublicIpAddress` + `ec2:Subnet` + `ec2:Vpc`; `CreateNetworkInterface` (`:5357-5362`) and `ResetNetworkInterfaceAttribute` (`:9519-9523`) do **not** carry `AssociatePublicIpAddress`. The public-IP-at-creation guardrail genuinely exists **only on the launch path** — a defender cannot express it on the standalone ENI-creation path (there is no auto-assign-public-IP on `CreateNetworkInterface` to gate, so this is expected, not a bug; noted to pre-empt a false Lens-X claim).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Participant forces public IPv4 in owner's `=false` shared subnet | `RunInstances --associate-public-ip-address` + shared subnet | "Only the VPC owner can [modify subnet attributes]" (`vpc-share-limitations.md:57`) — attack it: the override is ENI-scoped, not subnet-scoped. |
| `ec2:AssociatePublicIpAddress` Deny inert under `Resource:"*"` | `RunInstances` IAM eval | Multi-resource condition-match semantics; key only on NI row. |
| No key pins requested private IPv4 | `RunInstances`/`AssignPrivateIpAddresses` IAM | Absence of `ec2:PrivateIpAddress` (grep). |
| Cross-tenant private-IP pre-emption/collision | shared subnet address bookkeeping | "we select an **available** IP" (`using-instance-addressing.md:38`); multi-addr all-or-nothing (`:145`). |
| Existing-ENI-idx0 silently disables override | `RunInstances` placement | `working-with-ip-addresses.md:23` prose rule. |
| `MapPublicIpOnLaunch` Deny casing fail-open | `ModifySubnetAttribute` IAM | Generic `ec2:Attribute/${AttributeName}` matching. |
| Account-wide instance/IP enumeration | `DescribeInstances` | "Describe\* do not support resource-level permissions." |

---

## 7. Out-of-Scope Risk Categories
- **Secondary private-IP reassignment / `AllowReassignment` takeover** — owned by `using-instance-addressing` sibling Area 1.
- **Ephemeral public-pool reuse / dangling-DNS** — sibling Area 3.
- **Link-local IMDS SG/NACL non-filtering, IMDSv1-vs-v2** — sibling Area 4; the host/Nitro side of IMDS and Amazon's public-IPv4 pool internals are a **shared-responsibility / service-plane HARD STOP**, never a test target.
- **EIP cross-account transfer, `AllocateAddress` squatting** — hub plan cluster 1.
- **IPv6-at-launch assignment** — companion page `working-with-ipv6-addresses.html` (not this page); note IPv6 is safer (no force-reassign; must unassign first — sibling Area 6).
- Single-account self-DoS, product/feature-parity gaps, DNS rebinding against private endpoints.

---

## 8. Null hypotheses / doc gaps
- **Lens B/C/E (PassRole / privesc / role model):** N/A — this page defines no role-ARN input, no SLR (direct `RunInstances` runs under the caller; the Fleet SLR backbone does not apply here), no credential vending. Pages checked: target page + `using-instance-addressing.md` + `managing-network-interface-ip-addresses.md` — no role/credential field.
- **Lens G (SSRF):** N/A — no field the service dereferences; the only URL on the page is the link-local IMDS endpoint queried *from the instance*, not a server-side fetch. Pages checked: target page (all 4 sections).
- **Lens Q (upload):** N/A — no blob/file input. Lens K (LLM) N/A. Lens H (KMS), W (attestation), FF/J (tokens/OAuth) N/A — no such surface on an IP-assignment page.
- **Lens F (injection):** N/A — IP values are structured addresses validated against subnet CIDR, no translation layer.
- **DOC-GAP (needs live confirmation first, flagged in-area):**
  1. Cross-account private-IP uniqueness-check scoping + collision error behavior in a shared subnet (Area 4) — the single highest-value open question.
  2. Whether a shared-subnet participant's `--associate-public-ip-address` override is actually honored against owner `MapPublicIpOnLaunch=false` (Area 3a) — the plain reading says yes; confirm with a two-account canary.
  3. The exact attribute-name string `ec2:Attribute/${AttributeName}` populates for `MapPublicIpOnLaunch`, and whether a casing mismatch makes a Deny inert (Area 6).
- **DryRun caveat (reusable):** `DryRunOperation` on `RunInstances` is caller-IAM-only (evaluated before placement/address resolution) → it **cannot** answer Areas 3/4; those require real two-account canary launches with synthetic data in an authorized environment.

See [[reference-aws-iam-service-auth-ref-url]] and [[project-aws-research-plans]].
