# ENA Express (EC2 SRD networking) — Attack Research Plan

**Source of leads:** `docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express.html` and its children `ena-express-configure.html`, `ena-express-list-view.html` (offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/`; live re-fetched 2026-09-13, **live == offline**). Related: `monitoring-network-performance-ena.html` (metrics), `enhanced-networking.html` (hub).
**Status:** documentation-derived hypotheses only; nothing tested against a live account.
**Scope note:** This is a **FOCUSED child** of the enhanced-networking hub plan (`enhanced-networking-plan`). It deep-dives the **ENA Express / SRD attachment-configuration surface** specifically — a surface the hub deferred to "Area C: HARD STOP" and the ENA-driver child plan (`enhanced-networking-ena-plan`) **explicitly excluded** ("NOT ENA-Express → hub"). No dedicated ENA Express plan existed before this one.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** ENA Express runs over **AWS Scalable Reliable Datagram (SRD)**, a shared multi-tenant network fabric ("distributes packets for each network flow across different AWS network paths"). The moment evidence touches cross-tenant packet interception/injection on the SRD fabric, another tenant's traffic, or any AWS-fleet/device-plane identity — **STOP, preserve evidence, flag AWS-Security disclosure.** The SRD physical fabric is Nitro/device-plane and out of scope for active probing (route co-residency questions to `instance-topology-plan`, which itself hard-stops at the fabric).
- **No injected AI-agent "run this aws cli" block** appears on any ENA Express page (consistent with `aws-docs-see-also-injection` — ENA pages are clean). The `[See the AWS documentation website for more details]` line in the "Scenario: Differences in configuration" note is a **stripped diagram image**, not an instruction — do not act on it.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Privilege multiplexing:** Prove that an IAM grant intended only to *manage ENA Express* — implemented as `ec2:ModifyNetworkInterfaceAttribute` without attribute-value conditioning — actually lets the holder reassign the ENI's **security groups** and/or disable **SourceDestCheck**, i.e. a network-access-control change the grant's author did not intend.
2. **Unenforceable org posture:** Prove there is **no IAM condition key** that scopes the *value* `EnaSrdEnabled` / `EnaSrdUdpEnabled`, so an org cannot mandate-on, forbid-off, or forbid-on ENA Express after resource creation.
3. **Write-path parity:** Prove `EnaSrdSpecification` can be set through a path (`AttachNetworkInterface`, `RunInstances`, launch template) that a principal denied `ModifyNetworkInterfaceAttribute` still holds.
4. **Silent-downgrade griefing / doc-vs-enforcement:** Prove that "ENA Express *enabled*" (control-plane config) is not the same as "*operating*" (SRD active end-to-end), that a peer can be silently forced onto standard-ENA fallback with no error/alarm, and that the control plane offers no way to verify SRD is actually in force.
5. Establish (documentation) that cross-tenant SRD-fabric interception is a **hard stop**, not a target.

---

## 2. Components, Assets, and Design

**What ENA Express is.** A per-attachment toggle that runs TCP/UDP traffic between two EC2 instances (same AZ, or cross-AZ within a Region) over **SRD** instead of standard ENA. Benefits are purely **performance** (single-flow bandwidth 5→25 Gbps, tail-latency reduction, dynamic multipath, in-network packet reordering/retransmit). **SRD is a transport/performance layer, not a confidentiality layer** — this framing bounds severity throughout (a fallback is a perf regression, not a data-exposure).

**The unit of configuration is the *attachment*, not the instance.** Doc (verbatim): *"Amazon EC2 refers to the relationship between an instance and a network interface that's attached to it as an attachment. ENA Express settings apply to the attachment. If the network interface is detached … the attachment no longer exists, and the ENA Express settings … are no longer in force."* → the config object is `EnaSrdSpecification` living on `NetworkInterface.Attachment`. This is the key structural difference from the sibling `enaSupport` surface (which is an *instance* attribute set by `ModifyInstanceAttribute`).

**Config schema.** `EnaSrdSpecification { EnaSrdEnabled: bool, EnaSrdUdpSpecification: { EnaSrdUdpEnabled: bool } }`. UDP can only be enabled when TCP (`EnaSrdEnabled`) is enabled.

**Assets.**
- The ENI attachment config (`EnaSrdEnabled`/`EnaSrdUdpEnabled`) — availability/performance-guarantee integrity, not confidentiality.
- The **in-guest network config** the tuning script mutates (sysctl MTU, TCP output-queue limit, BQL, autocorking, TX/RX queue sizes, socket buffers, congestion control) — root-owned, in-guest.
- ENA Express **metrics** (SRD stats; driver ≥2.8) — in-guest driver counters surfaced via `monitoring-network-performance-ena`.
- The shared **SRD fabric** — AWS-owned, multi-tenant, **hard stop**.

**Identity / ownership.** Pure single-account: the ENI, the instance, and the attachment are all owned by one account. No cross-account share mechanism, no RAM, no role passed, no KMS, no external identity. Cross-tenant exposure exists *only* at the SRD fabric (hard stop).

**Untrusted-input seams.** (a) The two GitHub-hosted helper scripts fetched and run **in-guest as root** (TOFU supply chain, single-account). (b) A misconfigured/hostile *peer* instance forcing fallback (integrity/availability). No parser/translation layer, no upload, no server-side fetch on AWS identity.

```
                 Customer account (single tenant)
  ┌───────────────────────────────────────────────────────────────┐
  │  Instance i-... ── attachment ── ENI eni-...                    │
  │        (EnaSrdSpecification lives HERE, on the attachment)      │
  │   set via: AttachNetworkInterface | ModifyNetworkInterface-     │
  │            Attribute | RunInstances | LaunchTemplate | wizard   │
  │   read via: DescribeNetworkInterfaces .Attachment.EnaSrd*       │
  │   in-guest: check-ena-express-settings.sh (root sysctl/ethtool) │
  └───────────────────────────┬───────────────────────────────────┘
                              │ SRD transport (TCP/UDP), same Region
                              ▼
        ╔═══════════════ AWS SRD FABRIC (shared, multi-tenant) ═══════════════╗
        ║  dynamic multipath · packet reorder/retransmit in-network           ║
        ║  === HARD STOP: device/Nitro plane, no active cross-tenant probing ═╣
        ╚═════════════════════════════════════════════════════════════════════╝
                              ▲
                              │ fallback to standard ENA if either side unmet (SILENT)
                       Peer instance (same/other AZ, same Region)
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `AttachNetworkInterface` | SDK/CLI/PS | Existing | **Yes** | External | Attach ENI **and** set `--ena-srd-specification` in one call | Yes | Account principals w/ the action | **Write-path #1** for EnaSrd (Lens X). Also a create-time path that may skip a modify-time Deny. |
| `ModifyNetworkInterfaceAttribute` | SDK/CLI/PS | Existing | **Yes** | External | Update `--ena-srd-specification` on an existing attachment | Yes | Account principals w/ the action | ⭐ **Multiplexed setter** — same action also sets `--groups` (security groups), `--source-dest-check`, `--description`, `--attachment DeleteOnTermination` (Lens B/E/X). |
| `RunInstances` | SDK/CLI/PS | Existing | Yes | External | `NetworkInterfaces[].EnaSrdSpecification` at launch | Yes | Account principals | **Write-path #2** (Lens X); ties to `launch-templates-plan`/`launch-instances-plan`. |
| Launch template / launch wizard | Console/API | Existing | Yes | External | Advanced network config sets EnaSrd at launch | Yes | Account principals | `$Latest`/`$Default` late-binding → route to `launch-templates-plan`. |
| `DescribeNetworkInterfaces` | SDK/CLI/PS | Existing | No | External | Read `.Attachment.EnaSrdSpecification.{EnaSrdEnabled,EnaSrdUdpSpecification.EnaSrdUdpEnabled}` | Yes | Account principals | Reports **configured** state only — NOT whether SRD is *operating* (Lens U). |
| `check-ena-express-settings.sh` | in-guest shell | Existing | Yes (in-guest) | N/A (GitHub fetch) | Validates & **prints exact fix commands** for MTU/BQL/queues/buffers/congestion | N/A | root in-guest | `amzn/amzn-ec2-ena-utilities`; TOFU, no sig verify (Lens G/supply-chain, single-account). |

**Console-hidden / reference-only knobs to enumerate at hunt time:** confirm whether `ModifyNetworkInterfaceAttribute`'s `EnaSrdSpecification` is represented by any IAM `ec2:Attribute` value or a dedicated condition key (Service Authorization Reference is JS-rendered — **doc-gap, resolve at hunt time**, see Area 2). Check whether UDP-enable is silently accepted when TCP is disabled (schema says it shouldn't be).

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv IAM principal ("manage ENA Express") | ENI security groups / SourceDestCheck | Shared `ec2:ModifyNetworkInterfaceAttribute` action | Holder reassigns SG or disables SourceDestCheck on the ENI using only the ENA-Express-intended grant = **breach** (Area 1). |
| Org/SCP author | Post-creation EnaSrd value on any ENI | Absence of a value-level condition key | A `Deny` cannot be written that forbids `EnaSrdEnabled=true`/`false` by value → org posture unenforceable = **gap** (Area 2). |
| Principal denied `ModifyNetworkInterfaceAttribute` | EnaSrd config | `AttachNetworkInterface` / `RunInstances` / LT | Setting EnaSrd via an alternate write path the modify-Deny doesn't cover = **parity breach** (Area 3). |
| Low-priv peer / misconfig actor | A victim instance's SRD performance guarantee | Flip one side's `EnaSrdEnabled=false` | Peer silently falls back to standard ENA, no error/alarm; victim loses 25 Gbps single-flow guarantee = **integrity/availability griefing** (Area 4, single-account). |
| Any customer instance | Another tenant's traffic on SRD fabric | SRD multipath shared fabric | **HARD STOP** — any packet of another tenant observed/injected = device-plane breach, disclose. |
| In-guest root | GitHub-fetched tuning script | curl+run, no hash pin | MITM/compromised fetch → attacker-chosen root commands in-guest = supply-chain (Area 5, single-account, TOFU). |

---

## 5. Recommended Areas of Focus

### Area 1 — ⭐ `ModifyNetworkInterfaceAttribute` multiplexes ENA-Express with security-group & SourceDestCheck control (Lens B / E / X)
**Background.** ENA Express is configured on an existing attachment with `aws ec2 modify-network-interface-attribute --ena-srd-specification …`. The **same** action `ec2:ModifyNetworkInterfaceAttribute` also sets `--groups` (the ENI's security groups), `--source-dest-check`, `--description`, and the attachment's `DeleteOnTermination`. This is the ENI analogue of the confirmed `ec2:ModifyInstanceAttribute(userData)` → root privesc exemplar (`stop-start-plan`, `launch-instances-plan`, `enhanced-networking-ena-plan` Area A).
**Security Concern.** An operator who writes an IAM policy granting `ec2:ModifyNetworkInterfaceAttribute` to let a team "turn on ENA Express" has, absent a per-attribute condition key, also granted **security-group reassignment** (moving an ENI into a permissive SG = firewall bypass) and **SourceDestCheck disable** (enabling the instance to act as a NAT/router / spoof source IPs — see `using-eni-plan`, which flags SourceDestCheck as having no value-level key).
**High-level Test Scenarios (falsifiable):**
- **Claim:** A principal holding only `ec2:ModifyNetworkInterfaceAttribute` (Resource scoped to one `eni-*`) can call the same action with `--groups sg-<permissive>` and succeed. → **Oracle:** `DescribeNetworkInterfaces` shows the ENI's `Groups` changed under the scoped role; simulate first with `iam:SimulatePrincipalPolicy`. → **Severity:** intra-account SG-bypass / lateral = **Medium–High** (customer footgun *unless* it appears in an AWS-authored sample policy — see Area 6).
- **Claim:** The same grant lets the holder set `--source-dest-check false`, enabling IP spoofing / traffic interception within the VPC. → **Oracle:** attribute flips under the scoped role.
- **Variant (Lens X/S case-fail-open):** if any `ec2:Attribute` condition key *is* accepted for this action, test PascalCase-vs-lowercase enum fail-open (`ec2:Attribute` case-sensitivity fail-open is a confirmed corpus shape — `stop-start-plan`, `terminating-instances-plan`).
**Doc evidence:** `ena-express-configure.html` CLI section (`modify-network-interface-attribute --ena-srd-specification`); AWS CLI reference for the same command's other flags. **Severity-if-true:** Medium–High.

### Area 2 — ⭐ No value-level IAM condition key for `EnaSrdEnabled` / `EnaSrdUdpEnabled` → unenforceable org posture (Lens S / U)
**Background.** `EnaSrdSpecification` is a boolean config on the attachment. Same systemic class as `network-bandwidth-plan`, `burstable-unlimited-mode-plan`, `instance-optimize-cpu-plan`, and the enhanced-networking hub Area B: EC2 exposes only coarse (action + resource-ARN, maybe `ec2:Attribute` *name*) keys, no *value* key.
**Security Concern.** An org that wants to **mandate ENA Express on** (for a perf/SLA guarantee), or **forbid UDP-over-SRD**, or **prevent a downgrade to fallback**, has no SCP/IAM lever keyed on the EnaSrd value. Any principal with the action toggles it freely; the control plane cannot express "must stay enabled."
**High-level Test Scenarios:**
- **Claim:** There is no `ec2:` condition key (`ec2:EnaSrdEnabled`, `ec2:EnaSrdUdpEnabled`, or an `ec2:Attribute` value covering EnaSrd) usable in a `Deny` to forbid setting the value on `Modify`/`Attach`/`RunInstances`. → **Oracle:** resolve the **EC2 Service Authorization Reference** action rows for `ModifyNetworkInterfaceAttribute`, `AttachNetworkInterface`, `RunInstances`; enumerate condition keys; a `Deny` on the value fails to write or fails to bind. **This is the systemic anchor — resolve the JS-rendered ref at hunt time** (`aws iam` docs / `awscli` `list_amazonec2` fetch failed via WebFetch: doc-gap).
- **Variant (Lens S non-existent key):** confirm whether a plausibly-named key (`ec2:InterfaceType`-style) is *silently ignored* rather than enforced (confirmed corpus shape: a key that doesn't exist can't deny).
**Doc evidence:** `ena-express-configure.html` (only resource-level examples, no condition-key guidance anywhere on the ENA Express pages). **Severity-if-true:** Low–Medium (posture/hardening gap; **AWS-owned** limitation, worth filing as a Lens U/S enforcement gap, not a customer footgun).

### Area 3 — Write-path parity: EnaSrd settable via Attach / RunInstances / launch template, bypassing a modify-time Deny (Lens X)
**Background.** `EnaSrdSpecification` can be set at **five** points: `ModifyNetworkInterfaceAttribute`, `AttachNetworkInterface`, `RunInstances`, launch template, launch wizard.
**Security Concern.** A guardrail written only against `ModifyNetworkInterfaceAttribute` (the "obvious" path) does not cover a principal who instead **attaches a new ENI with `--ena-srd-specification`** or **launches with it in the NetworkInterfaces block**. Same write-path-parity class as `enhanced-networking-ena-plan` Area D (enaSupport via RegisterImage/AMI-inheritance vs ModifyInstanceAttribute).
**High-level Test Scenarios:**
- **Claim:** A principal explicitly denied `ModifyNetworkInterfaceAttribute` can still achieve `EnaSrdEnabled=true` via `AttachNetworkInterface --ena-srd-specification` (or via a launch template `$Latest` late-binding). → **Oracle:** EnaSrd set under the scoped role via the alternate path where the primary is denied.
- **Chain:** ties to `launch-templates-plan` / `ec2-fleet-config-plan` `$Latest`/`$Default` late-binding — a template edit changes EnaSrd for a whole fleet.
**Doc evidence:** `ena-express-configure.html` "Configure ENA Express at launch" + AttachNetworkInterface examples. **Severity-if-true:** Low–Medium.

### Area 4 — Silent fallback + "enabled ≠ operating" (Lens U / O; single-account griefing)
**Background.** Doc (verbatim): *"If ENA Express is not operating, the communication falls back to standard ENA transmission"* and *"If there are differences in the configuration, you can run into situations where traffic defaults to standard ENA transmission"* and *"If any requirement is unmet, the instances use the standard TCP/UDP protocol but without SRD."* No error, no alarm; metrics require in-guest **driver ≥2.8**.
**Security Concern.** (a) **Integrity/availability griefing (single-account):** a low-priv actor who can flip *one* peer's `EnaSrdEnabled=false` (or its UDP flag) silently strips the SRD path for the pair — the victim keeps believing it has a 25 Gbps single-flow guarantee. (b) **Doc-vs-enforcement:** `DescribeNetworkInterfaces` reports the *configured* flag, **not** whether SRD is actually operating end-to-end — a compliance/attestation control built on "ENA Express is on" is unverifiable from the control plane. (c) **Audit/monitoring blind spot:** the downgrade is observable only via in-guest driver SRD counters (route to `monitoring-network-performance-ena`), and microburst-scale degradation may not surface in CloudWatch (enhanced-networking hub Area E enabler).
**High-level Test Scenarios:**
- **Claim:** Flipping the receiver's `EnaSrdUdpEnabled` to `false` silently downgrades the sender's UDP flow to standard ENA with no control-plane signal on the sender side. → **Oracle:** sender's SRD UDP counters drop to zero while `DescribeNetworkInterfaces` on the sender still shows `EnaSrdEnabled/UdpEnabled=true`.
- **Claim:** No control-plane API returns "SRD operating = true/false" for a flow. → **Oracle:** exhaustively check Describe* output fields.
**Doc evidence:** `ena-express.html` "How ENA Express works" + benefits note. **Severity-if-true:** Low (single-account integrity/availability + doc-vs-API; **not** cross-tenant). SRD is performance-only, so no confidentiality loss on fallback.

### Area 5 — In-guest tuning-script supply chain (Lens G / TOFU; single-account, in-guest)
**Background.** `ena-express.html` instructs: *"download and run the ENA Express settings check script"* from `github.com/amzn/amzn-ec2-ena-utilities/.../check-ena-express-settings.sh`, which *"outputs the exact commands to fix any issues"* (root sysctl/ethtool/queue changes), plus a clone of `amzn/amzn-drivers` for best practices.
**Security Concern.** Fetched over the network with **no pinned hash / no signature verification** (TOFU). A compromised/MITM'd fetch yields attacker-chosen root commands run in-guest. This is **in-guest, on the customer's own instance identity — NOT AWS fleet identity** → *not* service-plane SSRF; it is an AWS-published insecure runbook (same class as `enhanced-networking-ena-plan` Area F, `configure-gpu-instances-plan` gpgcheck=0).
**High-level Test Scenarios:**
- **Claim:** The doc/script provides no integrity check (checksum/signature) before executing fetched fix commands as root. → **Oracle:** read the script + doc; confirm no `sha256`/GPG step. → **Severity:** Low (single-account, in-guest, requires network-position or repo compromise).
**Doc evidence:** `ena-express.html` "Tune performance for ENA Express settings on Linux instances." **Severity-if-true:** Low.

### Area 6 — (conditional) AWS-authored IAM artifact audit (Lens R / S)
**Background.** The ENA Express pages themselves print **no** IAM policy JSON, managed policy, CFN snippet, or SLR.
**Move.** If, at hunt time, any AWS-*managed* policy or AWS-*published sample* policy grants `ec2:ModifyNetworkInterfaceAttribute` on `Resource:"*"` (or `network-interface/*`) unconditioned, it inherits Area 1's SG/SourceDestCheck-reassignment reach and becomes **in-scope, reportable Tier-2** (uneditable/copy-verbatim AWS defect), not a customer footgun. Resolve any such policy with `iam:GetPolicyVersion` and audit statement-by-statement.
**Severity-if-true:** non-admin→lateral via SG reassignment = Medium–High **iff** the artifact is AWS-authored.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| ENA-Express grant → SG/SourceDestCheck reassignment | `ModifyNetworkInterfaceAttribute` | (none printed) — action-level authz only; **attack the absence of per-attribute conditioning** |
| Org cannot forbid/mandate EnaSrd value | IAM condition keys for EnaSrd | (none) — attack the missing value-level key |
| Modify-Deny bypassed via Attach/RunInstances/LT | multi write-path | (none) — attack write-path parity |
| Silent fallback strips SRD guarantee | SRD operating vs configured | fallback is by-design; **attack the lack of a control-plane "operating" signal + no alarm** |
| Root command injection via tuning script | in-guest script fetch | (none) — attack TOFU / no signature |
| Cross-tenant SRD packet observation | SRD fabric | AWS-owned isolation — **HARD STOP, do not probe; disclose if observed** |

---

## 7. Out-of-Scope Risk Categories
- **SRD physical/device fabric & cross-tenant packet interception** — Nitro/device plane, AWS-owned. Hard stop; co-residency questions route to `instance-topology-plan` (which also hard-stops).
- **Single-tenant self-DoS / performance regression** from misconfig (fallback is perf-only, not confidentiality).
- **In-guest kernel/driver tuning** as a customer responsibility (sysctl/ethtool) — except the AWS-published no-integrity fetch runbook (Area 5, Low).
- **IMDS / instance-internal** on managed vantage.
- **Third-party repo bugs** in `amzn-drivers` / `amzn-ec2-ena-utilities` source itself.
- Customer-authored IAM policies granting the multiplexed action (footgun) — **in scope only if AWS-authored** (Area 6).

---

## 8. Null hypotheses / doc-gaps (pages checked)
Pages read: `ena-express.html`, `ena-express-configure.html`, `ena-express-list-view.html` (offline + live), and the surrounding hub/metrics references.
- **Lens A (IDOR):** null — all ids (`eni-*`, `i-*`) are ownership-bound; no shared service account, no resource-by-id cross-tenant path. No disclosure-timing/sub-resource shape.
- **Lens B PassRole / C credential-vending:** null — no role ARN passed, no STS, no credential vending anywhere in the ENA Express flow.
- **Lens G SSRF (server-side fetch on AWS identity):** null — the only fetch is the in-guest git/script download run on the *customer's* instance identity, not AWS fleet identity (→ Area 5 supply-chain instead).
- **Lens H KMS / W attestation / Y TLS-SigV2:** null — no KMS, no attestation, no service endpoint of its own (inherits generic EC2 API transport).
- **Lens K prompt-injection / F translation-layer / Q upload:** null — no LLM, no parser/translation layer, no upload (scripts are downloads).
- **Lens P registration/OTP / J OAuth / M session-id:** null — none present.
- **Lens AA share/revoke:** null — ENA Express config is single-account on an attachment; not RAM-shareable, no cross-account grant.
- **Lens N namespace-migration / I tagging:** null — no dual namespace, no ENA-Express-specific tagging.
- **Lens R (printed IAM artifact):** null on these pages (none printed) → conditional Area 6 at hunt time.
- **DOC-GAP (resolve at hunt time):** the exact IAM **condition-key set** for `ModifyNetworkInterfaceAttribute` / `AttachNetworkInterface` / `RunInstances` re: `EnaSrdSpecification` — the Service Authorization Reference (`list_amazonec2.html`) is JS-rendered and did not return table content via WebFetch. Area 2 and Area 1's case-fail-open variant both hinge on resolving this (use the raw HTML/API model or `aws iam` tooling at hunt time).

---
*Prepared under the security-questionbuilder skill. Documentation-only; no live testing performed. ENA Express = SRD, a shared AWS fabric — cross-tenant fabric probing is a HARD STOP.*
