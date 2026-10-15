# EC2 Bring Your Own IP (BYOIP) — Attack / Research Plan

> **Skill:** `security-questionbuilder` (boundary-first threat modeling).
> **Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html
> **Scope of this plan:** the EC2 BYOIP feature family — provision / advertise / withdraw / deprovision of
> customer-owned publicly-routable IPv4 (/24) and IPv6 (/48 public, /60 or /56 non-public) ranges, the
> cryptographic ownership-proofing chain (X.509 + RDAP + ROA/RPKI + signed authorization message), BYOASN,
> public-IPv4 / IPv6 pools, and their IAM authorization surface. **Documentation-only** analysis; no live
> system was touched. Online `.html` twins were drift-checked against the offline mirror (result in §8).
>
> **Position in the plan family:** this is a **net-new page-level deep-dive child of the `ec2-networking`
> hub** (`ec2-networking-attack-research-plan.md`), whose summary lead #4 names BYOIP at one line. This plan
> *develops* that lead and **owns** the full BYOIP surface. See §7 for exactly what it owns vs. defers to the
> hub and to the EIP-transfer / address siblings.

---

## 0. Sources read (provenance)

Offline mirror under `/work/aws-docs/docs/`:

- UserGuide: `ec2-byoip.md` (target), `prepare-for-byoip.md`, `byoip-onboard.md`, `byoip-working-with.md`
- APIReference: `API_ProvisionByoipCidr.md`, `API_AdvertiseByoipCidr.md`, `API_WithdrawByoipCidr.md`,
  `API_DeprovisionByoipCidr.md`, `API_MoveByoipCidrToIpam.md`, `API_ByoipCidr.md`, `API_DescribeByoipCidrs.md`,
  `API_CidrAuthorizationContext.md`, `API_AsnAuthorizationContext.md`, `API_ProvisionIpamByoasn.md`,
  `API_AssociateIpamByoasn.md`, `API_Byoasn.md`
- IAM ground truth: `docs/service-authorization/latest/reference/list_ec2.md` (audited action-by-action; line
  numbers cited in §3/§6)

Prior raw research reused: `/work/aws-docs/.cache/plans/ec2-net-frag1-ip-eip-byoip.md` (IP/EIP/BYOIP cluster
fragment — its BYOIP leads are promoted and extended here).

**Drift check:** online `ec2-byoip.html`, `prepare-for-byoip.html`, `byoip-onboard.html` fetched and compared
sentence-for-sentence to the offline `.md`. **No material drift** (details §8).

---

## 1. Components, Assets, and Design

BYOIP has **no shared multi-tenant service fleet or data-plane translation layer** — unlike DocumentDB /
CloudShell, there is no customer-reachable proxy process to pivot from. The security-interesting machinery is
instead **(a) an out-of-band cryptographic ownership-proofing chain that terminates at third-party registries
(RIR / RPKI / IRR), not at AWS**, and **(b) an IAM authorization surface that is unusually coarse**. The
"assets" are therefore *control-plane authority over a globally-routable prefix* and *the trust artifacts that
gate it*.

### Customer-facing interface
- SigV4 EC2 control-plane APIs (SDK/CLI): `provision-byoip-cidr`, `advertise-byoip-cidr`,
  `withdraw-byoip-cidr`, `deprovision-byoip-cidr`, `move-byoip-cidr-to-ipam`, `describe-byoip-cidrs`, plus
  pool-consumption APIs (`allocate-address`, `describe-public-ipv4-pools`, `create-vpc`,
  `associate-vpc-cidr-block`, `describe-ipv6-pools`, `get-associated-ipv6-pool-cidrs`) and the IPAM-gated
  BYOASN APIs (`provision-ipam-byoasn`, `associate-ipam-byoasn`, …).
- No console-only hidden endpoint discovered; the "hidden knob" here is a **schema-level** one (§3): the
  authorization context is `Required: No` on `ProvisionByoipCidr`.

### Processes / hosts behind it
- An AWS BGP advertisement subsystem (announces the prefix from Amazon ASNs **16509 / 14618**; GovCloud **8987**;
  European Sovereign Cloud **16509 / 214101**).
- A validation subsystem that performs an out-of-band **RDAP `whois` lookup** (ARIN / RIPE / APNIC) to fetch
  the customer's uploaded X.509 cert, and an **RPKI validity check** (RIPEstat `stat.ripe.net/data/rpki-validation`)
  against the ROA. This subsystem **presents a customer-signed message to the RIR; the RIR authenticates the
  signature against the RDAP cert and checks the ROA** (byoip-onboard.md L20).
- An **IRR/RADb auto-writer** that creates route objects on the customer's behalf (ec2-byoip.md L51).

### Accounts / resources / identifiers
- **BYOIP CIDR** — has **no IAM resource type / ARN at all** for the four lifecycle actions (see §3). Named only
  as a request-body string (`--cidr`).
- **Public IPv4 pool** `ipv4pool-ec2-{hex}` and **IPv6 pool** `ipv6pool-ec2-{…}` — *do* have resource ARNs
  (`ipv4pool-ec2/${Ipv4PoolEc2Id}`, `ipv6pool-ec2/${Ipv6PoolEc2Id}`) but **no condition key for the pool id**.
- **BYOASN** — ASN value; no `ec2:Asn` condition key anywhere.
- **CidrAuthorizationContext / AsnAuthorizationContext** — `{Message, Signature}` bearer blobs.
- Signed message format: `1|aws|{account}|{cidr}|{YYYYMMDD}|SHA256|RSAPSS`, RSA-PSS over SHA-256.

### Identity / trust anchor
- The AWS-side caller identity is ordinary SigV4 IAM. **But the ownership gate's trust anchor is control of
  the RDAP record + the RPKI ROA for the prefix — orthogonal to AWS account identity.** The X.509 keypair is
  **self-signed and ephemeral**; its only "legitimacy" is that its public cert sits in the prefix's RDAP record.

### Untrusted-data entry → transform
- Customer-supplied `Message`/`Signature` → RIR verification. Customer-supplied `--cidr`, `--network-border-group`,
  `--asn` → BGP advertisement + IRR auto-write. These are the injection/authz seams.

```
 Customer AWS account (SigV4)                         Third-party trust roots (NOT AWS)
 ┌───────────────────────────┐                        ┌───────────────────────────────┐
 │ provision/advertise/       │   Message+Signature    │  RIR RDAP record (X.509 cert)  │
 │ withdraw/deprovision       │──────presented────────▶│  RPKI ROA (authorized ASNs)    │
 │ (ec2:Region-only IAM gate) │                        │  IRR / RADb (route objects)    │
 └─────────────┬──────────────┘                        └───────────────┬───────────────┘
               │ provisioned                                            │ auth result
               ▼                                                        ▼
 ┌───────────────────────────┐                        ┌───────────────────────────────┐
 │ Public IPv4/IPv6 pool      │  allocate-address /    │  AWS BGP advertiser            │
 │ (ipv4pool-ec2 / ipv6pool)  │  create-vpc --ipv6-pool│  (ASN 16509/14618/8987/214101) │
 │  → EIP / VPC CIDR          │                        │  announces prefix to Internet  │
 └───────────────────────────┘                        └───────────────────────────────┘
```

---

## 2. Trust-boundary map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|---|
| B1 | Any IAM principal granted `ec2:ProvisionByoipCidr` (region-wide) | A *specific* BYOIP CIDR / pool / ASN | lifecycle APIs have **no resource type** — IAM cannot name a CIDR | A principal intended to manage CIDR A provisions/withdraws CIDR B in the same region = **boundary breach** (the grant was meant to be per-prefix but can't be) |
| B2 | Holder of RDAP-record write access + ROA control | AWS account that provisions the prefix | signed `Message` names `{account}`; AWS presents it to RIR | Prefix provisioned under an account whose number was **not** cross-checked against the signed `{account}` = account-binding breach |
| B3 | Anyone who captures a `Message`+`Signature` pair | Re-provision of the same CIDR (later / another region / another account) | bearer blob, signer-chosen expiry, no AWS nonce / single-use | Identical blob accepted a second time, or in a different region, = **replay breach** |
| B4 | Party with RDAP write access *after* legitimate provisioning | The prefix's ongoing advertisement | cert left in RDAP (removal is advisory); no re-validation cadence | Advertisement continues after the ROA/cert is revoked/expired, OR a newly-inserted RDAP cert mints a valid message = persistence/takeover breach |
| B5 | Non-public IPv6 (/60) provisioner | The ownership gate | ROA **not required** on this path | A prefix provisionable with RDAP-cert signature **only** (no RPKI anchor) = single-anchor (weaker) gate |
| B6 | Caller holding only `ec2:AllocateAddress` on a pool | A *specific* IP within the pool | `AllocateAddress` has **no `ec2:PublicIpAddress` key** | Caller allocates a chosen/high-value address from the pool that IAM should have been able to deny = address-squatting within pool |
| B7 | One AWS account / team sharing an account | Another's BYOIP capacity | 5 ranges/region quota, **not** Service-Quotas adjustable | Exhausting the 5-range quota to deny a sibling team/account = DoS boundary |
| B8 | Account A | Cross-account use of A's range | RAM sharing **blocked unless** IPAM+Organizations | A range reachable/usable cross-account without the IPAM+Orgs path = sharing-isolation breach |
| B9 | BYOASN holder | ASN↔CIDR origin binding | `AssociateIpamByoasn` + `advertise --asn` | A prefix advertised from a BYOASN **not** listed in that prefix's ROA = ROA-vs-ASN consistency breach |
| B10 | Customer | AWS-managed IRR/RADb route objects | AWS auto-writes RADb; customer told "don't touch" | Route object content the customer can't audit, or a stale manual object silently failing provision = integrity/availability boundary |

---

## 3. API / interface surface (IAM-anchored)

Ground truth: `list_ec2.md` (line numbers below). **★ = required resource type.**

| API | Mutating | Resource type (★) | Condition keys | Scopable to a CIDR/pool/ASN? |
|---|---|---|---|---|
| `ProvisionByoipCidr` (L9257) | yes | **none** | `ec2:Region` only | **No — region only** |
| `AdvertiseByoipCidr` (L4662) | yes | **none** | `ec2:Region` only | **No — region only** |
| `WithdrawByoipCidr` (L9756) | yes | **none** | `ec2:Region` only | **No — region only** |
| `DeprovisionByoipCidr` (L6510) | yes | **none** | `ec2:Region` only | **No — region only** |
| `MoveByoipCidrToIpam` (L9245) | yes | `ipam-pool★` | `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag` | Only to the IPAM pool (tag/ARN) |
| `DescribeByoipCidrs` (L6630) | no | none | `ec2:Region` | region-wide read oracle |
| `DescribePublicIpv4Pools` (L7248) | no | none | `ec2:Region` | region-wide read oracle |
| `DescribeIpv6Pools` (L7080) | no | none | `ec2:Region` | region-wide read oracle |
| `GetAssociatedIpv6PoolCidrs` (L8204) | no | `ipv6pool-ec2★` | `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag` | by pool tag/ARN |
| `AllocateAddress` (L4668) | yes | `elastic-ip★`; `ipam-pool`; `ipv4pool-ec2` | elastic-ip: `aws:RequestTag`,`aws:TagKeys`,`ec2:Region`; pools: `aws:ResourceTag`,`ec2:Region`,`ec2:ResourceTag` | pool: yes (ARN/tag). **IP within pool: NO — no `ec2:PublicIpAddress`** |
| `ReleaseAddress` (L9383) | yes | `elastic-ip` | +`ec2:AllocationId`, `ec2:Domain`, **`ec2:PublicIpAddress`**, … | (contrast: Release *has* the IP key, Allocate does not) |
| `CreateVpc` (L5749) | yes | `ipam-pool`;`ipv6pool-ec2`;`vpc★` | `ec2:Ipv4IpamPoolId`,`ec2:Ipv6IpamPoolId`,`ec2:Region`,`ec2:VpcID`,tags | IPAM pool id yes; **public ipv6pool-ec2: only via ARN** |
| `AssociateVpcCidrBlock` (L4832) | yes | `ipam-pool`;`ipv6pool-ec2`;`vpc★` | +`ec2:Tenancy`,`ec2:VpcID`,IPAM pool ids | same |
| `ProvisionIpamByoasn` (L9263) | yes | `ipam★` | `aws:ResourceTag`,`ec2:Region`,`ec2:ResourceTag` | to IPAM only, **not to an ASN** |
| `DeprovisionIpamByoasn` (L6516) | yes | `ipam★` | same | to IPAM only |
| `AssociateIpamByoasn` (L4761) | yes | **none** | `ec2:Region` only | **No — region only** |
| `DisassociateIpamByoasn` (L7927) | yes | **none** | `ec2:Region` only | **No — region only** |
| `DescribeIpamByoasn` (L7008) | no | none | `ec2:Region` | region-wide read oracle |

**Schema-level hidden knob:** `CidrAuthorizationContext` is **`Required: No`** on `ProvisionByoipCidr`
(`API_ProvisionByoipCidr.md` L27) — the authorization context is an *optional* request parameter. The
`{Message, Signature}` object (`API_CidrAuthorizationContext.md`) is "authorization … to bring a specific IP
address range to a specific AWS account" but is not schema-mandatory.

**Confirmed IAM facts (all from the full key table L10041–L10190):**
- **No** `ec2:Cidr`, `ec2:ByoipCidr`, `ec2:PublicIpv4Pool`, `ec2:Ipv6Pool`, `ec2:Asn`, or `ec2:Byoasn` key
  exists anywhere. `ec2:Ipv4IpamPoolId`/`ec2:Ipv6IpamPoolId` reference **IPAM** pools, **not** public
  `ipv4pool-ec2-*` pools.
- **No** org/account global key (`aws:PrincipalOrgID`, `aws:ResourceOrgID`, `aws:PrincipalOrgPaths`) on **any**
  of these actions (grep over the whole file = zero matches).
- `ec2:PublicIpAddress` exists on `ReleaseAddress`, `EnableAddressTransfer`, `DisassociateNatGatewayAddress`
  and the elastic-ip resource row — but is **deliberately absent from `AllocateAddress`**.

---

## 4. Boundary-lens catalog walk

### Lenses that FIRE

**Lens S/U — condition-key scoping vs. enforcement (HEADLINE).** The four BYOIP lifecycle actions and both
`Associate/DisassociateIpamByoasn` carry **no resource type and only `ec2:Region`** (§3). Any policy that grants
them grants them **region-wide across every present and future BYOIP range and ASN in the account**. There is no
condition key to pin a CIDR, pool id, or ASN. → Lead 1, Lead 6.

**Lens P/N — identity-proofing / naming-authority of the ownership gate.** The gate anchors to RDAP-record +
ROA control, not AWS account identity (byoip-onboard.md L20). The signed `{account}` field is self-asserted and
not documented to be cross-checked against the caller; the authorization context is optional at the schema
level. → Lead 2.

**Lens P (replay) — bearer-blob freshness.** `Message`+`Signature` is an offline-signed blob with a
*signer-chosen* `{YYYYMMDD}` expiry, no AWS nonce, no documented single-use. Re-run is explicitly expected on
`failed-provision`. → Lead 3.

**Lens AA (lifecycle) / U — persistence of advertisement past the proof.** Cert removal is advisory; "Amazon
*reserves the right* to stop advertising" if a ROA goes invalid — **no stated automatic re-validation cadence**.
Advertisement can outlive the ROA/cert. → Lead 4.

**Lens P (degraded gate) — non-public IPv6 drops the ROA anchor.** `--no-publicly-advertisable` IPv6 needs no
ROA (RDAP cert only), provisions "within minutes." Single-anchor, fast, low-visibility. → Lead 5.

**Lens A (within-pool squatting) — `AllocateAddress` cannot pin the IP.** No `ec2:PublicIpAddress` key on
Allocate (present on Release) ⇒ IAM can restrict *which pool* but not *which address* a principal pulls. → Lead 7.

**Lens L (DoS / exhaustion).** 5 BYOIP ranges per region, **not** adjustable via Service Quotas (Support only).
No condition key caps per-principal consumption. An over-privileged sibling can exhaust the shared account quota
or black-hole a range via region-wide withdraw. → Lead 8 (cross-ref `fleet-quotas` sibling for the quota-DoS
pattern).

**Lens B/A (BYOASN origin binding).** ASN proof and CIDR proof are **independent** signed contexts; the docs do
not state the ROA must list the BYOASN before `advertise --asn X` succeeds. → Lead 9.

**Lens AA (cross-account sharing).** RAM sharing of a BYOIP range is blocked **unless** IPAM+Organizations — a
stated isolation guarantee to trace to its mechanism. → Lead 10 (defer mechanism to IPAM docs, outside mirror).

### Null hypotheses (pages checked)

- **Lens F (translation / wire-protocol injection) — N/A.** Read all four UserGuide pages + the lifecycle API
  refs; BYOIP has no customer-input→query/translation layer. The only "parse" is signature verification at the
  RIR. No injection seam.
- **Lens D (data→control-plane escape) — N/A.** No customer-reachable data-plane process exists in BYOIP;
  nothing to pivot from. (The advertiser/validator are AWS-internal, not customer-reachable.)
- **Lens Q (uploaded-blob parsing) — N/A for the service.** The X.509 cert is uploaded to the *RIR's* RDAP, not
  to an AWS parser; AWS fetches it via `whois`. No AWS-side blob-parse surface. (Noted as an RIR-side concern,
  out of AWS scope.)
- **Lens G (SSRF) — doc-gap, low.** The validator dereferences RIR/RIPEstat endpoints, but these are
  AWS-fixed, not customer-supplied URLs. No customer-controlled URL field on any BYOIP API. Marked low, not a
  lead.
- **Lens O (audit-log evasion) — doc-gap.** The async Local Zone / `instant`-style states and the
  "within minutes" non-public path were not traced to EventBridge/CloudTrail coverage in these pages; flagged
  as a follow-up (§8), not a confirmed lead.

---

## 5. NEW / changed surface — concentrate fire here

1. **The four lifecycle actions are IAM-unscopable to a CIDR** (region-only). This is the single highest-value,
   fully-confirmed structural fact. (Lead 1.)
2. **The signed-authorization bearer blob** — optional at schema level, signer-chosen expiry, no nonce,
   self-asserted `{account}`. (Leads 2 & 3.) **Highest-value falsifiable test.**
3. **Non-public IPv6 single-anchor gate** (Lead 5) — fastest/cheapest to exercise in an authorized lab.
4. **BYOASN** — association actions are also region-only unscopable (Lead 6), and ROA-vs-ASN consistency is
   undocumented (Lead 9). **Biggest documentation blind spot** (proof format lives in `tutorials-byoasn.html`,
   outside this mirror — §8).

---

## 6. Ranked leads (falsifiable hypotheses)

### Lead 1 — BYOIP lifecycle actions are IAM-unscopable to a CIDR (region-wide black-hole) — **HIGH (customer least-priv footgun), CONFIRMED structural**
- **Claim:** Any grant of `ec2:ProvisionByoipCidr` / `AdvertiseByoipCidr` / `WithdrawByoipCidr` /
  `DeprovisionByoipCidr` necessarily authorizes the principal over **every** BYOIP range in the region — a
  grant intended for one prefix cannot be constrained to it.
- **Mechanism:** `list_ec2.md` L9257/L4662/L9756/L6510 — empty resource line, `ec2:Region` sole key; no
  `ec2:Cidr`/`ec2:ByoipCidr` key in the key table (L10041–L10190).
- **Confirm/refute oracle:** author a policy attempting `Resource: arn:aws:ec2:…:byoip-cidr/…` or a
  `Condition` on the CIDR — IAM rejects/ignores it; a principal so-granted can `withdraw-byoip-cidr --cidr <any
  other provisioned prefix>` in the region. A single withdraw de-announces a production prefix.
- **Impact:** region-wide, un-cancellable (ec2-byoip.md L112 "cannot cancel a pending advertisement or
  withdrawal"); any delegation = full BYOIP authority. Blends into Lead 8 for the DoS framing.

### Lead 2 — `{account}` in the signed message may not be bound to the caller — **HIGH if unbound, needs live confirm**
- **Claim:** AWS does not document cross-checking the signed `{account}` field against the authenticated caller
  account; the trust anchor is RDAP+ROA control, not account identity.
- **Mechanism:** byoip-onboard.md L20 (RIR authenticates signature vs RDAP cert + ROA); message composed
  client-side (`1|aws|{account}|…`); `CidrAuthorizationContext` `Required: No` (`API_ProvisionByoipCidr.md` L27).
- **Oracle:** from Account B, `provision-byoip-cidr` with a `Message` whose `{account}` = Account A (or a random
  12-digit value) but a valid signature from the prefix's RDAP cert. Success ⇒ `{account}` not bound. Secondary:
  flip one digit of a correct account and resubmit.
- **Precondition:** attacker already controls RDAP cert + ROA (dominant precondition — so this is primarily an
  authz-clarity / account-confusion issue, not a standalone takeover). **Severity High, likelihood gated by that
  precondition.**

### Lead 3 — authorization context is a replayable bearer blob — **MEDIUM–HIGH, needs live confirm**
- **Claim:** `Message`+`Signature` is single-signer, signer-chosen expiry, no AWS nonce, no documented
  single-use ⇒ a captured pair is replayable (re-provision after deprovision, another region, possibly another
  account) within the self-chosen window.
- **Mechanism:** byoip-onboard.md L28 (expiry is signer-chosen), L78 (re-run expected on `failed-provision`);
  the blob is passed on the CLI (leaks to shell history / CI logs). `{YYYYMMDD}` is unbounded in the format.
- **Oracle:** (a) provision→deprovision→resubmit identical blob; (b) replay a us-east-1 blob to us-west-2; (c)
  set `{YYYYMMDD}` years out and confirm acceptance (does AWS cap the window?).
- **Impact:** anyone who captures the blob within the window can re-assert provisioning; mitigated by ROA/RDAP
  still having to be valid at verification time.

### Lead 4 — advertisement can outlive the ownership proof (no re-validation cadence) — **MEDIUM**
- **Claim:** No stated automatic/periodic ROA re-check; enforcement is discretionary ("reserves the right").
  A revoked/expired ROA (or removed RDAP cert) does not documented-ly auto-withdraw the prefix.
- **Mechanism:** prepare-for-byoip.md L258 ("Amazon reserves the right to stop advertising"); no cadence
  sentence anywhere; cert removal advisory (L196/L240).
- **Oracle:** provision+advertise with a valid ROA, then revoke/delete the ROA (or let it expire) and poll
  `describe-byoip-cidrs` over days/weeks; if state stays `advertised`, enforcement is discretionary-only.
- **Impact:** "provision while you control it, retain advertisement after you lose it" persistence.

### Lead 5 — non-public IPv6 is a single-anchor (ROA-less) gate — **MEDIUM**
- **Claim:** `--no-publicly-advertisable` IPv6 drops the RPKI/ROA anchor, leaving only the RDAP-cert signed
  message; provisions "within minutes."
- **Mechanism:** byoip-onboard.md L85 / prepare-for-byoip.md L32,L261 / ec2-byoip.md L42 (ROA not required,
  RDAP still required); L83 ("within minutes"). **Doc inconsistency to resolve:** UserGuide says `/60`
  (ec2-byoip.md L41), `API_ProvisionByoipCidr.md` L20 says `/56` — the min non-public prefix size disagrees.
- **Oracle:** provision a `--no-publicly-advertisable` IPv6 with a valid RDAP-cert signature and **no ROA**;
  reaching `provisioned` in minutes confirms ROA is not consulted. Then test whether a prefix that would fail
  the public gate can be non-public-provisioned.
- **Impact:** RDAP-record control alone suffices; limited BGP blast radius (reachable only via
  DX/VPN/TGW) but low owner-visibility and fast turnaround.

### Lead 6 — `Associate/DisassociateIpamByoasn` are region-only unscopable — **MEDIUM (least-priv footgun), CONFIRMED structural**
- **Claim:** Binding/unbinding a brought ASN to a CIDR is gated purely by action + region; no resource type,
  no `ec2:Asn` key.
- **Mechanism:** `list_ec2.md` L4761 / L7927 (empty resource line, `ec2:Region` only); no ASN condition key.
- **Oracle:** attempt to scope an `AssociateIpamByoasn` policy to a specific ASN/CIDR — not expressible; a
  so-granted principal can (dis)associate any BYOASN↔CIDR in the region.
- **Impact:** parallels Lead 1 for the ASN surface.

### Lead 7 — within-pool address squatting: `AllocateAddress` cannot pin the IP — **MEDIUM (least-priv footgun), CONFIRMED structural**
- **Claim:** IAM can restrict *which pool* a principal allocates from (ipv4pool-ec2 ARN/tag) but **not which
  specific address** — `AllocateAddress --address x.x.x.x` cannot be denied by condition key.
- **Mechanism:** `list_ec2.md` L4668 — AllocateAddress has **no `ec2:PublicIpAddress`** (present on Release
  L9386). byoip-working-with.md: `allocate-address --public-ipv4-pool --address`.
- **Oracle:** policy granting AllocateAddress on a pool but attempting to deny a specific `--address` — not
  expressible; the principal can claim any (e.g. reputation-sensitive / previously-used) address in the pool.
- **Impact:** intra-account; relevant where distinct teams share a BYOIP pool. Cross-reference the EIP-squatting
  / dangling-DNS leads owned by `using-instance-addressing` + `working-with-ip-addresses`.

### Lead 8 — shared 5-range quota exhaustion / region-wide withdraw DoS — **MEDIUM**
- **Claim:** 5 BYOIP ranges per region is a shared, **Service-Quotas-non-adjustable** account limit; combined
  with Lead 1, an over-privileged principal can exhaust it or de-announce prefixes region-wide.
- **Mechanism:** ec2-byoip.md L44 (5/region, Support-only increase); L112 (withdraw un-cancellable); Lead 1
  (region-wide authority).
- **Oracle:** provision 5 ranges to block a 6th; or `withdraw-byoip-cidr` a sibling's advertised prefix.
- **Impact:** availability; cross-ref the `fleet-quotas` plan's shared-pool intra-account DoS pattern.

### Lead 9 — BYOASN↔CIDR origin-consistency not documented to be enforced — **MEDIUM, needs live confirm + doc fetch**
- **Claim:** ASN proof and CIDR proof are independent contexts; docs don't state the prefix's ROA must authorize
  the BYOASN as origin before `advertise --asn X`.
- **Mechanism:** `API_AsnAuthorizationContext.md` (separate `{Message,Signature}`); ec2-byoip.md L109
  (ASN at advertise time); `AssociateIpamByoasn` header "a BYOIP CIDR that you own in the same Region."
- **Oracle:** with a provisioned CIDR + provisioned BYOASN, `associate-ipam-byoasn` then `advertise --asn X`;
  test whether AWS requires the prefix's ROA to list X (vs only Amazon ASNs). Also test associating a BYOASN
  with a non-public-path CIDR.
- **Blind spot:** BYOASN proof format lives in `tutorials-byoasn.html` (IPAM, not in this mirror) — §8.

### Lead 10 — RAM cross-account sharing isolation guarantee — **LOW–MEDIUM (trace mechanism)**
- **Claim:** "You cannot share your IP address range with other accounts using AWS RAM unless you use IPAM +
  Organizations" (ec2-byoip.md L45) is a stated isolation guarantee; trace it to the enforcing mechanism and
  test the IPAM+Orgs path for over-broad sharing.
- **Oracle / mechanism:** defer to IPAM+Organizations docs (outside this mirror). Flag for the IPAM plan.

---

## 7. What this plan OWNS vs. DEFERS (cross-references)

**Owns (develop fully here):**
- The four BYOIP lifecycle actions' IAM-unscopability (Lead 1) — promotes hub lead #4 from one line to a full
  lead with per-action `list_ec2` line numbers.
- The entire cryptographic ownership-proofing chain: X.509/RDAP/ROA/RPKI + signed message (Leads 2–5) — **no
  sibling covers this.**
- BYOASN region-only unscopability + origin-consistency (Leads 6, 9).
- Within-pool `AllocateAddress` IP-squatting as it pertains to BYOIP pools (Lead 7).
- BYOIP-specific 5-range quota DoS framing (Lead 8).

**Defers / cross-references (do not duplicate):**
- **EIP transfer** (`AcceptAddressTransfer`/`EnableAddressTransfer` account-binding, no dest-account key) →
  owned by `ec2-networking` hub + `using-instance-addressing` / `working-with-ip-addresses`.
- **EIP squatting / dangling-DNS / public-IPv4 pool reuse** → `using-instance-addressing`,
  `working-with-ip-addresses`. Lead 7 here is the BYOIP-pool-specific slice only.
- **Shared-quota DoS pattern** generically → `fleet-quotas` plan.
- **IPAM + Organizations sharing mechanism**, **BYOASN proof-message format**, **DNS-TXT (IPAM) ownership
  method** → Amazon VPC IPAM docs (`tutorials-byoip-ipam.html`, `tutorials-byoasn.html`) — outside this mirror.
- **ec2-networking hub** remains the parent; this plan is its BYOIP child.

---

## 8. Doc gaps & follow-ups for the next agent

1. **BYOASN proof format not in this corpus.** `AsnAuthorizationContext` message/signature format is documented
   only in `https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoasn.html` (IPAM, not mirrored). Fetch to
   close Lead 9's account/replay questions for the ASN path.
2. **Non-public IPv6 prefix-size contradiction.** UserGuide `/60` (ec2-byoip.md L41, prepare-for-byoip.md L245)
   vs. `API_ProvisionByoipCidr.md` L20 `/56`. Present in **both** offline and online (not drift) — resolve
   which the control plane actually enforces.
3. **EventBridge / CloudTrail coverage (Lens O).** Whether the async Local Zone states
   (`pending-advertising`/`pending-withdrawal`, `eu-central-1-ist-1`, up to 5 business days) and the
   "within minutes" non-public path emit timely events was not traced in these pages — confirm the observability
   surface for Leads 3–5.
4. **IPAM DNS-TXT ownership method.** The second ownership-proof method (DNS TXT via IPAM) is entirely in the
   IPAM user guide; a parallel Lens-P analysis of it is a separate follow-up.

### Drift check result (online vs offline)
Online `ec2-byoip.html`, `prepare-for-byoip.html`, `byoip-onboard.html` fetched and compared to the offline
`.md`: **no material differences.** Amazon ASNs (16509/14618), GovCloud 8987, European Sovereign Cloud
16509/214101, the message format, RSA-PSS/SHA256 signing command, whois/RIPEstat validation steps, cert-removal
advisory, 365-day example, non-public /60 "within minutes" — all identical online and offline. `list_ec2.md`
internally consistent (index ↔ detail blocks ↔ resource/condition-key tables). The only inconsistency is the
internal `/56` vs `/60` doc disagreement in item 2 (present in both mirrors, not a sync artifact).

---

*Produced by the `security-questionbuilder` skill. Documentation-only; all oracles are for execution by an
authorized hunter in a sanctioned test account against synthetic/canary prefixes — never against production or
AWS's own service plane.*
