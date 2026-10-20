# Amazon EC2 Elastic IP Addressing (ReleaseAddress & lifecycle) — Attack Research Plan

**Source of leads:** EC2 doc page for the target action `ReleaseAddress`
(`https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReleaseAddress_section.html` / `.md`)
plus the surrounding Elastic IP (EIP) lifecycle: `API_ReleaseAddress`, `API_AllocateAddress`,
`API_AssociateAddress`, `API_AcceptAddressTransfer`, `API_EnableAddressTransfer`,
`API_DisableAddressTransfer`, `API_DescribeAddressTransfers`, `API_ModifyAddressAttribute`,
`API_ResetAddressAttribute`, `API_MoveAddressToVpc`; UserGuide pages `elastic-ip-addresses-eip`,
`working-with-eips`, `using-instance-addressing-eips-releasing`, `transfer-EIPs-intro-ec2`,
`Using_Elastic_Addressing_Reverse_DNS`; and the IAM service-authorization reference `list_ec2`
(offline mirror `/work/aws-docs/docs/...`, cross-checked online at docs.aws.amazon.com).

**Status:** Documentation-derived hypotheses only. Nothing in this document was tested against a
live AWS account. Every "finding" is a boundary that *might not hold*, stated with the exact
observation that would confirm or refute it. A hunter/orchestrator executes this later against an
environment they are authorized to test.

---

## 0. How to use this document

- Each lead reads: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs.
- The target action `ReleaseAddress` is one node in the EIP lifecycle `AllocateAddress → AssociateAddress → DisassociateAddress → ReleaseAddress`, with a cross-account side-channel (`EnableAddressTransfer`/`AcceptAddressTransfer`) and an attribute channel (reverse DNS via `ModifyAddressAttribute`). The highest-value leads live at the **release → re-allocation** seam (a public IPv4 returning to Amazon's shared pool) and the **cross-account transfer** seam.
- **HARD STOP:** the moment evidence shows an identity / credential / ARN / account belonging to **AWS's own service plane** (e.g. the fleet that advertises the IP, the pool-management control plane), stop, preserve evidence, and flag for AWS-Security disclosure. Probing *which specific public IPs AWS currently has free in its pool* shades toward the service plane — keep probes to addresses you released yourself.
- **Shared-responsibility caveat:** "customer forgot to update DNS after releasing an EIP" is a customer-owned risk, not an AWS defect. Several leads below sit on that line; each one states explicitly whether the gap is AWS-owned (a missing preventive control AWS could add) or customer-owned (a footgun). Only AWS-owned gaps are reportable.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **Cross-account address takeover via re-allocation** — reclaim a *specific* public IPv4 that another account just released (or that you released and want back) by naming it in `AllocateAddress --address`, and show inbound traffic/DNS still destined for that IP now lands on your resource.
2. **Cross-account transfer abuse** — accept a transfer not intended for you, push an unwanted address onto a victim account, or exfiltrate an owned EIP out of an org to an external account that IAM/SCP cannot block.
3. **Cross-account IDOR on the lifecycle** — release / disassociate / move / re-tag an EIP owned by another account by naming its `AllocationId` or (deprecated) `PublicIp`.
4. **Enumeration oracle** — use the differential errors of `ReleaseAddress` / `AllocateAddress --address` / `AcceptAddressTransfer` to learn whether a given public IP or allocation id exists and who (roughly) owns it.
5. **Reverse-DNS / lock abuse** — set a PTR for a domain you do not own, or use the rDNS "lock" to block release/transfer as a denial primitive.
6. **Least-privilege / IAM-artifact gaps** — demonstrate an EIP action reachable because no condition key exists to constrain it (transfer destination, allocated address).

---

## 2. Components, Assets, and Design

**Customer-facing interface.** The EC2 query API / SDK / CLI over SigV4 (`ec2.<region>.amazonaws.com`). All relevant actions are standard public SDK actions (no non-SDK/internal endpoints surfaced for this surface). Console routes under **Network & Security → Elastic IPs**.

**Assets.**
- **Elastic IP address** — a *public IPv4 address*, a globally scarce shared resource. This is the crux: unlike most AWS resources, the asset is drawn from and returned to a **pool shared across all AWS customers**. Identifier shapes: the IP itself (`198.51.100.0`, globally meaningful and often publicly known via DNS), and the allocation id `eipalloc-<hex>` (account-scoped handle). Association handle `eipassoc-<hex>`.
- **Address pools:** Amazon's public IPv4 pool (shared, multi-tenant); BYOIP pools (`ipv4pool-ec2-…`, customer-brought); IPAM pools (`ipam-pool-…`); customer-owned Outpost CoIP pools. "a pool that you own" is a stated ownership boundary.
- **Reverse-DNS (PTR) record** attached to an EIP (`PtrRecord`), set via `ModifyAddressAttribute --domain-name`. Acts as an account **lock** on the address.
- **Address transfer** — a short-lived (7-day) pending cross-account hand-off state, visible via `DescribeAddressTransfers`.

**Ownership / trust zones.**
- **Customer account** owns an *allocated* EIP (bound by the SigV4 credential + allocation record).
- **AWS service plane** owns the *shared IPv4 pool* and the fleet that advertises the CIDR (network border group). Released addresses return here. **This is the shared-responsibility line and a hard stop.**
- A second **customer account** (transfer recipient, or the next allocator from the pool) is the cross-tenant counterpart for most leads.

**Identifier entropy / enumerability.** The *public IP* is low-entropy and frequently known to the attacker out-of-band (it was in DNS, allowlists, TLS certs, email SPF/rDNS). `eipalloc-` ids are account-scoped handles; cross-account actions that accept a raw IP (`AcceptAddressTransfer`, deprecated `ReleaseAddress --public-ip`, `AllocateAddress --address`) bypass the need to know the handle.

**Where untrusted data enters.** `--address` (attacker-chosen IP string), `--domain-name` (attacker-chosen PTR domain), `--transfer-account-id` (attacker-chosen recipient), `TagSpecification` values. No parser/translation layer or LLM in this surface (Lenses F/K null — see §8).

```
          allocate (--address lets you pick a SPECIFIC IP)
                 ┌──────────────────────────────────────────┐
                 ▼                                            │
   [Amazon shared IPv4 pool]  ──allocate──►  [EIP owned by Account A] ──associate──► [A's instance/ENI/NATGW/NLB]
        ▲   (multi-tenant,                      │  │  │
        │    AWS service plane)                 │  │  └─ ModifyAddressAttribute --domain-name ► PTR/rDNS record (LOCK)
        │                                       │  └──── EnableAddressTransfer --transfer-account-id ─┐
        └─────────── release ◄──────────────────┘                                                    ▼
                 (returns to shared pool;                                        [pending transfer] ──accept(--address)──► [EIP owned by Account B]
                  recoverable only until                                            7-day window, no AWS notification
                  re-allocated to another account)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Any customer account | Amazon shared IPv4 pool | `AllocateAddress --address <specific IP>` | Obtaining a *specific* IP that was in another party's DNS/allowlist, and receiving their traffic, = address-takeover breach. (Known class; AWS's documented control is "update your DNS".) |
| Attacker account B | Account A's EIP (pending transfer) | `AcceptAddressTransfer --address` (IP only; no source-account/allocation ref) | Account B accepting a transfer it was **not** named as recipient of = cross-account resource acquisition breach. |
| Source account A (insider/compromised) | Any external account | `EnableAddressTransfer --transfer-account-id` | An EIP leaving the org to an account no IAM/SCP condition key can block = exfiltration-control gap (AWS-owned: no `transfer-account-id` condition key exists). |
| Attacker account | Victim account A's EIP | `ReleaseAddress`/`DisassociateAddress`/`ModifyAddressAttribute` naming A's `AllocationId` or deprecated `PublicIp` | Mutating/releasing A's address from B's credential = cross-account IDOR. (Docs imply ownership *is* checked — `AuthFailure` when already owned by another account — this lead verifies that holds on every variant.) |
| Any account | Pool-occupancy / ownership state | differential errors (`AuthFailure` vs `InvalidAllocationID.NotFound` vs `InvalidAddress.NotFound` vs allocate success/fail) | A response that distinguishes "exists & foreign-owned" from "available" for an attacker-chosen IP = enumeration oracle over a shared resource. |
| Any account | Public DNS / anti-spam reputation | `ModifyAddressAttribute --domain-name <domain you don't own>` | A PTR record set for a domain the caller does not control = rDNS spoofing / reputation-forging. |
| Any customer surface | **AWS service plane / fleet advertising the CIDR** | any of the above | Any identity/credential/ARN/host of the pool-management or advertisement fleet = **hard-stop breach; preserve & disclose.** |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Ext-facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `AllocateAddress` | SDK | Yes | Yes | Allocate an EIP; `--address` recovers/picks a **specific** IP; `--public-ipv4-pool`/`--ipam-pool-id`/`--customer-owned-ipv4-pool` select a pool | Yes | any account | IAM keys: `aws:RequestTag`,`aws:TagKeys`,`ec2:Region` only — **no `ec2:PublicIpAddress`**, so policy cannot restrict *which* address is grabbed. |
| `ReleaseAddress` | SDK (target) | Yes | Yes | Release an EIP back to the pool; `AllocationId` required, `PublicIp` **deprecated**; `NetworkBorderGroup` optional | Yes | owner | `AuthFailure` if already allocated to another account. IAM keys incl. `ec2:AllocationId`,`ec2:PublicIpAddress`,`ec2:ResourceTag`. |
| `AssociateAddress` | SDK | Yes | Yes | Bind EIP to instance/ENI; releases any prior auto-assigned public IP back to pool | Yes | owner | Prior public IP "released back into Amazon's pool … cannot reuse". |
| `DisassociateAddress` | SDK | Yes | Yes | Unbind EIP (`--association-id`) | Yes | owner | Default-VPC release auto-disassociates. |
| `EnableAddressTransfer` | SDK | Yes | Yes | Start cross-account transfer; `--allocation-id` + `--transfer-account-id` | Yes | source owner | **No condition key for `transfer-account-id`** → destination uncontrollable by IAM/SCP. |
| `AcceptAddressTransfer` | SDK | Yes | Yes | Accept a transfer; **`--address` only** (IP string) | Yes | recipient | No source-account/allocation reference in request; verify acceptance is bound to the enable-time recipient. |
| `DisableAddressTransfer` | SDK | Yes | Yes | Cancel a pending transfer; `--allocation-id` | Yes | source owner | Revocation-completeness target (Lens AA). |
| `DescribeAddressTransfers` | SDK | No | Yes | List pending/accepted transfers (visible to source 14 days) | Yes | source owner | Disclosure-timing oracle target (account ids of counterparties?). |
| `ModifyAddressAttribute` | SDK | Yes | Yes | Set PTR/reverse-DNS `--domain-name` | Yes | owner | No documented domain-ownership validation; sets an account **lock** on the EIP. Keys incl. `ec2:Attribute`. |
| `ResetAddressAttribute` | SDK | Yes | Yes | Remove PTR record | Yes | owner | Unlocks the address for release/transfer. |
| `MoveAddressToVpc` | SDK (legacy) | Yes | Yes | EC2-Classic → VPC migration | Yes | owner | **Legacy**; IAM key `ec2:Region` only, no resource-level scoping (Lens X). Already covered by sibling `MoveAddressToVpc-attack-research-plan.md`. |
| `DescribeAddresses` / `DescribeAddressesAttribute` | SDK | No | Yes | Enumerate owned EIPs / PTR | Yes | owner | Scoping/leak check. |

**Undocumented/console-hidden knobs:** the deprecated `PublicIp` parameter on `ReleaseAddress` (and EC2-Classic `--public-ip` on `release-address`) is still accepted by the API though the console only exposes the allocation-id path → legacy-parity target (Lens X). `--address` on `AllocateAddress` is a prose-light but powerful "pick a specific IP" capability.

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — Address takeover via release → specific-address re-allocation (Lens EE / U / A) — PRIORITY 1

**Background.** A released EIP "is released to the IP address pool and can be allocated to a different AWS account." `AllocateAddress` accepts an `Address` parameter — "The Elastic IP address to recover or an IPv4 address from an address pool" — letting the caller request a *specific* public IPv4. Recovery fails only "after it is allocated to another AWS account." The only documented protection for the releaser is the advisory "Be sure to update your DNS records and any servers or devices that communicate with the address."

**Security Concern.** A public IPv4 frequently remains referenced after release — in DNS A-records, firewall/security-group allowlists, SPF/rDNS, hardcoded configs, TLS SANs. An attacker who can re-allocate that *specific* address inherits all traffic still destined for it (web requests, callbacks, email, API clients) → traffic interception, phishing from a "trusted" IP, bypass of IP allowlists. This is a known public class (IP reuse / dangling-DNS takeover); the research question is **what, if any, re-allocation friction AWS imposes** (cooldown/quarantine, per-account cadence, pool rotation) and whether an attacker can target a victim's address with non-trivial probability.

**High-level Test Scenarios (falsifiable):**
- **Claim:** A specific public IPv4 released by account A can be re-allocated by attacker account B with `AllocateAddress --address <that IP>` within a practically useful window. → **Mechanism:** `AllocateAddress.Address` + "can be allocated to a different AWS account". → **Oracle:** B's `AllocateAddress --address <A's just-released IP>` returns an `allocationId` for that exact IP (use an IP **you** released from a second controlled account — never probe foreign addresses). → **Preconditions:** two controlled accounts; an EIP released from one. → **Cost:** low (per-EIP charge). → **Severity:** High (traffic interception / allowlist bypass) if no cooldown; the *AWS-owned* question is whether a cooldown exists.
- **Claim:** There is **no quarantine/cooldown** before a released address is re-allocatable to a *different* account. → **Oracle:** measure time-to-reallocate across accounts; a success immediately or within minutes refutes "cooldown protects the releaser". → **Severity:** informational-to-High (defines the real-world risk of the above).
- **Claim:** `AllocateAddress --address` against an IP currently owned by another account is rejected with an error distinct from "available" (enumeration — see Area 4). → routes to Area 4.
- **Concrete impact to demonstrate:** beyond passive traffic interception — **ACME HTTP-01 / DNS-less domain-validation abuse** (a stale A-record pointing at the reclaimed IP lets the attacker pass a CA's domain-control check and mint a valid TLS cert for the victim's name), IP-allowlist bypass (the IP was on a firewall/security-group/partner allowlist), and inbound email/SPF/rDNS inheritance.
- **Look left/right (association-triggered freeing):** when you `AssociateAddress` an EIP onto an instance that had an auto-assigned public IP, that old public IP "is released back into Amazon's pool" — note the docs say ordinary public IPv4 is **not** recoverable by anyone (`--address` recovery is EIP-only), so this freed address goes back to blind-pool rotation rather than being targetable. Treat as a boundary clarification, not a takeover lead.
- **BYOIP sub-case (CRITICAL if it fails):** does releasing an EIP allocated from a **customer-owned BYOIP pool** return it to *that customer's own pool* (pool-scoped, `PublicIpv4Pool` = "a pool **that you own**"), or to Amazon's shared pool? → **Oracle:** account A allocates from its `PublicIpv4Pool`, releases; account B *outside A's Org/IPAM share* attempts `AllocateAddress --address <ip>` / `--public-ipv4-pool <A's pool>`. Expect failure (pool-ownership check). **If B succeeds, releasing a BYOIP address leaks control of RIR-registered, customer-owned address space outside the bringing org** (routing/reputation impact) = Critical. Docs (`ec2-byoip`) don't explicitly state per-address release semantics — confirm against `byoip-working-with.md` first (doc gap).

**Doc evidence:** `API_AllocateAddress` (`Address` param, "allocated to a different AWS account"); `using-instance-addressing-eips-releasing` ("update your DNS records"); `elastic-ip-addresses-eip` (auto-assigned public IP "released back into Amazon's pool … cannot reuse").
**Severity-if-true:** High. **Owner:** the *takeover mechanic* is largely customer-owned (stale DNS is the customer's responsibility — likely **out of scope** as a bug); the *absence of a re-allocation cooldown* and the *targetability* are AWS-owned design questions worth characterizing. **Stop:** do not enumerate the shared pool for foreign-owned addresses; confine to addresses you released yourself.

### Area 2 — Cross-account transfer: acceptance binding, forced-push, and revocation (Lens A / P / AA) — PRIORITY 2

**Background.** Transfer is a two-step handshake: source calls `EnableAddressTransfer --allocation-id --transfer-account-id`; recipient calls `AcceptAddressTransfer --address` (**IP only**). Recipient has 7 days; AWS does **not** notify the recipient; tags reset on completion; source sees pending/accepted transfers for 14 days via `DescribeAddressTransfers`. `DisableAddressTransfer` cancels a pending transfer.

**Security Concern.** `AcceptAddressTransfer` names only the public IP — not the source account or allocation id. If acceptance is bound *only* to knowing the IP (public, guessable) rather than strictly to the account(s) named at enable time, an unintended account could accept the transfer. Conversely, because AWS does not notify and the recipient accepts by IP, a source can *push* an address at a victim (quota/cost consumption, or planting a reputationally-poisoned IP). The reset of tags on transfer may strip ABAC/ownership tags that other controls depend on.

The service model *does* retain the intended recipient: the `AddressTransfer` object carries a `transferAccountId` field and an `addressTransferStatus` enum (`pending | disabled | accepted`). The open question is purely whether `Accept` cross-checks `caller == transferAccountId`.

**High-level Test Scenarios (falsifiable):**
- **Claim (core IDOR):** An account **other than** the enable-time `transfer-account-id` can accept the transfer by naming the IP. → **Mechanism:** `AcceptAddressTransfer` request carries only `Address`; the two handshake calls are never linked by a value the recipient must prove, yet `AddressTransfer.transferAccountId` exists server-side. → **Oracle:** account A enables transfer to account B; account **C** (not named, learns the IP the way an attacker would — DNS/CT logs/Shodan, not out-of-band) attempts `AcceptAddressTransfer --address`. Success, or any error *other than* authorization-denied (e.g. hitting a downstream state check like `AddressLimitExceeded`), supports "identity unchecked". `AccessDenied` = bound correctly. → **Severity:** High if it succeeds.
- **Claim (replay / FSM):** Once `accepted`, a second `AcceptAddressTransfer` for the same address (by the recipient or a third party) is cleanly rejected, not idempotently re-triggerable. → **Mechanism:** `addressTransferStatus` is a strict FSM with no "re-acceptable" state; accepted transfers stay *visible* to the source 14 days — does the allocation still carry an acceptable flag during that window? → **Oracle:** replay accept after success, from the same and a different account; any ownership flip refutes a clean FSM. → **Severity:** High if replay succeeds.
- **Claim (disable/expiry race):** `DisableAddressTransfer` or window-expiry immediately revokes acceptability — no race where an in-flight/retried `Accept` still lands after disable. → **Oracle:** concurrently race `DisableAddressTransfer` (source) against `AcceptAddressTransfer` (recipient); confirm no window where accept still succeeds after `Describe` shows `disabled`. → **Severity:** Medium (defeats a source's cancel of a mistaken/untrusted offer).
- **Claim (forced-push):** A source can force an unwanted/poisoned EIP onto a victim recipient (quota/cost consumption, reputation planting) given no AWS notification and accept-by-IP. → **Oracle:** complete a transfer where the recipient's only action was `AcceptAddressTransfer`; assess any recipient-side gate beyond that call. → **Severity:** Medium.
- **Claim (unvalidated recipient at enable):** `EnableAddressTransfer` accepts any syntactically valid 12-digit `transfer-account-id` without verifying it exists/is eligible — creating silent dangling offers and a confused-deputy risk where `transfer-account-id` is attacker-influenced input to a self-service tool. → **Oracle:** enable to a non-existent account id; a 200 + `pending` (no `InvalidAccountID`-style error) confirms. The UserGuide repeats 3× that all validation exceptions fire "when the transfer account tries to accept", implying enable does no recipient validation. → **Severity:** Low (hardening/operability; raises confused-deputy stakes).
- **Claim (tag-reset / accept-time tag mass-assignment):** Transfer completion **resets tags**, silently removing ABAC/ownership tags a security control relied on; and `AcceptAddressTransfer`'s `TagSpecification.N` lets the recipient set tags at accept whose real semantics are undocumented (the API description is copy-pasted *Describe-filter* boilerplate). → **Oracle:** transfer a tagged EIP; confirm tags gone and whether any policy keyed on them fails open; test what `TagSpecification.N` actually accepts at accept time. → **Severity:** Medium.
- **Claim (accept-time state oracle, chains with core IDOR):** The three accept-time exceptions (`AddressLimitExceeded`, `InvalidTransfer.AddressCustomPtrSet`, `InvalidTransfer.AddressAssociated`) are *differentiated* codes returned to the caller, so — *if* the core-IDOR claim holds — an uninvited party that can name any EIP learns the source address's rDNS and live-association state without being its owner. → **Severity:** Medium combined with core IDOR; Low standalone.
- **Claim (cross-org audit-lineage loss):** Transferring an EIP to an account **outside the organization** silently drops its IPAM audit history — undermining the docs' own "centralized security administration … vetted for security compliance" use case. → **Mechanism:** "If an Elastic IP address is transferred to an AWS account outside of the organization, the IPAM audit history of the Elastic IP address is lost." → **Severity:** Low/Informational (governance/forensics; Lens O).

**Doc evidence:** `transfer-EIPs-intro-ec2` (handshake, 7/14-day windows, "AWS does not notify", tags reset, three accept-time exception codes, IPAM-audit-loss sentence); `API_AcceptAddressTransfer` (`Address` required, no source ref, boilerplate `TagSpecification.N`); `API_AddressTransfer` (`transferAccountId`, `addressTransferStatus` enum — **and a doc inconsistency: its `transferOfferExpirationTimestamp` field says the recipient has "seven hours" while every other page says "seven days"** → confirm the actually-enforced window, Lens U); `API_EnableAddressTransfer`/`API_DisableAddressTransfer`.
**Severity-if-true:** High (cross-account acquisition / replay) / Medium (race, forced-push, tag issues). **Stop:** test only between accounts you control; on cross-account acquisition capture one request/response PoC and stop.

### Area 3 — Missing IAM control over transfer destination & allocated address (Lens S / CC / R) — PRIORITY 3

**Background.** From `list_ec2` service-authorization: `EnableAddressTransfer` and `AcceptAddressTransfer` expose condition keys `ec2:AllocationId`, `ec2:Domain`, `ec2:PublicIpAddress`, `ec2:Region`, `aws:ResourceTag`/`aws:RequestTag` — but **no condition key for the counterparty account** (`transfer-account-id` on enable, source account on accept). `AllocateAddress` (elastic-ip resource) exposes only `aws:RequestTag`/`aws:TagKeys`/`ec2:Region` — **no `ec2:PublicIpAddress`** to constrain which address is allocated.

**Security Concern.** A compromised or insider principal holding `ec2:EnableAddressTransfer` can move any in-scope EIP to **any external AWS account**, and no customer-authored IAM policy or Organizations SCP can constrain the destination, because the key to condition on does not exist. This is an EIP-exfiltration control gap that is **AWS-owned** (only AWS can add the condition key) — distinct from a customer footgun. Likewise, nothing can restrict an account to allocating only from an approved address set.

**High-level Test Scenarios (falsifiable):**
- **Claim:** No IAM/SCP condition can prevent `EnableAddressTransfer` to an arbitrary external account. → **Mechanism:** absence of a destination condition key in `list_ec2`. → **Oracle (safe-first):** `iam:SimulateCustomPolicy` — attempt to author a Deny that restricts `transfer-account-id`; confirm there is no key to express it. Then, under a scoped role, confirm an enable to an unlisted account is not denied. → **Severity:** High as an exfiltration/data-governance gap; **report to aws-security (Tier 2, AWS-owned missing control)**.
- **Claim:** `AllocateAddress` cannot be scoped to specific addresses/pools by IAM. → **Oracle:** confirm `ec2:PublicIpAddress` is absent from `AllocateAddress`'s keys (present only for release/associate). → **Severity:** Low–Medium hardening gap.
- **Claim:** `MoveAddressToVpc` has only `ec2:Region` (no resource-level), so it cannot be tag/ownership-scoped. → cross-ref sibling plan. → **Severity:** Low (legacy, EC2-Classic retired).

**Doc evidence:** `service-authorization/list_ec2` per-action condition-key lists (verbatim above). **Severity-if-true:** High (transfer destination). **Owner:** AWS (missing condition key). **Stop:** policy simulation is read-only; prefer it before any live scoped call.

### Area 4 — Enumeration / existence oracle over a shared resource (Lens A oracles) — PRIORITY 4

**Background.** The lifecycle exposes several differential responses on attacker-chosen identifiers: `ReleaseAddress` → `AuthFailure` ("already allocated to another AWS account") vs `InvalidAllocationID.NotFound` vs `InvalidAddress.NotFound` (wrong `NetworkBorderGroup`); `AllocateAddress --address` → success vs failure; `AcceptAddressTransfer` → `InvalidTransfer.AddressCustomPtrSet` / `AddressAssociated` / `AddressLimitExceeded`.

**Security Concern.** Because the public IP is a shared, externally meaningful identifier, any response that distinguishes "this IP exists and is foreign-owned" from "this IP is free" is an oracle over *other tenants' / the shared pool's* state — e.g. mapping which public IPs are currently live EIPs, or confirming a target's address is still held. The transfer exceptions additionally leak the *reverse-DNS* and *association* state of an address to a party attempting to accept it.

**High-level Test Scenarios (falsifiable):**
- **Claim:** `AllocateAddress --address <IP>` returns distinguishable outcomes for "foreign-owned" vs "available". → **Oracle:** compare the error for an IP you know is foreign-owned (one you just released that another of your accounts grabbed) vs a never-allocated IP. A stable difference = oracle. → **Severity:** Low–Medium (recon; elevates other leads).
- **Claim:** `ReleaseAddress` error codes distinguish ownership/existence of a named `AllocationId`/`PublicIp`. → **Oracle:** `AuthFailure` vs `NotFound` on controlled vs foreign ids. → **Severity:** Low.
- **Claim:** `AcceptAddressTransfer` exceptions (`AddressCustomPtrSet`, `AddressAssociated`) reveal a target address's rDNS/association state to a non-owner attempting accept. → **Severity:** Low–Medium (info leak).
- **Note (defense):** the allocation-id carries structure; a *foreign* `eipalloc-` id generally cannot be fabricated usefully — treat an all-`NotFound` result as a genuine null. **`DryRun` is caller-IAM only — NOT an ownership oracle** (evaluated before resource resolution).

**Doc evidence:** `API_ReleaseAddress` (error text), `API_AllocateAddress`, `transfer-EIPs-intro-ec2` (exception list). **Severity-if-true:** Low–Medium. **Stop:** do not sweep the shared pool for foreign addresses; demonstrate the *signal* on your own released addresses only.

### Area 5 — Reverse-DNS: domain-ownership & the address lock (Lens G / U / L) — PRIORITY 5

**Background.** `ModifyAddressAttribute --domain-name <domain>` sets a PTR record for an owned EIP; the docs list a forward A-record as a "best practice" prerequisite but describe no server-side domain-ownership check in the API path. A set rDNS record "locks" the EIP to the account — it "cannot be released … until the record is removed", and blocks transfer (`AddressCustomPtrSet`). Support-set rDNS locks even harder (requires a support case to unlock).

**Security Concern.** (a) If no ownership of the PTR domain is enforced, a caller can publish a PTR pointing their (legitimately-held) IP at an arbitrary domain — forging rDNS used by anti-spam/reputation systems, or creating misleading forward-confirmed-rDNS appearances. (b) The lock is a self-inflicted availability constraint but could be leveraged: a transfer recipient-side or automation flow that assumes an address is releasable may wedge.

**High-level Test Scenarios (falsifiable):**
- **Claim:** `ModifyAddressAttribute --domain-name` accepts a domain the caller does not control, with no verification. → **Oracle:** set `--domain-name victim-domain.example` on an owned EIP; `PtrRecordUpdate.Status` progresses without any ownership challenge = no validation. → **Severity:** Low–Medium (rDNS spoofing; AWS mediates actual PTR publication, so impact is bounded — characterize it).
- **Claim:** The rDNS lock can block release/transfer unexpectedly (availability/footgun). → **Oracle:** set rDNS, attempt `ReleaseAddress` → "locked to your account" error. → **Severity:** Low (documented behavior; test for surprising edge cases e.g. partial lock after `ResetAddressAttribute`).

**Doc evidence:** `Using_Elastic_Addressing_Reverse_DNS` (no ownership check documented; lock semantics; Support lock). **Severity-if-true:** Low–Medium. **Stop:** do not point rDNS at a domain to actually abuse third-party reputation; prove the *acceptance* of an unowned domain, not downstream abuse.

### Area 6 — Cross-account IDOR on the lifecycle & legacy-parameter parity (Lens A / X) — PRIORITY 6

**Background.** `ReleaseAddress`/`DisassociateAddress`/`ModifyAddressAttribute` act on an EIP named by `AllocationId` (and `ReleaseAddress` still accepts the **deprecated** `PublicIp`, plus EC2-Classic `--public-ip`). The docs strongly imply ownership is enforced (`AuthFailure` when the address is "already allocated to another AWS account").

**Security Concern.** Verify the ownership check holds on **every** naming path and every sibling action — including the legacy `PublicIp` path and `MoveAddressToVpc` — so that a foreign `AllocationId`/`PublicIp` cannot release, disassociate, re-tag, or move another account's address. Legacy/deprecated variants are the classic place an authz check is weaker than its modern twin.

**High-level Test Scenarios (falsifiable):**
- **Claim:** `ReleaseAddress` with a foreign `AllocationId` (or foreign deprecated `PublicIp`) is rejected on ownership, not merely existence. → **Oracle:** from account B, target account A's allocation id and A's public IP; expect `AuthFailure`, not success. Success on *either* path = cross-account IDOR (Critical). → **Severity:** Critical if it succeeds.
- **Claim:** The deprecated `PublicIp` path enforces the **same** ownership check as `AllocationId` (legacy parity). → **Oracle:** compare both on a foreign address. → **Severity:** High (parity gap).
- **Claim:** `ModifyAddressAttribute`/`ResetAddressAttribute` on a foreign allocation id is denied. → **Severity:** High.

**Doc evidence:** `API_ReleaseAddress` (`PublicIp` Deprecated; `AuthFailure`), target code-example page (shows SDKs still expose `PublicIp`/`AllocationId`). **Severity-if-true:** Critical/High. **Stop:** on any cross-account success, capture the single request/response as PoC and stop — do not release/mutate further foreign resources.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Re-allocate a victim's just-released specific IP and intercept traffic | `AllocateAddress --address` + shared pool | "update your DNS records"; recovery denied once "allocated to another AWS account" (but not before) |
| Accept a transfer not intended for you | `AcceptAddressTransfer` (IP-only request) | 7-day window; enable-time `transfer-account-id` (verify it binds acceptance) |
| Push an unwanted/poisoned EIP onto a victim | `EnableAddressTransfer` + no-notify accept | none documented beyond recipient running accept |
| Exfiltrate an org EIP to an external account | `EnableAddressTransfer` | **no `transfer-account-id` condition key** (SCP/IAM cannot block) |
| Release / re-tag / move another account's EIP | `ReleaseAddress`/`ModifyAddressAttribute`/`MoveAddressToVpc` | `AuthFailure` ownership check (verify parity on deprecated `PublicIp`) |
| Map shared-pool / ownership state | differential errors | allocation-id checksum/structure; `DryRun` ≠ ownership oracle |
| Forge reverse DNS for an unowned domain | `ModifyAddressAttribute --domain-name` | forward A-record "best practice" (verify if enforced); AWS mediates PTR publication |
| Wedge release/transfer via rDNS lock | PTR lock | documented lock; Support-lock |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Customer stale DNS / dangling records after releasing an EIP** — the *mechanism* of inheriting traffic is enabled by the customer failing to update DNS/allowlists. The takeover itself is a customer-owned (shared-responsibility) risk and is **not an AWS defect**; only AWS-owned sub-questions (re-allocation cooldown, targetability, missing condition keys) are in scope.
- **AWS's shared IPv4 pool internals / the fleet that advertises the CIDR (network border group)** — service plane. Enumerating which specific public IPs AWS currently holds free, or touching the advertisement/pool control plane, is a **hard stop**.
- **Per-EIP billing / quota of 5** as a pure cost nuisance against your own account (single-tenant self-DoS) — out of scope, and **quota/cost griefing is refuted by docs**: neither `AllocateAddress` nor `ReleaseAddress` exposes a target-account parameter, so every allocation lands in the *caller's* own account/quota/bill. The only in-scope forced-cost path is pushing an EIP onto a victim via *transfer* (Area 2).
- **IPAM cross-org audit-history loss on transfer** — a governance/forensics gap (traceability), not an access-control break; flagged (Area 2) but low severity.
- **BYOIP BGP hijacking / ROA / upstream routing** — out of scope (network/routing layer, not the HTTP/application EC2 API surface).
- **DNS rebinding and client-side issues** — not applicable to this server-side API surface.
- **Bugs in the third-party SDK example repos** linked from the target page (aws-doc-sdk-examples) — reference code, out of scope.

---

## 8. Null hypotheses / doc gaps (lenses checked, with pages read)

- **Lens F (translation/injection) — N/A.** Read `API_AllocateAddress`, `API_ReleaseAddress`, `working-with-eips`: the surface takes scalar IDs/IPs/tags; no query/wire-protocol/parser/translation layer.
- **Lens K (prompt injection) — N/A.** No LLM/agent in the EIP lifecycle (read all UserGuide EIP pages).
- **Lens H / W (KMS / attestation) — N/A.** No encryption-context or attestation gate on EIP actions (checked `list_ec2` condition keys — only tag/region/address keys).
- **Lens D / V (data→control plane / network segmentation) — N/A at the API layer.** The service-plane fleet is out of scope (§7); no customer-reachable control ENI in this surface.
- **Lens Q (file upload) — N/A.** No upload field (read allocate/associate/transfer/rDNS pages).
- **Lens J / FF (OAuth / JWT) — N/A.** SigV4-only; no 3P linking or bearer tokens.
- **Lens BB / DD / CC(full) — N/A.** No multi-parser request path, caching layer, or upstream-asserted-identity header in this SDK surface (the transfer-destination gap is captured as a condition-key gap in Area 3, not a CC fail-open).
- **Doc gaps to confirm against a live account first:**
  - Whether any **cooldown/quarantine** exists before a released IP is re-allocatable to a *different* account (Area 1) — docs neither confirm nor deny; only the binary "already allocated to another account" gate is documented.
  - Whether `AcceptAddressTransfer` acceptance is **strictly bound** to the enable-time `transfer-account-id` (Area 2) — the API request does not reference it; no prose asserts the binding as a security guarantee.
  - **Transfer window inconsistency: "seven days" (Enable/Describe/UserGuide) vs "seven hours" (`API_AddressTransfer.transferOfferExpirationTimestamp`)** — determine the actually-enforced expiry (Area 2/3).
  - **BYOIP release semantics** — no fetched page states whether a released BYOIP/CoIP address returns to the customer's pool or Amazon's shared pool; read `byoip-working-with.md` / `byoip-onboard.md` before testing Area 1's BYOIP sub-case.
  - Whether `ModifyAddressAttribute --domain-name` performs any **domain-ownership** verification (Area 5) — docs describe only a "best practice" forward A-record.
  - Exact **error-code differentials** for existence/ownership (Area 4) — `API_ReleaseAddress`/`API_AllocateAddress` **Errors** tables are empty (defer to Common Errors); pull the EC2 Common Errors reference to design the oracle precisely. `DescribeAddresses` behavior for a **non-owned** `AllocationId`/`PublicIp` is unspecified.
  - Whether a source can create **multiple concurrent pending offers** for one `AllocationId` (second overwrites vs errors) — undocumented; relevant to replay/race analysis (Area 2).
  - `AcceptAddressTransfer` **`TagSpecification.N`** real accept-time semantics (its API description is copy-pasted Describe-filter boilerplate).
  - Minor doc nit: `ReleaseAddress` lists `AllocationId` as "Required: No" directly under "This parameter is required." (unreconciled with the deprecated `PublicIp` alternate).

---
*Documentation-derived plan; no live testing performed. Prioritize Areas 1–3. Hard-stop on any AWS service-plane identity/credential/host; preserve evidence and route to AWS-Security.*
