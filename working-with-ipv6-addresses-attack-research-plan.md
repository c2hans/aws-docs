# Manage the IPv6 addresses for your EC2 instances — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-ipv6-addresses.html` (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/working-with-ipv6-addresses.md`, 267 lines; **offline == online byte-identical**, WebFetch of the live `.html` matches verbatim including `{{…}}` placeholder tokens — 2026-10-15). Supporting pages: `API_AssignIpv6Addresses` / `API_UnassignIpv6Addresses` / `API_AssignPrivateIpAddresses` (EC2 API Reference), `configuring-instance-metadata-options.md`, `instance-metadata-limiting-access.md`, `instancedata-data-retrieval.md`, `ec2-instance-metadata.md`, VPC `egress-only-internet-gateway.md`, `default-security-group.md`, `ipv4-ipv6-comparison.md`. IAM facts from `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (10,190 lines; read by **offline grep on the detailed `## Actions defined by Amazon EC2` table starting line 4603** — the online `.md`/summarizer fetch lands on the terse summary table and reports blank condition-key cells, a known truncation trap; see reference memory). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Relationship to siblings.** This is a **page-level deep-dive child of the `ec2-networking` hub** (`ec2-networking-attack-research-plan.md`) and the **IPv6 counterpart of `using-instance-addressing-attack-research-plan.md`**, which already OWNS: the secondary-*private-IPv4* cross-ENI/cross-account takeover via `AssignPrivateIpAddresses … AllowReassignment` (sibling Area 1), the general "no `ec2:PrivateIpAddress`/`ec2:Ipv6Address`/`AllowReassignment` key" gap (sibling Area 2), the link-local SG/NACL blind-spot (sibling Area 4), SG-per-ENI amplification (sibling Area 5), and a brief IPv6-is-*safer* lifecycle note (sibling Area 6). **This plan does NOT restate those** — it cross-references them and develops the IPv6-specific surface that the sibling only touched: IPv6's *public-by-default* exposure and its unscopability, IPv6 **prefix delegation** (a page-under-surfaced bulk knob), the IPv6 "no-forced-move but silent-conflict?" assign semantics (sibling Area 6 → mechanism level), and the page's shipped **IMDSv1 sample** + IPv6 IMDS endpoint `fd00:ec2::254`.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Many leads here are **AWS-owned IAM-expressiveness / documented-guarantee gaps** (Lens S/U/X) settleable *statically* with `iam:SimulateCustomPolicy` (no resources created) — do those first. The two that need a **live canary** (same-subnet in-use-IPv6 conflict; prefix-exhaustion) are flagged.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the Nitro/Xen host behind any link-local service — IMDS `169.254.169.254` / `[fd00:ec2::254]`, Route 53 Resolver, Time Sync, KMS), **stop, preserve evidence, flag for AWS-Security disclosure.** The host side of the metadata service is never a test target.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Prove an admin cannot forbid a globally-routable IPv6 address** on a launch or an assign — i.e. there is no IAM condition key equivalent to `ec2:AssociatePublicIpAddress` for IPv6, so a least-privilege/SCP author cannot keep an instance IPv6-dark. (Area 1 — headline, AWS-owned.)
2. **Delegate a whole IPv6 *prefix* (`Ipv6Prefix`/`Ipv6PrefixCount`) to an ENI** using only `ec2:AssignIpv6Addresses` on that ENI, via a knob the UserGuide page and console never surface — and show no IAM key or documented ceiling bounds how many addresses one call allocates (subnet exhaustion / noisy-neighbor in a shared subnet). (Area 2.)
3. **Settle the IPv6 assign-conflict semantics:** supply an explicit IPv6 that is already assigned to a *different* ENI in the same subnet (and one *outside* the subnet CIDR) and observe accept-and-steal vs clean error — the Errors section documents neither. (Area 3 — the IPv6 analogue of the sibling's IPv4 headline, needing a live two-ENI canary.)
4. **Confirm the page ships a working IMDSv1 (no-token) retrieval sample for `ipv6s`** while AWS elsewhere tells customers to enforce IMDSv2 — a Lens-U/R documentation defect; and that the IPv6 IMDS endpoint `[fd00:ec2::254]` is reachable past SG/NACL once enabled. (Area 4.)
5. **Enumerate what the `ipv6s` metadata category and its siblings disclose** as a self-scoped recon surface, and flag the `owner-id` ENI-ownership-mismatch nuance. (Area 5.)

---

## 2. Components, Assets, and Design

**Customer-facing interface.** Control-plane EC2 API/CLI/PowerShell + console. Four addressing entry points touched by this page:
- `RunInstances` with `--ipv6-addresses Ipv6Address=…` (explicit) **or** `--ipv6-address-count N` (EC2 picks) — assign at launch.
- `AssignIpv6Addresses` (`assign-ipv6-addresses` / `Register-EC2Ipv6AddressList`) — assign after launch.
- `UnassignIpv6Addresses` (`unassign-ipv6-addresses` / `Unregister-EC2Ipv6AddressList`).
- `DescribeInstances` — read `Instances[].Ipv6Address`.
- Plus an **in-instance read path**: IMDS at `http://169.254.169.254/latest/meta-data/network/interfaces/macs/<mac>/ipv6s` (and the IPv6 endpoint `[fd00:ec2::254]`).

**Assets.**
- **IPv6 address** — drawn from the VPC/subnet IPv6 CIDR; **globally unique and public by default** (`ipv4-ipv6-comparison.md` / `egress-only-internet-gateway.md`: *"IPv6 addresses are globally unique, and are therefore public by default."*). No RFC-1918/"private" analogue; no NAT. **Caller may specify the exact address** from the subnet range, or let EC2 choose. Assigned to the **primary ENI**. Not reassignable by a force-move flag ("must first unassign").
- **IPv6 prefix** — a delegated CIDR block (e.g. /80) on an ENI, via `Ipv6Prefix`/`Ipv6PrefixCount`. Readable from IMDS `…/ipv6-prefix`. **The UserGuide page does not mention prefixes at all** — only single addresses and `--ipv6-address-count`.
- **The absence of a public-IPv6 scoping key** — `ec2:AssociatePublicIpAddress` governs IPv4 auto-public-IP but has **no IPv6 twin** (0 hits for `AssociatePublicIpv6`/`PublicIpv6`). This *non-asset* is the headline.

**Resource / identifier shapes.** ENI id `eni-<17 hex>` (high entropy, not fabricable). IPv6 addresses / prefixes are **caller-supplied plain values**, NOT resources and NOT carrying any IAM condition key. A **subnet** can be **RAM-shared across accounts (VPC sharing)** → owner and participant ENIs co-reside in one subnet and share the IPv6 CIDR = the cross-account adjacency relevant to Area 3.

**Identity.** SigV4 IAM on the control plane. The four addressing actions carry **no role-ARN / PassRole / URL / token / KMS input** → Lens B/C/G/H/T null here (see §8).

```
  caller (IAM principal)
        │  RunInstances --ipv6-addresses|--ipv6-address-count   (launch-time)
        │  AssignIpv6Addresses(--network-interface-id, --ipv6-addresses | --ipv6-address-count | --ipv6-prefix | --ipv6-prefix-count)
        │  UnassignIpv6Addresses(--network-interface-id, --ipv6-addresses | --ipv6-prefix)
        ▼
   ENI (eni-… ; authz bound HERE, to network-interface*)
        │  holds: [primary IPv6] [secondary IPv6 …] [IPv6 prefix …]
   subnet IPv6 CIDR  ◄── globally-routable; reachability = f(route table: IGW↔ / EIGW→ / none) ──►  internet
        │  (subnet may be RAM-SHARED: acct A + acct B ENIs co-reside, share the IPv6 CIDR)
        ▼
   instance OS ──IMDS──► 169.254.169.254 / [fd00:ec2::254]  →  …/ipv6s, …/ipv6-prefix, …/owner-id  (NOT SG/NACL-filtered)
```

### Mandatory coverage sweep (pages read, per Step-1 discipline)
- **URL/dereference fields (Lens G):** none on this page's APIs — IPv6 values/prefixes are identifiers, not fetched URLs. The only server-reachable targets *from* the instance are the link-local host services (Area 4/5, distinct mechanism, instance-initiated). Read: the main page + `API_AssignIpv6Addresses`/`API_UnassignIpv6Addresses`. → G null (named in §8).
- **Upload/blob fields (Lens Q):** none — no file/image/blob param on any addressing API. Read: main + both API refs. → Q null.
- **Privileged-gate / consent steps (Lens P):** the IPv4 path's `AllowReassignment` consent flag is **absent** on the IPv6 API (confirmed) → no caller-set consent primitive here; the only "gate" is the subnet having an IPv6 CIDR. → P null (named).
- **"Revealed only after a step" (Lens A disclosure-timing):** none on this page.
- **IAM policy JSON / managed-policy / sample blocks (Lens R/S):** the page prints **no IAM JSON**, but it **ships copy-paste CLI/shell samples**, one of which is a working **IMDSv1 no-token** retrieval → audited as a shipped-artifact weak-default under Area 4 (Lens R/U). The IAM-expressiveness audit (Area 1/2) is done against `list_ec2.md` directly.
- **Secrets persisted (Lens T):** none — no key/token generated or stored. → T null.
- **Security guarantees asserted (Lens U):** "IPv6 … public by default", "must first unassign", default-SG auto-adds `::/0` outbound, IMDS "not filtered by SG/NACL", IPv6 IMDS endpoint "must be explicitly enabled" → traced to mechanisms in Areas 1/3/4.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Admin authoring a least-privilege policy / SCP | The *public-IPv6 exposure* of an instance | IAM `Condition` on `RunInstances`/`AssignIpv6Addresses` | **Breach of the guarantee = there is NO `ec2:AssociatePublicIpv6`/IPv6-address condition key** → the policy cannot express "do not give this workload a globally-routable address" the way `ec2:AssociatePublicIpAddress` lets it for IPv4. |
| Caller with `ec2:AssignIpv6Addresses` on one ENI | Subnet IPv6 CIDR capacity (shared by co-resident ENIs/tenants) | `Ipv6Prefix`/`Ipv6PrefixCount` bulk delegation | One call delegates a whole prefix (many thousands of addresses); **no IAM key and no documented ceiling** bound it → exhaustion/noisy-neighbor in a RAM-shared subnet. |
| Caller owning `eni-ATK` in a subnet | An in-use IPv6 on a foreign `eni-VIC` in the same (possibly RAM-shared) subnet | `AssignIpv6Addresses --ipv6-addresses <IP-in-use>` | **Breach = EC2 moves/accepts the in-use address with no permission on `eni-VIC`** (silent steal); clean refute = a documented/returned conflict error. The Errors section documents **neither** outcome. |
| Instance OS process (any, incl. a hijacked one) | Host metadata service (IPv4 + `[fd00:ec2::254]`) | Link-local HTTP, **not SG/NACL-filtered** | Reaching `…/ipv6s`/`…/owner-id` with **no token** (IMDSv1) is the page's own sample → confirms the weak path works; **host side is the hard-stop boundary.** |
| Any customer surface | AWS's own service plane (Nitro/Xen host behind link-local) | — | **Any identity/credential/ARN/account belonging to AWS's fleet = hard-stop breach.** |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internet-callable | Functionality | Authorized callers | Notes (IAM, from `list_ec2.md` detailed table) |
|---|---|---|---|---|---|---|---|
| `AssignIpv6Addresses` | SDK/CLI | Existing | **Yes** | Yes | Add IPv6 addr(s) **or prefix(es)** to an ENI | holder of the action on the target ENI | req `network-interface*`; keys **(L4697)**: `aws:ResourceTag/${K}`, `ec2:AvailabilityZone`, `ec2:ManagedResourceOperator`, `ec2:NetworkInterfaceID`, `ec2:Region`, `ec2:ResourceTag/${K}`, `ec2:Subnet`, `ec2:Vpc`. **No address/prefix-level key; no `AllowReassignment` param.** API params: `Ipv6AddressCount`, `Ipv6Addresses.N`, `Ipv6Prefix.N`, `Ipv6PrefixCount`, `NetworkInterfaceId*`. |
| `UnassignIpv6Addresses` | SDK/CLI | Existing | Yes | Yes | Remove IPv6 addr(s)/prefix(es) | holder on the ENI | req `network-interface*`; **same 8 keys (L9693)**. API params: `Ipv6Addresses.N`, `Ipv6Prefix.N`, `NetworkInterfaceId*` (no count-based bulk unassign documented). |
| `RunInstances` (`--ipv6-addresses`/`--ipv6-address-count`) | SDK/CLI | Existing | Yes | Yes | Assign IPv6 at launch | launcher | **No `ec2:Ipv6*` key on any RunInstances resource row** (grepped). `ec2:AssociatePublicIpAddress` (Bool, L10050) present on the `network-interface*` row — **IPv4-only; no IPv6 twin.** |
| `DescribeInstances` | SDK/CLI | Existing | **No** | Yes | Read `Instances[].Ipv6Address` | caller | read-side; cross-ref hub's unscopable-Describe oracle family. |
| IMDS `…/macs/<mac>/ipv6s` (+ `ipv6-prefix`, `subnet-ipv6-cidr-blocks`, `vpc-ipv6-cidr-blocks`, `owner-id`) | HTTP (in-instance) | Existing | No | **No** (link-local) | Read own ENI IPv6 data | any process on the instance | **Not SG/NACL-filtered**; IMDSv1 (no-token) sample shipped on this page; IPv6 endpoint `[fd00:ec2::254]` must be explicitly enabled. |

**Console-/page-under-surfaced knob (the inventory delta to chase first):** `Ipv6Prefix.N` / `Ipv6PrefixCount` on `AssignIpv6Addresses`. The **API reference documents them**, but **the UserGuide page and its console procedure show only single `Ipv6Address` values and `--ipv6-address-count`** — a reader following the page would never know a single `assign-ipv6-addresses` call can delegate an entire prefix. (This is a *page-level* under-surfacing, not a fully console-hidden API knob — state it precisely; do not over-claim it as undocumented.)

---

## 5. Recommended Areas of Focus

### Area 1 — IPv6 is public-by-default, yet no IAM key can forbid it (the missing `ec2:AssociatePublicIpv6`) *(HEADLINE)*
**Lens U / S / X (AWS-owned enforcement/expressiveness gap, Tier-2 reportable). Severity: Medium (High-impact as the structural enabler of unintended internet exposure).**

**Background.** `ipv4-ipv6-comparison.md` / `egress-only-internet-gateway.md`: *"IPv6 addresses are globally unique, and are therefore public by default."* There is no private/RFC-1918 IPv6 and no NAT; the IPv6 analogue of a NAT gateway is the **egress-only internet gateway**, and *"You can't associate a security group with an egress-only internet gateway … You can use a network ACL to control the traffic."* The console surfaces IPv6 assignment as a single innocuous **"Auto-assign IPv6 IP"** checkbox at launch (page, Console tab). Separately, `default-security-group.md` shows the default SG **auto-adds an outbound `::/0` allow-all rule "only if your VPC has an associated IPv6 CIDR block."**

**Security Concern.** For IPv4, an admin *can* forbid an instance from getting a public address: `ec2:AssociatePublicIpAddress` is a real Bool condition key (L10050) on `RunInstances`'s `network-interface*` row. **For IPv6 there is no equivalent** — grep of all 10,190 lines of `list_ec2.md`: `AssociatePublicIpv6`/`PublicIpv6` = **0 hits**, and no `ec2:Ipv6*` key attaches to `RunInstances`, `AssignIpv6Addresses`, or `UnassignIpv6Addresses` (the only IPv6 key in the whole catalog, `ec2:Ipv6IpamPoolId`, is a CIDR/IPAM-pool key on `Associate/Create Subnet/Vpc`, L4804/4836/5480/5753/10103). So an admin **cannot** author an identity policy or SCP that says "this workload may launch, but must not receive a globally-routable IPv6 address" — because every assigned IPv6 *is* globally routable, this is the direct IPv6 counterpart of forbidding a public IPv4, and the lever simply does not exist. The capability to express it exists in the service for IPv4 and was not provided for IPv6 — a **Lens-X action-family parity gap** (IPv4 twin scopable, IPv6 twin not) on top of the Lens-U guarantee gap.

**High-level Test Scenarios.**
- **Claim:** No IAM policy can prevent `RunInstances`/`AssignIpv6Addresses` from giving an instance a globally-routable IPv6. → **Oracle:** `iam:SimulateCustomPolicy` with a `Deny` keyed on a fabricated `ec2:AssociatePublicIpv6` (and on `ec2:Ipv6Address`) → the condition is **silently ignored / inert** (the Lens-S "key does not exist" failure shape, cf. the `ec2:InterfaceType` precedent) and the action is **Allowed**; the *IPv4* `Deny` keyed on `ec2:AssociatePublicIpAddress` on the same simulated `RunInstances` **is honored** — proving the parity gap. No resources created.
- **Claim (chain):** Reachability isn't only the SG — the default SG's auto-added `::/0` outbound rule + an IGW route for `::/0` make an "Auto-assign IPv6 IP" instance bidirectionally internet-reachable with no explicit operator action an IPv4-trained reviewer would flag. → **Oracle (doc-level, confirmed):** `default-security-group.md` outbound `::/0 All All`; `ipv4-ipv6-comparison.md` IGW-vs-EIGW routing. Severity rises where the subnet route table points `::/0` at a full IGW rather than an egress-only IGW.

**Doc evidence:** `list_ec2.md` L10050 (`ec2:AssociatePublicIpAddress`), L9982, grep (0 IPv6-public key); `ipv4-ipv6-comparison.md`; `egress-only-internet-gateway.md`; `default-security-group.md`. **In scope as an AWS-owned expressiveness gap**, not a customer footgun — the key does not exist to be used. **Stop condition:** once Simulate shows the IPv4 key honored and no IPv6 key exists, the gap is proven; the *runtime* exposure is a product-posture observation, not a further test.

### Area 2 — IPv6 Prefix Delegation: a page-under-surfaced bulk-allocation knob with no scoping or ceiling
**Lens L / U / A. Severity: Medium (cross-tenant subnet exhaustion on a shared subnet; otherwise single-tenant).**

**Background.** `API_AssignIpv6Addresses` accepts `Ipv6Prefix.N` (array of CIDRs) and `Ipv6PrefixCount` (Integer) — delegating one or more **IPv6 prefixes** (e.g. /80 blocks) to the ENI in a single call. The UserGuide page (this target) and its console procedure **never mention prefixes** — they show only explicit single `Ipv6Address` values and `--ipv6-address-count`. The delegated prefix is itself exposed via IMDS `…/ipv6-prefix`.

**Security Concern.** Authorization for the delegating call is bound **only** to the target `network-interface*` (same 8 keys, L4697); there is **no condition key for the prefix, its size, or its count** (grep: no `ec2:Ipv6Prefix*` key), and the API Errors section documents **no action-specific limit or rejection** (only generic `CommonErrors`). A caller holding merely `ec2:AssignIpv6Addresses` on an ENI can therefore request a large `Ipv6PrefixCount` and/or large prefixes, allocating a very large number of addresses from the subnet's IPv6 CIDR in one call. In a **RAM-shared subnet**, co-resident ENIs/tenants draw from the same CIDR → a Lens-L cross-tenant exhaustion / noisy-neighbor shape; even single-tenant, it is an un-guardrail-able allocation primitive the operator reading the page would not anticipate.

**High-level Test Scenarios.**
- **Claim:** `assign-ipv6-addresses --network-interface-id eni-MINE --ipv6-prefix-count <large>` succeeds with only the ENI-level permission, allocating prefixes the page never told the operator were possible. → **Oracle (live canary, cheap):** issue the call on a self-owned ENI; `describe-network-interfaces` shows `Ipv6Prefixes` populated. Refute = a documented `ValidationException`/limit (none is documented). → **Preconditions:** one owned ENI in an IPv6 subnet. → **Cost:** trivial. → **Severity:** Medium (High if a co-tenant in a shared subnet is denied addresses as a result — a cross-tenant availability oracle).
- **Claim:** No IAM policy can cap prefix size/count or forbid prefix delegation while allowing single-address assign. → **Oracle:** `iam:SimulateCustomPolicy` with a `Deny` on a fabricated `ec2:Ipv6PrefixCount`/`ec2:Ipv6Prefix` → inert.

**Doc evidence:** `API_AssignIpv6Addresses` (params `Ipv6Prefix.N`/`Ipv6PrefixCount`); page omission; `ec2-instance-metadata.md` (`…/ipv6-prefix`); `list_ec2.md` L4697. **Doc-gap to settle live:** the per-ENI / per-subnet prefix quota and whether EC2 clamps vs rejects — not documented on any page checked.

### Area 3 — IPv6 assign-conflict semantics: no forced-move, but what happens on an in-use / out-of-range address? *(develops sibling Area 6 to mechanism level)*
**Lens A / X. Severity: Informational→Medium (confirms the IPv4 takeover does NOT extend to IPv6; the residual open question is same-subnet in-use conflict).**

**Background.** The page: *"You can specify an IPv6 address from the IPv6 address range of the subnet, or let Amazon EC2 choose one for you,"* and the console step *"Enter an IPv6 address from the range of the subnet, or leave the field blank."* The sibling plan established IPv6 *"cannot be reassigned to another network interface — you must first unassign it."* **Confirmed:** `API_AssignIpv6Addresses` has **no `AllowReassignment` parameter** (the IPv4 twin `AssignPrivateIpAddresses` *does* — *"Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned"*). So the sibling's **IPv4 force-move primitive (sibling Area 1) does NOT extend to IPv6** — a genuine narrowing, not a bug.

**Security Concern.** That leaves exactly one undocumented edge: the caller **can still name an explicit IPv6**, and **neither** the API Errors section **nor** any prose documents what happens if that address is (a) **already assigned to a different ENI in the same subnet** or (b) **outside the subnet's IPv6 CIDR**. Both `AssignIpv6Addresses` and `UnassignIpv6Addresses` document only generic `CommonErrors` — no conflict/range error code. The expected safe behavior (given no `AllowReassignment`) is a clean rejection of an in-use address; the thing worth confirming is that EC2 does **not** silently reassign or silently no-op in a way that produces a race or a misleading success. Because subnets are RAM-shareable, the "different ENI in the same subnet" can be **cross-account**.

**High-level Test Scenarios.**
- **Claim (expected refute — this is a safety-confirmation test):** `assign-ipv6-addresses --network-interface-id eni-ATK --ipv6-addresses <IPv6-in-use-on eni-VIC>` is **rejected** (no `AllowReassignment` exists to force it). → **Oracle:** the call returns an error and `describe-network-interfaces` shows `eni-VIC` **still holds** the address. A *breach* would be the address silently moving to `eni-ATK` (or a success response that leaves state inconsistent). → **Preconditions:** two ENIs in one subnet (then the RAM-shared cross-account variant). → **Cost:** two canary ENIs. → **Severity:** Medium-if-breached (same-subnet IPv6 takeover, no force flag needed); Informational if cleanly rejected (documents the IPv4-vs-IPv6 asymmetry). → **Stop:** a clean reject closes this lead.
- **Claim:** An out-of-subnet-CIDR IPv6 is rejected (not silently accepted/dropped). → **Oracle:** error vs silent drop; silent drop = provisioning-integrity confusion (Lens U), low.
- **Takeover-via-unassign note (cross-ref, do not re-run):** the only IPv6 "takeover" path is `UnassignIpv6Addresses` on the **victim** ENI, which **is** authz-scoped to that ENI (L9693) — so it needs a permission the IPv4 `AllowReassignment` path does not. This is the sibling's Area 6 point; owned there.

**Doc evidence:** page (specify-from-range sentences); `API_AssignIpv6Addresses`/`API_UnassignIpv6Addresses` (no `AllowReassignment`, generic Errors only); `API_AssignPrivateIpAddresses` (`AllowReassignment` present — the contrast); `list_ec2.md` L4697/L9693. **Doc-gap to settle live:** the in-use-and-out-of-range outcomes — `DryRun`/Simulate cannot answer (caller-IAM only, evaluated before resource resolution — a false-positive trap); needs the real two-ENI call.

### Area 4 — The page ships a working IMDSv1 (no-token) sample while AWS pushes IMDSv2; IPv6 IMDS endpoint past SG/NACL
**Lens U / R (shipped-artifact weak default) + V (segmentation blind-spot). Severity: Low–Informational (doc defect) with a High-severity dependency if the sample is copied onto an SSRF-exposed workload.**

**Background.** The page's **"View IPv6 addresses using instance metadata"** section provides two tabs: an `IMDSv2` flow (token `PUT` then `GET` with `X-aws-ec2-metadata-token`) **and** an `IMDSv1` tab with the verbatim no-token command `curl http://169.254.169.254/latest/meta-data/network/interfaces/macs/{{mac-address}}/ipv6s` (+ a PowerShell `Invoke-RestMethod -Uri http://169.254.169.254/...` twin). Meanwhile `instancedata-data-retrieval.md` and `instance-metadata-transition-to-version-2.md` tell customers to move to and **enforce** IMDSv2 (`HttpTokens=required`), framing IMDSv1 as the weaker legacy mode.

**Security Concern.** This is a **Lens-U/R documentation defect**: AWS ships a copy-paste IMDSv1 sample on a current page while its own hardening guidance says to disable IMDSv1. A reader who copies the IMDSv1 form normalizes the token-less pattern that is precisely what an SSRF on the instance can reach. Compounding it (cross-ref sibling Area 4): `instance-metadata-limiting-access.md` confirms **SG/NACL do not filter IMDS** — mitigation is pushed to local firewall / network-appliance drops of dest `169.254.169.254` **and** `[fd00:ec2::254]`. The **IPv6 IMDS endpoint `[fd00:ec2::254]`** (`configuring-instance-metadata-options.md`) is net-new to this surface: it is **off unless explicitly enabled** (the `HttpProtocolIpv6` option), Nitro-only, and once on it is reachable past SG/NACL just like the IPv4 endpoint — a second metadata ingress an operator who hardened only the IPv4 address would miss.

**High-level Test Scenarios.**
- **Claim:** The current page presents a functional no-token IMDSv1 retrieval for `ipv6s` (weak-default sample). → **Oracle (doc-level, confirmed):** the `IMDSv1` tab text, verbatim offline==online. File as a Lens-U/R finding (AWS-authored, uneditable sample on a live page).
- **Claim:** Enabling `HttpProtocolIpv6` opens `[fd00:ec2::254]` as a second metadata ingress not covered by SG/NACL, so an IMDS egress control that only drops the IPv4 address is incomplete. → **Oracle (doc-level):** `instance-metadata-limiting-access.md` recommends dropping **both** addresses — the recommendation's existence proves the IPv6 endpoint is an independent reachable path. **HARD STOP** on any evidence from the host side.

**Doc evidence:** page "View IPv6 addresses using instance metadata" (IMDSv1 tab); `instancedata-data-retrieval.md`; `instance-metadata-transition-to-version-2.md`; `instance-metadata-limiting-access.md` ("drop packets with the destination IPv4 address … `169.254.169.254` and … the IPv6 address … `[fd00:ec2::254]`"); `configuring-instance-metadata-options.md` (IPv6 endpoint must be explicitly enabled). **Scope note:** IMDS as a generic SSRF target is owned by the instance-metadata plans and out-of-scope here except as this **shipped-sample** defect + the IPv6-endpoint segmentation fact.

### Area 5 — The `ipv6s` metadata category and siblings as a self-scoped recon surface; the `owner-id` ownership-mismatch nuance
**Lens A (read oracle) / O. Severity: Low (self-scoped; informational ownership nuance).**

**Background.** `ec2-instance-metadata.md` category table: `network/interfaces/macs/<mac>/ipv6s` = *"The IPv6 addresses assigned to the interface,"* with siblings `ipv6-prefix`, `subnet-ipv6-cidr-blocks`, `vpc-ipv6-cidr-blocks`, and non-IPv6 rows `owner-id`, `security-groups`/`security-group-ids`, `vpc-id`, `subnet-id`, `interface-id`.

**Security Concern.** This path is **self-scoped** (an instance reads only its own attached ENIs) — no documented cross-tenant leak, so it is **not** an IDOR. The one nuance worth flagging: `owner-id` is *"The ID of the owner of the network interface … an interface can be attached by a third party, such as Elastic Load Balancing … Traffic on an interface is always billed to the interface owner."* So metadata about an ENI attached to "your" instance can reflect a **different account's** resource (ELB-, service-, or RAM-attached ENI) — an ownership-mismatch surface relevant to ENI-confusion / confused-deputy reasoning (cross-ref the hub's `DeleteNetworkInterfacePermission` cross-account-ENI lead), not a secret leak.

**High-level Test Scenarios.**
- **Claim:** `…/owner-id` on a multi-attach / service-attached ENI returns an account id other than the instance owner's. → **Oracle:** compare `owner-id` to the instance's account on an ELB-attached ENI. → **Severity:** Low/Informational; feeds ENI-ownership analysis owned by the hub.

**Doc evidence:** `ec2-instance-metadata.md` category rows. → explicitly **not** a cross-tenant finding; recorded so a hunter does not over-invest.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Forbid a workload from getting a globally-routable IPv6 | `RunInstances`/`AssignIpv6Addresses` IAM | **No `ec2:AssociatePublicIpv6`/IPv6-address key** (vs IPv4's `ec2:AssociatePublicIpAddress`); prove inert via Simulate |
| Bulk-delegate an IPv6 prefix with only ENI-level permission | `AssignIpv6Addresses` `Ipv6Prefix`/`Ipv6PrefixCount` | page omits the knob; no prefix/count condition key; no documented ceiling |
| Steal an in-use IPv6 off a foreign same-subnet ENI | `AssignIpv6Addresses --ipv6-addresses` | **no `AllowReassignment`** on IPv6 (expected clean reject) — confirm EC2 does not silently reassign; test RAM-shared cross-account variant |
| Retrieve `ipv6s` with no token on a live page's sample | IMDS / page sample | AWS's own IMDSv2-enforcement guidance contradicts the shipped IMDSv1 sample |
| IMDS egress control that only blocks IPv4 `169.254.169.254` | `[fd00:ec2::254]` endpoint | `instance-metadata-limiting-access.md` says drop **both** addresses; endpoint off-by-default (`HttpProtocolIpv6`) |

---

## 7. Out-of-Scope Risk Categories
- **IMDS as a generic SSRF/credential target** on managed or customer instances — owned by the instance-metadata plans; in scope here only as (a) the **shipped IMDSv1 sample** defect and (b) the **IPv6 IMDS endpoint** segmentation fact (Area 4). The **host/Nitro side of any link-local service is a hard-stop** disclosure boundary, never a test target.
- **Customer-authored IAM policies** that over-grant `ec2:AssignIpv6Addresses`/`RunInstances` on `*` — a customer footgun (out of scope); the in-scope point is that **AWS provides no condition key** to scope IPv6 exposure/prefix allocation (Areas 1/2).
- **The IPv4 secondary-address takeover, the general no-address-key gap, the link-local SG/NACL blind-spot mechanism, and SG-per-ENI amplification** — owned by `using-instance-addressing-attack-research-plan.md` (sibling Areas 1/2/4/5); cross-referenced, not re-tested.
- **Single-tenant IPv6 exhaustion** (Area 2) is Low/out-of-scope except as a cross-tenant noisy-neighbor amplifier in a RAM-shared subnet.
- **The intrinsic internet-routability of IPv6** is a product-design property, not a bug; in scope only as the *IAM-expressiveness gap* that it cannot be forbidden (Area 1).

---

## 8. Null hypotheses / doc gaps (lenses that did not fire, pages named)
- **Lens B / C (PassRole / credential-vending):** N/A — `AssignIpv6Addresses`/`UnassignIpv6Addresses`/`RunInstances`(IPv6 params)/`DescribeInstances` take **no role ARN, no session-policy, no token** input. Read: main page + both API refs. No role is assumed on the caller's behalf.
- **Lens G (SSRF via a server-dereferenced field):** N/A for the page's own APIs — IPv6 addresses/prefixes are identifiers, not URLs the service fetches. The only server-side-reachable targets are the instance-initiated link-local host services (Area 4/5). Pages: main + API refs.
- **Lens Q (upload):** N/A — no file/image/blob field on any addressing API.
- **Lens H / T (KMS / persisted secret):** N/A — no key/encryption-context/secret generated or stored by this surface.
- **Lens K (prompt injection), F (translation/wire-protocol), W (attestation), FF (JWT), DD (cache), BB/CC (parser/upstream-context), J (OAuth):** N/A — no LLM/agent, no translation layer, no attestation gate, no token-validation, no caching layer, no OAuth/3P linking, no multi-parser request path on this control-plane addressing surface.
- **Lens P (proofing/consent gate):** N/A — the IPv4 `AllowReassignment` consent primitive is **absent** on the IPv6 API (confirmed); the only precondition is the subnet owning an IPv6 CIDR.
- **Lens A (cross-tenant IDOR):** the IMDS read path (Area 5) is self-scoped (not IDOR); the only cross-account adjacency is the RAM-shared-subnet variant of Area 3, which is a mutation-conflict question, not a read-IDOR. IPv6 addresses are not fabricable blind cross-account.
- **Doc-gaps to confirm live before investing:** (1) **in-use / out-of-range IPv6 assign** outcome (Area 3 — needs two real ENIs; `DryRun`/Simulate cannot answer); (2) **per-ENI / per-subnet IPv6 prefix quota and clamp-vs-reject** (Area 2); (3) **cross-account** behavior of both in a RAM-shared subnet. Re-check all cited `list_ec2.md` lines live (offline==online held 2026-10-15, but the IAM reference changes) — read the **detailed** `## Actions defined by Amazon EC2` table (from L4603), not the terse summary table the online fetch truncates to. See reference memory on the `list_ec2` slug/truncation trap.
```
```

🤖 Generated with [Claude Code](https://claude.com/claude-code)
