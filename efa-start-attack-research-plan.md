# EFA (Elastic Fabric Adapter) "Get started with EFA and MPI" — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start.html` (offline twin `efa-start.md`, byte-identical to online 2026-10-15) and its documentation neighborhood — `efa.md` (overview/basics/limits/instance-types/OS), `create-efa.md`, `detach-efa.md`, `efa-verify.md`, `efa-installer-containers.md`, `efa-changelog.md`, `efa-working-monitor.md`, `efa-acc-inst-types.md`, sibling walkthroughs `efa-start-nccl.md` / `efa-start-nixl.md`, plus `cr-cpg.md`, `placement-groups.md`, `security-group-connection-tracking.md`, `ena-nitro-perf.md`, `ec2-security-groups.md`, VPC `security-group-sharing.html` / `vpc-sharing.html`, and the authoritative IAM reference `service-authorization/.../list_ec2.md`.
Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> This plan belongs to the EC2-UserGuide `security-questionbuilder` corpus. It is the **EFA getting-started/enablement** page; it is a *tutorial* page (console/CLI steps + copy-verbatim shell), so the highest-yield surface is **AWS-authored copy-verbatim artifacts** (insecure sample SG, insecure passwordless-SSH config, optional-by-default supply-chain verification) and the **one structural IAM-expressiveness ceiling** (EFA/OS-bypass has no IAM condition key). The deeper, highest-severity-if-true surface is the **EFA/SRD OS-bypass fabric isolation model**, which the docs leave as a deliberate gap. Cross-references the ENA/SRD cluster (`ena-nitro-perf`, `ena-express`, `enhanced-networking-ena`) and the ENI cluster (`create-network-interface`, `modify-network-interface-attributes`, `network-interface-attachments`).

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (§5 is ordered); look left and right for adjacent bugs.
- **HARD STOP:** the instant any evidence shows an identity/credential/ARN/account/host belonging to AWS's **own service plane** (Nitro card internals, the EFA device firmware, the `efa-installer.amazonaws.com` origin, another AWS fleet), stop, preserve evidence, and flag for AWS-Security disclosure. Do **not** attempt RDMA against anything you cannot prove you own on both ends.
- `iam:SimulateCustomPolicy` / `SimulatePrincipalPolicy` is the safe first oracle for every IAM lead (no resources touched). Live confirmation only with synthetic canary instances **you own on both ends**, inside one VPC/AZ you control, torn down after.
- **`DryRunOperation` is caller-IAM-only — NOT an ownership/isolation oracle** (evaluated before resource resolution). Several leads below note this trap.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. **Cross-tenant RDMA/memory read-write (the prize).** Complete an SRD/RDMA read or write (or GPUDirect RDMA direct GPU-memory access) to an instance owned by a **different, non-consenting** AWS account — proving the EFA OS-bypass path reaches memory the SG/VPC/AZ model says is unreachable. **Critical.**
2. **OS-bypass firewall bypass.** Show that the mandatory self-referencing security group is *not* actually the enforcement point for EFA/SRD packets — i.e. that revoking it (or never being in it) does not stop RDMA — demonstrating "OS-bypass" bypasses AWS's own firewall, not just the guest kernel. **High–Critical.**
3. **IAM-expressiveness ceiling.** Confirm no customer-authored IAM policy can allow ordinary ENI operations while denying EFA/OS-bypass ones (no `ec2:InterfaceType` key). Scope: AWS-owned structural gap. **Informational→Medium (enabler).**
4. **Root RCE via the AWS-authored install runbook.** Show the default copy-verbatim install path (`curl … | sudo ./efa_installer.sh -y`) has only single-origin TLS protecting a root-executed, kernel-module-inserting installer, because every integrity check is optional/off-by-default. **High (AWS-authored artifact).**
5. **Credential/key compromise from AWS-authored sample configs** — the insecure SG (SSH `0.0.0.0/0`), the passwordless-SSH config (`StrictHostKeyChecking no` + `ForwardAgent yes` for `Host *` + no-passphrase key), and secrets baked into a shared EFA AMI. **Medium–High.**
6. **Live-session revocation completeness.** Show that unsharing/revoking the EFA SG does not sever an in-flight RDMA/SRD session (admission-check-once vs per-packet). **High if confirmed.**

---

## 2. Components, Assets, and Design

**What EFA is.** A network *device* (not a standalone service) attached to an EC2 instance by setting `InterfaceType=efa` (EFA-with-ENA) or `efa-only` on an elastic network interface. It provides **OS-bypass** transport via the **Scalable Reliable Datagram (SRD)** protocol: the Libfabric user-space API talks **directly to the EFA Nitro device**, bypassing the guest kernel TCP/IP stack, enabling **RDMA read/write** and **GPUDirect RDMA/Async (GDR/GDA)** between instances in a cluster. Backed by Nitro v4+/EFA v2+ (capability tiers versioned to Nitro generation).

**Customer-facing interfaces.**
- EC2 control-plane APIs (SigV4 IAM): `CreateNetworkInterface` / `RunInstances` / `AttachNetworkInterface` with `InterfaceType=efa|efa-only`; `ModifyNetworkInterfaceAttribute` (swap SG to enable OS-bypass); `DetachNetworkInterface`/`DeleteNetworkInterface`; launch templates; console "Advanced network configuration" (Network card index / Device index / Interface type).
- Data plane: the EFA device itself (libfabric `fi_info -p efa -t FI_EP_RDM`, provider `efa`, SRD on the wire). No TCP/UDP ports — EFA traffic is **not routable**, **cannot cross AZ or VPC**, and appears in VPC Flow Logs by **MAC address** with blank port/protocol fields.
- Guest-OS install surface: tarball from `efa-installer.amazonaws.com`, GPG key/sig from same origin, root-run `efa_installer.sh`, out-of-tree kernel modules (`efa`, `efa-nv-peermem`), libfabric + Open MPI 4.1/5 (`/opt/amazon/…`) and/or Intel MPI.

**Accounts / VPCs / ownership.**
- Customer account owns the ENIs, instances, SG, VPC, subnet, placement group, AMI.
- **Cross-account EFA fabric is a shipped, consent-based feature**: VPC subnet sharing + **Shared Security Groups** (same AWS Organization, RAM-mediated) + shared placement groups let a *different* account become a member of the same EFA SG. No uninvited-tenant path is documented.
- Nitro card = AWS service plane (hard stop). The EFA device/firmware and SRD fabric substrate are AWS-owned.

**Resource identifiers.** ENI `eni-…`, SG `sg-…`, subnet `subnet-…`, instance `i-…`, AMI `ami-…`, placement group by name. EFA has **no dedicated resource type or ARN** — it is purely a parameter *value*.

**Identity establishment.** SigV4/IAM for the control plane. On the data plane, RDMA peer admission is gated by **SG membership** (self-referencing all-traffic rule), not by any per-tenant cryptographic identity. Memory scoping = libfabric/driver memory-region (MR) registration + queue-pair (QP) rkeys (application layer).

**Untrusted-data entry / transform seams.** (a) The downloaded installer tarball + kernel modules → root/ring-0 (supply chain). (b) RDMA memory-registration handles (rkeys/QPs) → remote peer memory (the C/driver/libfabric parsing layer). (c) Copy-verbatim shell/config the user pastes as root.

```
                 ┌───────────────── Customer account / VPC / AZ ─────────────────┐
 EC2 control ───▶│ CreateNetworkInterface(InterfaceType=efa) / RunInstances /     │
 plane (SigV4)   │ ModifyNetworkInterfaceAttribute(swap SG)                        │
                 │        │                                                        │
                 │        ▼                                                        │
                 │   ENI (efa / efa-only) ── member of ──▶ self-ref "allow-all" SG │
                 │        │                                   ▲ (shared cross-acct │
                 │        │ libfabric (OS-BYPASS)             │  via RAM, same Org) │
   guest kernel  │        ▼                                   │                    │
   TCP/IP  ─X──▶ │   EFA device ══ SRD / RDMA r/w / GDR ══▶ peer EFA device         │
   (bypassed)    │        ║  (enforcement point: Nitro card? — DOC-GAP)            │
                 └────────╫────────────────────────────────────────────────────────┘
                          ▼
                 [AWS service plane: Nitro card / EFA firmware / SRD fabric] = HARD STOP
   install:  curl https://efa-installer.amazonaws.com/…tar.gz  →  sudo ./efa_installer.sh -y
             (TLS-only default; GPG + --check-signatures both OPTIONAL/off) → root + kmod insert
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `CreateNetworkInterface` | SigV4 | Existing | Yes | External | Create ENI; `InterfaceType=efa\|efa-only` enables EFA/OS-bypass | Yes | IAM principals w/ action | **No `ec2:InterfaceType` key** — cannot deny EFA vs normal (§5.A) |
| `RunInstances` (`--network-interfaces … InterfaceType=efa`) | SigV4 | Existing | Yes | External | Launch instance + inline EFA ENI | Yes | IAM principals | Same key gap; launch-template path identical |
| `AttachNetworkInterface` | SigV4 | Existing | Yes | External | Attach existing EFA ENI (stopped instance only) | Yes | IAM principals | No interface-type key |
| `ModifyNetworkInterfaceAttribute` | SigV4 | Existing | Yes | External | Swap SG on an EFA ENI to enable OS-bypass | Yes | IAM principals | `ec2:Attribute`/`ec2:SecurityGroupID` scopable, but EFA-blind |
| `DetachNetworkInterface` / `DeleteNetworkInterface` | SigV4 | Existing | Yes | External | Teardown (stop instance first) | Yes | IAM principals | Residual MR/QP state doc-gap (§5.F) |
| console Launch wizard (Advanced network config) | HTTPS | Existing | Yes | External | Network card index / Device index / Interface type = EFA | Yes | Console users | Must select subnet or EFA cannot be enabled |
| libfabric EFA provider (`fi_info -p efa`) | data plane | Existing | — | Data | SRD / RDMA r/w / GDR between peers | No (not routable, intra-VPC/AZ) | SG members | **No TCP/UDP; MAC-identified; the actual breach surface** |
| `efa-installer.amazonaws.com` tarball + GPG | HTTPS | Existing | — | External (download) | Install EFA sw + kernel modules as root | Yes (download) | anyone | Single-origin TLS = only default control (§5.D) |

Doc-flagged "testing should focus on" / verbatim leads kept as pointers: *"This security group is intended for testing purposes only"* (SG step); *"self-referencing … rules are mandatory for EFA to function. Without these rules, EFA traffic between instances will be blocked"* (availability claim, not a security claim — §5.B); *"Consider requiring the use of IMDSv2 … unless you have already set IMDSv2 as the default"* (optional hardening — §5.E).

**Undocumented/under-surfaced knob:** `efa` vs `efa-only` InterfaceType values and multi-card EFA (`NetworkCardIndex` N) are accepted by the API but have **no IAM condition key** gating them — the OS-bypass-enabling property is invisible to the policy evaluator.

---

## 4. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Customer A instance (EFA peer) | Customer B instance memory (another tenant) | SRD/RDMA r/w over EFA fabric | **An RDMA read/write completes to an instance owned by a non-consenting account → Critical breach.** |
| EFA ENI in self-ref SG | Any other member of that SG | SG "allow all to/from itself" | Any member reaching any member = *intended within one owner's cluster* (OOS); reaching a member the attacker was never shared into = breach. |
| libfabric/driver (guest) | Nitro-enforced firewall for EFA path | OS-bypass | A packet reaching a peer **after** the SG rule is revoked / without SG membership → firewall-bypass breach. |
| libfabric MR/rkey (app layer) | Remote peer address space | RDMA memory registration | Reading/writing a memory region the remote never granted → scoping breach (driver memory-safety bug class). |
| Guest root (install) | Kernel ring-0 + AWS install origin | `sudo ./efa_installer.sh` + kmod | A tampered tarball/origin yielding code exec as root/ring-0 → supply-chain breach (AWS-authored runbook). |
| SSH leader node | SSH agent / member nodes | `ForwardAgent yes` (`Host *`) + `StrictHostKeyChecking no` | A compromised member node hijacking the forwarded agent to reach the operator's *other* hosts → lateral movement enabled by AWS sample config. |
| Any customer surface | **Nitro card / EFA firmware / SRD fabric** | OS-bypass data path | Any identity/host of AWS's own fleet = **HARD STOP, disclosure**. |

---

## 5. Recommended Areas of Focus (priority order)

### Area A — EFA/OS-bypass has NO IAM condition key (`ec2:InterfaceType` does not exist) — Lens S/X/R  [HIGHEST-CONFIDENCE, AWS-OWNED]
**Background.** EFA is attached purely as the `InterfaceType=efa|efa-only` *value* on generic `CreateNetworkInterface`/`RunInstances`/`AttachNetworkInterface`. There is **no dedicated EFA IAM action, resource type, or ARN** — EFA has zero independent authorization grain.
**Security Concern.** `grep -ni "InterfaceType"` over the entire 10,190-line `list_ec2.md` returns **zero** matches; every `efa` hit is the substring inside "**Defa**ult". So an admin **cannot** write a policy that allows ordinary ENI create/attach while denying EFA/OS-bypass ENI create/attach (or the reverse). This is the confirmed instance of the skill's own variant note ("`ec2:InterfaceType` is not a real IAM key → cannot deny by it"). The property that *defines* EFA (OS-bypass, RDMA capability) is invisible to IAM.
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** A policy denying `ec2:CreateNetworkInterface` only when `InterfaceType=efa` is impossible to express. → **Oracle:** `iam:SimulateCustomPolicy` with a `Condition` on any guessed key (`ec2:InterfaceType`, `ec2:NetworkInterfaceType`) is silently ignored (the Deny never fires); the EFA create succeeds under a policy intended to block it. → No resource created.
- **Claim:** The only EFA-adjacent controls are one layer removed. → **Oracle:** confirm `ec2:Subnet`/`ec2:Vpc`/`ec2:SecurityGroupID` (defs at list_ec2 L10162/10172/10152) *can* pin where/which-SG an ENI lives, but identically for EFA and non-EFA — so a principal scoped to an allowed SG can swap it onto an EFA ENI just as freely (`ModifyNetworkInterfaceAttribute`, L8969 `security-group` row).
- **Lens X parity:** CreateNetworkInterface (L5359) vs RunInstances inline NIC (L9595) — both silent on InterfaceType; only incidental keys differ (`ec2:AssociatePublicIpAddress`, `ec2:AuthorizedService` on RunInstances). No EFA-relevant asymmetry.
**Doc evidence.** list_ec2.md whole-file grep; detailed rows L5359-5361 (CreateNetworkInterface), L9595/9599 (RunInstances), L4861 (AttachNetworkInterface), L8969-8970 (ModifyNetworkInterfaceAttribute). **Severity-if-true:** Informational→Medium — a structural IAM-expressiveness ceiling, AWS-owned; the enabler for Areas B/C (you cannot IAM-prevent a workload from going OS-bypass). Reportable as an AWS gap, not a customer footgun.

### Area B — EFA/SRD OS-bypass fabric isolation: where is the firewall actually enforced? — Lens V/D/U  [HIGHEST SEVERITY-IF-TRUE; DOC-GAP]
**Background.** The docs state the self-referencing SG is "**mandatory for EFA to function**" and that EFA traffic "can't cross AZ or VPC" and "is not routable." They **never** state *where* SG filtering of EFA/SRD packets is enforced for the EFA device path.
**Security Concern.** "OS-bypass" bypasses the **guest kernel TCP/IP stack** — the docs never claim it bypasses AWS's own enforcement. For the sibling ENA/IP path, AWS documents enforcement on the physically-separate **Nitro card** (`ena-nitro-perf.md:12,17,32`: "the Nitro card evaluates the packet against stateful firewall rules and access control lists"), and EFA capability tiers are versioned to Nitro generations — *suggestive* that EFA enforcement rides the same Nitro substrate, but **not proven**. If EFA enforcement is instead a one-time admission check at QP/address-handle setup (or guest-side only), then OS-bypass literally bypasses the firewall.
**High-level Test Scenarios:**
- **Claim:** The SG self-reference is an *availability* control, not an *isolation* control. → **Oracle:** doc-trace — AWS phrases it as "works/won't function," never "isolates your cluster from others" (`efa-start.md`, repeated verbatim in nccl/nixl siblings). Flag the inference gap; do not assert isolation on AWS's behalf.
- **Claim (the pairing that settles the whole plan):** Revoking the self-ref SG rule does **not** sever a live RDMA/SRD session. → **Oracle:** on two canary instances **you own**, establish an RDMA connection, then revoke the self-referencing SG rule and observe whether in-flight RDMA read/write still completes. Per-packet Nitro enforcement → traffic stops; one-time admission check → it continues. → **Severity: High** if revoke does not sever (gap between "revoked" and "actually gone").
- **Claim:** EFA enforcement is guest-side, not Nitro. → **Oracle:** side-channel/timing of an SG-denied RDMA attempt, or an attempt from an instance never admitted to the SG. **If any evidence points at Nitro-card internals or EFA firmware → HARD STOP, disclosure.**
**Doc evidence.** `efa.md` limitations; `efa-start.md` SG step; `ena-nitro-perf.md:12,17,32`; `efa-working-monitor.md:194-198` (EFA flows in VPC Flow Logs are MAC-identified, blank port/protocol). **Severity-if-true:** Medium–High if guest-side-only; Informational if Nitro-enforced (expected/benign). **Stop condition:** the moment enforcement is proven Nitro-side, close as benign; the moment you observe anything in AWS's fleet, stop and disclose.

### Area C — Cross-tenant RDMA memory reach (the prize + its two realistic paths) — Lens A/V  [CRITICAL IF TRUE; DOC-GAP]
**Background.** EFA exposes instance memory (and GPU memory via GDR) to the fabric. The documented confinement is only **VPC + AZ + SG membership**; account/tenant is *not* a documented boundary dimension. Memory scoping (which regions a remote peer may r/w) is a **libfabric/driver** MR-registration + QP-rkey construct (application layer) — the changelog proves these live in guest software (v1.48.0: "use-after-free in … MR logging", "race conditions in … QP locking", "verify QP number on CQE"; v1.44.0 "bind QPs and CQs to thread domains").
**Security Concern.** Two distinct breach shapes:
- **(C1) Uninvited cross-account RDMA** — the Critical prize. Confinement (same VPC + same AZ + shared SG) should make this unreachable by design. Any RDMA r/w completing between two **non-consenting** accounts is a platform-boundary finding.
- **(C2) Over-shared / compromised-participant lateral movement** — the *realistic* story. **Shared Security Groups** (same AWS Org, RAM-mediated) + shared subnets + shared placement groups are a shipped feature that puts a different account into the same self-ref "allow-all" EFA SG. Then one compromised participant has **direct RDMA memory access to every other member**, with no additional network-layer control between them (the SG is "allow all").
- **(C3) Nitro QP→ENI binding doc-gap** — if there is *no* hardware binding of queue-pairs to the owning ENI, a libfabric/driver memory-safety bug (the exact use-after-free / uninitialized-descriptor / QP-race classes in the changelog) on one cluster member is a **direct path into another member's address space**, not merely an app-level flaw.
**High-level Test Scenarios:**
- **Claim C1:** an RDMA read completes to an instance in a different, never-shared account. → **Oracle:** two accounts you control, *no* VPC/SG/placement-group share between them; attempt RDMA. Expected: unreachable. Success = **Critical**.
- **Claim C2:** within a legitimately shared EFA SG, a participant account can RDMA-read a peer's registered memory. → **Oracle:** canary org with a shared self-ref EFA SG; confirm RDMA works participant→owner, then that it reaches memory the owner did not intend to expose to that participant. Also: **does EFA/SRD even negotiate correctly over a shared SG?** (undocumented combination — doc-gap).
- **Claim C3:** no Nitro QP↔ENI binding exists. → **Oracle:** doc-gap confirmation first; then whether a crafted/foreign rkey or QP number is honored by a peer's EFA device. **If the device honors a QP/rkey not issued to the caller → HARD STOP (service-plane / cross-tenant memory) and disclose.**
**Doc evidence.** `efa.md` limitations; `efa-changelog.md` (MR/QP bug history); VPC `security-group-sharing.html`, `vpc-sharing.html`, `share-placement-group.md`; `ec2-security-groups.md:28`. **Severity-if-true:** C1 **Critical**; C2 **High** (cross-tenant lateral within an over-shared org); C3 **Critical if the hardware binding is absent** — top hunter priority alongside Area B. **Preconditions:** canary instances you own on both ends; never attempt against memory you cannot prove you own.

### Area D — AWS-authored install runbook: root RCE behind single-origin TLS — Lens R/Q/U  [HIGH, AWS-AUTHORED ARTIFACT]
**Background.** The default copy-verbatim path is `curl -O https://efa-installer.amazonaws.com/aws-efa-installer-1.50.0.tar.gz` (or `latest`) → `sudo ./efa_installer.sh -y`, which on every non-SUSE distro **builds and inserts out-of-tree kernel modules** (`efa`, `efa-nv-peermem`) as root.
**Security Concern.** The *only* default integrity control is TLS to the single host `efa-installer.amazonaws.com`. Both verification steps are optional and off by default, and the doc text actively invites skipping: GPG tarball verification is "(*Optional*)… If you do not want to verify the tarball file, skip this step"; per-package `--check-signatures` (added 1.48.0) is "optional. Without it, the installer does not perform individual signature verification." The GPG key **and** the signature are fetched from the **same origin** as the tarball (verify-against-same-origin — a compromise/MITM of that origin defeats both). The genuinely-independent artifacts (SHA256 table on `docs.aws.amazon.com`, the printed fingerprint `4E90 91BC…DD2D 3CCC`) exist cross-origin but are never wired inline into the download command — relegated to a "**Note** Alternatively…" aside (`efa-verify.md`). The **container** runbook (`efa-installer-containers.md`) is strictly weaker: only the coarse same-origin GPG step, `--check-signatures` never mentioned, installer run without `sudo` (implicit container-root).
**High-level Test Scenarios:**
- **Claim:** following the AWS default path, a tampered artifact/origin → root RCE + ring-0 kmod insert, with no default control catching it beyond TLS. → **Oracle (doc-reasoning + harness, no live AWS):** trace that no step pins a checksum inline; `latest` is a mutable single-origin pointer (ongoing-origin-compromise = fleet-wide fresh-install compromise); pinned old versions (≤1.47.0, still fetchable) have no per-package signing at all.
- **Claim:** `--no-verify` in the container doc is mistaken for "signature verification disabled." → **Oracle:** confirm `--no-verify` is only `lspci`-based device detection, not a security control (flag so a hunter does not misread it).
- **Kernel-module trust (Lens U doc-gap):** the EFA docs contain **zero** discussion of module signing, Secure Boot/MOK, or lockdown-mode interaction. Flag the EFA kernel driver as a device→guest channel worth separate review (cross-ref the known Nitro ENA-driver double-free history in `troubleshoot-ena-driver`); mark **doc-gap — confirm surface**.
**Doc evidence.** `efa-start.md:162,186-204,213,231,235`; `efa-verify.md`; `efa-installer-containers.md`; `efa-changelog.md` (1.48.0 = `--check-signatures` + libfabric memory-safety fixes, no CVE IDs cited). **Severity-if-true:** **High** — AWS-authored copy-verbatim runbook whose default path omits integrity; reportable (Tier 2, `aws-security`), not a customer footgun. **Stop condition:** do not attempt to tamper with or probe the real `efa-installer.amazonaws.com` origin — that is AWS service plane; this lead is settled by doc-reasoning + local analysis only.

### Area E — Insecure AWS-authored sample configs (SG, passwordless SSH, IMDS, AMI secret-baking) — Lens R/T/EE  [MEDIUM–HIGH, AWS-AUTHORED]
**Background.** The tutorial ships several copy-verbatim artifacts.
**Security Concern & Scenarios:**
- **(E1) EFA-enabled SG — SSH `0.0.0.0/0`.** Step 1 instructs an inbound SSH rule with **Source = Anywhere-IPv4** plus a self-referencing all-traffic rule. AWS prints an "intended for testing purposes only" warning, but the artifact is copy-verbatim and the warning is easily skipped. → **Oracle:** the created SG has `0.0.0.0/0:22` ingress. **Severity Medium** (acknowledged by AWS, so partially mitigated by the warning). The self-ref "allow all" rule is the Area B/C substrate.
- **(E2) Passwordless-SSH config — multiple footguns in one block.** Step 12 instructs `StrictHostKeyChecking no` (disables host-key verification → in-cluster MITM), `ForwardAgent yes` for `Host *` (agent forwarding to **all** hosts → a compromised member node can hijack the operator's forwarded agent to reach the operator's *other* credentials/hosts), `ssh-keygen -t rsa -N ""` (**no passphrase** private key), and copying the public key into every member's `authorized_keys`. → **Oracle:** `~/.ssh/config` contains `Host *` with both weakened options; `id_rsa` has empty passphrase. **Severity Medium–High** — `ForwardAgent yes` + `Host *` is the lateral-movement enabler. AWS-authored, no warning on the SSH options.
- **(E3) IMDSv2 optional.** The note only says "**Consider** requiring IMDSv2 … unless you have already set it as the account default" — IMDSv1 remains the effective default for the temp instance and the AMI. → **Oracle:** created instance/AMI has `HttpTokens=optional`. Cross-ref the Lens-R insecure-sample-default class (`MetadataOptions.HttpTokens:"optional"`). **Severity Medium.**
- **(E4) Secrets baked into a shared EFA AMI (Lens T/EE).** Steps 9–10 create an AMI from the temp instance **after** Steps 3 (GPG keyring), 5 (Intel vars), and before Step 12 (SSH key) — but the only cleanup instructed is "delete the tarball … to reduce size." Nothing tells the user to remove the imported GPG keyring, `authorized_keys`, or (if imaging after Step 12) the no-passphrase `id_rsa` before imaging. If the resulting AMI is later **shared or made public**, baked credentials/keys leak. → **Oracle:** inspect a created EFA AMI for residual `~/.ssh/id_rsa`, `authorized_keys`, GPG private material; check whether the AMI is shareable with its secrets intact (chains to Lens EE whoAMI-style name resolution if the AMI name is predictable). **Severity Medium–High if a private key or credential is baked and the AMI is shared.**
**Doc evidence.** `efa-start.md` Step 1 (lines ~55-75), Step 9 (~430-470), Step 12 (641-657); IMDS note line 122. **Severity:** per sub-item above. All AWS-authored copy-verbatim → reportable where the default is insecure (E2/E4 strongest).

### Area F — Detach/reattach residual RDMA state & SG-change on live EFA — Lens AA/X  [HIGH IF TRUE; DOC-GAP]
**Background.** `create-efa.md` says you *change the SG on an EFA to enable OS-bypass* and that EFA can only be attached/detached on a **stopped** instance. `detach-efa.md` is purely procedural ("stop first, then detach") and says **nothing** about MR/QP teardown or on-card state.
**Security Concern.** (a) **Revocation completeness** (pairs with Area B): does changing/removing the self-ref SG on a live EFA sever established RDMA, or only block new association? `security-group-connection-tracking.md:14` warns tracked connections survive a rule change until timeout — **and EFA/SRD likely isn't conntrack-tracked at all** (`efa-working-monitor.md` flow-log evidence: MAC-identified, blank port/protocol; non-TCP/UDP flows get minimal tracking), so there may be *no* grace-period drain semantics defined for EFA. (b) **ENI reuse**: if an EFA ENI (or its device/driver MR/QP state) is detached and reattached to a different instance — potentially a different participant in a shared VPC — does stale memory-registration state persist (analogous to EBS-volume-reuse-without-zeroing, but for RDMA handles)?
**High-level Test Scenarios:**
- **Claim:** SG revoke does not sever a live SRD/RDMA flow (see Area B oracle — same test). **Severity High if confirmed.**
- **Claim:** stale MR/QP state survives a stop→detach→reattach-to-different-owner cycle. → **Oracle:** canary ENI reuse across two instances you own; inspect whether prior memory handles remain valid. **If a reused ENI exposes a prior owner's memory → HARD STOP / cross-tenant → disclose.**
**Doc evidence.** `create-efa.md:8,11,56-59`; `detach-efa.md`; `security-group-connection-tracking.md:14,29-37`; `efa-working-monitor.md:194-198`. **Severity:** High if either holds; both are doc-gaps to confirm first.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| IAM policy cannot forbid EFA/OS-bypass attachment | CreateNetworkInterface/RunInstances/Attach | *(none — no `ec2:InterfaceType` key; this IS the gap)* |
| OS-bypass bypasses the firewall, not just the kernel | EFA device / SRD path | Self-referencing SG "mandatory for EFA to function" (availability claim only) |
| Cross-account RDMA to a non-consenting tenant | EFA fabric | "EFA traffic can't cross AZ or VPC"; "not routable"; SG membership |
| Over-shared SG → participant RDMA to all members | Shared Security Groups (RAM, same Org) | Same-Org + owner-opt-in consent gates |
| Driver/libfabric MR/QP memory-safety bug → peer memory | libfabric + `efa`/`efa-nv-peermem` kmod | *(app-level MR/rkey scoping; no documented Nitro QP↔ENI binding)* |
| SG revoke does not sever live RDMA session | SG + EFA data path | Connection-tracking grace period (likely N/A to SRD) |
| Root RCE via default install path | efa_installer.sh (root + kmod) | Single-origin TLS; optional GPG; optional `--check-signatures` |
| Credentials/keys baked into shared EFA AMI | AMI create (Steps 9-10) | *(only "delete tarball to reduce size")* |
| Lateral movement via `ForwardAgent yes`/`Host *` | passwordless-SSH sample config | *(none — AWS-authored, unwarned)* |
| SSH open to `0.0.0.0/0` | EFA-enabled SG sample | "testing purposes only" warning |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **A tenant RDMA-ing within its own cluster/SG** — intended behavior (`ec2-security-groups.md:28`), explicitly OOS.
- **Owner-consented cross-account EFA via Shared Security Groups / shared subnets / shared placement groups** used *as designed* — a trust-extension feature, not a bug (becomes in-scope only if the share can be joined *without* owner consent, or if unshare fails to sever — Area C2/F).
- **Nitro card internals, EFA device firmware, the SRD fabric substrate, the `efa-installer.amazonaws.com` origin** — AWS service plane; **HARD STOP + disclose**, never probe.
- **ptrace disable + CMA shared memory** (`kernel.yama.ptrace_scope=0`, Step 6): reduces intra-instance process isolation **on the customer's own instance** — a single-tenant self-inflicted hardening reduction; OOS except as defense-in-depth note for multi-user HPC nodes.
- **IMDS on the managed instance**, product/feature-parity gaps, single-tenant self-DoS, DNS-rebinding against private-only endpoints.
- **Customer-authored** IAM policies / SGs (footgun). The in-scope artifacts here are **AWS-authored** (the sample SG, SSH config, install runbook) — do not downgrade those to "customer footgun."
- **Third-party supply chain** (NVIDIA GPU driver, GDRCopy from GitHub, Intel MPI) pulled by the NCCL/NIXL siblings — bugs in those repos are OOS, but the AWS-authored *instruction to fetch them unpinned/unverified* is in-scope under Area D's lens (note for the sibling plans).

---

## 8. Null Hypotheses / Doc Gaps (lenses checked, with pages)
- **Lens G (SSRF) — null.** Read `efa-start.md`, `create-efa.md`, `efa.md`, `efa-working-monitor.md`: no field the service dereferences server-side on the customer's behalf (the installer URL is fetched by the *guest*, not an AWS service). N/A.
- **Lens K (prompt injection) — null.** No LLM/agent in the EFA enablement path. (NCCL/NIXL run ML *workloads*, but that is customer compute, not an AWS pipeline.) N/A.
- **Lens B/C (PassRole / credential vending) — null for this page.** EFA attach/create takes no role ARN; no STS/session-policy construction. N/A on `efa-start`; general EC2 launch PassRole lives in the launch-template/RunInstances plans.
- **Lens H (KMS/encryption-context) — null here.** No EFA-specific CMK/encryption-context surface (EBS encryption on the AMI is the generic EBS surface, OOS). 
- **Lens J (OAuth), M (session interception), FF (JWT) — N/A** — no web-session/token surface on this device-enablement page.
- **Lens P (proofing/registration) — N/A** — no registration/identity-proofing workflow.
- **DOC-GAPS to confirm surface first (not null):**
  1. **Where EFA/SRD SG enforcement happens** (Nitro card vs guest vs one-time admission) — Area B. The single most load-bearing gap.
  2. **Whether Nitro binds QPs to the owning ENI in hardware** — Area C3. Critical-if-absent.
  3. **Whether SG revoke/unshare severs a live RDMA/SRD session** — Area B/F.
  4. **Whether EFA/SRD negotiates correctly over a *shared* SG** (undocumented combination) — Area C2.
  5. **MR/QP state lifecycle across stop/detach/reattach** — Area F.
  6. **EFA kernel-module signing / Secure Boot / lockdown interaction** — Area D; zero docs, cross-ref ENA-driver history.
  7. **Whether EFA create/attach is even distinguishable to any control (SCP/tag) at all** given no InterfaceType key — Area A (confirmed negative in IAM; SCP/orchestration layer untested).

---

### Appendix — reusable facts confirmed during this build
- **`ec2:InterfaceType` is NOT a real IAM condition key** (0 hits in all of `list_ec2.md`; `efa` substring hits are "Default"). EFA has **no dedicated IAM action/resource/ARN** — purely a parameter value on generic ENI/instance actions. Confirms the skill's Lens-S variant note with line evidence (CreateNetworkInterface L5359-5361; RunInstances L9595/9599; AttachNetworkInterface L4861; ModifyNetworkInterfaceAttribute L8969-8970).
- **EFA = OS-bypass SRD on Nitro v4+;** confinement is VPC+AZ+SG only, account/tenant is not a documented boundary dimension; EFA traffic is not routable and MAC-identified in flow logs (blank port/protocol).
- **ENA/IP firewall is Nitro-card-enforced** (`ena-nitro-perf.md:12,17,32`) — the structural analogy that makes "EFA probably Nitro-enforced too" *plausible but unproven* for the EFA device path.
- **Shared Security Groups** (RAM, same AWS Org) + shared subnets + shared placement groups are the only documented cross-account path into an EFA fabric — consent-based.
- **Install default path integrity = single-origin TLS only;** GPG and `--check-signatures` both optional/off; `--check-signatures` added 1.48.0 (2026-04-14); older pinned versions have no per-package signing; container path strictly weaker. `--no-verify` (container) = `lspci` device check, not a security control.
- **list_ec2 slug** = `list_ec2` (not `list_amazonec2`); online `.md` truncates before the detailed action rows — use the offline mirror by grep for condition-key cells. See [[reference-aws-iam-service-auth-ref-url]].
- Sibling walkthroughs `efa-start-nccl` / `efa-start-nixl` reuse the **identical** insecure SG + passwordless-SSH artifacts and add NVIDIA-driver/GDRCopy (GitHub, unpinned) supply chain + GPUDirect RDMA — a future per-sibling plan should cross-ref Areas B/C/D/E here rather than restate them.
