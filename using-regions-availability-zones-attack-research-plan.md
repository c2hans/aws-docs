# EC2 "Regions and Zones" — Attack / Research Plan

**Target doc:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html
**Offline twin:** `docs/AWSEC2/latest/UserGuide/using-regions-availability-zones.md`
**Authoritative IAM source:** `docs/service-authorization/latest/reference/list_ec2.md` (trust this over User-Guide prose — see memory `reference-aws-iam-service-auth-ref-url`)
**Method:** `security-questionbuilder` (boundary-first). Produced 2026-10-15.

> **Relationship to the EC2 Networking hub plan.** This page is a *child* of `ec2-networking-attack-research-plan.md` (cluster 4: Placement / Topology / Zones; and cluster 1: IP/EIP/BYOIP). The hub already **owns** these leads — do **not** re-derive them here, follow the cross-references:
> - EIP **cross-account transfer** (no destination-account condition key) → hub cluster 1.
> - `AllocateAddress` has **no `ec2:PublicIpAddress` / no address-value** condition key → hub cluster 1.
> - **BYOIP** region-wide-advertisement unscopability → hub cluster 1.
> - The AZ-name-vs-Zone-ID footgun existed in the hub as a *secondary* lead. **This plan promotes it to a primary, fully-worked lead (L2)** because this is the page that *teaches customers the AZ name* (`us-east-1a`) and never mentions the ID — it is the origin of the footgun.
>
> Everything below is **net-new or promoted** surface specific to the Regions/Zones/Local-Zones/Wavelength/Outposts concepts this page introduces.

---

## §0 — Executive summary (where to spend the hunter's time)

This page looks like inert concept prose ("a Region is a physical location… an AZ is one or more data centers"). The security value is that **it defines the vocabulary customers write their isolation and residency controls in — and that vocabulary is a trap in three independent ways:**

1. **The zone opt-in toggle is a fully-unscopable, account-wide, one-way door.** `ModifyAvailabilityZoneGroup` has **no condition key and no resource type** in `list_ec2`, its `OptInStatus` has only one legal value (`opted-in`), and the API doc says you **must contact AWS Support to reverse it**. Any principal with `ec2:ModifyAvailabilityZoneGroup` permanently expands the account's physical footprint into a Local/Wavelength Zone that no SCP can scope and no self-service API can undo. **(L1 — primary.)**

2. **Residency/isolation controls keyed on the AZ *name* are a false guarantee.** Two condition keys exist — `ec2:AvailabilityZone` (the *name*, e.g. `us-east-1a`, which AWS randomizes **per account**) and `ec2:AvailabilityZoneId` (the *ID*, e.g. `use1-az1`, physically stable across accounts). The doc teaches only the name. AWS's own sharing docs (RAM, Capacity-Reservation-sharing, Dedicated-Host-sharing) say you **must** use the AZ ID for cross-account co-location. A defender who writes "deny launch outside `us-east-1a`" org-wide is pinning a *different physical zone in every account*. **(L2 — promoted primary.)**

3. **Outpost-ARN scoping is asymmetric and partly impossible.** `CreateVolume` carries **no `ec2:OutpostArn` key** (confirmed `list_ec2`), while `CreateSnapshot` and `CreateCapacityReservation` do. A policy intending "volumes may only be created in-Region, never on the on-prem Outpost" (or the reverse) **cannot be expressed** for `CreateVolume`. **(L4.)**

Secondary but worth a pass: unscopable `DescribeAvailabilityZones`/`DescribeRegions` recon oracles that leak the physical AZ-ID mapping, opt-in posture, and Local/Wavelength parent-zone topology (L5); the Outposts service-link / "same VPC / private IP" / "AWS operates, monitors, and manages" trust assertions with no customer-verifiable mechanism (L6); and the cross-service seam where Region opt-in actually lives in the `account:*` namespace, not EC2, with an STS global-endpoint token-validity quirk (L7).

**Highest-value first:** L2 (silent residency-control bypass, affects every org using AZ-name SCPs), then L1 (irreversible account-wide footprint expansion), then L4 (unexpressible Outpost isolation policy).

---

## §1 — Components, Assets, and Design

### What the page actually defines (the mechanism, not the marketing)
- **Region** — isolated set of AZs with its own regional endpoints. Doc asserts: *"Each Region is designed to be isolated from the other Regions"* and *"we don't automatically replicate resources across Regions."* Regions after 2019-03-20 are **opt-in** (disabled by default).
- **Availability Zone (AZ)** — "one or more data centers." Identified two ways:
  - **AZ name / zone code** = Region + letter, e.g. `us-east-1a`. **Randomized per account** (RAM/CR-sharing/DH-sharing docs confirm: *"AWS maps the physical Availability Zones randomly to the Availability Zone names for each AWS account"*).
  - **AZ ID (Zone ID)** = e.g. `use1-az1`. *"A unique and consistent identifier… the same physical location in every AWS account."*
- **Local Zone** — compute closer to a metro. *"To use a Local Zone, you must first enable it."* Opt-in via `ModifyAvailabilityZoneGroup`.
- **Wavelength Zone** — compute inside a carrier (telco) network. *"To use a Wavelength Zone, you must first opt in to the Zone."* Uses **Carrier IP** (carrier-gateway NAT; **no inbound connection from the internet**) and a **carrier network edge**.
- **Network border group** — *"a unique set of Availability Zones, Local Zones, or Wavelength Zones from which AWS advertises IP addresses"* (e.g. `us-west-2-lax-1a`). EIPs allocated to a border group are **immovable** between border groups (`AllocateAddress` doc: *"IP addresses cannot move between network border groups"*).
- **AWS Outposts** — on-prem rack/servers that are *"a pool of AWS compute and storage capacity deployed at a customer site. AWS operates, monitors, and manages this capacity as part of an AWS Region."* Reached from Region over an **encrypted service-link VPN**; Outpost resources *"communicate… using private IP addresses, all within the same VPC."* Outpost ARN form: `arn:aws:outposts:<region>:<account-id>:outpost/op-xxxx` (ARN embeds the owning account). Outpost **servers** are instance-store only (no EBS); recommended root volume ≤30 GiB.

### Assets & identifiers
| Asset | Identifier shape | Notes for the hunter |
|---|---|---|
| Physical AZ | AZ ID `use1-az1` (stable) ↔ AZ name `us-east-1a` (per-account random) | The name↔ID map **is itself a per-account secret-ish fact**; `DescribeAvailabilityZones` returns both → de-randomization oracle. |
| Zone group (Local/Wavelength) | group name e.g. `us-west-2-lax-1` | Opt-in toggle target; account-wide. |
| Network border group | name e.g. `us-west-2-lax-1a` | EIP locality boundary; immovable. |
| Outpost | ARN w/ account-id + `op-` id | Account-scoped by ARN construction; `op-` id entropy unknown (doc-gap). |
| Region | region name + opt-in status | Opt-in state governed by `account:*`, not `ec2:*`. |

### Design observations that generate questions
- **No data plane here** — this is a *control-plane concept* page. The "boundary" is almost entirely **IAM-policy expressibility** (can a defender *write* the control they think they can?) plus **documented-guarantee-vs-mechanism** (Lens U). That is unusual and shifts the lens weighting toward **S, U, X, L, AA** and away from F/G/Q/injection lenses.
- **The randomized AZ-name mapping is a deliberate availability feature** ("distribute resources across AZs") that **doubles as a security footgun** when reused as a policy key. Classic Lens-U "a guarantee for one property (spread) silently fails to be a guarantee for another (residency/isolation)."

---

## §2 — Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Low-priv principal in account | Account-wide physical footprint | `ec2:ModifyAvailabilityZoneGroup` (unscopable, one-way) | A principal denied every other expansion lever can still opt the whole account into a Local/Wavelength Zone; **no SCP can carry an exception and no self-service call reverses it** → control-gap breach. |
| Org security team's SCP author | Physical AZ residency intent | SCP keyed on `ec2:AvailabilityZone` (name) | Same SCP, applied to two accounts, authorizes **different physical zones** → the "deny outside AZ X" guarantee is void. Oracle: in account A `us-east-1a`=`use1-az1`, in account B `us-east-1a`=`use1-az4`; a launch "in `us-east-1a`" lands in different physical locations. |
| Policy author intending Outpost isolation | `CreateVolume` on/off an Outpost | `ec2:OutpostArn` **absent** from the volume resource row | No statement can allow/deny `CreateVolume` by Outpost ARN → "EBS must stay in-Region" (or "must stay on the Outpost") is **inexpressible**; `CreateSnapshot` *can* express it → asymmetry breach. |
| Any read-capable principal / cross-tenant recon | Physical topology + opt-in posture | `DescribeAvailabilityZones` / `DescribeRegions` (no condition key) | Caller with only `Describe*` learns the AZ-name→ID map, which zones are opted-in, and which parent zone fronts a Local/Wavelength Zone's control plane → de-randomization + footprint-recon oracle. |
| Customer workload in Wavelength Zone | VPC / Region services | Carrier gateway NAT, service-link | Any inbound path from the carrier/internet into the Wavelength subnet other than the documented NAT, or any Outpost→Region path outside the encrypted service link → segmentation breach. |
| Customer | AWS-managed Outpost capacity | *"AWS operates, monitors, and manages this capacity"* | Any customer-reachable identity/credential/management interface belonging to the AWS-operated Outpost control stack → **hard-stop service-plane breach; preserve evidence, flag for disclosure.** |
| Principal with `ec2:ModifyAvailabilityZoneGroup` but NOT `account:EnableRegion` | New Region vs new Zone | Two different namespaces govern "expand my footprint" | If zone opt-in (EC2) is reachable while Region opt-in (account) is denied, the EC2 toggle is a weaker-governed footprint-expansion path than the one the org actually locked down. |

**Canonical hard stop:** anything that surfaces an identity/ARN/account belonging to AWS's own Outpost or zone-control fleet is out of scope to exploit — document and stop.

---

## §3 — API / interface surface

| Name | Mutating? | Int/Ext | Functionality | Authorized callers | **Condition keys in `list_ec2`** | Notes |
|---|---|---|---|---|---|---|
| `ModifyAvailabilityZoneGroup` | **Mutating** | External | Opt the **account** into a Local/Wavelength zone group | any principal w/ the action | **NONE; no resource type; Access=Write** | `OptInStatus` only legal value `opted-in`; **opt-out requires AWS Support** → one-way. **(L1)** |
| `DescribeAvailabilityZones` | Non-mut | External | List zones (name, **ID**, type, opt-in, border group, parent zone) | any principal w/ the action | **NONE; Access=List** | De-randomization + topology oracle. `AllAvailabilityZones=true` reveals zones even when not opted-in. **(L5)** |
| `DescribeRegions` | Non-mut | External | List Regions + opt-in status + endpoint | any principal w/ the action | **NONE; Access=List** | Enumerates opt-in posture of all Regions. **(L5)** |
| `AllocateAddress` | Mutating | External | Allocate EIP, optionally pinned to a `NetworkBorderGroup` | any principal w/ the action | elastic-ip row: `aws:RequestTag/aws:TagKeys/ec2:Region` **only** | **No `ec2:NetworkBorderGroup` key** → border-group placement unscopable; EIP immovable once placed. **(L3)** Cross-ref hub cluster 1 for the rest of EIP surface. |
| `CreateVolume` | Mutating | External | Create EBS volume, optionally `--outpost-arn` | any principal w/ the action | volume row: `ec2:AvailabilityZone`, `ec2:AvailabilityZoneId`, `ec2:Encrypted`, `ec2:KmsKeyId`, `ec2:Region`, `ec2:Volume*` — **NO `ec2:OutpostArn`** | Cannot scope by Outpost. **(L4)** |
| `CreateSnapshot` | Mutating | External | Snapshot, can target Outpost | any principal w/ the action | **HAS `ec2:OutpostArn`** | The asymmetry counterpart to `CreateVolume`. **(L4)** |
| `account:EnableRegion` / `DisableRegion` / `GetRegionOptStatus` / `ListRegions` | Mut/Non-mut | External | Region opt-in control (different service!) | account principals | *(account namespace — not EC2)* | Region footprint governed outside EC2 → Lens U/cross-service **(L7)**. |

**Undocumented/under-surfaced knobs to probe:**
- `DescribeAvailabilityZones` `AllAvailabilityZones` param (shows non-opted-in zones) and the `parent-zone-id`/`parent-zone-name` filters — surfaced in the API ref, less so in console. Parent-zone fields reveal *which standard AZ runs a Local/Wavelength zone's control plane* ("some of the Local Zone and Wavelength Zone control plane operations, such as API calls").
- `ModifyAvailabilityZoneGroup` — console only ever shows "enable"; confirm the SDK/API accepts nothing but `opted-in` (so there's genuinely no self-service opt-out knob to find).

---

## §4 — Boundary-lens leads (the questions)

### L1 — `ModifyAvailabilityZoneGroup`: unscopable, account-wide, one-way footprint expansion  *(Lens S + U + AA + L) — PRIMARY*
- **Claim:** A principal granted only `ec2:ModifyAvailabilityZoneGroup` can permanently opt the **entire account** into a Local or Wavelength Zone, and no SCP/IAM policy can restrict *which* zone group, nor can any self-service API undo it.
- **Mechanism (doc evidence):** `list_ec2` — `ModifyAvailabilityZoneGroup` row has **no condition key and no resource type**, Access = Write. API ref: *"Changes the opt-in status of the specified zone group **for your account**"*; `OptInStatus` *"only valid value is `opted-in`. You must contact AWS Support to opt out."*
- **Confirm/Refute oracle:**
  - *Scopability:* attempt a policy `Allow ec2:ModifyAvailabilityZoneGroup` with any `Condition` on zone-group / Region / tag → if IAM silently ignores the condition (because no such key exists) and the call still succeeds for an *arbitrary* group, the control is unscopable. (Confirmed from `list_ec2` as doc-fact; live test is to verify IAM doesn't honor an unsupported condition.)
  - *Irreversibility:* confirm no `OptInStatus: not-opted-in` / no `opt-out` SDK path exists → the only reversal is a support ticket.
- **Severity:** Medium-High as a **least-privilege / blast-radius footgun**: expands physical/billing footprint (new-zone capacity, cross-metro data egress, new carrier edge), is irreversible without AWS, and is invisible to any zone-group-scoped guardrail. Not cross-account, so not Critical — but a genuine "control you cannot write."
- **Preconditions:** one principal with the action (often bundled in broad `ec2:*` or "EC2 power user" policies). **Cost:** one API call. **Reversal cost:** AWS Support ticket (asymmetric — attacker's cost ≪ defender's).
- **Follow-up for hunter:** check whether `ec2:ModifyAvailabilityZoneGroup` is included in common AWS-managed policies (`AmazonEC2FullAccess`, PowerUser) — if so, the footgun ships enabled.

### L2 — AZ *name* vs AZ *ID*: residency/isolation SCPs keyed on the name are a false guarantee  *(Lens U + S) — PROMOTED PRIMARY*
- **Claim:** An org that enforces data residency / blast-radius isolation with a condition on `ec2:AvailabilityZone` (the name, e.g. `us-east-1a`) believes it has pinned a physical location, but because AWS randomizes the name→physical map **per account**, the same SCP authorizes a **different physical AZ in every account** — so "all prod workloads in one AZ for latency" or "never co-locate tenants A and B" silently fails.
- **Mechanism (doc evidence):**
  - `list_ec2` condition-key defs: `ec2:AvailabilityZone` = *"the **name** of an Availability Zone"*; `ec2:AvailabilityZoneId` = *"the **ID** of an Availability Zone"* — **two distinct keys**.
  - This target page teaches **only the name** (`us-east-1a`); never mentions the ID.
  - AWS's own docs insist on the ID for cross-account correctness: RAM `working-with-az-ids` (*"us-east-1a… might not represent the same physical location as us-east-1a for a different account"*), `capacity-reservation-sharing.md:35-39`, `dh-sharing.md:53-57` (*"to identify the location… you must use the Availability Zone ID"*).
  - Instance/subnet/volume rows in `list_ec2` carry **both** keys — so the ID key *is available* to defenders who know to use it.
- **Confirm/Refute oracle:** In two accounts of the same org, call `DescribeAvailabilityZones` and compare the `zoneName`→`zoneId` map. If `us-east-1a` ≠ same `zoneId` across accounts (expected), then an identical `ec2:AvailabilityZone`-keyed SCP authorizes different physical zones → guarantee refuted. Conversely, show that only an `ec2:AvailabilityZoneId`-keyed policy is account-portable.
- **Severity:** High as a **silent-control-failure / design-trap**: the defender gets *no error*, the policy *looks* correct, and the failure is only visible by cross-referencing physical IDs the console hides. Impact = defeated residency/anti-affinity/isolation posture across a whole org.
- **Doc-gap to resolve first:** a possible **Nov 2025 change making new accounts use *consistent* (non-randomized) AZ-name mapping** could *narrow* this to pre-Nov-2025 accounts. The subagent found **no primary source** confirming it (RAM doc still says "random" as of 2026-10-15, no carve-out). **Hunter must confirm account vintage & current mapping behavior before asserting universality.** If the change is real, reframe L2 as "mixed fleet: old accounts randomized, new ones not — an org-wide name-keyed SCP is inconsistent *between* account generations," which is still a defect.
- **Cross-ref:** hub cluster 4 lists this as a secondary lead — this is the worked version; link back.

### L3 — `AllocateAddress` network-border-group placement is unscopable  *(Lens S)*
- **Claim:** A policy cannot restrict *which* network border group an EIP is allocated into, so a principal can pull a Carrier IP / Local-Zone IP (placing an account-advertised address at a carrier/metro edge) even if the intent was "Region EIPs only."
- **Mechanism:** `AllocateAddress` elastic-ip row in `list_ec2` supports only `aws:RequestTag/aws:TagKeys/ec2:Region` — **no `ec2:NetworkBorderGroup` key exists anywhere** in `list_ec2`. API ref: `NetworkBorderGroup` param *"limit the IP address to this location… IP addresses cannot move between network border groups."*
- **Confirm/Refute oracle:** author `Allow ec2:AllocateAddress` + `Condition {StringEquals: ec2:NetworkBorderGroup}` → IAM ignores the unknown key; `AllocateAddress --network-border-group <local-zone-group>` still succeeds. Breach = EIP placed in a border group the policy meant to forbid.
- **Severity:** Medium hardening gap. Immovability means a mistaken placement sticks (must release/re-allocate). **Cross-ref hub cluster 1** for the broader EIP/BYOIP picture — this lead is only the *border-group-param-is-unscopable* slice.

### L4 — `CreateVolume` cannot be scoped to an Outpost; `CreateSnapshot` can — asymmetry  *(Lens X + S)*
- **Claim:** A guardrail intending "EBS volumes may only be created in-Region (never on the on-prem Outpost)" — or the inverse, "data must stay on the Outpost" — is **inexpressible for `CreateVolume`**, even though the analogous `CreateSnapshot` guardrail *is* expressible, creating a parity gap an auditor would not expect.
- **Mechanism:** `list_ec2` — `CreateVolume` volume resource row lists `ec2:AvailabilityZone/AvailabilityZoneId/Encrypted/KmsKeyId/Region/Volume*` but **not `ec2:OutpostArn`** (line ~5743). `CreateSnapshot` **has `ec2:OutpostArn`** (line ~4999); CapacityReservation rows also have it (~4617/4728). This target page's own example is `create-volume --outpost-arn arn:aws:outposts:…` — i.e. the param exists at the API, but no matching condition key.
- **Confirm/Refute oracle:** policy `Deny ec2:CreateVolume if ec2:OutpostArn present` (or `Allow` only when absent) → IAM ignores the unsupported key, `create-volume --outpost-arn …` succeeds regardless. Then show `Deny ec2:CreateSnapshot when ec2:OutpostArn=…` *does* bite → asymmetry confirmed.
- **Severity:** Medium-High for Outpost customers with residency/exfil requirements: you can place customer data on (or pull it off) the physical on-prem rack in a way IAM cannot gate. Note the inverse exfil story too: data created on an Outpost (private, on-prem) vs snapshotted into Region.
- **Follow-up:** sweep *all* EC2 actions that accept an Outpost ARN param vs which carry the `ec2:OutpostArn` key — enumerate the full asymmetry set (this is one instance; there may be more).

### L5 — Unscopable `DescribeAvailabilityZones` / `DescribeRegions` recon oracles  *(Lens A + O)*
- **Claim:** Any principal with the (unconditionable) `Describe*` action can (a) **de-randomize** the account's AZ-name→ID map, (b) enumerate opt-in posture of all zones/Regions, and (c) learn which standard AZ fronts each Local/Wavelength Zone's control plane — useful for targeting and for inferring an account's physical footprint.
- **Mechanism:** both actions have **no condition key** in `list_ec2` (Access=List). `DescribeAvailabilityZones` returns `zoneName`+`zoneId`+`zoneType`+`optInStatus`+`networkBorderGroup`+`parentZoneId/Name`; `AllAvailabilityZones=true` reveals zones even without opt-in. API ref: parent zone *"handles some of the Local Zone and Wavelength Zone control plane operations, such as API calls."*
- **Confirm/Refute oracle:** with a minimal `Describe*`-only principal, dump the zone list and confirm `zoneId` + `parentZoneId` are present (physical topology leaked); confirm no `Condition` can restrict the call.
- **Severity:** Low-Medium (recon / enumeration). The de-randomization output *is the key fact L2 depends on* — so this is also the enabling oracle for L2's cross-account comparison. Note it as an **audit-evasion / recon** primitive, not a direct data breach.

### L6 — Outposts & Wavelength segmentation/management guarantees with no customer-verifiable mechanism  *(Lens V + U)*
- **Claim:** The page asserts strong isolation/management properties — Outpost resources *"communicate using private IP addresses, all within the same VPC"*; *"AWS operates, monitors, and manages this capacity"*; service link is *"an encrypted set of VPN connections"*; Wavelength has *"no inbound connection configuration from the internet."* Each is a *guarantee*; the hunter's job is to find the seam where the mechanism doesn't match.
- **Mechanism (doc evidence):** `what-is-outposts.md`, `how-outposts-works.md` (service link = encrypted VPN; constant Region connectivity required for DNS), `how-wavelengths-work.html` (carrier-gateway NAT; no internet ingress).
- **Confirm/Refute oracle (for a later live/network phase, NOT doc analysis):**
  - *Same-VPC claim:* is there any path by which an Outpost-resident resource reaches, or is reached from, a *different* customer's VPC or the AWS-operated management plane? (Hard-stop if the latter.)
  - *Service-link:* does any Outpost→Region traffic traverse a non-service-link path? Does loss of service link fail **open** for any control operation (DNS, auth)?
  - *Wavelength ingress:* can any inbound path reach a Wavelength subnet other than the documented carrier-gateway NAT?
- **Severity:** potentially High (segmentation) but **doc-gap heavy** — mark "confirm surface first." The *"AWS operates, monitors, and manages"* interface is the **hard-stop service-plane boundary**: if a probe surfaces an AWS-fleet identity/management endpoint on the Outpost, stop and flag for disclosure.
- **Doc-gaps found:** `carrier-gateway.html` and `outposts-local-rack-access.html` both 404 at the expected paths (content folded elsewhere / missing) — physical rack-access and ARN-ownership-check details are **not documented**; the `op-xxxx` ID entropy is unknown. Confirm these before building any L6 hypothesis.

### L7 — Region opt-in lives in `account:*`, not `ec2:*` — cross-service governance seam + STS global-endpoint token quirk  *(Lens U + cross-service)*
- **Claim:** The footprint-expansion lever for **Regions** is governed by a *different* IAM namespace (`account:EnableRegion/DisableRegion/GetRegionOptStatus/ListRegions`) than the one for **Zones** (`ec2:ModifyAvailabilityZoneGroup`). An org that carefully locks down one may leave the other open; and the STS global-endpoint token-validity rule creates a subtle availability/trust dependency on which Regions are enabled.
- **Mechanism:** `manage-acct-regions` doc — four `account:*` permissions control Region enable/disable; *"session tokens from the global AWS STS endpoint are valid **only** in AWS Regions that you enable, or that are enabled by default"*; enabling a Region *"propagates your IAM data and credentials to that Region."* EC2's `DescribeRegions` uses a *different* opt-in enum (`opt-in-not-required|opted-in|not-opted-in`) than `account:GetRegionOptStatus` (`ENABLING|DISABLING|ENABLED|DISABLED`) — don't conflate.
- **Confirm/Refute oracle:** verify a principal with broad `ec2:*` (including `ModifyAvailabilityZoneGroup`) but **no `account:*`** can still expand the Zone footprint while being unable to enable a Region → the two footprint levers have independent, easily-mismatched governance. Separately, confirm global-STS tokens fail in a freshly-enabled opt-in Region until credential propagation — a potential confused availability-vs-security assumption.
- **Severity:** Low-Medium governance/hardening. Primarily a "two doors, one lock" finding plus a cross-service doc clarity gap. Flag for completeness; lower priority than L1/L2/L4.

### Null hypotheses (lenses checked and not fired — pages read)
- **Lens F/G/Q (injection / SSRF / blob parsing):** N/A. Pages read: target page, `how-outposts-works`, `how-wavelengths-work`, `what-is-outposts`. This is concept/control-plane vocabulary; no customer-supplied string is dereferenced, fetched, or parsed server-side on these pages. (Outpost provisioning / ordering flows are a *different* doc set — out of scope for this page.)
- **Lens B (PassRole/confused deputy):** N/A for this page — no role-ARN input among the APIs here. (Outpost *service-linked role* exists but is owned by the Outposts service docs, not this page.)
- **Lens C (credential vending):** only tangential via L7's STS token-validity note; no AssumeRole/session-policy surface defined here.
- **Lens EE (predictable-name land-grab):** `op-xxxx` Outpost-ID entropy is undocumented (doc-gap) — noted under L6, not asserted.

---

## §5 — Prioritization (where NEW/changed surface concentrates)

1. **L2 (AZ-name residency footgun)** — broadest blast radius (whole-org silent control failure), *but* resolve the Nov-2025-consistent-mapping doc-gap first.
2. **L1 (ModifyAvailabilityZoneGroup one-way unscopable opt-in)** — cleanest doc-confirmed control-gap; verify managed-policy inclusion.
3. **L4 (CreateVolume Outpost-ARN asymmetry)** — concrete, doc-confirmed from `list_ec2`; expand to the full action-vs-key asymmetry sweep.
4. **L5 (Describe recon oracles)** — low severity but the enabling oracle for L2; cheap to confirm.
5. **L3 (border-group unscopable)** — hardening; defer to hub cluster 1 context.
6. **L7 (cross-service Region governance)** — governance clarity; completeness.
7. **L6 (Outposts/Wavelength segmentation)** — highest *potential* severity but doc-gap-heavy and needs a network/live phase + the service-plane hard stop; confirm surface before investing.

---

## §6 — Falsifiable-hypothesis leads (handoff for the hunter)

> Each is stated so a hunter with two authorized test accounts in one org can settle it. All read-only / policy-authoring except where noted; **never opt out of a zone group in a shared account without an AWS Support reversal path (L1 is one-way).**

- **H-L1a:** "`ec2:ModifyAvailabilityZoneGroup` honors no condition key." *Test:* attach `Allow` with a bogus `Condition` on the action; call with an arbitrary zone group; success ⇒ unscopable. **Caution: this mutates account state irreversibly — use a disposable test account.**
- **H-L1b:** "The action ships in a common AWS-managed policy." *Test:* grep `AmazonEC2FullAccess` / PowerUser policy JSON for `ModifyAvailabilityZoneGroup`.
- **H-L2:** "`us-east-1a` maps to different `zoneId` across two org accounts." *Test:* `aws ec2 describe-availability-zones --query 'AvailabilityZones[].[ZoneName,ZoneId]'` in each; compare. (Read-only.) *Then:* show an `ec2:AvailabilityZone`-keyed deny authorizes different physical zones vs an `ec2:AvailabilityZoneId`-keyed deny.
- **H-L2-gap:** "New (post-Nov-2025) accounts use consistent AZ-name mapping." *Test:* find a primary AWS source; compare mapping in an account created before vs after. If true, narrow L2's scope.
- **H-L4:** "`CreateVolume` cannot be denied by Outpost ARN but `CreateSnapshot` can." *Test:* author both denies; attempt `create-volume --outpost-arn` (expect allowed despite deny) and a snapshot targeting the Outpost (expect denied). (Mutating — tear down volumes/snapshots.)
- **H-L5:** "A `Describe*`-only principal leaks `zoneId` + `parentZoneId`." *Test:* minimal policy, call, inspect output. (Read-only.)
- **H-L3:** "`AllocateAddress` ignores an `ec2:NetworkBorderGroup` condition." *Test:* author the deny, allocate into a Local-Zone border group, observe success. (Mutating — release the EIP.)
- **H-L7:** "Zone opt-in (ec2) is reachable while Region opt-in (account) is denied under the same principal." *Test:* principal with `ec2:*` minus `account:*`; attempt each footprint lever.

---

## §7 — Doc-gaps & things the next agent must confirm before trusting this plan

- **Nov-2025 "consistent AZ mapping" rumor** — unconfirmed by any primary source as of 2026-10-15; RAM doc still says "random." (Blocks L2 universality.) WebSearch was unavailable to the subagent — re-check whatsnew/press.
- **`carrier-gateway.html` and `outposts-local-rack-access.html` return 404** at expected paths — physical rack access, ARN ownership-check internals, and `op-xxxx` entropy are undocumented. (Blocks L6.)
- **No `ec2:NetworkBorderGroup` / carrier / wavelength condition key** exists anywhere in `list_ec2` — confirmed by grep; re-grep on any `list_ec2` refresh.
- **`API_AvailabilityZone.html` object page** not independently fetched — exact response-field casing for `parentZoneId/Name` taken from filter names + example XML; confirm if precise schema matters.
- Verify every `list_ec2` line reference against the current file on refresh (line numbers drift): `ModifyAvailabilityZoneGroup` (~3654), `DescribeAvailabilityZones` (~1562), `DescribeRegions` (~2198), `CreateVolume` volume row (~5743, no OutpostArn), `CreateSnapshot` (~4999, has OutpostArn), condition-key defs `ec2:AvailabilityZone` (~10057), `ec2:AvailabilityZoneId` (~10058), `ec2:OutpostArn` (~10118), `ec2:Region` (~10138).

## §8 — Cross-references
- **Parent hub:** `ec2-networking-attack-research-plan.md` — EIP cross-account transfer, `AllocateAddress` address-value unscopability, BYOIP, and the AZ-name footgun as a *secondary* lead (promoted here in L2). This plan is the Zones/Regions/Local-Zones/Wavelength/Outposts *concept* child; keep L3/L6 aligned with the hub's IP/EIP cluster.
- **Sibling data points reused:** `capacity-reservation-sharing.md` and `dh-sharing.md` both independently document the AZ-name→ID randomization and the "use the AZ ID for cross-account" rule — strong corroboration for L2 and candidate siblings for their own CR-sharing / DH-sharing plans.
- **Authoritative IAM:** memory `reference-aws-iam-service-auth-ref-url` (use `list_ec2`, not the dead `list_amazonec2`).

---
*Generated by `security-questionbuilder` skill-agent, 2026-10-15. One page, one pass. Net-new/promoted leads only; shared IP/EIP/BYOIP surface deferred to the hub.*
