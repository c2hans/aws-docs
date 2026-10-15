# EC2 Networking — Attack / Research Plan

> **Target hub:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-networking.html`
> (offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-networking.md`)
> **Method:** AWS `security-questionbuilder` — boundary-first threat model. Every item is a
> documentation-derived, **falsifiable** research lead for a hunter to execute later.
> **Nothing in this plan was tested against a live account.** All leads are hypotheses with a
> Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions/Cost/Severity shape.
> **Authoritative IAM ground truth:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`
> (10190 lines) — overrides User-Guide prose on any conflict. Line numbers cited inline.
> **Produced:** 2026-10-15. Opus 4.8 synthesis of four parallel sub-agent deep-dives (Clusters 1–4).

---

## §0 — How to use this plan

This hub plan covers **all 14 child topics** of the EC2 Networking page, grouped into four
analysis clusters. It is net-new territory — no sibling networking plan existed in this repo
before (the existing 36-plan corpus is Fleet/Spot-Fleet only).

- **Read §4 (ranked leads) first.** Leads are ranked by severity across the whole surface; the
  top 5 are the ones worth a hunter's time before anything else.
- Each lead names its **cluster of origin** and the exact `list_ec2.md` line evidence so a hunter
  can re-derive it without re-reading the docs.
- Per-cluster detail (full action inventories, null hypotheses, doc-gaps) lives in the four
  fragment files under `/work/aws-docs/.cache/plans/ec2-net-frag{1,2,3,4}-*.md` — this plan is the
  synthesis; the fragments are the appendices.
- **Scope discipline for the hunter:** documentation-derived hypotheses only. The moment live
  evidence shows an identity / credential / ARN / account belonging to **AWS's own service plane**,
  stop, preserve evidence, flag for AWS-Security disclosure. Several leads below (EFA SRD injection,
  topology co-residency) deliberately stop at a *co-residency confirmation oracle* and treat the
  underlying physical side-channel as out of scope / shared-responsibility.

### Cluster map (14 children → 4 clusters)

| Cluster | Child topics | Fragment |
|---|---|---|
| **1 — IP / EIP / BYOIP** | using-instance-addressing, ec2-byoip, elastic-ip-addresses-eip | `ec2-net-frag1-ip-eip-byoip.md` |
| **2 — ENI / Secondary Networks** | using-eni, secondary-networks | `ec2-net-frag2-eni.md` |
| **3 — Placement / Topology / EFA / Enhanced-net** | placement-groups, ec2-instance-topology, efa, enhanced-networking, ec2-instance-network-bandwidth, network_mtu | `ec2-net-frag3-placement-efa.md` |
| **4 — VPC / Regions-Zones / Hostnames-DNS** | using-regions-availability-zones, ec2-instance-naming, using-vpc | `ec2-net-frag4-vpc-zones-dns.md` |

---

## §1 — Pentest objectives

1. **Cross-account IP hijack** — can an EIP (or BYOIP range) move to, or be reclaimed by, an
   account other than the one the owner intended? (Cluster 1)
2. **Cross-account ENI control** — can a cross-account ENI grant be over-revoked, or an ENI be
   attached across a VPC boundary the operator believed IAM confined? (Cluster 2)
3. **Cross-tenant fabric reach** — can EFA/SRD OS-bypass traffic or a Secondary-Network fabric
   cross the account/VPC boundary the docs assert it cannot? (Clusters 2, 3)
4. **Co-residency / placement recon** — can an unprivileged principal determine the physical host
   placement of its own or (worse) another account's instances? (Cluster 3)
5. **IAM scoping gaps** — enumerate every networking action that **cannot** be scoped (no resource
   type, or a missing condition key) and show the least-privilege design it silently defeats.
   (All clusters — this is the dominant theme.)
6. **Documented-guarantee vs enforcement** — every "only / cannot / is isolated" sentence traced to
   the mechanism that enforces it, flagging the ones that are asserted but never mechanized.

---

## §2 — Components, Assets, and Design

### Customer-facing interface
EC2 networking is a **SigV4 IAM control-plane API** (plus console + SDK). No separate wire protocol,
no proxy fleet, no multi-tenant translation layer in the DocumentDB/CloudShell sense — the "data
plane" here is the actual IP/ENI/RDMA fabric, and the trust boundaries are *network-layer and
account-layer*, not a shared service fleet. That shifts the highest-value findings from
"cross-tenant on a shared host service" toward **IAM-scoping gaps** and **asserted-but-unmechanized
network isolation guarantees**.

### Assets and identifier shapes

| Asset | ID / ARN shape | Ownership binding | Guessability |
|---|---|---|---|
| Elastic IP | `elastic-ip/${AllocationId}`, `eipalloc-{17hex}` | one account "until you release it" | AllocationId opaque; **the public IPv4 itself is the discriminator and is NOT secret** (scannable, DNS-indexable) |
| Public IPv4 (auto) | bare dotted-quad, no ARN | pool-owned, not account-owned | non-reclaimable once released |
| BYOIP CIDR / pool | `ipv4pool-ec2-{hex}`; **CIDR has no IAM resource type at all** | account+region only | unscopable in IAM |
| ENI | `eni-{17hex}` | one subnet/AZ/VPC for life | opaque |
| ENI attachment | `eni-attach-{17hex}` | **no IAM ARN resource type** | — |
| ENI permission (cross-acct grant) | no own ARN; addressed via parent `network-interface` | `AuthorizedUser`/`AuthorizedService` + `Permission` | — |
| Secondary Network / Subnet | `sn-{id}` / `ss-{id}` | regional, VPC-separate | — |
| Placement group | `placement-group/${PlacementGroupName}` (name, **not opaque id**) | `${Account}` segment in ARN = owner | **name is caller-chosen → predictable** |
| Network node (topology) | opaque `nn-...` string | "view unique per account" (ambiguous) | — |
| AZ | `ZoneName` (`us-east-1a`) vs `ZoneId` (`use1-az1`); **no `availability-zone` ARN resource type** | ZoneName per-account-randomized in 9 Regions pre-Nov-2025; ZoneId cross-account-consistent | — |
| Private/public DNS hostname | `ip-10-x-x-x.<region>.compute.internal`, `i-{id}.<region>.compute.internal`, `ec2-<ip>...amazonaws.com` | VPC-scoped resolution | **fully derivable from IP / instance-id** |

### Connection / trust-zone diagram (docs-implied)

```
   ┌─────────────────────────── Customer AWS account ───────────────────────────┐
   │                                                                             │
   │   SigV4 IAM principal ──► EC2 control-plane API (RunInstances, Allocate-    │
   │        │                   Address, CreateNetworkInterface*, Create-        │
   │        │                   PlacementGroup, DescribeInstanceTopology, …)     │
   │        │                                                                     │
   │        ▼                                                                     │
   │   ┌─────────── VPC ───────────┐      ┌──── Secondary Network ────┐          │
   │   │ subnet / primary ENI /    │      │ (NO SG / NO NACL /         │          │
   │   │ secondary ENI / EIP /     │      │  NO Flow Logs — isolation  │          │
   │   │ public IPv4 / SG / NACL   │      │  asserted, not mechanized) │          │
   │   └───────────┬───────────────┘      └────────────┬──────────────┘          │
   │               │ EFA / SRD OS-bypass (SG self-all-traffic; NOT filtered      │
   │               │ like ENA/IP — enforcement layer unnamed)                    │
   └───────────────┼──────────────────────────────────┼─────────────────────────┘
                   │                                   │
       ┌───────────▼───────────────┐       ┌───────────▼──────────────────┐
       │ Shared physical fabric /  │       │ Cross-account seams:          │
       │ network node (nn-...)     │       │  • EIP transfer (no dest-acct │
       │  — Cluster PG can co-     │       │    condition key)             │
       │    locate 2 accounts on   │       │  • ENI permission grant       │
       │    the SAME hardware by   │       │  • Placement-group RAM share  │
       │    design                 │       │  • BYOIP advertise (region-   │
       └───────────────────────────┘       │    wide, unscopable)          │
                                           └───────────────────────────────┘
                   ▲
                   │  Cross-account correlation oracles (documented, non-exploit):
                   │   ZoneId consistency · DescribeInstanceTopology nn-id match
                   └──────────────────────────────────────────────────────────
```

---

## §3 — Trust-boundary map (synthesized, breach-oracle column is the point)

| # | From | To | Crossing (API) | Breach oracle | Cluster |
|---|---|---|---|---|---|
| B1 | EIP owner (acct S) | account other than `--transfer-account-id` | `EnableAddressTransfer`→`AcceptAddressTransfer` | an account **not** named in the transfer accepts it → dest-acct restriction is UI convention, not server-side authz | 1 |
| B2 | principal with any BYOIP lifecycle action | the account's **entire** region-wide BYOIP inventory | `Advertise/Withdraw/Deprovision ByoipCidr` (no resource type) | principal acts on a CIDR it never provisioned → BYOIP is IAM-unscopable | 1 |
| B3 | previous EIP owner's stale external refs | next allocating account | `ReleaseAddress`→`AllocateAddress --address` | a *different* account reclaims the exact released IP → IP-squatting | 1 |
| B4 | principal scoped to one EIP via `ec2:AllocationId` | any instance/ENI in account | `AssociateAddress` (3 unstarred resource blocks) | scoped EIP associates to an unintended instance → cross-dimension policy trap | 1 |
| B5 | principal with scoped-create ENI permission | grants it did not create | `DeleteNetworkInterfacePermission` (no `AuthorizedUser`/`Permission` key) | principal revokes a grant to a different account/permission-type → over-broad revoke | 2 |
| B6 | instance in VPC X | ENI in VPC Y, same acct/AZ | `AttachNetworkInterface` (`instance*` has no `ec2:Vpc`) | cross-VPC attach that IAM could not have blocked → segmentation is product behavior, not IAM | 2 |
| B7 | customer principal | AWS-service requester-managed ENI | `ResetNetworkInterfaceAttribute` (no `ec2:Attribute` key; Reset allowed where Modify blocked) | Reset mutates service-owned ENI state → "you can't manage this" holds for Modify only | 2 |
| B8 | principal with `Describe*NetworkInterface*` | every ENI / every cross-acct grant | Describe (no resource type, `ec2:Region` only) | tag-scoped view-only design is unachievable → account-wide topology/ownership disclosure | 2 |
| B9 | VPC data plane | Secondary-Network east-west fabric | multi-homing via `--secondary-interfaces` | traffic crosses between Secondary Networks / into VPC despite "cannot communicate" claim (only a DHCP static route backs it) | 2 |
| B10 | tenant A EFA endpoint | tenant B EFA endpoint, diff acct/VPC, same AZ/node | SRD/RDMA OS-bypass send | frame received across acct/VPC → EFA isolation enforced at wrong layer | 3 |
| B11 | acct A (bare `DescribeInstanceTopology`) | acct B via shared Cluster PG, or unrelated acct via `nn-id` compare | `DescribeInstanceTopology` (no resource type) | identical `nn-...` node ID across accounts → shared global ID space, co-residency oracle | 3 |
| B12 | principal scoped via `ec2:Attribute` on `ModifyInstanceAttribute` | same attribute via `ResetInstanceAttribute` | `ResetInstanceAttribute` (no `ec2:Attribute` key) | attribute-scoped restriction bypassed via the reset twin | 3 |
| B13 | principal allow-listed to 3 PG strategies | precision-time PG | `CreatePlacementGroup --strategy precision-time` | policy written against documented 3-value enum silently permits/denies the undocumented 4th | 3 |
| B14 | shared-VPC participant acct | VPC-owner instance in shared subnet | `Describe/Stop/Terminate Instances` | participant acts on owner's instance (or reverse, or tunnels owner's EICE) → RAM isolation break | 4 |
| B15 | acct A | acct B, Org SCP on `ec2:AvailabilityZone` | AZ **name** used as physical-location proxy | same `ZoneName`→different `ZoneId` across accounts → name-based residency control is non-physical | 4 |
| B16 | customer VPC internal resolver | another tenant's instance | DNS query for `ip-…/i-….compute.internal` | resolver answers a record from a different VPC/account w/o a Resolver rule → cross-VPC DNS leak | 4 |
| HARD-STOP | any customer surface | **AWS's own service plane** | any | any AWS-fleet identity/credential/ARN/account observed → stop, preserve, disclose | all |

---

## §4 — Ranked leads (fire these first)

### [1] HIGH/CRITICAL — EIP cross-account transfer may not server-side-enforce the destination account *(Cluster 1, Lens AA)*

> **Claim:** The EIP transfer handshake may not actually enforce that only the account named in
> `--transfer-account-id` can accept; the restriction may be UI/CLI convention, not server-side authz
> tied to caller identity.
> **Mechanism:** `EnableAddressTransfer` (list_ec2.md L8005-8009) and `AcceptAddressTransfer`
> (L4608-4612) condition-key sets contain **no destination/transfer-account key anywhere in the
> 10190-line file**. UserGuide: "AWS does not notify transfer accounts… The owner of the source
> account must notify the owner of the transfer account" — the only thing stopping an uninvited
> account is not knowing the (non-secret) public IP.
> **Confirm/Refute oracle:** 3 accounts. S enables transfer naming T. From C (neither S nor T, with
> `ec2:AcceptAddressTransfer` on `Resource:"*"`), call `accept-address-transfer --address <ip>`.
> Success = boundary does not hold.
> **Preconditions/Cost/Severity:** 3 accounts; attacker learns the public IP during the 7-day
> pending window (scannable/DNS/log-leaked); ~zero cost. **High/Critical** — direct account-boundary
> IP hijack (DNS/cert takeover, interception).

### [2] HIGH — `DeleteNetworkInterfacePermission` cannot be scoped by who/what, while the create twin can *(Cluster 2, Lens AA/S)*

> **Claim:** A principal scoped to only *grant* cross-account ENI access to one account/permission-type
> can still *revoke any grant* on that ENI, including grants others made to other accounts.
> **Mechanism:** `CreateNetworkInterfacePermission` (L5364-5370) carries `ec2:AuthorizedUser`,
> `ec2:AuthorizedService`, `ec2:Permission`; `DeleteNetworkInterfacePermission` (L6094-6102) has
> **none of the three**, and its `network-interface` resource type is **not even `*required`**.
> **Confirm/Refute oracle:** Policy = scoped-create (via `ec2:AuthorizedUser`) + unscoped-delete on
> one `eni-*`. Have a second grant (to account B) made by a more-privileged principal. Confirm the
> first principal can delete account B's grant.
> **Preconditions/Cost/Severity:** two principals managing grants on one ENI; 2 policies + 1 ENI.
> **High** — silent over-broad revoke, no signal distinguishing own-grant from others'-grant revoke.
> **Note:** this capability is **entirely absent from the UserGuide** — only in the API ref /
> list_ec2.md (see §7 doc-gap).

### [3] HIGH/CRITICAL — EFA / SRD OS-bypass cross-tenant frame injection *(Cluster 3, Lens D/V)*

> **Claim:** EFA's "traffic can't cross AZs or VPCs" / "is not routable" may be enforced at a layer
> the OS-bypass path doesn't traverse. If so, a crafted SRD/RDMA frame from one tenant could reach a
> different-account EFA endpoint on the same physical fabric segment.
> **Mechanism:** efa.md concedes EFA traffic is a *distinct path* from the ENA/IP path ("This does
> not apply to normal IP traffic from the ENA device"); create-efa.md requires the EFA SG to allow
> **all** inbound/outbound to itself — i.e. OS-bypass traffic is not SG-filtered like IP traffic. The
> doc never names which layer performs the AZ/VPC check.
> **Confirm/Refute oracle:** two EFA instances in different accounts/VPCs, same AZ, ideally same
> shared Cluster PG (→ same `nn-` node). SRD send from one Libfabric endpoint to the other's EFA
> address. Received/acked across the boundary = **confirmed broken**; dropped / unaddressable =
> refuted (and that is a reportable "isolation verified" result).
> **Preconditions/Cost/Severity:** 2 accounts, Nitro v3+ EFA instances, same AZ. **Critical** if
> true — cross-tenant RDMA memory disclosure/injection bypassing the whole VPC model. The physical
> side-channel itself is out of scope; stop at the frame-reachability oracle.

### [4] MEDIUM-HIGH — BYOIP lifecycle actions are IAM-unscopable to a CIDR *(Cluster 1, Lens S/U)*

> **Claim:** IAM cannot restrict a principal to a *specific* BYOIP CIDR/pool — any principal granted
> the action acts on every BYOIP CIDR in the account+region.
> **Mechanism:** `ProvisionByoipCidr` (L9257), `AdvertiseByoipCidr` (L4662), `WithdrawByoipCidr`
> (L9756), `DeprovisionByoipCidr` (L6510) each have **no "Resource types" line** — only `ec2:Region`.
> No per-CIDR key exists in the condition-key table (L10040-10189).
> **Confirm/Refute oracle:** 2 BYOIP CIDRs (X,Y) in one account; policy granting only
> `WithdrawByoipCidr`/`AdvertiseByoipCidr` on `Resource:"*"` (the only possible form). Confirm it
> touches both X and Y.
> **Preconditions/Cost/Severity:** BYOIP is slow/expensive to provision — validate by careful reading
> or in an account already holding 2+ ranges. **Medium-High** — least-privilege BYOIP delegation is
> structurally impossible; a compromised low-trust principal can `WithdrawByoipCidr` every advertised
> range (10 s apart, byoip-onboard.md rate limit), **uncancellable mid-flight** → region-wide
> black-hole.

### [5] HIGH (if broken) — Shared-VPC owner/participant instance isolation *(Cluster 4, Lens A)*

> **Claim:** The owner/participant isolation in a shared VPC subnet might not hold — a participant may
> `Describe/Stop/Terminate` an owner-created instance ID (or reverse), or use the owner's EC2 Instance
> Connect Endpoint.
> **Mechanism:** using-vpc.md "Shared subnets": "Participants can't start, stop, terminate, or
> describe instances that the VPC owner created… VPC owners can't… instances created by
> participants… Participants can't use an EC2 Instance Connect Endpoint that the VPC owner created."
> Four asserted restrictions = four falsifiable oracles.
> **Confirm/Refute oracle:** from a participant principal, `DescribeInstances`/`StopInstances` an
> owner-created instance ID in the shared subnet (and reverse); attempt EICE tunnel through owner's
> endpoint. Any success = breach.
> **Preconditions/Cost/Severity:** 2 accounts, 1 RAM share, 1 instance each. Test with Describe first
> (non-destructive). **Critical if broken** — cross-account resource control on a core RAM feature.
> Per docs read alone this is an **unbroken (null) claim** — listed high because the oracle is clean
> and the blast radius is large.

---

## §5 — Secondary leads (worth time after the top 5)

- **[M] Released-EIP reclaim-by-address squatting** *(C1, Lens EE)* — `AllocateAddress` has **no
  `ec2:PublicIpAddress` key** (L4668-4673); recovery-by-address appears unrestricted to the original
  owner ("can't recover if… allocated to another AWS account" implies a race). Oracle: acct A
  release P; acct B `allocate-address --address P` at 1s/10s/60s/1h. Severity scales with victim's
  stale DNS/firewall/OAuth-callback references.
- **[M] AssociateAddress cross-dimension policy trap** *(C1, Lens A)* — 3 unstarred resource blocks
  (L4712-4717); a policy "locking" a principal to one EIP via `ec2:AllocationId` does not constrain
  which instance/ENI it attaches to. Guardrail-gap in guidance (UserGuide never warns of this).
- **[MH] `ResetNetworkInterfaceAttribute` on requester-managed ENIs** *(C2, Lens U)* — Reset allowed
  where Modify blocked (requester-managed-eni.md), and Reset has **no `ec2:Attribute` key** (L9519).
  Oracle: Reset `SourceDestCheck`/`Groups` on a NAT-GW/ELB ENI; behavior change = guarantee holds
  for Modify only.
- **[M] `Describe*NetworkInterface*` zero resource scoping** *(C2, Lens A/O)* — L7218/L7212 have no
  resource type; tag-scoped view-only ENI visibility is unachievable. Same shape for
  `DescribeSecondaryInterfaces/Networks/Subnets` (L7326-7345) and `DescribeNetworkInterfacePermissions`
  (discloses every cross-account grant).
- **[MH] Secondary-Network isolation asserted, not mechanized** *(C2, Lens V/D)* — no SG/NACL/Flow
  Logs (secondary-networks.md L55); "instances cannot communicate across different Secondary
  Networks" (L208) backed only by a DHCP-vended static route (L235 = routing, not access control).
  Oracle: reach a Secondary Interface's address space from a different Secondary Network / plain VPC
  instance with custom routes. Capacity-reservation-gated (nontrivial cost).
- **[M] `DescribeInstanceTopology` co-residency oracle** *(C3, Lens A/V)* — "view unique per account"
  (L6978, no resource type, `ec2:Region` only) is ambiguous: per-account relabel vs filtered shared
  ID space. Oracle: two accounts (same AZ/type, ideally shared Cluster PG) compare `nn-...` strings;
  a match = shared global space = cross-account placement recon. Stop at the oracle — physical
  side-channel out of scope.
- **[LM] `ResetInstanceAttribute` vs `ModifyInstanceAttribute` key asymmetry** *(C3, Lens R/S)* —
  `ec2:Attribute`/`ec2:Attribute/${AttributeName}`/`ec2:PlacementGroup` on Modify (L8806) but
  **absent on Reset** (L9513). Oracle: `iam:SimulatePrincipalPolicy` — no live mutation. **Also
  confirm the Reset parameter enum even includes `sriovNetSupport`/`enaSupport`/`disableApiTermination`
  via the EC2 API ref** (if not, moot for those attributes).
- **[LM] AZ-name vs AZ-ID residency-control footgun** *(C4, Lens U)* — Org SCP on
  `ec2:AvailabilityZone` (name) does **not** pin physical zone: name↔ID is per-account-randomized in
  9 Regions for pre-Nov-2025 accounts (az-ids.md). Oracle: two accounts `describe-availability-zones`,
  same `ZoneName`→different `ZoneId`. Fix is `ec2:AvailabilityZoneId`; neither doc cross-links it →
  the enabling doc-gap. Medium (compliance control gap).
- **[LM] PTR reverse-DNS lock as griefing/DoS** *(C1, Lens U)* — a PTR record locks an EIP against
  release and transfer-accept (Using_Elastic_Addressing_Reverse_DNS.md L12). If
  `ec2:ModifyAddressAttribute` is grantable independently of release/transfer, a low-privilege
  principal can lock a shared EIP; Support-assisted PTR extends the DoS to a ticket SLA.
- **[L] Secondary-Network quota squatting** *(C2, Lens L)* — 5 networks/region, no CIDR/count
  condition key on `CreateSecondaryNetwork`; one principal exhausts the shared ceiling.
- **[L] Prefix-assignment TOCTOU** *(C2, Lens P)* — "AWS verifies the prefix is not already
  assigned" (ec2-prefix-eni.md) is a runtime check; `AssignPrivateIpAddresses` has no IP-value key →
  test concurrent overlapping assignments.
- **[L] Spread-PG "distinct hardware" temporal scope** *(C3, Lens U)* — stated at placement time;
  silent on live-migration/maintenance drift. Oracle: long-window `nn-id` convergence check.
- **[L] Precision-time strategy absent from `ec2:PlacementGroupStrategy` description** *(C3, Lens U)*
  — key defn (L10133) names only cluster/spread/partition; a strategy allow-list policy may silently
  mis-handle `precision-time`. Oracle: `iam:SimulatePrincipalPolicy`.
- **[L] `sriovNetSupport` irreversibility / internal doc contradiction** *(C3, Lens E/B)* —
  sriov-networking.md says "no way to disable," then shows `--sriov-net-support simple`. API-ref
  cross-check, doc-only.
- **[Info] EC2-Classic dead rows in `RunInstances`** *(C4, Lens N)* — stale policy-language artifacts
  with empty condition keys; documentation-hygiene, not a live surface.

---

## §6 — Threat-model test objectives (grouped by what a hunter sets up)

- **Multi-account IP / grant tests (needs 3 accounts):** Leads [1] EIP transfer, [2] ENI permission
  over-revoke, [5] shared-VPC isolation, B3 EIP squatting.
- **EFA / topology fabric tests (needs EFA instances, same AZ, shared Cluster PG):** Lead [3] SRD
  injection, [M] topology co-residency oracle, [L] Spread-PG drift. These share a setup — provision
  once, run all three.
- **IAM-simulator-only (zero live resources):** `ResetInstanceAttribute` asymmetry, precision-time
  strategy enum, AZ-name/ID residency control, cross-dimension AssociateAddress trap. Cheapest wins —
  do these first to triage before standing up accounts.
- **Single-account live tests:** PTR lock, Secondary-Network quota/isolation, prefix TOCTOU,
  requester-managed-ENI Reset.
- **Doc-only API-reference cross-checks:** `sriovNetSupport` contradiction, BYOIP post-provision
  re-validation cadence, `ec2:Permission`/`DescribePublicIpv4Pools` block confirmation.

---

## §7 — Doc-gaps, drift, and carried unknowns

- **Cross-account ENI sharing is undocumented in the UserGuide entirely.** `CreateNetworkInterface-
  Permission` / `Delete…` / `Describe…` appear only in the API ref / list_ec2.md — never in
  using-eni.md or any of its 10 children. The HIGH Lead [2] lives outside the UserGuide's mental
  model, so an operator following only the Topics trail never learns the capability exists.
- **`AttachResourcesToPlacementGroup` / `DetachResourcesFromPlacementGroup`** exist in list_ec2.md
  (L9779/L9846) with full key sets but appear in **no** UserGuide page read; their doc links are
  path-truncated (`…/UserGuide/placement-groups.html`, missing `AWSEC2/latest/`). Resolve by reading
  `cr-cpg.md` (Capacity Reservations in Cluster PGs) + the EC2 API ref.
- **`ec2:PlacementGroupStrategy` enumerates only 3 of 4 strategies** (L10133 omits precision-time) —
  feeds Lead B13.
- **`ec2:Permission` (INSTANCE-ATTACH / EIP-ASSOCIATE)** confirmed in the key table (L10040-10189)
  but not attached to any of the 19 Cluster-1 actions — grep the full action list to find which
  action(s) use it (likely `CreateNetworkInterfacePermission`); carried from C1 Lead 6.
- **Secondary-Network isolation enforcement layer is never named** (only a DHCP static route hints at
  it) — resolve before the expensive RDMA-reachability test.
- **BYOIP post-provision re-validation cadence** — no page states whether AWS re-checks the ROA/RDAP
  record after initial provision; relevant to how long a revoked ROA keeps a CIDR advertisable.
  Doc-only gap, not testable without RIR cooperation.
- **`DescribePublicIpv4Pools`** resource/condition block not line-verified (pattern suggests List +
  `ec2:Region`); confirm before relying.
- **`ec2:ManagedResourceOperator` / `ModifyAddressAttribute` / `ResetAddressAttribute`** condition
  blocks not pulled this pass — fetch before a hunter relies on them (feeds PTR-lock and
  requester-managed-ENI leads).
- **Online/offline drift:** **none security-relevant** across all four clusters. Spot-checked live
  `.md` twins: using-eni, secondary-networks (byte-identical); using-vpc, using-regions-availability-
  zones, ec2-instance-naming (identical); transfer-EIPs-intro, ec2-byoip, byoip-onboard (identical);
  ec2-instance-topology, efa (identical prose — efa.md online has **newer silicon tables**, a
  corpus-staleness note for `/work/aws-docs` maintainers, not a finding). Six C1 and four C3 pages
  were not individually drift-checked — flagged for a follow-up pass before treating any
  absence-based claim as final.
- **Not read (follow-up):** `cr-cpg.md` (first priority — Attach/Detach-to-PG gap), EFA sub-pages
  (`detach-efa`, `efa-verify`, `efa-acc-inst-types`), Local-Zones / Wavelength User Guides (for Lens-V
  SG-parity gap), VPC-service "Share your VPC" page (for Lens-AA unshare behavior).

---

## §8 — Out-of-scope / null hypotheses (named so the next agent doesn't re-chase them)

**Hard out of scope:** anything touching AWS's own service plane (hard-stop + disclose); live
exploitation of any confirmed boundary beyond the minimum existence PoC; physical/hypervisor
side-channels (topology & EFA leads stop at the *co-residency confirmation oracle*).

**Null hypotheses (lens → why N/A, pages named in fragments):**

- **B/C confused deputy / PassRole** — no action in any cluster accepts a role ARN or acts on the
  caller's behalf; EIP/ENI/PG/VPC calls are direct SigV4. (Not ruled out for NAT-GW/ELB-managed EIPs,
  out of scope here.)
- **C credential vending / session scope** — no STS/session-policy/ProvidedContext mechanism anywhere.
- **F translation-layer / wire injection** — no parser/translator between customer input and a
  downstream call; inputs are structured API params.
- **G SSRF / dereferenced field** — no field (Description, tags, CIDR, hostname) is fetched/rendered
  server-side; DNS names *resolve* (standard DNS), not a service HTTP fetch.
- **I injection / O outbound** — no free-text rendered as code; BYOIP's RIR calls are AWS-internal,
  not customer-URL-driven.
- **N naming-authority spoofing** — BYOIP X.509/RDAP/ROA chain is designed to prevent exactly this
  (only post-provision re-validation cadence is an open gap).
- **Q blob upload / T secret reachability** — no upload surface, no secret created/persisted by any
  networking action.
- **R sample-IAM-policy audit** — no policy JSON/managed policy/SLR printed on any networking
  UserGuide page (contrast other service clusters).
- **L exhaustion (bandwidth burst, MTU/PMTUD blackhole)** — AWS self-discloses burst as best-effort
  shared (no isolation guarantee to falsify) and PMTUD-ICMP blackhole as a customer-NACL
  misconfiguration (not AWS-side).
- **X legacy twins** — EC2-Classic rows are dead; legacy Intel-82599 SR-IOV shares
  `ModifyInstanceAttribute` with ENA (no distinct surface beyond Lead [L] sriov).
- **M shared-identifier** — `eni-*` reused for customer/requester-managed/managed ENIs, distinguished
  by boolean fields; weak candidate, deferred pending a Describe-response schema check (out of scope
  for doc-only pass).
- **EE predictable private DNS hostnames** — resolution is explicitly VPC-scoped (hostname-types.md),
  so **refuted by the docs themselves**; only the narrow cross-VPC-extension question (one VPC
  spanning an AZ + Outpost/Local/Wavelength edge) stays open and needs those out-of-cluster guides.
- **ZoneId cross-account consistency as a "finding"** — it is a **published, intentional** capability
  (az-ids.md tells customers to use it to compare physical location across accounts); flagged so a
  hunter does not mistake it for a bug — it is the *mechanism* behind the topology co-residency oracle,
  not a vuln itself.

---

*Appendices (full action inventories, every null hypothesis with pages checked, per-cluster
doc-gaps): `/work/aws-docs/.cache/plans/ec2-net-frag{1,2,3,4}-*.md`.*
