# Change the security groups for your EC2 instance — Attack Research Plan

Source of leads: `UserGuide/changing-security-group.html` (offline `docs/AWSEC2/latest/UserGuide/changing-security-group.md`; verified identical online 2026-10-15) + IAM Service Authorization Reference `docs/service-authorization/latest/reference/list_ec2.md` (`ModifyInstanceAttribute` L8806–8810, `ModifyNetworkInterfaceAttribute` L8966–8972, `ModifySecurityGroupRules` L8998–9003; keys `ec2:Attribute` L10051, `ec2:SecurityGroupID` L10152, `ec2:Vpc` L10172). Status: documentation-derived hypotheses only; nothing tested against a live account.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.
- **Scope boundary vs sibling plans (do NOT duplicate):** this page is the **SG-membership-change** page. Its net-new surface is the `ModifyInstanceAttribute --groups` action (reassign the SG *set* bound to an instance's primary ENI) and its twin `ModifyNetworkInterfaceAttribute`. The page's second half ("Configure security group rules" = `Authorize*`/`Revoke*`/`ModifySecurityGroupRules` rule-CONTENT editing) is already owned by:
  - `ec2-security-groups-attack-research-plan.md` (chapter HUB, H1–H7: stateful-response egress bypass, self-ref mesh, most-permissive-wins/no-rule-content-key, 4 Describe oracles, AssociateSecurityGroupVpc, re-peering un-stale, prefix-list unshare, doc footguns).
  - `ec2-security-groups-privatelink-attack-research-plan.md` (cluster, Areas 1–8).
  - `creating-security-group-attack-research-plan.md` (CreateSecurityGroup create action).
  - `modify-network-interface-attributes-attack-research-plan.md` (ENI attribute surface, including the SG row on an ENI).
  Rule-content material here is cross-referenced, not re-derived. This plan owns the **membership-reassignment primitive and the twin-action parity gap** that no sibling covers.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes a hunter should try to produce:
1. **Firewall-swap without the SG-target scoping holding.** Attach an attacker-chosen, wide-open security group (`0.0.0.0/0:22`) to a victim/compliance-locked instance's primary ENI via `ModifyInstanceAttribute --groups`, where the operator's IAM intended to pin which SGs may be attached — proving the SG-target row was omittable or inert.
2. **Twin-action Deny bypass.** Perform the same primary-ENI SG-membership change through `ModifyNetworkInterfaceAttribute` when a Deny/boundary policy was written only against `ec2:ModifyInstanceAttribute` (or vice-versa) — proving the two actions reach one outcome under different required-resource authorization.
3. **`ec2:Attribute` Deny fail-open.** Defeat a Deny keyed on `ec2:Attribute`/`ec2:Attribute/${AttributeName}` that was meant to stop SG reassignment, via casing/enum-value mismatch between the Deny string and the value the request populates.
4. **`ec2:Vpc` mis-binding.** Show that an operator's "only attach SGs from VPC X" intent, expressed with `ec2:Vpc` on the security-group row, binds the *SG's* home VPC and does not constrain the *instance's* VPC, enabling a cross-VPC membership mismatch.
5. **Doc-footgun self-inflicted exposure/DoS.** Demonstrate that copy-verbatim of the page's mislabeled `revoke-security-group-*` CLI examples removes the opposite-direction rule from intent (inbound↔outbound swap) → over-exposure or self-DoS.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** SigV4 EC2 control-plane APIs + console (`Actions → Security → Change security groups`) + PowerShell. No data-plane/wire-protocol component on this page.

**The resource under change.** A **security group *membership* set** bound to a **network interface**. The page's load-bearing sentence: *"Security groups are associated with network interfaces. Adding or removing security groups changes the security groups associated with the primary network interface."* So "change the instance's security groups" is really "replace the SG set on the instance's **primary ENI**." Secondary-ENI SG changes go through `ModifyNetworkInterfaceAttribute` (page links `modify-network-interface-attributes.html`).

**Two distinct capabilities on one page:**
- **(a) Membership reassignment** — `ModifyInstanceAttribute(groups=[…])` / `ModifyNetworkInterfaceAttribute(Groups=[…])`. Replaces *which* SGs apply. **This plan's subject.**
- **(b) Rule-content editing** — `Authorize*`/`Revoke*`/`ModifySecurityGroupRules`. Edits what a given SG *permits*. Owned by sibling plans.

**Key design facts from the IAM reference (confirmed):**
- `ModifyInstanceAttribute` authorizes against **three** resource rows: `instance*` **(required)**, `security-group` **(not required — no `*`)**, `volume` (not required). The `--groups` call engages the non-required `security-group` row only when a group set is supplied.
  - `instance*` keys: `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:InstanceID`, `ec2:ResourceTag`, `ec2:Tenancy`, `ec2:Region`, … (full instance key set).
  - `security-group` keys: `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag`, **`ec2:SecurityGroupID`**, **`ec2:Vpc`**. (This is the *only* lever over *which* SG you may attach.)
- `ModifyNetworkInterfaceAttribute` authorizes against **four** rows: `instance` **(not required)**, `network-interface*` **(required)**, `security-group` (not required), `subnet` (not required).
  - `network-interface*` keys: `ec2:NetworkInterfaceID`, `ec2:Subnet`, `ec2:Vpc`, `ec2:ResourceTag`, `ec2:Attribute(/Name)`, `ec2:Region`.
  - `security-group` keys: identical to above (`ec2:SecurityGroupID`, `ec2:Vpc`, `ec2:ResourceTag`, `ec2:Region`).
- `ModifySecurityGroupRules` rows: `security-group*` (required; `ec2:SecurityGroupID`/`ec2:Vpc`/`ec2:ResourceTag`/`ec2:Region`), `security-group-rule*`, `prefix-list`. **No condition key over rule *content* (CIDR/port/protocol/direction)** — identical to the `Authorize*` posture (HUB H3). The page's own CLI example modifies a rule to `CidrIpv4=0.0.0.0/0`.

```
caller (SigV4 / console)
   │
   ├── ModifyInstanceAttribute(groups=[sg…])  ──auth──> required:[instance*]  +  optional:[security-group]
   │        (replaces SG set on PRIMARY ENI)                    │                        │
   │                                                     instance-keyed             SG-keyed (SecurityGroupID/Vpc/Tag)
   │                                                                                  ↑ SAME primary-ENI outcome
   └── ModifyNetworkInterfaceAttribute(Groups=[sg…]) ─auth─> required:[network-interface*] + optional:[instance, security-group, subnet]
            (replaces SG set on ANY ENI incl. primary)          │
                                                          ENI-keyed (NetworkInterfaceID/Subnet/Vpc/Tag)
```

The two arrows converge on one physical effect (SG set on the primary ENI) through two different *required* authorization anchors — the core seam of this page.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| IAM principal with instance-scoped write | the SG *set* on its primary ENI | `ModifyInstanceAttribute --groups` | A permissive/attacker SG becomes attached where the operator's SG-target scoping (`ec2:SecurityGroupID`/`ec2:ResourceTag`/`ec2:Vpc` on the SG row) was intended to block it → **membership-scoping breach** |
| Principal Denied `ModifyInstanceAttribute` on an instance | same primary-ENI SG set | `ModifyNetworkInterfaceAttribute(Groups=…)` on the ENI | ENI-route call succeeds and the primary ENI's SG set changes where the instance-anchored Deny refuses → **twin-action authorization-parity breach** |
| Operator Deny on SG-reassignment keyed by `ec2:Attribute` | the membership change | request populates the attribute value with a casing/enum the Deny string does not match | the reassignment succeeds despite the Deny → **condition-key fail-open** |
| Operator "SGs from VPC X only" (`ec2:Vpc`) | an instance in a *different* VPC | `ec2:Vpc` binds the SG's VPC, not the instance's | SG from VPC X attached to an instance whose ENI is in VPC Y (or the reverse scoping intent fails) → **wrong-resource key binding** |
| Low-priv principal who can edit SG rules | all instances sharing that SG (incl. cross-account via shared VPC) | `ModifySecurityGroupRules` → `0.0.0.0/0` | rule change propagates instantly to every associated resource — *owned by HUB H1/H3*, cross-ref only |
| Service plane | — | — | **HARD STOP** if any membership/attribute change surfaces an AWS-owned SG/ENI/account |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|
| `ec2:ModifyInstanceAttribute` (`--groups`) | SigV4 / console / PowerShell | **Yes** | Yes | holder of the action on `instance*` (+ `security-group` row if present) | **Replaces** the SG set on the **primary ENI**; required anchor = instance. Primary net-new action. |
| `ec2:ModifyNetworkInterfaceAttribute` (`Groups`) | SigV4 / console / PowerShell | **Yes** | Yes | holder of the action on `network-interface*` (+ optional instance/SG/subnet rows) | **Twin** that reaches the same primary-ENI SG set; required anchor = ENI, instance row is non-required. Page links it for secondary ENIs but it also governs the primary ENI. |
| `ec2:AuthorizeSecurityGroupIngress`/`Egress` | SigV4 / console | Yes | Yes | SG write holder | Rule-content add. **Owned by HUB.** |
| `ec2:RevokeSecurityGroupIngress`/`Egress` | SigV4 / console | Yes | Yes | SG write holder | Rule-content remove. **Owned by HUB.** Page CLI examples mislabeled (Area 5). |
| `ec2:ModifySecurityGroupRules` | SigV4 / console | Yes | Yes | SG write holder (`security-group*`+`security-group-rule*`) | Rule-content modify; no rule-content condition key; page example widens to `0.0.0.0/0`. Cross-ref HUB H3. |

Console-hidden / parameter note: the console "Change security groups" dialog only *adds/removes* against the current set; the API `--groups` takes a **full replacement list** — a caller can clear every existing SG in one call. No undocumented auth-weakening enum found on these actions (contrast `ModifyInstanceAttribute(userData)` which is the known privesc attribute — out of scope for this SG page but note it shares the action).

---

## 5. Recommended Areas of Focus

### Area 1 — Twin-action authorization parity: ModifyInstanceAttribute vs ModifyNetworkInterfaceAttribute (Lens X) — HEADLINE
**Background.** The page says changing an instance's SGs changes the SGs on its **primary network interface**, and points to `ModifyNetworkInterfaceAttribute` for secondary ENIs. But `ModifyNetworkInterfaceAttribute(Groups=…)` operates on **any** ENI including the primary. So the *same* primary-ENI SG set is mutable by two IAM actions whose **required** resources differ: `ModifyInstanceAttribute` is anchored on `instance*` (instance tags / `ec2:InstanceID`); `ModifyNetworkInterfaceAttribute` is anchored on `network-interface*` (`ec2:NetworkInterfaceID` / `ec2:Subnet` / ENI tags), with the `instance` row **non-required**.
**Security Concern.** A boundary/Deny policy an operator writes to stop SG reassignment of a protected instance — e.g. `Deny ec2:ModifyInstanceAttribute` on instances tagged `pci=true` — does **not** cover the ENI twin. If the primary ENI is not tagged/scoped the same way (ENIs frequently inherit no tags, or different ones), the twin reaches the identical outcome unblocked.
**High-level Test Scenarios.**
- **Claim:** A principal explicitly Denied `ec2:ModifyInstanceAttribute` on a target instance can still change that instance's primary-ENI SG set via `ec2:ModifyNetworkInterfaceAttribute`. → **Mechanism:** two actions, different required anchors (L8808 `instance*` vs L8968 `network-interface*`); page text ties both to the primary ENI. → **Oracle:** after the ENI-route call, `DescribeInstances`/`DescribeNetworkInterfaces` shows the new SG set on the primary ENI while the instance-route call returns `AccessDenied`. → **Pre:** control an instance + its primary ENI id; a Deny scoped to one action/anchor. → **Cost:** 2 API calls. → **Severity:** High (boundary bypass; Critical if the protected instance is a compliance/isolation asset reachable cross-tenant via shared VPC).
- **Claim (reverse):** A Deny on `ModifyNetworkInterfaceAttribute` keyed on ENI tags is bypassed by `ModifyInstanceAttribute --groups` (instance-anchored).
- **Variant (Lens X error-divergence):** compare validator strictness/ownership errors between the two actions when fed a foreign SG id or foreign ENI id (enumeration oracle).
**Doc evidence.** `changing-security-group.md` L10 ("Security groups are associated with network interfaces … changes the SGs associated with the primary network interface"); `list_ec2.md` L8806–8810, L8966–8972. **Severity-if-true:** High–Critical.

### Area 2 — SG-target row is non-required: *which* SG you may attach is often unscoped (Lens S / U)
**Background.** On both membership actions the `security-group` resource row is **not required** (no `*`). The *only* levers over which SG may be attached are `ec2:SecurityGroupID`, `ec2:ResourceTag` (on the SG), and `ec2:Vpc`, all on that optional row. A policy that scopes only the **required** resource (the instance / the ENI) and omits an SG-row statement authorizes attaching **any** security group.
**Security Concern.** An operator reasons "they can only modify instances they own" and grants `ModifyInstanceAttribute` on `instance` scoped by instance tag. Nothing then constrains the SG argument → the holder attaches a self-created `0.0.0.0/0:22`/`:3389` SG (or any SG visible in the VPC) to their own compliance-locked instance, instantly opening it. The membership swap takes effect on a `running` instance with **no restart** (page: instance must be `running` or `stopped`).
**High-level Test Scenarios.**
- **Claim:** With `ModifyInstanceAttribute` granted only via an instance-scoped statement (no SG-row condition), a caller can attach an arbitrary permissive SG. → **Oracle:** `SimulatePrincipalPolicy` for `ModifyInstanceAttribute` with a `security-group` resource context shows Allow regardless of the SG id; live confirm under a scoped canary role by attaching a canary open-SG, then `DescribeInstances`. → **Pre:** scoped instance-write role; ability to create or name an open SG in-VPC. → **Cost:** low. → **Severity:** Medium–High (self-inflicted exposure of a governed instance; High when the instance carries cross-tenant reachability).
- **Claim:** `ec2:SecurityGroupID`/`ec2:ResourceTag` on the SG row, *when present*, correctly bounds the attach to approved SGs (positive control — prove the lever works so the omission is the defect, not the key).
**Doc evidence.** `list_ec2.md` L8809 / L8970 (SG row, no `*`); keys L10152 (`ec2:SecurityGroupID`), L10172 (`ec2:Vpc`). **Severity-if-true:** Medium–High (customer-authored policy gap, but the *non-required-row* shape is an AWS design footgun worth noting; frame as hardening/least-priv guidance, Tier-2 only if an AWS-published sample policy omits the SG row — cross-check `iam-policies-ec2-console.html#ex-security-groups`, which this page sends operators to for "Required permissions").

### Area 3 — `ec2:Attribute` / `ec2:Attribute/${AttributeName}` casing & value fail-open (Lens S variant c)
**Background.** Both membership actions (and `ModifyInstanceAttribute` generally) expose `ec2:Attribute` ("Filters access by an attribute of a resource", String, L10051) and `ec2:Attribute/${AttributeName}`. An operator wanting to allow instance edits but forbid SG reassignment would write `Deny … when ec2:Attribute …` naming the SG attribute. The confirmed corpus pattern: a Deny written against one casing/enum is **inert** when the request populates the key with a different casing/field name (the `ec2:Attribute` case-sensitivity fail-open).
**Security Concern.** The underlying attribute for SG reassignment is historically `groupSet` (EC2 API) vs the CLI surface `--groups` vs console "security groups." If the condition value the service evaluates (`groupSet`) differs from what an operator guesses (`groups`, `securityGroups`, `GroupSet`), a `Deny StringEquals ec2:Attribute:"groups"` never matches and the reassignment proceeds.
**High-level Test Scenarios.**
- **Claim:** A `Deny ModifyInstanceAttribute` conditioned on `ec2:Attribute`/`ec2:Attribute/${AttributeName}` targeting SG reassignment can be bypassed because the evaluated attribute token differs in case/spelling from the policy string. → **Oracle:** author the Deny with the "obvious" value, call `--groups`, observe Allow; then enumerate which exact token (`groupSet`?) the key actually carries by binary-searching Deny values via `SimulatePrincipalPolicy`. → **Pre:** a scoped role + a Deny you author on a canary. → **Cost:** low (simulate-first). → **Severity:** Medium (High where this Deny is the sole control separating "edit instance" from "re-firewall instance").
- **Adjacent:** confirm whether `StringEqualsIgnoreCase` is required and whether the docs anywhere state the attribute token — if undocumented, mark **doc-gap** and recommend the hunter record the real token for the HUB.
**Doc evidence.** `list_ec2.md` L10051 (`ec2:Attribute`); L8808 (both keys on the instance row). **Severity-if-true:** Medium–High.

### Area 4 — `ec2:Vpc` binds the SG's home VPC, not the attach target (Lens S variant b)
**Background.** `ec2:Vpc` = "Filters access by the ARN of the VPC" (L10172) and appears on the `security-group` row of both membership actions **and** on the `network-interface*`/`subnet`/`instance` context of `ModifyNetworkInterfaceAttribute`. The confirmed corpus caveat: `ec2:Vpc` can evaluate to a *security group's* home VPC rather than the *target* of the operation.
**Security Concern.** An operator writing "only let SGs from VPC `vpc-prod` be attached" via `Condition {ec2:Vpc: vpc-prod-arn}` on the SG row is binding the **SG's** VPC — which is tautologically true for any SG that already lives in `vpc-prod` — and does **not** constrain the **instance/ENI's** VPC. Conversely, a condition intended to pin the *instance's* VPC placed on the wrong row silently does nothing. (SGs cannot in fact be attached across VPCs for a normal ENI, so the live impact is likely a **false sense of scoping** / inert condition rather than cross-VPC attach — the hunter should determine which, and whether shared-VPC / `AssociateSecurityGroupVpc` relaxes it — cross-ref HUB H5.)
**High-level Test Scenarios.**
- **Claim:** `ec2:Vpc` on the membership actions does not let an operator constrain the *instance's* VPC; a condition meant to do so is vacuous. → **Oracle:** `SimulatePrincipalPolicy` with SG-in-VPC-A vs instance-in-VPC-B contexts; observe which VPC the key resolves to. → **Severity:** Low–Medium (inert-control / wrong-resource binding; raises to Medium when combined with HUB H5 cross-VPC SG association).
**Doc evidence.** L8809/L8970 (`ec2:Vpc` on SG row); L10172. **Severity-if-true:** Low–Medium.

### Area 5 — Doc footguns in the page's CLI examples (Lens U / R-sample-code)
**Background.** Confirmed identical online and offline (2026-10-15), so these are real AWS doc defects, not a mirror sync artifact:
1. **Swapped revoke labels.** Under *"To remove an inbound rule"* the example runs `aws ec2 revoke-security-group-**egress**`; under *"To remove an outbound rule"* it runs `revoke-security-group-**ingress**` (`changing-security-group.md` L146–160). A copy-verbatim operator removes the **opposite-direction** rule from intent.
2. **Invalid flag typo.** All three revoke/modify CLI examples use `--group id` (space) instead of `--group-id` (L150, L158, L167) — the command errors, inviting the operator to "fix" it hastily and mis-target.
3. **`0.0.0.0/0` in the modify example.** The `modify-security-group-rules` example sets `CidrIpv4=0.0.0.0/0` (L168) directly beneath the SSH/RDP exposure Warning — an AWS-authored sample that widens a rule to the entire internet.
**Security Concern.** AWS-authored, copy-paste runbook content → operator-inflicted over-exposure (removed the wrong direction's deny; pasted the open-world CIDR) or self-DoS (revoked egress thinking ingress). Low severity individually but AWS-owned and reportable as doc-quality defects; same class as HUB H7.
**High-level Test Scenarios.** No live test — static doc defect. Confirm/Refute oracle = the quoted lines above. Recommend filing to doc-owners and the SG HUB. **Severity-if-true:** Low / Informational (AWS-authored content defect; cross-ref HUB H7 which already tracks the swapped-label item).

### Area 6 — Membership swap as an exposure/kill-chain primitive (Lens A/E adjacency, chaining)
**Background.** `ModifyInstanceAttribute --groups` is a single, no-restart, running-instance firewall change. It does not call `iam:PassRole` and is not itself a privesc, but it is a high-value **delivery primitive**: it changes *which* firewall applies, independent of rule content.
**Security Concern / chain.** Compose with sibling primitives: (a) attacker creates an open SG (`creating-security-group` plan: open-egress default + no create-time forbid) → (b) `ModifyInstanceAttribute --groups` swaps a victim/own governed instance onto it (this plan, Area 2) → (c) instance is now reachable from the internet / attacker IP; or combine with HUB H2 self-referencing SG to drop a target into a full-mesh SG. Rate at the **end** of the chain (network exposure of a protected workload), not the entry action.
**High-level Test Scenarios.**
- **Claim:** A caller with only instance-write + SG-create (no rule-content grant on the *target's* existing SGs) can still fully expose the instance by swapping SG membership rather than editing rules — bypassing controls that only guard `Authorize*` on known SGs. → **Oracle:** reachability change confirmed via SG set diff on the ENI; no `Authorize*` call made. → **Severity:** High (exposure of a governed instance via an unguarded path).
**Doc evidence.** page L8–L19; `list_ec2.md` membership rows. Cross-ref `creating-security-group` Area 1, HUB H2/H3. **Severity-if-true:** High.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Change primary-ENI SG set via the ENI twin to dodge an instance-anchored Deny | `ModifyNetworkInterfaceAttribute` vs `ModifyInstanceAttribute` | required-resource anchoring (`instance*` vs `network-interface*`) — attack the asymmetry |
| Attach arbitrary permissive SG because SG-row scoping was omitted | optional `security-group` row | `ec2:SecurityGroupID`/`ec2:ResourceTag`/`ec2:Vpc` on the SG row (prove they're the *only* lever and are omittable) |
| Defeat an SG-reassignment Deny via attribute-token casing | `ec2:Attribute`/`ec2:Attribute/${AttributeName}` | string-equality of the attribute value — attack casing/enum mismatch |
| Inert `ec2:Vpc` scoping (binds SG VPC not instance VPC) | `ec2:Vpc` on membership actions | VPC-ARN condition — attack wrong-resource binding |
| Operator removes wrong-direction rule / pastes 0.0.0.0/0 | page CLI examples | the Warning box + example correctness — attack the mislabeled/typo'd samples |
| Full exposure via membership swap without touching rule content | `--groups` replacement semantics | rule-content guards on known SGs — bypass by swapping the SG set |

---

## 7. Out-of-Scope Risk Categories
- **Rule-content semantics** (stateful-response egress bypass, most-permissive-wins, no-rule-content key, self-ref mesh, propagation-SLA) — owned by `ec2-security-groups` HUB (H1–H7) and the cluster/PrivateLink plan. Only cross-referenced here.
- `ModifyInstanceAttribute(userData)` / instance-profile / `$Latest` late-binding privesc — the confirmed PassRole-adjacent exemplar lives on the IAM-roles / launch-template pages, not this SG page.
- Shared-VPC `AssociateSecurityGroupVpc` cross-account SG reach — HUB H5.
- Customer-authored least-privilege footguns where the customer wrote the policy — hardening guidance, not a finding (becomes in-scope only if an **AWS-published** sample policy, e.g. at `iam-policies-ec2-console.html#ex-security-groups`, ships the gap — verify).
- IMDS on managed hosts, product/feature-parity gaps, single-tenant self-DoS.
- Any AWS service-plane SG/ENI/account — **HARD STOP + disclosure**.

## 8. Null hypotheses / doc gaps
- **Lens B / C (PassRole / credential vending):** NULL — read both membership actions and `ModifySecurityGroupRules`; none accepts a role ARN, token, or session-policy input. No fetch-on-behalf.
- **Lens G / Q (SSRF / upload):** NULL — read the whole page (console + CLI + PowerShell for both halves); no field the service dereferences, no blob/upload, no URL. SG rule "source" is a CIDR/SG-id/prefix-list, not a fetched URL.
- **Lens F / Y (injection / transport):** NULL — control-plane SigV4 actions only; no translation layer, no documented `http://` endpoint on this page.
- **Lens K (prompt injection):** NULL — no LLM/agent.
- **Lens H / W (KMS / attestation):** NULL — SGs/ENIs are not encrypted resources; no KMS key or attestation condition on these actions.
- **Lens P / FF / J (proofing / token / OAuth):** NULL — no registration gate, bearer token, or 3P link on this page.
- **Lens AA (share/revoke lifecycle):** N/A on membership change itself; the *rule-content* unshare/stale cases are HUB H6 — cross-ref, not re-derived here.
- **DOC-GAP (confirm live):** (1) the exact attribute token `ec2:Attribute` carries for an SG-set change (`groupSet`? `groups`?) is undocumented — Area 3 hunter must record it; (2) whether `ec2:Vpc` on the SG row resolves to the SG's VPC or the instance's VPC (Area 4) is not stated — simulate to settle; (3) whether an instance-anchored Deny is truly silent on the ENI twin (Area 1) must be confirmed by a scoped live test, not assumed.

---
*Related plans:* `ec2-security-groups-attack-research-plan.md` (HUB), `ec2-security-groups-privatelink-attack-research-plan.md` (cluster), `creating-security-group-attack-research-plan.md`, `modify-network-interface-attributes-attack-research-plan.md`, `iam-policies-ec2-console` (the "Required permissions" sample this page points operators to).
