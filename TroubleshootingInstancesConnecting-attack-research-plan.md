# EC2 "Troubleshoot connecting to your Linux instance" — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/TroubleshootingInstancesConnecting.html` (+ `.md`), and the adjacent pages/APIs it links or implies:
`connect-to-linux-instance`, `connect-linux-inst-ssh`, `connect-linux-inst-eic`, `connect-linux-inst-from-windows`, `ec2-instance-connect-methods`, `ec2-instance-connect-set-up`, `ec2-instance-connect-configure-IAM-role`, `connect-with-ec2-instance-connect-endpoint`, `permissions-for-ec2-instance-connect-endpoint`, `create-ec2-instance-connect-endpoints`, `eice-security-groups`, `eice-slr`, `log-ec2-instance-connect-endpoint-using-cloudtrail`, `ec2-serial-console`, `configure-access-to-serial-console`, `connect-to-serial-console`, `connection-prereqs-general` (fingerprint), `create-key-pairs`, `ec2-key-pairs`, `delete-key-pair`, `amazon-ec2-managed-instances`, `security-group-rules-reference`, `ec2-instance-launch-parameters`, `connect-with-systems-manager-session-manager`;
API refs `API_SendSSHPublicKey`, `API_SendSerialConsoleSSHPublicKey`, `API_CreateInstanceConnectEndpoint`, `API_Ec2InstanceConnectEndpoint`, `API_ModifyInstanceConnectEndpoint`, `API_DeleteInstanceConnectEndpoint`, `API_AttachVolume`, `API_DetachVolume`, `API_ModifyInstanceAttribute`, `API_ImportKeyPair`, `API_RunInstances`, `API_OperatorRequest`/`API_OperatorResponse`;
Service Authorization Reference `list_ec2-instance-connect`, `list_ec2`, `list_ebs`; AWS-managed policies `EC2InstanceConnect`, `Ec2InstanceConnectEndpoint`; EBS pages `share-volume`, `how-ebs-encryption-works`, `ebsapi-permissions`, `ebs-modifying-snapshot-permissions`; CFN `aws-resource-ec2-keypair`.

Status: **documentation-derived hypotheses only; nothing tested against a live account.** The local mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide` is missing or stale for some newer pages — online `.md` variants (append `.md` to the `.html` URL) and the offline Service Authorization mirror (`/work/aws-docs/docs/service-authorization/latest/reference/`) were used and are noted where staleness matters.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- This page is a **troubleshooting runbook**, so its highest value is that **AWS itself documents the break-glass primitives** (volume swap, key push, host-key upload) that double as attacker playbooks. The surface is dominated by **customer-plane IAM scoping, SSH-auth-equivalent primitives, and network-segmentation bypasses by design** — not cross-tenant. The few genuinely AWS-owned leads are: the **stock `EC2InstanceConnect` managed policy** (push-as-root, no `osuser`), the **`eic_harvest_hostkeys` → "AWS trusted host keys database"** upload whose auth model is undocumented, the **`Operator`/`Managed` "Reserved for internal use" knob** on `RunInstances`, and the **AWS-authored launch-wizard default SG** opening SSH to `0.0.0.0/0`.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the EC2/EBS fleet decrypt identity `aws:ec2-infrastructure/<instance_id>`, the serial-console proxy, the EIC host-key store backend, a shared Nitro host, cross-tenant data from a reclaimed host), stop, preserve evidence, flag for AWS-Security disclosure. Do **not** modify another tenant's `authorized_keys`, volume, or host-key record in a test account you do not own both sides of.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)

1. **Prove the stock EIC managed policy grants unconditional root.** Show that a principal holding only `arn:aws:iam::aws:policy/EC2InstanceConnect` can `SendSSHPublicKey --instance-os-user root` against **any** instance in the account and SSH in — i.e. AWS's own shipped onboarding policy is root-equivalent with no `ec2:osuser` or resource scoping.
2. **Prove / refute cross-account host-key poisoning of the "AWS trusted host keys database."** Determine the undocumented API + auth model behind `eic_harvest_hostkeys`, and whether an instance (or an account) can upload a host-key record bound to *another* instance/account → persistent, warning-less MITM of the browser-based EIC client.
3. **Prove the in-account SSH-auth-equivalent primitives that bypass the whole key-pair model.** Show that `ec2:ModifyInstanceAttribute(userData)` (no `iam:PassRole`), the documented **volume detach/attach → `authorized_keys` rewrite** flow, and `ebs:GetSnapshotBlock` on a shared/over-granted snapshot each yield read/write of a victim's root filesystem without ever touching SSH auth.
4. **Prove the network-segmentation bypasses are IAM-only.** Show that **serial console** access ignores SG+NACL entirely, and that **EICE `OpenTunnel`** is scoped to the *endpoint* (not the instance) so a grant with no `privateIpAddress` condition reaches every route-reachable host in the VPC.
5. **Prove / refute the `Operator`/`Managed` self-assertion.** Determine whether a customer can set `Operator.Principal` on their own `RunInstances` to spoof `Managed=true`, and whether "user-initiated connections to managed instances are not allowed" is enforced by any technical control or is console-UX-only (Lens U).
6. **Characterise the cross-service secret reach.** For CFN-created key pairs, prove `ssm:GetParameter` on `/ec2/keypair/*` + `kms:Decrypt` recovers the plaintext private key for a principal explicitly denied all `ec2:*KeyPair` actions (Lens T).
7. **Characterise detection/attribution gaps:** EICE `OpenTunnel` logs `privateIpAddress` not `instanceId`; Session Manager port-forwarding/SSH-over-SSM sessions are not command-logged; sustained EIC access requires repeated `SendSSHPublicKey` (a detection signal).

---

## 2. Components, Assets, and Design

**Customer-facing interfaces (connect methods this page covers).**
- **Direct SSH** (port 22) — key-pair auth; trust anchor is `~/.ssh/authorized_keys` on the root volume.
- **EC2 Instance Connect (EIC)** — `ec2-instance-connect:SendSSHPublicKey` pushes a public key into **instance metadata** (IMDS), where sshd's `AuthorizedKeysCommand /opt/aws/bin/eic_run_authorized_keys` reads it; the key **remains 60 seconds**. Browser-based client and `mssh` CLI.
- **EIC browser client host-key validation** — validated against an **"AWS trusted host keys database"**, populated at first boot and refreshed only by running `eic_harvest_hostkeys` **on the instance** after host-key rotation (`/opt/aws/bin/` on AL2, `/usr/share/ec2-instance-connect/` on Ubuntu).
- **EC2 Instance Connect Endpoint (EICE)** — an **identity-aware TCP proxy** into private subnets; `ec2-instance-connect:OpenTunnel`.
- **Serial console** — out-of-band console over an AWS-operated proxy; `ec2-instance-connect:SendSerialConsoleSSHPublicKey`; **independent of the VPC — ignores SG and NACL**.
- **Systems Manager Session Manager** — `ssm:StartSession` via SSM Agent + instance-profile role; no open inbound port.
- **The lost-key recovery runbook** — stop instance → `DetachVolume` root → `AttachVolume` to a temp instance → mount → overwrite `authorized_keys` → reattach → start.

**Processes / hosts behind the interfaces.**
- `sshd` + `eic_run_authorized_keys`/`eic_parse_authorized_keys`/`eic_curl_authorized_keys` (the `ec2-instance-connect` package, runs as user `ec2-instance-connect`).
- EICE service (AWS-operated proxy ENI in the customer VPC), serial-console proxy (AWS-operated, per-Region fixed fingerprinted endpoints), the EIC "trusted host keys" store (AWS-operated, backend undocumented).
- EBS attach KMS path: the **identity-only role** `arn:aws:iam::<acct>:role/aws:ec2-infrastructure/<instance_id>` that `kms:CreateGrant`/`Decrypt`s an encrypted volume at attach.

**Accounts / trust zones.** Single customer account is the norm. Cross-account seams appear only via: **RAM volume share → copy → attach**, **snapshot `createVolumePermission` public/private share → `CreateVolume`**, and **AMI share**. The **AWS service plane** owns the serial-console proxy, the EICE service, the EIC host-key store, and the EBS/EC2 fleet decrypt identity — all **hard-stop** on contact.

**Resources & identifier shapes.** `instance` (`i-[a-f0-9]+`), `volume` (`vol-…`), `snapshot` (`snap-…`, EBS-direct ARN has an **empty account field** `…:ec2:region::snapshot/…`), `image`/AMI (`ami-…`), `key-pair` (`key-…` high-entropy), `instance-connect-endpoint` (`eice-…`). `InstanceId` is **non-secret and enumerable/leaked** (URLs, CloudTrail, logs).

**Identity.** SigV4 IAM everywhere on the control plane. EICE tunnels authenticate with the caller's IAM entity but **the tunnel persists past credential expiry** up to `maxTunnelDuration` (≤3600s). The pushed EIC key is the only gate for the ensuing SSH session; serial console's `SendSerialConsoleSSHPublicKey` is the only IAM gate, then OS login takes over.

**Untrusted-data entry / transform seams.** `SSHPublicKey` blob (80–4096 chars, no documented algorithm allowlist at the API layer — validated only at the OS `eic_parse_authorized_keys` layer); `userData` (base64 → cloud-init → `authorized_keys`); a mounted foreign root volume's filesystem; `Operator.Principal` free-string on `RunInstances`.

**ASCII connection map.**
```
                         ┌─────────────────── AWS service plane (HARD STOP) ───────────────────┐
                         │  EIC "trusted host keys DB"   Serial-console proxy   EICE service    │
                         │  EBS/EC2 fleet decrypt id:  role/aws:ec2-infrastructure/<instance>   │
                         └───────▲───────────────────────▲──────────────────────▲──────────────┘
 caller (IAM/SigV4)              │ eic_harvest_hostkeys   │ SendSerialConsole…    │ OpenTunnel
     │                           │ (auth model UNDOCUMENTED)                      │ (scoped to ENDPOINT,
     │ SendSSHPublicKey (→IMDS, 60s)                      │ (ignores SG+NACL)     │  not instance)
     ▼                                                    ▼                       ▼
 ┌────────────── customer VPC ───────────────────────────────────────────────────────────────┐
 │  SG(22) ─ NACL ─ route(0.0.0.0/0→IGW) ─► [ sshd + eic_run_authorized_keys ]  on EC2 instance│
 │                                              trust anchor: /home/<user>/.ssh/authorized_keys │
 │  write paths to authorized_keys:  RunInstances(KeyName) | ModifyInstanceAttribute(userData) │
 │                                   | DetachVolume+AttachVolume(root→temp instance)+mount      │
 │                                   | CreateVolume(from shared/public snapshot) | ssm:SendCommand│
 │  root volume ──DetachVolume──► temp instance ──mount──► cp authorized_keys ──► reattach       │
 │  CFN key pair → SSM /ec2/keypair/<id> (SecureString)  ◄── ssm:GetParameter + kms:Decrypt      │
 └───────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv IAM principal | Any instance's OS (as root) | `SendSSHPublicKey` under stock `EC2InstanceConnect` policy | A key pushed as `InstanceOSUser=root` to an instance the principal was never meant to administer, then an SSH session — **breach** |
| On-instance code (root) | EIC "trusted host keys DB" | `eic_harvest_hostkeys` upload | A host-key record for **another** instance/account accepted, or an attacker key accepted as "trusted" with no browser-client warning — **breach** (service-plane store → HARD STOP if cross-account write works) |
| IAM principal w/ `ModifyInstanceAttribute` | Victim instance root fs | `userData` rewrite → cloud-init → `authorized_keys` | SSH as planted key on an instance scoped out of the principal's intended set — **breach** |
| IAM principal w/ `Attach/DetachVolume` (`Resource:*`) | Another team's root volume | documented recovery flow run offensively | Mount + read/modify a volume the principal does not own — **breach** (intra-account); cross-account attach **must fail** (ARN is account-scoped) |
| Principal denied `ec2:*Snapshot`/`CreateVolume` | Raw disk blocks of a snapshot | `ebs:GetSnapshotBlock`/`ListSnapshotBlocks` | Reading `authorized_keys`/secrets block-by-block despite the EC2-layer deny — **breach** (AWS self-documents this bypass) |
| Unrelated account | Victim root-volume data | `ModifySnapshotAttribute(createVolumePermission all)` → `CreateVolume` | Any account creating a volume from the shared/public snapshot and reading it — **breach** (cross-account, Critical) |
| Principal denied `ec2:*KeyPair` | CFN key pair private key | `ssm:GetParameter /ec2/keypair/<id>` + `kms:Decrypt` | Plaintext private key retrieved via SSM despite EC2 deny — **breach** (Lens T) |
| Any IAM principal w/ `OpenTunnel` on an EICE | Every route-reachable host in the VPC | tunnel with no `privateIpAddress` condition | A tunnel completing to an instance other than the one intended — **breach** of the assumed "scoped to one endpoint = one instance" |
| Any principal w/ `SendSerialConsoleSSHPublicKey` + account flag | Instance whose SG/NACL deny all SSH | serial console (VPC-independent) | A shell on an instance the network posture says is unreachable — **breach** of the SG/NACL segmentation assumption (by design; defender blind spot) |
| Customer `RunInstances` caller | The `Managed`/`Operator` trust signal | `Operator.Principal` free string | `Managed=true` readable on an instance AWS never delegated — **breach** of the integrity of the managed-resource signal |
| Any customer surface | AWS's own service plane | serial-console proxy / EICE / host-key store / fleet decrypt id | **Any** credential/ARN/account belonging to AWS → **HARD STOP, disclose** |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2-instance-connect:SendSSHPublicKey` | SigV4 | Existing | Yes (pushes key to IMDS) | External | Push 60s SSH key for `InstanceOSUser` | Yes | per IAM; stock `EC2InstanceConnect` = `Resource:*` | `InstanceOSUser` pattern permits `root`; `ec2:osuser` condition is **optional** |
| `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | SigV4 | Existing | Yes | External | Push key for serial console | Yes | per IAM + account `EnableSerialConsoleAccess` | **No** `InstanceOSUser` param, **no** `ec2:osuser` key; Nitro-only |
| `ec2-instance-connect:OpenTunnel` | SigV4/WS | Existing | Yes (opens tunnel) | External | EICE TCP tunnel into VPC | Yes | per IAM on the **endpoint** ARN | Resource = `instance-connect-endpoint*`, **not** instance; `privateIpAddress`/`remotePort`/`maxTunnelDuration` optional conditions |
| `eic_harvest_hostkeys` backend upload | **UNDOCUMENTED** | Existing | Yes (writes trust store) | **Internal** | Upload host key to "trusted host keys DB" | n/a (on-instance) | "whoever can exec as root on the instance" | **No** matching action in `list_ec2-instance-connect`; SCP/IAM cannot govern it — top research item |
| `ec2:EnableSerialConsoleAccess` / `Disable` / `GetSerialConsoleAccessStatus` | SigV4 | Existing | Yes/No | External | Account-wide serial console toggle | Yes | per IAM, `Resource:*` (account-level) | Not instance-scoped |
| `CreateInstanceConnectEndpoint` / `Modify` / `Delete` | SigV4 | Existing | Yes | External | Manage EICE | Yes | per IAM | `PreserveClientIp` default **false** |
| `ec2:AttachVolume` / `ec2:DetachVolume` | SigV4 | Existing | Yes | External | Attach/detach EBS | Yes | per IAM on `instance*`+`volume*` | **No** `ec2:Owner`/`aws:ResourceAccount` key on `volume`; ARN is account-scoped |
| `ec2:ModifyInstanceAttribute(userData)` | SigV4 | Existing | Yes | External | Rewrite user-data | Yes | per IAM on `instance` | **No `iam:PassRole`**; SSH-auth-equivalent via cloud-init |
| `ec2:ModifySnapshotAttribute(createVolumePermission)` | SigV4 | Existing | Yes | External | Share snapshot (incl. public) | Yes | per IAM | Public blocked only by opt-in "Block public access for snapshots" |
| `ebs:GetSnapshotBlock` / `ListSnapshotBlocks` / `ListChangedBlocks` | SigV4 | Existing | No | External | Read raw snapshot blocks | Yes | per IAM; ARN empty-account | **Documented bypass** of `ec2:CopySnapshot`/`CreateVolume` deny |
| `ssm:GetParameter /ec2/keypair/<id>` | SigV4 | Existing | No | External | Read CFN key-pair private key | Yes | per IAM + `kms:Decrypt` | Only CFN-created key pairs persist here |
| `ec2:RunInstances` `Operator.Principal` | SigV4 | Existing | Yes | External | Set managed/operator | Yes | per IAM | `OperatorRequest.Principal` = **"Reserved for internal use"**, no documented validation — hidden knob |
| `ssm:StartSession` / `ssm:SendCommand` | SigV4 | Existing | Yes | External | Shell / command exec | Yes | per IAM + instance profile | SSH-equivalent; port-forwarding/SSH sessions not command-logged |

"**Focus here**" leads (doc-flagged or least-trodden): the **undocumented host-key upload**, the **`Operator`/`Managed` reserved knob**, the **non-SDK-surfaced** EBS-direct read path, and the stock **`EC2InstanceConnect` managed policy**.

---

## 5. Recommended Areas of Focus

### Area A — Stock `EC2InstanceConnect` managed policy = unconditional root push *(PRIORITY 1, AWS-owned)*
**Background.** `arn:aws:iam::aws:policy/EC2InstanceConnect` (verified identical online + mirror) is exactly:
`{"Action":["ec2:DescribeInstances","ec2-instance-connect:SendSSHPublicKey"],"Effect":"Allow","Resource":"*"}` — `Resource:*`, **no `Condition`**. `ec2-instance-connect-configure-IAM-role` warns: "Otherwise, all IAM principals with permission for the `ec2-instance-connect:SendSSHPublicKey` action can connect to all EC2 instances." `InstanceOSUser` pattern (`API_SendSSHPublicKey`) permits `root`.
**Security Concern.** Admins attach "the EIC policy" believing they granted scoped SSH; they granted **push-as-any-OS-user (incl. root) to every instance in the account.** This is an **AWS-authored uneditable artifact** → Lens R/S, in scope and reportable (Tier 2), *not* a customer footgun.
**High-level Test Scenarios.**
- *Claim:* A principal holding **only** `EC2InstanceConnect` can `SendSSHPublicKey --instance-os-user root` against any instance whose sshd permits root (RHEL/SUSE default username is `root`) and SSH in. → *Oracle:* attach only this managed policy to a canary principal; push to `root`; SSH. → **Critical** (Lens E + Lens S "condition not enforced by default").
- *Claim:* Omitting `ec2:osuser` while scoping only the instance ARN still permits **any** OS user, because the ARN scopes *which instance*, not *which OS account*. → *Oracle:* instance-ARN-scoped policy, no `ec2:osuser`; push `root`; expect success. → **Medium-High**.
- *Claim:* `ec2:osuser` is exact-match/case-sensitive — a `StringLike "*"` or mixed-case typo fails open. → *Oracle:* test `StringEquals ec2-user` vs request `Ec2-User`, and `StringLike *`. → **Medium-High** (Lens S case-sensitivity fail-open).
**Doc evidence:** `aws-managed-policy/EC2InstanceConnect`, `API_SendSSHPublicKey`, `ec2-instance-connect-configure-IAM-role`, `list_ec2-instance-connect`. **Severity-if-true:** Critical.

### Area B — `eic_harvest_hostkeys` → "AWS trusted host keys database" *(PRIORITY 1, service-plane, doc-gap)*
**Background.** The troubleshooting page: rotated host keys "are not automatically uploaded to the AWS trusted host keys database … you must run the `eic_harvest_hostkeys` script … which uploads your new host key to EC2 Instance Connect. Note that a successful call results in no output." The browser-based EIC client does **not** do interactive TOFU — it trusts whatever this store returns. **No** matching IAM action (`UploadHostKey`/`PutHostKey`) exists in `list_ec2-instance-connect`, strongly implying an internal control-plane call reachable only from on-instance tooling — so **IAM/SCP cannot govern writes to this trust store.**
**Security Concern.** The backend API, request shape, and auth model are undocumented. The integrity of every future browser-client session hinges on how this upload is bound to `(AccountId, InstanceId)`. If binding is weak/spoofable → cross-account host-key poisoning = persistent, warning-less MITM.
**High-level Test Scenarios.**
- *Claim:* The upload authenticates via IMDS-derived instance identity, strictly scoping to the calling instance. → *Oracle:* run the script with IMDS (`169.254.169.254`) firewalled → fail-closed confirms IMDS dependency; `strace`/`tcpdump` the egress to identify the literal endpoint + whether SigV4 vs signed PKCS7 instance-identity document. → if strictly scoped: Low (safe). **If spoofable: Critical + HARD STOP (service-plane store).**
- *Claim:* A local root can upload an attacker-chosen host **public** key (drop it as `/etc/ssh/ssh_host_*.pub`, re-run harvest) that the browser client then silently trusts for future sessions. → *Oracle:* plant a mismatched pub key, harvest, connect via browser client from a clean session, observe silent acceptance. → **High** (transient root → durable stealthy MITM).
- *Claim (Lens A+EE):* Account B can upload a record for Account A's known `i-…` with no trust relationship. → *Oracle:* once the call is reverse-engineered, attempt from Account B against Account A's instance id; expect a `NotFound`-style reject if server-side scoping holds. → **Critical if write succeeds; HARD STOP.**
**Doc evidence:** `TroubleshootingInstancesConnecting#troubleshoot-host-key-validation`, `ec2-instance-connect-set-up`, `ec2-instance-connect-methods`, `list_ec2-instance-connect` (absence). **Severity-if-true:** High → Critical. **Stop condition:** any cross-account write, or any service-plane credential observed → stop & disclose.

### Area C — SSH-auth-equivalent write primitives to `authorized_keys` *(PRIORITY 1, customer-plane)*
**Background.** The whole SSH trust reduces to the content of `/home/<user>/.ssh/authorized_keys` on the root volume. The page itself teaches the volume-swap rewrite. Multiple one-action paths reach the same outcome.
**Security Concern.** Reviewers associate "SSH compromise" with key-pair/volume permissions and miss that `ModifyInstanceAttribute(userData)` alone (no `iam:PassRole`) is a strictly easier path.
**High-level Test Scenarios.**
- *Claim:* `ec2:ModifyInstanceAttribute --attribute userData` (base64 cloud-config with `ssh_authorized_keys`) applied on next boot plants a key — **no `iam:PassRole`, no instance-profile perm.** Confirmed in `list_ec2` (no PassRole dependency) + `API_ModifyInstanceAttribute` (`UserData` is a plain blob). → *Oracle:* stop canary; set userData; start; SSH with planted key. → **Critical** (unconditioned grants bundled into "EC2 power user"/CI roles). *Doc-gap:* whether a running (not stopped) instance accepts the change — `Using_ChangingAttributesWhileInstanceStopped` not fetched.
- *Claim (documented recovery, run offensively — Lens A intra-account):* a role with `ec2:Attach/DetachVolume` on `Resource:*` detaches another team's root volume and attaches to an attacker instance → mount → read/modify `authorized_keys`. No `ec2:Owner`/`aws:ResourceAccount` key exists on `volume`; only an explicit `ec2:ResourceTag`/`ec2:VolumeID` condition prevents it. → *Oracle:* unconditioned `Attach/DetachVolume`; detach a `team=victim` volume; attach to own instance. → **High** intra-account; **cross-account attach must FAIL** (volume ARN account-scoped) — refute that explicitly.
- *Claim (Lens H):* encryption is **not** a compensating control intra-account — the `aws:ec2-infrastructure/<instance>` identity-only role is same-account by construction, so an encrypted volume still attaches/mounts intra-account; a **CMK** gates only the (already-impossible) cross-account attach. → *Oracle:* repeat the attach against `aws/ebs`-encrypted and CMK-encrypted volumes intra-account; both succeed. → **High** (dispels "it's encrypted so it's safe").
- *Claim (Lens X — AWS self-documented):* `ebs:GetSnapshotBlock`/`ListSnapshotBlocks` read the full raw disk (incl. `authorized_keys`) of any nameable snapshot even when `ec2:CopySnapshot`/`ec2:CreateVolume` are explicitly **denied**. `ebsapi-permissions`: "you might give access to a user who is denied access to the same resource through the Amazon EC2 APIs." → *Oracle:* deny `ec2:CopySnapshot`/`CreateVolume`, allow `ebs:GetSnapshotBlock`+`ListSnapshotBlocks`; read a planted secret block-by-block. → **High** intra-account / **Critical** cross-account (shared snapshot).
**Doc evidence:** `API_ModifyInstanceAttribute`, `list_ec2`, `API_AttachVolume`/`API_DetachVolume`, `how-ebs-encryption-works`, `ebsapi-permissions`. **Severity-if-true:** Critical/High.

### Area D — Cross-account root-filesystem reach via snapshot/volume share *(PRIORITY 2)*
**Background.** The recovery runbook's volume-swap is intra-account; the cross-account analogues are the real IDOR-equivalents.
**Security Concern.** Sharing primitives hand out full root-volume contents (including `authorized_keys`), bypassing SSH auth entirely.
**High-level Test Scenarios.**
- *Claim (Lens AA):* `ModifySnapshotAttribute --group-names all` on an unencrypted root snapshot lets **any** account `CreateVolume` and read it; private share targets a named account. Public is blocked only if opt-in "Block public access for EBS snapshots" is enabled (not default-on in older accounts). → *Oracle:* share a canary snapshot publicly; from an unrelated account `CreateVolume`→attach→read. → **Critical** (zero trust relationship required).
- *Claim (Lens AA):* RAM volume share grants only view/copy, but `AWSRAMPermissionEBSVolumeCopyAccess` → `CopyVolumes` yields a fully-owned copy the consumer can attach/mount/read. Broad/org-wide grant = handing out volume contents. → *Oracle:* share a canary volume with copy-access; copy→attach→read planted secret. → **Critical** if the RAM permission is granted broadly.
**Doc evidence:** `ebs-modifying-snapshot-permissions`, `share-volume`. **Severity-if-true:** Critical.

### Area E — EICE `OpenTunnel` scoping & session decoupling *(PRIORITY 2)*
**Background.** EICE is an identity-aware TCP proxy; "configure route table rules to allow the endpoint to connect to **any instance in any subnet of the VPC**." `OpenTunnel`'s IAM **resource is the endpoint** (`instance-connect-endpoint*`), not the target instance; the only instance-binding condition is the optional CIDR `privateIpAddress`. Endpoint SG **inbound rules are ignored** ("allowed regardless of the inbound rules for the endpoint security group"). `PreserveClientIp` default **false** → all callers share the ENI IP. Tunnel **persists past IAM credential expiry** up to `maxTunnelDuration` (≤3600s).
**Security Concern.** "I scoped `OpenTunnel` to one endpoint" ≠ scoped to one instance; the real control is route tables + the optional CIDR condition + target-instance SG — not the thing most operators audit.
**High-level Test Scenarios.**
- *Claim:* `OpenTunnel` on an EICE ARN with no `privateIpAddress` condition reaches every route-reachable private IP/port in the VPC (incl. other subnets). → *Oracle:* grant endpoint-only; tunnel to multiple IPs/ports; all succeed. → **High** (Lens D/V).
- *Claim:* `PreserveClientIp=false` flattens source-IP SG rules on target instances; only an `aws:SourceIp` condition on the `OpenTunnel` call substitutes. → *Oracle:* two callers, different source IPs, target SG allows only VPC CIDR; both connect. → **Medium-High**.
- *Claim (Lens C):* a 15-min STS session opens a tunnel with `maxTunnelDuration=3600` that outlives the credential. → *Oracle:* expire the STS token; confirm the SSH session stays usable → **Medium** (revocation doesn't kill active tunnels).
**Doc evidence:** `connect-with-ec2-instance-connect-endpoint`, `permissions-for-ec2-instance-connect-endpoint`, `eice-security-groups`, `log-ec2-instance-connect-endpoint-using-cloudtrail`. **Severity-if-true:** High. *Attribution gap:* `OpenTunnel` logs `privateIpAddress`, not `instanceId` (private IPs recycle).

### Area F — Serial console = documented SG/NACL bypass *(PRIORITY 2)*
**Background.** `configure-access-to-serial-console`: "This connection is independent of the instance VPC … EC2 Serial Console **does not use the instance security group or the subnet network ACL**." Gates are only: (1) account `EnableSerialConsoleAccess`, (2) `SendSerialConsoleSSHPublicKey` IAM, (3) OS login. **No** `InstanceOSUser` param and **no** `ec2:osuser` condition key for this action → IAM cannot restrict which OS user. "Granting serial console permissions is equivalent to granting admin-level privileges on the instance."
**Security Concern.** An instance locked down to "no inbound SSH / bastion-only" is still fully reachable via serial console by anyone with the IAM action + account flag. Defenders auditing SGs/NACLs systematically miss this path.
**High-level Test Scenarios.**
- *Claim:* with SG denying all inbound SSH, a principal holding only `SendSerialConsoleSSHPublicKey` (+ account flag) reaches a login prompt. → *Oracle:* push + connect over the serial endpoint; success despite SG deny. → **High** (Lens D/V by design; a review blind spot).
- *Claim:* no IAM condition can restrict the OS user for serial console (unlike EIC's `ec2:osuser`). → *Oracle:* documentation-level — confirm `list_ec2-instance-connect` has only `aws:ResourceTag`/`ec2:ResourceTag` for this action. → **Medium-High** (structural IAM gap).
- *Claim (hygiene):* following the doc's `sudo passwd root` serial-console prereq creates a durable password-based root login that, if sshd allows root password auth, becomes a secondary network SSH path. → *Oracle:* set root password per doc; check AMI default `PermitRootLogin`/`PasswordAuthentication`; attempt network SSH as root. → **Medium** (doc tells you to open it, never to re-harden).
**Doc evidence:** `configure-access-to-serial-console`, `connect-to-serial-console`, `API_SendSerialConsoleSSHPublicKey`, `list_ec2-instance-connect`. **Severity-if-true:** High.

### Area G — `Operator`/`Managed` self-assertion & the "no user connections" guarantee *(PRIORITY 2, Lens U, AWS-owned)*
**Background.** The page: "User-initiated connections to managed instances are not allowed … find the **Managed** field … If the value is **true**, it's a managed instance." The linked `amazon-ec2-managed-instances` only restricts "directly modify the settings … or terminate it" — it **never** describes an SSH/SG/IAM control that blocks a connection. `RunInstances` accepts `Operator` (`OperatorRequest.Principal`, **"Reserved for internal use"**, no documented validation/allowlist/rejection). Visibility settings "do not affect … actual access permissions."
**Security Concern.** The troubleshooting page asserts a hard access guarantee with no documented enforcement mechanism (Lens U), and exposes a hidden knob that may let a customer forge the trust signal.
**High-level Test Scenarios.**
- *Claim:* "no user-initiated connections to managed instances" has no technical enforcement — normal SSH (owner key + SG) and `ssm:StartSession` still work on `Managed=true`. → *Oracle:* on a managed instance, attempt owner SSH + admin StartSession; success = convention-only control. → **Low** doc-accuracy / **High** if a customer builds a compliance boundary on it.
- *Claim:* a customer can set `Operator.Principal` on their own `RunInstances` to spoof `Managed=true`/an arbitrary principal. → *Oracle:* `RunInstances Operator.Principal=eks.amazonaws.com` from a normal principal; inspect `DescribeInstances` for `Operator.Managed=true`. Acceptance = spoofable signal; `ValidationException`/ignored = refuted. → **Medium-High** (deceives CSPM/inventory; chains with visibility-hiding to drop a live instance out of scope).
**Doc evidence:** `amazon-ec2-managed-instances`, `API_RunInstances`, `API_OperatorRequest`/`API_OperatorResponse`. **Severity-if-true:** Medium-High. *Doc-gap:* per-service (EKS/ECS/Lambda/WorkSpaces Core/Bedrock AgentCore) enforcement of the restriction is undocumented at the EC2 layer — follow-up per service.

### Area H — Cross-service private-key reachability for CFN key pairs *(PRIORITY 3, Lens T)*
**Background.** Console/CLI `CreateKeyPair` returns the private key once and **never stores it**. **Only** `AWS::EC2::KeyPair` via CloudFormation persists it to SSM `/ec2/keypair/{key_pair_id}` as a SecureString (retrieve with `ssm get-parameter --with-decryption`). (Corrects the common belief that *all* EC2-created key pairs land in SSM.)
**Security Concern.** The retrieval path uses **no `ec2:*` permission** — a principal explicitly denied all `ec2:*KeyPair` actions still recovers the plaintext key with `ssm:GetParameter` + `kms:Decrypt`.
**High-level Test Scenarios.**
- *Claim:* `Deny ec2:*KeyPair` + `Allow ssm:GetParameter /ec2/keypair/* , kms:Decrypt` → plaintext private key. → *Oracle:* CFN-create a key pair; from a second principal with that policy, `get-parameter --with-decryption`; success. → **High** intra-account; **Critical** if SSM read is wildcarded in a shared "read all params" policy.
- *Claim (Lens EE/T):* the path is keyed by high-entropy `key-…` id, not `KeyName`; `ec2:DescribeKeyPairs` (often granted as "harmless read") bridges name→id→secret. → *Oracle:* with only `DescribeKeyPairs`+`ssm:GetParameter`+`kms:Decrypt`, walk name→id→SSM. → **Medium-High**.
**Doc evidence:** `create-key-pairs#create-key-pair-cloudformation`, `aws-resource-ec2-keypair`, `ec2-key-pairs`, `delete-key-pair`. **Severity-if-true:** High. *Doc-gap:* which KMS key encrypts the CFN SSM SecureString is unstated.

### Area I — AWS-authored launch-wizard default security group *(PRIORITY 3, Lens R/U, AWS-owned)*
**Background.** The page itself: "The default security group for the VPC does not allow incoming SSH traffic by default. **The security group created by the launch instance wizard enables SSH traffic by default.**" `ec2-instance-launch-parameters`: "If you create a new security group, we automatically create an inbound rule that allows you to connect … from **all IP addresses** over SSH (Linux) or RDP (Windows)." AWS pairs this with a prose warning ("unsafe for production").
**Security Concern.** AWS (not the customer) authors a `0.0.0.0/0:22` inbound rule as the wizard default — a **disclosed** AWS-authored insecure default (Lens R carve-out: AWS-authored → in scope), mitigated only by a click-past warning, not a safe default or a creation-time guardrail.
**High-level Test Scenarios.**
- *Claim:* launching via the console wizard with a new SG yields `0.0.0.0/0:22` inbound unconditionally. → *Oracle:* already confirmed by doc text ("we automatically create"); live-confirm the resulting SG rule. → **Medium** (disclosed AWS-authored default).
**Doc evidence:** `TroubleshootingInstancesConnecting`, `ec2-instance-launch-parameters`, `security-group-rules-reference`. **Severity-if-true:** Medium.

### Area J — Host-key / fingerprint trust & `GetConsoleOutput` *(PRIORITY 3, Lens Y)*
**Background.** "Host key verification failed" ↔ `known_hosts` mismatch; the page recommends verifying the fingerprint via `connection-prereqs-general#connection-prereqs-fingerprint`. The authoritative fingerprint comes from **instance console output** (`BEGIN SSH HOST KEY FINGERPRINTS`), gated by "You must be the instance owner to get the console output." The doc frames fingerprint verification around the **untrusted third-party AMI** threat.
**Security Concern.** The fingerprint is sourced from *inside* the very boot process being verified — if the AMI or pre-sshd user-data is attacker-influenced, a forged fingerprint block can appear in console output the owner then trusts.
**High-level Test Scenarios.**
- *Claim:* an AMI/user-data combo can write an attacker-chosen `BEGIN SSH HOST KEY FINGERPRINTS` block into console output before real sshd key-gen, which the owner treats as authoritative. → *Oracle:* launch such an AMI; `get-console-output`; observe the forged block. → **Low-Informational** (the "public third-party AMI" caveat already discloses this residual risk; the IAM gate itself works).
**Doc evidence:** `connection-prereqs-general`, `TroubleshootingInstancesConnecting`. **Severity-if-true:** Low-Informational.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Push-as-root to any instance via stock policy | `SendSSHPublicKey` + `EC2InstanceConnect` policy | `ec2:osuser` + instance-ARN/tag scoping (**absent in the shipped policy**) |
| Cross-account host-key poisoning / MITM | `eic_harvest_hostkeys` → trusted-host-key store | assumed `(AccountId,InstanceId)` binding via instance identity (**undocumented**) |
| `authorized_keys` rewrite without SSH | `ModifyInstanceAttribute(userData)` | `ec2:ResourceTag`/`ec2:Attribute` condition (**opt-in**); **no `iam:PassRole`** |
| Read another team's root volume | `Attach/DetachVolume` | `ec2:ResourceTag`/`ec2:VolumeID` condition (opt-in); account-scoped ARN blocks cross-account |
| Read raw disk despite EC2 deny | `ebs:GetSnapshotBlock` | separate IAM surface; AWS warns in `ebsapi-permissions` |
| Cross-account root-fs via share | `ModifySnapshotAttribute`, RAM volume copy | "Block public access for EBS snapshots" (opt-in); KMS for encrypted |
| Private key recovery bypassing EC2 deny | SSM `/ec2/keypair/*` + KMS | scope `ssm:GetParameter` path + deny `kms:Decrypt` |
| VPC-wide reach from one EICE grant | `OpenTunnel` | optional `privateIpAddress` CIDR condition + route tables + target SG |
| SG/NACL bypass | serial console | account `EnableSerialConsoleAccess` off + `SendSerialConsoleSSHPublicKey` IAM scoping |
| Spoofed `Managed=true` / false "unreachable" | `RunInstances Operator.Principal` | **none documented** (field "reserved for internal use") |
| Wizard SG opens SSH to the world | launch-instance wizard | prose warning only |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Customer-authored SG/NACL/route-table misconfiguration** (typing `0.0.0.0/0` into a rule, narrowing NACL ephemeral egress, missing IGW route) — self-inflicted least-privilege footguns, **not reportable**. (The *wizard-authored* default SG in Area I is the exception — AWS authored it.)
- **A customer steering their own instance / their own IAM** — e.g. an admin who already holds `*:*` using these primitives on their own fleet.
- **IMDS on fully-managed hosts** (per standard carve-out).
- **SSH TOFU / `known_hosts` protocol design** critiques — SSH-protocol level, not AWS-specific.
- **AMI supply-chain integrity for AWS-owned Quick Start AMIs** — separate, larger surface.
- **whoAMI-style name-resolution squatting** against the *documented* recovery flow — **refuted**: the runbook pins a noted AMI **ID**, not a name/`latest` filter. Only a lead for *automated* re-implementations (IR Lambda / SSM Automation / Terraform) that resolve "the same AMI" by name without `--owners` — and that is a **code-review** question, **not** an AWS-doc claim; do not cite AWS docs for it.
- **Deep SSM Agent↔service protocol analysis** — not documented at that depth; Session Manager here is a cross-reference, not the focus.
- **Shared RDS/Aurora/Grover/storage infra** and anything reaching the **AWS service plane** — HARD STOP + disclose, not to be pursued as a pentest objective.

---

## 8. Null Hypotheses / Doc Gaps (surfaces needing confirmation first)

1. **`eic_harvest_hostkeys` backend API + auth model — UNKNOWN.** No action in `list_ec2-instance-connect`; not a customer IAM-governable call. **Top research item** — reverse-engineer the on-instance egress (endpoint, SigV4 vs signed instance-identity doc, scoping) before any poisoning test. Mark affected leads "doc-gap — confirm surface first." (Both the EIC and the network-path subagents independently flagged this.)
2. **`Operator.Principal` validation on `RunInstances`** — `API_RunInstances`/`API_OperatorRequest`/`API_OperatorResponse` state no acceptance/rejection behavior for customer-supplied values. Not testable from docs — needs a live `RunInstances` + `DescribeInstances` check.
3. **Enforcement of "user-initiated connections to managed instances are not allowed"** — no mechanism named in any EC2 UserGuide page; per-service (EKS Auto Mode / ECS managed instances / Lambda managed instances / WorkSpaces Core / Bedrock AgentCore) enforcement is undocumented at the EC2 layer. Pull each service's own docs.
4. **No SLR/IAM artifact** for the EC2-level managed-instances/`Operator` mechanism is documented (only Capacity Reservation Fleet, Capacity Manager, Spot SLRs exist in the EC2 UserGuide) — notable absence.
5. **Does `ModifyInstanceAttribute(userData)` require a stopped instance?** `Using_ChangingAttributesWhileInstanceStopped` not fetched — treat "stopped-only" as unconfirmed.
6. **KMS key encrypting the CFN key-pair SSM SecureString** — unstated (`alias/aws/ssm` default assumed, not confirmed).
7. **`aws:ResourceAccount`/cross-account condition-key coverage for EC2 actions** — the hosted Service Authorization HTML is a JS SPA and the `.md` export 404'd; all condition-key claims rest on the **offline mirror** `list_ec2.md`/`list_ebs.md`/`list_ec2-instance-connect` and should be re-verified against the live page if mirror staleness is a concern. (Absence of `ec2:Owner`/`aws:ResourceAccount` on the `volume` resource type is treated as doc-confirmed negative evidence.)
8. **SSM RunCommand/Session Manager write-paths to `authorized_keys`** — not deep-dived; a known additional SSH-equivalent primitive gated by `ssm:SendCommand` + instance profile.
9. **Lenses that did not fire** (named surfaces checked): **F** (translation/wire-protocol injection — no customer-input→backend-language transform on these pages), **K** (prompt injection — no LLM/agent in this connect path; Bedrock AgentCore appears only as a *managed-instance provider* name, not an input seam here), **J/OAuth** (no 3P OAuth linking), **W** (attestation-gated KMS — not on these pages), **BB/CC/DD** (multi-parser canonicalization, upstream-context injection, cache-key divergence — no authorizer/CDN/caching layer in these connect flows), **FF** (JWT/OIDC token validation — none in these flows). Null by evidence, not assumption.

---
*Generated by the `security-questionbuilder` skill against documentation only. No live AWS calls were made. All leads are falsifiable hypotheses for a downstream authorized hunter (`aws-vuln-hunter`).*
