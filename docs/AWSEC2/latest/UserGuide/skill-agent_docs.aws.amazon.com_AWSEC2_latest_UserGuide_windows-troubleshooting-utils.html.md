# EC2WinUtil (Windows Troubleshooting Utilities) — Attack Research Plan

**Assigned skill:** security-questionbuilder
**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/windows-troubleshooting-utils.html (+ `.md`)
**Companion page pulled in:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2winutil-driver-version-history.html
**Adjacent pages consulted:** `other-windows-device-drivers.md` (install recipe), `manage-device-drivers.md`, `ec2-serial-console.md` (+ family), `configure-access-to-serial-console.md`
**Source of leads:** offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/` cross-checked against live docs (2026-09-12). Both identical.
**Status:** documentation-derived hypotheses only. Nothing tested against a live account or a live instance.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows write access to, or tamper of, the AWS-owned driver-distribution bucket `ec2-windows-drivers-downloads`, or any identity/credential/ARN/account belonging to AWS's own service/distribution plane — stop, preserve evidence, flag for AWS-Security disclosure. Do **not** upload, overwrite, or delete any object in that bucket.
- **This target is unusually thin.** It is a single ~15-line page describing an **in-guest, customer-side kernel-mode Windows driver** (`EC2WinUtil`). There is **no EC2WinUtil control-plane API, no IAM action, no multi-tenant service fleet, and no service-side ingest of a customer-supplied blob.** Most catalog lenses are therefore genuine null hypotheses (Section 8 names the pages checked for each). The real surface is three things: (1) the **software supply chain** of a downloadable kernel driver, (2) the **crash-data → serial console → AWS** egress channel and its "no customer data" guarantee, and (3) the **EC2Launch v2 (SYSTEM) integration** seam. Everything cross-tenant/serial-console-authz is routed to the existing serial-console plan, not re-derived here.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Supply-chain integrity:** Prove or refute that the `EC2WinUtil.zip` a customer is told to download and `pnputil /add-driver`-install can be substituted/tampered (bucket object writable, transport downgrade, no verified signature) → attacker-controlled **kernel-mode code** executing on the customer instance.
2. **Guarantee integrity (Lens U):** Test the documented promise *"EC2WinUtil doesn't collect any customer data in its crash call stacks"* against what a Windows crash stack trace / faulting-module / error-code payload actually contains as it is written to the serial console and shipped to AWS for "crash trend" tracking.
3. **Data egress boundary:** Characterize the customer-kernel → serial-console → AWS collection path. Does customer instance memory/state leave the customer trust boundary in a form the customer cannot inspect or opt out of?
4. **SYSTEM integration seam:** Examine the v3.2.0 "enhanced console logging mechanism for use with EC2Launch v2 agent" — a channel between a kernel driver and a SYSTEM-privileged user-mode agent.
5. **Shared-AMI trust:** A shared / Marketplace AMI ships **without** the preinstalled driver; test whether a trojaned look-alike `EC2WinUtil.sys` baked into a shared AMI is distinguishable by the consumer.

---

## 2. Components, Assets, and Design

**What it is.** `EC2WinUtil` is an AWS-authored **kernel-mode Windows driver** (`.sys` + `.inf`, installed as a "primitive driver") that runs inside the **customer's** Windows Server EC2 instance. Its documented job: on a bug-check/crash it collects "basic crash information" — faulting module identity, Windows error code, and a stack trace of recent calls — and **writes it to the instance serial console**. Output also lets **AWS** "track crash trends for Amazon EC2 drivers, and diagnose large scale crash events." Docs assert it "doesn't collect any customer data in its crash call stacks."

**Provenance / distribution.**
- Preinstalled on **AWS-published** Windows Server AMIs (2016/2019/2022/2025 → "latest version").
- **NOT** preinstalled on AMIs shared with you or subscribed via **AWS Marketplace**.
- Since **v3.0.0** (June 2024) it is downloadable for manual install from a public S3 bucket:
  `https://s3.amazonaws.com/ec2-windows-drivers-downloads/EC2WinUtil/<version>/EC2WinUtil.zip`
  (e.g. `.../EC2WinUtil/3.2.0/EC2WinUtil.zip`). Prior to 3.0.0 there was no downloadable package.
- Install recipe (documented for the sibling AWSVMClock driver in `other-windows-device-drivers.md`, same bucket/idiom): `Invoke-WebRequest https://s3.amazonaws.com/ec2-windows-drivers-downloads/.../X.zip` → extract → `pnputil /add-driver X.inf /install` (requires local admin; installs a kernel driver).

**Version-history facts that are security-relevant.**
- `2.0.0` (2018): output on **MMIO serial ports for metal instance types**; "improved crash parsing and updated output format" → a parser exists.
- `1.0.1` (2018): renamed from `AwsAgent` to `EC2WinUtil` "due to a **namespace conflict with Amazon Inspector**" — a legacy name (`AwsAgent`) and a namespace collision are historical facts worth noting.
- `3.0.0` (2024): "modernized … added support for installation as a **primitive driver**" (kernel driver installable independent of a device).
- `3.1.0` (2026): "improved **power management** event handling."
- `3.1.1` (2026): "**increased call stack length** when logging to console output" → more bytes of kernel stack now reach the console.
- `3.2.0` (2026): "enhanced console logging mechanism **for use with EC2Launch v2 agent**" → new coupling to the SYSTEM-privileged launch agent.

**Assets.**
- Kernel integrity of the customer instance (the driver runs in ring-0).
- The `EC2WinUtil.zip` distribution object and its bucket (AWS-owned).
- Serial-console output stream of the instance (per-instance; IAM-gated read — see serial-console plan).
- The crash-trend telemetry AWS derives from console output.

**Identity / privilege.** No service API and no IAM action govern EC2WinUtil directly. Install requires **local Administrator** in-guest. The driver runs in **kernel mode**. The serial console it writes to is read via `ec2:SendSerialConsoleSSHPublicKey`-gated access (governed elsewhere).

```
                     ┌──────────────────────────────────────────────┐
   AWS-owned public  │  Customer Windows EC2 instance                │
   S3 bucket         │                                              │
 ec2-windows-drivers-│   [admin] pnputil /add-driver EC2WinUtil.inf │
   downloads  ──ZIP──▶   ───────────────▶  EC2WinUtil.sys (RING 0)  │
  (no doc'd hash/sig)│                          │  on bugcheck       │
                     │                          ▼                    │
                     │        crash stack/module/errcode ──▶ SERIAL  │
                     │                (v3.2.0: + EC2Launch v2 agent)  │  CONSOLE ──▶ AWS "crash trend"
                     └──────────────────────────────────────────────┘         (telemetry / collection)
                                                              ▲ read: IAM-gated per instance
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `EC2WinUtil.zip` download | HTTPS GET (S3 path-style) | New since v3.0.0 | Non-mut (read) | External (public bucket) | Fetch driver package | **Yes — unauthenticated public object** | Anyone | No documented checksum/signature/verification step in the page |
| `pnputil /add-driver …inf /install` | in-guest cmd | Existing | Mutating (installs kernel driver) | Internal to instance | Install/replace kernel driver | No | Local Administrator | Kernel-mode; TOFU on the package |
| Serial-console write (COM / MMIO) | in-guest → console | Existing | Non-mut (emit) | Data leaves guest to console | Emit crash stack | No (read is API-gated) | Driver → console; readers gated by serial-console IAM | Read path routed to serial-console plan |
| EC2Launch v2 console-logging hook (v3.2.0) | in-guest IPC/logging | New v3.2.0 | — | Internal to instance | Kernel↔SYSTEM-agent logging | No | SYSTEM agent | Doc-gap: mechanism undocumented |

**No** EC2 control-plane API, IAM action, condition key, managed policy, CFN resource, SLR, tag surface, KMS integration, SSRF-dereferenced field, or service-side upload endpoint is described for EC2WinUtil. (Confirmed by reading the two EC2WinUtil pages plus `manage-device-drivers.md` and `other-windows-device-drivers.md`.)

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Attacker on the network path / bucket-object controller | Customer instance **kernel** | Substituted/tampered `EC2WinUtil.zip` installed via `pnputil` | Customer installs a driver whose `.sys` bytes are not AWS's → attacker code in ring-0. **Any write to `ec2-windows-drivers-downloads` = HARD STOP.** |
| Customer instance kernel memory | Serial console / AWS crash-trend collection | Crash stack trace written to console + shipped to AWS | Any **customer data** (secret/pointer-leaked buffer/string) appears in console output despite the "no customer data" guarantee → guarantee broken (Lens U). |
| Kernel driver (ring-0) | EC2Launch v2 agent (SYSTEM, user-mode) | v3.2.0 "enhanced console logging mechanism" | The logging channel accepts/acts on data from a lower- or differently-trusted component such that a non-admin or the driver influences SYSTEM-agent behavior. |
| Publisher of a **shared/Marketplace AMI** | Consumer of that AMI | AMI ships (or omits) `EC2WinUtil.sys` | A trojaned look-alike driver baked into a shared AMI is indistinguishable to the consumer from the genuine AWS driver. |
| Reader of instance serial console | Another tenant's console | Serial-console IAM authz | Reading crash output for an instance you don't own. **Routed to the existing serial-console plan — not re-derived here.** |

---

## 5. Recommended Areas of Focus

### Area 1 — Driver-distribution supply chain: TOFU on a public-bucket kernel driver  (PRIORITY 1)
**Background.** Since v3.0.0 the customer is instructed to download `EC2WinUtil.zip` from `https://s3.amazonaws.com/ec2-windows-drivers-downloads/EC2WinUtil/<ver>/EC2WinUtil.zip`, extract it, and install it as a **kernel driver** via `pnputil /add-driver …inf /install`. The page (and the parallel AWSVMClock recipe) documents **no hash, no signature-verification step, and no integrity check** the operator is told to perform before installing ring-0 code.
**Security Concern.** The only integrity control implied is Windows Authenticode / the driver catalog (`.cat`) enforced by `pnputil`/PnP at install — which the docs never mention and the customer is never told to verify. If (a) the bucket object is writable/replaceable by a non-AWS principal, (b) a specific `<version>/` path can be created by an attacker (unlisted version squat that a script or a doc-follower fetches), or (c) transport can be downgraded/MITM'd before the `.cat` gate — the customer installs attacker-controlled kernel code. This is the highest-impact lead because the payoff is ring-0 on the instance and the blast radius is every operator who follows the recipe.
**High-level Test Scenarios (falsifiable):**
- **Claim:** the object `ec2-windows-drivers-downloads/EC2WinUtil/3.2.0/EC2WinUtil.zip` (and sibling paths) is writable by a non-AWS principal, or a new `EC2WinUtil/<attacker-version>/…` key can be created. → **Oracle:** an S3 `PutObject`/`ListBucket`/ACL probe returns anything other than `AccessDenied` for a non-owner. → **HARD STOP** on any positive: do **not** actually write; a read-only ACL/`GetBucketPolicy`/anonymous-`PutObject`-dry-run signal is the finding; preserve and disclose. Severity if true: **Critical** (fleet-wide kernel supply chain, AWS-owned).
- **Claim:** the ZIP has no verifiable AWS signature the customer can check, and the `.sys`/`.cat` relies solely on implicit PnP Authenticode. → **Oracle:** download the package (read-only), inspect for a detached signature/checksum manifest and verify the `.cat` chains to a Microsoft/Amazon WHQL cert; check whether the doc anywhere instructs verification. → Severity: **Informational–Low** as a doc/hardening gap; escalates only if the signature gate is absent or self-signed.
- **Claim:** the download can be forced over cleartext or a downgraded path (`http://s3.amazonaws.com/...`) that PnP would still install if the `.cat` is stripped. → **Oracle:** confirm whether `http://` is accepted/redirects, and whether an unsigned/`.cat`-stripped package is refused by `pnputil /add-driver … /install`. (Lens Y.) → Severity: **High** if an unsigned package installs.
**Doc evidence:** version-history download links; `other-windows-device-drivers.md` `Invoke-WebRequest … | pnputil /add-driver`. **Severity-if-true:** up to **Critical (HARD STOP)**.

### Area 2 — "No customer data" crash-stack guarantee vs. what a Windows stack trace actually carries  (Lens U)  (PRIORITY 2)
**Background.** The page asserts: *"EC2WinUtil doesn't collect any customer data in its crash call stacks."* The collected fields are the faulting **module identity**, the **Windows error code**, and a **stack trace of the most recent calls**; v3.1.1 explicitly **increased the call-stack length** logged to the console; and the output is shipped to AWS for crash-trend analysis.
**Security Concern.** A kernel stack trace and faulting-module context can incidentally embed customer-derived material: strings/pointers in stack frames, buffer fragments passed by value, module/driver names of third-party software, and — with a longer captured stack (v3.1.1) — more of it. "Doesn't collect any customer data" is a guarantee whose enforcing mechanism is prose, not an inspectable filter. Because the output crosses out of the customer trust boundary to AWS, an over-broad capture is a customer→AWS data-exposure gap even though it is not cross-*tenant*.
**High-level Test Scenarios (falsifiable):**
- **Claim:** a crafted bug-check can place customer-controlled bytes (a marker string / secret pattern) into the captured stack region so they appear verbatim in serial-console output. → **Oracle:** induce a controlled crash in a lab instance you own; read your own serial console; grep the emitted stack for the planted marker. If present → the "no customer data" guarantee is refuted for that path. Severity: **Low–Medium** (self-data egress to AWS; not cross-tenant).
- **Claim:** the longer call-stack capture (v3.1.1) widens the window of incidental data vs. v2.x. → **Oracle:** compare emitted stack byte-length / content across driver versions on identical crashes.
- **Claim:** the emitted module list discloses third-party/security-product presence (fingerprinting) to whoever can read the console. → **Oracle:** inspect module identifiers in output.
**Doc evidence:** windows-troubleshooting-utils.html crash-call-stacks section; v3.1.1 "increased call stack length." **Severity-if-true:** **Low–Medium** (raise to High only if a repeatable secret-in-stack leak crosses to a party the customer cannot control).

### Area 3 — EC2Launch v2 (SYSTEM) console-logging integration seam  (v3.2.0, [NEW])  (PRIORITY 3)
**Background.** v3.2.0 (June 2026) adds an "enhanced console logging mechanism **for use with EC2Launch v2 agent**." EC2Launch v2 runs as **SYSTEM** in the guest. This introduces a channel/coupling between a ring-0 driver and a SYSTEM-privileged user-mode agent that did not exist before, and is the newest (least-reviewed) component.
**Security Concern.** Any IPC/log surface where the SYSTEM agent consumes data emitted by (or shared with) the kernel driver is a place where content-trust and privilege can be confused: a non-admin who can write to a shared log/pipe/registry key the agent reads, a parser in the agent that trusts driver-formatted console records, or a path where the driver's output is re-ingested and acted upon by the SYSTEM agent.
**High-level Test Scenarios (falsifiable):**
- **Claim:** the "console logging mechanism" uses a named pipe / file / registry / event location that is writable by a non-admin, and the SYSTEM EC2Launch v2 agent reads/parses it → local privilege escalation into SYSTEM via crafted log records. → **Oracle:** with the v3.2.0 driver + EC2Launch v2 installed, enumerate the shared logging artifact's ACL; attempt a non-admin write; observe whether the SYSTEM agent parses attacker-shaped input. (Overlaps the ec2launch-v2 / configure-launch-agents plans — coordinate.)
- **Claim:** the agent's parser of driver console records mishandles length/format (v2.0.0 "crash parsing"/format history) → agent crash or memory error. → **Oracle:** feed malformed records; watch the agent.
**Doc evidence:** v3.2.0 changelog line; EC2Launch v2 SYSTEM privilege (ec2launch-v2 / ec2-windows-instances plans). **Severity-if-true:** **High** if non-admin → SYSTEM; **Medium** for agent-parser DoS. **Doc-gap:** the mechanism is entirely undocumented — confirm the surface in-guest first.

### Area 4 — Shared / Marketplace AMI omission → trojaned look-alike driver  (Lens Q / authenticity)
**Background.** "AMIs that are shared with you or that you subscribe to through AWS Marketplace **don't have the driver preinstalled.**" So a consumer of a shared AMI who wants the utility must add it — and an AMI *publisher* is free to bake in a file named `EC2WinUtil.sys`.
**Security Concern.** The consumer has no documented way to distinguish a genuine AWS-signed `EC2WinUtil` from a same-named malicious kernel driver baked into a shared/Marketplace AMI, or from a stale/downgraded version. This is the AMI-supply-chain shape (same family as the sharing-amis / windows-ami plans) specialized to a kernel driver.
**High-level Test Scenarios (falsifiable):**
- **Claim:** a shared AMI can present a driver named/described as `EC2WinUtil` that is not AWS's, and nothing in the documented workflow surfaces the discrepancy (no owner/authenticity filter, no signature-pin the consumer checks). → **Oracle:** inspect what identifies the genuine driver (publisher cert, version, catalog) and whether the consumer workflow verifies it; test whether a look-alike passes casual inspection / Device Manager. → **Severity:** **Medium–High** (in-guest kernel trojan via shared-AMI supply chain; consumer-side authenticity gap).
**Doc evidence:** version-history "AMIs that are shared with you … don't have the driver preinstalled." **Severity-if-true:** Medium–High.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Tampered/substituted driver ZIP → kernel RCE | S3 distribution + `pnputil` install | (implicit) Authenticode/`.cat` at install — **not documented, not customer-verified** |
| Write/squat on `ec2-windows-drivers-downloads` (HARD STOP) | AWS-owned bucket | Bucket policy / object ACL (AWS-owned; must be private/read-only) |
| Cleartext/downgraded fetch installing unsigned driver | transport + PnP gate | TLS + Authenticode — no `aws:SecureTransport`-style control at this layer |
| Secret/customer data in crash stack → serial console → AWS | EC2WinUtil crash capture | Prose guarantee "doesn't collect any customer data" (no inspectable filter) |
| Non-admin → SYSTEM via EC2Launch v2 logging channel | v3.2.0 integration | Undocumented (doc-gap) |
| Trojaned look-alike driver in shared/Marketplace AMI | AMI supply chain | None documented for consumer authenticity |
| Cross-tenant serial-console read of crash output | Serial console authz | IAM (instance-id/tag scoped) — **see serial-console plan** |

---

## 7. Out-of-Scope Risk Categories (state confidently)
- **Serial-console access-control / cross-tenant read** — governed by `ec2:SendSerialConsoleSSHPublicKey` + IAM; already covered by the existing `skill-agent_…ec2-serial-console.html.md` plan in this directory. Route there; do not re-derive.
- **Customer steering their own instance / installing their own driver** — a customer with local admin already controls their kernel; that is not a boundary breach.
- **Least-privilege footguns in a customer-authored install script** — out of scope (customer-authored). *Carve-out:* the AWS-published download recipe / package integrity IS in scope (Area 1) because it is AWS-authored and copied verbatim.
- **Windows OS / third-party bug-check bugs**, `pnputil` behavior, generic Windows driver-signing policy — Microsoft-owned, not EC2's service plane.
- **IMDS / managed-host internals** on the instance — out of scope for managed hosts.
- **DoS by crashing your own instance** — single-tenant self-DoS.

---

## 8. Null Hypotheses / Doc Gaps (pages named per discipline)
Pages read for triggers: `windows-troubleshooting-utils.md`, `ec2winutil-driver-version-history.md`, `manage-device-drivers.md`, `other-windows-device-drivers.md`, `ec2-serial-console.md`.

- **Lens A / M (cross-tenant IDOR, shared-id interception):** null for EC2WinUtil itself — no resource-by-id API, no tenant field, no shared service fleet. The only cross-tenant read surface (serial console) is a *separate* service with its own plan. **Not N/A for the console**, just routed elsewhere.
- **Lens B / C (PassRole / credential vending):** null — no role ARN input, no STS/session, no credential vending anywhere on these pages.
- **Lens D / V (data→control plane / network segmentation):** null — no ENI/VPC/control-plane component; the driver is in-guest only.
- **Lens E / R / S (RBAC/IAM privesc, managed/sample policy, condition-key semantics):** null — **no IAM policy JSON, no managed policy, no SLR, no condition key, no CFN/runbook block** is printed or referenced for EC2WinUtil. Highest-yield IAM lens has nothing to audit here.
- **Lens F (translation/injection):** partial — a **crash-output parser** exists (v2.0.0 "improved crash parsing," v3.2.0 logging mechanism); native memory-safety of that parser and of the EC2Launch v2 consumer is folded into Area 3. No customer-language translation layer otherwise.
- **Lens G (SSRF):** N/A — read all four driver/troubleshooting pages; **no field the service dereferences** server-side (no URL/host/webhook/logo/callback input; the only URL is the static AWS download link the *customer* fetches, covered as supply chain in Area 1, not SSRF).
- **Lens H / W (KMS / attestation):** null — no KMS key, encryption context, or attestation condition anywhere.
- **Lens I (tagging/ABAC):** null — no tag surface.
- **Lens J (OAuth/3P):** null — no third-party integration.
- **Lens K (prompt injection / LLM):** null — no LLM/agent in this pipeline.
- **Lens L (DoS):** low — a longer captured stack (v3.1.1) and a parser exist; only single-tenant self-impact, out of scope except the agent-parser DoS noted in Area 3.
- **Lens N / X (namespace migration / action-twin parity):** informational only — historical rename `AwsAgent`→`EC2WinUtil` (v1.0.1) resolved a "namespace conflict with Amazon Inspector"; no live dual-namespace or action-family authz to bypass today. Flagged for awareness, not an active lead.
- **Lens O (audit-log evasion):** informational — the crash channel *is* a telemetry/collection path; no security-operation logging to evade here.
- **Lens P (identity proofing / registration):** N/A — no registration/onboarding/verification workflow on these pages.
- **Lens Q (upload / rich content):** the "upload" analogue is the **downloaded driver package** and the **AMI-baked driver** — captured in Areas 1 and 4. No service-side blob ingest.
- **Lens T (cross-service secret reachability):** null — the driver generates/persists no secret, key, or credential.
- **Lens U (guarantee vs enforcement):** **fires** — the "doesn't collect any customer data" promise is prose-enforced; Area 2.
- **Lens Y (transport/signature):** **fires (secondary)** — the download's transport + package-signature integrity, folded into Area 1.
- **Lens AA (share/revoke lifecycle):** null — no share/grant/revoke operation for the driver (AMI-share authenticity is Area 4, a Lens-Q authenticity concern, not a revoke-completeness one).

**Doc gaps to close before hunting:**
1. The **integrity story** of `EC2WinUtil.zip` — is there an AWS signature/checksum manifest, and what exactly `pnputil` enforces (`.cat`/WHQL chain)? The page is silent; confirm the surface before rating Area 1.
2. The **EC2Launch v2 "console logging mechanism"** internals (v3.2.0) — pipe/file/registry, ACLs, parser — entirely undocumented; confirm in-guest first (Area 3).
3. Where AWS's **crash-trend collection** actually reads the console output from and under what identity — undocumented; relevant to how far customer stack data travels (Area 2).

---

## Completion Report
- **Assigned skill:** security-questionbuilder (`/work/.claude/skills/security-questionbuilder`)
- **Target:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/windows-troubleshooting-utils.html
- **Inputs read:** offline mirror + live page (identical); companion `ec2winutil-driver-version-history` (download URLs, version security-notes); `other-windows-device-drivers` (install recipe), `manage-device-drivers`, `ec2-serial-console` family.
- **Result:** research plan produced (documentation-derived hypotheses only; no live testing).
- **Crown jewels:** (1) TOFU/no-verified-integrity on a public-bucket **kernel** driver → potential fleet-wide supply-chain kernel RCE, with bucket-writability as a **HARD-STOP** AWS-service-plane check (Area 1); (2) "no customer data" crash-stack guarantee vs. real Windows stack contents shipped to AWS (Area 2); (3) new EC2Launch-v2/SYSTEM logging seam (Area 3); (4) shared-AMI look-alike-driver authenticity gap (Area 4).
- **Could not fully test from docs (recommend hunter/human follow-up):** package signature/checksum enforcement, the v3.2.0 SYSTEM-integration internals, and the AWS-side collection identity — all three are doc-gaps flagged above. Cross-tenant serial-console read is intentionally routed to the existing serial-console plan, not re-derived.
