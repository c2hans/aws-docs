# EFA + NCCL "Get started with EFA and NCCL for ML workloads" — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start-nccl.html` (offline twin `efa-start-nccl.md`, byte-identical to online 2026-10-15, 1094 lines) and its documentation neighborhood — the EFA family (`efa.md`, `efa-start.md`, `efa-verify.md`, `efa-changelog.md`, `efa-working-monitor.md`, `efa-installer-containers.md`), the DLAMI EFA guide (`dlami/.../tutorial-efa-using.html`), `cr-cpg.md`/`placement-groups.md`, `security-group-connection-tracking.md`, `ena-nitro-perf.md`, and the authoritative IAM reference `service-authorization/.../list_ec2.md`.
Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **This is the NCCL/GPU sibling of [`efa-start-attack-research-plan.md`](efa-start-attack-research-plan.md) (the MPI "Get started" page).** The two tutorials share the *identical* EFA-enablement scaffold — the mandatory self-referencing security group, passwordless SSH, the EFA installer, the AMI-bake/terminate steps, and the whole OS-bypass/SRD fabric-isolation question. **This plan does NOT restate those shared areas; it cross-references the MPI plan's Areas A/B/C/E/F and owns ONLY the net-new surface the NCCL variant introduces:** a far larger AWS-authored **supply chain** of unverified / verification-disabled / unpinned third-party kernel-mode software (NVIDIA GPU driver, CUDA, GDRCopy, NCCL, nccl-tests, Fabric Manager, EPEL), and the **GPUDirect RDMA (GDR) GPU-memory data plane** that upgrades the MPI plan's host-RAM "prize" (Area C) to direct cross-instance **GPU HBM** access. Per the MPI plan's own closing note (line 215): *"a future per-sibling plan should cross-ref Areas B/C/D/E here rather than restate them."* This is that plan.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (§5 ordered); look left and right for adjacent bugs.
- **HARD STOP:** the instant any evidence shows an identity/credential/ARN/account/host belonging to AWS's **own service plane** (Nitro card internals, EFA device firmware, the `efa-installer.amazonaws.com` origin, another AWS fleet, GPU memory of an instance you cannot prove you own on both ends), stop, preserve evidence, flag for AWS-Security disclosure. Never attempt RDMA/GDR against memory you cannot prove you own on both ends.
- `iam:SimulateCustomPolicy` / `SimulatePrincipalPolicy` is the safe first oracle for IAM leads (the IAM surface here is identical to MPI Area A — see cross-ref §5.X). Live confirmation only with synthetic canary instances **you own on both ends**, one VPC/AZ you control, torn down after.
- **Third-party-code CVEs are out of scope** (NVIDIA driver, GDRCopy, NCCL, nccl-tests, EPEL are not AWS code). What **is** in scope is the **AWS-authored instruction** to fetch/trust/execute them **unverified, with verification disabled, or unpinned, as root** — that runbook is a copy-verbatim AWS artifact (Lens R/U/D). Keep that line sharp in every finding.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. **Root/ring-0 code execution via the AWS-authored NCCL install runbook.** Show that the copy-verbatim steps instruct the operator to (a) **disable apt GPG signature verification** (`[trusted=yes]`), (b) run an **unverified NVIDIA `.run` driver** as root, (c) build & `dpkg -i`/`rpm -Uvh` an **unverified GDRCopy DKMS** kernel module, and (d) `git clone` **unpinned** nccl-tests — any one of which, if its upstream/transport is compromised, yields ring-0 on the GPU host. **High (AWS-authored artifact).**
2. **Cross-tenant GPUDirect RDMA (GDR) — the GPU-memory prize.** Complete an SRD/RDMA read or write **directly into another instance's GPU HBM** (via `nvidia-peermem`/`efa-nv-peermem` + GDRCopy + `FI_EFA_USE_DEVICE_RDMA=1`) owned by a **different, non-consenting** account — proving the OS-bypass path reaches GPU memory the SG/VPC/AZ model says is unreachable. **Critical.** (Deepens MPI Area C3 for the GPU plane.)
3. **aws-ofi-nccl plugin config / topology-file injection.** Show that NCCL auto-loads a topology/config file from an operator-home path (`NCCL_TOPO_FILE`) or plugin dir that a lower-privileged local actor can pre-plant, steering collective routing or the device-selection path. **Medium if confirmed.**
4. **Verification asymmetry as a defect.** Show the runbook verifies some artifacts (EFA tarball GPG optional; CUDA keyring) but **explicitly disables** verification for others (`[trusted=yes]`) and **omits** it entirely for others (`.run`, GitHub tarballs/clones) — an AWS-owned inconsistency that teaches operators an insecure default. **Low–Medium (Lens U).**

---

## 2. Components, Assets, and Design

**What the NCCL variant adds over the MPI page.** Same EFA device + SRD OS-bypass transport (see MPI plan §2). The NCCL tutorial layers on the **GPU compute + GPU-interconnect stack** and the **aws-ofi-nccl plugin** that bridges NCCL collectives onto Libfabric/EFA:

- **GPU driver + CUDA + cuDNN** — NVIDIA kernel-mode GPU driver (ring-0), CUDA Toolkit 13.x, cuDNN 9. Fetched per-OS from `developer.download.nvidia.com` repos (and, for Amazon Linux, the driver `.run` directly from `us.download.nvidia.com`).
- **NVIDIA Fabric Manager** — a root daemon (`systemctl enable/start nvidia-fabricmanager`) required on NVSwitch (P-series multi-GPU) instances to manage NVLink/NVSwitch fabric; version must match the driver major version.
- **GDRCopy** (`gdrdrv` DKMS kernel module + `libgdrapi`) — a second **out-of-tree kernel module** (ring-0), built from a GitHub release tarball, that enables low-latency CPU↔GPU-memory copies and underpins GPUDirect.
- **NCCL** (`github.com/NVIDIA/nccl` tag `v2.30.4-1`) built from source into `/opt/nccl`.
- **aws-ofi-nccl plugin** (`/opt/amazon/ofi-nccl`, installed by the EFA installer) — the NCCL→Libfabric→EFA shim; it is the component that selects the `efa` provider and auto-sets `NCCL_TOPO_FILE`.
- **nccl-tests** (`github.com/NVIDIA/nccl-tests`, **no tag/branch — floating default HEAD**) — the `all_reduce_perf` benchmark used in Step 8, launched via `mpirun` across the cluster.
- **GPUDirect RDMA data plane** — `FI_EFA_USE_DEVICE_RDMA=1` enables the EFA device to DMA **directly to/from GPU HBM**, bypassing both the guest kernel *and* host memory. This is the sharpest cross-tenant target.

**Accounts / VPCs / ownership, identity, and the OS-bypass fabric** are **identical to the MPI plan §2** (SG-membership admission, no per-tenant crypto identity on the data plane, Nitro = hard stop). Not restated.

**Untrusted-data entry / transform seams (NCCL-specific).**
- (a) **Supply chain, massively widened** — ≥7 distinct fetch-and-execute-as-root sources, several with verification disabled or absent (see §5.N1). Each lands kernel-mode code.
- (b) **GDR memory-registration handles** → remote-peer **GPU** address space (the C/driver/libfabric/peermem parsing layer; MR/QP rkeys now reference pinned GPU pages). Deepens MPI seam (b).
- (c) **aws-ofi-nccl config / topology XML** parsed at NCCL init from an operator-writable path (seam new to this page).

```
  Install (copy-verbatim, as root) — each arrow lands kernel-mode or root code:
    apt  [trusted=yes]  developer.download.nvidia.com  ─▶ CUDA/driver  (GPG DISABLED)
    wget us.download.nvidia.com/.../NVIDIA-*.run        ─▶ sudo sh *.run --dkms  (NO verify) ─▶ ring-0
    wget github.com/NVIDIA/gdrcopy .../v2.5.2.tar.gz    ─▶ build + dpkg/rpm gdrdrv DKMS (NO verify) ─▶ ring-0
    git clone github.com/NVIDIA/nccl -b v2.30.4-1       ─▶ sudo make (tag pin, mutable, no commit/sig)
    git clone github.com/NVIDIA/nccl-tests  (NO PIN)    ─▶ make (floating HEAD)
    dnf install dl.fedoraproject.org/.../epel-release    ─▶ 3rd-party repo (RHEL)
                             │
                             ▼
   GPU host ── nvidia-peermem/efa-nv-peermem + GDRCopy ──╮
                             │ FI_EFA_USE_DEVICE_RDMA=1  │
   EFA device ══ SRD / RDMA ══ GPUDirect (GDR) ═════════▶╫═▶ peer instance GPU HBM
                             (enforcement point: Nitro? — DOC-GAP, see MPI Area B)
                                                          ▼
                        [AWS service plane: Nitro / EFA firmware / SRD fabric] = HARD STOP
```

---

## 3. API / Interface Inventory

The EC2 control-plane API surface (`CreateNetworkInterface`/`RunInstances`/`AttachNetworkInterface`/`ModifyNetworkInterfaceAttribute` with `InterfaceType=efa|efa-only`, console launch wizard, libfabric EFA data plane) is **identical to the MPI plan §3** — including the confirmed **`ec2:InterfaceType` IAM-key gap** (0 hits in `list_ec2.md`). Not restated; see MPI §3 + Area A. The NCCL-specific interfaces are download/build/data-plane, not SigV4 APIs:

| Name | Method | New vs MPI | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `us.download.nvidia.com/.../NVIDIA-*.run` | HTTPS wget | **New** | — | External (download) | NVIDIA GPU driver, run as `sudo sh *.run --dkms` → ring-0 | Yes (download) | anyone | **No GPG/checksum step** in runbook (§5.N1-a) |
| `developer.download.nvidia.com/.../repos` | apt/dnf repo | **New** | — | External | CUDA/driver/cuDNN/Fabric Manager | Yes | anyone | Ubuntu 24.04/26.04 add it with **`[trusted=yes]`** = apt GPG verify disabled (§5.N1-b) |
| `github.com/NVIDIA/gdrcopy …v2.5.2.tar.gz` | HTTPS wget | **New** | — | External | GDRCopy src → `gdrdrv` DKMS kmod (ring-0) | Yes | anyone | Pinned tag, **no checksum/GPG** (§5.N1-c) |
| `github.com/NVIDIA/nccl.git -b v2.30.4-1` | git clone | **New** | — | External | NCCL src → `sudo make` | Yes | anyone | Tag pin (mutable; no commit/sig) (§5.N1-d) |
| `github.com/NVIDIA/nccl-tests.git` | git clone | **New** | — | External | benchmark src → `make` | Yes | anyone | **UNPINNED — floating default HEAD** (§5.N1-d) |
| `dl.fedoraproject.org/.../epel-release-latest-10` | HTTPS dnf | **New** (RHEL) | — | External | EPEL repo enablement | Yes | anyone | 3rd-party repo, `latest` floating (§5.N1-e) |
| EFA installer `--check-signatures` | shell flag | existing | — | — | per-package GPG verify of EFA RPM/DEBs | — | operator | **Optional / off by default** — defer to MPI Area D |
| GPUDirect RDMA (`FI_EFA_USE_DEVICE_RDMA=1`) + `nvidia-peermem` | data plane | **New** | — | Data | EFA DMA directly to/from GPU HBM | No (intra-VPC/AZ) | SG members | The cross-tenant GPU-memory target (§5.N2) |
| `NCCL_TOPO_FILE` auto-load (aws-ofi-nccl) | file read | **New** | — | Local | NCCL reads topology XML from home/plugin path | No | local | Operator-writable path parsed at init (§5.N3) |

Verbatim leads kept as pointers: *"EFA supports only NCCL 2.4.2 and later"*; the Step-8 NCCL_DEBUG line **auto-sets** `NCCL_TOPO_FILE` to `/home/ec2-user/install/plugin/share/aws-ofi-nccl/xml/p4d-24xl-topo.xml` (L908); *"you can also get the latest version by replacing the version number with `latest`"* for the EFA tarball (floating-version option).

---

## 4. Trust-Boundary Map (NCCL-specific rows; shared rows see MPI §4)

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Upstream repo / MITM / tampered mirror | Guest ring-0 (GPU host) | `[trusted=yes]` apt, unverified `.run`, unverified GDRCopy DKMS, unpinned clone — all `sudo` | Any substituted artifact executing as root/ring-0 because the AWS runbook disabled or omitted verification → supply-chain breach (AWS-authored). |
| Customer A instance GPU HBM | Customer B instance GPU HBM | GPUDirect RDMA (GDR) over EFA/SRD | **A GDR read/write completes into GPU memory of a non-consenting account → Critical.** (Deepens MPI Area C.) |
| Local lower-priv process on GPU host | NCCL collective routing / provider select | plant `NCCL_TOPO_FILE` / aws-ofi-nccl config in operator-writable path | NCCL at init reads an attacker-planted topology/config → steered routing or device selection. |
| GDR MR/rkey (app layer) | Remote peer **GPU** address space | pinned-GPU-page memory registration | Reading/writing a GPU memory region the remote never granted → GPU-memory scoping breach (peermem/driver memory-safety). |
| mpirun TCP bootstrap (`--mca btl tcp,self`) | Member nodes over EFA/ENA iface | passwordless SSH + ForwardAgent (MPI Area E) + TCP BTL | Bootstrap/agent hijack from a member node → see MPI Area E (not restated). |
| Any customer surface | **Nitro / EFA firmware / NVSwitch fabric mgr internals** | OS-bypass / GPU fabric | AWS-fleet identity/host = **HARD STOP, disclosure**. |

---

## 5. Recommended Areas of Focus (priority order)

### Area N1 — AWS-authored NCCL supply chain: ring-0 behind disabled/absent/unpinned verification — Lens R / U / D  [HEADLINE; HIGH; AWS-AUTHORED ARTIFACT]
**Background.** The NCCL tutorial is a copy-verbatim runbook that fetches and executes third-party **kernel-mode** software from ≥7 sources. Unlike the EFA tarball (which at least *offers* GPG + optional `--check-signatures`), most of these steps ship with verification **disabled, absent, or floating**. The code lands as root and as out-of-tree kernel modules (`--dkms`, `gdrdrv`), i.e. ring-0 on a GPU host that will later hold cross-tenant GDR memory regions.
**Security Concern (each item an AWS-authored instruction, confirmed in the offline twin):**
- **(N1-a) Unverified NVIDIA driver `.run`, run as root.** `efa-start-nccl.md:186-187` (Amazon Linux 2023): `wget https://us.download.nvidia.com/tesla/580.167.08/NVIDIA-Linux-x86_64-580.167.08.run && sudo sh NVIDIA-Linux-x86_64-580.167.08.run … --dkms --silent`. **No checksum, no GPG, no signature** step anywhere in that path — TLS-origin trust only, then direct ring-0 kmod build. Version is pinned (good) but integrity is never checked.
- **(N1-b) Apt GPG verification EXPLICITLY DISABLED — the sharpest finding.** Ubuntu 26.04 (`:284`) and Ubuntu 24.04 (`:296`): `sudo add-apt-repository -y 'deb [trusted=yes] https://developer.download.nvidia.com/compute/cuda/repos/ubuntu26.04/x86_64 /'`. **`[trusted=yes]` tells apt to accept the repo unconditionally, bypassing GPG signature verification** — even though the very same step *also* installs `cuda-keyring` (so the key is present; the flag deliberately overrides it). **Asymmetry proving it's a defect, not a necessity:** Ubuntu 22.04 (`:308`) and both Debian paths do the *same* install **without** `[trusted=yes]` — so AWS's own sibling steps show the flag is unnecessary. This is an AWS-authored instruction to disable package authentication on a root-privileged kernel-driver install.
- **(N1-c) Unverified GDRCopy → second ring-0 kernel module.** `:561`,`599`,`628`,`669`: `wget https://github.com/NVIDIA/gdrcopy/archive/refs/tags/v2.5.2.tar.gz`, build, then `sudo rpm -Uvh gdrcopy-kmod-…dkms….rpm` / `sudo dpkg -i gdrdrv-dkms_….deb`. **No checksum/GPG** on the tarball; the DKMS package inserts a kernel module.
- **(N1-d) Pinned-but-mutable NCCL + UNPINNED nccl-tests.** `:810` NCCL is `-b v2.30.4-1` (a git **tag** — mutable, re-pointable, no commit hash, no tag-signature verify, cloned under `sudo`), while `:835` **`git clone https://github.com/NVIDIA/nccl-tests.git` has no `-b`/tag → floating default-branch HEAD**: whatever is on the repo's default branch at build time is compiled and run across the cluster via `mpirun`. The pin discipline is inconsistent even within one page.
- **(N1-e) EPEL + CUDA repos.** RHEL 10 (`:476`) pulls `dl.fedoraproject.org/.../epel-release-latest-10.noarch.rpm` (3rd-party repo, `latest` floating); all OSes add NVIDIA CUDA repos via `yum-config-manager --add-repo` / `add-apt-repository`.
**High-level Test Scenarios (falsifiable):**
- **Claim:** The runbook authenticates *some* artifacts and not others, with no stated rationale, teaching an insecure default. → **Oracle:** doc-trace the verification posture of each of the 7 sources (table above): EFA tarball = optional GPG; CUDA apt = keyring **but `[trusted=yes]` overrides it on 2 of 5 OSes**; `.run` = none; GDRCopy = none; nccl = tag-only; nccl-tests = none; EPEL = none. The inconsistency *is* the finding (Lens U). No live action.
- **Claim:** `[trusted=yes]` is removable without breaking the install (proving it's gratuitous). → **Oracle:** on a canary you own, run the Ubuntu 24.04 step **without** `[trusted=yes]` (as AWS already does for 22.04/Debian) and confirm the CUDA repo still installs with keyring-based GPG — demonstrating AWS disabled auth unnecessarily. **Severity Medium–High (AWS-authored auth-disable on a root kmod path).**
- **Claim:** A substituted artifact at any unverified hop executes as root/ring-0. → This is standard supply-chain; **do not** attempt against the real upstreams. The in-scope deliverable is the documentation defect, not a live MITM. Note the kernel-module angle: the EFA docs contain **zero** discussion of module signing / Secure Boot / MOK / lockdown for `efa`, `efa-nv-peermem`, `gdrdrv`, or the NVIDIA driver — cross-ref MPI Area D's kmod-signing doc-gap and the ENA-driver double-free history (`troubleshoot-ena-driver`). Mark **doc-gap — confirm surface**.
**Doc evidence.** Lines cited above (offline twin, byte-identical online 2026-10-15). **Severity-if-true:** **High** for the aggregate (ring-0 install path with authentication disabled/absent in an AWS copy-verbatim runbook); the `[trusted=yes]` item is individually the most defensible report. **Stop condition:** this is a documentation/artifact finding — close once the verification-posture matrix is confirmed; do not MITM real NVIDIA/GitHub endpoints.

### Area N2 — GPUDirect RDMA (GDR): cross-tenant GPU-HBM reach — Lens A / V / F  [CRITICAL IF TRUE; DOC-GAP]
**Background.** `FI_EFA_USE_DEVICE_RDMA=1` (`:891`) enables the EFA device to DMA **directly to/from GPU HBM**, bridged by `nvidia-peermem`/`efa-nv-peermem` and GDRCopy. This is the NCCL path's realization of MPI Area C3 ("GPUDirect RDMA … Critical if the hardware binding is absent"), but the target is now **GPU device memory**, not host RAM — a distinct memory plane with its own registration path (pinned GPU pages, peermem-exported MRs).
**Security Concern.** The isolation question is identical in shape to MPI Area B/C and remains a **doc-gap**: the docs never state *where* SG/tenant filtering of EFA/SRD packets is enforced for the device path, nor whether Nitro binds a queue-pair/MR to the owning ENI/instance in hardware. GDR adds a second untrusted parsing layer (`nvidia-peermem` kernel module exporting GPU memory regions to the RDMA stack) and a second residual-state surface (pinned GPU pages / exported MRs across stop/detach/reattach). If QP↔ENI binding or MR scoping is absent, a crafted rkey could reach a peer's GPU memory.
**High-level Test Scenarios:**
- **Claim (the prize):** A GDR read/write completes into the **GPU memory** of an instance owned by a non-consenting account. → **Oracle:** on two canary GPU instances **you own on both ends**, in one VPC/AZ, establish a NCCL/libfabric GDR connection, then attempt an RDMA op targeting a GPU MR you did **not** have granted. **Severity Critical.** **The moment any evidence implicates Nitro internals, EFA/peermem firmware, or an instance you cannot prove you own → HARD STOP, disclose.**
- **Claim:** SG revoke does not sever a live **GDR** session (per-packet Nitro vs one-time admission). → **Oracle:** same as MPI Area B/F pairing, but over the GDR path; observe whether in-flight GPU RDMA continues after the self-ref SG rule is revoked. **High if confirmed.**
- **Claim:** Detach/reattach of an EFA ENI (or stop/start of a GDR host) leaves **GPU** MR/QP/pinned-page state recoverable by the next attachment (RDMA analogue of volume-reuse-without-zeroing, GPU edition). → **Oracle:** deepen MPI Area F onto the GPU plane. **High if stale GPU memory is readable.**
**Doc evidence.** `:891` (`FI_EFA_USE_DEVICE_RDMA=1`); `efa.md`/`efa-changelog.md` (MR/QP history); MPI plan Areas B/C/F (shared isolation model). **Severity-if-true:** Critical (C1/C3 class); High (revoke/residual). **Preconditions:** canary instances you own on both ends; never target memory you cannot prove you own. **Stop condition:** Nitro/firmware/foreign-instance evidence → disclose.

### Area N3 — aws-ofi-nccl plugin: `NCCL_TOPO_FILE` / config injection — Lens EE / F  [MEDIUM IF CONFIRMED]
**Background.** The Step-8 debug output (`:908`) shows the aws-ofi-nccl plugin **auto-setting** `NCCL_TOPO_FILE` to `/home/ec2-user/install/plugin/share/aws-ofi-nccl/xml/p4d-24xl-topo.xml` — a path **inside the operator's home directory**. NCCL and the plugin consume a topology XML (and other env/config) at init to decide collective routing, device selection, and provider choice.
**Security Concern.** A file the collective library trusts for routing decisions, resolved from an operator-writable (and, depending on AMI build, potentially group/other-writable) path, is a config-injection seam. A lower-privileged local process that can pre-plant or edit the topo XML before `mpirun` runs could steer NCCL's routing/device selection or trip the XML parser. `NCCL_TOPO_FILE` is also an **environment variable** passed verbatim through `mpirun -x` — attacker control of the environment or the file path redirects it.
**High-level Test Scenarios:**
- **Claim:** NCCL loads the topology XML from a path writable by a non-root local user, with no integrity check. → **Oracle:** on a canary, inspect the permissions of the auto-set `NCCL_TOPO_FILE` path and the `/opt/amazon/ofi-nccl` plugin share dir; plant a modified topo XML and observe whether NCCL ingests it (NCCL_DEBUG=INFO echoes the selected file). **Severity Medium** (local, pre-root; higher if it alters cross-node routing on a shared host).
- **Claim:** A malformed topology XML crashes or misroutes the collective (parser robustness). → **Oracle:** feed a deeply-nested/oversized XML; observe hang/crash. Low unless it crosses a tenant boundary.
**Doc evidence.** `:891-908` (mpirun `-x` env list + auto-set `NCCL_TOPO_FILE`). **Severity-if-true:** Medium. **Stop condition:** stays local/single-tenant → Low; close.

### Area N4 — Fabric Manager daemon + Debian modprobe-by-glob — Lens R / F  [LOW]
**Background.** On NVSwitch (P-series multi-GPU) instances the runbook enables a root daemon `nvidia-fabricmanager` whose package **must match the driver major version** (Debian path even greps `/proc/driver/nvidia/version` and substitutes `{{major_version_number}}`). The Debian GPU step also runs a shell one-liner that **finds a kernel module by glob** (`find … -name 'nvidia*uvm*.ko*' | head -1`) and `modprobe`s the discovered name.
**Security Concern.** (a) Fabric Manager is an always-on root daemon on the GPU host — attack surface for local priv-esc / fabric mis-management, but no documented multi-tenant exposure (single instance). (b) The modprobe-by-glob trusts whatever matching `.ko` is first in the modules tree; it requires root already (so low), but is a brittle, injectable pattern if the modules dir is ever writable pre-root. Version-mismatch between driver and Fabric Manager is an availability footgun AWS flags only implicitly.
**High-level Test Scenarios:**
- **Claim:** The Debian `find … head -1 … modprobe` loads an attacker-planted `.ko` if one is present earlier in the glob order. → **Oracle:** requires a writable modules path pre-root; inspect permissions. **Severity Low** (needs root or a writable `/lib/modules` already).
**Doc evidence.** Debian UVM one-liner + Fabric Manager steps (per-OS, offline twin). **Severity-if-true:** Low. Noted for completeness.

### Area X — Shared EFA scaffold (cross-reference only; NOT restated)
The following are **identical** to the MPI plan and owned there — run those areas, do not duplicate:
- **IAM-expressiveness ceiling (`ec2:InterfaceType` has no IAM key).** → MPI **Area A**. Confirmed 0 hits in `list_ec2.md`; applies verbatim to the NCCL launch path.
- **EFA/SRD OS-bypass fabric isolation (where is the firewall enforced?).** → MPI **Area B**. The load-bearing doc-gap; Area N2 is its GPU-plane instance.
- **Cross-tenant RDMA host-RAM reach + QP↔ENI binding + shared-SG path.** → MPI **Area C**. Area N2 extends C3 to GPU HBM.
- **Insecure AWS-authored sample configs:** the EFA-enabled SG (SSH `0.0.0.0/0` + self-ref all-traffic), passwordless SSH (`StrictHostKeyChecking no` + `ForwardAgent yes` for `Host *` + no-passphrase `id_rsa`), IMDSv2-optional, secrets baked into the shared EFA/NCCL AMI (Steps 1, 13, 8, 10). → MPI **Area E** (byte-identical blocks on this page — Step 1 SG, Step 13 passwordless SSH, Step 8 IMDSv1 variant, Step 10 AMI bake). **Note the NCCL AMI bakes *more* secrets** (GPU/CUDA/GDRCopy build artifacts, GitHub clones, the GPG keyring) — same Lens T/EE shape, slightly larger blast radius; still owned under MPI Area E.
- **EFA installer root-RCE behind single-origin TLS; `--check-signatures` optional/off.** → MPI **Area D**. (N1 is the *NCCL-added* supply chain on top of this.)
- **Detach/reattach residual RDMA state & SG-change on live EFA.** → MPI **Area F** (Area N2 adds the GPU-memory residual variant).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Substituted CUDA package accepted because GPG verify is disabled | `[trusted=yes]` apt repo (Ubuntu 24.04/26.04) | apt signature verification — **explicitly disabled by the runbook** (N1-b) |
| Tampered NVIDIA driver `.run` executes as root | `sudo sh NVIDIA-*.run --dkms` | none in runbook (TLS origin only) (N1-a) |
| Tampered GDRCopy tarball → malicious `gdrdrv` kmod | GitHub release tarball → DKMS | none in runbook (N1-c) |
| Floating nccl-tests HEAD compiled & run cluster-wide | `git clone … nccl-tests` (no pin) | none — version pin absent (N1-d) |
| Cross-tenant GPU HBM read/write via GDR | EFA device + nvidia-peermem + `FI_EFA_USE_DEVICE_RDMA=1` | Nitro QP↔ENI binding + MR scoping — **unproven (doc-gap)** (N2) |
| Live GDR session survives SG revoke | self-ref EFA SG | per-packet Nitro enforcement — **unproven** (N2) |
| Planted `NCCL_TOPO_FILE` steers collective routing | aws-ofi-nccl plugin / home-path XML | file integrity/permissions — unstated (N3) |
| Stale GPU MR/pinned pages recovered after detach/reattach | EFA ENI + GPU memory | state zeroing on teardown — unstated (N2/MPI F) |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **CVEs *in* the third-party code itself** — NVIDIA GPU driver, CUDA, cuDNN, GDRCopy, NCCL, nccl-tests, EPEL packages, Fabric Manager. Bugs in those upstreams are the vendors' / not-AWS's. **In scope is only the AWS-authored *instruction* to fetch/trust/execute them unverified/verification-disabled/unpinned as root** (N1).
- **Owner-consented cross-account EFA** via Shared Security Groups / shared subnets / shared placement groups used as designed (becomes in-scope only if joinable without consent, or if unshare fails to sever — MPI Area C2/F; N2 for GPU plane).
- **Single-tenant self-DoS** (version mismatch bricking the local GPU stack, Fabric Manager crash on one's own instance, OOM building NCCL).
- **IMDS on fully-managed hosts** generically — but the runbook's IMDSv1 curl variant (Step 8) and IMDSv2-optional posture are owned under MPI Area E.
- **Customer compute inside the ML workload** (the NCCL app in Step 9 is customer code; prompt-injection / model issues there are not an AWS pipeline — Lens K null, see §8).
- **Nitro card / EFA firmware / NVSwitch-fabric internals** — HARD STOP + disclosure, never a test target.

---

## 8. Null Hypotheses / Doc Gaps (lenses checked, with pages)
- **Lens G (SSRF) — null.** Read `efa-start-nccl.md` end-to-end: every URL is fetched by the *guest* via `wget`/`curl`/`git`/apt, not dereferenced by an AWS service on the customer's behalf. The Step-8 IMDS curl is guest→IMDS (local), not a server-side fetch. N/A (same as MPI).
- **Lens K (prompt injection) — null.** No LLM/agent in the EFA/NCCL enablement path; the ML workload in Step 9 is customer compute, not an AWS transform pipeline. N/A.
- **Lens B/C (PassRole / credential vending) — null for this page.** No role ARN / STS / session-policy construction in NCCL enablement. (Generic EC2 launch PassRole lives in the RunInstances/launch-template plans.) N/A.
- **Lens H (KMS) — null here.** No EFA/NCCL-specific CMK/encryption-context surface (EBS encryption of the AMI is the generic EBS surface, OOS).
- **Lens J / M / FF (OAuth / session / JWT) — N/A.** No web-session/token surface on this device-enablement page.
- **Lens P (proofing/registration) — N/A.** No registration/identity-proofing workflow.
- **Open doc-gaps for the hunter (NCCL-specific additions to MPI §8):**
  1. **GPUDirect RDMA (GDR) GPU-HBM isolation** — is a QP/MR bound to the owning ENI/instance in Nitro hardware for the *device-RDMA-to-GPU* path, or only admission-checked once? (Area N2 — the top NCCL-specific prize.)
  2. **`[trusted=yes]` necessity** — confirm (on a canary) the Ubuntu 24.04/26.04 CUDA install succeeds *without* it (as 22.04/Debian already do), establishing the auth-disable is gratuitous (N1-b).
  3. **Kernel-module signing / Secure Boot / lockdown** for `efa`, `efa-nv-peermem`, `gdrdrv`, and the NVIDIA driver — zero docs; cross-ref MPI Area D + ENA-driver double-free history.
  4. **`NCCL_TOPO_FILE` / aws-ofi-nccl config path permissions** on a freshly-built NCCL AMI (N3).
  5. **GPU MR / pinned-page lifecycle across stop/detach/reattach** — residual GPU memory recoverability (N2 / MPI F, GPU edition).

---

### Appendix — reusable facts confirmed during this build (2026-10-15, offline twin byte-identical to online)
- **`[trusted=yes]` apt flag is used on Ubuntu 26.04 (`:284`) and Ubuntu 24.04 (`:296`) ONLY** — Ubuntu 22.04 (`:308`) and both Debian paths install the identical NVIDIA CUDA repo *without* it. AWS's own sibling steps prove the GPG-disable is unnecessary → cleanest Lens-R/U report on the page.
- **nccl-tests is cloned UNPINNED** (`:835`, no `-b`) while NCCL is tag-pinned (`:810`, `-b v2.30.4-1`, mutable tag), driver pinned (`580.167.08`), GDRCopy pinned (`v2.5.2`), CUDA pinned (`13-0`/`13-3`) — inconsistent pin discipline within one AWS runbook.
- **NVIDIA driver `.run` (`:186-187`) and GDRCopy tarball (`:561` et al.) have NO checksum/GPG step** in the runbook; both land ring-0 (`--dkms`, `gdrdrv` DKMS). EPEL from `dl.fedoraproject.org` on RHEL (`:476`, `latest` floating).
- **GPUDirect RDMA knob = `FI_EFA_USE_DEVICE_RDMA=1`** (`:891`); the aws-ofi-nccl plugin **auto-sets `NCCL_TOPO_FILE`** to an operator-home path (`:908`).
- The **EFA control-plane / IAM surface is identical to the MPI sibling** — `ec2:InterfaceType` is NOT a real IAM key (0 hits `list_ec2.md`); do not re-derive, cite MPI Area A.
- **Structural relationship:** `efa-start.html` (MPI) and `efa-start-nccl.html` share Steps 1–2, 5, 8(IMDS), 10–13 verbatim; NCCL inserts Steps 3 (GPU driver/CUDA/cuDNN), 4 (GDRCopy), 6 (NCCL), 7 (nccl-tests) and the GDR test env. The third sibling `efa-start-nixl.html` (NIXL) is still un-planned — it will reuse this plan's N1 supply-chain shape + MPI's scaffold; a future NIXL plan should cross-ref both.
