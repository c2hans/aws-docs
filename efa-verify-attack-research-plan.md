# EFA — "Verify the EFA installer using a checksum" (`efa-verify.html`) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-verify.html` (offline twin `docs/AWSEC2/latest/UserGuide/efa-verify.md`, byte-content confirmed identical to online 2026-10-15, **including the malformed checksum rows** — see Area 3). Status: documentation-derived hypotheses only; nothing tested against a live account.

**Position in the EFA cluster.** This is a **page-level CHILD of the EFA hub (`efa-attack-research-plan.md`)** and a deliberate **THIN COMPLEMENT**, not a standalone surface. The hub's **Area 5** ("EFA software supply chain: TOFU single-origin + verification-off-by-default + unpinned deps") already owns the *general* supply-chain story and explicitly lists `efa-verify.md` as one of its doc-evidence pages. The sibling **`efa-start-attack-research-plan.md` Area D** owns the **GPG detached-signature (`.sig` + `.key`) authenticity path** and `--check-signatures`. This plan does **NOT restate** either; it cross-references them and owns only the **net-new, page-local defects of the CHECKSUM alternative itself** — the three things the hub summarizes in a single word ("MD5", "checksums offered") but never develops.

This page is **NULL-dominant on cloud attack surface**: it contains **no AWS API, no IAM action, no condition key, no ARN, no network interface, no identity/token, no server-side fetch, and no service-parsed upload.** It is pure **guest-side verification guidance** (local `md5sum`/`sha256sum` + a static reference table). Accordingly almost every lens is an explicit null (§8). The entire value is **Lens U** (a false documented guarantee), **Lens Y** (weak-crypto / same-channel trust anchor), and **Lens R** (AWS-authored, copy-verbatim guidance that is itself the defect). All leads are **owner = AWS** (AWS-published, uneditable copy-verbatim guidance) → **Tier-2 reportable** where they rise above informational, per the skill's AWS-authored-artifact carve-out.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- This is a **documentation/guidance-integrity** plan, not a live-API plan. The "oracle" for most leads is a **doc/crypto analysis** (comparing the stated guarantee to what the named mechanism can cryptographically provide), optionally corroborated by a single harmless download+hash on a canary host. **No AWS account action is required or appropriate** for Areas 1–3.
- HARD STOP: unchanged from the hub — the moment evidence shows an AWS service-plane identity/credential/ARN, stop and flag for disclosure. (Does not arise on this page.)

## 1. Pentest Objectives
1. **Falsify the publisher-identity guarantee.** Show that the checksum procedure as documented **cannot** "verify the identity of the software publisher" — it is an *integrity-against-accidental-corruption* primitive mis-sold as an *authenticity* control, and when the attacker controls the tarball origin it provides essentially nothing the TLS transport did not already provide.
2. **Break the weak-crypto option.** Show that offering **MD5** as a co-equal, un-deprecated verification choice lets an attacker who can serve a tarball produce a payload whose **MD5 matches the published value**, so the documented "if the checksums match, it is safe to run" conclusion is false under MD5.
3. **Expose the reference-table integrity gap.** Show that the authoritative checksum values themselves have **no integrity control** — demonstrated by the confirmed malformed/ambiguously-rendered rows in the published table (1.46.0/1.45.1/1.45.0/1.44.0 MD5, 1.43.1 SHA256) — and that the version-keyed table is unusable for the installer's own recommended `latest` download.

## 2. Components, Assets, and Design
- **What the page is.** A how-to that tells a customer, *after* downloading `aws-efa-installer-<ver>.tar.gz` from `efa-installer.amazonaws.com`, to run **`md5sum`** or **`sha256sum`** locally and compare the output against a value in a static **per-version table embedded in the doc page**.
- **The guarantee it asserts (verbatim).** *"We recommend that you do this to **verify the identity of the software publisher** and to check that the application has not been altered or corrupted since it was published."* And: *"If the checksums match, then it is safe to run the installation script. If the checksums do not match, do not run the installation script, and contact Support."*
- **Where it sits in the install flow.** `efa-start.md` Step "(Optional) Verify …" offers the **GPG path** (download `aws-efa-installer.key`, `gpg --import`, then `wget …-<ver>.tar.gz.sig && gpg --verify`) and then a **Note**: *"Alternatively, if you prefer to verify the tarball file by using an MD5 or SHA256 checksum instead, see [Verify the EFA installer using a checksum] (efa-verify.md)."* ⇒ **the checksum page is explicitly positioned as a substitute for the signature path.**
- **Trust-channel topology (the crux).** Two artifacts, **one trust root**:
  - the **tarball** → `https://efa-installer.amazonaws.com/…` (AWS-controlled HTTPS/CDN origin);
  - the **reference checksum** → embedded in the **docs.aws.amazon.com** HTML page (AWS-controlled HTTPS origin).
  Both are AWS-controlled and both are protected only by TLS-in-transit. There is **no out-of-band / second-channel** anchor for the checksum (no detached signature *over the checksum list*, no keyserver/WKD fingerprint, no Sigstore/transparency log).
- **No identifiers / no identity / no API.** The only "resource" is a 32-hex (MD5) or 64-hex (SHA256) string the user eyeballs. There is no caller, no credential, no tenant.

```
customer host (already holds the downloaded tarball)
      |  local, offline
      v
  md5sum / sha256sum  --->  hex string
      |  manual visual compare (human eyeball)
      v
  checksum table embedded in docs.aws.amazon.com HTML page   <-- same trust root (AWS HTTPS) as the tarball origin
      |
      v
  decision: "safe to run installation script"  (no automated enforcement; mismatch => "contact Support")
```

## 3. Trust-Boundary Map
This page sits **entirely inside the customer's own host** plus **two AWS-controlled read origins**. There is **no cross-tenant, cross-account, or data↔control boundary** on the page. The only meaningful boundary is the **integrity/authenticity boundary between "software AWS actually published" and "bytes the host is about to run as root."**

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Attacker who can serve/replace the tarball (origin/CDN compromise, MITM of a non-TLS mirror, or a poisoned `latest`) | Customer root shell (installer runs as root — hub Areas, efa-start Step) | A tampered tarball whose checksum the customer "verifies" | A malicious tarball **passes** the documented check (MD5 collision, or because the attacker also controls the only trust root the checksum lives on) → "safe to run" returns true for attacker bytes |
| AWS doc-publishing pipeline | Customer performing the compare | Static per-version table rendered into HTML | A **wrong, ambiguous, or unparseable** authoritative checksum value is published (confirmed: 5 malformed rows) → customer either accepts a bad compare or cannot complete it, with no integrity control over the reference value itself |
| Installer page recommending `latest` | This version-keyed table | `latest` → unknown version number | Customer who followed the recommended `latest` download **cannot select the correct table row** → verification is undefined/skipped (usability defeats the control) |

**Breach oracle in one line:** *the documented procedure returns "safe to run the installation script" for a tarball that is not the one AWS published* — or the procedure cannot be completed because the published reference is itself corrupt/undefined for the recommended download.

## 4. API / Interface Inventory
**None.** No SDK/CLI AWS action, no console route, no internal endpoint, no IAM action/condition key appears on this page. The only "interfaces" are two local coreutils (`md5sum`, `sha256sum`) and two static HTTPS read URLs (`efa-installer.amazonaws.com/<tarball>`, the docs page). There is nothing to put in the AWS API table — recorded here explicitly so a downstream hunter does not go looking for one.

## 5. Recommended Areas of Focus

### Area 1 — [HEADLINE, in-scope / Tier-2] The checksum procedure cannot "verify the identity of the software publisher" (Lens U + Lens Y)
**Background.** The page's own stated purpose is twofold: (a) "verify the **identity of the software publisher**" and (b) "check that the application has not been altered or corrupted." A keyed/unkeyed **hash** can only ever address (b) *and only against accidental corruption or an attacker who does not also control the reference value*. **Publisher identity (authenticity) requires a signature verified against an independently-trusted key** — exactly what the *other* path (`gpg --verify …tar.gz.sig` against `aws-efa-installer.key`) attempts. This page provides no key, no signature, and no second trust channel.
**Security Concern.**
- The published reference checksum lives on **docs.aws.amazon.com**, an AWS-controlled HTTPS origin; the tarball lives on **efa-installer.amazonaws.com**, an AWS-controlled HTTPS origin. **An adversary able to tamper with the tarball (origin/CDN compromise, or a MITM on a path where TLS is stripped/ignored) is in the same or an adjacent position to tamper with (or has already defeated the trust of) the reference value.** Against such an adversary the checksum compare adds **zero** authenticity assurance beyond TLS. It defends only the narrow case of *accidental* in-transit/at-rest corruption — which is (b), not (a).
- The page therefore **mis-sells an integrity primitive as an authenticity control.** A customer could reasonably build a compliance/attestation claim ("we verify the publisher of AWS-provided software") on a step that provides no such property. That false reliance is the AWS-owned defect.
- Framing against the sibling path: `efa-start.md` presents the checksum page as an **"Alternatively … instead"** of GPG signature verification, with **identical** "verify the identity of the software publisher" wording on *both*. The two are **not** security-equivalent — only the signature path even attempts authenticity — yet the doc equates them. (The GPG path has its own single-origin-TOFU weakness: the `.key` and `.sig` also come from `efa-installer.amazonaws.com` with no out-of-band fingerprint — that weakness is **owned by `efa-start` Area D**, cross-ref, not restated here.)
**High-level Test Scenarios.**
- *Claim:* the documented checksum procedure provides **no publisher-identity (authenticity) guarantee**, only accidental-corruption integrity. → *Oracle:* trace the trust chain on the page: (i) there is no signature and no key on this page; (ii) the reference value and the artifact share the single AWS trust root; (iii) a hash is not an authenticity primitive. Confirm the doc nonetheless asserts "verify the identity of the software publisher." *Settles doc-only.* *Severity:* **Low/Informational** as a pure doc-vs-mechanism inconsistency, **but AWS-owned and reportable** because a customer can build a false attestation on it (Lens U carve-out).
**Doc evidence:** efa-verify.md para 1 ("verify the identity of the software publisher"), the embedded table (reference-on-same-origin), efa-start.md L165-169 (GPG path + "Alternatively … checksum instead" Note). **Severity-if-true:** Informational→Low (AWS-authored guidance defect; owner-shared with the hub Area 5 TOFU finding).

### Area 2 — [in-scope / Tier-2] MD5 offered as a co-equal, un-deprecated verification option defeats "if the checksums match, it is safe" (Lens Y + Lens U)
**Background.** The page offers **MD5 and SHA256 as equal choices** — *"Use the **md5sum** utility for the MD5 checksum, or the **sha256sum** utility for the SHA256 checksum"* — with **no deprecation note, no "prefer SHA256," and a full MD5 column in the table.** MD5 has been cryptographically broken for collision resistance since 2004–2008 (practical **chosen-prefix** collisions, e.g. the Flame malware forged-signature class of attack).
**Security Concern.**
- The page's decision rule is **"If the checksums match, then it is safe to run the installation script."** Under **MD5**, "the checksums match" does **not** imply the tarball is the one AWS published: an adversary who can serve a tarball (origin/CDN control, or a `latest`/mirror poisoning path per hub Area 5) can craft a malicious archive whose **MD5 equals the published MD5** while differing in content. The tar format's trailing padding/extension fields and the installer being a shell-extracted archive give ample room for collision-block placement.
- Because MD5 and SHA256 are presented as **interchangeable**, a customer who chooses the MD5 branch (shorter, familiar, "good enough") believes they satisfied the exact same "safe to run" guarantee — but they bought a broken check. The weaker option is a **first-class documented path**, not a legacy footnote.
- This is **net-new depth** over the hub, which notes only the single word "MD5" in Area 5's list. The specific, falsifiable claim here is: *the "safe to run" conclusion is unsound for the MD5 branch as written.*
**High-level Test Scenarios.**
- *Claim:* a tarball tampered to collide with the published **MD5** will be declared "safe to run" by the page's own decision rule, while its **SHA256** would differ. → *Oracle (analysis):* confirm the page gives MD5 equal standing with no deprecation and that its match-rule makes no distinction; MD5 chosen-prefix collisions are public art. A full live PoC (building a real collision against a specific published tarball) is **out of scope for this doc plan** and unnecessary to establish the defect — the documented acceptance of MD5 as a sufficient check is itself the finding. *Severity:* **Medium** (AWS-authored guidance offering a broken integrity check as sufficient to gate root-run software; owner = AWS).
- *Adjacent:* check whether any EFA page ever says "MD5 is provided for legacy compatibility only, prefer SHA256." (As of 2026-10-15, **none does**.)
**Doc evidence:** efa-verify.md ("Use the md5sum utility … or the sha256sum utility"; "If the checksums match, then it is safe to run the installation script"; MD5 column present for all 60+ versions). **Severity-if-true:** Medium.

### Area 3 — [in-scope / Tier-2] The authoritative reference table has no integrity control: confirmed malformed rows + version/`latest` mismatch (Lens U + Lens O)
**Background.** The checksum values are the **anchor** of the whole procedure — the one thing that must be correct. They are maintained as a **hand-/template-rendered static table** in the doc, with **no checksum/signature over the checksum list itself** and no automated validation of row formatting.
**Security Concern — two concrete, confirmed defects:**
- **(a) Malformed/ambiguous published rows (confirmed offline AND online, identical, 2026-10-15).** Five rows render the hex value with **misplaced code-span backticks**, so the value is not cleanly delimited:
  - `EFA 1.46.0` MD5 → ``a88bbd9b71624d7ca401b54bc2fc0c19`` ` (backticks *trailing*, none leading)
  - `EFA 1.45.1` MD5 → ``91c3c87e16bbcaca1513252c38b771bb`` `
  - `EFA 1.45.0` MD5 → ``800aeddfa9d9c5f139a7b8f7c4fec627`` `
  - `EFA 1.44.0` MD5 → ``d024f6bebe080db42745103b84ca7c43`` `
  - `EFA 1.43.1` SHA256 → ``54211eda0c193138ee8ed09b5fb41c41fc76fe0a77935fa4ec8d989466342740`` `

  This proves the reference table is produced with **no formatting/validation gate**. The security concern is twofold: (i) a user comparing against an ambiguously-rendered value may mis-read it (a stray backtick could be mistaken for part of the value, or copy-paste could capture/drop a character) and either reject a good tarball or, worse, "massage" the compare until it passes; (ii) more structurally, it demonstrates that the **values themselves are mutable, hand-maintained, and unverified** — if a wrong value (benign typo or malicious edit of the doc) were published, there is **no integrity mechanism to detect it**, and the customer has no second source to cross-check against (Area 1).
- **(b) Version-keyed table vs `latest`-recommended download.** The table is indexed **by exact version** (`EFA 1.50.0`, `1.49.0`, …). But the installer page **recommends `latest`**: *"To download the latest stable version … You can also get the latest version by replacing the version number with `latest`."* A customer who downloads via `latest` **does not know which version they received**, so they **cannot select the correct table row** → the verification step is undefined and will, in practice, be skipped. The AWS-recommended convenience path **silently defeats** the AWS-recommended verification path.
**High-level Test Scenarios.**
- *Claim:* the published reference table has no integrity control, evidenced by malformed rows present in the live doc. → *Oracle:* already confirmed — the five rows above are byte-identical in the offline mirror and in a live fetch of `efa-verify.html`/`.md` (2026-10-15). *Severity:* **Low** (doc-integrity / detective-control reliability; AWS-owned).
- *Claim:* following the installer's `latest` recommendation makes the checksum table unusable (no version to key on). → *Oracle:* confirm `efa-start.md` L157-159 recommends `latest`, and `efa-verify.md` keys only by version; there is no "how to find the version of a `latest` download" guidance on either page. *Severity:* **Low** (usability-defeats-security; AWS-owned, owner-shared with hub Area 5 floating-version lead).
**Doc evidence:** efa-verify.md L51-54, L57 (malformed rows); efa-verify.md table header "The following table lists the checksums for recent versions"; efa-start.md L157-159 (`latest`). **Severity-if-true:** Low.

### Area 4 — [thin POINTER, deferred] Everything else about the EFA supply chain
Not developed here — cross-reference only, do not re-run:
- **Single-origin TOFU, verification-optional-by-default, `latest` floating version, unpinned root-run deps, container worst-case** → **EFA hub Area 5** (`efa-attack-research-plan.md`), which already cites this page.
- **GPG detached-signature path (`.key` + `.sig` + `gpg --verify`), `--check-signatures` per-package verification (added 1.48.0), the uncleared "key is not certified" WARNING in the documented expected output** → **`efa-start-attack-research-plan.md` Area D** (and the NCCL/NIXL siblings for their variants).
- **The installer running as root / the tarball being extracted and executed** → hub + efa-start; this page stops at "safe to run," it does not run anything.
- **Container-image bake of an unverified tarball** → `efa-installer-containers-attack-research-plan.md` Area A1.

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Tampered tarball declared "safe to run" via checksum compare | Checksum verification ritual | "If the checksums match, it is safe to run" — **MD5 branch is collision-breakable; reference shares the single AWS trust root** (Areas 1, 2) |
| Customer builds a "we verify the publisher" attestation on this step | Doc guarantee wording | "verify the identity of the software publisher" — **a hash provides no authenticity; only the GPG path attempts it** (Area 1) |
| Wrong/ambiguous reference value published, undetectable | Static checksum table | **No integrity control over the table; 5 malformed rows confirmed live** (Area 3a) |
| Verification silently skipped on the recommended path | `latest` download + version-keyed table | **No way to map a `latest` download to a table row** (Area 3b) |

## 7. Out-of-Scope Risk Categories
- **Live MD5-collision construction against a specific published EFA tarball** — the documented *acceptance* of MD5 as sufficient is the finding; building a real collision is unnecessary and out of scope for a documentation-derived plan.
- **Compromising `efa-installer.amazonaws.com` or docs.aws.amazon.com, or MITM of AWS TLS** — those are the *preconditions* the leads reason about, not actions to perform; attacking AWS infrastructure is a service-plane HARD STOP.
- **The installer executing as root, and all downstream dependency supply chain** — owned by hub Area 5 and the efa-start siblings (deferred, Area 4).
- **The GPG signature path's own TOFU weakness** — owned by `efa-start` Area D.
- **Customer-authored verification choices** (choosing to skip, choosing MD5) are footguns *only to the extent the customer originates them*; here they are **in scope** precisely because the **weak options and the false guarantee are AWS-published, copy-verbatim guidance** (skill carve-out).

## 8. Null hypotheses / doc gaps
Every lens below is **N/A for this page**, with the page(s) checked named (per skill discipline). This page is pure guest-side verification guidance with no cloud attack surface:
- **Lens A (cross-tenant/IDOR)** — N/A: no resource, no identifier, no tenant, no API on efa-verify.md.
- **Lens B / C (PassRole / credential vending)** — N/A: no role ARN, no STS, no credential anywhere on the page.
- **Lens D / V (data↔control / network segmentation)** — N/A: no ENI, subnet, SG, endpoint, or host-reachability content (that is the hub's Areas 2-4 and create-efa).
- **Lens E (RBAC/privesc)** — N/A: no IAM principal/role model on the page.
- **Lens F (translation/injection)** — N/A: `md5sum`/`sha256sum` are local hash utilities; no service-side parser transforms customer input here.
- **Lens G (SSRF)** — N/A: there is **no field the service dereferences**; the only fetches are the *customer's own* `curl`/`wget` of a static AWS URL (on the installer page, not this one). Checked: efa-verify.md full text — no server-side fetch role exists.
- **Lens H (KMS/encryption-context)** — N/A: no KMS, no key, no encryption context.
- **Lens I / S (tagging / condition-key semantics)** — N/A: no IAM policy, tag, or condition key on the page.
- **Lens J (OAuth/3P)** — N/A: no linking, no `state`, no 3P.
- **Lens K (prompt injection)** — N/A: no LLM/agent in this path.
- **Lens L (DoS/exhaustion)** — N/A: hashing a local file the customer already downloaded; no shared fleet, no service-side parser. (Zip-bomb/parse-exhaustion of the tarball by the *installer* is a hub/efa-start concern, not this page.)
- **Lens M (shared-identifier interception)** — N/A: no session id, token, or presigned URL.
- **Lens N (namespace migration)** — N/A: no ARN/namespace.
- **Lens P (proofing/registration)** — N/A: no gate, code, or uniqueness constraint. (The "contact Support" on mismatch is advisory, not a verifiable gate.)
- **Lens Q (upload validation)** — N/A on this page: the tarball is parsed by the *customer's own* installer, not uploaded to or rendered by an AWS service; the service-side-parse angle is deferred to hub/efa-installer-containers.
- **Lens T (cross-service secret reachability)** — N/A: no secret generated/persisted.
- **Lens O (audit-log evasion)** — partial/weak: the checksum ritual is itself a *detective* control, and Areas 2-3 are about that control being defeatable/unreliable; there is no AWS audit log on this guest-side step. Not a standalone finding.
- **Lenses W / AA / BB / CC / DD / EE / FF** — N/A: no attestation, share/revoke, multi-parser request path, upstream-asserted identity, cache, predictable-name resolution, or JWT/token on the page.
- **FIRING lenses:** **U** (Area 1 false publisher-identity guarantee; Area 3 doc-vs-mechanism + usability-defeats-security), **Y** (Areas 1-2 same-channel trust anchor + broken MD5), **R** (all three areas — the defect *is* the AWS-authored, copy-verbatim guidance).

**Carried doc-gaps for a downstream reader:**
- No EFA page states a preference order (SHA256 over MD5) or marks MD5 as legacy — confirm this remains true before down-rating Area 2.
- No page explains how to determine the version of a `latest`-downloaded tarball so it can be matched to the table — confirm before down-rating Area 3b.
- The signed `.sig`/`.key` path's trust anchor (same-origin TOFU) is the stronger-but-still-weak alternative; its depth lives in `efa-start` Area D — a hunter weighing "which verification path is least bad" should read both.

**Cross-refs:** [[efa-attack-research-plan]] (hub Area 5), [[efa-start-attack-research-plan]] (Area D GPG path), [[efa-installer-containers-attack-research-plan]] (A1 container bake), [[reference-aws-iam-service-auth-ref-url]] (N/A here — no IAM surface, recorded for completeness).
