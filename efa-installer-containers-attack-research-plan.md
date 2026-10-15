# EFA — Install the EFA software in a container — Attack Research Plan

Source of leads: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/efa-installer-containers.md` (the target page), cross-read with `efa-changelog.md`, `efa.md`, `create-efa.md`, and the authoritative IAM reference `docs/service-authorization/latest/reference/list_ec2.md`. Online twin `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-installer-containers.md` spot-checked 2026-10-15 — **byte-for-byte identical offline↔online, no drift**. Status: **documentation-derived falsifiable hypotheses only; nothing tested against a live account.** No claim below asserts a confirmed bug.

---

## Relationship to sibling plans (READ FIRST — this plan deliberately defers, does not duplicate)

This is the **page-level deep-dive child of the EFA hub plan** (`efa-attack-research-plan.md`) for the single page `efa-installer-containers.html`. The hub already owns the **general EFA installer supply chain** in its **Area 5** (single-origin TOFU on `efa-installer.amazonaws.com`, optional/absent GPG verification, MD5 checksums, floating `latest`, unpinned `git clone`/`pip install` deps run as root, the `docker run --network host --gpus all` NIXL/ETCD worst-case). It also owns the SRD/RDMA cross-tenant hard-stop (hub Area 4), the self-referencing all-traffic SG + cluster pivot (hub Areas 2–3), `InterfaceType` IAM-unscopability (hub Area 1), and OS-bypass detection blind spots (hub Area 6). **Do not re-run those.** The `efa-start`, `efa-start-nccl`, and `efa-start-nixl` plans own the host-side (non-container) installer walkthroughs and the AMI-bake variant.

**This plan OWNS only the container-execution-context net-new surface** that exists *because the installer runs inside a container*:
1. The container-specific **verification-and-safety-bypass flags** (`--no-verify`, `--skip-kmod`, `--skip-limit-conf`) and the opaque umbrella **`--enable-ngc`** — and the **undocumented NGC flag family** the changelog exposes but the page hides.
2. **Dockerfile-layer baking → container-image / registry supply chain** (distinct from the host-run and AMI-bake variants the siblings own).
3. The **container ↔ host kernel-module trust seam** created by `--skip-kmod` (container trusts the host's ring-0 EFA kmod).
4. **Containerized OS-bypass bypasses the container network namespace / CNI** — an isolation gap specific to RDMA-in-a-container.
5. **`apt-get upgrade -y` / `yum update -y` as Step 1** — a *second* unpinned supply-chain origin (distro mirrors) the host pages don't foreground.
6. The container **memlock/`ulimit` "configure as part of container creation"** documented-but-unenforced step.

Where this plan's leads touch TOFU/optional-verification/`latest` framing, it **cross-references hub Area 5** rather than restating it, and develops only the container-specific delta.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order (§5 is ranked); look left and right for adjacent bugs.
- This page is a **guest-OS / container build-and-runtime procedure**, not an AWS control-plane API. There is **no new EC2 API, no IAM action, and no condition key** on this page (confirmed: the page contains only shell commands). The highest-value leads are therefore **supply-chain / insecure-sample-code (Lens R-code), documented-guarantee-vs-mechanism (Lens U), and container network/kernel isolation (Lens V)** — not cross-tenant IDOR or PassRole (owned elsewhere).
- **Safe-first oracle:** every lead here is settled by *reading the installer script and the shipped image layers* (static) or by running the documented commands in an **isolated canary container** and observing what they install/skip — **no AWS account or live fabric is touched**. Do NOT attempt the SRD/RDMA cross-tenant confirmation here — that is hub Area 4 and sits on the HARD STOP line.
- **HARD STOP:** if any container-runtime test produces evidence that OS-bypass/SRD traffic from the container reaches **another AWS account** or the **Nitro/fabric service plane**, stop, preserve evidence, flag for AWS-Security disclosure. The isolation leads in §5 Area 4 are *confirm-the-mechanism-first* doc-gaps, not things to break against a live fabric.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Ship a root-equivalent backdoor through a container image** — get a tampered/unverified EFA installer or dependency baked into a Dockerfile layer that is then pushed to a registry (ECR/NGC/Docker Hub) and pulled by every cluster node, with the AWS-published steps providing no mandatory verification in the copy-paste path.
2. **Prove the "optional" verification is effectively never run in container builds** — show the GPG sub-step is visually separated from and absent in the install command, so an unattended `docker build` executes `efa_installer.sh` on an unverified tarball by default.
3. **Characterize what `--enable-ngc` actually disables** — show the umbrella flag silently applies `--skip-kmod`/`--skip-limit-conf`/`--no-verify`-equivalent behavior (plus the undocumented `--skip-rdma-core`/`--skip-mpi` family) with no operator-visible per-check accounting, so an operator cannot audit which safety checks were waived.
4. **Map the container↔host kernel trust seam** — confirm `--skip-kmod` means the containerized RDMA stack binds to the *host's* EFA kernel module, so a compromised host kmod (or a host that lies about EFA) is fully trusted by every container, and the container never validates it.
5. **Show containerized OS-bypass evades container network controls** — confirm EFA/SRD traffic from the container ignores the container network namespace / CNI / Kubernetes NetworkPolicy (it goes straight to the Nitro device), so a container believed network-isolated can still speak RDMA to peers.

---

## 2. Components, Assets, and Design

**What this page is.** A **procedure**, run by a human in a container shell *or* baked into a **Dockerfile**, to install the EFA userspace software stack (libfabric + rdma-core + OFI/NCCL plugin + optionally MPI) *inside a container image*. There is no API and no AWS identity involved in the page itself — the commands run with whatever privilege the build/run context grants (root by default in `docker build`).

**The commands (verbatim), with their trust properties:**
| Step | Command | Trust property |
|---|---|---|
| 1 | `apt-get update && apt-get upgrade -y` / `yum update -y` | **Unpinned** pull from the base image's **distro mirrors** — a *second* supply-chain origin, no digest/snapshot pin, `-y` auto-approves. |
| 2 | `curl -O https://efa-installer.amazonaws.com/aws-efa-installer-{{version}}.tar.gz` | Single-origin download (hub Area 5). `curl` **without `-f`/`--fail`** (a 4xx/5xx body is saved as the "tarball"), no TLS/cert pin, `{{version}}` placeholder + "we recommend … the **latest**" → unpinned. |
| 2 (Optional) | `wget …/aws-efa-installer.key && gpg --import … && gpg --verify …tar.gz.sig` | **Marked "(Optional)"**; key + sig + tarball all from the **same origin** (TOFU, hub Area 5); manual visual fingerprint diff; **separated from the install command**. |
| 3 | `tar -xf … && cd aws-efa-installer && ./efa_installer.sh -y --skip-kmod --skip-limit-conf --no-verify` | Root-run installer with **three safety checks disabled**; the command block **does not reference the verification step** → copy-paste path installs unverified. |
| 3 (alt) | `./efa_installer.sh -y --enable-ngc` (v1.49.0+) | **Opaque umbrella** flag — "handles all container-specific configuration automatically." Hides which checks are waived. |
| 4 | `rm -rf /tmp/efa` | Cleanup. |

**Assets / trust anchors.**
- **The EFA installer tarball + GPG key + sig** — same single origin as the host pages (`efa-installer.amazonaws.com`); hub Area 5 owns the origin-TOFU analysis.
- **The base-image distro state** — Step 1's `apt-get upgrade`/`yum update` make the *image contents* a function of whatever the distro mirror serves at build time (non-reproducible).
- **The host's EFA kernel module** — because `--skip-kmod` is mandatory in containers (the page: "The container environment can't modify kernel modules"), the container's userspace RDMA stack is bound to the **host-loaded `efa` kmod** (ring-0, outside the container). The container trusts it implicitly.
- **The resulting container image layer** — the install commands become **cached, shippable image layers** pushed to a registry and pulled fleet-wide.

**Container execution/runtime facts (from efa.md + create-efa.md):**
- EFA = **OS-bypass**: "The Libfabric API bypasses the operating system kernel and communicates directly with the EFA device to put packets on the network" (efa.md L49). In a container this means RDMA/SRD traffic **bypasses the container's network namespace** too — CNI/NetworkPolicy/iptables in the netns never see it.
- RDMA requires **locked (pinned) memory**; the page says `--skip-limit-conf` is used because "You can't set `ulimit` inside a container. Configure this as part of the container creation instead" → the operator must pass `--ulimit memlock=-1` (or equivalent) at `docker run`/pod spec, an **unenforced documented step** and a privilege knob.
- Container needs the **EFA device exposed** (device passthrough / `--network host` per hub Area 5's NIXL example) — collapsing container network isolation back onto the EFA self-referencing all-traffic SG (hub Areas 2–3).

**Undocumented-knob delta (changelog vs page).** `efa-changelog.md` reveals an NGC flag *family* the page never shows:
- The page says `--enable-ngc`; the **changelog (1.49.0) talks about `--build-ngc`** and `--disable-build-ngc` (the latter *removed* in 1.49.0, "Remove auto-detect of build-ngc use case"). **Doc-vs-doc flag-name conflict** → an operator may invoke the wrong/nonexistent flag.
- 1.49.0: "`--skip-mpi` and `--skip-rdma-core` are now **global choices, not restricted to the NGC use case**"; "`--skip-rdma-core` is **no longer implied** when `--build-ngc` is specified" — i.e. the set of checks the umbrella flag waives **changed across versions** and is not reflected on the page.
- 1.48.0 (April 2026): "**Add individual RPM/DEB package signature verification support**" — per-package signature verification **did not exist before 1.48.0**, and per hub Area 5 is **off by default** even now. A container built on `latest` before 1.48.0, or without the per-package flag, cannot verify the individual packages the installer lays down.

**ASCII — the container supply-chain pipeline (the net-new seam this plan owns):**
```
distro mirror ──apt-get upgrade -y──┐
                                     ▼
efa-installer.amazonaws.com ──curl (no --fail, no pin, {{version}}/latest)──► /tmp/efa/*.tar.gz
   (GPG key+sig, SAME origin) ··· (Optional) gpg --verify  [SKIPPED in install cmd / unattended build]
                                     ▼
                       ./efa_installer.sh -y --skip-kmod --skip-limit-conf --no-verify
                                 (or  --enable-ngc  ← opaque; waives ??? )
                                     ▼
                       ┌──── Dockerfile layer (CACHED) ────► REGISTRY (ECR/NGC/DockerHub)
                       │                                         │ pulled fleet-wide
                       ▼                                         ▼
            userspace libfabric/rdma-core ──binds to──► HOST efa kmod (ring-0, OUTSIDE container)
                       │
                       └──OS-bypass SRD──► Nitro device  [bypasses container netns / CNI / NetworkPolicy]
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| CI/CD / `docker build` context running the AWS steps | Root filesystem of every image built from this Dockerfile | Root-run `efa_installer.sh` on an **unverified** tarball (verification is a separate "(Optional)" block, absent from the install command) | A tampered/`latest`-drifted tarball or distro package executes as root and is **baked into a shipped image layer** that fleet nodes pull. |
| Distro package mirror | Container image contents | `apt-get upgrade -y` / `yum update -y` (Step 1, unpinned) | Image contents differ build-to-build / a compromised or MITM'd mirror injects a package; non-reproducible image. |
| Operator's security intent ("verify / don't waive checks") | Actual installer behavior under `--enable-ngc` | Opaque umbrella flag + undocumented `--build-ngc`/`--skip-rdma-core`/`--skip-mpi` family | The flag waives more (or different) checks than the operator believes; no per-check accounting is emitted → auditor cannot tell which safety steps ran. |
| Container userspace RDMA stack (`--skip-kmod`) | **Host** ring-0 `efa` kernel module | Direct device binding; container never loads/validates the kmod | A container trusts and binds to a host-supplied kmod it cannot inspect; a lying/compromised host kmod is fully trusted by every container. |
| Container (believed network-isolated by CNI/NetworkPolicy) | EFA/SRD peers on the fabric | OS-bypass: libfabric → EFA device directly, **skipping the container netns** | SRD/RDMA traffic leaves/enters the container with **no CNI/NetworkPolicy/iptables mediation** → "network-isolated" container still speaks RDMA. |
| Tenant A container (EFA) | **Tenant B** instance on same SRD segment / shared Cluster-PG | SRD frame / RDMA op (hub Area 4) | **(HARD STOP — owned by hub Area 4)** cross-account RDMA read/write. Referenced only; not tested here. |

---

## 4. API / Interface Inventory

**No AWS API, IAM action, or condition key appears on this page.** It is a shell/Dockerfile procedure. The entire control surface is:

| "Interface" | Type | Mutating? | Internet-callable? | Notes |
|---|---|---|---|---|
| `efa_installer.sh` CLI flags | Local script args | Yes (host/image state) | No | `--skip-kmod`, `--skip-limit-conf`, `--no-verify`, `--enable-ngc` (page); `--build-ngc`, `--skip-rdma-core`, `--skip-mpi` (changelog, **not on page**). |
| `curl -O …aws-efa-installer-{{version}}.tar.gz` | HTTPS GET | No | Yes (egress) | No `--fail`, no cert pin, unpinned version. Single origin (hub Area 5). |
| `wget …aws-efa-installer.key` / `.sig` | HTTPS GET | No | Yes (egress) | Same-origin key+sig (TOFU). Optional. |
| `apt-get upgrade -y` / `yum update -y` | Package mgr | Yes (image) | Yes (egress) | Second origin: distro mirrors, unpinned. |

**Console-hidden / parameter-only knob:** the full NGC flag family (`--build-ngc`/`--disable-build-ngc`[removed]/`--skip-rdma-core`/`--skip-mpi`) is accepted by the script but **only `--enable-ngc` is shown on this page** — the §3-of-the-skill "most-permissive value the tool accepts with nothing to warn the operator" shape, applied to safety-check-waiving flags.

---

## 5. Recommended Areas of Focus (ranked)

### Area 1 — [in-scope, HIGHEST] Unattended container build installs an UNVERIFIED installer as root → poisoned image layer shipped fleet-wide (Lens R-code / Lens Y, container delta of hub Area 5)
**Background.** AWS's container procedure separates verification from installation: the GPG check is a **"(Optional)"** block, and the actual install command — `tar -xf … && ./efa_installer.sh -y --skip-kmod --skip-limit-conf --no-verify` — **does not reference the verification output at all**. In a `docker build` (the page's first documented mode: "adding commands to a Dockerfile"), there is **no human to perform the manual fingerprint diff**, so the copy-paste/baked path runs the installer on whatever the download produced.
**Security Concern (container-specific delta over hub Area 5):**
- **Verification is not just optional, it is structurally decoupled from install** — unlike a human at a shell who might run the optional block, an automated image build that copies the documented steps installs unverified by default. The install command would succeed on a substituted tarball.
- **`curl -O` has no `--fail`** → an origin/CDN error page or redirect body is saved as `aws-efa-installer-<ver>.tar.gz`; `tar -xf` on a non-tar fails loudly, but a *substituted valid tar* does not — the failure modes do not include "wrong publisher."
- **`{{version}}`/`latest` unpinned** (hub Area 5) is more damaging in a container than on a host: the image is meant to be an immutable artifact, yet its EFA stack is a function of what `latest` resolved to at build time, with **no digest recorded in the image**.
- **The baked result is a shippable, cached layer** pushed to a registry (ECR/NGC/Docker Hub) and pulled by every node — so a single poisoned build fans out to the whole cluster (chains to hub Areas 2–4 pivot/RDMA once the image runs on EFA hosts).
**High-level Test Scenarios.**
- *Claim:* the documented Dockerfile path installs the EFA stack with **no mandatory integrity check**, so a tampered/`latest`-drifted tarball yields root-equivalent content in every image built from it. → *Oracle (static):* build a canary image using the page's steps verbatim; confirm the build **succeeds without ever invoking `gpg --verify`** and that nothing fails when the tarball's publisher is unknown; confirm no digest/version is pinned in the resulting image. *No AWS account touched.*
- *Claim:* `curl -O` without `--fail` persists a non-200 body as the tarball. → *Oracle:* point the step at a URL returning a 403/redirect; confirm a file named `aws-efa-installer-<ver>.tar.gz` is written.
**Doc evidence:** efa-installer-containers.md Steps 2–3 ("(Optional) Verify…"; install command omits verification). **Severity-if-true:** **High** (root-equivalent content baked and shipped; owner-shared — AWS owns the optional/decoupled-verification framing and the no-`--fail` curl, the customer owns choosing to pin/verify). **Stop:** once the no-verification default is confirmed statically; do not pursue the live-fabric chain here.

### Area 2 — [in-scope] `--enable-ngc` is an opaque umbrella that waives an undocumented, version-varying set of safety checks (Lens U documented-guarantee-vs-mechanism; Lens R-code)
**Background.** For v1.49.0+ the page offers `./efa_installer.sh -y --enable-ngc` as a one-flag replacement for `--skip-kmod --skip-limit-conf --no-verify`, stating it "**handles all container-specific configuration automatically**." The page gives **no enumeration** of what that entails. The changelog reveals the surrounding flag family and that its behavior has *changed across versions*.
**Security Concern.**
- **No per-check accounting:** an operator or auditor cannot tell from the page which safety checks `--enable-ngc` waived (kmod? limits? device detection? rdma-core? mpi?). "Automatically" is prose, not a mechanism — the Lens-U gap: the guarantee ("handles configuration") is not traceable to an inspectable behavior.
- **Doc-vs-doc flag-name conflict:** the page says `--enable-ngc`; `efa-changelog.md` (1.49.0) describes `--build-ngc` / `--disable-build-ngc` (removed) and global `--skip-rdma-core`/`--skip-mpi`. An operator copying from release notes vs the UG may invoke a **nonexistent or wrong flag**, silently getting a different (possibly full/none) install. "Full install is avoided in all NGC install use cases" (changelog) — i.e. the flag changes *what packages land*, including possibly skipping `rdma-core` depending on version/other flags.
- **Behavior drift across versions** means a pinned-to-`latest` Dockerfile silently changes which checks run when the installer version rolls — an integrity/compliance regression invisible in the Dockerfile text.
**High-level Test Scenarios.**
- *Claim:* `--enable-ngc` applies the three documented skips **plus** undocumented `--skip-rdma-core`/`--skip-mpi`-class behavior, with no stdout accounting of what was waived. → *Oracle (static/canary):* run `./efa_installer.sh -y --enable-ngc` in an isolated container with `--help` and verbose/dry output captured; diff the installed package set against a plain `-y` install and against the explicit three-flag form; record which checks were silently skipped. *No AWS account touched.*
- *Claim:* the UG `--enable-ngc` and changelog `--build-ngc` are not the same spelling → an operator can invoke a flag the installer rejects/ignores. → *Oracle:* grep `efa_installer.sh` for both flag strings; confirm which the current installer accepts.
**Doc evidence:** efa-installer-containers.md Note ("`--enable-ngc` … handles all container-specific configuration automatically"); efa-changelog.md 1.49.0 (`--build-ngc`, `--disable-build-ngc` removed, `--skip-rdma-core` no longer implied, `--skip-mpi`/`--skip-rdma-core` now global), 1.48.0 ("individual RPM/DEB package signature verification support" added — i.e. absent before). **Severity-if-true:** **Medium** (operator cannot audit waived safety checks; AWS-owned doc/behavior gap — Tier-2 reportable as an AWS-authored procedure that hides which integrity checks ran). **Stop:** once the waived-check set and the flag-name conflict are characterized from the script + docs.

### Area 3 — [in-scope, lower] `--skip-kmod` creates a container→host kernel-module trust seam; `--no-verify`/`--skip-limit-conf` remove the only local sanity checks (Lens V / Lens U)
**Background.** The page mandates `--skip-kmod` ("The container environment can't modify kernel modules") and `--no-verify` ("device detection uses `lspci`, which doesn't work in a containerized environment"). So the container's userspace RDMA stack (libfabric/rdma-core) is installed **without loading or validating any kernel module and without confirming an EFA device is present** — it binds at runtime to whatever **host-loaded `efa` kmod** (ring-0) and device the host exposes.
**Security Concern.**
- **Implicit trust of the host kmod:** the container never loads, versions, or validates the EFA kernel module — it is the host's. A host whose `efa` kmod is compromised, downgraded, or lying (e.g. a malicious/mislabeled node in a shared cluster) is fully trusted by every container that `--skip-kmod`-installed. The container has **no documented mechanism to attest the kmod it will use**. (Changelog corroborates kmod fragility historically: v1.9.3 "Fix `--skip-kmod` installation mode to **actually work**.")
- **`--no-verify` removes the only "am I really on EFA?" check** → a container built for EFA runs identically on a non-EFA host, silently falling back to a different transport (efa.md notes Windows/non-EFA fallback to plain ENA) — an integrity/assumption gap for workloads that *believe* they got OS-bypass isolation.
- **`--skip-limit-conf` + "configure `ulimit` as part of container creation"** pushes the **memlock** (pinned-memory) limit to the run context (`--ulimit memlock=-1`), an **unenforced documented step**: forget it and RDMA registration fails (self-DoS, OOS); set it wide and you grant the container broad locked-memory capability (resource/isolation knob). The page states the requirement but nothing enforces it.
**High-level Test Scenarios.**
- *Claim:* a `--skip-kmod` container binds to the host `efa` kmod with no validation. → *Oracle (canary):* install per the page in a container, then inspect at runtime which kernel module/device the libfabric EFA provider opens (`fi_info -p efa`, `/sys/class/infiniband`, `/dev/infiniband`); confirm it is host-provided and unversioned by the container. *Stays in-guest; no fabric traffic.*
- *Claim:* the memlock step is unenforced. → *Oracle:* run the image without `--ulimit memlock`; confirm RDMA memory registration fails rather than being blocked at build with a clear error.
**Doc evidence:** efa-installer-containers.md Step 3 flag descriptions; efa.md L49 (OS-bypass direct-to-device); efa-changelog.md v1.9.3 (`--skip-kmod` historical bug). **Severity-if-true:** **Low–Medium** (host-kmod trust is largely an operator/host-security concern = shared-responsibility; raises severity as an enabler for the hub Area 4 fabric questions). **Stop:** at characterizing the trust seam; do NOT probe cross-tenant RDMA (hub Area 4 / HARD STOP).

### Area 4 — [in-scope, lower] Containerized OS-bypass bypasses the container network namespace / CNI (Lens V, container delta of hub Area 4)
**Background.** EFA is OS-bypass: libfabric talks "**directly** with the EFA device" (efa.md L49). Inside a container that device is reached via passthrough / `--network host`, so SRD/RDMA traffic **never traverses the container's network namespace** — CNI plugins, Kubernetes `NetworkPolicy`, and in-netns `iptables` do not see or constrain it.
**Security Concern.** Operators commonly assume container/pod network policy confines a workload's traffic. For EFA that assumption is **false by construction**: a container believed network-isolated can still establish SRD/RDMA sessions to any reachable peer (subject only to the EFA self-referencing all-traffic SG, hub Areas 2–3, and the physical SRD segment). This is the container-specific framing of hub Area 4's isolation question — the *enforcement layer customers would reach for (CNI/NetworkPolicy) is simply absent on this path*. The hub owns the cross-tenant RDMA confirmation; this plan owns the **"CNI/NetworkPolicy does not apply to EFA" documentation/enforcement gap**.
**High-level Test Scenarios.**
- *Claim:* a `NetworkPolicy`/CNI rule that would block TCP/IP egress does **not** block EFA/SRD egress from the same pod. → *Oracle (single-account canary cluster):* apply a deny-all `NetworkPolicy`, confirm TCP is blocked, then confirm an EFA `fi_pingpong`/libfabric session to an in-account peer still completes. **Keep strictly intra-account**; the instant any peer is outside the account/VPC → **HARD STOP** (hub Area 4).
**Doc evidence:** efa.md L49 (direct-to-device OS-bypass), L506–507 ("EFA traffic can't cross AZ/VPC … is not routable" — the *only* stated confinement, and it is physical, not CNI); efa-installer-containers.md (container context). **Severity-if-true:** **Medium** (isolation-assumption gap; the cross-tenant escalation is hub Area 4's HARD STOP, not re-tested here). **Stop:** at confirming CNI/NetworkPolicy non-application intra-account.

### Area 5 — [in-scope, lower] `apt-get upgrade -y` / `yum update -y` as Step 1 = a second unpinned supply-chain origin (Lens R-code)
**Background.** The procedure's first step mutates the base image from the **distro mirrors** with `-y` auto-approval and no snapshot/digest pin.
**Security Concern.** Distinct origin from `efa-installer.amazonaws.com` (hub Area 5): the image's integrity now also depends on the distro mirror and the base image's trust config at build time. `apt-get upgrade -y` can pull a compromised or simply newer-and-incompatible package, and makes the image **non-reproducible** (same Dockerfile, different contents over time). On RHEL-based images `yum update -y` similarly auto-trusts repo GPG config inherited from the base image. This is a classic insecure-sample-pattern in AWS-authored copy-verbatim steps.
**High-level Test Scenarios.**
- *Claim:* Step 1 makes the image a function of mirror state with no pin. → *Oracle (static):* build the image twice at different times; diff installed package versions; confirm no `--no-upgrade`/snapshot/digest pin is documented.
**Doc evidence:** efa-installer-containers.md Step 1. **Severity-if-true:** **Low** (reproducibility + second supply-chain origin; owner-shared). **Stop:** once the unpinned second origin is documented.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Root-equivalent backdoor shipped in a container image via unverified installer | `efa_installer.sh` on an unverified tarball, baked to a layer | GPG sig verification — **"(Optional)", decoupled from the install command, same-origin TOFU, `latest` unpinned, `curl` no `--fail`** |
| Operator cannot audit which safety checks ran | `--enable-ngc` umbrella + undocumented NGC flag family | "handles all container-specific configuration automatically" — **prose only; waived-check set undocumented & version-varying; UG vs changelog flag-name conflict** |
| Container trusts a host kernel module it cannot inspect | `--skip-kmod` + host `efa` kmod (ring-0) | None documented — container never loads/validates/attests the kmod |
| "Network-isolated" container still speaks RDMA | OS-bypass path vs CNI/NetworkPolicy | Only physical "can't cross AZ/VPC / not routable" (efa.md) — **CNI/NetworkPolicy do not apply to EFA traffic** |
| Unenforced memlock/`ulimit` container-creation step | `--skip-limit-conf` note | "Configure this as part of the container creation instead" — **documented, not enforced** |
| Non-reproducible image / second supply origin | `apt-get upgrade -y` / `yum update -y` | None — unpinned, `-y` auto-approve |
| Cross-tenant RDMA read/write | SRD fabric (hub Area 4) | **Owned by hub plan; HARD STOP — not tested here** |

---

## 7. Out-of-Scope Risk Categories (state them)
- **The SRD/RDMA cross-tenant fabric boundary** and the **InterfaceType IAM-unscopability**, **self-referencing SG pivot**, and **OS-bypass detection blind spots** — owned by the **hub plan** (Areas 1–4, 6) and the ENI/ENA/placement-group cluster plans. Not re-tested here.
- **Single-tenant self-DoS** — forgetting `--ulimit memlock` so your own RDMA fails, or an incompatible `apt-get upgrade` breaking your own build. Documented here as an enabler/footgun, not a reportable boundary breach.
- **Customer-authored Dockerfile least-privilege choices** — a customer running the container `--privileged` or with over-broad device passthrough is a customer footgun (out of scope) *except* where AWS's published steps themselves induce it (`--network host`, `--ulimit memlock=-1` are AWS-suggested in the NIXL worst-case = hub Area 5).
- **IMDS / instance-profile exposure to the container** — generic container-on-EC2 metadata concern, not specific to this page.
- **Bugs in the third-party NGC base images / NVIDIA toolkit** — the container is customer compute; in-scope only via the AWS-authored install steps.

## 8. Null hypotheses / doc gaps (lenses checked, with pages read)
- **Lens A / X (cross-tenant IDOR, twin-action authz):** N/A — this page has **no AWS API, no resource ID, no authz decision**. It is a local shell/Dockerfile procedure (read full page). Re-open only if a managed "EFA container" control-plane service appears.
- **Lens B / C / E (PassRole / credential-vending / RBAC privesc):** N/A — no role ARN, no `AssumeRole`, no IAM principal on this page (read full page). The container's AWS identity (if any) is the host instance profile — generic, owned elsewhere.
- **Lens G (SSRF):** N/A — the `curl`/`wget`/`apt`/`yum` fetches are **customer-container-initiated**, not a *service* dereference of a customer-supplied field; they are **supply chain (Areas 1/5)**, not SSRF. (Checked: no field the AWS service fetches on the customer's behalf.)
- **Lens H / W (KMS / attestation):** N/A — no customer-managed key, encryption context, or PCR/attestation gate anywhere in the container install (read page + efa.md). Doc-gap carried from hub: whether SRD traffic is encrypted on the wire is unstated.
- **Lens I / S (tagging / condition-key semantics):** N/A — no IAM policy, tag, or condition key on this page (confirmed; the whole EFA IAM surface = `InterfaceType` unscopability, owned by hub Area 1).
- **Lens K (prompt injection):** N/A — the installed libraries (libfabric/NCCL/MPI) are compute transports, not an LLM pipeline the service controls.
- **Lens L (resource exhaustion):** fires only as **self-DoS** (missing memlock) → documented under Area 3, rated out-of-scope severity.
- **Lens Q (file/upload parsing):** partial — the tarball is a parsed archive, but it is a *supply-chain download* (Area 1), not a service-side upload-parse. No image/SVG/doc upload surface on this page.
- **Lens EE (predictable-name land-grab):** considered — the image's registry name/tag and `latest` tag are a predictable namespace, but **registry name-squatting is a customer/registry concern**, not an AWS-authored resolution step on this page; the AWS-side `latest` installer tag is the hub Area 5 floating-version issue. Marked a thin pointer, not a new lead.
- **Lens U (doc-vs-enforcement):** **FIRES** — Area 2 (`--enable-ngc` prose vs mechanism; UG-vs-changelog flag conflict) and Area 3 (`--no-verify` removes the EFA-presence check; memlock documented-not-enforced).
- **Lens V (network/kernel isolation):** **FIRES** — Area 3 (container→host kmod trust) and Area 4 (OS-bypass vs CNI/NetworkPolicy).
- **Lens R-code / Y (insecure sample code / transport-TOFU):** **FIRES** — Areas 1 & 5 (container delta of hub Area 5: decoupled-optional verification in unattended builds, `curl` no `--fail`, second distro origin, baked shippable layer).
- **Lens D / F / J / M / N / O / T / BB / CC / DD / FF:** did not fire — no data/control-plane split, translation layer, OAuth/3P link, session-id routing, ARN-namespace migration, audit-log API, cross-service secret store, multi-parser request path, upstream-asserted identity, caching layer, or JWT/OIDC token on this page (checked efa-installer-containers.md end-to-end + efa.md/create-efa.md/efa-changelog.md context). **Lens O** detection evasion for OS-bypass is owned by hub Area 6.
- **Carried doc-gaps for the hunter:** (1) exact set of checks `--enable-ngc` waives per installer version (settle by reading `efa_installer.sh`); (2) whether `--enable-ngc` (UG) and `--build-ngc` (changelog) are aliases, one deprecated, or a doc error; (3) whether the container validates the host kmod version/signature at libfabric init (Area 3); (4) whether per-package RPM/DEB signature verification (added 1.48.0) is on or off under `--enable-ngc`.
