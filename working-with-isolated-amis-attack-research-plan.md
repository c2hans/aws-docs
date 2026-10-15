# Updating Attestable AMIs (working-with-isolated-amis) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-isolated-amis.html` (= `working-with-isolated-amis.md`, "Updating Attestable AMIs that have no interactive access"), cross-read with `replace-root.md` (root-volume replacement), `list_ec2.md` + `list_kms.md` (Service Authorization Reference), and the NitroTPM-attestation cluster. Status: documentation-derived hypotheses only; nothing tested against a live account. Offline mirror `/work/aws-docs`, cross-checked online 2026-10-15.

> This plan is a **page-level COMPLEMENT** inside a dense sibling cluster. It owns ONLY the **UPDATE / RE-SYNC lifecycle** surface of Attestable AMIs — the operational workflow where a software change forces a new AMI, and a measurement-changing event (stop/start or root-volume-replacement) forces a manual re-sync of the attestation service (KMS key policy). It was explicitly deferred here by [[al2023-isolated-compute-recipe]] ("Stale-reference-measurement-in-KMS-policy after AMI update → working-with-isolated-amis"). It DEFERS: build/measurement root-cause → `attestable-ami` / `build-sample-ami`; the KMS attestation gate internals / PCR under-binding / reproducible-PCR bypass → `nitrotpm-attestation`; NitroTPM enable/disable lifecycle & control-plane↔guest split-brain → `nitrotpm-instance`; isolated-compute recipe content → `al2023-isolated-compute-recipe`.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- Settle every IAM-scopability lead READ-ONLY first with `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (a condition key either applies to an action or it does not — no resource creation). Escalate to a live canary only for the runtime-behaviour questions explicitly flagged "needs canary".
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the Nitro controller, the NitroTPM key-vending plane, any cross-tenant EK/attestation signer), stop, preserve evidence, flag for AWS-Security disclosure. The NitroTPM attestation signer and EK provisioning are AWS service-plane — do not probe them.

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Stale-policy outage (availability):** force a measurement-changing event on a victim's isolated/attested instance (stop/start, or root-volume replacement) so its live PCRs/measurements no longer match the KMS key policy, denying the instance its KMS-sealed secrets until a human re-syncs the policy out-of-band. Prove the EC2 action is reachable under an intra-account scoped principal.
2. **Under-binding on re-sync (confidentiality/integrity):** show that the operator practice this page induces — updating the KMS key policy "to the new reference measurements" every time the AMI changes — pushes operators toward a loose/wildcard/old+new PCR condition that then also admits an attacker-built Attestable AMI's measurements.
3. **EK-persistence vs reset ambiguity:** resolve whether the NitroTPM key material (EK/identity) survives a root-volume replacement (as this page asserts) or is reset (as `replace-root.md` asserts), and show the consequence for a verifier that pins on instance identity rather than PCRs.
4. **Root-volume-swap workload substitution:** determine whether `CreateReplaceRootVolumeTask` lets a principal who does NOT own the attestation policy swap the measured workload of a running attested instance (retaining network identity, IAM profile, instance identity docs) under a stale or relaxed policy.
5. Confirm the three claims are enforced by a *mechanism*, not just prose, and that no EC2/KMS condition key was expected to carry a guarantee it does not.

## 2. Components, Assets, and Design
**What the page describes.** The *isolated compute environment* AMI = an Attestable AMI built with interactive access removed (no SSH/SSM/console; see `al2023-isolated-compute-recipe`). After launch, **no user or operator can connect** → **no in-place software install or update is possible**. The only update path is: build a NEW Attestable AMI → (a) launch a new instance from it, OR (b) **root-volume replacement** on the original instance. Any software change ⇒ a **new hash** (new PCR reference measurements).

**Assets:**
- **NitroTPM key material (EK / instance NitroTPM identity).** Page asserts it "persists through stop/starts and root volume replacement operations" for the whole instance lifecycle. (CONTESTED — see Area 2.)
- **Reference measurements (NitroTPM PCRs) in the NitroTPM Attestation Document.** Change on: (i) stop+start of an Attestable-AMI instance; (ii) root-volume replacement with a *different* AMI; (iii) any software change in a rebuilt AMI.
- **The attestation service binding** — concretely, an **AWS KMS key policy** whose `Condition` pins `kms:RecipientAttestation:NitroTPMPCR<n>` / `:ImageSha384` so that `kms:Decrypt`/`GenerateDataKey` only succeed when the caller presents a matching attestation document. This is the sealed-secret gate the isolated workload depends on.

**Design / pipeline (implied):**
```
 build new Attestable AMI (new hash)                    [owner build plane -> attestable-ami]
        │
        ├─(a) RunInstances(new AMI) ───────────► new instance, new EK?, new PCRs
        │
        └─(b) CreateReplaceRootVolumeTask ─────► SAME instance (same ENI/IP/DNS/IAM profile/instance-store),
             (ImageId = new AMI)                   NEW root volume, NEW PCRs, EK: PERSIST (this page)
                                                                       vs RESET (replace-root.md)  ← CONTRADICTION
        │
   measurement change
        │
        ▼
 operator MUST manually update KMS key policy          [customer out-of-band step; NO AWS automation documented]
   Condition: kms:RecipientAttestation:NitroTPMPCRn = <new measurement>
        │
        ▼
 isolated instance presents attestation doc ─► KMS Decrypt gate ─► sealed secret
   (between the event and the re-sync: GAP — fail-closed outage, or operator relaxes the pin)
```

**Identity / privilege levels relevant here:**
- Caller of `StopInstances`+`StartInstances` on the instance (intra-account, instance-scopable).
- Caller of `CreateReplaceRootVolumeTask` (needs the instance + AMI/snapshot/volume per the resource rows — see Area 4).
- Author of the KMS key policy (`kms:PutKeyPolicy`) — the attestation gate owner.
- The isolated workload itself (the KMS Decrypt caller presenting the attestation document).

## 3. API / Interface Inventory
| Name | Method | New/Existing | Mutating | Facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2:CreateReplaceRootVolumeTask` | API | Existing | **Mutating** | External | Swap the root volume of a *running* instance (from launch-state snapshot / specified snapshot / **AMI** / existing volume) | Yes (SigV4) | holder of the action on instance* (+image/snapshot/volume) | The page's primary "update the original instance" path. Scopable — see Area 4. Resets NitroTPM data per `replace-root.md`. |
| `ec2:DescribeReplaceRootVolumeTasks` | API | Existing | Non-mutating | External | Read RVR task state | Yes | tag/region scopable | task state oracle |
| `ec2:StopInstances` / `ec2:StartInstances` | API | Existing | **Mutating** | External | Stop then start an instance | Yes | instance*-scopable (`ec2:InstanceID`,`aws:ResourceTag`) | **This page says a stop+start CHANGES the reference measurements** → forced-resync primitive. No condition key marks an instance as "attested". |
| `ec2:RunInstances` (new AMI) | API | Existing | **Mutating** | External | Launch a fresh instance from the rebuilt AMI | Yes | broad; see `attestable-ami` | alternative update path; new EK + new PCRs |
| `kms:PutKeyPolicy` | API (KMS) | Existing | **Mutating** | External | Update the attestation-gated key policy to the new reference measurements | Yes | key-policy admin | the manual re-sync step; schema-validation of PCR values is the Area 3 question |
| `kms:Decrypt` / `kms:GenerateDataKey` (w/ `Recipient` attestation) | API (KMS) | Existing | Non-mutating | External | The sealed-secret gate the isolated workload calls | Yes | gated by `kms:RecipientAttestation:*` | fail-direction when PCRs drift = Area 1 |

No new/undocumented API is introduced by this page; its surface is the *composition* of existing EC2 lifecycle actions with the KMS attestation gate, plus the operator re-sync procedure.

## 4. Trust-Boundary Map
| From (actor) | To (resource) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Intra-account principal with Stop+Start on the instance | The instance's attestation validity | `StopInstances`+`StartInstances` changes reference measurements | KMS Decrypt by the isolated workload starts failing after a forced stop/start it did not authorize at the attestation layer → self-inflicted secret outage requiring manual re-sync = availability breach |
| Intra-account principal with `CreateReplaceRootVolumeTask` on the instance | The measured workload running under a retained identity | RVR-via-AMI swaps the root (new PCRs) while keeping ENI/IP/IAM-profile/instance-identity-doc | A workload the policy-owner did not approve runs under the original instance's network+IAM identity; if KMS policy pins EK not PCRs (and EK persists), the swap passes the gate = integrity breach |
| KMS key-policy author (re-sync practice) | The sealed secret | Loose/old+new/wildcard `kms:RecipientAttestation:NitroTPMPCRn` to tolerate frequent AMI updates | A measurement set the author never intended (an attacker-built Attestable AMI) satisfies the relaxed condition and decrypts = confidentiality breach (Lens W under-binding) |
| AWS NitroTPM key-vending / attestation signer plane | — | — | **HARD STOP** — any EK/signer/cross-tenant attestation material is AWS service plane; do not probe, flag for disclosure |

## 5. Recommended Areas of Focus (priority order; one block per firing lens)

### Area 1 — EK persist-vs-reset DOC-VS-DOC CONTRADICTION [Lens U — integrity-of-the-guarantee] — **HEADLINE, Tier-2 reportable (AWS-authored, currently published)**
**Claim:** Two live AWS pages make mutually-exclusive assertions about whether NitroTPM key material survives a root-volume replacement, so at least one published security guarantee is wrong, and a verifier that trusts the wrong one is defeated.
- **Mechanism (doc evidence — verified online == offline byte-consistent 2026-10-15):**
  - `working-with-isolated-amis.md:18` (verbatim): *"An instance retains its NitroTPM key material for the entire instance lifecycle, and persists through stop/starts and root volume replacement operations."* — unqualified, covers **all** RVR.
  - `replace-root.md` (AMI-considerations subsection, verbatim): *"If the instance supports NitroTPM, the NitroTPM data for the instance is reset and new keys are generated."* — directly opposite, scoped to RVR-**via-AMI**.
  - The contradiction is **scoped to RVR-via-AMI**; the three other RVR source methods (launch-state snapshot / specified snapshot / existing volume) are **silent** on NitroTPM → a second doc-gap.
- **Two mutually-exclusive consequences, both reportable:**
  - **Claim A (EK persists — isolated-amis page is right):** an EK-pinned verifier is **fooled across a workload swap**. RVR-via-AMI changes the measured workload (new PCRs) but the EK/instance identity is unchanged → any attestation/consumer that binds on EK or instance identity rather than on live PCRs accepts the substituted workload. Confidentiality/integrity.
  - **Claim B (EK reset — replace-root page is right):** an EK-pinned gate **breaks on a legitimate update**; worse, the isolated-amis page only instructs the operator to update *reference measurements* (PCRs), never to re-enroll a new EK → silent availability break **plus** an undocumented re-enrollment requirement. Availability + doc-gap.
- **Confirm/Refute oracle (needs canary):** launch an Attestable-AMI NitroTPM instance; `GetInstanceTpmEkPub` → record EK. Run `CreateReplaceRootVolumeTask` with `ImageId` = a *different* Attestable AMI; after the task completes, `GetInstanceTpmEkPub` again. **EK unchanged ⇒ Claim A** (isolated-amis correct, replace-root wrong). **EK changed ⇒ Claim B** (replace-root correct, isolated-amis wrong). Settle via EK read only — no secret decryption needed.
- **Preconditions:** one account, one instance, two Attestable AMIs. Cost: minutes. **Severity: High** (a published, byte-confirmed contradiction in a security guarantee; whichever way it resolves, one AWS page misleads a verifier). Route EK-read mechanics to [[retrieve-ekpub]] and [[verify-nitrotpm-support-on-instance]]; this plan OWNS the contradiction itself.
- **Stop condition:** EK read settles the direction. Do not decrypt a sealed secret to "prove" the swap — the EK delta is the whole PoC.

### Area 2 — Root-volume-swap workload substitution under a retained identity [Lens AA — lifecycle completeness + Lens A-adjacent] [High]
**Claim:** A principal who holds `ec2:CreateReplaceRootVolumeTask` on a victim instance but does **not** own the paired KMS key policy can swap the measured workload of a running attested instance while it keeps its ENI/IP/DNS, IAM instance profile, and auto-updated instance identity document — and, if the policy pins EK (and Claim A holds) or the policy is stale/relaxed, the substituted workload inherits the gate.
- **Mechanism:** `replace-root.md` — RVR-via-AMI keeps the instance (same ENI/IP/IAM profile/instance-store); instance identity documents are auto-updated; boot mode cannot change (must match `currentInstanceBootMode`); instance must be running; RAM is erased on the automatic reboot. `list_ec2.md:5382-5389` — `CreateReplaceRootVolumeTask` resource rows: `image` (ec2:ImageID/ImageType/Owner/Public/RootDeviceType/ResourceTag), `instance*` (ec2:InstanceID + ec2:InstanceProfile + more), `snapshot`, `volume*`, `replace-root-volume-task*` (only aws:RequestTag/aws:TagKeys/ec2:Region) → **the action IS richly scopable** (CORRECTED premise: the first grep caught only the task-ARN row, which carries only tag/region keys; the full block shows the image/instance/snapshot/volume rows carry rich keys).
- **Confirm/Refute oracle:** scope a principal `ec2:CreateReplaceRootVolumeTask` on instance ARN X with `ImageId` NOT constrained by an `ec2:ImageID`/`ec2:Owner` condition; confirm it can RVR instance X to an attacker-chosen AMI, inheriting X's ENI/IAM profile. Combine with Area 1 outcome to decide whether the gate also follows.
- **Severity: High** if the paired policy is EK-pinned or stale (chains Area 1-A / Area 3-a); **Medium** as an isolation/identity-reuse concern on its own. The reportable hardening gap: nothing on either page tells the operator to constrain `ec2:ImageID`/`ec2:Owner` on `CreateReplaceRootVolumeTask` for attested instances.
- **Stop condition:** one successful RVR to a non-owner-chosen AMI with retained identity proves the primitive. Do not pivot into the inherited IAM role.

### Area 3 — KMS under-binding on re-sync: the AWS-RECOMMENDED PCR7 certificate-pinning workaround [Lens W — attestation-conditioned authz under-binding] — **HEADLINE #2, Tier-2 reportable (AWS-authored)**
**Claim:** AWS's own documentation recommends a looser binding — pin the KMS policy to **PCR7** (the UEFI Secure Boot *certificate*) instead of PCR4/PCR12 (the exact *measurement*) — specifically to avoid the re-sync pain this target page creates. That looser binding tolerates **any** AMI signed with the same certificate, including old/untrusted builds, until the operator manually rotates the cert.
- **Mechanism (doc evidence — verified online == offline byte-consistent):** `nitrotpm-attestation-document-content.md:28` (verbatim): *"If you need to maintain a single KMS policy that persists across instance updates, you can create a policy that validates against PCR7 to validate a UEFI Secure Boot certificate... Keep in mind that this model requires you to still generate a new certificate, install it in your policy and update AMIs if you want to prevent instances launched from old (untrusted) AMIs from passing your KMS policy."* Cross-linked from `prepare-attestation-service.md:13`. AWS's own caveat sentence is a tacit admission that **absent cert rotation, old/untrusted AMI builds keep passing the policy** — textbook Lens W under-binding: the condition that tolerates the legitimate "new hash after update" also tolerates an attacker-built AMI signed with the same un-rotated cert.
- **Scoping facts (verified):** exactly **5** KMS actions carry `kms:RecipientAttestation:NitroTPMPCR<0-23>` / `:ImageSha384` — `Decrypt`, `DeriveSharedSecret`, `GenerateDataKey`, `GenerateDataKeyPair`, `GenerateRandom` (`list_kms.md:390-502`, corroborated by `conditions-nitro-tpm.md:15`). `Encrypt` and the two `*WithoutPlaintext` siblings do **not** carry the key. Operator is `StringEqualsIgnoreCase`; missing attestation ⇒ deny (fail-closed, `conditions-nitro-tpm.md:35-37`). **No `StringLike`/wildcard/multi-value PCR example exists anywhere** in the NitroTPM attestation doc set — AWS's own sample (`prepare-attestation-service.md:19-44`) is exact-match-safe. The PCR7 scheme is AWS's *documented alternative* to wildcarding, with the same semantic loosening ("signed by X" rather than "is exactly Y").
- **Confirm/Refute oracle (needs canary):** build Attestable AMI gen-N signed with cert C; create a KMS policy pinning `kms:RecipientAttestation:NitroTPMPCR7` = hash(C). Rebuild to gen-N+1 (new software, same cert C). Launch an instance from the **original** gen-N AMI; attempt a gated `kms:Decrypt`. **Decrypt succeeds ⇒ confirmed under-binding** (policy cannot distinguish AMI generation; only cert rotation would). 
- **Severity: High, Tier-2 reportable** — AWS-authored guidance on an AWS doc page that directly undermines the "update your KMS key policy to the new reference measurements" instruction the target page issues; the only stated mitigation is phrased as an opt-in afterthought with no automation. DEFER generic PCR-condition-key hygiene (stale-document replay, index/family confusion, malformed-PCR acceptance at `PutKeyPolicy`) → already owned by [[attestation-attest-plan-note]] (its Areas 3/5, incl. line 132); this plan's net-new contribution is the PCR7 certificate-pinning under-binding + the explicit EC2-trigger→KMS-outage causal chain.

### Area 4 — Stop/start (and RVR) forced re-sync → fail-closed secret outage [Lens L — availability] [Medium]
**Claim:** Any intra-account principal scoped to `ec2:StopInstances`+`ec2:StartInstances` (or `ec2:CreateReplaceRootVolumeTask`) on a victim attested instance can force a reference-measurement change, after which every gated KMS call from that instance fails until a human updates the key policy out-of-band — a self-inflicted / insider DoS of the isolated workload's sealed-secret path.
- **Mechanism:** `working-with-isolated-amis.md:12-16` — stop+start, and RVR-with-a-different-AMI, both change reference measurements and "you must then update your attestation service... update your KMS key policy." `conditions-nitro-tpm.md:37` — mismatch ⇒ deny (fail-closed). `list_ec2.md` — `StopInstances`/`StartInstances` are `instance*`-scopable (`ec2:InstanceID`, `aws:ResourceTag`), but **no condition key marks an instance as "attested"** → IAM cannot carve out "don't let this role bounce an attested instance" except by generic instance ARN/tag.
- **Confirm/Refute oracle (needs canary):** grant a principal `ec2:StopInstances`+`ec2:StartInstances` on instance ARN X but no `kms:PutKeyPolicy`; stop/start X; confirm the next `kms:Decrypt`/`GenerateDataKey` from X returns AccessDenied-class until the policy is re-synced.
- **Severity: Medium** — availability only, no confidentiality impact, bounded to a principal already holding EC2 lifecycle perms on that instance (insider / over-permissioned-role). The page itself names this as a known tradeoff; the reportable angle is that **neither this page nor `prepare-attestation-service.md` offers any IAM-level mitigation** (no attested-instance condition key), leaving it entirely to customer IAM design.
- **Stop condition:** one observed post-bounce AccessDenied proves the primitive.

### Area 5 — No automated re-sync primitive → standing drift [Lens U / Lens O — doc/product gap] [Medium]
**Claim:** The re-sync the page mandates is entirely manual and out-of-band; AWS documents **no** automation (EventBridge, CloudWatch Events, AWS Config, Systems Manager) to update a KMS key policy when an AMI/measurement changes.
- **Mechanism:** `working-with-isolated-amis.md:16` — imperative, customer-performed ("you must then update... update your KMS key policy"). Grep across `UserGuide/*attestation*`, `working-with-isolated-amis.md`, `nitrotpm*.md` for "EventBridge"/"CloudWatch Events"/"AWS Config" → **zero hits**.
- **Consequence (chains Area 3):** an operator who cannot keep up with manual re-sync is explicitly steered by AWS (Area 3) toward the looser PCR7 cert-binding — because no automation exists to steer toward. A policy that accumulates "old+new" measurements to preserve availability across the re-sync lag is the same drift the PCR7 scheme formalizes.
- **Severity: Medium**, AWS-owned process/architecture gap — reportable as a doc/product gap, not a vuln.
- **Oracle:** documentation-settled (absence). No canary needed.

## 6. Threat Model Test Objectives
| # | Objective (boundary-breach) | Firing lens | Primary oracle | Owner / severity | Needs canary? |
|---|---|---|---|---|---|
| 1 | Resolve EK persist-vs-reset; defeat an EK/identity-pinned verifier across an RVR workload swap (Claim A) OR expose a silent break + undocumented re-enroll (Claim B) | U | `GetInstanceTpmEkPub` before/after RVR-via-AMI: EK delta decides | AWS-authored / **High** | Yes |
| 2 | Swap measured workload of a running attested instance under retained ENI/IP/IAM identity via `CreateReplaceRootVolumeTask` by a non-policy-owner | AA, A | RVR to an attacker-chosen AMI succeeds with identity retained; chains #1/#3 | Customer-IAM footgun + AWS-hardening-gap / **High-if-chained** | Yes |
| 3 | Confirm AWS-recommended PCR7 cert-pinning admits an old/untrusted-but-same-cert AMI build to the KMS gate | W | gen-N AMI decrypts under a PCR7 policy pinned while gen-N+1 is current | AWS-authored / **High** | Yes |
| 4 | Force fail-closed sealed-secret outage via scoped stop/start or RVR, no `kms:PutKeyPolicy` held | L | post-bounce `kms:Decrypt` → AccessDenied until re-sync | Customer-IAM + AWS no-mitigation-key / **Medium** | Yes |
| 5 | Establish there is no documented automated re-sync primitive | U, O | grep: zero automation hits across the cluster | AWS doc/product gap / **Medium** | No |
| 6 | Verify the three other RVR source methods' NitroTPM behavior (silence = doc-gap) | U | `GetInstanceTpmEkPub` + attestation after RVR-via-snapshot / launch-state / existing-volume | AWS doc-gap / **Medium** | Yes |

## 7. Out-of-Scope Risk Categories (HARD STOPs — flag for disclosure, do not probe)
- **NitroTPM key-vending plane / EK provisioning / attestation signer** — AWS service plane. Reading your own instance's EK via `GetInstanceTpmEkPub` is in scope (Area 1 oracle); anything that reaches the signer, a cross-tenant EK, or the Nitro controller is a HARD STOP — preserve evidence, flag for AWS-Security.
- **KMS attestation-gate internals / COSE/signature validation / reproducible-PCR root cause** — owned by [[nitrotpm-attestation-plan-note]] / [[attestable-ami-plan-note]]; do not re-derive here.
- **Any cross-tenant decrypt of a secret** — confirm the gate *admits* an attestation (existence of the authz bypass) via a canary in your own account; never decrypt another tenant's sealed data.
- **Build-plane supply chain, guest runtime-integrity (post-boot overlay / TOCTOU)** — owned by [[build-sample-ami-plan-note]] / [[al2023-isolated-compute-recipe-plan-note]] / [[attestable-ami-plan-note]].
- **Live secret exfiltration beyond minimum PoC** — the moment a gate admits an unauthorized attestation, that is the PoC. Stop.

## 8. Null Hypotheses & Documentation Gaps (named pages checked)
- **Lens A/IDOR (cross-tenant) — NULL on this page.** Every resource named (instance, AMI, KMS key, RVR task) is the caller's own; RVR/stop-start/PutKeyPolicy are all account-local. No shared-fleet or cross-tenant primitive is introduced by `working-with-isolated-amis.md` or `replace-root.md`. (The cross-tenant EK/signer concern is the HARD STOP, not an IDOR lead.)
- **Lens B/C (PassRole / credential vending) — NULL.** No role-ARN input, no STS/session-policy field, no credential-vending on either page.
- **Lens F (translation/injection) — NULL.** No parser/translator/wire-protocol layer on this surface.
- **Lens G/SSRF — NULL.** No field the service dereferences (only AMI/snapshot/volume IDs and PCR hashes; the KMS `Recipient` attestation doc is customer-supplied-to-KMS, not a server-fetch target). Checked: `working-with-isolated-amis.md`, `replace-root.md`, `prepare-attestation-service.md`, `nitrotpm-attestation-document-content.md`.
- **Lens O/audit — PARTIAL/GAP.** Stop/Start/RVR/PutKeyPolicy all emit CloudTrail, but **no documented signal distinguishes an attestation-measurement change event** or warns that a sealed-secret path just went stale (feeds Area 5).
- **DOC-GAPs to settle on a canary:**
  1. **Headline:** which of `working-with-isolated-amis.md:18` vs `replace-root.md` is correct about EK survival across RVR-via-AMI (Area 1).
  2. NitroTPM behavior of the **three non-AMI RVR source methods** (launch-state snapshot / specified snapshot / existing volume) — all silent (Area 6, Objective 6).
  3. Does `PutKeyPolicy` validate PCR-ID range (0-23) / hex length/case at write time? `list_kms.md:582` shows no `RecipientAttestation` key on `PutKeyPolicy`; `conditions-nitro-tpm.md:21` gives only a prose format rule → malformed-value acceptance already flagged by [[attestation-attest-plan-note]] (its line 132); not re-opened here.
  4. Does a stop/start that changes measurements require EK re-enrollment, or only PCR-reference update? (Depends on Area 1 resolution.)

<!-- Plan complete: Sections 0–8. Headline findings: (Area 1) live doc-vs-doc EK persist-vs-reset contradiction, byte-confirmed online==offline 2026-10-15; (Area 3) AWS-recommended PCR7 cert-pinning under-binding at nitrotpm-attestation-document-content.md:28. Both Tier-2 AWS-authored. Supporting: Area 2 RVR workload substitution, Area 4 forced-resync DoS, Area 5 no-automation gap. Subagent A confirmed Area 1; Subagent B confirmed Area 3/4/5. -->

