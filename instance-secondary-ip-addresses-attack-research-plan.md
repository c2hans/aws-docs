# instance-secondary-ip-addresses — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-secondary-ip-addresses.html` (`.md` twin; offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/instance-secondary-ip-addresses.md`, confirmed **byte-identical offline==online 2026-10-15**). IAM facts from `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (10190 lines, read by targeted offline grep). Status: documentation-derived hypotheses only; nothing tested against a live account.

**Scope / relationship to siblings (READ FIRST — this plan deliberately does NOT duplicate):** This is a **page-level deep-dive child of the `ec2-networking` hub** (`ec2-networking-attack-research-plan.md`) and a **narrow sibling of two existing plans** that already own most of this page's mechanisms:

- **`using-instance-addressing-attack-research-plan.md`** OWNS: the `AssignPrivateIpAddresses … AllowReassignment=true` cross-ENI / (RAM-shared-subnet) cross-account **secondary private-IPv4 takeover** (its Area 1); the fact that the 4 assign/unassign actions have **no `ec2:PrivateIpAddress`/`ec2:Ipv6Address`/`AllowReassignment` condition key** and no `ec2:AuthorizedUser` (its Area 2); the EIP **rides-along / is moved** on *reassign* ("any Elastic IP associated with the IP is also moved"); ephemeral public-IPv4 pool reuse / dangling-DNS; link-local SG/NACL-bypass; SG-per-ENI-not-per-IP; IPv6-is-safer ("must unassign first").
- **`working-with-ip-addresses-attack-research-plan.md`** OWNS: launch-time IPv4 assignment generally — `ec2:AssociatePublicIpAddress` inert-Deny; the **private-IPv4 VALUE is not expressible** (`ec2:PrivateIpAddress` does not exist); shared-VPC participant forcing public exposure; `DescribeInstances` unscopable read oracle.
- This plan CROSS-REFERENCES both and OWNS only the two surfaces this specific page uniquely introduces into the corpus (see §5): **(A1)** the `UnassignPrivateIpAddresses` → **EIP auto-disassociation collateral twin-path** (a revocation-side effect, scopable on the obvious `DisassociateAddress` action but **unscopable** on this collateral path), and **(A3)** the **doc-integrity gap** that this how-to omits `--allow-reassignment` entirely, hiding the sibling-owned destructive force-move primitive from a reader. Also develops the **launch-time *secondary* private-IP params** (`run-instances --secondary-private-ip-addresses` / `--secondary-private-ip-address-count`) as a concrete instance of the working-with-ip-addresses value-unexpressibility gap (§5 A2).

See [[reference-aws-iam-service-auth-ref-url]] and [[project-aws-research-plans]].

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The safe first oracle for every IAM-expressibility lead here is **`iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** — it settles "is this condition key inert?" with **zero resources created**. Escalate to a live scoped call only with synthetic canary ENIs/EIPs.
- **`DryRunOperation` is caller-IAM-only, evaluated before resource resolution** — it is NOT an ownership oracle for the cross-ENI / cross-account questions (false-positive trap; see Lens A variant coverage).
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (host/Nitro side of any link-local service, a managed/requester ENI's owning service), stop, preserve evidence, flag for AWS-Security disclosure. The host side of IMDS/Resolver/Time/KMS link-local endpoints is **never** a test target.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Collateral EIP takedown that bypasses EIP-scoped IAM:** disassociate a victim's Elastic IP via `UnassignPrivateIpAddresses` on a reachable ENI, under a principal that is **denied/scoped on `DisassociateAddress` by `ec2:AllocationId`/`ec2:PublicIpAddress`** — proving the collateral path routes around the control that governs the obvious path.
2. **Launch-time secondary-IP value forcing:** show that no identity policy can pin or forbid *which* secondary private IPv4 value a `RunInstances` call requests (collision / impersonation of a known internal-service IP at birth).
3. **Doc-integrity:** show the how-to a customer follows for assign/unassign silently omits the `AllowReassignment` force-move knob, so an operator building a "least-privilege secondary-IP role" from this page cannot even see the primitive the sibling plan proves is destructive.
4. (Deferred, see §5 pointers) secondary private-IP cross-ENI/cross-account **takeover** itself → `using-instance-addressing` Area 1.

---

## 2. Components, Assets, and Design

**Customer-facing interface:** EC2 control-plane API (SigV4), console "Manage IP addresses", AWS CLI, Tools for PowerShell. No service fleet / translation layer — the "data plane" is the VPC IP/ENI fabric itself.

**Resources & identifiers:**
- **network-interface** `arn:…:ec2:…:network-interface/${NetworkInterfaceId}` (`eni-…`) — the ONLY resource type the assign/unassign actions bind to.
- **elastic-ip** `arn:…:ec2:…:elastic-ip/${AllocationId}` (`eipalloc-…`, scopable by `ec2:AllocationId`/`ec2:PublicIpAddress`) — the collateral asset silently disassociated on unassign.
- **secondary private IPv4 address** — a value on an ENI, **not** an independently-ARN'd/condition-keyed resource (no `ec2:PrivateIpAddress` key exists anywhere in `list_ec2`).

**Actions on this page:**
| Role | Action | Path |
|---|---|---|
| Assign at launch | `RunInstances` `--secondary-private-ip-addresses {val}` / `--secondary-private-ip-address-count N` | caller identity |
| Assign after launch | `AssignPrivateIpAddresses` `--private-ip-addresses` / `--secondary-private-ip-address-count` (`Register-EC2PrivateIpAddress`) | caller identity |
| Unassign | `UnassignPrivateIpAddresses` `--private-ip-addresses` (`Unregister-EC2PrivateIpAddress`) | caller identity |
| OS config (client-side) | `ec2-net-utils` / `systemd-networkd` / routing rules | in-guest, out of scope |

**ASCII (collateral-coupling view — the net-new seam):**
```
caller --AssignPrivateIpAddresses(targetENI, AllowReassignment)--> [secondary priv IP moves cross-ENI]  (sibling-owned)
caller --UnassignPrivateIpAddresses(targetENI, privIP)----------> [secondary priv IP removed]
                                                      \__ SIDE EFFECT: associated EIP (eipalloc-…) DISASSOCIATED
                                                          (no ec2:AllocationId / ec2:PublicIpAddress binding here)
caller --DisassociateAddress(eipalloc-…)------------------------> [EIP disassociated]  (scopable by AllocationId)
         ^^^ the "obvious" path a Deny/scope is written against — the Unassign side-effect bypasses it
```

**Identity:** SigV4 IAM only; no STS/credential-vending/token field on this surface.

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `RunInstances` (`--secondary-private-ip-addresses` / `-count`) | API/CLI | Existing | **Yes** | Yes | holders of `ec2:RunInstances` + resource rows | launch-time secondary IP; **no IP-value condition key on any resource row** (§5 A2) |
| `AssignPrivateIpAddresses` | API/CLI/PS | Existing | **Yes** | Yes | `ec2:AssignPrivateIpAddresses` on `network-interface*` | accepts `AllowReassignment` (**page omits it**, §5 A3); force-move takeover → sibling |
| `UnassignPrivateIpAddresses` | API/CLI/PS | Existing | **Yes** | Yes | `ec2:UnassignPrivateIpAddresses` on `network-interface*` | **auto-disassociates associated EIP as a side effect** (§5 A1 HEADLINE) |
| `DisassociateAddress` (contrast) | API/CLI | Existing | Yes | Yes | `ec2:DisassociateAddress` on `elastic-ip` (+ `network-interface`) | scopable by `ec2:AllocationId`/`ec2:PublicIpAddress` — the twin the collateral path bypasses |

**Undocumented/console-hidden knob:** `AssignPrivateIpAddresses.AllowReassignment` (Bool, API-ref only) — **absent from this entire how-to page** (grep of the page for `reassign` = 0 hits). The console "Manage IP addresses" flow and this CLI how-to never surface it; it is the force-move knob the sibling plan proves turns assign into a cross-ENI takeover.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller with `ec2:UnassignPrivateIpAddresses` on an ENI, **denied `DisassociateAddress`** | victim's Elastic IP (`eipalloc-…`) | documented unassign side effect "EIP … also disassociated" | EIP transitions to disassociated under a principal the `DisassociateAddress` scope would have blocked = **collateral-twin control bypass** (High) |
| Caller with `RunInstances` | a specific private IPv4 value in-subnet | `--secondary-private-ip-addresses {val}` | a launch succeeds requesting a chosen internal-service IP that no policy could forbid; collision/pre-empt in shared subnet (Med–High cross-account) |
| Caller with `ec2:AssignPrivateIpAddresses` on target ENI | another ENI's secondary private IP (+ its EIP) | `AllowReassignment=true` | **→ `using-instance-addressing` Area 1 (owned there)**; here only the doc-visibility of the knob |
| Caller | AWS service plane (host side of link-local / managed ENI owner) | n/a | **HARD STOP** — never a target |

---

## 5. Recommended Areas of Focus

### Area 1 — [HEADLINE, NET-NEW] `UnassignPrivateIpAddresses` collateral EIP-disassociation is an unscopable twin of `DisassociateAddress` (Lens X + Lens AA + Lens S/U)
**Background:** This page states verbatim (line 122): *"When a secondary private IPv4 address is unassigned from a network interface, the Elastic IP address (if it exists) is also disassociated."* So `UnassignPrivateIpAddresses` has a **documented second effect** — detaching an EIP — that is the exact capability of `DisassociateAddress`.

**Security Concern:** The two paths to the same end-state have **asymmetric IAM scopability**:
- `DisassociateAddress` (list_ec2 7885–7889) binds the `elastic-ip` resource and carries **`ec2:AllocationId` + `ec2:PublicIpAddress`** → an admin CAN write "may only disassociate EIP X" or deny by AllocationId.
- `UnassignPrivateIpAddresses` (list_ec2 9696–9702) binds **only `network-interface*`** with keys {`aws:ResourceTag`, `ec2:AvailabilityZone`, `ec2:ManagedResourceOperator`, `ec2:NetworkInterfaceID`, `ec2:Region`, `ec2:ResourceTag`, `ec2:Subnet`, `ec2:Vpc`} — **no `elastic-ip` row, no `ec2:AllocationId`, no `ec2:PublicIpAddress`**. The EIP it detaches is never named in the authorization decision.

⇒ A principal **explicitly denied `DisassociateAddress`** (or scoped to only its own AllocationIds) can still detach *any* EIP whose private IP it can reach, simply by unassigning that secondary IP — the EIP-level control is **inert against the collateral path**. This is both a **Lens X twin/collateral-action parity** gap and a **Lens AA revocation-completeness** gap (the "detach EIP" capability survives the control meant to govern it), and a **Lens O audit** angle (a defender alerting on `DisassociateAddress` CloudTrail events is blind to EIP detachment that arrives as a side effect of `UnassignPrivateIpAddresses`).

**High-level Test Scenarios (falsifiable):**
- **Claim:** A role with `Allow ec2:UnassignPrivateIpAddresses` on an ENI (or `Resource:*`) and an **explicit `Deny ec2:DisassociateAddress`** can still cause a victim EIP associated with a secondary IP on that ENI to become disassociated. → **Oracle:** post-call `DescribeAddresses` shows the EIP `AssociationId` gone though the deny is in force. → **Refute:** EC2 blocks the unassign when a secondary IP has an associated EIP without `DisassociateAddress`, or the EIP survives. → **Precondition:** reachable ENI with a secondary private IP that has an associated EIP (canary). → **Severity:** High (control bypass → availability takedown; the detached EIP, if subsequently released, becomes squattable — chains to the hub's released-EIP reclaim-squatting lead).
- **Claim:** No condition key can restrict *which* EIP `UnassignPrivateIpAddresses` is allowed to collaterally detach. → **Oracle:** `iam:SimulateCustomPolicy` for `ec2:UnassignPrivateIpAddresses` with a `Condition` on `ec2:AllocationId`/`ec2:PublicIpAddress` returns the key as not-applicable/implicit-deny-or-ignored (inert). → **Severity:** Medium (expressibility gap; High when it *is* the only control standing between a scoped role and EIP detachment).
- **Adjacent (Lens O):** does the collateral disassociation emit a distinct CloudTrail event (its own `DisassociateAddress` record) or only appear as `UnassignPrivateIpAddresses`? If the latter, EIP-detachment detections keyed on `DisassociateAddress` miss it. → **Oracle:** compare CloudTrail management events for the two paths.

**Doc evidence:** page line 122 (verbatim side effect); `list_ec2.md` 9696–9702 (Unassign keys) vs 7885–7889 (`DisassociateAddress` carries `ec2:AllocationId`/`ec2:PublicIpAddress`). **Severity-if-true:** High.

---

### Area 2 — [NET-NEW framing] Launch-time *secondary* private-IPv4 value is unexpressible in IAM (Lens S/U)
**Background:** This page documents assigning secondary private IPs **at launch**: `run-instances --secondary-private-ip-addresses {{10.251.50.12}}` (explicit value) or `--secondary-private-ip-address-count N` (EC2 chooses). This is a `RunInstances` parameter, distinct from the post-launch `AssignPrivateIpAddresses` path the sibling owns.

**Security Concern:** Confirmed by whole-corpus grep (0 hits for `ec2:PrivateIpAddress`/`ec2:SecondaryPrivate*`) and by reading every `RunInstances` resource row (list_ec2 9585–9610): **no resource row carries any private-IP-value condition key.** The `instance*` row (9591) carries 20+ keys (InstanceType, Tenancy, Metadata*, InstanceProfile, …) but **no IP-value key**; the `network-interface*` row (9595) carries `ec2:AssociatePublicIpAddress`/`Subnet`/`Vpc`/`NetworkInterfaceID` but **no private-IP-value key**. ⇒ An admin **cannot** author a policy that pins or forbids *which* secondary private IPv4 a launch requests. In a shared/known-addressing subnet this allows a launch to deliberately request a **known internal-service IP** (collision / pre-emption / impersonation at birth) with no IAM backstop.

**High-level Test Scenarios:**
- **Claim:** `iam:SimulateCustomPolicy` shows a `Condition` keyed on any private-IP value is inert on `RunInstances` (the key does not exist). → **Oracle:** simulate; key unrecognized/ignored. → **Severity:** Medium (expressibility).
- **Claim (cross-account, shared VPC — composition):** a RAM-share participant can `RunInstances --secondary-private-ip-addresses <hardcoded internal IP>` in the owner's subnet and either pre-empt it (victim launch/attach DoS) or collide. → **Oracle:** two-account canary in a shared subnet; observe whether EC2 rejects a cross-account duplicate/already-in-use secondary IP, and with what error scoping. → **Refute:** EC2 enforces subnet-wide uniqueness cross-account cleanly with a benign error. → **Precondition:** RAM-shared subnet. → **Severity:** Med–High. **Cross-ref** `working-with-ip-addresses` Area 2/4 (owns the private-IP-value-not-expressible fact + the shared-subnet collision doc-gap) — this is the **secondary-IP-at-launch instance** of that gap; do not re-derive, confirm the secondary params inherit it.

**Note (distinct feature — flag, out of this page's scope):** `list_ec2` now shows `RunInstances` carrying **`secondary-interface`** (`arn:…:secondary-interface/${SecondaryInterfaceId}`, 9597/9993) and **`secondary-subnet`** (9598/9995) resource types. These are a *different* feature (secondary **network interfaces/subnets**, not secondary IPs on one ENI) and are not covered by this page's prose. Recommend a separate plan trace them — their `RunInstances` rows carry only tag/Region keys, a potential new scoping gap.

**Doc evidence:** page lines 51–60; `list_ec2.md` 9585–9610 (full RunInstances row set); 0-hit grep for IP-value keys. **Severity-if-true:** Medium (High in a shared subnet).

---

### Area 3 — [NET-NEW] Doc-integrity: the how-to omits `AllowReassignment`, hiding the destructive force-move primitive (Lens U — documented-guarantee / doc-vs-API)
**Background:** The sibling (`using-instance-addressing` Area 1) proves `AssignPrivateIpAddresses … AllowReassignment=true` is a cross-ENI (and RAM-shared-subnet cross-account) **takeover** primitive, consent set by the *gaining* caller. **This page — the primary how-to a customer follows to assign/unassign secondary IPs — never mentions `AllowReassignment`** (grep of the page for `reassign` = 0 hits; the CLI example is a plain `assign-private-ip-addresses` with no `--allow-reassignment`).

**Security Concern:** An operator who builds a "secondary-IP management" IAM role or runbook from this page sees only the benign add/remove flow and has **no cue that the same `ec2:AssignPrivateIpAddresses` grant also authorizes force-stealing an in-use secondary IP (and its EIP) from another ENI** — because the knob is API-ref-only. The guarantee a reader *infers* ("this permission just adds an IP to my own ENI") is contradicted by the API. This is a Lens-U doc-vs-mechanism gap: the enforcement reality (grant = force-move capability, no condition key to forbid it — see sibling Area 2) is invisible on the page that teaches the permission.

**High-level Test Scenarios:**
- **Claim:** a role scoped to `ec2:AssignPrivateIpAddresses` "to manage my ENIs' secondary IPs" (as this page implies) can, with `AllowReassignment=true`, move a secondary IP off a *different* ENI it did not intend to touch. → **Oracle:** sibling-owned (reassign across two canary ENIs). → Here the deliverable is the **doc-gap finding** itself: file that AWS's how-to omits the security-relevant parameter. → **Severity:** Informational/Low as a pure doc defect; the underlying primitive's severity (High) is owned and rated by the sibling.

**Doc evidence:** page lines 66–79 (assign how-to, no `AllowReassignment`); API_AssignPrivateIpAddresses `AllowReassignment` param (API-ref only). **Severity-if-true:** Low (doc-integrity) — pointer to sibling High.

---

### Area 4 — OS-configuration step: client-side only (Lens F/V — scoped OUT, with one hunter note)
**Background:** "Configure the operating system to use secondary IP addresses" — `ec2-net-utils`, `systemd-networkd`/`service network restart`, `ip addr`, and (for ≥2 interfaces on the same subnet) **routing rules to work around asymmetric routing**.

**Security Concern:** This is **in-guest, customer-owned** configuration — no AWS trust boundary is crossed, so it is **out of scope** (customer footgun / product behavior). The one note worth carrying for a hunter: the asymmetric-routing hint signals that multi-secondary-IP / multi-ENI-same-subnet instances rely on **source-based routing in the guest**, not on any AWS-side per-IP isolation (reinforces the sibling's "SG is per-ENI, not per-IP" point — don't re-test here). No parser/translation layer, no server-side dereference. **Null** for Lens F/K/Q.

**Doc evidence:** page lines 92–118. **Severity:** out of scope.

---

### §5-Pointers — surfaces OWNED by siblings (do NOT re-run; cross-reference)
- **Secondary private-IP cross-ENI / cross-account takeover via `AllowReassignment`** → `using-instance-addressing` **Area 1** (headline). Includes "any Elastic IP associated with the IP is also **moved**" on *reassign* (distinct from this plan's unassign→*disassociate* collateral).
- **No `ec2:PrivateIpAddress`/`ec2:Ipv6Address`/`AllowReassignment`/`ec2:AuthorizedUser` key on the 4 assign/unassign actions** → `using-instance-addressing` **Area 2** (reconfirmed here: Assign 4700–4705, Unassign 9696–9702; `ec2:AuthorizedUser` exists on `CreateNetworkInterfacePermission` 5548 but is absent from assign/unassign).
- **Ephemeral public-IPv4 pool reuse / dangling-DNS; link-local SG/NACL bypass; IPv6-is-safer** → `using-instance-addressing` Areas 3/4/6.
- **Launch-time public/private IPv4 generally; `ec2:AssociatePublicIpAddress` inert-Deny; shared-VPC participant forced exposure; `DescribeInstances` read oracle** → `working-with-ip-addresses` Areas 1/3/7.
- **Released-EIP reclaim-squatting; EIP cross-account transfer; `AllocateAddress` no-value key** → `ec2-networking` hub (Area 1 cluster). (Area 1 above *chains into* released-EIP squatting if the collaterally-detached EIP is then released.)

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Detach a victim EIP via unassign while denied `DisassociateAddress` | `UnassignPrivateIpAddresses` collateral | `ec2:AllocationId`/`ec2:PublicIpAddress` scoping on `DisassociateAddress` — **does it bind the collateral path?** (claim: no) |
| EIP-detach detection evasion | CloudTrail | alerting keyed on `DisassociateAddress` — **does the collateral path emit it?** |
| Force a chosen secondary private IPv4 at launch | `RunInstances --secondary-private-ip-addresses` | identity-policy IP-value scoping — **no such key exists** |
| Cross-account secondary-IP collision/pre-empt in shared subnet | `RunInstances`/`AssignPrivateIpAddresses` | subnet-wide uniqueness check — cross-account scope **undocumented** |
| Operator under-scopes a secondary-IP role unaware of force-move | this page's how-to | the page should surface `AllowReassignment` — **it omits it** |

---

## 7. Out-of-Scope Risk Categories
- In-guest OS network configuration (`ec2-net-utils`, routing rules, asymmetric-routing workarounds) — customer-owned (§5 Area 4).
- IMDS/Resolver/Time/KMS **host/Nitro side** of link-local — service plane, **HARD STOP**.
- Single-tenant self-DoS (detaching your own EIP).
- The sibling-owned mechanisms listed in §5-Pointers (re-tested there, not here).
- Shared VPC subnet-attribute product behavior where it is the owner's documented design (vs the composition gaps flagged as leads).

## 8. Null hypotheses / doc gaps
- **Lens A (direct cross-tenant IDOR):** partial-null — the takeover shape exists but is owned by the sibling; `eni-…` IDs are not fabricable blind, residual is known-ENI resource-level-perm enforcement. Pages checked: this page + `using-instance-addressing`.
- **Lens B/C/E (PassRole/vending/privesc):** N/A — no role ARN, STS, token, or SLR on this surface; all three actions run under caller identity. Pages checked: this page, `list_ec2` assign/unassign/RunInstances rows.
- **Lens F/K/Q (injection/prompt/upload):** N/A — no translation layer, no LLM, no upload/URL field; the only "config" step is in-guest. Page checked: §Configure-OS.
- **Lens G (SSRF):** N/A — no field the service dereferences server-side (IPs/ENI-ids are identifiers, not fetched URLs). Pages checked: all three page sections.
- **Lens H/W/Y/FF (KMS/attestation/TLS-sig/JWT):** N/A — none present on this surface.
- **Doc-gaps for the hunter to settle live (two-account canary where noted; `SimulateCustomPolicy` first):**
  1. Does `UnassignPrivateIpAddresses` succeed (and detach the EIP) when the caller lacks/`Deny`s `DisassociateAddress`? (Area 1 — the whole finding turns on this.)
  2. Does the collateral disassociation emit a distinct `DisassociateAddress` CloudTrail event? (Area 1 Lens O.)
  3. Cross-account secondary-IP uniqueness/collision behavior in a RAM-shared subnet (Area 2).
  4. The new `secondary-interface`/`secondary-subnet` RunInstances resource types — separate plan (Area 2 note).

---
*Null-lens discipline satisfied: every N/A above names the page(s)/rows checked. Nothing here claims a bug exists — each lead claims a boundary might not hold and states exactly how to settle it.*
