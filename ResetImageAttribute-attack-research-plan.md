# EC2 `ResetImageAttribute` (AMI launch-permission model) — Attack Research Plan

**Source of leads:** docs.aws.amazon.com (verified against offline mirror `/work/aws-docs/docs`):
- `AWSEC2/latest/APIReference/API_ResetImageAttribute.md` (target), `API_ModifyImageAttribute.md`, `API_DescribeImageAttribute.md`, `API_CancelImageLaunchPermission.md`
- `AWSEC2/latest/UserGuide/`: `sharing-amis.md`, `sharingamis-intro.md`, `sharingamis-explicit.md`, `share-amis-with-organizations-and-OUs.md`, `share-amis-org-ou-manage.md`, `cancel-sharing-an-AMI.md`, `block-public-access-to-amis.md`, `manage-block-public-access-for-amis.md`, `usingsharedamis-finding.md`, `ec2-allowed-amis.md`
- `service-authorization/latest/reference/list_ec2.md` (IAM actions + `image` resource condition keys)
- Target devguide page: `ec2/latest/devguide/example_ec2_ResetImageAttribute_section.html` (online == offline, confirmed 2026-10-20)

**Status:** documentation-derived hypotheses only. Nothing has been tested against a live AWS account. Every lead below is a boundary that the docs imply *should* hold, written so a hunter with two cooperating test accounts can confirm or refute it.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered); look left and right for adjacent bugs the plan did not anticipate.
- **DryRun is NOT an ownership oracle.** `DryRun` on these APIs (`ResetImageAttribute`, `ModifyImageAttribute`, `DescribeImageAttribute`, `CancelImageLaunchPermission`) returns `DryRunOperation` vs `UnauthorizedOperation` based on *caller IAM only*, evaluated before resource ownership resolution. Never treat a `DryRunOperation` as proof you can touch a foreign resource — it is a false-positive trap. Confirm with a real (canary) call.
- **AMI resource IDs are structured and carry a checksum** (`ami-<17 hex>` modern / `ami-<8 hex>` legacy). A *fabricated* foreign AMI id generally cannot be made to validate; enumeration must use ids observed from `DescribeImages` with public/shared filters, not brute force. Treat "cannot fabricate a valid foreign id" as a genuine null for pure-guess IDOR.
- **HARD STOP:** the moment any evidence shows an identity, credential, ARN, or account belonging to **AWS's own service plane** (e.g. an AMI owned by the `amazon`/`aws-marketplace` alias resolving to AWS-internal infrastructure, or a KMS/snapshot grant naming an AWS-service account), stop, preserve evidence, and flag for AWS-Security disclosure. Do not escalate.
- Use **synthetic/canary AMIs and snapshots** only. Never reset/modify launch permissions on an AMI you do not own in a test account, and never act on production or third-party AMIs.

---

## 1. Pentest Objectives

Concrete boundary-breach outcomes a hunter is trying to achieve (each maps to a lens in Section 5):

1. **Cross-account launch-permission mutation** — call `ResetImageAttribute` / `ModifyImageAttribute` against an AMI owned by *another* account and have it take effect (strip or add launch permissions on a resource you do not own). *Expected to be blocked by the documented "your AWS account must own the AMI" rule — prove the rule actually holds across all four sibling APIs.*
2. **Cross-account launch-permission disclosure** — read the full `launchPermission` grantee list (account IDs, org/OU ARNs) of an AMI you do not own via `DescribeImageAttribute` or a sibling.
3. **Griefing / availability** — as a shared-to or unrelated account, remove *other* grantees' or an owner's launch permissions (e.g. coerce `CancelImageLaunchPermission` or `ResetImageAttribute` to affect someone other than the caller).
4. **Revocation incompleteness** — after `ResetImageAttribute` wipes launch permissions, retain access to the AMI's backing EBS snapshot data / KMS decrypt / running instances (see deep-dive Section 5-Area-F).
5. **Unintended public exposure / Block-Public-Access bypass** — make an AMI public despite BPA, or keep an already-public AMI reachable after it was "made private" (see deep-dive Section 5-Area-G).
6. **IAM condition-key bypass** — defeat a Deny/Allow keyed on `ec2:Public` / `ec2:Owner` / `ec2:ImageType` guarding these attribute mutations.
7. **Unvalidated grantee land-grab** — share to / be resolved as an organization, OU, or account that does not exist or that the sharer is not a member of.

---

## 2. Components, Assets, and Design

### What the target actually is
`ResetImageAttribute(ImageId, Attribute=launchPermission[, DryRun])` resets an AMI attribute to its **default**. Today `launchPermission` is the **only** valid attribute. The documented effect (CLI/PowerShell help + `sharingamis-explicit.md`): *"removes all public and explicit launch permissions from the specified AMI … the owner of the AMI always has launch permissions and is therefore unaffected."* The target devguide page states *"By default, AMIs are private."* So `ResetImageAttribute` = **"make this AMI fully private again."** No output on success; `return=true`.

It is one of a **four-API family** that manages the single mutable security-relevant attribute of an AMI — its `launchPermission` list:

| API | Role | Who is supposed to call it |
|---|---|---|
| `ModifyImageAttribute` (Attribute=launchPermission, Add/Remove) | Add/remove grantees: `UserId` (account), `UserGroup=all` (public), `OrganizationArn`, `OrganizationalUnitArn` | **Owner only** |
| `ResetImageAttribute` (Attribute=launchPermission) | Wipe **all** grantees → private | **Owner only** |
| `DescribeImageAttribute` (Attribute=launchPermission) | Read the grantee list | Owner (reads full list) |
| `CancelImageLaunchPermission` | Remove **the caller's own** account from a shared AMI's launch permissions | **A shared-to (non-owner) account**, on an AMI it does not own |

### Assets
- **The `launchPermission` list** of each AMI — the access-control data itself. Its grantees are: AWS account IDs (12-digit), the special group `all` (= public), organization ARNs, OU ARNs.
- **Grantee account IDs / org/OU ARNs** — disclosed by `DescribeImageAttribute` (example response shows `<userId>495219933132</userId>`). These are tenant-identifying data.
- **The AMI itself** and its backing **EBS snapshots + KMS keys** — sharing the AMI grants *launch-time* access to referenced snapshots without sharing the snapshots directly (deep-dive Area F).
- **Account-level Block-Public-Access-for-AMIs setting** (per-Region; optionally governed by an Organizations *declarative policy*).

### Identity / ownership model
- Identity: SigV4 IAM principals. Authorization: IAM action `ec2:ResetImageAttribute` (access level **Write**), plus — critically — an **ownership check** the docs assert in prose ("To share an AMI, your AWS account must own the AMI"). The `image` resource carries condition keys `ec2:Owner` (owning account), `ec2:Public`, `ec2:ImageID`, `ec2:ImageType`, `ec2:RootDeviceType`, `ec2:Region`, `aws:ResourceTag/*`.
- `CancelImageLaunchPermission` is the one deliberate **cross-account write**: IAM access level **"Permissions management, Write"**, and it mutates the launch-permission list of an AMI the caller does **not** own — but is documented to only ever remove the caller's *own* account (the API takes no target principal parameter, only `ImageId`).

### Connection diagram (control-plane only; no data plane in the target)
```
  Caller (account A, IAM principal)
        │  SigV4  ec2:ResetImageAttribute / ModifyImageAttribute / DescribeImageAttribute
        ▼
  EC2 control plane ──► [IAM authorizer: action + resource(image*) + condition keys]
        │                          │
        │                          └─► ownership gate ("account must own the AMI")  ← prose-asserted
        ▼
  AMI launchPermission list  ──(grants launch access to)──►  backing EBS snapshots + KMS CMK
        ▲                                                         (cross-account at launch time)
        │  CancelImageLaunchPermission (account B = shared-to, non-owner, removes SELF only)
  Caller (account B)
```

### Mandatory coverage sweep — pages checked (so null verdicts are evidenced)
- **URL/fetch fields (Lens G):** none. No field on any of the four APIs is a URL/host the service dereferences. Checked: all four API reference pages + sharing pages. → **SSRF N/A (evidenced).**
- **Upload/blob fields (Lens Q):** none. No file/image/blob input. `uefiData`/`productCodes` are read-only via `DescribeImageAttribute`, not writable here. → **Upload N/A (evidenced).**
- **Gates before privileged state change (Lens P):** the ownership gate; BPA setting; Marketplace-product-code "cannot be made public" constraint. Covered in Areas B, G.
- **"Revealed only after a step" (Lens A disclosure):** grantee account IDs/ARNs visible via `DescribeImageAttribute` (owner); shared-to accounts cannot see owner's tags except `ec2:SharedTag/` prefix. Covered in Area C.
- **IAM artifacts (Lens R/S):** the `image` resource condition keys in `list_ec2.md`; the AWS-managed role `AWSDataLifecycleManagerServiceRoleForAMIManagement` references `ResetImageAttribute` — pull and audit (Area H).
- **Generated secrets (Lens T):** the KMS CMK + EBS snapshot reachability granted by a share (Area F).
- **Guarantee words (Lens U):** "By default AMIs are private"; "must own the AMI"; "cannot be made public" (Marketplace); "the owner … always has launch permissions"; "Other users can't alias their AMIs"; BPA "any attempt to make an AMI public is automatically blocked." Covered in Areas B, D, G.

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating? | Internet-facing | Functionality | Callable by | Notes / lead |
|---|---|---|---|---|---|---|---|
| `ResetImageAttribute` | POST/Query | Existing | **Mutating** | Yes | Wipe launchPermission → private | Owner (asserted) | **Target.** Only `launchPermission` valid. No per-grantee granularity — all-or-nothing. |
| `ModifyImageAttribute` | POST/Query | Existing | **Mutating** | Yes | Add/Remove launchPermission grantees; also `description`, `imdsSupport` | Owner (asserted) | Grantee types: `UserId`, `UserGroup=all`, `OrganizationArn.N`, `OrganizationalUnitArn.N`. `ProductCode.N` = "Not supported". Write-twin of Reset. |
| `DescribeImageAttribute` | POST/Query | Existing | Non-mutating | Yes | Read one attribute incl. `launchPermission`, `productCodes`, `uefiData`, `lastLaunchedTime`, `deregistrationProtection` | List access | Returns grantee account IDs + org/OU. Read side of the IDOR pair. |
| `CancelImageLaunchPermission` | POST/Query | Existing | **Mutating (cross-account)** | Yes | Remove caller's own account from a shared AMI | **Non-owner (shared-to)** | Access level **Permissions management, Write**. No target param — self-only by design. Parity/abuse candidate. |
| `EnableImageBlockPublicAccess` / `DisableImageBlockPublicAccess` / `GetImageBlockPublicAccessState` | POST/Query | Existing | Mutating / read | Yes | Toggle/read account-level BPA-for-AMIs | Admin (restrictable) | Governs whether `ModifyImageAttribute …Group=all` can succeed. Deep-dive Area G. |
| `DescribeImages` (with `--executable-users`, `is-public`, `owner-alias` filters) | Query | Existing | Non-mutating | Yes | Enumerate public / shared-to-me AMIs; source of valid foreign AMI ids | all | The practical id-discovery oracle feeding every IDOR lead. |

**Undocumented / console-hidden knob sweep:** `ResetImageAttribute` exposes only `Attribute=launchPermission` — no hidden permissive enum today, but the API is explicitly forward-looking ("currently you can only reset the launch permission attribute"). `DescribeImageAttribute` accepts a *much larger* attribute enum (`kernel|ramdisk|productCodes|sriovNetSupport|bootMode|tpmSupport|uefiData|lastLaunchedTime|imdsSupport|deregistrationProtection|blockDeviceMapping`) — the read surface is far wider than the write surface; `blockDeviceMapping` is documented-deprecated and returns `Client.AuthFailure` (a differential-error signal). `ModifyImageAttribute` accepts `ProductCode.N` marked "Not supported" yet still present in the model — test whether it is silently accepted (Area B).

---

## 4. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Account A principal | AMI owned by account B | `ResetImageAttribute` / `ModifyImageAttribute` with B's `ami-…` id | Launch-permission list of B's AMI changes on A's call → **cross-account write breach (Critical)**. |
| Account A principal | Launch-permission list of B's AMI | `DescribeImageAttribute Attribute=launchPermission` | A reads B's grantee account IDs / org / OU ARNs → **cross-account disclosure breach (High)**. |
| Shared-to account B | AMI owned by A (launch-perm list) | `CancelImageLaunchPermission` (by design removes B only) | B's call removes an account *other than B*, or removes A's owner grant → **breach**. Self-only removal = expected (no breach). |
| AMI owner A | Backing EBS snapshot + KMS CMK of A | Share grants grantee launch-time snapshot access | After `ResetImageAttribute` revokes the share, grantee B still reads snapshot data / decrypts / launches → **revocation-incompleteness breach (High)** (Area F). |
| AMI owner A (under BPA) | Public (`Group=all`) | `ModifyImageAttribute …Add…Group=all` | Succeeds despite BPA enabled, or an already-public AMI stays reachable after "made private" → **unintended-public-exposure breach (High)** (Area G). |
| Policy author | `ec2:Public` / `ec2:Owner` Deny on image mutation | IAM condition-key evaluation | A crafted request classified "allowed" by the condition key reaches the mutation the Deny intended to stop → **condition-key bypass (Medium–High)** (Area D). |
| AMI owner A | Non-existent / non-member org or OU | `ModifyImageAttribute OrganizationArn.N` | Share accepted for an org/OU that doesn't exist or A isn't a member of → **unvalidated-grantee land-grab (Medium–High)** (Area E). |
| **Any caller** | **AWS service-plane AMI** (`amazon`/`aws-marketplace` alias) | any of the four APIs | Any mutation/credential/ARN touching AWS's own fleet → **HARD STOP, disclose.** |

---

## 5. Recommended Areas of Focus

> Ordered by priority: cross-account write/disclosure first, then revocation & public-exposure, then condition-key & IAM-artifact hardening.

### Area A — Cross-account launch-permission mutation & authorization parity across the four-API family  *(Lens A + Lens X — highest priority)*

**Background.** All four APIs name an AMI by a bare `ImageId` in the request. The owner-only rule for mutation is asserted in *prose* ("To share an AMI, your AWS account must own the AMI"; "users … can't delete, share, or modify it"), not in the API contract. `CancelImageLaunchPermission` is deliberately cross-account and sits in the same family — a prime place for a validator to diverge between the four code paths that all mutate one list.

**Security Concern.** If any one of `ResetImageAttribute` / `ModifyImageAttribute` / `CancelImageLaunchPermission` resolves the AMI and mutates its launch-permission list *before or instead of* enforcing ownership — or enforces ownership differently than its siblings — a non-owner can strip, add, or reset grantees on a resource it does not own. Because the four actions share one underlying list, a parity gap in one path is a cross-account write.

**High-level Test Scenarios (falsifiable):**
- **Claim:** Account A can call `ResetImageAttribute` on account B's private AMI and wipe B's launch permissions. **Mechanism:** target API takes only `ImageId`; ownership is prose-asserted. **Oracle:** from A, `reset-image-attribute --image-id <B's ami>`; then B runs `describe-image-attribute … launchPermission` and sees its grantees removed. Expected: `AuthFailure`/`InvalidAMIID`/`AccessDenied` for A. **Severity if true:** Critical (cross-account write / griefing).
- **Claim:** Account A can call `ModifyImageAttribute …Remove…UserId=<C>` on B's AMI, severing B↔C sharing. **Oracle:** C loses `describe-images --executable-users self` visibility of B's AMI after A's call. **Severity:** Critical.
- **Claim (parity/twin, Lens X):** `CancelImageLaunchPermission` removes an account **other than** the caller, or removes the **owner's** grant. **Mechanism:** API takes only `ImageId`, no target — but test whether an undocumented/body-injected principal, or calling it against an AMI shared to an *org/OU* (docs say it *cannot* be used for org/OU shares) behaves inconsistently. **Oracle:** after B calls cancel on an org-shared AMI, check whether B (or a sibling org account) actually lost access despite the documented limitation. **Severity:** High.
- **Claim (validator divergence oracle, Lens A variant):** the four APIs return *different* errors (`AuthFailure` vs `InvalidAMIID.NotFound` vs `InvalidAMIID.Unavailable` vs 500) for the same foreign/nonexistent id, forming an existence-enumeration oracle across tenant boundaries. **Oracle:** diff error code/latency for (a) own AMI, (b) a real foreign private AMI id, (c) a well-formed nonexistent id. **Severity:** Low–Medium (enumeration enabler).

**Doc evidence:** `API_ResetImageAttribute.md`, `API_ModifyImageAttribute.md`, `API_CancelImageLaunchPermission.md`; `sharingamis-explicit.md` ("must own"; "can't … modify it"); `cancel-sharing-an-AMI.md` (org/OU limitation). **Severity-if-true:** Critical (write) / High (parity) / Low–Medium (oracle). **Stop condition:** one confirmed cross-account mutation = report immediately; do not iterate across more AMIs.

### Area B — Marketplace & attribute-scope integrity on the mutation path  *(Lens U + Lens X)*

**Background.** `ModifyImageAttribute` docs state *"Images with an AWS Marketplace product code cannot be made public"* and carry a `ProductCode.N` parameter marked **"Not supported."** `ResetImageAttribute` only accepts `launchPermission`, but `ModifyImageAttribute` multiplexes `launchPermission` / `description` / `imdsSupport` and several grantee sub-parameters (`UserId`, `UserGroup`, `OrganizationArn`, `OrganizationalUnitArn`, `OperationType`) that are only valid "when the `Attribute` parameter is `launchPermission`."

**Security Concern.** A parameter-combination or ordering trick (e.g. supplying `LaunchPermission.Add.Group=all` together with `Attribute=description`, or populating `ProductCode.N` despite "Not supported", or mixing `OperationType` with a non-launchPermission attribute) could bypass the Marketplace "cannot be made public" constraint or cause a grantee change to be applied under a code path that skipped the public-share guard/BPA.

**High-level Test Scenarios:**
- **Claim:** A Marketplace-product-code AMI can be made public by routing the `Group=all` add through an unexpected attribute/parameter combination. **Oracle:** `describe-image-attribute … launchPermission` shows `group=all` on a product-coded AMI. **Severity:** High (unintended public exposure of a paid/isolated image).
- **Claim:** `ProductCode.N` ("Not supported") is silently accepted and mutates product codes, flipping an AMI into or out of the Marketplace-constrained class and thereby changing whether it can be made public. **Oracle:** product code appears/disappears via `describe-image-attribute … productCodes`. **Severity:** Medium–High.
- **Claim:** Sub-parameters documented as "launchPermission-only" (`OrganizationArn`, `OperationType`) are honored when `Attribute` is set to `description`/`imdsSupport`, skipping launch-permission validation. **Oracle:** launch-permission change takes effect under a non-launchPermission attribute call. **Severity:** Medium–High.

**Doc evidence:** `API_ModifyImageAttribute.md` lines 12, 53–82. **Severity-if-true:** High. **Stop condition:** confirm the public flag flipped once; stop.

### Area C — Cross-account disclosure of the grantee list & shared-tag leakage  *(Lens A disclosure-timing + Lens I)*

**Background.** `DescribeImageAttribute Attribute=launchPermission` returns the AMI's grantee list — account IDs, org ARNs, OU ARNs (sample response: `<userId>495219933132</userId>`). Account IDs are documented as tenant identifiers. Sharing docs state other accounts *cannot* see the owner's tags **except** tags with the `ec2:SharedTag/` prefix, which are visible to all shared-to accounts and *only the owner* can create/modify/delete.

**Security Concern.** (1) Whether a **non-owner** (e.g. a shared-to account, or any account) can read the *full* grantee list of an AMI — exposing which other accounts/orgs an AMI is shared with. (2) Whether the `ec2:SharedTag/` visibility or mutation restriction can be broken (a shared-to account creating/modifying a shared tag, or seeing non-shared tags).

**High-level Test Scenarios:**
- **Claim:** A shared-to account B can enumerate *all* grantees of A's AMI (not just itself) via `DescribeImageAttribute`. **Oracle:** B's call returns C's `userId`/org ARN. **Severity:** High (cross-account relationship disclosure).
- **Claim:** An unrelated account can read `launchPermission` of a public AMI and of a privately-shared AMI it is not a grantee of. **Oracle:** non-empty grantee list returned to a non-grantee. **Severity:** Medium–High.
- **Claim:** A shared-to account can create/modify an `ec2:SharedTag/` tag (docs say only the owner can). **Oracle:** tag mutation by non-owner succeeds / non-shared tags become visible. **Severity:** Medium.

**Doc evidence:** `API_DescribeImageAttribute.md` (example 1); `sharingamis-explicit.md`/`share-amis-with-organizations-and-OUs.md` ("other accounts cannot see the tags … exception `ec2:SharedTag/` … Only the resource owner can create, modify, or delete"). **Severity-if-true:** High. **Stop condition:** one cross-account disclosure confirmed = report.

### Area D — IAM condition-key scoping semantics for the `image` resource  *(Lens S + Lens U)*

**Background.** The `image` resource supports condition keys `ec2:Owner`, `ec2:Public`, `ec2:ImageID`, `ec2:ImageType`, `ec2:RootDeviceType`, `ec2:Region`, `aws:ResourceTag/*` (from `list_ec2.md`). `ResetImageAttribute` / `ModifyImageAttribute` are **Write** actions on `image*`. Customers build Denies like "deny making images public" or "only act on images I own" using these keys. (`ResetImageAttribute`'s own top-level action row shows an *empty* condition-key cell — resource-level keys attach via the `image` resource type.)

**Security Concern.** Classic condition-key fail-open shapes (per the skill's Lens-S variants): does `ec2:Public` evaluate the image's **current** state or the **requested** new state (so a Deny on `ec2:Public=true` fails to stop a *transition* to public)? Is `ec2:Owner` the AMI's owning account (so `ec2:Owner` ≠ caller can scope out foreign images — and does it actually populate on these attribute APIs)? Case-sensitivity / absent-key fail-open on `ec2:ImageType` / `ec2:Public`. Whether a Deny keyed on these is simply *inert* on the attribute-mutation path because the key does not populate there.

**High-level Test Scenarios:**
- **Claim:** A Deny `ec2:ModifyImageAttribute` with `Condition: Bool{ec2:Public: true}` does NOT prevent an AMI being *made* public (key reflects pre-request state or is absent at eval). **Oracle:** under a principal holding that Deny, `…Add…Group=all` still succeeds. **Severity:** High (guardrail believed-enforced is advisory).
- **Claim:** `ec2:Owner` does not populate / is ignored on `ResetImageAttribute`, so a policy intending "only reset images I own" is inert. **Oracle:** `SimulatePrincipalPolicy` first (no resources touched), then a scoped canary call. **Severity:** Medium–High.
- **Claim:** `ec2:Public` / `ec2:ImageType` are case-sensitive and a Deny written against one casing is inert against the request's casing. **Oracle:** simulate both casings. **Severity:** Medium.

**Doc evidence:** `service-authorization/latest/reference/list_ec2.md` (`image` resource condition keys; `ResetImageAttribute`/`ModifyImageAttribute` rows). **Severity-if-true:** Medium–High. **Oracle note:** use `iam:SimulatePrincipalPolicy`/`SimulateCustomPolicy` as the safe first oracle; escalate to a live scoped canary call only to confirm. **Stop condition:** confirm the Deny is inert via simulate + one canary.

### Area E — Unvalidated org / OU grantee (land-grab & confused sharing)  *(Lens AA grantee-validation)*

**Background.** `ModifyImageAttribute` accepts `OrganizationArn.N` and `OrganizationalUnitArn.N`. Docs state *"The AMI owner can share an AMI with any organization or OU, including organizations and OUs that they're not a member of"* and warn that specifying a bare ID instead of a full ARN errors. Sharing with an OU grants **all nested child accounts** access.

**Security Concern.** Since an owner may share with orgs/OUs it is not a member of, the grantee target is validated for *format* but possibly not for *existence/ownership*. This is the Lens-AA "unvalidated grantee" shape and an Organizations-side confused-deputy surface: can an AMI be shared to a **non-existent** org/OU ARN (stored, then satisfied later when that ARN is created — a land-grab), or to an attacker-crafted ARN that resolves to accounts the sharer did not intend? Conversely, does revoking an org/OU share propagate to all nested accounts promptly?

**High-level Test Scenarios:**
- **Claim:** `ModifyImageAttribute …Add…OrganizationalUnitArn=<well-formed but non-existent OU>` is accepted and stored. **Oracle:** `describe-image-attribute … launchPermission` lists the bogus OU; later creation of a matching OU grants access (land-grab). **Severity:** Medium–High.
- **Claim:** Sharing to an OU ARN in a *different* org's namespace resolves to that org's accounts. **Oracle:** an account under the foreign OU gains `--executable-users self` visibility. **Severity:** High (cross-org exposure) — *if this ever reaches an AWS-owned org, HARD STOP.*
- **Claim (revoke side):** After `ResetImageAttribute` wipes an org/OU grant, a child account that already launched retains access (ties to Area F). **Oracle:** child-account instance launch still succeeds post-reset. **Severity:** High.

**Doc evidence:** `share-amis-with-organizations-and-OUs.md` (considerations: "any organization or OU, including … not a member of"; ARN-format warning); `share-amis-org-ou-manage.md`. **Severity-if-true:** Medium–High. **Stop condition:** confirm acceptance of one bogus grantee; stop.

### Area F — Shared-snapshot / KMS reachability & revocation completeness  *(Lens T + Lens H + Lens AA — DEEP DIVE, see integrated findings below)*

**Background.** Sharing docs: *"You do not need to share the Amazon EBS snapshots that an AMI references in order to share the AMI … the system provides the instance access to the referenced EBS snapshots for the launch."* For encrypted AMIs, the grantee must additionally be allowed to use the CMK. The central question for the **target** (`ResetImageAttribute`, which *removes* the share): does removing launch permission actually sever the grantee's downstream access to snapshot data, KMS decrypt, and running instances — or does a derived capability linger?

> **Integrated deep-dive findings for this area are appended in Section 9-A (subagent: shared-snapshot/KMS).**

### Area G — Block-Public-Access-for-AMIs & "default private" guarantee enforcement  *(Lens U + Lens AA — DEEP DIVE, see integrated findings below)*

**Background.** BPA-for-AMIs: *"When block public access is enabled, any attempt to make an AMI public is automatically blocked. However, if you already have public AMIs, they remain publicly available."* Per-Region, account-level, optionally via an Organizations declarative policy ("you can't modify the setting directly within an account" when a declarative policy is in use). Default enabled for new accounts; **disabled** for accounts that had any public AMI on/after 2023-07-15. `ResetImageAttribute` is the "go private" path — its interaction with BPA (which only blocks "going public") is the enforcement seam.

> **Integrated deep-dive findings for this area are appended in Section 9-B (subagent: BPA & guarantees).**

### Area H — AWS-authored IAM artifact: DLM service role referencing `ResetImageAttribute`  *(Lens R)*

**Background.** The AWS-managed policy `AWSDataLifecycleManagerServiceRoleForAMIManagement` (found in the mirror referencing `ResetImageAttribute`) is attached to the DLM service-linked/service role for AMI lifecycle management — a copy-verbatim, customer-uneditable artifact.

**Security Concern.** Audit confirms (from the mirrored policy JSON) the statement:
```json
{ "Effect": "Allow",
  "Action": ["ec2:ResetImageAttribute","ec2:DeregisterImage","ec2:CreateImage","ec2:CopyImage","ec2:ModifyImageAttribute"],
  "Resource": "*" }          // no Condition block, no ec2:Owner / tag scoping
```
Both launch-permission mutators are granted on **`Resource:"*"` with no condition**. The DLM service role can therefore `ResetImageAttribute`/`ModifyImageAttribute` (and `DeregisterImage`) against **any image the role can name**, not just those managed by a lifecycle policy. The artifact is AWS-authored and customer-uneditable (copy-verbatim via the service-linked role), so a scoping gap here is AWS's defect (Tier 2), not a customer footgun. The hunter's job is to determine whether this grant is actually reachable/abusable — i.e. whether a lower-privileged principal that can influence DLM (or assume/pass into the role) can leverage the unconditioned grant to reset/modify launch permissions on images outside its lifecycle scope.

**High-level Test Scenarios:**
- **Claim:** A principal holding only this managed policy can `ResetImageAttribute`/`ModifyImageAttribute` on an image not covered by any DLM lifecycle policy (the `Resource:"*"` has no owner/tag condition). **Oracle:** `iam:SimulatePrincipalPolicy` under a role holding exactly the artifact (safe first oracle, no resources touched) → `allowed`; then a scoped canary call on an own test AMI tagged outside any DLM policy. **Severity:** Medium (over-broad AWS-authored grant; reportable because uneditable — Tier 2).
- **Claim:** The `ec2:DescribeImageAttribute` + `CreateImage`/`CopyImage` + `DeleteSnapshot` combination (all `Resource:"*"`/`snapshot/*`) lets the DLM role read/copy/delete across images/snapshots beyond intended scope. **Oracle:** simulate each action against a foreign-tagged resource ARN. **Severity:** Medium.

**Doc evidence:** `aws-managed-policy/latest/reference/AWSDataLifecycleManagerServiceRoleForAMIManagement.md`; `ebs/latest/userguide/managed-policies.md`, `service-role.md`. **Severity-if-true:** Medium. **Stop condition:** read + simulate; no live resource mutation needed.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Non-owner resets/modifies/reads another account's AMI launch permissions | `Reset`/`Modify`/`Describe`/`CancelImageLaunchPermission` | "your AWS account must own the AMI"; "can't … modify it" (prose ownership gate) |
| `CancelImageLaunchPermission` removes an account other than caller / owner grant | `CancelImageLaunchPermission` | "Removes **your** AWS account"; no target param; owner "always has launch permissions" |
| Marketplace-coded AMI made public via parameter trick | `ModifyImageAttribute` | "Images with an AWS Marketplace product code cannot be made public"; `ProductCode.N` "Not supported" |
| Grantee retains snapshot/KMS/instance access after `ResetImageAttribute` | AMI↔snapshot↔KMS linkage | Reset "removes all public and explicit launch permissions" (Section 9-A) |
| Make AMI public despite BPA, or already-public AMI stays reachable | BPA-for-AMIs setting | "any attempt to make an AMI public is automatically blocked" (per-Region) (Section 9-B) |
| Deny on `ec2:Public`/`ec2:Owner` bypassed on mutation path | IAM condition keys on `image` | `ec2:Public`/`ec2:Owner` condition keys |
| Share accepted to non-existent / non-member org/OU | `ModifyImageAttribute OrganizationArn/OrganizationalUnitArn` | ARN-format validation; Organizations membership (Area E) |
| Grantee-list enumeration via differential errors | all four APIs | distinct error codes; AMI id checksum |

---

## 7. Out-of-Scope Risk Categories

- **Customer-authored least-privilege footguns** — a customer writing an over-broad IAM policy for themselves (in scope only for the *AWS-authored* DLM managed policy, Area H).
- **Integrity/security of third-party shared AMIs** — "You use a shared AMI at your own risk; Amazon can't vouch for the integrity or security of AMIs shared by other users." Backdoored/malicious *content* of a foreign AMI is a user-due-diligence matter, not a service boundary bug (unless the sharing mechanism itself is broken).
- **Single-account self-DoS** — resetting your own AMI's permissions.
- **IMDS on instances launched from an AMI** — the instance's runtime posture (unless `imdsSupport`/AMI-config integrity is the vector, Area B).
- **Shared storage / Grover / EBS backend infrastructure internals** — AWS-owned.
- **AWS service-plane AMIs (`amazon`/`aws-marketplace` alias)** — HARD STOP + disclose, not a target.
- **DNS rebinding / network-layer attacks** — no network/data plane in this target.

---

## 8. Null hypotheses / doc gaps

- **SSRF (Lens G): N/A** — pages checked: all four API references + all sharing/BPA pages; no field is a URL/host the service dereferences. Genuine null.
- **Upload/file parsing (Lens Q): N/A** — pages checked: same set; no blob/file/image input on the write path. Genuine null.
- **Translation-layer/injection (Lens F): N/A** — no customer-input-to-backend-language transform; inputs are an AMI id, an attribute enum, and principal/ARN grantees validated structurally.
- **Prompt injection / LLM (Lens K): N/A** — no LLM/agent in this surface.
- **Attestation-gated auth (Lens W): N/A** — no attestation condition on these APIs (NitroTPM/`uefiData` are read-only via `DescribeImageAttribute`, not gated here).
- **Fabricated-id pure-guess IDOR:** partial null — AMI ids carry a checksum, so a *guessed* foreign id won't validate; IDOR leads (Area A/C) must use ids discovered via `DescribeImages` public/shared filters.
- **Doc-gap — confirm surface first:** (1) the exact ordering of ownership check vs AMI resolution in each of the four APIs (prose only); (2) whether `DescribeImageAttribute launchPermission` is readable by non-owners/non-grantees; (3) the lifetime of snapshot/KMS access after launch-permission revocation (Area F); (4) whether org/OU grantee ARNs are validated for existence/membership at `ModifyImageAttribute` time (Area E). Each marked for live confirmation by the hunter before deeper work.

---

## 9. Integrated Deep-Dive Findings (subagent documentation analysis)

*(Populated from two documentation-only subagent passes — snapshot/KMS reachability and BPA/guarantee enforcement. See Sections 9-A and 9-B below.)*

### 9-A. Shared-snapshot / KMS reachability & revocation completeness (Area F deep-dive)

**Core thesis:** `ResetImageAttribute` wipes the AMI's `launchPermission` list, but a grantee's *derived* access to the underlying data is established through **separate resources** (the backing EBS snapshot's `createVolumePermission`, the CMK key policy, and per-volume KMS grants) whose lifecycles are **not tied to the AMI's launch-permission state**. "I reset the AMI" is therefore not equivalent to "I revoked this account's access to the data." Five concrete leads:

- **[Critical — by design] Default launch/copy re-encrypts under the grantee's OWN key → permanent independent copy.** `AMIEncryption.md` states an encrypted snapshot you don't own (shared AMI) is, on launch/`CopyImage` with no `KmsKeyId`, *"restored to a volume that is encrypted by **your AWS account's default KMS key**."* Combined with `sharingamis-explicit.md` "Usage" (*"after they have launched an instance … they can then create an AMI from their instance"*), once a grantee launches **even once**, they hold a self-keyed copy that survives any owner-side `ResetImageAttribute`, key-policy revoke, or snapshot delete. **Oracle:** grantee B launches from A's encrypted shared AMI (no enc params); `describe-volumes` shows the root volume's `KmsKeyId` = B's own default key, not A's CMK; A then fully revokes — B's instance and its ability to `CreateImage`/`CreateSnapshot` are unaffected. **Severity: Critical** (documented default behavior — revocation gives a false sense of undoing past exposure).
- **[Critical — by design] Snapshot `createVolumePermission` / S3 / CMK grants for *copy* outlive the AMI reset.** `how-ami-copy-works.md` (Cross-account copying): to let a grantee copy a shared AMI, the owner must grant read on *the storage that backs the AMI, not just the AMI itself* — set via `modify-snapshot-attribute` `createVolumePermission` on the **snapshot** (a different resource/API than `ResetImageAttribute`). `ResetImageAttribute` accepts only `Attribute=launchPermission`, so it cannot touch snapshot permissions. **Oracle:** A shares AMI + snapshot (`modify-snapshot-attribute add --user-ids B`) + CMK; A then calls only `reset-image-attribute`; B runs `create-volume --snapshot-id <snap>` directly (no AMI ref) and succeeds. **Severity: Critical** (fully independent data path survives AMI "revocation").
- **[High] `ModifyImageAttribute Remove={UserId=X}` returns false-success when an org/OU share overlaps.** `share-amis-org-ou-manage.md` states verbatim: *"If you try to stop sharing the AMI by removing launch permissions for the account, Amazon EC2 returns a success message. **However, the AMI continues to be shared with the account.**"* So targeted `Remove` is an **unreliable revocation primitive**; only `ResetImageAttribute` (which clears `UserId`+`Group`+`OrganizationArn`+`OrganizationalUnitArn` as one list) or explicit OU removal actually closes the door. **Oracle:** A shares to Org O (containing B) **and** to B's account id; `Remove UserId=B` returns `true`; `describe-image-attribute launchPermission` still lists the OU; B can still `RunInstances`; then `reset-image-attribute` and B fails. **Severity: High** (a security control's own success signal is a documented false positive — directly extends the exposure window for the Critical leads above).
- **[High] Per-volume KMS grant lifecycle is tied to the volume/instance, not the AMI share.** `kms/.../determining-access-grants.md` shows the cross-account decrypt is a KMS **grant** to an EC2-infrastructure assumed-role in the grantee account, constrained to one volume via `EncryptionContextSubset{aws:ebs:id}`. KMS docs (`grants.md`, `grant-best-practices.md`) note service-created grants have lifecycles tied to their resource and *"do not automatically expire."* No doc links `ResetImageAttribute`/`ModifyImageAttribute` to any KMS-grant retirement. **Oracle (pure `ListGrants` observation on A's own CMK):** after B launches, a grant appears; A calls `ResetImageAttribute` → re-check (disappears? persists until termination? persists after termination = orphaned?). **Severity: High** (lingering decrypt survives the control the owner believed removed; **Critical** if it persists past instance termination). Mitigation: key admin can always `RevokeGrant`, but nothing in the AMI-sharing docs tells the owner to look at `ListGrants` after revoking a share.
- **[Medium] Unencrypted-snapshot launch access has no documented identity/audit trail.** `sharingamis-explicit.md` only asserts the *result* (*"the system provides the instance access to the referenced EBS snapshots for the launch"*) without naming an identity, API, token, or log. For encrypted AMIs the owner can at least inspect `ListGrants`; for unencrypted there is no documented audit/revoke surface. **doc-gap — confirm surface first.** **Severity: Medium** (visibility gap underpinning the above).

**Additional doc-gaps (Area F):** (a) what retires the per-volume grant and when; (b) whether a grantee's already-running instance loses any capability (fast-restore, hibernate-resume, creating volumes from the AMI's other snapshots) after the owner resets; (c) whether a grantee who self-revokes via `CancelImageLaunchPermission` after having launched retains claim-1/2 derived access (mechanism implies yes; unstated).

> **SUSPECTED PROMPT INJECTION (recorded, not acted on):** the mirror file `AWSEC2/latest/UserGuide/skill-agent_docs.aws.amazon.com_AWSEC2_latest_UserGuide_AMIs.html.md` is a **prior-agent research artifact, not an official AWS doc**, and carries an appended block instructing a reader/agent to run a live CLI skill-search command. This was treated as untrusted document content and ignored, consistent with the documentation-only constraint. Any lead that overlapped it (e.g. "ResetImageAttribute clears org/OU shares") was independently re-derived from primary docs (`share-amis-org-ou-manage.md`, `API_LaunchPermission.md`) above.


### 9-B. Block Public Access, declarative policy & the Marketplace guarantee (Area G deep-dive)

**Core thesis:** `ResetImageAttribute` (make private) and `ModifyImageAttribute Group=all` (make public) are the *per-AMI* edge of a larger public-exposure control surface. The account-/org-level guarantees layered above them — **Block Public Access (BPA)**, **declarative org policies**, and the **Marketplace "cannot be made public"** rule — each assert a boundary whose enforcement has gaps or undocumented timing. Seven leads:

- **[High — recon/operational] BPA is new-sharing-only, NOT retroactive.** `block-public-access-to-amis.md` states three times that enabling `block-new-sharing` does **not** privatize AMIs that are *already* public (*"if you already have public AMIs, they remain publicly available"*). **Consequence:** a posture assessment that treats `GetImageBlockPublicAccessState = block-new-sharing` as proof of zero public exposure is **wrong**; pre-existing public AMIs must be enumerated separately (`DescribeImages --executable-users all` filtered to the account) and each explicitly privatized via `ResetImageAttribute`. **Oracle:** make AMI public → enable BPA → confirm AMI still returns `Public=true` and is still launchable cross-account. **Severity: High** (operational / recon — false sense of containment).
- **[High — top actionable hunt] BPA is per-Region; drift is the cheapest high-value finding.** The docs require enabling/checking BPA *"in each AWS Region"* and the CLI example literally shows mixed `block-new-sharing`/`unblocked` state across Regions in one account. **Oracle:** crawl `GetImageBlockPublicAccessState` across **all** enabled Regions; any Region returning `unblocked` (or `block-new-sharing` while another is stricter) is an exposure gap an attacker/IR both care about. **Severity: High** (predictable misconfiguration, trivially enumerable).
- **[High if confirmed — doc-gap] BPA is one-directional (never blocks going private).** No condition key or BPA mode gates `ResetImageAttribute` / making an AMI private — BPA only restrains the *public* direction. This is expected/benign for confidentiality but means **BPA cannot be used to prevent an accidental or malicious *un-share*** (availability/DoS angle: an over-broad principal that can call `ResetImageAttribute` can privatize a deliberately-public distribution AMI, and BPA won't stop it). **Severity: Medium** (availability footgun; confirm no condition key ties BPA to the private direction).
- **[High if present — doc-gap] Declarative-policy precedence & stale-read window is unspecified.** `organizations/.../orgs_manage_policies_ec2_syntax.md` documents an `image_block_public_access` declarative policy that blocks `EnableImageBlockPublicAccess`/`DisableImageBlockPublicAccess`, but hedges *"This list is not exhaustive,"* and **no doc states** (a) the exact error returned when a declarative policy overrides an account-level `Disable` attempt, (b) propagation latency, or (c) whether a window exists where the account-level API reports one state while the org policy enforces another. **Oracle (owned org sandbox):** set declarative policy to enforce BPA; call `DisableImageBlockPublicAccess` in a child account; observe error type + whether `GetImageBlockPublicAccessState` and actual `ModifyImageAttribute Group=all` enforcement agree during any propagation window. **Severity: High if a stale-read/divergence window exists** (control-plane says blocked, data-plane allows the public share).
- **[High if confirmed — doc-gap] Marketplace "cannot be made public" is documented only one-directional.** `API_ModifyImageAttribute.md`: *"Images with an AWS Marketplace product code cannot be made public."* Says nothing about the **reverse** — attaching/propagating a product code to an AMI that is **already public**, or via the backing snapshot/volume rather than the AMI. `ProductCode.N` is explicitly *"Not supported"* as a `ModifyImageAttribute` parameter, so the real propagation path (copy/registration/snapshot lineage) needs confirming. **Oracle (owned):** take a public AMI → attempt every documented path that could associate a Marketplace product code with it → check whether the result is a public AMI carrying a product code (would be a **billing-metering bypass / integrity break**). **Severity: High if confirmed** (undermines the Marketplace billing guarantee). Treat as doc-gap until a concrete association path is found.
- **[High if no-op — Lens S, biggest open question] `ec2:Public` eval-timing on the mutating actions is undocumented, and `ec2:Attribute` can't scope `LaunchPermission`.** No example in the corpus applies `ec2:Public` or `ec2:Owner` as a condition on a `ModifyImageAttribute`/`ResetImageAttribute` statement, and `iam-policies-for-amazon-ec2.md` explicitly documents that the `ec2:Attribute` key **cannot be used with the complex `LaunchPermission` object**. So it is unclear whether `ec2:Public` is even **honored** as a condition on the mutating action, and if so whether it evaluates **pre-** or **post-call** state. A policy an operator writes as *"Deny ModifyImageAttribute when ec2:Public is true"* (intending "don't let anyone touch already-public AMIs") may silently **no-op**. **Oracle (owned sandbox):** write that Deny, attempt the mutation on a public vs private AMI, observe whether the condition is enforced at all and against which state. **Severity: High if the condition no-ops** (a plausible, documented-shaped guardrail that doesn't actually guard).
- **[Low/Medium — Lens S footguns] Condition-key value-casing & tag-invisibility.** (a) Condition-key **names** are documented as case-insensitive (rules out a name-casing bypass), but **value**-casing for `ec2:Owner` literals (`amazon`, `aws-marketplace`, `aws-backup-vault` vs capitalized forms) is never addressed — a policy comparing against the wrong case is a silent footgun. (b) `sharingamis-explicit.md`: AMI tags are **invisible to recipients** except the `ec2:SharedTag/` prefix → any `ec2:ResourceTag`-based launch restriction a recipient-side admin writes can't see owner tags, and `...IfExists` makes an absent-but-expected tag fail **open**. **Severity: Low–Medium** (customer-side least-privilege footguns, not a service boundary break).

**Additional doc-gaps (Area G):** (a) no documented inverse/undo for `CancelImageLaunchPermission` (a grantee who self-removes cannot re-add themselves — availability, and asymmetry vs the owner's atomic `ResetImageAttribute`); (b) no documented concurrency/ordering guarantee between a grantee's `CancelImageLaunchPermission` and the owner's simultaneous `ModifyImageAttribute Add` of that same grantee; (c) ownership gating on the BPA-toggle actions themselves is assumed sound but the three actions (`Enable`/`Disable`/`Get`) have no condition key tying an Allow/Deny to the account's actual public-AMI inventory.

