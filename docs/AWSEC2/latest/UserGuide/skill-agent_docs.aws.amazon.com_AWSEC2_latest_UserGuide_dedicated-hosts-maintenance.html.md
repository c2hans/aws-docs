# EC2 Dedicated Host — Host Maintenance — Attack Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance.html
**Sub-pages in scope:** `dedicated-hosts-maintenance-basics.html`, `dedicated-hosts-maintenance-configuring.html`
**Source of leads:** offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance*.md`; IAM Service Authorization Reference `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`; `API_ModifyHosts.md`; sibling pages `dedicated-hosts-recovery-enable.md`, `dedicated-hosts-billing.md`, `reschedule-event.md`. Online page fetched 2026-09-09 — **identical** to offline mirror; **no injected "See also" / AI-agent instruction block** on these pages.
**Status:** documentation-derived hypotheses only. Nothing tested against a live account. Skill: `security-questionbuilder`.

---

## 0. How to use this document
- Each lead is: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The safe first oracle for every IAM lead here is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (touches no resources). Escalate to a live scoped call only with a throwaway Dedicated Host you allocated as canary.
- **HARD STOP:** Host maintenance is driven by AWS's own **live-migration fleet** moving a running instance's memory/CPU/network state between physical hosts. The moment evidence touches that migration channel, a source-host memory-scrub, replacement-host provenance, or any AWS-fleet identity/credential/ARN → **stop, preserve evidence, flag for AWS-Security disclosure.** Do not probe the migration plane.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Prove an org/SCP cannot durably enforce Dedicated-Host resilience posture.** Show a principal holding only `ec2:ModifyHosts` can flip `HostMaintenance`→off / `HostRecovery`→off / `AutoPlacement`→on and that **no value-scoped condition key exists** to deny it (the org's `AllocateHosts` guard is bypassable post-allocation).
2. **Prove attribute-multiplex privilege bleed.** Show a grant intended only to re-target `InstanceFamily`/`InstanceType` on a host also authorizes disabling maintenance/recovery, because `ModifyHosts` is one action over five attributes scopable only by `ec2:Attribute` (test case-sensitivity fail-open).
3. **Refute or confirm the "host-in-a-resource-group cannot toggle maintenance" guarantee** is enforced at the API/IAM layer, not just the console.
4. **Refute** cross-account IDOR on `ModifyHosts` / `ModifyInstanceEventStartTime` (host-id / instance-id ownership).
5. **Name and hard-stop** the live-migration service-plane boundary; confirm billing/reservation-transfer integrity is AWS-owned and not customer-drivable.

---

## 2. Components, Assets, and Design

**What host maintenance is.** A per-Dedicated-Host setting (`on`/`off`). When AWS *detects* a Dedicated Host has degraded (host enters `permanent-failure` state), and maintenance is `on`, EC2 **automatically allocates a replacement Dedicated Host in the same account** (new host ID, same attributes: auto-placement, AZ, DH-Reservation association, host affinity, maintenance & recovery settings, instance type, **Tags**) and migrates the running instances to it, then releases the degraded host.

**Two migration modes (mode is chosen by AWS per instance, not by the customer):**
- **Live migration** — instance moved within 24h *without* stop/restart; retains Instance ID, metadata, EBS attachments, EIP/private IP, **and memory/CPU/networking state**. → This is a full running-VM migration performed by AWS's fleet = **service plane**.
- **Reboot-based** — instance scheduled for an *instance reboot* event (14 days out, reschedulable within 7 days); stopped & restarted into **reserved capacity** on the replacement host; loses memory/CPU/net state; retains ID/metadata/EBS/EIP.
- **Not auto-migratable:** EBS-root instances get an *instance stop* event at 28 days; instance-store-root instances (C1, C3, D2, I2, M1, M2, M3, R3, X1) get an *instance retirement* (terminate) event at 28 days.

**Disable behavior (`dedicated-hosts-maintenance-configuring.md`):** disabling sends an eviction email; customer must migrate within 28 days; **after 28 days instances on a degraded host are terminated and the host is released automatically.** ⇒ toggling maintenance `off` is an availability-affecting action.

**Interfaces / control surface (all AWS control-plane, SigV4):**
- `ec2:ModifyHosts` (`aws ec2 modify-hosts` / `Edit-EC2Host`) — sets `HostMaintenance`, `HostRecovery`, `AutoPlacement`, `InstanceFamily`, `InstanceType` on an existing host. **This is the entire customer-facing write surface for this feature.**
- `ec2:AllocateHosts` — sets the same posture at creation.
- `ec2:ModifyInstanceEventStartTime` (`modify-instance-event-start-time`) — reschedule the reboot/stop event.
- Notifications: email + AWS Health Dashboard (out of band).

**Accounts / tenancy.** A Dedicated Host is **single-tenant dedicated hardware** for one account — no co-tenant on the same physical host. The multi-tenancy that matters is at the **AWS fleet level**: the replacement host is *different physical hardware* drawn from AWS's pool, and live migration moves VM state across AWS's migration infrastructure. Those are AWS-owned planes.

**Cross-service governance edges:** **AWS License Manager** (host resource groups; BYOL license counting — "licenses associated with the degraded host are released when the host is released"), **Dedicated Host Reservations** (billing; transferred to the replacement host).

```
Customer IAM principal
      │  ec2:ModifyHosts (HostMaintenance/HostRecovery/AutoPlacement/InstanceType/Family)
      ▼
  ┌──────────────────────────┐        AWS detects degradation
  │  Dedicated Host (h-xxxx)  │────────────────────────────────►  permanent-failure
  │  single-tenant HW         │                                        │
  └──────────────────────────┘                                        │ auto-allocate (same acct)
        │ instances                                                    ▼
        │                                              ┌──────────────────────────┐
        │  ┌── live migration (mem/CPU/net state) ────►│ Replacement DH (h-YYYY,   │
        └──┤        [AWS fleet = SERVICE PLANE]         │ new ID, retains Tags +    │
           └── reboot-based (stop/start → reserved cap) │ settings + DH-Reservation)│
                                                        └──────────────────────────┘
  License Manager (HRG, license release)   ◄── cross-service governance ──►  DH Reservations / billing
```

---

## 3. API / Interface Inventory

| Name | Method | Mutating | Facing | Functionality | Callable from Internet | Authorized callers | Notes (condition keys — from `list_ec2.md`) |
|---|---|---|---|---|---|---|---|
| `ModifyHosts` | POST (Query) | **Yes** | External | Set `HostMaintenance`, `HostRecovery`, `AutoPlacement`, `InstanceType`/`InstanceFamily` on an existing DH | Yes (SigV4) | account principals w/ `ec2:ModifyHosts` | Resource `dedicated-host*`. **Condition keys ONLY: `aws:ResourceTag/${TagKey}`, `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`.** Multiplexed setter. **PRIMARY target (Lens S/U/X).** |
| `AllocateHosts` | POST (Query) | Yes | External | Allocate a DH; set posture at creation | Yes | `ec2:AllocateHosts` | Resource `dedicated-host*`. Condition keys incl. **value-scoping** `ec2:AutoPlacement`, `ec2:HostRecovery`, `ec2:InstanceType`, `ec2:Quantity`, `aws:RequestTag`. **Asymmetry vs ModifyHosts is the crown jewel.** |
| `ModifyInstanceEventStartTime` | POST (Query) | Yes | External | Reschedule the reboot/stop scheduled event | Yes | `ec2:ModifyInstanceEventStartTime` | Resource `instance*`; keys incl. `ec2:InstanceID`, `ec2:ResourceTag`, `ec2:Tenancy`. Ownership-scoped by instance. |
| `ReleaseHosts` | POST (Query) | Yes | External | Release a DH | Yes | `ec2:ReleaseHosts` | Resource `dedicated-host*`, keys `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag`. AWS auto-releases the degraded host — customer path is adjacent. |
| `DescribeHosts` | GET (Query) | No | External | View host state / reserved capacity | Yes | `ec2:DescribeHosts` | Reflects reserved capacity as "used" during reboot-based maintenance. |

**Undocumented/console-hidden knob check:** `API_ModifyHosts.md` exposes `HostMaintenance`, `HostRecovery`, `AutoPlacement`, `InstanceFamily`, `InstanceType` — the console "Modify host" dialog surfaces only some of these together. The API accepts all five in whatever combination (except `InstanceType`+`InstanceFamily` mutually exclusive). No `authorizerType:NONE`-style hidden weakener here, but the **API surface is broader than the per-attribute IAM guard** — see Area 1/2.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv IAM principal (`ec2:ModifyHosts`) | Org/SCP-intended resilience posture | `modify-hosts --host-maintenance off` / `--host-recovery off` | A principal the org intends to bind flips the value and **no condition key can deny by value** → posture guarantee is advisory only. |
| Principal granted "re-target instance family only" | Host maintenance/recovery/auto-placement | `ModifyHosts` multiplexes 5 attrs under 1 action | Setting `HostMaintenance`/`HostRecovery`/`AutoPlacement` succeeds under a grant meant only for `InstanceFamily` (no `ec2:Attribute` scoping, or case-fail-open). |
| Host inside a License-Manager host resource group | Its maintenance setting | Direct `ModifyHosts` API (bypassing console block) | Doc says it "can't be turned on or off" for HRG hosts — an API `ModifyHosts(HostMaintenance)` that **succeeds** on an HRG member = doc-vs-enforcement gap. |
| Caller (account A) | Another account's host (`h-…`) / instance event | `ModifyHosts --host-ids` / `ModifyInstanceEventStartTime --instance-id` | A 200 on a foreign-owned host-id / instance-id = cross-account IDOR (expected: AccessDenied). |
| Running instance on degraded host | AWS live-migration fleet (**service plane**) | Automatic live migration of mem/CPU/net state | **HARD STOP** — any reach into the migration channel, source-host memory residue, or replacement-host provenance implicates AWS's own plane. |
| Customer billing | Degradation-triggered billing stop + DH-Reservation transfer | AWS auto-detect + auto-transfer | Billing stops "as soon as maintenance is initiated"; reservation transfers to replacement. Customer cannot trigger degradation and cannot launch on `permanent-failure` → no free-compute path (refute). |

---

## 5. Recommended Areas of Focus

### Area 1 — `ModifyHosts` value-scoping gap: no `ec2:HostMaintenance` key + Allocate-vs-Modify enforcement asymmetry  *(Lens S / U / X — PRIMARY / crown jewel)*
**Background.** Dedicated-Host resilience posture (`HostMaintenance`, `HostRecovery`, `AutoPlacement`, `InstanceType`) can be set two ways: at creation via `AllocateHosts` and post-creation via `ModifyHosts`. `AllocateHosts` exposes **value-scoping** condition keys — `list_ec2.md:4651-4658` shows `ec2:AutoPlacement`, `ec2:HostRecovery`, `ec2:InstanceType`, `ec2:Quantity`. `ModifyHosts` (`list_ec2.md:8757-8763`) exposes **only** `aws:ResourceTag/${TagKey}`, `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`.

**Security Concern.**
1. **No `ec2:HostMaintenance` condition key exists anywhere in `list_ec2.md`** (grep: zero hits). ⇒ An org/SCP **cannot** write a policy that *requires* host maintenance stay `on`, nor one that *denies* turning it `off`, by value. The only lever is `ec2:Attribute` (deny *modifying the attribute at all*), which is coarser and also blocks legitimate re-targeting.
2. `ec2:HostRecovery` *does* exist and *is* honored by `AllocateHosts`, but it is **absent from `ModifyHosts`'s condition-key set** — so a Deny keyed on `ec2:HostRecovery` for `ModifyHosts` is **inert** (the key is never populated in that request's authz context → the Deny's `StringEquals` never matches → fail-open guard). This is the confirmed Lens-S "condition key silently ignored / does not apply to this action" shape (cf. `ec2:InterfaceType`, and the SEV-SNP `AllocateHosts` gap in `[[project_sev-snp-plan]]`).
3. Net: an org can force `HostRecovery=on` / a maintenance-compatible `InstanceType` at *allocation*, but **any principal holding `ec2:ModifyHosts` can silently reverse it afterward** (`--host-recovery off`, `--auto-placement on`) with no value-scoped IAM guard available to stop them. Combined with the documented **disable → 28-day auto-terminate** behavior (`dedicated-hosts-maintenance-configuring.md`), flipping `HostMaintenance` off is an availability-degrading change with no durable governance control.

**High-level Test Scenarios (falsifiable):**
- **Claim:** There is no way to author an IAM/SCP condition that denies `ModifyHosts` by the *value* `HostMaintenance=off` (or `HostRecovery=off`). → **Oracle:** enumerate the ModifyHosts condition-key set in `list_ec2.md` / `iam:SimulateCustomPolicy` a Deny keyed on `ec2:HostRecovery` (or a hypothetical `ec2:HostMaintenance`) against a `ModifyHosts(HostMaintenance=off)` request context — the Deny fails to fire = confirmed. **Confirmed by docs already; live step just proves the inert Deny.**
- **Claim:** An `AllocateHosts`-time `ec2:HostRecovery==on` guard is bypassable post-allocation via `ModifyHosts`. → **Oracle:** with a scoped role holding `AllocateHosts` (guarded) + `ModifyHosts`, allocate a host (recovery on), then `modify-hosts --host-recovery off` succeeds.
- **Claim (case-fail-open):** the only usable guard, `ec2:Attribute`, fails open under casing variance — a `Deny` keyed on `ec2:Attribute StringEquals "hostMaintenance"` is inert if the request populates the key with a different casing (`HostMaintenance`). → **Oracle:** `SimulateCustomPolicy` the Deny vs each casing (mirrors the confirmed `ec2:Attribute` case-fail-open in `[[project_ec2-instance-resize-plan]]` / `[[project_instance-optimize-cpu-plan]]`). Doc-gap: no worked `ec2:Attribute` example exists for `ModifyHosts` — confirm the exact attribute-name token the request populates.

**Doc evidence:** `list_ec2.md:8757-8763` (ModifyHosts keys), `:4651-4658` (AllocateHosts keys), `:9896` (dedicated-host resource keys incl. `ec2:HostRecovery`/`ec2:AutoPlacement`), `:10044` (`ec2:HostRecovery` definition); `API_ModifyHosts.md` (five mutable attributes); `dedicated-hosts-maintenance-configuring.md` (disable→28-day terminate).
**Severity-if-true:** **Medium** — AWS-owned IAM governance/hardening gap (org cannot durably enforce resilience/compliance posture; availability-affecting toggle unguardable by value). Not cross-account. Reportable as an AWS-owned condition-key coverage gap (same family as the confirmed SEV-SNP `AllocateHosts` gap). Case-fail-open on `ec2:Attribute` = Medium.

---

### Area 2 — `ModifyHosts` attribute-multiplex privilege bleed + host IDOR  *(Lens A / X / R)*
**Background.** `ModifyHosts` is a single action multiplexed over five attributes (`AutoPlacement`, `HostMaintenance`, `HostRecovery`, `InstanceFamily`, `InstanceType`). The same shape as the confirmed `ModifyInstanceAttribute` multiplex.

**Security Concern.** A grant of `ec2:ModifyHosts` intended only for one purpose (e.g. re-target `InstanceFamily` when repurposing hardware) also authorizes disabling maintenance/recovery and **turning on `AutoPlacement`** — which silently lets untargeted instance launches land on that host. Scopable only if the operator writes an `ec2:Attribute` condition (and per Area 1 that guard is coarse + potentially case-fail-open).

**High-level Test Scenarios:**
- **Claim:** any AWS-**published/managed** policy that grants `ec2:ModifyHosts` grants it unscoped (no `ec2:Attribute`) → resize-family permission silently includes maintenance/recovery/auto-placement control. → **Oracle:** resolve every managed policy containing `ec2:ModifyHosts` via `iam:GetPolicyVersion` and audit for an accompanying `ec2:Attribute` condition; `SimulatePrincipalPolicy` the policy against a `ModifyHosts(HostMaintenance=off)` request. **Route to Lens R if any AWS-managed policy is over-broad.**
- **Claim (IDOR):** `modify-hosts --host-ids h-<foreign>` mutates another account's host. → **Oracle:** call against a host-id not owned by the caller; expect `AccessDenied`/not-found. Host IDs are structured/opaque (`h-0…`, 17-char) — treat as existence-checked; also test the `DryRunOperation` trap (caller-IAM only, **not** an ownership oracle).
**Doc evidence:** `API_ModifyHosts.md`; `list_ec2.md:8757-8763`; `dedicated-hosts-maintenance-basics.md` (auto-placement retained on replacement).
**Severity-if-true:** unscoped **AWS-published** grant = Medium–High (Lens R, in scope, reportable); customer-authored unscoped grant = Low footgun; cross-account IDOR = Critical (but expected to refute).

---

### Area 3 — "Host in a host resource group can't toggle maintenance" — doc-vs-enforcement  *(Lens U — doc-gap)*
**Background.** `dedicated-hosts-maintenance.html`: *"Host maintenance can't be turned on or off for hosts already within a host resource group. Hosts added to a host resource group retain their host maintenance setting."* Host resource groups are a **License Manager** governance construct.

**Security Concern.** Is that lock enforced by the `ModifyHosts` API / IAM, or only by the EC2 console flow? If the control-plane API accepts `ModifyHosts(HostMaintenance=…)` on a host that is a member of a License-Manager HRG, the documented guarantee is console-only prose — a governance bypass letting a principal change the maintenance posture the HRG/License-Manager policy is meant to fix.

**High-level Test Scenarios:**
- **Claim:** `modify-hosts --host-maintenance on/off` on an HRG-member host returns success (not an `UnsupportedOperation`/validation error). → **Oracle:** place a canary host into an HRG (License Manager), call `modify-hosts --host-maintenance off`; a 200 = doc-vs-enforcement gap. Refute = a clean rejection.
- **Adjacent:** does "hosts added to an HRG retain their setting" mean a host allocated with maintenance `off` keeps it inside an HRG that expects `on` (or vice-versa) → posture drift the HRG cannot correct.
**Doc evidence:** `dedicated-hosts-maintenance.html` Considerations; License Manager host-resource-groups guide (cross-service; requires confirming HRG surface first).
**Severity-if-true:** Low–Medium (governance-prose vs API enforcement gap; owner shared EC2/License-Manager). Mark **doc-gap — confirm HRG surface first.**

---

### Area 4 — Live-migration service-plane boundary  *(Lens V / service plane — HARD STOP, out of scope)*
**Background.** Live migration moves a running instance's **memory, CPU, and networking state** to a *different physical host* within 24h without stop/restart (`dedicated-hosts-maintenance-basics.html`).

**Security Concern (naming only — do NOT probe).** The migration channel, the scrub of the source (degraded) host's memory, and the provenance/sanitization of the replacement hardware drawn from AWS's pool are all **AWS-owned service-plane** properties. A Dedicated Host is single-tenant, so there is no same-host co-tenant to attack; the interesting residue/integrity questions live entirely inside AWS's fleet.
**Oracle / rule:** any observation that reaches the migration plane, AWS-fleet identity, or cross-host memory residue → **stop, preserve evidence, disclose to AWS-Security.** Not a customer-testable surface.
**Severity:** N/A to the hunter (hard stop). Listed so the hunter does not wander into it and mis-scope.

---

### Area 5 — Degradation-triggered billing stop + DH-Reservation transfer  *(billing integrity — expected NULL)*
**Background.** *"As soon as host maintenance is initiated, you are no longer billed for the degraded Dedicated Host. Billing for the replacement… begins only after it enters `available`."* *"If the degraded host had an active Dedicated Host Reservation, it is transferred to the new Dedicated Host."*

**Security Concern & refutation.** A free-compute / billing-evasion path would require the *customer* to (a) trigger or fake degradation and (b) keep usable compute on the non-billed host. But: degradation is **AWS-detected** (not a customer API), and a `permanent-failure` host **cannot launch instances** and its running instances are being migrated off. The reservation transfer is AWS-orchestrated. ⇒ **No customer-drivable exploit** — refute. Residual AWS-owned integrity question (mis-transfer of a reservation to the wrong replacement, or billing-stop without an actual replacement) is an **AWS billing-plane** concern, not customer-exploitable.
**Oracle:** attempt `RunInstances` targeting a `permanent-failure` host → must fail; confirm no API lets a customer move a host to `permanent-failure`.
**Severity:** informational / null.

---

### Area 6 — Reschedule scheduled event (`ModifyInstanceEventStartTime`)  *(Lens A — minor)*
**Background.** Reboot events are reschedulable within 7 days; EBS-stop / instance-store-retire events at 28 days. `reschedule-event.html` + `modify-instance-event-start-time` (`--instance-id`, `--instance-event-id`, `--not-before`).

**Security Concern.** (1) IDOR: is `instance-event-id` bound to the owner's instance, or accepted on existence? (2) Can the forced stop/terminate be deferred *indefinitely*? Doc caps it: reschedule only *up to the event deadline*, only *before start*, not within 5 min of start, and ≥60 min out — so no indefinite deferral. Resource type is `instance*` with `ec2:InstanceID`/`ec2:ResourceTag` keys → ownership-scoped.
**Oracle:** `modify-instance-event-start-time` with a foreign `--instance-id` → expect AccessDenied; try `--not-before` beyond the deadline → expect validation error.
**Severity:** Low (bounded; ownership-scoped). Confirm the event-id↔instance binding.

---

### Area 7 — Replacement host: new ID, retained tags & settings  *(Lens I — minor)*
**Background.** The replacement host gets a **new host ID** but retains Tags, maintenance/recovery settings, auto-placement, host affinity, and the DH-Reservation association (`dedicated-hosts-maintenance-basics.html`).

**Security Concern.** (1) If a customer IAM policy scopes access to a **specific host-id ARN** (`dedicated-host/h-XXXX`), the replacement host (new ID) falls outside that statement → a permission/deny that was pinned to the old ID silently stops applying (same owner, so more a stale-scope footgun than cross-tenant). (2) Tag-fidelity: if ABAC/cost-allocation/SCP keys on a tag, does the replacement copy **all** tags faithfully (including any security-relevant tag)? A dropped tag on the replacement could open or close an ABAC gate unexpectedly.
**Oracle:** allocate a canary host, tag it (incl. an ABAC-relevant key), pin a policy to its host-id ARN, then compare against the tag/ARN behavior expected on a new-ID replacement (can only be fully tested if a maintenance event is simulated by AWS — mark doc-gap for the replacement path).
**Severity:** Low (same-account governance hygiene). Mark **doc-gap — replacement path not customer-triggerable.**

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Org cannot deny `HostMaintenance=off` / `HostRecovery=off` by value | `ec2:ModifyHosts` IAM | *(none — no `ec2:HostMaintenance` key; `ec2:HostRecovery` not in ModifyHosts set)* — Area 1 |
| Allocate-time posture guard reversed post-allocation | `AllocateHosts` vs `ModifyHosts` | `ec2:HostRecovery`/`ec2:AutoPlacement` on AllocateHosts only — Area 1 |
| `ec2:Attribute` guard fails open under casing | `ModifyHosts` | `ec2:Attribute`/`ec2:Attribute/${AttributeName}` (must be authored; case-sensitivity untested) — Area 1/2 |
| Multiplexed grant leaks maintenance/auto-placement control | `ec2:ModifyHosts` | `ec2:Attribute` scoping (operator-authored) — Area 2 |
| AWS-managed policy grants `ec2:ModifyHosts` unscoped | managed policies | audit via `GetPolicyVersion` — Area 2 (Lens R) |
| HRG maintenance-lock is console-only prose | License Manager HRG + `ModifyHosts` | doc claim "can't be turned on/off" — Area 3 |
| Cross-account host / event IDOR | `ModifyHosts`, `ModifyInstanceEventStartTime` | `dedicated-host*` / `instance*` resource ownership, `ec2:InstanceID` — Area 2/6 |
| Live-migration memory/state integrity | AWS fleet | **service plane — hard stop** — Area 4 |
| Billing-stop / reservation-transfer abuse | billing plane | degradation AWS-detected; `permanent-failure` can't launch — Area 5 |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **AWS live-migration fleet / migration channel / source-host memory scrub / replacement-hardware provenance** — AWS service plane; hard stop (Area 4).
- **Dedicated Host is single-tenant** — no same-host cross-tenant memory/side-channel target exists at the customer layer.
- **Billing-plane integrity of the reservation transfer / degradation-triggered billing stop** — AWS-owned; not customer-drivable (Area 5).
- **Customer-authored** over-broad `ec2:ModifyHosts` grants — least-privilege footgun (out of scope) *unless* the over-broad grant ships in an **AWS-managed/AWS-published** policy (then Area 2 / Lens R, in scope).
- **Inability to trigger degradation** — there is no customer API to move a host to `permanent-failure`; DoS/free-compute via forced maintenance is not a customer primitive.
- SigV2/transport-downgrade (Lens Y), SSRF (G), file upload (Q), prompt injection (K), OAuth (J), attestation (W) — see §8 null hypotheses.

---

## 8. Null Hypotheses / Doc Gaps
- **Lens G (SSRF) — NULL.** Read all three maintenance pages + configuring. No field the service dereferences (no URL/URI/host/webhook/logo/import). Host maintenance takes only enum toggles and IDs.
- **Lens Q (upload) — NULL.** No file/blob/image input on this surface.
- **Lens K / F (LLM / translation-injection) — NULL.** No parser, LLM, or wire-protocol translation; inputs are booleans/enums/resource-IDs.
- **Lens J (OAuth/3P) — NULL.** No 3P integration on this feature.
- **Lens W (attestation) — NULL.** No attestation-conditioned authz here.
- **Lens Y (transport/signature) — NULL for this page.** Control-plane SigV4 only; SigV2-downgrade is a corpus-wide EC2 Query-API question, not specific to host maintenance (see `[[project_ec2-api-intro-plan]]`).
- **Lens AA (share/revoke) — NULL.** Host maintenance is not a cross-account share. License release on host release (`dedicated-hosts-maintenance.html`) is License-Manager accounting, AWS-orchestrated.
- **Lens C/B (PassRole/credential-vending) — NULL.** No role ARN is passed to this feature; migration is performed by the AWS fleet, not a customer-supplied role.
- **Doc gaps to confirm before hunting:** (a) exact attribute-name token `ModifyHosts` populates into `ec2:Attribute` (needed for Area 1 case-fail-open test — no worked example in docs); (b) whether the HRG maintenance-lock (Area 3) is API- or console-enforced (License Manager surface must be read first); (c) the new-ID replacement host's tag/ARN behavior (Area 7) is only observable through an AWS-driven maintenance event, not a customer API.

---

## Completion Report
- **Assigned skill:** `/work/.claude/skills/security-questionbuilder` (security-questionbuilder).
- **Target:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance.html (+ `-basics`, `-configuring` sub-pages).
- **Inputs read:** the 3 target pages (offline + live — identical, no injected agent block); `list_ec2.md` (ModifyHosts / AllocateHosts / ModifyInstanceEventStartTime / dedicated-host & host-reservation resource keys); `API_ModifyHosts.md`; sibling `dedicated-hosts-recovery-enable.md`, `dedicated-hosts-billing.md`, `reschedule-event.md`.
- **Result:** documentation-derived research plan produced (7 focus areas, boundary map, API inventory, threat-model table, null hypotheses).
- **Crown jewel:** Area 1 — no `ec2:HostMaintenance` condition key exists, and `ModifyHosts` lacks the value-scoping keys (`ec2:HostRecovery`/`ec2:AutoPlacement`) that `AllocateHosts` has → an org cannot durably enforce DH resilience posture; allocate-time guards are reversible post-allocation with no value-scoped IAM control (same family as the confirmed SEV-SNP `AllocateHosts` gap). Doc-confirmed; needs live IAM-simulation to close the `ec2:Attribute` case-fail-open sub-question.
- **Could not fully test (recommend follow-up):** live `iam:SimulateCustomPolicy` on the inert-Deny and `ec2:Attribute` casing questions (Area 1); License-Manager HRG API-vs-console enforcement (Area 3); replacement-host tag/ARN fidelity, which is not customer-triggerable (Area 7). Route to `aws-vuln-hunter` with a throwaway Dedicated Host as canary.
