# Paravirtual (Xen) Drivers for Windows Instances — Attack Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/xen-drivers-overview.html
(markdown mirror: `.../xen-drivers-overview.md`)
**Source of leads:** the target page only (online == offline verified 2026-09-22; page content pulled live via `.md`). Companion pages referenced but not deep-analyzed here: `Upgrading_PV_drivers.html`, `pvdrivers-troubleshooting.html`, and the SSM State-Manager auto-update walkthrough in the *AWS Systems Manager User Guide*.
**Status:** documentation-derived hypotheses only. Nothing tested against a live account. No AWS-service-plane action taken.
**Injection check:** page carries **no** injected "run this aws CLI" AI-agent block (cf. [[aws-docs-see-also-injection]]). Clean.

---

## 0. How to use this document

- This is a **thin, in-guest, single-account, customer-shared-responsibility** page. It documents AWS-authored **kernel-mode Windows drivers** (AWS PV, Citrix PV, Red Hat PV) that run *inside the customer's own EC2 Windows instance*, plus how to download/update them and subscribe to release notifications. There is **no PV-driver control-plane API, IAM action, managed policy, or multi-tenant fleet** on this page — so most Step-4 lenses are genuine null hypotheses (see §8).
- Near-identical twin of two already-written plans — **reuse, do not re-derive**: [[ec2winutil-troubleshooting-plan]] and [[ena-driver-install-win-plan]]. Same download bucket (`ec2-windows-drivers-downloads`), same SNS publisher account (`801119661308`), same TOFU supply-chain shape, same HARD STOP.
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order.
- **HARD STOPS (two, both AWS service plane):**
  1. **Do not write objects to `s3://ec2-windows-drivers-downloads/`** — that is AWS's distribution plane. Bucket *writability* is the finding; probing existence is fine, mutating is a hard stop, preserve evidence and route `aws-security`.
  2. **Do not probe the Xen hypervisor / XenStore cross-domain boundary** — XenStore, the `xen*` kernel drivers' host-facing ring buffers, and the LiteAgent↔AWS-API command channel all terminate at the Xen hypervisor = AWS service plane. Memory-safety of a `xenvbd`/`xennet` device-descriptor parser or a cross-domain XenStore read is out of scope; the moment evidence touches another domain or the host, stop and flag.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)

1. **Supply-chain integrity of the driver package** — determine whether an actor positioned on the network path (MITM) or the distribution namespace can cause a customer/SSM-automation to install an **attacker-controlled kernel-mode driver** (fleet-wide kernel RCE), given the page documents a download-and-run flow with **no hash/signature-verification step**.
2. **Signature-lifecycle integrity** — the page itself documents an AWS PV driver whose Authenticode signature **expired** (7.4.3, "signature expires on March 29, 2019"). Establish whether expired/soon-to-expire signed drivers are still installable/loadable and whether that weakens the code-signing guarantee customers rely on.
3. **SSM auto-update permission surface** — the "Automatically Update PV Drivers" path runs via **AWS Systems Manager (State Manager)** as SYSTEM in-guest. Determine whether the IAM/SSM permission composition to drive it enables a `ssm:SendCommand`-style SYSTEM RCE or confused-deputy (companion-page, resolve in SSM docs).
4. **Notification-channel abuse** — the cross-account SNS topic subscription flow: any integrity/abuse issue (spoofed release notice → social-engineered downgrade).
5. Confirm the correct **out-of-scope line** so a hunter does not burn time on the hypervisor plane or on customer-authored config.

---

## 2. Components, Assets, and Design

**What this page actually describes:** the set of paravirtual (PV) drivers baked into Amazon Windows AMIs that let the guest OS see virtualized EBS/instance-store volumes and network on **Xen-generation** instances. (On **Nitro** generation these PV drivers are *not used*; the LiteAgent user-mode service self-stops from v8.2.4.)

**Driver families (all in-guest, kernel-mode + one user-mode agent):**
- **AWS PV** — `%ProgramFiles%\Amazon\Xentools`. Kernel components under `HKLM\SYSTEM\CurrentControlSet\Services`: `xenbus, xeniface, xennet, xenvbd, xenvif`. Ships `xenstore_client.exe` (reads hypervisor XenStore) + public symbols. User-mode service **LiteAgent** handles shutdown/restart events "from AWS APIs on Xen generation instances."
- **Citrix PV** (legacy) — `%ProgramFiles%\Citrix\XenTools`. Components `xenevtchn, xeniface, xennet, Xennet6, xensvc, xenvbd, xenvif`; user-mode `XenGuestAgent`.
- **Red Hat PV** (legacy) — `%ProgramFiles%\RedHat`. `rhelnet`, `rhelscsi`. Not recommended >12 GB RAM (boot failure).

**Assets / distribution artifacts (the real attack surface):**
- **Download URLs (public, HTTPS, path-style S3):**
  - `https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/Latest/AWSPVDriver.zip`
  - versioned: `.../AWSPV/8.6.1/AWSPVDriver.zip`, `.../8.4.3/…`, `.../8.3.5/…`
- **SSM auto-update:** State-Manager runbook, walkthrough at `systems-manager/…/state-manager-update-pv-drivers.html`.
- **SNS release-notification topic (cross-account):** `arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers` (us-east-1 only). Account **801119661308** is the AWS publisher (same account as the ENA/EC2WinUtil driver notifications — confirms the download bucket is AWS-owned, not land-grabbable).
- **In-guest hypervisor interface:** `xenstore_client.exe` → XenStore (`root\wmi` class `AWSXenStoreBase`, e.g. `.XenTime`). Xen event channels via `xenevtchn`/`xenbus`.

**Identity / trust model:** none on this page. The "actors" are: (a) the in-guest local administrator running the installer; (b) SSM/State-Manager acting as SYSTEM in-guest; (c) the AWS control plane pushing shutdown/restart via LiteAgent+XenStore; (d) the Xen hypervisor. There is no customer-facing PV-driver API and no per-tenant resource ID.

**ASCII — install / trust pipeline (where an attacker could stand):**

```
                    (MITM / TLS-downgrade)              (bucket land-grab: REFUTED, AWS-owned)
                            │                                     │
customer admin / SSM  ──HTTPS GET──►  s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/.../AWSPVDriver.zip
   (SYSTEM in-guest)                            │
        │                                       ▼
        │                          AWSPVDriver.zip  ── NO documented hash/sig-verify step ──►  installer (Pnputil, v8.5.0+)
        │                                                                                          │
        ▼                                                                                          ▼
  install → kernel-mode xen* drivers loaded  ◄────── Authenticode / .cat (Windows-enforced; 7.4.3 EXPIRED 2019-03-29)
        │
        ▼
  ==================  GUEST / HYPERVISOR BOUNDARY (HARD STOP below this line) ==================
  xenstore_client.exe / xenbus / event channels  ──►  Xen XenStore  ──►  Xen hypervisor (AWS plane)
  LiteAgent  ◄── shutdown/restart "from AWS APIs" ──  AWS control plane (AWS plane)
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| Driver ZIP download | HTTPS GET | Existing | No (read) | External (public S3) | Fetch AWS PV driver package | Yes (anonymous) | Anyone | `ec2-windows-drivers-downloads` bucket; path-style HTTPS; **no documented integrity check on ZIP** |
| SSM State-Manager auto-update | SSM assoc/`SendCommand` (companion) | Existing | Yes (installs kernel driver as SYSTEM) | External→in-guest | Auto-update PV drivers | Via IAM | SSM-authorized principals | Permissions NOT printed on this page → resolve in SSM docs (Lens R/S) |
| `xenstore_client.exe` | Local CLI | Existing | Read | Internal (in-guest→hypervisor) | Read XenStore entries | No | Local user | Hypervisor interface — HARD STOP |
| LiteAgent (`Services.msc`) | Local Win service | Existing | Yes (shutdown/restart) | Internal | Receives shutdown/restart "from AWS APIs" | No | AWS control plane via XenStore | Xen-gen only; self-stops on Nitro v8.2.4+ |
| SNS `Subscribe` to topic | SNS API/Console/CLI/PS | Existing | Yes (creates sub) | External | Release notifications | Yes | Any AWS caller | Cross-account topic `…:801119661308:ec2-windows-drivers`, us-east-1 only |

No `[NEW]` markers on this page. Newest datum: AWS PV **8.6.1** (2026-07-21) — "Updated runtime dependencies in the installer package."

---

## 4 & 5. Recommended Areas of Focus (firing lenses, priority order)

### ⭐ Area 1 — Driver-package supply-chain: TOFU download → kernel RCE (Lens G-fetch + Lens Y transport + Lens EE namespace)
**Background:** The page instructs customers to "[Download] the driver package and run the install program manually" from `https://s3.amazonaws.com/ec2-windows-drivers-downloads/AWSPV/Latest/AWSPVDriver.zip`, or to let SSM do it automatically. The installed artifacts are **kernel-mode drivers** (`xenbus/xeniface/xennet/xenvbd/xenvif`) — the highest-privilege code that can run in the guest.
**Security Concern:** The page documents **no hash, checksum, or signature-verification step** on the downloaded ZIP before install. A trust-on-first-use gap: whoever controls the bytes at install time controls the kernel.
**High-level Test Scenarios (falsifiable claims):**
- **Claim (MITM/downgrade):** A network-position attacker (or a WS2016/legacy TLS-1.2-negotiation downgrade, cf. the sibling ENA page's TLS-1.2 note) can substitute a malicious `AWSPVDriver.zip` because the client performs no out-of-band integrity check. → **Oracle:** installed driver hash ≠ AWS-published hash yet install proceeds; or TLS negotiated < the documented floor. → **Refuted if** the installer/.cat enforce Authenticode and the ZIP carries a verified detached signature the doc-flow checks.
- **Claim (land-grab / Lens EE):** the bucket name `ec2-windows-drivers-downloads` is a predictable global namespace; if ever relinquished, an attacker pre-registers it and serves trojaned kernel drivers to the whole Windows fleet. → **Oracle:** bucket ownership/account. → **REFUTED (documented):** the SNS publisher account `801119661308` is AWS's, and the same account/bucket serves ENA + EC2WinUtil; the bucket is actively AWS-owned. Land-grab is **not** viable while AWS holds it. **Retain as a monitoring lead only.**
- **KEY verifiable datum (collapses severity):** Authenticode signature + catalog (`.cat`) on the shipped `.sys` files, and whether the installer (`Pnputil`, v8.5.0+) enforces signature validation. Windows kernel-driver signing is mandatory, so a naive swap likely fails to load — **this is the control that most likely defeats the MITM claim.** Establish it first.
**Doc evidence:** "Download the driver package and run the install program manually"; download URLs; "Updated the PV installer to use `Pnputil`" (8.5.0). **Severity-if-true:** fleet-wide guest kernel RCE = High (customer-guest scope; not cross-tenant unless the bucket itself is compromised → then Critical + HARD STOP). **Stop condition:** do not write to the bucket.

### Area 2 — Signature-lifecycle / expired-signing-cert integrity (Lens Y + Lens U)
**Background:** The changelog states, for **7.4.3**: *"AWS PV driver version 7.4.3's signature expires on March 29, 2019."* Also documents multiple end-of-support versions (8.4.3 last for WS2012/R2; 8.3.5 last for WS2008 R2) still **available for download**.
**Security Concern:** A published, downloadable, AWS-signed kernel driver whose signing certificate has **expired** undermines the Authenticode guarantee (Area 1's main control). Legacy versions remaining downloadable widen the window for a documented-downgrade attack.
**High-level Test Scenarios:**
- **Claim:** an expired-signature AWS PV driver (7.4.3) is still installable/loadable on a supported OS, so the "drivers are signed" guarantee is advisory, not enforced end-to-end. → **Oracle:** attempt load on a lab guest; observe whether Windows blocks on expired cert vs honors a countersignature/timestamp. → **Refuted if** the driver carries a trusted RFC-3161 timestamp (expiry of the signing cert does not invalidate a timestamped signature) — likely the real answer; note it.
- **Claim (downgrade):** because EOL versions remain at stable URLs, an attacker who can influence the version string in an SSM association or a social-engineered runbook can force install of a weaker/older driver. → **Oracle:** version-pinning controls in the SSM auto-update path.
**Doc evidence:** the 7.4.3 changelog line; the "available for download but no longer supported" lines. **Severity-if-true:** Low–Medium (integrity of a documented guarantee; AWS-owned to fix). **Stop condition:** none beyond Area 1.

### Area 3 — SSM State-Manager auto-update: SYSTEM-exec permission composition (Lens R/S — doc-gap)
**Background:** "Use AWS Systems Manager to automatically update the PV drivers" → State-Manager walkthrough in the SSM User Guide. This installs kernel drivers **as SYSTEM** inside the instance.
**Security Concern:** the target page prints **no IAM policy** for this path. The composition of `ssm:SendCommand` / `ssm:CreateAssociation` scoped to `Resource:*` (or `instance/*`) with no ownership condition is a known SYSTEM-RCE / confused-deputy shape.
**High-level Test Scenarios:**
- **Claim:** a principal holding the SSM permissions the walkthrough requires can drive driver install/arbitrary-document execution as SYSTEM on instances it does not own (missing `ssm:resourceTag`/ownership condition). → **Oracle:** resolve the actual required policy in the SSM State-Manager doc and audit statement-by-statement; prove under a scoped role via `iam:SimulatePrincipalPolicy` first.
**Doc evidence:** the SSM auto-update bullet + external walkthrough link. **Severity-if-true:** SendCommand→SYSTEM RCE = High. **Route:** resolve in SSM docs; cross-reference the same pattern already documented in [[create-vss-snaps-plan]] (`instance/*` SendCommand→SYSTEM), [[using-cloudwatch-plan]], and the SSM-Distributor variant in [[ena-driver-install-win-plan]]. **Do not re-derive** — reuse those.

### Area 4 — Release-notification channel abuse (Lens M/O — low)
**Background:** Cross-account SNS topic `arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers`; customers subscribe by email to learn of new driver releases.
**Security Concern:** minimal. Subscription is one-directional (customer → AWS topic); customers cannot publish. The only shape worth a line: a spoofed *out-of-band* "new driver available" message (not via SNS) could social-engineer a downgrade/trojan install feeding Area 1/2. **The SNS topic itself is not attacker-writable.**
**High-level Test Scenarios:** confirm the topic policy does not allow non-AWS `Publish`. **Oracle:** topic resource policy. **Severity:** Informational.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Trojaned ZIP installed as kernel driver | Download URL + installer | Authenticode `.cat` on `.sys`; `Pnputil` sig-enforcement (8.5.0+) — **verify this is the real control** |
| Expired-signature driver still loads | 7.4.3 package | RFC-3161 timestamp on signature (likely present) |
| Forced version downgrade to EOL driver | SSM association / manual | Version pinning + signature; EOL URLs still live (gap) |
| SYSTEM RCE via SSM auto-update perms | State-Manager runbook (companion) | IAM scoping in SSM doc (not on this page) |
| Cross-VM XenStore / device-parser reach | `xenstore_client`, `xen*` drivers | Xen hypervisor domain isolation — **AWS plane, HARD STOP** |
| Spoofed release notification → downgrade | SNS topic (cross-acct) | Topic policy blocks non-AWS Publish |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Xen hypervisor / XenStore cross-domain boundary** — XenStore reads (`xenstore_client.exe`, `AWSXenStoreBase`), `xenbus`/event-channel plumbing, and the LiteAgent↔"AWS APIs" shutdown/restart channel all terminate at the Xen hypervisor = **AWS service plane. HARD STOP.**
- **Kernel-driver device-descriptor memory-safety** (`xenvbd`/`xennet`/`xenvif` parsing host-supplied ring buffers) — the "attacker" is the host/hypervisor; a cross-tenant break requires host compromise = **out of scope / HARD STOP**, even though the changelog shows historical memory-corruption fixes (7.2.5 invalid-memory deref, 0x0000DEAD bugcheck, 8.3.3 invalid-SRB crash).
- **In-guest customer configuration** — TCP-offload toggle, DSRM boot, storage-pool/page-83 behavior, jumbo-frame config: customer shared-responsibility, out of scope.
- **Writing to `s3://ec2-windows-drivers-downloads/`** — AWS distribution plane; probing existence OK, mutation = HARD STOP.
- **Legacy Citrix/Red Hat driver internals** — no download surface on this page, EOL.
- **Nitro-generation instances** — PV drivers not used; LiteAgent self-stops. This whole page is Xen-generation only.

---

## 8. Null Hypotheses / Doc Gaps

**Genuinely null (pages checked: the target page in full — it is the only in-scope surface; no profile/settings/API-reference surface exists for PV drivers):**
- **A (cross-tenant IDOR):** no PV-driver API, no resource-by-ID, no multi-tenant fleet on this page. Null.
- **B/C (PassRole / credential vending):** no role ARN accepted, no STS/session, no credential vending. Null (SSM auto-update role lives in the SSM doc → Area 3).
- **D/V (data→control-plane / network segmentation):** the only guest→control channel is LiteAgent/XenStore = hypervisor plane = HARD STOP, not a testable customer boundary. Null-in-scope.
- **E (RBAC privesc):** no service role model on this page. Null.
- **F (injection/parser):** the only parsers are kernel drivers parsing hypervisor data = HARD STOP. Null-in-scope.
- **H (KMS):** none. **I (tagging/ABAC):** none. **J (OAuth/3P):** none. **K (LLM/agent):** none. **N (namespace migration):** none. **W (attestation):** none. **AA (share/revoke):** none. **BB/CC/DD (edge/parser-diff/cache/upstream-context):** no request-routing/auth layers. **FF (JWT/token):** none. All null — no triggering field on the page.
- **EE (land-grab):** bucket is AWS-owned (acct 801119661308) → **REFUTED**, retained as monitoring-only.

**Firing:** **G** (TOFU fetch, Area 1), **Y** (transport + signature-lifecycle, Areas 1–2), **U** (documented signing guarantee vs enforcement, Area 2), **R/S** (SSM permission doc-gap, Area 3 — resolve off-page), **M/O** (notification channel, Area 4, informational).

**Doc gaps to confirm surface first:**
1. Whether the shipped `.sys`/`.cat` are Authenticode-signed with a valid RFC-3161 timestamp, and whether `Pnputil`-based install enforces it (the pivotal control for Area 1/2). Not stated on this page.
2. The exact IAM/SSM policy required by the State-Manager auto-update walkthrough (Area 3) — lives in the SSM User Guide; resolve and audit statement-by-statement.
3. Whether the ZIP has any published SHA/detached signature customers are told to verify — page shows none; confirm on the `Upgrading_PV_drivers.html` companion.

---

*Method: security-questionbuilder (Steps 1–6). This target is a documentation twin of [[ec2winutil-troubleshooting-plan]] and [[ena-driver-install-win-plan]]; reuse their TOFU/HARD-STOP framing rather than re-analyzing the shared bucket.*
