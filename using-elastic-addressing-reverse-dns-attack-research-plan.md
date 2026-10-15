# EC2 Elastic IP Reverse DNS (PTR for email) — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/Using_Elastic_Addressing_Reverse_DNS.html` (target, read in full; online `.md` twin **byte-identical** to the offline mirror, 2026-10-15) + `API_ModifyAddressAttribute.md` / `API_ResetAddressAttribute.md` / `API_DescribeAddressesAttribute.md` / `API_AddressAttribute.md` / `API_PtrUpdateStatus.md` + `service-authorization/latest/reference/list_ec2.md` (10190-line IAM reference, read by targeted offline grep). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

This is a **page-level deep-dive child of the `ec2-networking` hub** and a **procedural child/complement of `elastic-ip-addresses-eip-attack-research-plan.md`** (the EIP overview plan). The overview plan already owns reverse-DNS as its two summary leads **D1** (ModifyAddressAttribute.DomainName free-text, undocumented ownership gate, async PENDING → PTR reputation-laundering) and **D2** (PTR locks EIP against release AND transfer-accept; Support-set = no self-service unlock). **This plan OWNS the reverse-DNS surface in full and deepens D1/D2 with the authoritative IAM condition-key audit the overview plan did not perform.** It cross-references, and does not restate, the overview plan's transfer-hijack / released-EIP-squatting / forced-reassociation / NetworkBorderGroup / 7-day-vs-7-hour leads, and the `working-with-eips` / `transfer-EIPs-intro-ec2` siblings.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The cheapest first oracle for every IAM lead here is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (no resource touched). Escalate to a live scoped call only with a canary EIP you own.
- **`DryRun` on `ModifyAddressAttribute` is caller-IAM-only** (evaluated before resource resolution and before any forward-DNS/ownership check) — it is NOT an ownership or forward-DNS-enforcement oracle. The real enforcement surfaces only asynchronously in `PtrRecordUpdate.reason` / `.status`.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the reverse-DNS provisioning backend, the AWS resolver fleet, the Support-lock subsystem), stop, preserve evidence, flag for AWS-Security disclosure. Reverse-DNS activation is performed by an AWS-managed backend you must never pivot into.

---

## 1. Pentest Objectives (boundary-breach goals)
1. Set a PTR (reverse-DNS) record whose **domain value** an admin's IAM policy was supposed to forbid — i.e. prove the PTR target string is unscopable (Area 1).
2. Publish a PTR for an EIP that points at a domain the caller does **not** own / whose forward A record does **not** resolve to the caller's EIP — i.e. prove the documented forward-DNS prerequisite fails open (Area 1).
3. **Lock** another principal's / another team's EIP against release (and transfer-accept) using only `ec2:ModifyAddressAttribute`, with no `ec2:ReleaseAddress` and no cooperation from the EIP owner (Area 2).
4. **Tear down** a victim's legitimately-configured PTR (degrading their outbound email reputation) and/or **unlock** a victim EIP for release, using `ec2:ResetAddressAttribute` (Area 3).
5. Enumerate every EIP's PTR / pending-PTR state account-wide with an unscopable `DescribeAddressesAttribute` read oracle (Area 4).
6. Characterize the async enforcement/observability gap: no synchronous validation error, `reason`-only failure channel, no EventBridge, GovCloud asymmetry (Area 5).

---

## 2. Components, Assets, and Design

**What the page does.** Lets an EIP owner set / clear a **reverse-DNS (PTR) record** for an Elastic IP, so that mail receivers performing a reverse lookup on the sending IP see a chosen hostname (an anti-spam reputation signal). Three control-plane actions:

| Action | CLI | Role here |
|---|---|---|
| `ModifyAddressAttribute` | `aws ec2 modify-address-attribute --allocation-id … --domain-name …` | **Set** the PTR domain for an EIP |
| `ResetAddressAttribute` | `aws ec2 reset-address-attribute --allocation-id … --attribute domain-name` | **Clear** the PTR domain (reset to default) |
| `DescribeAddressesAttribute` | `aws ec2 describe-addresses-attribute --attribute domain-name` | **Read** PTR + pending-update state |

**Assets:** the PTR record (a reputation/identity artifact for outbound email); the EIP itself (whose *releasability* becomes conditional on PTR state); the account's email-sending topology (which EIPs are email senders, inferable from PTR presence).

**Design / pipeline (inferred from the API shape):**
```
caller --SigV4--> ec2:ModifyAddressAttribute (sync IAM authz on elastic-ip*; returns 200 + PtrRecordUpdate.Status=PENDING)
                        |
                        v  (async, out of band)
            AWS reverse-DNS provisioning backend
                        |-- resolves the forward A record (DNS lookup of caller-supplied DomainName)  [? ownership check ?]
                        |-- publishes PTR in the in-addr.arpa zone AWS controls for the IP block
                        |-- sets a release/transfer LOCK on the EIP while a PTR exists
                        v
            PtrRecordUpdate.Status -> {PENDING -> ... }, PtrRecordUpdate.reason populated on failure
```
- **Identity model:** direct SigV4 IAM; no PassRole, no service-linked role, no cross-account handshake on this surface (contrast the EIP *transfer* surface owned by the overview/transfer siblings).
- **Resource identifier:** `elastic-ip` ARN / `AllocationId` (`eipalloc-<17 hex>`, high-entropy, not fabricable) / `PublicIp`. The PTR domain value is an **opaque free-text String** with no documented pattern, length cap, or charset restriction.
- **Trust zones crossed:** (a) caller account ↔ AWS reverse-DNS backend (service plane — hard stop); (b) caller ↔ the global DNS reputation namespace (the PTR is published into AWS-controlled reverse zones and consumed by third-party mail receivers — an *outbound trust* boundary); (c) intra-account cross-team (one principal's attribute-write affecting another team's EIP releasability).

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller holding scoped `ModifyAddressAttribute` | The **PTR domain value** published for an EIP | free-text `DomainName` param, no value-scoping condition key | A PTR is published whose domain string an admin policy intended to forbid (Area 1). |
| Caller | Third-party mail-receiver reputation (global reverse-DNS trust) | PTR published into AWS reverse zone, consumed by anti-spam | A PTR points at a domain the caller doesn't control / whose forward A doesn't resolve to the caller's EIP, yet activates (Area 1 fail-open). |
| Intra-account team B (`ModifyAddressAttribute` only) | Team A's EIP *releasability* | PTR-sets-lock, lock survives independent of `ReleaseAddress` IAM | Team A can no longer release/transfer their EIP; only `ResetAddressAttribute` clears it (Area 2). |
| Intra-account team B (`ResetAddressAttribute`) | Team A's email reputation / EIP lock state | reset clears PTR (sabotage) and unlocks (enables release) | Team A's PTR disappears → mail flagged spam; or EIP becomes releasable (Area 3). |
| Any caller with `DescribeAddressesAttribute` | Every EIP's PTR / pending state account-wide | blank resource type, `ec2:Region`-only | Reading PTR state of EIPs the caller has no tag/ARN grant on (Area 4). |
| Caller-supplied `DomainName` | AWS resolver fleet (forward-A verification) | async server-side DNS resolution of attacker hostname | AWS resolver queries attacker's authoritative NS (blind DNS-interaction oracle) (Area 5, minor). |
| **Any caller surface** | **AWS reverse-DNS / Support-lock backend** | async provisioning | **Any identity/credential/ARN of AWS's own fleet = HARD STOP.** |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Ext-facing | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `ModifyAddressAttribute` | SigV4 | **Yes** | Yes | Set PTR domain for an EIP | holder of `ec2:ModifyAddressAttribute` on the `elastic-ip*` | `DomainName` free-text, Required:No; **Errors block empty** (only CommonErrors) |
| `ResetAddressAttribute` | SigV4 | **Yes** | Yes | Clear PTR domain | holder of `ec2:ResetAddressAttribute` on the `elastic-ip*` | `--attribute domain-name`; also *unlocks* the EIP |
| `DescribeAddressesAttribute` | SigV4 | No | Yes | Read PTR + `PtrRecordUpdate` | holder of `ec2:DescribeAddressesAttribute` | **blank resource type + `ec2:Region` only = unscopable** |
| `ReleaseAddress` (cross-ref) | SigV4 | Yes | Yes | Release EIP | holder of `ec2:ReleaseAddress` | **blocked by the PTR lock regardless of this grant** |

Response objects: `AddressAttribute{ allocationId, ptrRecord, ptrRecordUpdate, publicIp }`; `PtrUpdateStatus{ reason, status, value }`. No `[NEW]` marker; no console-hidden parameter beyond the three above (`DomainName` is the only mutable attribute).

**IAM condition-key audit (authoritative, from `list_ec2.md`):**

| Action | Resource type | Condition keys | Line |
|---|---|---|---|
| `ModifyAddressAttribute` | `elastic-ip*` (**required**) | `aws:ResourceTag/${TagKey}`, `ec2:AllocationId`, `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:Domain`, `ec2:PublicIpAddress`, `ec2:Region`, `ec2:ResourceTag/${TagKey}` | 8717 |
| `ResetAddressAttribute` | `elastic-ip*` (**required**) | *(identical set to above)* | 9489 |
| `DescribeAddressesAttribute` | *(none)* | **`ec2:Region` only** | 6582 |
| `ReleaseAddress` | `elastic-ip` (not required) | `aws:ResourceTag`, `ec2:AllocationId`, `ec2:Domain`, `ec2:PublicIpAddress`, `ec2:Region`, `ec2:ResourceTag` | 9383 |

Key definitions (verified line 10049/10072/10050): `ec2:AllocationId` = "the allocation ID of the Elastic IP address" (**which EIP**); `ec2:Domain` = "the **domain** of the Elastic IP address" (= `standard`/`vpc` classifier, **NOT the PTR domain name**); `ec2:PublicIpAddress` = the EIP's own IP; `ec2:Attribute`/`ec2:Attribute/${AttributeName}` = "an attribute of a resource" (here the attribute *name* `domain-name`, not its value). **Full-corpus grep: `ec2:DomainName` / `ec2:PtrRecord` / `ec2:ReverseDns` = 0 hits.**

---

## 5. Recommended Areas of Focus

### Area 1 — PTR domain *value* is IAM-unscopable → reverse-DNS reputation spoofing / FCrDNS fail-open  (HEADLINE — Lens S / U, with Lens P "skip-the-gate" sub-test)
**Background.** The page's purpose is anti-spam reputation: "assign static reverse DNS records … to reduce the chance that your email … will be flagged as spam." The only documented safety precondition is the **forward-DNS requirement**: *"Before you create a reverse DNS record, you must set a corresponding forward DNS record (record type A) that resolves to an Elastic IP address in your account."*

**Security Concern.**
- **No condition key scopes the DomainName value.** `ModifyAddressAttribute` carries `ec2:AllocationId`/`ec2:Domain`/`ec2:PublicIpAddress` (which pin **which EIP**) but there is **no `ec2:DomainName`/`ec2:PtrRecord`/`ec2:ReverseDns` key anywhere in `list_ec2.md`** (0 hits), and `DomainName` is a free-text `String`, `Required: No`, with an **empty Errors block** in `API_ModifyAddressAttribute.md`. ⇒ An admin **cannot** author an identity/SCP policy that restricts *which* domain a principal publishes as a PTR; any principal who may modify an EIP's attribute may set its PTR to **any domain string**.
- **Is the forward-DNS prerequisite enforced, or advisory?** The empty Errors block means there is no *synchronous* "forward record missing / not pointing at your EIP" rejection; validation (if any) is **asynchronous** and surfaces only in `PtrRecordUpdate.reason` with `Status: PENDING` → `?`. If it fails **open** (PTR activates regardless of the forward record), the sole anti-spoof control is absent.
- **Even when enforced, FCrDNS proves pointing, not ownership.** The requirement is only that a forward A record *resolves to an EIP in your account* — it never verifies the caller controls/owns the **domain's zone**. A caller who controls DNS for a **look-alike** domain (`mai1-bankofexample.com`) can point its A at their own EIP and publish a matching PTR → a forward-confirmed reverse-DNS pair for a deceptive hostname, exactly the trust signal receivers key on.

**High-level Test Scenarios (falsifiable claims).**
- **Claim:** a role scoped by `ec2:Attribute`/tag to "manage EIP attributes" can set the PTR to an arbitrary unrelated domain → **Oracle:** `SimulateCustomPolicy` shows no policy construct can deny by domain value; live `modify-address-attribute --domain-name attacker-chosen.example` on a canary EIP returns 200 + `PENDING`. **Severity:** Low–Med (policy-expressiveness gap; AWS-owned if it blocks a legitimate guardrail).
- **Claim (skip-the-gate / fail-open):** publish a PTR whose forward A record does **not** resolve to the caller's EIP (or set no forward record at all) → does `PtrRecordUpdate` reach an active state anyway, or does `reason` report failure? **Oracle:** canary EIP, set PTR with a deliberately mismatched forward record; poll `DescribeAddressesAttribute` for terminal `status`/`reason`. Active = fail-open FCrDNS bypass. **Severity:** Med (reverse-DNS spoofing / spam-filter trust abuse).
- **Claim (laundering, holds even if gate enforced):** a look-alike domain whose A record the attacker legitimately points at their own EIP yields a forward-confirmed PTR AWS presents as valid → **Oracle:** receiver-side reverse lookup returns the deceptive hostname; demonstrates the gate authenticates *pointing* not *authority*. **Severity:** Med (phishing/deliverability reputation abuse; impact lands on third-party receivers, not AWS tenants).

**Doc evidence:** target "Considerations" bullet 1; `API_ModifyAddressAttribute.md` (DomainName String/Required:No, empty Errors); `list_ec2.md` 8717 + 0-hit grep. **Severity-if-true:** Low–Medium.

---

### Area 2 — PTR-record EIP lock = release/transfer denial + cost-accrual griefing  (Lens AA / L / U)
**Background.** *"If a reverse DNS record is associated with an Elastic IP address, the Elastic IP address is **locked to your account and cannot be released** from your account until the record is removed."* And the stickier variant: *"If you contacted Support to set up reverse DNS … you can remove the reverse DNS, but you **can't release the Elastic IP address because it is locked by Support** … contact AWS Support to unlock."*

**Security Concern.**
- The lock is **service-enforced on the EIP**, independent of `ec2:ReleaseAddress` IAM. `ReleaseAddress` (`list_ec2` 9383) is a distinct action with its own keys, but the PTR lock pre-empts it with the error *"The address cannot be released because it is locked to your account."* ⇒ A principal holding **only `ec2:ModifyAddressAttribute`** (scoped to a victim EIP by tag/`ec2:AllocationId`) — and **no `ReleaseAddress`** — can **set a PTR and thereby prevent the EIP owner from releasing or transferring the EIP**, a one-way action the owner cannot reverse without the mirror action `ResetAddressAttribute`.
- **Revocation incompleteness (Lens AA):** the lock is cleared only by the *opposite* action (`ResetAddressAttribute`); if the attacker holds `Modify` but the owner lacks `Reset`, the lock is durable. The **Support-lock** escalation removes self-service entirely: a Support-set PTR locks the EIP such that even clearing the record does not permit release — unlock is a human Support case.
- **Cost / availability (Lens L):** a locked EIP cannot be released to stop charges; combined with Area 3 it is a cross-team denial primitive. Cross-ref overview **D2**: the lock also blocks **transfer-accept**, so a locked EIP cannot be moved out of the account either (persistence / stranding).

**High-level Test Scenarios.**
- **Claim:** `ModifyAddressAttribute`-only principal locks an EIP against `ReleaseAddress` held by another principal → **Oracle:** scoped role sets PTR on canary EIP; a second role with `ReleaseAddress` gets *"locked to your account"* on release. **Severity:** Low–Med intra-account cross-team DoS/cost.
- **Claim:** removing the PTR via `ResetAddressAttribute` restores releasability, but a Support-set PTR does not → **Oracle:** doc-confirmed for the Support path; live-confirm the self-service path (reset → release succeeds). **Severity:** Low (griefing); Med if chained with transfer-lock to strand an EIP.

**Doc evidence:** target "Considerations" bullets 2–3; "Remove a reverse DNS record" error block; `list_ec2.md` 9383 (ReleaseAddress is a separate action). **Severity-if-true:** Low–Medium (intra-account; availability/cost + persistence).

---

### Area 3 — `ResetAddressAttribute` as a reverse-DNS teardown / email-reputation sabotage twin  (Lens X / AA, with Lens S case-sensitivity sub-test)
**Background.** `ResetAddressAttribute --attribute domain-name` clears the PTR and (per Area 2) unlocks the EIP. It carries the **same required resource type and condition-key set** as `ModifyAddressAttribute` (`list_ec2` 9489) — a symmetric write pair.

**Security Concern.**
- **Sabotage twin:** a principal with `ResetAddressAttribute` scoped to a victim EIP can **delete a legitimately configured PTR**, so the victim's outbound mail loses its reverse-DNS and gets flagged as spam — precisely the harm the page exists to prevent. Integrity/availability attack on email **deliverability**, achievable without touching the mail system itself.
- **Unlock-then-release chain (Lens X/AA):** Reset both removes the PTR **and** unlocks the EIP. A griefer with `Reset` + `ReleaseAddress` can unlock a victim's intentionally PTR-locked EIP and release it → the EIP returns to the shared pool and is reclaimable by another account (chains into the overview plan's **L1** released-EIP squatting / dangling-trust takeover). This defeats the "lock" the owner relied on for retention.
- **Lens S case-sensitivity fail-open:** both actions expose `ec2:Attribute` / `ec2:Attribute/${AttributeName}`. The attribute name is the lowercase enum `domain-name`. A Deny written `"ec2:Attribute":"domain-name"` is a known fail-open class if the request populates a differently-cased / differently-spelled attribute token — and an `ec2:Attribute`-based Deny on `Modify` may not symmetrically cover `Reset` (or vice-versa). **Oracle:** `SimulateCustomPolicy` with casing variants; confirm whether a Deny intended to protect the PTR attribute is inert.

**High-level Test Scenarios.**
- **Claim:** `Reset`-scoped principal strips a victim EIP's PTR → **Oracle:** canary EIP with an active PTR, scoped role runs `reset-address-attribute`; `DescribeAddressesAttribute` shows PTR gone. **Severity:** Med (email-reputation sabotage).
- **Claim:** an `ec2:Attribute="domain-name"` Deny fails open under casing / does not cover both twins → **Oracle:** `SimulateCustomPolicy`. **Severity:** Low–Med (guardrail-inert).

**Doc evidence:** "Remove a reverse DNS record" section; `list_ec2.md` 9489; `ec2:Attribute` def 10050. **Severity-if-true:** Low–Medium (chains to High only via the released-EIP-squatting dangling-trust end-state owned by the overview plan).

---

### Area 4 — `DescribeAddressesAttribute` unscopable account-wide PTR read oracle  (Lens A / O)
**Background.** The read side of the PTR surface.

**Security Concern.** `DescribeAddressesAttribute` has a **blank resource-type cell and only `ec2:Region`** (`list_ec2` 6582, Access level **List**) — it **cannot be scoped by tag, ARN, or AllocationId**. ⇒ Any principal granted `ec2:DescribeAddressesAttribute` reads the `PtrRecord` + `PtrRecordUpdate` (value/status/**reason**) of **every EIP in the account/Region**, including EIPs they have no `Modify`/tag grant on. This is the same inert-ABAC shape as the corpus's other Describe oracles (`DescribeAddresses`, `DescribeInstances`, `DescribeSpotFleetRequests`, `DescribeCapacityReservations`). Recon value: PTR presence fingerprints which EIPs are **email senders** (the account's mail topology), and `reason` on pending/failed updates can leak internal domain names / provisioning errors. Confirms overview-plan **O2**.

**High-level Test Scenarios.**
- **Claim:** no policy construct restricts `DescribeAddressesAttribute` to a tagged subset of EIPs → **Oracle:** `SimulateCustomPolicy` shows resource/tag conditions are not evaluable (blank resource type); a scoped read returns foreign-team EIP PTR state. **Severity:** Low (intra-account read oracle / email-infra info disclosure).

**Doc evidence:** `list_ec2.md` 6582; `API_AddressAttribute.md` + `API_PtrUpdateStatus.md` (ptrRecord/ptrRecordUpdate/reason fields). **Severity-if-true:** Low.

---

### Area 5 — Async enforcement opacity, resolver-side DNS interaction, observability & GovCloud asymmetry  (Lens U / O / G-minor)
**Background.** The whole surface is **asynchronous** (`Status: PENDING`, failures only in `reason`), control-plane-only, and region/partition-asymmetric.

**Security Concern.**
- **Lens U (guarantee vs enforcement):** the forward-DNS "must set … before" guarantee has **no synchronous enforcement mechanism** (empty Errors). Whether it is enforced at all, and whether it fails open, is the pivotal Area-1 question — settle it before investing in the laundering branch.
- **Lens O (defender blind spot):** `Modify`/`Reset` are CloudTrail **management events** (Access level Write) logged by default — so the *setup* of a PTR lock or a reputation teardown is auditable — **but there is no documented EventBridge event** for PTR state change (confirm against the EC2 native event catalog). A defender has no push signal "your EIP's reverse DNS changed" or "your EIP was locked"; detection is poll-only via the unscopable `DescribeAddressesAttribute` (Area 4). The async `reason` channel is the only failure signal and is not an alarm source.
- **Lens G (minor):** the forward-A verification requires AWS infra to perform a **server-side DNS resolution of the caller-supplied `DomainName`**. This is a blind **DNS-interaction oracle** (attacker sets `DomainName` to a hostname on their own authoritative NS / an interactsh domain and watches for the AWS resolver query) — confirms the verification path exists and when it runs, and could fingerprint the resolver source. Not classic HTTP SSRF (no fetched URL), low value; note as corroboration for the Area-1 enforcement timing.
- **Lens U/X (GovCloud asymmetry):** *"[AWS GovCloud (US) Region] You can't create a reverse DNS record. AWS must assign the static reverse DNS records for you. Open a support case…"* ⇒ a **different enforcement/provisioning path** in GovCloud (human Support, AWS-assigned). Parity question: is the PTR lock / unlock behavior and the forward-DNS check the same across partitions, and does the Support-assignment path introduce the Support-lock stickiness (Area 2) by default?

**High-level Test Scenarios.**
- **Claim:** no synchronous validation error exists for a bad forward record → **Oracle:** `API_ModifyAddressAttribute.md` Errors block is empty; live call returns 200+PENDING on a mismatched domain. **Severity:** Informational (feeds Area 1).
- **Claim:** no EventBridge event fires on PTR change/lock → **Oracle:** diff the EC2 event catalog (`automating_with_eventbridge.md`). **Severity:** Low (detection gap, enabler).
- **Claim:** AWS resolver queries an attacker NS during forward verification → **Oracle:** interactsh-style canary domain as `DomainName`. **Severity:** Informational.

**Doc evidence:** target "Considerations" bullets 1 & 4; `API_PtrUpdateStatus.md` (reason/status); `API_ModifyAddressAttribute.md` (empty Errors). **Severity-if-true:** Informational–Low.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Publish PTR with an admin-forbidden domain value | `ModifyAddressAttribute` | *(none — no `ec2:DomainName` key; `ec2:Attribute` keys on attribute name only)* |
| PTR for a domain not owned / forward-A mismatch activates | reverse-DNS backend | "must set a corresponding forward DNS record … that resolves to an EIP in your account" (enforcement unverified) |
| Lock a foreign EIP against release with `Modify` only | EIP lock | "locked to your account … until the record is removed"; `ReleaseAddress` is a separate action |
| Strip a victim's PTR → email flagged spam | `ResetAddressAttribute` | PTR exists specifically "to reduce the chance … flagged as spam" |
| Unlock + release a victim's PTR-locked EIP | `ResetAddressAttribute` + `ReleaseAddress` | the lock is the only retention guarantee; reset removes it |
| `ec2:Attribute="domain-name"` Deny inert (casing / twin-coverage) | IAM policy eval | `ec2:Attribute` / `ec2:Attribute/${AttributeName}` |
| Account-wide PTR / mail-topology enumeration | `DescribeAddressesAttribute` | *(none — blank resource type, `ec2:Region` only)* |
| No push alert on PTR change / lock | EventBridge/CloudTrail | management events logged (setup auditable); no EventBridge event |

---

## 7. Out-of-Scope Risk Categories
- The **AWS reverse-DNS provisioning backend, the AWS resolver fleet, the in-addr.arpa zones AWS controls, and the Support-lock subsystem** — service plane. Any credential/ARN/identity belonging to them is a HARD STOP + disclosure.
- **EIP cross-account transfer hijack, released-EIP squatting, forced reassociation, NetworkBorderGroup, the 7-day-vs-7-hour contradiction** — owned by `elastic-ip-addresses-eip-attack-research-plan.md` (D-leads, T-leads, L1, S1, O1/O2, B1, X1) and `transfer-EIPs-intro-ec2` / `working-with-eips`. This plan only *chains into* L1 (release-after-unlock) and D2 (transfer-lock), it does not re-derive them.
- **Third-party mail-receiver / anti-spam behavior** — AWS does not control how receivers weight a PTR; the reputation-laundering impact lands on receivers, not on AWS tenants (keeps Area 1 at Medium, not Critical).
- **Customer-authored IAM footguns** — out of scope; but note there is *no AWS-managed policy / sample policy / CFN / SLR* shipped on this page (nothing to audit under Lens R), so there is no AWS-authored artifact defect here.
- Single-tenant self-DoS (locking your own EIP) and product gaps.

---

## 8. Null hypotheses / lenses that did not fire (pages checked: the target page in full, `API_ModifyAddressAttribute/ResetAddressAttribute/DescribeAddressesAttribute/AddressAttribute/PtrUpdateStatus`, `list_ec2.md` rows 3642/4278/4364/6582/8717/9383/9489 + condition-key defs)
- **Lens B/C (PassRole / credential vending):** N/A — no role ARN, no `iam:PassRole`, no STS/session surface on these three actions (verified in the detail rows; contrast `ReplaceIamInstanceProfileAssociation` which does carry PassRole).
- **Lens G (SSRF):** no HTTP-fetched URL field; `DomainName` drives a DNS resolution, captured as a *minor* interaction oracle in Area 5, not classic SSRF.
- **Lens Q (upload):** N/A — no blob/file input.
- **Lens F (translation/injection):** N/A — no wire-protocol/query translation layer; `DomainName` is stored as a DNS record value (any injection risk is downstream DNS-zone handling in the AWS backend = out of scope / hard stop).
- **Lens K (prompt injection):** N/A — no LLM/agent.
- **Lens H / W (KMS / attestation):** N/A — no encryption key or attestation gate on this surface.
- **Lens FF / DD / CC / BB (token / cache / upstream-context / multi-parser):** N/A — single SigV4 action, no authorizer/cache/JWT/multi-hop parser in path.
- **Lens Y (transport/sig):** N/A beyond generic EC2 endpoint posture (not specific to this page).
- **Lens R / S (AWS-authored artifact):** no managed/sample/CFN/SLR policy printed on this page; **Lens S fires only** as the condition-key-semantics analysis in Areas 1 & 3 (no value key; `ec2:Attribute` casing).
- **Lens A cross-account IDOR:** partial-null — `AllocationId` is `eipalloc-<17 hex>` (high entropy, not fabricable) and `elastic-ip*` is a *required* resource type on both write actions, so blind cross-**account** PTR mutation is not a direct shape; the real cross-boundary exposure is **intra-account cross-team** (Areas 2/3) + the **unscopable read oracle** (Area 4). No cross-account write path on this surface (transfer is the cross-account path and is owned elsewhere).

**Open doc-gaps to settle first (ordered):** (1) Is the forward-DNS prerequisite enforced, and does it fail open? (Area 1 — gates everything.) (2) Does `ResetAddressAttribute` fully restore releasability on the self-service path (vs the Support-lock path)? (Area 2/3.) (3) Is there any EventBridge event for PTR state change? (Area 5.) (4) GovCloud/partition parity of the lock + forward check (Area 5).

Cross-ref: `elastic-ip-addresses-eip-attack-research-plan.md` (parent/overview — D1/D2/L1/O2), `working-with-eips-attack-research-plan.md`, `transfer-EIPs-intro-ec2-attack-research-plan.md`, `ec2-networking-attack-research-plan.md` (hub). See the IAM reference slug note in memory ([[reference-aws-iam-service-auth-ref-url]]).
