# Verify that an EC2 instance is enabled for NitroTPM — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/verify-nitrotpm-support-on-instance.html` (= `.md` twin; offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/verify-nitrotpm-support-on-instance.md`), cross-checked against the Service Authorization Reference `list_ec2.md` (pulled live 2026-10-15, 35,512 HTML lines), the EC2 API Reference (`API_DescribeInstances`, `API_Instance`, `API_GetInstanceTpmEkPub`), and the sibling NitroTPM plans. **Status: documentation-derived hypotheses only; nothing tested against a live account.** Offline == online byte-identical 2026-10-15.

> This plan is the **INSTANCE-side READ/VERIFY-surface COMPLEMENT** of the NitroTPM cluster — the twin of `verify-nitrotpm-support-on-ami-attack-research-plan.md` (which owns the *AMI*-side `DescribeImages` read path). It is scoped to the single page `verify-nitrotpm-support-on-instance.html` and deliberately does **not** restate its siblings — it cross-references them:
> - **`verify-nitrotpm-support-on-ami-attack-research-plan.md`** — the AMI-side twin. Owns `DescribeImages`-unscopable-cross-account-read, the `DescribeImageAttribute` "owner-only" prose-vs-API gap, the `tpm-support`-filter-ABSENT-from-`API_DescribeImages` defect, and the whoAMI self-asserted-flag chain. **This instance plan is the mirror case: `DescribeInstances` is unscopable too, but instances are account-scoped (intra-account only), and the `tpm-support` filter here is PRESENT, not absent.**
> - **`nitrotpm-attack-research-plan.md`** (hub complement) — owns `GetInstanceTpmEkPub` (EK pubkey as per-instance identifier), `RegisterImage --tpm-support v2.0` enablement, BitLocker sealing, cross-acct AMI share. This plan cross-refs `GetInstanceTpmEkPub` only as the **scopable twin** of the unscopable `DescribeInstances` (Area 2); it does NOT re-develop the EK-tracking surface.
> - **`nitrotpm-attestation-attack-research-plan.md`** — owns KMS/PCR/replay/COSE/attestation-gate depth. The "verify = read a self-asserted flag, not an attestation" theme (Area 3) defers all real attestation mechanics there.
> - **`enable-nitrotpm-prerequisites-attack-research-plan.md`** / **`enable-nitrotpm-support-on-ami-attack-research-plan.md`** — own launch-prerequisite IAM-inexpressibility and the enablement runbook.
> - All children of **`ec2-security-hub-plan-note`** (NitroTPM = Area 2 of the EC2 Security chapter).
>
> **Net-new surface owned here:** (1) the **instance-side** read-path scopability facts (`DescribeInstances` unscopable + account-scoped; the `tpm-support` filter PRESENT); (2) the **Lens-X parity asymmetry** between the scopable `GetInstanceTpmEkPub` and the unscopable `DescribeInstances` reading the same NitroTPM posture; (3) the **Windows `tpm.msc` guest-OS verification path** — a verification surface the AMI page has no equivalent for; (4) the instance-level **console blind spot** (this page is the authoritative source cited by the AMI plan's Area 5).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The two safe first oracles here are **read-only and resource-free**: `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (settles every condition-key-scopability claim with no resource created), and a plain `describe-instances` read against a **synthetic self-owned canary instance** (one NitroTPM-enabled, one not). No instance belonging to another account is ever touched; `tpm.msc` is run only on a canary Windows instance the tester owns.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected on this read-only page.)

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Read the NitroTPM-enablement fact (`TpmSupport=v2.0`) of instances the caller is not meant to see** — specifically, instances owned by *another team in the same account* whose `TpmSupport`/metadata an admin tried to gate with ABAC — via the **IAM-unscopable** `DescribeInstances` path (the page's primary verify command).
2. **Prove an admin cannot restrict `TpmSupport` visibility at the instance level**: show that `DescribeInstances` (the command the page tells you to use) carries **no resource-type and no tag condition key**, so any `ec2:ResourceTag`/`aws:ResourceTag`-keyed Deny attached to it is inert — while the *adjacent* instance-level TPM read `GetInstanceTpmEkPub` **is** fully scopable, creating a false sense that TPM posture is locked down.
3. **Enumerate every NitroTPM-enabled instance in the account** with the server-side `tpm-support` filter (confirmed present on `DescribeInstances`), unscopably, as a recon oracle for targeting attestation/BitLocker-dependent workloads.
4. **Show "verify" is not assurance** — that instance-level verification reads a `TpmSupport` value **inherited at launch from a self-declared AMI `RegisterImage` flag**, with no attestation that a functioning, uncompromised TPM is present (whoAMI chain, deferred to the AMI/attestation siblings).
5. **Characterize the Windows `tpm.msc` guest path and the console blind spot** — confirm that control-plane verification is API-only (console hides `TpmSupport`), and that the guest-OS `tpm.msc` check reads a manufacturer string with no cryptographic binding and leaves no control-plane / CloudTrail record.

---

## 2. Components, Assets, and Design

**Interface.** Read-only EC2 control-plane APIs over SigV4 HTTPS, plus one guest-OS (Windows MMC snap-in) local check. Three documented verification surfaces:

| Surface | Underlying mechanism | What it returns re: NitroTPM | Page framing |
|---|---|---|---|
| `describe-instances --instance-ids <id> --query Reservations[].Instances[].TpmSupport` | `ec2:DescribeInstances` | `TpmSupport` string (`"v2.0"` or field absent) inside `Reservations[].Instances[]` | **Primary** verify command (CLI) |
| `(Get-EC2Instance -InstanceId <id>).Instances.TpmSupport` | `ec2:DescribeInstances` | same, via Tools-for-PowerShell | PowerShell equivalent |
| `tpm.msc` → **TPM Manufacturer Information** field | Guest-OS MMC snap-in; **no API, no IAM** | manufacturer name + NitroTPM version string | **Windows instances only**, in-guest |

**Not on this page but adjacent (cross-ref only):** the server-side **`tpm-support` filter** (`describe-instances --filters Name=tpm-support,Values=v2.0`) — *not* shown on the page (the page uses client-side `--query`), but confirmed present in `API_DescribeInstances` and reachable via the same `ec2:DescribeInstances` action.

**Asset under contention.** The `TpmSupport` instance attribute — a per-instance metadata string whose only legal value is `v2.0`. Confirmed in `API_Instance.md` ("`tpmSupport` — If the instance is configured for NitroTPM support, the value is `v2.0`.") with **no owner/attestation caveat**. It is **set at launch** (inherited from the AMI's `TpmSupport`, which is itself set once at `RegisterImage` and immutable — see the AMI siblings) and is **invisible in the EC2 console** (page: "The Amazon EC2 console does not display the `TpmSupport` field.").

**Identifier shape.** `i-<17 hex>` — not fabricable blind. Critically, `DescribeInstances` returns **only instances in the caller's own account** — there is no cross-account instance read. So, unlike the AMI twin (public/shared AMIs cross the account boundary), the instance oracle is **intra-account only**: its targets are instances owned by other principals/teams *within the same account*, discoverable via `DescribeInstances` itself (no prior id knowledge needed).

**Trust zones.** (a) Within one account: principal/team A ↔ principal/team B instances (the ABAC/least-privilege boundary an admin tries to draw with tags). (b) AMI owner ↔ instance launcher (the `TpmSupport` value is inherited across this boundary at launch — the whoAMI seam). (c) Guest OS ↔ Nitro hypervisor (the `tpm.msc` manufacturer string is asserted by the virtual device, not attested).

```
   RegisterImage --tpm-support v2.0   (AMI owner, self-asserted; no attestation)
            │  (AMI.TpmSupport = "v2.0", immutable — see AMI siblings)
            ▼
   RunInstances  ──inherits──►  Instance.TpmSupport = "v2.0"  (console-hidden)
                                        │
          ┌─────────────────────────────┼──────────────────────────────┐
          ▼                             ▼                               ▼
  describe-instances            describe-instances              tpm.msc  (in-guest,
   --query ...TpmSupport         --filters tpm-support           Windows only; reads
   [ec2:DescribeInstances        [same action; account-wide      "TPM Manufacturer
    UNSCOPABLE: region-only,      NitroTPM-instance enum]         Information" string;
    no resource type, no tag]                                     NO IAM, NO CloudTrail]
          │
   (contrast) GetInstanceTpmEkPub  [SCOPABLE: instance* + ec2:InstanceID + tags + ~20 keys]
                                   = the locked-down instance-TPM read the admin CAN gate
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2:DescribeInstances` | GET (SigV4) | Existing | **Non-mutating** | External | Returns instance metadata incl. `TpmSupport`; supports server-side `tpm-support` **filter** | Yes | Any principal allowed `ec2:DescribeInstances` in the account | **Blank resource type + ONLY `ec2:Region` (`list_ec2.md`, access level List)** → IAM-unscopable; account-scoped (own account only) |
| `ec2:GetInstanceTpmEkPub` | POST (SigV4) | Existing | Non-mutating | External | Returns the instance's NitroTPM EK public key | Yes | Scopable per-instance | **`instance*` required + ~20 condition keys** incl. `ec2:InstanceID`, `aws:ResourceTag/${k}`, `ec2:ResourceTag/${k}`, `ec2:InstanceType`, `ec2:Tenancy` (access level Read) → the **scopable twin** (Area 2). Owned by `nitrotpm-attack-research-plan.md`; referenced here only for parity |
| `tpm.msc` (Windows MMC) | — (guest-OS) | Existing | Non-mutating | **Internal to guest** | Shows TPM Manufacturer Information | No (requires instance login) | Anyone with Windows session on the instance | No IAM, no API, no CloudTrail; manufacturer-string assertion, not attestation |

**Console-hidden knob:** the page itself documents one — `TpmSupport` is accepted/returned by the API/CLI but **not surfaced in the EC2 console**. The server-side `tpm-support` *filter* is a second console/prose-hidden knob (present in `API_DescribeInstances` but not shown on this verification page).

---

## 4. Boundary-Lens Catalog — firing lenses

### AREA 1 — `DescribeInstances` is the primary verify command and is IAM-unscopable (Lens X / U / S / A) — HEADLINE
**Background.** The page's primary (and only CLI/PowerShell) verification command is `aws ec2 describe-instances … --query …TpmSupport`. `list_ec2.md` shows `DescribeInstances` with a **blank resource-type cell and `ec2:Region` as its only condition key** (access level List) — confirmed by direct read of the action block. There is **no `instance*` resource type, no `aws:ResourceTag`/`ec2:ResourceTag`, no `ec2:InstanceID`** on this action.

**Security Concern.** An admin who wants to restrict which principals can read instance NitroTPM posture (e.g. an ABAC policy `Deny ec2:DescribeInstances unless ec2:ResourceTag/team = ${aws:PrincipalTag/team}`) **cannot** — the key is not wired to the action, so the Deny is **inert / fails open** (vacuously, the condition never matches a resource the action is scoped to). Any principal holding `ec2:DescribeInstances` reads `TpmSupport` for **every instance in the account**. This is the same unscopable-read-oracle shape as `DescribeImages` (AMI twin), `DescribeKeyPairs` ([[describe-keys-plan-note]]), and `manage-spot-fleet`'s `DescribeSpotFleetRequests`.

**Scope distinction (lowers severity vs the AMI twin).** `DescribeInstances` returns **only the caller's own account's instances** — there is no public/shared/cross-account instance catalog. So this is an **intra-account cross-team** disclosure + inert-ABAC footgun, **not** the cross-account read that made the AMI twin's `DescribeImages` headline High. Do not over-claim cross-tenant here.

**High-level Test Scenarios.**
- Claim: *A principal denied instance-metadata visibility by an `ec2:ResourceTag`-keyed policy can still read any instance's `TpmSupport`.* → Oracle: `iam:SimulateCustomPolicy` with `ec2:DescribeInstances` + a `Deny` conditioned on `ec2:ResourceTag/team` returns **Allow** (the condition is inert because the action has no such key); confirm live with a scoped canary role reading a differently-tagged canary instance's `TpmSupport`. → Severity: **Low–Medium** (intra-account info disclosure + AWS-schema inert-ABAC fact).
- Claim: *`DescribeInstances` cannot be restricted to a subset of instances at all for this read.* → Oracle: show `list_ec2` lists no `instance` resource type on the action; a `Resource` ARN other than `*` in an Allow on `ec2:DescribeInstances` is rejected/ignored. → Severity: Informational (AWS-owned schema fact; feeds the parity finding in Area 2).

**Doc evidence.** `list_ec2.md` `DescribeInstances` block (resource type blank; condition keys = `ec2:Region` only; access level List). Page: `describe-instances … --query Reservations[].Instances[].TpmSupport`.

---

### AREA 2 — Scopability parity asymmetry: `GetInstanceTpmEkPub` (scopable) vs `DescribeInstances` (unscopable) read the same NitroTPM posture (Lens X / U) — HIGHEST NET-NEW VALUE
**Background.** Two instance-level reads expose NitroTPM state. `GetInstanceTpmEkPub` (reads the TPM endorsement-key pubkey) **requires `instance*`** and carries ~20 condition keys — `ec2:InstanceID`, `aws:ResourceTag/${k}`, `ec2:ResourceTag/${k}`, `ec2:InstanceType`, `ec2:Tenancy`, `ec2:AvailabilityZone`, etc. (confirmed in `list_ec2.md`, access level Read). `DescribeInstances` (reads the `TpmSupport` *enablement flag*) carries **none** of those (Area 1).

**Security Concern.** This is a **twin-divergence (Lens X)**: an admin who hardens the *obviously sensitive* TPM read (`GetInstanceTpmEkPub` — "that's the crypto identity, lock it to the owning team by tag/instance-id") reasonably believes NitroTPM posture is gated. But the **enablement fact itself** (`TpmSupport=v2.0` — which instances even have a TPM, i.e. which run attestation/BitLocker-dependent workloads) leaks through the **un-scopable `DescribeInstances`**, which the verification page actively tells operators to use. The security-sensitive signal (target selection: *which* instances to attack for their sealed secrets) is readable on the path the admin could not fence, while the less-actionable signal (the pubkey) is on the path they did fence. The guarantee a careful operator infers from `GetInstanceTpmEkPub`'s rich key set — "I can restrict who sees my instances' TPM" — is **false for `TpmSupport`**.

**High-level Test Scenarios.**
- Claim: *A scoped role denied `GetInstanceTpmEkPub` on team-B instances can still enumerate team-B instances' `TpmSupport` via `DescribeInstances`.* → Oracle: `iam:SimulateCustomPolicy` shows `GetInstanceTpmEkPub` Deny (keyed on `ec2:ResourceTag`) correctly denies, while `DescribeInstances` Allow returns the same instances' `TpmSupport`; confirm live on canary instances. → Severity: **Medium** (defense-in-depth / false-assurance gap; AWS-owned schema asymmetry → reportable as a Lens-U doc/enforcement inconsistency, not a product break).
- Claim: *No condition key anywhere lets an admin restrict `TpmSupport` reads to instance owners.* → Oracle: grep `list_ec2` — no action returning `TpmSupport` carries `instance*`/`ec2:InstanceID`/tag keys (only `DescribeInstances`, which returns it, is unscopable). → Severity: Informational.

**Doc evidence.** `list_ec2.md`: `GetInstanceTpmEkPub` (`instance*` + ~20 keys) vs `DescribeInstances` (`ec2:Region` only). `API_Instance.md` `tpmSupport` field (no owner caveat). Cross-ref `nitrotpm-attack-research-plan.md` (owns the EK-identity surface).

---

### AREA 3 — The server-side `tpm-support` filter enables unscopable account-wide NitroTPM-instance enumeration (Lens U / A — recon oracle)
**Background.** The page uses client-side `--query` on `TpmSupport`, but `API_DescribeInstances.md` confirms a **server-side filter `tpm-support` — "Indicates if the instance is configured for NitroTPM support (`v2.0`)."** This is reachable via the same unscopable `ec2:DescribeInstances` action. **Mirror-case to the AMI twin:** the AMI plan's Area 3 found the `tpm-support` filter **ABSENT** from `API_DescribeImages` (a doc defect); here it is **PRESENT** on `DescribeInstances` — the opposite integrity state, worth recording so the hunter does not inherit the AMI plan's "filter missing" assumption.

**Security Concern.** `describe-instances --filters Name=tpm-support,Values=v2.0 --query 'Reservations[].Instances[].InstanceId'` returns, in one unscopable call, the id list of **every NitroTPM-enabled instance in the account** — a precise target list for workloads that rely on measured boot / BitLocker sealing / attestation-gated KMS. No instance-id knowledge is needed up front, and (Area 1) no tag/ABAC Deny can trim the result.

**High-level Test Scenarios.**
- Claim: *A low-privilege principal can produce a complete account-wide inventory of NitroTPM instances despite tag-based segmentation.* → Oracle: run the filtered `describe-instances` under a scoped canary role; confirm it returns instances tagged for other teams. → Severity: **Low–Medium** (intra-account recon amplifier; raises severity of any later cross-team lateral-movement chain).

**Doc evidence.** `API_DescribeInstances.md` filter list (`tpm-support`). Page command (client-side `--query`). Contrast: `verify-nitrotpm-support-on-ami-attack-research-plan.md` Area 3.

---

### AREA 4 — "Verify" reads a launch-inherited, self-asserted flag — not an attestation (Lens U / W / EE — whoAMI chain)
**Background.** Instance `TpmSupport` is **inherited at launch from the AMI's `TpmSupport`**, which is a value the AMI publisher set once with `RegisterImage --tpm-support v2.0` and which carries **no attestation** that a functioning, uncompromised TPM is present (`API_Instance.md` and `API_DescribeImages` return the string with no owner/attestation caveat). The page's verb is "verify," but the operation is "read a flag."

**Security Concern.** A consumer who launches a shared/community AMI and "verifies NitroTPM" on the resulting instance is **trusting the AMI publisher's self-declaration**, transitively — exactly the whoAMI name-confusion seam. The instance-level verify adds no assurance over the AMI-level verify; it reflects the same self-asserted bit one hop later. "Verify NitroTPM is enabled" ≠ "a trustworthy TPM will attest this instance."

**High-level Test Scenarios.**
- Claim: *An instance launched from an untrusted AMI reports `TpmSupport=v2.0` with no signal distinguishing a genuine vs. a publisher-asserted TPM.* → Oracle: launch a canary from a self-registered AMI with `--tpm-support v2.0`; `describe-instances` reports `v2.0` with no attestation field — identical output to a trusted AMI. → Severity: **Low** on this page (the real attestation break lives in `nitrotpm-attestation-attack-research-plan.md`; this is the "verification ≠ attestation" doc-clarity lead). 

**Defers to:** `nitrotpm-attestation-attack-research-plan.md` (PCR/KMS attestation gate), `nitrotpm-attack-research-plan.md` (whoAMI Windows name-filter, `RegisterImage` self-assert), `verify-nitrotpm-support-on-ami-attack-research-plan.md` Area 4. **Do not re-develop attestation mechanics here.**

**Doc evidence.** `API_Instance.md` `tpmSupport`; AMI siblings for the `RegisterImage` self-assert.

---

### AREA 5 — Windows `tpm.msc` guest-OS verification: manufacturer string ≠ attestation; no control-plane record (Lens U / O / F — NET-NEW, no AMI-page analogue)
**Background.** The page's second half ("Verify NitroTPM access on your Windows instance") is a **guest-OS** procedure with no AWS API: log into the instance, run `tpm.msc`, read the **TPM Manufacturer Information** field for the manufacturer name + NitroTPM version. This surface **does not exist on the AMI verification page** — it is unique to the instance page.

**Security Concern.**
- (Lens U) The guest check reads a **manufacturer/version string asserted by the virtual TPM device** — it confirms the OS can *see* a TPM, not that the TPM is genuine, uncompromised, or cryptographically bound to this instance. It is weaker assurance than the (already weak) control-plane flag, and an operator may over-trust a reassuring MMC window.
- (Lens O) The guest-side `tpm.msc` check produces **no CloudTrail / control-plane event** — a NitroTPM "verification" performed this way is invisible to an account auditor, and conversely a defender watching CloudTrail sees nothing. (The control-plane `DescribeInstances` path *is* logged; `tpm.msc` is not.)
- (Lens F, low) The manufacturer-info string is attacker-influenceable only from inside the guest (requires an existing session), so it is a **self-trust** concern, not a cross-boundary injection — note and bound it, do not inflate.

**High-level Test Scenarios.**
- Claim: *A compromised or mis-provisioned guest can display a plausible TPM Manufacturer Information string that an operator treats as proof of a healthy NitroTPM.* → Oracle (bounded, canary only): on a tester-owned Windows canary, confirm `tpm.msc` reads device-reported strings with no cryptographic verification path exposed in the UI. → Severity: **Informational–Low** (guest-side assurance-clarity; no cross-tenant primitive).
- Claim: *Instance NitroTPM verification via `tpm.msc` leaves no account-level audit record.* → Oracle: perform the guest check, confirm absence of a corresponding CloudTrail event. → Severity: **Informational** (audit blind spot; raises severity only as an enabler).

**Doc evidence.** Page §"Verify NitroTPM access on your Windows instance" (steps 1–3, `tpm.msc`, "TPM Manufacturer Information"). `connecting_to_windows_instance.md` (prerequisite).

---

### AREA 6 — Instance-level console blind spot (Lens O / U — authoritative source for the AMI plan's Area 5)
**Background.** Page: "The Amazon EC2 console does not display the `TpmSupport` field." This page is the **source citation** behind the AMI plan's Area 5 ("console blind spot confirmed at AMI *and instance* level").

**Security Concern.** NitroTPM enablement for a *running instance* is verifiable **only** via API/CLI/PowerShell (control plane) or `tpm.msc` (guest). A console-only operator or a console-scoped auditor **cannot see** which instances are NitroTPM-enabled, so a compliance posture built on console review has a blind spot; conversely, API-only visibility means tag-based ABAC (which doesn't work on `DescribeInstances`, Area 1) is the *only* lever an admin has, and it fails open.

**High-level Test Scenarios.**
- Claim: *An operator restricted to the console cannot determine instance NitroTPM status, forcing reliance on the unscopable `DescribeInstances`.* → Oracle: confirm the console surfaces no `TpmSupport`; the only programmatic path is the Area 1 action. → Severity: **Informational** (operational/assurance gap). 
- **Open doc-gap (needs live check):** does **AWS Config** / **Resource Explorer** / **Systems Manager Inventory** surface `TpmSupport`? If none do, the console blind spot is total for non-API auditors. (Carried from the AMI plan's Area 5 as the sole remaining doc-gap; still unresolved — settle with a live read of the Config `AWS::EC2::Instance` resource schema.)

**Doc evidence.** Page line 10 (console blind spot). Cross-ref `verify-nitrotpm-support-on-ami-attack-research-plan.md` Area 5.

---

## 5. Recommended Areas of Focus (priority order)
1. **Area 2** — scopability parity asymmetry (`GetInstanceTpmEkPub` scopable vs `DescribeInstances` unscopable). Highest net-new value; AWS-owned Lens-U/X inconsistency; settles with `iam:SimulateCustomPolicy` (no resource).
2. **Area 1** — `DescribeInstances` unscopable + inert-ABAC. Foundational; intra-account only (lower sev than AMI twin). 
3. **Area 3** — `tpm-support` filter present → account-wide enumeration oracle (recon amplifier; corrects the AMI plan's "filter absent" into "present here").
4. **Area 5** — Windows `tpm.msc` guest path (unique to this page; assurance + audit-blind-spot clarity).
5. **Area 4** — verify-≠-attestation (defer depth to attestation/AMI siblings).
6. **Area 6** — instance console blind spot + Config/Resource-Explorer doc-gap.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Intra-account cross-team read of any instance's `TpmSupport` despite ABAC | `ec2:DescribeInstances` | Tag/ownership condition keys — **absent on the action (inert)** |
| Admin hardens EK read but `TpmSupport` leaks via unscoped Describe | `GetInstanceTpmEkPub` vs `DescribeInstances` | `instance*`+tag scoping exists on one twin, not the other |
| Account-wide NitroTPM-instance inventory | `describe-instances --filters tpm-support` | None (unscopable action + server-side filter) |
| Over-trusting a self-asserted / launch-inherited `TpmSupport` | AMI→instance inheritance; `tpm.msc` string | None on this page (attestation lives elsewhere) |
| NitroTPM verification invisible to CloudTrail / console auditor | `tpm.msc` guest check; console | Control-plane logging covers `DescribeInstances` only; `tpm.msc` unlogged; console hides the field |

---

## 7. Out-of-Scope Risk Categories
- **Cross-account instance read** — `DescribeInstances` is account-scoped; there is no public/shared instance catalog. The cross-account angle belongs to the AMI twin (`DescribeImages` on public AMIs), not here. Treat any apparent cross-account instance read as a HARD-STOP service-plane signal, not an expected finding.
- **Attestation / PCR / KMS-RecipientAttestation mechanics** — owned by `nitrotpm-attestation-attack-research-plan.md`.
- **`GetInstanceTpmEkPub` EK-as-identifier tracking, `RegisterImage` enablement, whoAMI name-confusion, BitLocker sealing** — owned by `nitrotpm-attack-research-plan.md` / the enable-* siblings.
- **Guest-OS exploitation of the Windows TPM stack** (BitLocker, VBS, measured boot internals) — customer-OS surface, out of scope except as the "assurance ≠ attestation" clarity lead (Area 5).
- **IMDS on managed hosts, product/feature-parity gaps, single-tenant self-DoS.**

---

## 8. Null hypotheses / doc gaps
- **Lens A cross-tenant IDOR — NULL (strong):** `DescribeInstances` returns only own-account instances; `i-<17 hex>` is not blind-fabricable; no cross-account instance path exists. The only live oracle is intra-account (Areas 1–3).
- **Lens B/C/D/H/J/M/N/Q/Y/BB/CC/DD/FF — N/A:** read-only page with two Describe-backed commands + one guest MMC check. No role ARN / PassRole, no credential vending, no control-plane escape, no KMS field, no OAuth, no session id, no namespace migration, no upload/URL the service dereferences, no TLS/sig knob, no multi-parser routing, no upstream-context header, no cache layer, no JWT. (Pages checked: the target page in full + `API_DescribeInstances`/`API_Instance`/`API_GetInstanceTpmEkPub` + `list_ec2` `DescribeInstances`/`GetInstanceTpmEkPub` rows.)
- **Lens G SSRF — N/A:** no field on this page is dereferenced server-side (the only URLs are the embedded `tpm-1.png` doc asset and intra-doc links; `--instance-ids` is an identifier, not a fetched URL).
- **Lens L DoS — N/A:** no parser/upload/size limit introduced; `DescribeInstances` is a standard paginated read.
- **Lens R/S IAM-artifact — N/A on this page:** no policy JSON / managed policy / CFN / runbook block printed here (the inert-ABAC *fact* about `DescribeInstances` is a Lens-U/X schema finding, Areas 1–2, not an artifact audit).
- **Open doc-gap (carried):** does **AWS Config `AWS::EC2::Instance`** / **Resource Explorer** / **SSM Inventory** expose `TpmSupport`? If not, Area 6's console blind spot is complete for non-API auditors. Settle with a live read of the Config resource schema before investing. (Same gap the AMI plan carried; still unresolved 2026-10-15.)
- **Mirror integrity:** offline `.md` == online `.md` byte-identical 2026-10-15. The `tpm-support` filter is **present** in `API_DescribeInstances` (contrast the AMI plan's finding that it is absent from `API_DescribeImages`).

---

*Cross-references: [[verify-nitrotpm-plan-note]] (AMI twin), [[nitrotpm-plan-note]] (hub), [[ec2-security-hub-plan-note]] (chapter), [[project-aws-research-plans]] (convention), [[reference-aws-iam-service-auth-ref-url]] (list_ec2 fetch technique).*
