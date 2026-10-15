# EC2 Instance Hostnames & Domains — Attack / Research Plan

> **Scope anchor (target page):** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/understanding-ec2-instance-hostnames-domains.html`
> **Primary surface page:** `hostname-types.html` (the real meat; the target page is a thin FQDN-anatomy intro)
> **Position in corpus:** page-level child of the **EC2 Networking hub** (`ec2-networking-attack-research-plan.md`). Siblings already covering adjacent IP surface: `using-instance-addressing`, `working-with-ip-addresses`, `working-with-ipv6-addresses`, `instance-secondary-ip-addresses`, `using-regions-availability-zones`. **This plan OWNS the DNS/hostname naming layer; it DEFERS the underlying IP-assignment/takeover primitives to those siblings and references them rather than re-deriving them.**
>
> **⚠ Overlapping sibling — read first: `ec2-instance-naming-attack-research-plan.md`** (covers the *parent* topic page `ec2-instance-naming.html`, which also parents `hostname-types.html`). That plan already owns: the **IAM key-table detail** (its L8974-9028 read lists MORE keys on `ModifyPrivateDnsNameOptions` than §3 below — `ec2:InstanceID`, `ec2:InstanceType`, `ec2:Tenancy`, `ec2:MetadataHttpTokens` etc. in addition to the generic `ec2:Attribute`), the **correction of a hub-fragment "zero conditionability" drift error** (the Modify*DnsNameOptions actions ARE tag/ARN-scopable — see §3 caveat), the public `ip.aws` surface, dangling-DNS reuse, the IP-name-A-record guarantee, and subnet-owner hostname-type control. **The two plans AGREE on the headline (no condition key scopes hostname *type* or the DNS A/AAAA *toggle values* — only generic/`ec2:Attribute` levers exist, likely listed-but-inert → Lens S).** This plan's genuine NET-NEW contribution over that sibling is **LEAD A1 (data-plane cross-account DNS *resolution* leak in a shared VPC)** — the sibling frames shared-VPC only as control-plane subnet-owner *influence*, never the `.2`-resolver cross-account identifier disclosure. Treat §5 LEAD A1 + the reversible-public-name framing as the delta; cross-reference the sibling for everything else rather than trusting §3's narrower key list.
> **Method:** AWS `security-questionbuilder` (6-step boundary-first). Documentation-only. Produces leads a hunter (`aws-vuln-hunter`) executes against an authorized account later. Online `.md` twins verified byte-identical to the offline mirror for `hostname-types` and the target page — **no drift**.

---

## §0 — How to use this plan

Read §1–§4 for the mental model, then execute §5 (Recommended Areas of Focus) — that is the ranked hit-list. Each lead in §5 is a falsifiable claim with (a) the exact doc sentence that makes it plausible, (b) a confirm/refute oracle a hunter can run in a lab account, and (c) severity-if-true. §6 is the threat model, §7 is out-of-scope, §8 is the null hypotheses (lenses checked and found not to fire, with the pages read — so a follow-up agent does not re-walk them).

**The one-line headline** (if you read nothing else): *Across the entire EC2 IAM surface there is **no condition key** that scopes which hostname type an instance/subnet/ENI gets, nor whether a resource-name DNS A/AAAA record is answered. These are security-relevant DNS-exposure toggles that an org literally cannot write a guardrail for.* Everything else radiates from that fact plus the reversible public `ip.aws` name and the silent cross-account resolution gap in shared VPCs.

---

## §1 — Pentest Objectives

1. **Determine whether an org can constrain hostname/DNS exposure via IAM at all** (Lens S/U) — the headline. If not, that is itself the deliverable: a documented guarantee-vs-enforceability gap for every EC2 customer.
2. **Confirm cross-account DNS data-plane resolution scope in a RAM-shared VPC** (Lens A/V) — can participant account B resolve participant account A's resource-name (instance-ID-bearing) and IP-name (private-IPv4-bearing) FQDNs via the .2 resolver, yielding co-tenant instance-ID / private-IP enumeration the control-plane isolation statement never covers?
3. **Confirm the public `ip.aws` / `compute.amazonaws.com` hostname is a reversible, internet-resolvable public-IP↔hostname oracle** and chase the **dangling-DNS / cross-account IP-reuse** consequence (Lens EE/AA) that the docs establish mechanically but never warn about.
4. **Confirm the IP-name A-record "always answered, no suppression knob" guarantee** (Lens U) and map what an operator can and cannot turn off.
5. **Map the new, least-audited surface** — `modify-public-ip-dns-name-options` (ENI-level, net-new), the `ip.aws` namespace, base36 encoding — and ask whether the new ENI-level control introduces an authz asymmetry vs the legacy instance/subnet-level private-name controls.

---

## §2 — Components, Assets, and Design

### What the feature is
EC2 attaches DNS hostnames to instances/ENIs. Two independent axes:

- **Private hostnames** (resolve inside the VPC via the Amazon-provided Route 53 Resolver at VPC-CIDR `+2`):
  - **IP name** (legacy): `ip-<private-ipv4-dashed>.<region>.compute.internal`, e.g. `ip-10-24-34-0.us-west-2.compute.internal`. **Embeds the private IPv4.** A record **always answered, not suppressible.**
  - **Resource name** (RBN): `<instance-id>.<region>.compute.internal`, e.g. `i-0123456789abcdef.us-west-2.compute.internal`. **Embeds the EC2 instance ID.** A/AAAA records **individually suppressible.**
- **Public hostnames** (split-horizon: resolve to public IP from the internet, to private IP inside the VPC):
  - **Legacy IPv4:** `ec2-<public-ipv4-dashed>.<region>.compute.amazonaws.com`.
  - **New `ip.aws` forms** (dual-stack / IPv4-only / IPv6-only): a **base36 encoding** of the primary public IPv6 GUA and/or primary public IPv4. Doc example: label `q3cdpO` decodes to IPv4 `52.54.55.56`.

### Identifiers and their shape (matters for enumeration — Lens A/EE)
- **Instance ID** inside resource name: `i-` + 17 hex chars → high entropy, not brute-forceable blind, but **deterministically derivable from any leaked instance ID**.
- **Private IPv4** inside IP name: low entropy, **trivially enumerable across a subnet CIDR**.
- **Public IPv4/IPv6** inside public name: **reversibly encoded** — hostname→IP is a documented decode, IP→hostname a documented encode. Public names are **globally unique and internet-resolvable**.

### Control surface (who sets what, at which level)
| Setting | API (instance) | API (subnet default) | Level | IAM scopability (see §3) |
|---|---|---|---|---|
| Private hostname type (ip-name / resource-name) | `ModifyPrivateDnsNameOptions` + `RunInstances.PrivateDnsNameOptions.HostnameType` | `ModifySubnetAttribute --private-dns-hostname-type-on-launch` | instance / subnet | **unscopable** (no DNS condition key) |
| Resource-name DNS A record on/off | `ModifyPrivateDnsNameOptions` / `RunInstances…EnableResourceNameDnsARecord` | `ModifySubnetAttribute --enable-resource-name-dns-a-record-on-launch` | instance / subnet | **unscopable** |
| Resource-name DNS AAAA record on/off | …`EnableResourceNameDnsAAAARecord` | `ModifySubnetAttribute --enable-resource-name-dns-aaaa-record-on-launch` | instance / subnet | **unscopable** |
| Public hostname type (dual-stack / ipv4 / ipv6) | **`ModifyPublicIpDnsNameOptions`** (net-new) | — | **network-interface** | **unscopable** for DNS (has generic keys only) |
| DNS prerequisite | VPC attrs `EnableDnsHostnames` + `EnableDnsSupport` | (VPC-level) | VPC | owner-only in shared VPC |

### Trust zones in play
- **Customer account / VPC** (owns instances, reads/writes hostname options for own resources).
- **Shared-VPC owner vs participant accounts** (RAM): owner sets VPC/subnet DNS attributes and subnet-level hostname defaults; participants launch instances but cannot modify VPC/subnet attributes.
- **Amazon-provided DNS resolver** (.2) — a service-plane component operating at **VPC scope**; the account-awareness of its resolution is the central open question.
- **Public internet** (resolves public hostnames to public IPs; the public-IP pool is cross-account/shared).

### Pipeline (DNS exposure)
```
RunInstances / ModifyPrivateDnsNameOptions / ModifyPublicIpDnsNameOptions / ModifySubnetAttribute(defaults)
        │  (no IAM DNS condition key anywhere — §3)
        ▼
Instance/ENI hostname record set  ──► Route 53 Resolver (.2, VPC-scoped) ──► private A/AAAA (in-VPC)
        │                                                                    (IP-name A: always on)
        └──► public hostname (ip.aws / compute.amazonaws.com, base36/dotted) ──► public internet (split-horizon)
                     │
                     └─ public IP sourced from shared, NOT-account-bound pool  ──►  dangling-DNS on IP reuse
```

---

## §3 — API / Interface Inventory

| Name | Mutating | Facing | New/Existing | Authorized callers | Resource type (list_ec2) | DNS-relevant condition keys | Notes |
|---|---|---|---|---|---|---|---|
| `RunInstances` | yes | external | existing | account principals | many | **none for hostname/DNS** (`list_ec2.md` L9585-9609 — no hostname/DNS key on any row) | `PrivateDnsNameOptions{HostnameType, EnableResourceNameDnsARecord, EnableResourceNameDnsAAAARecord}` sub-object is accepted but **not governable by IAM** |
| `ModifyPrivateDnsNameOptions` | yes | external | existing | instance owner | `instance*` | **none** — only generic `ec2:Attribute` / `ec2:Attribute/${AttributeName}` + standard tag/AZ/Region/Subnet/Vpc (L8974-8978) | sets instance private hostname type + A/AAAA toggles |
| `ModifyPublicIpDnsNameOptions` | yes | external | **NEW** | ENI owner | `network-interface*` | **none for DNS** — `aws:ResourceTag`, `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:AvailabilityZone`, `ec2:Region`, `ec2:ResourceTag`, `ec2:Subnet`, `ec2:Vpc` (L8980-8984) | **PRESENT in list_ec2 = confirmed shipped.** Required params `HostnameType` + `NetworkInterfaceId`. Controls public `ip.aws` form at **ENI level** — a different granularity than legacy private controls |
| `ModifySubnetAttribute` | yes | external | existing | subnet owner | `subnet*` | **none for DNS** — adds `ec2:SubnetID`/`ec2:Vpc`/`ec2:AvailabilityZone(Id)` + generic `ec2:Attribute` (L9024-9028) | sets subnet-level launch defaults for ALL three private toggles; owner-only in shared VPC |
| `DescribeInstances` | no | external | existing | account principals | *(blank resource type)* | `ec2:Region` only (L6996-7000) | **unscopable read oracle** — returns `PrivateDnsName`, `PublicDnsName`, hostname options |
| `DescribeNetworkInterfaces` | no | external | existing | account principals | *(blank)* | `ec2:Region` only (L7218-7222) | **unscopable read oracle** — `--query NetworkInterfaces[].PublicIpDnsNameOptions` |
| `DescribeNetworkInterfaceAttribute` | no | external | existing | account principals | *(blank)* | `ec2:Region` only (L7206-7210) | **unscopable read oracle** |
| Route 53 Resolver (.2) | no | in-VPC data plane | existing | anything in the VPC | n/a (not an IAM-gated API) | n/a | the **data-plane** resolution path; account-awareness UNDOCUMENTED (Lead A1) |

**⚠ §3 key-list caveat:** the "condition keys" column above is the SUBSET this plan's IAM subagent captured. The overlapping sibling `ec2-instance-naming-attack-research-plan.md` read the same rows (L8974-9028) and enumerated MORE standard keys on these actions (e.g. `ec2:InstanceID`/`ec2:InstanceType`/`ec2:Tenancy`/`ec2:MetadataHttpTokens` on `ModifyPrivateDnsNameOptions`). **This does NOT change any finding** — the headline is the *absence of a DNS-value key*, which both reads confirm. Trust the sibling's fuller list for the exact scopable keys; trust the sweep below for what is absent.

**IAM-reference whole-file sweep result (authoritative, `list_ec2.md`):** ZERO hits for `PrivateDnsHostnameType`, `EnableResourceNameDnsARecord`, `EnableResourceNameDnsAAAARecord`, `HostnameType`, or `DnsHostnameType` as condition keys. The only `Dns`-named keys in all of EC2 are the VPC-endpoint `ec2:VpceServicePrivateDnsName`-class keys (L10176/10177/10180) — unrelated. `ec2:Attribute` is defined L10051, `ec2:Attribute/${AttributeName}` L10052.

---

## §4 — Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Shared-VPC participant account B | Participant account A's instance identity (instance ID / private IP) | `.2` resolver answering A's resource-name/IP-name FQDN to B's query (data plane) | **B resolves (or reverse-resolves) an FQDN that reveals A's instance ID or private IP → cross-account identifier disclosure the control-plane isolation statement never covered** |
| Any internet host | A customer's current public IP / instance reachability | Reversible decode of public `ip.aws`/`compute.amazonaws.com` hostname | Deriving the live public IP from a known hostname, or deriving the hostname from a target IP → **recon oracle** (low-sev alone; feeds the next row) |
| New tenant that receives a recycled public IP | Trust pinned to the *previous* owner's public hostname | Public IP released to shared pool → reassigned → identical derived hostname now resolves to the new tenant | **A TLS cert / firewall allowlist / allow-rule keyed on the stale hostname now authorizes or routes to a different account's instance → dangling-DNS trust transfer** |
| Org security team (would-be author of a guardrail) | The hostname-type / DNS-A-record toggles | Any SCP/IAM policy attempting `Condition` on hostname type or DNS record | **No condition key exists → the policy cannot be written → the control is unenforceable** (guarantee-vs-mechanism gap) |
| Instance operator wanting to suppress private-IP exposure | The IP-name A record | (none — there is no API/knob) | **A record answered unconditionally in-VPC with no off switch → documented control gap** |
| VPC-share participant | Own instances' DNS/hostname generation | Depends entirely on owner-set `EnableDnsHostnames`/`EnableDnsSupport` + subnet defaults | Participant's DNS posture is dictated by an attribute the participant can only *describe*, never modify → **control-ownership asymmetry** |
| Any customer surface | **Amazon's `.2` resolver internals / public-IP pool mechanics** | — | **HARD STOP** — reaching AWS service-plane internals (resolver host, pool allocator) is out-of-scope; stop and flag. |

---

## §5 — Recommended Areas of Focus (ranked leads)

### ★ LEAD S/U-1 (HEADLINE) — No IAM condition key scopes hostname type or resource-name DNS record toggles, anywhere in EC2
- **Claim:** An organization cannot write an SCP/IAM policy that forces resource-name (RBN) hostnames, forbids IP-name hostnames (which leak private IPv4), or forces resource-name DNS A/AAAA records off — because EC2 exposes no condition key for any of these on `RunInstances`, `ModifyPrivateDnsNameOptions`, `ModifyPublicIpDnsNameOptions`, or `ModifySubnetAttribute`.
- **Mechanism (doc evidence):** `list_ec2.md` whole-file sweep (§3) — zero hits for the five candidate keys; the only governance hooks are the generic `ec2:Attribute` / `ec2:Attribute/${AttributeName}` pair, which key on the *attribute being modified*, not its *value*.
- **Confirm/Refute oracle:**
  1. Attempt an IAM policy with `Condition: {StringEquals: {"ec2:Attribute/privateDnsHostnameType": "resource-name"}}` (and the DNS-record attribute names) on `ModifyPrivateDnsNameOptions` / `ModifySubnetAttribute`; observe whether the condition ever actually gates the call or is silently ignored (policy-simulator + live call with a disallowed value).
  2. **Case-sensitivity fail-open sub-test (known EC2 corpus pattern):** `ec2:Attribute/${AttributeName}` is matched against the exact attribute token; if the real token differs in case/spelling from what an operator guesses (e.g. `privateDnsHostnameType` vs `PrivateDnsHostnameType`), the condition **fails open** (no match → not denied). Enumerate the exact attribute-name tokens these APIs emit and test whether a plausibly-written Deny misses them.
  3. Confirm there is no `aws:RequestTag`-style indirect lever either.
- **Severity if true:** Medium-High as a *control gap* affecting **every EC2 customer** — "disable IP-name hostnames fleet-wide" and "never answer private-IP A records" are reasonable least-exposure guardrails that are simply inexpressible. This is the plan's primary deliverable even if every other lead refutes.
- **Cross-ref:** fits the hub's recurring "generic `ec2:Attribute` is the only lever; value-level scoping impossible" theme (see `ModifySubnetAttribute` note in `project-aws-research-plans`).

### ★ LEAD A1 (HIGHEST-VALUE live test) — Cross-account DNS resolution in a shared VPC leaks co-tenant instance IDs / private IPs
- **Claim:** In a RAM-shared subnet, participant account B can resolve participant account A's **resource-name** FQDN (→ A's instance ID) and **IP-name** FQDN (→ A's private IPv4) via the `.2` resolver, and possibly reverse-resolve a co-tenant private IP to its owning account's name — none of which the shared-VPC isolation statement forbids.
- **Mechanism (doc evidence):** `AmazonDNS-concepts.md:21` — the resolver is reached at VPC-CIDR+2 and resolves Amazon-provided private hostnames **"for the VPC"** (VPC scope, no per-account filter stated). `vpc-sharing.md:8` — isolation is explicitly **only** "participants cannot view, modify, or delete *resources*" (control-plane / API, says nothing about name resolution). `vpc-share-limitations.md` enumerates participant/owner boundaries for flow logs, ENIs, route tables, SGs, subnets — **DNS resolution scope is absent from the whole list.** `using-vpc.md:48-52` — EC2 shared-subnet notes restrict only start/stop/terminate/describe. **Reverse DNS (PTR) of a co-tenant IP: entirely silent.**
- **Confirm/Refute oracle:** In an account owning a shared VPC + a participant account, launch instances in each; from the participant, (a) `dig <peer-instance-id>.<region>.compute.internal` and `<peer-private-ipv4-dashed>` IP-name against `.2`; (b) attempt PTR on a co-tenant private IP. **A non-empty answer that reveals the other account's instance ID or private IP = confirmed cross-account identifier disclosure.** Compare against the control-plane expectation (`DescribeInstances` from the participant must NOT show the peer).
- **Severity if true:** High — turns a documented control-plane isolation guarantee into a data-plane leak of another account's instance IDs (which then feed LEAD S/U-1's deterministic resource-name derivation and sibling IDOR leads) and private IPs. Verdict in docs is **DOC-GAP** (neither confirmed nor denied), which is exactly the kind of silent boundary this method targets.
- **Cross-ref:** disclosure/segmentation; coordinate with the hub's shared-VPC isolation theme and `using-regions-availability-zones` only insofar as both note shared-VPC participant limits — but **this DNS-resolution angle is net-new and owned here.**

### ★ LEAD EE/AA-1 — Public `ip.aws` hostname is a reversible public-IP oracle feeding cross-account dangling-DNS trust transfer
- **Claim (two linked):**
  (a) The public hostname is a documented, bidirectional, internet-resolvable encode/decode of the public IP — a stable recon oracle.
  (b) Because the public IP comes from a **shared pool not bound to any account**, once released and reassigned the *identical* derived hostname resolves to a **different tenant**, so any trust pinned to that hostname (TLS SAN, firewall allowlist, allow-rule) silently follows the IP to the new owner.
- **Mechanism (doc evidence):** `hostname-types.md:47-49` — base36 label *is* the public IP ("`q3cdpO` is resolved to the IPv4 address of 52.54.55.56"); IPv4 `compute.amazonaws.com` form is a reversible dotted→hyphen transform (L68-71). `hostname-types.md:12` + target page L24 — public FQDNs are "accessible from the public internet" / "globally unique." `using-instance-addressing.md:54` (load-bearing) — public IP "is **not associated with your AWS account** … released back into the public IPv4 address pool." `hostname-types.md:76` ("Important") — changing the primary public IP makes "the previously-generated public hostname **will no longer be valid**." The cross-account-reuse *consequence* is **never warned about** in any page = DOC-GAP.
- **Confirm/Refute oracle:** (a) Decode a known `ip.aws`/`ec2-*` hostname to its IP and vice-versa (pure doc-math, trivially confirmable). (b) In a lab: allocate → release a public IP, re-allocate repeatedly, observe whether the same IP (hence same hostname) can land in a second account, and whether DNS for the old hostname now points at the new instance. Documented mitigation to note: `Using_Elastic_Addressing_Reverse_DNS.md:12` — an EIP with a reverse-DNS record is "locked to your account and cannot be released."
- **Severity if true:** (a) Low alone (recon). (b) Medium-High where a hostname-pinned trust exists — classic dangling-DNS/subdomain-takeover shape, cross-account.
- **Cross-ref:** the public-IP *pool/release/takeover primitive* itself is OWNED by `using-instance-addressing` (ephemeral public-IPv4 pool reuse / dangling-DNS) and `working-with-ip-addresses`. **This plan owns only the hostname-derivation/reversibility layer on top of it** — reference, don't re-derive.

### LEAD U-2 — IP-name A record is answered unconditionally, with no suppression knob
- **Claim:** An operator who must use IP-name hostnames (or whose subnet default is IP-name) cannot prevent the private-IPv4 A record from being answered inside the VPC — there is no API/flag, unlike the resource-name form.
- **Mechanism (doc evidence):** `hostname-types.md:286` — *"For private DNS hostnames based on IP names, you cannot configure whether a DNS A record query for the instance is responded to or not. DNS A record queries are **always** responded to irrespective of the guest OS hostname settings."* Contrast: resource-name A/AAAA are suppressible via the `--enable-resource-name-dns-a/aaaa-record` flags (L367-371, 424-429). `hostname-types.md:314` — "Enable IP name IPv4 (A record) … selected automatically and can't be changed." The only escape is an IPv6-only subnet, which forces resource name (L256, 307).
- **Confirm/Refute oracle:** Confirmed in docs. Live: attempt every `modify-private-dns-name-options` / `modify-subnet-attribute` combination against an IP-name instance and show the A record still resolves. **Any config that suppresses it refutes.**
- **Severity if true:** Low-Medium — a guarantee-vs-control gap (private IPv4 always discoverable via DNS for IP-name instances), compounds LEAD A1 in shared VPCs.

### LEAD X/S-3 — New ENI-level public-name control vs legacy instance/subnet private-name control: granularity & authz asymmetry
- **Claim:** `ModifyPublicIpDnsNameOptions` operates at the **network-interface** level and is net-new, whereas the private-name controls live at instance/subnet level. This split (plus the fact that the new API carries `ec2:Subnet`/`ec2:Vpc`/tag keys but still no DNS-value key) may let a principal who owns/attaches an ENI set public-name behavior independent of instance-level or subnet-default governance — an under-tested parity gap.
- **Mechanism (doc evidence):** `ModifyPublicIpDnsNameOptions` in `list_ec2.md` L8980-8984 (`network-interface*`, required `NetworkInterfaceId`); `hostname-types.md:122-229` (new API/cmdlet/`PublicIpDnsNameOptions` ENI field). Legacy private controls at instance (`ModifyPrivateDnsNameOptions`, `instance*`) and subnet (`ModifySubnetAttribute`, `subnet*`).
- **Confirm/Refute oracle:** Test whether a principal permitted `ModifyPublicIpDnsNameOptions` on an ENI (but not instance/subnet DNS actions) can change the instance's public hostname form; test whether a secondary/attached ENI owned via a different principal diverges from the subnet default; check the undocumented/most-permissive `HostnameType` enum value for warnings.
- **Severity if true:** Low-Medium — hardening/least-privilege parity gap. Flagged primarily because this is the **least-audited (newest) surface** per the subagent's new-feature callout.

### LEAD V/A-4 (secondary) — Participant DNS posture is owner-controlled and only describable
- **Claim:** A shared-VPC participant's hostname generation and resolution behavior is entirely gated by `EnableDnsHostnames`/`EnableDnsSupport` and subnet hostname-type defaults that only the **owner** can set; the participant can describe but not change them — an undocumented control-ownership coupling.
- **Mechanism (doc evidence):** `hostname-types.md:81, 175` + `AmazonDNS-concepts.md:65-73` (both VPC attrs required, else no hostnames / no resolution). `vpc-share-limitations.md:64` — "Participants cannot modify VPCs or their related attributes. Only the VPC owner can … can describe VPCs, their attributes." L57 — participants can't modify shared subnets/attributes either. No page connects the two facts.
- **Confirm/Refute oracle:** As a participant, attempt to toggle these attrs (expect deny) and confirm instance DNS posture tracks the owner's setting with no participant override.
- **Severity if true:** Low — documents a coupling; mainly context for LEAD A1. **DOC-GAP** on the explicit statement.

### LEAD O-5 (low) — IMDS public-IP/hostname refresh data flow
- **Claim/finding:** Changing the primary public IPv4 forces an IMDS refresh so `public-hostname`/`public-ipv4` stay current (`hostname-types.md:76`). **Low security signal** — keeps IMDS consistent, no cross-tenant/stale-leak path evident in docs. Recorded so a follow-up agent does not re-investigate. Only worth a glance if IMDSv1 exposure on this instance is already in play (see sibling IMDSv1 findings in `working-with-ipv6-addresses` / spot/fleet examples).

---

## §6 — Threat Model (attacker goals → path → evidence)

1. **Co-tenant recon in a shared VPC** → launch participant instance → query `.2` for peer resource-name/IP-name FQDNs (LEAD A1) → obtain peer instance IDs + private IPs → feed resource-name derivation (LEAD S/U-1 implies IDs → FQDNs deterministically) and sibling identifier-based IDORs. **Evidence:** DNS answer revealing another account's instance ID / private IP.
2. **Internet recon → dangling trust** → decode target's public hostname to current IP, or watch a released IP get re-used (LEAD EE/AA-1) → inherit any hostname-pinned trust (TLS/allowlist) belonging to the prior tenant. **Evidence:** stale hostname resolving to attacker-controlled recycled IP.
3. **Guardrail evasion / inexpressible control** → org believes it can force RBN-only + A-records-off via SCP → no condition key exists (LEAD S/U-1) → every instance can still be launched with IP-name hostnames leaking private IPv4 (LEAD U-2). **Evidence:** policy-sim shows the condition never gates; live launch with disallowed value succeeds.
4. **ENI-level public-name override** → principal with only ENI DNS permission flips public hostname form outside instance/subnet governance (LEAD X/S-3). **Evidence:** public hostname changes via `ModifyPublicIpDnsNameOptions` without instance/subnet DNS permission.

---

## §7 — Out of Scope / Hard Stops

- **Live resolution against any account you are not authorized to test.** All DNS/API testing in §5 runs only in the authorized lab accounts with synthetic instances/canary data.
- **AWS service-plane internals:** the `.2` Route 53 Resolver host, the public-IP pool allocator, DNS backend. Reaching or manipulating these is a hard stop — preserve evidence, flag for disclosure, do not probe.
- **No modification/termination of any resource you did not create.** Confirm existence of a leak (e.g. a resolvable co-tenant FQDN) and stop — do not act on the resolved target.
- **The IP-assignment/takeover primitives** (allocating/releasing public IPs, EIP transfer, secondary-IP reassignment) are OWNED by sibling plans; execute those via their plans, not here. This plan confirms only the DNS/hostname layer.
- **DNS enumeration / port scanning / subdomain brute of real AWS ranges** — out of scope (HTTP/application + authorized-account API/DNS only).

---

## §8 — Null Hypotheses (lenses checked, found not to fire — with pages read)

- **Lens F (translation-layer / query injection):** N/A. Hostname strings are structured encodings (base36/dotted-IP), not a customer-authored query language fed to a downstream interpreter. Pages read: `hostname-types.md`, target page, `AmazonDNS-concepts.md`. No injection seam.
- **Lens G (SSRF / server-side dereference):** N/A. No field on these APIs is a URL/host the service fetches/unfurls server-side; hostnames are generated by AWS, not supplied-and-dereferenced. Pages read: `hostname-types.md`, `API_ModifyPublicIpDnsNameOptions.md`, `API_PrivateDnsNameOptionsRequest.md`.
- **Lens Q (uploaded blob / parser):** N/A. No blob/file input in this surface. Pages read: the two API-reference objects above.
- **Lens B/C (PassRole / credential vending):** N/A. No role-ARN input, no STS/session-policy construction in the hostname APIs. Pages read: `list_ec2.md` rows for all four mutating APIs (no role/PassRole key).
- **Lens P (gate-before-privileged-state-change / OTP):** N/A. No challenge/code/uniqueness gate in hostname config. Pages read: `hostname-types.md` scenarios.
- **Lens D (data→control-plane escape):** Partially folded into LEAD A1 (data-plane resolver reaching cross-account identity) but no evidence of reaching control-plane *APIs* from the DNS data path. Pages read: `AmazonDNS-concepts.md`, `vpc-sharing.md`, `vpc-share-limitations.md`.
- **Headline positive lenses that DID fire:** S/U (LEAD S/U-1, U-2), A/V (LEAD A1, V/A-4), EE/AA (LEAD EE/AA-1), X/S (LEAD X/S-3), O (LEAD O-5, low).

---

## Appendix — Source facts & verification state

- **Online == offline:** `understanding-ec2-instance-hostnames-domains.md` and `hostname-types.md` confirmed byte-identical to their `docs.aws.amazon.com` `.md` twins — no sync drift.
- **Authoritative IAM reference:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (use `list_ec2`, NOT dead `list_amazonec2`). Key line numbers cited inline in §3.
- **Core surface page:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/hostname-types.md` (446 lines) — public/private hostname tables, base36 encoding, scenarios, the "always-answered IP-name A record" sentence (L286), the public-IP-change "Important" box (L76).
- **API-reference objects read:** `API_PrivateDnsNameOptionsRequest.md`, `API_ModifyPublicIpDnsNameOptions.md` (required `HostnameType`+`NetworkInterfaceId`, errors = common only), plus `API_ModifyPrivateDnsNameOptions.md`, `API_PrivateDnsNameOptionsOnLaunch.md`, `API_PrivateDnsNameOptionsResponse.md`, `API_LaunchTemplatePrivateDnsNameOptions(Request).md` present in corpus.
- **Supporting pages (from DNS-mechanism subagent):** `AmazonDNS-concepts.md`, `vpc-sharing.md`, `vpc-share-limitations.md`, `using-vpc.md`, `using-instance-addressing.md`, `elastic-ip-addresses-eip.md`, `Using_Elastic_Addressing_Reverse_DNS.md`, `vpc-dns-updating.md`.
- **Two parallel Opus subagents** produced §3 (IAM audit) and §5 LEAD A1/EE-1/U-2/V-4 (DNS mechanism + shared-VPC disclosure). Both verified no online/offline drift on their pages.
