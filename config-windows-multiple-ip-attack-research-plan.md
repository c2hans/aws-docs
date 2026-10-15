# EC2 "Configure secondary private IPv4 addresses for Windows instances" — Attack Research Plan

Source of leads: `config-windows-multiple-ip.html` / offline `/work/aws-docs/docs/AWSEC2/latest/UserGuide/config-windows-multiple-ip.md` ("Configure secondary private IPv4 addresses for Windows instances"), plus its prerequisite `instance-secondary-ip-addresses.html` and the EC2 IAM reference `list_ec2`. Status: documentation-derived hypotheses only; nothing tested against a live account.

> **Scope note — this is a page-level child, NOT a new hub.** This page is a Windows *guest-OS configuration how-to*: it introduces **no new EC2 API, parameter, role, URL, upload, or cross-account surface**. The control-plane mechanism it depends on — assigning/reassigning a secondary private IPv4 via `AssignPrivateIpAddresses … AllowReassignment=true` — is **already OWNED** by `using-instance-addressing-attack-research-plan.md` (its Area 1 cross-ENI/cross-account secondary-IP takeover) and must NOT be restated here. This plan owns exactly one net-new surface the siblings leave open: **the Windows-specific severing of the guest-OS↔control-plane IP binding (static conversion), and the stale-binding / split-brain / detection-blindness it creates when the control plane reassigns the IP underneath it.** All control-plane IAM/takeover depth is cross-referenced, not re-derived.
>
> **Related plans (cross-ref, do not duplicate):**
> - `using-instance-addressing-attack-research-plan.md` — OWNS `AssignPrivateIpAddresses`/`AllowReassignment` secondary-IPv4 cross-ENI takeover, ephemeral public-IP reuse, link-local SG/NACL blind spot, SG-per-ENI.
> - `working-with-ip-addresses-attack-research-plan.md` — launch-time IPv4 assignment, `ec2:AssociatePublicIpAddress` inert-Deny, shared-VPC public exposure, `DescribeInstances` unscopable oracle.
> - `working-with-ipv6-addresses-attack-research-plan.md` — IPv6 instance addressing (IPv6 is SAFER on the force-move axis: no `AllowReassignment`).
> - `ec2-networking-attack-research-plan.md` — hub (ENI permissions, EIP transfer, shared-VPC isolation).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The highest-value lead here (Area 1) is a **chain**: it uses the sibling-owned control-plane takeover primitive as its *entry* and this page's static-conversion as its *amplifier*. Rate it at the severity of the chain's end.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the host/Nitro side of any link-local service, the DHCP/ENI backplane), stop, preserve evidence, flag for AWS-Security disclosure. The guest OS and the customer's own ENIs are the only test surface.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Prove the stale guest-OS binding survives a control-plane reassignment:** after a secondary private IPv4 is reassigned away from a Windows instance (victim V) to another ENI (attacker A) via the sibling's `AssignPrivateIpAddresses … AllowReassignment=true` primitive, show that V's Windows guest **still claims and sources traffic from that IP** (static config persists, no DHCP renew to correct it) → an in-subnet IP conflict / split-brain between V and A that V's owner is not notified of.
2. **Quantify the Windows-vs-Linux amplification:** confirm that the AWS-authored Windows procedure deliberately converts the guest to static (severing DHCP reflection) where Amazon Linux's `ec2-net-utils` would auto-reconcile the same reassignment on lease renewal — i.e. the same control-plane action is *more* damaging and *longer-lived* on a Windows guest that followed this page.
3. **Map the detection blind spot:** determine whether the losing instance's owner has any signal (EventBridge event / distinct CloudTrail record / guest-OS event) that their secondary IP was reassigned, or whether the only authoritative truth is a `DescribeNetworkInterfaces`/`DescribeInstances` poll the owner must initiate.
4. **Application-layer persistence:** show that an IIS site bound to the (now-reassigned) secondary private IP (Step 3) keeps the binding in the guest, so service availability/routing follows the stale OS view rather than the control-plane truth.

## 2. Components, Assets, and Design

**Customer-facing interface of THIS page:** none that is an API — the page drives the **Windows guest operating system** (Network & Sharing Center / `ncpa.cpl`, Internet Protocol Version 4 (TCP/IPv4) Properties, Advanced TCP/IP "IP Settings", IIS Manager site bindings) and the `ipconfig /all` PowerShell command. The only AWS-API dependency is the **prerequisite** (control-plane assignment of the secondary IP), which lives on another page.

**The asset at risk:** the **binding between a private IPv4 address and the correct ENI/guest**, and everything that trusts it as a stable identity — in-VPC service reachability, source-IP-based ACLs/allowlists, and the IIS site binding.

**The design seam (the whole point of this plan):** there are **two independent record-keepers for the same IP**:
- **Control plane (authoritative):** the EC2/VPC backplane holds the real ENI↔private-IPv4 mapping; it is mutated by `AssignPrivateIpAddresses` / `UnassignPrivateIpAddresses` and reflected to a DHCP-managed guest on lease renewal. This is the source of truth for routing and for which ENI the subnet delivers the IP's packets to.
- **Guest OS (advisory, now static):** after this page's Step 1, the Windows guest holds a **hand-typed static copy** of the primary + secondary IPs with **no feedback channel** back to the control plane ("now this information is static and not managed by DHCP", line 97).

```
   Control plane (authoritative)                 Windows guest (advisory, STATIC)
   ┌──────────────────────────┐                  ┌───────────────────────────────┐
   │ ENI eni-V ⇄ 10.200.0.129  │   assign/        │ TCP/IPv4: 10.200.0.128 (static)│
   │ (secondary private IPv4)  │   unassign/       │           10.200.0.129 (static)│
   │                          │   AllowReassign  │ IIS site bound to .129          │
   └──────────┬───────────────┘   (sibling-owned) └───────────────┬───────────────┘
              │                                                   │
   AssignPrivateIpAddresses(eni-A, .129, AllowReassignment=true)  │ NO feedback / no renew
              ▼                                                   ▼
   ENI eni-A (attacker) now owns .129  ───────────X───────────  guest V still believes it owns .129
                        = SPLIT-BRAIN / stale binding (this plan's surface)
```

On a **DHCP** guest the lower-right box would re-sync on the next lease renewal (Amazon Linux `ec2-net-utils` "refreshes secondary IPv4 addresses during DHCP lease renewal", `instance-secondary-ip-addresses.md:113`). This page **removes that re-sync** for Windows. That removal is the vulnerability-relevant delta.

**Identity / roles:** none introduced by this page. All authz lives on the prerequisite control-plane action (owned by the sibling).

**Where untrusted data enters:** nowhere on this page server-side (no field the service dereferences, no upload, no URL, no token). The only "input" is the operator hand-typing IPs into the OS and the IIS binding selection — both local to the guest.

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| (prerequisite) `AssignPrivateIpAddresses` | SigV4 | Existing | Yes | External | Assign/reassign secondary private IPv4 to an ENI | Yes | caller w/ `ec2:AssignPrivateIpAddresses` on target `network-interface*` | **Owned by `using-instance-addressing` plan.** Carries `AllowReassignment`; force-moves the IP (and any associated EIP) with no source-owner check. |
| (prerequisite) `UnassignPrivateIpAddresses` | SigV4 | Existing | Yes | External | Remove a secondary private IPv4 from an ENI | Yes | caller w/ `ec2:UnassignPrivateIpAddresses` on target `network-interface*` | Cross-ref sibling. Does the guest learn it lost the IP? (Area 3) |
| `DescribeNetworkInterfaces` / `DescribeInstances` | SigV4 | Existing | No | External | Read the authoritative ENI↔IP map | Yes | — | The only way the owner detects the split-brain (Area 3). Unscopable read oracle (cross-ref `working-with-ip-addresses` Area 7). |
| Windows guest TCP/IPv4 static config | OS GUI | Existing | n/a | Internal-to-guest | Hard-codes primary+secondary IP in the guest | No | local admin on the instance | THIS page. No feedback to control plane. |
| IIS site binding | OS GUI | Existing | n/a | Internal-to-guest | Binds a website to the secondary private IP | No | local admin on the instance | THIS page, Step 3. Stale on reassignment. |

No `[NEW]` markers on this page. No undocumented/console-hidden API knob (the page is pure OS procedure).

---

## 5. Recommended Areas of Focus

### Area 1 — Stale guest-OS static binding survives a control-plane reassignment → split-brain IP claim (HEADLINE; Lens U + AA, chained to sibling `using-instance-addressing` Area 1)

**Background.** This page's Step 1 converts the Windows guest from DHCP to **static** IPv4 addressing and tells the operator to hand-enter the primary and secondary private IPv4 addresses: *"To enable your Windows instance to use multiple IP addresses, you must configure your instance to use static IP addressing rather than a DHCP server"* (`:26`) and *"The instance retains the same IP address information as before, but now this information is static and not managed by DHCP"* (`:97`). Independently, the control plane allows a secondary private IPv4 to be **reassigned to a different ENI**: *"Secondary private IPv4 addresses that are assigned to a network interface can be reassigned to another one if you explicitly allow it"* (`using-instance-addressing.md`), via `AssignPrivateIpAddresses … AllowReassignment=true` (sibling-owned). AWS even documents this as a *feature*: *"Redirect internal traffic to a standby instance in case your instance fails, by reassigning the secondary IP address to the standby instance"* (`using-instance-addressing.md`, Use cases).

**Security Concern.** The guest's static config has **no feedback channel** to the control plane. When the secondary IP is reassigned away from the Windows instance (whether maliciously via the sibling's takeover primitive, or benignly by a failover tool), the Windows guest **keeps the IP in its static TCP/IPv4 config and keeps claiming it** — there is no DHCP lease to expire and re-pull the correct set. The API reference confirms the only documented confirmation path is a pull the *gaining* side performs, never a push to the loser: *"Remapping an IP address is an asynchronous operation. When you move an IP address from one network interface to another, check `network/interfaces/macs/mac/local-ipv4s` in the instance metadata to confirm that the remapping is complete"* (`API_AssignPrivateIpAddresses.md`). A statically-configured Windows guest never consults IMDS for its addresses, so it is never corrected. **Confirmed doc-gap:** no canonical AWS page documents what happens inside the running guest OS when a secondary IP is unassigned/reassigned — so an operator who followed this page has no warning that their static binding is now a lie. This is a Lens-U enforcement gap (the "retains the same IP address information" guarantee is only true until the control plane moves it) and a Lens-AA revocation-completeness gap (the control-plane grant moved but the guest-side binding was never severed).

**Amplifier (why Windows specifically).** The same reassignment on an Amazon Linux guest self-heals: `ec2-net-utils` *"refreshes secondary IPv4 addresses during DHCP lease renewal"* (`instance-secondary-ip-addresses.md:113`). This Windows page is the **only** OS-config page in the corpus that directs a conversion to static, so it uniquely makes the sibling's takeover **longer-lived and silent** on the victim side.

**High-level Test Scenarios (falsifiable claims).**
- **Claim:** After `AssignPrivateIpAddresses(eni-A, 10.200.0.129, AllowReassignment=true)` moves `.129` from Windows victim V to attacker ENI A, V's guest still advertises `.129` (ARP/traffic) because its static config persists. → **Oracle:** on V run `ipconfig /all` (still shows `.129` as a static IPv4) while `DescribeNetworkInterfaces`/`DescribeInstances` and A's IMDS `local-ipv4s` show `.129` now belongs to A → an in-subnet duplicate-IP / split-brain confirmed by two record-keepers disagreeing. → **Preconditions:** attacker holds `ec2:AssignPrivateIpAddresses` on **A's (target) ENI only** — the API documents **no source-owner consent check** (`API_AssignPrivateIpAddresses` Errors section carries only Common Error Types; `AllowReassignment` is a plain boolean on the request), so V's owner never authorizes the move (same-account cross-team, or cross-account on a RAM-shared subnet — see sibling); V previously followed this page. → **Cost:** two instances in one subnet. → **Severity-if-true:** intra-account cross-team = **Medium–High** (service hijack / source-IP-ACL confusion persists on V); cross-account via shared subnet = **High** (inherits the sibling's cross-tenant takeover severity, now with a silent, durable victim-side stale claim). → **Stop:** once V's `ipconfig` and the control-plane map provably disagree.
- **Claim:** the moved secondary IP drags its Elastic IP with it, so an attacker reassigning `.129` also silently relocates V's public EIP. → **Oracle:** API ref *"any Elastic IP address that is associated with the IP address is also moved"* (`API_AssignPrivateIpAddresses.md`); confirm the EIP now routes to A while V's static guest still binds the private IP. → **Severity-if-true:** High (public-facing traffic redirected; chains to sibling's EIP-ride-along note).
- **Claim:** on *unassign* (not reassign) the IP and its EIP are torn down but V keeps the static binding. → **Oracle:** prereq page *"When a secondary private IPv4 address is unassigned from a network interface, the Elastic IP address (if it exists) is also disassociated"* (`instance-secondary-ip-addresses.md`); V's `ipconfig` still shows `.129` → stale binding + dangling-EIP exposure.

### Area 2 — The static-conversion procedure is an AWS-authored weak default relative to the Linux path (Lens U / doc-completeness; Low–Medium, AWS-owned)

**Background.** The corpus has exactly one page telling customers to abandon DHCP for static addressing: this one. The Linux guidance (same prerequisite page) keeps the guest on DHCP and lets `ec2-net-utils` reconcile automatically.

**Security Concern.** The page presents static conversion as a plain requirement with no mention of the trade-off it introduces: a static guest cannot reflect any later control-plane IP change (reassignment, unassignment, EIP move) and will silently diverge. The two Important callouts (`:29` "must match exactly … could become unreachable"; `:97` RDP drop) warn only about *typos at configuration time*, never about *post-configuration divergence from the control plane*. Because the procedure is AWS-authored and copied verbatim by operators, the omission is AWS's documentation defect, not a customer footgun.

**High-level Test Scenarios.**
- **Claim:** no sentence on this page or its prerequisite warns that a reassignment/unassignment will leave the static Windows guest misconfigured. → **Oracle:** doc read (confirmed by this plan's recon — the only guest-OS behavioral statement anywhere is "static and not managed by DHCP"). → **Severity:** Informational–Low (documentation completeness), but it *enables* Area 1's silent persistence; file as the Lens-U doc-vs-mechanism gap.
- **Claim:** AWS could but does not point Windows operators at an IMDS-polling reconciliation step (equivalent to Linux's lease-renewal refresh). → **Oracle:** `API_AssignPrivateIpAddresses.md` recommends IMDS `local-ipv4s` for the *gaining* side; no equivalent reconciliation guidance exists for a static Windows guest. → **Severity:** Low (hardening-guidance gap).

### Area 3 — Reassignment detection blind spot for the losing owner (Lens O; Low–Informational as an enabler)

**Background.** Area 1's impact depends on how long the split-brain goes unnoticed. The losing instance's owner needs a signal that their secondary IP moved.

**Security Concern.** The guest gets no OS-level push (no DHCP event — it is static). The question is whether the control plane gives the *owner* a push signal (EventBridge event / distinct CloudTrail record) or whether detection is a poll they must initiate (`DescribeNetworkInterfaces`/`DescribeInstances`). If the only authoritative truth is an owner-initiated poll, the stale binding can persist indefinitely undetected.

**High-level Test Scenarios (all confirmed from the IAM reference + event catalog; impact still needs a live canary).**
- **Claim (CONFIRMED doc-fact):** reassigning/unassigning a secondary private IP emits **no EventBridge event** of any kind. → **Oracle:** the complete EC2 native EventBridge event-type list (`automating_with_eventbridge.md`) contains no network-interface / private-IP / assign / unassign / reassign event — only AMI/Fleet/Spot/Instance-State-change/ODCR events; `EC2 Instance State-change Notification` fires only on lifecycle (pending/running/stopping/…), never on IP reassignment. → **Severity:** Low as a standalone gap, but it **removes the only real-time detection channel** → materially raises Area 1 (a reassignment can go unnoticed indefinitely). → **Stop:** event absence is already settled from docs; no live test needed for this claim.
- **Claim (CONFIRMED doc-fact):** `AssignPrivateIpAddresses`/`UnassignPrivateIpAddresses` are Access-level **Write** APIs → logged as CloudTrail **management events by default**, but there is **no purpose-built "your IP was taken" signal**; the record lands in the **ENI-owning account's** trail and names the actor + target ENI. In a **cross-account** reassignment (attacker ENI in the attacker's account on a RAM-shared subnet), the victim's trail may carry no record attributable to the loss. → **Oracle:** `list_ec2` Access-level rows + CloudTrail default-logging of management events; detection requires the owner to build a custom rule on `AWS API Call via CloudTrail` or query the trail. → **Severity:** Low–Medium (cross-account detection gap; enabler for Area 1).
- **Claim (CONFIRMED doc-fact):** `DescribeNetworkInterfaces` (`list_ec2:7218-7222`) and `DescribeInstances` (`:6996-7000`) are **unscopable read oracles** — blank resource type, only `ec2:Region`, Access-level List — so the owner *can* poll the authoritative `PrivateIpAddresses` set to detect divergence, but the detection API itself cannot be tag/ENI-scoped (any grant reads every ENI's assignments in the region). → cross-ref `working-with-ip-addresses` Area 7. → **Severity:** Low (the owner's only reliable detection is a poll they must initiate; the API's unscopability is a separate least-priv note).
- **Supporting fact (Lens-S, confirmed):** the four assign/unassign actions have **no IAM lever to distinguish a stealing reassign from a benign one** — `AllowReassignment` does not exist as a condition key anywhere in `list_ec2`, and neither `ec2:PrivateIpAddress` nor `ec2:Ipv6Address` exists; `ec2:AuthorizedUser` exists on EC2 but is **not** carried by any of the four actions. The only scoping is on the **target** ENI (`ec2:NetworkInterfaceID`/tags/`ec2:Subnet`/`ec2:Vpc`), never the source. (Owned in depth by the `using-instance-addressing` sibling; reproduced here only to anchor the detection-side severity.)

### Area 4 — IIS site binding to the secondary private IP follows the stale guest view (Step 3; Lens U, Low–Medium)

**Background.** Step 3 binds an IIS website to the specific secondary private IP: *"if your instance is running a website on IIS, you can configure IIS to use the secondary private IP address"* and the binding dialog *"for IP address, select the secondary private IP address"* (`:Step3`).

**Security Concern.** The IIS binding is a second guest-local record of the IP, equally disconnected from the control plane. After a reassignment (Area 1), IIS keeps binding to `.129` on V while the subnet now delivers `.129` to attacker A. Depending on L2/host behavior (service-plane, not tested), V's IIS may stop receiving traffic for `.129` (availability) while A can stand up a service on the hijacked IP — any downstream system that trusts `.129` as "the website" is now pointed at A's instance.

**High-level Test Scenarios.**
- **Claim:** an IIS site bound to a reassigned secondary IP retains the stale binding in the guest with no error until manually corrected. → **Oracle:** after reassignment, inspect IIS site bindings on V (still `.129`) vs the control-plane map. → **Severity:** Low–Medium (service hijack / availability of a host-bound app; the cross-tenant severity is inherited from Area 1, not re-counted here).
- **Note:** the binding default is permissive ("By default, each website accepts HTTP requests from all IP addresses") — pinning to a single secondary IP is the operator's intentional narrowing, so the risk is the *staleness* of that pin, not the binding feature itself.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Stale guest static binding persists after control-plane reassignment → split-brain IP claim | Windows guest TCP/IPv4 static config vs ENI mapping | None — page states config is "static and not managed by DHCP" (`:97`); no re-sync documented for Windows |
| Windows static conversion makes a sibling-owned takeover longer-lived than on Linux | Guest OS procedure asymmetry | Linux `ec2-net-utils` DHCP-renew re-sync (`instance-secondary-ip-addresses.md:113`); Windows has no equivalent |
| Owner has no push signal that the secondary IP moved | EventBridge / CloudTrail / guest OS | CloudTrail management event on the API call (owner must own/read the trail); no guest signal — see Area 3 |
| IIS site binding follows the stale OS IP after reassignment | IIS Manager binding (Step 3) | None documented |
| Operator mis-types the static IP → self-inflicted unreachability | Step 1 "must match exactly" | Warning prose only (`:29`); self-DoS, out of scope |

## 7. Out-of-Scope Risk Categories
- **Single-tenant self-DoS:** mis-typing the static IP and losing connectivity ("the instance could become unreachable", `:29`); the few-seconds RDP drop during DHCP→static conversion (`:97`). The *operator inflicts this on their own instance* — out of scope as a bug, retained only as context for the integrity gap.
- **The control-plane takeover primitive itself** (`AssignPrivateIpAddresses`/`AllowReassignment` authz, missing `ec2:PrivateIpAddress` key, cross-account via RAM-shared subnet): **owned by `using-instance-addressing`**, not re-adjudicated here.
- **Host/Nitro side of DHCP, the ENI backplane, link-local services (IMDS .254 / Resolver .253):** AWS service plane — hard stop.
- **ARP/L2 behavior of the shared subnet fabric** as an AWS-operated mechanism — only the *guest's* observable claim to the IP is in scope, not the backplane's L2 implementation.
- **IPv6:** this page is IPv4-only; IPv6 instance addressing is the `working-with-ipv6-addresses` plan (and is safer on the force-move axis — no `AllowReassignment`).

## 8. Null hypotheses / doc gaps (lenses checked, pages named)
Pages checked for triggers: `config-windows-multiple-ip.md` (target, full), `instance-secondary-ip-addresses.md` (prerequisite, full), the Linux OS-config section within it, and `list_ec2` (grep).

- **Lens A (cross-tenant IDOR):** N/A *as a net-new surface on this page* — no resource-by-ID API is introduced here; the IDOR-shaped takeover is the sibling's Area 1. The *disclosure-timing* and *sub-resource* variants have no trigger on a guest-OS procedure page.
- **Lens B/C (PassRole / vending):** N/A — no role ARN, no STS, no credential field on this page (no Fleet SLR; the prerequisite API runs under the caller's own identity).
- **Lens F (injection / translation):** N/A — no parser/translator; the only "input" is operator-typed IP strings consumed by the local Windows TCP/IP stack, not an AWS backend.
- **Lens G (SSRF):** N/A — read target page + prerequisite; **no field the service dereferences** (no `*Url`/`*Uri`/webhook/fetch). The `ipconfig`/console values are displayed, not fetched.
- **Lens Q (upload):** N/A — no upload/blob/image field; the PNG references on the page are AWS doc screenshots, not customer uploads.
- **Lens H (KMS), W (attestation), Y (transport/TLS), FF (JWT), DD (cache), CC (upstream-context), BB (canonicalization), EE (predictable-name):** no trigger — no key, no attestation gate, no endpoint/TLS claim, no token, no cache layer, no multi-parser request path, no name-resolution step on this page.
- **Lens R/S (IAM-artifact / condition-key):** no IAM policy JSON, managed policy, or sample policy is printed on this page. (The reassignment action's condition-key scoping is audited by the sibling.) → N/A on this page, cross-ref sibling.
- **Lens P (proofing/registration):** N/A — no registration/verification/uniqueness gate.
- **Settled from docs (no live test needed):** (a) **no EventBridge event** exists for IP assign/unassign/reassign (confirmed against the full EC2 event catalog, Area 3); (b) the four assign/unassign actions scope only the **target** ENI and have **no `AllowReassignment`/`ec2:PrivateIpAddress`/`ec2:Ipv6Address` condition key** and no source-owner consent check; (c) the moved secondary IP **drags its associated EIP** (`API_AssignPrivateIpAddresses`), and *unassign* **disassociates** the EIP (`instance-secondary-ip-addresses.md`); (d) there is **no canonical AWS page** documenting running-guest behavior on reassignment, and the Windows static conversion is the only OS-config page severing DHCP reflection.
- **Doc gaps that still need a two-instance (or two-account) canary** — all gate impact, none answerable by `DryRun` (caller-IAM-only, pre-resolution): (1) exact guest-OS behavior after reassignment — does Windows surface a duplicate-IP / gratuitous-ARP conflict, or silently keep claiming `.129` (Area 1 core); (2) what the shared-subnet fabric does with a split-brain claim (which ENI receives `.129` packets) — note the L2/backplane *mechanism* is AWS service-plane (hard stop); observe only the two guests' and the control-plane's views; (3) whether the EIP relocation is observable to the losing owner; (4) cross-account reach confirmation via a RAM-shared subnet (sibling-owned; re-confirm the Windows-amplified persistence end-to-end).
