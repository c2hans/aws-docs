# EC2 `CreateDhcpOptions` — Attack Research Plan

Source of leads: `API_CreateDhcpOptions.html` / `.md`; `API_NewDhcpConfiguration`; EC2 Service Authorization Reference (`/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`); VPC User Guide `VPC_DHCP_Options` / `DHCPOptionSetConcepts` / `DHCPOptionSet`; VPC quotas page. Sibling deep-dive reused: **`ec2-AssociateDhcpOptions-attack-research-plan.md`** (the deploy half of this primitive). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Read this with the sibling.** `CreateDhcpOptions` *authors* a DHCP option set; `AssociateDhcpOptions` *deploys* it onto a VPC. Create alone mints an inert config object — the network-integrity impact materializes only on association. This plan therefore concentrates on what is **distinct to the create/authoring step**: the content-invisibility of IAM at authoring time, tag-on-create self-widening, and the fact that Create is the inseparable first half of a silent VPC-wide DNS/NTP/NetBIOS-hijack kill chain whose second half is already planned.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the AWS Resolver fleet `169.254.169.253` / `.2` address, Time Sync `169.254.169.123`), stop, preserve evidence, flag for AWS-Security. Those are the shared-responsibility line — probing *into* them is out of scope; configuring instances to *use or avoid* them is the in-scope customer knob.

---

## 1. Pentest Objectives (boundary-breach goals)
1. Author a DHCP option set whose `domain-name-servers` / `ntp-servers` / `netbios-name-servers` point at an **attacker-controlled IP**, such that no org IAM guardrail on `ec2:CreateDhcpOptions` could have prevented the malicious *content* (content-invisibility).
2. Prove that an org **cannot** express "DHCP option sets must use `AmazonProvidedDNS`" or "DNS servers must be within the VPC CIDR" via any EC2 condition key on the create action.
3. Via `TagSpecification` on create, **self-assign** the very tag value that a downstream ABAC policy (on Associate/Delete) keys on — defeating tag-based scoping.
4. Demonstrate the Create→Associate **kill chain**: one principal holding `ec2:CreateDhcpOptions` + `ec2:AssociateDhcpOptions` silently repoints DNS/NTP for *every* instance in a VPC within "a few hours", no instance access, no `route53:*`, no restart.
5. Confirm whether the create API performs any **value validation** (IP format, server counts, lease-time bounds) that could be abused for a parser/DoS edge, or bypassed to inject out-of-spec values.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 Query/JSON API action `CreateDhcpOptions` (SigV4, public EC2 endpoint `ec2.<region>.amazonaws.com`). SDK + CLI (`aws ec2 create-dhcp-options`). Console route under VPC → DHCP option sets.

**What it creates.** A **DHCP option set** — resource type `dhcp-options`, ARN `arn:${Partition}:ec2:${Region}:${Account}:dhcp-options/${DhcpOptionsId}`, id shape `dopt-<hex>`. The set is a bag of key/value DHCP options:

| Option key (`NewDhcpConfiguration.Key`) | Value shape | Notes / abuse role |
|---|---|---|
| `domain-name` | free-text string | unqualified-hostname suffix; multi-value quirk on Windows |
| `domain-name-servers` | up to **4** IPs, or literal `AmazonProvidedDNS` | **the DNS-MITM payload** — any IP the instances will trust for resolution |
| `ntp-servers` | up to **8** IPs (4 IPv4 + 4 IPv6) | clock-skew → TLS/SigV4 breakage if hostile |
| `netbios-name-servers` | up to **4** IPs | Windows NTLM-relay / WPAD angle |
| `netbios-node-type` | `1\|2\|4\|8` | |
| `ipv6-address-preferred-lease-time` | 140 … 2147483647 s (≈68 yr per API; concepts page says up to 4294967295 ≈138 yr — **doc inconsistency**, Lens U) | how fast IPv6 instances renew → how fast a hostile set "takes" / how long it "sticks" |

**Immutability (critical design fact).** *"After you create a DHCP option set, you can't modify it. To update the DHCP options for your VPC, you must create a new DHCP option set and then associate it with your VPC."* → **the content is frozen at the moment of `CreateDhcpOptions`.** Create is the *only* authoring moment, and it is exactly the moment IAM has no content condition key. There is no later "ModifyDhcpOptions" surface to gate either.

**Ownership / accounts.** Create acts **only in the caller's own account/region** — no cross-account input, no role ARN, no URL. The set is a passive config object until `AssociateDhcpOptions` binds it to a VPC. Cross-account blast radius lives entirely on the *associate* side (shared-VPC owner→participant), already modeled in the sibling plan. DHCP option sets are **not directly RAM-shareable**.

**Identity.** SigV4 IAM principal. Two IAM actions are consumed when tags are supplied: `ec2:CreateDhcpOptions` **and** `ec2:CreateTags` (see §3).

```
caller (SigV4)
   │  CreateDhcpOptions(DhcpConfiguration=[dns=attacker-ip, ntp=…], TagSpecification=[…])
   ▼
[EC2 control plane]  ── mints dopt-xxxx (content frozen, no content IAM gate) ──┐
   │                                                                            │ (inert until associated)
   ▼                                                                            ▼
AssociateDhcpOptions(dopt-xxxx, vpc-yyyy)  ──►  every instance in vpc-yyyy picks up
                                                 attacker DNS/NTP within "a few hours"
                                                 on DHCP lease renewal — no restart
```

---

## 3. API / Interface Inventory

| Name | Method | Mutating | Internet-callable | Authorized callers | IAM resource types | Condition keys available | Notes |
|---|---|---|---|---|---|---|---|
| **CreateDhcpOptions** | SigV4 | **Yes** (Write) | Yes | any principal w/ `ec2:CreateDhcpOptions` (+ `ec2:CreateTags` if tagging) | `dhcp-options*` (required) | **none on the action row** (Condition-key + Possible-value columns are empty in `list_ec2.md`). At create the `dhcp-options` type exposes `aws:RequestTag/${TagKey}`, `aws:TagKeys`, `ec2:Region`; `ec2:DhcpOptionsID` / `aws:ResourceTag` / `ec2:ResourceTag` are **moot at create** (resource/tag not yet existent) | **No condition key references any option VALUE.** |
| AssociateDhcpOptions | SigV4 | Yes | Yes | `ec2:AssociateDhcpOptions` | `dhcp-options*` + `vpc*` (two legs) | per-leg tag/region only | **deploy half — see sibling plan.** |
| DeleteDhcpOptions | SigV4 | Yes | Yes | `ec2:DeleteDhcpOptions` | `dhcp-options*` | tag/region; `ec2:DhcpOptionsID` usable | can't delete a set in use |
| DescribeDhcpOptions | SigV4 | No (List) | Yes | `ec2:DescribeDhcpOptions` | **none** (no resource type) | **none** | account-wide enum oracle, returns `ownerId` (sibling Area 6) |
| CreateTags | SigV4 | Yes (Tagging) | Yes | `ec2:CreateTags` | many incl. `dhcp-options` | `aws:RequestTag`, `aws:TagKeys`, `ec2:CreateAction`, `ec2:Region`, `ec2:ResourceTag` | the second action implicitly required by tag-on-create |

**Undocumented/knob check:** the API accepts arbitrary `domain-name-servers` IP values (incl. public, private, or link-local) with no console warning; the console does not surface that a custom DNS server can be *any* reachable IP. The `ipv6-address-preferred-lease-time` bound disagrees between API ref (2147483647) and concepts page (4294967295) — a validation-boundary lead.

---

## 4. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Low-priv networking principal | Content of a DHCP option set | `CreateDhcpOptions` with attacker DNS/NTP IPs | A set is created with hostile `domain-name-servers` that **no org IAM policy on the create action could have blocked** — content-invisibility proven. |
| Creator | Downstream ABAC gate (Associate/Delete keyed on `aws:ResourceTag`) | `TagSpecification` on create sets the gating tag value | Creator reads/associates/deletes a set the ABAC policy was meant to scope, because the creator picked the tag value at birth. |
| Creator (Create) + associator (Associate) | Every instance in a VPC (and all VPCs the set is later attached to) | Create→Associate chain; DHCP lease renewal | Instances in the target VPC resolve DNS via the attacker IP within "a few hours", **no instance credential, no restart** → network-position privilege escalation (spoof `sts`/`s3`/metadata mirrors). |
| Any principal w/ create | Shared service plane (AWS Resolver / Time Sync) | setting `domain-name-servers`=`AmazonProvidedDNS` / NTP = `169.254.169.123` | **Out of scope / HARD STOP** — configuring instances to *use* AWS's resolver is the intended knob; probing into the resolver fleet is the shared-responsibility line. |

---

## 5. Recommended Areas of Focus

### Area 1 (PRIMARY, Lens U + S) — Content-invisibility: IAM cannot constrain the baked-in option VALUES
**Background.** DHCP option values (`domain-name-servers`, `ntp-servers`, `netbios-name-servers`, `domain-name`) are set *only* at `CreateDhcpOptions` and are **immutable thereafter** ("After you create a DHCP option set, you can't modify it"). The EC2 authorization reference shows the `CreateDhcpOptions` action row with **empty Condition-key and Possible-value columns**; the only keys the `dhcp-options` type exposes at create are tag/region keys. **No condition key anywhere references a DHCP option value.**

**Security Concern.** An organization can grant `ec2:CreateDhcpOptions` but is **structurally unable** to require that option sets use `AmazonProvidedDNS`, or that custom `domain-name-servers` fall inside the VPC CIDR / an approved resolver allowlist. The guardrail an org most wants here is inexpressible in IAM/SCP. Strongest corroboration that AWS itself treats this content as needing a gate: AWS Managed Services (AMS) Advanced wraps DHCP-set changes in a change-management workflow that **validates DNS servers and requires approval** — i.e. AWS bolts on *outside* IAM exactly the control the native API lacks. (Corroborate the AMS validation wording live; flagged doc-gap.)

**High-level Test Scenarios (falsifiable claims).**
- **Claim:** No `Deny` on `ec2:CreateDhcpOptions` can be written that blocks `domain-name-servers=<attacker-ip>` while allowing `AmazonProvidedDNS`. → **Oracle:** enumerate the full condition-key set for the action via `iam:GetContextKeysForCustomPolicy` / the SAR; attempt to author an SCP that permits only `AmazonProvidedDNS` → **no key exists to reference the value** = confirmed. → **Severity if true:** Medium (enforcement-gap enabler; becomes High→Critical as the authoring step of the Area 4 chain).
- **Claim:** The create API accepts a link-local / metadata-adjacent IP (e.g. `169.254.x.x`) or a public attacker IP as `domain-name-servers` with no validation error. → **Oracle:** `create-dhcp-options` with such values; 200 + `dopt-` returned. → **Severity:** informational alone; it is the payload for Area 4.
- **Claim (doc-vs-doc, Lens U):** `ipv6-address-preferred-lease-time` max differs between API ref (2147483647) and the VPC concepts page (4294967295). → **Oracle:** submit `4294967295`; accept vs `ValidationException` reveals which doc is wrong. → **Severity:** Low/Informational (doc-integrity; file to AWS).

**Doc evidence:** `DHCPOptionSet.md:21` (immutability); `list_ec2.md:471` (empty condition columns); API ref value bounds. **Severity-if-true:** Medium (High/Critical in-chain).

---

### Area 2 (PRIMARY, Lens I + S) — Tag-on-create self-widening defeats downstream ABAC
**Background.** `CreateDhcpOptions` with `TagSpecification.N` consumes a **second** IAM action, `ec2:CreateTags` (two IAM-action rows under the action in `list_ec2.md:471-472`). The `dhcp-options` type at create exposes `aws:RequestTag/${TagKey}` and `aws:TagKeys`.

**Security Concern.** If an org scopes the *dangerous* downstream actions (`AssociateDhcpOptions`, `DeleteDhcpOptions`, or `DescribeDhcpOptions`-derived workflows) with ABAC on `aws:ResourceTag/<k>`, the creator can **set that tag's value at birth** via `aws:RequestTag`, pre-satisfying the gate — classic EC2 tag-on-create self-widen. Worse, if the org forgets to also condition the **`ec2:CreateTags` leg** with `aws:RequestTag`/`aws:TagKeys`, the creator can set arbitrary tags (or create **untagged** sets that slip ABAC that assumes a tag is always present).

**High-level Test Scenarios.**
- **Claim:** A principal scoped by `aws:ResourceTag/env=prod` on `AssociateDhcpOptions` can create a set tagged `env=prod` and then associate it, despite never being entrusted with "prod". → **Oracle:** under a scoped role, `create-dhcp-options --tag-specifications 'ResourceType=dhcp-options,Tags=[{Key=env,Value=prod}]'` then associate; success = ABAC bypass. Prove the role *cannot* do it for an un-self-tagged foreign set (bounds blast radius). → **Severity:** Medium–High (ABAC is the access-control mechanism).
- **Claim:** Omitting the `ec2:CreateTags` condition lets the creator mint sets with **no** gating tag, invisible to tag-filtered governance (Config rule `ec2-dhcp-options-tagged` is content-blind — tags only). → **Oracle:** create without required tag; policy that `Deny`s create-without-tag only works if `ec2:CreateTags` leg carries `aws:RequestTag` / `Null:aws:RequestTag/<k>=true`. → **Severity:** Medium.

**Doc evidence:** `list_ec2.md:471-472` (dual IAM actions); SAR `dhcp-options` resource condition keys. **Severity-if-true:** Medium–High.

---

### Area 3 (PRIMARY, Lens X + kill chain) — Create is the unblockable first half of the silent DNS/NTP-hijack chain
**Background.** `CreateDhcpOptions` mints the hostile config; `AssociateDhcpOptions` deploys it. Per the VPC guide, *"any existing instances and all new instances … use the new options. You don't need to restart or relaunch … Instances automatically pick up the changes within a few hours."*

**Security Concern.** Neither action has a **content** condition key, and `ec2:DhcpOptionsID` on the *create* leg is **moot** (the resource does not exist at authz time — a guardrail that *looks* scoping but isn't, the classic EC2 "create-time id key" trap). So a principal holding `ec2:CreateDhcpOptions` + `ec2:AssociateDhcpOptions` can, with two calls and **no instance access, no `route53:*`, no reboot**, repoint DNS for every instance in a VPC → MITM higher-privileged roles' instances (spoof `sts.amazonaws.com`, `s3`, package mirrors, SSM). This is **network-position privilege escalation**. Rate at the **end** of the chain.

**High-level Test Scenarios.**
- **Claim:** `ec2:DhcpOptionsID` placed as a `Condition` on `CreateDhcpOptions` does **not** restrict which set gets created (resource doesn't exist yet). → **Oracle:** author such a policy; create still succeeds for any content = guardrail inert. → **Severity:** Medium (misleading-control).
- **Claim (chain):** low-priv networking principal + create + associate → victim instances in a shared/targeted VPC resolve `sts`/`s3` via attacker DNS within hours. → **Oracle:** (sibling plan Area 1) observe DNS queries landing on attacker resolver; **stop at existence proof**, do not harvest credentials. → **Severity:** **High→Critical** (identity/credential MITM across privilege tiers).
- **Claim (persistence tuning):** a very long `ipv6-address-preferred-lease-time` makes a hostile set "stick" (slow re-lease after defenders associate a clean set); a very short one accelerates uptake of the hostile set. → **Oracle:** compare lease-renewal cadence. → **Severity:** Low (attacker QoL / resilience tuning).

**Doc evidence:** `DHCPOptionSet.md:72` (silent few-hours uptake); `list_ec2.md:471`; sibling plan Areas 1–4. **Severity-if-true:** High–Critical (chain end).

---

### Area 4 (Lens L) — Resource exhaustion / quota of DHCP option sets
**Background.** *"You can create as many additional DHCP option sets as you want"* (prose), but a per-Region quota exists in EC2 Service Quotas (value **not confirmed** on the VPC quotas page fetched — doc-gap).

**Security Concern.** A principal with only `ec2:CreateDhcpOptions` can loop creation to exhaust the per-account/region DHCP-option-set quota → **self-DoS** (legit automation can't create new sets; blocks the defender's remediation path of "create clean set + associate"). Cross-tenant impact: none (per-account quota). Combined with Area 3, exhausting the quota *after* associating a hostile set can delay cleanup.

**High-level Test Scenarios.**
- **Claim:** Unbounded create loop hits a quota that then blocks remediation-via-new-set. → **Oracle:** confirm the quota value + adjustability in Service Quotas (`L-…` for DHCP option sets); attempt bulk create in a canary account. → **Severity:** Low (single-tenant self-DoS) — raise to Medium if it demonstrably blocks defender remediation during an active Area-3 hijack.

**Doc evidence:** `DHCPOptionSet.md:18` (create as many as you want); VPC quotas page (DHCP quota absent → confirm live). **Severity-if-true:** Low–Medium.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Author hostile DNS/NTP content that no IAM guardrail can block | `CreateDhcpOptions` content | **None** — no content condition key; immutability means create is the only gate point |
| Self-assign ABAC tag at create to pass downstream gate | `TagSpecification` + `ec2:CreateTags` leg | `aws:RequestTag`/`aws:TagKeys` on the CreateTags leg (often omitted) |
| `ec2:DhcpOptionsID` condition on create | create-time id key | Inert (resource absent at authz) |
| Create→Associate silent VPC DNS hijack | chain w/ `AssociateDhcpOptions` | No content key on either action; lease-renewal makes it silent |
| Lease-time value out-of-bounds | `ipv6-address-preferred-lease-time` | API value validation (bounds doc-inconsistent) |
| Quota exhaustion | per-Region DHCP-set quota | Service Quotas cap (value unconfirmed) |

---

## 7. Out-of-Scope Risk Categories
- Probing **into** the AWS Resolver fleet (`169.254.169.253`, `.2`) or Time Sync (`169.254.169.123`) — shared-responsibility line / **HARD STOP**. Configuring instances to use/avoid them is the in-scope customer knob.
- Cross-account blast radius of a hostile set — that is a property of **`AssociateDhcpOptions` onto a shared VPC** (see sibling plan Area 5), not of create.
- The downstream DNS-MITM *exploitation* (credential capture, lateral movement) — stop at existence proof; harvesting is out of scope.
- A customer writing their own over-broad IAM policy that grants create `Resource:*` — customer footgun, out of scope. (The *absence of a content condition key* is AWS-owned and in scope as Area 1.)
- IMDS behavior on managed hosts; DNS rebinding against private-only endpoints.

## 8. Null hypotheses / doc gaps
- **Lens A/EE (cross-account / predictable-name):** NULL. Create acts only in the caller's account; `dopt-` ids are not a global/first-come namespace and aren't resolved by name. Pages checked: API ref (no cross-account input), SAR `dhcp-options` ARN (account-scoped).
- **Lens G (SSRF):** NULL at the create step — no field is dereferenced server-side at create. `domain-name-servers` IPs are handed to *instances* via DHCP, not fetched by the control plane. (The MITM they enable is modeled under Area 3, not SSRF.) Pages checked: API ref, NewDhcpConfiguration, concepts.
- **Lens B/C (PassRole/vending):** NULL — no role ARN, token, or credential input.
- **Lens F (injection/parser):** THIN — `domain-name` is free-text stored and relayed; no evidence of a server-side translator at create. Possible low-value value-validation edges (lease-time bounds, IP-list length) → Area 1/4. Mark "doc-gap — confirm value validation live."
- **Lens H/W/Y/FF/J/K/Q/BB/CC/DD:** NULL — no KMS, attestation, transport knob, token, OAuth, LLM, upload, multi-parser routing, cache, or JWT surface on this action. Pages checked: API ref + authorization reference.
- **Doc gaps to confirm live:** (1) exact DHCP-option-set per-Region quota + adjustability; (2) AMS Advanced DHCP-content validation wording; (3) `ipv6-address-preferred-lease-time` true max (2147483647 vs 4294967295).

---
*Reuses EC2 crown-jewel moves: content-invisibility (no value condition key), create-time-id-key-is-moot, tag-on-create self-widen, and the Create+Associate DNS-hijack chain documented in `ec2-AssociateDhcpOptions-attack-research-plan.md`.*
