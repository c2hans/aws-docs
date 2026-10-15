# Amazon EC2 Instance IP Addressing — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html` (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/using-instance-addressing.md`, 171 lines; offline==online byte-identical head, WebFetch of the online `.md` matches — 2026-10-15) and its child pages `instance-secondary-ip-addresses.md`, `managing-network-interface-ip-addresses.md`, `working-with-ip-addresses.md`, `working-with-ipv6-addresses.md`, `config-windows-multiple-ip.md`; IAM facts from `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (10190+ lines, read by offline grep — online `.md` truncates before condition-key tables; see [[reference-aws-iam-service-auth-ref-url]]). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

**Position in the corpus.** This is a **page-level deep-dive child of the `ec2-networking.html` hub** ([[ec2-networking-attack-research-plan]]). The hub owns the EIP/BYOIP/ENI/placement/VPC-zone surface at hub level; this plan develops the one hub child — `using-instance-addressing.html` — that the hub left at summary level, and OWNS the three surfaces this page uniquely introduces into the corpus:
1. **Secondary *private* IP reassignment** (`AssignPrivateIpAddresses` + `AllowReassignment`) — a cross-ENI / (shared-subnet) cross-account private-IP takeover path the hub never developed.
2. **The auto-assigned *ephemeral* public-IPv4 pool reuse / dangling-record surface** — distinct from the hub's EIP (`AllocateAddress`) "reclaim-by-address squatting" lead (that is the *Elastic* IP path; this is the *ephemeral* pool that is "not associated with your AWS account").
3. **The link-local address model** (reserved host services bypass SG/NACL; non-reserved `169.254.0.0/16` is VPC-routable).

It **cross-references, does not restate** (all owned by the hub): EIP cross-account transfer (`EnableAddressTransfer`/`AcceptAddressTransfer`, no dest-account key), released-EIP reclaim-by-address squatting via `AllocateAddress`, BYOIP region-wide unscopability, `DeleteNetworkInterfacePermission` over-revoke, shared-VPC owner/participant isolation, `Describe*NetworkInterface*` zero-resource-scoping, EFA/SRD.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **IAM-scoping leads are settleable WITHOUT touching a live resource** via `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (shows a condition key is inert / a key is absent). Escalate to a live scoped call only with synthetic canary ENIs/instances in a test account you own.
- **`DryRunOperation` is caller-IAM-only** — it is evaluated before resource resolution, so it is NOT an ownership/reassignment oracle (false-positive trap). The cross-ENI/cross-account reassignment questions need two real ENIs (and, for the cross-account variant, a RAM-shared subnet spanning two canary accounts you own).
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the host side of a link-local service — IMDS/KMS/Route 53 Resolver/Time Sync), stop, preserve evidence, flag for AWS-Security disclosure. Do not probe the host side of a link-local service.

---

## 1. Pentest Objectives
Stated as concrete boundary-breach outcomes:
1. **Move an in-use *secondary private IPv4* off a network interface you do not own** (same subnet; then the shared-subnet cross-account variant) using `AssignPrivateIpAddresses … AllowReassignment=true`, and observe the victim ENI lose the address → intra-VPC traffic redirect / service impersonation.
2. **Demonstrate that no IAM policy can forbid reassignment or pin *which* private IP** a principal may (re)assign — only *which ENI* — so an admin cannot author a least-privilege guardrail for the primitive in (1).
3. **Inherit a *released ephemeral public IPv4*** that still has live DNS A-records / firewall allowlists / callback trust pinned to it, by cycling instances in the shared pool → dangling-record traffic hijack across the tenant boundary.
4. **Establish the link-local control blind spot**: confirm (from docs) that SG/NACL do not filter traffic to the reserved link-local services (IMDS `.254`, Route 53 Resolver `.253`, Time Sync `.123`, KMS) and reason about the non-reserved `169.254.0.0/16` VPC-routing seam.
5. For each: identify whether the control an operator *would* reach for exists, and if not, record the enforcement gap.

---

## 2. Components, Assets, and Design

**Mechanism (not marketing).** EC2 instance addressing binds four address *kinds* to a **network interface (ENI)**, which is the actual IAM resource:

- **Primary private IPv4** — one per ENI, from the subnet CIDR, chosen at launch (or caller-specified). Stays with the ENI across stop/start/hibernate; **released on terminate**. *Not* reassignable.
- **Secondary private IPv4** — additional subnet-CIDR addresses on an ENI. **Reassignable from one ENI to another "if you explicitly allow it"** (the `AllowReassignment` flag on `AssignPrivateIpAddresses`). This is the mutable, movable asset at the center of the headline lead.
- **Public IPv4 (ephemeral/auto-assign)** — drawn from **Amazon's shared pool, "not associated with your AWS account"**; released back to the pool on stop/hibernate/terminate or on EIP-associate; **"you cannot reuse it."** The caller cannot choose the address. (Contrast Elastic IP = an account-owned `elastic-ip` resource; owned by the hub.)
- **IPv6** — from the VPC/subnet IPv6 CIDR; globally unique; "cannot be reassigned to another network interface — you must first unassign it." Optional immutable **primary IPv6**.

Behind the customer: the **VPC data plane / mapping service** translates these addresses to the underlying host; a **DHCP** service allocates private IPv4; the **underlying host (Nitro controller / Xen hypervisor)** answers the reserved link-local addresses *out of band of the VPC route table and SG/NACL*. Identity to the control plane is SigV4 IAM; the ENI is named by `eni-…` id or ARN `arn:${Partition}:ec2:${Region}:${Account}:network-interface/${…}`.

**Resource / identifier shapes.** ENI id `eni-<17 hex>` (high entropy — not fabricable); private/public IPv4 and IPv6 are **caller-supplied plain values**, NOT resources and NOT carrying any condition key. A **subnet** can be **shared across accounts via RAM (VPC sharing)** → owner and participant ENIs co-reside in one subnet and one IPv4 CIDR = the cross-account adjacency that upgrades the private-IP-takeover lead.

```
                         ┌─────────────────────────── customer account(s) ───────────────────────────┐
   caller (SigV4 IAM) ── EC2 control plane ── ENI (eni-…, the IAM resource)
                             │  AssignPrivateIpAddresses(--network-interface-id, --private-ip, AllowReassignment)
                             │  AssignIpv6Addresses / Unassign* / AssociateAddress
                             ▼
     subnet CIDR  ◄── [primary priv IPv4] [secondary priv IPv4 *movable*] [IPv6] ──►  (possibly RAM-SHARED: acct A + acct B ENIs co-reside)
                             │
   ephemeral public IPv4 ◄── Amazon shared pool ("not associated with your account"; released → pool; "cannot reuse")
                             │
   169.254.0.0/16 ── RESERVED (.254 IMDS, .253 R53 Resolver, .123 Time, KMS) → answered by HOST, SG/NACL do NOT filter
                  └─ non-reserved → follows VPC route; SG/NACL DO filter
```

### Mandatory coverage sweep (pages read, per Step-1 discipline)
- **URL/dereference fields (Lens G):** none on this page's own APIs — the IP values are identifiers, not fetched URLs. The only server-dereferenced targets reachable *from* an instance are the link-local services (Area 4). Read: all 5 child pages + main. → Area 4 only; no `*Url` field → G otherwise null (named below).
- **Upload/blob fields (Lens Q):** none — no file/image/document field on any addressing API. Read: main + `managing-network-interface-ip-addresses.md`, `config-windows-multiple-ip.md`. → **null, pages named** (§8).
- **Privileged-gate / consent steps (Lens P):** the `AllowReassignment` "explicitly allow it" phrase (Area 1) and the EIP "Allow the Elastic IP address to be reassociated" checkbox (`managing-network-interface-ip-addresses.md:48`) are consent flags — audited under Area 1/§3, since the question is *whose* consent.
- **"Revealed only after" statements (Lens A disclosure-timing):** none on this page.
- **IAM policy JSON / managed policy / sample policy (Lens R/S):** this page prints **no** policy JSON; the condition-key audit is pure Lens S against `list_ec2` (Areas 1–3). The sample-policy / PassRole surface is owned by the hub + the EC2-prerequisites pages — cross-ref, not restated.
- **Generated secrets (Lens T):** none.
- **Asserted guarantees (Lens U):** "you cannot reuse it" (released public IP), "not associated with your AWS account", "remains associated … released when the instance is terminated", "cannot be reassigned … must first unassign", "Security groups and network ACLs do not filter this traffic" — each traced to its enforcement mechanism in Areas 1–4.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller with `AssignPrivateIpAddresses` on **its own ENI** | A **secondary private IPv4 in use on a *different* ENI**, same subnet, same account (another team) | `AssignPrivateIpAddresses --network-interface-id <my-eni> --private-ip <victim's-IP> --allow-reassignment` | The IP leaves the victim ENI and binds to the attacker ENI; victim loses it; intra-subnet traffic/ARP for that IP now reaches the attacker. **Breach = the move succeeds without any permission on the source ENI.** |
| Caller in **account B** (participant) in a **RAM-shared subnet** | A secondary private IPv4 in use on an ENI owned by **account A** in the same shared subnet | same call, cross-account co-residency | Same move succeeds across the account boundary → **cross-account** intra-VPC impersonation. **Critical if it holds.** |
| Admin authoring a least-privilege policy | The reassignment primitive itself | IAM `Condition` on `AssignPrivateIpAddresses` | **Breach of the guarantee = there is no `AllowReassignment`/`ec2:PrivateIpAddress` key**, so the policy cannot express "deny reassignment" or "only these IPs" — only "only these ENIs". |
| Attacker tenant | A **released ephemeral public IPv4** previously owned by victim tenant | Launch/stop cycle draws from the shared pool; attacker inherits an address with live DNS/allowlist/callback trust | Attacker's instance receives traffic/credentials/webhooks that were destined for the victim's old IP → **cross-tenant hijack via a dangling pointer the victim left behind.** |
| Instance (data plane) | Host-plane link-local services (IMDS/KMS/R53/Time) | Traffic to `169.254.169.254/.253/.123` answered by the Nitro/Xen host, **SG/NACL do not filter** | Any SSRF reaching `169.254.169.254` from the instance = IMDS creds (owned generally; **host side = hard stop**). The *doc fact* here is the **control blind spot**: no SG/NACL can block IMDS egress. |
| Instance with a custom route for a **non-reserved** `169.254.x` | Another host/ENI the route points at | Non-reserved link-local follows the VPC route and IS SG/NACL-filterable | Precedence confusion: does a customer route for a near-reserved address ever shadow/!shadow a reserved one? (segmentation reasoning, Area 4). |
| Any customer surface | **AWS's own service plane** (host side of any link-local service) | — | **Hard stop.** Reaching the host/Nitro side, or any AWS-fleet credential, is a disclosure event — preserve evidence, do not exploit. |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Ext-facing | Functionality | Authorized callers | Notes (IAM facts, `list_ec2`) |
|---|---|---|---|---|---|---|
| `AssignPrivateIpAddresses` | SDK/CLI | **Yes** | Yes | Add secondary priv IPv4 to an ENI; **`AllowReassignment` bool** moves an in-use IP | holder of the action on the target ENI | req `network-interface*`; keys: `aws:ResourceTag`, `ec2:AvailabilityZone`, `ec2:ManagedResourceOperator`, `ec2:NetworkInterfaceID`, `ec2:Region`, `ec2:ResourceTag`, `ec2:Subnet`, `ec2:Vpc` (L4700). **No IP-level key; no `AllowReassignment` key.** |
| `UnassignPrivateIpAddresses` | SDK/CLI | Yes | Yes | Remove secondary priv IPv4 | holder on the ENI | same key set (L9696) |
| `AssignIpv6Addresses` | SDK/CLI | Yes | Yes | Add IPv6 to an ENI (no reassignment flag — must unassign first) | holder on the ENI | same key set (L4694) |
| `UnassignIpv6Addresses` | SDK/CLI | Yes | Yes | Remove IPv6 | holder on the ENI | same key set (L9690) |
| `AssociateAddress` / `DisassociateAddress` | SDK/CLI | Yes | Yes | Bind/unbind an **Elastic** IP to an ENI/priv-IP; `AllowReassociation` | holder | `elastic-ip`+`instance`/`network-interface`; EIP path owned by hub |
| `AllocateAddress` | SDK/CLI | Yes | Yes | Allocate an **Elastic** IP (optionally from BYOIP/IPAM pool) | any holder | **summary row BLANK — no resource type, no condition key (L86-87)** → cannot pin *which* EIP; `ec2:PublicIpAddress` key exists (L10136) but applies to the already-allocated `elastic-ip` resource, not allocation. Reclaim-squatting owned by hub; reconfirmed here. |
| `RunInstances` (`--secondary-private-ip-addresses` / `--count`) | SDK/CLI | Yes | Yes | Assign secondary IPs at launch | launcher | launch-path keys owned by Fleet/RunInstances plans |
| `ModifyNetworkInterfaceAttribute` | SDK/CLI | Yes | Yes | ENI attrs incl. SG set | holder | SG-per-ENI (Lens I, Area 5) |
| `ModifySubnetAttribute` (auto-assign public IP) | SDK/CLI | Yes | Yes | Toggle subnet public-IP auto-assign | holder | VPC-service action; influences ephemeral-pool draw (Area 3) |

**Console-hidden / under-surfaced knob:** `AllowReassignment` (and the EIP `AllowReassociation`) are *the* auth-weakening parameters here — the console surfaces them as a benign checkbox ("Allow the Elastic IP address to be reassociated", `managing-network-interface-ip-addresses.md:48`); the API accepts the boolean with, per the docs, **no condition key to deny it**. This is the inventory delta to chase first.

---

## 5. Recommended Areas of Focus

### Area 1 — Secondary private-IPv4 cross-ENI / cross-account takeover via `AllowReassignment` *(HEADLINE)*
**Lens A / X / S. Severity-if-true: cross-account (shared subnet) = High–Critical; same-account cross-team = Medium–High (customer-exposure, intra-account).**

**Background.** `using-instance-addressing.md`: "secondary private IP addresses can be reassigned from one instance to another" and (Multiple IP addresses) "Secondary private IPv4 addresses that are assigned to a network interface **can be reassigned to another one if you explicitly allow it**." The mechanism is `AssignPrivateIpAddresses` with the **`AllowReassignment=true`** flag (`instance-secondary-ip-addresses.md`, `managing-network-interface-ip-addresses.md`): the caller names a **target** ENI (`--network-interface-id`) and a **specific IPv4** (`--private-ip-addresses`); when `AllowReassignment` is set, EC2 moves that IP even if it is currently assigned to a *different* ENI.

**Security Concern.** The IAM authorization for `AssignPrivateIpAddresses` is bound to the **target** `network-interface*` (keys `ec2:NetworkInterfaceID`/`ec2:Subnet`/`ec2:Vpc`/`aws:ResourceTag`, L4700). The API (`API_AssignPrivateIpAddresses`) takes **only** `NetworkInterfaceId` (target, Required=Yes) + `AllowReassignment` — there is **no `SourceNetworkInterfaceId`/owner parameter**, and the Errors section links only to generic `CommonErrors.md` (no action-specific "IP in use on another account's ENI" error documented). The **source** ENI that *loses* the IP is thus **not named in the request and has no documented authorization check**. The "explicitly allow it" consent is the **caller's** `AllowReassignment` flag — i.e. the party *gaining* the IP sets it, **not** the party losing it. If EC2 only validates the caller against the target ENI, then a caller who owns *any* ENI in a subnet can pull an in-use secondary private IPv4 off a victim ENI in the **same subnet** by naming that IP. Because subnets are **RAM-shareable across accounts** (VPC sharing), the same-subnet adjacency can be **cross-account** — and critically, the docs state the "participants must own any network interfaces that they specify" isolation rule **only for `RunInstances`/instance-lifecycle actions** (`using-vpc.md#ec2-shared-VPC-subnets`); **no equivalent ownership rule is documented for `AssignPrivateIpAddresses`/`AssignIpv6Addresses` against a pre-existing ENI** — the docs are silent on exactly the cross-account question, not reassuring.

**Impact amplifier (EIP rides along).** `API_AssignPrivateIpAddresses`: "When you move a secondary private IP address to another network interface, **any Elastic IP address that is associated with the IP address is also moved.**" So an Area-1 private-IP theft of a secondary IP that has an EIP associated **also steals the public Elastic IP** onto the attacker ENI — one call pivots both the private *and* public reachability of the victim service. Remapping is **asynchronous** (confirm via instance-metadata `network/interfaces/macs/<mac>/local-ipv4s`). Note also: "you can reassign the secondary private IPv4 address of **the primary network interface** to another network interface" — the primary ENI is not a safe harbor for its *secondary* IPs.

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** With only `ec2:AssignPrivateIpAddresses` on my own `eni-ATK`, I can call `assign-private-ip-addresses --network-interface-id eni-ATK --private-ip-addresses <IP-in-use-on eni-VIC> --allow-reassignment` and EC2 **moves the IP off `eni-VIC`** with no permission on `eni-VIC`. → **Mechanism:** `AssignPrivateIpAddresses` authz scoped to target ENI only (L4700); no source-ENI key; `AllowReassignment` caller-set. → **Oracle:** `describe-network-interfaces` shows the IP gone from `eni-VIC` and present on `eni-ATK`; a ping/ARP for that IP in-subnet now resolves to the attacker. Refute = `AccessDenied`/`InvalidParameterValue` citing the source ENI owner. → **Preconditions:** two ENIs in one subnet; attacker holds the action on its own ENI only. → **Cost:** trivial (two canary ENIs). → **Severity:** Medium–High intra-account.
- **Claim (cross-account escalation):** The same move works when `eni-VIC` is owned by **account A** and `eni-ATK` + the caller are **account B (participant)** in a **RAM-shared subnet**. → **Mechanism:** VPC-sharing co-residency + target-only authz. → **Oracle:** cross-account IP move confirmed via each account's `describe-network-interfaces`; attacker now answers traffic/ARP for a victim-account service IP. → **Severity:** **Critical** (cross-account intra-VPC impersonation / interception). **Stop condition:** confirm the move once on canary ENIs you own in both accounts; do not pivot to real traffic.
- **Claim (consent asymmetry):** The victim ENI's owner has **no setting to opt out** of being a reassignment source (no "disallow reassignment" ENI attribute is documented). → **Oracle:** search `list_ec2` + ENI attributes for any owner-side reassignment-block; absence confirms the asymmetry.

**Doc evidence:** `using-instance-addressing.md` (Multiple IP addresses bullets); `instance-secondary-ip-addresses.md:66-80`; `managing-network-interface-ip-addresses.md:48,64-70`; `list_ec2.md:4700`. **Doc-gap to settle live:** the docs never state whether `AssignPrivateIpAddresses` validates the *source* ENI's owner — this is THE question; `iam:SimulateCustomPolicy` cannot answer it (needs the real two-ENI call). Confirm the AllowReassignment semantics against `API_AssignPrivateIpAddresses` first.

### Area 2 — No IAM key to forbid reassignment or pin *which* private IP
**Lens S / U (AWS-owned enforcement-gap). Severity: Medium (the enabler that makes Area 1 un-guardrail-able).**

**Background & Concern.** Grep of all 10190 lines of `list_ec2.md`: **`AllowReassignment`, `ec2:PrivateIpAddress`, and `ec2:Ipv6Address` do not exist anywhere in EC2's condition-key catalog** (only `ec2:PublicIpAddress` L10136, for the `elastic-ip` resource — a different asset). The four assign/unassign actions carry only ENI-scoping keys (`ec2:NetworkInterfaceID`/`Subnet`/`Vpc`/tag). **Pointed contrast — the mechanism exists but was not applied here:** `ec2:AuthorizedUser` ("Filters access by an IAM principal that has permission to use a resource") **does exist** on EC2 and *is* wired onto `CreateNetworkInterfacePermission`/`CreateVerifiedAccessEndpoint` (L~5548/5718) — yet it is **absent** from all four private-IP/IPv6 assign/unassign actions. And `AssociateAddress`/`DisassociateAddress` carry `ec2:PublicIpAddress`/`ec2:AllocationId` to pin exactly *which* EIP — but the private-IP (re)assignment path has no equivalent to pin *which* IP. The capability to scope exists in the service; it simply is not attached to the reassignment primitive.

**High-level Test Scenarios:**
- **Claim:** An admin **cannot** write an identity/SCP policy that (a) denies `AssignPrivateIpAddresses` when `AllowReassignment=true`, or (b) restricts *which* private IPs may be (re)assigned — only *which ENI*. → **Oracle:** `iam:SimulateCustomPolicy` with a `Deny` keyed on a fabricated `ec2:AllowReassignment`/`ec2:PrivateIpAddress` → the condition is **silently ignored** (inert — the Lens-S "key does not exist" failure shape, cf. the `ec2:InterfaceType` precedent) and the Assign is Allowed. → **Severity:** Medium; it is the structural reason Area 1 has no least-privilege mitigation. In scope as an AWS-owned expressiveness gap (not a customer footgun — the key simply does not exist to be used).
- **Claim (binds-wrong-resource variant):** `ec2:Subnet`/`ec2:Vpc` on `AssignPrivateIpAddresses` evaluate to the **target ENI's** subnet/VPC, not the IP's prior owner — so even a subnet-scoped grant does not stop an in-subnet takeover (it *permits* it). → **Oracle:** Simulate a subnet-scoped Allow; confirm it authorizes a same-subnet reassignment. 

### Area 3 — Auto-assigned ephemeral public-IPv4 pool reuse → dangling-record hijack
**Lens A / M / EE / L. Severity: cross-tenant inheritance of trust pinned to the IP = High; pure cost = Low.**

**Background.** `using-instance-addressing.md` (Public IPv4 addresses): "A public IP address is assigned to your instance from **Amazon's pool** of public IPv4 addresses, and is **not associated with your AWS account**. When a public IP address is disassociated from your instance, it is **released back into the public IPv4 address pool, and you cannot reuse it.**" Release triggers: stop/hibernate/terminate; EIP-associate; etc. Plus: "If you use **dynamic DNS** … it might take up to **24 hours** … new instances might not receive traffic while terminated instances continue to receive requests."

**Security Concern.** A public IPv4 released by victim tenant A returns to the shared pool and is later **re-leased to a different tenant B** on a subsequent launch. Anything that still *points at that IP* — a stale DNS A-record, a partner/firewall IP allowlist, an OAuth/webhook callback keyed on source IP, a hardcoded peer — now resolves/trusts **attacker B's instance**. This is the classic cloud IP-reuse / "dangling IP" cross-tenant exposure, and the docs confirm the two preconditions (address not account-bound; released to a shared pool reused by others). The caller cannot *choose* the IP, which bounds targeting — but a motivated attacker can **cycle instances to land on a specific recently-released address** (land-grab, Lens EE), and the 24h DNS propagation window widens the dangling period.

**High-level Test Scenarios:**
- **Claim:** There is **no documented cooldown/hold-down** before a released ephemeral public IPv4 is re-leased to another account → a victim's just-released IP can be inherited by an attacker within the DNS-propagation window. → **Mechanism:** the "released back into the pool … cannot reuse it" + 24h-propagation sentences. → **Oracle (your own accounts):** in acct A, note the auto-assigned public IP of a running instance, then stop/terminate it; in acct B, launch/stop instances in a loop and record how often (and how soon) acct A's just-released IP reappears on an acct-B instance. A single reappearance confirms cross-account reuse with no owner binding. **Do not target a third party's IP or real DNS record.** → **Preconditions:** two canary accounts; auto-assign public IP on. → **Cost:** low (public-IPv4 hourly charge). → **Severity:** High (if a real deployment left a dangling record) — but the *finding* here is the **absence of a cooldown / targeting-resistance guarantee**, an AWS-owned design property, plus the operator-guidance gap (the page's "optimization" section never warns about dangling-record risk on release).
- **Claim (targeting / land-grab, Lens EE):** Repeated launch-stop cycling measurably biases which released addresses an attacker receives → specific-IP targeting is feasible, not purely probabilistic. → **Oracle:** measure hit-rate for a chosen just-released address vs random baseline.
- **Cross-ref (do not re-derive):** the **Elastic**-IP equivalent (reclaim a *specific* released EIP by address, `AllocateAddress --address` with no `ec2:PublicIpAddress` scoping on allocation) is owned by the hub; reconfirmed here that `AllocateAddress`'s summary row is blank (L86-87) so allocation is unscopable. The ephemeral-pool path differs: **no address choice at all**, but **also no account binding and an explicit "cannot reuse" recycle** — a cleaner cross-tenant inheritance story.

**Doc-gap to settle live:** cooldown duration (if any) and targeting bias — both measurable only empirically; mark "doc-gap — confirm live."

### Area 4 — Link-local address model: SG/NACL bypass of reserved host services + non-reserved VPC-routing seam
**Lens G / D / V / O. Severity: the SSRF-to-IMDS target itself is well-known (out-of-scope as a managed-host IMDS issue unless it reaches the service plane); the net finding is the **control blind spot** (Low–Medium) + a segmentation reasoning note.**

**Background.** `using-instance-addressing.md` (Link-local addresses): the reserved services (IMDS `169.254.169.254`, Route 53 Resolver `.253`, Time Sync `.123`, "AWS KMS servers") "run on the underlying host, not on the instance … you're communicating with either the Xen hypervisor or the Nitro controller. The underlying host handles traffic to these reserved addresses instead of forwarding it … **Security groups and network ACLs do not filter this traffic.**" And: "AWS does not reserve every IPv4 address in `169.254.0.0/16`. Traffic to a **non-reserved** address in this range **follows the applicable VPC route**. Your security groups and network ACLs **can** filter this traffic." IPv6 link-local `fe80::/10`.

**Security Concern & Scenarios:**
- **Claim (Lens O/U — control blind spot):** No SG or NACL can block an instance's egress to `169.254.169.254` (IMDS), `.253`, `.123`, or the KMS link-local endpoint, because the host answers out of band of the VPC data path. → **Mechanism:** the verbatim "Security groups and network ACLs do not filter this traffic." → **Oracle:** doc-confirmed; the *control* implication is that IMDS-exfil defenses must be instance-local (IMDSv2 hop-limit/`HttpTokens`, host firewall), never SG/NACL. This is a **documented blind spot**, worth stating so a defender does not build an SG-based IMDS egress control that silently does nothing. → **Severity:** Low–Informational (defensive-guidance gap); the actual SSRF-to-IMDS primitive is owned by instance-metadata plans and is out-of-scope as a managed-host concern unless a fetch reaches the **host/service plane** (then **hard stop**).
- **Claim (Lens V — segmentation/precedence):** For a **non-reserved** `169.254.x` the customer can add a VPC route; does any customer route for an address adjacent to the reserved set ever get **shadowed by** (or shadow) the host-intercept behavior, creating a confusion where traffic the customer believes is VPC-routed is host-intercepted or vice-versa? → **Mechanism:** the "does not reserve every address … follows the applicable VPC route" split. → **Oracle:** enumerate exactly which addresses are host-intercepted vs route-followed (the doc lists `.254/.253/.123` + KMS; the full reserved set is the question) and test whether a route to a near-reserved address behaves as documented. → **Severity:** Low unless a reserved service can be reached via an unexpected path (would be a host-plane finding → **hard stop**).
- **Claim (Lens D):** From the data plane, the only host services reachable are the enumerated link-local ones; nothing on this page suggests a *control-ENI* reachable from the instance. → mostly a **null** for data→control escape *on this page* (defer to ENI/secondary-network cluster in the hub). Named here so it is not an unexamined gap.

### Area 5 — SG-per-ENI (not per-IP) → added/stolen secondary IP inherits the ENI's allow rules
**Lens I. Severity: Medium (amplifier for Area 1).**

**Background.** `using-instance-addressing.md`: "You associate security groups with **network interfaces, not individual IP addresses**. Therefore, each IP address you specify in a network interface is subject to the security group of its network interface."

**Concern & Scenario.** A secondary private IPv4 **moved onto the attacker ENI** (Area 1) immediately inherits the attacker ENI's security groups — and, conversely, an IP added to a victim ENI rides the victim's existing allow rules. **Claim:** after an Area-1 takeover, the stolen IP is reachable per the *attacker's* SG, so the attacker can expose a service on the victim's former IP with its own (looser) rules, or receive connections that peers send to that IP under the assumption of the victim's (tighter) posture. → **Oracle:** confirm the moved IP answers on ports the attacker ENI's SG allows but the victim's did not. → **Severity:** Medium; chains with Area 1 to raise the impact (impersonation + attacker-chosen exposure).

### Area 6 — IPv6 reassignment / primary-IPv6 immutability lifecycle
**Lens A / X / U. Severity: Low–Medium.**

**Background.** "An IPv6 address **cannot be reassigned** to another network interface — you must first **unassign** it." Primary IPv6: "After you assign a primary IPv6 address, you can't change it … until the instance is terminated or the network interface is detached" (`managing-network-interface-ip-addresses.md:36`).

**Concern & Scenarios:**
- **Claim:** The IPv6 "must unassign first" rule means there is **no `AllowReassignment`-style forced move for IPv6** → the Area-1 primitive does *not* extend to IPv6 (a genuine narrowing — the attacker must first `UnassignIpv6Addresses` on the victim ENI, which **is** authz-scoped to that ENI). → **Oracle:** confirm `UnassignIpv6Addresses` requires the action on the victim ENI (L9690) → IPv6 takeover needs a permission the private-IPv4 path does not. Documents the asymmetry (IPv6 is *safer* here) rather than a bug. → **Severity:** Informational (scoping note that prevents over-claiming Area 1 onto IPv6).
- **Claim (Lens L minor):** "the entire operation fails if one of the IP addresses can't be assigned" (all-or-nothing multi-IP assign) + per-ENI IP caps (`AvailableIpPerENI`) → a batch assign can be used to probe which specific IPs are free (existence oracle via the failure) and secondary-IP caps enable a subnet-address-exhaustion self-DoS. → **Severity:** Low.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Pull an in-use secondary private IPv4 off a foreign ENI (same subnet) | `AssignPrivateIpAddresses` + `AllowReassignment` | "reassigned … **if you explicitly allow it**" — test whether "you" is the *gaining* caller only (no source-owner consent) |
| Same, cross-account in a RAM-shared subnet | VPC sharing + target-only authz | per-ENI IAM scoping (`ec2:NetworkInterfaceID`) — test that it does **not** bind the source ENI |
| Prove no policy can forbid reassignment / pin the IP | IAM `list_ec2` | absence of `AllowReassignment` / `ec2:PrivateIpAddress` keys (Simulate) |
| Inherit a released ephemeral public IPv4 with live trust | shared public-IPv4 pool | "not associated with your account … released … cannot reuse" — test for cooldown / targeting bias |
| Build an SG/NACL control for IMDS egress (and watch it do nothing) | link-local reserved services | "Security groups and network ACLs **do not filter** this traffic" |
| Expose the moved IP under the attacker's SG | ENI security-group binding | "security groups … **not individual IP addresses**" |

---

## 7. Out-of-Scope Risk Categories
- **IMDS on managed/customer instances** as a generic SSRF target (owned by instance-metadata plans); in scope here **only** as the SG/NACL control-blind-spot *fact* (Area 4) — and the **host/Nitro side of any link-local service is a hard-stop** disclosure boundary, never a test target.
- **Elastic IP** cross-account transfer, reclaim-by-address squatting, BYOIP, `DeleteNetworkInterfacePermission`, shared-VPC owner/participant isolation, `Describe*NetworkInterface*` scoping — **owned by the `ec2-networking` hub**; cross-referenced only.
- **Launch-path** secondary-IP assignment (`RunInstances --secondary-private-ip-addresses`) IAM — owned by RunInstances/Fleet plans.
- Customer-authored IAM policies that over-grant `ec2:AssignPrivateIpAddresses` on `*` — a customer footgun (out of scope); the in-scope point is that **AWS provides no condition key** to scope it tighter (Area 2).
- Single-tenant self-DoS via subnet-IP exhaustion (Area 6) — Low/out-of-scope except as a noisy-neighbor amplifier in a shared subnet.
- Pure cost abuse of public-IPv4 charges — Low.

## 8. Null hypotheses / doc gaps (lenses that did not fire, pages named)
- **Lens Q (upload):** N/A — read main + `managing-network-interface-ip-addresses.md`, `instance-secondary-ip-addresses.md`, `config-windows-multiple-ip.md`, `working-with-ip-addresses.md`, `working-with-ipv6-addresses.md`; no file/image/blob field on any addressing API.
- **Lens G (SSRF via a service-dereferenced field):** N/A for the page's own APIs — IP values are identifiers, not fetched URLs; the only server-side-reachable targets are the link-local host services (Area 4, distinct mechanism). Pages: all 5 above.
- **Lens B/C/R/T (PassRole / credential-vending / IAM-artifact / stored-secret):** N/A — no role-ARN input, no printed policy JSON, no generated/persisted secret on these pages. Pages: main + children. (Sample-policy/PassRole surface lives on the EC2-prerequisites + hub pages — cross-ref.)
- **Lens F/K/W/FF/DD/BB/CC (injection / LLM / attestation / token / cache / canonicalization / upstream-context):** N/A — no translation layer, LLM, attestation gate, JWT/OIDC, caching layer, multi-parser request path, or asserted-identity header on the addressing surface.
- **Lens P (proofing/registration):** the only "consent" primitives are the `AllowReassignment`/`AllowReassociation` flags — audited under Area 1/§3 as an authorization-asymmetry question, not a registration workflow.
- **Doc-gaps to confirm live before investing:** (1) **source-ENI owner check** on `AssignPrivateIpAddresses` reassignment (the Area-1 headline — settleable only with two real ENIs; `DryRun`/Simulate cannot answer it); (2) **cross-account** behavior in a RAM-shared subnet; (3) **cooldown / targeting bias** of the ephemeral public-IPv4 pool (Area 3 — empirical); (4) the **exact reserved link-local set** beyond `.254/.253/.123`+KMS (Area 4). Confirm `AllowReassignment` semantics against `API_AssignPrivateIpAddresses` and re-check all cited `list_ec2` lines live (offline==online held on 2026-10-15, but the IAM reference changes).

---
Cross-references: [[ec2-networking-attack-research-plan]] (hub — EIP/BYOIP/ENI/shared-VPC), [[project-aws-research-plans]], [[reference-aws-iam-service-auth-ref-url]].
