# Isolate data from your own operators — Attack Research Plan

**Target:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/isolate-data-operators.html
**Source of leads:** the target page (17 lines, offline mirror `docs/AWSEC2/latest/UserGuide/isolate-data-operators.md`) + its immediate cluster siblings `working-with-isolated-amis.html`, `attestable-ami.html`, `nitrotpm-attestation.html`, `nitrotpm.html`. Live page fetched 2026-09-13 — **identical to offline mirror, and carries NO injected "See also / AI-agent toolkit" block** (unlike some EC2 pages; see [[aws-docs-see-also-injection]]).
**Status:** documentation-derived hypotheses only; nothing tested against a live account.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (a Nitro host login path, EC2 host-manager access, the Nitro measurement/KMS verifier internals), stop, preserve evidence, flag for AWS-Security disclosure.
- **This is a customer-side best-practices / shared-responsibility page, not an API surface.** It defines no EC2 API, IAM action, resource, or condition key of its own. Its entire security content is one **AWS guarantee** (Nitro zero-operator-access) plus **five customer best-practice controls**. Accordingly this plan is dominated by **Lens U** (documented-guarantee-vs-actual-enforcement). The *enforcement mechanisms* that any of these leads would actually be tested against live in the **sibling control-plane plans** — this document's job is to state the boundary the page implies, prove the enforcement gap on paper, and **route the concrete API probes to the right sibling plan** rather than duplicate them.

---

## 1. Pentest Objectives (boundary-breach goals, stated as outcomes)

The page's own promise is: *"When processing highly sensitive data, you might consider restricting access to that data by preventing even your own operators from accessing the EC2 instance."* The adversary is therefore **NOT** a foreign tenant/account — it is the **customer's own same-account operator**: an IAM principal in the *same account* holding broad EC2 control-plane rights (`ec2:*`) and/or KMS admin, whom the customer wishes to exclude from the instance's plaintext data. Objectives:

- **O1.** As a same-account operator *without* in-guest interactive access, read the instance's sensitive data anyway — via a control-plane path that routes *around* all five in-guest controls (detach/snapshot/mirror/re-image), proving the five best-practices are not sufficient on their own.
- **O2.** Defeat the (implicit) attestation gate that is supposed to make O1 impossible, by re-pointing it — i.e. show the operator who is meant to be excluded can, in the same account, redefine the KMS attestation condition to admit a *malicious* replacement image (the **circular-trust** break).
- **O3.** Documentation-integrity: show the AWS-authored guidance is *incomplete* in a way that leads a diligent customer to a false sense of isolation (a compliance control built on the five bullets alone does not hold).
- **O4 (null / hard-stop).** Confirm the AWS "zero operator access" claim is enforced only by the Nitro hardware/firmware and is therefore out of scope for hunting.

---

## 2. Components, Assets, and Design

**Customer-facing interface:** none new. The page is prose guidance. It composes three pre-existing mechanisms:
1. **The AWS Nitro System "zero operator access" guarantee** (links to the Nitro whitepaper `security-design-of-aws-nitro-system/no-aws-operator-access.html`) — "no mechanism for any AWS system or person to log in to Nitro hosts, access instance memory, or access customer data on local encrypted instance storage or remote encrypted EBS." → an **AWS**-side property; enforcement = Nitro hardware/firmware = **service plane = HARD STOP**.
2. **Custom Attestable AMIs** (owned by [[attestable-ami-plan]]) → the AMI-build/measurement-provenance side.
3. **Five in-guest best-practice controls** (the payload of this page):
   - **C1** Remove all interactive access (no SSH/RDP/serial getty/SSM agent).
   - **C2** Only trusted software/code in the AMI.
   - **C3** Configure a network firewall *within the instance* (host firewall, e.g. iptables/nftables).
   - **C4** Read-only & immutable storage/filesystems (erofs/dm-verity per sibling `attestable-ami.html`).
   - **C5** Restrict instance access to authenticated, authorized, logged API calls.

**Assets to protect:** the sensitive plaintext data *inside the running instance* (memory, local encrypted instance store, attached encrypted EBS), against a **same-account privileged operator**.

**The design gap (the whole finding surface).** Controls C1–C5 all live **inside the guest**. The operator the customer wants to exclude holds the **EC2/KMS control plane**, which sits **outside the guest** and **beneath** all five controls. The page never states the two external dependencies that actually make the isolation hold:
- **(D-a)** the sensitive data must be **ephemeral** — in memory or on encrypted *instance store* that is destroyed on stop — OR any at-rest EBS/instance-store key must itself be **attestation-gated** so a re-imaged/detached copy cannot decrypt it; and
- **(D-b)** the operator to be excluded must **not hold `kms:PutKeyPolicy`** (or equivalent) on the attestation-gating key — otherwise they simply re-point the gate.

```
                         SAME AWS ACCOUNT
  ┌───────────────────────────────────────────────────────────────┐
  │  Operator IAM principal  (ec2:*, kms:*)   ◀── adversary here    │
  │        │  control plane (OUTSIDE the guest, BELOW C1–C5)        │
  │        ▼                                                        │
  │  StopInstances → DetachVolume → attach to operator box → mount  │  ← routes around C1/C3/C4
  │  CreateSnapshot → (Copy/RestoreVolume) → mount                  │  ← routes around C1/C3/C4
  │  CreateTrafficMirrorSession → operator collector                │  ← routes around C3 (host fw)
  │  EnableSerialConsoleAccess / SendSSHPublicKey / ReplaceRootVol  │  ← routes around C1/C2
  │  PutKeyPolicy (re-point PCR gate to malicious image)            │  ← breaks the attestation gate (O2)
  │        │                                                        │
  │        ▼                                                        │
  │  ┌───────────── Attestable-AMI instance (guest) ─────────────┐  │
  │  │  C1 no interactive  C2 trusted sw  C3 host fw             │  │
  │  │  C4 erofs/dm-verity C5 API-only    NitroTPM (EK persists) │  │
  │  └───────────────────────────────────────────────────────────┘ │
  └───────────────────────────────────────────────────────────────┘
        Nitro host / measurement path / KMS verifier  = AWS SERVICE PLANE = HARD STOP
```

---

## 3. Trust-Boundary Map

| # | Boundary | Owner A → Owner B | Documented control | Breach oracle |
|---|---|---|---|---|
| B1 | AWS operator → customer instance data | AWS ↔ customer | Nitro "zero operator access" (HW/FW) | An AWS identity reads instance memory/EBS/instance-store. **HARD STOP / out of scope** — enforced by Nitro silicon; not testable from a customer account. |
| B2 | **Same-account operator (control plane) → in-guest plaintext** | customer-operator ↔ customer-workload | C1–C5 (in-guest, advisory) | Operator reads plaintext via a control-plane path (detach / snapshot / mirror / re-image) that never touches C1–C5. **This is the page's real boundary.** |
| B3 | Same-account operator → attestation gate | customer-operator ↔ customer-KMS-admin | (implicit) attestation-gated secret + SoD on `kms:PutKeyPolicy` | Operator re-points the KMS `RecipientAttestation` condition to a malicious replacement image's measurements and decrypts. |
| B4 | Replacement image ↔ persistent NitroTPM identity | image build ↔ TPM key material | measurement change on stop/start & root-vol-replace (sibling `working-with-isolated-amis.html`) | A re-imaged instance still holds the *same* NitroTPM key material but new PCRs → whether that materially helps/hurts the operator (see A-2). |

---

## 4. API / Interface Inventory

**The page defines none.** The operator's bypass toolkit is drawn entirely from *existing* EC2/KMS control-plane actions, catalogued here **only to route them** — audit each in the named sibling plan, not here:

| Operator action (bypasses which control) | Mutating | Callable by same-acct operator | Routed to |
|---|---|---|---|
| `ec2:StopInstances` → `ec2:DetachVolume` → attach-elsewhere → mount (C1/C3/C4) | Y | yes if `ec2:*` | [[stop-start-plan]], [[ebs-storage-plan]] |
| `ec2:CreateSnapshot` → copy/share/restore → mount (C1/C4) | Y | yes | [[ebs-storage-plan]], [[copying-amis-plan]], [[sharing-amis-plan]] |
| `ec2:CreateTrafficMirrorSession` → operator collector (C3 host-firewall) | Y | yes | *no dedicated sibling — see Area 3, flag for a Traffic-Mirroring plan* |
| `ec2:EnableSerialConsoleAccess` + serial console (C1) | Y | yes (account-level) | [[serial-console-plan]] |
| `ec2:SendSSHPublicKey` / EC2 Instance Connect (C1) | Y | yes | [[connect-linux-eic-plan]] |
| `ec2:ModifyInstanceAttribute --user-data` (C1/C2, requires stop) | Y | yes | [[stop-start-plan]], [[enhanced-networking-plan]] (userData-as-root exemplar) |
| `ec2:ReplaceRootVolume` / re-image with malicious AMI (C1/C2) | Y | yes | [[win-fast-launch-plan]]/[[attestable-ami-plan]] (RegisterImage), `working-with-isolated-amis.html` |
| `kms:PutKeyPolicy` on the attestation key (B3 gate) | Y | yes if kms admin | [[nitrotpm-attestation-plan]] (AF-3 PCR-value acceptance) |

None is *new*, none is documented on this page, and — the point — none is gated by anything the five in-guest controls can influence.

---

## 5. Recommended Areas of Focus

### Area 1 ⭐ (crown jewel) — The five in-guest controls do not bind the same-account operator's control plane (Lens U + Lens X-shaped bypass)

**Background.** The page's stated goal is preventing *"even your own operators from accessing the EC2 instance."* It then lists five controls (C1–C5) that are **all in-guest**. The operator to be excluded, however, is a control-plane principal.

**Security Concern.** Every one of C1–C5 is defeated by a same-account control-plane action that never enters the guest, so a customer who implements exactly the five bullets and stores sensitive data on an attached EBS volume (or on any storage that survives a stop) is **not** isolated from their own operator. The page states no additional requirement.

**High-level Test Scenarios (falsifiable claims):**
- **A-1a (detach path).** *Claim:* an operator holding `ec2:StopInstances`+`ec2:DetachVolume`+`ec2:AttachVolume` reads the instance's data by stopping it, detaching the (encrypted) root/data EBS volume, and attaching it to an operator-controlled instance — **C1/C3/C4 never evaluated**. *Mechanism:* page lists only in-guest controls; EBS default KMS key is decryptable by any same-account principal with `kms:Decrypt` via `kms:ViaService=ec2` (see [[ebs-storage-plan]], [[bdm-concepts-plan]]). *Oracle:* plaintext of a canary file appears on the operator box. *Precondition:* data at rest on EBS (not memory/instance-store only). *Severity:* the *isolation guarantee fails*, but this is a **customer-side shared-responsibility footgun** if the customer chose EBS-at-rest + didn't attestation-gate the volume key → **Low/Informational** as a *bug*; the **doc omission is the reportable part** (Area 4).
- **A-1b (snapshot path).** *Claim:* `ec2:CreateSnapshot` on the volume → `CreateVolume`/restore → mount reads the same data without ever stopping the target. *Oracle:* canary in a snapshot the operator restores. Route to [[ebs-storage-plan]] (ParentSnapshot / createVolumePermission divergence).
- **A-1c (traffic mirror path).** *Claim:* `ec2:CreateTrafficMirrorSession` copies the instance's live network traffic to an operator-owned target, defeating **C3** (the *in-guest* firewall does not see the mirror, which taps at the ENI/Nitro layer). *Oracle:* sensitive bytes in transit appear at the operator collector. *Severity:* Medium if the workload transmits sensitive data in cleartext internally; Low if TLS-everywhere. **No sibling plan covers Traffic Mirroring — recommend a dedicated `traffic-mirroring` plan.**
- **A-1d (serial / EIC re-entry).** *Claim:* even with C1 "interactive access removed," `ec2:EnableSerialConsoleAccess` (account-level toggle) + `ec2:SendSSHPublicKey` re-introduce an access path **iff** the AMI still runs a getty/sshd — the attestable AMI *should* have neither, so this is the control that C1+C2 actually defend; test whether an operator can `ReplaceRootVolume`/re-image to *re-add* one (→ Area 2). Route: [[serial-console-plan]], [[connect-linux-eic-plan]].

**Doc evidence:** target page bullets 1–5; `working-with-isolated-amis.html` ("no way for any user or operator to connect… no way to install or update software after launch"). **Severity-if-true:** as a *bug*, Low/Informational (customer-authored config + customer's own operator = footgun, per skill severity carve-out). As a *doc-completeness defect*, see Area 4.

---

### Area 2 ⭐ (crown jewel) — The attestation gate is circular: the excluded operator controls the gate (Lens U + Lens W + Lens R/S)

**Background.** The only thing that turns C1–C5 from advisory into *enforced* is attestation-gating the sensitive secret to KMS (so a detached/re-imaged copy cannot decrypt). Sibling `working-with-isolated-amis.html` states plainly: *"An instance retains its NitroTPM key material for the entire instance lifecycle, and persists through stop/starts and root volume replacement operations"* and that stop/start or root-volume-replacement **change the reference measurements** — *"you must update your KMS key policy to the new reference measurements."*

**Security Concern.** The customer's own operator — the adversary — is in the **same account** and typically holds KMS admin (`kms:PutKeyPolicy`). So the operator can: (1) `ReplaceRootVolume` with a **malicious** AMI that re-adds interactive access (defeating C1/C2); (2) the instance keeps its NitroTPM key material but now presents *new* PCRs so KMS attestation fails; (3) the operator **updates the KMS key policy** (`PutKeyPolicy`) to the malicious image's measurements — exactly the documented remediation for a legitimate re-image — and now the malicious instance attests successfully and decrypts the secret, which the operator reads over the re-added SSH. **The gate that is supposed to exclude the operator is administered by the operator.** The page never states the required separation of duties (operator must *not* hold `kms:PutKeyPolicy`/`kms:*` on the attestation key, nor `ec2:ReplaceRootVolume`/`RegisterImage`).

**High-level Test Scenarios:**
- **A-2a.** *Claim:* a principal that can `ReplaceRootVolume`/`RegisterImage` **and** `kms:PutKeyPolicy` on the attestation key can, end-to-end, launch a malicious replacement, re-point the PCR condition, and decrypt the protected secret. *Oracle:* the canary secret decrypts under a malicious-measurement instance. *Precondition:* operator role holds both action families (the common "EC2 admin also KMS admin" reality). *Severity:* the isolation goal is fully defeated; but customer-authored role scoping → **Low/Informational as a bug**, **reportable as a doc/guidance gap** (Area 4).
- **A-2b (PCR-value acceptance — Tier-2 hook).** *Claim:* `PutKeyPolicy` accepts an attacker-chosen/under-binding/wildcard/all-zero `kms:RecipientAttestation:PCR*` value with no schema validation, making the re-point trivial and silent. *This is the AWS-side enforcement question* and is **owned by [[nitrotpm-attestation-plan]] AF-3/AF-4** — do not re-hunt here; cite it as the dependency.
- **A-2c (measurement self-assertion).** *Claim:* the malicious replacement AMI's reference measurements are computed by the operator's own `nitro-tpm-pcr-compute` (public, deterministic, unsigned by AWS) — so the operator can produce a valid baseline for their malicious image at will. Owned by [[attestable-ami-plan]] Area 2 — cite, don't re-hunt.

**Doc evidence:** `working-with-isolated-amis.html` (NitroTPM key material persists across root-volume replacement; "update your KMS key policy to the new reference measurements"); [[nitrotpm-attestation-plan]] AF-1/AF-3. **Severity-if-true:** isolation defeated; **reportable slice = the AWS best-practices page omits the mandatory SoD constraint** → Informational/Low, `aws-security` doc-integrity.

---

### Area 3 — Traffic-mirror & ENI-layer taps vs the "in-guest firewall" control (Lens V / Lens D shaped)

**Background.** C3 tells customers to *"configure a network firewall within the instance."* An in-guest firewall filters what the guest OS sees; it cannot see a tap placed at the ENI/Nitro layer by the control plane.

**Security Concern.** `ec2:CreateTrafficMirrorSession`/`CreateTrafficMirrorTarget` (and, at the SG layer, `ec2:ModifyNetworkInterfaceAttribute --groups`, `AuthorizeSecurityGroupIngress`) let the same-account operator observe or reach the instance's network *below* C3. This is the network-boundary analogue of Area 1's storage bypass.

**Test Scenarios:** **A-3a** operator mirrors the target ENI to an operator collector and captures internal cleartext; **A-3b** operator swaps the ENI's security groups to open an ingress path the in-guest firewall would still block at L7 but that exposes a listening service. *Oracle:* traffic/connection reaching the operator that C3 was meant to stop. *Severity:* Medium if internal traffic is sensitive+cleartext; else Low. **Gap:** no sibling plan covers VPC Traffic Mirroring — **recommend spawning a `traffic-mirroring` questionbuilder pass** for `ec2:*TrafficMirror*` (is there any ownership/attestation condition key? almost certainly not → Lens S "key does not exist").

---

### Area 4 ⭐ (the reportable one) — Documentation-completeness defect in AWS-authored guidance (Lens U, doc-vs-enforcement integrity)

**Background.** This is an AWS-authored best-practices page a customer follows verbatim to build a compliance/isolation control.

**Security Concern.** The page presents C1–C5 as *the* way to *"prevent even your own operators from accessing the EC2 instance,"* but **omits both external dependencies that the isolation actually requires** (D-a: data must be ephemeral or its at-rest key attestation-gated; D-b: the operator must be denied `kms:PutKeyPolicy`/`ReplaceRootVolume`/`RegisterImage` — separation of duties). A customer who implements exactly the five bullets and stores data on EBS, while the operator retains normal EC2+KMS admin, has **no isolation at all** (Areas 1–2). The guidance therefore induces a false sense of security.

**Test Scenarios (documentation oracles, no live account needed):**
- **A-4a.** Does the page (or any linked page reachable in ≤1 hop) state the ephemerality/attestation-gate requirement (D-a)? *Refute oracle:* find such a sentence. *Current read: absent.*
- **A-4b.** Does it state the separation-of-duties requirement on `kms:PutKeyPolicy`/re-image (D-b)? *Current read: absent* — and `working-with-isolated-amis.html` actively tells the reader to *update the KMS key policy* on re-image, reinforcing the operator-holds-the-gate assumption.
- **A-4c.** Does it warn that the five controls do not defend the detach/snapshot/mirror control-plane paths? *Current read: absent.*

**Doc evidence:** the target page (five bullets, no external-dependency caveat); `working-with-isolated-amis.html`. **Severity:** Informational/Low, **but AWS-owned and worth filing** — a customer could build an attestation/compliance claim on incomplete guidance (exactly the Lens-U reporting rationale). Route `aws-security` doc-integrity, **Tier-2-adjacent** (AWS-authored guidance, copied verbatim into customer runbooks).

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Operator detaches encrypted EBS and mounts elsewhere | EBS + KMS default key | in-guest C1/C3/C4 (do not apply to control plane) |
| Operator snapshots + restores the volume | EBS snapshot | C4 immutability (integrity only, not confidentiality) |
| Operator mirrors ENI traffic | VPC Traffic Mirroring | C3 in-guest firewall (below-guest tap, not covered) |
| Operator re-images with a malicious AMI + re-points KMS PCR policy | ReplaceRootVolume + `kms:PutKeyPolicy` + NitroTPM persistence | attestation gate — but administered by the very operator (circular) |
| Operator re-enables serial/EIC on a re-imaged instance | serial console / EC2 Instance Connect | C1 "remove interactive access" (defeated by re-image) |
| AWS operator reads instance memory/data | Nitro host | Nitro zero-operator-access (HW/FW) — **out of scope, HARD STOP** |

---

## 7. Out-of-Scope Risk Categories

- **The AWS Nitro "zero operator access" guarantee (B1).** Enforced by Nitro silicon/firmware; not reachable or falsifiable from a customer account. Any evidence touching a Nitro host / the KMS attestation verifier internals = **HARD STOP, service plane.**
- **Cross-account / cross-tenant.** This page's threat model is strictly **intra-account** (your *own* operators). No shared fleet, no cross-tenant resource, no foreign identifier. Lens A/B/C/D-cross-tenant/N/AA do not fire *here* (they fire on the sibling API plans).
- **Customer-authored least-privilege footguns as *bugs*.** The operator's IAM role scope and the customer's data-at-rest/key-gating choices are customer-authored → footgun, **Low/Informational**. The *AWS-authored doc omission* (Area 4) is the in-scope reportable slice.
- **The AMI build/measurement supply chain and the KMS PCR-gate enforcement** → owned by [[attestable-ami-plan]] and [[nitrotpm-attestation-plan]]; cite as dependencies, do not re-hunt.
- **IMDS on the managed host, DNS rebinding against private endpoints** — not raised by this page.

---

## 8. Null hypotheses / doc gaps

- **Lenses that do NOT fire on this page (no trigger present, pages checked = the target + `working-with-isolated-amis.html` + `attestable-ami.html`):** A (cross-tenant — intra-account only), B/C (no role ARN passed, no credential vending on this page), F (no translator/parser), G (no server-side URL deref — the only URLs are the Nitro whitepaper and kernel-doc links, none fetched by a service), H/I (no KMS-context/tag surface on *this* page — lives in siblings), J (no OAuth/3P), K (no LLM/agent), L (no parser/size limit), M (no shared session id), N (no namespace migration), O (no audit surface defined here), P (no registration/OTP), Q (no upload on this page), Y (no transport/sig surface), AA (no share/revoke on this page). Record each as an **explicit null**, not silence.
- **Lenses that DO fire:** **U** (Areas 1/2/4 — the whole page is a guarantee-vs-enforcement study), **W** (Area 2, attestation gate — but the enforcement is owned by [[nitrotpm-attestation-plan]]), **V** (Area 3, traffic mirror below the in-guest firewall), **R/S** (Area 2 — does the operator role artifact pair `ec2:ReplaceRootVolume`/`RegisterImage` with `kms:PutKeyPolicy` unconditioned; is there any condition key to bind the attestation key to a role — likely "key does not exist").
- **Doc gaps to confirm live before a hunter invests:**
  1. Is EBS-at-rest under the *default* aws/ebs key decryptable by any same-account `kms:Decrypt` holder without an explicit key-policy grant? (Confirms A-1a reachability — [[ebs-storage-plan]].)
  2. Does `kms:PutKeyPolicy` accept an arbitrary/under-binding `RecipientAttestation:PCR*` value with no schema check? (A-2b — owned by [[nitrotpm-attestation-plan]] AF-3/AF-4.)
  3. Does any EC2 or KMS **condition key** exist that lets a customer forbid an operator from `ReplaceRootVolume`/re-image *of an attestable instance* or from editing the attestation key? (Likely **Lens S "key does not exist"** → the SoD is enforceable only by coarse action-level denies, which the page never mentions.)
  4. Does VPC Traffic Mirroring expose any ownership/attestation condition key (Area 3)? Almost certainly not → recommend a dedicated `traffic-mirroring` pass.

---

## Cross-references
Related plans (do not duplicate — cite): [[nitrotpm-attestation-plan]] (KMS PCR gate, fail-open, PutKeyPolicy value acceptance), [[attestable-ami-plan]] (build/measurement provenance, self-asserted PCRs), [[nitrotpm-plan]] (EK/instance identity), [[ebs-storage-plan]] + [[bdm-concepts-plan]] (detach/snapshot/default-key decrypt), [[copying-amis-plan]]/[[sharing-amis-plan]] (snapshot vend), [[serial-console-plan]]/[[connect-linux-eic-plan]] (re-entry), [[stop-start-plan]] (userData-as-root, stop mechanics), [[aws-docs-see-also-injection]] (this page is clean).
