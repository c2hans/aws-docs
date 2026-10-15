# Elastic IP Addresses (EIP) — Attack / Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html
**Service / surface:** Amazon EC2 — Elastic IP addresses (allocate / associate / release lifecycle, cross-account transfer, reverse-DNS-for-email, network border group, quota).
**Position in corpus:** Page-level deep-dive **child of the `ec2-networking` hub plan**. This plan is the designated **owner** of the hub's deferred lead **#1 (EIP cross-account transfer hijack)** and of **released-EIP squatting / dangling-DNS**. It cross-references — and does **not** duplicate — its siblings:
- `ec2-byoip-attack-research-plan.md` (owns BYOIP pool crypto-proofing, within-pool `AllocateAddress` squatting, BYOIP non-transferability).
- `using-instance-addressing-attack-research-plan.md` (owns secondary private-IPv4 cross-ENI/cross-account takeover; "EIP rides along" with a moved secondary IP).
- `working-with-ip-addresses-attack-research-plan.md` (owns launch-time `ec2:AssociatePublicIpAddress` / public-IP-on-launch).
- `instance-secondary-ip-addresses-attack-research-plan.md` (owns `UnassignPrivateIpAddresses` → EIP auto-disassociation unscopable collateral).

**Method:** `security-questionbuilder` (boundary-first). Documentation-only; no live AWS calls. All leads are falsifiable claims with a confirm/refute oracle for a downstream hunter. Online pages cross-checked against the offline mirror; IAM reference read offline from `list_ec2.md` (online `.html`/`.md` truncates condition-key tables).

**Analysis provenance:** overview + transfer page read directly; two Opus subagents (A = cross-account transfer; B = lifecycle/squatting/reverse-DNS/quota/oracle); IAM rows re-verified by line number in this plan.

---

## §0 — Executive summary (the shape of this surface)

An Elastic IP is a scarce, globally-routable, account-reassignable IPv4 resource. Its security turns on three seams, and the documentation shows all three are **structurally under-governed by IAM**:

1. **The shared Amazon address pool is a cross-tenant seam.** Release returns an address to a pool from which "a different AWS account" can allocate it, and `AllocateAddress` has **no condition key for the IP you request** — so you cannot write an IAM policy restricting *which* address a principal reclaims. This is the released-EIP squatting / dangling-trust primitive (Leads L1–L3).
2. **Cross-account transfer has no counterparty condition key.** `EnableAddressTransfer` / `AcceptAddressTransfer` can be IAM-scoped by *which EIP* (AllocationId / PublicIpAddress / tag) but by **no key for the destination or source account**, and "AWS does not notify transfer accounts" — a two-step handshake whose second step is driven entirely by an out-of-band, human-relayed public-IP string (Leads T1–T5).
3. **Reverse-DNS (`ModifyAddressAttribute.DomainName`) is caller-supplied free text** whose ownership gate is undocumented, and it doubles as a *lock* that blocks both release and transfer-acceptance (Leads D1–D2).

Supporting structural gaps: `AssociateAddress` reassociation is default-automatic with no IAM key (`AllowReassociation`/`AllowReassignment` is not a condition key and the doc even disagrees with itself on the field's name — Lead S1); `NetworkBorderGroup` is advisory with **zero** IAM representation (Lead B1); `DescribeAddresses`/`DescribeAddressesAttribute`/`DescribeAddressTransfers` are all **unscopable read oracles** gated only by `ec2:Region` (Leads O1–O2). One genuine upstream **doc contradiction**: the transfer window is "**seven days**" in the UserGuide (×3) vs "**seven hours**" in `API_AddressTransfer.md` (Lead X1 — cheapest to confirm, recalibrates every time-boxed lead).

**Highest-value leads for a hunter with two in-scope accounts:** T1 (transfer hijack via no counterparty key + no notification), L1 (released-EIP squatting race), S1 (forced reassociation steal).

---

## §1 — Components, Assets, and Design

### Customer-facing interface
EC2 public API (SigV4 IAM), console **Elastic IPs** pane, CLI/PowerShell. No non-SDK endpoints in this surface. All operations are account-scoped request/response; there is no data-plane protocol here — the "data plane" of an EIP is BGP advertisement + packet routing, owned entirely by AWS.

### Assets
- **The IPv4 address itself** — the scarce, trust-bearing asset. Trust bound to an IP (firewall allowlists, SPF / stale DNS A-records, outbound sender reputation, OAuth/IP allowlists) is inherited by whoever next holds it.
- **The allocation** (`eipalloc-…`) — the account-scoped handle; the ARN is keyed by **AllocationId**, *not* by the public IP (`arn:…:ec2:region:account:elastic-ip/${AllocationId}`, list_ec2 L9938).
- **The reverse-DNS (PTR) record** — a sender-reputation / attribution asset; also a *lock*.
- **Tags** — reset on transfer; name-tag re-created at accept-time.

### Identifier shape & entropy
- Public IPv4 — 32-bit, fully enumerable/observable externally (passive DNS, Shodan, cert transparency, allowlist leaks). This is the enumeration surface, not a secret.
- `eipalloc-…` / `eipassoc-…` — opaque, per-allocation; a **new AllocationId is minted on every `AllocateAddress`**, including "recovery" (nothing in the docs promises AllocationId continuity across release→recover — see H0-5).

### Ownership / trust zones
- **Amazon's shared IPv4 pool** (AWS-owned, multi-tenant inventory) ↔ **customer account allocation**. Release crosses *into* the shared pool; allocate crosses *out of* it. **This is the only place in this surface where one tenant's action (release) creates another tenant's opportunity (reclaim).**
- **Source account ↔ transfer (destination) account** — explicit cross-account seam via the transfer handshake.
- **Caller's request context ↔ the EIP's current association holder** — `AssociateAddress` can tear an EIP off a resource it is currently bound to.

### Untrusted-data entry points
- `AllocateAddress.Address` (free IPv4 string → pool lookup).
- `AcceptAddressTransfer.Address` (free IPv4 string → pending-transfer lookup).
- `ModifyAddressAttribute.DomainName` (free domain string → reverse-DNS publish).
- `*.NetworkBorderGroup` (free zone-group string → existence-validated only).

### Connection sketch
```
   Amazon shared IPv4 pool  (AWS-owned, multi-tenant)
        ^   |  release returns to pool                allocate --address X
        |   v  (becomes reclaimable by ANY account)   (no ec2:PublicIpAddress key)
   +----------------------+   EnableAddressTransfer(--transfer-account-id Y)   +----------------------+
   |  Source account A    | ----- 7-day* handshake, NO counterparty key -----> |  Transfer account B  |
   |  elastic-ip/eipalloc |       AWS sends NO notification                     |  accept --address IP |
   +----------------------+                                                     +----------------------+
        | AssociateAddress (AllowReassociation default-auto, no IAM key)
        v
   instance / network-interface  --(ModifyAddressAttribute.DomainName: free text, undocumented ownership gate)--> public PTR
```

---

## §2 — Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Any AWS account B | Address just released by account A | `AllocateAddress --address <A's old IP>` against the shared pool | B obtains the specific IP A just held, before A re-claims it → **dangling-trust takeover** (L1) |
| Transfer (dest) account B | EIP owned by source account A | `EnableAddressTransfer`(A) + `AcceptAddressTransfer --address <IP>`(B) | Ownership moves with **no counterparty IAM key** and **no AWS notification** to B → mis-delivered or socially-engineered transfer (T1–T3) |
| Principal P holding `ec2:AssociateAddress` on an EIP | Any instance / ENI | `AssociateAddress(AllocationId, InstanceId)` with default-auto reassociation | EIP is torn off its current holder and re-pointed with no consent and no `AllowReassociation` IAM key (S1) |
| Any principal with `ec2:ModifyAddressAttribute` on an owned EIP | Public reverse-DNS namespace | `DomainName` free-text PTR publish | PTR for an attacker-chosen reputable-looking domain the caller does not own becomes active (D1) |
| Any principal with `ec2:DescribeAddresses` in a region | Entire account EIP inventory | unscopable List (no resource type) | Full association/instance/private-IP/border-group inventory readable; cannot be narrowed by resource ARN (O1) |
| Any principal with `ec2:DescribeAddressTransfers` in a region | All pending/accepted transfers | unscopable List | Pending-transfer public IPs + counterparty state readable account-wide (O2) |
| Customer assumption of "border-group isolation" | — | `NetworkBorderGroup` field | No such IAM key exists → any assumed isolation is unenforceable (B1) |
| **Any customer surface** | **AWS's own service/BGP plane** | — | **HARD STOP** — any AWS-fleet credential/identity/ARN or control-plane reach ⇒ preserve evidence, flag for disclosure, do not proceed |

---

## §3 — API / interface surface

| Name | Mut? | Ext? | Resource type (list_ec2) | Condition keys of interest | Notes |
|---|---|---|---|---|---|
| `AllocateAddress` | ✓ | ✓ | `elastic-ip*` (L4670) + `ipam-pool`,`ipv4pool-ec2` alts | `aws:RequestTag`,`aws:TagKeys`,`ec2:Region` **only** | **No `ec2:PublicIpAddress`/`AllocationId`/`Domain`** → the requested IP is **unscopable** (L1). `Address` = "recover **or an IPv4 from a pool**". |
| `AssociateAddress` | ✓ | ✓ | `elastic-ip`,`instance`,`network-interface` (alts, none required; L4714–16) | `ec2:AllocationId`,`ec2:Domain`,`ec2:PublicIpAddress`,`ec2:Region`,tags | `AllowReassociation` default-auto; **not** an IAM key. Resource types are alternates → open "need-perm-on-EIP-or-target?" question (S1). |
| `DisassociateAddress` | ✓ | ✓ | `elastic-ip`,`network-interface` (L7887) | `ec2:AllocationId`,`ec2:Domain`,`ec2:PublicIpAddress`,`ec2:Region`,tags | Non-disassociable guard (dual-stack+primary+last-IPv4) is a stability guard, not authz (S2). |
| `ReleaseAddress` | ✓ | ✓ | `elastic-ip` (L9385) | `ec2:AllocationId`,`ec2:Domain`,**`ec2:PublicIpAddress`**,`ec2:Region`,tags | Returns IP to shared pool "can be allocated to a different AWS account". PTR lock blocks release (D2). |
| `EnableAddressTransfer` | ✓ | ✓ | `elastic-ip*` (L8005) | `aws:ResourceTag`,`ec2:AllocationId`,`ec2:Domain`,`ec2:PublicIpAddress`,`ec2:Region`,`ec2:ResourceTag` | Scopes *which EIP*; **NO destination-account key** (T1). |
| `AcceptAddressTransfer` | ✓ | ✓ | `elastic-ip*` (L4608) | `aws:RequestTag`,`aws:TagKeys`,`ec2:AllocationId`,`ec2:Domain`,`ec2:PublicIpAddress`,`ec2:Region` | **NO source-account key**; carries `aws:RequestTag` → tag-on-accept also needs `ec2:CreateTags`. ARN keyed by *source's* AllocationId — self-scoping by dest is near-impossible (T2). CLI takes `--address <IP>` only. |
| `DisableAddressTransfer` | ✓ | ✓ | `elastic-ip*` (L7752) | same as Enable | Source-side cancel; 7-day* window to use (T4). |
| `DescribeAddressTransfers` | ✗ | ✓ | **none** (L6570) | `ec2:Region` **only** | Unscopable transfer-state oracle (O2). |
| `DescribeAddresses` | ✗ | ✓ | **none** (L6576) | `ec2:Region` **only** | Unscopable account-wide EIP inventory oracle (O1). `Filter.N` includes `network-interface-owner-id`. |
| `DescribeAddressesAttribute` | ✗ | ✓ | **none** (L6582) | `ec2:Region` **only** | Unscopable PTR/attribute oracle. |
| `ModifyAddressAttribute` | ✓ | ✓ | `elastic-ip*` (L8719) | +`ec2:Attribute`,`ec2:Attribute/${AttributeName}` | `DomainName` free text; async `PENDING` publish; undocumented ownership gate (D1). |
| `ResetAddressAttribute` | ✓ | ✓ | `elastic-ip*` (L9491) | same as Modify | `Attribute`=`domain-name` only. |

**Resolved mystery:** `ec2:Permission` (def L10122) is a **network-interface** key (CreateNetworkInterfacePermission; values INSTANCE-ATTACH / EIP-ASSOCIATE), **not** an EIP-share primitive. There is no cross-account "share EIP" API — only transfer and pool-release. (Carried from the hub's frag1 "ec2:Permission mystery", now closed.)

---

## §4 — Leads (falsifiable, with oracle)

### Transfer (Lens A / AA / P) — owner of hub lead #1

**T1 — No counterparty condition key on the transfer handshake.**
*Claim:* An IAM policy can restrict *which EIP* a principal may enable/accept for transfer, but **cannot** restrict *which account* it is transferred to or from — so a compromised/over-trusted principal in the source account can enable transfer of any in-scope EIP to an arbitrary attacker account, and nothing in IAM prevents it.
*Mechanism:* `EnableAddressTransfer` (L8005) and `AcceptAddressTransfer` (L4608) carry only `ec2:AllocationId`/`ec2:PublicIpAddress`/`ec2:Domain`/tag/`ec2:Region` keys — grep of `list_ec2.md` finds **no** `transfer-account-id`, source-account, or `aws:PrincipalOrgID`-style key tied to these actions. CLI: `enable-address-transfer --allocation-id X --transfer-account-id Y`; the `transfer-account-id` is a plain request param with no policy lever.
*Oracle:* In a 2-account test, write a source-account Deny/Condition attempting to restrict `EnableAddressTransfer` to a specific `transfer-account-id`; confirm no condition key makes it enforceable. Then confirm the transfer completes to an account the policy "intended" to exclude.
*Preconditions/cost:* source principal with `ec2:EnableAddressTransfer`; a destination account. Free.
*Severity:* **High** — cross-account asset exfiltration of a trust-bearing IP, un-gatable by IAM.

**T2 — Accept-side self-scoping is structurally defeated by the ARN shape.**
*Claim:* The transfer (destination) account cannot write an effective resource-level policy to restrict *which* transfers it will accept, because `AcceptAddressTransfer`'s required resource is `elastic-ip*` whose ARN is keyed by the **source account's** AllocationId — an identifier the destination does not know in advance and never owned.
*Mechanism:* ARN `…:elastic-ip/${AllocationId}` (L9938); accept CLI references the address by **public IP only** (`accept-address-transfer --address 100.21.184.216`), while IAM scoping keys are AllocationId/PublicIpAddress of a resource in the *source's* account.
*Oracle:* attempt a destination-side policy scoping accept to specific AllocationIds; show it cannot match an inbound transfer whose AllocationId is unknown pre-accept. Check whether `ec2:PublicIpAddress` condition on accept is even evaluated when the dest account doesn't own the resource yet.
*Severity:* Medium (hardening gap enabling T3).

**T3 — No notification + human-relayed IP string = mis-delivery / social-engineering primitive.**
*Claim:* Because "AWS does not notify transfer accounts" and accept is driven solely by a public-IP string passed out-of-band, an attacker who learns a pending-transfer IP (or who induces a source operator to fat-finger a `transfer-account-id`) can accept a transfer not intended for them, or race the intended recipient.
*Mechanism:* transfer page L28 ("AWS does not notify transfer accounts… the source account must notify…"); accept = `--address <IP>` with 7-day* window; `DescribeAddressTransfers` (O2) is an unscopable oracle that could surface pending-transfer IPs within an account.
*Oracle:* with source A enabling transfer to intended account B, confirm whether an unrelated account C that knows the IP can call `accept-address-transfer --address <IP>` — i.e., is accept gated to the *named* `transfer-account-id`, or to *any* account presenting the IP? (Doc never states accept is bound to the enabled target account — **key open question**.) If accept succeeds from a non-targeted account, severity is Critical.
*Severity:* High→Critical **if** accept is not bound to the enabled `transfer-account-id`.

**T4 — Transfer window drift / stale-pending griefing.**
*Claim:* A source account can leave an EIP in `pending` transfer, and the asymmetric visibility (source sees pending; accepted transfers visible to source 14 days) plus `DisableAddressTransfer` create confusion/griefing around whether an address is "really" owned.
*Mechanism:* 7-day* accept window → auto-return to source; 14-day post-accept visibility to source; `DisableAddressTransfer` cancels. Combine with X1 (window length is doc-contradictory).
*Oracle:* confirm actual window; confirm whether a disabled-then-re-enabled transfer resets tags/PTR state.
*Severity:* Low–Medium (operational/griefing).

**T5 — Tag reset on transfer erases ABAC-based controls silently.**
*Claim:* "Any tags associated with an Elastic IP being transferred are reset when the transfer is complete" — any **tag-based access control or cost/ownership attribution** keyed on the EIP's tags is silently voided across the transfer, and the destination re-creates only a chosen `Name` tag.
*Mechanism:* transfer page L29; accept-console step re-creates a `Name` tag of the accepter's choosing; Accept carries `aws:RequestTag`/`aws:TagKeys` (+ `ec2:CreateTags`).
*Oracle:* confirm tags are stripped; confirm no original tag survives to anchor source-side ABAC.
*Severity:* Medium (control-erasure / attribution-laundering).

### Shared-pool squatting / dangling-DNS (Lens A / EE / M)

**L1 — Released-EIP targeted reclaim by an unrelated account.**
*Claim:* Account B can reclaim account A's just-released IP via `AllocateAddress --address <A's old IP>`, because `AllocateAddress` has **no `ec2:PublicIpAddress` key** (the requested IP is unscopable) and the "recovery" flow proves the `Address` param accepts arbitrary pool addresses.
*Mechanism:* `API_AllocateAddress` "Address = recover **or an IPv4 from an address pool**"; `ReleaseAddress`/`API_AllocateAddress` "released to the IP address pool and can be allocated to **a different AWS account**"; list_ec2 L4670 key set lacks `ec2:PublicIpAddress`.
*Oracle:* 2-account live test — A releases, B immediately `allocate-address --address <IP>`. Doc states success hinges only on "has it been allocated to another account yet"; no cooldown/quarantine/affinity documented (H0-1).
*Preconditions/cost:* B needs only default `ec2:AllocateAddress` + knowledge of the target IP (external recon). Free, racing.
*Severity:* **High** — dangling-trust takeover (allowlists, SPF/stale A-records, sender reputation, IP-keyed OAuth).

**L2 — Squatting scope is standard-pool-only, not BYOIP.**
*Claim:* BYOIP-sourced EIPs are *not* squattable the same way (pool is registration-bound to one account); risk is specific to Amazon-pool EIPs.
*Oracle:* cross-ref `ec2-byoip-attack-research-plan.md` (BYOIP pool ownership). Flag H0-4 open.
*Severity:* scope-limiting.

**L3 — No documented anti-targeting mitigation.**
*Claim:* No cooldown/quarantine/random-only-reassignment is documented for standard-pool release→reallocate, so there is no documented defender control against L1.
*Oracle:* absence check (grep done; none found). Documentation-completeness claim.
*Severity:* raises L1 feasibility.

### Associate / Disassociate (Lens AA)

**S1 — Forced reassociation steal; EIP-side permission may suffice.**
*Claim:* A principal with `ec2:AssociateAddress` on an EIP can forcibly tear that EIP off whatever resource currently holds it (default-auto reassociation) and re-point it onto any instance/ENI — and because the three resource types are IAM **alternates**, it is unclear whether permission on the *target* instance is even required.
*Mechanism:* `API_AssociateAddress` "already associated with a different instance → it is disassociated… and associated with the specified instance"; "Reassociation is automatic". `AllowReassociation`/`AllowReassignment` is **not** a condition key (grep: zero matches). list_ec2 L4714–16 lists `elastic-ip`/`instance`/`network-interface` as alternates.
*Oracle:* principal with `ec2:AssociateAddress` scoped to `elastic-ip/eipalloc-X` only (no instance grant) — does `AssociateAddress(X, InstanceId=I)` succeed against an instance it has no IAM rights on? If yes → EIP owner can redirect traffic onto / steal reachability of arbitrary instances.
*Severity:* Medium–High (traffic redirect / reachability DoS, esp. with shared/transferred EIPs).

**S2 — Non-disassociable guard is a stability control, not authz (rule-out).**
*Claim:* The dual-stack-DNS + primary-IPv4 + last-remaining-IPv4 non-disassociable condition is an availability guard, not a security boundary, and does not block S1.
*Oracle:* doc reading — `DisassociateAddress` IAM row carries no key referencing this rule.
*Severity:* Low (rules out a false mitigation).

### Network border group (Lens S / U)

**B1 — `NetworkBorderGroup` has zero IAM surface; any assumed isolation is unenforceable.**
*Claim:* `NetworkBorderGroup` is advisory geographic partitioning, validated only for existence (`InvalidAddress.NotFound`), with **no** condition key — you cannot write a policy restricting which border groups a principal allocates/releases into.
*Mechanism:* grep `list_ec2.md`: zero `NetworkBorderGroup` condition-key matches; overview frames it as advertisement scope only.
*Oracle:* doc-confirmed by absence; secondary — does `DescribeAvailabilityZones` leak border-group / Local-Zone / Wavelength topology account-wide?
*Severity:* Low–Medium (gap-flag: false isolation assumption).

### Reverse DNS for email (Lens O / G)

**D1 — `DomainName` is free text with an undocumented ownership gate (PTR reputation-laundering).**
*Claim:* `ModifyAddressAttribute.DomainName` accepts caller-supplied free text; the only documented check (matching forward A-record) is phrased as *user responsibility*, and the publish is async (`PENDING`) with no documented `FAILED` path — so a weak/absent gate would let an attacker publish a reputable-looking PTR for a domain they do not own.
*Mechanism:* `API_ModifyAddressAttribute` `DomainName` (no format/ownership constraint stated); `Using_Elastic_Addressing_Reverse_DNS` "you must set a corresponding forward DNS record" phrased as best practice; `PtrRecordUpdate.Status: PENDING` only.
*Oracle:* set `DomainName` to a domain with no matching forward A-record / not controlled by caller; observe whether `PENDING` ever becomes an active PTR or flips to a rejected state. (Not SSRF — AWS performs resolution — but attribution/reputation abuse.)
*Severity:* Medium (email-reputation laundering).

**D2 — Reverse-DNS lock = release/transfer DoS primitive.**
*Claim:* A PTR record locks the EIP: it cannot be released, and (per transfer page `InvalidTransfer.AddressCustomPtrSet`) cannot be transfer-accepted, until the PTR is removed; Support-set PTRs have **no self-service unlock**.
*Mechanism:* `Using_Elastic_Addressing_Reverse_DNS` ("locked to your account… cannot be released"); transfer page L99.
*Oracle:* doc-confirmed. Live only to time the Support-unlock SLA.
*Severity:* Low (self-DoS / quota-automation footgun), but note it **blocks T1-style transfer** — a defensive side effect.

### Read oracles (Lens A)

**O1 — `DescribeAddresses` unscopable account-wide inventory oracle.**
*Claim:* `DescribeAddresses`/`DescribeAddressesAttribute` have no resource type (blank) and only `ec2:Region` — cannot be narrowed to a subset of EIPs via resource ARNs; any holder sees the account's full EIP inventory (association, instance IDs, private IPs, allocation IDs, border groups, PTR domain).
*Mechanism:* list_ec2 L6576–6586 blank resource column; `Filter.N` includes cross-account `network-interface-owner-id`.
*Oracle:* doc-confirmed for unscopability. Secondary/unconfirmed: whether an EIP on a cross-account-**shared** ENI leaks the owner account via `network-interface-owner-id` (needs shared-ENI test — cross-ref `using-instance-addressing`).
*Severity:* Medium (least-privilege structural gap).

**O2 — `DescribeAddressTransfers` unscopable transfer-state oracle.**
*Claim:* No resource type, `ec2:Region` only — any principal with the action sees all pending/accepted transfer public IPs + counterparty state, feeding T3.
*Mechanism:* list_ec2 L6570.
*Severity:* Low–Medium (recon feeder for T3).

### Doc-integrity

**X1 — Transfer-window contradiction: "seven days" vs "seven hours".**
*Claim:* The accept window is "**seven days**" in the UserGuide (transfer page L26/L27/L95, ×3) but "**seven hours**" in `API_AddressTransfer.md` (`transferOfferExpirationTimestamp` description). Both identical online+offline → **upstream AWS authoring contradiction**, not mirror drift.
*Oracle:* single live `enable-address-transfer` then observe the returned expiration timestamp. Cheapest lead; recalibrates T3/T4 timing.
*Severity:* Low intrinsically; **high leverage** (settles every time-boxed transfer lead).

---

## §5 — Null hypotheses (checked, pages named)

- **H0-1 (release cooldown exists):** Refuted by absence — `elastic-ip-addresses-eip.md`, `using-instance-addressing-eips-releasing.md`, `API_ReleaseAddress`, `API_AllocateAddress`: no quarantine/affinity timer. (Supports L1/L3.)
- **H0-2 (`AllowReassociation`/`AllowReassignment` is IAM-scopable):** Refuted — zero condition-key matches in `list_ec2.md` (10,190 lines) for either spelling. (Underpins S1.)
- **H0-3 (`NetworkBorderGroup` IAM-scopable / enforces isolation):** Refuted — zero condition-key matches. (B1.)
- **H0-4 (BYOIP EIPs squattable like Amazon-pool):** Open — needs `ec2-byoip` pool-ownership read; deferred to that sibling plan. (L2.)
- **H0-5 (recovered EIP keeps original AllocationId/ARN):** Open — recovery example shows no response `allocationId`; nothing confirms ARN continuity. Matters for whether an old `elastic-ip/eipalloc-X` policy "reattaches" after recover.
- **H0-6 (EIP quota = cross-tenant DoS):** Refuted/low — quota is per-account (5/Region, BYOIP excluded); the only cross-tenant interaction is L1's shared-pool race (a takeover, not exhaustion).
- **H0-7 (`DescribeAddresses*` resource-level restrictable):** Refuted — blank resource column, `ec2:Region` only. (O1.)
- **H0-8 (Lens B PassRole / confused-deputy):** N/A for this surface — read all four UserGuide pages + eight API refs; no EIP action accepts a role ARN or acts "on your behalf" (reverse-DNS resolution is AWS-performed infra, not a caller-passed identity). The confused-deputy shape lives in BYOIP (crypto proof) and transfer (counterparty), both captured above.
- **H0-9 (org/SCP global keys on transfer):** Checked — no `aws:PrincipalOrgID`/`aws:ResourceOrgID`-type key tied to the four transfer actions in `list_ec2.md`; transfer cannot be constrained to an organization via a service-specific key. (Reinforces T1.)

---

## §6 — Priority & NEW/changed surface

1. **T1 / T3** — transfer hijack: no counterparty key + no notification + (open) accept-not-bound-to-target. Start here; needs 2–3 accounts.
2. **L1** — released-EIP squatting race: single most reusable dangling-trust primitive; needs 2 accounts.
3. **S1** — forced reassociation steal / EIP-side-permission-suffices: single-account testable.
4. **D1** — reverse-DNS ownership gate: single-account, cheap.
5. **O1 / O2** — unscopable oracles: doc-confirmed; add to any least-privilege writeup.
6. **X1** — doc contradiction: 1 API call, do first to calibrate T3/T4.

**NEW/notable surface flags:** cross-account **transfer** is the newest EIP capability and the least IAM-governed; the **accept-is-bound-to-target-account?** question (T3 oracle) is the single highest-impact unknown and is **not answered anywhere in the docs**.

---

## §7 — Hunter preconditions & hard stops

- **Accounts:** 2 minimum (A source, B dest); 3 ideal (C to test T3 non-targeted accept).
- **Perms:** default `ec2:AllocateAddress/AssociateAddress/ReleaseAddress/EnableAddressTransfer/AcceptAddressTransfer/ModifyAddressAttribute/DescribeAddresses*`.
- **Canaries only:** use throwaway EIPs; never point a PTR at a real third-party domain; tear down every allocation (release) to avoid lingering squatter-exposed addresses.
- **Hard stop:** any AWS-fleet credential/identity/ARN, BGP/control-plane reach, or ability to affect another real tenant's live routing ⇒ stop, preserve evidence, flag for disclosure. **Confirm existence, never exploit beyond it** — e.g. for L1, allocating the target IP once is the PoC; do not then weaponize inherited trust.

## §8 — Online-vs-offline drift

Four UserGuide pages (`elastic-ip-addresses-eip`, `transfer-EIPs-intro-ec2`, `using-instance-addressing-eips-releasing`, `Using_Elastic_Addressing_Reverse_DNS`) + eight API refs spot-checked online `.md` vs offline mirror: **byte-identical** modulo cosmetic wrap. The `AllowReassociation` (param) vs `AllowReassignment` (example text) inconsistency and the 7-day/7-hour window contradiction (X1) are present **identically in both copies** → upstream AWS authoring issues, not mirror staleness. `list_ec2.md` read offline only (online truncates condition-key tables), per the standing mandate.

---

*Child of `ec2-networking` hub. Owns: EIP cross-account transfer (hub lead #1) + released-EIP squatting/dangling-DNS + EIP reverse-DNS + associate/disassociate reassociation + EIP read oracles. Defers: BYOIP pool squatting/crypto → `ec2-byoip`; secondary-private-IP takeover → `using-instance-addressing`; launch-time public-IP → `working-with-ip-addresses`; `UnassignPrivateIpAddresses`→EIP-auto-disassociate → `instance-secondary-ip-addresses`.*
