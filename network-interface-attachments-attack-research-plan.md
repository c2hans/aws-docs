# EC2 Network Interface Attachments — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/network-interface-attachments.html` (offline mirror `docs/AWSEC2/latest/UserGuide/network-interface-attachments.md`, byte-identical to the online `.md` twin 2026-10-15) + the IAM Service Authorization Reference `docs/service-authorization/latest/reference/list_ec2.md` (`AttachNetworkInterface` @4858, `DetachNetworkInterface` @7728, read by offline grep). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Relationship to siblings (READ FIRST — this is a COMPLEMENT, not a standalone).** This page is already cited as a lead-source by the **`using-eni-attack-research-plan.md`** (that plan's lead #2 = cross-VPC attach via `attachments.md:42`; lead #7 = force-detach side effects via `attachments.md:124`). `using-eni` is **authoritative** for the ENI-resource lifecycle/attribute/grant surface (`CreateNetworkInterface`, `ModifyNetworkInterfaceAttribute`, `ResetNetworkInterfaceAttribute`, `Create/DeleteNetworkInterfacePermission`, the `Describe*` oracles, requester-managed/managed-ENI hard stop). This plan owns ONLY the net-new **attachment-specific** surface: the `Attach`/`Detach` action pair, **ENI relocation between instances**, the **instance↔ENI relationship-binding gap**, **force-detach IMDS/index integrity**, and the **cross-service-managed-ENI detach boundary**. Where the two overlap, this plan deepens with the exact `list_ec2` resource-row evidence and cross-refs rather than restating. IP-assignment / EIP-ride-along is deferred to `using-instance-addressing` / `instance-secondary-ip-addresses` / `working-with-ip-addresses`; Windows guest split-brain to `config-windows-multiple-ip`. See [[reference-aws-iam-service-auth-ref-url]].

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The two mutating actions here require resource-level permission on **both** an `instance` and a `network-interface`. The static IAM leads (Areas 1–2) are settleable with **`iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** — **no resources created**. Behavioral leads (Areas 3–5) need a self-owned single-account canary; the cross-team relocation lead (Area 1b) needs two IAM principals in one account (or a RAM-shared subnet across two accounts).
- **`DryRunOperation` is caller-IAM-only** — it is evaluated before resource resolution, so it is NOT an ownership/relationship oracle (false-positive trap; corpus rule).
- **HARD STOP:** service-managed / requester-managed ENIs (ELB, Lambda, WorkSpaces, NAT gateway, EKS `Managed=true`) are the **AWS service plane**. The documented "you do not have permission to access the resource" error (`:95`) *is* the boundary. Do not attempt to detach/attach, force-detach, or probe a service-owned ENI you did not create. If any evidence shows you reaching an AWS-fleet identity/ENI, stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives
Concrete breach outcomes a hunter should try to produce:
1. **Graft a network interface the caller does not own onto an instance the caller controls** (or vice-versa) — relocating another party's IPs / EIPs / SGs / MAC onto an attacker-controlled host, or inserting an attacker-controlled NIC into a victim host — using one `AttachNetworkInterface` call where authz binds only one of the two named resources.
2. **Prove an admin cannot write a guardrail** that (a) forbids cross-VPC attach / requires same-VPC, (b) pins or forbids a `DeviceIndex` / `NetworkCardIndex` (e.g. forbid the primary slot), or (c) forbids **force-detach** — because no condition key expresses any of these.
3. **Desynchronize the control-plane attachment state from the IMDS / guest view** via force-detach (`:124`) so instance metadata reports a NIC that is gone (or hides one that is attached) with no EventBridge signal.
4. **Use the ENI `description` field as a cross-service recon oracle** (`:95`) to enumerate which AWS service and resource owns a reachable ENI, via the unscopable `DescribeNetworkInterfaces`.
5. Confirm the **"you can't detach the primary network interface"** guarantee (`:12`) is enforced by the API for every path (including force-detach and any lower-level twin), not merely by the console.

---

## 2. Components, Assets, and Design

**Mechanism.** A *network interface attachment* binds an existing elastic network interface (ENI, `eni-…`) to an EC2 instance (`i-…`) at a numeric **device index** (and, on multi-card instance types, a **network-card index**). The attachment itself has an opaque id `eni-attach-…`. An attachment is created by `AttachNetworkInterface` (hot/warm/cold — running/stopped/at-launch) and removed by `DetachNetworkInterface`.

**Assets riding on an attachment.** The ENI carries its own private IPv4/IPv6 addresses, any associated **Elastic IPs**, its **security groups**, its MAC, and `sourceDestCheck`. Moving an ENI between instances moves *all* of that network identity with it (relocation primitive). The **primary** ENI (device index 0) is special: it cannot be detached.

**Identity / authz.** SigV4 IAM. `AttachNetworkInterface` and `DetachNetworkInterface` each require resource-level permission on **two** resources (`instance*` **and** `network-interface*`, both `*required` per `list_ec2`). Same-AZ is a hard requirement (ENI and instance must share an AZ). The ENI may live in a **different VPC that the caller owns** (`:42`).

**Identifier shapes.** `eni-…` / `eni-attach-…` / `i-…` — 17-hex-char suffixes (high entropy; not fabricable → blind cross-account IDOR is a partial null, like `sfr-`/`cr-` elsewhere in the corpus). The attachment id `eni-attach-…` has **no IAM resource type** — `DetachNetworkInterface` authz resolves it server-side to the `(instance, network-interface)` pair.

```
                         same AZ required
   ┌──────────────┐   AttachNetworkInterface   ┌─────────────────────────┐
   │  instance i-X │◄──(instance* AND eni*)────►│ ENI eni-Y               │
   │  (VPC A)      │   device-index / card-idx  │  - private IPv4/IPv6    │
   └──────┬────────┘                            │  - Elastic IP(s)        │
          │ IMDS view (may go STALE on          │  - security groups      │
          │  force-detach :124)                 │  - MAC / sourceDestCheck│
          ▼                                     │  (VPC A **or** VPC B)   │
   169.254.169.254                              └─────────────────────────┘
   network/interfaces/macs/...                   may be SERVICE-MANAGED
                                                 (ELB/Lambda/WS/NATGW) → :95 HARD STOP
```

**Mandatory coverage sweep (pages read):** target page in full (considerations list `:11-20`, Attach console/CLI/PS `:40-80`, Detach console/CLI/PS `:93-140`); `list_ec2.md` rows for both actions + whole-corpus condition-key grep; cross-ref `using-eni.md`, `scenarios-enis.md`, `requester-managed-eni.md`, `config-windows-multiple-ip.md`, `automating_with_eventbridge.md` (event catalog), `using-instance-addressing.md` (public-IP behavior). No URL/host field the service dereferences (→ Lens G null), no upload/blob (→ Q null), no role-ARN/PassRole/STS/token/secret/KMS/sample-IAM-policy/attestation/JWT surface on this page (→ B/C/H/R/T/W/FF nulls — see §8, pages named).

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internet-callable | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `AttachNetworkInterface` | `ec2:AttachNetworkInterface` | Existing | **Mutating** | Yes (SigV4) | Attach ENI to instance at device-index (+ optional network-card-index) | principal with Write on **both** `instance*` and `network-interface*` | Requires same-AZ; ENI may be in a different owner-VPC (`:42`). Params: `--network-interface-id`, `--instance-id`, `--device-index`, (`--network-card-index`). |
| `DetachNetworkInterface` | `ec2:DetachNetworkInterface` | Existing | **Mutating** | Yes (SigV4) | Detach a secondary ENI by attachment-id; optional `--force` | principal with Write on **both** `instance*` and `network-interface*` (resolved from attachment-id) | CLI takes only `--attachment-id`; IAM resolves to (instance, ENI). `--force` has **no condition key**. Cannot detach primary (device-index 0). |
| `DescribeNetworkInterfaces` | `ec2:DescribeNetworkInterfaces` | Existing | Non-mutating | Yes | Read ENI incl. `description`, `attachment`, owner | *(see `using-eni`)* unscopable (blank resource type, only `ec2:Region`) | **Recon oracle** backing Area 4 (`description` reveals service owner). Owned by `using-eni` #5 — cross-ref only. |

Console-hidden / under-surfaced knobs: `--network-card-index` (multi-card types) and `--force` (detach) are accepted by the API with **no IAM condition key** governing their values (see Area 2).

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller holding attach on instance `i-X` (team/acct A) | ENI `eni-Y` owned by team/acct B | `AttachNetworkInterface(i-X, eni-Y)` | Attach succeeds while the caller lacks Write on `eni-Y` — the ENI's IPs/EIPs/SGs are grafted onto the attacker's host. **Both resources are `*required`, so pure success here would mean one row's authz was skipped.** |
| Caller holding attach on ENI `eni-Y` (A) | Instance `i-Z` owned by B | `AttachNetworkInterface(i-Z, eni-Y)` | Attach inserts a caller-controlled NIC (attacker SGs/routes/`sourceDestCheck`) into victim host `i-Z` while the caller lacks Write on `i-Z`. |
| Caller in VPC A | ENI in VPC B (same owner) | cross-VPC attach (`:42`) | No condition key can require the ENI's VPC to equal the instance's VPC → "same-VPC-only" guardrail is inexpressible (deepens `using-eni` #2). |
| Control plane (attachment state) | IMDS / guest OS view | force-detach (`:124`) | IMDS reports a NIC that control-plane shows detached (or blocks same-index reattach) — state desync with **no EventBridge event**. |
| Any caller | AWS service plane (ELB/Lambda/WS/NATGW ENI) | detach attempt (`:95`) | **HARD STOP.** The permission error is the designed boundary; any success reaching a service-owned ENI = disclosure-grade breach. |

---

## 5. Recommended Areas of Focus

### Area 1 — ENI relocation & the instance↔ENI relationship-binding gap  *(HEADLINE; Lens A / S / V / X)*
**Background.** `AttachNetworkInterface` requires resource-level permission on **both** `instance*` and `network-interface*` (both `*required`, `list_ec2`:4860-4862). The page explicitly supports two relocation shapes: *"You can detach a secondary network interface from one instance and attach it to another instance"* (`:13`) and *"The network interface can reside in … a different VPC that you own … multi-homed instances across VPCs with different networking and security configurations"* (`:42`).

**Security Concern.** There is **no condition key that expresses the *relationship* between the two named resources.** The `network-interface*` row carries `ec2:Vpc`/`ec2:Subnet`, but those evaluate to the **ENI's own** home VPC/subnet (Lens-S "binds the wrong resource" — the same shape as `ec2:Vpc` on `AssociateSecurityGroupVpc`); the `instance*` row carries **no `ec2:Vpc`/`ec2:Subnet` at all**. So a policy cannot require ENI.VPC == instance.VPC, cannot forbid cross-VPC attach, and cannot bind "only attach ENIs this instance's owner owns." Enforcement that the ENI and the instance belong to the same party rides entirely on both resources independently passing their own ABAC/ARN scoping — the join is unmechanized.

**High-level Test Scenarios (falsifiable claims):**
- *Claim:* A principal scoped (by tag/ARN) to its own instance `i-X` but **not** to ENI `eni-Y` can nonetheless attach `eni-Y` to `i-X`, grafting `eni-Y`'s private IPs + any associated **Elastic IP** + security groups onto `i-X`. → **Oracle:** attach returns 200 under a scoped role holding Write on `i-X` only; refute = `AccessDenied` on the `network-interface*` element. Settle the *policy* question first with `iam:SimulateCustomPolicy` (does a Deny on `eni-Y` block the call?), then a single-account canary with two tag-scoped roles.
- *Claim:* Symmetrically, a principal scoped to ENI `eni-Y` but not to victim instance `i-Z` can insert `eni-Y` (attacker SGs / `sourceDestCheck=disabled` routing node) into `i-Z`. → **Oracle:** same, scoped to the ENI row only.
- *Claim:* An org that intends "instances may only attach ENIs from their own VPC" **cannot author that policy** — no key cross-references the two VPCs. → **Oracle:** `SimulateCustomPolicy` with every plausible `ec2:Vpc`/`ec2:Subnet` condition shows the cross-VPC attach still `allowed` (the NI-row `ec2:Vpc` matches the ENI's VPC regardless of the instance's).
- *Adjacent (Lens X):* does the ENI relocation reach the **IPs/EIPs** before any ownership re-check? Cross-ref the EIP-ride-along facts in `using-instance-addressing` (secondary-IP move carries the EIP). Attaching an ENI relocates its *entire* address set in one call — a coarser relocation than the per-IP primitive that plan owns.

**Doc evidence:** `attachments.md:13,42`; `list_ec2.md`:4858-4863 (both rows + absent instance-VPC key). **Severity-if-true:** intra-account cross-team ENI/EIP/SG hijack = **Medium–High**; via RAM-shared subnet across accounts = **High** (bounded by both-resource authz — the realistic win is the cross-team / shared-subnet case, not blind cross-account). **Stop:** once the policy-expressibility question is settled by Simulate + one canary attach/detach you created; do not iterate across foreign resources.

### Area 2 — Device-index / network-card-index / force not expressible in IAM  *(Lens S / U)*
**Background.** Attach takes `--device-index` and (multi-card types) `--network-card-index`; detach takes `--force`. The primary ENI lives at device-index 0 and *"you can't detach the primary network interface"* (`:12`).

**Security Concern.** Whole-corpus grep of `list_ec2.md` returns **ZERO** hits for `ec2:DeviceIndex`, `ec2:NetworkCardIndex`, `ec2:InterfaceType`, `ec2:DeleteOnTermination`, `ec2:AttachmentId`, and **`ec2:Force`**. (This reconfirms `using-eni` #3 for the value-level keys and adds the attach/detach-specific `DeviceIndex`/`NetworkCardIndex`/`Force` absence.) Consequently:
- No policy can **pin or forbid a device index** (e.g. "never attach at index 0 / the primary slot", "secondary NICs only at index ≥ 1").
- No policy can restrict **which network card** a NIC lands on (relevant to multi-card bandwidth/placement on `p`/`trn` families).
- No policy can **forbid force-detach**, even though the page itself warns to use it *"only as a last resort"* (`:124`).
- The "cannot detach the **primary** NIC" guarantee is therefore enforceable only by **API orchestration**, never by IAM — a Lens-U guarantee-vs-mechanism gap.

**High-level Test Scenarios:**
- *Claim:* A Deny intended to forbid force-detach (`"ec2:Force":"true"` or similar) is **inert** because the key does not exist. → **Oracle:** `SimulateCustomPolicy` shows the Deny never matches; a live force-detach still succeeds under a role carrying only `ec2:DetachNetworkInterface`.
- *Claim:* The primary-NIC protection holds for **every** path — confirm no lower-level/legacy twin (Lens X) and that `--force` does not bypass it. → **Oracle:** `detach-network-interface --attachment-id <primary-attach> --force` on a *self-owned* instance returns a validation/authorization error (expected `OperationNotPermitted`); a 200 would be a finding. Canary only; never against a foreign/primary that is not yours.
- *Claim:* An admin "pin the secondary NIC to a specific device index" control is impossible. → **Oracle:** Simulate with every `ec2:*Index`-shaped condition shows no match.

**Doc evidence:** `attachments.md:12,124`; `list_ec2.md` grep (0 hits for the five keys above). **Severity-if-true:** least-privilege/guardrail-expressibility gap = **Low–Medium** (High only where chained into Area 1 relocation or Area 3 force-detach integrity).

### Area 3 — Force-detach IMDS / index-lock integrity & detection blind spot  *(Lens O / U / L)*
**Background.** Verbatim (`:124`): force detachment *"can prevent you from attaching a different network interface on the same index until you restart the instance. It can also prevent the instance metadata from reflecting that the network interface was detached until you restart the instance."* (Deepens `using-eni` #7.)

**Security Concern.** Two first-class integrity/availability effects, both with **no purpose-built event** (confirmed in `config-windows-multiple-ip` Area 3 against the full `automating_with_eventbridge.md` catalog: there is **no EventBridge event** for ENI attach/detach/reassign; only a CloudTrail *management* event, logged by default, lands — in the instance/ENI owner's trail):
1. **IMDS state desync (integrity):** after a force-detach the instance metadata (`network/interfaces/macs/…`) can keep advertising a NIC that the control plane shows detached. Any guest-OS or in-instance logic that trusts IMDS for its interface/IP inventory (overlaps the Windows static-binding **split-brain** owned by `config-windows-multiple-ip`) now operates on a phantom NIC until a restart it may never schedule.
2. **Index-lock DoS:** the device index stays occupied until restart → a `maintain`/automation attempt to attach a replacement NIC at the same index fails. One forced detach can wedge an index on a long-lived instance.

**High-level Test Scenarios:**
- *Claim:* Post-force-detach IMDS still lists the detached ENI's MAC/IP while `DescribeNetworkInterfaces` shows it detached — a control-plane-vs-guest divergence usable to confuse IMDS-trusting software or to hide a NIC removal. → **Oracle:** self-owned canary; force-detach a secondary ENI; diff `curl 169.254.169.254/latest/meta-data/network/interfaces/macs/` against `describe-network-interfaces`. Refute = IMDS updates immediately.
- *Claim:* No EventBridge event fires for the detach; the only signal is a CloudTrail `DetachNetworkInterface` management event in the ENI/instance owner's account (so a cross-account relocation onto an attacker's ENI/instance leaves the victim's trail without a tailored "your NIC was moved" record). → **Oracle:** inspect EventBridge + CloudTrail during the canary.
- *Claim:* The same-index reattach lock enables a per-instance availability wedge without terminating anything. → **Oracle:** force-detach, then attempt same-index attach → expect failure until restart.

**Doc evidence:** `attachments.md:124`; `config-windows-multiple-ip` Area 3 (event-catalog negative); `using-eni` #5 (unscopable Describe). **Severity-if-true:** integrity/detection = **Low–Medium**; **Medium** when chained to Area 1 relocation (hides the move) or to the Windows split-brain.

### Area 4 — Cross-service-managed ENI detach boundary + `description` recon oracle  *(Lens U + service-plane HARD STOP)*
**Background.** Verbatim (`:95`): *"If you try to detach a network interface that is attached to a resource from another service, such as an Elastic Load Balancing load balancer, a Lambda function, a WorkSpace, or a NAT gateway, you get an error that you do not have permission to access the resource. To find which service created the resource attached to a network interface, check the description of the network interface. If you delete the resource, then its network interface is deleted."*

**Security Concern.** Two things to probe **without touching the service plane**:
1. **Does the boundary hold for *all* service-managed ENI classes and for the force-detach path?** The error is the documented control. The research question is whether any variant (force-detach, a lower-level twin, an unusual requester-managed type) is accepted where the normal detach is refused. **This must be answered doc-side or against a self-created ELB/NAT-gateway canary only** — a success against a service-owned ENI you do not own is a **hard-stop, disclosure-grade** result; preserve evidence and stop. Cross-ref `using-eni` HARD STOP (requester-managed + `Managed=true` ENIs = AWS plane).
2. **The `description` field is a recon oracle.** The page tells the operator to read the ENI `description` to learn which service and resource created it; `DescribeNetworkInterfaces` is **unscopable** (blank resource type, only `ec2:Region` — `using-eni` #5). So a principal who can describe ENIs can enumerate, account-wide, which ELB/Lambda/WorkSpace/NAT-gateway owns each ENI (service + often the resource name embedded in the description) — an inventory/attack-surface map with no ownership scoping.
3. **Cascade note (Lens AA):** *"If you delete the resource, then its network interface is deleted"* — deleting the fronting service resource cascades to the ENI; conversely a detach is refused. Confirm there is no path where detaching/force-detaching strands or re-parents a service-managed ENI.

**High-level Test Scenarios:**
- *Claim (recon):* `DescribeNetworkInterfaces` with no resource scoping returns `description` + `requesterId`/`attachment` for ENIs the caller does not own, revealing service ownership account-wide. → **Oracle:** read-only describe under a least-privilege describe role; confirm foreign/service ENI metadata is returned.
- *Claim (boundary):* every detach variant against a service-managed ENI returns the documented permission error. → **Oracle:** self-created ELB/NAT-gateway ENI canary only; `detach-network-interface` (± `--force`) → expect `AuthFailure`/`OperationNotPermitted`. **STOP on any 200.**

**Doc evidence:** `attachments.md:95`; `using-eni` #5 (unscopable Describe), HARD STOP. **Severity-if-true:** recon oracle = **Low–Medium**; any detach reaching the service plane = **Critical + hard stop**.

### Area 5 — Launch-time & multi-NIC public-IPv4 behavior shifts  *(Lens U, low)*
**Background.** `:14` *"you can't enable the auto-assignment of public IPv4 addresses if you add a secondary network interface during launch"*; `:30` (Attach section) *"If the public IPv4 address on your instance is released, it does not receive a new one if there is more than one network interface attached."* `:18` same-subnet multi-NIC → asymmetric routing; `:19` IPv6-only subnet → secondary NIC's private DNS resolves to the **primary NIC's primary IPv6**.

**Security Concern.** The **number of attached NICs silently changes public-IPv4 addressing behavior** — adding a secondary NIC at launch suppresses auto-assign, and a released public IP is not re-issued once >1 NIC is attached. This is primarily a correctness/availability footgun, but it interacts with the ephemeral-public-IP **dangling-DNS / pool-reuse** surface owned by `using-instance-addressing` (a box that silently loses its public IP after a second NIC attach may leave a stale public-DNS record). The IPv6-only DNS reflection (`:19`) is a minor identity note (secondary NIC's hostname points at the primary NIC's IPv6).

**High-level Test Scenarios:**
- *Claim:* attaching a secondary NIC to a running instance and then releasing/losing the public IP yields no replacement, potentially orphaning a public-DNS record. → **Oracle:** cross-ref `using-instance-addressing` dangling-DNS lead; canary observe. **Severity:** **Low** (chains into the sibling's dangling-DNS lead, which owns the primitive).

**Doc evidence:** `attachments.md:14,18,19,30`. **Severity-if-true:** **Low / Informational**; defers to `using-instance-addressing` / `working-with-ip-addresses`.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Graft foreign ENI onto own instance (or own ENI into victim instance) | `AttachNetworkInterface` (dual `*required` rows) | Both-resource authz — does each row's ABAC/ARN scoping actually bind, or is one skipped? No relationship key exists (Area 1). |
| Admin cannot forbid cross-VPC attach / force same-VPC | `AttachNetworkInterface` NI-row `ec2:Vpc` | `ec2:Vpc` binds the ENI's *own* VPC; no cross-check to instance VPC (Area 1, Lens S). |
| Admin cannot forbid force-detach / pin device-index | `DetachNetworkInterface --force`, `--device-index` | No `ec2:Force`/`ec2:DeviceIndex`/`ec2:NetworkCardIndex` key (Area 2). |
| Primary NIC undetachable on every path | `DetachNetworkInterface` | API orchestration only — confirm `--force` + twins don't bypass (Area 2). |
| IMDS vs control-plane state desync | force-detach | Documented warning `:124`; no EventBridge event; CloudTrail only (Area 3). |
| Account-wide service-ENI inventory via `description` | `DescribeNetworkInterfaces` | Unscopable read; `description` reveals service owner (Area 4). |
| Service-plane ENI detach refusal holds | `DetachNetworkInterface` on managed ENI | Documented permission error `:95` = the control (Area 4) — HARD STOP on success. |

---

## 7. Out-of-Scope Risk Categories
- **AWS service-plane / requester-managed / `Managed=true` ENIs** — ELB/Lambda/WorkSpaces/NAT-gateway/EKS-owned interfaces. The `:95` permission error is the designed boundary; do not probe. Any reach = hard-stop disclosure, not a test to pursue.
- **The host / Nitro side of IMDS** (`169.254.169.254`) — the metadata-staleness lead (Area 3) is tested from *inside your own canary instance* only; the hypervisor/Nitro service is off-limits.
- **Blind cross-account IDOR by fabricating `eni-…`/`i-…`/`eni-attach-…`** — 17-hex-char high-entropy ids are not guessable; this is a genuine partial-null (same as `sfr-`/`cr-` in the corpus). Realistic cross-party wins require a RAM-shared subnet or known ids, not fabrication.
- **Single-tenant self-DoS** (index-lock on your own instance absent a cross-party effect) — informational.
- **IP-assignment / EIP-ride-along / ephemeral-pool / dangling-DNS / link-local IMDS filtering** — owned by `using-instance-addressing`, `instance-secondary-ip-addresses`, `working-with-ip-addresses`; referenced, not re-tested here.
- **ENI-resource lifecycle/attribute/grant/`sourceDestCheck`-MITM/requester-managed-reset** — owned by `using-eni`; this plan only cross-refs.
- **Shared RDS/Grover/storage infra, product/feature-parity gaps, DNS rebinding against private-only endpoints.**

## 8. Null hypotheses / doc gaps (lenses that did not fire — pages checked named)
- **Lens G (SSRF) — N/A.** Read the full target page + Attach/Detach CLI/PS sections: no field the service dereferences/fetches/previews. `--network-interface-id`/`--instance-id`/`--device-index` are identifiers, not URLs.
- **Lens Q (upload) — N/A.** No blob/image/document/attachment field on this page.
- **Lens B / C (PassRole / credential-vending) — N/A.** Neither action accepts a role ARN, token, or session-policy; both run under the caller's own identity (no SLR, no `AssumeRole`). Checked both `list_ec2` rows and the page.
- **Lens R / S-artifact — N/A for shipped artifacts; S (condition-key semantics) FIRES** (Areas 1–2). No IAM policy JSON / managed policy / CFN / runbook block is printed on the page (checked whole page), so there is no AWS-authored artifact to audit here; the S findings are reference-table semantics, not a shipped policy.
- **Lens H (KMS), T (secret storage), W (attestation), FF (JWT), DD (cache), BB (parser-differential), CC (upstream-context), EE (predictable-name), K (prompt injection), P (proofing), J (OAuth), N (namespace migration) — N/A.** None of their triggers appear on the attachments page or in the two action rows (no key material, no token/claims, no caching layer, no multi-parser request path, no asserted-identity header, no predictable global namespace, no LLM/agent, no registration/OTP flow, no 3P linking, no dual-ARN migration).
- **Doc gaps for the hunter to settle live (DryRun cannot — it is caller-IAM-only):**
  1. Does `AttachNetworkInterface` actually enforce authz on **both** `instance*` and `network-interface*` elements, or can one be skipped (Area 1 — the whole plan's pivot)? Settle policy-side with `SimulateCustomPolicy`, then one self-created canary.
  2. Does force-detach bypass the primary-NIC-undetachable guarantee or any service-managed-ENI refusal (Areas 2, 4)? Canary / self-owned ELB only.
  3. Exact IMDS-vs-control-plane staleness window and whether any event beyond the CloudTrail management event fires (Area 3).
  4. Whether a RAM-shared subnet lets a participant attach/detach ENIs or instances owned by the subnet owner (cross-account edge of Area 1) — needs a two-account canary; `using-vpc.md` documents the "participants own the ENIs they specify" rule for *RunInstances*, never for `AttachNetworkInterface` (same doc-gap shape as the `AssignPrivateIpAddresses` gap owned by `using-instance-addressing`).

---
*Confirmed offline==online 2026-10-15. `list_ec2.md`: `AttachNetworkInterface` @4858 (instance* + network-interface*, both required), `DetachNetworkInterface` @7728 (instance* + network-interface*, both required); 0 hits for `ec2:DeviceIndex`/`ec2:NetworkCardIndex`/`ec2:InterfaceType`/`ec2:DeleteOnTermination`/`ec2:AttachmentId`/`ec2:Force`. See [[reference-aws-iam-service-auth-ref-url]].*
