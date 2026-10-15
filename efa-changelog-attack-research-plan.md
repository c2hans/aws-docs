# EFA Release Notes / Changelog — Attack Research Plan
Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-changelog.html` (offline twin `docs/AWSEC2/latest/UserGuide/efa-changelog.md`, 93 lines, **byte-identical offline↔online verified 2026-10-15**). Status: documentation-derived hypotheses only; nothing tested against a live account.

> **This page is a page-level CHILD of the EFA hub** (`efa-attack-research-plan.md`). It is **NULL-DOMINANT on the cloud attack surface**: the entire page is a single version-history TABLE (version | changes | release date) for the `efa_installer.sh` software bundle. It contains **ZERO** AWS API, IAM action, condition key, ARN, resource identifier, network interface, credential, token, URL-the-service-dereferences, or tenant-id. Lenses A/B/C/D/E/G/H/I/J/K/M/N/P/Q/T/V/W/AA/BB/CC/DD/EE/FF are **N/A for this page** (pages named in §8). The page's security value is **not a new surface** — it is the **authoritative dependency-version & bug-fix-history catalog** that (a) *corroborates and version-targets* three existing sibling hypotheses, and (b) carries a thin net-new **Lens U / Lens N "patch-currency is unenforced + old vulnerable installer versions remain installable + per-package signature verification was added late"** surface. Firing lenses: **F (corroboration/oracle), R/Q/Y (supply-chain version ground truth), U (deprecation vs enforcement), N (version-boundary events).**

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right.
- **Read this plan as the "version ground-truth sheet" for the whole EFA cluster.** When any sibling plan says "unpinned deps" / "`latest`" / "known-buggy parser" / "signature verification", this page tells the hunter *which concrete version* ships what, and *when* a fix or a control entered the product. Use it to pin the exact installer version a given data-path bug is present/absent in before investing in a live test.
- **HARD STOP (inherited from the hub):** the moment evidence shows EFA/SRD traffic, an RDMA memory region, a queue-pair/Address-Handle, or any credential/ARN reaching **another AWS account** or **AWS's own Nitro/fabric service plane**, stop, preserve evidence, flag for AWS-Security disclosure. The memory-safety bug-fix history catalogued here (Area 1) sits adjacent to that line **by corroboration only** — a guest-side libfabric/rdma-core crash is single-tenant self-DoS (OOS); any cross-tenant effect is the hub's Area 4 HARD STOP, **not** something to drive from this page.

## 1. Pentest Objectives (boundary-breach goals this page *supports*, not owns)
This page produces **no standalone breach objective.** It supplies evidence/version-targeting for objectives owned elsewhere:
1. **(Supports hub Area 4 / HARD STOP)** Version-target the EFA data-path parser (libfabric provider, `rdma-core`, efa kernel driver) memory-safety / QP-number-confusion bug class — determine *which installer versions* carry an un-fixed UAF / double-free / ABA / missing-QP-verification defect in the QP/CQ/AH/MR code paths, so a downstream parser-fuzzing / isolation test is aimed at the right binary. (Lens F.)
2. **(Supports hub Area 5 + efa-start Area D + containers A1/A2)** Establish the **authoritative dependency version map** and the **date per-package signature verification entered the product** (1.48.0), to settle the "optional-off GPG / unpinned deps / `latest`" supply-chain concern. (Lens R/Q/Y.)
3. **(Net-new, this page owns)** Show that **patch currency is advisory-only** and **superseded/EOL installer versions bundling known-buggy components remain installable**, enabling a *pin-to-old-vulnerable-version* posture that no documented EC2/EFA control prevents. (Lens U/N.)

## 2. Components, Assets, and Design
- **Customer-facing interface described by the page:** none. The page documents the *contents* of the `efa_installer.sh` tarball (an AWS-published, customer-host-run shell installer — the install mechanism itself is owned by hub Area 5, efa-start Area D, and `efa-installer-containers`). This page is pure release metadata.
- **The bundled software components the changelog tracks** (= the real attack surface, owned by the hub and siblings; this page is the version oracle for all of them):
  - `libfabric` (AWS fork, `*amzn*` tags) — the userspace OFI provider / EFA RDM + efa-direct data path. **The parser/transport that touches peer-supplied packets.**
  - `efa` kernel driver (`amzn-drivers`, `efa_linux_*`) — the in-guest ring-0 Nitro-device driver.
  - `efa-nv-peermem` (`efa_nv_peermem_linux_*`) — GPUDirect RDMA peer-memory kernel module (DKMS).
  - `rdma-core` — userspace verbs / QP / CQ / AH management.
  - `aws-ofi-nccl` / `libnccl-ofi` — NCCL↔Libfabric shim (GPU collectives).
  - `Open MPI` (`*amzn*`), `PRRTE`/`prrte-aws`, `OpenPMIx`/`pmix-aws`, Intel MPI 2019 (first supported 1.4.0).
  - `efa-config`, `efa-profile` — config/tuning packages (huge-page reservation, collectives decision files).
  - Utility scripts: `efa_test.sh` (post-install `fi_pingpong`), distributed at `/opt/amazon/efa/bin` since 1.36.0.
- **Installer flags whose semantics the changelog reveals** (cross-ref containers A2/A3): `--enable-gdr`/`-g` (made a **no-op** in 1.14.0; GDR default-on in driver), `--minimal` (1.8.0, kmod+rdma-core only), `--skip-kmod` ("fixed to actually work" 1.9.3 — i.e. previously silently broken), `--build-ngc`/`--disable-build-ngc` (the latter *removed* in 1.49.0), `--skip-rdma-core`, `--skip-mpi` (both became **global** choices in 1.49.0, previously NGC-only).
- **Identity / accounts / network:** none on this page.
- **Assets at stake (via the components, not the page):** peer-reachable RDMA memory regions, QP/CQ/AH state, GPU HBM (via peermem), the shared SRD fabric — all owned by hub Area 4 and efa-start Area C.

No pipeline diagram applies — this is a flat metadata table.

## 3. Trust-Boundary Map
The page itself crosses **no** trust boundary. The boundaries its *contents* bear on (all owned elsewhere; listed so the hunter can route evidence):

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle | Owner |
|---|---|---|---|---|
| Peer instance (any tenant) on SRD fabric | Local instance libfabric/rdma-core/efa-driver QP·CQ·AH·MR parser | Peer-supplied SRD/RDMA descriptors, CQEs, packet entries | **(HARD STOP)** cross-tenant memory read/write or device-side effect; guest-only crash = self-DoS (OOS). *This page supplies the version→bug map.* | **hub Area 4** |
| AWS software origin | Customer host (install time) | `efa_installer.sh` TOFU download + bundled deps | Tampered/old/unpinned component executes as root; **sig-verify absent < 1.48.0** | **hub Area 5 / efa-start D / containers A1-A2** |
| Operator intent ("keep current / patched") | Actual installed version | No EC2/EFA control forces patch currency; old versions remain fetchable | A fleet silently running a superseded installer with un-fixed data-path bugs | **this page — Area 3** |

## 4. API / Interface Inventory
**None.** No SDK API, console route, non-SDK endpoint, or control-plane action appears on this page. (The EFA control-plane actions — `CreateNetworkInterface --interface-type efa`, `AttachNetworkInterface`, `RunInstances`, etc. — are inventoried by the hub §4 and `create-efa`.) Record as an explicit null: there is nothing here to put in the AWS column table.

## 5. Recommended Areas of Focus

### Area 1 — [HEADLINE / corroboration + version-targeting oracle] The data-path memory-safety & QP-confusion bug-fix history (Lens F → feeds hub Area 4 HARD STOP)
**Background.** The changelog records, version by version, the fixes AWS landed in the exact code paths that any EFA tenant-isolation guarantee depends on. The dense entries:
- **1.48.0 (libfabric 2.4.0amzn3.0):** "Fix **use-after-free** bugs in DC packet completion, CQ drain, AH unit test, and MR logging"; "Fix **race conditions** in `efa_rdm_ep_get_peer` and QP locking"; "Fix **uninitialized descriptor arrays causing segfault** with `FI_EFA_ENABLE_SHM_TRANSFER=0`"; "Fix **memory leaks** in fi_info, err_buf, EFA device destruction"; "Add **null check for base_ep in CQ polling to handle destroyed QPs**"; "Set qp->base_ep in efa_qp_create and return error if efa_mr_reg_ibv_mr returns NULL"; "**Move QP table from domain to device with device-level locking**"; "**Add QP generation to data path direct request ID and verify QP number on CQE**"; "Convert MR registration counters to **atomic** operations".
- **1.47.0:** libfabric "Add **packet entry generation counter to prevent ABA problem**"; "Fix **double-free** in eager/mulreq/longread RTM packet processing"; **rdma-core 61.0** "**Verify QP number on CQE processes**"; **efa driver 3.0.0** "**Check for QP number correctness on completion poll**".
- **1.45.0 (libfabric 2.3.1amzn2.0):** "Fix the **race condition** in cntr progress"; "Handles RMA completion correctly for **removed peers**"; "Evict AH entries from implicit AV when AH limit is reached".
- **1.44.0 / earlier:** QP/CQ thread-domain binding, "Fix **CQ poll after QP destroy**".

**Security Concern.** Two of these are **isolation-relevant, not merely stability fixes**: *QP-number verification on the completion queue entry (CQE)* and the *ABA-prevention generation counter* were **added** (1.44.0→1.48.0). That an explicit "verify the QP number on completion" check had to be introduced means there was a product window in which a completion could be processed **without confirming it belonged to the expected queue pair** — precisely the mechanism the hub's Area 4 cross-tenant-RDMA HARD-STOP hypothesis turns on (a receiver validating a peer's QP/AH). The UAF / double-free / use-after-destroy / "removed peers" fixes cluster in the peer-facing RTM-packet, CQ-drain, AH, and MR paths — the code that parses attacker-influenceable wire input.

**High-level Test Scenarios.**
- *Claim:* an installer version **before** the fix that introduced QP-number-on-CQE verification processes completions without binding them to the owning QP → *Oracle (version-targeting, doc-first):* use this table to pin the exact installer version in use; map it to the libfabric/`rdma-core`/driver versions; cross-check the upstream fix commits. Only if the hub's Area-4 mechanism-confirmation step establishes a cross-tenant path does a live test become warranted — **and a cross-account/cross-VPC completion is an immediate HARD STOP.**
- *Claim:* the UAF/double-free/segfault fixes are reachable from peer-supplied RTM packets / malformed CQEs → *Oracle:* targeted parser review/fuzz of the named functions **in-guest only**; a guest-local crash is self-DoS (OOS); a crash or memory effect that crosses the guest↔Nitro or tenant line is the hub's HARD STOP.
- *Adjacent (Lens F native-memory variant):* every one of these fixes trusts an attacker-influenceable length/offset/generation/pointer before validating it — the exemplar bug class for this lens.

**Doc evidence:** efa-changelog.md rows 1.44.0, 1.45.0, 1.47.0, 1.48.0 (verbatim above). **Severity-if-true:** Critical + HARD STOP (cross-tenant); Low/OOS (guest-only self-DoS). **Status: corroboration + version oracle only — do NOT drive a live isolation test from this page; defer to hub Area 4 and its mechanism-confirmation gate.**

### Area 2 — [in-scope, net-new confirmation] Dependency version ground-truth + per-package signature verification arrived only in 1.48.0 (Lens R / Q / Y → settles hub Area 5, efa-start D, containers A2)
**Background.** The changelog is the single authoritative source for which component versions ship in each `efa_installer.sh`. The decisive security entry:
- **1.48.0 (April 14, 2026):** "**Add individual RPM/DEB package signature verification support**."
- **1.14.0 (Oct 2021):** "Add **packages list and compare RPM/DEB to list** during installation to prevent unknown package installations" (an allow-list check — *not* a cryptographic signature check).

**Security Concern.** The 1.48.0 entry **confirms, from AWS's own release notes, that no per-package RPM/DEB signature verification existed in any EFA installer before April 2026** (every version 1.4.0–1.47.0, i.e. the bulk of deployed fleets). This is the authoritative settlement of the hub Area 5 / efa-start Area D "GPG/`--check-signatures` optional and off by default" concern and the source of the `efa-installer-containers` A2 claim "per-pkg sig-verify ONLY added 1.48.0." The 1.14.0 "compare to packages list" is an **integrity-by-manifest** check (prevents *unexpected* packages) that provides **no authenticity** — it does not detect a tampered-but-expected package. Combined with the hub's TOFU single-origin download and `latest` resolution, a bundle fetched by a pre-1.48.0 installer (or with per-package verification not engaged) runs unverified component code **as root**.

**High-level Test Scenarios.**
- *Claim:* a currently-deployed EFA installer predates 1.48.0 and therefore performs no cryptographic per-package verification → *Oracle:* read the installed version (`cat /opt/amazon/efa/...`/package metadata); compare against this table; confirm against the installer script whether signature verification is invoked and whether it is default-on or opt-in even in ≥1.48.0 (changelog says "add **support**" — support ≠ default-enforced; **confirm the default** in the installer source, owned by efa-start Area D).
- *Claim:* the `*amzn*`-tagged libfabric/`rdma-core`/driver forks are fetched from the single AWS origin with no out-of-band checksum → defer the fetch/TOFU mechanics to hub Area 5; this page only supplies the version list the hunter checks the origin against.
- *Adjacent:* this table lets the hunter enumerate the **full transitive dependency set and versions** (libfabric, rdma-core, efa-driver, aws-ofi-nccl, Open MPI, PRRTE, OpenPMIx, efa-nv-peermem, GDRCopy via peermem, Intel MPI) that the NCCL (N1) / NIXL (N2) root-level supply-chain siblings reason about — the authoritative "what `latest` actually installs" sheet.

**Doc evidence:** efa-changelog.md rows 1.48.0, 1.14.0; full version table. **Severity-if-true:** supply-chain integrity gap — High if a tamper/MITM path is confirmed by hub Area 5 (AWS-authored installer = Tier-2 reportable); Informational on this page alone. **Status: confirmation of a sibling-owned concern — the signature-verification timeline is settled here; the fetch/default-enforcement test belongs to hub Area 5 / efa-start D.**

### Area 3 — [in-scope, net-new, OWNED by this page] Patch currency is advisory-only; superseded/EOL installer versions bundling known-buggy components remain installable (Lens U / N)
**Background.** The changelog documents a continuous "upgrade / discontinue / drop support" cadence but states **no mechanism that forces a fleet to run a current (or patched) EFA version.** Explicit EOL/deprecation statements include: "**Discontinue support for Amazon Linux 2. The last EFA installer version supporting AL2 is 1.49.0**" (1.50.0); "Discontinue support for openSUSE Leap" (1.49.0); "Deprecate support for Ubuntu 20.04" (1.43.0); "Deprecate support for Debian 10" (1.40.0); "Drop support for CentOS 7 and RHEL 7" (1.34.0); "Drop support for Amazon Linux 1 and Ubuntu 16.04" (1.12.0); and many more.

**Security Concern.** Two unenforced-guarantee shapes:
1. **Pin-to-old (Lens U/N).** Because an operator who must stay on an EOL OS is *explicitly directed* to a specific older installer ("the last version supporting AL2 is **1.49.0**"), AWS both (a) keeps older versioned installers fetchable and (b) *recommends* pinning to them. 1.49.0 bundles libfabric 2.4.0amzn5.0 / efa-driver 3.1.0 / rdma-core 63.0 — but any AL2 operator is frozen there and will **never receive 1.50.0's** fixes, and nothing documented stops a fleet from pinning to a *much* older version (e.g. a pre-1.48.0 build with no per-package signature verification *and* pre-QP-verification data-path code from Area 1). There is **no EC2/EFA control plane condition key** that can assert "instances must run EFA ≥ X" — EFA attachment is already IAM-unscopable (hub Area 1, no `ec2:InterfaceType` key), so patch-level is a fortiori unexpressible. Patch currency is therefore a **prose/advisory property with no enforcement mechanism** — the canonical Lens-U gap.
2. **Flag-semantics drift as an operational-integrity footgun (Lens U).** The changelog shows installer flags silently changing meaning across versions: `--skip-kmod` "fixed to **actually work**" (1.9.3 — i.e. earlier it silently did nothing); `-g/--enable-gdr` turned into a **no-op** (1.14.0); `--disable-build-ngc` **removed** and `--skip-mpi`/`--skip-rdma-core` promoted to **global** (1.49.0). An automation/IaC bake script carried across versions can therefore request a hardening/skip behavior that a different installer version silently ignores or re-scopes — the same **UG-vs-changelog flag-name conflict** flagged by `efa-installer-containers` A2 (UG says `--enable-ngc`; changelog says `--build-ngc`). This page is the authoritative source confirming that conflict and the per-version semantics.

**High-level Test Scenarios.**
- *Claim:* nothing in the EC2/EFA control plane can enforce a minimum EFA installer/driver version on attached instances → *Oracle:* grep `list_ec2.md` for any version/patch-level condition key touching EFA/ENI attachment (expected: none — consistent with hub Area 1's zero-`ec2:InterfaceType` finding). Pure documentation/IAM-reference check, no resource created.
- *Claim:* an older versioned installer (pre-1.48.0) remains downloadable from the AWS origin and installs without per-package signature verification → *Oracle:* confirm older-version availability at the origin (fetch metadata only; mechanics owned by hub Area 5) and map to this table.
- *Claim:* a flag requested by a carried-over bake script is silently ignored/re-scoped on a different installer version → *Oracle:* diff the flag's documented semantics across the versions in play (this table) + the installer `--help`; confirm against containers A2/A3.

**Doc evidence:** efa-changelog.md rows 1.50.0 (AL2 EOL), 1.49.0, 1.43.0, 1.40.0, 1.34.0, 1.12.0 (deprecations); rows 1.9.3, 1.14.0, 1.49.0 (flag drift). **Severity-if-true:** Low–Medium (unenforced-currency / operational-integrity footgun). The *consequence* of running an old version (Area 1 data-path bugs, Area 2 no-sig-verify) is where real severity lives — this area establishes that the old version is *reachable and sometimes recommended*. **Status: owned here; net-new relative to all siblings.**

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Pre-QP-verification data-path processes a completion not bound to the owning QP (version-targeted via this table) | libfabric / rdma-core / efa driver QP·CQ path | "verify QP number on CQE" / "QP generation" — **added** 1.44.0→1.48.0 (mitigation is *recent*; older versions lack it); HARD STOP on cross-tenant confirm (hub Area 4) |
| Fleet runs a pre-1.48.0 installer with no cryptographic per-package verification | `efa_installer.sh` RPM/DEB install | per-package signature verification **absent before 1.48.0**; 1.14.0 manifest-compare provides no authenticity (hub Area 5 / efa-start D) |
| Operator pinned to an EOL/old installer bundling un-fixed data-path components | installed EFA version | no control-plane min-version enforcement; EOL pinning is *recommended* ("last version supporting AL2 is 1.49.0") — **prose only** |
| Carried-over IaC requests a skip/hardening flag silently re-scoped across versions | installer flag parser | flag semantics changed un-versioned (`--skip-kmod`, `-g`, `--build-ngc`, global `--skip-mpi/-rdma-core`); UG-vs-changelog name conflict (containers A2) |

## 7. Out-of-Scope Risk Categories
- **AWS Nitro / SRD fabric internals and hypervisor-side EFA device memory safety** — service plane / shared-responsibility line. The UAF/double-free/ABA/race fixes catalogued in Area 1 are in the **guest-side** libfabric/rdma-core/driver client; a guest-only crash is single-tenant **self-DoS (OOS)**. Any cross-tenant or guest↔Nitro effect is the hub Area 4 **HARD STOP**, not an exploit target.
- **The installer download/TOFU mechanics, GPG `.sig`/`.key`, `--check-signatures` default** — owned by hub Area 5 and efa-start Area D; this page only supplies the version list and the sig-verify-introduction date.
- **Container-bake / Dockerfile root-install specifics** — owned by `efa-installer-containers`.
- **Upstream libfabric / rdma-core / Open MPI / NCCL / GDRCopy project bugs themselves** — third-party reference repos; in scope only insofar as AWS ships and runs them as root via the installer (and then via the owning sibling plan, version-targeted by this table).
- **Product/feature-parity gaps and OS-support matrices** — the deprecation rows are evidence for Area 3's unenforced-currency point, not findings in themselves.

## 8. Null hypotheses / doc gaps (lenses checked, with the page read)
Page checked for every lens: `efa-changelog.md` (the sole page this plan owns), full 93-line table, 2026-10-15.
- **Lens A (cross-tenant IDOR):** N/A — no resource-by-ID API, no tenant/customer id, no identifier of any kind on the page. (EFA-resource IDOR deferred to hub §4 / create-efa.)
- **Lens B/C (PassRole / credential vending):** N/A — no role ARN, no `PassRole`, no STS, no credential field on the page.
- **Lens D/V (data→control / network segmentation):** N/A on this page — no ENI, subnet, SG, control-VPC, or interface mention. (SRD/network isolation owned by hub Areas 4/7.)
- **Lens E (RBAC/privesc):** N/A — no role model, no admin identity, no IAM artifact printed.
- **Lens G (SSRF):** N/A — no field the *service* dereferences server-side; the only URLs on the page are human-readable GitHub release-tag links in the changelog prose (not fetched by any service, not customer-supplied). Checked every row.
- **Lens H (KMS/encryption-context):** N/A — no key, no encryption context.
- **Lens I/S (tagging / condition-key semantics):** N/A — no policy, no condition key, no tag on the page. (The *absence* of any min-version condition key is itself Area 3's Lens-U point, confirmed by cross-ref to hub Area 1's zero-`ec2:InterfaceType` finding.)
- **Lens J (OAuth/3P):** N/A — no 3P integration.
- **Lens K (prompt injection):** N/A — no LLM/agent on this page. (NIXL/NCCL inference-data paths owned by efa-start-nixl/-nccl.)
- **Lens L (DoS):** the "resource exhaustion on systems with high core counts" / huge-page-reservation / Open-MPI-hang fixes are **guest-side self-DoS** on the operator's own cluster (OOS); no cross-tenant shared-fleet exhaustion is introduced by the page.
- **Lens M (shared-identifier interception):** N/A — no session/token/presigned id.
- **Lens N (namespace migration):** no dual-live ARN/namespace. The only version-boundary events (per-package sig-verify entering at 1.48.0; AL2 EOL at the 1.50.0 boundary) are folded into Areas 2/3 (Lens U) rather than a classic migration-window bypass.
- **Lens O (audit-log evasion):** N/A — the page describes no logging surface. (EFA observability/flow-log blind-spots owned by `efa-working-monitor`.)
- **Lens P (proofing/registration):** N/A — no registration/identity-proofing workflow.
- **Lens Q (upload):** N/A as an upload surface — but the installer's bundled packages *are* attacker-relevant blobs executed as root; that is the Lens-R/Q **supply-chain** framing of Area 2, routed to hub Area 5. No service-side file-parse/render on this page.
- **Lens R/Q/Y (supply chain) — FIRES (Area 2):** the changelog is the AWS-authored dependency manifest; it confirms the sig-verify-absent-before-1.48.0 window. Depth (fetch/TOFU/default-enforcement) deferred to hub Area 5 / efa-start D.
- **Lens T (cross-service secret reachability):** N/A — no secret generated/persisted.
- **Lens U — FIRES (Area 3):** patch currency and OS-support guarantees are prose with no enforcement mechanism; flag semantics drift un-versioned.
- **Lens W (attestation):** N/A — no attestation/PCR/enclave on the page.
- **Lens AA (share/revoke):** N/A — no share/grant lifecycle.
- **Lens BB/CC/DD (parser/upstream-context/cache divergence):** N/A — no request path, authorizer, or caching layer on the page.
- **Lens EE (predictable-name land-grab):** N/A — no namespace the service resolves by name.
- **Lens FF (JWT/OIDC):** N/A — no token validation.
- **Lens F — FIRES as corroboration/oracle (Area 1):** the bug-fix history version-targets the data-path parser bug class; cross-tenant reachability is **not** decidable from this page and is held behind hub Area 4's HARD STOP + mechanism-confirmation gate.

**Doc gaps to confirm before investing (routed to owners):** (1) whether per-package signature verification is **default-enforced** in ≥1.48.0 or merely "supported"/opt-in — read the installer source (efa-start Area D). (2) The exact installer version(s) deployed on the target fleet — read in-guest. (3) Whether older versioned installers are still fetchable from the AWS origin without a checksum (hub Area 5). (4) Whether the QP-number-on-CQE verification gap was ever cross-tenant-reachable (hub Area 4 — HARD STOP, mechanism-first).

---
*Prepared from AWS documentation only, 2026-10-15. The sole owned page (`efa-changelog.md`) is byte-identical offline↔online. This plan is a **version-ground-truth / corroboration child** of `efa-attack-research-plan.md`: it owns the net-new Lens-U/N "unenforced patch currency + late signature verification" surface (Area 3) and supplies the authoritative dependency-version & data-path-bug-fix map that version-targets hub Area 4 (Lens F, HARD STOP) and settles hub Area 5 / efa-start Area D / containers A2 (Lens R/Q/Y). Downstream hunter: use Areas 1–2 as a lookup sheet, not a live-test driver; Area 3 is settleable by IAM-reference grep + in-guest version read with no service-plane risk.*
