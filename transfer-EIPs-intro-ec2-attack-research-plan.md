# Transfer an Elastic IP Address Between AWS Accounts — Attack / Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/transfer-EIPs-intro-ec2.html
**Service / surface:** Amazon EC2 — the **cross-account Elastic IP transfer handshake** specifically: `EnableAddressTransfer` → (out-of-band notify) → `AcceptAddressTransfer`, plus `DisableAddressTransfer` and `DescribeAddressTransfers`.
**Position in corpus:** Page-level deep-dive **child of `elastic-ip-addresses-eip-attack-research-plan.md`** (which is itself the designated owner of `ec2-networking` hub lead #1). This plan **drills into the transfer sub-feature only** and intentionally does **not** re-derive the sibling EIP surfaces — it cross-references them:
- `elastic-ip-addresses-eip-attack-research-plan.md` (parent — released-EIP squatting/dangling-DNS L1–L3, associate/reassociate steal S1, reverse-DNS D1–D2, read oracles O1–O2, overall EIP model).
- `ec2-byoip-attack-research-plan.md` (BYOIP pool ownership — the reason BYOIP EIPs are non-transferable here).
- `using-instance-addressing-attack-research-plan.md` (secondary private-IPv4 + "EIP rides along").

**Method:** `security-questionbuilder` (boundary-first). Documentation-only; no live AWS calls. All leads are falsifiable claims with a confirm/refute oracle. Online pages read directly; **API Reference and IAM Service Authorization Reference re-read online by two Opus subagents** and quoted verbatim below (the subagent also saved local copies: `API_AcceptAddressTransfer.md`, `API_EnableAddressTransfer.md`, `API_DisableAddressTransfer.md`, `API_DescribeAddressTransfers.md`, `API_AddressTransfer.md`, `list_ec2.html` under `/work/aws-docs/`).

---

## §0 — Executive summary (what this feature actually is)

Cross-account EIP transfer is a **lightweight two-step handshake with no authenticated channel and no account-scoping IAM key**:

1. **Source** `enable-address-transfer --allocation-id X --transfer-account-id Y` — designates exactly one destination account `Y` (the API param is a singular `String`, Required: Yes).
2. **AWS sends NO notification to anyone.** The source operator must relay — out of band — the public IPv4 string to the destination operator.
3. **Destination** `accept-address-transfer --address <IP>` — the accept call's only functional input is the **public IPv4 address string** (`Address`, Required: Yes; plus optional `DryRun` and `TagSpecification.N`). There is **no source-account-id, no transfer-account-id, and no allocation-id** parameter on accept.

Three structural facts drive every lead in this plan, all **confirmed from the authoritative references**:

- **(A) The accept call carries no counterparty identifier, and the docs never state that acceptance is bound to the designated `TransferAccountId`.** The API Reference describes accept purely as "the Elastic IP address you are accepting for transfer." Whether the server enforces that only account `Y` may accept is the single highest-impact unknown and is **not answered anywhere in the documentation** → **TR2 (Critical if unbound)**.
- **(B) No IAM condition key scopes the transfer counterparty.** `EnableAddressTransfer`/`AcceptAddressTransfer`/`DisableAddressTransfer` expose only tag keys + `ec2:AllocationId`/`ec2:Domain`/`ec2:PublicIpAddress`/`ec2:Region`. There is **no** `transfer-account-id` key, **no** `aws:SourceAccount`, **no** `aws:PrincipalOrgID`, **no** `aws:ResourceOrgID` → **TR1 (High)**, and an organization cannot confine transfers to its own accounts via a service key.
- **(C) The destination has no AWS-native inbound signal.** "AWS does not notify transfer accounts"; `DescribeAddressTransfers` is documented purely from the **source** perspective (there is no documented way for a destination to *enumerate* pending transfers addressed to it — it must be told the IP) → **TR3 (High, social-engineering/mis-delivery primitive)**.

Supporting, transfer-specific gaps this page surfaces that the parent plan did not fully develop: a **validate-late asymmetry** (enable succeeds on a transfer that is doomed to fail at accept, and the EIP is not documented-locked while pending — **TR5**); **repeated-enable semantics on one allocation ID are undocumented** (overwrite vs multi-designee race — **TR4**); an **out-of-org transfer destroys IPAM audit history** (forensics evidence-loss — **TR6**); **tags reset** across transfer, voiding ABAC and allowing a `Name`-tag spoof at accept (**TR7**); **14-day source-side post-accept visibility** (tracking asymmetry — **TR8**); and the **"seven days" vs "seven hours" contradiction now confirmed to exist *within* the API Reference itself** (**X1**).

**Highest-value leads:** **TR2** (is accept bound to the designated account?) → **TR1/TR3** (no key + no notification) → **TR4** (repeated-enable race) → **TR6** (audit-history destruction).

---

## §1 — Components, Assets, and Design

### Customer-facing interface
EC2 public API (SigV4 IAM), console **Elastic IPs** pane (Enable / Accept / Disable transfer actions), CLI, PowerShell. No non-SDK endpoints. Two distinct principals in two different AWS accounts drive the flow; there is **no AWS-mediated message channel between them** — the only inter-account linkage is the pending-transfer record keyed by the public IP and the designated account ID.

### Assets
- **The IPv4 address** — the scarce, trust-bearing asset. Whoever ends up holding it inherits any trust bound to it (firewall allowlists, SPF/stale DNS A-records, sender reputation, IP-keyed OAuth). The transfer moves *ownership of trust*, not just an address.
- **The pending-transfer record** (`AddressTransfer` object) — `addressTransferStatus ∈ {pending, disabled, accepted}`, `allocationId`, `publicIp`, `transferAccountId`, `transferOfferExpirationTimestamp`, `transferOfferAcceptedTimestamp`.
- **IPAM audit history** of the EIP — a chain-of-custody/forensics asset that is **destroyed** on out-of-org transfer.
- **Tags** — reset on transfer; a single `Name` tag re-creatable by the accepter at accept time.

### Identifier shape & entropy
- **Public IPv4** — the accept key. 32-bit, **not a secret**: internet-visible, in passive DNS, logs, cert transparency, allowlists. This is precisely why "accept keyed on the IP string" is dangerous: the gating value is public.
- `eipalloc-…` — the source-side allocation handle and the only thing an IAM policy or `DisableAddressTransfer` can name; the **destination never knows it before accept** (accept is by IP), which is why dest-side resource-level scoping is structurally defeated (see parent T2).

### Ownership / trust zones
- **Source account A ↔ destination account B** — the explicit cross-account seam. The crossing mechanism is the handshake; the **breach oracle is "ownership of the EIP moves to an account the source did not intend, or an account other than the designated `TransferAccountId` accepts."**
- **In-organization ↔ out-of-organization** — a forensics/governance boundary: out-of-org transfer silently drops IPAM audit history and escapes org-scoped tracking.
- **Any customer surface ↔ AWS BGP/service plane** — hard stop (routing is AWS-owned).

### Untrusted-data entry points
- `AcceptAddressTransfer.Address` — free IPv4 string → pending-transfer lookup (the critical one).
- `EnableAddressTransfer.TransferAccountId` — free 12-digit account-id string, **existence-only validated at enable; no notification; typo = silent mis-delivery**.
- `AcceptAddressTransfer.TagSpecification.N` — accepter-chosen tags (the `Name`-tag spoof).

### Connection sketch
```
  Account A (SOURCE)                                   Account B (DESTINATION / "transfer account")
  ------------------                                   --------------------------------------------
  enable-address-transfer                              accept-address-transfer
    --allocation-id eipalloc-X        (NO AWS           --address <public IP>        <-- only input is
    --transfer-account-id B  (single)  notification      (no account/alloc param)        the PUBLIC IP string
         |                              — source must        ^
         v                              relay the IP         |  Is this gated to B, or will ANY
  AddressTransfer{status=pending,       OUT OF BAND)         |  account presenting the IP accept? (TR2)
    publicIp, transferAccountId=B,  ------------------------>+
    expires in 7 DAYS... or 7 HOURS? (X1) }
         |
         |  describe-address-transfers  (SOURCE-side view; dest has NO documented inbound-enum)  (TR3)
         |  pending visible 7 days; accepted record visible to SOURCE for 14 days  (TR8)
         v
  Validations deferred to B's ACCEPT call (TR5):
    AddressLimitExceeded | InvalidTransfer.AddressCustomPtrSet | InvalidTransfer.AddressAssociated
    (source can enable a doomed transfer; EIP NOT documented-locked while pending; only SOURCE can remediate)
  On complete: tags RESET (TR7); if out-of-org, IPAM audit history LOST (TR6)
```

---

## §2 — Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Destination account B (or any account C that learns the IP) | EIP owned by source A | `accept-address-transfer --address <IP>` (no account param) | **An account other than the designated `TransferAccountId` accepts** the transfer → cross-account asset hijack (TR2) |
| Compromised/over-trusted principal in source A | Arbitrary attacker account | `enable-address-transfer --transfer-account-id <attacker>` | Transfer enabled to an account IAM cannot exclude (no counterparty key) → exfiltration of a trust-bearing IP (TR1) |
| Attacker impersonating a legitimate source operator | Destination operator | out-of-band "please accept 100.x.x.x" relay; AWS sends no notification | Destination accepts an illegitimate transfer with no AWS-native way to validate it (TR3) |
| Source A at `enable` time | Destination B at `accept` time | three deferred validations (quota / PTR / association) | Source enables a transfer B cannot complete; EIP stays usable by A while "pending"; remediation only source-side (TR5) |
| Insider / compromised account in org O | External account outside O | out-of-org `enable`→`accept` | IPAM audit history for the EIP is destroyed → chain-of-custody evidence loss (TR6) |
| Source A, post-accept | Destination B's holding of the IP | `describe-address-transfers` 14-day retained record | Source retains a durable IP⇄account⇄timestamp record the destination cannot purge (TR8) |
| Any principal with `ec2:DescribeAddressTransfers` | All transfer records in region | unscopable List (no resource type, `ec2:Region` only) | Pending/accepted transfer public IPs + counterparty account IDs readable account-wide (feeds TR3) |
| **Any customer surface** | **AWS BGP / service plane** | — | **HARD STOP** — any AWS-fleet credential/ARN or control-plane reach ⇒ preserve evidence, flag disclosure |

---

## §3 — API / interface surface (verbatim from the API Reference + `list_ec2`)

| Name | Mut? | Request params (exact) | Resource type (list_ec2) | Condition keys (list_ec2) | Notes |
|---|---|---|---|---|---|
| `EnableAddressTransfer` | ✓ | `AllocationId` (String, **Req**), `TransferAccountId` (String, **Req**, singular), `DryRun` | `elastic-ip*` | `aws:ResourceTag`,`ec2:AllocationId`,`ec2:Domain`,`ec2:PublicIpAddress`,`ec2:Region`,`ec2:ResourceTag` | `TransferAccountId` is the **only** param naming the counterparty and has **no matching condition key** → TR1. Designates one account. |
| `AcceptAddressTransfer` | ✓ | `Address` (String, **Req**), `DryRun`, `TagSpecification.N` | `elastic-ip*` | `aws:RequestTag`,`aws:TagKeys`,`ec2:AllocationId`,`ec2:Domain`,`ec2:PublicIpAddress`,`ec2:Region` | **No account/source param; accept keyed on public IP only.** Docs never state acceptance is bound to the designated account → TR2. `TagSpecification.N` → `Name`-tag spoof (TR7); also needs `ec2:CreateTags`. |
| `DisableAddressTransfer` | ✓ | `AllocationId` (String, **Req**), `DryRun` | `elastic-ip*` | `aws:ResourceTag`,`ec2:AllocationId`,`ec2:Domain`,`ec2:PublicIpAddress`,`ec2:Region`,`ec2:ResourceTag` | Keyed on `AllocationId` (only source owns it) ⇒ implicitly source-only; **page states nothing explicit about who may disable or any window**. |
| `DescribeAddressTransfers` | ✗ | `AllocationId.N` (Array, No), `MaxResults` (5–1000), `NextToken`, `DryRun` | **none** (all resources) | `ec2:Region` **only** | Unscopable read oracle. Returns `AddressTransfer[]` incl. `transferAccountId`. Documented **source-side** only; **no documented destination inbound-enumeration** → TR3. |

**`AddressTransfer` object fields:** `addressTransferStatus` (`pending|disabled|accepted`), `allocationId`, `publicIp`, `transferAccountId`, `transferOfferAcceptedTimestamp`, `transferOfferExpirationTimestamp`.

**Account-scoping condition keys — REFUTED across all four actions:** no `transfer-account-id`/`ec2:TransferAccountId`, no `aws:SourceAccount`, no `aws:PrincipalOrgID`, no `aws:ResourceOrgID`. Only tag + EIP-identity + region keys exist.

**Console-only knob the CLI/API does not expose:** the **"Multiple accounts" Transfer type** (console enable flow). The CLI `enable-address-transfer` takes a single `--transfer-account-id`; the console offers "Multiple accounts" only when transferring **multiple EIPs**. Whether this maps *one* EIP to *several* destinations (a race) or merely batches *several* EIPs is **not stated** → TR4.

---

## §4 — Leads (falsifiable, with oracle)

### TR2 — Is acceptance bound to the designated `TransferAccountId`? *(headline — the one unknown the docs refuse to answer)*
*Claim:* Because `accept-address-transfer` takes **only the public-IP `Address`** and the API Reference never states that the accepting principal must be the account named in `EnableAddressTransfer.TransferAccountId`, an account **other than the designated destination** that learns the (public, non-secret) IP can accept the transfer and seize the address.
*Mechanism (doc evidence):* `API_AcceptAddressTransfer` — the only functional parameter is `Address` ("The Elastic IP address you are accepting for transfer."); no source/transfer-account/allocation parameter. `API_EnableAddressTransfer.TransferAccountId` designates one account, but **no doc sentence ties accept back to it**, and there is no IAM key for it. The accept-driving value (the IP) is internet-public.
*Confirm/refute oracle:* 3 accounts — Source S, designated Dest A, unrelated Dest C. S enables transfer of `eipalloc-X` to **A**. Before A accepts, have **C** (which only knows the public IP) call `accept-address-transfer --address <IP>`.
  - **Confirmed/Critical** if C's accept succeeds (acceptance is bound only to the IP, not to the designated account).
  - **Refuted** if C gets a terminal error and only A can accept (acceptance *is* server-side bound to `TransferAccountId`, despite no doc/IAM expression).
*Preconditions/cost:* 3 accounts; free. **Confirm existence only — if C can accept, that single success is the PoC; do not then weaponize inherited IP trust.**
*Severity:* **Critical if unbound** (cross-account hijack of a trust-bearing public IP by any account that reads a public value); otherwise collapses to TR1+TR3.

### TR1 — No account-scoping condition key on the handshake *(High)*
*Claim:* IAM can restrict *which EIP* a principal may enable/accept/disable for transfer, but **cannot** restrict *which account* it goes to or comes from; a compromised or over-trusted source principal can transfer any in-scope EIP to an arbitrary external account, and an org cannot confine transfers to its own accounts via a service key.
*Mechanism:* `list_ec2` rows (above) — only tag/`ec2:AllocationId`/`ec2:Domain`/`ec2:PublicIpAddress`/`ec2:Region`; **no** `transfer-account-id`, `aws:SourceAccount`, `aws:PrincipalOrgID`, `aws:ResourceOrgID` on any of the four actions (subagent-verified).
*Oracle:* In a 2-account test, author a source-side policy that *attempts* to restrict `EnableAddressTransfer` to a specific destination account (there is no key to express it); confirm the transfer completes to an "excluded" account regardless. Confirm an SCP cannot block out-of-org transfer via a service-specific key.
*Severity:* **High** — un-gatable cross-account exfiltration of a scarce trust-bearing asset.

### TR3 — No notification + public-IP accept + no destination-side inbound enumeration = mis-delivery / social-engineering *(High)*
*Claim:* The destination has **no AWS-native signal** that a transfer is pending to it and **no documented way to enumerate inbound transfers**; acceptance depends entirely on an out-of-band, unauthenticated relay of a public IP string. An attacker who controls/imitates a source operator can induce a destination to accept an illegitimate transfer, or a source typo in the destination account ID silently mis-delivers the offer to a wrong (possibly attacker) account.
*Mechanism:* transfer page — "AWS does not notify transfer accounts about pending Elastic IP address transfer requests. The owner of the source account must notify the owner of the transfer account…"; accept = `--address <IP>` only; `DescribeAddressTransfers` documented source-side only (no inbound list for the destination).
*Oracle:* (a) Source S enables transfer to a *wrong* account W; confirm AWS sends **no** notification to W or the intended account (check console/CloudTrail/email). (b) From W, confirm there is **no** describe call that lets W enumerate transfers addressed *to* W without being told the IP. (c) Confirm W can accept knowing only the public IP string.
*Severity:* **High** — social-engineering/mis-delivery of a public IP; chains with TR2 (if unbound, the "wrong account" need not even be designated).

### TR4 — Repeated `enable-address-transfer` on one allocation ID: overwrite vs multi-designee race *(Medium–High)*
*Claim:* The docs are **silent** on what happens when `enable-address-transfer` is called twice on the same `eipalloc` with different `--transfer-account-id` values. If it appends rather than overwrites (or if the console "Multiple accounts" option maps one EIP to several destinations), multiple accounts become eligible acceptors and whoever accepts first wins — a first-come ownership grab / griefing primitive among co-designees.
*Mechanism:* CLI `enable-address-transfer` is singular (`--transfer-account-id`), but console offers a **"Multiple accounts"** Transfer type; neither the page nor the API ref states the semantics of a second enable on a pending allocation (overwrite / append / error). `AddressTransfer` status is per-address (`pending`), suggesting one record — but this is unconfirmed.
*Oracle:* S enables `eipalloc-X` to A; without disabling, enables `eipalloc-X` to B. `describe-address-transfers --allocation-ids eipalloc-X`:
  - **Refuted** if the second call errors ("transfer already enabled") or the record now shows only B (overwrite, single-designee).
  - **Confirmed** if both A and B appear eligible; then have A and B both attempt accept and observe whether both can win (true race) or one gets a terminal error.
*Severity:* Medium–High (non-deterministic cross-account ownership of a public IP if multi-designee is real).

### TR5 — Validate-late asymmetry: source enables a doomed transfer; EIP not locked while pending; remediation only source-side *(Medium)*
*Claim:* Three accept-time validations (`AddressLimitExceeded`, `InvalidTransfer.AddressCustomPtrSet`, `InvalidTransfer.AddressAssociated`) are **deferred to the destination's accept call**. The source can enable a transfer that is structurally doomed, the docs do **not** state the EIP is locked/unusable while pending (the `AddressAssociated` case implies it stays associated and serving live traffic), and the only remediation (disassociate / remove PTR) lives entirely in the **source** account — so a confused destination burns support cycles on opaque errors it cannot self-resolve.
*Mechanism:* transfer page — each exception reads "the source account can enable… but this exception occurs when the transfer account tries to accept the transfer"; remediation sentences all require source action. No sentence states a pending transfer locks the EIP.
*Oracle:* S associates EIP to a live instance, enables transfer to A. Confirm (a) enable succeeds despite association; (b) the IP keeps serving traffic / `describe-addresses` still shows it associated while pending (refutes "locked while pending"); (c) A's accept returns `InvalidTransfer.AddressAssociated` with remediation only S can perform. Repeat with a custom PTR for `AddressCustomPtrSet`.
*Severity:* Medium (griefing / operator-confusion / TOCTOU window; amplifies TR3 phishing).

### TR6 — Out-of-organization transfer destroys IPAM audit history *(Medium)*
*Claim:* Transferring an Amazon-pool EIP to an account **outside the AWS Organization** silently **loses the IPAM audit history** for that address — a deliberate evidence-destruction / chain-of-custody-break vector an insider or compromised account can use to launder an address out of the org's tracking.
*Mechanism:* transfer page — "You can use Amazon VPC IPAM to track the transfer of Elastic IP addresses to accounts in an organization… **If an Elastic IP address is transferred to an AWS account outside of the organization, the IPAM audit history of the Elastic IP address is lost.**"
*Oracle:* With IPAM + Organizations, record an EIP's history (`get-ipam-address-history`), transfer it **out of org** and accept, then re-query history → confirm it is gone/empty; repeat an **in-org** transfer and confirm history is retained (isolates the loss to the org perimeter).
*Severity:* Medium (Lens O audit-evasion / forensics loss on a cross-account path; higher as an insider-exfiltration enabler).

### TR7 — Tag reset voids ABAC and enables a `Name`-tag spoof at accept *(Medium)*
*Claim:* All tags are reset on transfer; any IAM `aws:ResourceTag`-based access control, cost-allocation, or ownership/compliance tagging keyed on the EIP's tags is **silently voided** on both sides, and the destination may re-create a `Name` tag with an **attacker-chosen value** (e.g. mimicking an expected naming convention downstream automation trusts).
*Mechanism:* transfer page — "Any tags that are associated with an Elastic IP address being transferred are reset when the transfer is complete."; accept console step — "create a tag with a key of 'Name' and a value that you specify"; `AcceptAddressTransfer.TagSpecification.N` + `aws:RequestTag`/`aws:TagKeys`.
*Oracle:* Source sets `CostCenter`/`Owner`/`Name` tags and an ABAC policy keyed on `Owner`; after transfer+accept (with a spoofed `Name`), confirm non-`Name` tags are gone and the ABAC decision changed solely due to tag loss.
*Severity:* Medium (control-erasure, attribution-laundering, Name-tag spoof).

### TR8 — 14-day source-side post-accept visibility (tracking asymmetry) *(Low–Medium)*
*Claim:* After a transfer completes, the **source** retains a queryable record (public IP ⇄ destination account ID ⇄ acceptance timestamp) for **14 days** via `describe-address-transfers`; the destination has no stated way to purge or opt out — an observability asymmetry outliving the handshake.
*Mechanism:* transfer page — "Accepted transfers are visible to the source account… for 14 days after the transfers have been accepted."; `AddressTransfer.transferAccountId` + `transferOfferAcceptedTimestamp` returned to source.
*Oracle:* Post-accept, query `describe-address-transfers` daily from the source; confirm the destination account ID + timestamps persist ~14 days and note the exact expiry day; confirm whether anything beyond static transfer metadata (e.g. live association) is exposed.
*Severity:* Low–Medium (privacy/tracking of the destination; not data-plane).

### TR9 — Destination quota checked at accept, no reservation on pending *(Low — mostly a correct-posture rule-out)*
*Claim:* The per-account/per-Region quota (default 5) is enforced **at accept on the destination** (`AddressLimitExceeded`), so a transfer cannot push an *unwilling* destination over quota (accept simply fails) — correct posture. But pending inbound transfers appear to **reserve no quota**, so a near-quota destination can hold more pending offers than it can fulfill, producing confusing late `AddressLimitExceeded` failures.
*Mechanism:* transfer page `AddressLimitExceeded`; quota page — "all AWS accounts have a quota of five (5) Elastic IP addresses per Region, because public (IPv4) internet addresses are a scarce public resource."
*Oracle:* Bring Dest A to 5/5; confirm source `enable` succeeds but A's `accept` fails `AddressLimitExceeded`; enable several transfers to A at 4/5 and confirm quota is only evaluated per-accept (no pending reservation).
*Severity:* Low (operator-confusion; not a cross-tenant DoS — refuted as an exhaustion vector).

### X1 — "Seven days" vs "seven hours" — contradiction confirmed *within* the API Reference *(Low intrinsic / high leverage)*
*Claim:* The accept/expiry window is stated **inconsistently**: the User Guide and `API_DescribeAddressTransfers` say **seven days**; `API_AddressTransfer.transferOfferExpirationTimestamp` says **seven hours** ("the transfer account has **seven hours** to allocate the Elastic IP address to complete the transfer"). The contradiction exists not just UG-vs-API but **between two sibling pages of the same API Reference** — an upstream AWS authoring defect, identical online and offline.
*Mechanism:* verbatim quotes captured from `API_AddressTransfer.md` (seven hours) and `API_DescribeAddressTransfers.md` / transfer page (seven days).
*Oracle:* one live `enable-address-transfer`, read the returned `transferOfferExpirationTimestamp`, compute the delta from now → settles the true window and recalibrates the TR2/TR3/TR4 race windows.
*Severity:* Low intrinsically; **high leverage** (one API call fixes the time budget for every transfer-race lead) and a filable doc-integrity defect (Lens U).

---

## §5 — Null hypotheses / containment boundaries (checked, pages named)

- **BYOIP / IPAM-pool / CoIP EIPs are non-transferable (containment boundary CONFIRMED, not a gap):** transfer page explicitly rejects all three via this flow (BYOIP, "Amazon-provided contiguous IPAM pool", Outposts CoIP). This is a *correct* boundary preventing hijack of customer-owned/org-managed address space through the lightweight handshake. **Oracle:** attempt `enable-address-transfer` on each class, expect enable-time rejection. Cross-ref `ec2-byoip` for pool ownership. (Would be a finding only if any of them *succeeds*.)
- **Lens B (PassRole / confused deputy): N/A** — read all three transfer-flow pages + five transfer API refs; no transfer action accepts a role ARN or acts "on your behalf." The counterparty-confused-deputy shape is captured as TR1/TR3, not a PassRole.
- **Lens H (KMS): N/A** — EIP transfer has no encryption context / CMK surface.
- **Org/SCP global keys (`aws:PrincipalOrgID`/`aws:ResourceOrgID`): absent** on all four actions (subagent-verified in `list_ec2`) → reinforces TR1; an org **cannot** block out-of-org transfer via a service-specific key (TR6's governance gap).
- **Quota as cross-tenant DoS:** refuted — quota is per-account, enforced on the destination at accept (TR9).
- **"Locked while pending" assumption:** doc-silent; `AddressAssociated` exception implies the EIP stays usable → treated as open in TR5, not assumed.

---

## §6 — Priority & NEW/changed surface

1. **TR2** — accept-not-bound-to-designated-account: the single highest-impact unknown, unanswerable from docs. 3 accounts. **Do first.**
2. **TR1 / TR3** — no account key + no notification + no inbound enumeration: the structural backbone; 2–3 accounts.
3. **TR4** — repeated-enable overwrite-vs-race: pure documentation silence; 3 accounts.
4. **TR6** — out-of-org IPAM audit-history destruction: insider forensics-loss; needs IPAM + Organizations.
5. **TR5 / TR7** — validate-late asymmetry + tag-reset/ABAC void: single/2-account, cheap.
6. **X1** — do the 1-call window probe early to calibrate all race windows.
7. **TR8 / TR9** — low-severity, document in any least-privilege/privacy writeup.

**NEW/notable:** cross-account transfer is the newest and least-IAM-governed EIP capability. The **accept-binding question (TR2)** and the **repeated-enable semantics (TR4)** are *documentation silences*, not documented behaviors — exactly where empirical testing is mandatory. TR6 (audit-history destruction) is a filable governance/forensics gap even if every authz check holds.

---

## §7 — Hunter preconditions & hard stops

- **Accounts:** 3 ideal (Source S, designated Dest A, unrelated Dest C for TR2); 2 minimum. IPAM + Organizations for TR6.
- **Perms:** default `ec2:EnableAddressTransfer / AcceptAddressTransfer / DisableAddressTransfer / DescribeAddressTransfers / AllocateAddress / AssociateAddress / DisassociateAddress / ModifyAddressAttribute / DescribeAddresses`, plus `ec2:CreateTags` for the accept-tag path.
- **Canaries only:** throwaway EIPs; never point a PTR at a real third-party domain; **release every allocation at teardown** so no squatter-exposed address lingers; never leave a transfer pending to a real external account.
- **Confirm existence, never exploit beyond it:** for TR2, a single successful accept from a non-designated account **is** the PoC — stop there; do not then redirect real traffic or exercise inherited IP trust. For TR6, confirming the history is empty is the PoC; do not use the laundered address.
- **HARD STOP:** any AWS-fleet credential/identity/ARN, BGP/control-plane reach, or ability to affect another real tenant's live routing ⇒ stop, preserve evidence, flag for AWS-Security disclosure.

## §8 — Online-vs-offline drift & provenance

The target UserGuide page was read online (not present in the offline mirror — `transfer-EIPs-intro-ec2.md` returned NOT FOUND offline). Five API Reference pages and the IAM Service Authorization Reference were read **online** by two Opus subagents and quoted verbatim; local copies were saved to `/work/aws-docs/` (`API_AcceptAddressTransfer.md`, `API_EnableAddressTransfer.md`, `API_DisableAddressTransfer.md`, `API_DescribeAddressTransfers.md`, `API_AddressTransfer.md`, `list_ec2.html`). The **seven-days / seven-hours** contradiction (X1) is present identically across sources → upstream authoring defect, not mirror staleness. IAM condition-key claims (TR1) were taken from `list_ec2` online; the parent plan's offline `list_ec2.md` line numbers (Enable L8005 / Accept L4608 / Disable L7752 / DescribeAddressTransfers L6570) agree with the online rows re-read here.

---

*Child of `elastic-ip-addresses-eip-attack-research-plan.md`. Owns the deep dive on the **cross-account transfer handshake only**: TR1 (no account key), TR2 (accept-binding — headline), TR3 (no-notify/social-eng), TR4 (repeated-enable race), TR5 (validate-late), TR6 (IPAM audit-history loss), TR7 (tag-reset ABAC void), TR8 (14-day source visibility), TR9 (quota posture), X1 (seven-days/hours doc contradiction). Defers released-EIP squatting, associate/reassociate steal, reverse-DNS publishing, and EIP read-oracle inventory to the parent plan; BYOIP pool ownership to `ec2-byoip`.*
