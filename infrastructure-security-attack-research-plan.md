# EC2 Infrastructure Security (overview page) — Attack Research Plan

Source of leads: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/infrastructure-security.md` (the EC2 Security chapter topic "Infrastructure security in Amazon EC2", `infrastructure-security.html`) and its linked children — `interface-vpc-endpoints.md`, `connect-linux-inst-eic.md` + the EC2 Instance Connect / EC2 Instance Connect Endpoint (EICE) family, `ec2-security-groups.md`, and the SSM Session Manager / Run Command cross-service pointers. Authoritative IAM: `/work/aws-docs/docs/service-authorization/latest/reference/{list_ec2.md, list_ec2-instance-connect.md, list_ssm.md}` (grepped directly — trusted over User-Guide prose per skill discipline). Status: documentation-derived hypotheses only; **nothing tested against a live account**. Offline == online verified verbatim 2026-10-15 (no drift).

This page is a **template-driven, guarantee-dense / API-sparse** security-chapter overview: it asserts security *properties* (TLS floor, VPC/physical-host isolation, MAC/IP anti-spoofing) and then catalogs **network-traffic-control options**. It introduces **no new API of its own**. Its value is therefore (a) guarantee-vs-enforcement (Lens U/Y/V) and (b) the fact that it is the one chapter page that *enumerates the alternative, IAM-gated instance-ingress channels* side-by-side.

**De-duplication (this plan is a COMPLEMENT, not a restatement).** Two existing sibling plans already own most of this page's cross-references; they are cross-referenced, not re-derived:
- Physical-host isolation / hypervisor CPU-memory isolation / memory-scrub-on-stop / block-storage-reset / Nitro operator-isolation / EBS-&-in-transit encryption / the TLS-at-rest story → **`ec2-data-infrastructure-protection-attack-research-plan.md`** (which already pulls `infrastructure-security.md`'s network-traffic-control section in as a trust-boundary citation) and **`data-protection-attack-research-plan.md`** (T1 inter-instance Nitro encryption, T4 transport/`aws:SecureTransport`, no `aws:TlsVersion` key).
- Security groups + NACLs + the PrivateLink **interface VPC endpoint for the EC2 API** (`com.amazonaws.<region>.ec2`) + its endpoint-policy posture → **`ec2-security-groups-privatelink-attack-research-plan.md`** (its objective #5 already covers the EC2-API endpoint).
- Shared-VPC owner/participant isolation, source/dest-check-on-ENI, dual-homed OS-bridge, requester-managed-ENI Reset→SourceDestCheck=true → **`using-vpc-`, `scenarios-enis-`, `requester-managed-eni-`, `ena-nitro-perf-attack-research-plan.md`**.

**What THIS plan uniquely owns:** the **EC2 Instance Connect / EICE IAM-gated ingress family** (service prefix `ec2-instance-connect`, no dedicated prior plan), the **source/destination-check disable lever** as a Lens-S "no dedicated condition key" finding, and the **overview-page synthesis** that security groups are documented as "the primary mechanism" while the same page lists ≥3 IAM-gated channels (EIC, SSM Session Manager, Run Command) that reach the instance with **no inbound SG rule at all** — each governed by a *different* IAM service, a split-brain audit surface.

---

## 0. How to use this document

- Each lead in Section 5: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the hypervisor, the Nitro controller, the AWS network fabric that enforces anti-spoof), stop, preserve evidence, flag for AWS-Security disclosure. The physical-host / anti-spoof guarantees on this page are *AWS-infra enforcement claims* — characterize the mechanism, do not attempt to break it.
- Safe first oracle for every IAM-scoping lead is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (a condition key either applies to an action or it does not — no resource creation needed). Escalate to a live scoped call only with synthetic canary data.
- `list_*.md` line numbers are from the author's read at research time (`list_ec2.md` ≈ 10,190 lines); re-grep if the mirror refreshes.

## 1. Pentest Objectives

1. Determine whether the documented **TLS 1.2 floor** for the EC2 API is actually *enforceable by the customer* (an IAM condition key to deny weaker transport), or is only endpoint-construction prose (Lens Y). Cross-ref `data-protection` T4.
2. Determine whether an admin can **IAM-deny disabling source/destination checking** on an ENI — i.e. forbid turning an instance into a NAT/router/forwarder — or whether no dedicated condition key exists and the only lever is the known fail-open `ec2:Attribute` string class (Lens S).
3. Determine whether the **EC2 Instance Connect** path (`ec2-instance-connect:SendSSHPublicKey` / `SendSerialConsoleSSHPublicKey`) actually bounds *which instance* and *which OS user* a principal can push an SSH key to, or whether the scoping is tag-only / the `ec2:osuser` gate is weak or non-enforcing.
4. Determine whether an **EC2 Instance Connect Endpoint (EICE) `OpenTunnel`** lets a caller reach arbitrary `host:port` inside the endpoint's VPC (a private-subnet lateral-movement primitive that bypasses inbound SG rules), and whether `ec2-instance-connect:privateIpAddress` / `remotePort` actually constrain it.
5. Determine whether the AWS-published **sample IAM policies** on the EIC/EICE pages (copy-verbatim artifacts) scope least-privilege or over-grant (Lens R/S, Tier-2 reportable).
6. Determine whether an org that audits **only security-group inbound rules** has an accurate picture of who can reach its instances, given the ≥3 IAM-gated SG-bypass ingress channels this page catalogs (synthesis / Lens U).

## 2. Components, Assets, and Design

**Customer-facing interface.** The EC2 **control-plane API** (SigV4 over HTTPS), reachable from the Internet or privately via a PrivateLink **interface VPC endpoint** (`com.amazonaws.<region>.ec2`). No data-plane protocol is owned by *this* page.

**Instance-ingress channels this page catalogs** (the security-relevant inventory):
- **Security groups** (per-ENI stateful filter, enforced Nitro-side) + **network ACLs** (subnet-level stateless) — the documented "primary mechanism" + "secondary/defense-in-depth".
- **EC2 Instance Connect (EIC)** — `ec2-instance-connect:SendSSHPublicKey` pushes an **ephemeral (~60 s) SSH public key** to the instance's authorized-keys for a named OS user; actual SSH then flows over the network (still needs a path + SG). **Serial-console** variant `SendSerialConsoleSSHPublicKey` reaches the instance via the serial console (an out-of-band path independent of the VPC network).
- **EC2 Instance Connect Endpoint (EICE)** — `ec2-instance-connect:OpenTunnel` opens a WebSocket SSH tunnel to a **private-subnet** instance with **no public IP, no bastion, no inbound-from-Internet SG rule**. Resource type `instance-connect-endpoint*`.
- **SSM Session Manager** (`ssm:StartSession`) and **Run Command** (`ssm:SendCommand`) — interactive shell / command execution over the **SSM agent's outbound-443 channel**, needing **no inbound SG rule at all**. Separate service (`ssm`), separate IAM.

**Accounts / zones.** Customer account/VPC ↔ the AWS network fabric (enforces MAC/IP anti-spoof, hypervisor CPU/memory isolation, memory-scrub, block reset — the shared-responsibility line, HARD STOP). EICE introduces a small AWS-managed data path (the endpoint) inside the customer VPC.

**Enforcement points that matter here.**
- Anti-spoof / isolation / scrub → **Nitro + AWS network fabric** (not customer-reachable; HARD STOP).
- SG / NACL → Nitro-side per-ENI / per-subnet.
- EIC key push → `ec2-instance-connect` authorizer (IAM) + the instance's `ec2-instance-connect` package writing authorized-keys.
- EICE tunnel → the EICE + its own security group (`eice-security-groups.md`).
- Source/dest-check → an ENI attribute toggled by `ec2:ModifyNetworkInterfaceAttribute` / `ec2:ModifyInstanceAttribute`.

```
                         Internet / corp net
                                 │
        ┌────────────────────────┼─────────────────────────┐
        │  SG inbound (22/3389)   │   NO inbound SG rule needed │
        ▼                         ▼                            ▼
   direct SSH/RDP          EICE OpenTunnel (WSS)        SSM agent (out 443)
   (SG-gated)              → private-subnet host         StartSession / SendCommand
        │                   ec2-instance-connect:*        ssm:*  (DIFFERENT IAM svc)
        ▼                         │                            │
   ┌────────────────────── EC2 instance (ENI) ──────────────────────┐
   │  authorized-keys ← EIC SendSSHPublicKey (ephemeral, ec2:osuser) │
   │  sourceDestCheck attr (NAT/router lever; no dedicated IAM key)  │
   └── Nitro: CPU/mem isolation · mem-scrub · MAC/IP anti-spoof (HARD STOP) ─┘
```

## 3. API / Interface Inventory

| Name | Service | Mutating | Resource types | Scoping condition keys (from `list_*`) | Notes |
|---|---|---|---|---|---|
| `SendSSHPublicKey` | ec2-instance-connect | Y (push key) | `instance*` | `aws:ResourceTag`, `ec2:ResourceTag`, **`ec2:osuser`** | Ephemeral ~60 s key; OS-user named in request |
| `SendSerialConsoleSSHPublicKey` | ec2-instance-connect | Y | `instance*` | `aws:ResourceTag`, `ec2:ResourceTag` (**no `ec2:osuser`**) | Out-of-band serial-console path; serial console must be enabled account-wide |
| `OpenTunnel` | ec2-instance-connect | Y (tunnel) | `instance-connect-endpoint*` | `aws:ResourceTag`, `ec2:ResourceTag`, `ec2-instance-connect:MaxTunnelDuration`, `ec2-instance-connect:privateIpAddress`, `ec2-instance-connect:remotePort` | SG-bypass ingress to private subnet |
| `CreateInstanceConnectEndpoint` / `Delete…` / `Describe…` | ec2 | Y / Y / N | (see `list_ec2.md`) | tag/region | Endpoint lifecycle (in `list_ec2`, not `ec2-instance-connect`) |
| `ModifyNetworkInterfaceAttribute` | ec2 | Y | `network-interface*` (+instance, security-group, subnet) | `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:Subnet`, `ec2:Vpc`, `ec2:NetworkInterfaceID`, tags | **No `SourceDestCheck` key** — toggles `sourceDestCheck` attr via generic `ec2:Attribute` |
| `ModifyInstanceAttribute` | ec2 | Y | `instance*` | `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, many | Instance-level `sourceDestCheck` set |
| `ssm:StartSession` | ssm | Y (shell) | `instance`, `managed-instance`, `document`, `task` | `aws:ResourceTag`, `ssm:resourceTag`, **`ssm:SessionDocumentAccessCheck`** | SG-bypass interactive access |
| `ssm:SendCommand` | ssm | Y (exec) | `instance`, `managed-instance`, `document` | tag-based | SG-bypass command exec |
| EC2 API via interface VPC endpoint | ec2 | — | — | endpoint policy | Owned by `ec2-security-groups-privatelink` plan (xref) |

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| IAM principal w/ `ec2-instance-connect:SendSSHPublicKey` | an instance's authorized-keys for a chosen OS user | key push gated by `instance*` + `ec2:osuser` | pushing a key for `root`/`ec2-user` of an instance the principal should not administer, or for an OS user the policy meant to exclude |
| IAM principal w/ `OpenTunnel` on an EICE | arbitrary `host:port` in the endpoint's VPC | WSS tunnel | a TCP connection completing to a private IP / port the `privateIpAddress`/`remotePort` conditions were meant to forbid |
| IAM principal w/ `ssm:StartSession`/`SendCommand` | instance OS (as `ssm-user`/root) | SSM agent outbound channel | shell/command on an instance with **no inbound SG rule** permitting it → SG audit blind spot |
| IAM principal w/ `ModifyNetworkInterfaceAttribute` | ENI `sourceDestCheck=false` | generic `ec2:Attribute` toggle | turning a shared-subnet instance into a forwarder when a Deny meant to forbid it is inert (case-sensitivity / no dedicated key) |
| any customer surface | hypervisor / Nitro / AWS network fabric | — | **HARD STOP** — any reach into anti-spoof/isolation/scrub enforcement = service-plane breach, preserve & disclose |

## 5. Recommended Areas of Focus

### Area 1 — EC2 Instance Connect & EICE: IAM-gated SG-bypass ingress (HEADLINE, net-new)
This family (service prefix `ec2-instance-connect`) is the net-new surface this plan owns. Offline==online verbatim for `permissions-for-ec2-instance-connect-endpoint.md` (no drift). The unifying defect: **"which instance / which OS user / which destination" is never a *mandatory* IAM dimension — every scoping condition key is optional, so a copy-paste or minimal policy produces a broad grant that reaches instances with no inbound SG rule.** AWS docs never state the IAM evaluation default for a zero-`Condition` statement on these security-sensitive actions (reportable doc-gap).

#### Area 1a — [HIGH] `ec2:osuser` is OPTIONAL, not mandatory → `SendSSHPublicKey` can push a key as `root`/any OS user
**Mechanism.** `list_ec2-instance-connect.md` lists `ec2:osuser` as one of several *optional* condition keys for `SendSSHPublicKey` (alongside `aws:ResourceTag`, `ec2:ResourceTag`); nothing marks it required. `ec2-instance-connect-configure-IAM-role.md` phrases osuser restriction as "Consider restricting…" — advisory. Every AWS **sample** policy happens to include the osuser condition, masking that it is optional.
**Oracle.** Attach `{Allow, ec2-instance-connect:SendSSHPublicKey, Resource: instance/i-xxx}` with **no Condition**, call `SendSSHPublicKey OsUser=root`. ALLOW (not AccessDenied) confirms the key push authorizes any OS user up to root — bounded only by sshd's root-login / `AuthorizedKeysCommand` posture, not by IAM. Safe pre-check: `iam:SimulateCustomPolicy` on the no-Condition policy with `ec2:osuser=root` context absent.
**Severity-if-true.** High — "can push a key to instance X" → "root on X", contingent on OS sshd config not IAM.
**Stop condition.** Once simulate/live shows osuser is not enforced for a Condition-less grant; do not pivot to using the key for lateral movement.

#### Area 1b — [HIGH] `OpenTunnel` Resource names only the EICE, never the target instance → generic VPC TCP relay
**Mechanism.** `OpenTunnel`'s only resource type is `instance-connect-endpoint*` — **`instance*` is NOT a supported resource type**, so IAM cannot pin "which instance" at all; destination is controlled only by the *optional* `ec2-instance-connect:privateIpAddress` / `remotePort` keys. `permissions-for-ec2-instance-connect-endpoint.md`: "When this condition key is used, attempting to connect … results in failure" — implying no restriction when the key is absent. `connect-with-ec2-instance-connect-endpoint.md`: route tables can let the endpoint "connect to any instance in any subnet of the VPC."
**Oracle.** Grant `OpenTunnel` on a specific EICE ARN with no privateIpAddress/remotePort condition; `OpenTunnel` to a private IP:port that is NOT the intended target (an internal DB on 5432, another host's 22) but is reachable per route-table/SG. Success = EICE is an unscoped lateral-movement primitive gated only by target-side SG + route table, not by IAM destination. Safe pre-check: `iam:SimulateCustomPolicy` showing the grant evaluates ALLOW regardless of destination context.
**Severity-if-true.** High — the core SG-bypass claim: IAM authorizes *use of the endpoint*, not *the destination*; destination-scoping is opt-in and easily omitted.

#### Area 1c — [MED, Tier-2 reportable] AWS's own sample EICE SG rule uses VPC-CIDR source → endpoint reaches the whole VPC
**Mechanism.** `eice-security-groups.md` "Client IP preservation off" sample inbound rule literally recommends source `{{VPC IPv4 CIDR}}` "to allow connections to all instances in the VPC"; it also states endpoint ingress "is allowed regardless of the inbound rules for the endpoint security group" (EICE-Service traffic bypasses the endpoint's own inbound SG — only IAM gates inbound to the EICE). The vendor's copy-paste artifact itself widens blast radius, compounding 1b.
**Oracle.** Doc-only (Lens R): the AWS-authored example rule, applied verbatim, produces VPC-wide reachability once route tables permit — flag as an AWS-shipped weak default (Tier-2). Live confirm: build the SG from the sample, confirm any VPC instance accepts the tunneled connection regardless of caller.
**Severity-if-true.** Medium — amplifies 1b from "possible" to "the vendor's setup instructions produce it."

#### Area 1d — [MED–HIGH, Lens AA] Shared-VPC participant can self-provision an EICE and reach other participants' instances
**Mechanism.** `create-ec2-instance-connect-endpoints.md`: "You can create an EC2 Instance Connect Endpoint in a subnet shared with you. However, you can't use EC2 Instance Connect Endpoints that the VPC owner created in a subnet shared with you." → reuse of someone else's EICE is barred, but a participant's **own** EICE in the shared subnet is not barred from reaching other participants' instances (that's governed only by route tables/SGs per 1b/1c). No cross-account IAM/resource-policy gate is documented for `instance-connect-endpoint` (no resource-based policy / sharing mechanism exists).
**Oracle.** Account B (participant, not owner) creates its own EICE in the shared subnet, `OpenTunnel`s to a private IP of an Account A instance in the same VPC. Success = cross-account lateral movement via self-provisioned EICE with no explicit cross-account gate.
**Severity-if-true.** Medium–High — cross-account seam in a feature marketed as "connect without SG inbound rules." Cross-ref `using-vpc` (shared-VPC isolation) and `scenarios-enis`.
**Stop condition.** Confirm a tunnel completes to a foreign-account instance's port; do NOT authenticate into or act on that instance.

#### Area 1e — [MED, Lens O] `OpenTunnel` CloudTrail never records which OS user/account was targeted inside the tunnel; logging pages are disjoint
**Mechanism.** `log-ec2-instance-connect-endpoint-using-cloudtrail.md` `OpenTunnel` sample logs only `instanceConnectEndpointId`, `maxTunnelDuration`, `remotePort`, `privateIpAddress` — **no instance ID, no OS user, nothing about what happens inside the TCP stream**. The classic-EIC `SendSSHPublicKey` logging (`monitor-with-cloudtrail.md#ec2-instance-connect-cloudtrail`, logs instanceId + osUser + public key) lives on a *separate* page/anchor; the EICE logging page does not even show `SendSSHPublicKey` as an event. A defender triaging only the EICE page sees "who opened a tunnel to IP:port" but not "who logged in as what."
**Oracle.** Drive `OpenTunnel`+SSH through an EICE; confirm CloudTrail never correlates the tunnel to an instance ID or OS user → post-tunnel activity attribution blind spot.
**Severity-if-true.** Medium (detection/audit gap). Not an access-control bypass; weakens incident response.

#### Area 1f — [LOW–MED] `CreateInstanceConnectEndpoint` scopes by subnet/tag only — decoupled from `OpenTunnel`-destination permission
**Mechanism.** `list_ec2.md` `CreateInstanceConnectEndpoint` condition keys = `aws:RequestTag`, `aws:TagKeys`, `ec2:Region`, `ec2:SubnetID` (+SG-resource) — nothing about which instances the endpoint may later reach. "I scoped the subnet" ≠ "I scoped the instance set" (see 1b/1c).
**Oracle.** Create an EICE in a subnet with multiple unrelated services; confirm IAM offers no creation-time mechanism to pin eventual destinations — subnet is the only administrative boundary.
**Severity-if-true.** Low–Medium — reinforces that "which instance" is never a first-class IAM concept for `OpenTunnel`.

**Area-1 refuted / null (checked, not broken):**
- "SendSSHPublicKey scopable only by tag, not a specific instance ARN" → **REFUTED**: resource ARN `instance/${InstanceId}` lets admins pin specific instances (the real gap is osuser, 1a, not instance-pinning).
- "OpenTunnel / SendSSHPublicKey are unlogged" → **REFUTED** for both: each logs its own requestParameters; the gap is *granularity* (1e), not absence.
- "EICE reachable cross-account via resource policy" → no resource-based policy/sharing exists for `instance-connect-endpoint`; cross-account exposure is only the indirect shared-VPC-self-provisioning path (1d).
- **Cosmetic doc inconsistency:** `list_ec2-instance-connect.md` ops table shows `MaxTunnelDuration` (capital M) vs condition-key table `maxTunnelDuration` (lowercase) — note if writing policy JSON by copy-paste.

### Area 2 — Source/destination-check disable has no dedicated IAM condition key (Lens S)
**Background.** The page: *"you can disable source/destination checking for the network interface"* to run NAT/routing/firewall. Disabling `sourceDestCheck` turns an instance into a forwarder that can send/receive traffic for IPs other than its own assigned addresses (within the limits of the still-binding MAC/IP anti-spoof rule and the subnet route table).
**Security Concern.** An org that wants to *forbid* instances becoming routers (a lateral-movement / traffic-interception enabler) cannot express that cleanly in IAM. **Confirmed from `list_ec2.md`: there is NO `SourceDestCheck` / `sourcedest` condition key anywhere.** The only lever on `ModifyNetworkInterfaceAttribute` (network-interface* row) and `ModifyInstanceAttribute` (instance* row) is the generic **`ec2:Attribute` / `ec2:Attribute/${AttributeName}`** string key — the known **case-sensitivity fail-open class** (a Deny written against a lowercase enum is inert when the key is populated with the exact request-field casing; the attribute token is `sourceDestCheck`).
**High-level Test Scenarios.**
- Claim: a policy `Deny ec2:ModifyNetworkInterfaceAttribute if ec2:Attribute/sourceDestCheck exists` (or value-matched) fails to block the disable because of attribute-name/value casing or because the request routes through `ModifyInstanceAttribute` instead. → Oracle: `iam:SimulateCustomPolicy` with the Deny vs a request setting `sourceDestCheck=false` under each of the two actions and each casing; a simulate-ALLOW where the author expected DENY confirms the gap.
- Claim: with source/dest-check disabled on a shared-subnet instance, traffic for a *peer tenant's* IP can be intercepted. → **Likely bounded / refute-leaning:** the MAC/IP anti-spoof rule still binds the instance to its own assigned addresses, and in a shared VPC the *owner* controls route tables (a participant cannot add a route pointing peer traffic at the forwarder). Treat cross-tenant interception as REFUTED unless the hunter also controls the subnet route table; the realistic impact is **within-account** NAT/forwarder enablement. Cross-ref `scenarios-enis` (dual-homed OS-bridge) and `requester-managed-eni` (Reset→SourceDestCheck=true).
**Doc evidence.** `infrastructure-security.md` §Isolation-on-physical-hosts last two paragraphs; `list_ec2.md` ModifyNetworkInterfaceAttribute (≈8966) / ModifyInstanceAttribute (≈8806), key defs `ec2:Attribute` (10051–10052); whole-file grep `sourcedest` = 0 hits.
**Severity-if-true.** Medium (IAM-unexpressible hardening control; AWS-owned condition-key gap). Low if only the case-sensitivity variant and the dedicated-key absence are confirmed with no cross-tenant reach.
**Stop condition.** Once simulate shows whether a clean Deny is expressible; do not attempt live traffic interception across tenants (HARD STOP territory).

### Area 3 — TLS floor is endpoint-construction, not customer-enforceable (Lens Y; cross-ref data-protection T4)
**Background.** *"We require TLS 1.2 and recommend TLS 1.3"* + PFS cipher suites, for AWS-published API calls.
**Security Concern.** This is enforced by how the HTTPS endpoint is built, **not** by an IAM condition the customer can author. `data-protection` T4 already confirmed: `aws:SecureTransport` is the only applicable transport key (teethless — there is no plaintext EC2 endpoint to deny), and **no `aws:TlsVersion` / `aws:SignatureVersion` key exists**, so a customer cannot write "deny this principal unless TLS ≥1.2 / SigV4-only." A compliance control built on the doc's promise is advisory.
**High-level Test Scenarios.** Claim: no IAM/SCP condition key lets a customer *enforce* the min-TLS or signature-version floor on EC2. → Oracle: grep `list_ec2.md` + global condition keys for `TlsVersion`/`SignatureVersion` (expected absent); confirm `aws:SecureTransport` is the only lever. Claim: an interface VPC endpoint for the EC2 API has no documented min-TLS floor on the endpoint-policy side either (open doc-gap carried from the hub's Lens-Y line).
**Doc evidence.** `infrastructure-security.md` lines 10–12; cross-ref `data-protection-attack-research-plan.md` T4.
**Severity-if-true.** Low / Informational (doc-vs-enforcement; AWS-owned; matters only if a customer builds attestation/compliance on the claim).

### Area 4 — "Security groups are the primary mechanism" vs the IAM-gated SG-bypass channels on the same page (synthesis, Lens U)
**Background.** The page says *"Leverage security groups as the primary mechanism for controlling network access"* — then, in the same bullet list, recommends **EC2 Instance Connect**, **SSM Session Manager** (*"instead of opening inbound SSH or RDP ports"*), and **SSM Run Command** (*"instead of connecting to your instances"*).
**Security Concern.** Three of the page's own recommendations reach the instance **without any inbound security-group rule**: EICE `OpenTunnel`, `ssm:StartSession`, `ssm:SendCommand`. Each is gated by a **different IAM service** (`ec2-instance-connect`, `ssm`) than the EC2 SG model. **An org whose network-exposure audit inspects only SG/NACL inbound rules has a false sense of isolation** — a private, SG-locked-down instance can still be fully reachable (shell/command/root) by any principal holding the right `ssm:*` or `ec2-instance-connect:*` grant. This is the overview page's load-bearing synthesis.
**High-level Test Scenarios.**
- Claim: a principal with `ssm:StartSession` on an instance (tag-scoped) obtains an interactive shell on a host whose SG has **zero** inbound rules. → Oracle: on a canary instance with an empty inbound SG + SSM agent + instance profile, `start-session` succeeds; the SG audit shows "no ingress" while the session runs as `ssm-user`/root. Severity: the access is as-designed, but the **cross-control blind spot is the finding** — document which IAM services must be audited together with SG rules.
- Claim: `ssm:SessionDocumentAccessCheck` (Bool) and the `document` resource are the only thing standing between a broad `ssm:StartSession` grant and arbitrary-instance shell; if a policy omits the document-scoping it is instance-tag-only. → Oracle: `iam:SimulateCustomPolicy` on `StartSession` with/without `SessionDocumentAccessCheck=true`.
- Treat the full SSM authz model as **POINTER-level** (SSM is a separate service with its own authoritative plan surface); the deliverable here is the *synthesis + audit-coverage gap*, not a full SSM audit.
**Doc evidence.** `infrastructure-security.md` control-network-traffic bullets (security-groups-primary; EC2 Instance Connect; Session Manager; Run Command); `list_ssm.md` StartSession (1764–1769) / `ssm:SessionDocumentAccessCheck` (1995); `list_ec2-instance-connect.md`.
**Severity-if-true.** Medium (defense-in-depth / audit-coverage gap; the individual channels are by-design). Raises to High only if a specific channel is found to bypass an *intended* IAM scope (that lives in Area 1).

### Area 5 — Physical-host / anti-spoof / scrub guarantees (Lens U/V — characterize only, HARD STOP; owned by data-infra sibling)
**Background.** *"The hypervisor isolates CPU and memory … memory … is scrubbed (set to zero) … every block of storage is reset … the AWS network allows instances to send traffic only from the MAC and IP addresses assigned to them. Otherwise, the traffic is dropped."*
**Security Concern.** These are **AWS-infra enforcement claims** on the shared-responsibility line. They are **not customer-testable without attacking AWS's own service plane** → HARD STOP. The MAC/IP anti-spoof statement is the enforcement mechanism *behind* several customer-facing features (source/dest-check in Area 2; secondary-IP assignment; `using-instance-addressing`). Record it as the trust-boundary floor; do not probe. Any observation that this isolation leaks (reading another instance's scrubbed memory, spoofing a MAC/IP that the fabric accepts, reaching a co-resident host) is a **Critical service-plane breach → preserve evidence, stop, disclose.**
**Owned by.** `ec2-data-infrastructure-protection-attack-research-plan.md` (Nitro isolation / scrub) and `data-protection-attack-research-plan.md` (T1 inter-instance encryption). This plan only cites them.
**Severity-if-true.** Critical if ever broken — but out of normal test scope (AWS-infra).

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Push SSH key to an instance / OS user outside intended scope | `ec2-instance-connect:SendSSHPublicKey` | `instance*` resource scoping + `ec2:osuser` (Area 1) |
| Tunnel to arbitrary host:port in a private subnet | EICE `OpenTunnel` | `privateIpAddress`/`remotePort`/`MaxTunnelDuration` keys + EICE SG (Area 1) |
| Forbid instance becoming NAT/router | `ModifyNetworkInterfaceAttribute(sourceDestCheck)` | **no dedicated key; `ec2:Attribute` fail-open class** (Area 2) |
| Enforce min-TLS / SigV4 on EC2 API | EC2 control-plane | `aws:SecureTransport` only; **no `aws:TlsVersion`** (Area 3) |
| Reach SG-locked-down instance via IAM channel | SSM SM / Run Command / EICE | tag-scoped `ssm:*` / `ec2-instance-connect:*`; SG audit blind spot (Area 4) |
| Read scrubbed memory / spoof MAC-IP / co-resident reach | hypervisor / Nitro / fabric | AWS-enforced; **HARD STOP** (Area 5) |

## 7. Out-of-Scope Risk Categories

- **Hypervisor / Nitro / AWS-network-fabric enforcement** (CPU-memory isolation, memory scrub, block reset, MAC/IP anti-spoof): AWS-infra, shared-responsibility line — HARD STOP, not customer-testable.
- **Full SSM authorization model** (`ssm:*` depth beyond the SG-bypass synthesis): separate service; pointer-level only here.
- **Security-group rule authoring / PrivateLink EC2-API endpoint policy**: owned by `ec2-security-groups-privatelink-attack-research-plan.md`.
- **EBS / in-transit / in-memory encryption guarantees**: owned by `data-protection` + `ec2-data-infrastructure-protection` plans.
- **Single-tenant self-DoS**, customer-authored IAM footguns, Windows-OS/AD/JEA guest-side hardening recommendations (guest-OS configuration, out of scope).
- **DNS rebinding against private-only endpoints**, product/feature-parity gaps.

## 8. Null Hypotheses / Doc Gaps (pages checked)

- **Lens A/IDOR (classic cross-tenant resource-by-ID):** N/A on *this* page — it owns no resource-returning API. Instance/ENI IDs carry the usual EC2 structure; EICE ids are tag/ARN-scopable. Checked: the whole page + the EIC/EICE IAM rows. (EIC key-push *scoping* is a Lens-A-adjacent question handled in Area 1.)
- **Lens G/SSRF:** N/A — no field on this page or its EIC/EICE children is a URL the service dereferences server-side. Checked: `infrastructure-security.md`, `connect-linux-inst-eic.md`, EICE create/modify pages. (The EICE tunnel is a raw TCP relay, not a server-side fetch.)
- **Lens Q/upload, K/prompt-injection, F/translation, H/KMS, J/OAuth, DD/cache, FF/JWT:** N/A — no upload, LLM, parser, KMS-key input, OAuth link, cache layer, or JWT verification on this page or its children. Checked: the page + EIC/EICE family + the two SSM pointers.
- **Lens Y (TLS):** fires weakly (Area 3) — the enforceability gap is real but AWS-owned/Informational; the heavy transport analysis is already in `data-protection` T4.
- **Carried doc-gaps:**
  1. Whether the EC2-API **interface VPC endpoint** enforces (or can be made to enforce) a min-TLS floor on the endpoint-policy side — open from the hub's Lens-Y line; not resolved on this page.
  2. Whether `SendSerialConsoleSSHPublicKey` (serial-console path) is reachable independent of the VPC network and whether its lack of an `ec2:osuser` key (vs `SendSSHPublicKey` which has one) is a scoping asymmetry — flagged to Area 1.
  3. Exact enforcement of `ec2:osuser` and `ec2-instance-connect:privateIpAddress`/`remotePort` (string-match semantics, fail-open behavior) — needs the Area-1 deep analysis + a canary.
  4. Whether the `ec2:Attribute/sourceDestCheck` casing variant is DENY-effective — settle via `iam:SimulateCustomPolicy` (Area 2).

---
*Area 1 (EC2 Instance Connect / EICE) sub-leads 1a–1f above are from a dedicated deep-dive subagent (checked `list_ec2-instance-connect.md`, EIC/EICE UserGuide pages, EICE CloudTrail logging pages; online verbatim match). Area 2 (source/dest-check) and Area 4 (SSM synthesis) were analyzed directly from `list_ec2.md`/`list_ssm.md` after the planned subagent for that surface was unavailable.*
