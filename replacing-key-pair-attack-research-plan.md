# Replacing a Key Pair (Add / Replace / Remove a public key on a Linux instance) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/replacing-key-pair.html` ("Add or replace a public key on your Linux instance"), verified against the online `.md` twin 2026-10-15 (offline mirror does **not** carry this page under that name; siblings and `list_ec2.md` were read offline). Supporting pages (subagent-verified, offline==online, zero drift): `building-shared-amis.md`, `sharing-amis.md`, `usingsharedamis-confirm.html`, `sharingamis-explicit.html`, `share-amis-with-organizations-and-OUs.html`, `sharingamis-intro.html`, `docs/linux/{al2,al2023,al2027}/ug/cloud-init.md`. Status: **documentation-derived hypotheses only; nothing tested against a live account.**

This is a **page-level deep-dive CHILD** of the EC2 key-pairs cluster. It is the **guest-OS runbook counterpart** to the control-plane key-pair plans and specifically the authoritative complement to `delete-key-pair-attack-research-plan.md` **Lead D1 (delete-as-false-revocation)**: that lead observed "there is NO EC2 action that revokes a key pair from running instances"; **this page documents the manual, in-guest procedure that is the only revocation mechanism that exists**, and this plan analyzes that mechanism's enforcement, completeness, and cross-account reach. It COMPLEMENTS and cross-references the siblings — it does not restate them:
- `ec2-key-pairs-attack-research-plan.md` (HUB), `create-key-pairs-attack-research-plan.md`, `delete-key-pair-attack-research-plan.md`, `describe-keys-attack-research-plan.md`.

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- **This page has NO EC2 control-plane API of its own.** Its entire mechanism is: SSH to the instance as the default user and text-edit `~/.ssh/authorized_keys`. The security value is therefore almost entirely in **Lens U (guarantee-vs-enforcement), Lens AA (revocation completeness), Lens O (control-plane invisibility), Lens E (no-IAM-governance), and the cross-account AMI path (EE/A/AA).** Classic cross-tenant IDOR, SSRF, injection, KMS, and token lenses are **genuine nulls** here (pages named in §8).
- **Scope discipline:** the actual read/write of `authorized_keys` is a **guest-OS / customer-responsibility** operation and is OUT OF SCOPE as an AWS service-plane bug (§7). The IN-SCOPE, AWS-owned residue is: (a) a documentation enforcement **asymmetry** AWS could close, and (b) the fact that AWS's own control-plane presents key-pair *revocation* as governable while the real revocation happens somewhere no AWS control or audit can see. Report those as AWS-owned doc/assurance gaps (Tier-2-adjacent / Informational), not as cross-tenant exploits.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected to fire on this page.)

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. **Demonstrate revocation is incomplete.** After the owner "revokes" a departed user per the page's reason (b) — delete the EC2 key pair and/or scrub the default user's `authorized_keys` — show that SSH access *still* succeeds via a path the procedure did not cover (another OS user's `authorized_keys`, an alternate login the page's own Warning admits, a pre-existing AMI, or an attacker-planted key).
2. **Demonstrate control-plane invisibility.** Show that an `authorized_keys` add/remove produces **no** CloudTrail event, no change in `DescribeKeyPairs`/`DescribeInstances.KeyName`, and no IMDS reflection of the planted key — i.e. a defender auditing SSH access from the EC2 control plane is blind to the true authorizer set.
3. **Demonstrate cross-account persistence via a shared AMI.** Show that a publisher who creates an AMI without scrubbing `authorized_keys` retains an SSH backdoor into every consumer instance launched from the shared/public/Org-shared AMI — invisible to the consumer's control plane. (Treated as a documented customer-responsibility risk; the AWS-owned finding is the audit-backstop asymmetry, Area 4.)
4. **Characterize the add-key persistence primitive.** Show that an attacker with one-time default-user shell can plant a durable key that survives `DeleteKeyPair`, key rotation, and the owner's password changes.

---

## 2. Components, Assets, and Design

**Customer-facing interface on this page:** none that is an AWS API. The operations are: `ssh` to the instance (port 22) as the default user (`ec2-user` etc.) and edit a text file. The only AWS surfaces *referenced* are on sibling pages — CreateKeyPair / ImportKeyPair (`create-key-pairs`), retrieve public key (`describe-keys`), connect (`connect-to-linux-instance`).

**The actual access-control artifact:** `~/.ssh/authorized_keys` for the **default system account only** (the page explicitly scopes to "the default user, such as `ec2-user`"; other OS users have their own `authorized_keys` the EC2 key pair never touches — "For information about adding users to your instance, see the documentation for the operating system").

**Three operations the page defines:**
- **ADD** — paste a new public key *underneath* the existing one (append; both keys now authorize).
- **REPLACE** — add new, test, then **(Optional)** delete the original. The delete is explicitly optional and manual.
- **REMOVE ALL** — delete all entries (page Warning: you are then locked out unless an alternate login exists).

**Key lifecycle facts (verified):**
- Launch-time injection is a **first-boot, append** action: "when your instance boots **for the first time**, the public key material is placed … within `~/.ssh/authorized_keys`." It does not clear pre-existing entries (an AMI is a disk snapshot; any baked-in entry survives verbatim).
- **AMI inheritance (Important box, verbatim):** "If you create a Linux AMI from an instance, the public key material is copied from the instance to the AMI. If you launch an instance from the AMI, the new instance includes the public key from the original instance. To prevent someone who has the private key from connecting to the new instance, you can remove the public key from the original instance *before* creating the AMI."
- **No revocation API exists.** `list_ec2.md` (`docs/service-authorization/latest/reference/`) carries exactly four key-pair actions — `CreateKeyPair`, `ImportKeyPair`, `DeleteKeyPair`, `DescribeKeyPairs` — and condition keys `ec2:KeyPairName`, `ec2:KeyPairType` only. **`grep RevokeKeyPair = 0`.** There is no EC2 action that touches `authorized_keys`.

**ASCII — the decoupling that is the whole point of this page:**
```
EC2 CONTROL PLANE                         |   GUEST OS (the real ACL)
  key-pair resource (name/id/fingerprint) |   ~/.ssh/authorized_keys  (default user)
  CreateKeyPair / ImportKeyPair ----------+--> [first boot only, APPEND] ---> entry(s)
  DeleteKeyPair  --------- removes EC2 object only; DOES NOT touch the file ----X
  DescribeKeyPairs / DescribeInstances.KeyName = immutable launch record, NOT the file
  (no API reads or writes authorized_keys)  |   + other OS users' authorized_keys (invisible)
                                            |   + attacker-planted keys (invisible)
AMI (disk snapshot) --- bakes authorized_keys verbatim --> shared/public AMI --> consumer acct instance
```
The vertical bar is the trust boundary: **everything to the right is where access is actually granted, and no AWS control-plane action, condition key, or CloudTrail event crosses it.**

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| EC2 control plane (DeleteKeyPair / IAM / CloudTrail) | guest `authorized_keys` (real ACL) | — none; they are decoupled | Any SSH that still succeeds after the EC2 key pair is deleted, or any `authorized_keys` entry no EC2 API reports, proves the control plane does not govern or observe access. |
| Default-user key-pair scope | other OS users' `authorized_keys` | page scopes to default user only | SSH as a non-default OS user whose key the EC2 key-pair procedure never touched = revocation scope gap. |
| Anyone with one-time default-user shell | durable instance access | ADD a public key to `authorized_keys` | Access that survives `DeleteKeyPair` + launch-key rotation + owner password change = persistence token outside the control plane. |
| **AMI publisher account** | **AMI consumer account instance** | baked-in `authorized_keys` entry in a shared/public/Org-shared AMI | Consumer instance's `authorized_keys` contains a publisher-controlled key; publisher SSHes in with the matching private key = **cross-account backdoor**, invisible to consumer control plane. |
| any customer surface | AWS's own service plane | — | Not reachable from this page (guest-OS file edits + customer SSH only). Hard stop if ever observed. |

---

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| *(none on this page)* | — | — | — | — | guest-OS file edit over SSH | SSH to instance only | **anyone with default-user shell / root / sudo** | **No EC2 API, no IAM action, no condition key governs this operation** — the central fact. |
| `CreateKeyPair` / `ImportKeyPair` | SDK | Existing | yes | External | create/import the key referenced | yes | `ec2:CreateKeyPair`/`ImportKeyPair` (scopable by `ec2:KeyPairName`; Import lacks `KeyPairType`) | Analyzed in `create-key-pairs` sibling — crypto-floor / parser leads live there. |
| `DescribeKeyPairs` / retrieve public key | SDK | Existing | no | External | retrieve public key material to paste | yes | `ec2:DescribeKeyPairs` (**unscopable**, `ec2:Region` only) | Analyzed in `describe-keys` sibling. `KeyName` is an immutable launch record (sibling Area 4). |
| `DeleteKeyPair` | SDK | Existing | yes | External | delete EC2 key-pair object | yes | `ec2:DeleteKeyPair` (scopable by name; `KeyPairId` bypass) | Analyzed in `delete-key-pair` sibling. **Does not revoke running-instance access** (D1 — this plan is its guest-side complement). |
| `ModifyImageAttribute` (launchPermission) | SDK | Existing | yes | External | share AMI (user / Org / OU / public) carrying baked `authorized_keys` | yes | `ec2:ModifyImageAttribute` | The sharing mechanism behind the cross-account backdoor (Area 4). Shares launch rights only; exposes no filesystem content. |

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — Revocation incompleteness: the documented "revoke" procedure is non-atomic, partial, and bypassable (Lens AA + Lens U) — HEADLINE
**Background.** The page's reason (b) is a security guarantee: "If someone has a copy of the private key (`.pem` file) and you want to prevent them from connecting to your instance … you can delete the public key on the instance and replace it with a new one." This, plus `DeleteKeyPair`, is AWS's documented answer to "how do I revoke a key pair."

**Security Concern.** The mechanism is a **manual, non-atomic, guest-OS file edit** whose completeness the page's own text repeatedly undercuts:
- **Scope gap:** the procedure touches only the **default user's** `authorized_keys`. Any additional OS user's key is untouched — the page explicitly defers other-user management to the OS docs.
- **Alternate-login gap:** the Warning admits "unless you've configured an alternate way to log in" — password auth, EC2 Instance Connect, SSM Session Manager, another key, a cron/rsyslog backdoor all survive key removal (cf. `usingsharedamis-confirm`'s six-item manual checklist).
- **Non-atomic REPLACE:** add-new-then-**optionally**-delete-old leaves a window (or a permanent state) where both keys authorize; the delete step is marked "(Optional)."
- **Control-plane residue:** `DeleteKeyPair` removes only the EC2 object and never the file (sibling D1); the EC2 object and the file revoke independently and neither covers the other.

**High-level Test Scenarios (falsifiable claims).**
- *Claim:* After deleting the EC2 key pair AND scrubbing the default user's `authorized_keys`, SSH still succeeds as a different OS user whose key was never in the EC2 key-pair model. *Oracle:* authenticated SSH session as that user. *Severity:* revocation bypass (High to the instance owner; intra-account).
- *Claim:* The departed-user `.pem` still authorizes between the "add new" and "delete old" steps, or indefinitely because the delete is optional. *Oracle:* SSH with the old key after a "replace." *Severity:* Medium–High.
- *Claim:* An alternate login (password/EIC/SSM/second key) survives "remove all keys." *Oracle:* login via the alternate path post-removal. *Severity:* Medium (documented, but defeats the stated revocation intent).

**Doc evidence:** `replacing-key-pair.html` reason (b), REPLACE step 7 "(Optional)", Warning box; `delete-key-pair` D1. **Severity-if-true:** Low–High (customer-mechanism, but AWS frames it as THE revocation procedure → the guarantee-vs-enforcement gap is AWS-owned at the doc layer). **Stop condition:** once one surviving-access path is shown, the incompleteness is established; do not enumerate every OS user.

### Area 2 — `authorized_keys` is invisible to and ungoverned by the EC2 control plane (Lens O + Lens E + Lens M) — HEADLINE
**Background.** No EC2 action reads or writes `authorized_keys`; access to perform the edit is "anyone with default-user shell / root / sudo," decided entirely by the guest OS.

**Security Concern.** Two consequences AWS's control plane cannot address:
- **Audit blindness (Lens O):** adding or removing a key produces **no CloudTrail event, no EC2 management event, and no change in `DescribeKeyPairs` or `DescribeInstances.KeyName`** (that name is the immutable launch record — `describe-keys` Area 4). IMDS `public-keys/0/openssh-key` reflects only the launch key, never a planted one. A SOC that models "who can SSH to this box" from EC2 metadata/CloudTrail is blind to the true authorizer set.
- **Persistence primitive (Lens M/E):** the "ADD a public key" operation is a durable persistence mechanism. An attacker with one-time default-user shell (stolen `.pem`, transient RCE, a leaked launch key) plants their own key; it survives `DeleteKeyPair`, launch-key rotation, and owner password changes, because the owner only ever scrubs the key(s) they know about.

**High-level Test Scenarios.**
- *Claim:* An `authorized_keys` add/remove yields zero CloudTrail / zero control-plane signal. *Oracle:* edit the file; diff CloudTrail + `DescribeKeyPairs`/`DescribeInstances.KeyName` + IMDS — all unchanged. *Severity:* audit-evasion enabler (Low–Informational on its own; raises other findings).
- *Claim:* A planted key survives `DeleteKeyPair` and launch-key rotation. *Oracle:* delete/rotate the EC2 key pair; SSH with the planted key still works. *Severity:* persistence (High to owner; intra-account).

**Doc evidence:** `replacing-key-pair.html` (no API named for the edit); `list_ec2.md` (4 key-pair actions, no revoke, no `authorized_keys` surface); `describe-keys` Area 4. **Severity-if-true:** Low–Informational as a standalone gap; High as the persistence/audit-evasion enabler in a chain. **Stop condition:** confirm one add and one delete produce no control-plane signal.

### Area 3 — Cross-account SSH backdoor via a shared AMI carrying baked `authorized_keys` (Lens EE + Lens A/AA, cross-account) — HIGHEST SEVERITY (but see scope note)
**Background (verbatim).** Important box: "the public key material is copied from the instance to the AMI … the new instance includes the public key from the original instance." Launch-time injection is **first-boot append**, so any entry already on the AMI's disk is preserved. AMIs are shared cross-account via `ModifyImageAttribute` launchPermission (user, Org/OU, or `Group=all` public).

**Security Concern.** A publisher who images an instance without scrubbing `authorized_keys` bakes their own key into **every** instance any consumer later launches from the AMI, across accounts/Orgs/public. The consumer has **no control-plane way to detect it**: subagent-confirmed that `DescribeImages`/`DescribeImageAttribute` expose no filesystem content, and `usingsharedamis-confirm.html` tells the consumer to detect it only by a **manual, post-boot** `sudo find / -name authorized_keys -exec cat {} \;`. This is a silent, durable, cross-account initial-access primitive that bypasses `DeleteKeyPair`/key-pair IAM entirely (those govern EC2's key-pair objects, not file content).

**High-level Test Scenarios.**
- *Primary oracle:* launch from a shared/public/Org-shared AMI; run the AWS-recommended `find … authorized_keys … cat`; if a key appears that is not the launch key, attempt SSH with a candidate publisher key. Success = cross-account backdoor. *Severity:* High–Critical to the consumer.
- *Rebundle-persistence control:* scrub the key, re-image, relaunch, re-check — confirms the key does not spontaneously reappear (isolates the issue to initial AMI content; rules out cloud-init re-injection, see Area 5).
- *Negative control:* confirm no `DescribeImages`/`DescribeImageAttribute` field surfaces `authorized_keys` → establishes pre-launch undetectability.

**Doc evidence:** `replacing-key-pair.html` Important box; `building-shared-amis.md`; `usingsharedamis-confirm.html`; `sharingamis-{explicit,intro}.html`; `share-amis-with-organizations-and-OUs.html`. **Severity-if-true:** High–Critical to a trusting consumer. **SCOPE NOTE / Stop condition:** AWS documents this on BOTH sides (publisher: scrub before sharing; consumer: check after launch), so the raw backdoor is a **documented customer-responsibility / guest-OS risk, NOT an unpatched AWS service-plane vulnerability** → see §7. The genuinely AWS-owned, reportable residue is Area 4. Stop at the negative-control confirmation; do not weaponize against a real third-party AMI.

### Area 4 — AWS audit-backstop asymmetry: host keys get an automated safety net, user `authorized_keys` does not (Lens U, AWS-owned) — THE REPORTABLE RESIDUE
**Background (verbatim).** `building-shared-amis.md` states, for leftover SSH **host keys**: "If you forget to remove the existing SSH host key pairs from your public AMI, our routine auditing process notifies you and all customers running instances of your AMI of the potential security risk. After a short grace period, we mark the AMI private."

**Security Concern.** AWS documents an **automated auditing + grace-period + auto-private backstop for one leftover-credential class (host keys**, mainly a MITM risk) but documents **no equivalent for leftover user `authorized_keys`** — the arguably more severe class, because it is a direct inbound backdoor (Area 3). The publisher-side guidance for `authorized_keys` is purely manual (`ec2-bundle-vol --exclude`, "clear out or delete the `authorized_keys` file"), with the page's own disclaimer that "No list of security guidelines can be exhaustive."

**High-level Test Scenarios.**
- *Claim:* No AWS routine-audit / auto-private process is documented for public AMIs that ship a populated user `authorized_keys`, despite one existing for host keys. *Oracle:* documentation review (settled; this is a doc-layer finding). If AWS confirms the asymmetry reflects actual auditing scope (not just docs), it is a real detection-coverage gap, not only a doc gap.
- *Adjacent:* does any publish-time check (`ModifyImageAttribute Group=all`) warn or scan for leftover credentials? Docs show none — public-sharing pages punt entirely to the manual guideline page.

**Doc evidence:** `building-shared-amis.md` ("Remove SSH host key pairs" vs "Remove sensitive data" sections). **Severity-if-true:** Low–Informational, **AWS-owned** (documentation/assurance asymmetry; worth filing to `aws-security` precisely because a customer could reasonably assume the host-key auditing net also covers user keys). **Stop condition:** finding is documentation-settled; file and move on.

### Area 5 — cloud-init re-injection cadence (Lens U doc-gap, de-risking lead)
**Background.** `replacing-key-pair.html` confirms the AWS-specific half: key injection is **first-boot** and **append** ("boots for the first time … an entry within"). The underlying cloud-init SSH-module mechanics — `ssh_deletekeys`, per-boot vs per-instance-ID semaphore, `cloud-init clean` — are **not documented** on the AL2/AL2023/AL2027 pages (they only list "Adds a user's public SSH keys to `.ssh/authorized_keys`" with no cadence).

**Security Concern.** This decides two things for the leads above: (a) whether a consumer's manual removal of a baked-in key **survives reboot** (expected yes — first-boot action doesn't re-run on the same instance-ID), and (b) whether the EC2 launch-specified key would **reappear** independently (expected: only on a fresh instance-ID / rebundle). A wrong assumption here produces a false lead for Area 3's rebundle control.

**High-level Test Scenarios.**
- *Claim:* Deleting a key from `authorized_keys` and rebooting (same instance-ID) does not restore it. *Oracle:* delete, reboot, re-check file. *Severity:* Informational (confirms Area 1/3 mechanics).
- *Claim:* The AL cloud-init pages do not document `ssh_deletekeys`/`cloud-init clean` semantics. *Oracle:* doc review (settled; doc-gap). *Severity:* Informational.

**Doc evidence:** `replacing-key-pair.html`; `docs/linux/{al2,al2023,al2027}/ug/cloud-init.md`, `amazon-linux-cloud-init.md`. **Severity-if-true:** Informational. **Stop condition:** one reboot test settles the cadence.

### Area 6 — Stale key-pair reference breaks ASG / EC2 Fleet / launch-template launches (Lens L, thin pointer)
**Background.** Step 6: "If you're using Auto Scaling, EC2 fleet, or a launch template to launch your instances, check whether the key pair that you're replacing is specified in your launch template or launch configuration. Otherwise, instance launches will fail."

**Security Concern.** Replacing/deleting a key pair while a launch template / ASG / fleet still references it arms a **time-delayed availability break** decoupled (in time and CloudTrail) from the key change — the same latent-DoS shape as `delete-key-pair` **Lead D4**; and the inverse (re-import a freed name) is `delete-key-pair` **D3** (delete→reimport land-grab) + hub Area 4.

**High-level Test Scenarios.** *Claim:* a referencing ASG's next scale-out fails after a key replace with no synchronous warning. *Oracle:* replace key, trigger scale-out, observe launch failure. **DEFER** mechanics to `delete-key-pair` D3/D4 and the hub; this page only re-raises the pointer. **Severity-if-true:** latent intra-account DoS (D4). **Stop condition:** cross-reference satisfied; do not re-derive.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Revocation bypass via second OS user / alternate login / optional-delete window | guest `authorized_keys` | "delete the public key … replace it with a new one" (reason b) + Warning |
| Persistence key survives `DeleteKeyPair` + rotation | guest `authorized_keys` ↔ EC2 key-pair object | DeleteKeyPair (sibling D1) — claims to let you deny access |
| Control-plane audit blindness to key add/remove | CloudTrail / DescribeKeyPairs / IMDS | implicit "key pair = how access is controlled" framing across the key-pairs chapter |
| Cross-account backdoor via shared-AMI baked key | AMI launchPermission + `authorized_keys` | Important box ("remove … *before* creating the AMI") + `building-shared-amis` scrub guidance + `usingsharedamis-confirm` consumer check |
| Audit-backstop asymmetry (host keys vs user keys) | AWS AMI auditing process | `building-shared-amis` host-key auto-private backstop (no user-key equivalent) |
| Stale key reference → ASG/fleet/LT launch failure | launch template / ASG / fleet | Step 6 "check … Otherwise, instance launches will fail" |

---

## 7. Out-of-Scope Risk Categories (stated as confidently as in-scope)
- **The guest-OS `authorized_keys` edit itself** — reading/writing the file over SSH is a customer-managed, guest-OS operation with no AWS API; AWS cannot govern or audit it and does not claim to. Not an AWS service-plane bug.
- **The raw shared-AMI backdoor (Area 3)** — AWS documents the risk on BOTH the publisher side (`building-shared-amis`: scrub `authorized_keys` before bundling) and the consumer side (`usingsharedamis-confirm`: manually find/inspect `authorized_keys` after launch, keep a second session open). It is **documented, intended customer due-diligence**, not an unpatched AWS vulnerability. In scope only as the **doc/assurance asymmetry of Area 4**.
- **Customer SSH / sshd config, password auth, alternate login channels** — customer responsibility; this plan only notes they defeat the revocation *intent* (Area 1), it does not treat them as AWS bugs.
- **IMDS on managed hosts, user-data execution, EC2 Instance Connect / SSM internals** — owned by other plans (`ec2-security-iam` N-leads, `infrastructure-security`); only referenced here as alternate-login survivors.
- **Cross-account IDOR on the key-pair *object*** — GENUINE NULL: key pairs are not RAM-shareable, have no `launchPermission`, and their ARN is account-scoped (`describe-keys` null). The cross-account vector on this topic is the AMI path (Area 3), not the key-pair resource.
- **Single-tenant self-DoS** (locking yourself out via "remove all keys") — the Warning documents it; customer footgun, out of scope.

---

## 8. Null hypotheses / doc gaps (lenses that did not fire, pages checked)
- **Lens G (SSRF) — N/A.** Read the entire page: no field the service dereferences server-side. "Create a key pair" and "retrieve the public key" are console/client/CLI-side (siblings); pasting a public key into `authorized_keys` is a manual guest-OS edit. No `*Url`/`*Uri`/webhook/fetch field.
- **Lens Q (upload) — N/A on this page.** No file uploaded to an AWS service; pasting key text is guest-side. The public-key **parser** question (malformed key material) belongs to `ImportKeyPair` → `create-key-pairs` sibling Area 2, not here.
- **Lens F (translation/injection) — N/A.** No translation layer or wire-protocol parser on this page.
- **Lens H (KMS/encryption-context) — N/A.** No encryption context here; the CFN-KeyPair private-key → SSM `/ec2/keypair/{id}` SecureString/KMS reachability (Lens T) is owned by the **hub §9** and `create-key-pairs` Area 3.
- **Lens B/C (PassRole / credential vending) — N/A.** No role ARN, no STS, no session policy on this page.
- **Lens S (condition-key semantics) — N/A on-page / defer.** No policy JSON printed here. The salient fact — that **no IAM action or condition key governs the `authorized_keys` edit** — is captured under Lens E/U (Area 2); scoping of `Delete`/`Import`/`Describe` is owned by siblings.
- **Lens D/V (data→control-plane / network segmentation) — N/A on this page.** The page's network interaction is customer SSH (port 22) to the customer's own instance; no control-ENI/storage-ENI reach is implied.
- **Lens I / J / K / W / Y / BB / CC / DD / FF — N/A.** No tagging, OAuth/3P link, LLM/agent, attestation gate, transport/TLS claim, multi-parser request path, upstream-asserted identity, cache layer, or JWT/token on this guest-OS runbook page.
- **Lens A classic cross-tenant IDOR — GENUINE NULL** (key-pair object not cross-account reachable, as above). Cross-account reach exists only via the AMI path (Area 3, lenses EE/AA).
- **Doc gaps to confirm before investing:** (1) cloud-init `ssh_deletekeys`/`cloud-init clean`/per-boot-vs-per-instance semantics undocumented on AL pages (Area 5); (2) whether AWS's routine AMI auditing actually scans for populated user `authorized_keys` or only host keys (Area 4 — the asymmetry may be doc-only or may reflect real coverage); (3) whether any publish-time (`ModifyImageAttribute Group=all`) check warns on leftover credentials (docs show none).

---
**Cross-references:** this plan is the guest-side complement of `delete-key-pair` **D1** (and pointers to D3/D4); it defers all control-plane key-pair IAM to `delete-key-pair`, `create-key-pairs`, `describe-keys`, and the `ec2-key-pairs` HUB. IAM reference: `list_ec2.md` at `docs/service-authorization/latest/reference/` (use slug `list_ec2`, not `list_amazonec2`).
