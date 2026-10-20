# EC2 `UnassignPrivateIpAddresses` — Attack Research Plan

**Source of leads:**
- Target example page: `https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_UnassignPrivateIpAddresses_section.html` (+ `.md`)
- API reference: `https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnassignPrivateIpAddresses.html`
- IAM authorization: local mirror `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (actions table ~L4537/L9696; sibling IP-family rows L104/L110/L4694/L4700/L9690; ModifyNetworkInterfaceAttribute L8966–8972; Detach L7728; Delete L6088) — cross-checked against online service-authorization reference.
- Concept: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requester-managed-eni.html`, `using-eni.html`, `multiple-ip-addresses.html`.
- Supporting deep-dive artifacts (documentation-only, with full citations): `_unassignip_research/subagent_managed_eni.md` (ManagedResourceOperator + requester-managed ENI + AWS-managed-policy survey), `_unassignip_research/subagent_scoping_chain.md` (IP-value scoping gap + reassignment chain + ID formats).

**Status:** documentation-derived hypotheses only; nothing tested against a live account. Built with the `security-questionbuilder` method. Related prior plans: `ec2-RunInstances-attack-research-plan.md`, `RevokeSecurityGroupIngress-attack-research-plan.md`, `ResetInstanceAttribute-attack-research-plan.md`.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Prefer **`iam:SimulatePrincipalPolicy` / `iam:SimulateCustomPolicy`** as the resource-free first oracle for every IAM-scoping lead — no ENI need be touched.
- **DryRun caveat (confirmed corpus trap):** `DryRunOperation` is evaluated against caller IAM *before* resource resolution — it is **NOT an ownership/existence oracle**. Do not treat a `DryRunOperation` success as proof the NIC exists or is owned.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane** (e.g. the service account that operates a requester-managed ENI), stop, preserve evidence, flag for AWS-Security disclosure. Operating on a requester-managed ENI *within your own account* is NOT by itself a service-plane breach — see §7.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Unassign a secondary private IP / IPv4 prefix on a network interface the caller should not be able to touch** — i.e. an ENI in another account, or an ENI the policy author believed was out of scope.
2. **Prove the IP/prefix-value scoping gap:** a principal granted "unassign on NIC X" can strip *every* secondary IP/prefix on X, including a specific VIP the author meant to protect — because no condition key can name an IP/prefix.
3. **Operate on a requester-managed / AWS-managed ENI** (RDS/NAT/PrivateLink/ELB/Lambda/EFS/TGW/Resource-Gateway) despite the documented prohibition — a control-plane enforcement-parity break.
4. **IP-takeover chain:** free a victim's secondary IP (Unassign) and re-home it to an attacker-controlled ENI (`AssignPrivateIpAddresses AllowReassignment`) in the same subnet → intra-account traffic interception / connectivity denial.
5. **Confirm no cross-account / service-plane reach** is possible (expected result = negative; document it as a guarantee, not a finding).

---

## 2. Components, Assets, and Design

**What the action is.** `ec2:UnassignPrivateIpAddresses` is a single-resource, **mutating (Write)** EC2 control-plane API. It removes **secondary** private IPv4 addresses and/or **IPv4 Prefix Delegation prefixes** from one network interface.

**API surface (API reference):**
| Param | Type | Required | Role |
|---|---|---|---|
| `NetworkInterfaceId` | String | **Yes** | the resource the action binds to (`eni-…`) |
| `PrivateIpAddress.N` | Array\<String\> | No | which secondary IPv4(s) to remove |
| `Ipv4Prefix.N` | Array\<String\> | No | which delegated IPv4 prefix(es) to remove |
| *(response)* `return` | Boolean | — | `true` on success; no body otherwise |

**IAM authorization (service-authorization reference):**
- **Resource type (required):** `network-interface*` (account-scoped ARN `arn:${Partition}:ec2:${Region}:${Account}:network-interface/${NetworkInterfaceId}`).
- **Condition keys (exactly 8):** `aws:ResourceTag/${TagKey}`, `ec2:AvailabilityZone`, `ec2:ManagedResourceOperator`, `ec2:NetworkInterfaceID`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:Subnet`, `ec2:Vpc`.
- **Access level:** Write.

**Actors / ownership.** Caller = an IAM principal in the account that owns the ENI. The ENI lives in a customer subnet/VPC. A subset of ENIs are **requester-managed** — created by an AWS service (RDS, NAT GW, PrivateLink interface endpoint, ELB, Lambda, EFS mount target, Transit Gateway, Resource Gateway `rgw-…`) in the customer's account but **operated by the service's account** (`Requester ID` ≠ customer). This is the only trust seam in the action.

**ASCII — where the action sits:**
```
IAM principal (customer acct)
        │ ec2:UnassignPrivateIpAddresses(NetworkInterfaceId, [PrivateIpAddress.N|Ipv4Prefix.N])
        ▼
EC2 control plane ──► network-interface (eni-…) ── secondary IPs / IPv4 prefixes
        ▲                    │
        │                    ├─ customer-managed ENI  → unassign allowed
        └─ IAM authz          └─ requester-managed ENI → doc says unassign PROHIBITED (prose/control-plane, not IAM)
           (8 condition keys,       (operator = AWS service account)
            whole-NIC granularity)
```

---

## 3. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| IAM principal A (team/role A) | ENI owned by same account, "belongs to" team B | `UnassignPrivateIpAddresses` with NIC-level (not IP-level) grant | A removes a secondary IP/VIP on an ENI the policy author intended B-only → **intra-account teardown**; or A re-homes it to A's ENI → **traffic interception** |
| Customer IAM principal | **Requester-managed ENI** (AWS service operates it) | Same API against a `requester-managed=true` ENI | the unassign **succeeds** (or mutates IPs) on a service-managed ENI despite the documented prohibition → **control-plane enforcement break** (availability of the managed service) |
| Customer IAM principal | ENI in **another AWS account** | naming a foreign `eni-…` | a foreign ENI's IP is unassigned → **cross-account breach (Critical)** — expected impossible (resource is account-scoped); confirm as guarantee |
| Caller request context | AWS **service plane** | reaching the operator (service) identity of a managed ENI | any identity/credential/ARN of the AWS fleet → **HARD STOP**, disclosure |

---

## 4. API / Interface Inventory (the action and its authorization twins)

| Name | Mutating | Resource | Condition keys (on NIC resource) | Notes |
|---|---|---|---|---|
| **UnassignPrivateIpAddresses** (target) | Write | `network-interface*` | 8-key set (see §2) — **incl. `ec2:ManagedResourceOperator`** | removes secondary IPv4 + IPv4 prefixes; no IP/prefix-value key |
| AssignPrivateIpAddresses (write twin) | Write | `network-interface*` | **identical 8-key set** | adds secondary IPv4/prefixes; has `AllowReassignment` (chain) |
| AssignIpv6Addresses | Write | `network-interface*` | **identical 8-key set** | IPv6 analogue |
| UnassignIpv6Addresses | Write | `network-interface*` | **identical 8-key set** | IPv6 analogue |
| ModifyNetworkInterfaceAttribute | Write | `instance`/`network-interface*`/`security-group`/`subnet` | NIC leg **adds** `ec2:Attribute` + `ec2:Attribute/${AttributeName}` | the one sibling with per-attribute scoping |
| DetachNetworkInterface | Write | `instance*`/`network-interface*` | 8-key set | teardown twin |
| DeleteNetworkInterface | Write | `network-interface*` | 8-key set | teardown twin (detached only) |
| CreateTags / DeleteTags on NIC | Write | `network-interface*` | `aws:RequestTag`/`aws:TagKeys`/`ec2:NetworkInterfaceID`/… | **self-tag channel** → can widen a tag-keyed Unassign grant |

**Key structural observations (confirmed from the reference):**
- **The Assign/Unassign × Private/IPv6 family is fully condition-key-SYMMETRIC** (all four share the identical 8-key set). → The usual "attribute-family / twin asymmetry" crown jewel (Lens X/S) is a **genuine NULL** here. Documented honestly below.
- **No IP-value or prefix-value condition key exists anywhere in the EC2 catalog** (no `ec2:PrivateIpAddress`, `ec2:SecondaryIp`, `ec2:Ipv4Prefix`; the only IP-valued key, `ec2:PublicIpAddress`, is **elastic-ip-only**). → whole-NIC-only scoping. This is the primary crown jewel (Area 1).
- `ec2:ManagedResourceOperator` is present on Unassign but is an **AWS-internal service-linked-role operator key** (value = a service operator string), *not* a customer control for managed ENIs; the requester-managed prohibition is a **control-plane guard** (Area 2 / Lens U).
- **An AWS-managed, customer-attachable policy (`AmazonVPCCrossAccountNetworkInterfaceOperations`) grants Unassign on `Resource:"*"` with no condition** → Area 2b / Lens R, the default delivery vector for Areas 1 & 3.
- `ec2:Vpc` and `ec2:Subnet` bind the **NIC's own** VPC/subnet (the correct target for this action — not the mis-binding seen on `AssociateSecurityGroupVpc`).

---

## 5. Recommended Areas of Focus

### Area 1 — IP/prefix-value scoping gap: Unassign is scopable only at whole-NIC granularity (PRIMARY)
**Background.** The action takes `PrivateIpAddress.N` and `Ipv4Prefix.N`, i.e. it operates at the granularity of an individual IP/prefix. But none of the 8 condition keys — nor any key in the entire EC2 condition-key catalog — can name an IP or prefix value. The finest IAM scoping available is the whole network interface (`ec2:NetworkInterfaceID`, `ec2:Subnet`, `ec2:Vpc`, `aws:/ec2:ResourceTag`).
**Security Concern.** A policy author who wants "principal may manage the app's own extra IPs but must not disturb the failover VIP / cluster virtual IP / a sibling container's secondary IP on the shared ENI" **cannot express that in IAM.** Any principal allowed to unassign *one* secondary IP on a NIC can strip **all** of them (and all IPv4 prefixes). This is the same structural shape confirmed for `RevokeSecurityGroupIngress` (scopable only at whole-SG granularity; no rule-ID key) — see `RevokeSecurityGroupIngress-attack-research-plan.md`.
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** No EC2 condition key constrains the IP/prefix value. → **Mechanism:** full grep of the ~148-row `list_ec2.md` condition-key master table (L~9990–10190) returns no `*PrivateIp*`/`*SecondaryIp*`/`*Prefix*`/`*IpAddress*` key — the **only** IP-valued key is `ec2:PublicIpAddress`, which applies solely to the **`elastic-ip`** resource, never to ENI private IPs/prefixes. → **Oracle:** author a policy attempting `StringEquals "ec2:PrivateIpAddress": "10.0.0.82"` and show IAM policy-sim treats the key as never-present (unconstrained allow). → **Severity:** Medium (availability/teardown; High where a cross-team shared ENI carries a load-bearing VIP).
- **Claim:** A grant intended for "manage secondary IPs on ENI X" lets the holder remove a specific protected VIP on X. → **Oracle:** `iam:SimulatePrincipalPolicy` for `ec2:UnassignPrivateIpAddresses` on `eni-X` returns `allowed` regardless of which `PrivateIpAddress.N` is supplied (the sim has no IP context to differentiate). → **Severity:** Medium–High.
**Doc evidence:** API_UnassignPrivateIpAddresses params; list_ec2.md condition-key catalog (absence). **Severity-if-true:** Medium–High (availability).

### Area 2 — Requester-managed ENI prohibition: a control-plane (not IAM) guarantee; enforcement-parity across InterfaceType (Lens U + X)
**Background.** `requester-managed-eni.html` ("Considerations") states that on a requester-managed network interface you **cannot** "Assign or unassign private IP addresses" (also cannot modify attributes / attach / detach / associate EIP / specify at launch), **but you *can* still reset network interface attributes** and add/remove tags. `using-eni.md` (L74–75): "created and managed by AWS services… You can't manage these network interfaces yourself." **The prohibition is enforced by an EC2 control-plane resource-state guard keyed off the ENI's `requester-managed` attribute — independent of IAM**, and documented *only* in the User Guide concept page, **not** in the API reference's Errors section (a practitioner reading only the API ref would never learn of it — doc-gap).
> **Correction vs first draft (confirmed by subagent IAM survey):** `ec2:ManagedResourceOperator` is **NOT** the customer's lever for this. The service-authorization reference (L10111) defines it as "Filters access by the presence of an EC2 operator provisioning a managed resource" — a String whose value is an AWS **operator service identifier** (`scaler.lambda.amazonaws.com`, `network-connectors.lambda.amazonaws.com`, `workspaces-instances.amazonaws.com`, `bedrock-agentcore.amazonaws.com`). Every observed use is an **Allow**-side `StringEquals` inside **AWS's own service-linked-role** policies to scope the *service operator's* reach — never a customer-facing Deny. The actual customer-side protection is the control-plane guard above (and, where customers want their own ABAC, a **resource tag**, as `BedrockAgentCoreNetworkServiceRolePolicy` does with `aws:ResourceTag/AmazonBedrockAgentCoreManaged=true`), not `ManagedResourceOperator`.
**Security Concern.** A guarantee enforced by control-plane logic (rather than IAM) is only as good as its coverage of every managed-ENI **InterfaceType**. The `InterfaceType` enum is open-ended and growing (`interface`, `vpc_endpoint`, `trunk`, `branch`, `efa`, `gateway_load_balancer_endpoint`, `load_balancer`, and the newer `rgw-` **Resource Gateway Interface** shown in the current doc's own CLI output). If the "is this requester-managed?" gate keys off a stale list, a **newer managed-ENI type could fail open to Unassign**, letting a customer principal break the data plane of a managed service in their own account. Also: the "you can still **reset** attributes" carve-out mirrors the `ResetInstanceAttribute` one-way-ratchet shape — reset may move a managed ENI toward a less-safe default even where modify is blocked.
**High-level Test Scenarios:**
- **Claim:** `UnassignPrivateIpAddresses` on a `requester-managed=true` ENI is rejected for **every** current InterfaceType. → **Oracle (behavioral, authorized account only):** against the tester's own managed ENIs, confirm the API returns an authorization/validation error; look for any InterfaceType (esp. the newest, e.g. Resource Gateway `rgw-`) where it is **not** rejected. → **Severity:** High if any type fails open (managed-service availability); else documents the guarantee.
- **Claim:** the "can still reset attributes" carve-out on a managed ENI changes a security-relevant setting (e.g. source/dest check) toward a less-safe default. → **Oracle:** compare ResetNetworkInterfaceAttribute's effect on a managed ENI vs documented default. → **Severity:** Low–Medium.
**Doc evidence:** requester-managed-eni.html "Considerations" list; using-eni.md L74–75; `ec2:ManagedResourceOperator` definition list_ec2.md L10111. **Severity-if-true:** High (fail-open to a managed ENI) / else confirmed guarantee.

### Area 2b — AWS-managed, customer-attachable policy grants Unassign on `Resource:"*"` with NO condition (Lens R / S — Tier-2, AWS-owned)
**Background.** `AmazonVPCCrossAccountNetworkInterfaceOperations` is an **AWS-managed policy** the docs explicitly say you can "attach … to your users, groups, and roles." Its statements grant `ec2:AssignPrivateIpAddresses` **and** `ec2:UnassignPrivateIpAddresses` on `Resource: "*"` with **no `Condition` block at all**. The EC2 User Guide's own `ExamplePolicies_EC2.md` contains **zero** occurrences of `UnassignPrivateIp` — AWS ships no scoped example to copy instead.
**Security Concern.** Because the policy is AWS-authored and **uneditable / copy-verbatim**, a customer who attaches it to grant the legitimate cross-account-ENI use case **simultaneously** grants unconditioned authority to unassign secondary IPs/prefixes on **every** ENI in the account (subject only to the Area-2 control-plane guard for requester-managed ENIs). This is the skill's **Tier-2 carve-out** (weak default in an AWS-authored artifact), *not* a customer footgun. It is the delivery vector that makes Area 1 (no IP-value scoping) and Area 3 (takeover chain) reachable by default.
**High-level Test Scenarios:**
- **Claim:** a principal holding **only** `AmazonVPCCrossAccountNetworkInterfaceOperations` can unassign secondary IPs on an arbitrary customer-managed ENI it has no business-level ownership of. → **Oracle:** resolve the live policy with `iam:GetPolicyVersion`, then `iam:SimulatePrincipalPolicy` for `ec2:UnassignPrivateIpAddresses` on a foreign-team `eni-…` under a role holding exactly that policy → expect `allowed` (no condition to deny it). → **Severity:** Medium–High (intra-account over-grant in an AWS-owned artifact).
- **Claim:** no AWS-published scoped alternative exists to steer customers toward. → **Oracle:** grep `ExamplePolicies_EC2.md` / managed-policy reference → confirm absence. → **Severity:** Informational (reinforces the above).
**Doc evidence:** `aws-managed-policy/latest/reference/AmazonVPCCrossAccountNetworkInterfaceOperations` JSON; `ExamplePolicies_EC2.md` (0 hits). **Severity-if-true:** Medium–High, **route `aws-security` (Tier-2)**.

### Area 3 — Unassign→Reassign IP-takeover chain (Lens M + A, intra-account)
**Background.** `AssignPrivateIpAddresses` carries an `AllowReassignment` flag — the API doc: "Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface," and "When you move a secondary private IP address to another network interface, any Elastic IP address … is also moved." So a secondary IP (and any EIP riding on it) can be relocated across ENIs. Unassign frees an IP back to the subnet pool; Assign can then claim it (no `AllowReassignment` needed once free; needed for a one-step steal while still assigned).
**Security Concern.** Chain within one account across trust-separated principals: (1) principal A `UnassignPrivateIpAddresses` removes victim's secondary IP/VIP from `eni-victim`; (2) A `AssignPrivateIpAddresses --allow-reassignment` assigns that same IP to `eni-attacker` in the same subnet; (3) traffic destined to that IP now lands on A's ENI → **traffic interception / service impersonation** (or simple connectivity denial if left unassigned). Both legs are scopable only at whole-NIC granularity (Area 1), so a broad `network-interface/*` grant makes this trivial.
**High-level Test Scenarios:**
- **Claim:** `AllowReassignment=true` moves a secondary IP across ENIs without the losing ENI's owner's consent (only the caller's NIC-level perms on each ENI are checked). → **Oracle:** `iam:SimulatePrincipalPolicy` shows both Unassign on `eni-victim` and Assign on `eni-attacker` allowed under A's policy; doc confirms reassignment semantics. → **Severity:** High (intra-account traffic interception) — **explicitly intra-account, not cross-account.**
- **Claim:** the chain needs only a wildcard `network-interface/*` Write grant, which Area 1 shows cannot be narrowed to protect a specific IP. → **Oracle:** policy composition review. → **Severity:** High as a least-priv footgun on a shared VPC.
**Doc evidence:** API_AssignPrivateIpAddresses `AllowReassignment`; multiple-ip-addresses.html. **Severity-if-true:** High (intra-account).

### Area 4 — Cross-account / cross-tenant reach (Lens A) — expected NEGATIVE, confirm as guarantee
**Background.** Resource type is `network-interface*`, account-scoped ARN `arn:${Partition}:ec2:${Region}:${Account}:network-interface/${NetworkInterfaceId}`. `eni-` IDs appear in AWS's own reference pages in both legacy 8-hex (`eni-197d9972`) and current 17-hex (`eni-01d32da61c165ac3e`) forms — partly enumerable, but access is bound by the account segment of the ARN, not ID secrecy.
**Security Concern.** If authorization checked existence rather than ownership, a foreign `eni-…` could be named.
**High-level Test Scenarios:**
- **Claim:** naming a foreign-account `eni-…` is rejected (ownership-bound, not existence-bound). → **Oracle:** the call returns `AccessDenied`/`InvalidNetworkInterfaceID.NotFound` for a foreign ENI under a scoped role; **do not** rely on DryRun (caller-IAM-only). → **Severity:** Critical **if** it ever succeeds (cross-account); otherwise a confirmed guarantee.
- **Claim:** error-string / latency differences between "not found" and "access denied" form an enumeration oracle for foreign ENI existence. → **Oracle:** compare responses for known-foreign vs random `eni-…`. → **Severity:** Low (enumeration only).
**Doc evidence:** list_ec2.md resource definition; elastic-network-interfaces.html ID format. **Severity-if-true:** Critical (if cross-account) / Low (enum oracle).

### Area 5 — Self-tag widening of a tag-scoped Unassign grant (Lens S)
**Background.** A common pattern scopes Unassign by `ec2:ResourceTag/owner` or `aws:ResourceTag`. Tagging a NIC is a separate action (`CreateTags`/`DeleteTags` on `network-interface`).
**Security Concern.** If the principal that holds a tag-keyed Unassign grant can **also** tag NICs, it can self-assign the gating tag onto a NIC it should not control, widening its own blast radius (classic ABAC self-widening). Unassign itself has **no** `aws:RequestTag` (can't tag in-call), so the widening requires a separate `CreateTags` grant.
**High-level Test Scenarios:**
- **Claim:** a principal with `ec2:CreateTags` on `network-interface/*` + tag-keyed Unassign can tag a foreign-team NIC with the gating value, then unassign its IPs. → **Oracle:** `iam:SimulatePrincipalPolicy` for CreateTags then UnassignPrivateIpAddresses under the self-applied tag. → **Severity:** Medium–High (defeats the ABAC control).
**Doc evidence:** CreateTags NIC row (list_ec2.md); `aws:/ec2:ResourceTag` on Unassign. **Severity-if-true:** Medium–High (where ResourceTag is the access-control mechanism).

### Area 6 — Audit / observability (Lens O, enabler)
**Claim:** UnassignPrivateIpAddresses is CloudTrail-logged with `networkInterfaceId` and the IP/prefix list. → **Oracle:** confirm the event records *which* IPs were removed (not just the NIC). If the IP list is omitted from the record, teardown of a specific VIP is harder to attribute. → **Severity:** Low–Informational (raises Area 1/3 severity as an enabler).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Strip a protected VIP via whole-NIC grant | IAM scoping of Unassign | *(none — no IP-value condition key)* → Area 1 |
| Default over-grant via AWS-managed policy | `AmazonVPCCrossAccountNetworkInterfaceOperations` | *(none — unconditioned `Resource:"*"`)* → Area 2b |
| Unassign IPs on a service-managed ENI | requester-managed ENI gate | control-plane prohibition ("can't assign/unassign private IPs") → Area 2 |
| Enum-type fail-open on new InterfaceType | managed-ENI gate coverage | prose guarantee vs InterfaceType enum → Area 2 |
| IP takeover via Unassign→Assign(AllowReassignment) | AssignPrivateIpAddresses | NIC-level perms only; no IP-level scoping → Area 3 |
| Cross-account unassign of a foreign ENI | resource ownership binding | account-scoped `network-interface*` ARN → Area 4 (expected deny) |
| ABAC self-widening via self-tagging the NIC | CreateTags + ResourceTag condition | tag-write separation of duties → Area 5 |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Operating on a requester-managed ENI within the tester's OWN account is NOT a cross-account/service-plane breach by itself** — the ENI is in the customer account; the AWS operator identity is not reachable through this API. Breaking a managed service's data plane this way is an **availability** concern (in scope as Area 2 only if the documented prohibition fails open). Reaching the operator **service account's** identity/credentials = **HARD STOP** + disclosure.
- Unassigning the **primary** private IPv4 address — not possible by design (only secondary IPs/prefixes); not a finding.
- Customer-authored over-broad `network-interface/*` grants are a **customer least-privilege footgun** unless they ship in an **AWS-authored** sample/managed policy (then Area 2/Lens R applies, Tier-2).
- Single-tenant self-DoS, IMDS on managed hosts, DNS rebinding against private-only endpoints, product/feature-parity gaps.
- Live memory-safety/parser fuzzing of the EC2 front-end — out of scope for a documentation plan (no parser surface exposed by this simple query API).

---

## 8. Null Hypotheses / Doc Gaps (lenses checked that did not fire)
- **Lens X / S (attribute-family & twin asymmetry) — NULL.** Confirmed: `AssignPrivateIpAddresses`, `UnassignPrivateIpAddresses`, `AssignIpv6Addresses`, `UnassignIpv6Addresses` carry the **identical** 8 condition keys and the same `network-interface*` resource. No fail-open asymmetry across the family. (The only asymmetric sibling, `ModifyNetworkInterfaceAttribute`, *adds* `ec2:Attribute` — a tightening, not a gap, and a different operation.) Pages checked: list_ec2.md rows for all four actions + Modify/Detach/Delete.
- **Lens B / C (PassRole / credential vending) — N/A.** The action takes no role ARN, token, or credential; it neither assumes nor vends. Pages checked: API reference (params = NIC + IPs/prefixes only), list_ec2.md (no `iam:PassRole` dependency).
- **Lens G (SSRF) — N/A.** No field is a URL/host the service dereferences. Pages checked: API reference, example page.
- **Lens Q (upload) — N/A.** No blob/file input. Pages checked: API reference.
- **Lens H / W (KMS / attestation) — N/A.** No encryption-context or attestation parameter. Pages checked: list_ec2.md condition keys (no `kms:*`).
- **Lens F (injection) — N/A.** Inputs are a NIC ID and IP/prefix strings validated as network objects; no translation/query layer. Pages checked: API reference.
- **Lens Y / BB / CC / DD / FF (transport/sig, canonicalization, upstream-context, cache, JWT) — N/A** for this SigV4 EC2 query API. Doc-gap note: internal EC2 front-end hop behavior is undocumented; not a lead at the documentation layer.
- **Doc-gap — confirm surface first:** whether the requester-managed prohibition (Area 2) is enforced uniformly across *all* current `InterfaceType` values is not stated per-type in the docs; this must be confirmed behaviorally in an authorized account before Area 2 can be rated.

---

*Hunter handoff: start at Area 1 (structural, confirmable by `iam:SimulatePrincipalPolicy` alone), then Area 2 (behavioral, needs an authorized account with managed ENIs of varied InterfaceType), then Area 3. Area 4 is a guarantee to confirm negative. Use synthetic/canary ENIs only; tear down anything created; honor the HARD STOP in §0/§7.*
