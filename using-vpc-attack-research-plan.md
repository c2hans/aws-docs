# Virtual Private Clouds for your EC2 instances — Attack / Research Plan

> **Target:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.html
> **Offline mirror:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/using-vpc.md`
> **IAM ground truth:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (10,190 lines) + `list_ec2-instance-connect.md` (85 lines)
> **Parity:** online `.html.md` == offline, **byte-identical, verified 2026-10-15** for `using-vpc`, `vpc-share-limitations`, `default-security-group`.
> **Method:** `security-questionbuilder` (6-step boundary-first). Severity rubric: cross-**account** data access = Critical; cross-tenant on shared fleet = High; AWS-authored artifact defects = in-scope Tier-2; customer-authored footguns = out of scope.
> **Role in the corpus:** This is the **authoritative page-level plan for the shared-VPC owner/participant isolation model** — the `ec2-networking` hub's lead #5. Multiple sibling plans (`create-network-interface` A2, `working-with-ip-addresses` A3, `using-instance-addressing`, `config-windows-multiple-ip`) **defer** shared-VPC isolation here. Cross-reference those siblings; do not restate them.

---

## §0 — How to use this document

This is a research plan, not a findings report. Each lens in §5 states a **falsifiable claim**, the **doc evidence** that makes it plausible, a **confirm/refute oracle**, and **severity-if-true**. A downstream hunter executes these against an authorized two-account Org (VPC owner + participant), using synthetic/canary data only, and **stops at the first observation that reaches AWS's own service plane**. Everything here is derived from documentation only; no live system was touched to produce it.

**The one move, applied here:** the `using-vpc.html` page makes a chain of *isolation promises* about who can touch what in a shared subnet, a default-VPC *internet-reachability* posture, and an IPv6-only *instance-class constraint*. For each promise, we ask: **is it enforced by a mechanism a customer can see/scope in IAM, or only by an invisible server-side account filter — and does the enforcement actually hold at the seam where one account's request crosses into a subnet owned by another account?**

---

## §1 — Objectives

1. Determine whether the four "Shared subnets" isolation claims (instance start/stop/terminate/describe symmetry; ENI ownership; EICE non-use) are backed by any **customer-expressible IAM control**, or only by implicit cross-account ARN scoping that the customer cannot tighten, audit, or reason about.
2. Probe the **owner↔participant seam** for any asymmetry, naming trick, or RAM-lifecycle gap that lets one party reach the other's instances/ENIs/EICE/flow-logs/routing.
3. Characterize the **default-VPC internet-by-default posture** as a shipped-insecure-default (AWS-authored) and establish its exact blast radius (what is actually reachable vs. what the default SG blocks).
4. Confirm the **IPv6-only Nitro requirement** is a server-side launch gate with no IAM key, and tie it to the known "IPv6 public-by-default, no IAM opt-out" finding.
5. Hand the hunter a prioritized, oracle-equipped lead list that another agent can execute cold.

---

## §2 — Components, Assets, and Design

### Actors / ownership zones
- **VPC owner account** — owns the VPC, subnets, route tables, NACLs, internet/NAT/egress-only gateways, the VPC default security group, and any EICE *it* creates. Shares specific **subnets** (never whole VPCs, never default-VPC subnets) to participants via **AWS RAM**, constrained to the **same AWS Organization**.
- **Participant account(s)** — launch instances / create ENIs / create their own EICE *inside* the owner's shared subnet. Own only the resources they create. Live in a **different AWS account** than the owner.
- **AWS EC2 control plane** — enforces the account-boundary filtering that makes the "can't describe/start/stop the other party's instances" promises true (there is no customer-visible mechanism). **Hard stop:** any identity/ARN/credential belonging to AWS's own fleet is out of scope — preserve evidence and flag.

### Assets
- Instances, ENIs, EICE endpoints (each ARN-scoped to its *creator's* account, even when living in the owner's subnet).
- The shared **subnet** resource (ARN account segment = **owner**, not participant — RAM delegates use, not ownership).
- Routing/NACL/gateway control (wholly owner-controlled).
- Flow logs (each party logs only ENIs it owns; owner can additionally log the whole subnet).
- Default-VPC auto-config: `MapPublicIpOnLaunch=true`, DNS hostnames on, `0.0.0.0/0 → igw` main route.

### Identifier shapes
- `subnet-…`, `i-…`, `eni-…`, `eice-…` — opaque, 17-hex-char. The subnet ID is **shared knowledge** (participant must specify it to launch), so the participant *legitimately holds* an identifier for a resource in the owner's account — the classic Lens-A precondition.

### Connection diagram
```
          AWS RAM share (same-Org ONLY)
Owner acct  ───────────────────────────▶  Participant acct
  │  owns: VPC, subnet(ARN=owner), RT, NACL, IGW/NAT/EIGW,       │
  │        default SG, owner-created instances/ENIs/EICE         │
  │                                                              │
  └── shared subnet ───────────────────────────────────────────┘
        │                                   │
   owner launches here              participant launches here
   (instance ARN=owner)             (instance ARN=participant,
                                     ENI ARN=participant, EICE ARN=participant)
        │                                   │
        └──── EC2 control plane: account-boundary filter ────┘
             (the ONLY thing enforcing the 4 isolation claims)
```

---

## §3 — Trust-boundary map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Participant | Owner-created instance in shared subnet | RunInstances/Start/Stop/Terminate/DescribeInstances w/ a known `i-…` | Participant **describes, starts, stops, or terminates** an instance whose ARN is in the owner's account → isolation claim #2 broken |
| Owner | Participant-created instance in shared subnet | same | Owner performs any of the 4 ops on a participant-owned `i-…` → claim #3 broken |
| Participant | Owner-created ENI in shared subnet | Attach/Detach/Modify/Delete w/ known `eni-…` | Participant attaches/detaches/modifies/deletes an owner ENI → "cannot work with" broken |
| Participant | Owner-created EICE | `ec2-instance-connect:OpenTunnel` on owner `eice-…` | Participant opens a tunnel through the **owner's** EICE → claim #4 broken (**reaches instances via a cross-account endpoint**) |
| Participant | Owner routing/NACL/gateways | Create/Modify/Delete/Associate RT/NACL/IGW/NAT | Participant mutates owner-controlled routing → "only the VPC owner can" broken |
| Owner | Participant flow logs | Describe/Delete flow logs on participant ENIs | Owner reads/deletes a participant's flow logs → "cannot describe or delete" broken |
| Participant | Owner default SG | RunInstances specifying owner's default SG id | Launch succeeds using the owner's default SG → "can't launch using the default SG" broken |
| Internet | Default-subnet instance | Auto-assigned public IPv4 + `0.0.0.0/0`→igw route | Instance is internet-reachable the moment it launches, with no explicit opt-in → shipped-insecure-default blast radius |
| Any customer | **AWS EC2 service plane** | — | **HARD STOP** — any AWS-fleet identity/ARN/credential; preserve + flag. |

---

## §4 — API / interface inventory

| Name | Mut? | Ext? | Resource row (list_ec2.md) | Condition keys that matter | Scopable to ownership? |
|---|---|---|---|---|---|
| `RunInstances` | Y | Y | `instance*` L9591, `network-interface*` L9595, `subnet*` L9602 | `ec2:Subnet`, `ec2:Vpc`, `ec2:SubnetID` (static ARN **allowlist** only), tags | **No** — no "do I own this subnet/ENI" key |
| `StartInstances` | Y | Y | `instance*` L9650 | `aws:ResourceTag`, `ec2:InstanceID`, `ec2:ResourceTag`, instance-attribute keys | **No** — no subnet/vpc/creator key |
| `StopInstances` | Y | Y | `instance*` L9674–5 | same family | **No** |
| `TerminateInstances` | Y | Y | `instance*` L9686–7 | same family (+`ec2:ProductCode`) | **No** |
| `DescribeInstances` | N | Y | **none** L6996–7000 | **only `ec2:Region`** | **Unscopable** — no resource type at all; List-level |
| `CreateInstanceConnectEndpoint` | Y | Y | `instance-connect-endpoint*` L5155–7 | `ec2:SubnetID` (allowlist), `aws:RequestTag` | **No** — allowlists subnet, not owner |
| `DeleteInstanceConnectEndpoint` | Y | Y | `instance-connect-endpoint*` L5908–10 | base only | **No** |
| `ec2-instance-connect:OpenTunnel` | Y | Y | `instance-connect-endpoint*` L44–48 (ic file) | `*:remotePort`, `*:privateIpAddress`, `*:MaxTunnelDuration`, tags | **No endpoint-ownership key** — only tunnel params/tags |
| `ec2-instance-connect:SendSSHPublicKey` | Y | Y | `instance*` L50–54 (ic file) | `ec2:osuser`, `aws:ResourceTag` | partial (osuser) |
| `CreateDefaultVpc` / `CreateDefaultSubnet` | Y | Y | (hub-frag) | `ec2:Region` only | **Unscopable** |
| `ModifySubnetAttribute` (MapPublicIpOnLaunch) | Y | Y | `subnet*` | no value-level key for the auto-public-IP toggle | **No** |

**Zero org/account-scoping keys exist anywhere in `list_ec2.md`:** `aws:PrincipalOrgID`, `aws:ResourceOrgID`, `aws:PrincipalAccount`, `ec2:AccountId`, `ec2:ResourceAccount`, `aws:PrincipalOrgPaths` → **0 hits each** (confirmed, matches corpus-wide finding). The only "owner" key is `ec2:Owner` (L10119), used **only** on AMI/snapshot/FPGA-image provenance — **never** on `instance`/`network-interface`/`subnet`/`instance-connect-endpoint`.

---

## §5 — Recommended areas of focus (per firing lens)

### A1 — Lens A (cross-tenant IDOR): the 4 shared-subnet isolation claims are server-side-only, with NO customer-expressible IAM backing  ⟵ **CROWN JEWEL / Critical-if-broken**
- **Claim:** A participant, holding the (legitimately-known) `i-…`/`eni-…`/`eice-…` of an **owner-created** resource co-located in the same shared subnet, can describe/start/stop/terminate/attach/open-tunnel against it — breaking the symmetric isolation promise.
- **Mechanism (doc evidence):** `using-vpc.md` L50–52 states the symmetric prohibition verbatim. **Subagent A proved** none of these prohibitions map to any ownership/subnet/creator condition key: Start/Stop/Terminate carry only instance-attribute/tag keys (no `ec2:Subnet`/`ec2:Vpc`); **`DescribeInstances` has no resource type at all and only `ec2:Region`** (L6996–7000) — *entirely unscopable*; `OpenTunnel` has no endpoint-ownership key. The sole enforcer is the implicit cross-account ARN account-segment filter (`arn:…:${Account}:instance/…`, L9949).
- **Confirm/Refute oracle:** In a two-account Org with a RAM-shared subnet, launch an owner instance; from the **participant** credential call `DescribeInstances`/`StopInstances`/`TerminateInstances` naming that `i-…`. **Confirm** = any of the four operations returns the owner's instance data or mutates its state. **Refute** = `UnauthorizedOperation`/empty filter for all four, in both directions.
- **Why this is the highest-value test:** the promise is a bare account-boundary filter with *zero* defense-in-depth and *zero* customer auditability. If the server-side filter has any edge case (e.g. a describe path that keys off subnet membership rather than resource-ARN account, a batch/by-filter call that leaks co-resident instances, a tag-based projection), it is a **cross-account** disclosure/control → **Critical**. The hunter should specifically try **filter-based** `DescribeInstances` (by `subnet-id`, by `vpc-id`, by tag) — the List-level, resourceless nature of the action (confirmed L6996–7000) is exactly where a co-residency leak would hide.
- **Adjacent shapes to test:** (i) *naming trick* — supply the instance by a secondary name (ENI id, private IP, tag) rather than `i-…`; does authz check one naming while the op acts on another? (ii) *sub-resource leakage* — `DescribeNetworkInterfaces`/`DescribeInstanceStatus`/`DescribeInstanceTopology` filtered to the shared subnet; do owner resources appear?

### A2 — Lens A/V (EICE cross-account tunnel): participant → owner-created EICE
- **Claim:** A participant can `OpenTunnel` through the **owner's** EICE in the shared subnet and reach an instance, despite `using-vpc.md` L52 ("Participants can't use an EC2 Instance Connect Endpoint that the VPC owner created").
- **Mechanism:** `OpenTunnel` (list_ec2-instance-connect.md L44–48) has **no endpoint-ownership condition key** — only `remotePort`/`privateIpAddress`/`maxTunnelDuration`/tags. The block is purely that the owner's `eice-…` ARN lives in the owner's account (L9950). EICE is an **identity-aware TCP proxy** that authorizes "before it reaches your VPC" — so a successful cross-account tunnel is a **network-reachability breach into the owner's instances**.
- **Oracle:** Owner creates EICE in shared subnet; participant (holding the `eice-…` id) calls `OpenTunnel`. **Confirm** = tunnel establishes / TCP reaches an instance. **Refute** = authz failure. Severity-if-true: **High–Critical** (cross-account instance access).
- **Doc-gap to flag (subagent B):** when a participant creates an EICE *without* specifying an SG, the doc says EICE "use[s] the default security group for the VPC" — which belongs to the **owner**. It is unresolved whether a participant can even create an EICE that falls back to the owner's default SG, or whether that path is blocked. Mark "doc-gap — confirm surface first."

### A3 — Lens U (documented-guarantee vs enforcement): "must be Nitro-based" in IPv6-only subnets is a server-side gate with no IAM key
- **Claim:** The "Any instances launched into an IPv6-only subnet must be Nitro-based" guarantee (`using-vpc.md` L65) is enforced only by RunInstances server-side validation; a customer cannot express or audit it in IAM.
- **Mechanism:** Subagent B grepped `list_ec2.md` — a generic `ec2:InstanceType` key exists, but **no** `ec2:Hypervisor`/`ec2:IsNitro` key (0 hits). The linked `instance-types.md#instance-hypervisor-type` lists hypervisors with **no enforcement mechanism**.
- **Oracle:** Attempt `RunInstances` of a Xen (non-Nitro) type into an IPv6-only subnet. **Confirm-as-documented** = server rejects. The research question is not "can I break it" (low value) but **"is the only control a server-side gate, leaving admins unable to pre-restrict via IAM except by hand-maintaining an `ec2:InstanceType` allowlist?"** → Lens-U hardening gap, Low/informational unless the gate itself is bypassable.

### A4 — Lens R/U (AWS-authored insecure default): default-VPC is internet-reachable by default
- **Claim:** Every default subnet ships `MapPublicIpOnLaunch=true` + DNS hostnames + a `0.0.0.0/0 → igw` main route (`using-vpc.md` L20, L39; `default-vpc-components.md`; `subnet-public-ip.md` "default subnets have this attribute set to `true`"; `work-with-default-vpc.md` sample `"MapPublicIpOnLaunch": true`). Any instance launched with no network config is **immediately public-IP-assigned and internet-routed**.
- **Precision guard (do NOT overstate — subagent B):** the default **security group** is **not** open to `0.0.0.0/0` inbound. Its only inbound rule is self-referencing (same-SG sources); the doc explicitly says the default rules "do **not** allow the instances to receive traffic from the internet gateway." So the shipped exposure is **auto-public-IP + DNS + 0.0.0.0/0 egress route**, gated inbound by the self-referencing default SG — until the operator adds any inbound rule. Frame it as *"a public IP and a route to the internet are assigned without opt-in; only the default-SG inbound rule stands between that and exposure"* — an AWS-authored default-posture observation (Tier-2 / Lens R), **not** a "wide-open SG" claim.
- **Oracle:** documentation-confirmed; no live test needed to establish the default. If the hunter wants blast-radius evidence: launch into a default subnet with no explicit SG/IP config and confirm a public IPv4 + igw route are present. Severity: hardening/posture (not a cross-account breach).

### A5 — Lens S/EE (owner↔participant asymmetry & RAM lifecycle)
- **Claim set (from `vpc-share-limitations.md`, subagent B):** The owner↔participant permission matrix has **asymmetries** worth probing:
  - Owner can **describe** participant ENIs; participant has no reciprocal read of owner ENIs. → test whether the owner's describe-visibility of participant ENIs leaks more than intended (tags, attachment, private IPs).
  - Flow logs: owner can log the **whole shared subnet** (capturing participant traffic); participant can log only its own ENIs. → **owner-side cross-tenant traffic visibility is by-design** but worth characterizing (is participant traffic in the owner's subnet flow log a documented data-exposure the participant can't see or opt out of?).
  - SG cross-reference: participant SG rules may reference owner/other-participant SGs by `account-number/security-group-id` **even without SG sharing** — test whether this reference leaks existence/membership of SGs across accounts (enumeration oracle).
  - "Participants can't launch using the **default** SG (it belongs to the owner)" and "can't share default SGs / default-VPC SGs" (`security-group-sharing.md`). → confirm the launch-time block holds; try naming the owner's default SG id in participant RunInstances.
- **Oracle:** per bullet, the breach is the asymmetric read/enumeration succeeding beyond what the matrix grants. Severity: High if it yields another account's resource data; else hardening.

### A6 — Lens A (default-VPC/subnet creation is unscopable)
- `CreateDefaultVpc`/`CreateDefaultSubnet` carry only `ec2:Region` (hub-frag). Not cross-account, but note: an account-wide actor can recreate a deleted default VPC (re-establishing the internet-by-default posture) with no finer IAM grain. Lens-S hardening note; Low.

---

## §6 — Threat-model test objectives (execution checklist for the hunter)

1. **[Critical] Cross-account instance control/describe** — participant↔owner, all four ops, including **filter-based** DescribeInstances by subnet/vpc/tag (A1). This is the first and most important test.
2. **[High] EICE cross-account tunnel** — participant `OpenTunnel` on owner EICE (A2) + the no-SG-fallback doc-gap.
3. **[High] ENI cross-account mutation** — participant attach/detach/modify/delete of owner ENI; owner-side describe-leak of participant ENIs (A1 adjacent, A5).
4. **[Med] SG cross-reference enumeration** — participant rule referencing owner/other-participant SG by `acct/sg-id` as an existence oracle (A5).
5. **[Med] Routing/NACL/gateway mutation** — participant attempts to create/modify/associate RT/NACL/IGW/NAT in the shared VPC (A5).
6. **[Low] IPv6-only Nitro gate** — non-Nitro RunInstances into IPv6-only subnet; characterize server-side-only enforcement (A3).
7. **[Posture/Tier-2] default-VPC internet-by-default** — document the shipped default; precision-guard the default-SG inbound framing (A4).
8. **Preconditions:** two accounts in one AWS Org, RAM subnet share active, synthetic/canary instances only, teardown of every created resource. **Stop at any AWS-fleet identity.**

---

## §7 — Out of scope

- Customer-authored IAM policies / SG rules / NACL misconfigurations (footguns, not AWS defects) — **except** AWS-shipped defaults (default VPC/SG posture, A4) which are Tier-2 in-scope.
- Live exploitation beyond existence proof; data exfiltration beyond minimum PoC; any escalation once a boundary is shown broken.
- AWS service-plane internals, fleet identities, control-ENI reachability — **HARD STOP + flag**.
- Non-HTTP/application-layer: no port scanning, DNS enumeration, subnet bruting.
- Topics **owned by sibling plans** (cross-reference, do not re-test here): secondary-IP cross-account takeover (`using-instance-addressing`), IPv6 public-by-default IAM gap (`working-with-ipv6-addresses`), ENI create/modify/delete scoping (`create-network-interface`, `modify-network-interface-attributes`, `delete-eni`), launch-time public-IP key `ec2:AssociatePublicIpAddress` (`working-with-ip-addresses`), Windows static-binding split-brain (`config-windows-multiple-ip`).

---

## §8 — Null hypotheses (lenses checked and NOT firing, with pages read)

- **Lens B (confused deputy / PassRole):** N/A — read `using-vpc.md`, `vpc-sharing.md`, `vpc-share-limitations.md`, EICE pages; no field on this surface where the service assumes a caller-supplied role ARN. (EICE uses the *caller's* IAM entity, not an assumed role.)
- **Lens C (credential vending / session scope):** N/A — no STS/session-policy/token-vending field on these pages.
- **Lens D (data→control-plane escape):** not on this page's surface — the shared-subnet control-plane filter is the relevant seam (covered under A1), but no documented data-path-to-control-ENI primitive appears here. Mark adjacent (`requester-managed-eni` sibling owns the service-plane-seam angle).
- **Lens F (injection/translation):** N/A — no customer-input-to-query transform on this surface.
- **Lens G (SSRF):** N/A — read all five sections of `using-vpc.md` plus `default-vpc`, `subnet-public-ip`, EICE pages; no field the service dereferences (no URL/host/callback). The only "fetch" is the EICE TCP proxy, covered under A2.
- **Lens Q (blob parse):** N/A — no upload/parse field on this surface.
- **Lens T (secret storage):** N/A — no service-generated secret persisted by this surface.
- **Lens N (EC2-Classic remnants):** checked — no EC2-Classic language remains on `using-vpc.md`; null.

**Doc-gaps flagged (confirm surface before testing):** (1) EICE no-SG fallback to owner's default SG for a participant-created endpoint (A2); (2) exact server-side mechanism of the DescribeInstances account filter (A1) — unspecified in docs, must be probed empirically.

---

*Plan authored from documentation only, 2026-10-15. Executable by `aws-vuln-hunter` against an authorized two-account Org. Supersedes the shared-VPC deferral stubs in `ec2-networking` hub lead #5 and sibling plans.*
