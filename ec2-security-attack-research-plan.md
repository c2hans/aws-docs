# Amazon EC2 — Security Chapter — Attack Research Plan (HUB)

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html` (offline twin `docs/AWSEC2/latest/UserGuide/ec2-security.md`) and its 13 linked child topics. Authoritative IAM: `docs/service-authorization/latest/reference/list_ec2.md` (slug `list_ec2`; grep offline — the online page truncates before the detailed condition-key tables). Status: documentation-derived hypotheses only; nothing tested against a live account.

This is the **hub plan** for the EC2 Security chapter. The chapter landing page is a shared-responsibility overview + topic index — it defines no API of its own. Its security value is as a **map**: it enumerates the 13 sub-surfaces that together make up "Security in Amazon EC2." This plan reconstructs the chapter-level trust-boundary picture and routes a hunter, in priority order, to the **six child attack-research plans** produced alongside it (each a full §0–§8 plan in its own right).

## 0. How to use this document
- The hub owns the **cross-cutting synthesis**: the shared-responsibility line as a scope boundary, the chapter-wide trust-boundary map, and the ranked routing table into the child plans. It does **not** restate each child's leads — it points at them.
- Each child plan carries its own falsifiable leads in the skill's Claim → Mechanism → Oracle → Preconditions → Severity → Stop-condition shape. Work them in the priority order of §5 below.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (Nitro controller, a Nitro-attestation PKI private key, a shared-fleet host credential), stop, preserve evidence, flag for AWS-Security disclosure.
- **Shared-responsibility scope rule (chapter-defining):** the landing page splits "security *of* the cloud" (AWS-owned — in scope only at the HARD-STOP tier) from "security *in* the cloud" (customer-owned). Guest-OS config a customer performs on their own instance (patching, in-guest hardening, their own IAM policies) is **out of scope** — EXCEPT where AWS ships the artifact the customer copies verbatim (managed policies, sample policies/CFN/runbooks, published setup commands): those are AWS-authored and **in scope / Tier-2 reportable** (Lens R/S/U carve-out). This carve-out is where the chapter's highest-confidence findings live.

## 1. Pentest Objectives (chapter-level, stated as concrete breach outcomes)
1. From a principal holding only an AWS-**managed** EC2 policy, reach `admin` (non-admin→admin privesc inside one account) — *EC2FastLaunchFullAccess / AmazonEC2FullAccess, see IAM child.*
2. Retrieve a private key / credential EC2 generated, via a **second service** whose IAM the origin API would deny — *CloudFormation key pair → SSM Parameter Store, see Key-pairs child.*
3. Defeat an **attestation-conditioned** KMS authorization (NitroTPM PCR gate) so sealed data decrypts for a principal the gate should exclude — *NitroTPM/attestation child.*
4. Reach another tenant's data at rest after the customer believes a KMS key disable/delete revoked it — *EBS cached data key, data-protection child.*
5. Mutate another account's effective network posture (or evade its audit trail) through **security-group referencing** across a shared/peered VPC — *security-groups/PrivateLink child.*
6. Execute code as SYSTEM in a guest the caller has no RDP/SSH to, via an EC2 control-plane write that feeds the boot pipeline — *`ModifyInstanceAttribute(userData)` → EC2Launch, Windows child & IAM child.*

## 2. Components, Assets, and Design (chapter decomposition)

The chapter's 13 topics decompose into **six research clusters**, each with its own plan:

```
                    EC2 SECURITY CHAPTER (ec2-security.html)
                      shared-responsibility split (scope line)
   ┌──────────────┬──────────────┬───────────────┬──────────────┬───────────────┬──────────────┐
   │  IAM /roles  │  Key pairs   │ NitroTPM +    │ Data + Infra │ Security      │ Windows / CG │
   │              │              │ attestation   │ protection   │ groups +      │ / updates /  │
   │              │              │               │              │ PrivateLink   │ compliance   │
   ├──────────────┼──────────────┼───────────────┼──────────────┼───────────────┼──────────────┤
   │ managed pols │ CreateKeyPair│ PCR / measured│ EBS KMS enc  │ Authorize/    │ Credential   │
   │ SLR policies │ ImportKeyPair│ boot          │ at-rest/trans│ Revoke SG     │ Guard (VBS)  │
   │ instance-    │ CFN KeyPair  │ kms:Recipient │ Nitro isolat.│ SG-referencing│ EC2Launch v2 │
   │ profile      │ →SSM param   │ Attestation   │ encryption-  │ endpoint pols │ sample cmds  │
   │ PassRole     │ store        │ :NitroTPMPCR  │ by-default   │ conn-tracking │ SSM patching │
   │ IMDS creds   │              │ attest. doc   │              │ SG VPC assoc  │ Win Update   │
   └──────┬───────┴──────┬───────┴───────┬───────┴──────┬───────┴───────┬───────┴──────┬───────┘
          │              │               │              │               │              │
   ec2-security-   ec2-key-pairs-  nitrotpm-      ec2-data-infra  ec2-security-   ec2-windows-
   iam-...plan.md  ...plan.md      attestation-   structure-...   groups-         credential-
                                   ...plan.md     plan.md         privatelink-    guard-...plan.md
                                                                  ...plan.md
```

**Chapter-wide assets:** IAM principals + AWS-managed/SLR policies; EC2-generated secrets (key-pair private keys, password data, UEFI/TPM EK data); attestation measurements (PCRs) and the attestation-document signing PKI; EBS data-encryption keys cached in Nitro hardware; security-group rules + the SG-reference graph across accounts; the guest-OS boot pipeline (EC2Launch/EC2Config) as a code-exec sink.

**Identity shapes present:** SigV4 IAM principals; instance-profile role creds vended via IMDS; the new documented **Instance Identity Role** (`/identity-credentials/ec2/security-credentials/ec2-instance`, no trust policy, no identity/resource-policy enforcement found); attestation = boot-state measurement, NOT caller identity (the load-bearing distinction in the NitroTPM child).

**Compliance-validation** and **Resilience** topics are AWS-global-infrastructure / shared-responsibility prose with no queryable control-plane surface of their own → null at the chapter level (see §8); their only live hooks (cross-Region AMI/snapshot copy, DLM) are carried as doc-gaps into the data-protection child.

## 3. Trust-Boundary Map (chapter level)

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Non-admin IAM principal (one managed policy) | Any role/instance-profile in account | `iam:PassRole` scoped only by `PassedToService=ec2` + unconditioned `RunInstances` | Launch an instance with a foreign privileged role attached; pull its creds from IMDS → acted as admin. **Critical.** |
| Principal denied `ec2:*KeyPair*` | Cleartext private key | CFN stores key at SSM `/ec2/keypair/{id}` SecureString | `ssm:GetParameter --with-decryption` returns the private key the EC2 API would deny. **Med-High.** |
| Any customer with a public AMI recipe | Attestation-gated KMS key | PCR condition value is publicly reproducible from boot binaries | A self-registered identical AMI attests and decrypts; PCR clause contributes zero security, only `Principal` does. **Critical-if-Principal-broad.** |
| IR operator who "disabled the CMK" | Running EBS volume's plaintext | Nitro caches the data key until detach | Volume keeps serving plaintext after key disable/delete → break-glass assumption false. **High.** |
| Account A principal | Account B's effective SG posture + audit trail | SG-referencing never IAM-authorized; cross-account ref invisible in B's CloudTrail | Authorize/Revoke naming B's SG succeeds with only "exists" check; B sees no CloudTrail event. **High/Critical.** |
| Principal with only `ec2:ModifyInstanceAttribute` | SYSTEM code exec in a guest OS | EC2Launch v2 `executeScript` runs userData at boot | Rewrite userData + reboot → SYSTEM shell on an instance the caller can't RDP/SSH to; disables Credential Guard GPO. **High.** |
| **Any customer surface** | **AWS Nitro / attestation PKI / shared-fleet host** | — | **HARD STOP — service plane. Preserve evidence, disclose.** |

## 4. API / Interface Inventory (chapter-spanning highlights; full tables in children)
- **Mutating + managed-policy-reachable privesc:** `RunInstances` (+ `iam:PassRole`), `ec2:ModifyInstanceAttribute(userData)` (no condition keys — Lens B/E exemplar), `AssociateIamInstanceProfile`.
- **Secret-generating / secret-adjacent:** `CreateKeyPair`, `ImportKeyPair`, `GetPasswordData`, `GetInstanceTpmEkPub`, `GetInstanceUefiData` — none carry action-specific isolation condition keys.
- **Unscopable read oracles:** `DescribeKeyPairs` (blank resource, only `ec2:Region`), general `ec2:Describe*` resource-level-scoping absence.
- **Attestation / KMS gate:** `kms:Decrypt`/`GenerateDataKey` with `Recipient`; key-policy conditions `kms:RecipientAttestation:NitroTPMPCR<N>` vs enclave `:PCR<N>` (name collision), `PutKeyPolicy` (no semantic PCR validation documented).
- **Network authz:** `AuthorizeSecurityGroupIngress/Egress`, `Revoke*` (no rule-content condition keys; SG-referencing never authorized; `security-group-rule` tag-ABAC only when `TagSpecifications` present), `AssociateSecurityGroupVpc` (`ec2:Vpc` binds the SG's home VPC, not the target).
- **Console-hidden / under-documented knobs:** the Instance Identity Role endpoint; CFN KeyPair's SSM path; `ModifyInstanceMetadataOptions` (no fine-grained conditions → IMDSv2-enforcement SCPs weak).

## 5. Recommended Areas of Focus (ranked routing into the child plans)

Priority order follows Step-5 rules: AWS-authored-artifact privesc and cross-account/service-plane reach first; single-tenant and informational last.

### Area 1 — IAM / managed-policy self-escalation  →  `ec2-security-iam-attack-research-plan.md`  [CRITICAL]
Background: AWS-managed, customer-attachable policies and EC2 SLR policies. Security Concern: `EC2FastLaunchFullAccess` pairs `iam:PassRole` on `instance-profile/*`+`role/*` (gated only by `PassedToService=ec2`) with an unconditioned `RunInstances` → non-admin→admin in one artifact; **doc-vs-JSON drift** (prose claims a name restriction the shipped JSON lacks). Same pattern in `EC2FastLaunchServiceRolePolicy` (PassRole `Resource:"*"`). `AmazonEC2FullAccess` → confused-deputy via `ModifyInstanceAttribute(userData)` IMDS-cred theft. New Instance Identity Role has no documented enforcement for its "supported services" allowlist. Oracle: `iam:SimulatePrincipalPolicy`/`SimulateCustomPolicy` under a role holding exactly the artifact (no resources touched), then a scoped live launch with canary data. Severity: Critical.

### Area 2 — Attestation-conditioned KMS gate (Lens W exemplar)  →  `nitrotpm-attestation-attack-research-plan.md`  [CRITICAL-if-Principal-broad / HIGH]
Background: NitroTPM PCRs + EC2 instance attestation gating KMS. Security Concern: the gate authenticates **boot-state measurements, not caller identity**, and AWS's own Attestable-AMI recipe is public → PCR4/7/12 are deterministic from public binaries; the PCR condition's security collapses onto the `Principal` clause the docs under-emphasize. Also: single-PCR under-binding accepted by `PutKeyPolicy`; `NitroTPMPCR<N>` vs enclave `PCR<N>` name collision; validation guidance **disables CRL checking**; no replay/freshness (nonce "not used" for KMS path). Oracle: author a key policy keyed only on PCR0 / clone the public recipe and attest / submit a bogus PCR99 to `PutKeyPolicy`. Severity: Critical where key-policy `Principal` is broad; High otherwise.

### Area 3 — Cross-service secret reachability (key pairs)  →  `ec2-key-pairs-attack-research-plan.md`  [MEDIUM-HIGH]
Background: `CreateKeyPair` generates a private key; the `AWS::EC2::KeyPair` CFN resource persists it to SSM `/ec2/keypair/{id}` as a SecureString. Security Concern: create-side and read-side permissions live in **disjoint IAM namespaces** — a principal denied all `ec2:*KeyPair*` reads cleartext via `ssm:GetParameter --with-decryption`; the path input (KeyPairId) is itself discoverable via unscopable `DescribeKeyPairs` or `cloudformation:DescribeStacks`. Plus Lens S: `CreateKeyPair`/`ImportKeyPair` lack `ec2:KeyPairName` (silent non-enforcement of name-scoped policies); `ImportKeyPair` land-grab under a soon-to-exist name. Oracle: Lens T two-permission diff under a scoped role. Severity: Med-High.

### Area 4 — Network authz & SG-referencing  →  `ec2-security-groups-privatelink-attack-research-plan.md`  [HIGH / CRITICAL]
Background: SG rule authorization + PrivateLink endpoint policy. Security Concern (AWS-documented, not hypothesis): SG-**referencing** is never IAM-authorized ("only checks whether the SG exists") → IAM policies scoped to the referenced SG are inert, and cross-account references give the referenced-SG owner **zero CloudTrail visibility**; this is the normal RAM-shared/peered-VPC segmentation path. No condition key inspects rule content (`0.0.0.0/0` not IAM-deniable); `security-group-rule` tag-ABAC only fires when `TagSpecifications` is present (Revoke has no such type); unshare doesn't sever existing enforcement (Lens AA); connection-tracking lets revoked traffic survive up to 432000s. Oracle: `SimulatePrincipalPolicy` + cross-account CloudTrail diff. Severity: High/Critical.

### Area 5 — Guest boot-pipeline code exec + Windows artifacts  →  `ec2-windows-credential-guard-attack-research-plan.md`  [HIGH / MEDIUM]
Background: Credential Guard (VBS/NitroTPM-dependent), EC2Launch v2 boot pipeline, Windows best-practices + update pages. Security Concern: `ec2:ModifyInstanceAttribute(userData)` (no condition keys) feeds EC2Launch v2 `executeScript` → SYSTEM code exec at boot, able to disable the Credential-Guard GPO (chains with Area 1). AWS install pages print `Invoke-WebRequest`+`msiexec` with no hash/signature check (Lens R). Windows Update off-by-default on AWS AMIs undercuts the same page's patch recommendation (Lens U). Severity: High (code-exec lead); Medium (artifacts).

### Area 6 — Data-at-rest / Nitro isolation guarantees  →  `ec2-data-infrastructure-protection-attack-research-plan.md`  [HIGH / MEDIUM]
Background: EBS KMS encryption, encryption-in-transit, Nitro isolation claims. Security Concern: disabling/deleting a CMK does NOT revoke an attached running volume (plaintext data key cached in Nitro memory until detach — break-glass assumption false, Lens U); `ec2:KmsKeyId` present on `CreateVolume` but absent on `RunInstances`/`CopySnapshot` (approved-CMK-only policies unenforceable at launch/copy, Lens S); "always-on memory encryption" and Nitro-isolation claims are unfalsifiable from any `Describe*` API (Lens U). Severity: High (CMK-disable gap); Medium (rest).

## 6. Threat Model Test Objectives (chapter-level)

| Threat / Test Case | Component | Documented mitigation to attack | Child plan |
|---|---|---|---|
| Managed-policy holder self-escalates to admin | IAM managed/SLR policies | prose "restricted to ec2fastlaunch-named profiles" | IAM |
| Boot-measurement gate decrypts for excluded principal | NitroTPM/KMS | "attestation proves instance integrity" | NitroTPM |
| Private key read bypassing EC2 IAM wall | Key pairs / SSM | key material scoped to `ec2:*KeyPair*` | Key pairs |
| Cross-account SG posture change w/o owner audit | Security groups | IAM scoping of referenced SG + CloudTrail | SG/PrivateLink |
| SYSTEM shell via control-plane write | EC2Launch / userData | RDP/SSH + Credential Guard protect creds | Windows |
| Data served after "key disabled" | EBS/KMS/Nitro | "disable the key = break glass" | Data/Infra |
| Service-plane credential/ARN exposure | Nitro / attestation PKI | shared-responsibility line | HARD STOP — all children |

## 7. Out-of-Scope Risk Categories (chapter-wide)
- Guest-OS configuration the **customer** performs (patching cadence, in-guest hardening, their own-authored IAM policies, RDP/SSH exposure of their own SGs) — security *in* the cloud, customer-owned. (The AWS-authored artifact carve-out in §0 overrides this only for copy-verbatim AWS content.)
- AWS global-infrastructure resilience / Region-AZ isolation / compliance-program membership (Resilience + Compliance-validation topics) — prose, no queryable surface, shared-responsibility AWS side except at HARD STOP.
- IMDS reachability on a fully-managed host as a generic concern (the specific `ModifyInstanceAttribute`→IMDS-cred-theft chain IS in scope; "IMDS exists" is not).
- Single-tenant self-DoS (e.g. a customer locking their own data by deleting a CMK with no attached volume).
- Nitro/Enclaves internals, shared-fleet host memory, attestation-PKI private keys — **HARD STOP**, disclose, do not probe.

## 8. Null hypotheses / doc gaps (chapter level)
- **Compliance validation** (`compliance-validation.md`) and **Resilience** (`disaster-recovery-resiliency.md`): no API/mechanism of their own; null at hub level. Live hooks (cross-Region AMI/snapshot copy, Data Lifecycle Manager, snapshot-share revocation immediacy) carried as doc-gaps into the data-protection child (Lens AA — `ebs-modifying-snapshot-permissions.md` unread).
- Lenses that fired across the chapter: **R, S, B, E, C, T, U, W, V, AA, A, X, I, M, FF** (distribution per child §8s).
- Lenses null across all six clusters with pages named in each child §8: **F (no translation layer), G (no server-side-dereferenced URL field — profile/branding pages absent from this chapter), J (no 3P OAuth), K (no LLM/agent), N (no namespace migration), P (no registration/proofing), Q (no upload), BB/CC/DD (no multi-parser edge/authorizer/cache layer), EE (the `/aws/service/` and `/ec2/keypair/` SSM namespaces are AWS-exclusive / id-based, not land-grabbable)** — recorded with evidence, not bare N/A.
- **Carried doc-gaps for the hunter (resolve before deep investment):** (1) which KMS key encrypts the CFN KeyPair SSM SecureString (never stated); (2) whether AWS's Nitro attestation PKI publishes/uses a CRL in practice (gates the CRL-disabled validation lead); (3) whether `PutKeyPolicy` schema-validates PCR index/length (needs live confirmation); (4) SSM Patch Manager / Automation-runbook IAM docs sit outside the EC2 mirror (control-plane→guest reach unquantified); (5) Fleet/SpotFleet SLR privesc trigger path needs the API reference outside this cluster; (6) EC2 interface-endpoint TLS-floor statement absent (Lens Y open); (7) Nitro Enclaves guide tree not pulled in (likely extends Lens W).
- **Drift:** no offline/online drift found on the hub page or on the pages spot-checked by the children; `security-iam-awsmanpol.html` online twin matched the shipped JSON exactly (the IAM finding is a doc-vs-JSON *prose* drift, not a mirror sync issue).

---
### Child plans (all at `/work/aws-docs/`)
1. `ec2-security-iam-attack-research-plan.md` — IAM / managed policies / instance-profile PassRole / IMDS. **[Critical headline]**
2. `nitrotpm-attestation-attack-research-plan.md` — NitroTPM PCRs + attestation-conditioned KMS (Lens W). **[Critical-if-broad]**
3. `ec2-key-pairs-attack-research-plan.md` — key-pair secret reachability via SSM (Lens T). **[Med-High]**
4. `ec2-security-groups-privatelink-attack-research-plan.md` — SG-referencing authz + CloudTrail blind spot + PrivateLink. **[High/Critical]**
5. `ec2-windows-credential-guard-attack-research-plan.md` — EC2Launch userData→SYSTEM + Windows/CG/updates. **[High]**
6. `ec2-data-infrastructure-protection-attack-research-plan.md` — EBS/KMS encryption + Nitro isolation guarantees. **[High]**
