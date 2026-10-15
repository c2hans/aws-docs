# EFA + NIXL for inference ("Get started with EFA and NIXL") — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start-nixl.html` (offline twin `efa-start-nixl.md`, 1092 lines, content-identical to online 2026-10-15) and its neighborhood — the sibling getting-started pages `efa-start.md` (MPI) and `efa-start-nccl.md`, the EFA core pages `efa.md`/`create-efa.md`/`detach-efa.md`/`efa-verify.md`/`efa-changelog.md`/`efa-working-monitor.md`, `security-group-rules-reference.md`, and the authoritative IAM reference `service-authorization/.../list_ec2.md`.
Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **This plan is the per-sibling COMPLEMENT to [`efa-start-attack-research-plan.md`](efa-start-attack-research-plan.md) (the MPI getting-started page).** The NIXL page reuses the **identical** AWS-authored copy-verbatim artifacts — the insecure self-referencing + SSH-`0.0.0.0/0` security group (Step 1), the passwordless-SSH footgun block (`StrictHostKeyChecking no` + `ForwardAgent yes` for `Host *` + no-passphrase key, Step 12), the single-origin-TLS EFA installer with optional-off GPG/`--check-signatures` (Step 5), the AMI-secret-baking lifecycle (Steps 9–10), and the whole EFA/SRD OS-bypass fabric with **no `ec2:InterfaceType` IAM key**. Those are **owned by the MPI plan's Areas A–F and are NOT restated here** — this plan cross-references them (§5 pointers) and develops ONLY the surface that exists *because this is the NIXL inference variant*:
> 1. **The ETCD coordination plane** (`etcd --listen-client-urls http://0.0.0.0:2379`, no auth, cleartext) sitting *inside* the allow-all EFA SG — net-new, headline. **(Area N1)**
> 2. **A far broader root-level supply chain** than MPI's single `efa-installer.amazonaws.com` origin: `pip install nixl` (unpinned/unhashed), `sudo git clone … && sudo ninja install` of NIXL/cpprestsdk/etcd-cpp built & installed as **root**, unpinned GitHub tag tarballs (GDRCopy), the NVIDIA `.run` driver, and a locally-built Docker image. **(Area N2)**
> 3. **KV-cache = model inference data on the RDMA fabric** — raises the data-sensitivity (and therefore severity) of the MPI plan's cross-tenant-RDMA prize. **(Area N3)**
> 4. **Docker `--network host` + `-p 2379:2379`** host-namespace exposure. **(Area N4)**

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (§5 is ordered); look left and right for adjacent bugs.
- **HARD STOP:** the instant any evidence shows an identity/credential/ARN/account/host belonging to AWS's **own service plane** (Nitro card internals, the EFA device firmware, the `efa-installer.amazonaws.com` origin, another AWS fleet), stop, preserve evidence, flag for AWS-Security disclosure. Never attempt RDMA against anything you cannot prove you own on **both** ends.
- All ETCD / NIXL / RDMA live tests run **only against synthetic canary instances you own on both ends**, in one VPC/AZ you control, torn down after. ETCD and NIXL are third-party software — a bug *inside* etcd/nixl/vLLM is OOS; the **AWS-authored instruction to run them insecurely inside an allow-all cluster** is in-scope (same framing the MPI plan applies to the unpinned installer).
- `iam:SimulateCustomPolicy` is the safe first oracle for any IAM lead; `DryRunOperation` is caller-IAM-only, **not** an ownership oracle.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. **Unauthenticated cross-member read of the ETCD coordination store.** From a second cluster member (or, worse, a different-account participant in a shared EFA SG), read NIXL handshake/metadata keys out of `http://<peer>:2379` with no credential → recon of RDMA addressing + memory-region descriptors. **Medium–High (High if cross-account).**
2. **ETCD metadata poisoning → KV-cache transfer MITM/redirect.** Write to the unauthenticated ETCD store so a decode (consumer) node resolves a prefill (producer) endpoint/metadata the attacker controls → the KV-cache handoff is redirected, dropped, or served to an attacker endpoint. **High.**
3. **KV-cache memory exfil over RDMA.** Chain ETCD-leaked RDMA addressing (Obj 1) into an actual SRD/RDMA read of a peer's registered KV-cache memory — inference prompts/activations of **another workload** (or, the prize, another account). **Critical if cross-account; High cross-member.**
4. **Root RCE via the NIXL/GDRCopy/ETCD-CPP build-from-source + `pip install` supply chain.** Show the AWS-authored default path installs code built from unpinned upstreams **as root** with no integrity pin, broader than the EFA-installer origin the MPI plan already covers. **High (AWS-authored runbook).**
5. **Confirm the OS-bypass IAM/fabric gaps carry over unchanged** — see MPI plan Areas A/B/C/F (cross-referenced, not re-tested here).

---

## 2. Components, Assets, and Design (delta over the MPI plan)

**What NIXL adds to the EFA picture.** NIXL (NVIDIA Inference Xfer Library, `github.com/ai-dynamo/nixl`, ≥1.0.0) is a user-space transfer library layered **on top of EFA + Libfabric**. Its job in *disaggregated inference* is to move the **KV-cache between a prefill ("producer") node and a decode ("consumer") node**, and between GPU/CPU/storage memory tiers, using the EFA `LIBFABRIC` backend (`--backend LIBFABRIC`, VRAM↔VRAM GPUDirect by default). So the memory now flowing across the SRD fabric is **model inference state**, not opaque HPC buffers.

**New components introduced by this page (not present in the MPI tutorial):**
- **ETCD server** — nixlbench "requires ETCD for coordination between client and server" and uses it for **metadata exchange** between hosts. Launched two ways, both insecure by construction:
  - bare: `etcd --listen-client-urls "http://0.0.0.0:2379" --advertise-client-urls "http://localhost:2379" &`
  - Docker: `docker run -d --name etcd-server -p 2379:2379 -p 2380:2380 quay.io/coreos/etcd:v3.5.18 … --listen-client-urls=http://0.0.0.0:2379 --advertise-client-urls=http://0.0.0.0:2379 --listen-peer-urls=http://0.0.0.0:2380 …`
  - Reachability advertised as `--etcd-endpoints http://{{ETCD_SERVER_IP}}:2379` from **host 2** in the cross-instance test → ETCD is deliberately exposed on the cluster network, not loopback.
  - Health probe is unauthenticated HTTP: `curl -L http://localhost:2379/health` → `{"health":"true"}`.
- **NIXL + nixlbench** — installed via PyPI (`pip install nixl` / `pip3.11 install nixl`) **or** built from source as root (`sudo git clone https://github.com/ai-dynamo/nixl.git && … sudo ninja install`, prefix `/usr/local/nixl`).
- **ETCD CPP API build chain** (source path only) — `sudo dnf install grpc-devel protobuf-devel …`; **cpprestsdk** built from `git clone https://github.com/microsoft/cpprestsdk.git` with `-DWERROR=OFF` and `sudo make install`; **etcd-cpp-apiv3** from `git clone https://github.com/etcd-cpp-apiv3/etcd-cpp-apiv3.git` + `sudo make install`.
- **GDRCopy** (Step 4, GPUDirect RDMA copy) from unpinned GitHub tag `wget …/gdrcopy/archive/refs/tags/v2.5.2.tar.gz`, built and installed via `sudo rpm -Uvh`/`sudo dpkg -i` — this inserts the `gdrdrv` **kernel module**.
- **NVIDIA GPU driver** `.run` executed as root (`sudo sh NVIDIA-Linux-x86_64-580.167.08.run -m kernel-open --no-drm … --dkms --silent`) + CUDA network repo + `nvidia-fabricmanager`.
- **Docker** — installed and run with `--network host --gpus all` for both etcd and nixlbench; a container image built locally from `nixl/benchmark/nixlbench/contrib/build.sh`.
- **vLLM NixlConnector** (Step 14, optional) — `kv_connector:NixlConnector`, `kv_role:kv_both` (symmetric producer+consumer), `kv_buffer_device:cuda`, `backends:["LIBFABRIC"]`, served on port 8200.

**Ownership / trust zones (delta).** All of the above run **inside the customer's own instances**, but they are reachable across the **allow-all self-referencing EFA SG** (Step 1), which is the shared surface: ETCD:2379, SSH:22 (also `0.0.0.0/0`), the vLLM port 8200, and the RDMA fabric are all reachable **member-to-member with no additional network control**, and — via the MPI plan's Area C2 — potentially **cross-account** when the SG is RAM-shared within an Org.

```
   ┌───────────────── EFA cluster (one allow-all self-ref SG; maybe RAM-shared) ──────────────┐
   │  Host 1 (prefill / "producer")                     Host 2 (decode / "consumer")          │
   │  ┌───────────────┐                                 ┌───────────────┐                     │
   │  │ vLLM NixlConn │   KV-cache (VRAM) ═══ SRD/RDMA (EFA LIBFABRIC) ═══▶ KV-cache (VRAM)     │
   │  └───────┬───────┘                                 └───────┬───────┘                     │
   │          │ metadata/handshake (endpoints, MR/rkey hints)   │                             │
   │          ▼                                                  ▼                             │
   │   etcd  http://0.0.0.0:2379  ◀───── unauthenticated, cleartext, reachable by EVERY ───────┤
   │   (no RBAC, no TLS, no client-cert; Docker also -p 2379:2379 w/ --network host)  member   │
   └──────────────────────────────────────────────────────────────────────────────────────────┘
                                   (SSH 22 open 0.0.0.0/0; vLLM 8200 member-reachable)
   install (root): pip install nixl | sudo git clone … && sudo ninja install | wget tag.tar.gz | NVIDIA .run
```

---

## 3. API / Interface Inventory (delta over the MPI plan)

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| ETCD client API `:2379` (`/health`, `/v3/kv/*`) | HTTP (cleartext) | **New to this tutorial** | Yes | Data (intra-cluster) | NIXL coordination / metadata exchange | Within SG only (not Internet) | **ANY SG member — no auth** | Bound `0.0.0.0`; no RBAC/TLS/cert → Area N1 |
| ETCD peer API `:2380` | HTTP | New | Yes | Data | etcd cluster peering | Within SG | No auth | Docker variant exposes both; single-node here |
| nixlbench `--etcd-endpoints http://IP:2379` | lib call | New | — | Data | Benchmark coordination over ETCD | Within SG | SG members | Trusts whatever ETCD returns (poisonable) |
| vLLM NixlConnector handshake (port 8200 + NIXL) | HTTP + NIXL | New (optional) | Yes | Data | KV-cache producer/consumer handshake | Within SG | SG members | `kv_role:kv_both` symmetric → every node is both |
| `pip install nixl` / `pip3.11 install nixl` | PyPI | New | — (install) | External download | Install NIXL as a Python pkg | Yes (download) | anyone | Unpinned, no hash; currently official NVIDIA pkg → Area N2 |
| `sudo git clone github.com/ai-dynamo/nixl` + `sudo ninja install` | HTTPS git | New | — | External | Build+install NIXL from source **as root** | Yes | anyone | Unpinned `main`; built+installed root → Area N2 |
| cpprestsdk / etcd-cpp-apiv3 `git clone` + `sudo make install` | HTTPS git | New | — | External | Build ETCD CPP deps **as root** | Yes | anyone | Unpinned; `-DWERROR=OFF`; root install |
| GDRCopy tag tarball + `sudo rpm -Uvh`/`dpkg -i` | HTTPS | New | — | External | Build+insert `gdrdrv` kmod | Yes | anyone | Unpinned tag; kernel module → Area N2 |
| `docker run … --network host --gpus all -p 2379:2379` | docker | New | Yes | Data | Run etcd/nixlbench containers | — | local | Host net namespace; port publish → Area N4 |

Verbatim doc leads kept as pointers: *"NIXL Benchmark (nixlbench) requires ETCD for coordination between client and server"*; *"Use the IP address of the first host as the ETCD server IP for metadata exchange"*; *"`kv_role` to `kv_both` … the connector can act as both producer and consumer."* Everything in the Step-1 SG, Step-5 installer, Step-12 SSH, Step-9/10 AMI rows is **identical to the MPI page → see the MPI plan's Areas A–F.**

---

## 4. Trust-Boundary Map (delta rows only; see MPI plan for the EFA-fabric / install / SSH rows)

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Any cluster member (or shared-SG cross-acct participant) | Peer's ETCD store `:2379` | self-ref allow-all SG + `0.0.0.0` bind + no auth | Reading/writing a peer's NIXL coordination keys with **no credential** = isolation breach of the metadata plane. |
| Attacker-written ETCD key | A decode/consumer node's NIXL resolution | metadata exchange trust | A consumer node connecting to / transferring KV-cache to an **attacker-chosen** endpoint because it trusted a poisoned ETCD value = handshake MITM. |
| ETCD-leaked RDMA addressing | Peer KV-cache (VRAM) | SRD/RDMA read (EFA) | An RDMA read returning **another workload's KV-cache** (inference prompt/activation bytes) = cross-member memory breach (Critical if cross-account). |
| `pip`/`git`/`.run` upstream origin | Guest root + kernel (gdrdrv/nvidia kmods) | copy-verbatim root install, unpinned | A tampered/typosquatted upstream yielding root/ring-0 exec with no integrity pin catching it = supply-chain breach (AWS-authored runbook). |
| Container (`--network host`) | Host network namespace + published `:2379` | Docker host net + `-p 2379:2379` | A container-reachable or host-reachable ETCD/benchmark surface widening the exposure beyond intended = segmentation breach. |
| Any customer surface | **Nitro / EFA firmware / SRD fabric** | OS-bypass data path | Any AWS-fleet identity/host = **HARD STOP, disclose.** |

---

## 5. Recommended Areas of Focus (priority order)

### Area N1 — ETCD coordination plane: unauthenticated, cleartext, inside the allow-all cluster — Lens V/A/Y/L/M  [HEADLINE, NET-NEW]
**Background.** nixlbench "requires ETCD for coordination between client and server" and for **metadata exchange** between hosts. The AWS-authored commands launch it as `etcd --listen-client-urls "http://0.0.0.0:2379"` (bare) or `docker run … -p 2379:2379 … --listen-client-urls=http://0.0.0.0:2379` (Docker), and the cross-instance test points host 2 at `--etcd-endpoints http://{{ETCD_SERVER_IP}}:2379`. etcd v3.5 ships **authentication disabled by default** (RBAC must be explicitly enabled; no TLS/client-cert flags are present in any command), and the health check is bare HTTP. The transport is therefore **cleartext, unauthenticated, and bound to all interfaces**, while Step 1's self-referencing "all traffic" SG makes TCP 2379 reachable by **every other member of the cluster** — and, via the MPI plan's Area C2 (RAM-shared Shared Security Groups, same Org), potentially by a **different AWS account's** participant.
**Security Concern.** The NIXL metadata exchanged through ETCD is the handshake substrate for the KV-cache transfer: endpoint/host identities, segment types, and connection/addressing hints the consumer uses to reach the producer. An unauthenticated member who can **read** ETCD gets free recon of the fabric (who the peers are, what segments/endpoints exist — the addressing precursor to Area N3's RDMA read); one who can **write/delete** ETCD can poison coordination so a decode node resolves an attacker endpoint (handshake MITM / KV-cache redirect) or so the benchmark/transfer stalls (DoS). None of this requires any EFA/RDMA bug — it is a plain unauthenticated-datastore-on-a-flat-network exposure that the AWS tutorial creates by copy-verbatim instruction.
**High-level Test Scenarios (falsifiable):**
- **Claim:** a second canary instance in the same SG can `curl http://<peer>:2379/health` and then `etcdctl --endpoints http://<peer>:2379 get "" --prefix --keys-only` with **no credential**, dumping NIXL coordination keys. → **Oracle:** keys returned = unauthenticated cross-member read. **Severity Medium** (High if the same read succeeds from a *different-account* participant in a RAM-shared SG — cross-ref MPI Area C2).
- **Claim:** writing/deleting an ETCD key the consumer trusts changes where the KV-cache handshake points. → **Oracle:** on canary prefill+decode you own, run nixlbench/vLLM, overwrite the producer-metadata key via `etcdctl put`, observe the consumer connect to / fail over to the attacker-set value. **Severity High** (coordination-plane MITM/DoS).
- **Claim (transport):** there is no `aws:…`/etcd mechanism in the tutorial enforcing TLS or auth on 2379. → **Oracle:** doc-trace — no `--client-cert-auth`, `--trusted-ca-file`, `--auth-token`, or `https://` anywhere in Steps 7/13; the only "security" boundary is the allow-all SG. Lens Y cleartext note.
- **Enumeration/segmentation (Lens L/M):** ETCD `:2379` reachable from every member means one noisy/compromised member can wipe the store (`etcdctl del "" --prefix`) → cluster-wide coordination DoS; distinct keys/latency form a peer-enumeration oracle.
**Doc evidence.** `efa-start-nixl.md` Step 7 (lines ~620–660 Docker etcd; ~745–760 bare etcd; `/health` probe), Step 13 (lines ~948–1010 cross-host, `--etcd-endpoints http://{{ETCD_SERVER_IP}}:2379`). **Severity-if-true:** **Medium–High** (High on the write/MITM path or any cross-account read). **Preconditions:** two canary instances you own in one SG; never point at a store you don't own. **Stop condition:** if a read returns metadata attributable to another *account*/the AWS fleet → HARD STOP + disclose.

### Area N2 — Root-level NIXL/GDRCopy/ETCD-CPP/driver supply chain (broader than the EFA installer) — Lens R/Q/EE/U  [HIGH, AWS-AUTHORED RUNBOOK]
**Background.** Beyond the single `efa-installer.amazonaws.com` origin the MPI plan's Area D already covers, this page adds a **much larger set of root-executed, integrity-unpinned installs**: `pip install nixl` / `pip3.11 install nixl` (no version pin, no `--require-hashes`); `sudo git clone https://github.com/ai-dynamo/nixl.git` of unpinned `main` followed by `sudo ninja && sudo ninja install`; cpprestsdk and etcd-cpp-apiv3 cloned and `sudo make install`'d as root (cpprestsdk built with `-DWERROR=OFF`, suppressing hardening-relevant warnings); the GDRCopy **kernel module** built from an unpinned GitHub tag tarball and `sudo rpm -Uvh`/`sudo dpkg -i`'d; and the NVIDIA GPU driver `.run` run as root with `--silent`. Several of these insert out-of-tree kernel modules (`gdrdrv`, `nvidia`, plus EFA's `efa`/`efa-nv-peermem`).
**Security Concern.** Every one of these is a copy-verbatim instruction with **no integrity pin** (no pinned commit/digest, no hash, no signature verification mentioned for any of the git/pip/tarball fetches), executed with root. `pip install nixl` currently resolves to the **official NVIDIA `nixl` package** (verified: publisher NVIDIA, maintainers `nv-*`/`dynamo-ops`) — so this is **not** a live typosquat today — but the lead is the *unpinned/unhashed root install* pattern: a future upstream account/registry compromise, a dependency-confusion collision on any transitive dep, or a tag-move on the GitHub sources flows straight to ring-0 on the EFA AMI, which is then **baked into a reusable/shareable AMI** (Steps 9–10) and fanned out to the whole cluster (Step 11). The `-DWERROR=OFF` on a C++ REST SDK installed system-wide as root is a minor hardening regression worth noting.
**High-level Test Scenarios:**
- **Claim:** no step in Steps 4/6/7 pins a commit, digest, or hash for NIXL/GDRCopy/cpprestsdk/etcd-cpp/the NVIDIA driver. → **Oracle (doc-reasoning + local harness, no live AWS):** trace each fetch; confirm `pip install nixl` has no `==version`/`--require-hashes`, the git clones have no `--branch <tag>`/`git checkout <sha>` for NIXL `main`, and the tag tarballs are mutable refs. **Severity High** as an AWS-authored runbook that defaults to unverified root installs.
- **Claim (EE):** the `nixl` PyPI name (and adjacent names a fat-fingered copy could hit) is the land-grab surface. → **Oracle:** confirm current ownership is NVIDIA (done — official); flag that any *future* release or a transitive dep is the actual exposure, not the current name. **Severity:** Informational now, High-if-compromised.
- **Claim (U/kmod):** the page says nothing about module signing / Secure Boot / MOK for `gdrdrv` or the NVIDIA driver. → **Oracle:** doc-gap; cross-ref the MPI plan's Area D kernel-module note and the ENA-driver double-free history. Mark **doc-gap — confirm surface.**
**Doc evidence.** `efa-start-nixl.md` Step 3 (NVIDIA `.run`, lines ~140–165 AL2023 / ~290–320 Ubuntu), Step 4 (GDRCopy tag tarball ~360–415), Step 6 (`pip install nixl` ~530–540; `sudo git clone … sudo ninja install` ~545–580), Step 7 (cpprestsdk/etcd-cpp `git clone` + `sudo make install` ~715–745). **Severity-if-true:** **High** — AWS-authored, copy-verbatim, root + ring-0, baked into a shareable AMI; reportable (Tier 2, `aws-security`), not a customer footgun. **Stop condition:** never tamper with or probe any real upstream origin (NVIDIA/PyPI/GitHub) — settle by doc-reasoning + local analysis only.

### Area N3 — KV-cache as the RDMA payload: inference-data sensitivity upgrade to the cross-tenant-RDMA prize — Lens A/V (+K-adjacent)  [CRITICAL IF CROSS-ACCOUNT; builds on MPI Area C]
**Background.** The MPI plan's Area C owns the EFA/SRD cross-tenant RDMA memory-reach prize (C1 uninvited cross-account, C2 over-shared-SG lateral, C3 Nitro QP↔ENI binding gap). On the NIXL page the memory that EFA moves is explicitly the **KV-cache** between prefill and decode nodes (`kv_buffer_device:cuda`, VRAM↔VRAM GPUDirect via `--backend LIBFABRIC`). That KV-cache is **model inference state** — it encodes the tokens/prompt context and attention state of whatever inference request is in flight.
**Security Concern.** This does not create a *new* RDMA primitive — it changes the **data classification of a successful read**. Where the MPI plan's C-reads return opaque HPC buffers, an equivalent read here returns another workload's (or another tenant's) **prompts/activations** — directly sensitive inference content. It also adds a precondition shortcut: Area N1's ETCD leak supplies the peer addressing/segment metadata that makes a targeted KV-cache read practical rather than blind. The `kv_role:kv_both` symmetric default means **every** node is simultaneously a producer and consumer, maximizing the number of nodes holding readable KV-cache at any moment.
**High-level Test Scenarios:**
- **Claim:** ETCD-leaked metadata (N1) + an RDMA read (MPI Area C mechanism) returns a peer's KV-cache bytes. → **Oracle:** on two canary nodes you own, run a known-plaintext inference, use N1-read metadata to target the peer's registered KV segment, confirm the known plaintext appears. **Severity:** High cross-member; **Critical** if the peer is a different, non-consenting account (then HARD STOP + disclose — this is the service-plane/cross-tenant line).
- **Claim:** `kv_both` symmetry widens the readable-memory window. → **Oracle:** doc-trace Step 14 config; confirm both producer and consumer register KV buffers. Informational enabler.
- **Pointer:** all three C-sub-claims (C1/C2/C3), the Nitro-enforcement question (MPI Area B), and the SG-revoke-doesn't-sever-live-RDMA test (MPI Area B/F) apply **unchanged** — run them per the MPI plan; this area only re-rates the payload.
**Doc evidence.** `efa-start-nixl.md` intro ("KV-cache transfer between prefill and decode nodes … KV-cache movement between various storage layers"), Step 14 (`kv_connector:NixlConnector`, `kv_role:kv_both`, `kv_buffer_device:cuda`, `backends:["LIBFABRIC"]`). **Severity-if-true:** inherits MPI Area C (**Critical** cross-account), with inference-data sensitivity making even the cross-member case clearly impactful. **Preconditions:** canary nodes you own on both ends.

### Area N4 — Docker `--network host` + published `:2379` host-namespace exposure — Lens V/L  [MEDIUM]
**Background.** The Docker test path installs Docker, runs etcd with `-p 2379:2379 -p 2380:2380`, and runs both etcd and nixlbench containers with `--network host --gpus all`. A locally-built image comes from `nixl/benchmark/nixlbench/contrib/build.sh` (unpinned repo).
**Security Concern.** `--network host` drops the container's network namespace isolation so the container shares the host's interfaces directly (relevant to how the etcd `0.0.0.0` bind in Area N1 reaches the EFA ENI), and `-p 2379:2379` publishes the store on the host. `--gpus all` + host networking is a broad grant for a benchmark container built from unpinned upstream (`build.sh`). This mostly **amplifies Area N1's reachability** rather than being a standalone finding, but is worth noting as the mechanism by which the containerized etcd becomes member-reachable.
**High-level Test Scenarios:**
- **Claim:** the containerized etcd is reachable from a peer exactly as the bare one is (host-net + port publish). → **Oracle:** repeat N1's cross-member read against the Docker-launched etcd. Same severity as N1.
- **Claim:** `build.sh` pulls unpinned content into the image. → **Oracle:** doc-trace; cross-ref Area N2 (supply chain). Informational.
**Doc evidence.** `efa-start-nixl.md` Step 7 Docker tab (lines ~600–700), Step 13 Docker tab (~948–990). **Severity-if-true:** **Medium** (segmentation-widening enabler for N1).

### Pointers to the MPI plan (owned there — do NOT re-run here)
- **Area A** — EFA/OS-bypass has **no `ec2:InterfaceType` IAM key** (0 hits in `list_ec2.md`); identical for the NIXL launch path (Steps 2/11 use the same `InterfaceType=EFA with ENA`/`EFA-only`, multi-card `NetworkCardIndex`). → MPI Area A.
- **Area B** — where EFA/SRD SG enforcement actually happens (Nitro vs guest vs one-time admission); SG-revoke-doesn't-sever-live-RDMA. → MPI Area B.
- **Area C** — cross-tenant RDMA memory reach (C1/C2/C3). → MPI Area C (payload re-rated here as N3).
- **Area D** — EFA installer single-origin TLS + optional-off GPG/`--check-signatures` (Step 5 here is byte-identical). → MPI Area D (NIXL *adds* the N2 upstreams).
- **Area E** — insecure AWS-authored SG (`0.0.0.0/0:22` + self-ref all-traffic, Step 1), passwordless-SSH footgun (`StrictHostKeyChecking no` + `ForwardAgent yes` `Host *` + `-N ""` key, Step 12), IMDS, AMI secret-baking (Steps 9–10). **All identical on this page.** → MPI Area E.
- **Area F** — detach/reattach residual MR/QP state; SG change on live EFA. → MPI Area F.

---

## 6. Threat Model Test Objectives (delta)

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Unauthenticated cross-member read of NIXL metadata | ETCD `:2379` | *(none — no auth/TLS; only the allow-all SG)* |
| ETCD write → KV-cache handshake MITM/redirect | ETCD + NIXL/vLLM coordination | *(none — store trusted implicitly)* |
| Cluster-wide coordination DoS (`etcdctl del --prefix`) | ETCD | *(none)* |
| KV-cache (inference prompts/activations) read over RDMA | EFA fabric + NIXL VRAM segments | *(MPI Area C mitigations; account not a documented boundary)* |
| Root/ring-0 RCE via unpinned pip/git/tarball/.run installs | NIXL, GDRCopy, cpprestsdk, etcd-cpp, NVIDIA driver | *(none — no pin/hash/signature on any of them)* |
| Secrets + unverified binaries baked into shared AMI | AMI create (Steps 9–10) | *(only "delete the tarball to reduce size")* |
| Container host-net + published 2379 widening exposure | Docker `--network host`/`-p 2379` | *(none)* |
| (shared with MPI) OS-bypass unforbiddable in IAM; SG not isolation; install origin | see §5 pointers | see MPI plan Areas A/B/D |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **A tenant transferring KV-cache within its own cluster/SG as designed** — intended NIXL behavior; OOS.
- **Owner-consented cross-account EFA via Shared Security Groups / shared subnets / shared placement groups** used as designed — in-scope only if joinable without consent or if unshare fails to sever (MPI Area C2/F).
- **Bugs *inside* etcd, nixl, nixlbench, vLLM, GDRCopy, cpprestsdk, etcd-cpp-apiv3, the NVIDIA driver, or Docker** — third-party software, OOS. **In-scope:** the AWS-authored *instruction* to run them insecurely (etcd `0.0.0.0`/no-auth, unpinned root installs) inside an allow-all cluster.
- **Nitro card internals, EFA device firmware, the SRD fabric substrate, `efa-installer.amazonaws.com`, PyPI/GitHub/NVIDIA upstream origins** — AWS service plane or external origins; **HARD STOP / do not probe.**
- **IMDS on the managed instance, single-tenant self-DoS, product/feature-parity gaps, `ptrace_scope`/CMA intra-instance isolation on the customer's own node, DNS-rebinding against private-only endpoints.**
- **Customer-authored IAM/SGs** (footgun). The in-scope artifacts here are **AWS-authored** copy-verbatim (the SG, SSH config, etcd commands, install runbook) — do not downgrade those.

---

## 8. Null Hypotheses / Doc Gaps (lenses checked, with pages)
- **Lens G (SSRF) — null.** Read the full page; the only server-side-ish fetchers are the *guest's own* `curl`/`wget`/`pip`/`git`, not an AWS service dereferencing a customer-supplied URL. N/A. (The ETCD `--advertise-client-urls` value is operator-set, not attacker-reachable as an SSRF primitive against an AWS service.)
- **Lens K (prompt injection) — adjacent, not primary.** The KV-cache carries LLM state, but the LLM is **customer compute**, not an AWS pipeline; "user steering their own model" is OOS. In-scope only insofar as an *indirect* path (another tenant's poisoned ETCD metadata or RDMA-written KV-cache influencing a victim's inference) is proven — folded into N1/N3 rather than a standalone lens.
- **Lens B/C/H/J/M/FF/P — N/A for this page** (no role-ARN/STS, no CMK/encryption-context specific to NIXL, no OAuth/web-session/JWT, no registration/proofing workflow). Same determinations as the MPI plan §8.
- **Lens Y (transport) — FIRES at N1** (cleartext HTTP ETCD, no TLS enforcement mechanism) rather than null.
- **DOC-GAPS to confirm surface first (not null):**
  1. **Exact contents/schema of the NIXL keys in ETCD** — do they include RDMA memory-region descriptors/rkeys (direct Area N3 enabler) or only endpoint identities? (page says "metadata exchange", no schema). **Load-bearing for N1→N3 chain.**
  2. **Whether vLLM NixlConnector also stands up an unauthenticated side channel on port 8200** across the SG (Step 14). Confirm surface.
  3. **Whether a RAM-shared EFA SG actually permits a different account to reach `:2379`** (combines MPI C2 doc-gap with N1). 
  4. All MPI-plan doc-gaps (Nitro enforcement, QP↔ENI binding, SG-revoke severance, MR/QP lifecycle, kmod signing) carry over unchanged.

---

## Kill chain (compose — rate at the end of the chain)
**ETCD unauth read (N1) → leak peer RDMA addressing/segment metadata → targeted SRD/RDMA read of a peer's KV-cache VRAM (N3, MPI Area C mechanism) → exfil another workload's inference prompts/activations.** Entry point is a trivial unauthenticated `etcdctl get`; the end of the chain is cross-member (High) or cross-account (Critical, HARD STOP) inference-data disclosure. Parallel chain: **ETCD unauth write (N1) → poison producer metadata → decode node transfers KV-cache to attacker endpoint (coordination MITM, High).** Both are enabled by the AWS-authored copy-verbatim `0.0.0.0`/no-auth etcd commands sitting inside the AWS-authored allow-all SG — i.e. two AWS-authored artifacts compose into the exposure.

---

### Appendix — reusable facts confirmed during this build
- **NIXL page = sibling of `efa-start.md`;** reuses the identical insecure SG (Step 1), passwordless-SSH (Step 12), EFA installer (Step 5), AMI-bake lifecycle (Steps 9–10). Offline `efa-start-nixl.md` (1092 lines) content-identical to online 2026-10-15.
- **Net-new vs MPI:** ETCD coordination server (`0.0.0.0:2379`, HTTP, etcd v3.5.18, no RBAC/TLS/cert in any command), `pip install nixl` + `sudo git clone … sudo ninja install` build-from-source, GDRCopy `gdrdrv` kmod from unpinned tag, cpprestsdk/etcd-cpp root builds, NVIDIA `.run`, Docker `--network host -p 2379:2379`, vLLM NixlConnector (`kv_role:kv_both`, `backends:["LIBFABRIC"]`).
- **`nixl` PyPI package is official NVIDIA** (publisher NVIDIA; maintainers `nv-*`/`dynamo-ops`/`dmitry-tokarev`; latest 1.5.0, 2026-09-30) — current name is NOT a squat; the lead is the unpinned/unhashed root-install pattern, not a live typosquat.
- **EFA installer version on this page = `aws-efa-installer-1.50.0`** (MPI plan cited 1.50.0 too); `--check-signatures` still optional/off (added 1.48.0).
- **Supported base AMIs:** AL2023, Ubuntu 24.04, Ubuntu 22.04; EFA supports NIXL ≥1.0.0.
- Cross-refs: [[efa-start-attack-research-plan]] (Areas A–F owned there), ena/SRD cluster (`ena-nitro-perf` for Nitro-enforcement analogy), ENI cluster, and the IAM reference `list_ec2` (`ec2:InterfaceType` = 0 hits). See [[reference-aws-iam-service-auth-ref-url]].
```
