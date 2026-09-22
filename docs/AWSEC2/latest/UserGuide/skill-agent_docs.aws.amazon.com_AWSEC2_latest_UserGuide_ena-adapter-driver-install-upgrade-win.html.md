# ENA Windows Driver Install/Upgrade — Attack Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-adapter-driver-install-upgrade-win.html
(offline mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ena-adapter-driver-install-upgrade-win.md`)
**Skill:** security-questionbuilder (documentation-only; nothing tested against a live account)
**Date:** 2026-09-22 · **Verification:** live `.md` == offline mirror on 2026-09-22; **NO injected "run this aws CLI" AI-agent block on this page** (contrast some other EC2 pages — see memory `[[aws-docs-see-also-injection]]`).

> **Read first.** This is a **thin, in-guest, single-account customer runbook**: how to download and install the Amazon Elastic Network Adapter (ENA) driver on a Windows EC2 instance. It has **no service API of its own, no IAM policy JSON, no multi-tenant fleet, and no resource-by-ID surface.** Most control-plane lenses (A/B/C/D/E/H/I/J/K/M/N/V/W/AA/BB/CC/DD/FF) are genuine null hypotheses here. The entire net-new attack surface is a **software supply-chain / trust-on-first-use (TOFU)** shape around a public S3 download + an admin-run `install.ps1`, plus an alternate **SSM Distributor** deployment path.
>
> This page is a near-twin of `windows-troubleshooting-utils.html` (EC2WinUtil) — see memory `[[ec2winutil-troubleshooting-plan]]`. Same distribution bucket, same TOFU shape, same HARD STOP. The API-side ENA surface (`enaSupport`, `EnaQueueCount`, ModifyInstanceAttribute privesc) lives in the sibling plan `[[enhanced-networking-ena-plan]]` / hub `[[enhanced-networking-plan]]` — **do NOT re-derive it here.**

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order.
- **HARD STOPS (two):**
  1. **Writing an object to `s3://ec2-windows-drivers-downloads/…` (AWS distribution plane).** Probing *read/anonymous-list* is fine; *any write attempt* to test a takeover = stop immediately, preserve evidence, route `aws-security`. Never publish/replace a driver artifact.
  2. **The ENA driver's parsing of device/descriptor data (Nitro card ↔ driver).** Memory-safety bugs there are the hypervisor/device fabric, not a customer-reachable tenant boundary. Out of scope; do not probe.

---

## 1. Pentest Objectives (boundary-breach goals)
1. Determine whether an attacker can cause a Windows EC2 instance following this runbook to **execute an attacker-controlled `install.ps1` / driver payload as local administrator** (supply-chain / MITM / TOFU).
2. Determine whether the `AwsEnaNetworkDriver` **SSM Distributor** deployment path can be abused for cross-node code execution via an over-broad `ssm:SendCommand` / distributor IAM grant.
3. Determine whether a **shared/Marketplace AMI or a "not-latest" AMI** can ship a trojaned or look-alike ENA driver that a customer trusts by authenticity assumption.
4. Confirm the download namespace (`ec2-windows-drivers-downloads`) is AWS-owned and non-claimable (land-grab refutation).

---

## 2. Components, Assets, and Design

**Actors / components**
- **Customer instance (Windows EC2)** — the only compute in play. The whole procedure runs *inside* the guest, as **local administrator**.
- **AWS driver distribution bucket** — `ec2-windows-drivers-downloads` (S3, global namespace). Owned by AWS distribution account **`801119661308`** (inferred from the sibling notification topic `arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers` printed in the version-history page). Serves:
  - `https://ec2-windows-drivers-downloads.s3.amazonaws.com/ENA/Latest/AwsEnaNetworkDriver.zip` (moving "Latest" pointer)
  - `https://s3.amazonaws.com/ec2-windows-drivers-downloads/ENA/x64/<version>/AwsEnaNetworkDriver.zip` (pinned versions, from the version-history table)
- **AWS Systems Manager Distributor** — alternate deployment: an AWS-published package named **`AwsEnaNetworkDriver`** deployed to SSM managed nodes ("install once, or with scheduled updates"). Delegates entirely to the SSM User Guide; **no IAM printed on this page**.
- **The artifact** — a `.zip` containing `install.ps1` + driver binaries (`.sys`/`.inf`/`.cat`). Extracted with `expand-archive`, then `install.ps1` is run.

**Assets**
- Integrity of the code executed as admin in the guest (the driver + install script).
- The AWS distribution bucket namespace and its objects.

**Untrusted-data entry / transform (the only injection seams on this page)**
1. **Network fetch → disk → admin-exec:** `invoke-webrequest <url> -outfile …zip` → `expand-archive` → `install.ps1` (admin). No documented integrity check between fetch and exec.
2. **SSM Distributor package resolution → managed-node exec** (SYSTEM).
3. **AMI-baked driver** (authenticity assumption — "if your instance isn't based on one of the latest Windows AMIs…").

```
                            HTTPS GET (invoke-webrequest, no hash/sig verify)
customer Windows guest  ─────────────────────────────────────────────►  s3://ec2-windows-drivers-downloads/ENA/Latest/AwsEnaNetworkDriver.zip
 (local administrator)                                                     (AWS acct 801119661308)
        │  expand-archive  →  install.ps1  (RUN AS ADMIN)  ── code exec in guest
        │
        └── OR: SSM Distributor  ──►  package "AwsEnaNetworkDriver"  ──►  SYSTEM exec on managed node
```

---

## 3. API / Interface Inventory

| Name | Method | Mutating | Facing | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|
| `invoke-webrequest …/ENA/Latest/AwsEnaNetworkDriver.zip` | in-guest PowerShell | n/a (read) | in-guest → S3 (public read) | yes (anonymous S3 read) | anyone | **No hash/sig verify.** "Latest" is a moving pointer. |
| S3 GET `…/ENA/x64/<ver>/AwsEnaNetworkDriver.zip` | HTTPS | n/a | public | yes | anyone | Pinned versions from version-history table; same lack of verify. |
| `install.ps1` | PowerShell (admin) | yes (installs kernel/user NIC driver) | in-guest | n/a | local admin | Runs whatever is in the extracted zip. |
| SSM Distributor deploy of `AwsEnaNetworkDriver` | `ssm:SendCommand` / distributor API | yes (SYSTEM exec) | control-plane → node | via IAM | IAM principal w/ SSM perms | **No IAM shown here — doc-gap, resolve in SSM User Guide.** |
| Device Manager "Roll Back Driver" | GUI | yes | in-guest | n/a | local admin | Roll-back uses local Driver Store copy. |

No `[NEW]` markers. No non-SDK API. No enum/knob delta.

---

## 4. Recommended Areas of Focus (firing lenses)

### Area 1 — Supply-chain / TOFU on the driver artifact  ⭐ PRIMARY  (Lens G-TOFU + Lens Y transport + Lens EE land-grab)
**Background.** The runbook downloads `AwsEnaNetworkDriver.zip` from a public S3 URL and, with **no documented hash, code-signature, or Authenticode check on the downloaded package**, extracts it and runs `install.ps1` **as local administrator**. Every version link in `ena-driver-releases-windows.html` is the same bucket with the same no-verify pattern.

**Security Concern.** Any means of substituting the zip content before `install.ps1` runs yields **admin-level (and, since it installs a NIC driver, effectively kernel-level) code execution in the guest**. Three sub-vectors:
- **(a) Namespace/land-grab (Lens EE):** is `ec2-windows-drivers-downloads` guaranteed AWS-owned and non-claimable? A dangling/unclaimed global bucket name that a lookup trusts by name = classic Bucket-Monopoly / whoAMI shape.
- **(b) Transport MITM / downgrade (Lens Y):** the page's own **Note** tells Windows Server 2016-and-earlier users to force `[Net.ServicePointManager]::SecurityProtocol = Tls12` for the session — implying stock old-Windows sessions may negotiate **weaker/failed TLS** to the S3 endpoint. A network-position attacker (or a customer who works around the error insecurely) could tamper with the fetch. Also note the download is a raw `invoke-webrequest` with no pinning.
- **(c) TOFU (no integrity anchor):** even over good TLS, there is no out-of-band hash/signature the customer can verify the zip against; trust rests entirely on S3+TLS. `install.ps1` content is never attested.

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** `ec2-windows-drivers-downloads` is a first-come global name a non-AWS party could occupy. → **Refute oracle:** the bucket resolves and its objects are served from AWS distribution acct `801119661308` (SNS `arn:aws:sns:us-east-1:801119661308:ec2-windows-drivers` corroborates AWS ownership); a create-bucket of that exact name returns `BucketAlreadyExists`/`BucketAlreadyOwnedByYou`≠you. **Expected result: REFUTED (AWS-owned).** Record the ownership evidence; **do NOT write objects (HARD STOP).**
- **Claim:** Windows binaries `.sys`/`.cat` in the zip are Authenticode-signed, so a swapped-but-unsigned payload fails to install even if the fetch is tampered. → **Confirm/Refute oracle:** inspect the shipped `.cat`/`.sys` for a valid Microsoft/AWS Authenticode signature and whether `install.ps1` enforces WHQL/signature; if signed+enforced, MITM-swap is defeated at install → downgrades (b)/(c). **This is the key mitigation to verify.**
- **Claim:** a stock Windows Server 2016 session downgrades below TLS 1.2 to the S3 endpoint, opening a MITM window. → **Oracle:** capture the TLS handshake from an un-patched WS2016 image; a <1.2 negotiation (or a plaintext fallback) proves the exposure the Note hints at.

**Doc evidence:** install steps (`invoke-webrequest`, `expand-archive`, `install.ps1`), the TLS-1.2 **Note**, version-history table URLs.
**Preconditions:** for (b) a network MITM position or a customer working around the TLS error; for (a) a namespace gap (expected none). **Cost:** low (read/inspect only). **Severity-if-true:** MITM/land-grab → guest admin/kernel RCE = **High**, and **fleet-wide** if the shared "Latest" object were ever writable = would be Critical + HARD STOP — but ownership is expected AWS, so realistic residual = TOFU/transport hardening gap (Low–Medium) unless a signature-enforcement gap is confirmed.
**Stop condition:** the moment any test would *write* to the bucket, or reach the AWS distribution account — stop, preserve, disclose.

### Area 2 — SSM Distributor deployment path  (Lens R/S + Lens B/E cousin)
**Background.** The alternate method deploys the AWS-published `AwsEnaNetworkDriver` package via **Systems Manager Distributor** ("install once, or with scheduled updates"), which executes on managed nodes as **SYSTEM**. The page prints **no IAM** and hands off to the SSM User Guide.
**Security Concern.** Distributor deployment = `ssm:SendCommand`-class action → arbitrary-package SYSTEM exec on nodes. If the operator's SSM/distributor policy is scoped with `Resource:"*"` (a recurring EC2-runbook footgun — see memory `[[create-vss-snaps-plan]]`, `[[using-cloudwatch-plan]]`), a principal who can deploy this "benign" package can deploy *any* package to *any* managed node = lateral RCE.
**Test Scenarios:**
- **Claim:** the IAM required to deploy `AwsEnaNetworkDriver` via Distributor is scopable to specific nodes/packages, not `Resource:"*"`. → **Oracle:** resolve the Distributor deploy permissions in the SSM User Guide / any sample policy; a printed `ssm:SendCommand` on `Resource:"*"` with no `ssm:resourceTag`/document constraint = over-grant. **Doc-gap: not on this page — resolve in SSM docs before rating.**
- **Claim:** a scheduled Distributor "auto-update" association could pin an attacker-influenced package/version. → route to the SSM Distributor package-integrity model.
**Severity-if-true:** cross-node SYSTEM exec via over-broad grant = **High** (intra-account). **This is a doc-gap lead — confirm the SSM surface first.**

### Area 3 — AMI-baked driver authenticity  (Lens U guarantee + Lens EE/whoAMI adjacency)
**Background.** The page opens: "If your instance isn't based on one of the **latest Windows AMIs that Amazon provides**…" — i.e. the driver normally arrives *preinstalled in an AWS AMI*, and the customer trusts it by provenance.
**Security Concern.** A **shared/community/Marketplace AMI**, or a whoAMI-style name-match on an AMI lookup that omits `--owners amazon`, could ship a **trojaned or look-alike ENA driver** the customer never re-verifies. The runbook offers no way to attest the *preinstalled* driver's authenticity.
**Test Scenarios:**
- **Claim:** a customer who selects a non-Amazon AMI by name/pattern can be served an image whose preinstalled `AwsEnaNetworkDriver` is attacker-built. → **Oracle:** this is the AMI-authenticity boundary, not this page's. **Route to `[[allowed-amis-plan]]` / `[[finding-an-ami-plan]]` (whoAMI owner-omission) and `[[sysprep-ami-plan]]` (SYSTEM-hook supply-chain).** Do not re-derive here.
**Severity-if-true:** guest RCE via trojaned driver in an untrusted AMI = **High**, but owner-to-fix is AMI selection, not this doc.

---

## 5. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Swap `AwsEnaNetworkDriver.zip` in transit → admin RCE | in-guest fetch→`install.ps1` | S3 + TLS only; **no hash/sig step documented**; verify Authenticode on `.sys`/`.cat` |
| Claim the distribution bucket name (land-grab) | `ec2-windows-drivers-downloads` | AWS ownership (acct 801119661308) — expected REFUTED |
| TLS downgrade on WS2016 → MITM | old-Windows PowerShell session | doc Note forcing TLS 1.2 (hints at default weakness) |
| Over-broad SSM Distributor deploy → cross-node SYSTEM exec | SSM Distributor | none on this page — SSM IAM model (doc-gap) |
| Trojaned preinstalled driver in untrusted AMI | AMI provenance | "AMIs that Amazon provides" (provenance assumption only) |

---

## 6. Out-of-Scope / Null Hypotheses (pages checked: this page + `ena-driver-releases-windows.md` version-history + `troubleshoot-ena-driver.md` reference)
- **Lens A/B/C/D/E/H/I/J/K/M/N/V/W/AA/BB/CC/DD/FF — NULL.** No service API, no role ARN/PassRole, no multi-tenant fleet, no resource-by-ID, no KMS/tag/OAuth/JWT/authorizer/cache/network-ENI surface on this page. Single-account, in-guest runbook.
- **Lens F (native memory-safety of the ENA driver) — OUT OF SCOPE / HARD STOP.** The version-history changelog documents historical driver memory-corruption/race classes (NBL double-release, OOB, reset-loop), but these are the driver parsing **device/descriptor data from the Nitro card** — the hypervisor/device fabric, not a customer-reachable cross-tenant boundary. Do not probe.
- **Lens L (DoS) — OUT OF SCOPE.** Reboot/stop-start of the customer's own instance is self-inflicted, single-tenant.
- **Lens O — informational.** The public docs expose AWS distribution account `801119661308` (SNS topic) — publicly documented, not a finding; useful only as bucket-ownership evidence.
- **`enaSupport` / `EnaQueueCount` / ModifyInstanceAttribute-userData privesc — NOT HERE.** That is the API-side ENA surface → `[[enhanced-networking-ena-plan]]` / `[[enhanced-networking-plan]]`.

## 7. Handoff notes for the next agent
- **Crown lead = Area 1** (supply-chain/TOFU). The single highest-value *verifiable* datum is **whether the shipped `.sys`/`.cat` are Authenticode-signed and whether `install.ps1` enforces signature** — that mitigation, if present, collapses the MITM/TOFU severity. Inspect an actual zip (read-only) to settle it.
- **Do NOT write to `ec2-windows-drivers-downloads`** (HARD STOP #1). Ownership is expected AWS (acct 801119661308) → land-grab REFUTED without any write.
- **Area 2 is a doc-gap:** resolve the SSM Distributor IAM model in the AWS Systems Manager User Guide before rating; look for `ssm:SendCommand` `Resource:"*"`.
- **Area 3 belongs to the AMI-authenticity plans** — route, don't re-derive.
- Sibling pages already in mirror: `ena-driver-releases-windows.md` (download URLs + changelog), `troubleshoot-ena-driver.md`. Twin plan: `[[ec2winutil-troubleshooting-plan]]` (identical bucket + TOFU + HARD STOP shape).

---
**Completion:** documentation-derived hypotheses only; nothing tested against a live account. Firing lenses: G-TOFU, Y, EE, R/S (doc-gap), U. All cross-tenant/control-plane lenses NULL for this in-guest page.
