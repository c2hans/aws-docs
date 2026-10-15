# Prerequisites for BYOIP (`prepare-for-byoip.html`) — Attack / Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/prepare-for-byoip.html` (offline twin
`docs/AWSEC2/latest/UserGuide/prepare-for-byoip.md`, 261 lines). Supporting: `byoip-onboard.md` (provision phase),
`ec2-byoip.md`, `byoip-working-with.md`, API refs `API_ProvisionByoipCidr.md` / `API_CidrAuthorizationContext.md`,
and the IAM ground truth `service-authorization/latest/reference/list_ec2.md`.
**Status: documentation-derived hypotheses only; nothing tested against a live account or any RIR.**
Online `.md` fetched and compared sentence-for-sentence to the offline mirror on **2026-10-15 — no material drift**
(ASNs 16509/14618/8987/214101, openssl commands, /24-/48-/60 prefix sizes, 24-hour ROA window, cert-removal
advisory all byte-identical).

> **Position in the plan family.** This is a **page-level deep-dive child of the existing
> `ec2-byoip-attack-research-plan.md`** (itself a child of the `ec2-networking` hub). The parent OWNS the whole
> BYOIP feature + the crypto ownership-proofing chain at *summary* level (its Leads 1–10). **This plan develops the
> granular PREPARATION-PHASE artifact surface** — the three steps this page uniquely documents (private-key/X.509
> cert creation, RDAP upload, ROA authorization) — and cross-references the parent for everything else. It does
> NOT restate the parent's IAM-unscopability table (parent §3), the signed-authorization-message/replay analysis
> (parent Leads 2–3, which live in `byoip-onboard.md`, not here), the within-pool `AllocateAddress` squatting
> (parent Lead 7), the 5-range quota DoS (parent Lead 8), or BYOASN (parent Leads 6/9). See §7 for the exact
> owns-vs-defers split.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop
  condition.** Work in priority order; look left and right for adjacent bugs.
- **This page's distinctive property:** BYOIP's ownership gate is anchored **outside AWS** — at the RIR (RDAP
  record) and the RPKI (ROA). This page is the recipe for *building that out-of-AWS anchor*. Therefore most leads
  here are **(a) weaknesses in the AWS-authored proofing artifact / workflow** and **(b) ROA/RDAP misconfiguration
  footguns the AWS doc actively instructs** — not classic in-AWS cross-tenant bugs. Rate accordingly and keep the
  shared-responsibility line in view: the RDAP/ROA objects themselves are RIR-owned, not AWS-owned.
- **HARD STOP:** the moment any oracle would touch a *real* third party's RIR allocation / RDAP record / ROA, or
  reveal an identity/credential/ARN belonging to AWS's own service plane (e.g. the internal RDAP-fetch/validation
  fleet), stop, preserve evidence, flag for AWS-Security disclosure. All oracles below are for an **authorized lab
  holding its own test RIR allocation** or `iam:Simulate*` only.

---

## 1. Pentest Objectives (boundary-breach goals)

1. Provision/advertise an IP range **to an AWS account that was never cross-checked against the proof** — i.e.
   demonstrate the X.509-cert-in-RDAP anchor authorizes a prefix without binding it to the calling account
   (develops parent Lead 2 at the artifact level).
2. Show the **self-signed cert carries no binding** to the account or the CIDR (arbitrary CN), so the entire proof
   reduces to "who can write the RDAP comments field."
3. Show the proof **artifact persists** past its documented lifetime (cert left in RDAP, no re-validation cadence,
   signer-chosen expiry) → a re-provisioning / takeover window (develops parent Lead 4).
4. Show the **non-public-IPv6 path drops the ROA anchor**, leaving a single (RDAP-cert) anchor (parent Lead 5,
   mechanism established here).
5. Identify **ROA-authorization footguns the doc instructs** (over-permissive max-length enabling more-specific
   hijack; the "existing-ASN-first" ordering warning as a self-inflicted-outage trigger).

---

## 2. Components, Assets, and Design

This page has **no customer-reachable AWS process and no new AWS API**. Its "components" are a key-generation
recipe and two writes into **third-party registry objects** that later become AWS's trust input.

**Customer-facing interface (this page):**
- A **Linux terminal** (the doc explicitly offers **AWS CloudShell** or WSL as the environment — `:11`). Commands
  are pure `openssl`; nothing calls an AWS API on this page. The AWS control-plane call (`provision-byoip-cidr`
  with `--cidr-authorization-context`) happens on the *next* page (`byoip-onboard.md:58/63`) — parent-owned.
- Two manual writes to the customer's **RIR account**: (a) paste the PEM cert into the RDAP record's free-text
  field; (b) create a ROA in the RIR's RPKI console.

**Trust artifacts created here (the real assets):**
- **Private RSA-2048 key** (`private-key.pem`), AES-256-encrypted with a passphrase (`:52`). This is the signing
  key for the later authorization message — the single cryptographic secret the whole gate rests on.
- **Self-signed X.509 certificate** (`certificate.pem`), 365-day example expiry (`:199`), **arbitrary Common
  Name** ("not needed for AWS provisioning … can be any internal or public domain name" `:222`), PEM on one line.
- **RDAP record entry** — the cert pasted into **ARIN "Public Comments"** on the Network Information object /
  **RIPE "descr"** on the inetnum/inet6num / **APNIC "remarks"** (`:236–238`). A **human-readable free-text
  field**, not a structured cryptographic object.
- **ROA object** — RPKI Route Origin Authorization listing authorized origin ASNs (Amazon 16509+14618; GovCloud
  8987; ESC 16509+214101) + existing ASNs, with a **maxLength** and an expiration date (`:29`, `:245`).

**Identity / trust anchor:** control of the **RIR account** that owns the inetnum/inet6num object (to write the
RDAP comment and the ROA). The X.509 keypair is self-signed and **ephemeral**; its only legitimacy is sitting in
that RDAP field. **The AWS account identity is orthogonal** — nothing on this page binds the cert, the key, or the
ROA to any specific AWS account.

**Untrusted-data entry → transform:** the PEM cert the customer places in RDAP is later **fetched (whois/RDAP) and
parsed by an AWS-internal validation fleet**, which authenticates the signed authorization message against it and
checks the ROA (`byoip-onboard.md:20`). That fetch+parse is AWS-internal (not customer-reachable) — noted for
completeness, out of direct scope.

```
 Preparation phase (THIS page — no AWS API)              RIR / RPKI (NOT AWS)            AWS (parent-owned)
 ┌───────────────────────────────┐                     ┌────────────────────────┐     ┌────────────────────┐
 │ openssl genpkey (RSA2048,AES) │  private-key.pem     │                        │     │ provision-byoip-   │
 │ openssl req -x509 (CN=any)    │─────────────────────▶│  RDAP record           │     │ cidr (SigV4,       │
 │   → certificate.pem (1 line)  │   paste PEM into     │   comments/descr/remarks│◀───│  ec2:Region only)  │
 └───────────────────────────────┘   free-text field   │   = cert anchor         │ fetch+parse cert,  │
 ┌───────────────────────────────┐                     │                        │ verify signed msg, │
 │ create ROA (ASNs+maxLength+exp)│────────────────────▶│  RPKI ROA (origin ASNs)│ check ROA          │
 └───────────────────────────────┘                     └────────────────────────┘     └────────────────────┘
     (private key reused next page to sign  1|aws|{account}|{cidr}|{YYYYMMDD}|SHA256|RSAPSS  — parent owns)
```

---

## 3. API / Interface Inventory

**This page defines NO AWS API.** All commands are `openssl`; all registry writes are RIR-portal/manual. The AWS
control-plane actions that *consume* these artifacts (`ProvisionByoipCidr`, `AdvertiseByoipCidr`, …) are inventoried
and IAM-audited in **parent §3** — reused verbatim here; the key facts that matter for this page's leads:

| Item | Where defined | Relevance to this page's leads |
|---|---|---|
| `openssl genpkey -aes256 -algorithm RSA … 2048` | this page `:52` | the signing key; AES-256 at-rest + passphrase (opsec, Lens T) |
| `openssl req -new -x509 -key … -days 365` | this page `:199` | self-signed cert, signer-chosen expiry, arbitrary CN `:222` |
| RDAP write (ARIN Public Comments / RIPE descr / APNIC remarks) | this page `:236–238` | the trust anchor is a free-text field; write access = RIR-account control |
| ROA (origin ASNs + maxLength + expiry) | this page `:29/:245/:248` | authorization object; maxLength footgun; ROA-less non-public-IPv6 path |
| `provision-byoip-cidr --cidr-authorization-context Message=…,Signature=…` | `byoip-onboard.md:63` (**parent-owned**) | `CidrAuthorizationContext` is `Required: No` (`API_ProvisionByoipCidr.md`); `{account}` self-composed `:31/:37` |
| `ProvisionByoipCidr`/`AdvertiseByoipCidr`/`WithdrawByoipCidr`/`DeprovisionByoipCidr` | `list_ec2.md` (**parent §3**) | **no resource type, `ec2:Region` only** — region-wide, un-pinnable to a CIDR (parent Lead 1) |

**Undocumented/console-hidden knob (reconfirmed from parent, relevant here):** `--cidr-authorization-context` is
**optional at the schema level** (`API_ProvisionByoipCidr.md`), i.e. the proof artifact this whole page builds is
not schema-mandatory on the consuming call. Keep that pointer; the deep analysis is parent Leads 2–3.

---

## 4. Trust-Boundary Map

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|---|
| T1 | Holder of **write access to a prefix's RDAP record** (RIR-account control) | An AWS account that provisions the prefix | cert in RDAP comments + later signed msg whose `{account}` is self-composed | Prefix reaches `provisioned`/`advertised` under an AWS account **not cross-checked** against anything the cert or RDAP binds = account-binding breach (parent Lead 2; mechanism = the cert carries **no** account/CIDR field, §P1) |
| T2 | The self-signed X.509 cert as a **bearer anchor left in RDAP** | Future (re-)provisioning of the same CIDR | cert removal is advisory, expiry signer-chosen, no AWS re-validation cadence | Cert still valid + still in RDAP after provisioning ⇒ a captured/re-generated signature re-asserts provisioning (parent Leads 3/4; artifact created & "optionally" removed **here** §P2) |
| T3 | Anyone who can originate from a **ROA-authorized ASN** | The prefix's routing, via an over-permissive ROA maxLength | the doc instructs maxLength = CIDR size "for full flexibility to divide across Regions" (`:248`) | A more-specific announcement (longer than intended) still passes RPKI-valid because maxLength was set loose = de-aggregation/hijack-enabling ROA the doc instructed (§P3) |
| T4 | Non-public-IPv6 (`/60`) provisioner | The ownership gate | ROA **not required** on this path (`:32/:261`) | A prefix reaching `provisioned` with **RDAP-cert signature only, no ROA** = single-anchor (weaker) gate (parent Lead 5; condition set **here**) |
| T5 | Operator who follows the migration step in the wrong order | Their own production routing | "create a ROA for your existing ASN **before** Amazon's" (`:255`) | ROAs for Amazon ASNs created while the existing ASN lacks a ROA ⇒ existing advertisements invalidated = self-inflicted availability break (§P5) |
| T6 | Customer who generates the key in **AWS CloudShell** (`:11`) | The BYOIP signing key's at-rest location | key file persists in CloudShell's managed home dir; passphrase typed interactively | Private key / passphrase recoverable from CloudShell persistent storage or shell history by a principal with CloudShell access who should not reach the BYOIP key = opsec/secret-reachability concern (§P6, Low) |

---

## 5. Recommended Areas of Focus (one block per firing lens)

### Area P1 — The self-signed cert carries no account/CIDR binding; the RDAP free-text field is the whole root of trust (HEADLINE)
**Lenses:** P (identity-proofing integrity) + U (guarantee-vs-enforcement).
**Background.** BYOIP's "we verify you control the address range" (`byoip-onboard.md:20`) resolves, on this page, to
three facts: (1) the cert is **self-signed** — no CA, no external PKI anchor (`:43`, `:199`); (2) its **Common Name
is explicitly arbitrary** — "not needed for AWS provisioning … can be any internal or public domain name" (`:222`),
and every other DN field "can be left blank" (`:196`); (3) it is pasted into a **human-readable free-text field** —
ARIN *Public Comments*, RIPE *descr*, APNIC *remarks* (`:236–238`). Nothing in the cert names the AWS account or the
CIDR. The CIDR↔account binding is asserted **only later**, in a client-composed string
`1|aws|{account}|{cidr}|…` signed by this keypair (`byoip-onboard.md:31/37`) — and `{account}` is typed by the
caller, with `CidrAuthorizationContext` `Required: No`.
**Security Concern.** The ownership gate therefore reduces to **"who can write the RDAP comments field of the
inetnum/inet6num object"**, plus a self-asserted account number. A party with RDAP write access to a prefix
(a stale RIR account, a mis-delegated sub-allocation, an acquired/transferred netblock whose RDAP control was never
cleaned up) can mint a cert with any CN, place it, and sign a message naming **any AWS account**. Whether AWS
cross-checks that `{account}` against the authenticated caller is undocumented (parent Lead 2).
**High-level Test Scenarios (falsifiable).**
- *Claim:* the signed `{account}` is not bound to the caller. *Oracle:* from lab Account B, `provision-byoip-cidr`
  with a `Message` whose `{account}` = Account A (or a random 12-digit value) but a valid signature from the
  prefix's RDAP cert. Success ⇒ account not bound. (Mechanism anchored here; test executes on the parent's
  provision page.)
- *Claim:* the cert's CN/DN is never validated. *Oracle:* provision with a cert whose CN is a random/unrelated
  domain; success confirms CN is cosmetic (as the doc states, but confirm AWS does not later assert it).
- *Claim:* the proof is schema-optional. *Oracle:* `provision-byoip-cidr` **without** `--cidr-authorization-context`
  for a range whose RDAP+ROA already satisfy AWS — does provisioning proceed on registry state alone?
**Doc evidence:** `:43/:196/:199/:222/:236–238`; `byoip-onboard.md:20/31/37`; `API_ProvisionByoipCidr.md`
(`Required: No`). **Severity-if-true:** High (account-confusion / mis-provision), **but likelihood gated by the
dominant precondition of RDAP write control** — primarily an authz-clarity/account-binding defect, not standalone
takeover. Reportable as an AWS-workflow weakness only insofar as AWS fails to bind `{account}`; the RDAP field
weakness itself is an RIR property (out of AWS scope — state it).

### Area P2 — Proof artifact persists past its documented lifetime (advisory removal, signer-chosen expiry, no re-validation cadence)
**Lenses:** AA (revocation completeness) + U.
**Background.** The page frames the cert as transient — "only used during the provisioning phase" (`:23`), "must
only be valid for the duration of the provisioning process" (`:196`), "**You can** remove the certificate from your
RIR's record after provisioning is complete" (`:23/:240`). Every one of these is **advisory**: removal is optional
("You can"), the 365-day expiry is an **example the signer chooses** ("Be sure to set the expiration
appropriately" `:196`), and **nothing on this page or in `byoip-onboard.md` states an AWS re-validation cadence**.
The ROA likewise has an expiration date the customer sets (`:29`), and enforcement of ROA validity is discretionary
— "Amazon **reserves the right** to stop advertising" (`:258`).
**Security Concern.** A cert left in RDAP with a long/unbounded validity remains a **standing signing anchor**: the
same keypair can re-sign a fresh authorization message to re-provision after a deprovision, or (per parent Lead 3)
replay a captured message. The advertisement can outlive the ROA/cert because re-checks are discretionary, not
scheduled. This is the artifact-lifecycle root of parent Leads 3 (replay) and 4 (persistence).
**High-level Test Scenarios.**
- *Claim:* AWS never re-validates. *Oracle:* provision+advertise with a valid ROA, then **delete the ROA / let it
  expire** and poll `describe-byoip-cidrs` over days; state remaining `advertised` ⇒ discretionary-only enforcement.
- *Claim:* expiry window is uncapped. *Oracle:* set the cert `-days` and the ROA expiry years out; confirm AWS
  accepts them (does provisioning cap the signer-chosen window?).
- *Claim:* a left-behind cert re-authorizes. *Oracle:* deprovision, leave the cert in RDAP, re-sign and re-provision
  — succeeds within the cert's validity ⇒ persistence window = cert lifetime, not provisioning duration.
**Doc evidence:** `:23/:196/:240/:258`; cross-ref parent Leads 3/4. **Severity-if-true:** Medium — persistence of
advertisement past the proof; the AWS-owned slice is the **absence of a documented re-validation cadence / expiry
cap**, which a customer could reasonably assume exists.

### Area P3 — ROA max-length the doc instructs enables more-specific announcement (de-aggregation / hijack-enabling)
**Lenses:** U (documented-guidance-vs-security) + AA.
**Background.** The page instructs: "You must set the **maximum length** to the size of the CIDR that you are
bringing in" and, for the IPAM path, "for IPv4 CIDRs you must set the maximum length … to `/24` … **This ensures
that you have full flexibility to divide your public IP address across AWS Regions**" (`:245/:248`). A ROA's
`maxLength` governs the **longest** more-specific prefix an authorized ASN may originate while staying RPKI-valid.
Setting maxLength to the full `/24` (IPv4) or `/48` (IPv6) is **the loosest value the range allows**.
**Security Concern.** RPKI's main protection is that a ROA with `maxLength == prefixLength` forbids RPKI-valid
more-specifics (the classic anti-hijack posture). The AWS doc instead instructs the **permissive** setting so AWS
can split the block across Regions — meaning any ASN the ROA authorizes (including, transiently, an existing ASN
left in the ROA per `:245`, or a mis-entered ASN) can originate RPKI-valid more-specifics. The security trade-off
(flexibility vs. anti-hijack tightness) is **not surfaced to the operator**. If the customer additionally lists an
ASN they no longer control, or fat-fingers an ASN, the loose maxLength widens the blast radius.
**High-level Test Scenarios.**
- *Claim:* the instructed maxLength permits more-specifics. *Oracle:* with a lab allocation, create the ROA exactly
  as instructed (maxLength = /24), then verify (via a looking-glass / RPKI validator) that a more-specific /25–/32
  from an authorized ASN validates RPKI-"valid" rather than "invalid".
- *Claim:* existing-ASN entries linger. *Oracle:* follow `:245` (list existing ASNs + Amazon ASNs); confirm the doc
  gives no step to *remove* the existing ASN after cutover ⇒ a standing RPKI authorization for the old origin.
**Doc evidence:** `:245/:248`. **Severity-if-true:** Low–Medium — a documentation/guidance weakness (AWS-authored
instruction steers toward the permissive ROA); the actual routing security is RIR/RPKI-owned. File as an
AWS-doc-guidance concern, not a service bug.

### Area P4 — Non-public IPv6 drops the ROA anchor (single-anchor gate established here)
**Lenses:** P (degraded gate).
**Background.** Twice this page states the ROA step is skipped for non-public IPv6: "**A ROA is not required for
non-publicly advertisable IPv6 address space**" (`:32`, repeated `:261`), and the most-specific non-public range is
`/60` (`:245`). On that path the **only** ownership anchor is the RDAP-cert signed message — the RPKI/ROA leg of
the trust chain is absent.
**Security Concern.** The non-public path is a **single-anchor** gate: RDAP-record control alone (one free-text
field at the RIR) suffices, with no RPKI cross-check. The parent (Lead 5) owns the provisioning-side test ("reaches
`provisioned` within minutes"); this page is where the **condition is set** (ROA omitted). Also surfaces the
**doc-internal `/60`-vs-`/56` contradiction** the parent flagged (this page `:245` says `/60`;
`API_ProvisionByoipCidr.md` says `/56`) — present in both offline and online, **not drift**, must be resolved live.
**High-level Test Scenarios.**
- *Claim:* non-public IPv6 provisions with no ROA. *Oracle:* provision a `--no-publicly-advertisable` `/60` with a
  valid RDAP-cert signature and **no ROA**; reaching `provisioned` confirms ROA is not consulted (parent Lead 5).
- *Claim:* min non-public prefix is ambiguous. *Oracle:* attempt `/56` and `/60` non-public provisioning; whichever
  the control plane accepts resolves the doc contradiction.
**Doc evidence:** `:32/:245/:261`; `API_ProvisionByoipCidr.md`. **Severity-if-true:** Medium — weaker gate +
low owner-visibility; blast radius limited (non-public ranges reach only via DX/VPN/TGW).

### Area P5 — "Existing-ASN-first" migration ordering = self-inflicted-outage trigger
**Lenses:** U (operational-guidance integrity) + L (availability).
**Background.** "When you migrate advertisements from an on-premises workload to AWS, you must create a ROA for your
**existing ASN before** creating the ROAs for Amazon's ASNs. Otherwise, you might see an impact to your existing
routing and advertisements" (`:255`). Creating the Amazon-ASN ROA first (or an invalid/non-compliant ROA) can make
the existing origin RPKI-"invalid" and drop live advertisements — and provisioning actions are **un-cancellable**
(`ec2-byoip.md:112`, parent Lead 1/8).
**Security Concern.** This is an availability footgun the sequence of this page can trigger: a single out-of-order
ROA edit affects **production routing**, not a lab resource. It is self-inflicted (own account), so **not an
attacker primitive by itself** — but combined with the parent's Lead 1 (region-wide, un-pinnable BYOIP lifecycle
authority) an over-privileged *sibling* principal who can create/modify ROAs (outside AWS) or withdraw the prefix
(inside AWS) can weaponize the same ordering against a peer team.
**High-level Test Scenarios.**
- *Claim:* out-of-order ROA creation invalidates existing advertisements. *Oracle:* (lab, with a disposable
  allocation) create the Amazon-ASN ROA before the existing-ASN ROA and observe RPKI-validity flip on the existing
  origin via a validator. **Do not run against any live/production prefix.**
**Doc evidence:** `:255/:258`; `ec2-byoip.md:112`. **Severity-if-true:** Low as self-DoS (out of scope per §7);
Medium if chained to a cross-team authority gap (defer the authority side to parent Lead 1/8).

### Area P6 — Key material in CloudShell / shell history (opsec / secret-reachability, LOW)
**Lenses:** T (cross-service secret reachability) + O (residue).
**Background.** The page recommends performing these tasks in **AWS CloudShell** (`:11`). The private key
(`private-key.pem`, AES-256 + passphrase) and later the base64 signature are produced in that managed shell;
CloudShell persists the user's home directory in AWS-managed storage between sessions.
**Security Concern.** The BYOIP signing key — the one secret the whole gate rests on — may come to rest in
CloudShell's persistent home dir, and the passphrase / `text_message` / `signed_message` (`byoip-onboard.md:37/51`)
may land in shell history or CI logs. A principal with CloudShell access (or access to the backing store) who
should not reach the BYOIP key could recover it. This is a **customer opsec footgun**, not an AWS service defect:
the key is customer-generated and the doc even encrypts it at rest (`-aes256`). Noted for completeness and to warn
the hunter off treating CloudShell storage as an in-scope service bug.
**High-level Test Scenarios.** *Oracle:* confirm whether `private-key.pem` persists across CloudShell sessions and
whether the passphrase prompt/`signed_message` echo into history; evaluate who in-account can read the home-dir
backing store. **Severity:** Low / Informational; **out-of-scope as a service bug** (customer-owned key, customer
environment).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Provision a prefix to an unbound AWS account | cert-in-RDAP + self-composed `{account}` | "we verify that you control the address range" (`byoip-onboard.md:20`) — but cert has no account field (§P1) |
| Re-provision after deprovision via left-behind cert | RDAP cert, signer-chosen expiry | "only used during provisioning … you can remove" (`:23/:240`) — advisory, no re-validation cadence (§P2) |
| RPKI-valid more-specific via instructed maxLength | ROA maxLength = /24 | "ensures full flexibility to divide across Regions" (`:248`) — permissive by instruction (§P3) |
| Non-public IPv6 provisioned with no ROA | ROA-less path | "A ROA is not required for non-publicly advertisable IPv6" (`:32/:261`) (§P4) |
| Out-of-order ROA drops live advertisements | ROA ordering | "create a ROA for your existing ASN before Amazon's" (`:255`) (§P5) |
| BYOIP signing key recoverable from CloudShell | private-key.pem at rest | `-aes256` + passphrase (`:52`) — customer-owned (§P6) |

---

## 7. What this plan OWNS vs. DEFERS (cross-references)

**Owns (develops here, net-new granular depth over the parent):**
- The **preparation-phase trust-artifact mechanics**: self-signed cert with arbitrary unbound CN, free-text RDAP
  comment/descr/remarks anchor, ROA authorization semantics (§P1, §P3, §P4).
- The **artifact lifecycle** (advisory removal, signer-chosen expiry, no re-validation cadence) as the *root cause*
  of the parent's replay/persistence leads (§P2).
- The **"existing-ASN-first" ordering** availability footgun (§P5) and the **CloudShell key-material** opsec note
  (§P6).
- Re-confirms the `/60`-vs-`/56` doc contradiction at this page's line (`:245`) (§P4).

**Defers / cross-references (do NOT duplicate):**
- **The signed authorization message** format, RSA-PSS signing command, replay, and the `{account}`-binding *test*
  → live in `byoip-onboard.md`, **owned by `ec2-byoip-attack-research-plan.md` (parent Leads 2–3)**. §P1 anchors
  the *mechanism* (cert has no account field) but the provisioning-call test is the parent's.
- **IAM-unscopability of the four lifecycle actions** (region-only, no CIDR resource type) → **parent §3 / Lead 1**.
- **5-range quota DoS**, **within-pool `AllocateAddress` squatting**, **BYOASN region-only + ROA-vs-ASN origin
  consistency** → parent Leads 8 / 7 / 6+9.
- **RAM cross-account sharing isolation (IPAM+Organizations path)** → parent Lead 10 + Amazon VPC IPAM docs
  (`tutorials-byoip-ipam.html`, `tutorials-byoasn.html`) — outside this mirror.
- **AWS-internal RDAP fetch + cert parse** (a potential Lens-Q/F parser surface) → AWS-internal, not customer-
  reachable; §8 doc-gap, not a lead.
- **ec2-networking hub** is the grandparent; **ec2-byoip plan** is the direct parent of this page-level child.

---

## 8. Null hypotheses / doc gaps (lenses checked, pages named)

- **Lens A (cross-tenant IDOR) — N/A.** Read the full `prepare-for-byoip.md`: it defines no resource-by-ID AWS API;
  the only identifiers are the customer's own CIDR/ASN and RIR objects. The provisioning IDOR surface (if any) is
  on the parent's provision page, and parent §3 shows the lifecycle actions take a CIDR *string*, not an ARN.
- **Lens G (SSRF) — N/A on this page / low overall.** No field on this page is a customer-supplied URL the service
  dereferences. AWS selects the RIR RDAP/RPKI endpoint from the CIDR, not from caller input (parent §4 Lens G).
  The RIR-portal links (`:236–253`) are browser destinations for the human, not server-fetched by AWS.
- **Lens B/C (PassRole / credential vending) — N/A.** No role ARN, no `PassRole`, no STS, no credential-vending
  field anywhere on this page (pure openssl + manual RIR writes).
- **Lens F (translation/injection) — N/A for the customer surface.** The only parse is AWS's internal verification
  of the cert/signature at the RIR/validation fleet (byoip-onboard.md:20) — AWS-internal, not a customer-input→
  query layer. Flagged as a doc-gap parser surface in §7, not a confirmed lead.
- **Lens Q (uploaded-blob parsing) — out-of-scope / doc-gap.** The X.509 cert is uploaded to the **RIR's** RDAP, not
  to an AWS parser; AWS later fetches and parses it internally. The cert bytes are attacker-influenced (anyone with
  RDAP write controls them), so AWS's cert/PEM/ASN.1 parse is a theoretical hardening question — but AWS-internal
  and not customer-API-reachable. Mark **doc-gap — confirm the AWS-side parse surface first**, do not assume N/A.
- **Lens K / H / W / FF / BB / CC / DD / EE / N / Y — N/A.** No LLM/agent, no KMS/encryption-context, no attestation,
  no JWT/OIDC, no multi-parser request path, no upstream-context header, no caching layer, no predictable-name
  shadow resource, no namespace migration, and no HTTP/TLS/signature-version surface **on this preparation page**
  (confirmed by reading all 261 lines). The transport/signature analysis of the *provision* call belongs to the
  parent.
- **Lens O (audit-log evasion) — doc-gap (shared with parent).** Whether cert placement, ROA creation, and the
  async "up to 24 hours" ROA-propagation window (`:250`) emit any AWS-side signal is untraceable from these pages —
  the registry writes are at the RIR (no AWS log at all), and the AWS-side ingestion/validation observability is
  undocumented. Carry forward with parent §8 item 3.

**Doc gaps for the next agent:**
1. **`{account}` binding (the single highest-value live test).** Does AWS cross-check the signed `{account}`
   against the authenticated caller at `provision-byoip-cidr`? Settles §P1 / parent Lead 2. Requires a lab holding
   a real/test RIR allocation (expensive precondition).
2. **Re-validation cadence / expiry cap.** Is there any periodic ROA/RDAP re-check, or a cap on the signer-chosen
   cert/ROA expiry? Settles §P2.
3. **`/60` vs `/56` non-public-IPv6 minimum.** This page `:245` says `/60`; `API_ProvisionByoipCidr.md` says `/56`.
   Present in both offline and online (not drift) — resolve which the control plane enforces (§P4).
4. **AWS-side cert fetch+parse hardening.** The internal RDAP whois fetch + X.509 parse consumes attacker-influenced
   bytes; its robustness is undocumented (Lens Q/F doc-gap, §7). AWS-internal — flag for AWS-Security, do not probe.

### Drift check result (online vs offline, 2026-10-15)
Online `prepare-for-byoip.html` fetched (`.md` twin) and compared to the offline mirror: **no material drift.**
Identical: the 3-step onboarding model, `openssl genpkey -aes256 … 2048` / `openssl req -new -x509 … -days 365`,
arbitrary-CN note, ARIN/RIPE/APNIC RDAP-field instructions, Amazon ASNs 16509/14618 (GovCloud 8987, ESC
16509/214101), maxLength = CIDR-size with /24 IPv4 / /48 public IPv6 / /60 non-public IPv6, 24-hour ROA window,
cert-removal advisory, "reserves the right to stop advertising", "ROA not required for non-public IPv6", and the
CloudShell/WSL tip. The signed-authorization-message content confirmed to live in `byoip-onboard.md` (not this
page) and is parent-owned.

---

*Produced by the `security-questionbuilder` skill. Documentation-only; every oracle is for execution by an
authorized hunter in a sanctioned lab holding its own test RIR allocation (or via `iam:Simulate*`) — never against
production, any third party's RIR/RDAP/ROA, or AWS's own service plane.*
