# Verify NitroTPM support on an AMI — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/verify-nitrotpm-support-on-ami.html` (= `.md` twin; offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/verify-nitrotpm-support-on-ami.md`), cross-checked against the Service Authorization Reference `list_ec2.md` (`/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`) and the EC2 API Reference. **Status: documentation-derived hypotheses only; nothing tested against a live account.** Offline == online byte-identical 2026-10-15 (incl. the PowerShell doc defect in Area 6).

> This plan is the **READ/VERIFY-surface COMPLEMENT** of the NitroTPM cluster. It is scoped to the *single verification page* and deliberately does NOT restate its siblings — it cross-references them:
> - **`nitrotpm-attack-research-plan.md`** (hub complement) — owns `GetInstanceTpmEkPub`, `RegisterImage --tpm-support v2.0` enablement, whoAMI Windows name-filter, BitLocker sealing, cross-acct AMI share.
> - **`nitrotpm-attestation-attack-research-plan.md`** — owns KMS/PCR/replay/COSE/CRL/attestation-gate depth.
> - **`enable-nitrotpm-prerequisites-attack-research-plan.md`** — owns launch-prerequisite IAM-inexpressibility, static instance-type-list drift, BitLocker/snapshot silence, unverified Secure-Boot `.ps1`.
> This page is where a consumer **reads** the `TpmSupport` flag back. Its net-new surface is the **read-path scopability asymmetry** between the two documented commands, the **"verify" = read-a-self-asserted-flag** integrity gap, and the **console blind spot** that forces API-only verification.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The two safe first oracles here are **read-only and resource-free**: `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (settles every condition-key-scopability claim with no resource created), and a plain `describe-images` / `describe-image-attribute` read against a **synthetic self-owned canary AMI** plus a **public** AMI. No AMI is ever created, modified, launched, or shared beyond canary scope.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected on this read-only page.)

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Read the NitroTPM-enablement fact (`TpmSupport=v2.0`) of an AMI the caller does not own** — a public AMI, an AMI shared to the account, or (stretch) another tenant's private AMI — via the **IAM-unscopable** `DescribeImages` path, where an admin intended that fact be gated.
2. **Prove an admin cannot restrict visibility of NitroTPM status** of their own/their org's AMIs: show that the only command that carries scoping keys (`DescribeImageAttribute`) is bypassed by the page's *primary*, unscopable command (`DescribeImages`).
3. **Enumerate NitroTPM-enabled AMIs across the visible catalog** (public + shared + self) with the `tpm-support` filter run without an owner pin — a recon oracle for targeting NitroTPM/attestation-dependent workloads.
4. **Show "verify" is not assurance** — that the documented verification reads a **self-declared `RegisterImage` flag** with no attestation of a functioning TPM, so a consumer "verifying" a third-party/shared AMI trusts the publisher's claim (whoAMI chain).
5. **Quantify the console blind spot** — confirm CLI/API is the sole verification path and what a console-only auditor cannot see.

---

## 2. Components, Assets, and Design

**Interface.** Read-only EC2 control-plane APIs over SigV4 HTTPS. Two documented verification commands + a discovery command, each in AWS CLI and Tools-for-PowerShell form:

| Command (CLI) | Underlying API | What it returns re: NitroTPM | Page framing |
|---|---|---|---|
| `describe-images --image-ids <id> --query Images[*].TpmSupport` | `ec2:DescribeImages` | `TpmSupport` string (`"v2.0"` or empty) inside the `Images[]` list | **Primary** verify command; no owner caveat |
| `describe-image-attribute --image-id <id> --attribute tpmSupport` | `ec2:DescribeImageAttribute` | `{"TpmSupport":{"Value":"v2.0"}}` | **"if you are the AMI owner"** |
| `describe-images --owners self --filters Name=tpm-support,Values=v2.0 --query Images[].ImageId` | `ec2:DescribeImages` | list of IDs of NitroTPM AMIs | "the AMIs **that you own**" |

**Asset under contention.** The `TpmSupport` image attribute — a per-AMI metadata string whose only legal value is `v2.0`. It is **set at registration** (`RegisterImage --tpm-support v2.0`, see `enable-nitrotpm-support-on-ami.md:12,44`; `RegisterImage` is the *only* enablement path — not console, not VM Import/Export), **immutable thereafter**, and **invisible in the EC2 console** (`verify-nitrotpm-support-on-ami.md`: "The Amazon EC2 console does not display `TpmSupport`."). It is therefore readable only through the three commands above.

**Identifier shape.** `ami-<17 hex>` — not fabricable blind (so cross-account IDOR by guessing an id is a genuine partial-null), but public/shared AMI IDs are freely discoverable via `DescribeImages` itself (and the `tpm-support` filter), so the "need a valid id" precondition is trivially met for the public/shared catalog.

**Trust zones.** AMI-owner account ↔ consumer accounts (via `launchPermission`: explicit share, org/OU share, or **public**). The verification page sits entirely on the **consumer read path** — the one place a would-be launcher inspects an AMI's security posture before trusting it.

```
                    RegisterImage --tpm-support v2.0   (owner, self-asserted; no attestation)
                                 │
                                 ▼
                       ┌───────────────────┐
   AMI owner acct ───► │  AMI.TpmSupport    │  (immutable, console-hidden)
                       │   = "v2.0"         │
                       └─────────┬─────────┘
         launchPermission (explicit / org / PUBLIC)
                                 │
          ┌──────────────────────┼───────────────────────┐
          ▼                      ▼                         ▼
  describe-image-attribute   describe-images         describe-images
   --attribute tpmSupport    --image-ids <id>        --filters tpm-support
   [SCOPABLE: image*,         [UNSCOPABLE:            [UNSCOPABLE + omit
    ec2:Owner, ec2:Public,     region-only]           --owners = catalog
    ec2:ImageID, tag]                                  enumeration oracle]
          │                      │                         │
          ▼                      ▼                         ▼
     "owner only"          returns TpmSupport        enumerate all NitroTPM
     (page claim)          to anyone who can          AMIs the caller can see
                           see the image
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Low-priv principal in acct A (admin tried to hide NitroTPM posture) | `TpmSupport` of A's own AMIs | `ec2:DescribeImages` (region-only, no `image` resource type) | A `describe-images` call returns `TpmSupport` for an AMI the admin's Deny/scoping was meant to withhold — **because no condition key can bind it** |
| Consumer in acct B | `TpmSupport` of a **public** or **B-shared** AMI owned by acct A | `ec2:DescribeImages` on a visible foreign AMI | B reads A's AMI NitroTPM-enablement fact via `DescribeImages` where the "owner-only" attribute path (`ec2:Owner`) would deny |
| Any principal (recon) | the whole visible NitroTPM AMI catalog | `describe-images --filters Name=tpm-support,Values=v2.0` **without `--owners`** | A single filtered call returns foreign/public NitroTPM AMI IDs = a targeting list for attestation/BitLocker-dependent workloads |
| Consumer "verifying" a 3rd-party AMI | the trust decision "this AMI has a real TPM" | reading a self-asserted `RegisterImage` flag | `TpmSupport=v2.0` is present on an AMI whose image was **not** attested — the reader trusts a publisher-set string (whoAMI shape) |

---

## 4. API / Interface Inventory

| Name | Mutating | Resource type (list_ec2) | Condition keys (list_ec2) | Callable by | Notes |
|---|---|---|---|---|---|
| `ec2:DescribeImages` | No (List) | **(blank)** | **`ec2:Region` ONLY** | anyone who can see the image (self/amazon/aws-marketplace/shared/**public**) | Page's **primary** verify command; returns `TpmSupport` in `Images[]`; `tpm-support` filter; **fully IAM-unscopable** |
| `ec2:DescribeImageAttribute` | No (List) | **`image*` (required)** | `aws:ResourceTag`, `ec2:ImageID`, `ec2:ImageType`, **`ec2:Owner`**, **`ec2:Public`**, `ec2:Region`, `ec2:ResourceTag`, `ec2:RootDeviceType` | page says "**if you are the AMI owner**" | `--attribute tpmSupport`; fully scopable — the asymmetric twin |

Confirmed condition-key definitions (`list_ec2.md`): `ec2:Owner` = "Filters access by the owner of the resource (amazon, aws-marketplace, or an AWS account ID)" (String, l.10119); `ec2:Public` = "Filters access by whether the image has public launch permissions" (Bool, l.10135). **Neither is available on `DescribeImages`.** No `ec2:TpmSupport` / `ec2:NitroTpm` condition key exists anywhere in `list_ec2.md` (0 hits — consistent with the hub & prerequisites plans: enablement is not value-gatable, and now confirmed the *read* of it is not scopable either).

---

## 5. Recommended Areas of Focus

### Area 1 — HEADLINE: `DescribeImages` is an IAM-unscopable NitroTPM read oracle; the page's own primary command bypasses the "owner-only" scopable path (Lens X / U / A / S)
**Background.** The page documents TWO ways to read the same `TpmSupport` fact and frames the attribute path as owner-restricted ("If you are the AMI owner, you can describe the `tpmSupport` image attribute"). But the **first, preferred, un-caveated** command is `describe-images --query Images[*].TpmSupport`, backed by `ec2:DescribeImages`, which in `list_ec2.md` has a **blank resource type and only `ec2:Region`** — it cannot be scoped by image, owner, public-flag, image-type, or tag. The scopable keys (`ec2:Owner`, `ec2:Public`, `ec2:ImageID`, `aws:ResourceTag`) exist **exclusively** on `DescribeImageAttribute`.

**Security Concern.** An org that wants to control *who can see which of its AMIs are NitroTPM-enabled* (e.g. to avoid revealing which golden images back attestation/BitLocker-gated workloads) **has no IAM lever on the path the docs tell everyone to use.** Any principal holding `ec2:DescribeImages` (an extremely common, often wildcard-granted read permission) reads `TpmSupport` for every AMI it can see. This is the same unscopable-read-oracle shape as the `describe-keys` sibling (`DescribeKeyPairs` blank + `ec2:Region`-only) and `manage-spot-fleet` (`DescribeSpotFleetRequests`) — inert-ABAC: a `Deny` keyed on `ec2:Owner`/`aws:ResourceTag` attached to `DescribeImages` **never fires** because the key is absent (silent fail-open on a "restrict NitroTPM visibility" mandate).

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** `iam:SimulateCustomPolicy` for `ec2:DescribeImages` with a `Condition` on `ec2:Owner`, `ec2:Public`, `ec2:ImageID`, or `aws:ResourceTag` evaluates the condition as **inapplicable/ignored** (the key is not in context) → the statement is effectively unconditioned. → **Oracle:** simulate `allowed` regardless of the condition value; contrast with the same condition on `DescribeImageAttribute` where it binds. Settles with zero resources.
- **Claim:** a scoped role holding `ec2:DescribeImages` but **explicitly Denied `ec2:DescribeImageAttribute`** still reads `TpmSupport` of a target AMI via `describe-images --query Images[*].TpmSupport`. → **Oracle:** run both calls under the scoped role against a self-owned canary AMI; the attribute call is `AccessDenied`, the images call returns `"v2.0"`.
- **Claim:** the two commands return the **same** fact, so the "owner-only" framing of the attribute path provides **no confidentiality** for the fact itself. → **Oracle:** diff the `TpmSupport` value from both commands on one AMI.

**Doc evidence:** `verify-nitrotpm-support-on-ami.md` (both commands); `list_ec2.md` DescribeImages row (l.6906–6910, blank resource type + `ec2:Region`) vs DescribeImageAttribute row (l.6882–6886, `image*` + 8 keys). **Severity-if-true:** Low–Medium (intra-account visibility footgun that is **AWS-owned** — the absence of a scopable key on `DescribeImages` is an AWS schema fact, not a customer policy error; file as the doc-vs-enforcement inconsistency, Lens U). Elevated to Medium where the NitroTPM-posture of golden images is itself sensitive recon.

### Area 2 — Non-owner reads a foreign/public/shared AMI's NitroTPM status via `DescribeImages` (Lens A — cross-boundary read / disclosure-timing)
**Background.** `DescribeImages` returns the `Images[]` list — including `TpmSupport` — for every AMI the caller can "see": self, `amazon`, `aws-marketplace`, AMIs shared to the account via `launchPermission`, and **public** AMIs. The scopable twin `DescribeImageAttribute` is framed owner-only.

**Security Concern.** The NitroTPM-enablement fact of **another account's** AMI (public, or shared to the caller) is disclosed to a party the "owner-only" attribute path would refuse. For a defender this is low-value in isolation, but it is the **recon primitive** that makes Area 4 (whoAMI trust) targeted: an attacker learns exactly which third-party/shared AMIs claim NitroTPM before deciding which to impersonate or substitute.

**High-level Test Scenarios:**
- **Claim:** acct B, with no relationship to acct A beyond a public or B-shared A-owned AMI, reads that AMI's `TpmSupport` via `describe-images --image-ids <A's ami>`. → **Oracle:** from B, `describe-images` the public AMI id; `TpmSupport` present. (Needs the API to return the field to non-owners — see subagent follow-up / DOC-GAP below.)
- **Claim:** `DescribeImageAttribute --attribute tpmSupport` is genuinely owner-restricted at the **API** level for a non-owner on a public/shared AMI (i.e. the asymmetry is real, not just an IAM-key artifact). → **Oracle:** from B, attempt the attribute call on A's public AMI → expect `AuthFailure`/`AccessDenied` while `describe-images` succeeds.

**CONFIRMED (doc-level, subagent):** `API_DescribeImages.md` — "The images available to you include public images, private images that you own, and private images owned by other AWS accounts for which you have explicit launch permissions"; `API_Image.md` l.212–213 defines `tpmSupport` with **no owner caveat** → `DescribeImages` returns `TpmSupport` to any non-owner who can see the image (public via `--executable-users all`; shared via `--executable-users self`), documented as ordinary unrestricted calls (`usingsharedamis-finding.md`). **Sharpening (Lens U doc-vs-API):** the "owner-only" restriction on `DescribeImageAttribute` exists **only in UserGuide prose — `API_DescribeImageAttribute.md` has NO "Required permissions" section and states no owner restriction / error contract anywhere.** So the asymmetry a defender relies on is itself undocumented at the API layer and must be live-confirmed (does the attribute call actually deny a non-owner, or does the prose over-promise?).

**Doc evidence:** `verify-nitrotpm-support-on-ami.md`; `API_DescribeImages.md`; `API_Image.md:212`; `API_DescribeImageAttribute.md` (owner-restriction absent). **Residual live check:** confirm the attribute call's *actual* non-owner behavior (deny vs allow) — one cross-account pair of calls against a public NitroTPM AMI. **Severity-if-true:** Low (cross-account metadata disclosure of a posture flag; Medium as a chain enabler to Area 4). If `DescribeImageAttribute` turns out NOT to deny non-owners either, the "owner-only" doc framing is a Lens U over-promise worth filing on its own.

### Area 3 — `tpm-support` catalog-enumeration oracle (Lens U authenticity-filter-omission / Lens A)
**Background.** The discovery example pairs the `tpm-support` filter with `--owners self`. But `--owners self` is the *example author's* choice, not a constraint of the filter. `DescribeImages` with `--filters Name=tpm-support,Values=v2.0` and **no `--owners`** applies the filter across the caller's default visible scope (which includes public + shared AMIs; by default `DescribeImages` without owners can return a very large public set).

**Security Concern.** A single unauthenticated-to-the-owner call enumerates **all NitroTPM-enabled AMIs the caller can see** — a ready-made targeting list for workloads that depend on NitroTPM attestation/BitLocker, and the enumeration half of the whoAMI chain (which public NitroTPM AMIs exist, by whom, with what names).

**CONFIRMED + NET-NEW doc defect (subagent):** `--executable-users all` makes `DescribeImages` enumerate the **entire public AMI catalog**; pairing it with `--filters Name=tpm-support,Values=v2.0` yields every public NitroTPM AMI across all owners in one call (omitting `--owners`/`Owner.N` broadens, never narrows, scope). **NET-NEW Lens U doc-vs-API gap:** the `tpm-support` filter is **NOT listed in the `Filter.N` catalog of `API_DescribeImages.md`** (nor in the CLI `describe-images --filters` reference) — it is documented as a valid filter only on `DescribeInstances`. The tutorial on this page uses a `DescribeImages` filter that the `DescribeImages` API reference does not acknowledge: the tutorial outruns the API contract, so the filter's exact match semantics and default scope are unspecified by the authoritative reference and must be live-confirmed.

**High-level Test Scenarios:**
- **Claim:** `describe-images --filters Name=tpm-support,Values=v2.0` **without** `--owners` returns foreign/public AMI IDs (not just self). → **Oracle:** run the filter with no owner pin; count results with `OwnerId != self`.
- **Claim:** `describe-images --executable-users all --filters Name=tpm-support,Values=v2.0` returns the global public NitroTPM inventory. → **Oracle:** run it; count distinct `OwnerId`.
- **Claim:** the filter + `--owners amazon`/`aws-marketplace` reveals which *vendor* images claim NitroTPM. → **Oracle:** vary `--owners`; observe the vendor NitroTPM inventory.

**Doc evidence:** `verify-nitrotpm-support-on-ami.md` ("find AMIs" example); `API_DescribeImages.md` (`Filter.N` list — `tpm-support` **absent**; `--executable-users all` documented for public enumeration). **Severity-if-true:** Low–Medium (recon amplifier; its value is as the delivery scope for Area 4). The undocumented-filter gap is additionally an Informational Lens U doc defect worth filing on its own.

### Area 4 — "Verify" reads a self-asserted flag, not an attestation (Lens U / EE — whoAMI trust chain)
**Background.** The page's verb is **"verify."** But `TpmSupport=v2.0` is set by whoever runs `RegisterImage --tpm-support v2.0` (`enable-nitrotpm-support-on-ami.md:12,44`; the hub plan's HEADLINE: enablement is IAM-ungatable *by value* and is self-asserted). There is **no cryptographic binding** between the flag and the presence of a functioning NitroTPM in the image — the flag is a publisher-set metadata string. (Actual attestation lives at *launch/runtime* via `GetInstanceTpmEkPub` + the attestation-sibling's KMS/PCR gate, not at AMI-describe time.)

**Security Concern.** A consumer who follows this page to "verify" a **shared or public third-party AMI** before launching an attestation/BitLocker-dependent workload is trusting the AMI *publisher's* self-declaration. Combined with the known whoAMI name-filter risk (hub plan: Windows `TPM-Windows_Server-*` lookups without `--owners amazon`), an attacker who publishes an AMI with `TpmSupport=v2.0` and a plausible name can have a victim "verify" and adopt it. The page offers **no warning** to owner-pin third-party NitroTPM AMIs.

**High-level Test Scenarios:**
- **Claim:** a self-registered canary AMI carrying `TpmSupport=v2.0` on a root volume that does **not** actually provide a working TPM still reports `v2.0` to every reader of this page's commands — i.e. "verify" confirms the flag, not the capability. → **Oracle:** register a canary with `--tpm-support V20`, read it back via both commands; the flag is present irrespective of real TPM function. (Register under canary account only.)
- **Claim:** no NitroTPM doc (this page, `enable-nitrotpm-support-on-ami`, `enable-nitrotpm-prerequisites`, `nitrotpm`) tells the consumer to owner-pin third-party NitroTPM AMIs or warns the flag is self-asserted. → **Oracle:** doc grep (settles immediately). Chains to hub-plan whoAMI Area and attestation-sibling 3rd-party-verifier-trust gap.

**CONFIRMED (subagent):** `TpmSupport` is caller-supplied at `RegisterImage` with no validation that the image actually contains working TPM support; there is no attestation at describe time. The generic AMI-trust guidance *does* exist (`usingsharedamis-finding.md` recommends sourcing from trusted publishers / `--owners amazon aws-marketplace`), but it is **never cross-referenced from any NitroTPM page** — a consumer who lands on the "verify" page is given no pointer to it, and the term "whoAMI" appears nowhere in AWS docs. The verify page thus frames an untrusted self-asserted read as "verification" with no adjacent warning.

**Doc evidence:** page title/intro verb "verify"; `enable-nitrotpm-support-on-ami.md:12,44`; `usingsharedamis-finding.md` (uncross-referenced owner-pin guidance); cross-ref `nitrotpm-attack-research-plan.md` (RegisterImage self-assertion, whoAMI) and `nitrotpm-attestation-attack-research-plan.md` (no EK cert chain → verifier trust gap). **Severity-if-true:** Medium (misplaced-trust / provisioning-integrity; the real breach is realized at launch, owned by the attestation + hub plans — this page is the *entry point* that frames the untrusted read as "verification").

### Area 5 — Console blind spot forces API-only verification (Lens O / U — observability)
**Background.** "The Amazon EC2 console does not display `TpmSupport`." The only verification path is CLI/API/PowerShell.

**Security Concern.** A console-only operator or auditor **cannot** see or verify NitroTPM status at all — compounding the prerequisites-plan Area 5 / attestation-plan Area 7 finding that NitroTPM state is console-invisible. Every silent-downgrade outcome in the sibling plans (snapshot/VM-Import drops `TpmSupport`; restored AMI silently lacks it; resize to a non-NitroTPM type) is therefore **invisible to the one tool most operators use**. Detection of a NitroTPM regression depends on someone running the right CLI query.

**CONFIRMED + EXTENDED (subagent):** the console blind spot is restated at the **instance** level too — `verify-nitrotpm-support-on-instance.md` (line ~10) says the instance's NitroTPM state is likewise not shown in the console and must be read via CLI/in-guest tooling; the prerequisites page restates it a third time. So neither the AMI's nor the running instance's NitroTPM posture is visible in the console, and in-guest tooling (`tpm2-tools`, Windows `Get-Tpm`) is the only alternative verification surface. Whether **AWS Config / Resource Explorer** expose `TpmSupport` remains a true DOC-GAP (no doc affirms or denies it) — the one residual item on this page.

**High-level Test Scenarios:**
- **Claim:** no console view, AWS Config rule, or Resource Explorer attribute surfaces `TpmSupport`, so an inventory/compliance control built in the console is blind to NitroTPM posture. → **Oracle:** check whether a Config managed rule / Resource Explorer attribute surfaces it (residual DOC-GAP — not resolvable from docs alone; one live check in a canary account settles it).
- **Claim:** the `DescribeInstances` / instance console view does not surface the *instance's* effective NitroTPM state either. → **Oracle:** CONFIRMED doc-side (`verify-nitrotpm-support-on-instance.md`); live-confirm the `DescribeInstances` field set once.

**Doc evidence:** `verify-nitrotpm-support-on-ami.md` ("The Amazon EC2 console does not display `TpmSupport`."); `verify-nitrotpm-support-on-instance.md` (~l.10, instance-level restatement); `enable-nitrotpm-prerequisites.md` (third restatement). **Severity-if-true:** Low (detection/assurance gap; enabler, not a direct breach).

### Area 6 — Copy-verbatim PowerShell doc defect (Lens U / R — shipped artifact integrity, Informational)
**Background.** The PowerShell "find AMIs" example prints `-Filter @{Name="tpm-support; Values="v2.0"}` — the hashtable literal has **broken quoting**: a missing closing quote after `tpm-support`. The correct form is `@{Name="tpm-support"; Values="v2.0"}`. Confirmed **byte-identical in offline mirror and online** 2026-10-15 (genuine live defect, not a mirror artifact).

**Security Concern.** Low direct risk, but it is an AWS-authored copy-verbatim snippet that **fails to parse / silently mis-parses** on paste — a reader may silently get wrong/empty results from the *security-verification* command and conclude an AMI lacks NitroTPM (or vice-versa). Flag as a doc-integrity defect (the one place this page could mislead a diligent operator).

**High-level Test Scenarios:**
- **Claim:** pasting the snippet verbatim throws a PowerShell parse error or binds `Name` incorrectly, so the verification returns a misleading result. → **Oracle:** parse the literal (static; settles immediately — the mismatched quotes are self-evident).

**Doc evidence:** `verify-nitrotpm-support-on-ami.md` PowerShell block. **Severity-if-true:** Informational (AWS-owned doc defect in a verification artifact).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Read own-AMI NitroTPM posture despite a scoping Deny | `ec2:DescribeImages` | "owner-only attribute" framing — **bypassed**; no `image`/`ec2:Owner` key on DescribeImages |
| Cross-account read of a public/shared AMI's `TpmSupport` | `ec2:DescribeImages` vs `DescribeImageAttribute` | attribute path owner-restriction — asymmetric vs the images path |
| Enumerate the visible NitroTPM AMI catalog | `tpm-support` filter without `--owners` | example uses `--owners self` (not enforced) |
| Trust a self-asserted `TpmSupport` flag on a 3rd-party AMI | "verify" wording + RegisterImage self-assertion | **none** — no attestation at describe time, no owner-pin warning |
| Console-only auditor misses NitroTPM regression | console vs CLI | "console does not display TpmSupport" (documented, unmitigated) |
| Mis-parse the verification command | PowerShell snippet | broken-quote defect, unmitigated |

---

## 7. Out-of-Scope Risk Categories
- **Attestation / KMS / PCR / replay / EK-cert / COSE / CRL depth** → `nitrotpm-attestation-attack-research-plan.md`.
- **`RegisterImage --tpm-support` enablement, `GetInstanceTpmEkPub`, cross-acct AMI share, Windows whoAMI name-filter mechanism** → `nitrotpm-attack-research-plan.md` (hub). This plan only consumes the whoAMI *entry point* framing.
- **Launch-prerequisite IAM-inexpressibility, instance-type-list drift, BitLocker/snapshot silent downgrade, Secure-Boot `.ps1`** → `enable-nitrotpm-prerequisites-attack-research-plan.md`.
- **Blind cross-account IDOR by fabricating `ami-<17hex>`** — not feasible (id not fabricable; and the real exposure is of *visible* public/shared AMIs, which needs no guessing). Genuine partial-null.
- Shared Nitro hardware / NitroTPM silicon isolation, the shared-responsibility line (**HARD STOP**), single-tenant self-DoS.

---

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens B/C (PassRole / vending):** N/A — no role ARN, token, or credential field on this read-only page (read: full page).
- **Lens G (SSRF):** N/A — the only URLs are doc hyperlinks to the CLI/PowerShell reference; no field the service dereferences (read: full page).
- **Lens Q (upload):** N/A — no blob/file input (read: full page).
- **Lens H (KMS):** N/A on this page — `TpmSupport` read carries no encryption context (KMS/BitLocker-sealing owned by prerequisites + attestation plans).
- **Lens F / V / D / W / BB / CC / DD / FF:** N/A — single-call read API, no translation layer, no network segmentation surface, no attestation gate *on this page* (W fires at launch, owned by attestation sibling), no multi-parser path, no asserted-upstream-context, no cache config, no JWT (read: full page + list_ec2 rows).
- **DOC-GAPs — status after subagent doc deep-dive (`a798de670583689af`):**
  1. **RESOLVED (doc-level):** `API_DescribeImages.md` + `API_Image.md:212` confirm `DescribeImages` returns `TpmSupport` to any non-owner who can see a public/shared AMI, with no owner caveat. The *asymmetry* is real at the doc layer **but** `API_DescribeImageAttribute.md` has **no "Required permissions" section and documents no owner restriction** — the "owner-only" claim is UserGuide prose only. Residual: one live cross-account pair of calls to confirm the attribute call's actual deny behavior (Area 1/2).
  2. **RESOLVED + sharpened:** `--executable-users all` enumerates the full public catalog; omitting `--owners` broadens scope. **NET-NEW:** the `tpm-support` filter is **absent from `API_DescribeImages.md`'s `Filter.N` list** (documented only for `DescribeInstances`) — tutorial outruns the API reference; live-confirm match semantics (Area 3).
  3. **PARTIALLY RESOLVED:** instance-level console blind spot CONFIRMED (`verify-nitrotpm-support-on-instance.md`). Whether **AWS Config / Resource Explorer** expose `TpmSupport` is the sole **true remaining DOC-GAP** — unanswerable from docs; one canary-account check settles it (Area 5).

No `ec2:TpmSupport`/`ec2:NitroTpm` condition key exists in `list_ec2.md` (grep: 0 hits) — confirms both enablement (hub) and now *read-scoping* of NitroTPM status are not IAM-expressible.

**Subagent-confirmed summary (doc-level, not live):** (1) `DescribeImages` leaks `TpmSupport` to non-owners; the `DescribeImageAttribute` owner-restriction is UserGuide-prose-only, absent from the API reference. (2) Neither `ec2:Owner` nor `ec2:Public` is on `DescribeImages`. (3) `--executable-users all` + `tpm-support` filter = global public-catalog NitroTPM enumeration; the filter is undocumented in the `DescribeImages` API `Filter.N` catalog. (4) `TpmSupport` is self-asserted at `RegisterImage`, no attestation; no NitroTPM page cross-references the owner-pin guidance in `usingsharedamis-finding.md`; "whoAMI" absent from AWS docs. (5) Console blind spot confirmed at AMI **and** instance level; Config/Resource-Explorer coverage is the only true residual gap. (6) The PowerShell broken-quote defect is byte-identical online and offline (live defect).
