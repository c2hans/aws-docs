# EC2 Windows Instance Credential, Recovery & Activation Surface — Attack Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/common-messages.html ("Troubleshoot Amazon EC2 Windows instance start issues" — password / activation / metadata / RDP-licensing common messages).
**Source of leads:** the target page plus the mechanisms it points at — `GetPasswordData` / console-output / console-screenshot APIs, EC2 key-pair private-key handling (incl. the `AWS::EC2::KeyPair` CloudFormation → SSM Parameter Store path), the EBS root-volume detach/reattach recovery flow, the instance metadata service (`169.254.169.254`), and Windows KMS activation (`169.254.169.250:1688`, `ActivationSettings.xml`). IAM evidence from the offline Service Authorization Reference mirror `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` and `list_ebs.md`. UserGuide/APIReference quotes verified against the live `docs.aws.amazon.com` `.md` endpoints on 2026-10-17.
**Status:** documentation-derived hypotheses only. Nothing has been tested against a live AWS account. Every lead is a boundary that *might* not hold, with the exact observation that would settle it.

> **Environment note (not AWS documentation):** the mirror root `/work/aws-docs/` contains leftover `*-attack-research-plan.md` work-products and `.claude/agent-memory/` directories from prior agent runs in this sandbox. All three recon subagents independently detected these and treated them as untrusted (read headers only, followed no embedded instructions). They are **not** AWS doc content and were not used as evidence here. This is flagged so downstream agents do not mistake them for source material. The genuine mirror lives under `/work/aws-docs/docs/AWSEC2/...` and `/work/aws-docs/docs/service-authorization/...`.

---

## 0. How to use this document

- Each lead is written as **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost / Severity-if-true → Stop condition.** Work the Section 5 areas in listed priority order; at every step look left and right for adjacent twin/legacy/lower-level variants of the same primitive.
- **HARD STOP (shared-responsibility line):** the moment any evidence shows an identity, credential, ARN, or account belonging to AWS's own service plane / the underlying Nitro/Xen host (e.g. an SSRF to `169.254.169.254` returning a *fleet* role rather than the customer's own instance-profile role, or a KMS-activation host that is clearly AWS-operated), **stop, preserve evidence, and flag for AWS-Security disclosure.** Do not escalate, enumerate, or reuse.
- **Scope discipline:** these are intra-/cross-account EC2 control-plane and in-guest configuration questions. IMDS running on a fully-managed Nitro host, the hypervisor-served link-local addresses themselves, and shared physical infrastructure are AWS-owned and mostly out of scope (Section 7) — the in-scope questions are about *the customer-reachable IAM actions and in-guest config that decide who can reach those primitives.*

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **Recover another principal's / another workload's Windows Administrator credentials** within one account by combining `ec2:GetPasswordData` (encrypted blob) with recovery of the matching private key from SSM Parameter Store (`/ec2/keypair/{key_pair_id}`) via `ssm:GetParameter` — proving a secret wall on the EC2 side is bypassable on the SSM side.
2. **Read another workload's disk data** by exercising the documented root-volume detach→attach-to-my-instance recovery flow against a volume I do not own, where IAM scoping does not bind volume-owner to instance-owner.
3. **Escalate from `ec2:ModifyInstanceAttribute` to code execution as an instance-profile role** by rewriting `userData` with no `iam:PassRole` in path.
4. **Read raw snapshot bytes via the EBS direct APIs** (`ebs:GetSnapshotBlock`) on a snapshot shared/reachable under weaker IAM than the EC2 control plane requires.
5. **Steal a running instance's live IAM-role credentials** via an in-guest SSRF/open-proxy relay to the IMDS credentials endpoint — gated by whether IMDSv2 is enforced.
6. **Subvert Windows activation integrity** by repointing the locally-editable `TargetKMSServer` / `slmgr /skms` target (or via `ReadFromUserData`), and characterize the unauthenticated plaintext activation channel.
7. For every lead: confirm **existence only**, under a **least-privilege scoped role**, with **synthetic canary data** — never dump real data, never cross into the AWS service plane.

---

## 2. Components, Assets, and Design

**Customer-facing interfaces exercised by this page**
- **EC2 control-plane APIs** (SigV4): `GetPasswordData`, `GetConsoleOutput`, `GetConsoleScreenshot`, `CreateKeyPair`/`DeleteKeyPair`, `AttachVolume`/`DetachVolume`, `ModifyInstanceAttribute`, `ModifySnapshotAttribute`, `CreateSnapshot`.
- **SSM Parameter Store** (`ssm:GetParameter`) — *cross-service* resting place for CloudFormation-created key-pair private keys.
- **EBS direct APIs** (`ebs:GetSnapshotBlock`, `ebs:ListSnapshotBlocks`) — a separate REST/JSON service (`ebs-2019-11-02`) with its own IAM namespace and byte-granular reads.
- **In-guest surfaces:** RDP (TCP 3389), the EC2Config/EC2Launch/EC2Launch v2 agents, `ActivationSettings.xml` / `config.xml` on the instance filesystem, `slmgr.vbs`.
- **Link-local host services** (served by Nitro/Xen, *not* the instance): IMDS `169.254.169.254`, Microsoft-KMS activation `169.254.169.250:1688` and `169.254.169.251`, Route 53 Resolver `169.254.169.253`, Time Sync `169.254.169.123`.

**Processes / runtimes behind the interface**
- In-guest launch agents: **EC2Config** (Server 2012 R2 and earlier), **EC2Launch** (2016/2019), **EC2Launch v2** (2022+). These *generate* the Administrator password at first boot and *encrypt* it with the public half of the launch key pair.
- The AWS control plane serves the already-encrypted `passwordData` blob — AWS never holds the private key and never decrypts (decryption is client-side).

**Accounts / trust zones**
- **Customer account** owns instances, volumes, snapshots, key pairs, SSM parameters.
- **AWS service plane / underlying host** owns the Nitro/Xen controller that answers the link-local addresses. `using-instance-addressing.md`: *"These services run on the underlying host, not on the instance… The underlying host handles traffic to these reserved addresses… Security groups and network ACLs do not filter this traffic."* This is the hard shared-responsibility line.
- No multi-tenant *service* account is exposed by this page — the only multi-tenancy here is **intra-account cross-workload / cross-team** (the realistic blast radius for most leads) plus the AWS-owned host plane (hard stop).

**Resource identifiers & entropy**
- `InstanceId` (`i-...`), `VolumeId` (`vol-...`), `SnapshotId` (`snap-...`), `KeyPairId` (`key-...`) — account-internal but **enumerable/discoverable within the account** via `Describe*`; the SSM private-key parameter name is **deterministically derived** from the public `KeyPairId`: `/ec2/keypair/{key_pair_id}`.

**Identity / credentials in play**
- Key-pair **private key** = the decryption credential for the Windows password; the headline asset.
- Instance-profile role creds, vended at IMDS `iam/security-credentials/<role>`.
- Windows Administrator password (RSA-encrypted-at-rest blob returned by `GetPasswordData`).

**Where untrusted / caller-controlled data enters & transforms**
- `userData` → consumed by the launch agent at boot and executed (EC2Launch v2 `.run-once`) → downstream action with the instance-profile role (injection seam, Lens B/E).
- `ActivationSettings.xml` `ReadFromUserData` → KMS target taken from user data (seam, Lens V).
- The EC2 console output / screenshot → base64 blobs returned to the caller (info-leak surface, Lens O/U).

```
                      ┌──────────────────────────────────────────────┐
  caller (IAM) ──────▶│ EC2 control plane (SigV4)                     │
   GetPasswordData ──▶│   returns passwordData = RSA(pubkey, pw)      │
   Modify…Attribute ─▶│   userData rewrite ─▶ agent boot ─▶ role creds│
   Attach/DetachVol ─▶│   volume⇄instance (only AZ cross-checked)     │
  └── ssm:GetParameter│──▶ SSM Param Store  /ec2/keypair/{KeyPairId}  │ ◀── private key (CFN-created pairs)
  └── ebs:GetSnapshot…│──▶ EBS direct API (ebs-2019-11-02) raw blocks │
                      └───────────────┬──────────────────────────────┘
   in-guest ─ RDP 3389 ◀── decrypt(privkey, passwordData) [client-side]
   in-guest ─ ActivationSettings.xml / slmgr /skms ─▶ 169.254.169.250:1688 (MS-KMS, plaintext)
   in-guest ─ app / proxy / SSRF ─▶ 169.254.169.254 iam/security-credentials/<role>  [AWS host plane — HARD STOP if fleet identity]
```

---

## 3. API / Interface Inventory

| Name | Method | Mutating | Facing | Functionality | Callable from Internet | Authorized callers | Notes / lens |
|---|---|---|---|---|---|---|---|
| `ec2:GetPasswordData` | SigV4 | Non-mut (Read) | External | Returns RSA-encrypted Admin password for a Windows instance | Yes | Resource `instance*`; scoped by `ec2:ResourceTag`,`ec2:InstanceID`,`ec2:Region`,etc. | **A / C / X** — returns a credential-bearing blob by instance ID |
| `ec2:GetConsoleOutput` | SigV4 | Read | External | Console/system log; Windows = last 3 system-event-log errors; incl. agent version + RDP cert thumbprint | Yes | Resource `instance*`, same key family | **A / O / X** — info leak |
| `ec2:GetConsoleScreenshot` | SigV4 | Read | External | JPG screenshot of running instance desktop | Yes | Resource `instance*`, same key family | **A / O / X** — can capture on-screen secrets |
| `ssm:GetParameter` (`--with-decryption`) | SigV4 | Read | External | Reads `/ec2/keypair/{key_pair_id}` = private key (CFN-created pairs) | Yes | Resource = parameter ARN; `ssm:*` namespace | **T** — the cross-service wall-bypass |
| `ec2:AttachVolume` | SigV4 | Mutating | External | Attach EBS volume to an instance | Yes | Requires `instance*` **and** `volume*`; only AZ cross-checked | **A / S** — cross-workload disk read |
| `ec2:DetachVolume` (+`Force`) | SigV4 | Mutating | External | Detach volume (Force = no FS flush) | Yes | `volume*` (+optional `instance`) | **A / S / L** — `Force` not separately gated |
| `ec2:ModifyInstanceAttribute` | SigV4 | Mutating | External | Modify instance attribute incl. `userData` | Yes | `instance*`; `ec2:Attribute/${AttributeName}` key available | **B / E / S** — userData→role-exec privesc |
| `ec2:ModifySnapshotAttribute` | SigV4 | Mutating | External | Set `createVolumePermission` (UserId / `all`) | Yes | `snapshot*` | **AA** — public share, no grantee validation |
| `ebs:GetSnapshotBlock` / `ListSnapshotBlocks` | REST/SigV4 | Read | External | Raw snapshot block bytes / block index | Yes | `ebs:*` prefix; `snapshot*`; narrower key set (no owner key); KMS for encrypted | **X** — lower-level twin of control-plane read |
| `ec2:ModifyInstanceMetadataOptions` | SigV4 | Mutating | External | Set `HttpTokens` (optional/required), hop limit, endpoint | Yes | `instance*`; gateable by `ec2:MetadataHttpTokens` etc. | **V / U** — IMDSv2 enforcement toggle |
| In-guest `slmgr.vbs /skms <ip:port>` / `ActivationSettings.xml` | local | Mutating (local) | In-guest | Repoint Windows KMS activation target | No (local) | any sufficiently-privileged guest process | **V / Y** — locally editable, incl. `ReadFromUserData` |
| IMDS `GET …/iam/security-credentials/<role>` | HTTP (link-local) | Read | In-guest / host plane | Returns live role creds (IMDSv1 = no token) | No (link-local) | any on-instance caller within hop limit | **G** — SSRF target; **HARD STOP if fleet identity** |

**Non-SDK / easily-overlooked:** the **EBS direct APIs** (`ebs:GetSnapshotBlock`) are a separate service most IAM reviews never model — flag every policy that grants `ebs:*`. The **SSM key-pair parameter** path is derivable from a *public* identifier and is retrievable by anyone with `ssm:GetParameter` on it even if denied `ec2:GetPasswordData`.

---

## 4–5. Recommended Areas of Focus (one block per firing lens, priority order)

### AREA 1 — [HIGHEST] Key-pair private key reachable via SSM bypasses the EC2 password wall (Lens T + C + chain to A)

**Background.** For CloudFormation-created key pairs (`AWS::EC2::KeyPair`), `create-key-pairs.html` states: *"When you create a new key pair using CloudFormation, the private key is saved to AWS Systems Manager Parameter Store. The parameter name has the following format: `/ec2/keypair/{key_pair_id}`"* and shows the retrieval verbatim: `aws ssm get-parameter --name /ec2/keypair/key-05abb699beEXAMPLE --with-decryption …`. The private key is the sole credential needed to decrypt the `passwordData` blob that `GetPasswordData` returns (`ec2-key-pairs.html`: *"the private key is required to decrypt the administrator password"*). The `KeyPairId` is treated as non-secret (listed by `describe-key-pairs`).

**Security Concern.** The EC2 side implies a wall — *"Amazon EC2 doesn't keep a copy of your private key"* (`ec2-key-pairs.html`) — but the CloudFormation path silently re-homes that private key into SSM Parameter Store under a path **deterministically derived from a public identifier**, governed by a **different IAM action in a different service namespace** (`ssm:GetParameter`, not `ec2:GetPasswordData`). A principal explicitly denied `ec2:GetPasswordData` (or who has it but lacks the key) may still read the cleartext private key from SSM, then combine it with a `GetPasswordData` blob to obtain Administrator access.

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** a role with `ssm:GetParameter` on `/ec2/keypair/*` but **no** `ec2:GetPasswordData` can still recover the private key for a key pair it does not "own." → **Oracle:** `get-parameter --with-decryption` returns PEM material for a `key-...` id discovered via `describe-key-pairs`. → Sev **High** (intra-account credential recovery).
- **Claim:** the SSM parameter is `SecureString` under the **AWS-managed** `alias/aws/ssm` key, so `kms:Decrypt` is delegated via `kms:ViaService` and the caller needs no explicit KMS grant. → **Oracle:** `--with-decryption` succeeds under a role with no `kms:*` statement. → Sev **Medium–High**. *(Doc-gap: the EC2 page does not restate "SecureString"/`alias/aws/ssm` inline — confirm the parameter Type and KMS key first.)*
- **Claim:** the private-key parameter **outlives** the key pair / stack (no cascade delete) → stale credential lingers. → **Oracle:** delete the key pair; `get-parameter` still returns the PEM.
- **Chain:** SSM private key + `GetPasswordData` blob → decrypt Admin password → RDP as Administrator of a workload the caller was not granted. Rate at the **end** of the chain = **High**.

**Preconditions:** key pair created via CloudFormation; caller holds `ssm:GetParameter` (often granted broadly). **Cost:** low. **Stop condition:** PEM retrieved for one non-owned key pair = confirmed; stop (do not harvest further keys).
**Owner-to-fix:** shared — AWS owns the managed-key delegation + the "store the private key in SSM" design choice and the public-id-derived path; the customer owns the least-privilege composition. Reportable as a design concern because the storage decision and path shape are AWS-authored.

---

### AREA 2 — [HIGH] `GetPasswordData` / console-output / screenshot: ownership binding & twin parity (Lens A + X + O)

**Background.** All three — `GetPasswordData`, `GetConsoleOutput`, `GetConsoleScreenshot` — gate on a **single IAM action against resource type `instance*`**, scoped only by standard EC2 condition keys (`aws:ResourceTag`, `ec2:InstanceID`, `ec2:ResourceTag`, `ec2:Region`, instance-attribute keys). **No doc prose anywhere states "the instance must belong to the caller's account"** — ownership is implicit in the account-scoped ARN only. `connect-rdp.html`: *"Your account must have permission to call the GetPasswordData action."*

**Security Concern.** Within an account, if any of these is granted on `Resource:"*"` (or without tag/ID scoping), a low-privilege or cross-team principal can read **every** Windows instance's encrypted password blob, **every** console log (which `GetConsoleOutput` docs say includes the *last three system event-log errors* plus the RDP cert thumbprint and agent version), and **every** desktop screenshot — a direct cross-workload info/credential-exposure path. Because they are three sibling reads of overlapping instance state, a Deny written for one may be absent on another (twin-parity gap).

**High-level Test Scenarios:**
- **Claim:** `GetPasswordData` returns a non-empty blob for an instance the caller does not administer, when IAM is wildcard-scoped. → **Oracle:** non-empty `passwordData` for a foreign `i-...`. → Sev **High** (combined with Area 1 private key = Admin).
- **Claim:** a policy that Denies `GetPasswordData` on sensitive instances leaves `GetConsoleScreenshot` / `GetConsoleOutput` **un-denied**, exposing the same secrets by another door (screenshot of a logon banner / credential-manager window; cert thumbprint; event-log error text). → **Oracle:** screenshot/console returns for the instance the password-Deny was meant to protect.
- **Claim (enumeration oracle):** distinct error/latency/empty-vs-404 behavior across these reads lets a caller enumerate which `i-...` exist / are Windows / have password-gen enabled. → **Oracle:** differential responses (Lens A variant: 500-vs-400-vs-200-empty).

**Preconditions:** wildcard or loosely-tagged grant of the read actions. **Cost:** low. **Severity:** cross-workload credential/info exposure = **High** intra-account; **note** cross-*account* is blocked by the ARN namespace (null for cross-account unless an SSRF/assumed-role path crosses it). **Stop:** one foreign read confirmed.

---

### AREA 3 — [HIGH] `ModifyInstanceAttribute(userData)` → code execution as instance-profile role, no PassRole (Lens B/E + S)

**Background.** The recovery procedures on the target page rely on editing in-guest launch behavior; the control-plane equivalent is `ec2:ModifyInstanceAttribute`, which the IAM reference shows supports the `ec2:Attribute/${AttributeName}` condition key against `instance*`. `userData` is executed by the launch agent at (re)boot; EC2Launch v2's `.run-once` mechanism re-runs once-only tasks (the target page's reset flow deletes `.run-once` and warns *"Any scripts set to run once will be triggered by this action."*).

**Security Concern.** A principal with `ec2:ModifyInstanceAttribute` (and stop/start) but **no `iam:PassRole`** can rewrite `userData` on an instance that already has an instance profile, then reboot → the injected script runs **as the instance-profile role** — privilege escalation that never touches `iam:PassRole`. This is the corpus's confirmed PassRole-adjacent exemplar.

**High-level Test Scenarios:**
- **Claim:** `ModifyInstanceAttribute --attribute userData` succeeds without `iam:PassRole` on an instance with an attached richer role; reboot executes attacker script with that role's creds. → **Oracle:** canary action (e.g. write a tagged canary object) performed under the instance-profile role after reboot. → Sev **High–Critical** (depends on role).
- **Claim (Lens S case-sensitivity fail-open):** a Deny keyed on `ec2:Attribute` written with the lowercase enum (`userData` vs the request's casing) is **inert**, because the key is populated with the PascalCase request field — the Deny does not match and the modify proceeds. → **Oracle:** a policy intended to block `userData` edits still allows them due to casing. → Sev **High** (the control that should stop this area is itself defeated).

**Preconditions:** target instance has an instance profile; caller holds ModifyInstanceAttribute + reboot. **Cost:** low (own canary instance). **Stop:** canary role action observed once. **HARD STOP** if the role turns out to be an AWS service-linked / fleet role.

---

### AREA 4 — [HIGH] EBS detach/attach recovery flow = cross-workload disk read; `ebs:GetSnapshotBlock` lower-level twin (Lens A + S + X + AA)

**Background.** The target page's metadata-recovery procedure is: stop the affected instance, **detach its root volume, attach it to a *temporary* instance, read/edit it, reattach.** The IAM reference shows `AttachVolume`/`DetachVolume` require resource types `instance*` **and** `volume*` but the only platform-enforced cross-check is **Availability Zone** (`API_AttachVolume.html`: *"The volume and instance must be within the same Availability Zone"*). There is **no** documented "volume-owner must equal instance-owner" binding and **no "original instance only" guarantee**; `ebs-attaching-volume.html` even documents the disk-signature-collision side effect of attaching a foreign root volume.

**Security Concern.** If `ec2:AttachVolume` is granted without tying volume and instance scopes together (e.g. `Resource:"*"`, or tags that the caller can also set), a principal can attach **another workload's volume to its own instance and read all its data** — exactly the recovery flow, pointed at a volume it doesn't own. `DetachVolume`'s `Force` is a request parameter, not a separate permission, so anyone with detach can force-detach (data-loss / availability angle). Separately, the **EBS direct APIs** (`ebs:GetSnapshotBlock`/`ListSnapshotBlocks`) read snapshot bytes under a **different service prefix with a narrower condition-key set and no owner key**, bypassing the EC2 "create a volume then mount it" path entirely.

**High-level Test Scenarios:**
- **Claim:** a role with `ec2:AttachVolume`/`DetachVolume` scoped only by AZ/`*` can attach a canary volume owned by a *different* role/tag to the caller's instance and read its filesystem. → **Oracle:** canary file written to volume B (by role B) is read from the caller's instance after attach. → Sev **High** (cross-workload data read).
- **Claim:** `ec2:AttachVolume` scoped by `ec2:ResourceTag` on the *instance* only (not the *volume*) still lets any volume be attached. → **Oracle:** attach succeeds for an untagged/foreign-tagged volume. (Lens S: condition binds the wrong resource of the two required.)
- **Claim (snapshot share, Lens AA):** `ModifySnapshotAttribute createVolumePermission=all` makes an unencrypted snapshot **public with no grantee validation and no consent**; revoking the share does **not** delete volumes/copies already created by consumers; only `SharedSnapshot*` CloudTrail events (detect, not prevent) fire. → **Oracle:** a second account creates a volume from the shared snap; after unshare, that volume still reads. → Sev **High** (cross-account data exposure if misused) / **Medium** footgun otherwise.
- **Claim (Lens X twin):** a role with only `ebs:GetSnapshotBlock`/`ebs:ListSnapshotBlocks` (no `ec2:CreateVolume`/`ec2:DescribeSnapshots`) reads raw bytes of a reachable snapshot; for encrypted snaps the sole extra gate is `kms:Decrypt` on the CMK. → **Oracle:** `GET /snapshots/{id}/blocks/{idx}?blockToken=…` returns `BlockData` for a snapshot the control-plane path would not surface. → Sev **High**.

**Preconditions:** same-AZ volume; loosely-scoped attach/detach or snapshot-share perms. **Cost:** low. **Stop:** one cross-workload read confirmed. **HARD STOP** if a volume/snapshot resolves to AWS-managed state.

---

### AREA 5 — [MED-HIGH] IMDS credential theft via in-guest SSRF / open proxy; IMDSv2 fail-open default (Lens G + V + U)

**Background.** The target page literally instructs: *"open an Internet browser from the instance and enter the following URL for the metadata server: `http://169.254.169.254/latest/meta-data/`."* The credentials path `…/iam/security-credentials/<role>` returns live `AccessKeyId`/`SecretAccessKey`/`Token`. AWS's own docs warn: *"ensure that you don't expose your credentials when the services make HTTP calls on your behalf… HTTP proxies, HTML/CSS validator services, and XML processors."* IMDSv1 requires **no token**; IMDSv2 needs a session token and rejects tokenless `GET`s with `401`. The order-of-precedence table shows that when the AMI is not `ImdsSupport: v2.0` and the account default is "no preference," the resulting config is **`V1 or V2` (token optional)** — i.e. **IMDSv1 reachable by default** unless an admin explicitly enforced IMDSv2.

**Security Concern.** Any in-guest SSRF, open reverse-proxy, or request-relay on a Windows instance with IMDSv1 permitted can read the instance-profile role's live credentials with a single unauthenticated `GET`. Raising `HttpPutResponseHopLimit` (documented for container compatibility: *"increasing the hop limit to 2"*) widens how far a relayed request can reach IMDS. The condition keys `ec2:MetadataHttpTokens`/`…HopLimit`/`…Endpoint` only restrict *launch/modify* API calls — they are a principal-side guardrail, **not enforced on the IMDS network path**.

**High-level Test Scenarios:**
- **Claim:** an instance left at the default (`HttpTokens: optional`) yields role creds to a tokenless `GET` from an in-guest process/proxy. → **Oracle:** `/iam/security-credentials/<role>` returns a credential JSON over IMDSv1. → Sev **High** (role creds) — **but SCOPE:** this is the customer's own instance-profile role on an AWS-managed host; it is in scope only as *the customer's* credential exposure. **If the returned identity is an AWS fleet/service role, HARD STOP + disclose.**
- **Claim:** `HttpPutResponseHopLimit > 1` lets a containerized/relayed caller reach IMDS it otherwise could not. → **Oracle:** reach IMDS from +1 hop with hop limit 2.
- **Claim (Lens U):** an org that believes IMDSv2 is enforced has not set `modify-instance-metadata-defaults --http-tokens-enforced enabled`, so launches still permit IMDSv1 (guarantee is advisory). → **Oracle:** a new instance launches with `optional` despite the intended enforcement.

**Preconditions:** an in-guest SSRF/proxy primitive (out-of-band to this doc) or a legitimately owned test instance. **Cost:** low on own instance. **Stop:** one credential read on own instance; do not use creds beyond proving retrieval.

---

### AREA 6 — [MED] Windows KMS activation channel: locally repointable, unauthenticated, plaintext (Lens V + Y + H-naming)

**Background.** `ec2config-service.md`: `ActivationSettings.xml` *"Controls product activation using a key management server (AWS KMS)"*; fields `TargetKMSServer` (*"the private IP address of a AWS KMS"*), `SetAutodiscover`, and **`ReadFromUserData` (*"Gets the AWS KMS server from UserData"*)**. The target page instructs operators to repoint it directly: `slmgr.vbs /skms 169.254.169.250:1688` then `slmgr.vbs /ato`. The channel is standard Microsoft-KMS over plaintext TCP 1688; **no instance-identity-document signing is referenced in the activation path** (the signed `instance-identity/pkcs7` primitive exists but is not used here).

**Security Concern.** The activation target is a **locally-editable, user-data-influenceable** value pointing at an **unauthenticated plaintext** service. On the link-local path it is AWS-host-served and SG/NACL-exempt (host plane — out of scope to attack *the AWS KMS host*), but the **`ReadFromUserData` / local-XML / `slmgr /skms`** levers are **customer-controllable** and let an in-guest or `ModifyInstanceAttribute(userData)` actor redirect activation to an attacker-run KMS, forge activation state, or (chaining Area 3) seed a malicious KMS target at provisioning. Note the doc's own naming confusion: "AWS KMS" here means **Microsoft Key Management Service for volume licensing**, *not* AWS Key Management Service — a Lens-U doc-integrity nit worth filing because it misleads threat-modeling.

**High-level Test Scenarios:**
- **Claim:** `TargetKMSServer` / `slmgr /skms` can be repointed in-guest to an attacker-controlled host and Windows will attempt activation against it over plaintext 1688. → **Oracle:** activation traffic egresses to the attacker target. → Sev **Medium** (licensing-integrity / activation-state spoof; not a credential boundary).
- **Claim:** `ReadFromUserData=true` lets the KMS target be set from `userData`, so Area 3's userData rewrite also controls activation. → **Oracle:** KMS target observed to follow a crafted user-data value.
- **Claim (Lens Y):** no `aws:SecureTransport`-style enforcement is possible on this guest-originated plaintext path; nothing pins or signs the activation server. → **Oracle:** doc search confirms no signing/TLS requirement.

**Preconditions:** in-guest privilege or userData-write. **Cost:** low. **Severity:** Medium (integrity/licensing, not data/credential cross-boundary). **Stop:** redirect demonstrated once; do **not** attack the real AWS KMS host.

---

### AREA 7 — [LOW-MED] AWS-authored IAM artifacts & sample code shipped with these flows (Lens R + S)

**Background.** `create-key-pairs.html` ships a **"Required IAM permissions"** block for the CloudFormation key-pair flow (`ssm:PutParameter`, `ssm:DeleteParameter`, …) and the `AWS::EC2::KeyPair` CloudFormation resource itself; the reset/recovery pages ship runbook-style permission guidance. These are copied verbatim by customers.

**Security Concern.** Per the skill's carve-out, a weak default in an **AWS-authored, copy-verbatim** artifact is AWS's defect, not a customer footgun. Audit each statement-by-statement.

**High-level Test Scenarios:**
- **Claim:** the shipped CFN key-pair permission set grants `ssm:PutParameter`/`GetParameter` on an over-broad `/ec2/keypair/*` (or `*`) path, so a principal holding only the artifact can read **other** key pairs' private keys. → **Oracle:** `iam:SimulateCustomPolicy` (no resources touched) shows allow on a foreign `/ec2/keypair/{id}`; escalate to a scoped live call only with a canary pair. → Sev **Medium–High**.
- **Claim:** sample launch snippets set `MetadataOptions.HttpTokens: "optional"` (IMDSv1) as the default (Lens R variant / insecure sample code). → **Oracle:** read the shipped snippet.
- **Claim (Lens S):** an `ec2:Attribute`/tag condition in a sample policy binds presence not ownership, or is case-sensitive and inert. → **Oracle:** simulate the policy against a foreign resource.

**Preconditions:** none for simulate. **Cost:** minimal. **Severity:** non-admin→broader-reach = Medium–High; route `aws-security` (Tier 2). **Oracle-first:** `iam:SimulatePrincipalPolicy`/`SimulateCustomPolicy` before any live call.

---

### AREA 8 — [LOW] Predictable SSM key-pair parameter name — pre-registration / land-grab (Lens EE, speculative)

**Background.** The private-key parameter name `/ec2/keypair/{key_pair_id}` is deterministic and the `KeyPairId` is public.

**Security Concern (speculative — mark doc-gap).** If a lower-privileged principal with `ssm:PutParameter` on `/ec2/keypair/*` can **pre-create** a parameter at the name a future CloudFormation key-pair will use, does the stack **fail, overwrite, or adopt** the attacker's parameter? If adopt/collide, the attacker could substitute a known private key or deny the stack. **Oracle:** pre-put a parameter at a to-be-used `/ec2/keypair/{id}` and observe CFN behavior. **Severity:** Low unless adoption is shown. Confirm the surface first — the `KeyPairId` is server-assigned at create time, which likely defeats pre-registration (so this may be a null hypothesis once the id-assignment timing is confirmed).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Recover foreign key's private key via SSM | SSM Parameter Store `/ec2/keypair/{id}` | "EC2 doesn't keep a copy of your private key" (contradicted by CFN→SSM); IAM scoping on `ssm:GetParameter`; SecureString/`alias/aws/ssm` (unconfirmed) |
| Read foreign Admin password blob | `ec2:GetPasswordData` on `instance*` | Resource-level IAM + condition keys; account-scoped ARN |
| Twin leak via console output/screenshot | `GetConsoleOutput` / `GetConsoleScreenshot` | Same action-level IAM; no additional guard vs the password Deny |
| userData→role privesc without PassRole | `ec2:ModifyInstanceAttribute` | `ec2:Attribute/${AttributeName}` condition key (case-sensitivity fail-open risk) |
| Cross-workload disk read via attach | `ec2:AttachVolume`/`DetachVolume` | Only AZ cross-check; customer-authored tag/ID scoping |
| Raw snapshot byte read | `ebs:GetSnapshotBlock` | Separate `ebs:*` IAM + KMS on encrypted; narrower key set |
| Public / orphaned snapshot share | `ec2:ModifySnapshotAttribute` | Block Public Access for snapshots (opt-in); "share only with those you trust" prose |
| IMDS credential theft | IMDS `169.254.169.254` | IMDSv2 enforcement (`HttpTokens=required`) + hop limit; **fail-open default** |
| Activation redirect / spoof | `ActivationSettings.xml` / `slmgr /skms` / `ReadFromUserData` | None documented (plaintext, unsigned, locally editable) |
| AWS-authored IAM artifact over-grant | CFN key-pair perms / sample snippets | statement scoping as shipped |

---

## 7. Out-of-Scope Risk Categories (state as confidently as in-scope)

- **The AWS-managed host plane itself:** the Nitro/Xen controller answering `169.254.169.254` / `169.254.169.250`-`.251` / `.253` / `.123`. These are AWS-owned, SG/NACL-exempt by design (`using-instance-addressing.md`). Attacking *the host service* — or any credential/identity that proves to be an **AWS fleet role** — is a **HARD STOP + disclosure**, not a finding to pursue.
- **IMDS on a fully-managed instance** as a generic "IMDSv1 exists" complaint — in scope only as *the customer's own* instance-profile credential exposure chained from an SSRF primitive; not as a vuln in the metadata service.
- **Shared physical / hypervisor infrastructure, side channels, the Microsoft-KMS activation servers AWS operates.**
- **Customer-authored** IAM policies that are over-broad (least-privilege footgun the customer inflicts on themselves) — in scope **only** when the weak default ships in an AWS-managed policy / AWS-published sample / CFN / runbook copied verbatim (Area 7).
- **In-guest OS vulnerabilities, RDP CVEs, Windows licensing/CAL product behavior** ("No Terminal Server License Servers…", "Some settings are managed by your organization") — product/feature behavior, not an AWS trust-boundary.
- **Single-tenant self-DoS** (e.g. `Force` detach corrupting your own FS; deleting `.run-once`), **DNS rebinding against private-only endpoints.**
- **The downloaded `EC2Install.zip`** is AWS-hosted on S3 (`ec2-downloads-windows`) over HTTPS — supply-chain of that artifact is out of scope here (note only).

---

## 8. Null Hypotheses / Doc Gaps (pages checked named)

- **Lens D (data-plane→control-plane escape): N/A for this surface.** Checked `using-instance-addressing.md`, `ec2config-service.md`, `common-messages.md`. The only "control" plane reachable from the guest is the AWS host plane via link-local — which is the hard-stop boundary, not a customer control plane. No customer-owned control ENI exposed by these pages.
- **Lens F (translation/wire-protocol injection): N/A.** Checked the password/console/volume/activation pages — no customer-input-to-backend-language translator in this flow. (`userData`→shell is covered under B/E as script execution, not a translation layer.)
- **Lens J (OAuth/3P linking): N/A.** No 3P integration/OAuth in any page read (`connect-rdp.html`, key-pair, volume, metadata pages).
- **Lens K (prompt injection): N/A.** No LLM/agent in this surface.
- **Lens M (shared-identifier interception):** partial — the **RDP self-signed cert thumbprint** is exposed via `GetConsoleOutput`/system log (`connect-rdp.html`), relevant only to RDP MITM verification; folded into Area 2 as info-leak. No session/presigned-URL interception in these pages.
- **Lens N (namespace migration): N/A.** No dual-ARN / legacy-vs-new namespace in these pages.
- **Lens P (identity proofing / registration): N/A.** No onboarding/KYC/OTP flow here.
- **Lens Q (file upload): N/A** for the service — the only "download" is AWS→you (`EC2Install.zip`). The console screenshot/output are *returned* blobs (covered under O/A), not uploads.
- **Lens W (attestation-conditioned authz): doc-gap, adjacent.** NitroTPM / Nitro Enclaves attestation (`kms:RecipientAttestation`, PCR policies) is *not* in these Windows troubleshooting pages, but Windows instances do use NitroTPM — flagged as a **doc-gap; confirm surface on the NitroTPM/Enclaves pages** before concluding (route a separate focus pass there).
- **Lens BB / CC / DD / FF (edge/parser/cache/JWT): N/A.** No API-Gateway/CloudFront/ALB/authorizer/Cognito/JWT component in this surface.
- **Lens H (KMS encryption-context confusion): mostly N/A** — the only crypto here is RSA-with-the-launch-keypair (client-side) and the SSM `SecureString` key (Area 1), plus CMK-gated encrypted-snapshot sharing (Area 4). No per-resource branch-key / encryption-context model in these pages.
- **Lens Y beyond activation:** `status.aws.amazon.com` is referenced as plain `http://` in the page but is a status site, not an authenticated endpoint — informational only.

---

### Priority recap for the hunter
1. **Area 1** (SSM private-key wall bypass) — highest, self-contained, strong doc anchor.
2. **Area 3** (userData→role privesc) and **Area 4** (volume attach / `ebs:GetSnapshotBlock`) — high, confirmed primitives.
3. **Area 2** (password/console/screenshot twin parity).
4. **Area 5** (IMDS, respecting the hard stop).
5. **Area 6/7/8** — medium/low, integrity & artifact audits.
Compose the kill chain explicitly: **Area 2 (foreign password blob) + Area 1 (foreign private key from SSM) → Administrator RDP**; and **Area 3 (userData rewrite) → Area 6 (seed malicious KMS target via `ReadFromUserData`)**. Rate each chain at the severity of its end state.
