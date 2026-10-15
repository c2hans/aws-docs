# EC2 Hostname Types (`hostname-types.html`) — Attack / Research Plan

> **Scope of this file.** Page-level plan for the single User Guide page
> `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hostname-types.html`
> (offline mirror `docs/AWSEC2/latest/UserGuide/hostname-types.md`, 446 lines).
> Built with the `security-questionbuilder` boundary-first method. **Documentation-only** — no
> live system was touched; every lead is a falsifiable hypothesis for a hunter to execute later.
>
> **Sync check (user requirement):** the online `.md` twin was fetched 2026-10-15 and is
> content-identical to the offline mirror (public/private comparison table, three public
> hostname types, base36 worked examples, `View`/`Modify` CLI blocks, private IP-name vs
> resource-name sections, Scenario 1/2 launch-wizard defaults, stop-to-change + instance-store
> considerations). No drift.

---

## 0. Relationship to sibling plans — READ FIRST (de-duplication contract)

This page is **already folded into** two existing plans. This file **complements** them; it does
**not** restate their leads. Where they are authoritative, defer to them:

| Sibling plan | Owns (do not duplicate here) |
|---|---|
| `ec2-instance-naming-attack-research-plan.md` (**authoritative parent** for this surface) | The full §0–§8 structure and ranked leads **L1–L6**: IAM-ungated launch-time hostname posture; the `ec2:Attribute` inert-key / `ModifySubnetAttribute` ~10-attribute over-grant (instance-action focus); the unconditional IP-name A-record recon oracle; dangling AWS-native **IPv4** public-hostname cross-account reuse; split-horizon peer private-IP disclosure; shared-VPC subnet-owner-default-vs-participant-override. **It also carries the corrected IAM ground-truth** (these Modify actions ARE tag/ARN-scopable per `list_ec2.md` L8974-9028, contradicting an earlier hub-fragment "zero conditionability" drift). |
| `understanding-ec2-instance-hostnames-domains-attack-research-plan.md` | **LEAD A1** — data-plane cross-account DNS *resolution* leak in a RAM-shared VPC via the `.2` AmazonProvidedDNS resolver (co-tenant instance-ID / private-IP disclosure the control-plane isolation statement never covers), and the reversible-public-name dangling-DNS framing. |
| `working-with-ipv6-addresses-attack-research-plan.md` | IPv6-public-by-default-but-unscopable (no `ec2:AssociatePublicIpv6` / `ec2:Ipv6*` key); **confirmed no `AllowReassignment` on `AssignIpv6Addresses`**; IPv6 prefix delegation; shipped IMDSv1 `ipv6s` sample. |
| `using-instance-addressing-attack-research-plan.md` | The secondary private-IPv4 **cross-ENI/cross-account takeover primitive** (`AssignPrivateIpAddresses` + `AllowReassignment`, no source-ENI check, EIP rides along). This plan *consumes* that primitive; it does not re-derive it. |

**What THIS plan uniquely owns (net-new, page-specific depth):**
- **N1** — the `.ip.aws` **base36 FQDN as an offline, no-query address-disclosure oracle** that
  defeats IPv6 128-bit address-space obscurity (the page ships the full reversible worked example).
- **N2** — the **ENI-level public-hostname-type state machine** and the doc-stated silent
  **"no longer valid"** invalidation when the underlying IP changes — and its **IPv6-side**
  dangling-reuse angle (sibling L4 was IPv4-only).
- **N3** — the doc-stated **IMDS auto-refresh forced by a primary-public-IPv4 change**, as a
  data→control influence reachable via the cross-account IP-reassignment primitive.
- **N4** — the precise **Lens-S claim for `ModifyPublicIpDnsNameOptions`** (the *network-interface*
  action; sibling L2 covered the *instance* action): `ec2:Attribute/${AttributeName}` is almost
  certainly **listed-but-inert** because the public-hostname type is not a classic
  DescribeNetworkInterfaceAttribute attribute → any Deny keyed on it fails open.
- **N5** — the **immutability / non-remediability** edges: stop-to-change-hostname-type, and
  instance-store-root-volume types (C1/C3/D2/I2/M1/M2/M3/R3/X1) that can only be configured at
  launch (a victim cannot remediate a bad posture without relaunch).

---

## 1. Components, Assets, and Design

**What the page describes.** How an EC2 instance's DNS *name* is derived, where that derivation
is configured, and which plane answers queries for it. Two independent naming systems:

### Private hostnames — configured at the **instance** level
- **IP name** (legacy): `ip-<private-ipv4>.<region>.compute.internal` (or `.ec2.internal` in
  us-east-1). Exists for instance life. As a Private DNS hostname it returns **only** the private
  IPv4 (A record). **The A-record response is non-suppressible** — "DNS A record queries are
  always responded to irrespective of the guest OS hostname settings."
- **Resource name**: `<instance-id>.<region>.compute.internal`. Can return A and/or AAAA; the
  A/AAAA toggles are caller-configurable per instance or defaulted per subnet. Auto-selected and
  **not modifiable** in IPv6-only subnets.

### Public hostnames — configured at the **network-interface** level (NEW `.ip.aws` surface)
Three mutually-exclusive types, chosen by `ModifyPublicIpDnsNameOptions`, constrained by which IPs
are present on the ENI:
- **Dual-stack — IP based name**: `<ipv6-base36>-<ipv4-base36>.<region>.ip.aws`
- **IPv6 — IP based name**: `<ipv6-base36>.<region>.ip.aws`
- **IPv4 — IP based name**: `ec2-<pub-ipv4-dashed>.<region>.compute.amazonaws.com`

**Split-horizon DNS**: public hostnames resolve to **private** IPs from inside the VPC and to
**public** IPs from the internet. Answered by the **Amazon DNS resolver** (AWS service plane).

**The base36 encoding (page-shipped worked example — the N1 asset):**
- `q3cdpO` ⇄ IPv4 `52.54.55.56` (base36 of the 32-bit address)
- `f5lnz-0khrm-nt2u3-gyqqt-nbdl5` ⇄ IPv6 GUA `FFFF:1407:4:f000:81d:2689:1066:4489` (base36 of the
  128-bit address, split into five labels)
- The IPv4-style name `ec2-52-54-55-66…compute.amazonaws.com` embeds the dotted IPv4 directly.
- **The FQDN string itself is the plaintext of the IP addresses** — fully reversible with no DNS
  query and no AWS credential.

**Assets at stake:**
- The exact **public IPv4** and the exact **IPv6 GUA** of any ENI with a public hostname (via N1).
- The **instance-id** (resource name) and **private IPv4** (IP name) — internal recon (sibling L3).
- Instance **IMDS** metadata consistency (N3).
- The **binding** between an AWS-provided public hostname and whichever account currently holds
  the underlying IP (N2 dangling reuse).

**Identity / control:** standard SigV4 IAM for the three Modify actions; the **VPC owner** gates
existence (`EnableDnsHostnames` + `EnableDnsSupport` must both be on or "there is no hostname type
defined or generated"); the **subnet owner** sets launch defaults (shared-VPC lever, sibling L6).

**Diagram:**
```
                       (control-plane: SigV4 IAM)
caller ──ModifyPrivateDnsNameOptions──▶ instance*        (private IP/resource name, A/AAAA toggles)
caller ──ModifyPublicIpDnsNameOptions─▶ network-interface* (public hostname type; .ip.aws / compute.amazonaws.com)
caller ──ModifySubnetAttribute───────▶ subnet*           (launch defaults; subnet-owner governed)
                                   │
                                   ▼
                 Amazon DNS resolver (.2 / public authoritative)  ◀── AWS SERVICE PLANE (hard stop)
                                   │  split-horizon
          in-VPC query → private IP            internet query → public IP
                                   │
   FQDN string ──(base36, offline, no query)──▶ exact IPv4 + full IPv6 GUA   [N1 oracle]
```

---

## 2. Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Anyone who observes a `.ip.aws` / `compute.amazonaws.com` FQDN (logs, SNI, Referer, cert-transparency, screenshots) | The ENI's exact public IPv4 **and full IPv6 GUA** | base36 decode of the hostname labels — **offline, no DNS query, no creds** | Recovering the 128-bit IPv6 GUA from the hostname string alone = defeat of IPv6 address-space obscurity (N1) |
| Caller with `ec2:ModifyPublicIpDnsNameOptions` on an ENI they can name | The public DNS posture of that ENI | ENI-scoped Write; type constrained by present IPs | Setting/altering a public hostname type on an ENI whose IP binding the caller does not legitimately control (N2/N4) |
| Account B that acquires a released public IPv4 / EIP (or first IPv6 GUA) previously bound to account A's ENI | The **same AWS-provided public hostname** account A still has dangling CNAMEs to | Hostname is **derived from the IP**; reassignment hands the identical name to the next holder | Account B serving/answering for a hostname account A's clients still trust = subdomain-takeover (N2; IPv4 side = sibling L4, **IPv6 side = net-new here**) |
| Caller who can reassign a victim ENI's **primary public IPv4** (e.g. via the using-instance-addressing takeover primitive) | The victim instance's **IMDS** state | Doc-stated: changing primary public IPv4 "forces a downstream refresh of IMDS" | A metadata mutation observed on an instance whose guest OS the caller does not own (N3 data→control) |
| Any principal issued a narrow IAM Deny keyed on `ec2:Attribute/public-hostname-type` (or similar) | `ModifyPublicIpDnsNameOptions` | Policy evaluation of a key that likely never populates for this action | The Modify call **succeeds despite the Deny** (key inert → fail-open) (N4 Lens-S) |
| Victim running an instance-store-root-volume type (C1/C3/D2/I2/M1/M2/M3/R3/X1) | Their own hostname posture | Config is launch-time-only; cannot stop to change | Victim cannot remediate a bad/leaky hostname type without a full relaunch (N5 availability/immutability) |
| Any customer surface | **Amazon DNS resolver fleet / `.ip.aws` + `compute.amazonaws.com` authoritative-zone control plane** | — | **HARD STOP** — any identity/credential/ARN/account of AWS's own DNS service plane → preserve evidence, flag for disclosure, do not probe |

---

## 3. API / interface surface (page-scoped)

| Name | Method | New/Existing | Mutating | Facing | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ModifyPublicIpDnsNameOptions` | SigV4 / `modify-public-ip-dns-name-options` | **NEW** (`.ip.aws` era, ~2025) | **Yes** | External | Set ENI public hostname type (`public-dual-stack-dns-name` / IPv4 / IPv6) | IAM on `network-interface*` | **Resource = ENI, not instance.** Keys: `aws:ResourceTag`, `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:AvailabilityZone`, `ec2:Region`, `ec2:ResourceTag`, `ec2:Subnet`, `ec2:Vpc`. **No key for the hostname-type enum value.** (`list_ec2.md` L8980) |
| `ModifyPrivateDnsNameOptions` | SigV4 / `modify-private-dns-name-options` | Existing | **Yes** | External | Set instance private hostname type + A/AAAA toggles | IAM on `instance*` | Keys incl `ec2:Attribute(+/${AttributeName})`, `ec2:InstanceID`, `ec2:MetadataHttpTokens`, `ec2:Tenancy`, … **No key for the hostname-type value or the A/AAAA toggle values.** (L8974) |
| `ModifySubnetAttribute` | SigV4 / `modify-subnet-attribute` | Existing | **Yes** | External | Set subnet launch defaults (`PrivateDnsHostnameTypeOnLaunch`, A/AAAA-on-launch) | IAM on `subnet*` (**subnet owner** in shared VPC) | Governs *participant* launches — sibling L6. |
| `DescribeNetworkInterfaces` (`.PublicIpDnsNameOptions`) | SigV4 | Existing | No | External | Read ENI hostname type + all three public DNS names | IAM on ENI | Read oracle for the public names (which already encode the IPs — N1). |
| `DescribeInstances` / console Details | SigV4 | Existing | No | External | Read private IP-name / resource-name / answer config | IAM | Sibling L3 recon oracle. |
| `RunInstances` (`PrivateDnsNameOptions`) | SigV4 | Existing | **Yes** | External | Bake private hostname posture at launch | IAM | Sibling L1 (launch-time ungated posture) + N5 (only option for instance-store-root types). |
| Amazon DNS resolver (`.2` / public authoritative for `.ip.aws`, `compute.amazonaws.com`, `compute.internal`) | DNS | Existing | No (query) | **Internal + Internet (split-horizon)** | Answer A/AAAA | Anyone who can send a query to the resolver | **AWS service plane — hard stop.** Cross-account resolution-leak angle = sibling A1. |

**Undocumented-knob / parity sweep:** the three public-hostname **enum values**
(`public-dual-stack-dns-name`, `public-ipv4-dns-name`, `public-ipv6-dns-name`) are request inputs
with **no matching condition key** — an admin cannot write "may set IPv4-only but not dual-stack."
The A/AAAA resource-name toggles are likewise value-unscopable. This is the central IAM-expressiveness
gap for the page (see N4 and sibling L1/L2).

---

## 4. Boundary-lens leads (ranked; net-new only — siblings own the rest)

### N1 — `.ip.aws` base36 FQDN is an offline IPv6-GUA disclosure oracle  — Lens U / A — **High (research-worthy, novel)**
- **Claim:** The public hostname is advertised as a *convenience* name, but the FQDN **string**
  is a complete, reversible plaintext encoding of the ENI's exact public IPv4 **and** its full
  128-bit IPv6 GUA. Anywhere the hostname leaks — TLS SNI, HTTP `Referer`/`Origin`, certificate
  transparency logs (if an ACM/other cert is issued for the `.ip.aws` name), CDN/access logs,
  error pages, screenshots, email headers — an attacker recovers the **exact IPv6 GUA** with
  pencil-and-paper base36, **no DNS query and no AWS credential**. IPv6's practical
  defense-in-depth ("128-bit space is not scannable") is therefore nullified for any instance
  that was ever named this way.
- **Mechanism (doc evidence):** the page ships the full worked example — `q3cdpO`→`52.54.55.56`,
  `f5lnz-0khrm-nt2u3-gyqqt-nbdl5`→`FFFF:1407:4:f000:81d:2689:1066:4489`, "base36 representation of
  the primary public IPv6 address … along with a base36 representation of the primary public IPv4
  address." It even states the IPv6 label is **the first IPv6 GUA assigned to the ENI**, so the
  decode yields the *canonical* address, not a rotating one.
- **Confirm/Refute oracle:** (offline, documentation-grade) implement the base36 decode and show it
  round-trips the page's own example and arbitrary addresses. (Live, by a hunter) given a leaked
  `.ip.aws` name, decode → send a single probe to the recovered IPv6 GUA → the decoded address is
  reachable/responds = oracle confirmed. **Stop at reachability** — do not enumerate neighbours.
- **Preconditions:** instance was assigned a dual-stack or IPv6 public hostname; the name leaked
  into any observable channel. **Cost:** trivial. **Severity if true:** High — turns an un-scannable
  IPv6 host into a directly addressable target and leaks the IPv4 simultaneously; also a
  cross-correlation primitive (same ENI's v4 and v6 provably linked from one string).
- **Why net-new:** siblings note "reversibility" as a *property*; none develop it into the
  IPv6-obscurity-defeat oracle with the leak-channel enumeration and the "first GUA = canonical"
  observation.

### N2 — Public-hostname-type state machine + silent "no longer valid" invalidation → IPv6-side dangling reuse — Lens EE / AA — **High**
- **Claim:** Because the hostname is **derived from** the IP (not an independent allocation),
  (a) changing the primary private IPv4 **or the first IPv6 GUA** silently makes the
  previously-generated public hostname "no longer valid" with **no event, no CNAME teardown**,
  stranding any external DNS record that points at it; and (b) when that IP (public IPv4/EIP **or**
  the first IPv6 GUA) is later held by a **different account**, that account inherits the identical
  AWS-provided hostname. The IPv4/EIP case is sibling L4; **the IPv6-GUA case is net-new** and is
  *not* mitigated by the IPv6 sibling's "no `AllowReassignment`" finding, because reuse here does
  not require force-moving an in-use address — it only requires the GUA to be released and
  re-allocated (or a caller to name it explicitly on a fresh ENI).
- **Mechanism (doc evidence):** the **Important** note — "If you change the primary private IPv4
  address or the first IPv6 GUA … the previously-generated public hostname will **no longer be
  valid**." The three-type section ties each name deterministically to "the first IPv6 GUA assigned
  to the network interface." `ModifyPublicIpDnsNameOptions` only *selects a type*; it never pins the
  name to an owner/account.
- **Confirm/Refute oracle:** (hunter, two synthetic accounts) A assigns an IPv6 GUA, takes the
  IPv6/dual-stack hostname, publishes a CNAME to it; A releases the GUA; B re-allocates the same GUA
  (or names it on B's ENI) and enables the public hostname → B's ENI answers (split-horizon public
  side) for the name A's clients still resolve. Confirmed if B's content is served under A's old
  `.ip.aws` name. Refuted if AWS refuses to re-issue the name to a different account or scopes it.
- **Preconditions:** address release+reacquire across accounts (IPv6 GUA churn, or EIP pool reuse
  for the IPv4 variant). **Severity:** High (cross-account subdomain takeover of AWS-native names).

### N3 — Primary-public-IPv4 change forces victim IMDS refresh (data→control) — Lens D — **Medium–High**
- **Claim:** An actor who can change a victim ENI's **primary public IPv4** (e.g. via the
  cross-account/cross-ENI reassignment primitive owned by `using-instance-addressing`) does not
  merely change a label — the page states it **"forces a downstream refresh of Instance Metadata
  Service (IMDS)… automatically updated."** So an address-plane action the victim did not initiate
  mutates the victim instance's **control-plane metadata** (public-hostname / public-ip fields the
  guest and its software may trust), without any `Modify*DnsNameOptions` call and without touching
  the instance directly.
- **Mechanism (doc evidence):** the **Important** note's IMDS clause; combine with the
  `using-instance-addressing` takeover primitive (no source-ENI ownership check on reassignment).
- **Confirm/Refute oracle:** (hunter) reassign the victim ENI's primary public IPv4 from an
  attacker-controlled path → read victim IMDS `public-ipv4`/`public-hostname` → confirmed if they
  change to attacker-influenced values with no victim action. Also test whether the auto-refresh
  can be used as a **liveness/causality oracle** (did the refresh fire = did my reassignment land).
- **Severity:** Medium–High — depends on whether any guest software keys trust/config off IMDS
  public-hostname; at minimum a cross-account-induced control-plane state change.

### N4 — `ec2:Attribute/${AttributeName}` likely inert on `ModifyPublicIpDnsNameOptions` (ENI action) → Deny fails open — Lens S — **Medium**
- **Claim:** `ModifyPublicIpDnsNameOptions` lists `ec2:Attribute` and `ec2:Attribute/${AttributeName}`
  (L8980), but the public-hostname **type** is not among the classic
  `DescribeNetworkInterfaceAttribute` attributes (`description`, `groupSet`, `sourceDestCheck`,
  `attachment`). These keys appear to be a copy-paste from the `Modify*Attribute` family
  (`ModifyInstanceAttribute`/`ModifySnapshotAttribute`, where they genuinely populate). If the key
  never populates for this action, a least-privilege policy that tries to **Deny** altering the
  hostname type via `ec2:Attribute/...` **matches nothing and fails open** — the operator believes
  the posture is pinned; it is not. (Sibling L2 made this claim for the *instance* action
  `ModifyPrivateDnsNameOptions`; this is the parallel, independent claim for the *network-interface*
  action, plus the point that **neither** action exposes a key for the hostname-type **value**.)
- **Mechanism (doc evidence):** `list_ec2.md` L8974/L8980 vs the EC2 API `DescribeNetworkInterfaceAttribute`
  / `DescribeInstanceAttribute` attribute enums; `ModifySnapshotAttribute` (L9006) shown as the
  family where `ec2:Attribute` is real (it has `ec2:Add/userId`, `ec2:Remove/group`, etc.).
- **Confirm/Refute oracle:** `SimulateCustomPolicy` / `SimulatePrincipalPolicy` with a Deny on
  `ec2:Attribute/${AttributeName} StringEquals <hostname-type-ish name>` → if the Modify call is
  still Allowed, key is inert. (No live mutation needed — simulate only.)
- **Severity:** Medium — a silent least-privilege/guardrail-bypass; the hostname-type value is
  **not expressible as an IAM condition** at all, so "may set IPv4-only but never dual-stack/`.ip.aws`"
  cannot be written.

### N5 — Non-remediable hostname posture (stop-to-change + instance-store-root launch-only) — Lens U / availability — **Low**
- **Claim:** A victim cannot quickly remediate a leaky/undesired hostname posture: changing the
  **hostname type** requires **stopping the instance**, and instances with an **instance-store root
  volume** (C1, C3, D2, I2, M1, M2, M3, R3, X1) **cannot be stopped**, so their hostname type and
  DNS-answer options are **fixed at launch** — remediation requires a full relaunch (new instance,
  new IPs, downstream churn). This widens the exposure window for N1/N2 and defeats "just turn it
  off" incident response.
- **Mechanism (doc evidence):** Considerations block — "To change the hostname type, you must first
  stop the instance… Because you can't stop an instance with an instance store root volume, you can
  only configure the hostname type and DNS hostname options at instance launch. Only the following
  instance types support instance store root volumes: C1, C3, D2, I2, M1, M2, M3, R3, and X1."
- **Confirm/Refute oracle:** documentation-grade (constraint is explicitly stated); hunter can
  confirm the API rejects `ModifyPrivateDnsNameOptions` hostname-type change on a running /
  instance-store-root instance.
- **Severity:** Low on its own; an **exposure-window amplifier** for N1/N2.

### Launch-time reinforcement (defers to siblings; recorded, not re-led)
- **Scenario 2 force-on A record:** in IPv4/dual-stack subnets the wizard selects **"Enable IP name
  IPv4 (A record) DNS requests"** automatically and **"can't be changed"** — the launch-time
  manifestation of sibling **L3**'s non-suppressible IP-name A-record oracle. No new lead; strengthens L3.
- **IPv6-only subnet forces resource name + non-modifiable A toggles:** sibling L1/L2 territory.
- **VPC-owner gate (`EnableDnsHostnames`+`EnableDnsSupport`):** sibling L6 shared-VPC lever.

---

## 5. Prioritization — where to concentrate fire

1. **N1** (base36 offline IPv6-GUA disclosure) — highest novelty, zero cost, pure-doc confirmable
   now; live confirmation is a single reachability probe. Start here.
2. **N2** (IPv6-side dangling public-hostname reuse) — high impact, needs a two-account canary;
   extends sibling L4 into IPv6 where the `AllowReassignment` mitigation does **not** apply.
3. **N3** (IMDS auto-refresh via cross-account IP reassignment) — high if any guest trusts IMDS
   public-hostname; chains onto the `using-instance-addressing` primitive.
4. **N4** (inert `ec2:Attribute` on the ENI action + value-unscopability) — simulate-only,
   cheap, confirms a silent guardrail gap.
5. **N5** (non-remediability) — low, but quote it as the exposure-window multiplier for N1/N2.

**Null hypotheses (pages checked, lens does not fire):**
- **Lens F (injection):** N/A — read the whole page; no customer input is parsed into another
  language. Hostname strings are AWS-generated from IPs, not caller free-text.
- **Lens B/C (PassRole / credential vending):** N/A — no role ARN, no STS, no session-policy input
  on any of the three Modify actions (confirmed against `list_ec2.md` rows).
- **Lens Q (upload):** N/A — no blob/file field on this page.
- **Lens G (SSRF):** N/A for the *control* actions (no field the service dereferences); the only
  "service dereferences a name" surface is the **Amazon DNS resolver**, which is the **hard-stop
  service plane** and is routed to sibling A1 for the cross-account resolution-leak question, not
  pursued here.

---

## 6. Hard-stop & rules of engagement

- **Documentation-only** here. Every live oracle above is a task for a downstream hunter in an
  **authorized** account with **synthetic canary** data; tear down all created ENIs/addresses.
- **AWS service-plane hard stop:** the Amazon DNS resolver fleet and the `.ip.aws` /
  `compute.amazonaws.com` authoritative-zone control plane are AWS-owned. Any identity, credential,
  ARN, or account belonging to them → **stop immediately, preserve evidence, flag for disclosure.**
- Confirm existence, never exploit beyond it: for N1 stop at a single reachability probe of the
  decoded address; for N2 stop once the name resolves/serves under the second account; for N3 stop
  at the first observed IMDS field change. **No neighbour enumeration, no data exfiltration.**
- Stay on-scope: no DNS zone-walking, no port scans, HTTP/application + control-plane API only.

---

## 7. Pointers for the next agent

- Authoritative IAM table: `docs/service-authorization/latest/reference/list_ec2.md`
  — `ModifyPrivateDnsNameOptions` L8974, `ModifyPublicIpDnsNameOptions` L8980,
  `ModifySnapshotAttribute` L9006 (the family where `ec2:Attribute` is genuinely populated — use as
  the comparison for the N4 inert-key argument). **Use `list_ec2`, not the dead `list_amazonec2`.**
- Parent/sibling plans in this directory: `ec2-instance-naming-attack-research-plan.md` (read L1–L6
  before touching anything here), `understanding-ec2-instance-hostnames-domains-attack-research-plan.md`
  (LEAD A1), `working-with-ipv6-addresses-attack-research-plan.md`, `using-instance-addressing-attack-research-plan.md`.
- Target page: `docs/AWSEC2/latest/UserGuide/hostname-types.md` (online twin verified identical
  2026-10-15).
- The base36 codec for N1 is the one piece of tooling worth writing first — it is both the
  documentation-grade proof and the live decode step, and it costs nothing.
