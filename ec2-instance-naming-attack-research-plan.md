# EC2 Instance Hostnames & DNS Naming — Attack / Research Plan

> **Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html`
> (offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-instance-naming.md`)
> **Children folded in:** `understanding-ec2-instance-hostnames-domains.md`, `hostname-types.md`
> (the hub page is a 2-link stub; all real content lives in the two children).
> **Method:** AWS `security-questionbuilder` — boundary-first threat model. Every item is a
> documentation-derived, **falsifiable** research lead for a hunter to execute later.
> **Nothing in this plan was tested against a live account.** All leads are Claim → Mechanism
> (doc evidence) → Confirm/Refute oracle → Preconditions/Cost/Severity hypotheses.
> **Authoritative IAM ground truth:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`
> — the **action→resource table (L8974–9028)** is authoritative, NOT the per-condition-key reverse
> index (L3888–3940, which prints blank cells for every action and must not be read as "no keys").
> **Produced:** 2026-10-15. Opus 4.8 synthesis of two parallel sub-agent deep-dives (IAM-scoping; `.ip.aws`/dangling-DNS/shared-VPC).

---

## §0 — How to use this plan

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (§5 is ranked); look left and right for adjacent bugs.
- **Relationship to the hub plan.** This is the dedicated **page-level child** of
  `ec2-networking-attack-research-plan.md` (Cluster 4, fragment `.cache/plans/ec2-net-frag4-vpc-zones-dns.md`),
  the hostname/DNS sibling of `using-regions-availability-zones-attack-research-plan.md`.
  **It corrects a drift error in that fragment** (see §5 L1) and goes net-new on the public
  `.ip.aws` surface, dangling-DNS reuse, the always-on A-record oracle, and the shared-VPC
  subnet-owner lever. Where this plan and the hub differ, **this plan's IAM table (§4) is correct**
  — it was re-derived from the authoritative action→resource table.
- **HARD STOP:** the moment live evidence shows an identity/credential/ARN/account belonging to
  **AWS's own service plane** (the AmazonProvidedDNS resolver fleet, the `.ip.aws`/`compute.amazonaws.com`
  authoritative zone infrastructure), stop, preserve evidence, flag for AWS-Security disclosure. The
  DNS *resolver* and the AWS-owned authoritative zones are AWS infrastructure — probe them only as a
  client issuing ordinary queries; do not attempt to reach their control plane.

---

## §1 — Pentest objectives

1. **Launch-time guardrail gap** — show that a principal authorized to `RunInstances` into a subnet
   **cannot be IAM-restricted** to a particular hostname type / A-/AAAA-record posture, because no
   condition key covers `PrivateDnsNameOptions` (§5 L1).
2. **Deceptive-policy / inert-key** — show that a least-privilege policy written against bare
   `ec2:Attribute` to gate the DNS-hostname Modify actions **silently matches nothing** (fail-open),
   and that `ModifySubnetAttribute` is one action governing ~10 unrelated subnet attributes (§5 L2).
3. **Internal recon oracle** — show that the IP-name A record is answered **unconditionally**
   (owner cannot opt out) and the resolver cannot be SG/NACL-filtered, giving a low-noise host-discovery
   oracle reachable cross-VPC (peering) and from on-prem (Resolver inbound endpoint) (§5 L3).
4. **Dangling AWS-native hostname reuse** — show that because the public hostname is a deterministic
   function of the current public IP with **no account binding**, releasing + reassigning an IP/EIP
   hands the next (cross-account) holder the victim's old `ec2-…amazonaws.com` / `.ip.aws` hostname (§5 L4).
5. **Cross-account private-IP disclosure via split-horizon** — once DNS resolution is enabled over a
   (possibly cross-account) peering connection, the *public* hostname of a peer's internet-facing
   instance resolves to its **private** IP for the peer VPC (§5 L5).
6. **Shared-VPC subnet-owner influence** — characterise exactly how much the subnet owner's
   `PrivateDnsHostnameTypeOnLaunch` default controls (vs cannot force) participant-launched instance
   hostnames (§5 L6).
7. **Documented-guarantee vs enforcement** — trace every "only / cannot / always / within the VPC"
   claim on these pages to the mechanism that enforces it (§6).

---

## §2 — Components, Assets, and Design

### Customer-facing interface
A **SigV4 IAM control-plane** feature (console + CLI + SDK) that configures how EC2 instance/ENI
names are *constructed* and whether the **AmazonProvidedDNS resolver** (the per-VPC `.2` resolver /
Route 53 Resolver) answers A/AAAA queries for those names. There is **no customer-reachable service
fleet, wire protocol, parser, or translation layer** here — the only "data plane" is DNS resolution
over UDP/TCP 53 against the AWS resolver, plus the AWS-owned authoritative zones
(`compute.internal`/`ec2.internal`, `compute.amazonaws.com`, `ip.aws`). That shifts all value toward
**IAM-scoping gaps**, **asserted-but-unmechanized guarantees**, and **namespace/predictability**
properties — not cross-tenant-on-a-shared-host findings.

### Hostname taxonomy (the asset the feature produces)

| Class | Scope set | Format | Derived from | Configurable? |
|---|---|---|---|---|
| **Private — IP name** (legacy) | instance | `ip-10-24-34-0.ec2.internal` (us-east-1) / `ip-10-24-34-0.<region>.compute.internal` | **private IPv4** | A record **always answered — cannot be disabled** |
| **Private — Resource name** | instance | `i-0123….ec2.internal` / `i-0123….<region>.compute.internal` | **instance ID** | A and/or AAAA answering is opt-in (per-instance or per-subnet) |
| **Public — IPv4 IP-based** | network interface | `ec2-52-54-55-66.<region>.compute.amazonaws.com` | **public IPv4** | split-horizon; globally resolvable |
| **Public — IPv6 IP-based** | network interface | `<base36-ipv6>.<region>.ip.aws` | **public IPv6 GUA** (base36) | `.ip.aws` zone |
| **Public — Dual-stack IP-based** | network interface | `<base36-ipv6>-<base36-ipv4>.<region>.ip.aws` | **public IPv6 GUA + public IPv4** (base36) | `.ip.aws` zone |

Identifier properties that drive the lenses:
- **Private names are fully predictable** — both forms are a pure function of the private IP or the
  instance ID (neither secret; instance IDs are returned by countless Describe calls).
- **Public names are reversible** — the base36 label is an unkeyed, unsalted positional encoding of
  the exact public IPv4/IPv6; `hostname-types.md` gives both directions (`q3cdpO` ⇄ `52.54.55.56`).
  Anyone can encode/decode `.ip.aws` labels locally without resolving them.
- **Hostnames carry no account/ownership binding** — the namespace is keyed only on the IP (or
  instance ID), so whoever currently holds the IP owns the name.

### `[NEW]` surface — the public `.ip.aws` feature (prioritise)
The public-hostname feature (hostname types `public-dual-stack-dns-name` / `public-ipv4-dns-name` /
`public-ipv6-dns-name`, action **`ModifyPublicIpDnsNameOptions`**, domain `ip.aws`) **shipped
~2025-05-20/21** (botocore model `api-change-ec2-5655`, "Release of Dualstack and Ipv6-only EC2
Public DNS hostnames", 2025-05-21). It has **no entry in the EC2 User Guide DocumentHistory and no
"What's New" post** — a *quietly-shipped* surface with less public scrutiny than a headlined launch.
Per Step 5, it leads the ranking.

### ASCII — resolution paths and trust zones
```
                                 AWS-owned authoritative zones (service plane — HARD STOP on control-plane reach)
                                 ┌───────────────────────────────────────────────┐
                                 │ compute.internal / ec2.internal  (private)     │
                                 │ compute.amazonaws.com / ip.aws   (public)      │
                                 └───────────────▲───────────────────────────────┘
  caller inside VPC-A  ──DNS q──►  AmazonProvidedDNS (.2 resolver, per-VPC)  ──┤
  (cannot be SG/NACL-filtered)         │  split-horizon:                        │
  peer VPC-B (cross-acct, if           │   • inside VPC → PRIVATE IP            │
   DNS-resolution-over-peering ON) ────┤   • from internet → PUBLIC IP         │
  on-prem via Resolver INBOUND ────────┘   • IP-name A record ALWAYS answered   │
   endpoint (DX/VPN)                                                            │
                                                                                 │
  Control plane:  RunInstances(PrivateDnsNameOptions)  ModifyPrivateDnsNameOptions(instance)
                  ModifySubnetAttribute(subnet default)  ModifyPublicIpDnsNameOptions(ENI)
                  Describe{Instances,Subnets,NetworkInterfaces}  (read; unscopable)
```

---

## §3 — Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Principal w/ `RunInstances` in subnet X | Hostname-type policy the subnet owner intended | `PrivateDnsNameOptions` request block overrides subnet default | A launch succeeds with a hostname type the operator believed IAM/subnet pinned — because **no condition key gates it** |
| Policy author (least-priv intent) | DNS-hostname Modify actions | Bare `ec2:Attribute` condition in an Allow/Deny | The condition **never matches** → Allow never grants / **Deny never blocks** (inert key fail-open) |
| Any principal reaching the VPC resolver | Any instance's private-IP liveness | `ip-<ip>.…compute.internal` A query (always answered) | A query returns an authoritative A record for an IP the querier was never granted visibility to; works despite target SG/NACL and owner opt-out intent |
| Cross-account IP holder (next tenant) | Victim's old AWS-native public hostname | Release + reassign of public IPv4 / EIP | The attacker's new instance answers to `ec2-<victim-ip>.compute.amazonaws.com` / `<base36>.ip.aws` with **no AWS-side action** |
| Principal in peer VPC-B (diff account) | Peer VPC-A instance's **private** IPv4 | Public hostname resolved over DNS-resolution-enabled peering | Public hostname resolves to the **private** IP of a different account's instance |
| Subnet owner (account A) | Participant (account B) launches in shared subnet | `ModifySubnetAttribute` sets `PrivateDnsHostnameTypeOnLaunch` default | Participant instances inherit owner-chosen hostname/record posture by default (participant cannot change the subnet default) |
| Customer surface | **AWS's own resolver fleet / `.ip.aws` zone control plane** | Any query | **HARD STOP** — reaching the resolver/zone control plane (not just issuing queries) is a service-plane breach |

---

## §4 — API / Interface Inventory

Authoritative resource types + condition keys from `list_ec2.md` **action→resource table L8974–9028**
(NOT the blank reverse-index at L3888–3940).

| Name | Mutating? | Resource type (required\*) | Key condition keys | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| **RunInstances** (`PrivateDnsNameOptions`) | Yes | multi (`instance*`,`subnet*`,`network-interface*`,`image*`,…) | `aws:RequestTag`, `ec2:InstanceType`, `ec2:Tenancy`, AZ, `ec2:MetadataHttpTokens`… | Yes (SigV4) | any principal w/ RunInstances | **No condition key anywhere covers `PrivateDnsNameOptions`/`HostnameType`/record flags** → launch-time hostname posture is IAM-ungated. `HostnameType` enum `ip-name\|resource-name` (lowercase). Defaults inherited from subnet. |
| **ModifyPrivateDnsNameOptions** | Yes | `instance*` | `aws:/ec2:ResourceTag`, `ec2:InstanceID`, AZ, `ec2:InstanceType`, `ec2:Tenancy`, **`ec2:Attribute`(+/`${AttributeName}`)** | Yes | principal w/ action on the instance | **Scopable** by instance tag/ARN (hub fragment's "no keys" was wrong). Flips IP-name↔resource-name + A/AAAA answering. |
| **ModifyPublicIpDnsNameOptions** `[NEW ~2025-05]` | Yes | `network-interface*` | `aws:/ec2:ResourceTag`, AZ, **`ec2:Subnet`**, **`ec2:Vpc`**, **`ec2:Attribute`(+/`${AttributeName}`)** | Yes | principal w/ action on the ENI | Switches public hostname type (`public-dual-stack/ipv4/ipv6-dns-name`). Scopable by ENI/subnet/VPC. |
| **ModifySubnetAttribute** | Yes | `subnet*` | `aws:/ec2:ResourceTag`, `ec2:SubnetID`, AZ, **`ec2:Vpc`**, **`ec2:Attribute`(+/`${AttributeName}`)** | Yes | principal w/ action on the subnet | **One action governs ~10 unrelated attributes** (MapPublicIpOnLaunch, AssignIpv6…, EnableDns64, PrivateDnsHostnameTypeOnLaunch, Enable{A,AAAA}RecordOnLaunch, Outpost LNI…). Only `ec2:Attribute/${AttributeName}` isolates the DNS ones. |
| **DescribeInstances** | No | **(blank)** | `ec2:Region` only | Yes | any principal w/ action | **Unscopable** read oracle — reads private/resource hostname config account/region-wide. |
| **DescribeNetworkInterfaces** | No | **(blank)** | `ec2:Region` only | Yes | any principal w/ action | **Unscopable** — reads every ENI's `PublicIpDnsNameOptions`. |
| **DescribeSubnets** | No | **(blank)** | `ec2:Region` only | Yes | any principal w/ action | **Unscopable** — reads subnet `PrivateDnsHostnameTypeOnLaunch` defaults. |

**No `ec2:HostnameType` (or any hostname-type-named) condition key exists anywhere in the file.** The
only value-level lever is `ec2:Attribute/${AttributeName}` on the three Modify actions — and its
runtime population for those actions is itself an open question (§5 L2).

---

## §5 — Recommended Areas of Focus (ranked)

### L1 — Launch-time hostname posture is IAM-ungated: no condition key covers `RunInstances` `PrivateDnsNameOptions` *(highest — new-adjacent control gap)*
**Background.** `RunInstances` accepts a `PrivateDnsNameOptions` block (`HostnameType` = `ip-name|resource-name`,
`EnableResourceNameDnsARecord`, `EnableResourceNameDnsAAAARecord`); defaults are inherited from the
subnet but the launcher may override per-instance (API_RunInstances: "The default values are inherited
from the subnet"). The post-launch Modify actions carry rich condition keys; `RunInstances` does not —
for *this* field.

**Security Concern.** An organization that wants "all instances must launch as resource-name with
AAAA answering" (e.g. for an IPv6-migration or an internal naming-governance control) **cannot express
that in IAM.** There is no `ec2:HostnameType` key, and an exhaustive sweep of every `RunInstances`
resource-type row found **no condition key naming `PrivateDnsNameOptions`/`HostnameType`/
`EnableResourceNameDns{A,AAAA}Record`.** The only enforcement points are post-launch (`ModifyPrivateDnsNameOptions`/
`ModifySubnetAttribute`) — i.e. detect-and-remediate, never prevent.

**High-level Test Scenarios (falsifiable claims).**
- **Claim:** A scoped role holding `ec2:RunInstances` (resource-scoped to a subnet) can launch with
  `PrivateDnsNameOptions.HostnameType=ip-name` even under a policy that attempts to `Deny` it by any
  condition → **Mechanism:** no condition key for the field → **Oracle:** `iam:SimulatePrincipalPolicy`
  with a `Condition` on a hostname-type-flavored key reports the key unrecognized/ignored; the simulated
  `RunInstances` is Allowed regardless of the requested `HostnameType`. No live launch required.
- **Claim:** The subnet default set by the owner is *not* a guardrail — a participant/caller overrides it
  at launch (ties to L6). → **Oracle:** API model confirms the override field; simulate/launch both ways.

**Doc evidence:** API_RunInstances.md (`PrivateDnsNameOptions`, "defaults inherited from the subnet");
API_PrivateDnsNameOptionsRequest.md (enum/flags); list_ec2.md RunInstances rows (no matching key).
**Severity-if-true:** Medium (least-privilege / preventive-control gap; customer-owned governance intent defeated). **Stop:** once the simulator confirms no key gates the field.

### L2 — Deceptive IAM: bare `ec2:Attribute` is likely inert on the DNS Modify actions, and one `ModifySubnetAttribute` governs ~10 attributes *(Lens S / U — corrects the hub)*
**Background.** The hub fragment stated these three actions have "no condition keys / zero
conditionability." That read the **reverse-index** section (L3888–3940, blank cells for every action).
The **authoritative action→resource table (L8974–9028)** shows each is `*`-required-resource-scoped and
carries `ec2:Attribute` + `ec2:Attribute/${AttributeName}` plus tag/ARN keys. The real finding is
subtler and more dangerous than "unscopable."

**Security Concern.** Two fail-open shapes:
1. **Bare `ec2:Attribute` probably never populates** for `ModifyPrivateDnsNameOptions` /
   `ModifyPublicIpDnsNameOptions` / `ModifySubnetAttribute`. That key is defined to filter the literal
   `Attribute` request *field* that only `ModifyImageAttribute`/`ModifyInstanceAttribute`/
   `ModifySnapshotAttribute` actually have. The DNS actions use named fields (`PrivateDnsHostnameType`,
   `HostnameType`, `PrivateDnsHostnameTypeOnLaunch`) with **no `Attribute` selector**. So a least-priv
   policy written as `"Deny": … "Condition":{"StringEquals":{"ec2:Attribute":"…"}}` **matches nothing →
   the Deny never fires** (and an Allow so-conditioned never grants). The policy *looks* restrictive and
   isn't — exactly the Lens-S "key silently ignored" shape (variant a), manifesting as "never populated"
   rather than case-mismatch.
2. **`ModifySubnetAttribute` is one IAM action for ~10 semantically unrelated subnet attributes**
   (MapPublicIpOnLaunch, AssignIpv6AddressOnCreation, EnableDns64, the three DNS-hostname toggles,
   Outpost LNI, …). A grant scoped only by `subnet*` ARN/tag confers control over **all** of them. The
   *only* way to say "may toggle DNS-hostname defaults but not MapPublicIpOnLaunch" is
   `ec2:Attribute/${AttributeName}` keyed on the exact PascalCase field name — easy to omit, and whose
   runtime population for this action should itself be verified.

**High-level Test Scenarios.**
- **Claim:** `"ec2:Attribute":"PrivateDnsHostnameType"` (or any value) in a Deny on `ModifyPrivateDnsNameOptions`
  does not block the call. → **Oracle:** `iam:SimulatePrincipalPolicy` with that Deny vs the bare action —
  if the action is still Allowed, the key is inert. Corroborate with a scoped-role live call on a **canary
  instance you own** (read-only effect: just flips a hostname toggle on your own resource; no cross-tenant touch).
- **Claim:** `ec2:Attribute/${AttributeName}` *does* bind for `ModifySubnetAttribute` (so the per-attribute
  isolation is at least achievable) — or does **not** (so the whole action is all-or-nothing). → **Oracle:**
  simulate `ModifySubnetAttribute` with `Condition` on `ec2:Attribute/MapPublicIpOnLaunch` vs
  `ec2:Attribute/PrivateDnsHostnameTypeOnLaunch`; observe whether the simulator honors either.
- **Claim (case-sensitivity — likely N/A here, record it):** the enum values are already lowercase-hyphenated
  (`ip-name`, `resource-name`, `public-ipv4-dns-name`), so the PascalCase-Deny case-mismatch fail-open that
  bites `ModifyInstanceAttribute`'s camelCase `Attribute` enum does **not** apply on the *value* side here.

**Doc evidence:** list_ec2.md L8974–9028; iam-policies-for-amazon-ec2.md (`ec2:Attribute` semantics, L195–266);
API_ModifySubnetAttribute.md (attribute list); API_ModifyInstanceAttribute.md (the camelCase `Attribute` enum, contrast).
**Severity-if-true:** Low–Medium (deceptive least-privilege; a policy author believes a control exists that doesn't). **Report as a doc/behavior finding** if bare `ec2:Attribute` is listed-but-inert — it is AWS-owned reference content. **Stop:** once the simulator settles whether the key populates.

### L3 — The IP-name A record is an unconditional, un-opt-out-able internal recon oracle *(Lens U + V)*
**Background.** `hostname-types.md`: *"For private DNS hostnames based on IP names, you cannot configure
whether a DNS A record query for the instance is responded to or not. **DNS A record queries are always
responded to irrespective of the guest OS hostname settings.**"* And `AmazonDNS-concepts.md`: *"You cannot
filter traffic to or from the Amazon DNS server using network ACLs or security groups."*

**Security Concern.** The private IP-name namespace (`ip-<a-b-c-d>.<region>.compute.internal`) is fully
predictable, and the resolver answers A queries for live IPs **authoritatively, unconditionally, and
unfilterable** — independent of the target's SG/NACL posture, the target owner's opt-out intent, or guest-OS
hostname settings. Any principal that can reach the resolver can sweep a VPC CIDR and get an authoritative
liveness yes/no per IP — a lower-noise alternative to ICMP/TCP host discovery. Reach is **not limited to the
same VPC**: a Route 53 Resolver **inbound endpoint** extends the resolver to on-prem over DX/VPN, and a
peered VPC with DNS-resolution-over-peering enabled extends it to another account (see L5).

**High-level Test Scenarios.**
- **Claim:** From inside VPC-A, `dig ip-10-0-0-<n>.<region>.compute.internal A` returns an authoritative
  record for a live ENI the querier has no IAM/console visibility into, for the full CIDR, and the owner
  cannot suppress it. → **Oracle:** batch A queries vs a known mix of live/dead IPs; live IPs resolve,
  dead ones NXDOMAIN — an enumeration oracle. Confirm toggling the instance's resource-name A/AAAA settings
  does **not** affect the IP-name A answer.
- **Claim (reach):** the same oracle works from on-prem through a Resolver inbound endpoint and from a peer
  VPC. → **Oracle:** query from each vantage; compare.

**Doc evidence:** hostname-types.md ("always responded to…"); AmazonDNS-concepts.md ("cannot filter… with
NACLs or security groups"); resolver-forwarding-inbound-queries.md.
**Severity-if-true:** Low–Medium (information disclosure / recon enabler; intra-VPC an attacker with presence
already has host-scan options, but the *unsuppressable + cross-boundary via inbound endpoint* properties and
the documented inability to opt out are the AWS-owned facts worth a hunter's confirmation). **Stop:** once the enumeration oracle is demonstrated on canary IPs you own.

### L4 — Dangling AWS-native public hostname reuse on IP/EIP reassignment (cross-account) *(Lens EE / AA)*
**Background.** The public hostname is a **pure deterministic function of the current public IP** with no
account/ownership binding (base36 of the IP for `.ip.aws`; dotted-quad for `compute.amazonaws.com`).
`hostname-types.md`: changing the IP means "**the previously-generated public hostname will no longer be
valid**" (and forces an IMDS refresh). `elastic-ip-addresses-eip.md`: associating an EIP changes the
instance's public DNS hostname "to match the Elastic IP address." AWS's own dangling-DNS guidance
(`routing-to-ec2-instance.md`: *"If you release the elastic IP… delete the DNS record… a dangling DNS record
can be taken over"*) targets **customer Route 53 records**, not AWS's auto-generated hostnames.

**Security Concern.** When a public IPv4/EIP is released and later re-assigned to a **different account's**
instance, that next holder's instance automatically answers to the victim's old
`ec2-<ip>.compute.amazonaws.com` / `<base36>.ip.aws` hostname — **no AWS-side action, no console step.**
Any third party still pointing a CNAME (or hardcoded reference) at that AWS-native hostname is now resolving
to the attacker's instance: a classic cloud subdomain-takeover shape, but at the AWS-native-hostname layer
AWS does *not* warn about (its warning is only about the customer's own A/CNAME record). The `.ip.aws` form
is **brand-new (May 2025)** and even less likely to be on defenders' takeover-monitoring lists.

**High-level Test Scenarios.**
- **Claim:** Across two accounts you control, release a public IPv4 from account-A instance, churn
  allocations until account-B is handed that IP, and show account-B's instance now resolves/serves the
  identical `ec2-<ip>.compute.amazonaws.com` and `.ip.aws` hostname. → **Oracle:** the AWS-generated hostname
  is byte-identical across the two owners; a CNAME you pre-pointed at it now reaches account-B's instance.
  **Preconditions/Cost:** two accounts; EIP/public-IP churn (nondeterministic, may need many allocations);
  entirely within your own accounts — no third-party victim touched.
- **Adjacent:** quantify how fast a released public IPv4 can be re-acquired (pool-reuse timing) — the shorter,
  the more practical the attack.

**Doc evidence:** hostname-types.md (Important note); elastic-ip-addresses-eip.md; routing-to-ec2-instance.md;
protection-from-dangling-dns.md (shows AWS scopes its protection to Route 53 *delegation* records, not this).
**Severity-if-true:** High (cross-account hijack of traffic sent to a stable AWS-provided hostname), **but note the
root cause is IP reuse / customer dangling reference — this is largely a shared-responsibility + documentation-gap
finding; it does not by itself cross into AWS's service plane.** Report the **doc gap** (no AWS warning that its
auto-generated public hostnames are dangling-reusable) as AWS-owned. **Stop:** at demonstrating identical-hostname reuse across your own accounts.

### L5 — Split-horizon discloses a peer account's **private** IP once DNS-resolution-over-peering is enabled *(Lens A / V)*
**Background.** `vpc-peering-dns.md`: with DNS resolution enabled on a peering connection, a query from one
side using the **public** DNS hostname of an instance on the other side resolves to that instance's **private**
IPv4. The peering can be **cross-account** (requester/accepter in different accounts; each owner opts in).

**Security Concern.** This is a *mutual opt-in*, so not an unauthenticated default leak — but in common
multi-account landing-zone / hub-and-spoke / partner-integration topologies, enabling DNS-resolution-over-peering
(often done for convenience) silently discloses the **private addressing** of every internet-facing instance to
the peer account via the public hostname. An operator who thinks "public hostname → public IP only" is wrong
inside the peering relationship.

**High-level Test Scenarios.**
- **Claim:** From account-B's peer VPC, resolving account-A's instance public hostname returns account-A's
  **private** IP. → **Oracle:** `dig` the public hostname from the peer VPC with resolution enabled vs disabled;
  enabled → private IP, disabled → public IP (or NXDOMAIN). Demonstrates the cross-account private-IP disclosure
  surface the toggle actually opens.
**Doc evidence:** vpc-peering-dns.md; AmazonDNS-concepts.md.
**Severity-if-true:** Low–Medium (private-topology disclosure to an *already-peered* account; gated by a documented opt-in — characterize precisely, likely a hardening/awareness finding not a boundary break). **Stop:** once the enabled-vs-disabled difference is shown.

### L6 — Shared-VPC subnet-owner default vs participant launch-time override *(Lens A/U — characterize, not break)*
**Background.** `ModifySubnetAttribute.PrivateDnsHostnameTypeOnLaunch` (+ the two record toggles) is set
**only by the subnet owner**; `vpc-share-limitations.md`: *"Participants cannot modify shared subnets or their
related attributes. Only the VPC owner can."* But `RunInstances.PrivateDnsNameOptions` lets the participant
**override** per-instance at launch (L1).

**Security Concern.** The subnet owner's hostname-type default is an **influence, not an enforcement** —
participant instances *inherit* it by default (so an owner who flips the subnet to `ip-name` nudges every
participant default toward the always-answered IP-name A record of L3), but the owner **cannot force** a
participant's launch-time choice, and (L1) IAM gives the owner no condition key to enforce one either. Worth
stating crisply so a hunter doesn't over-claim an owner→participant control that isn't there, and doesn't
miss that the owner *can* steer the default toward the L3-oracle-exposed IP-name scheme.

**High-level Test Scenarios.**
- **Claim:** A participant launching in a shared subnet whose owner set `PrivateDnsHostnameTypeOnLaunch=resource-name`
  can still launch an `ip-name` instance by passing `PrivateDnsNameOptions.HostnameType=ip-name`. → **Oracle:**
  cross-account launch with explicit override; inspect the resulting instance's hostname type.
- **Claim:** The owner cannot IAM-prevent that override (follows from L1 — no key on the field).
**Doc evidence:** vpc-share-limitations.md; API_RunInstances.md; using-vpc.md (shared-subnet model).
**Severity-if-true:** Low (least-privilege/awareness; depends on L1). **Stop:** once override-despite-default is shown.

---

## §6 — Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Launch with a hostname posture the org tried to forbid | RunInstances `PrivateDnsNameOptions` | *(none — no condition key; subnet default is overridable)* → L1 |
| Least-priv policy on DNS Modify silently inert | `ec2:Attribute` on the 3 Modify actions | "scope the action with a Condition" → L2 (key may never populate) |
| Over-broad subnet control via one action | ModifySubnetAttribute (~10 attrs) | `ec2:Attribute/${AttributeName}` per-attribute isolation → L2 |
| Unsuppressable private-IP liveness enumeration | IP-name A record + AmazonProvidedDNS | "always responded… cannot be disabled"; "cannot filter resolver with SG/NACL" → L3 (the mitigation IS the vuln) |
| Cross-account hijack of AWS-native public hostname | public IP → `compute.amazonaws.com`/`ip.aws` | AWS dangling-DNS guidance covers only customer R53 records → L4 (gap) |
| Peer account learns private IP via public hostname | split-horizon over peering | mutual DNS-resolution opt-in required → L5 |
| Subnet owner cannot force participant hostname type | shared VPC + RunInstances override | "only owner can modify subnet attrs" (but not launch choices) → L6 |
| Reach AWS resolver / `.ip.aws` zone control plane | AmazonProvidedDNS fleet | **HARD STOP — service plane** |

---

## §7 — Out-of-Scope Risk Categories

- The **AmazonProvidedDNS resolver fleet** and the **AWS-owned authoritative zones** (`.ip.aws`,
  `compute.amazonaws.com`, `compute.internal`) as *targets* — issue ordinary queries only; any attempt to
  reach their control plane is a HARD STOP service-plane breach.
- **IP-pool reuse itself** (that released public IPv4s are re-handed to other accounts) — a documented,
  shared-responsibility property of the EC2 public-IP pool; L4 scopes to the *hostname-reuse + doc-gap*
  consequence, not to "fix IP reuse."
- **Customer-authored dangling Route 53 records** — AWS already warns about these; out of scope as a
  customer footgun. L4's in-scope angle is the *missing warning for AWS's own auto-generated hostnames*.
- **A principal steering its own instances' hostnames** within one account — ordinary intended function;
  only cross-account / cross-team influence is interesting.
- **Within-VPC host scanning in general** — an attacker already inside a VPC has other discovery methods;
  L3's in-scope angle is the *unsuppressable + cross-boundary-via-inbound-endpoint + no-opt-out* properties.
- Reverse DNS (PTR) record customization — separate feature (`Using_Elastic_Addressing_Reverse_DNS`), not this page.

---

## §8 — Null hypotheses / doc gaps (lenses checked, with pages read)

- **Lens B/C (PassRole / credential vending) — N/A.** Read ec2-instance-naming.md, understanding-…-domains.md,
  hostname-types.md, API_RunInstances.md, API_Modify{Private,PublicIp}DnsNameOptions.md. No role-ARN,
  AssumeRole, session-policy, or credential field in the hostname/DNS surface.
- **Lens F (translation/injection) — N/A.** Hostname construction is string formatting from an IP/instance-ID
  plus a documented enum; no parser/wire-protocol/query-builder, no customer free-text that reaches a backend
  language. (The base36 encoding is pure numeral conversion, not a parser of attacker-controlled structure.)
- **Lens G (SSRF) — N/A.** No field on these pages is a URL/host the service dereferences server-side; DNS
  names *resolve* via standard DNS, which is not a service-side HTTP/fetch sink.
- **Lens K/Q/J/H/W/FF/DD/BB/CC — N/A.** No LLM/agent, no upload/file, no OAuth/3P link, no KMS/encryption
  context, no attestation gate, no JWT/token validation, no cache layer, no multi-parser request path, no
  trusted-upstream-context header in this surface (all five pages + the three API models read).
- **Lens S case-sensitivity value-fail-open — recorded N/A on the *value* side** (enums are already
  lowercase-hyphenated), but the *inert-bare-`ec2:Attribute`* shape IS live → L2.
- **Doc gaps to confirm surface first:**
  1. **Runtime population of `ec2:Attribute` / `ec2:Attribute/${AttributeName}`** for the three DNS Modify
     actions — the SAR table lists them but the API shapes lack an `Attribute` selector; needs a
     `SimulatePrincipalPolicy` / scoped-canary confirmation (L2). This is the single most load-bearing unknown.
  2. **`.ip.aws` global resolvability + any rate/abuse controls** — docs assert public resolvability; whether
     `.ip.aws` is reachable/enumerable identically to `compute.amazonaws.com` and whether AWS applies any
     anti-enumeration control is undocumented (L3/L4).
  3. **Public-IPv4 pool re-acquisition timing** — undocumented; governs L4 practicality.
  4. **No User-Guide DocumentHistory / "What's New" entry for the May-2025 `.ip.aws` launch** — itself a
     documentation gap worth noting (quiet-ship, less external review).
```
```
