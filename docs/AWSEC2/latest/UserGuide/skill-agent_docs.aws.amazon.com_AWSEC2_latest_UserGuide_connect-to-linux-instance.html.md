# Connect to Linux Instance (SSH) — Attack Research Plan

Source of leads: `docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html` (hub) + its linked prerequisite/method pages — `connection-prereqs-general.html`, `connect-linux-inst-ssh.html`, `connect-linux-inst-from-windows.html` (PuTTY), `linux-file-transfer-scp.html`, `connect.html` (method matrix), and the key-pair sub-tree (`ec2-key-pairs.html`, `create-key-pairs.html`, `describe-keys.html`, `verify-keys.html`, `replacing-key-pair.html`, `TroubleshootingInstancesConnecting.html`, `building-shared-amis.html`). Offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` cross-checked against live docs. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Scope note / de-duplication.** This target is a *client-side SSH connection hub*. Two connection methods it references have their own dedicated plans — **do not re-derive them here**:
> - **EC2 Instance Connect** (`SendSSHPublicKey`, EICE `OpenTunnel`) → `/work/aws-docs/ec2-instance-connect-attack-research-plan.md`.
> - **Serial Console** → `skill-agent_..._ec2-serial-console.html.md` (same dir).
> Session Manager / Fleet Manager (RDP) are separate services out of this plan's scope. This plan concentrates on the surface the SSH-connect flow *uniquely* introduces: **host-key fingerprint verification, key-pair private-key lifecycle, and the key-replacement / lost-key access paths.**

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the fleet identity behind `GetConsoleOutput` retention, or the KMS `alias/aws/ssm` managed-key operator), stop, preserve evidence, flag for AWS-Security disclosure.
- All key-pair private-key probes MUST use synthetic canary key pairs the tester created; never read another real tenant's material.

---

## 1. Pentest Objectives (boundary-breach goals, stated as outcomes)
1. **Bypass key-pair authentication entirely** — obtain interactive SSH/root on a target Linux instance *without ever possessing its `.pem` private key*, using only EC2/EBS control-plane IAM (key-replacement & lost-key recovery flows).
2. **Recover a CloudFormation-provisioned key pair's private key from SSM Parameter Store** under a principal *denied* the EC2 key-pair actions (cross-service reachability, Lens T).
3. **Defeat the documented MITM protection** — make the console-output host-key fingerprint "verification" pass while the tester (or an AMI publisher) holds the host private key (supply-chain / TOFU).
4. **Read another principal's instance boot secrets** (host keys, cloud-init/user-data echoes) via `GetConsoleOutput` without an ownership binding.
5. **Persist covert SSH access** into instances launched from a shared/published AMI (baked `authorized_keys`).

---

## 2. Components, Assets, and Design

**Customer-facing interface.** SSH (TCP/22) from an operator workstation to the instance's public IPv4 DNS / IPv6 address, authenticated by an **EC2 key pair** (`.pem` private key on client → matching public key in the instance's `~/.ssh/authorized_keys`). PuTTY path adds a `.pem`→`.ppk` conversion (PuTTYgen). SCP/rsync reuse the same key over SSH. This flow uses **no service-plane API at connect time** (see `connect.html` matrix: SSH client = "IAM permissions: No, Key pair: Yes").

**Assets.**
- **Key-pair private key** — the credential. AWS explicitly *does not keep a copy* for keys created via the console/CLI/API or imported. **Only the CloudFormation `AWS::EC2::KeyPair` path persists the private key server-side** (SSM Parameter Store — see Area 2). Whoever holds it gets shell.
- **Instance host key** (`/etc/ssh/ssh_host_*_key`) — server identity; its fingerprint is the MITM anchor.
- **Console output** — buffered early-boot text (kernel + cloud-init), containing the host-key fingerprint block and potentially user-data echoes.
- **`authorized_keys`** on the instance root volume — the access-control list SSH actually enforces; mutable via the volume, not just via a live shell.

**Identity / ownership split.**
- **Customer account / IAM principal** owns the instance, key pairs, EBS volumes, and calls `GetConsoleOutput`, `Create/Import/DeleteKeyPair`, `Attach/DetachVolume`.
- **AWS service plane** owns: the console-output capture/retention path; the `alias/aws/ssm` KMS managed key that encrypts EC2-created private keys in Parameter Store; the reactive "public-AMI host-key audit" process.
- **AMI publisher** (third party) is a distinct trust actor: their AMI defines the *initial* host key and the *initial* `authorized_keys` baked at build time.

**Connection pipeline (SSH path):**
```
operator workstation                         AWS control plane            EC2 instance (customer VPC)
   .pem (private key) ──ssh -i──────────────────────────────────────────▶ sshd:22
        │                                                                    │ authorized_keys (public key)
        │  (optional MITM check)                                             │ /etc/ssh/ssh_host_*_key
        └── aws ec2 get-console-output ──▶ [console buffer] ──fingerprint──▶ (written by instance's OWN first boot)
                                                     ▲
   CFN AWS::EC2::KeyPair ONLY ──▶ SSM Parameter Store /ec2/keypair/{id} (SecureString) [plain CreateKeyPair does NOT]
```
**The load-bearing observation:** the two "trust anchors" the docs hand the operator — the console-output fingerprint and the `.pem` — are both derived from state the *instance/AMI* or a *second AWS service* controls, not from an independent authority. That is the whole attack surface.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| IAM principal w/ EBS rights, no `.pem` | Instance shell (default user) | Stop → DetachVolume(root) → attach to temp inst → edit `authorized_keys` → reattach | Interactive SSH obtained **without** the target's private key → key-pair auth boundary is not the real gate |
| IAM principal denied EC2 key actions | EC2-created private key | `ssm:GetParameter /ec2/keypair/{id}` (+ `kms:ViaService` decrypt) | Cleartext private key retrieved by a role the EC2 API would deny |
| Any account principal (broad policy) | Foreign instance's boot secrets | `ec2:GetConsoleOutput` on `Resource:"*"` | Host-key fingerprints / cloud-init secrets of an instance the caller didn't launch |
| AMI publisher | Every instance launched from the AMI | Baked host key + baked `authorized_keys` survive into launched instances | Identical host-key fingerprint across independent launches; publisher's key logs in |
| Operator (MITM victim) | Instance identity | Console-output fingerprint compare | Fingerprint "match" against attacker-planted value while attacker holds host private key |
| **Any customer surface** | **AWS service plane** | console-output retention fleet / `alias/aws/ssm` operator | **HARD STOP** — preserve evidence, disclose |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `GetConsoleOutput` | Query API | No | External | Returns buffered boot output incl. host-key fingerprints; `--latest` flag | Yes (SigV4) | Account principals w/ the action | Doc says "must be instance owner" but *no launcher-identity condition key* exists; supports `ec2:ResourceTag`/`aws:ResourceTag`/`ec2:InstanceID` (opt-in) |
| `CreateKeyPair` | Query API | Yes | External | Generates key pair; returns private key **once** | Yes | Account principals | Plain API does NOT persist the private key; only the **CFN** `AWS::EC2::KeyPair` path writes it to SSM `/ec2/keypair/{id}` (Area 2) |
| `ImportKeyPair` | Query API | Yes | External | Uploads a customer-supplied **public** key | Yes | Account principals | Key-strength validation? (Lens P) — imported RSA fingerprint = **MD5** |
| `DeleteKeyPair` | Query API | Yes | External | Deletes key pair | Yes | Account principals | Direct call vs CFN: direct `DeleteKeyPair` on a CFN-created pair plausibly orphans the SSM private key (Area 2 delete-orphan lead) |
| `DescribeKeyPairs` | Query API | No | External | Lists key pairs + **fingerprints** + key-pair-id | Yes | Account principals | key-pair-id is the deterministic SSM path component → enumeration input |
| `StopInstances` / `DetachVolume` / `AttachVolume` | Query API | Yes | External | Root-volume swap used in key-replacement | Yes | Account principals | The real gate for the auth-bypass path (Area 1); check ownership scoping of `AttachVolume` (`instance/*`) |
| SSH `sshd` :22 | protocol | — | External (SG-gated) | Interactive login | Yes (if SG allows) | Holder of matching private key | SG source is scoped-IP in the doc's sample (good) |

Non-SDK / knob check: none unique to this hub beyond what the EIC/serial plans cover. `GetConsoleOutput --latest` and console-output *retention/caching* semantics are under-documented (doc-gap).

---

## 5. Recommended Areas of Focus

### Area 1 — Key-pair authentication bypass via root-volume `authorized_keys` rewrite  *(TOP PRIORITY)*
**Background.** The hub tells operators the private key is what grants access ("anyone who possesses your private key can connect"). But `replacing-key-pair.html` and `TroubleshootingInstancesConnecting.html#replacing-lost-key-pair` document an official recovery flow that **injects a new public key without any private key and without in-guest access**: *stop the instance, detach its root volume, attach it to a temporary instance as a data volume, edit `~/.ssh/authorized_keys`, reattach, restart.*
**Security Concern.** This makes SSH key-pair auth **bypassable by any principal holding EBS/EC2 control-plane rights** (`ec2:StopInstances` + `ec2:DetachVolume` + `ec2:AttachVolume` on the target + a temp instance). The access-control boundary is not the private key; it is EBS volume-attach IAM — which is frequently over-granted and, per the EBS/VSS plans, often scoped `instance/*` / `volume/*` **without an ownership condition**. This is the same `AttachVolume`-unconditioned shape flagged in the EBS-storage and VSS-restore plans, applied to credential injection.
**High-level Test Scenarios (falsifiable):**
- *Claim:* A role with `ec2:AttachVolume`/`DetachVolume` scoped by a tag it can set, but **no** key-pair or SSH rights, can mount a target's root volume and append an attacker public key to `authorized_keys`, yielding SSH as `ec2-user`. → *Oracle:* successful `ssh -i attacker.pem` after reattach. *Sev:* **High** (intra-account instance takeover bypassing key auth).
- *Claim:* `AttachVolume`/`DetachVolume` authorize on volume/instance **existence not ownership** (no ownership condition key), letting the swap target a volume the caller shouldn't reach. → route to Lens X and the EBS plan's `ebs/ec2` authz-divergence lead. *Sev:* High if cross-boundary.
- *Adjacent:* the same primitive reads any secret on the mounted root FS (not just injects keys) — data theft without shell.
**Doc evidence:** `replacing-key-pair.html`; `TroubleshootingInstancesConnecting.html#replacing-lost-key-pair` (Steps 1–8). **Severity-if-true:** High. **Stop:** once shell is proven on one canary instance.

### Area 2 — Private-key recovery from Parameter Store (CloudFormation path)  *(Lens T — cross-service secret reachability)*
**Background — scope-corrected.** The SSM-storage behavior is **NOT** a property of plain `CreateKeyPair`. Doc text is explicit and path-dependent:
- **Console / CLI / API path:** *"the public key is stored in Amazon EC2, and you store the private key"* + *"Amazon EC2 doesn't keep a copy of your private key"* (`create-key-pairs.html`, `ec2-key-pairs.html`). → **nothing to recover server-side.**
- **CloudFormation `AWS::EC2::KeyPair` path:** *"the private key is saved to AWS Systems Manager Parameter Store... `/ec2/keypair/{key_pair_id}`"* (`create-key-pairs.html` + `aws-resource-ec2-keypair.html`). The `PutParameter` is performed by **CloudFormation's execution role** (its required-perms note demands `ssm:PutParameter`), not by EC2 internally — so this Lens-T oracle applies to **CFN-provisioned key pairs** (and tooling replicating the `CreateKeyPair→PutParameter` pattern: some Terraform/CDK constructs — unconfirmed).
**Security Concern.** For CFN-created pairs, the EC2 key-pair API wall is bypassable at the storage service: a principal **denied** `ec2:*KeyPair*` but holding `ssm:GetParameter` recovers the cleartext private key → full SSH. The path is **deterministic and enumerable** from `KeyPairId`, which read-only `ec2:DescribeKeyPairs` / `ec2:DescribeInstances` (commonly granted) return openly.
**High-level Test Scenarios (falsifiable):**
- *Claim (breach oracle):* A role **denied** `ec2:DescribeKeyPairs`+`ec2:CreateKeyPair` but allowed `ssm:GetParameter` on `/ec2/keypair/*` retrieves the cleartext private key of any CFN-created key pair in-account. → *Oracle:* `aws ssm get-parameter --name /ec2/keypair/<id> --with-decryption` returns cleartext. *Sev:* **Critical if confirmed** (instance-access-equivalent credential across an IAM boundary the operator thought was EC2-scoped).
- *Claim (provenance discriminator):* the same call **404s (ParameterNotFound)** for a console/CLI-created pair → a hunter can fingerprint *how* each key pair was provisioned. *Sev:* Low (recon oracle).
- *Claim (delete-orphan — TOP hunter target):* a **direct** `ec2:DeleteKeyPair` (bypassing CFN) against a CFN-created pair removes only the EC2-side public key (`delete-key-pair.html`: *"you're only deleting the public key... stored in Amazon EC2"*) and **plausibly orphans the SSM parameter with the live private key**, while future `DescribeKeyPairs` no longer surfaces the `KeyPairId` (secret outlives resource; access survives for anyone who recorded the ID). CFN-orchestrated delete *does* cascade (`aws-resource-ec2-keypair.html`: *"it also deletes the parameter..."*). → *Oracle:* create via CFN, note `KeyPairId`, `ec2:delete-key-pair`, then `ssm get-parameter` still returns the key. *Sev:* High (stale credential).
- *KMS delegation (unconfirmed — confirm first):* if `alias/aws/ssm`'s key policy delegates via `kms:ViaService=ssm.<region>.amazonaws.com`, the breach needs **only** `ssm:GetParameter` (no `kms:Decrypt` in the caller's policy) → raises likelihood. **HARD STOP if evidence points at the managed-key operator.**
**Doc evidence:** `create-key-pairs.html` (both paths), `aws-resource-ec2-keypair.html`, `delete-key-pair.html`. **Severity-if-true:** Critical (CFN path). **Owner:** shared — AWS owns path predictability + managed-key delegation; customer owns whether SSM policies scope `/ec2/keypair/*` narrowly.

### Area 2b — `ImportKeyPair` weak / attacker-known public key  *(Lens P / weak-cred — lower priority)*
**Background.** `create-key-pairs.html` lists accepted types (RSA 1024/2048/4096, ED25519; DSA rejected) but documents **no minimum-strength enforcement, no duplicate detection, no check against known-compromised keys.**
**Security Concern.** A low-priv principal with only `ec2:ImportKeyPair` can import a 1024-bit RSA key, or a public key whose private half the attacker already holds; the imported `KeyName` then becomes launchable by any role that can `RunInstances` with `KeyName=<imported>`.
**Oracle:** `import-key-pair` with an attacker-known pubkey succeeds; instance launched with it is attacker-accessible. **Severity:** Medium (needs a second privilege to weaponize). **Owner:** customer (least-priv + key hygiene); AWS's missing strength validation is a doc-gap, not a bug. **Lens R note:** CFN `AWS::EC2::KeyPair` returns only `KeyPairId`/`KeyFingerprint` via `Fn::GetAtt` (not `KeyMaterial`) — no AWS-authored sample echoes the private key into stack outputs; the danger is a *customer* wiring `ssm get-parameter --with-decryption` into automation (out-of-scope footgun).

### Area 3 — MITM / host-key fingerprint verification integrity  *(Lens U / Y / supply chain)*
**Background.** The docs' *only* MITM defense is: `get-console-output` → read the `BEGIN SSH HOST KEY FINGERPRINTS` block → compare to the SSH prompt. Verification is recommended specifically "if you launched your instance from a public AMI provided by a third party."
**Security Concern.** The fingerprint is written by the **instance's own first boot** — so if the AMI publisher pre-baked the host key, both the fingerprint *and* the private host key are attacker-controlled, and the documented check is a **self-referential compare that always passes** while the publisher can passively MITM/decrypt every session. The actual defense lives only in `building-shared-amis.html` ("Remove SSH host key pairs" → `shred -u /etc/ssh/*_key*` so keys regenerate on first boot) and is **publisher-courtesy, not AWS-enforced**; AWS's only backstop is a *reactive* "routine auditing → mark AMI private after a grace period" (no SLA — doc-gap).
**High-level Test Scenarios (falsifiable):**
- *Claim:* Two instances launched independently from the same third-party public AMI share an identical host-key fingerprint → the AMI ships pre-baked keys → MITM precondition met. → *Oracle:* diff the `BEGIN SSH HOST KEY FINGERPRINTS` blocks across two launches (read-only, safe). *Sev:* **Critical/passive** for anyone launching from that AMI; owner-to-fix = publisher (primary) + AWS reactive-only (doc-gap).
- *Claim:* Nothing in the connect flow forces the operator to verify freshness (no doc pointer to boot-time key-regen log lines) → operators trust a baked key silently.
- *Crypto note (Y, Informational):* imported-RSA key-pair fingerprints use **MD5** and EC2-created RSA uses **SHA-1** (`verify-keys.html`) — weak hashes; a fingerprint-collision angle on the *key-pair* fingerprint is low-impact but worth a note.
**Doc evidence:** `connection-prereqs-general.html#connection-prereqs-fingerprint`; `building-shared-amis.html` (remove SSH host keys). **Severity-if-true:** Critical (supply-chain passive MITM) / Informational (hash choice).

### Area 4 — `GetConsoleOutput` authorization scoping & boot-secret exposure  *(Lens A / X / O)*
**Background.** The UserGuide asserts *"You must be the instance owner to get the console output."*
**Security Concern.** "Owner" is **not an IAM primitive** — `GetConsoleOutput` supports `ec2:ResourceTag`/`aws:ResourceTag`/`ec2:InstanceID` conditions but there is **no launcher-identity condition key**. A broad `ec2:GetConsoleOutput` on `Resource:"*"` lets any account principal read the host-key fingerprints *and* cloud-init/user-data echoes of instances they never launched — intra-account lateral recon of other teams' boot secrets. Console output is **buffered/cached** ("posted shortly after a state transition, not continuously updated") so it can be stale.
**High-level Test Scenarios:**
- *Claim:* Principal B (no launch relationship to instance X) with `ec2:GetConsoleOutput` on `*` reads X's console output → confirms existence-not-ownership crossing. *Oracle:* 200 + fingerprint block returned. *Sev:* Medium (intra-account).
- *Claim:* user-data / cloud-init secrets surface in console output (no doc warning against embedding secrets — doc-gap). *Oracle:* canary token in user-data appears in `get-console-output`.
- *Audit (O):* `GetConsoleOutput` **is** a CloudTrail management event (detection exists) — but detection ≠ prevention; note no way to enforce launcher-scoping.
**Doc evidence:** `connection-prereqs-general.html`; live `instance-console.html`/`troubleshoot-unreachable-instance.html`; service-authorization `list_ec2` condition keys. **Severity-if-true:** Medium.

### Area 5 — Shared-AMI baked `authorized_keys` persistent access  *(Lens AA — supply chain / persistence)*
**Background.** `replacing-key-pair.html`: *"If you create a Linux AMI from an instance, the public key material is copied from the instance to the AMI... To prevent someone who has the private key from connecting to the new instance, you can remove the public key from the original instance before creating the AMI."*
**Security Concern.** A shared/public AMI carries the **builder's public key** in `authorized_keys` → the AMI author retains SSH access to *every* instance a consumer launches from it, unless the consumer manually scrubs it. This is a documented persistence/backdoor vector orthogonal to the host-key issue in Area 3.
**High-level Test Scenarios:**
- *Claim:* An instance launched from a third-party public AMI contains a non-default entry in `~/.ssh/authorized_keys` → builder backdoor. *Oracle:* inspect `authorized_keys` on a fresh launch. *Sev:* High for the consumer (persistent foreign access); owner-to-fix = AMI publisher + consumer diligence. Cross-reference the `sharing-amis` / `share-amis-orgs-ous` plans.
**Doc evidence:** `replacing-key-pair.html` (AMI key-copy paragraph). **Severity-if-true:** High (persistent access).

---


## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Shell without private key via volume swap | EBS AttachVolume IAM | "possession of private key" access model (`ec2-key-pairs.html`) |
| Private-key recovery via SSM | Parameter Store `/ec2/keypair/*` | EC2 key-pair API access wall |
| Passing fingerprint check w/ attacker host key | console-output fingerprint | `building-shared-amis` remove-host-keys step (publisher-only) |
| Cross-principal console-output read | `GetConsoleOutput` | "must be instance owner" prose (no IAM key) |
| Persistent access via baked authorized_keys | AMI build | "remove public key before AMI" prose |
| Weak fingerprint hash (MD5/SHA-1) | `verify-keys` | none |

## 7. Out-of-Scope Risk Categories
- **EC2 Instance Connect / EICE** → own plan (`ec2-instance-connect-attack-research-plan.md`). Do not re-derive.
- **Serial Console** → own plan (same dir).
- **Session Manager / Fleet Manager (RDP)** → separate services.
- Client-side only issues (local `.pem` file perms, PuTTYgen passphrase choice, WSL `cp` of key) — customer-workstation hygiene, not a service boundary. The doc's `chmod 400` and Windows-ACL guidance is *correct* and the SG SSH sample source is *scoped-IP* (not `0.0.0.0/0`) → no footgun there.
- IMDS on managed hosts; shared-responsibility in-guest OS config.
- **HARD STOP:** anything reaching the console-output retention fleet identity or `alias/aws/ssm` operator = AWS service plane.

## 8. Null hypotheses / doc gaps
- **SG SSH sample = secure** (source is operator IP, not `0.0.0.0/0`) — Lens R null for this page (the `0.0.0.0/0` rows are web-server ports only).
- **Prompt-injection / SSRF / translation-layer / attestation lenses (K/G/F/W): N/A** — read the hub, all four SSH-method pages, prereqs, key-pair sub-tree; no LLM, no server-side fetch of a customer-supplied URL, no wire-protocol translator, no attestation gate on this surface.
- **No AI-agent "See also / run this CLI" injection block** on the connect pages (grep matches were legitimate `get-console-output` examples). Contrast the injection block seen on other EC2 pages (`project_aws-docs-see-also-injection`).
- **Doc-gaps to confirm on live/API before hunting:** (a) **[top target]** whether a *direct* (non-CFN) `DeleteKeyPair` on a CFN-created pair orphans the live SSM private key (CFN-orchestrated delete *does* cascade); which KMS key encrypts `/ec2/keypair/*` and whether `kms:ViaService` removes the need for identity-policy `kms:Decrypt`; condition keys on `Create/Import/DescribeKeyPairs`; (b) console-output retention/caching window and the fleet identity behind `--latest`; (c) whether AWS warns against secrets in user-data surfacing in console output; (d) `ImportKeyPair` key-strength validation. Mark these "confirm surface first."
