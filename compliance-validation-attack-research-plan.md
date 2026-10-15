# Amazon EC2 — Compliance Validation — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/compliance-validation.html` (verified identical online `.md` and offline mirror `docs/AWSEC2/latest/UserGuide/compliance-validation.md`). Cross-checked: EC2 IAM reference `docs/service-authorization/latest/reference/list_ec2.md`, AWS Artifact IAM reference `docs/service-authorization/latest/reference/list_artifact.md`, and the EC2 Security chapter sibling list.
Status: documentation-derived hypotheses only; nothing tested against a live account.

> **VERDICT UP FRONT — NULL-DOMINANT PAGE.** This is one of AWS's fully-templated Security-chapter boilerplate pages (the same five sentences appear verbatim across dozens of services — see `docs/*/compliance-validation.md` for `sdk-for-swift`, `ebs`, `systems-manager`, `appstream2`, `neptune-analytics`, `verified-access`, `security-ir`, …). It defines **no EC2 API, no request field, no resource, no identifier, no process/fleet, and no EC2-specific trust boundary of its own.** Its entire content is three outbound *pointers* to other services and one shared-responsibility statement. There is **no EC2 attack surface introduced or described by this page.** Every lens below is therefore a null hypothesis for the EC2 target; the handful of genuinely investigable mechanisms live in **other services** (AWS Accounts, AWS Artifact) and are documented as scoped-out pointers so a hunter does not re-derive them from zero. This plan's value is a defensible, page-by-page NULL with the three cross-service leads correctly attributed and bounded.

---

## 0. How to use this document
- This is a NULL-dominant plan. Sections 5–6 are intentionally short; the load-bearing content is Section 8 (null hypotheses with pages named) and Section 7 (out-of-scope, stated as confidently as in-scope).
- Each cross-service lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Severity → why it is **not** an EC2 finding.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (No path on this page approaches that line — all surfaces are documentation/pointer only.)

---

## 1. Pentest Objectives
There is no EC2 boundary-breach objective reachable from this page. For completeness, the only *compliance-adjacent* objectives that exist for EC2 live on **other** pages and already have dedicated plans:
- **EC2 snapshot-lock "compliance mode"** (`ec2:LockSnapshot` / `ec2:UnlockSnapshot`, condition key `ec2:SnapshotCoolOffPeriod`, `list_ec2.md` l.8706 / l.9709 / l.10154). This is EC2's only IAM surface containing the word "compliance," and it is **not referenced by this page.** It is covered by the existing **data-protection** and **disaster-recovery-resiliency** plans (sample drifts `ec2:SnapshotTime` vs real `ec2:SnapshotCoolOffPeriod`; immutable-WORM lock semantics). Do not re-open it here.
- Nothing else. The page's "compliance" is organizational/attestation compliance (SOC/PCI/HIPAA audit evidence), not a technical control with an EC2 enforcement mechanism.

---

## 2. Components, Assets, and Design
**Customer-facing interface introduced by this page:** none. The page is static prose with four hyperlinks.

**Full content inventory (every sentence, mapped to its real owner):**

| # | Doc statement | Links to | Owning service (NOT EC2) |
|---|---|---|---|
| S1 | "Our new AWS sign-up experience is not designed for regulated workloads … sign up for AWS (advanced) / activate advanced features" | `accounts/latest/reference/getting-started.html`, `.../activate-advanced-features.html` | **AWS Accounts / sign-up** |
| S2 | "To learn whether an AWS service is within the scope of specific compliance programs, see AWS services in Scope" | `aws.amazon.com/compliance/services-in-scope/` | **AWS marketing/compliance portal** (not an API) |
| S3 | "You can download third-party audit reports using AWS Artifact … Downloading Reports in AWS Artifact" | `artifact/latest/ug/downloading-documents.html` | **AWS Artifact** |
| S4 | "Your compliance responsibility … is determined by the sensitivity of your data … see AWS Security Documentation" | `docs.aws.amazon.com/security/` | **Shared-responsibility model** (prose) |

**Processes / hosts / fleets:** none described. **Accounts/VPCs owning what:** none described (no EC2 data-plane/control-plane split appears). **Network interfaces/sockets:** none. **Resource & identifier shape:** no EC2 resource or ID is defined. **Identity establishment:** none described. **Roles/privilege levels:** none described. **Untrusted-data entry/transform:** none — the page accepts no input and dereferences no customer-supplied value.

No ASCII pipeline is warranted: the docs imply no pipeline. The page is a leaf pointer node, not a mechanism.

---

## 3. API / Interface Inventory
| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | **The page introduces NO API.** | — | — | EC2 has zero compliance-validation-specific action. |

Cross-service actions a reader might reach *from* this page (documented for scoping only, NOT EC2 surface):
- `artifact:GetReport` / `GetReportMetadata` / `GetTermForReport` / `ListReports` — AWS Artifact report download. Resource type `report*`; condition keys `artifact:ReportCategory`, `artifact:ReportSeries` (`list_artifact.md`). → scoped out (§7), lead L3.
- AWS Accounts sign-up / `activate-advanced-features` — no public SDK action printed on the linked pages' summary; account-posture toggle. → scoped out (§7), lead L1/L2.

No `[NEW]` marker, no "testing should focus on…" sentence, no undocumented/console-hidden knob — the page has no parameters at all.

---

## 4. Trust-Boundary Map
| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| — | — | **No EC2 trust boundary is defined or crossed by this page.** | n/a |

The page sits entirely on the customer side of the shared-responsibility line and does not describe any component that talks across an ownership line. The only boundaries reachable *via the links* belong to AWS Accounts and AWS Artifact and are addressed in §7.

---

## 5. Recommended Areas of Focus
No EC2 lens fires on this page. The three cross-service leads below are recorded so a hunter targeting *those* services has the pointer — but each is **explicitly out of scope for the EC2 compliance-validation target** and must be routed to the owning service's own plan, not pursued here.

### Area X-1 (cross-service, AWS Accounts) — "not designed for regulated workloads" as advisory-vs-enforced (Lens U)
- **Background:** S1 states the "new AWS sign-up experience is not designed for regulated workloads" and directs regulated users to "sign up for AWS (advanced)" or "activate advanced features."
- **Security Concern:** Is "not designed for regulated workloads" an *enforced* control (does a new-sign-up account have EC2/compliance capabilities actually withheld or gated?) or purely **advisory prose** with no mechanism behind it? If a compliance control is built on the assumption that a "basic" account cannot run regulated workloads but EC2 APIs behave identically regardless of sign-up tier, the guarantee is advisory-only.
- **High-level Test Scenarios (lead L1):** **Claim:** a "new sign-up experience" account can call the same EC2 control-plane APIs with the same authorization as an "advanced" account (i.e. the distinction gates *features/billing/support*, not EC2 API authorization). → **Mechanism:** S1 prose; no IAM condition key for sign-up tier exists in `list_ec2.md`. → **Oracle:** compare `DescribeAccountAttributes` / EC2 RunInstances authorization across the two tiers; absence of any `aws:` or `ec2:` condition key keyed on sign-up tier = advisory-only. → **Severity-if-true:** Informational (doc-vs-enforcement), **AWS Accounts-owned, not EC2.**
- **Doc evidence:** S1. **Routing:** AWS Accounts, not this plan.

### Area X-2 (cross-service, AWS Artifact) — report-download authorization scoping (Lens A / S / P)
- **Background:** S3 → `artifact:GetReport` downloads third-party audit reports; authorization is scoped by `artifact:ReportCategory` and `artifact:ReportSeries` condition keys over resource type `report*` (`list_artifact.md`), and `artifact:GetTermForReport` gates an NDA/term acceptance.
- **Security Concern:** AWS Artifact reports are **AWS-published global artifacts, not customer data** — so cross-*tenant* disclosure is not the risk. The real question is whether the term/NDA acceptance gate (`GetTermForReport`) is actually required before `GetReport`, and whether `ReportCategory`/`ReportSeries` conditions bind what a least-privilege policy intends (Lens S presence-vs-ownership — but "ownership" is moot since reports are not account-scoped).
- **High-level Test Scenarios (lead L3):** **Claim:** `GetReport` succeeds without the corresponding term acceptance, or a policy scoped to one `ReportSeries` reaches another. → **Oracle:** `iam:SimulateCustomPolicy` on a report-series-scoped policy; live call under a scoped role with canary. → **Severity-if-true:** Low (non-customer-data agreement bypass), **AWS Artifact-owned, not EC2.**
- **Doc evidence:** S3 + `list_artifact.md`. **Routing:** AWS Artifact, not this plan.

### Area X-3 — shared-responsibility prose (Lens U null)
- S4 is pure shared-responsibility boilerplate pointing at `docs.aws.amazon.com/security/`. No mechanism, no guarantee with an enforcement surface. Null.

---

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| (none for EC2) | — | The page documents no EC2 mitigation to attack; it points to attestation evidence and account posture only. |
| advisory-vs-enforced regulated-workload gate | AWS Accounts (not EC2) | S1 prose — no IAM mechanism; test is Lens U doc-vs-enforcement, routed to AWS Accounts |
| report-download term/scope gate | AWS Artifact (not EC2) | `artifact:ReportCategory`/`ReportSeries` + `GetTermForReport`; routed to AWS Artifact |

---

## 7. Out-of-Scope Risk Categories (stated as confidently as in-scope)
- **The entire page's technical substance is cross-service.** AWS Accounts sign-up posture (S1), the compliance-program marketing portal (S2), AWS Artifact report download (S3), and the shared-responsibility model (S4) are **not EC2 surface** and must not be pursued under the EC2 target. Any finding there is reported against the owning service, not EC2.
- **AWS Artifact reports are AWS-published global compliance artifacts, not customer data** — do not frame report access as a cross-tenant IDOR; there is no per-account report ownership to breach.
- **Shared-responsibility / attestation-program membership** ("is EC2 in scope for PCI/SOC/HIPAA") is an AWS Compliance organizational attestation, not a technical control with an enforcement mechanism to attack. Out of scope.
- **EC2 snapshot-lock compliance mode** (`ec2:LockSnapshot`, `ec2:SnapshotCoolOffPeriod`) is EC2's only "compliance"-named IAM surface but is **not referenced by this page** and is already covered by the data-protection and disaster-recovery-resiliency plans — do not duplicate.
- Standard managed-host carve-outs apply but are moot here: there is no host, parser, fetch, upload, token, cache, or network path on this page.

---

## 8. Null hypotheses / doc gaps (pages named per skill discipline)
Pages read to adjudicate these nulls: `AWSEC2/.../compliance-validation.md` (full), `list_ec2.md` (grepped `compliance`), `list_artifact.md` (full action/condition-key list), EC2 Security-chapter sibling listing, and five peer-service `compliance-validation.md` copies to confirm the template is boilerplate.

| Lens | Verdict | Why null (pages checked) |
|---|---|---|
| A (IDOR / cross-tenant) | **NULL** | No EC2 resource, ID, or resource-by-ID API on the page. Artifact reports aren't account-scoped. |
| B / C (PassRole / vending) | **NULL** | No role ARN, no AssumeRole, no credential input on the page or its EC2 surface. |
| D / V (data→control / segmentation) | **NULL** | No ENI, VPC, control plane, or fleet described. |
| E (RBAC privesc) | **NULL** | No role model on the page. |
| F (injection) | **NULL** | No parser/translator; page accepts no input. |
| G (SSRF) | **NULL** | No field the service dereferences. Page read in full; the four links are static anchor hrefs, not server-side-fetched values. |
| H (KMS/enc-context) | **NULL** | No KMS mention. (Snapshot-lock compliance mode handled in other plans.) |
| I / S (tagging / condition-key) | **NULL for EC2**; thin for Artifact | No EC2 tag/condition surface. Artifact's `ReportCategory`/`ReportSeries` noted as X-2 (out of scope). |
| J (OAuth/3P) | **NULL** | No 3P linking. |
| K (prompt injection) | **NULL** | No LLM/agent. |
| L (DoS) | **NULL** | No parser/limit/shared fleet on the page. |
| M (shared-id interception) | **NULL** | No session/token/presigned URL. |
| N (namespace migration) | **NULL** | No ARN/namespace change. |
| O (audit-log evasion) | **NULL** | No operation to log. |
| P (proofing/registration) | **thin, cross-service** | S1 sign-up-tier gate → X-1 (AWS Accounts). Artifact term acceptance → X-2 (Artifact). Neither is EC2. |
| Q (upload) | **NULL** | No upload/media field. |
| R (IAM-artifact audit) | **NULL** | No IAM policy JSON, managed policy, SLR, CFN, or runbook block printed on the page. |
| T (secret reachability) | **NULL** | Page generates/persists no secret. |
| U (doc-vs-enforcement) | **fires only cross-service** | "Not designed for regulated workloads" (S1) is the sole guarantee-word; its mechanism is AWS Accounts posture, not EC2 → X-1. "Compliance responsibility" (S4) is shared-responsibility prose with no enforcement surface. |
| W (attestation-conditioned authz) | **NULL** | No Nitro/enclave/PCR attestation on this page (distinct from the NitroTPM attestation surface in the ec2-security hub plan). |
| X (action-family parity) | **NULL** | No action family on the page. |
| Y (transport/TLS/sig) | **NULL** | No endpoint/signature surface. |
| AA (share/revoke lifecycle) | **NULL** | No share/grant. |
| BB / CC / DD (canonicalization / upstream-context / cache) | **NULL** | No multi-parser request path, no authorizer, no cache on the page. |
| EE (predictable-name land-grab) | **NULL** | No service-resolved predictable namespace. |
| FF (token/claims validation) | **NULL** | No JWT/OIDC/Cognito surface. |

**Doc gap:** none. The page is complete, stable, and intentionally thin; the NULL verdict is a true null (template boilerplate), not an unexamined-surface false negative. No surface here needs "confirm surface first" — there is confirmed to be no surface.

---

## Summary for the next agent
`compliance-validation.html` for EC2 is a **templated boilerplate pointer page with zero EC2 attack surface.** Do not spend hunter time against the EC2 target here. The only investigable mechanisms are cross-service and belong to **AWS Accounts** (sign-up-tier advisory-vs-enforced, X-1) and **AWS Artifact** (report-download term/scope gate, X-2) — route those to those services' own plans. EC2's genuine "compliance mode" surface is snapshot-lock (`ec2:SnapshotCoolOffPeriod`), which is on *other* pages and already planned (data-protection, disaster-recovery-resiliency). This plan exists to close the page with a defensible, page-named NULL and the correct cross-service attributions.
