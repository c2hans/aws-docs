# EC2 "Test whether enhanced networking is enabled" — Attack Research Plan

Source of leads: `test-enhanced-networking-ena.html` (the single verification/read-surface page) + the IAM Service Authorization Reference `list_ec2.md` (offline mirror `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`). Status: documentation-derived hypotheses only; nothing tested against a live account. Target page re-verified **offline==online byte-identical 2026-10-15** (WebFetch of the `.md` twin == `docs/AWSEC2/latest/UserGuide/test-enhanced-networking-ena.md`).

**This is a page-level READ-SURFACE child/complement of `enhanced-networking-attack-research-plan.md`** (the ENA / SR-IOV / ENA-Express hub-child plan, which already lists this page as a lead source). The parent owns the full **write/enable surface** — `ModifyInstanceAttribute`/`RegisterImage` enablement, `sriovNetSupport` irreversibility (Area 5), ENA-Express `EnaSrdSpecification` three-path unscopability (Area 1), SRD-vs-inspection (Area 3), driver-install Lens-R audit (Area 6), metrics side-channel (Area 7), and a *summary-level* read-oracle note (Area 4b, scoped to the **single-attribute** `DescribeInstanceAttribute`/`DescribeImageAttribute`). This complement develops **only** the read/verification surface this specific page documents — the **bulk** `DescribeInstances`/`DescribeImages` read oracle, the client-side `--query` false-scoping tell, the control-plane-attribute-vs-actual-driver attestation gap, and the in-guest `ethtool` audit-blindspot — and **cross-references, does not restate,** the parent's write-side leads. Where this plan and the parent both touch the read oracle, this plan **sharpens** parent Area 4b (see Area 1 reconciliation).

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order.
- The safe first oracle for every IAM-scopability lead is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (no resource touched).
- **`DryRunOperation` is caller-IAM-only, NOT an ownership oracle.** (Describe actions here have no DryRun anyway.)
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (the SRD fabric, Nitro card, host-manager), stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives (boundary-breach goals)
1. Prove or refute that the **AWS-documented verification procedure** on this page (`describe-instances`/`describe-images` + `--query`) cannot be IAM-scoped to the enhanced-networking fact alone, nor even to specific instances — so a "let the perf/compliance team verify ENA state" grant is in reality a **Region-wide inventory read** of every instance and image.
2. Characterize the asymmetry: the page steers readers to the **least** scopable of the two read paths (bulk `DescribeInstances`, Region-only) when a strictly narrower one exists (`DescribeInstanceAttribute`, `instance*`-scopable).
3. Establish that the `--query "...EnaSupport"` projection is **client-side only** and provides zero server-side data minimization (false-scoping tell for a runbook author).
4. Prove or refute the **attestation gap**: the control-plane `enaSupport` attribute (what the API returns) reports *configuration intent*, not that the `ena` driver is actually loaded/active — so a compliance control built on the API value alone is bypassable/misleading (the page's own `ethtool` step is the tell).
5. Record the in-guest `ethtool -i` check as a **zero-CloudTrail** state-enumeration path (audit blind spot).

---

## 2. Components, Assets, and Design

**What this page is.** A pure **read/verification** runbook: "test whether enhanced networking is enabled" on an instance or an AMI. It documents **five** ways to read the same fact, across two planes:

- **Control plane (AWS API):**
  1. `aws ec2 describe-instances --instance-ids i-… --query "Reservations[].Instances[].EnaSupport"` → `[true]`
  2. `aws ec2 describe-images --image-id ami-… --query "Images[].EnaSupport"` → `[true]`
  3. PowerShell `(Get-EC2Instance -InstanceId i-…).Instances.EnaSupport` → `True` (maps to `ec2:DescribeInstances`)
  4. PowerShell `(Get-EC2Image -ImageId ami-…).EnaSupport` → `True` (maps to `ec2:DescribeImages`)
- **Guest OS plane (no AWS API):**
  5. `ethtool -i eth0` (or `ens5`) inside the instance → shows `driver: ena` (enabled) vs `driver: vif` (not loaded).

**Assets exposed by the read.** `DescribeInstances` returns the *entire* reservation/instance structure (instance type, state, every ENI, private/public IPs, SG ids, subnet/VPC, tags, **IAM instance-profile ARN**, launch time, AMI id, placement, metadata-options, …). `DescribeImages` returns full AMI metadata (owner, name, description, block-device mappings, snapshot ids, platform, `EnaSupport`, `SriovNetSupport`). The `enaSupport` boolean is a single leaf of a very wide object; the page's `--query` hides that width from the reader.

**Identifiers.** `i-…`, `ami-…`, `eth0`/`ens5` (guest). No new resource type.

**ASCII (read planes):**
```
                 ┌─ ec2:DescribeInstances (bulk)  ──► FULL instance object  ─┐
compliance/perf ─┤  ec2:DescribeImages    (bulk)  ──► FULL image object      ├─ client-side JMESPath --query
   principal     └─ (narrower, NOT used by page: DescribeInstanceAttribute) ─┘   (cosmetic; server sent all)
                 ┌─ in-guest `ethtool -i eth0` ──► actual loaded driver (ena/vif) ── NO control-plane event
shell on instance┘      ▲ this is the ONLY path that proves the driver is live; the API attribute does not
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Principal granted "verify ENA state" (`ec2:DescribeInstances`/`DescribeImages`) | Every instance & image in the Region | bulk Describe, no resource-type row, only `ec2:Region` | the grant returns full instance/image inventory (IPs, SGs, tags, IAM-profile ARN) the author believed scoped to "the EnaSupport flag" |
| Runbook author relying on `--query` | Data actually returned over the wire | JMESPath applied **after** the full response arrives client-side | server transmits the complete object; `--query` is not a security boundary |
| Compliance control reading `EnaSupport==true` | Actual runtime driver state | control-plane attribute ≠ loaded driver | instance reports `EnaSupport=true` while guest driver is `vif` (not `ena`) — attestation says "configured", not "active" |
| Attacker with a guest shell | Enhanced-networking posture | `ethtool -i` in-guest | state enumerated with **no** CloudTrail/control-plane record |
| Any customer surface | AWS SRD fabric / Nitro card | — | **hard stop** |

---

## 4. API / Interface Inventory

| Name | Mutating | Ext-facing | Functionality (this page) | Resource types / scopability | Notes |
|---|---|---|---|---|---|
| `ec2:DescribeInstances` | no | yes | read `EnaSupport` (bulk; page's primary method) | **blank resource row; condition keys = `ec2:Region` ONLY** (list_ec2 L6996–7000) | account/Region-wide; **cannot** be scoped to specific instances by ARN/tag. Access level: List. Returns full instance object. |
| `ec2:DescribeImages` | no | yes | read AMI `EnaSupport` (bulk) | **blank resource row; `ec2:Region` ONLY** (list_ec2 L6906–6910) | same unscopability; also reads **shared/public** AMIs (cross-account by design). |
| `ec2:DescribeInstanceAttribute` | no | yes | *(narrower read path the page does NOT use)* | **`instance*` required; scopable by `ec2:InstanceID`, `aws:ResourceTag`, 20+ instance keys** (list_ec2 L6924–6933) | **but NO `ec2:Attribute` key** → scopable to *which instances*, not *which attribute* (parent Area 4b). |
| `ec2:DescribeImageAttribute` | no | yes | *(narrower AMI read path, not used by page)* | `image*` row (list_ec2 L6882+) | parent Area 4b owns the attribute-name-unscopability. |
| `Get-EC2Instance` / `Get-EC2Image` (PowerShell) | no | yes | PS twins of the two bulk Describes | identical authz to the CLI APIs | Lens-X read-twin parity (Area 4). |
| `ethtool -i <iface>` (guest) | no | n/a (guest OS) | read actual loaded NIC driver/version | no IAM; needs a shell on the instance | no control-plane event (Area 3). |

**Doc-flagged read-twin tell (verbatim, this page):** the page presents the API-attribute check **and** the guest `ethtool` check as *both* necessary — the first example shows the driver as `vif` ("the `ena` kernel driver is **not loaded**") while an instance can still carry `EnaSupport=true` at the attribute level. That juxtaposition is the mechanism behind Area 2.

---

## 5. Recommended Areas of Focus

### Area 1 — The AWS-documented verification runbook uses the maximally-unscopable bulk read oracle; `--query` is cosmetic [Lens O / U / S / X] — PRIMARY
**Background.** This page tells the reader to verify enhanced-networking state with `describe-instances … --query "Reservations[].Instances[].EnaSupport"` (and the AMI/PowerShell equivalents). These map to `ec2:DescribeInstances` / `ec2:DescribeImages`.
**Security Concern.** Confirmed from `list_ec2.md`: `DescribeInstances` (L6996–7000) and `DescribeImages` (L6906–6910) each have a **blank resource-type row and only `ec2:Region` as a condition key** — i.e. they are **account-wide, Region-only unscopable read oracles** (the same inert-ABAC shape the corpus has repeatedly found: `manage-spot-fleet`'s `DescribeSpotFleetRequests`, `DescribeCapacityReservations`, etc.). A grant handed out so a perf/compliance team can "check whether ENA is on" is in reality a grant to **enumerate every instance (type, all ENIs, private/public IPs, SG ids, subnet/VPC, tags, IAM instance-profile ARN, metadata-options, AMI id) and every image in the Region.** Two sharpeners unique to this page:
- **False-scoping tell (Lens U):** the `--query "...EnaSupport"` is **client-side JMESPath applied to the already-returned full response** — it provides *zero* server-side data minimization. A runbook author who copies this verbatim may believe they've narrowed the read; they have not. There is no server-side projection parameter for `DescribeInstances`.
- **Steered to the broader path (Lens X / S asymmetry — reconciles parent Area 4b):** a strictly narrower read path exists and the page does **not** use it — `DescribeInstanceAttribute` requires the **`instance*`** resource type and carries `ec2:InstanceID`, `aws:ResourceTag/${TagKey}`, and 20+ instance condition keys (L6924–6933), so it **can** be scoped to a specific team's instances by ARN/tag. The page instead recommends bulk `DescribeInstances`, which **cannot** be scoped to instances at all (Region only). Net: the AWS-authored verification runbook steers the customer toward the least-scopable option. (Parent Area 4b observed that *neither* attribute-call can be scoped by attribute-name; this complement adds that the **bulk** call this page actually uses can't be scoped by instance-identity either — strictly broader exposure.)
**High-level Test Scenarios.**
- *Claim:* a policy intending "verify EnaSupport only" cannot be written for `DescribeInstances` — any grant that lets the call succeed returns the full instance inventory, scopable only by Region. → *Oracle:* `iam:SimulateCustomPolicy` for `ec2:DescribeInstances` with an attempted `aws:ResourceTag`/`ec2:InstanceID` condition shows the key is **not evaluated** (no resource type) → the condition is inert; the only effective narrowing is `ec2:Region`.
- *Claim:* `--query` does not reduce what crosses the wire. → *Oracle:* capture the raw `describe-instances` HTTPS response (owned account) with and without `--query`; the server payload is identical, full-object either way.
- *Claim:* `DescribeInstanceAttribute --attribute enaSupport` CAN be tag/ARN-scoped to specific instances where `DescribeInstances` cannot. → *Oracle:* `iam:SimulateCustomPolicy` — a `Deny` keyed on `ec2:InstanceID` blocks `DescribeInstanceAttribute` on the wrong instance but is inert against `DescribeInstances`.
**Doc evidence.** This page (all four API examples + `--query`); `list_ec2.md` L6996–7000 (DescribeInstances), L6906–6910 (DescribeImages), L6924–6933 (DescribeInstanceAttribute). **Severity-if-true:** Low–Medium (intra-account least-privilege over-exposure / unscopable read oracle; AWS-authored runbook steers to the broad path — Lens-U/R-adjacent since the page is copy-verbatim guidance). Not cross-account.

### Area 2 — Control-plane `enaSupport` attribute ≠ actual loaded driver: an attestation gap the page itself reveals [Lens U] — net-new
**Background.** The page documents the API attribute check **and** the in-guest `ethtool -i` check. Its first `ethtool` example shows `driver: vif` with the caption "the `ena` kernel driver is **not loaded**," establishing that an instance's *actual* enhanced-networking state is a guest-OS runtime fact, separate from the control-plane `enaSupport` boolean.
**Security Concern.** The `enaSupport` instance/AMI attribute is a **capability/configuration** flag ("this instance is permitted & configured to use ENA"), **not** proof that the `ena` driver is loaded and the SR-IOV NIC is actually in use. The page implicitly concedes this — otherwise the `ethtool` step would be redundant. Consequence: a security/compliance control that attests "enhanced networking is active" purely from `describe-instances .EnaSupport == true` reports **intent, not reality**. The two can diverge: `EnaSupport=true` while the booted OS loaded a fallback driver (`vif`) — exactly the page's negative example — or an AMI carrying `EnaSupport=true` launched on a configuration where the driver never initializes. A false "compliant / enhanced-networking-on" verdict could underpin a performance SLA or a (mis)guided security assumption (e.g. "SRD/ENA path is in use"). This is a **Lens-U documented-guarantee-vs-actual-enforcement** finding: the mechanism that proves the guarantee is the guest driver, but the attestation reads the control-plane flag.
**High-level Test Scenarios.**
- *Claim:* an instance can report `EnaSupport=true` via `DescribeInstances` while `ethtool -i eth0` shows a non-`ena` driver (the API value does not track driver-load state). → *Oracle (owned canary):* on an instance with `enaSupport=true` set but booted on a kernel/driver that doesn't load `ena`, compare `describe-instances .EnaSupport` (true) against `ethtool -i` (`driver: vif`) — divergence confirms the attribute is not a runtime proof.
- *Claim:* no control-plane API returns the *actual* loaded driver/version — only the configuration attribute. → *Oracle:* enumerate the EC2 read APIs for a field exposing the live NIC driver; absence confirms the attestation must come from in-guest `ethtool`, which the control plane cannot vouch for.
**Doc evidence.** This page (`ethtool` `vif` negative example + API-attribute examples presented together). **Severity-if-true:** Low / Informational (attestation / doc-vs-reality integrity; worth filing because an AWS-published verification page could lead a customer to build a compliance control on the weaker signal). Not a privilege boundary.

### Area 3 — In-guest `ethtool -i` state enumeration has zero control-plane footprint [Lens O] — net-new, Informational
**Background.** The page's definitive "is enhanced networking actually active" check is `ethtool -i <iface>` executed **inside the guest**.
**Security Concern.** This read requires only a shell on the instance and produces **no CloudTrail / control-plane event** — an attacker (or any process) with guest access can enumerate the actual NIC driver, version, and `bus-info` with no API footprint, and cross-reference it against what the account's defenders see via `DescribeInstances`. Minor on its own; recorded for completeness as the audit-blindspot twin of Area 1's control-plane oracle (control-plane read is logged but over-broad; guest read is precise but unlogged).
**High-level Test Scenarios.** *Claim:* `ethtool -i eth0` yields driver/version/bus-info with no corresponding CloudTrail entry. → *Oracle:* run on an owned instance; confirm no `Describe*`/mgmt event is emitted for the in-guest command. **Severity-if-true:** Informational (shared-responsibility guest plane; out-of-scope-leaning).

### Area 4 — PowerShell read-twin parity + bulk-vs-attribute read twins [Lens X] — minor
**Background.** The page offers `Get-EC2Instance`/`Get-EC2Image` as equal alternatives to the CLI calls.
**Security Concern.** `Get-EC2Instance`→`ec2:DescribeInstances` and `Get-EC2Image`→`ec2:DescribeImages` are authz-identical to their CLI twins — no new surface, but confirm no SDK/cmdlet-specific path reads the attribute under a *different* action (it does not). The sharper X point is the bulk-vs-single asymmetry already captured in Area 1 (bulk `DescribeInstances` Region-only vs `DescribeInstanceAttribute` `instance*`-scopable) — a defender choosing a read path for a verification tool should prefer the attribute call for scopability, contrary to this page's steer.
**Oracle.** `iam:SimulateCustomPolicy` confirms the PS cmdlets evaluate under the same action names. **Severity-if-true:** Informational.

### Area 5 — `DescribeImages` cross-account read of a shared/public AMI's `EnaSupport` [Lens A — by-design, Low]
**Background.** `describe-images --image-id ami-…` resolves owned, explicitly-shared, and public AMIs.
**Security Concern.** The AMI `EnaSupport`/`SriovNetSupport` values of another account's **public or shared-to-you** AMI are readable — but this is by-design public AMI metadata, not an isolation break. Recorded to close the Lens-A trigger (resource-by-id read): there is no ownership check to bypass because public AMI metadata is intentionally public; a *private* AMI you were never shared returns not-found/empty. **Severity:** Low / null (by-design). Cross-ref the parent's RegisterImage/AMI-enable write path for the AMI-level *mutation* surface.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| "Verify ENA" grant = Region-wide inventory read | `DescribeInstances`/`DescribeImages` | *none* — blank resource row, only `ec2:Region` (Area 1) |
| `--query` believed to scope the read | CLI client | none — JMESPath is client-side post-filter (Area 1) |
| Narrower scopable path exists but page steers past it | `DescribeInstanceAttribute` (`instance*`) | tag/`ec2:InstanceID`-scopable, but page recommends the broad bulk call (Area 1 / 4) |
| Attestation on `EnaSupport==true` ≠ driver active | control-plane attribute vs guest driver | guest `ethtool` is the only runtime proof; API value is config intent (Area 2) |
| Unlogged guest state enumeration | `ethtool -i` | no CloudTrail (Area 3) |

---

## 7. Out-of-Scope Risk Categories
- **The write/enable surface** — `ModifyInstanceAttribute`/`RegisterImage` enablement, `sriovNetSupport` irreversibility, ENA-Express `EnaSrdSpecification`, driver-install Lens-R audit, metrics side-channel: all owned by `enhanced-networking-attack-research-plan.md` (Areas 1–7). This complement is read-only.
- **Guest-OS driver behavior / `ethtool` itself** — shared-responsibility guest plane; in scope here only as the Area-2 attestation tell and Area-3 audit note.
- **IMDS on the managed host / Nitro card / SRD fabric** — hard stop.
- **Public AMI metadata being public** (Area 5) — by-design, not a vulnerability.
- **Single-tenant self-DoS, perf/feature-parity gaps** — product behavior.

## 8. Null hypotheses / doc gaps
- **Lens G (SSRF): NULL** — read this page in full; the only fetch-shaped operation is the guest-side `ethtool`/driver read, dereferenced by the customer's own OS, not an EC2 control-plane fetch identity. No `*Url`/`*Uri`/location field. (Driver-download SSRF-null already settled by parent §7/§8.)
- **Lens A (cross-tenant IDOR): NULL** — the two Describe calls return only owned (or intentionally-public, Area 5) resources; no tenant-id/resource-id in a body that an authz check reads differently from the credential. `DescribeInstances` is Region-scoped-only but still bounded to the caller's own account's instances.
- **Lens B/C/E/F/H/I/J/K/L/M/N/P/Q/V/W/Y/AA/BB/CC/DD/EE/FF: NULL for this surface** — this is a read-only verification page: no role ARN/PassRole, no credential vending, no RBAC mutation, no parser/translation layer, no KMS/encryption-context, no tagging mutation, no OAuth, no LLM, no size/zip limit, no session id, no namespace migration, no registration/proofing, no file upload, no network-segmentation claim, no attestation gate, no transport/sig claim, no share/revoke, no multi-parser request path, no trusted-upstream header, no caching layer, no predictable-name resolution, no JWT/token validation. Page checked: `test-enhanced-networking-ena.md` (121 lines, full).
- **Open doc-gaps to confirm before investing:** (1) does any EC2 read API expose the *actual loaded* NIC driver (would close/strengthen Area 2)? none found in a `list_ec2` sweep — confirm live. (2) Confirm via `iam:SimulateCustomPolicy` that `aws:ResourceTag`/`ec2:InstanceID` are genuinely inert on `DescribeInstances` (Area 1 primary oracle) — settles the whole plan without touching a resource.
- **Drift:** target page `test-enhanced-networking-ena.md` re-fetched and confirmed **offline==online byte-identical 2026-10-15**. `list_ec2.md` condition-key cells for the three Describe actions read offline 2026-10-15 (online twin truncates before these rows via WebFetch — offline grep is authoritative per [[reference-aws-iam-service-auth-ref-url]]).
