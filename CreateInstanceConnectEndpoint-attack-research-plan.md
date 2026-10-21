# CreateInstanceConnectEndpoint (EC2 Instance Connect Endpoint / EICE) — Attack Research Plan

**Source of leads:**
- `API_CreateInstanceConnectEndpoint.html` / `.md` (target), `API_Ec2InstanceConnectEndpoint.html` (response shape)
- UserGuide: `connect-with-ec2-instance-connect-endpoint`, `permissions-for-ec2-instance-connect-endpoint`, `eice-security-groups`, `eice-slr`, `log-ec2-instance-connect-endpoint-using-cloudtrail`
- IAM refs: `list_ec2.md` (CreateInstanceConnectEndpoint row, line 5155), `list_ec2-instance-connect.md` (OpenTunnel/SendSSHPublicKey)
- AWS-managed policy `Ec2InstanceConnectEndpoint` (SLR policy, v2, edited 2025-07-31)

**Status:** documentation-derived hypotheses only. Nothing tested against a live account. Online docs cross-checked against the offline mirror; they agree.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the EICE Service is an AWS-owned, multi-tenant "identity-aware TCP proxy" fleet. The moment evidence shows an identity/credential/ARN/host belonging to that fleet (or any AWS service plane), stop, preserve evidence, flag for AWS-Security disclosure. Do **not** attack the shared proxy fleet itself; the customer-facing OpenTunnel/Create APIs are the in-scope entry.
- `DryRunOperation` is caller-IAM-only — **not** an ownership/existence oracle (evaluated before resource resolution). Do not treat a DryRun pass as proof an action would succeed.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. **Create-path scoping escape:** create an EICE with a security group or in a subnet/VPC that a least-privilege policy (keyed on `ec2:SecurityGroupID` / `ec2:SubnetID` / `ec2:Vpc`) was written to forbid — by exploiting the **non-required security-group leg** or a missing condition key (PreserveClientIp / IpAddressType).
2. **ABAC self-widen:** create an EICE whose tags satisfy an `OpenTunnel` `aws:ResourceTag` allow the creator was not meant to reach, then tunnel to protected instances.
3. **Lateral reach primitive:** stand up an EICE and use `OpenTunnel` to reach instances across subnets/AZs of the VPC that the creator has no instance-level permission on (OpenTunnel has **no instance resource and no instance-tag key**).
4. **SLR over-privilege:** show the AWS-managed `Ec2InstanceConnectEndpoint` SLR policy performs an ENI/SG action its stated purpose ("manage ENIs created by the customer") does not require — specifically the **unconditioned `security-group/*` and `subnet/*` legs**.
5. **Revocation gap:** show an established tunnel survives revocation/expiry of the IAM credentials that opened it (doc-asserted), and whether Delete/Modify actually tears live tunnels down.
6. **Audit gap:** show a security-relevant EICE operation that produces no CloudTrail record (e.g. `ModifyInstanceConnectEndpoint` is not in the logged-API list).

---

## 2. Components, Assets, and Design

**What it is.** EICE lets you SSH/RDP to instances with no public IP, from the internet, with no bastion and no IGW. It is an **identity-aware TCP proxy**: the AWS-owned *EC2 Instance Connect Endpoint Service* terminates a private tunnel opened with the caller's IAM credentials (`OpenTunnel`), authenticates/authorizes it, then forwards TCP into the customer VPC through an **ENI the service provisions in the customer's subnet** (via the SLR).

**Identifiers.** Endpoint id `eice-...` (ARN `arn:aws:ec2:region:acct:instance-connect-endpoint/eice-...`, max len 1283). Note the CloudTrail example uses `eici-...` / key `instanceConnectEndpointId` — legacy-prefix inconsistency worth noting.

**Processes / fleets.**
- **EICE Service** — AWS-owned multi-tenant proxy fleet (service principal `ec2-instance-connect.amazonaws.com`). Terminates `OpenTunnel`. **Service plane → hard stop.**
- **EICE ENI** — lives in the *customer* subnet, created/managed by the **SLR `AWSServiceRoleForEC2InstanceConnect`**. This ENI is the ingress point into the VPC.
- **Target instances** — customer-owned, reached by VPC routing from the EICE subnet.

**Accounts/VPCs.** Single-account by design: endpoint, ENI, and instances are all in the caller's account/VPC. Cross-AZ reach is allowed (data-transfer charge). "You can configure route table rules to allow the endpoint to connect to any instance in any subnet of the VPC" → **one EICE ⇒ whole-VPC reach**.

**Identity / auth.** SigV4 IAM on `CreateInstanceConnectEndpoint` and on `OpenTunnel`. Tunnel lifetime is **decoupled from credential lifetime** (see Lead 5.5). Max tunnel 3600 s; 20 concurrent connections/endpoint; 1 endpoint per VPC per subnet.

**Untrusted inputs to Create:** `SubnetId` (required), `SecurityGroupId.N` (0–16, optional → default SG), `IpAddressType` (ipv4/dualstack/ipv6), `PreserveClientIp` (bool), `TagSpecification.N`, `ClientToken`.

```
Internet client ──SigV4 OpenTunnel──►  EICE Service (AWS multi-tenant proxy)   [HARD STOP zone]
                                             │  TCP forward
                                             ▼
                              EICE ENI  (customer subnet A, SLR-provisioned)
                                             │  VPC route tables / SG egress
                                             ▼
                          target instance (subnet B, any AZ in VPC)
  Create-path authz:  ec2:CreateInstanceConnectEndpoint (+CreateNetworkInterface, CreateTags, iam:CreateServiceLinkedRole)
  Use-path authz:     ec2-instance-connect:OpenTunnel  (scoped on the ENDPOINT, not the instance)
                      ec2-instance-connect:SendSSHPublicKey (scoped on the instance, ec2:osuser)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller IAM principal | EICE ENI placement (subnet/SG/VPC) | `CreateInstanceConnectEndpoint` | Endpoint created in a subnet/VPC or with an SG a scoped policy forbade = create-scoping breach |
| Caller IAM principal | Any instance in the VPC | `OpenTunnel` (endpoint-scoped) | TCP reaches an instance the caller has no instance-level permission to, and no `remotePort`/`privateIpAddress` condition blocked it |
| Internet client | Customer VPC | EICE Service proxy + ENI | Reaching any VPC host other than the authorized target/port = routing/segmentation breach |
| Caller (tag-setter at create) | OpenTunnel ABAC allow | `TagSpecification` → `aws:ResourceTag` on endpoint | Creator self-tags endpoint to satisfy an OpenTunnel allow it shouldn't reach |
| SLR `AWSServiceRoleForEC2InstanceConnect` | Any SG / any subnet in account | unconditioned policy legs | Service modifies/creates against an ENI/SG the "customer-created EICE" purpose did not require |
| Established tunnel | IAM credential lifecycle | tunnel persists after creds expire | Tunnel keeps forwarding after the opening credentials are revoked/expired |
| Any customer | **EICE Service fleet** | shared multi-tenant proxy | Any cross-tenant data/credential on the proxy = **HARD STOP, service plane** |

---

## 4. API / Interface Inventory

| Name | Namespace | Mutating | Ext-facing | Functionality | Authorized callers | Condition keys (notable) | Notes |
|---|---|---|---|---|---|---|---|
| CreateInstanceConnectEndpoint | ec2 | yes | yes | create EICE + ENI | IAM w/ create perms | endpoint leg: RequestTag/TagKeys/Region/**SubnetID**; **security-group leg (NOT required)**: SecurityGroupID/Vpc/ResourceTag; subnet leg: AZ/Region/SubnetID/Vpc/ResourceTag | **No key for PreserveClientIp or IpAddressType.** Needs CreateNetworkInterface+CreateTags+iam:CreateServiceLinkedRole |
| ModifyInstanceConnectEndpoint | ec2 | yes | yes | modify EICE | IAM | (check list_ec2:3739) | **NOT in CloudTrail logged-API list** (Lead 5.6) |
| DeleteInstanceConnectEndpoint | ec2 | yes | yes | delete EICE | IAM | (check list_ec2:963) | Logged |
| DescribeInstanceConnectEndpoints | ec2 | no | yes | list EICEs | IAM | no resource-level (needs `*`) | Logged; recon |
| OpenTunnel | ec2-instance-connect | yes (readOnly:false) | yes | open TCP tunnel to instance | IAM (endpoint-scoped) | `instance-connect-endpoint*`; aws/ec2:ResourceTag; **maxTunnelDuration / privateIpAddress / remotePort** | **No instance resource / no instance-tag key.** Note PascalCase `MaxTunnelDuration` vs camelCase `maxTunnelDuration` in the ref |
| SendSSHPublicKey | ec2-instance-connect | yes | yes | push ephemeral SSH key (60 s) | IAM (instance-scoped) | aws/ec2:ResourceTag; **ec2:osuser** | Instance-scoped, unlike OpenTunnel |
| SendSerialConsoleSSHPublicKey / OpenSerialConsoleSession | ec2-instance-connect | yes | yes | serial console | IAM (instance-scoped) | ResourceTag | adjacent surface |

---

## 5. Recommended Areas of Focus

### 5.1 Create-path: non-required security-group leg fails open  — **Lens S / U** — Severity: Medium–High
**Background.** `CreateInstanceConnectEndpoint` has three IAM legs. Only `instance-connect-endpoint*` and `subnet*` are marked required (`*`); the **`security-group` leg is NOT required**. `SecurityGroupId.N` is optional and defaults to "the default security group for your VPC."
**Security Concern.** An admin who scopes EICE creation with `ec2:SecurityGroupID` / `ec2:ResourceTag` on the SG (to force EICEs onto a locked-down egress SG) is bypassed: **omit `SecurityGroupId.N`** and the SG leg's conditions are never evaluated — the default SG attaches. If the VPC default SG has broad egress, the EICE can reach the whole VPC on any port its outbound rules allow.
**High-level Test Scenarios.**
- Under a role whose EICE-create is `Deny` unless SG tag `eice=true`: call Create with no `SecurityGroupId.N`. **Confirm:** endpoint created with default SG (Deny inert). **Refute:** AccessDenied.
- Does `ec2:SecurityGroupID` get enforced when an SG *is* supplied but a second is omitted? (partial-evaluation like the Authorize* family.)
**Doc evidence:** `list_ec2.md:5157-5159` (no `*` on security-group leg); Create param doc "If you don't specify a security group, the default security group for your VPC will be associated." **Severity-if-true:** Medium–High (least-priv create-scoping escape; High if the default SG grants broad VPC egress).

### 5.2 PreserveClientIp / IpAddressType are not IAM-expressible — **Lens S / U** — Severity: Medium
**Background.** `PreserveClientIp` and `IpAddressType` change the security posture: with `PreserveClientIp=false` (default) the **instance SG must allow the whole VPC CIDR** on the management port; the EICE ENI's own inbound SG rules are *ignored* ("Traffic to the endpoint … is allowed regardless of the inbound rules for the endpoint security group").
**Security Concern.** The create action exposes **no condition key** for either parameter. An org cannot write IAM that says "EICEs must use PreserveClientIp=true" (to force client-IP-based SG filtering) or "ipv4 only." The only control over who connects is the OpenTunnel IAM policy — the network layer is deliberately open from the ENI.
**High-level Test Scenarios.**
- Enumerate create-leg keys: confirm no `ec2:PreserveClientIp`/`ec2:IpAddressType` exists (string-match the IAM ref; absence = lead).
- Create a `PreserveClientIp=false` EICE and confirm the instance SG rule granting `VPC-CIDR:22` now accepts traffic sourced from the EICE ENI for *every* instance in the VPC with that rule → whole-VPC SSH reach from one endpoint.
**Doc evidence:** `list_ec2.md:5157`; `eice-security-groups.md` ("allowed regardless of the inbound rules for the endpoint security group"); Considerations ("If you turn off client IP preservation, the security groups for the instances must allow traffic from the VPC"). **Severity:** Medium (hardening/doc-vs-enforcement gap; the reachability itself is by-design).

### 5.3 Tag-on-create → OpenTunnel ABAC self-widen — **Lens I / S (self-widen variant)** — Severity: High
**Background.** Create supports `aws:RequestTag`/`aws:TagKeys` on the endpoint leg. `OpenTunnel`'s only resource is the **endpoint**, and it supports `aws:ResourceTag/${TagKey}` / `ec2:ResourceTag/${TagKey}` on that endpoint.
**Security Concern.** If OpenTunnel is gated by an endpoint tag (e.g. `Allow OpenTunnel where ResourceTag/team=payments`), a principal who can create an EICE **and set tags at create** can mint an endpoint tagged `team=payments` and then tunnel through it — self-granting the OpenTunnel allow. The gate is only sound if CreateInstanceConnectEndpoint independently denies the privileged tag (via `aws:RequestTag` condition) — easy to forget.
**High-level Test Scenarios.**
- Role allowed to create EICEs (no `RequestTag` restriction) + allowed `OpenTunnel` only on `ResourceTag/team=payments`. Create EICE with `TagSpecification team=payments`; then OpenTunnel. **Confirm:** tunnel opens. **Refute:** create denied or OpenTunnel denied.
- Also test `CreateTags`/`ModifyInstanceConnectEndpoint` *after* create to add the blessed tag (post-create self-widen), mirroring the Accept/Authorize self-widen pattern seen elsewhere in EC2.
**Doc evidence:** `list_ec2.md:5157` (RequestTag on create); `list_ec2-instance-connect.md:46` (OpenTunnel ResourceTag). **Severity:** High (ABAC access-control bypass to a connect primitive).

### 5.4 OpenTunnel is endpoint-scoped, not instance-scoped — whole-VPC connect primitive — **Lens A / V / X** — Severity: High
**Background.** `OpenTunnel`'s required resource is `instance-connect-endpoint*`. It has **no instance resource type and no instance-level condition key** — the only instance-targeting controls are `ec2-instance-connect:privateIpAddress` (CIDR) and `remotePort`, which **default to unrestricted** if not set. `SendSSHPublicKey` (which *is* instance+`ec2:osuser` scoped) is only needed when you don't already hold a key; the Considerations note "If you use your own key pair, you can use any Linux AMI" — i.e. with a pre-installed key, **OpenTunnel alone yields raw TCP to the instance.**
**Security Concern.** A principal granted `OpenTunnel` on an endpoint (resource `*` or a shared endpoint) can reach **any instance/port reachable by VPC routing from that endpoint's subnet**, independent of any instance-level IAM, instance tags, or SendSSHPublicKey scoping — unless the admin remembered to pin `privateIpAddress` + `remotePort`. This is the classic "the control is on the wrong resource" shape (Lens X: the checked read `SendSSHPublicKey` is instance-scoped; its tunnel twin `OpenTunnel` is not).
**High-level Test Scenarios.**
- Grant `OpenTunnel` on one endpoint with no `privateIpAddress`/`remotePort` condition. Attempt tunnels to multiple instances across subnets/AZs. **Confirm:** TCP reaches instances the principal has no `ec2:*`/instance-tag grant on.
- Confirm default behavior: omit both condition keys → any private IP / any port accepted (doc says if not specified, no restriction).
- Chain: pre-shared key on target + OpenTunnel → full SSH without `SendSSHPublicKey`/`ec2:osuser` ever evaluated.
**Doc evidence:** `list_ec2-instance-connect.md:44-48`; `permissions-for-…#iam-OpenTunnel` (privateIpAddress/remotePort optional); Considerations (own key pair). **Severity:** High (connect-scope breach across the VPC; the `remotePort`/`privateIpAddress` defaults are fail-open).

### 5.5 Tunnel lifetime decoupled from credential lifetime — revocation gap — **Lens AA / O** — Severity: Medium–High
**Background.** Doc: "The duration of the connection is not determined by the duration of your IAM credentials. If your IAM credentials expire, the connection continues to persist until the specified maximum duration is reached" (up to 3600 s; default 3600 s if `maxTunnelDuration` unset).
**Security Concern.** Revoking/expiring the IAM principal (key deactivation, role-session kill, SCP change) does **not** sever an already-open tunnel. An attacker who opens a long tunnel just before detection keeps live TCP (interactive shell) for up to an hour after creds are killed. Also: if `maxTunnelDuration` is omitted in policy, it silently defaults to the 3600 s max — a scoped-down policy that forgets the key gets the maximum, not the minimum (fail-open default).
**High-level Test Scenarios.**
- Open a tunnel, then deactivate/revoke the opening credentials. **Confirm:** existing tunnel keeps forwarding; measure survival window.
- Does `DeleteInstanceConnectEndpoint` / `ModifyInstanceConnectEndpoint` (e.g. swapping to a deny-all SG) tear down **live** tunnels, or only block new ones? (resilience + incident-response oracle.)
- Confirm `maxTunnelDuration` absent ⇒ 3600 s default (not a minimum).
**Doc evidence:** Considerations paragraph on connection duration; `permissions-…#iam-OpenTunnel` (default 3600). **Severity:** Medium–High (defeats credential revocation as an IR control; fail-open duration default).

### 5.6 CloudTrail coverage gap: ModifyInstanceConnectEndpoint not listed — **Lens O** — Severity: Low–Informational (enabler)
**Background.** The logging page lists only `CreateInstanceConnectEndpoint`, `DescribeInstanceConnectEndpoints`, `DeleteInstanceConnectEndpoint` as logged management events, plus `OpenTunnel`. **`ModifyInstanceConnectEndpoint` is absent** from the list, yet the permissions page treats it as a first-class mutating action.
**Security Concern.** If Modify (e.g. changing the endpoint's security groups / posture) is genuinely unlogged, an attacker can re-point or re-open an endpoint's egress without a CreateTrail record — a blind spot for detection built on the documented event set.
**High-level Test Scenarios.** Call `ModifyInstanceConnectEndpoint` and check Event history / data for a management event. **Confirm:** no record (or only partial). **Refute:** event present (doc list merely incomplete).
**Doc evidence:** `log-ec2-instance-connect-endpoint-using-cloudtrail.md:15-19`. **Severity:** Low–Informational (detection gap; raises severity of 5.1/5.3 as an enabler).

### 5.7 SLR `Ec2InstanceConnectEndpoint` over-broad legs — **Lens R / S** — Severity: Medium–High
**Background.** The AWS-managed, **uneditable** SLR policy (v2, edited **2025-07-31**) is attached to `AWSServiceRoleForEC2InstanceConnect`. Its stated purpose: "create and manage network interfaces … required by EICE." Two legs exceed that shape:
- `ec2:ModifyNetworkInterfaceAttribute` on **`arn:aws:ec2:*:*:security-group/*` with NO Condition** — the service may reference/modify against **any** SG in the account, not just eice-tagged resources.
- `ec2:CreateNetworkInterface` on **`arn:aws:ec2:*:*:subnet/*`** (all subnets) unconditioned; only the `network-interface/*` leg is tag-gated.
- `ec2:DeleteNetworkInterface` / `ModifyNetworkInterfaceAttribute` / `Assign*Ipv6` are gated by `aws:ResourceTag/InstanceConnectEndpointId = eice-*` — a **tag the service sets at create via `aws:RequestTag`**. If a customer with `ec2:CreateTags` can stamp `InstanceConnectEndpointId=eice-*` onto a **non-EICE ENI**, the SLR's tag-scoped delete/modify legs would then apply to that foreign ENI (tag-collision confused-deputy).
**Security Concern.** Because the policy is AWS-authored and copy-verbatim/uneditable, a weak default here is AWS's defect (disclosure Tier 2). The unconditioned `security-group/*` leg and the customer-settable scoping tag are the audit targets.
**High-level Test Scenarios.**
- `iam:GetPolicyVersion` the live `Ec2InstanceConnectEndpoint` v2; diff vs this doc. Statement-by-statement, confirm the `security-group/*` leg has no Condition.
- Tag a non-EICE ENI `InstanceConnectEndpointId=eice-xxxx` with `ec2:CreateTags`; test whether any EICE lifecycle operation (delete endpoint) induces the SLR to act on that ENI. Use **canary ENIs only**; this probes a confused-deputy, not destruction of real resources — stop at first proof.
- `iam:SimulatePrincipalPolicy` against the SLR as the safe first oracle (no resources touched).
**Doc evidence:** `Ec2InstanceConnectEndpoint.md:124-141` (unconditioned security-group leg), `:46-52` (subnet leg), `:128-141` (tag-scoped delete). **Severity:** Medium–High (AWS-managed over-grant; cross-ENI reach via tag collision if provable).

### 5.8 Describe recon + idempotency/race — **Lens A / L** — Severity: Low
**Background.** `DescribeInstanceConnectEndpoints` has no resource-level permissions (needs `Resource:*`). `ClientToken` provides idempotency; quota is 1 endpoint per VPC/subnet and 20 concurrent connections/endpoint.
**Security Concern / Scenarios.** (a) Does Describe leak endpoints (ids, subnet/VPC, SGs, ENI ids) beyond what the caller's other grants would show? (b) Idempotency race: two concurrent Creates with different ClientTokens against the 1-per-subnet quota — clean error or partial/duplicate ENI? (c) 20-connection cap: can one principal exhaust an endpoint's connection slots (self/noisy-neighbor DoS within the account)? **Severity:** Low (single-account info/DoS).

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Create EICE with default SG to dodge SG-scoped create policy | CreateInstanceConnectEndpoint | non-required security-group leg (5.1) |
| Self-tag endpoint to satisfy OpenTunnel ABAC | Create + OpenTunnel | RequestTag/ResourceTag coupling (5.3) |
| Reach non-authorized instances via one endpoint | OpenTunnel | endpoint-scoped resource, optional privateIpAddress/remotePort (5.4) |
| Keep shell alive past credential revocation | EICE Service tunnel | credential/tunnel-lifetime decoupling (5.5) |
| Mutate endpoint posture without a CloudTrail trace | ModifyInstanceConnectEndpoint | logged-API list omits Modify (5.6) |
| SLR acts on a foreign ENI/SG | AWSServiceRoleForEC2InstanceConnect | unconditioned security-group/subnet legs, customer-settable scoping tag (5.7) |
| PreserveClientIp posture cannot be IAM-enforced | CreateInstanceConnectEndpoint | no condition key (5.2) |

---

## 7. Out-of-Scope Risk Categories
- The **EICE Service** multi-tenant proxy fleet itself (attacking it, cross-tenant on it) — AWS service plane, **hard stop / disclose only**.
- IMDS on managed/target instances; SSH-layer crypto; the sshd on the customer's own instance.
- Single-account self-DoS beyond the connection-cap note (5.8) is informational.
- Customer-authored IAM least-privilege footguns (in scope **only** for the AWS-managed SLR policy, 5.7).
- Data-plane byte inspection of the tunnel (it is a TCP proxy; SSH content is customer's responsibility).

## 8. Null hypotheses / doc gaps
- **SSRF (Lens G): N/A** — read all Create params, Ec2InstanceConnectEndpoint response, security-group and SLR pages; no field is a URL/host the service fetches server-side. `SubnetId`/`SecurityGroupId` are resolved internally, not dereferenced externally.
- **KMS / encryption-context (Lens H): N/A** — no customer-key or encryption-context field on this action.
- **File upload / parser (Lens Q/F): N/A** — no blob/parse input.
- **Cross-account (Lens B/C): N/A by design** — endpoint, ENI, instances are same-account; no role-ARN/PassRole input (the SLR is auto-created, 5.7 covers it). Confirm `iam:CreateServiceLinkedRole` cannot be pointed at a custom role.
- **Doc gaps to confirm on a live account first:** exact condition keys on `ModifyInstanceConnectEndpoint` (what it can change — SGs? PreserveClientIp?); whether `ModifyInstanceConnectEndpoint` is truly unlogged; exact `maxTunnelDuration` default when the key is omitted in policy; the live `Ec2InstanceConnectEndpoint` SLR v2 JSON (pull with GetPolicyVersion). Mark these "doc-gap — confirm surface first."

---
*Prioritization (Step 5): fire order is 5.4 (whole-VPC connect primitive) ≈ 5.3 (ABAC self-widen) > 5.1 (SG-leg fail-open) > 5.7 (SLR over-grant, recently changed 2025-07-31) > 5.5 (revocation gap) > 5.2 > 5.6 > 5.8. The 2025-07-31 SLR edit makes 5.7 "changed surface" — diff v1→v2.*
