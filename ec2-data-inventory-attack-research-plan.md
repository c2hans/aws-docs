# EC2 Instance Data Inventory — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/ec2-data-inventory.html` (target) and the surfaces it fans out to — `user-data.md`, `ec2-instance-metadata.md`, `configuring-instance-metadata-options.md`, `iam-policies-for-amazon-ec2.html`, `finding-an-ami.md` / `usingsharedamis-finding.md` / `sharing-amis.md` / `share-amis-with-organizations-and-OUs.md` / `cancel-sharing-an-AMI.md`, `vm-import/.../required-permissions.md` + `vmexport-prerequisites.md` + `building-shared-amis.md`, `API_ExportImage.md`, `ebs/.../API_GetSnapshotBlock.md`, `global-view.html`, `Using_Filtering.html`, `security-group-rules.md`, `security-group-assoc.md` + `API_AssociateSecurityGroupVpc`, `working-with-managed-prefix-lists.md` / `sharing-managed-prefix-lists.md` / `work-with-shared-prefixes.md` / `security-group-sharing.md`, and the Service Authorization Reference `list_ec2` (via `servicereference.us-east-1.amazonaws.com/v1/ec2/ec2.json`).
Status: documentation-derived hypotheses only; nothing tested against a live account. The target page is a *system-administrator inventory playbook* — it is a read lens over six EC2 characteristics. This plan treats each characteristic's read API as an entry point and follows it to the write-twin / sharing / fetch mechanism that actually crosses a boundary.

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- The inventory page itself breaks nothing — the value is that it enumerates, in one place, exactly which read action touches each sensitive characteristic (user data, AMIs, SG rules). Every one of those reads has a *write/share/fetch sibling* that is the real target; the page is the map to them.
- **HARD STOP:** the moment evidence shows an identity / credential / ARN / account belonging to AWS's own service plane (e.g. the `vmie.amazonaws.com` fleet identity, the VM Import/Export regional canonical account, any Nitro/Host-Manager interface), stop, preserve evidence, and flag for AWS-Security disclosure. Do not probe further.
- **Scope discipline:** several leads below are *intra-account least-privilege footguns a customer inflicts on themselves* (unscopable `Describe*`, over-broad inventory roles). Those are **out of scope** against AWS and are called out as such in §7 — do not spend hunter time proving a customer can over-grant their own policy. The in-scope set is: cross-account boundary breaks, AWS-authored artifact defects (Lens R/S/U), and condition-key semantics that make an *intended* control unexpressible or silently inert.

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. **Read another characteristic than you were granted** — hold a "read-only inventory" grant (`ec2:DescribeInstanceAttribute`) and extract `userData` secrets that the grant's author believed were out of reach. (Lens T)
2. **Turn an inventory-write sibling into code execution** — overwrite `userData` on a stopped instance and bounce it to run attacker code as root under the instance's IAM role. (Lens B/E)
3. **Make a victim launch your image** — publish a public AMI whose `Name` matches a victim's `describe-images`-without-`--owners` inventory/automation and have it selected. (Lens EE)
4. **Reach into another account's network boundary and keep reaching after revocation** — poison a RAM-shared prefix list, or ride a stranded shared-SG/prefix-list reference that survives unshare, to widen a consumer's ingress. (Lens AA/U/V)
5. **Defeat an intended IAM guardrail with a condition key that binds the wrong resource or does not exist** — associate an SG into an unapproved VPC despite an `ec2:Vpc` restriction; omit `TagSpecifications` to bypass a `security-group-rule` tag scope. (Lens S)
6. **Exfiltrate a full disk image / snapshot bytes past the AMI-sharing controls** — `export-image` a VMDK of baked secrets into an S3 bucket, or `ebs:GetSnapshotBlock` the raw blocks directly. (Lens T/X)
7. **Confused-deputy the VM Import/Export service** into acting under the `vmimport` role via the world-known static `ExternalId`. (Lens B/C)

## 2. Components, Assets, and Design

The target page documents six characteristics and the read action for each:

| Characteristic | Read action (per target page) | Sensitive asset exposed | Write/share/fetch sibling (the real target) |
|---|---|---|---|
| Geographic location | EC2 Global View console; `DescribeInstances` per-Region | instance inventory, cross-Region footprint | — (read-only aggregation, single-account) |
| Hardware specs | `DescribeInstances`, `DescribeInstanceTypes` | instance types | — (public spec data) |
| Images | `DescribeInstances`→`ImageId`, `DescribeImages`, `ExportImage` | AMI contents, baked secrets | `ModifyImageAttribute` (launchPermission), `ExportImage`, `ebs:GetSnapshotBlock`, name-based AMI resolution |
| IP / DNS | `DescribeInstances` | private IPs, public DNS→IP mapping | — (single-account read) |
| Security group rules | `DescribeSecurityGroupRules`, `DescribePrefixLists` | ingress/egress exposure, referenced CIDRs/SGs | `Authorize*/Revoke*SecurityGroup*`, `ModifySecurityGroupRules`, `AssociateSecurityGroupVpc`, RAM prefix-list / SG sharing |
| User data | `DescribeInstanceAttribute --attribute userData` | **launch scripts, commonly credentials/API keys/join tokens** | `ModifyInstanceAttribute --attribute userData`, IMDS `GET /latest/user-data` |

**Design facts that create the boundaries:**
- **User data** is a 16 KB opaque instance attribute; on Linux it runs **as root** at boot; it is readable via the control-plane `DescribeInstanceAttribute` **and** via IMDS `169.254.169.254` with no authentication beyond the (same-host-trivial) IMDSv2 PUT token. AWS's own doc: *"any software running on the instance can view its metadata… do not store sensitive data… as user data."* It is modifiable only while **stopped**, then takes effect on next boot. (`user-data.md`, `ec2-instance-metadata.md`)
- **AMIs** are resolved by `DescribeImages`; **without `--owners`** the result set spans *all public AMIs plus owned plus shared-with-you*. Only `ImageOwnerAlias ∈ {amazon, aws-backup-vault, aws-marketplace}` is unforgeable; `Name`/`Description` are attacker-controllable. (`finding-an-ami.md`, `sharing-amis.md`)
- **VM Import/Export**: `ExportImage` writes a VHD/VMDK/RAW full-disk image into a **customer S3 bucket in the same account**, via the `vmie.amazonaws.com` service assuming the customer's `vmimport` role whose trust is gated only by a **fixed, world-known `ExternalId: vmimport`**. (`required-permissions.md`, `API_ExportImage.md`)
- **Security groups / prefix lists**: cross-account SG references are **existence-checked only** (no authz against the referenced SG's owner, **no CloudTrail event to that owner**). RAM-shared managed prefix lists **always resolve to the latest version** in every consumer SG rule, and references **survive unshare** ("stranded reference" that keeps auto-updating). (`security-group-rules.md`, `working-with-managed-prefix-lists.md`, `security-group-sharing.md`)
- **Describe\* actions do not support resource-level permissions** (`DescribeInstances/SecurityGroups/Images/SecurityGroupRules/ManagedPrefixLists` scope only by `ec2:Region`). The lone exception is `DescribeInstanceAttribute` (`instance` resource type, tag/ID conditions) — **but it has no per-attribute condition key**, so it is all-or-nothing across `userData`/`instanceType`/etc. (`iam-policies-for-amazon-ec2.html`, `list_ec2`)

```
                 ┌─────────────────────────── Customer account A ───────────────────────────┐
  "read-only     │                                                                           │
   inventory"    │   DescribeInstanceAttribute(userData) ──► 16KB script (SECRETS)           │
   role ─────────┼──►  (no per-attribute IAM scope: all-or-nothing)                          │
                 │                                                                            │
   Modify+Stop/  │   ModifyInstanceAttribute(userData) ──► stop/start ──► root exec ──► IMDS  │
   Start ────────┼──►  169.254.169.254/iam/security-credentials/<role> ──► instance-role creds│
                 │                                                                            │
   DescribeImages│   (no --owners) ──► resolves ANY public AMI by Name ◄──┐                   │
                 │                                                        │ attacker publishes │
   ExportImage ──┼──► vmimport role (ExternalId=vmimport) ──► S3 bucket (full disk, secrets)  │
                 │                                                        │                   │
   SG rule ──────┼──► references pl-… (RAM-shared) ──always latest version──┐                 │
                 └──────────────────────────────────────────────────────────┼───────────────┘
                                                                             │
            Account B (prefix-list owner / AMI publisher / referenced SG owner): mutates CIDRs,
            publishes name-matched AMI, is referenced without authz/CloudTrail ◄── cross-account seam
```

## 3. API / Interface Inventory

| Name | Mutating? | Internal/External | Callable from Internet | Authorized callers | Resource-level IAM? | Notes / lens |
|---|---|---|---|---|---|---|
| `DescribeInstanceAttribute` | No | External (SigV4) | Yes | per-account IAM | **Yes** (`instance`, tag/ID) — **but no per-attribute key** | reads `userData`; all-or-nothing per instance → **T, S** |
| `ModifyInstanceAttribute` | **Yes** | External | Yes | per-account IAM | Yes; **has `ec2:Attribute`/`ec2:Attribute/${AttributeName}`** | write-twin of the above; `userData` write → **B/E** |
| `DescribeInstances` | No | External | Yes | per-account IAM | **No** (Region only) | returns private IP + public DNS; foreign-ID = silent-empty, bad-ID = error → **A, V** |
| `DescribeImages` | No | External | Yes | per-account IAM | **No** (Region only) | **no `--owners` ⇒ whole public AMI namespace** → **EE** |
| `ModifyImageAttribute` (launchPermission) | **Yes** | External | Yes | per-account IAM | Yes (`image`) | adds `UserId`/`Group=all`/`OrganizationArn`/OU — **grantee not membership-checked** → **AA** |
| `ExportImage` | **Yes** | External | Yes | per-account IAM + `iam:PassRole` on `vmimport` | Yes (`image`) + PassRole | writes full disk image to S3 via service role → **B/C, T, R** |
| `ebs:GetSnapshotBlock` | No | External (EBS direct API) | Yes | per-account IAM (`ebs:` ns) + snapshot KMS | — | raw snapshot bytes, bypasses AMI/CopySnapshot path → **X** |
| `DescribeSecurityGroupRules` | No | External | Yes | per-account IAM | **No** (Region only) | returns `ReferencedGroupInfo`, cross-account `GroupOwnerId`, `PrefixListId` → **A** |
| `Authorize/RevokeSecurityGroupIngress/Egress` | **Yes** | External | Yes | per-account IAM | `security-group*`; `security-group-rule*` **only when `TagSpecifications` present** | referenced-SG existence-checked only; tag scope opt-out-able → **A, S** |
| `AssociateSecurityGroupVpc` | **Yes** | External | Yes | per-account IAM | `security-group*` (`ec2:Vpc`=home VPC) **+** `vpc*` (`ec2:VpcID`) | `ec2:Vpc` binds the SG's **home** VPC, not the **target** → **S** |
| `DescribePrefixLists` | No | External | Yes | per-account IAM | **No** | **legacy AWS-managed-only call** — wrong tool for customer/shared `pl-…` → **U (tooling gap)** |
| `DescribeManagedPrefixLists` / `GetManagedPrefixListEntries` | No | External | Yes | per-account IAM | List: **No**; GetEntries: **Yes** (`prefix-list*`) | shared-list resolution; always-latest-version → **AA/U** |
| EC2 Global View console | No | External (console) | Yes (console) | **caller's own creds**, single-account | n/a | **not** an SLR / Resource Explorer / Organizations aggregation — client-side Region fan-out → **A/V (null-ish)** |
| IMDS `GET /latest/user-data` | No | **Instance-local** `169.254.169.254` | No (link-local) | **any process on the instance**, no IAM | n/a | role-independent user-data readback; SSRF pivot → **T** |

Doc-flagged focus sentence (verbatim, `ec2-instance-metadata.md`): *"the data is not protected by authentication or cryptographic methods. Anyone who has direct access to the instance, and potentially any software running on the instance, can view its metadata."* — AWS plants the user-data/IMDS lead here; keep the pointer.

No `[NEW]` markers on these pages (mature APIs). Prioritization in §5 therefore follows cross-tenant / service-plane reach and AWS-authored-artifact defects, not newness.

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| "Read-only inventory" principal | `userData` secrets on every instance | `DescribeInstanceAttribute` (no per-attribute scope) | **Extracting a credential from an instance whose `userData` the grant's author believed was unreadable** = secret-sprawl breach (T) |
| `ModifyInstanceAttribute`+Stop/Start holder | The instance's attached IAM role creds | overwrite `userData` → boot → root → IMDS `iam/security-credentials/*` | **Attacker code runs as root under a role the principal never held `PassRole` for** = privilege escalation (B/E) |
| Any process / SSRF on an instance | `userData` + role creds | IMDS link-local, no auth | **A link-local GET returning the user-data script / role creds** = SSRF-to-secrets (T); **link-local hit under AWS fleet identity = HARD STOP** |
| Attacker (any account) | Victim's launch pipeline | publish public AMI with a matching `Name`; victim `DescribeImages` without `--owners` | **Victim launches an instance from the attacker's AMI** = supply-chain code exec (EE) |
| Prefix-list / shared-SG **owner** (account B) | Consumer account A's SG ingress | RAM share → consumer references → owner edits CIDRs (always-latest) | **Consumer A's effective ingress widens (e.g. gains `0.0.0.0/0`) with no A-side consent event** = cross-account network-boundary breach (U/V); **persists after unshare** (AA) |
| Policy author (intended guardrail) | `AssociateSecurityGroupVpc` target VPC | `ec2:Vpc` condition on the association | **An SG associates into an unapproved target VPC despite the `ec2:Vpc` restriction** = the control binds the wrong resource (S) |
| Caller | `security-group-rule` tag-scoped Authorize | omit `TagSpecifications` from the request | **A rule the tag-scope should block is created** = resource-level control bypassed by omission (S) |
| `ExportImage` caller | `vmie.amazonaws.com` fleet acting under `vmimport` | PassRole + fixed `ExternalId: vmimport` trust | A cross-account assumption of a `vmimport` role whose trust was deployed from the AWS sample as-is (B/C) — **if evidence reaches the service fleet identity, HARD STOP** |
| Account B | Account A's SG (referenced in B's rule) | `Authorize*` referencing A's `sg-…` | **B authors the reference with no authz check against A and A sees no CloudTrail** = silent cross-account reference (A/O) |
| Any `ebs:GetSnapshotBlock` holder | Raw snapshot bytes | EBS direct API (separate namespace) | **Snapshot block bytes read without `CopySnapshot`/image-registration and without triggering AMI-share controls** (X) |

Canonical boundaries that are **null on these pages** (see §8): data-plane→control-plane ENI hop, STS session-policy / ProvidedContext vending, translation-layer injection, LLM/prompt, OAuth/3P link, JWT/OIDC, cache-key, canonicalization/multi-parser, attestation, upstream-context — none of these mechanisms appear in the inventory surface.

## 5. Recommended Areas of Focus

### Area 1 — `ModifyInstanceAttribute(userData)` → root RCE under the instance role (Lens B/E, write-twin of Lens X; PRIMARY, Critical)
**Background.** The target page reads `userData` with `DescribeInstanceAttribute`. The write-twin, `ModifyInstanceAttribute --attribute userData`, is editable while the instance is **stopped** and the script "are run as the **root** user" on next boot (`user-data.md`, "Update the instance user data"). The instance's attached-role credentials are then reachable from that root process at IMDS `iam/security-credentials/{role}` (`ec2-instance-metadata.md` metadata-category table).
**Security Concern.** A principal holding `ec2:ModifyInstanceAttribute` + `ec2:StopInstances`/`StartInstances` (or just Modify on an already-stopped instance) obtains **code execution as root under the instance's IAM role without ever holding `iam:PassRole`** — the canonical "write user-data, bounce the box" EC2 privesc. The role may be far more privileged than the caller. This is the Lens B/E variant the skill flags as a confirmed exemplar: *a non-PassRole action that reaches a role's live credentials.*
**High-level Test Scenarios.**
- *Claim:* `ModifyInstanceAttribute(userData)`+Stop/Start escalates to the instance role → *Mechanism:* `user-data.md` stop→modify→start procedure + root-exec statement + `ec2-instance-metadata.md` IAM-cred category → *Oracle:* in a 2-role canary, a scoped principal with only Modify/Stop/Start (no PassRole, no sts perms) overwrites `userData` with a script that calls `aws sts get-caller-identity`, bounces the instance, and the output shows the **instance role**'s identity, not the caller's → confirmed privesc → *Preconditions:* target instance has a more-privileged instance profile; caller holds Modify+Stop+Start on it → *Cost:* low (one stop/start cycle) → *Severity:* **Critical** (role-scoped RCE).
- *Adjacent (defense):* because `ec2:Attribute`/`ec2:Attribute/${AttributeName}` **are** available on `ModifyInstanceAttribute` (unlike on Describe), a `Deny` with `"ec2:Attribute":"userData"` *can* block exactly this path — test whether that Deny actually fires (ties to Area 5 case-sensitivity). The point for AWS framing: the block requires deliberate, non-default hardening nothing in the baseline docs applies.
Doc evidence: `user-data.md` (update procedure, root-exec); `ec2-instance-metadata.md` (IAM creds category); `list_ec2` (`ec2:Attribute` present on Modify, absent on Describe). Severity-if-true: **Critical**.

### Area 2 — `userData` secret reachability: all-or-nothing read + role-independent IMDS (Lens T; PRIMARY, High)
**Background.** The inventory page's own user-data step exists *because* user data commonly contains setup scripts — and AWS warns those scripts "commonly contain credentials/API keys/join tokens." Two readback paths exist: the control-plane `DescribeInstanceAttribute` and instance-local IMDS.
**Security Concern.**
1. **No per-attribute IAM scope.** `DescribeInstanceAttribute`'s condition-key set (confirmed from `list_ec2`) has **no `ec2:Attribute*` key** — so a policy cannot allow reading `instanceType` while denying `userData`. Any principal with the broad "read-only EC2 inventory" grant the target page's use-case implies (monitoring/inventory tooling) can exfiltrate **every instance's `userData`**. This is a Lens T cross-reachability shape: the secret is reachable through a grant whose author never intended it.
2. **IMDS is role-independent.** `GET http://169.254.169.254/latest/user-data` returns the (auto-decoded) script to **any process on the instance** with no IAM at all — the standard SSRF→secrets pivot; if IMDSv1 is allowed, a single tokenless GET suffices.
**High-level Test Scenarios.**
- *Claim:* a "read-only inventory" role can read `userData` secrets it was never meant to → *Oracle:* grant only `ec2:DescribeInstanceAttribute` (+ Region/tag scope), attempt `--attribute userData` across instances, and attempt to *also* author a Deny carving out `userData` — confirm no condition key exists to express it (re-grep the `DescribeInstanceAttribute` row of `list_ec2` for `ec2:Attribute`; `iam:SimulateCustomPolicy` as the no-touch oracle) → *Severity:* **High** (secret sprawl; scales with what the scripts embed).
- *Claim:* IMDS yields `userData` + role creds regardless of the role's policy → *Oracle:* from any process on a canary instance, `curl …/latest/user-data` and `…/iam/security-credentials/` → AWS-documented design fact; no live test needed to establish the mechanism → *Severity:* **High** (SSRF pivot); **if the fetch ever egresses under an AWS fleet identity rather than instance-local, HARD STOP.**
Doc evidence: `list_ec2` (DescribeInstanceAttribute condition keys, no `ec2:Attribute`); `ec2-instance-metadata.md` ("any software running on the instance… do not store sensitive data as user data"); `user-data.md` (reservation-wide availability). Severity-if-true: **High**.

### Area 3 — AMI name-confusion: `DescribeImages` without `--owners` ("whoAMI") (Lens EE; PRIMARY, High–Critical)
**Background.** The inventory page's AMI step uses `DescribeImages`. Per `finding-an-ami.md`, *"By default, this command returns all AMIs that are public, that you own, and that are shared with you"* — i.e. omitting `--owners` opens the result set to the **entire public AMI namespace**. Only `ImageOwnerAlias ∈ {amazon, aws-backup-vault, aws-marketplace}` is unforgeable; `Name`/`Description` are attacker-controllable (`sharing-amis.md`).
**Security Concern.** A victim pipeline/automation (Terraform `data "aws_ami"` without `owners`, Packer, a CI inventory script modeled on this page) that resolves an AMI by `Name` filter without an owner constraint can be made to select an **attacker-published public AMI** named to match the victim's convention (`web-server-3.1`, `golden-image-prod`) — supply-chain code execution in the victim's fleet. This is the publicly disclosed 2024 "whoAMI" class, which AWS's own doc enables by making `--owners` optional.
**High-level Test Scenarios.**
- *Claim:* an unowned `DescribeImages --filters Name=name,Values=<victim-convention>` resolves to an attacker image → *Mechanism:* `finding-an-ami.md` default-scope sentence; `usingsharedamis-finding.md` showing `--owners amazon aws-marketplace` as the *recommended* scoping (⇒ unscoped = all public) → *Oracle:* publish a public AMI with a name matching the target's documented/leaked convention; show the victim's resolver returns it (sorted-by-`CreationDate` "most_recent" selection is the amplifier) → *Preconditions:* victim automation omits `--owners`/`owner-id`; attacker knows the name pattern → *Cost:* trivial (one public AMI) → *Severity:* **High–Critical** (code exec via AMI substitution).
- *Adjacent:* confirm whether `most_recent=true` without owner pin lets a freshly-published attacker AMI win on `CreationDate`; and whether the target consumes `ImageOwnerAlias` at all (the only unforgeable field).
Doc evidence: `finding-an-ami.md`; `usingsharedamis-finding.md`; `sharing-amis.md` (owner-alias unforgeable, Name/Description not). Severity-if-true: **High–Critical**.

### Area 4 — Shared managed prefix-list / SG poisoning + revocation-survival (Lens U/V + Lens AA; PRIMARY, High)
**Background.** The inventory page resolves SG-rule sources via prefix lists (`pl-…`). RAM-shared managed prefix lists: *"Resources that reference the prefix always use the current (latest) version"* and consumers have **no "pin to version N" control** (`working-with-managed-prefix-lists.md`, `work-with-shared-prefixes.md`). After unshare: *"existing references continue to function as normal… use the latest version"*; for shared SGs, *"Existing participant ENIs continue to get any security group rule updates… Unsharing only prevents… new associations"* (`security-group-sharing.md`).
**Security Concern.**
1. **Poisoning (U/V):** a compromised/malicious **prefix-list owner (account B)** can add `0.0.0.0/0` and **instantly widen ingress on every consumer SG across every subscribed account**, with no consumer approval step per update. The SG "boundary" is only as trustworthy as every account ever granted "reference this list."
2. **Stranded reference (AA):** after RAM unshare / `delete-resource-share`, the consumer's existing references **keep working and keep auto-updating** — "revoke access" does not sever the trust relationship; the owner retains a live, owner-controlled channel into the consumer's network boundary indefinitely.
**High-level Test Scenarios.**
- *Claim:* a prefix-list owner silently widens a consumer's ingress → *Oracle:* 2-account canary — B shares `pl-X`, A references it in an inbound SG rule, B adds `0.0.0.0/0`; observe A's **effective** SG rules open to the world with no A-side event → *Severity:* **High** (cross-account network boundary).
- *Claim:* the channel survives revocation → *Oracle:* after the above, B `delete-resource-share`; A's reference persists and still updates on B's next edit → confirms Lens AA stranded reference → *Severity:* **High**.
- *Adjacent (O):* does A receive **any** signal (CloudTrail/EventBridge) on an owner-side prefix-list version bump? (Owner edits are logged in B, not A.)
Doc evidence: `working-with-managed-prefix-lists.md` ("always use the latest version", centralized propagation); `work-with-shared-prefixes.md`/`sharing-perms.md` (no consumer pin/modify); `security-group-sharing.md` (unshare leaves existing associations live). Severity-if-true: **High**.

### Area 5 — Condition-key semantics on SG actions: wrong-resource binding, phantom key, opt-out tag scope (Lens S; PRIMARY, Medium–High)
**Background.** The inventory page relies on SG-rule reads; the write/associate siblings carry condition keys whose *semantics* decide whether an intended guardrail actually holds. Three distinct failure shapes, all confirmed structurally from `list_ec2`.
**Security Concern & scenarios.**
- **S-1 — `ec2:Vpc` binds the SG's home VPC, not `AssociateSecurityGroupVpc`'s target.** The action's resource table lists `ec2:Vpc` only under the `security-group*` row; the `vpc*` row exposes `ec2:VpcID`/`ec2:Tenancy`, and `ec2:Vpc` is defined as "ARN of the VPC [that owns the resource]." *Claim:* a policy using `Condition: StringEquals{ec2:Vpc: <approved-vpc-arn>}` to pin the allowed **target** VPC restricts nothing about the target — it only filters SGs by their **origin** VPC. *Oracle:* grant `AssociateSecurityGroupVpc` with that condition; associate a home-VPC-matching SG into an **unapproved** target VPC — if it succeeds, wrong-resource binding is live. *Severity:* **Medium–High** (breaks a docs-example-encouraged allow-list pattern — the same `ec2:Vpc` idiom is shown working correctly for `Authorize*`). **Strongest lead for live confirmation (documentation-derived, not documentation-stated).**
- **S-2 — `ec2:InterfaceType` does not exist.** Zero matches in the full `list_ec2` (actions + condition-key tables). *Claim:* any policy/tooling scoping by `ec2:InterfaceType` builds on a non-existent control — a `Deny` keyed on it never fires (key simply absent). *Oracle:* `SimulateCustomPolicy` with a Deny keyed on `ec2:InterfaceType` — observe it never constrains. *Severity:* **Medium** (silent fail-open on a defense-in-depth key).
- **S-3 — `security-group-rule` tag conditions are opt-out by omission.** Doc verbatim: *"Policies using the security-group-rule resource-level permission are only enforced when the API request includes TagSpecifications."* *Claim:* a tag-scoped `Authorize*` restriction is bypassed by simply omitting `TagSpecifications`. *Oracle:* policy scoping `AuthorizeSecurityGroupIngress` by `security-group-rule` tag; call without `TagSpecifications` — if the rule is created, confirmed. *Severity:* **High** (documented resource-level control defeated client-side, no server-side fallback).
- **Null on case-sensitivity:** `iam-policies-for-amazon-ec2.html` states "Condition keys are not case-sensitive" (key *names*). The value-side `StringEquals` case trap (Area 1's `userData` Deny) remains **plausible but unconfirmed** — close the doc-gap on the IAM `StringEquals` operator reference before treating it as a finding.
Doc evidence: `list_ec2` per-action resource/condition tables; `security-group-rules.md`; `iam-policies-for-amazon-ec2.html` (multi-resource condition caveat, "not case-sensitive"). Severity-if-true: **Medium–High**.

### Area 6 — VM Import/Export confused-deputy + full-disk secret dump + sample-policy wildcards (Lens B/C + T + R; Medium–High)
**Background.** The inventory page's "create a VM file from an AMI" step calls `ExportImage`, which has `vmie.amazonaws.com` assume the customer's `vmimport` role and write a VHD/VMDK/RAW **full disk image** into a customer S3 bucket.
**Security Concern.**
- **B/C — static ExternalId confused deputy.** The AWS-sample trust policy gates assumption with only `sts:ExternalId: vmimport` — a **fixed string identical across all customers who follow the docs**. AWS's doc has to *recommend an optional* hardening with `aws:SourceAccount`/`aws:SourceArn`, implying the baseline deployed from the sample lacks per-account scoping. The doc also warns `aws:SourceVpc`/`SourceVpce`/`VpcSourceIp` "are not available and might cause your requests to fail" with this `iam:PassRole` — a documented condition-key evasion caveat. *Oracle:* examine whether a target's `vmimport` trust was deployed verbatim (static ExternalId only). **If any evidence reaches the `vmie` fleet identity, HARD STOP.**
- **T — secret dump.** `building-shared-amis.md`: *"We recommend against storing sensitive data… Always delete the shell history before bundling… the shell history contains your access key,"* and `shred` "might not remove all copies… journalling file systems… snapshots." The exported image is a full filesystem dump whose new trust boundary is the destination **S3 bucket's ACL/IAM/KMS** — plus a fixed, publicly documented regional **AWS canonical account** gets `READ_ACP`+`WRITE` on that bucket (`vmexport-prerequisites.md`). *Oracle:* export a canary image, confirm "deleted" secrets survive in the artifact; audit who can read the destination bucket.
- **R — AWS-authored policy wildcards.** The sample `vmimport` **role** policy grants `ec2:ModifySnapshotAttribute, CopySnapshot, RegisterImage, Describe*` on `Resource:"*"`, and the KMS block (`Decrypt, Encrypt, GenerateDataKey*, ReEncrypt*, CreateGrant`) defaults to `Resource:"*"` unless manually narrowed; the user-side sample grants the whole import/export EC2 action list on `Resource:"*"`. (S3 statements *are* scoped to named buckets.) These are **AWS-authored, copy-verbatim** artifacts → in scope, Tier 2. *Oracle:* `iam:GetPolicyVersion` on the deployed role + statement-by-statement audit; prove a role holding only this artifact can CopySnapshot/RegisterImage/KMS-decrypt across the whole account.
Doc evidence: `required-permissions.md` (trust policy, PassRole note, wildcard role/user policies, optional SourceAccount hardening); `vmexport-prerequisites.md` (canonical-account ACL); `building-shared-amis.md` (baked-secret/shred). Severity-if-true: **Medium–High** (B/C conditional on deployment; R intra-account privesc breadth on role compromise).

### Area 7 — AMI launchPermission org/OU grantee not membership-checked + incomplete revoke (Lens AA; Medium–High)
**Background.** `ModifyImageAttribute` shares an AMI via `launchPermission` to a `UserId`, `Group=all`, `OrganizationArn`, or `OrganizationalUnitArn`.
**Security Concern.** `share-amis-with-organizations-and-OUs.md` states verbatim: *"The AMI owner can share an AMI with any organization or OU, including organizations and OUs that they're not a member of."* — **no membership/ownership relationship is enforced**; only *format* (ARN syntax) is validated. A typo'd/guessed/stale OrgArn can leak a full AMI (baked app code/config) to an unintended org. Revocation is also incomplete: `cancel-image-launch-permission` **cannot** remove org/OU-level or public shares, and consumers who already launched *"can then create an AMI from the instance they launched"* — derivative AMIs/snapshots survive any clawback.
**High-level Test Scenarios.**
- *Claim:* launchPermission accepts a non-member / nonexistent org/OU ARN → *Oracle:* `ModifyImageAttribute … Add OrganizationArn=<a-foreign-or-fabricated-org-arn>`; observe accept vs error (format-only validation ⇒ accept) → *Severity:* **Medium–High** (data leak to an unintended org; blast radius if the ARN is later claimed/reassigned).
- *Claim:* revocation is incomplete → *Oracle:* share → consumer copies/derives → owner revokes; confirm derivative images and org/OU shares persist → *Severity:* **Medium** (durable unauthorized copies).
Doc evidence: `share-amis-with-organizations-and-OUs.md` ("any organization or OU… not a member of"); `cancel-sharing-an-AMI.md` (no revoke path for org/OU/public); `sharingamis-intro.md` (derivative-AMI persistence). Severity-if-true: **Medium–High**.

### Area 8 — Cross-account SG reference: no authz, no CloudTrail to the owner (Lens A + O; Medium–High)
**Background.** The inventory output shows `ReferencedGroupInfo` with a cross-account `GroupOwnerId`. Doc verbatim (`security-group-rules.md`): *"We do not authorize against referenced security groups… We only check whether the security group exists,"* and *"When a referenced security group is owned by another account, the owner account does not receive CloudTrail events for these actions."*
**Security Concern.** Account B can author, in its own SG, a rule naming account A's `sg-…` as source — with **no IAM check against A and no CloudTrail event delivered to A**. Where peering/TGW/shared-VPC connectivity exists, this undermines A's expectation that being referenced is a mutual, visible operation; it is also a blind-spot for A's detection.
**High-level Test Scenarios.**
- *Claim:* B references A's SG with no A-side authz or log → *Oracle:* 2-account peered canary; B `AuthorizeSecurityGroupIngress` referencing A's `sg-…`; confirm success, A's IAM had no veto, A's CloudTrail shows nothing → *Severity:* **Medium–High** (cross-account trust/audit gap; actual traffic impact gated on connectivity).
- *Adjacent:* stale-rule behavior when A deletes the referenced SG (rule marked stale, not removed) — enumeration/misconfig surface.
Doc evidence: `security-group-rules.md` (no referenced-SG authz; no cross-account CloudTrail). Severity-if-true: **Medium–High**.

### Area 9 — `ebs:GetSnapshotBlock` as a quieter snapshot-byte exfil cousin (Lens X; Medium)
**Background.** `DescribeInstances→ImageId→` AMI maps to backing EBS snapshots. `ebs:GetSnapshotBlock` (EBS direct APIs, `ebs:` namespace) reads **raw snapshot block bytes directly**, independent of `ec2:CopySnapshot`/image registration.
**Security Concern.** It is a **separate IAM action with no documented alias/implicit grant to `ec2:CopySnapshot`**, but an account that wildcard-grants `ebs:*` alongside `ec2:*` gets block-level snapshot read that **bypasses AMI/snapshot-level sharing controls entirely** — a quieter exfiltration path for snapshot data (including deleted-but-not-scrubbed secrets per Area 6).
**High-level Test Scenarios.**
- *Claim:* `ebs:GetSnapshotBlock` reaches snapshot bytes outside the CopySnapshot/image path → *Oracle:* with only `ebs:ListSnapshotBlocks`+`GetSnapshotBlock` (+ KMS for encrypted), read blocks of an owned snapshot; confirm no `ec2:CopySnapshot` needed → *Preconditions:* `ebs:*` granted; snapshot KMS key access if encrypted → *Severity:* **Medium** (exfil-path/control-coverage gap; **not** cross-account by itself — standard resource-policy still applies).
- *Note (Lens X alias check, refuted):* `CancelConversionTask`/`CancelImportTask`/`CancelExportTask` are **three distinct co-listed actions** in AWS's own sample policy, not aliases — the alias hypothesis is refuted by doc evidence (one doc-gap: `cancel-conversion-task` CLI page 404, so a formal deprecation banner was not confirmable).
Doc evidence: `ebs/.../API_GetSnapshotBlock.md` (separate namespace, own IAM + KMS gate); `required-permissions.md` (three distinct cancel actions). Severity-if-true: **Medium**.

### Area 10 — Enumeration oracle, unscopable `Describe*`, public-DNS topology (Lens A/V/O; Low — mostly footgun/by-design)
**Background.** The inventory relies on `DescribeInstances`/`DescribeSecurityGroupRules`/`DescribeManagedPrefixLists`, none of which support resource-level permissions (Region-only).
**Security Concern (bounded).**
- **A (ID oracle):** `DescribeInstances` returns a silent empty for a real-but-foreign-owned instance ID vs an explicit error for a malformed/nonexistent ID — a boolean existence/ownership oracle. But current-gen IDs are **17 random hex chars (~68 bits)**, so this is a confirm-against-a-known-ID oracle, not an enumeration primitive → **Low/informational, documented behavior.**
- **Footgun (out of scope):** `Describe*` cannot be tag/resource-scoped, so a "read-only inventory" grant sees **all** instances/SGs/AMIs account-wide, with private IPs and public-DNS→IP topology riding along. This is an **intra-account least-privilege limitation the customer must architect around (separate accounts/VPCs)** — AWS documents it openly; **not an exploitable primitive against AWS** (§7).
- **O (detectability):** `Describe*` recon generates CloudTrail management events by default — inventory enumeration is **not stealthy**; informational OPSEC note.
- **Global View** is a client-side single-account Region fan-out using the caller's own creds — **no SLR / Resource Explorer / Organizations aggregation**, so no cross-account aggregation surface here (null).
Doc evidence: `iam-policies-for-amazon-ec2.html` ("Describe\* API actions do not support resource-level permissions"); `list_ec2`/servicereference (no `Resources` for these actions); `ec2-data-inventory.html` (private-IP + public-DNS columns); `global-view.html` (ordinary identity policy, no SLR). Severity-if-true: **Low / Informational** (mostly out-of-scope footgun).

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| `userData` write → root RCE under instance role | `ModifyInstanceAttribute` + Stop/Start | `ec2:Attribute:"userData"` Deny *can* block it, but is non-default — attack the absence of baseline hardening |
| "Read-only inventory" role reads every `userData` secret | `DescribeInstanceAttribute` | **None** — no per-attribute condition key exists; attack = prove inexpressibility via SimulateCustomPolicy |
| SSRF/local process → `userData` + role creds | IMDS `169.254.169.254` | IMDSv2 token (same-host trivial); IMDSv1-optional default widens it — attack the sample's missing `--metadata-options` |
| Victim launches attacker AMI | `DescribeImages` name resolution | `--owners`/owner-id pinning (optional) — attack the unscoped default |
| Owner silently widens consumer ingress; survives unshare | RAM-shared prefix list / shared SG | **None** — no consumer version-pin or circuit breaker; attack the always-latest + stranded-reference design |
| SG associated into unapproved VPC despite `ec2:Vpc` | `AssociateSecurityGroupVpc` | The `ec2:Vpc` condition — attack its wrong-resource binding (home vs target VPC) |
| Tag-scoped Authorize bypassed by omitting TagSpecifications | `AuthorizeSecurityGroup*` | The `security-group-rule` tag condition — attack its "only enforced when TagSpecifications present" opt-out |
| Confused-deputy / full-disk secret dump via export | `ExportImage` + `vmimport` role | Static `ExternalId: vmimport`; optional SourceAccount/SourceArn — attack the verbatim-sample deployment + wildcard role policy |
| AMI shared to a non-member / fabricated org/OU | `ModifyImageAttribute` launchPermission | Format-only validation — attack the absence of membership/existence check + incomplete revoke |
| Cross-account SG reference, no authz, no owner CloudTrail | `AuthorizeSecurityGroup*` referencing foreign `sg-…` | Existence-check only — attack the missing cross-account authz + audit blind spot |
| Snapshot bytes read bypassing AMI-share controls | `ebs:GetSnapshotBlock` | Separate `ebs:` IAM grant + snapshot KMS — attack over-broad `ebs:*` wildcard grants |

## 7. Out-of-Scope Risk Categories
- **Unscopable `Describe*` and over-broad "inventory" roles** (Area 10 footgun) — an intra-account least-privilege limitation the customer architects around; AWS documents it openly. Not an exploitable primitive against AWS.
- **Public DNS→private IP topology exposure** — by-design since EC2's inception; private IPs ride along only on the caller's own-account read.
- **Public AMI / public snapshot visibility cross-account** — the documented sharing model, not a leak (the oracle only distinguishes public/shared vs private-and-foreign).
- **Single-tenant self-DoS / self-inflicted secret storage in user data** — the customer choosing to put secrets in user data is a documented anti-pattern, not an AWS flaw (the *reachability-through-an-unintended-grant* in Area 2 **is** in scope).
- **IMDS on fully-managed hosts, the Nitro/Host-Manager side of any instance, the `vmie.amazonaws.com` fleet identity and the VM Import/Export regional canonical account** — the shared-responsibility/service-plane line; **HARD STOP** on contact, never a test target.
- **Customer-authored IAM policies** that over-grant (vs the AWS-authored `vmimport`/user samples in Area 6, which **are** in scope as copy-verbatim artifacts).
- **Case-sensitivity value trap on `ec2:Attribute` Deny** — carried as a *plausible-but-unconfirmed* sub-lead of Areas 1/5 pending the IAM `StringEquals` operator doc-gap; do not report as a finding until confirmed.

## 8. Null hypotheses / doc gaps
- **Lens D (data→control-plane ENI hop), V (control/storage ENI reach):** N/A on this surface — the inventory APIs are control-plane SigV4 calls; no customer↔control ENI topology is described. Pages checked: target, `global-view.html`, `security-group-rules.md`. (The *network-boundary* content here is SG/prefix-list policy, handled under Areas 4/5/8, not ENI segmentation.)
- **Lens C (STS session-policy / ProvidedContext vending), N (namespace migration):** N/A — no credential-vending lookup, no dual ARN namespace. The only role-assumption is the `vmimport` confused-deputy (Area 6, Lens B/C). Pages checked: `required-permissions.md`, `list_ec2`.
- **Lens F (translation/wire-protocol injection), K (prompt/LLM):** N/A — user data is "opaque data: what you give is what you get back" (no server-side parse/transform); no translator, no LLM. Pages checked: `user-data.md`, target.
- **Lens G (SSRF server-side fetch), J (OAuth/3P link), Q (upload):** N/A for a *service-side* fetch/upload — the only URLs on these pages are doc hyperlinks; the only "fetch" is **instance-local IMDS** (Area 2, Lens T), and the only blob is the customer S3 export artifact (Area 6, Lens T), neither a server-dereferenced customer-supplied URL. No `*Url`/`*Uri`/webhook/logo/avatar field, no 3P OAuth link, no server-parsed upload field. Pages checked: target, `user-data.md`, `AMIs.md`, `required-permissions.md`.
- **Lens H (KMS encryption-context confusion):** carried only as the Area-6 `vmimport` KMS `Resource:"*"` breadth (Lens R); no per-resource branch-key / encryption-context pattern on these pages. Pages checked: `required-permissions.md`.
- **Lens M (shared-id interception), W (attestation), Y (transport/TLS/sig), BB (canonicalization/multi-parser), CC (upstream-context), DD (cache-key), FF (JWT/OIDC):** N/A — no session/presigned-id, no PCR/attestation gate, no documented transport-floor or SigV2 acceptance, no multi-parser request path, no authorizer-emitted context, no caching layer, no JWT in the inventory surface. Pages checked: target + the six fan-out clusters.
- **Lens X alias hypothesis:** refuted — `CancelConversionTask`/`CancelImportTask`/`CancelExportTask` are distinct co-listed actions; the live `ebs:GetSnapshotBlock` cousin is the surviving Lens-X lead (Area 9).
- **Doc-gaps to close before hunting:** (1) exact EC2 API error codes `InvalidInstanceID.Malformed` vs `.NotFound` for the Area-10 oracle; (2) the IAM `StringEquals` value case-sensitivity statement (Areas 1/5); (3) a dedicated resource-ID-format page (`resource-ids.html` is retired — ID entropy inferred from live example IDs only); (4) formal deprecation status of `cancel-conversion-task`; (5) whether a *newer* `ec2:Attribute`-style condition key has since been added to `DescribeInstanceAttribute` (re-grep `list_ec2` at hunt time — would partially close Area 2 lead #1). The Service Authorization Reference HTML is too large to render in full; use `servicereference.us-east-1.amazonaws.com/v1/ec2/ec2.json` as the authoritative machine copy.
