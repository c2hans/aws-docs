# NitroTPM (device, EK, AMI-enablement & sealing) — Attack Research Plan

> **Scope split — read this first.** This plan is the **COMPLEMENT** to the existing
> `nitrotpm-attestation-attack-research-plan.md` (same directory). That plan owns everything
> *attestation*: the Attestation Document, COSE_Sign1 signing, KMS `kms:RecipientAttestation:NitroTPMPCR*`
> conditioned key policies, PCR under-binding, replay/freshness, CRL/alg-pinning, enclave-vs-NitroTPM
> key-family confusion. **This plan deliberately does NOT re-derive any of that.** It owns the
> *rest* of the NitroTPM hub (`nitrotpm.html`) surface that the attestation plan leaves open:
> the **Endorsement Key retrieval API** (identity/privacy/IDOR), the **AMI-enablement supply chain**
> (`RegisterImage --tpm-support`), the **Windows preconfigured-AMI discovery path** (whoAMI land-grab),
> the **BitLocker sealing "original instance only" guarantee** and **state non-portability**,
> **verification/console blind spots**, and **cross-account AMI sharing** of a TpmSupport image.
> Where a lead touches the attestation boundary, it is marked **→ DEFER to attestation plan** and
> only the hand-off is recorded here.

Source of leads: hub `nitrotpm.html` + 6 children (`enable-nitrotpm-prerequisites.html`,
`enable-nitrotpm-support-on-ami.html`, `verify-nitrotpm-support-on-ami.html`, `nitrotpm-instance.html`,
`verify-nitrotpm-support-on-instance.html`, `retrieve-ekpub.html`), the API reference
`API_GetInstanceTpmEkPub.html`, the Windows AMI reference `windows-ami-reference/ami-windows-tpm.html`,
the SSM public-parameters page, and the IAM Service Authorization Reference
`service-authorization/.../list_ec2` (authoritative over User-Guide prose). Online `.html.md` twins
were fetched this session; where offline/online or doc-vs-reference drift exists it is called out.
Status: **documentation-derived hypotheses only; nothing tested against a live account.**

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity.**
  Work in priority order (§5); look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own
  Nitro service plane (hypervisor signing material, internal attestation PKI, host-level TPM backing
  store), stop, preserve evidence, flag for AWS-Security disclosure. Do not exploit beyond existence.
- **Dummy/synthetic data only.** EK reads are non-mutating; AMI register/share and BitLocker tests are
  mutating — use throwaway AMIs/instances in an account you own; never target another tenant's resource.

## 1. Pentest Objectives
1. Determine whether `GetInstanceTpmEkPub` enforces **caller-account ownership** of the `InstanceId`,
   or only existence (cross-account EKpub read = IDOR), and whether its error behavior leaks an
   existence oracle.
2. Determine whether the EK — a stable, per-instance identifier — enables **intra-account cross-tenant
   tracking** when a role is granted the action on `Resource:"*"` without the available tag conditions.
3. Determine whether NitroTPM can be turned on by any path other than `RegisterImage --tpm-support v2.0`,
   and whether the enablement decision is **gatable by IAM** (is there a condition key that lets an org
   force or forbid `v2.0`?).
4. Determine whether AWS's documented **Windows preconfigured-AMI discovery pattern** (`TPM-Windows_Server-*`)
   resolves to an attacker-registered look-alike when owner-pinning is dropped (whoAMI-class).
5. Determine whether the **"BitLocker/NitroTPM state is bound to the original instance"** guarantee has
   any documented export/clone/migration path (confidentiality) — and separately whether it is a silent
   **DR/availability footgun** (snapshot restore → permanently unreadable volume).
6. Determine whether **cross-account AMI sharing** of a TpmSupport AMI (via `ModifyImageAttribute`
   launchPermission) propagates the NitroTPM attribute to launchers and whether that is scopable.
7. Catalogue the **console/verification blind spots** (`TpmSupport` not shown in console) as a
   detection-evasion surface.

## 2. Components, Assets, and Design

**Provenance / currency check.** `nitrotpm.html` + the 6 children + `API_GetInstanceTpmEkPub.html` +
`ami-windows-tpm.html` were fetched live (`.html.md`) this session and compared to the offline mirror
and to `list_ec2`. The Windows AMI page's HTML and `.html.md` twin returned **identical** content.
**Key doc-vs-reference finding:** the User-Guide/attestation-plan assertion that
`GetInstanceTpmEkPub` and `RegisterImage` carry **"zero condition keys"** is **FALSE per `list_ec2`** —
see the corrections in §4 Lens A and Lens R/S. This plan treats `list_ec2` as authoritative.

**What this cluster is.** NitroTPM is a per-instance virtual **TPM 2.0** device from the AWS Nitro
System. Beyond attestation (other plan), it provides: a permanent per-instance **Endorsement Key (EK)**
whose public half is retrievable via API; **sealing/unsealing** of secrets to the TPM under a PCR policy
(the headline consumer is **Windows BitLocker** sealing the drive-encryption key); and an **AMI-level
enablement attribute** (`TpmSupport = "v2.0"`) that must be present for an instance to get a vTPM.

**Processes / tooling / planes:**
- **Nitro System (AWS-owned):** backs the vTPM, holds EK private material, enforces that vTPM state is
  bound to the specific instance object. Not customer-reachable. **HARD-STOP zone.**
- **Control-plane APIs (customer-callable):** `GetInstanceTpmEkPub` (read EKpub), `RegisterImage`
  (`--tpm-support v2.0 --boot-mode uefi`, the ONLY enablement path), `DescribeImages`/`DescribeInstances`
  (verify `TpmSupport`), `ModifyImageAttribute` (cross-account AMI share).
- **Guest OS:** Windows BitLocker (seals volume key to the vTPM); tpm2-tools / OpenSSL consume EKpub.
- **Discovery plane:** SSM public parameters under `/aws/service/ami-windows-latest` (owner-authenticated
  by namespace) and `DescribeImages` name-filtering (owner-pinning is caller's responsibility).

**Accounts / trust zones:** customer account (owns instance, AMI, IAM) ↔ AWS Nitro plane (root of trust,
HARD STOP) ↔ **any other AWS account** that can register an AMI or receive a shared AMI (relevant to the
whoAMI discovery path and to cross-account launchPermission sharing).

**What is a "resource" and its identifier shape:**
- **Instance** (`i-` + 17 hex) — resource type `instance*` for `GetInstanceTpmEkPub`. 17-hex entropy makes
  blind enumeration infeasible.
- **AMI** (`ami-…`) — resource type `image*` for `RegisterImage`/`ModifyImageAttribute`; carries the
  immutable `TpmSupport` attribute. **AMI *name* is attacker-choosable and is the whoAMI pivot.**
- **EKpub** — raw public-key material (base64), formats `der` | `tpmt`, types `rsa-2048` | `ecc-sec-p384`.
  **No EK certificate chain is returned** (no manufacturer genuineness proof) — relevant to anyone trying
  to build third-party attestation trust on the EK (→ hand-off to attestation plan).

**Identity establishment:** SigV4 IAM only; no resource-based sharing primitive exists for `instance`
objects (unlike AMIs/snapshots), so instance ownership is account-bound by ARN resolution.

**ASCII pipeline (the non-attestation NitroTPM surface this plan owns):**
```
                         [AWS Nitro plane — HARD STOP]
                          vTPM backing, EK private key
                                   │
   RegisterImage --tpm-support v2.0 --boot-mode uefi   (ONLY enablement path; immutable)
   caller (image*)  ─────────────────────────────────────────►  AMI{TpmSupport=v2.0}
        │                                                             │
        │ ModifyImageAttribute launchPermission (cross-acct share)    │ RunInstances
        ▼                                                             ▼
   other account launches  ─────────────────────────────────►  Instance{vTPM, EKpub}
                                                                  │        │
                       GetInstanceTpmEkPub (instance*) ◄──────────┘        │ BitLocker seal
                       returns EKpub (rsa-2048|ecc-p384)                    ▼
                                                               sealed drive key bound to
                                                               THIS vTPM + PCRs; NOT in
                                                               snapshot / VM-export / console
```

## 3. API / Interface Surface

| Name | Mutating | Resource (list_ec2) | Condition keys (list_ec2) | Callable by | Notes |
|---|---|---|---|---|---|
| `GetInstanceTpmEkPub` | No | `instance*` | `ec2:InstanceID`, `aws:ResourceTag/*`, `ec2:ResourceTag/*`, `ec2:Region`, `ec2:InstanceType`, `ec2:Tenancy` | owner of instance (hyp.) | **CORRECTION:** attestation plan said "zero keys" — false. 2 EK **types** (`rsa-2048`,`ecc-sec-p384`), 2 formats. No EK cert returned. "retrieve at any time" = no running-state gate. |
| `RegisterImage` | Yes | `image*` (+`snapshot`) | image: `aws:RequestTag/*`,`aws:TagKeys`,`ec2:ImageID`,`ec2:Owner`,`ec2:Region`; snapshot: `ec2:SnapshotID`,`ec2:ParentVolume`,`ec2:Owner`… | AMI creator | **CORRECTION:** has condition keys — but **NONE constrain the `TpmSupport` or `BootMode` *value*.** No `ec2:TpmSupport` key exists anywhere. `ec2:BootModeOverride` exists but is a **launch/CreateImage-time** key, absent from RegisterImage. ONLY enablement path (not console, not VM Import/Export). Immutable after register. |
| `DescribeImages` / `DescribeInstances` | No | `image*`/`instance*` | standard | anyone w/ Describe | Only programmatic way to read `TpmSupport`; **console does not show it**. |
| `ModifyImageAttribute` (launchPermission) | Yes | `image*` | `ec2:Attribute`,`ec2:Public`,`ec2:Owner`,`ec2:ImageID`,`ec2:Region` | AMI owner | Cross-account/public share of a TpmSupport AMI. Can it make a NitroTPM AMI **public**? |
| SSM `get-parameters-by-path /aws/service/ami-windows-latest` | No | n/a (SSM) | n/a | anyone | Owner-authenticated **by namespace**; no owner arg exists or is needed. **Safe path.** |

**Undocumented/console-hidden knobs:** `KeyType=ecc-sec-p384` on `GetInstanceTpmEkPub` (UserGuide examples
only show RSA); `TpmSupport` attribute entirely absent from the console (both AMI and instance views).
The delta between "API accepts `--tpm-support v2.0`" and "console cannot set or display it" is itself a
lead (Lens U/EE below).

## 4. Boundary-Lens Catalog

### Lens A — Cross-tenant / cross-account resource access (IDOR)  ★ HEADLINE
**Correction anchor:** `GetInstanceTpmEkPub` **does** support `ec2:InstanceID`, `aws:ResourceTag/*`,
`ec2:ResourceTag/*`, `ec2:Region`, `ec2:InstanceType`, `ec2:Tenancy` (per `list_ec2`) — the attestation
plan's "zero condition keys" claim is factually wrong for this action and should be corrected there.

**Lead A-1 (cross-account EKpub read).**
- **Claim:** A principal with `ec2:GetInstanceTpmEkPub` on `Resource:"*"` can read the EKpub of an
  instance **in another account** by naming its `InstanceId`.
- **Mechanism:** The two doc pages state no cross-account restriction; "retrieve … at any time." EC2 has
  no resource-based sharing for `instance` objects, so the expectation is account-scoped ARN resolution —
  but this is an *inference from general EC2 behavior*, not a documented guarantee.
- **Confirm/Refute oracle:** Call with a syntactically valid `InstanceId` owned by a different account,
  principal allowed on `Resource:"*"`:
  - `InvalidInstanceID.NotFound` → account-scoping enforced server-side; **refuted**, no existence oracle.
  - `UnauthorizedOperation` → instance found but denied → **existence oracle** (weaker leak).
  - key material returned → **confirmed cross-account IDOR (Critical).**
- **Preconditions / Cost:** two accounts you own; one API call. **Severity:** Critical if confirmed;
  expected refuted by design (17-hex entropy also defeats blind enumeration).

**Lead A-2 (intra-account cross-tenant EK harvesting — the plausible one).**
- **Claim:** Because the tag condition keys exist but are optional, a role granted the action on
  `Resource:"*"` with **no `Condition`** can read the EKpub of *every* instance in a shared account,
  including other teams'/tenants' instances, enabling stable per-instance tracking.
- **Mechanism:** EK is a permanent per-instance identifier (TPM spec); AWS exposes
  `ec2:ResourceTag/*` / `aws:ResourceTag/*` to scope it, but nothing *requires* their use.
- **Confirm/Refute oracle:** In one account, role A (tag `team=A`, policy allows on `Resource:"*"`)
  reads EKpub of an instance tagged `team=B`; repeat later and compare `keyValue` — identical value
  across time ⇒ confirmed stable tracking identifier reachable cross-team.
- **Severity:** Low–Medium. This is a **customer IAM-authoring hygiene gap**, not an AWS API defect —
  AWS shipped the condition keys needed to prevent it. Report as a least-privilege footgun with the
  exact `Condition` block that fixes it.

**Note (EK → `MakeCredential` channel):** knowing EKpub lets any party wrap a secret *to* that TPM via
TPM2_MakeCredential/ActivateCredential (private EK never leaves the TPM). This is a **by-design TPM
feature**, not a vuln, and does **not** shortcut the PCR-policy that gates BitLocker unseal (see Lens U).
Record as informational; do not chase.

### Lens R / S — AWS-authored IAM artifact & condition-key semantics (enablement supply chain)  ★ HEADLINE
**Lead R-1 (NitroTPM enablement is IAM-ungatable by value).**
- **Claim:** An org **cannot** write an IAM policy that forces NitroTPM on, forbids it, or requires
  `--boot-mode uefi` to accompany `--tpm-support v2.0`, because **no condition key keys off the
  `TpmSupport` or boot-mode *value* at `RegisterImage` time.**
- **Mechanism (doc evidence):** `list_ec2` — `RegisterImage` resource `image*` carries only
  `aws:RequestTag/*`, `aws:TagKeys`, `ec2:ImageID`, `ec2:Owner`, `ec2:Region` (+ snapshot keys). There is
  **no `ec2:TpmSupport` key anywhere** in `list_ec2`. `ec2:BootModeOverride` exists but is a
  launch/CreateImage-time key, **not** on `RegisterImage`. Enablement is also the *only* path
  (`enable-nitrotpm-support-on-ami` — not console, not VM Import/Export) and is **immutable** after
  register.
- **Confirm/Refute oracle:** Attempt to author a Deny/Condition on `RegisterImage` that references the
  TpmSupport value; confirm there is no key to bind to (policy simulator / IAM docs). Confirm an unprivileged
  AMI creator can register `--tpm-support v2.0` with **`--boot-mode` omitted or non-uefi** and observe
  whether the service rejects at register or only at launch (the register-vs-launch split is the gap).
- **Severity:** Medium (governance/guardrail gap). Two concrete consequences: (a) a central-images team
  cannot *mandate* NitroTPM via SCP/condition — only via out-of-band build process; (b) a hardened-image
  policy that assumes "if TpmSupport=v2.0 then boot-mode is uefi" is not enforced by IAM and must be
  checked post-hoc with `DescribeImages`.

**Lead S-1 (register-time vs launch-time boot-mode key split).**
- **Claim:** The existence of `ec2:BootModeOverride` only at launch/CreateImage (not RegisterImage) means
  the boot-mode↔TpmSupport coupling is enforced, if at all, at a *different* control point than where the
  AMI attribute is minted — a classic "two control points, one checked" seam.
- **Oracle:** register a `v2.0` AMI with an inconsistent boot-mode and launch it; observe which layer
  rejects. **Severity:** Low–Medium (depends on whether launch silently "fixes" or faults).

### Lens EE / U — Predictable-name / land-grab via AWS's documented discovery pattern (whoAMI)  ★ HEADLINE
**Lead EE-1 (name-filter discovery without owner pinning → attacker AMI).**
- **Claim:** AWS's own `ami-windows-tpm.html` trains customers/IaC to find the hardened NitroTPM+Secure-Boot
  Windows image by the **name pattern `TPM-Windows_Server-*` / `TPM-Windows*`**. Any derivative
  `DescribeImages`/`Get-EC2Image` call that keeps the name filter but **drops `--owners amazon`** resolves
  globally across *all visible AMIs*, letting an attacker-registered look-alike (matching name + `platform=windows`
  + plausible `creation-date`) be selected instead — the Datadog whoAMI shape, now on a security-hardening
  image class where trust is highest and least re-verified.
- **Mechanism (doc evidence):** Page documents **two** paths:
  - **Safe:** SSM `/aws/service/ami-windows-latest` (`get-parameters-by-path … | grep TPM-Windows_Server`)
    — owner-authenticated **by namespace**, no owner arg exists; NOT exploitable.
  - **Risk-adjacent:** `describe-images --owners amazon --filters Name=name,Values=TPM-Windows_Server-* …`
    — AWS's example *does* include `--owners amazon`, but the governing sentence foregrounds **date
    filtering** ("The best way to ensure that your search returns the AMIs… is to add date filtering for
    the name") as the integrity control, not owner pinning. A user who extracts just the name-filter half
    (syntactically valid, returns results) inherits the oracle.
- **Confirm/Refute oracle:** In an account you own, register an AMI named `TPM-Windows_Server-2099.01.01`,
  `platform=windows`; run `describe-images --filters Name=name,Values=TPM-Windows_Server-*
  Name=platform,Values=windows` **without** `--owners`; confirm your AMI appears in results alongside/above
  AWS's. (Do **not** share it publicly or target anyone else's tooling.)
- **Severity:** Medium-High. Elevated because the look-alike can present a Secure-Boot+NitroTPM instance
  carrying **Microsoft's standard public db/KEK/PK** (`Microsoft Corporation KEK 2K CA 2023`,
  `Windows UEFI CA 2023`) — so its PCR7 lineage *looks* compliant to automated scanners while running
  attacker OS content. Capped below Critical: requires the victim's tooling to omit owner-pinning
  (outside this page's own examples) and the attacker to get a matching-name AMI visible to the victim.
- **Defender note:** the fix is a one-word addition (`--owners amazon` / `-Owner amazon`) OR use the SSM
  path exclusively. Flag any IaC/Packer/Lambda AMI-selector that keys off `TPM-Windows*` without owner.

### Lens U / W — Documented guarantee vs enforcement: BitLocker "original instance only" & non-portability
**Lead U-1 (sealing guarantee — confidentiality).**
- **Claim (to refute):** The guarantee *"BitLocker volumes encrypted with NitroTPM-based keys can only be
  used on the original instance"* can be broken by exporting/cloning/migrating the vTPM state.
- **Mechanism:** `enable-nitrotpm-prerequisites` "Considerations" state vTPM state is **not** in EBS
  snapshots, **not** in VM Import/Export, **not** shown in console, and BitLocker-NitroTPM keys work only
  on the original instance. The sealed key is bound to this vTPM's SRK + boot-time PCRs, evaluated *inside*
  the specific TPM.
- **Confirm/Refute oracle:** Enumerate every documented path that touches instance/volume state
  (CreateImage, CreateSnapshot, VM Export, CopyImage, AMI from instance) and confirm **none** carry
  NitroTPM/vTPM state; attempt to attach a BitLocker-sealed snapshot to a second instance and confirm the
  volume is **unreadable** (different EK, different PCRs). Finding an export/clone API would flip this to a
  real break.
- **Severity:** Informational (no break found — matches by-design TPM semantics; absence of any documented
  export mechanism = by-design, not a gap). **This is a REFUTE-expected lead; its value is closing it.**

**Lead U-2 (silent DR / availability footgun — operational).  ★ the actionable half of U**
- **Claim:** Teams relying on **EBS-snapshot DR** for BitLocker-protected instances will silently lose
  recoverability: restoring a sealed root volume to a new instance yields a **permanently unreadable
  volume**, because the only path to the drive key (vTPM state) is not in the snapshot.
- **Oracle:** snapshot a BitLocker-sealed volume (same account, fully authorized), restore to a new
  instance, confirm BitLocker cannot unseal.
- **Severity:** **Medium operational-risk** (not a security break). Report to defenders: DR runbooks,
  golden-image fleet rebuilds, and instance-replacement automation that assume volume backups are
  restorable are wrong for NitroTPM-sealed volumes. Document the correct recovery (BitLocker recovery key
  escrow) as the mitigation.

### Lens AA — Cross-account AMI sharing of a TpmSupport image (lifecycle)
**Lead AA-1.**
- **Claim:** `ModifyImageAttribute` launchPermission can share — or make **public** — an AMI carrying the
  immutable `TpmSupport=v2.0` attribute, and the recipient's launched instances inherit NitroTPM, with no
  condition key that can scope the share by the TpmSupport value.
- **Mechanism:** `list_ec2` — `ModifyImageAttribute` on `image*` with `ec2:Attribute`,`ec2:Public`,
  `ec2:Owner`; `TpmSupport` is a fixed AMI attribute (set at RegisterImage, immutable). No `ec2:TpmSupport`
  key to gate sharing on.
- **Confirm/Refute oracle:** Share a `v2.0` AMI to a second account you own; launch there; `DescribeInstances`
  confirms `TpmSupport=v2.0` on the launched instance (attribute propagated). Test whether `--launch-permission
  Add={Group=all}` makes it public. **Severity:** Low–Medium — primarily a provenance/trust concern
  (a shared "hardened" AMI's TpmSupport is attacker-asserted; recipients should pin owner, re-linking to
  Lens EE). Ties to the attestation plan's Secure-Boot-key reproducibility point.

### Lens L — Portability / availability constraints (footgun catalogue)
- `NitroTPM is not supported on AWS Outposts, Local Zones, or Wavelength Zones` — a hardened image that
  *requires* NitroTPM silently cannot launch there (availability, not security). Record as a deployment
  constraint, not a breach.

## 4b. Explicit NULL hypotheses (pages checked, lens does not fire)
- **Lens G (SSRF):** NULL — read all 6 children + API ref + Windows AMI page; no field the NitroTPM
  surface dereferences server-side (EKpub is read-out, not a fetched location).
- **Lens Q (blob/upload parse):** NULL — no NitroTPM API ingests a customer blob the service parses
  (RegisterImage references a snapshot by ID, not an uploaded TPM-state blob; vTPM state is non-importable).
- **Lens F (translation/injection), P (business-logic gate / OTP), B (PassRole), C (cred-vending),
  D (data→control escape), K/BB/CC/DD/FF:** NULL for this surface — no role-ARN input, no session-policy,
  no customer-reachable host beyond the control-plane API, no gate/code/challenge, no translation layer.
- **Attestation / KMS `RecipientAttestation` / PCR binding / replay-freshness / COSE alg / CRL /
  enclave-vs-NitroTPM key confusion / EK-certificate-chain trust:** **→ DEFER to
  `nitrotpm-attestation-attack-research-plan.md` (Areas 1–8).** Only the hand-off is recorded here:
  the EK-cert-absence fact (no chain returned by `GetInstanceTpmEkPub`) is an *input* to that plan's
  third-party-verifier trust analysis.

## 5. Priority order (concentrate fire)
1. **Lead R-1 (Lens R/S)** — NitroTPM enablement is IAM-ungatable by value; no `ec2:TpmSupport` key.
   Highest-value because it is an AWS-platform governance gap (not a customer misconfig), cheap to confirm
   from `list_ec2` alone, and corrects a factual error in the sibling plan.
2. **Lead EE-1 (Lens EE/U)** — whoAMI on `TPM-Windows_Server-*` without owner pinning. Medium-High,
   concrete reproducible oracle, security-hardening image class.
3. **Lead A-1 (Lens A)** — cross-account `GetInstanceTpmEkPub` IDOR. Critical *if* confirmed; expected
   refuted, but one API call to close, and the error-code behavior is a free existence-oracle check.
4. **Lead A-2 (Lens A)** — intra-account cross-tenant EK tracking via `Resource:"*"` + no tag condition.
   Low–Medium, customer-hygiene, but the exact fix policy is a deliverable.
5. **Lead U-2 (Lens U)** — silent DR/availability footgun on snapshot restore of sealed volumes.
   Medium operational-risk; high defender value.
6. **Lead AA-1 (Lens AA)** — cross-account/public share of a TpmSupport AMI; provenance concern.
7. **Lead U-1 (Lens U/W)** + **Lead L** — refute-expected sealing guarantee + Outpost/LZ/WZ constraint.
   Lowest; value is in closing them cleanly.

## 6. Hand-offs & carried doc-gaps
- **To attestation plan:** EK has **no certificate chain** returned → feeds that plan's third-party
  verifier trust-establishment analysis (manufacturer-genuineness gap). Secure-Boot db/KEK/PK are
  Microsoft's public certs baked into AWS's Windows AMI build → reproducible PCR7 lineage across all
  launchers of the same dated AMI (ties to attestation Area 1 reproducible-measurement).
- **Doc-gaps:** (a) Neither doc page states the cross-account authorization behavior of
  `GetInstanceTpmEkPub` — must be confirmed live (Lead A-1). (b) Whether the service rejects a
  `--tpm-support v2.0` + non-uefi `--boot-mode` combination at register or only at launch is undocumented
  (Lead S-1). (c) Whether `ModifyImageAttribute Group=all` can make a NitroTPM AMI public is not called out
  on the NitroTPM pages (Lead AA-1). (d) EK **rotation**/`TPM2_Clear` semantics on an AWS vTPM across
  stop/start/resize are not documented — assumed stable-for-instance-life (Lead A-2 depends on this).

## 7. Severity summary

| Lead | Lens | Class | Verdict (doc-stage) | Severity |
|---|---|---|---|---|
| R-1 | R/S | AWS platform guardrail gap | plausible — no `ec2:TpmSupport` key in `list_ec2` | **Medium** (governance) |
| EE-1 | EE/U | supply-chain / name-resolution | plausible on tooling drift | **Medium-High** |
| A-1 | A | cross-account IDOR | expected refuted; needs live oracle | Critical-if-true / Low |
| A-2 | A | intra-account cross-tenant tracking | real misconfig risk; AWS provides fix | Low–Medium |
| U-2 | U | DR/availability footgun | by-design; silent data-loss | **Medium** (operational) |
| AA-1 | AA | AMI provenance / share | plausible; unscopable by TpmSupport | Low–Medium |
| U-1 | U/W | sealing confidentiality | no break found (by-design) | Informational |
| L | L | deployment constraint | documented | Informational |

## 8. One-line corrections this plan makes to the sibling attestation plan
- Attestation plan **Area 8** claims **zero condition keys** on `RegisterImage` **and**
  `GetInstanceTpmEkPub`. **Both are false per `list_ec2`:** `GetInstanceTpmEkPub` carries
  `ec2:InstanceID`/`aws:ResourceTag`/`ec2:ResourceTag`/`ec2:Region`/`ec2:InstanceType`/`ec2:Tenancy`;
  `RegisterImage` carries `aws:RequestTag`/`aws:TagKeys`/`ec2:ImageID`/`ec2:Owner`/`ec2:Region`
  (+snapshot keys). What is genuinely absent is a key on the **`TpmSupport` *value*** (no `ec2:TpmSupport`
  anywhere) and `ec2:BootModeOverride` on `RegisterImage` (it is launch/CreateImage-time only). The
  correct statement is "**enablement is not value-gatable**," not "no condition keys exist."
