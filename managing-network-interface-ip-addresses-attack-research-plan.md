# Manage the IP addresses for your network interface — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/managing-network-interface-ip-addresses.html` (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/managing-network-interface-ip-addresses.md`); IAM facts from `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (EC2 Service Authorization Reference, 10190 lines); CLI ref `associate-address.html`; companion page `modify-network-interface-attributes.md`. Status: documentation-derived hypotheses only; nothing tested against a live account. Online == offline byte-identical (verified 2026-10-15, no content drift).

> **This is a CONVERGENCE / COMPLEMENT plan, not a new mechanism plan.** The target page is the ENI-centric unified **"Manage IP addresses"** console/CLI hub. It introduces *no new EC2 API*: it wires together six actions already owned in depth by sibling plans under one console action and one `--network-interface-id` target. This plan therefore (a) owns the **convergence framing** that the siblings — each scoped to one IP family — cannot see, (b) owns three net-new *management-page* surfaces (primary-IPv6 irreversibility as a post-create operation, the "auto-assign public IP only affects the primary ENI" footgun, the AllowReassociation default), and (c) **cross-references, does not restate,** the per-action takeover/collateral primitives. Do NOT re-derive the sibling-owned leads; follow the pointers.

**Sibling plans (authoritative for the per-action depth):**
- `using-instance-addressing-attack-research-plan.md` — `AssignPrivateIpAddresses … AllowReassignment=true` cross-ENI / cross-account secondary-private-IPv4 takeover; link-local model; ephemeral public-IP pool reuse.
- `instance-secondary-ip-addresses-attack-research-plan.md` — `UnassignPrivateIpAddresses` collateral EIP-disassociation (unscopable twin of `DisassociateAddress`).
- `working-with-ip-addresses-attack-research-plan.md` — launch-time IPv4; `ec2:AssociatePublicIpAddress` inert-Deny; no private-IP-value key; shared-VPC forced public exposure.
- `working-with-ipv6-addresses-attack-research-plan.md` — IPv6 family (confirmed safer: no `AllowReassignment` force-move); IPv6-public-by-default unscopable.
- `elastic-ip-addresses-eip-attack-research-plan.md` / `working-with-eips-…` / `transfer-EIPs-intro-ec2-…` / `using-instance-addressing-eips-releasing-…` / `using-elastic-addressing-reverse-dns-…` — EIP associate/disassociate/transfer/release/squatting/reverse-DNS.
- `using-eni-…` / `create-network-interface-…` / `network-interface-attachments-…` — ENI resource lifecycle/attribute/attach.
- `config-windows-multiple-ip-attack-research-plan.md` — guest-OS static-binding split-brain after reassignment.
- `ec2-networking-attack-research-plan.md` — the hub over all of the above.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The highest-value finding here is the **convergence least-privilege gap (Area 1)** — it is the lens the single-family siblings structurally miss. Areas 2–4 are the page's net-new management-operation footguns. Everything in §5 marked **[POINTER]** defers to a named sibling; confirm there, do not re-run here.
- Settle every IAM-scoping question first with `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (no resources touched). Escalate to a live scoped call only with synthetic canary ENIs/EIPs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (a *requester-managed* or `Managed=true` ENI, a host/Nitro link-local service, an AWS-owned `ec2:ManagedResourceOperator`), stop, preserve evidence, flag for AWS-Security disclosure. Never probe the host side of a link-local service.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. Hold an IAM role scoped to "manage IP addresses on network interfaces I own" and use the *single* grant to perform an operation on another team's / another account's ENI that the page presents as benign IP housekeeping — specifically: force-move a secondary private IPv4 (+ its EIP), detach an EIP, or lock a primary IPv6 — proving the convergence grant is coarser than the operations it authorizes.
2. From a RAM-shared-subnet participant vantage, manipulate the IP configuration of an ENI in the owner's subnet (or pre-empt/strand addresses) that the owner cannot see or prevent.
3. Permanently and irreversibly bind an ENI's **primary IPv6** to a wrong/attacker-chosen GUA such that the owner cannot remediate without detaching or terminating the interface.
4. Demonstrate that no IAM policy can express the guardrails an operator would reasonably want on this page (which IP value, forbid force-reassociation, forbid force-reassignment, forbid primary-IPv6 lock, cap public exposure) — i.e. the "Manage IP addresses" capability is all-or-nothing per ENI identity.
5. Mislead an exposure audit via the "auto-assign public IP only affects the primary ENI" silent no-op.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 control-plane (SigV4 IAM) + console "Network Interfaces → Actions → Manage IP addresses / Associate address / Disassociate address". Six underlying actions, all keyed on a single `--network-interface-id`:

| Console control | CLI | API action | PowerShell |
|---|---|---|---|
| IPv4 "Assign new IP address" | `assign-private-ip-addresses` | `AssignPrivateIpAddresses` | `Register-EC2PrivateIpAddress` |
| IPv4 remove | `unassign-private-ip-addresses` | `UnassignPrivateIpAddresses` | `Unregister-EC2PrivateIpAddress` |
| IPv6 "Assign new IP address" | `assign-ipv6-addresses` | `AssignIpv6Addresses` | `Register-EC2Ipv6AddressList` |
| IPv6 remove | `unassign-ipv6-addresses` | `UnassignIpv6Addresses` | `Unregister-EC2Ipv6AddressList` |
| "Assign primary IPv6 IP → Enable" | `assign-ipv6-addresses` (`EnablePrimaryIpv6`) | `AssignIpv6Addresses` | `Register-EC2Ipv6AddressList` |
| "Auto-assign public IP" | *(ENI auto-assign-public-IPv4 attribute; no standalone IAM action)* | — | — |
| "Associate address" (+ "Allow … reassociated") | `associate-address` (`--allow-reassociation`) | `AssociateAddress` | `Register-EC2Address` |
| "Disassociate address" | `disassociate-address` | `DisassociateAddress` | `Unregister-EC2Address` |

**Resource & identifier shape.** Target is always a `network-interface` (`eni-…`); EIP named by `--allocation-id` (`eipalloc-…`) or `--association-id` (`eipassoc-…`); IP values are literal IPv4/IPv6 strings the caller supplies. ENI IDs are 17-hex (not checksum-fabricable blind, but enumerable within an account and knowable in a shared VPC).

**Accounts/VPCs.** Direct control-plane actions run **under the caller's own identity** (no service-linked role, no PassRole on this surface). The two trust lines that matter: (a) **intra-account cross-team** — team A's role scoped to its ENIs by tag/ARN vs team B's ENIs; (b) **cross-account via RAM-shared subnet** — a participant operating on/near ENIs in the owner's subnet.

**Untrusted-data transforms / injection seams:** none on this page — all inputs are identifiers and IP-value strings, not server-dereferenced URLs, uploads, roles, or parsed blobs. (SSRF/upload/PassRole/injection lenses are null here; see §8 with pages named.)

```
                 ┌─────────────────────────── "Manage IP addresses" (one console action) ───────────────────────────┐
 caller IAM ───▶ │  AssignPrivateIp | UnassignPrivateIp | AssignIpv6 | UnassignIpv6 | (EnablePrimaryIpv6) | Associate │
 (own identity)  │  Address | DisassociateAddress   — ALL target a single  eni-xxxx  (--network-interface-id)        │
                 └──────────────────────────────────────────────┬─────────────────────────────────────────────────┘
                                                                 ▼
                                            network-interface*  (eni-xxxx)   ◀── owned by: same-account other team,
                                            scoped in IAM ONLY by:                or cross-account subnet participant
                                            {ENI-id, Subnet, Vpc, AZ, Region, tag, ManagedResourceOperator}
                                            ── NO per-operation, per-IP-value, or safety condition key ──
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Role scoped "manage IPs on my ENIs" | Another team's ENI (same account) | Any of the 6 actions, authz keyed only on `network-interface` identity | Performing a *destructive* IP op (steal secondary IP+EIP, detach EIP, lock primary IPv6) on an ENI the role's author did not intend to include |
| Shared-VPC **participant** | ENI in **owner's** subnet | Participant-reachable ENI ops; owner "cannot modify" but can the participant? | Any IP mutation on an owner-subnet ENI the owner cannot see/prevent (chains to create-network-interface + working-with-ip-addresses siblings) |
| Caller holding `AssociateAddress` | An EIP currently associated with another running instance/ENI | Default `AllowReassociation=true` force-move | EIP yanked off a live instance; victim loses reachability |
| Caller holding `AssignIpv6Addresses` | Victim ENI with no primary IPv6 yet | `EnablePrimaryIpv6` sets first GUA, immutable | Primary IPv6 permanently bound to attacker/wrong GUA; owner can't change without detach/terminate |
| Exposure auditor | Secondary ENI "Auto-assign public IP" | Console accepts toggle but it "only affects the primary network interface" | Auditor's belief about public reachability diverges from reality (silent no-op) |
| Any caller | AWS service plane | A *requester-managed* / `Managed=true` ENI appears as a target | **HARD STOP** — do not operate; preserve evidence; disclose |

---

## 4. API / Interface Inventory

| Name | Mutating | Ext-facing | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|
| `AssignPrivateIpAddresses` | Yes | Yes | Yes (SigV4) | any principal with the action on the target ENI | `network-interface*` only; 8-key generic set; **`AllowReassignment` param is NOT an IAM key** → force-move unforbiddable. [POINTER→using-instance-addressing] |
| `UnassignPrivateIpAddresses` | Yes | Yes | Yes | same | Collateral **EIP auto-disassociation** (unscopable twin of DisassociateAddress). [POINTER→instance-secondary-ip-addresses] |
| `AssignIpv6Addresses` | Yes | Yes | Yes | same | Carries the **`EnablePrimaryIpv6`** request param (console "Assign primary IPv6 IP"); no primary-IPv6 condition key. **Area 2.** |
| `UnassignIpv6Addresses` | Yes | Yes | Yes | same | IPv6 removal; no force-move analogue (IPv6 safer). [POINTER→working-with-ipv6-addresses] |
| `AssociateAddress` | Yes | Yes | Yes | principal with action on EIP + target ENI/instance | **Default reassociation = ON**; `--allow-reassociation` not an IAM key. **Area 4.** [POINTER→elastic-ip-addresses-eip for forced-reassoc steal] |
| `DisassociateAddress` | Yes | Yes | Yes | principal with action on the EIP | `elastic-ip` row scopable by `ec2:AllocationId`/`ec2:PublicIpAddress` — the *scopable* twin whose unscopable sibling is `UnassignPrivateIpAddresses`. |
| "Auto-assign public IPv4" ENI toggle | Yes | Yes (console) | — | — | **No standalone IAM action / no condition key**; `ec2:AssociatePublicIpAddress` exists only on `RunInstances`. **Area 3.** |

Console-hidden / under-surfaced knob: the `EnablePrimaryIpv6` parameter and the ENI auto-assign-public-IPv4 toggle are presented only in this console flow; neither has a dedicated IAM lever (both confirmed below).

---

## 5. Recommended Areas of Focus

### Area 1 — Convergence least-privilege gap: one ENI-identity grant authorizes six destructive IP operations  *(Lens S / U / A — PRIMARY, the page-specific finding)*
**Background.** The page teaches operators to treat "managing IP addresses" as a single capability on a single ENI target. IAM honours that framing *too literally*: all six actions are authorized **only** by the target ENI's identity/placement/tags — the required `network-interface*` row carries exactly `{aws:ResourceTag/${TagKey}, ec2:AvailabilityZone, ec2:ManagedResourceOperator, ec2:NetworkInterfaceID, ec2:Region, ec2:ResourceTag/${TagKey}, ec2:Subnet, ec2:Vpc}` and nothing operation-specific (confirmed: `AssignIpv6Addresses` 4694–4698, `AssignPrivateIpAddresses` 4700–4704, `UnassignIpv6Addresses` 9690–9694, `UnassignPrivateIpAddresses` 9696–9700; `AssociateAddress` 4712–4717; `DisassociateAddress` 7885–7889).

**Security Concern.** A role an admin writes as "let the net-ops team manage IP addresses on ENIs tagged `team=netops`" **cannot distinguish** benign assignment from the destructive primitives the siblings own, because the discriminating conditions **do not exist as IAM keys**: whole-file grep = **0 hits** for `AllowReassignment` (`allowreassoc`), `ec2:PrivateIpAddress`, `ec2:Ipv6Address`, `ec2:PrimaryIpv6`/`EnablePrimaryIpv6`. So the single grant simultaneously confers: force-move of a secondary private IPv4 **and its EIP** (`AssignPrivateIpAddresses`+`AllowReassignment`), collateral EIP detachment (`UnassignPrivateIpAddresses`), a permanent primary-IPv6 lock (`AssignIpv6Addresses`+`EnablePrimaryIpv6`), and default EIP force-reassociation (`AssociateAddress`). The only expressible fence is *which ENI*, not *which operation* or *which IP value*.

**High-level Test Scenarios.**
- Claim: a policy allowing the 6 actions on `network-interface` resources tagged `team=X` grants no way to forbid `AllowReassignment` / primary-IPv6-lock / specific IP values. → **Oracle:** `iam:SimulateCustomPolicy` with such a policy returns `allowed` for an `AssignPrivateIpAddresses` call carrying `AllowReassignment=true` and for an `AssignIpv6Addresses` call setting `EnablePrimaryIpv6` — with no condition able to flip it to `implicitDenied`. Build the attempted-Deny policy (`Condition` on each nonexistent key) and show it is **silently inert** (the key is undefined → the condition never matches → no narrowing).
- Claim: if an ENI is reachable by tag/ARN to the role, *all six* ops succeed regardless of which team/account owns the addresses on it. → **Oracle:** scoped-role live call against a canary ENI owned by a second principal but matching the tag/ARN scope.
- Adjacent (sub-resource isolation): tearing down one address on an ENI collaterally affects a sibling resource (the EIP riding a secondary private IP) — see Area 4 / instance-secondary-ip-addresses.

**Doc evidence:** target page unifies all six under one "Manage IP addresses" action + single `--network-interface-id`; `list_ec2.md` rows above. **Severity-if-true:** intra-account cross-team Medium–High (least-privilege footgun customers *cannot* close because the keys don't exist — an AWS-owned expressiveness gap, Lens U/S, worth filing); cross-account via shared subnet High. **Stop condition:** once Simulate shows the Deny is inert and one scoped live op crosses to a non-owned ENI, the gap is proven — do not enumerate further ENIs.

### Area 2 — Primary IPv6 is a one-way, irreversible lock settable as a post-create management operation  *(Lens U / AA)*
**Background.** The console "Assign primary IPv6 IP → Enable" (backed by `AssignIpv6Addresses` with `EnablePrimaryIpv6`) sets the primary IPv6 to "the first GUA associated with the network interface." Verbatim: *"After you assign a primary IPv6 address, you can't change it. This address is the primary IPv6 address until the instance is terminated or the network interface is detached."*

**Security Concern.** This is a **one-way state transition with no disable path.** The companion page `modify-network-interface-attributes.md` enumerates every attribute `ModifyNetworkInterfaceAttribute` can change (Description, Security groups, Delete-on-termination, Source/dest check, Idle connection-tracking timeout) — **primary IPv6 is not among them** (confirmed online==offline). And there is **no condition key** gating it (`ec2:PrimaryIpv6`/`ec2:EnablePrimaryIpv6` = 0 hits), so a principal holding `AssignIpv6Addresses` on a reachable ENI (Area 1 shows how coarse that grant is) can **permanently bind** the primary IPv6 to a GUA of their timing/choosing. The owner's only remediation is **detach or terminate** the interface — itself an availability-impacting action (a "fix as disruptive as the problem" footgun), and possibly blocked (primary ENI cannot be detached; DeleteOnTermination/attachment constraints). This complements `create-network-interface` Area 5 (which owns the *create-time* irreversibility); this plan owns it as a **post-create management operation** reachable from the "Manage IP addresses" flow.

**High-level Test Scenarios.**
- Claim: a caller with only `AssignIpv6Addresses` on a victim ENI can set its primary IPv6 before the owner does, locking a chosen GUA. → **Oracle:** canary ENI with no primary IPv6; scoped-role `assign-ipv6-addresses … EnablePrimaryIpv6` succeeds; subsequent attempts (by owner) to change it fail; `ModifyNetworkInterfaceAttribute` offers no disable.
- Claim: the lock cannot be scoped/forbidden by policy. → **Oracle:** `SimulateCustomPolicy` with a Deny `Condition` on `ec2:PrimaryIpv6` is inert (key undefined).
- Downstream: if IPv6 allow-lists / SG references / DNS AAAA depend on the primary GUA, a wrong lock is un-remediable without interface churn.

**Doc evidence:** target page primary-IPv6 paragraph; `modify-network-interface-attributes.md` attribute list; `list_ec2.md` 0-hit grep. **Severity-if-true:** Medium (integrity/availability griefing + unclosable guardrail gap; higher where primary GUA is security-load-bearing). **Stop condition:** one successful lock on a canary + confirmed absence of a disable API.

### Area 3 — "Auto-assign public IP … only affects the primary network interface" — silent no-op / exposure-audit confusion  *(Lens U / O)*
**Background.** Verbatim: *"To assign or unassign a public IPv4 address to a network interface, choose **Auto-assign public IP**. You can enable or disable this for any network interface, but it only affects the primary network interface."*

**Security Concern.** The control is offered **"for any network interface"** but is **effective only on the primary ENI**. Two directions of confusion: (a) a user *enables* it on a secondary ENI expecting public reachability — the console accepts it with no error/warning and it is **silently ignored** (false sense of *connectivity*, benign); (b) an **exposure auditor** reading "Auto-assign public IP: disabled" on a secondary ENI may wrongly conclude no auto public-IPv4 path exists, when the **primary** ENI's setting is what actually governs reachability (false sense of *isolation* — security-relevant). Critically, this ENI-level auto-assign toggle has **no standalone IAM action and no condition key**: `ec2:AssociatePublicIpAddress` (Bool, def L10050) appears only on `RunInstances`' `network-interface*` row (L9595) and the glossary/resource-type tables (L9982) — **never** on `ModifyNetworkInterfaceAttribute` or the Assign/Unassign actions (confirmed, exactly 3 hits). So there is no policy lever to govern this per-ENI public-exposure toggle after launch.

**High-level Test Scenarios.**
- Claim: enabling auto-assign-public-IP on a secondary ENI is accepted but assigns no public IPv4. → **Oracle:** console/API toggle on a secondary ENI; `DescribeNetworkInterfaces` shows no `Association.PublicIp`.
- Claim: no IAM policy can allow/deny this toggle specifically. → **Oracle:** no action/condition key maps to it (grep confirms); `SimulateCustomPolicy` cannot target it.
- Chain: the ephemeral public IPv4 this governs comes from the shared pool → dangling-DNS / reuse angle. **[POINTER→using-instance-addressing Area 3]** (ephemeral public-IP pool reuse / dangling-DNS); do not re-derive.

**Doc evidence:** target page auto-assign sentence; `list_ec2.md` `ec2:AssociatePublicIpAddress` = 3 hits all `RunInstances`/glossary. **Severity-if-true:** Low–Informational (audit-confusion / unclosable toggle; AWS-owned doc+expressiveness gap). **Stop condition:** confirm the no-op + absence of a key.

### Area 4 — AssociateAddress default-reassociation ("Allow the Elastic IP address to be reassociated")  *(Lens AA / S)*
**Background.** The console checkbox "Allow the Elastic IP address to be reassociated if the network interface is currently associated with another instance or network interface" maps to `AssociateAddress --allow-reassociation`. The CLI ref states reassociation is the **default**: *"If the Elastic IP address is already associated with a different instance, it is disassociated from that instance and associated with the specified instance"* and *"Reassociation is automatic, but you can specify false to ensure the operation fails if the Elastic IP address is already associated with another resource."*

**Security Concern.** `AllowReassociation` is a **request parameter, not an IAM condition key** (grep `allowreassoc` = 0 hits). So an admin **cannot** author a policy that permits `AssociateAddress` but forbids the force-move of an already-associated EIP — the fail-safe (`AllowReassociation=false`) is purely caller-opt-in. Within the account this is primarily a **same-account automation hazard** (the caller must already hold the allocation): a script or role re-associating an EIP will silently yank it off a different live instance/ENI, causing an availability break on the victim. The forced-reassociation *steal* primitive and the EIP-side scoping (`ec2:AllocationId`/`ec2:PublicIpAddress`) are owned by the EIP siblings; this plan owns the fact that the **ENI "Manage IP addresses" flow surfaces the default-ON behavior with no policy lever to forbid it.**

**High-level Test Scenarios.**
- Claim: a role with `AssociateAddress` on EIP `eipalloc-X` and target ENI `eni-Y` can move `eipalloc-X` off a live instance with no `AllowReassociation` guardrail enforceable by policy. → **Oracle:** `SimulateCustomPolicy` shows no condition can gate the reassociation; live canary moves an EIP that was associated with instance-A onto ENI-B, A loses the EIP.
- Claim: the EIP side *is* scopable (`ec2:AllocationId`/`ec2:PublicIpAddress` on `AssociateAddress` 4714 / `DisassociateAddress` 7887) but the force-move flag is not — asymmetry. → **Oracle:** compare the two policies under Simulate.

**Doc evidence:** target page checkbox; `associate-address.html` default-reassociation; `list_ec2.md` 4712–4717 / 7885–7889. **Severity-if-true:** Medium (same-account availability/automation footgun; unclosable flag). **[POINTER→elastic-ip-addresses-eip S1]** for the cross-identity forced-reassociation steal and `AllowReassociation`-is-not-a-key depth; **[POINTER→working-with-eips / transfer-EIPs / releasing / reverse-dns]** for allocate/squatting/transfer/PTR. **Stop condition:** Simulate + one canary move.

### §5 POINTERS (sibling-owned; confirm there, do NOT re-run here)
- **[POINTER] Secondary private-IPv4 cross-ENI / cross-account takeover via `AssignPrivateIpAddresses … AllowReassignment=true` (+ EIP rides along):** → `using-instance-addressing` Areas 1/2 (no SourceNetworkInterfaceId / no source-owner consent; gaining caller sets consent; EIP "also moved").
- **[POINTER] `UnassignPrivateIpAddresses` collateral EIP auto-disassociation (unscopable twin of `DisassociateAddress`):** → `instance-secondary-ip-addresses` Area 1.
- **[POINTER] No private-IP / IPv6 *value* condition key; symmetric across launch + assign:** → `working-with-ip-addresses` Area 2 / `using-instance-addressing` Area 2.
- **[POINTER] IPv6 is safer (no `AllowReassignment` force-move; must unassign first):** → `working-with-ipv6-addresses`. Do not over-claim the IPv4 takeover onto IPv6.
- **[POINTER] Shared-VPC participant creating/holding ENIs with chosen IPs in the owner's subnet; cross-account IP collision/strand:** → `create-network-interface` Area 2 / `working-with-ip-addresses` Area 3.
- **[POINTER] Unscopable Describe read-oracles (`DescribeNetworkInterfaces`/`DescribeInstances` blank-resource-type + only `ec2:Region`):** → `using-eni` / `working-with-ip-addresses` Area 7.
- **[POINTER] Guest-OS static-binding split-brain after a reassignment (Windows):** → `config-windows-multiple-ip` Area 1.
- **[POINTER] EIP transfer / release-squatting / reverse-DNS PTR griefing:** → `transfer-EIPs` / `using-instance-addressing-eips-releasing` / `using-elastic-addressing-reverse-dns`.
- **[POINTER] Link-local model (SG/NACL do not filter IMDS/.253/.123):** → `using-instance-addressing` Area 4. HARD STOP on the host side.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| One "manage IPs" grant authorizes a destructive op on a non-owned ENI | 6 actions on `network-interface*` | Resource-level IAM on ENI identity/tags — but no per-operation / per-IP-value / safety key exists (Area 1) |
| Permanent primary-IPv6 lock on a victim ENI | `AssignIpv6Addresses` `EnablePrimaryIpv6` | "can't change it until terminate/detach"; no disable in `ModifyNetworkInterfaceAttribute`; no condition key (Area 2) |
| Public-exposure audit misled by secondary-ENI auto-assign toggle | ENI auto-assign-public-IPv4 attribute | Doc says "only affects the primary network interface"; no IAM lever (Area 3) |
| Unforbiddable EIP force-reassociation | `AssociateAddress` default `AllowReassociation=true` | `AllowReassociation` is a request param, not an IAM key; only `--no-allow-reassociation` opt-in (Area 4) |
| Secondary private-IPv4 + EIP force-move / collateral detach | `AssignPrivateIpAddresses`/`UnassignPrivateIpAddresses` | **Deferred** → using-instance-addressing / instance-secondary-ip-addresses |
| Shared-VPC participant IP manipulation / strand | ENI in owner subnet | **Deferred** → create-network-interface / working-with-ip-addresses |

---

## 7. Out-of-Scope Risk Categories (state as confidently as in-scope)
- **Single-tenant self-DoS** (your own script yanking your own EIP) — footgun, not a cross-trust finding, except where it crosses a team/account boundary.
- **Customer-authored IAM policies** that under-scope ENI access — a customer footgun; the *reportable* angle is the **absence of condition keys** (AWS-owned expressiveness gap, Area 1/2/3/4), not the customer's policy.
- **IMDS / link-local host side**, Nitro, any requester-managed / `Managed=true` ENI — AWS service plane, **HARD STOP** / disclose.
- **Shared VPC / BYO-VPC infra**, DNS rebinding against private-only endpoints.
- Per-action takeover/collateral/transfer depth already **owned by named siblings** — out of scope *for this plan* (follow the pointers); not out of scope for the hunt.

---

## 8. Null hypotheses / doc gaps (pages named)
- **Lens B/C (PassRole / credential vending) — N/A.** Read: full target page + `modify-network-interface-attributes.md`. All six actions run under the caller's own identity; no role ARN, no SLR, no STS, no `iam:PassRole` field anywhere on this surface.
- **Lens G (SSRF) — N/A.** Read: target page + associate-address CLI ref. No field the service dereferences/fetches/renders; inputs are ENI/EIP identifiers and literal IP strings.
- **Lens Q (upload) / F (injection) / K (prompt) / H (KMS) / W (attestation) / Y (transport) / J (OAuth) / FF (JWT) / N (namespace migration) / BB / CC / DD / EE / M (session) / T (secret storage) — N/A.** Read: target page. No upload/blob, no translation layer, no LLM, no customer KMS field, no attestation, no `http://`/TLS claim, no 3P link, no token, no dual namespace, no multi-parser request path, no asserted-upstream identity header, no cache layer, no predictable-name resolution, no session id, no generated-secret persistence on this page.
- **Lens R (AWS-authored IAM artifact) — N/A on this page.** No managed/sample policy or CFN/runbook JSON is printed here. (The *expressiveness* gaps in Areas 1–4 are Lens U/S, filed as AWS-owned, not an artifact audit.)
- **Lens A cross-account IDOR by blind ID fabrication — partial-null.** `eni-…`/`eipalloc-…`/`eipassoc-…` are not blind-fabricable across accounts; the realistic cross-account path is the **RAM-shared-subnet** participant vantage (deferred to siblings) and **intra-account cross-team** tag/ARN scoping (Area 1).
- **Doc gaps to confirm live first:** (i) does enabling auto-assign-public-IP on a secondary ENI error or silently no-op (Area 3)? (ii) exact `EnablePrimaryIpv6` behavior when a GUA already exists vs none (Area 2)? (iii) does `AssociateAddress` default-reassociation emit a distinct CloudTrail disassociate event on the victim side, or hide inside the associate call (Area 4 + Lens O)? — all cheap DryRun/canary tests; DryRun is caller-IAM-only, so the no-op/behavioral questions need a canary ENI/EIP.

---
*Convergence complement. Owns: the one-grant-six-destructive-ops least-privilege gap (Area 1), primary-IPv6 post-create irreversibility (Area 2), auto-assign-public-IP silent no-op (Area 3), AllowReassociation default (Area 4). Defers all per-action takeover/collateral/transfer depth to the named siblings. All IAM facts grepped from `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`; online==offline byte-identical 2026-10-15.*
