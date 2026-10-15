# Elastic Fabric Adapter (EFA) — Attack Research Plan

Source of leads: offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/{efa,create-efa,detach-efa,efa-start,efa-start-nccl,efa-start-nixl,efa-acc-inst-types,efa-installer-containers,efa-working-monitor,efa-verify,efa-changelog}.md`, their online `.html`/`.md` twins at `docs.aws.amazon.com/AWSEC2/latest/UserGuide/` (all 10 child pages spot-checked 2026-10-15 — **byte-for-byte identical offline↔online, no drift on any page**), and `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (authoritative IAM ground truth, trusted over User-Guide prose on conflict). Status: **documentation-derived falsifiable hypotheses only; nothing tested against a live account.** No claim below asserts a confirmed bug.

**Relationship to sibling plans (read these for the surface this plan deliberately defers):**
- **`.cache/plans/ec2-net-frag3-placement-efa.md`** — the placement-group / topology / enhanced-networking *cluster fragment* that first flagged EFA SRD cross-tenant frame injection and the self-referencing SG. This plan is the dedicated, page-complete EFA deep-dive that owns the full 10-child EFA tree; it cross-references frag3 for placement-group **co-residency** (shared Cluster-PG → cross-account physical adjacency, the precondition for any cross-tenant RDMA question).
- **ENI cluster** (`using-eni`, `create-network-interface`, `modify-network-interface-attributes`, `network-interface-attachments`, `delete-eni`, `managing-network-interface-ip-addresses`): an EFA *is* an ENI variant (`InterfaceType=efa`/`efa-only`). Generic ENI IDOR, cross-VPC attach, SG-change, attach/detach, and delete-collateral are owned there. This plan owns only what is **EFA-specific**: the OS-bypass/RDMA/SRD device, the `InterfaceType`-unscopability, the mandatory self-referencing SG, and the installer supply chain.
- **ENA cluster** (`ena-express`, `ena-nitro-perf`, `enhanced-networking-ena`): ENA Express is the *other* SRD consumer. **EFA SRD is distinct** — EFA SRD cannot cross AZ/VPC and is non-routable; ENA Express SRD works cross-AZ in-Region and silently falls back to standard ENA. Nitro flow-cache/conntrack behavior and the shared-NIC bandwidth governor are owned by `ena-nitro-perf`/`ec2-instance-network-bandwidth`.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (§5 is ranked); look left and right for adjacent bugs.
- **Safe-first oracle for every IAM lead:** `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` — proves a condition key is inert/absent with **zero resources touched**. Escalate to a live scoped call only with synthetic canary data under a role holding *exactly* the artifact.
- **HARD STOP:** the moment evidence shows EFA/SRD traffic, an RDMA memory region, a queue-pair, or any credential/ARN reaching **another AWS account** or **AWS's own Nitro/fabric service plane**, stop, preserve evidence, and flag for AWS-Security disclosure. The RDMA-isolation and SRD-fabric questions (§5 Area 4) sit on that line by design — treat them as *confirm-the-mechanism-first* doc-gaps, not things to actively break against a live fabric.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Attach a privileged device-type the admin tried to forbid** — create/attach an `efa`/`efa-only` (OS-bypass, RDMA-capable) interface from a principal an org policy *intended* to restrict to plain `interface` ENIs, and show no IAM/SCP condition could have stopped it.
2. **Pivot across an EFA cluster** — from one compromised cluster member, reach every peer on all ports (self-referencing all-traffic SG) and/or assume the leader's identity (forwarded ssh-agent + disabled host-key checking + passphrase-less key).
3. **Compromise the EFA software supply chain** — substitute a tampered installer / dependency that the AWS-published walkthrough runs as root with verification off by default.
4. **(HARD STOP) Cross the SRD/RDMA tenant boundary** — address, read, or write an RDMA memory region, or inject an SRD frame received, on an instance outside the sender's account/VPC — falsifying "EFA traffic can't cross … VPCs."
5. **Evade EFA-aware detection** — move laterally over OS-bypass traffic that IP-5-tuple flow-log tooling cannot parse, and/or reset driver counters an operator alerts on.

## 2. Components, Assets, and Design

**Customer-facing interface / selection knob.** EFA is not a distinct API; it is a **value of the `InterfaceType` parameter** on `CreateNetworkInterface` / `RunInstances --network-interfaces` / launch templates: `interface` (plain ENA), `efa` (EFA-with-ENA), `efa-only` (EFA device only, no IP). Console field: "Interface type → EFA with ENA / EFA-only" (create-efa.md). The device-type *is* the privilege boundary (OS-bypass + RDMA vs ordinary IP).

**Processes / stack (data plane).**
```
AI/ML app (NCCL/NIXL) ─┐                         ┌─ EFA device (OS-bypass, SRD, RDMA R/W, GPUDirect RDMA/GDA)
HPC app (Open MPI /    ├─ Libfabric (user-space, ├─ kernel-BYPASS ──► Nitro card ──► SRD fabric (intra-AZ, intra-VPC, non-routable)
  Intel MPI) ──────────┘   OFI; rdma-core, QP/AH) │
                                                  └─ ENA device (TCP/IP, kernel stack) ──► VPC routing  (EFA-with-ENA only)
```
- **EFA device**: "built-in OS-bypass and congestion control through the Scalable Reliable Datagram (SRD) protocol"; "Libfabric API bypasses the operating system kernel and communicates directly with the EFA device to put packets on the network" (efa.md). RDMA read (all Nitro v4+), RDMA write (most v4+), GPUDirect RDMA/Async on select instances. EFA generations v1(Nitro v3)→v4(Nitro v6).
- **Consumers**: Open MPI 4.1+, Intel MPI 2019 U5+, NCCL 2.4.2+, NIXL 1.0.0+, DeepEP v2, AWS Neuron SDK 2.3+ (efa.md "Supported interfaces and libraries").
- **Installer / supply chain**: `efa-installer.amazonaws.com` serves `aws-efa-installer-<ver>.tar.gz`, `aws-efa-installer.key` (GPG, RSA), and the checksum table (efa-start*.md, efa-verify.md). `efa_installer.sh` run as root.
- **Security group**: EFA requires an SG "that allows all inbound and outbound traffic to and from the security group itself" (create-efa.md, efa-start.md Step 1).

**Accounts / VPCs / network.** Single-account/single-VPC/single-AZ by design: "EFA traffic can't cross Availability Zones or VPCs" and "is not routable" (efa.md). An EFA is created in one subnet, immovable, attachable only to **stopped** instances in the **same AZ** (create-efa.md). Multi-tenancy question is physical: EFA-supported instances are large/metal (implicitly single-tenant per host), but a **shared Cluster placement group** can place *different accounts'* instances on adjacent hardware (see frag3 plan) — the only documented path to cross-tenant physical proximity.

**Resource identifiers.** ENI id `eni-…` (the EFA). Fabric-level addressing (queue-pair numbers, Address Handles/Address Vectors) surfaces **only** in `efa-changelog.md` bug-fix lines — never in an architectural/security doc.

**Identity.** Control-plane: SigV4 IAM on EC2 ENI actions. Data-plane: none — OS-bypass means the guest process talks to the device directly; there is no per-RDMA-op IAM check.

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Principal an org policy *intends* to deny OS-bypass/RDMA | An `efa`/`efa-only` interface | `CreateNetworkInterface --interface-type efa` / `RunInstances … InterfaceType=efa` | A deny/allow policy keyed on interface-type cannot be written — **no `ec2:InterfaceType` key exists** (grep of full `list_ec2.md` = 0). `SimulateCustomPolicy` shows every attempted condition is inert → EFA attaches regardless. |
| Compromised instance in an EFA SG | Every other instance in that SG, all ports/protocols | Self-referencing **all-traffic** inbound+outbound SG rule (AWS-mandated) | A connection on any port to a peer in the same SG succeeds — the AWS-published "mandatory" rule *is* the lateral-movement surface. |
| Compromised cluster node | Leader node identity + all nodes | Forwarded ssh-agent socket + `StrictHostKeyChecking no` + passphrase-less `id_rsa` in `authorized_keys` (AWS walkthrough) | Using the forwarded agent / unprotected key to SSH as the default user to the leader or any node = acting as another identity the attacker was not given. |
| Customer host running the AWS walkthrough | Root shell on that host | Root-run `efa_installer.sh` + unpinned/unverified downloads from single origin | A tampered `latest` tarball, GPG key (same origin, TOFU), or unpinned `git clone`/`pip install` executes as root. |
| Tenant A instance (EFA, OS-bypass) | **Tenant B** instance on the same SRD fabric segment / shared Cluster-PG hardware | SRD frame / RDMA op addressed by QP/AH, bypassing VPC routing & SG | **(HARD STOP)** a frame is received by, or an RDMA read/write completes against, an instance outside the sender's account/VPC → falsifies "EFA traffic can't cross … VPCs". |
| Guest process (either tenant) | Nitro EFA device / SRD fabric control | Malformed SRD/RDMA descriptors over the OS-bypass path | **(HARD STOP)** device/hypervisor-side crash or memory disclosure crossing the guest↔Nitro line = service-plane. Guest-side libfabric crash that stays in-guest = self-DoS (OOS). |
| Lateral attacker on OS-bypass path | Detection/forensics plane | EFA flow logs = MAC addrs, no ports/proto; EKS Container Insights omits 5 SRD-anomaly metrics; counters zero on driver reset | A pivot over EFA produces flow-log rows no IP-5-tuple rule matches, and/or a driver reset erases the counters an alarm watched. |

## 4. API / Interface Inventory (from `list_ec2.md`, verified)

| Name | Mutating | Resource row → relevant condition keys | Interface-type scopable? | Notes |
|---|---|---|---|---|
| `CreateNetworkInterface` | Yes | `network-interface*` → aws:RequestTag, aws:TagKeys, **ec2:NetworkInterfaceID**, ec2:Region; `security-group` → SecurityGroupID, Vpc, ResourceTag; `subnet*` → SubnetID, AZ, Vpc | **NO** | `--interface-type efa\|efa-only` is the EFA selector; **no condition key constrains its value.** |
| `AttachNetworkInterface` | Yes | `instance*` → InstanceType, Tenancy, PlacementGroup, … ; `network-interface*` → NetworkInterfaceID, AZ, Subnet, Vpc, ResourceTag | **NO** | Attaching an already-`efa` ENI likewise cannot be gated on its EFA-ness. Requires **stopped** instance. |
| `RunInstances` | Yes | `network-interface` row (see using-eni/create-network-interface plans) | **NO** | `InterfaceType=efa` inline at launch; same key gap (grep-confirmed absent on every row). |
| `ModifyNetworkInterfaceAttribute` | Yes | `network-interface*` → **ec2:Attribute, ec2:Attribute/${AttributeName}**, NetworkInterfaceID; `security-group` → SecurityGroupID, Vpc | Partial | Changes the EFA's SG. `ec2:Attribute` can gate *which attribute* (e.g. `groupSet`) and SecurityGroupID *which SG*, but **not** whether the resulting SG is the wide self-referencing one. |
| `DetachNetworkInterface` / `DeleteNetworkInterface` | Yes | see delete-eni / network-interface-attachments plans | — | detach-efa.md defers entirely to generic ENI procedures; requires stopped instance. |
| `DescribeInstanceTypes` | No | (filter `network-info.efa-supported=true`) | — | Read oracle: enumerates EFA-capable instance types per Region (efa.md CLI block). No resource-level scoping. |

**Console-hidden / parameter-only knobs:** `InterfaceType` enum (`efa`/`efa-only`) is a plain request field with **no IAM surface** — the exact "most-permissive value accepted by the API with nothing to warn the operator" shape §3-of-the-skill asks for. Installer flags `--no-verify`, `--skip-kmod`, `--skip-limit-conf`, and the umbrella `--enable-ngc` (efa-installer-containers.md) bypass checks with low operator visibility.

## 5. Recommended Areas of Focus (ranked)

### Area 1 — [HEADLINE] EFA attachment is IAM-unscopable: no `ec2:InterfaceType` condition key (Lens S / U)
**Background.** OS-bypass + RDMA is a materially more powerful network capability than ordinary IP networking, selected purely by the `InterfaceType` request parameter. An admin's natural control is "only approved workloads may attach EFA / RDMA interfaces."
**Security Concern.** That control is **unexpressible.** A full grep of `list_ec2.md` returns **zero** matches for `InterfaceType`, `interface-type`, `rdma`, `SRD`, or `OsBypass`. `CreateNetworkInterface`, `AttachNetworkInterface`, and `RunInstances` carry no condition key for the interface type on any resource row (§4). This is the confirmed "a condition key that does not exist → cannot deny by it" variant of Lens S, developed for EFA: the privileged device-type rides a parameter with no IAM backstop. Because the gap is in the **AWS-defined IAM schema** (not a customer policy), it is a Lens-U documented-capability-vs-enforcement defect AWS owns, not a customer footgun.
**High-level Test Scenarios.**
- *Claim:* a principal allowed `ec2:CreateNetworkInterface`/`RunInstances` for ordinary ENIs can always also create/attach `efa`/`efa-only` interfaces → *Oracle:* `SimulateCustomPolicy` with every plausible denying condition (there is no key to name) returns Allow; a scoped live `create-network-interface --interface-type efa` succeeds. *Severity:* **Medium** (AWS-owned enforcement gap; reportable Lens U).
- *Claim:* tag-based ABAC cannot substitute, because tags are applied *after* type selection and `aws:RequestTag` doesn't encode interface type → confirm the only levers are subnet/SG/Region, none of which encode EFA-ness.
- *Adjacent:* does `ModifyNetworkInterfaceAttribute` let a plain ENI be converted to EFA post-hoc? (Doc implies type is fixed at create; confirm — if convertible, the `ec2:Attribute` gate becomes relevant.)
**Doc evidence:** `list_ec2.md` (grep=0); create-efa.md CLI `--interface-type efa|efa-only`. **Severity-if-true:** Medium, Tier-2 reportable (AWS schema gap).

### Area 2 — [HEADLINE, in-scope] AWS-mandated self-referencing all-traffic security group (Lens V / S / R-published-config)
**Background.** The AWS getting-started walkthrough (all three: MPI, NCCL, NIXL, Step 1) tells the customer to build and attach an SG whose inbound and outbound rules are **Type: All traffic, Source/Destination: the SG itself**.
**Security Concern.** This is an AWS-authored config the customer copies verbatim. The broad rule is framed as **unconditionally mandatory**, in production and test alike: *"The self-referencing inbound and outbound rules (allowing all traffic to and from the security group itself) are mandatory for EFA to function."* The **only** "testing purposes only" caveat in the step applies to the *SSH-ingress source* (0.0.0.0/0), **not** to the all-traffic self-reference — the broader rule gets the weaker warning. Any single compromised instance in an EFA cluster therefore has unrestricted L3/L4 reach (every port, every protocol) to every peer in the SG — the cluster's internal segmentation is zero by AWS's own instruction.
**High-level Test Scenarios.**
- *Claim:* membership in an EFA SG = full mesh connectivity, so one foothold → lateral movement to all cluster peers → *Oracle:* from a canary instance in the SG, open an arbitrary non-EFA TCP/UDP port to a peer and connect; it succeeds because the self-ref rule is all-traffic not RDMA-scoped. *Severity:* **High** (cross-host lateral movement on a shared cluster).
- *Claim:* the walkthrough offers no narrower alternative (e.g. restricting the self-ref rule to the EFA/SRD requirement specifically) → confirm no scoped variant is documented; the customer cannot both run EFA and keep intra-cluster segmentation using AWS's guidance.
**Doc evidence:** efa-start.md#efa-start-security, efa-start-nccl.md#nccl-start-base-setup, efa-start-nixl.md#nixl-start-base-setup. **Severity-if-true:** High.

### Area 3 — [in-scope, chains with Area 2] Passwordless-SSH cluster trust pattern (Lens P)
**Background.** The same three walkthroughs establish inter-node trust for MPI/NCCL/NIXL launches.
**Security Concern.** The documented pattern is maximally permissive and framed as the **persistent operational config** (no "testing only" caveat, unlike the SG's SSH source): global `Host * StrictHostKeyChecking no` + `Host * ForwardAgent yes`, plus a **passphrase-less** key `ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa` whose public half is hand-appended to peers' `authorized_keys` with no `from=`/`command=` restriction, under well-known default users (`ec2-user`/`ubuntu`/`admin`/`admin`). No rotation/revocation/rollback is described.
**High-level Test Scenarios.**
- *Claim:* compromising any node yields the leader's forwarded ssh-agent and host-key-check-disabled SSH to all nodes → *Oracle:* on a canary cluster, from a non-leader node use the forwarded `SSH_AUTH_SOCK` to authenticate to the leader as the default user. *Severity:* **High** (identity pivot across the cluster).
- *Claim:* `StrictHostKeyChecking no` globally enables MITM of *any* SSH destination from the leader, not just cluster peers → confirm the config is unscoped (`Host *`).
- *Chain with Area 2:* the self-ref all-traffic SG guarantees port 22 reachability between all members, so the SSH pivot has no network obstacle.
**Doc evidence:** efa-start.md Step 12 / efa-start-nccl.md Step 13 / efa-start-nixl.md Step 12. **Severity-if-true:** High.

### Area 4 — [HARD STOP / doc-gap] SRD-fabric & RDMA memory-region tenant isolation (Lens D / V / F)
**Background.** EFA does OS-bypass RDMA (read/write) and GPUDirect RDMA directly to/from device and GPU memory, over the SRD fabric, addressed by queue-pair numbers and Address Handles.
**Security Concern.** The isolation guarantees are **asserted as fabric properties with no documented enforcement mechanism and no memory-isolation statement at all.** efa.md states "EFA traffic can't cross Availability Zones or VPCs" and "is not routable" **without** attributing the confinement to security groups, NACLs, route tables, or any named control — it reads as an inherent fabric constraint. **No page in the EFA corpus describes how RDMA memory regions are isolated between instances/tenants, or how a receiving instance validates a peer's QP number / Address Handle.** Supporting signal that this is a real risk surface: `efa-changelog.md` shows **QP-number verification on CQE was *added* as a fix** (1.44.0 "Verify QP number on CQE", 1.47.0 "Add QP generation to data path … and verify QP number on CQE"), and a recurring class of memory-safety bugs (use-after-free, double-free, ABA, races) lives in the exact QP/CQ/AH/MR code paths (1.42.0, 1.44.0, 1.45.0, 1.47.0, 1.48.0) — i.e. the code that would have to be correct for any isolation guarantee to hold.
**High-level Test Scenarios (confirm-the-mechanism-first; do NOT actively break a live fabric).**
- *Claim:* EFA/SRD confinement to AZ/VPC is physical/addressing-based, not SG/route-enforced → *Oracle (doc/architecture first):* identify from AWS whether an SRD endpoint can even *form* an Address Handle to a peer outside its VPC. Only if a documented or observed path exists does a live test become warranted — and a received cross-VPC/cross-account frame is an immediate **HARD STOP**, service-plane disclosure.
- *Claim:* RDMA memory regions are isolated per-instance by the Nitro device, not by anything the guest controls → treat as doc-gap; the enforcement owner is AWS/Nitro (service plane). Guest-side libfabric memory-safety bugs that stay in-guest are self-DoS (OOS); only a cross-tenant effect is in scope and is a hard stop.
- *Precondition for any cross-tenant angle:* cross-account physical adjacency, which per the corpus is only reachable via a **shared Cluster placement group** (see frag3 plan) — enumerate that path before anything else.
**Doc evidence:** efa.md (efa-basics, efa-limits); efa-changelog.md (QP/CQE/MR fix lines). **Severity-if-true:** Critical + HARD STOP. **Status: doc-gap — confirm the isolation mechanism with AWS before any live interaction.**

### Area 5 — [in-scope] EFA software supply chain: TOFU single-origin + verification-off-by-default + unpinned deps (Lens Y / R-code)
**Background.** AWS's walkthroughs install EFA and its ML/HPC dependencies by downloading and running code **as root**.
**Security Concern.** The trust chain is weak at every link, in AWS-published copy-verbatim steps:
- **Single-origin TOFU:** the installer tarball, the GPG public key (`wget …/aws-efa-installer.key && gpg --import`), and the checksum table all come from `efa-installer.amazonaws.com`. Compromise of that origin/CDN yields payload **and** validating key. No out-of-band key (no keyserver, WKD, or second-channel fingerprint).
- **Verification is opt-in and sometimes absent:** *"(Optional) Verify … If you do not want to verify the tarball file, skip this step"* (efa-start.md, efa-start-nccl.md); the **NIXL** install step has **no tarball-verification sub-step at all**. Per-package `--check-signatures` is off by default. Checksums offered include **MD5**. The fingerprint check is a manual visual diff; the documented "expected" GPG output includes the uncleared `WARNING: This key is not certified with a trusted signature!`.
- **Floating version:** AWS documents replacing the pinned version with **`latest`** (efa-start.md, and `{{version}}` with "we recommend … the latest" in the container doc) — unpinned, no hash bound to `latest`.
- **Unpinned deps run as root:** `git clone` without a tag/commit for **nccl-tests**, **NIXL** (`sudo git clone … ai-dynamo/nixl`), **cpprestsdk** (+ unpinned `git submodule update`), **etcd-cpp-apiv3**, each followed by root `make/ninja install`; `pip install nixl` / `pip install vllm` and `sudo pip3.11 install meson ninja pybind11` with no version pin or `--require-hashes`.
- **Container worst-case:** NIXL benchmark `docker run -it --gpus all --network host nixlbench:latest` (host network + full GPU passthrough + `latest` tag) and an ETCD container bound to `0.0.0.0:2379/2380` with no auth and plaintext-HTTP health checks.
**High-level Test Scenarios.**
- *Claim:* a MITM/origin-compromise of `efa-installer.amazonaws.com` or a poisoned `latest`/unpinned-dep yields root code-exec on every host following the guide, with verification skippable → *Oracle:* trace each download in the walkthrough; confirm (a) verification is optional/absent, (b) key and payload share an origin, (c) `latest`/branch refs are documented. *Severity:* **High** (root compromise; owner-shared — AWS owns the TOFU single-origin + optional-verification framing; the customer owns choosing to pin/verify).
- *Note (non-finding, do not carry):* "DeepEP"/`amazon-contributing` is referenced on efa.md's library list but **does not appear** in any install walkthrough — no sourced supply-chain step for it in these pages.
**Doc evidence:** efa-start.md L157-167, efa-start-nccl.md L698-835, efa-start-nixl.md (install/benchmark steps), efa-verify.md, efa-installer-containers.md. **Severity-if-true:** High.

### Area 6 — [in-scope, lower] OS-bypass monitoring & forensic blind spots (Lens O)
**Background.** EFA packets never traverse the guest kernel network stack; monitoring is split across guest-side driver counters, VPC Flow Logs, and CloudWatch.
**Security Concern.**
- **Flow-log shape differs:** *"EFA traffic is identified by the `srcAddress` and `destAddress`, which are both formatted as MAC addresses"* with `sourcePort`/`destPort`/`protocol` shown as `-` (efa-working-monitor.md). Detection tooling that parses flow logs as IPv4/IPv6 5-tuples silently fails to match EFA rows → a lateral pivot over EFA is invisible to such rules. The doc shows only an `ACCEPT` example and **never discusses SG REJECT or SG interaction with EFA flows** — leaving open whether SGs filter SRD payload traffic at all (see Area 7).
- **EKS metric gap:** CloudWatch Container Insights "supports all EFA driver metrics, except `retrans_bytes`, `retrans_pkts`, `retrans_timeout_events`, `unresponsive_remote_events`, and `impaired_remote_conn_events`" — exactly the SRD-path-anomaly counters most useful for spotting adversarial fabric behavior are the ones excluded for container workloads.
- **Counter reset = anti-forensics:** metrics are cumulative "since instance launch or the last driver reset" → an attacker who can trigger a driver reset zeroes the history an operator alarms on.
- **Guest-only richest signal:** the `rdma`/`/sys/class/infiniband/.../hw_counters` metrics require in-guest shell access; no external API equivalent → a hunter blind without instance access, and so is a defender relying only on the API.
**High-level Test Scenarios.** *Claim:* a flow-log/alerting pipeline built for IP 5-tuples misses EFA lateral movement; a driver reset erases SRD anomaly counters → *Oracle:* generate EFA traffic on a canary, confirm flow-log rows carry MAC addrs/empty ports, and that a driver reset zeros `retrans_*`/`*_remote_*`. *Severity:* **Low–Medium** (detection enabler, raises severity of Areas 2–4).
**Doc evidence:** efa-working-monitor.md. **Severity-if-true:** Low–Medium.

### Area 7 — [doc-gap] SG association on `efa-only` interfaces may be vestigial; detach cleanup unspecified (Lens X / AA)
**Background.** Every CLI example in efa-acc-inst-types.md passes `Groups={{security_group_id}}` on `efa-only` interfaces, yet efa.md's table says EFA-only interfaces have no IP addressing, and no doc says SGs filter SRD payload traffic.
**Security Concern.** Two silences: (1) **Is `Groups=` on an `efa-only` ENI a functional control or dead config?** If SGs do not actually filter SRD/RDMA frames (plausible given OS-bypass and the MAC-only flow-log shape), then the Area-2 self-ref SG is *also* not what confines EFA traffic — the confinement is purely fabric-level (ties to Area 4), and operators who believe their SG restricts EFA traffic are mistaken. (2) **Detach/delete cleanup:** detach-efa.md defers wholly to generic ENI procedures and says **nothing** about tearing down SRD/QP/Address-Handle/memory-region state; detach requires a stopped instance. Changelog QP-destroy/cleanup fixes ("Fix CQ poll after QP destroy", "null check for base_ep … to handle destroyed QPs") hint teardown correctness has been buggy.
**High-level Test Scenarios.** *Claim:* an SG rule change does not alter what EFA/SRD traffic is permitted (SG is enforced only on the ENA/IP path) → *Oracle:* with EFA traffic flowing, remove/narrow the self-ref SG rule and observe whether EFA (not ENA) traffic is affected; if unaffected, SG is non-functional for SRD. *Claim:* stale QP/AH state could be addressable after detach → doc-gap, service-plane adjacent, confirm mechanism first. *Severity:* Informational–Medium (mostly a doc-vs-enforcement clarification; escalates Area 4 framing).
**Doc evidence:** efa-acc-inst-types.md (Groups= on efa-only), efa.md (table), detach-efa.md, efa-changelog.md. **Severity-if-true:** Low–Medium.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Attach OS-bypass/RDMA device despite org intent to forbid it | CreateNetworkInterface/RunInstances `InterfaceType` | *(none exists)* — no `ec2:InterfaceType` key; test that no IAM/SCP condition can block it |
| One foothold → full cluster lateral movement | Self-referencing all-traffic SG | SG membership (but rule is all-traffic, so no intra-cluster L4 segmentation) |
| Identity pivot to leader / all nodes | Passwordless SSH + agent forwarding | *(none)* — `StrictHostKeyChecking no`, passphrase-less key, no rotation |
| Root RCE via tampered installer/dep | EFA installer + git/pip deps | GPG sig + checksums — **both optional, same-origin TOFU, MD5, `latest` unpinned** |
| Cross-tenant RDMA read/write or SRD frame | SRD fabric / RDMA MR / QP-AH | "can't cross AZ/VPC", "not routable" — **mechanism undocumented**; HARD STOP on confirm |
| Evade EFA-aware detection | Flow Logs / CloudWatch / driver counters | Flow Logs capture EFA (MAC-only); EKS omits 5 SRD metrics; counters reset-zeroable |
| SG believed to confine EFA traffic but doesn't | SG on efa/efa-only ENI | SG association exists; **enforcement on SRD payload undocumented** |

## 7. Out-of-Scope Risk Categories
- **AWS Nitro/SRD fabric internals and hypervisor-side EFA device memory safety** — service plane / shared-responsibility line. The changelog UAF/double-free/ABA fixes are in the **guest-side** libfabric/rdma-core client; a guest-only crash is single-tenant self-DoS (OOS). Any cross-tenant effect is a HARD STOP, not a thing to exploit.
- **Intra-customer noisy-neighbor / bandwidth contention** (efa-acc-inst-types.md: EFA↔ENA share a NIC; NCIs share NIC/GPU on P5/P6/P6e) — documented, intra-customer across the customer's *own* large/metal (single-tenant) instances → self-contention, OOS unless a *shared-across-tenants* NIC is confirmed (not indicated by any example).
- **Generic ENI behavior** (IDOR by `eni-` id, cross-VPC attach mechanics, delete-collateral, IP management) — owned by the ENI-cluster sibling plans; not restated here.
- **Placement-group co-residency / topology oracle** — owned by frag3 plan; referenced only as the precondition for Area 4.
- **Customer-authored** SG/SSH/installer hardening choices → footguns the customer inflicts on themselves. *(Carve-out: the SG and SSH and supply-chain patterns in Areas 2/3/5 are **in scope** precisely because they are **AWS-published, copy-verbatim** walkthrough steps, not customer-originated.)*
- IMDS on these managed hosts; product/feature-parity gaps; Intel-MPI OS-support nuances.

## 8. Null hypotheses / doc gaps (lenses checked, with pages)
- **Lens A (cross-tenant IDOR):** N/A beyond Area 1 — checked efa.md, create-efa.md, detach-efa.md. EFA adds no resource-by-ID API of its own; it is an ENI (defer to using-eni/create-network-interface). No tenant-id-in-body shape.
- **Lens B/C (PassRole / credential vending):** N/A — checked all 10 EFA pages + the CreateNetworkInterface/Attach/RunInstances IAM rows; no role-ARN input, no STS/session-policy, no credential-vending in the EFA path. (RunInstances PassRole for instance profiles is owned by the fleet/RunInstances plans, not EFA-specific.)
- **Lens G (SSRF):** N/A — checked create-efa.md, efa-start*.md, efa-installer-containers.md, efa-working-monitor.md. No field the *service* dereferences server-side; the installer downloads are **customer-host-initiated**, not a service fetch (so they are supply chain = Area 5, not SSRF).
- **Lens H (KMS/encryption-context):** N/A for EFA — no customer-managed key or encryption context in the EFA interface; data-in-transit SRD encryption is not discussed in these pages (doc-gap: whether SRD traffic is encrypted on the wire is unstated — note for Area 4).
- **Lens K (prompt injection):** N/A — the ML libraries (NCCL/NIXL/MPI) are compute transports, not an LLM pipeline the *service* controls; no customer-document→model→action seam in EFA itself.
- **Lens I/J/M/N/T/W/BB/CC/DD/EE/FF:** did not fire — no tagging-as-access-control, OAuth/3P linking, session-id routing, ARN-namespace migration, cross-service secret store, attestation gate, multi-parser request path, upstream-asserted-identity, caching layer, predictable global namespace, or JWT/OIDC token in the EFA surface (checked the full 10-page tree + IAM rows). Re-open if a future EFA control-plane API or a managed EFA cluster service appears.
- **Doc gaps to confirm before investing:** (1) the SRD/EFA AZ-VPC confinement **enforcement mechanism** (Area 4) — physical/addressing vs software; (2) whether **SGs filter SRD payload** at all (Area 7); (3) whether **SRD traffic is encrypted in transit**; (4) detach-time **SRD/QP/MR teardown** semantics (Area 7); (5) whether any EFA-supported instance size is ever **multi-tenant per host** (all documented examples are large/metal → implicitly single-tenant).

---
*Prepared from AWS documentation only, 2026-10-15. All offline pages confirmed byte-identical to their online `.md` twins by the two analysis passes. Downstream hunter: start at Areas 1–2 (settleable with `SimulateCustomPolicy` + a canary cluster, no service-plane risk), hold Area 4 behind a mechanism-confirmation step and the HARD STOP.*
