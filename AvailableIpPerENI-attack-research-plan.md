# Maximum IP addresses per network interface — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/AvailableIpPerENI.html` (offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/AvailableIpPerENI.md`, 105 lines) + adjacent `ec2-prefix-eni.md`, `using-eni.md`, `using-instance-addressing.md`; authoritative IAM reference `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (10,190 lines; slug `list_ec2`, NOT `list_amazonec2`); `API_NetworkInfo.html`. Status: documentation-derived hypotheses only; nothing tested against a live account. All page content verified online==offline byte-identical 2026-10-15.

**What this page is.** `AvailableIpPerENI.html` is a **limits / capacity-governor reference page** — a child of `using-eni.html` (Elastic Network Interfaces), cited by `using-instance-addressing.md`, `network-interface-attachments.md`, and `ec2-prefix-eni.md`. It documents, per instance type: the maximum number of network interfaces (ENIs), the maximum **private IPv4 addresses per ENI**, and the maximum **IPv6 addresses per ENI** (stated to be a *separate* ceiling from the IPv4 one), plus the capability claim that "all instance types support IPv6 addressing except C1, M1, M2, M3, and T1." It introduces **no mutating API**; its only API surface is the read action `DescribeInstanceTypes` / `Get-EC2InstanceType` (`NetworkInfo.*`).

**Positioning in the corpus.** This is the **IP-addressing-cluster counterpart of `fleet-quotas-attack-research-plan.md`** — the first-and-only page whose primary surface is the *numeric ceilings* that bound the launch/assign primitives the other siblings describe. It therefore owns **Lens L (resource/IP exhaustion)** and **Lens U (limit-enforcement-point + doc-vs-API capability-table integrity)**, and it deliberately **does NOT restate** the assign/reassign *takeover* mechanics or the "no IP-value condition key" depth — those are owned by:
- `using-instance-addressing-attack-research-plan.md` — `AssignPrivateIpAddresses … AllowReassignment` cross-ENI/cross-account takeover; the no-`ec2:PrivateIpAddress`/`ec2:Ipv6Address`/`AllowReassignment`-key facts; EIP rides-along; link-local SG/NACL bypass.
- `working-with-ip-addresses-attack-research-plan.md` — launch-time IPv4 assignment, shared-VPC forced exposure, cross-tenant private-IP collision, `DescribeInstances` oracle.
- `instance-secondary-ip-addresses-attack-research-plan.md` — `UnassignPrivateIpAddresses` collateral EIP-disassociation; launch-time secondary-IP value unexpressible.
- `working-with-ipv6-addresses-attack-research-plan.md` — IPv6 public-by-default-but-unscopable; the IPv6 prefix-delegation bulk knob; IPv6 is "safer" (no `AllowReassignment` force-move).
- `ec2-networking-attack-research-plan.md` (hub) — shared-VPC owner/participant isolation; released-EIP squatting; BYOIP.

This plan's **net-new contribution** is the capacity-governor framing: the per-ENI maxima are the *amplifier* that converts those siblings' per-IP primitives into a **subnet-wide IP-exhaustion blast radius**, and there is **no IAM lever** to bound it. See [[reference-aws-iam-service-auth-ref-url]] and [[project-aws-research-plans]].

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- This page is a **limits reference**, not an API surface. The leads are predominantly **availability/cost (Lens L)** and **control-gap / doc-integrity (Lens U)**. There is no cross-tenant *data* read on this page's own surface; the cross-account severity comes only from the shared-subnet *consumption* amplifier (Area 1), which composes this page's ceilings with the RAM-shared-subnet participant model owned by the siblings.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. a host/Nitro-side ENI, a control ENI), stop, preserve evidence, flag for AWS-Security disclosure. The ENI/IP data plane is the actual fabric — never probe the host side of any reserved service.
- `DryRunOperation` is caller-IAM-only (evaluated before resource resolution) — NOT an ownership/exhaustion oracle.

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Cross-tenant subnet IP exhaustion:** from one principal, assign secondary IPv4 (directly or via `/28` prefixes) up to the documented per-ENI maxima across the maximum number of ENIs on a large instance, and **exhaust a RAM-shared subnet's CIDR so a co-tenant's `RunInstances`/`AssignPrivateIpAddresses` fails** — proven by a co-tenant launch returning an insufficient-free-addresses error attributable to the attacker's consumption.
2. **Prove the control gap:** demonstrate (via `iam:SimulateCustomPolicy`, no resources touched) that **no IAM condition key** can be authored to cap how many IPv4/IPv6 addresses a principal assigns per ENI / per subnet — i.e. an admin cannot write "this team may assign at most N secondary IPs."
3. **Doc-vs-API capability integrity:** confirm whether the prose claim "all instance types support IPv6 except C1/M1/M2/M3/T1" matches `NetworkInfo.Ipv6Supported` for every current instance type (a Lens U capability-table diff a compliance control might trust).

## 2. Components, Assets, and Design

- **Customer-facing interface:** EC2 control-plane APIs (SigV4). On *this page*: only the read action `DescribeInstanceTypes` (CLI `describe-instance-types`, PowerShell `Get-EC2InstanceType`). The *governed* mutating actions live on sibling pages: `AssignPrivateIpAddresses`, `AssignIpv6Addresses`, `RunInstances`, and the prefix actions `AssignPrivateNatGatewayAddress`/`work-with-prefixes` (`ec2-prefix-eni.md`).
- **Asset governed:** the finite **private-IPv4 address space of a VPC subnet** (a shared, consumable pool), and secondarily the IPv6 /64 per subnet. The per-ENI maxima are *per-instance-type hardware/service ceilings*, not account quotas.
- **Identifier shapes:** instance type names (public, non-secret), ENI ids (`eni-…`), subnet ARNs/ids. No tenant-scoped secret identifier appears on this page.
- **Ownership split that matters:** in a **RAM-shared subnet**, the subnet is owned by account O; participants P1…Pn launch ENIs/instances into it and each **consumes from the same shared IPv4 pool**. The subnet owner sets size (CIDR) but **cannot cap per-participant consumption** (Area 1 / Area 2).
- **The amplifier (net-new, from `ec2-prefix-eni.md`):** a prefix counts as **one IP** against the AvailableIpPerENI limit, but an IPv4 `/28` prefix = **16 real subnet addresses**. So the per-ENI "limit" numbers **understate true subnet consumption by up to 16×**.

```
  Shared subnet (owner O, fixed CIDR, finite IPv4 pool)
        ├── Participant P1  instance (type T) ── ENI×MaxNICs(T) ── each ENI: up to Ipv4PerIntf(T) IPs
        │                                                           └─ OR up to (Ipv4PerIntf-1) × /28 prefixes = ×16 addrs
        ├── Participant P2  instance ...
        └── (victim) Participant P3  RunInstances  ← fails if pool exhausted by P1
  Enforcement of "fair share": subnet sizing / CIDR reservation ONLY. No IAM condition key. ← the gap
```

## 3. API / Interface Inventory

| Name | Method | Mutating | Facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `DescribeInstanceTypes` | GET/Query | No | External | Reports `NetworkInfo.{MaximumNetworkInterfaces, Ipv4AddressesPerInterface, Ipv6AddressesPerInterface, Ipv6Supported, …}` | Yes | Any caller with `ec2:DescribeInstanceTypes` | **Unscopable** — blank resource type, only `ec2:Region` (list_ec2 6990–6994). Returns **public, non-tenant** spec data. |
| `AssignPrivateIpAddresses` *(sibling-owned)* | POST | Yes | External | Add secondary private IPv4 to an ENI, up to the per-ENI limit | Yes | `network-interface*` holder | list_ec2 4700–4704; **no IP-count condition key** (see Area 2). |
| `AssignIpv6Addresses` *(sibling-owned)* | POST | Yes | External | Add IPv6 to an ENI, up to the (separate) per-ENI limit | Yes | `network-interface*` holder | list_ec2 4694–4698; no IP-count key. |
| `RunInstances` *(sibling-owned)* | POST | Yes | External | Launch; `--secondary-private-ip-address-count`, `--ipv6-address-count` consume at launch | Yes | multi-resource | list_ec2 9585–9603; NI row 9595 has **no IP-count key**. |
| Prefix assignment *(adjacent, `ec2-prefix-eni.md`)* | POST | Yes | External | Assign `/28` IPv4 or `/80` IPv6 prefix to ENI; each counts as one against the limit | Yes | ENI holder | **16× (IPv4) real-address amplifier** per prefix. |

No `[NEW]` marker on this page. No non-SDK/console-hidden knob on this page (the hidden knobs live on the mutating siblings).

## 4. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Participant P1 (one account) | Shared-subnet IPv4 pool (owner O's resource, consumed by all participants) | `AssignPrivateIpAddresses` / prefix assign / `RunInstances`, up to per-ENI maxima this page defines | **A co-tenant P3 launch/assign fails for want of free addresses, attributable to P1's consumption** = cross-account availability breach on a shared resource |
| Any caller | `DescribeInstanceTypes` capability data | Unscopable List action | **Not a breach** — returns public instance-type spec data; account-wide read of non-secret data (Informational) |
| Admin (policy author) | The assign actions | Attempt to author a per-count IAM guardrail | **No condition key exists to bind IP-count** → the intended control is unexpressible (Lens U/S control-gap) |
| Doc reader / compliance control | `NetworkInfo.Ipv6Supported` | Diff prose IPv6-exception list vs API boolean | A capability cell that contradicts the API (Lens U doc-integrity) |

Canonical boundaries that do **not** appear on this page (null): data-plane→control-plane, credential vending, confused-deputy/PassRole, OAuth, translation-layer injection — see §8.

## 5. Recommended Areas of Focus

### Area 1 — Cross-tenant subnet IP exhaustion amplified by the per-ENI maxima (Lens L, PRIMARY)
**Background.** This page defines, per instance type, `MaximumNetworkInterfaces` and `Ipv4AddressesPerInterface`. The documented worked example: `c8i.48xlarge` = **24 NICs × 64 IPv4/NIC = up to 1,536 private IPv4 addresses on a single instance** (AvailableIpPerENI.md:62–64). `ec2-prefix-eni.md:56` then establishes that a `/28` prefix **counts as one IP against this limit** but represents **16 real subnet addresses** — so prefix delegation pushes one `c8i.48xlarge` to ≈ 24 × 63 × 16 ≈ **24,000+ IPv4 addresses** drawn from the subnet, dwarfing most subnet CIDRs (a /20 is 4,096 addresses).

**Security Concern.** In a **RAM-shared subnet** (owner O, participants P1…Pn drawing from one shared IPv4 pool — see `working-with-ip-addresses` Area 3 and the hub shared-VPC model), a single participant can legitimately consume the entire subnet's address space using nothing but the per-ENI capacities this page documents, **starving every other participant's launches** (`RunInstances` / `AssignPrivateIpAddresses` fail with insufficient free addresses). The owner's only lever is subnet sizing / CIDR reservation — an administrative control, **not** an IAM one (Area 2).

**High-level Test Scenarios.**
- *Claim:* a participant can exhaust a shared subnet's IPv4 pool via secondary-IP + prefix assignment up to this page's per-ENI maxima → *Mechanism:* AvailableIpPerENI.md:8,54–64 ceilings + ec2-prefix-eni.md:56 "each prefix counts as one IP address" (16 real addrs each) → *Oracle:* in a 2-account shared-subnet canary, P1 assigns prefixes/secondary IPs up to the ceiling; then a P2 `RunInstances` into the same subnet returns an insufficient-addresses error → cross-account DoS confirmed → *Preconditions:* RAM-shared subnet, two accounts, a large instance type (or several small ones) → *Cost:* low (instance-hours + prefix assigns) → *Severity:* **High** (cross-tenant availability on a shared resource); intra-account cross-team = Medium.
- *Claim:* the per-ENI "limit" understates true consumption 16× for IPv4 → *Oracle:* assign `(Ipv4PerIntf − 1)` `/28` prefixes to one ENI and observe 16×(limit−1) subnet addresses marked consumed in the subnet's available-IP count → confirms the headline ceiling is a *prefix-slot* count, not an address count → *Severity:* Informational supporting fact that raises Area 1 blast radius.
- *Adjacent:* does hitting the ceiling produce a **clean, attributable** error or a generic one (enumeration/attribution for the defender)? Does the subnet owner get any signal (CloudWatch `AvailableIpAddressCount`, no EventBridge event — cross-ref config-windows-multiple-ip Area 3 "no IP-assign EventBridge event")?

Doc evidence: AvailableIpPerENI.md:8,54–64; ec2-prefix-eni.md:31–32,56. Severity-if-true: **High** (shared subnet).

### Area 2 — No IAM condition key can cap per-principal IP consumption (Lens U + Lens S, PRIMARY, control-gap)
**Background.** The page presents the maxima as the sole governor of per-ENI IP count. The maxima are enforced **server-side by the instance type**, not by any IAM mechanism the customer can tighten.

**Security Concern.** An administrator who wants "team X may assign at most N secondary IPs" or "no prefix delegation for team X" — a natural guardrail against Area 1 — **cannot author it**: confirmed by exhaustive `list_ec2.md` grep, there is **no `ec2:PrivateIpAddress`, `ec2:Ipv6Address`, `Ipv6AddressCount`, `SecondaryPrivateIpAddressCount`, `ec2:IpCount`, or any IP-quantity condition key anywhere** (0 hits each). The only numeric `*Count*` keys in the entire EC2 service — `ec2:InstanceCount` (10090) and `ec2:TargetInstanceCount` (10164) — are about **instance** counts (Capacity Reservations), not IP counts. The four assign/unassign actions (`AssignPrivateIpAddresses` 4700–4704, `AssignIpv6Addresses` 4694–4698, `UnassignPrivateIpAddresses` 9696–9700, `UnassignIpv6Addresses` 9690–9694) carry only `network-interface*` + {`aws:ResourceTag`, `ec2:AvailabilityZone`, `ec2:ManagedResourceOperator`, `ec2:NetworkInterfaceID`, `ec2:Region`, `ec2:ResourceTag`, `ec2:Subnet`, `ec2:Vpc`}. `RunInstances`' NI row (9595) likewise has no IP-quantity key. `ec2:Subnet`/`ec2:Vpc` (10162/10172) bind **which** subnet/VPC (ARN identity), never **how much** of its pool.

**High-level Test Scenarios.**
- *Claim:* no policy can forbid or cap IP assignment by count → *Oracle:* `iam:SimulateCustomPolicy` with a Deny attempting any count condition on `AssignPrivateIpAddresses` shows the key is undefined/inert (contrast with `ec2:InstanceCount` which *is* live on launch/CR actions) — no resource touched → *Severity:* **Medium** (control-gap enabling Area 1); AWS-owned framing because the page implies the ceiling is "the limit" without noting it is per-ENI-only and unbounded per subnet/principal.
- *Claim:* `ec2:Subnet` looks like a scoping lever but only restricts *which* subnet, not consumption → confirms the gap is structural, not a missing-policy footgun.

Doc evidence: list_ec2.md 4694–4704 / 9690–9700 / 9595 / 10090 / 10162 / 10172; whole-file 0-hit grep for IP-count keys. Severity-if-true: **Medium** (control-gap; High when it is the enabler of a confirmed Area 1 cross-tenant exhaustion).

### Area 3 — IPv6 capability claim vs `NetworkInfo.Ipv6Supported` (Lens U, doc-vs-API integrity)
**Background.** The page asserts "all instance types support IPv6 addressing except C1, M1, M2, M3, and T1" (AvailableIpPerENI.md:8). `API_NetworkInfo` exposes a per-instance-type Boolean `Ipv6Supported` (confirmed field + type), making the claim directly diffable against the control plane.

**Security Concern.** A compliance/attestation control (or an automated placement guardrail) might trust the prose exception list rather than querying the API. If any current instance type's `Ipv6Supported` disagrees with the "C1/M1/M2/M3/T1-only" exception set, the doc is a false source of truth. Separately, the page's own worked examples (CLI + PowerShell) **only query `MaximumNetworkInterfaces` and `Ipv4AddressesPerInterface` — never `Ipv6AddressesPerInterface` or `Ipv6Supported`**, despite the lead sentence asserting a *separate* IPv6 ceiling (a page self-consistency gap, identical online/offline).

**High-level Test Scenarios.**
- *Claim:* `Ipv6Supported==false` exactly for {C1,M1,M2,M3,T1} and `true` for all else → *Oracle:* `describe-instance-types --query 'InstanceTypes[*].[InstanceType, NetworkInfo.Ipv6Supported]'` across all types; any mismatch is a Lens U doc-vs-API defect → *Severity:* **Informational/Low** (AWS-owned; reportable because a customer could build a control on the false claim). **doc-gap:** field existence/type confirmed from docs; live value cross-check not performed (out of scope here).
- *Claim:* the "separate IPv6 limit" is enforced independently of the IPv4 limit → cross-ref `working-with-ipv6-addresses` plan (owns the IPv6-prefix bulk knob and the "no `AllowReassignment` on IPv6" fact); verify the IPv6 ceiling is a genuinely separate counter (so Area 1's IPv4 exhaustion does not consume IPv6 slots and vice-versa).

Doc evidence: AvailableIpPerENI.md:8,43–47,76–82; API_NetworkInfo (`ipv6Supported` Boolean). Severity-if-true: **Informational/Low**.

### Area 4 — `DescribeInstanceTypes` as an (near-null) read oracle (Lens A, LOW)
**Background.** `DescribeInstanceTypes` is unscopable — blank resource type, only `ec2:Region` (list_ec2 6990–6994) — the same inert-ABAC shape as the corpus's other `Describe*` oracles (`DescribeInstances`, `DescribeNetworkInterfaces`).

**Security Concern (bounded).** Unlike those siblings, the data returned here is **public, non-tenant instance-type specification data** — there is no cross-tenant information disclosure, so this is **near-null**. It is noted only for completeness and to pre-empt a false Lens-A positive: an unscopable `Describe*` is *not* automatically a finding when its payload carries no tenant-owned data.

Doc evidence: list_ec2.md 6990–6994. Severity-if-true: **Informational** (null — public data).

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-tenant subnet IPv4 exhaustion via per-ENI maxima + prefixes | Shared subnet pool / `AssignPrivateIpAddresses` / prefix assign | "Mitigation" is only subnet sizing / CIDR reservation (administrative, non-IAM) — attack the absence of any per-principal IAM cap |
| Admin cannot author an IP-count guardrail | IAM policy on assign actions | None — no IP-quantity condition key exists (attack = prove inexpressibility via SimulateCustomPolicy) |
| IPv6 support prose vs API boolean | `DescribeInstanceTypes.NetworkInfo.Ipv6Supported` | The prose exception list — attack = diff against the API across all types |
| Prefix "counts as one IP" masks 16× real consumption | `ec2-prefix-eni.md` limit accounting | None — attack the understated accounting as the Area-1 amplifier |

## 7. Out-of-Scope Risk Categories
- **Public instance-type spec data** returned by `DescribeInstanceTypes` — not tenant data; its unscopability is Informational only.
- **Single-tenant self-exhaustion** of one's own subnet (own account only) — least-privilege/self-DoS, out of scope.
- The **assign/reassign cross-ENI/cross-account takeover** primitive, EIP rides-along, link-local SG/NACL bypass → owned by `using-instance-addressing`; do not re-derive here.
- **Launch-time IPv4 assignment / shared-VPC forced public exposure / cross-tenant private-IP collision** → owned by `working-with-ip-addresses`.
- **Collateral EIP-disassociation on unassign** → owned by `instance-secondary-ip-addresses`.
- **IPv6 public-by-default-but-unscopable, IPv6 prefix bulk knob, no-AllowReassignment-on-IPv6** → owned by `working-with-ipv6-addresses`.
- **Host/Nitro side of any ENI / reserved service** — hard-stop disclosure boundary, never a test target.
- The per-ENI maxima themselves are **not Service-Quotas-raisable** (instance-type hardware properties), so there is no `servicequotas`/`support:CreateCase` increase-path surface on this page (contrast `fleet-quotas` Area 5).

## 8. Null hypotheses / doc gaps
- **Lens A (cross-tenant IDOR):** N/A on this page's own surface — the only read action returns public, non-tenant data (Area 4); the only mutating path (assign) is owned by siblings. Pages checked: target, `using-eni.md`, `ec2-prefix-eni.md`.
- **Lens B/C (PassRole / credential vending), E (RBAC privesc), K (prompt injection), F (translation/injection), W (attestation), FF (JWT), DD (cache), CC (upstream-context), BB (canonicalization), N (namespace migration), J (OAuth):** N/A — no role ARN, STS, LLM, parser, token, authorizer, cache, multi-parser request path, dual namespace, or 3P-link field on the target or its two adjacent pages. Pages checked: `AvailableIpPerENI.md`, `using-eni.md`, `ec2-prefix-eni.md`.
- **Lens G (SSRF), Q (upload):** N/A — no field the service dereferences/fetches, no uploaded blob (the only URLs on the page are documentation hyperlinks to the Instance Types Guide / CLI reference, not server-dereferenced inputs). Pages checked: target + adjacents.
- **Lens T (secret reachability), H (KMS):** N/A — the page generates/persists no secret or key.
- **Lens Y (transport/sig):** N/A — standard SigV4 EC2 control-plane; no transport claim on this page.
- **Lens O (audit evasion):** carried as a sub-lead of Area 1 (no purpose-built IP-assign EventBridge event — cross-ref config-windows-multiple-ip Area 3), not developed independently here.
- **Doc-gaps (confirm live, DryRun insufficient):** (a) actual per-type `Ipv6Supported` values vs the prose exception list (Area 3); (b) whether hitting the per-ENI ceiling / subnet exhaustion yields a clean attributable error vs generic (Area 1 attribution/oracle); (c) whether the IPv6 per-ENI counter is truly independent of the IPv4 counter (Area 3); (d) API-ref lowerCamelCase vs UserGuide PascalCase `NetworkInfo.*` casing origin (cosmetic; inference only).

---
*Cross-references: [[project-aws-research-plans]], [[reference-aws-iam-service-auth-ref-url]]. Siblings in the ec2-networking IP-addressing cluster: using-instance-addressing, working-with-ip-addresses, instance-secondary-ip-addresses, working-with-ipv6-addresses, config-windows-multiple-ip, ec2-networking (hub). Quota-page analogue: fleet-quotas.*
