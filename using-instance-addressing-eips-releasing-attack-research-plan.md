# Release / Recover an Elastic IP Address — Attack Research Plan

Source of leads:
- Target page: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing-eips-releasing.html` (= `.md`), "Release an Elastic IP address" (Console / AWS CLI `release-address` / PowerShell `Remove-EC2Address`), plus the in-page "recover" sub-section (`allocate-address --address <ip>` / `New-EC2Address -Address`).
- `API_ReleaseAddress.md` and `API_AllocateAddress.md` (fetched online 2026-10-15; byte-identical risk not checked offline — API_ReleaseAddress/API_AllocateAddress not mirrored locally).
- Offline IAM reference `/work/aws-docs/list_ec2.html`: `ReleaseAddress` action detail (line 30293), `AllocateAddress` action detail (line 12467). Re-verify by line.

Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Scope note / sibling plans.** This is a *narrow procedural sibling* in the Elastic-IP cluster. The broad EIP leads already live in dedicated plans and are **NOT re-derived here**:
> - `elastic-ip-addresses-eip-attack-research-plan.md` (OVERVIEW) — cross-account **transfer** hijack (T1-T5), released-EIP shared-Amazon-pool **squatting** (L1-L3), **reverse-DNS** (D1-D2), forced reassociation (S1), unscopable read oracles (O1-O2), NetworkBorderGroup zero-IAM-key (B1), 7-day/7-hour transfer contradiction (X1).
> - `working-with-eips-attack-research-plan.md` (PROCEDURAL) — IPAM-pool targeted/sequential **land-grab** (N2), `GetIpamPoolAllocations` cross-account oracle (N2a), AllocateAddress IPAM scoping is tag-only (N1), AssociateAddress private-IP binding (N3).
> This plan OWNS only the **release ↔ recover** surface those two did not fully reach: the ReleaseAddress IAM key-set, the release-vs-allocate **scoping asymmetry**, the **recover-by-`--address`** mechanics, the **[Default VPC] auto-disassociate-on-release** footgun, the **re-release `AuthFailure` recon oracle**, and the **tag/AllocationId continuity loss** on recovery.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (EIP pools are AWS-fleet-owned), stop, preserve evidence, flag for AWS-Security disclosure.
- Dummy/canary only. Release and recover are **mutating**; `--dry-run` and read-only `describe-addresses` are the only non-mutating probes. Do not release an EIP you cannot afford to lose to the pool — release is practically irreversible once another account grabs it.

---

## 1. Pentest Objectives
Concrete boundary-breach outcomes this page's surface could enable:
1. **Scoping-asymmetry escape:** demonstrate that an IAM policy can lock *which* EIP a principal may **release** but cannot lock *which* IP a principal **recovers/allocates** — recover an IP the policy author believed was out of reach.
2. **Cross-account recovery / dangling-IP takeover:** recover (via `allocate-address --address`) a specific IPv4 that another account released, before/instead of the original owner, inheriting its DNS/trust residue — proving the "cannot recover after it is allocated to another AWS account" guarantee is a **race**, not an IAM control.
3. **Release-induced service interruption + takeover:** in a **default VPC**, release force-disassociates a *live, in-use* EIP; show a principal scoped only to `ec2:ReleaseAddress` (by tag/AllocationId) can tear a victim's address off a running resource and return it to the pool.
4. **Re-release error-differential recon:** use the `AuthFailure`-vs-success response of ReleaseAddress on an already-released IP as an oracle to detect whether a previously-owned address is still floating or has been claimed by another account.
5. **ABAC/reference dropout on recovery:** show that a recovered EIP returns with **no tags** (and possibly a **new AllocationId**), silently voiding any ABAC policy or automation keyed on the old tags/ID.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 control-plane API over SigV4 (`https://ec2.<region>.amazonaws.com`), console route **EC2 → Elastic IPs**, CLI `aws ec2 release-address` / `aws ec2 allocate-address`, PowerShell `Remove-EC2Address` / `New-EC2Address`. All synchronous.

**Assets / resources.**
- **Elastic IP address (EIP):** a public IPv4 drawn from an AWS-owned regional pool (or a BYOIP / IPAM / CoIP pool). Two identifiers: the **AllocationId** (`eipalloc-…`) and the **public IPv4 value** (`203.0.113.3`). The IP value is a *global, non-account-scoped, predictable* identifier; the AllocationId is account-scoped and opaque.
- **The regional IP pool** — AWS-fleet-owned shared asset. A released EIP returns here and "can be allocated to a **different AWS account**" (API_AllocateAddress). This is the shared multi-tenant surface.
- **NetworkBorderGroup (NBG)** — the AZ/Local-Zone/Wavelength set an IP is advertised from; "IP addresses cannot move between network border groups." No IAM condition key exists for it (overview plan B1).
- **Tags** on the EIP — ABAC inputs; **not preserved** across release→recover.

**Who owns what.** Customer account owns the *allocation* (AllocationId) while held; AWS owns the *IP value and the pool*. Release transfers the IP value back to AWS's pool, severing the customer's ownership of that value even though DNS/firewall/allowlist references to the value persist in the world. This value↔ownership split is the core of every lead below.

**Where untrusted/attacker input enters.** The `Address` parameter of AllocateAddress (recover a *specific* IPv4 the caller names) and the `AllocationId`/`PublicIp`/`NetworkBorderGroup` parameters of ReleaseAddress. The caller fully controls which IP value to attempt to recover.

```
   customer A (holds EIP 203.0.113.3, DNS A-record points here)
        | release-address --allocation-id eipalloc-X
        v
  +-------------------------------+     [Default VPC] auto-disassociates live resource first
  |  AWS regional IPv4 pool        |<--- IP value 203.0.113.3 returns here (shared, AWS-owned)
  +-------------------------------+
        ^  allocate-address --address 203.0.113.3   (RACE: first caller wins)
        |
   customer B (attacker)  --- recovers the specific value, inherits A's dangling DNS/trust
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| IAM principal scoped to release a tagged EIP | A *live, associated* EIP on another resource in the same account (default VPC) | `ReleaseAddress` auto-disassociates then releases | A running resource loses its public IP + the IP enters the pool, driven by a principal who held only `ec2:ReleaseAddress` scoped by tag → unexpected DoS/teardown |
| Account B (attacker) | IP value just released by Account A (AWS pool) | `AllocateAddress Address=<A's old IP>` | Account B's `describe-addresses` shows it now owns A's former public IPv4 → cross-account value takeover (race) |
| IAM policy author's intent ("principal may only touch *these* EIPs") | Any IP the principal recovers/allocates | `AllocateAddress` has **no `ec2:PublicIpAddress`/`ec2:AllocationId` key** | A principal recovers/allocates an IP value the policy intended to exclude → scoping-asymmetry escape |
| Account A (recovering its own IP) | AWS pool / another account | server-side "cannot recover after allocated to another account" + `AuthFailure` on re-release | Differential error (`AuthFailure` vs success) reveals cross-account ownership state of an IP the caller no longer holds → recon oracle |
| ABAC policy / automation keyed on EIP tags or AllocationId | The *recovered* EIP (tags dropped, possibly new AllocationId) | recover returns a fresh resource with no tags | A tag-gated policy that governed the EIP before release does not apply after recover → silent control dropout |
| **Any customer surface** | **AWS's own IPv4 pool / fleet identity** | pool allocation | **Hard stop** — reaching pool-internal state or an AWS-owned account/credential = disclosure-grade breach |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ReleaseAddress` (`ec2:ReleaseAddress`) | POST/Query | Existing | **Mutating** | External | Release an EIP back to the pool | Yes (ec2 endpoint) | Any principal with `ec2:ReleaseAddress` on the `elastic-ip` resource | **Scopable** by `ec2:AllocationId`, `ec2:PublicIpAddress`, `ec2:Domain`, `aws:ResourceTag`, `ec2:ResourceTag`, `ec2:Region` (list_ec2 L30293). Params: `AllocationId` (prose "required" / model "Required: No"), `PublicIp` (**Deprecated** but accepted), `NetworkBorderGroup`, `DryRun`. |
| `AllocateAddress` (`ec2:AllocateAddress`) | POST/Query | Existing | **Mutating** | External | Allocate a *new* EIP **or recover a specific released IP** (`Address=<ip>`) | Yes | Any principal with `ec2:AllocateAddress` on `elastic-ip*` | **NOT scopable by IP value** — only `aws:RequestTag`, `aws:TagKeys`, `ec2:Region` on `elastic-ip*` (list_ec2 L12467). `Address`, `NetworkBorderGroup`, `PublicIpv4Pool`, `IpamPoolId`, `CustomerOwnedIpv4Pool`, `Domain`, `TagSpecification` params. `ipam-pool`/`ipv4pool-ec2` resource types add `ec2:ResourceTag`. |
| `DescribeAddresses` | GET/Query | Existing | Non-mutating | External | List EIPs | Yes | account-wide, no resource scoping (overview O1) | Read oracle; owned by overview plan. |
| Console "Release Elastic IP addresses" | — | Existing | Mutating | External | Wraps ReleaseAddress | — | console users | — |

**Undocumented/hidden-knob notes:**
- `AllocateAddress.Address` ("The Elastic IP address to recover **or** an IPv4 address from an address pool") is the recover-by-value knob — the console surfaces "Recover" only lightly; the raw param lets you name any IPv4.
- `ReleaseAddress.PublicIp` is marked **Deprecated** yet still a documented accepted parameter → a second, legacy way to name the resource (Lens X parity check: is the `PublicIp` path condition-key-checked the same as the `AllocationId` path?).
- `ReleaseAddress.AllocationId`: prose says "This parameter is required." while the model says "Required: No" → doc-vs-model contradiction (Lens U); and if neither `AllocationId` nor `PublicIp` is required at the model level, what does a release with only `NetworkBorderGroup` resolve to?

---

## 5. Recommended Areas of Focus

### Area 1 — Release↔Allocate IAM scoping asymmetry (HEADLINE) — Lens S, Lens X
**Background.** `ReleaseAddress` carries a rich condition-key set on `elastic-ip`: `ec2:AllocationId`, `ec2:PublicIpAddress`, `ec2:Domain`, `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, `ec2:Region` (list_ec2 L30293). `AllocateAddress` on `elastic-ip*` carries only `aws:RequestTag/${TagKey}`, `aws:TagKeys`, `ec2:Region` (list_ec2 L12467) — **no `ec2:PublicIpAddress`, no `ec2:AllocationId`.**

**Security Concern.** A policy author can precisely constrain *which* EIP a principal may **release** (by IP value or AllocationId or tag), and may reasonably believe the inverse — "this principal can only (re)allocate addresses we approve" — is equally expressible. It is not: the IP value a principal **recovers or allocates is unscopable at the IAM layer.** Any holder of `ec2:AllocateAddress` can attempt to recover/allocate *any* IPv4 value, bounded only by server-side pool state (availability + "not owned by another account") and `ec2:Region`.

**High-level Test Scenarios.**
- **Claim:** With an identity policy `Allow ec2:AllocateAddress` + a `Deny ec2:AllocateAddress` conditioned on `ec2:PublicIpAddress`/`ec2:AllocationId`, the Deny is **inert** → **Mechanism:** those keys are absent from the AllocateAddress rows (L12467) → **Oracle:** `allocate-address --address <denied-ip>` under the scoped role still succeeds (or fails only on availability, never `AccessDenied`); `iam:SimulateCustomPolicy` with that policy returns `allowed` for the IP → **Severity:** Medium (customer-expectation gap; AWS-owned key-coverage asymmetry) — **but see Area 2 for the cross-account escalation.**
- **Claim:** The deprecated `ReleaseAddress.PublicIp` path and the `AllocationId` path do **not** enforce the same condition keys → **Mechanism:** two ways to name one EIP; `ec2:PublicIpAddress` and `ec2:AllocationId` are both listed, but does a `PublicIp`-named release evaluate `ec2:AllocationId` conditions (and vice-versa)? → **Oracle:** release a tag/AllocationId-Deny-scoped EIP via `--public-ip` and see whether the Deny still bites → **Severity:** Medium if a legacy naming bypasses a condition.
- **Stop condition:** asymmetry demonstrated by one SimulateCustomPolicy + one scoped `--dry-run`; no need to actually mutate.
**Doc evidence:** list_ec2 L12467 (AllocateAddress), L30293 (ReleaseAddress). **Severity-if-true:** Medium (escalates via Area 2).

### Area 2 — Cross-account recovery of a specific released IP (dangling-IP takeover race) — Lens EE, Lens U, Lens A
**Background.** API_AllocateAddress: *"After you release an Elastic IP address, it is released to the IP address pool and can be allocated to a **different AWS account** … To attempt to recover an Elastic IP address that you released, specify it in this operation."* And: *"You **cannot** recover an Elastic IP address that you released **after it is allocated to another AWS account**."* The target page restates: *"You can't recover an Elastic IP address if it has been allocated to another AWS account."*

**Security Concern.** The only barrier against another account recovering a just-released IPv4 is **a race plus a server-side ownership check** — there is no IAM key, no cooldown documented on this page, and no notification. Because `Address` lets a caller name a *specific* IPv4 (predictable, globally-visible identifier) and `AllocateAddress` is unscopable by IP (Area 1), an attacker who learns that a target's EIP was released (or who watches a target's known IP) can repeatedly attempt `allocate-address --address <target-ip>` and win the IP the instant it lands in the pool — inheriting any DNS A-records, firewall allowlists, SPF/MX entries, and partner allowlist trust that still point at that value. This is the EIP-value analogue of the whoAMI / Bucket-Monopoly predictable-name land-grab.

**High-level Test Scenarios.**
- **Claim:** Account B can recover an IPv4 that Account A released, before A re-recovers it → **Mechanism:** pool is cross-account; `Address` targets a specific value; no cooldown on this page → **Oracle:** A releases `203.0.113.3`; B runs `allocate-address --address 203.0.113.3` and B's `describe-addresses` returns ownership of it → **Severity:** **High–Critical** (cross-account value takeover + dangling-DNS hijack). *Requires two consenting in-scope test accounts; never target a real third party's IP.*
- **Claim:** There is no enforced cooldown/quarantine returning a released IP to its *former* owner first → **Mechanism:** this page lists only two recovery blockers (another-account allocation; limit exceed) — silent on timing → **Oracle:** measure the window between release and successful cross-account recover; a near-zero window = pure race → **Severity:** High.
- **Claim:** `NetworkBorderGroup` does not scope *who* can recover, only *where* the IP lives → **Mechanism:** NBG has zero IAM key (overview B1); recover must match the IP's NBG but any account can supply it → **Oracle:** recover with correct NBG from a second account → confirms NBG is not an isolation control.
- **Stop condition:** one successful cross-account recover (or a clean refusal proving a cooldown/owner-preference exists). **Hard stop** if the recovered IP exposes any AWS-pool-internal metadata.
**Doc evidence:** API_AllocateAddress (recover/cross-account prose); target page recovery rules. **Severity-if-true:** High–Critical. *(Cross-ref overview L1-L3 for the general squatting framing; this plan adds the recover-by-`--address` targeting + race-window specifics.)*

### Area 3 — [Default VPC] release force-disassociates a LIVE EIP — Lens AA, Lens L, Lens U
**Background.** The target UserGuide page states the EIP to release *"must not be currently associated with an AWS resource."* The API tells a different story: **"[Default VPC] Releasing an Elastic IP address automatically disassociates it from any instance that it's associated with."** Only **[Nondefault VPC]** returns `InvalidIPAddress.InUse` and requires manual disassociation first.

**Security Concern.** In a **default VPC**, `ReleaseAddress` is *not* gated by the association precondition the UserGuide implies — it will tear a live, actively-serving EIP off a running instance and return it to the pool in one call. A principal scoped (by tag/AllocationId) to release "unused" EIPs can therefore disrupt a *production, in-use* address: the resource loses connectivity and the IP becomes immediately recoverable by anyone (chains to Area 2). The precondition the operator relies on as a safety guarantee ("I can't release something that's in use") is enforced only in nondefault VPCs — a doc-vs-mechanism gap (Lens U).

**High-level Test Scenarios.**
- **Claim:** In a default VPC, `release-address` on an *associated* EIP succeeds and silently disassociates the live resource → **Mechanism:** API "[Default VPC] … automatically disassociates" → **Oracle:** associate an EIP to a canary instance in a default VPC, release it, observe the instance lose the public IP and the IP leave the account → **Severity:** High (unexpected teardown + feeds takeover). **Confirm whether default VPCs still exist / are reachable in the test account** (newer accounts may lack them → mark doc-gap).
- **Claim:** A tag-scoped `ReleaseAddress` grant intended for "stale EIP cleanup" automation can be aimed at a live production EIP sharing the tag → **Mechanism:** `aws:ResourceTag` scoping on ReleaseAddress + auto-disassociate → **Oracle:** scoped role releases a live tagged EIP → **Severity:** High (intra-account cross-team DoS).
- **Stop condition:** one default-VPC release of a canary association demonstrating auto-disassociate.
**Doc evidence:** target page "must not be currently associated" vs API_ReleaseAddress "[Default VPC] … automatically disassociates". **Severity-if-true:** High.

### Area 4 — Re-release `AuthFailure` differential as a cross-account ownership oracle — Lens A, Lens O
**Background.** API_ReleaseAddress: *"If you attempt to release an Elastic IP address that you already released, you'll get an `AuthFailure` error **if the address is already allocated to another AWS account**."* The `PublicIp` parameter (deprecated) still lets a caller name an IP by value.

**Security Concern.** The error returned by ReleaseAddress on an IP the caller no longer owns is **state-dependent**: `AuthFailure` specifically when the IP has been grabbed by *another account*, versus a different error (e.g. `InvalidAddress.NotFound`/`AuthFailure`-absence) otherwise. This forms a recon oracle: an attacker (or a former owner) can probe whether a specific previously-released IP value is now owned by someone else — information about cross-account pool state that `DescribeAddresses` (self-scoped) does not expose.

**High-level Test Scenarios.**
- **Claim:** `release-address --public-ip <ip>` for an IP not owned by the caller returns distinguishable responses based on whether another account holds it → **Mechanism:** API "AuthFailure … if already allocated to another AWS account" → **Oracle:** compare error codes/messages/latency for (a) a floating released IP vs (b) one re-allocated by a second test account → a stable differential = oracle → **Severity:** Low–Medium (recon enabler; feeds Area 2 timing).
- **Note:** Also probe whether `DryRun` short-circuits before this state check (if so, the oracle requires a real call; if not, DryRun gives a free probe). Recall **DryRun is caller-IAM-only and NOT an ownership oracle** — treat a `DryRunOperation` result as inconclusive for ownership.
- **Stop condition:** differential confirmed or refuted with 2–3 paired calls.
**Doc evidence:** API_ReleaseAddress re-release paragraph. **Severity-if-true:** Low–Medium.

### Area 5 — Tag + AllocationId continuity loss on recovery (ABAC/automation dropout) — Lens AA, Lens I
**Background.** Target page: *"You **can't recover tags** associated with an Elastic IP address."* The recovery example returns a fresh `AllocateAddressResponse` with an `allocationId`; the docs **never state the recovered EIP keeps its prior AllocationId** (overview plan open item H0-5).

**Security Concern.** A recovered EIP comes back **stripped of its tags**, and possibly with a **new AllocationId**. Any ABAC policy, SCP, or automation keyed on `aws:ResourceTag`/`ec2:ResourceTag` of that EIP (e.g. "only team-X may associate EIPs tagged `team=X`"; cost-allocation; a Deny guardrail) **silently stops applying** to the recovered resource — the guardrail evaporates exactly when the IP is reclaimed, and whoever recovers it can re-tag it as their own (`TagSpecification` on AllocateAddress gates on `aws:RequestTag`, which the recoverer controls). This mirrors the transfer-time tag-reset footgun (overview T5) but on the release→recover path.

**High-level Test Scenarios.**
- **Claim:** A recovered EIP has no tags and does not inherit prior ABAC scoping → **Mechanism:** page "can't recover tags" → **Oracle:** tag an EIP `owner=victim`, release, recover, inspect tags (empty) and test whether a `Deny unless aws:ResourceTag/owner=victim` policy now treats it as unscoped → **Severity:** Medium (High if tag-ABAC is the sole access control on EIP association).
- **Claim:** Recovery returns a different AllocationId, breaking references → **Mechanism:** docs silent on ID continuity → **Oracle:** compare `allocationId` before release vs after recover → **Severity:** Low–Medium (automation/reference breakage; resolves overview H0-5).
- **Stop condition:** tag-empty + ID-continuity observed once each.
**Doc evidence:** target page recovery rules; API_AllocateAddress response. **Severity-if-true:** Medium.

### Area 6 — ReleaseAddress parameter-model contradictions (doc-vs-model) — Lens U
**Background.** API_ReleaseAddress: `AllocationId` — prose "This parameter is required." but model "**Required: No**"; `PublicIp` — "**Deprecated**" yet documented and accepted; `NetworkBorderGroup` wrong value → `InvalidAddress.NotFound`.

**Security Concern.** Low direct impact but worth a cheap pass: (a) which identifier actually governs a release when both/neither are supplied, and (b) does a release that supplies only `NetworkBorderGroup` (no AllocationId/PublicIp) resolve to *something* (an arbitrary address in that NBG?) — if the model truly makes both optional, the resolution rule is unspecified and could mis-target.

**High-level Test Scenarios.**
- **Claim:** A release with neither `AllocationId` nor `PublicIp` is accepted at the model layer and mis-resolves → **Oracle:** `--dry-run` ReleaseAddress with only `--network-border-group` → `MissingParameter` (safe/fail-closed) vs `DryRunOperation` (concerning) → **Severity:** Low (Informational unless it resolves to a real foreign address).
- **Stop condition:** one `--dry-run`.
**Doc evidence:** API_ReleaseAddress Request Parameters. **Severity-if-true:** Informational–Low.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| IAM Deny on recovering/allocating a specific IP is inert | `AllocateAddress` key-set | "scope EIP actions with condition keys" — but no `ec2:PublicIpAddress`/`ec2:AllocationId` key exists on AllocateAddress (L12467) |
| Cross-account recovery of a released IP wins the race | AWS regional pool + `Address` param | "cannot recover after allocated to another AWS account" (a race + server check, no IAM/cooldown on this page) |
| Default-VPC release tears off a live EIP | `ReleaseAddress` auto-disassociate | UserGuide "must not be currently associated" (enforced only in nondefault VPC) |
| Re-release error reveals cross-account ownership | `ReleaseAddress` error path | `AuthFailure` only "if already allocated to another AWS account" |
| ABAC guardrail evaporates on recover | tag/AllocationId continuity | "can't recover tags"; ID continuity unspecified |
| Legacy `--public-ip` release bypasses a condition keyed on AllocationId | deprecated `PublicIp` param | both keys listed, parity unverified |

---

## 7. Out-of-Scope Risk Categories
- **The AWS IPv4 pool / fleet internals** — reaching pool-internal state, an AWS-owned account, or fleet credentials is a **hard stop** → disclosure, not continued testing.
- **General released-EIP squatting from the shared Amazon pool, EIP transfer hijack, reverse-DNS reputation, IPAM/sequential land-grab, unscopable Describe oracles, NetworkBorderGroup zero-key, 7-day/7-hour transfer contradiction** — owned by `elastic-ip-addresses-eip-attack-research-plan.md` and `working-with-eips-attack-research-plan.md`; do not re-file here.
- **Customer-authored** least-privilege footguns (a customer writing an over-broad ReleaseAddress grant) — out of scope *as a bug*; in scope only as the *mechanism* demonstrating Area 3's cross-team DoS.
- **BYOIP / CoIP pool ownership and crypto proofing** → `ec2-byoip` plan family.
- **EIP quota exhaustion as the recovery blocker** ("exceeding your Elastic IP address limit") → `fleet-quotas` / EIP-quota surface, not re-derived here.
- Single-account self-inflicted release of one's own unused EIP (no cross-boundary effect).

## 8. Null hypotheses / doc gaps
- **Lens G/K/F/Q/W/BB/CC/DD/FF (SSRF, prompt-injection, translation-layer, upload, attestation, canonicalization, upstream-context, cache, JWT):** N/A for this surface — the release/recover page and both API refs expose only two synchronous control-plane mutators over an IP identifier; no server-side fetch, no parser, no upload, no token/cache/authorizer layer. Pages checked: target UserGuide page, `API_ReleaseAddress.md`, `API_AllocateAddress.md`, `list_ec2.html` rows L12467/L30293.
- **Lens B/C (PassRole/vending):** N/A — neither action accepts a role ARN or vends credentials. (Note the adjacent `ReplaceIamInstanceProfileAssociation` row carries `iam:PassRole` but is a different action, not in scope here.)
- **Doc-gaps to confirm surface first (mark leads accordingly):**
  - Whether a **cooldown/quarantine** returns a released IP to its former owner before the pool (this page is silent; measure in Area 2).
  - Whether recovery returns the **same AllocationId** (overview H0-5 still open; Area 5).
  - Whether **default VPCs** exist in the test account (Area 3 precondition).
  - Whether the deprecated **`PublicIp`** release path evaluates the same condition keys as `AllocationId` (Area 1 parity).
  - `API_ReleaseAddress.md` / `API_AllocateAddress.md` were read **online only** — not in the local mirror; re-confirm offline if sync integrity matters.

---
*Generated by the security-questionbuilder skill against documentation only. No live AWS account was contacted. Nothing here asserts a bug exists — each lead states a boundary that might not hold and the exact observation that settles it.*
