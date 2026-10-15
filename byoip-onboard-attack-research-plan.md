# BYOIP Onboarding Procedure — Attack / Research Plan

**Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/byoip-onboard.html`
**Offline twin:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/byoip-onboard.md` (335 lines)
**Drift check:** online `.md` twin fetched and compared — **byte-identical, no drift** (ASNs 16509 / 14618 / 8987 / 214101 identical; message format identical).
**Skill:** security-questionbuilder (6-step boundary-first method)
**Date of analysis:** 2026-10-15
**Analyst note / model:** produced from documentation only. No live system was touched. This plan lists boundaries that *might* not hold and the exact observation that would settle each — it never asserts a bug exists.

---

## §0 — Scope, relationship to the parent plan, and reading order

This is a **page-level deep-dive COMPLEMENT** of the existing parent plan, not a replacement:

- **Parent (owns the service-wide BYOIP surface):** `/work/aws-docs/ec2-byoip-attack-research-plan.md`
  — target `ec2-byoip.html`; a page-level child of the `ec2-networking` hub. Already owns **Leads 1–10**:
  Lead 1 (four lifecycle actions IAM-unscopable to a CIDR — `ec2:Region` only), Lead 2 (self-asserted
  `{account}` in the signed message not bound to the caller; `CidrAuthorizationContext` `Required: No`),
  Lead 3 (replayable bearer blob / signer-chosen expiry / no nonce), Lead 4 (no re-validation cadence →
  advertisement outlives proof), Lead 5 (non-public IPv6 drops ROA = single-anchor gate), Lead 6 (BYOASN
  region-only), Lead 7 (`AllocateAddress` within-pool IP-squatting, no `ec2:PublicIpAddress`), Lead 8 (5-range/
  region quota DoS), Lead 9 (ROA-vs-ASN origin consistency), Lead 10 (EIP transfer deferred to siblings).

- **This plan (owns only what the ONBOARDING PROCEDURE page uniquely adds):** the step-by-step
  provision → advertise → withdraw → deprovision → **validate** procedure. It develops the *mechanism-level*
  surface that only becomes visible on this page — the exact signing command, the **provision-time-only** auth
  context (the asymmetry the parent names but does not anchor), the signer-chosen expiry example, the
  advertisable-status immutability, the 10-second rate limit, the `NetworkBorderGroup` advertise knob, and the
  entire `#byoip-validation` whois/RDAP/RIPEstat recon section.

**Reading order:** parent first (service model + IAM ground truth), then this page-level plan for the procedure
mechanics. Every lead here is cross-referenced to the parent lead it refines; where this plan merely *sharpens* a
parent lead, it says so and does not re-derive it.

**Hard-stop reminder (unchanged from parent):** every lead below is to be tested only against a researcher's own
account and own IP ranges with synthetic/canary values. The moment any observation implicates **AWS's own service
plane, another customer's prefix, or a real third party's RDAP/ROA record**, stop, preserve evidence, and flag for
disclosure. The RIPEstat / whois recon in A2 is read-only against public data but must still target only ranges you
own or AWS's own published anchors — never probe a third party's holdings as part of a PoC.

---

## §1 — Components, Assets, and Design (onboarding procedure view)

The onboarding page describes a **four-party, two-phase** control flow. The parent plan has the full component
list; here is the procedure-specific decomposition that the lenses attach to.

**Actors / zones**
- **Caller** — an IAM principal in the customer account holding `ec2:ProvisionByoipCidr` /
  `ec2:AdvertiseByoipCidr` / `ec2:WithdrawByoipCidr` / `ec2:DeprovisionByoipCidr` (all region-wide; see parent Lead 1).
- **AWS BYOIP control plane** — receives `provision-byoip-cidr` with a `CidrAuthorizationContext`
  (`Message` + `Signature`), relays the signed message to the RIR, and later honours advertise/withdraw/deprovision
  **with no further cryptographic proof**.
- **RIR (ARIN / RIPE / APNIC)** — holds the RDAP record (self-signed X.509 cert) and the RPKI ROA; authenticates
  the signature against the cert and checks authorization against the ROA. **Trust anchor lives here, not in AWS IAM.**
- **RIPE NCC RIPEstat** — a **public, unauthenticated** Data API (`stat.ripe.net/data/rpki-validation`) the
  customer is told to `curl` to verify the ROA. Third-party dependency reachable by anyone.

**Two-phase trust model (the crux of this page)**
```
PHASE 1 — PROVISION (one-time, cryptographically gated)
  caller ──provision-byoip-cidr(--cidr, CidrAuthorizationContext{Message,Signature})──▶ AWS CP ──▶ RIR
           message = 1|aws|{account}|{cidr}|{YYYYMMDD-expiry}|SHA256|RSAPSS
           signature = RSA-PSS/SHA256(saltlen=-1) over message, base64, tr '+=/' '-_~'
           ── async: pending-provision → provisioned  (publicly-advertisable: up to 1 week;
              non-public IPv6: "within minutes", NO ROA required)
           ── advertisable flag is set HERE and is IMMUTABLE thereafter

PHASE 2 — ADVERTISE / WITHDRAW / DEPROVISION (ongoing, NO crypto proof — IAM only)
  caller ──advertise-byoip-cidr(--cidr [,NetworkBorderGroup])──▶ AWS CP ──▶ BGP announce   (≤ once / 10 s)
  caller ──withdraw-byoip-cidr(--cidr)─────────────────────────▶ AWS CP ──▶ BGP withdraw   (≤ once / 10 s)
  caller ──deprovision-byoip-cidr(--cidr)──────────────────────▶ AWS CP  (after release EIP + disassoc IPv6 + withdraw)

RECON (anyone, no AWS creds)
  attacker ──whois RDAP(range)──▶ RIR            → reads the X.509 cert in Public Comments/descr/remarks
  attacker ──GET stat.ripe.net/.../rpki-validation?resource=ASN&prefix=CIDR──▶ RIPEstat
                                                 → learns whether a prefix has a VALID ROA for an Amazon ASN
```

**Assets** (procedure-specific): the plaintext `Message`, the detached RSA-PSS `Signature`, the self-signed X.509
private key `private-key.pem`, the provisioned pool's advertisable flag, and the BGP advertisement state itself
(the real-world asset — route origination for the customer's prefix).

**Identifier shape:** the only identifier any Phase-2 action takes is the raw `--cidr` string (plus optional
`NetworkBorderGroup`). There is no pool-id, no account scoping in the call, no `ec2:Cidr` condition key (parent Lead 1).

---

## §2 — Trust-boundary map (procedure seams)

| # | From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|---|
| B1 | Caller (IAM, region-wide) | A *provisioned* prefix's BGP advertisement | `advertise`/`withdraw`-byoip-cidr — **no auth context** | A principal that never held the signing key toggles advertisement of a prefix it did not provision → ownership proof did not gate the operation (**sharpens parent Lead 1 + Lead 4**). |
| B2 | Signed `Message` for region/NBG X | Honoured for region/NBG Y | message carries no region/NBG token; region+`NetworkBorderGroup` supplied out-of-band on the CLI | Same `Message`/`Signature` accepted to provision/advertise in a region or border group the proof never named (**sharpens parent Lead 3 oracle (b)**). |
| B3 | Signer (chooses expiry date) | AWS validity window | expiry is a signer-chosen field in the message, no documented upper bound | A far-future expiry (`99991231`) is accepted → the proof blob is effectively non-expiring and infinitely replayable (**sharpens parent Lead 3 oracle (c)**). |
| B4 | Anyone on the internet | ROA/RDAP ownership state | public `whois` RDAP + RIPEstat `rpki-validation` API | A third party enumerates which prefixes carry a VALID ROA for an Amazon ASN (16509/14618/8987/214101) with zero AWS credentials → onboarding state is a public oracle (**net-new; parent §8 flagged observability only generically**). |
| B5 | Caller | advertisable-vs-non-public flag | flag set at provision, **immutable** afterward | Confirm no API path flips the flag post-provision → a mis-provision (or a malicious non-public provision of a prefix, parent Lead 5) is a one-way door the owner cannot self-remediate without full deprovision. |
| B6 | Caller (shared account) | account-global 10 s rate limiter | `advertise`/`withdraw` "at most once every 10 seconds … even if you specify different address ranges" | One principal's advertise/withdraw calls throttle *another* team's recovery advertise in the same account → shared-limiter contention / recovery-delay (**bounds parent Lead 8**). |

---

## §3 — API / interface surface (onboarding actions)

IAM ground truth is the parent plan's §3 (lines cited from `list_ec2.md`:
`ProvisionByoipCidr` L9257, `AdvertiseByoipCidr` L4662, `WithdrawByoipCidr` L9756, `DeprovisionByoipCidr` L6510 —
all **empty resource type, `ec2:Region` sole condition key**). This plan does **not** re-audit it. The procedure-level
delta, confirmed from the API reference pages, is the **request-parameter asymmetry**:

| Action | Mutating | Auth context required? | Request params (from API ref) | Procedure note |
|---|---|---|---|---|
| `ProvisionByoipCidr` | yes | **YES — `CidrAuthorizationContext{Message,Signature}`** (`Required: No` on the *struct*, see parent Lead 2) | `Cidr`(req), `CidrAuthorizationContext`, `PubliclyAdvertisable`, `NetworkBorderGroup`, `PoolTagSpecifications`, `MultiRegion`, `Asn`, `DryRun` | one-time crypto gate; async `pending-provision`→`provisioned`; publicly-advertisable up to 1 week, non-public "within minutes", no ROA |
| `AdvertiseByoipCidr` | yes | **NONE** | `Cidr`(req), `Asn`, `NetworkBorderGroup`, `DryRun` | **no `CidrAuthorizationContext` parameter exists** — IAM-only gate; ≤ 1 call / 10 s account-wide; `NetworkBorderGroup` selects a Local Zone border group |
| `WithdrawByoipCidr` | yes | **NONE** | `Cidr`(req), `DryRun` | **no auth context** — IAM-only; ≤ 1 call / 10 s account-wide |
| `DeprovisionByoipCidr` | yes | **NONE** | `Cidr`(req), `DryRun` | **no auth context** — IAM-only; requires prior release-EIP + disassociate-IPv6 + withdraw; "up to a day" |
| `DescribeByoipCidrs` | no | NONE | `MaxResults`, `NextToken`, `DryRun` | monitors `pending-provision`/`provisioned`/`failed-provision`/`pending-advertising`/`pending-withdrawal`; returns a `ByoipCidr` object |

**Key observation (B1 generator):** the expensive cryptographic ownership proof is attached to **exactly one** of
the four lifecycle actions. Everything that actually controls real-world routing of the prefix after provisioning
(advertise / withdraw) and the teardown (deprovision) is gated by **region-wide IAM alone** — no re-proof, no
`CidrAuthorizationContext` parameter even exists on those actions. The onboarding page makes this concrete by
printing the advertise/withdraw/deprovision commands verbatim **without** a `--cidr-authorization-context` option.

**Non-SDK / console-hidden knob to flag:** `NetworkBorderGroup` on `AdvertiseByoipCidr` (and provision) is an
advertise-time choice of Local Zone border group (`us-east-1-dfw-2`, `us-west-2-lax-1`, `us-west-2-phx-2`;
`eu-central-1-ist-1` async). It is not surfaced in the onboarding prose beyond a Note. See A8.

---

## §4 — Boundary-lens leads (NET-NEW to the onboarding page)

Each lead is a falsifiable claim with a doc-anchored mechanism and a confirm/refute oracle. Parent Leads 1–10 are
**not** repeated; where a lead sharpens a parent lead it is marked `(sharpens Lead N)`.

### A1 — Provision-time-only crypto proof: all ongoing routing control is IAM-only  ★ HEADLINE
- **Lens:** U (guarantee vs enforcement) + X (sibling-action parity) + refines A/Lead 1 & Lead 4.
- **Claim:** The signed-message ownership proof gates **only** `ProvisionByoipCidr`. Any principal holding
  `ec2:AdvertiseByoipCidr` / `ec2:WithdrawByoipCidr` (region-wide — no `ec2:Cidr` key) can start or stop BGP
  advertisement of **any already-provisioned prefix in the region** with **no cryptographic re-proof**, because
  those actions have no `CidrAuthorizationContext` parameter at all.
- **Mechanism (doc evidence):** `byoip-onboard.md` L114–122 shows `advertise-byoip-cidr`/`withdraw-byoip-cidr`
  invoked with only `--cidr` and `--region` (no `--cidr-authorization-context`). `API_AdvertiseByoipCidr.md` /
  `API_WithdrawByoipCidr.md` request-parameter lists contain **no** `CidrAuthorizationContext`. Parent Lead 1
  (region-wide IAM, no CIDR scoping) supplies the authz half.
- **Confirm/refute oracle:** in your own account, provision a canary range you own; then from a *second* principal
  granted only `ec2:WithdrawByoipCidr` (no provision rights, never possessed the key), call `withdraw-byoip-cidr`
  on that CIDR. If the withdrawal succeeds (prefix stops being advertised) the crypto proof did not gate the
  operation — ownership is enforced once, at provision, then never again. **Breach oracle:** a principal that
  cannot prove ownership changes the real-world routing state of a provisioned prefix.
- **Preconditions / cost / severity:** needs an own provisioned range + two principals in one account; read-only
  w.r.t. other tenants. **Severity if true:** High — intra-account, a least-privilege-footgun that turns a
  region-wide IAM grant into unrestricted BGP advertise/withdraw over every BYOIP prefix the account provisioned
  (route black-holing / flapping). Cross-account escalation is **out of scope** and a hard stop; this lead stays
  intra-account.
- **Why net-new:** the parent states "advertisement outlives proof" (Lead 4) abstractly; this anchors it to the
  concrete API-parameter asymmetry the onboarding page exposes, and reframes it as a sibling-action-parity gap.

### A2 — RIPEstat / RDAP as an unauthenticated public BYOIP-onboarding recon oracle  ★ net-new
- **Lens:** A (disclosure) + O (observability/recon) + G-adjacent (service-named external dependency).
- **Claim:** The documented validation step is a **public oracle**: anyone, with no AWS credentials, can determine
  whether an arbitrary prefix has a **valid ROA for an Amazon ASN** — i.e. is onboarded (or being onboarded) to
  AWS BYOIP — and can read the self-signed X.509 cert the owner published in RDAP.
- **Mechanism (doc evidence):** `byoip-onboard.md` L160–334 (`#byoip-validation`): `whois -h whois.arin.net …` /
  `whois.ripe.net` / `whois.apnic.net` return the cert from `Public Comments`/`descr`/`remarks`; the RIPEstat
  curl `https://stat.ripe.net/data/rpki-validation/data.json?resource={{ASN}}&prefix={{CIDR}}` returns
  `"status":"valid" | "invalid_asn" | "unknown"` for any ASN+prefix pair. Doc lists the Amazon ASNs to test:
  16509, 14618 (commercial), 8987 (GovCloud), 16509/214101 (European Sovereign Cloud).
- **Confirm/refute oracle:** against **your own** range (or AWS's own published anchors only), issue the RIPEstat
  query for ASN 16509 and observe the `validity` transition `unknown → valid` across the provision window. The
  research question is **not** "can I read my own ROA" (obviously yes) but: *does this let an outside party
  (a) fingerprint which customer prefixes are AWS-hosted, (b) detect an in-progress onboarding (the up-to-1-week
  publicly-advertisable window) before BGP changes, or (c) read the owner's self-signed cert and metadata?*
  Confirm by showing the state is observable with zero AWS auth. **Breach oracle:** onboarding/ownership state of
  a prefix is disclosed to an unauthenticated third party.
- **Preconditions / cost / severity:** trivial, read-only, offline-ish (public APIs). **Severity if true:**
  Low–Medium as a standalone info-leak, but a **force-multiplier**: it tells an attacker *which* prefixes are
  worth targeting with A1 (region-wide withdraw) and *when* a prefix is mid-onboarding (a race window, cf. the
  parent's hijack-timing framing). **Discipline:** only ever query ranges you own or AWS's own anchors — do not
  enumerate a third party's holdings as a PoC. Flag any cross-party disclosure for responsible disclosure instead
  of exercising it.

### A3 — Signed message carries no region / border-group binding → cross-region & cross-NBG replay  (sharpens Lead 3)
- **Lens:** C/P (scope of a bearer credential) + replay.
- **Claim:** The `Message` (`1|aws|{account}|{cidr}|{YYYYMMDD}|SHA256|RSAPSS`) binds **account + CIDR + expiry +
  algorithm only** — it contains **no Region and no NetworkBorderGroup**. Region and NBG are supplied out-of-band
  on the CLI (`--region`, `NetworkBorderGroup`). So one validly-signed blob is replayable to provision/advertise
  the same CIDR in any region or any border group the caller's IAM permits.
- **Mechanism (doc evidence):** message format `byoip-onboard.md` L28–40 (no region token). Region emphasised
  separately at L59–64 ("You must specify the AWS Region …"). `NetworkBorderGroup` is an independent
  advertise/provision parameter (`API_AdvertiseByoipCidr.md`). `MultiRegion` is a provision flag (API ref).
- **Confirm/refute oracle:** with one `Message`/`Signature` pair for a CIDR you own, attempt provision in two
  different regions / border groups; if both accept the same blob, the proof is region-agnostic. **Breach oracle:**
  a proof minted for one location authorises a location it never named.
- **Severity if true:** Medium — widens the blast radius of a leaked/replayed blob (parent Lead 3) across the full
  region/NBG matrix, including Local Zones where advertisement is async (A8).

### A4 — Shipped example message is EXPIRED; expiry is signer-chosen with no documented upper bound  (sharpens Lead 3)
- **Lens:** R (copy-verbatim shipped artifact) + P (gate strength) + W (guidance integrity).
- **Claim (two parts):**
  (a) The verbatim example `text_message="1|aws|0123456789AB|198.51.100.0/24|20211231|SHA256|RSAPSS"`
      (L37) carries expiry **20211231** — ~5 years in the **past** as of 2026-10-15. A reader who adapts the
      example but forgets the date ships an **already-expired** proof. Does the control plane reject a past-dated
      message with a clear error, or silently? (Null-hypothesis-worthy: it almost certainly rejects — the research
      value is *what the error reveals* and whether the staleness is caller-diagnosable.)
  (b) Conversely, because the expiry is a **signer-chosen** field with no documented ceiling, a signer can set
      `99991231`, making the authorization blob effectively **non-expiring** and infinitely replayable (parent
      Lead 3's "no nonce" plus this unbounded horizon = a durable bearer credential).
- **Mechanism (doc evidence):** L28 "the date is the expiry date of the message"; example L37; no upper-bound
  statement anywhere on the page; no nonce/one-time-use statement.
- **Confirm/refute oracle:** (a) submit a past-dated message for your own CIDR → observe accept/reject + error
  text/timing (an enumeration oracle on account/CIDR validity if the error differs by field). (b) submit a
  far-future expiry → if accepted, document the maximum horizon. **Breach oracle:** a non-expiring or
  staleness-silent proof.
- **Severity if true:** Medium — reinforces the "replayable bearer blob" risk the parent raised; the net-new angle
  is the **shipped-expired example** (a documentation-integrity defect) and the **unbounded horizon**.

### A5 — Exact signing mechanism: RSA-PSS saltlen=-1 + URL-safe base64 transform + "do not modify any values"
- **Lens:** P (crypto gate) + W (guidance integrity / tamper surface).
- **Claim:** The page prescribes a precise, non-obvious signing recipe and warns the operator *not* to change any
  value. Research questions: is the verifier strict about the **exact** PSS parameters (salt length = -1 → max/
  hash-length-derived, SHA-256), or will it accept weaker/alternative paddings or digests announced in the message
  itself (the message *names* `SHA256|RSAPSS` — is that field **honoured as a selector** by the verifier, i.e. can
  a caller downgrade by editing it, or is it fixed server-side)? Does the URL-safe transform `tr '+=/' '-_~'`
  create any canonicalization ambiguity on the verifier side?
- **Mechanism (doc evidence):** L50–52 signing command (`openssl dgst -sha256 -sigopt rsa_padding_mode:pss
  -sigopt rsa_pss_saltlen:-1 -sign private-key.pem … | openssl base64 | tr -- '+=/' '-_~'`); L47–48 Important
  note "do not modify or replace any of the values"; message trailer `…|SHA256|RSAPSS` (L31) names the alg **inside
  the signed string**.
- **Confirm/refute oracle:** against your own key/CIDR, vary only the **algorithm selector substring** in the
  message (keep a valid signature over the modified string) and observe whether the verifier treats `SHA256|RSAPSS`
  as authoritative (algorithm-confusion / downgrade surface) or ignores it in favour of a fixed server-side policy.
  **Breach oracle:** verifier honours a caller-chosen algorithm field, or accepts a non-prescribed padding/digest.
- **Severity if true:** High if a downgrade is accepted (crypto gate weakened); otherwise a documented null
  hypothesis ("alg field is cosmetic; verifier fixes PSS/SHA-256"). Likely null, but it is the kind of
  message-is-self-describing field that has produced real alg-confusion bugs, so it earns an explicit test.

### A6 — Advertisable-vs-non-public flag is a one-way door (immutability footgun)  (sharpens Lead 5)
- **Lens:** P (state-transition irreversibility) + U (guarantee).
- **Claim:** "You can only specify whether an address range is publicly advertisable **during provisioning**. You
  cannot change the advertisable status later on" (L87–88). Combined with parent Lead 5 (a **non-public** IPv6
  range needs **no ROA** — a weaker gate), this means a prefix provisioned non-public can **never** be made public,
  and vice-versa, without a full deprovision (up to a day, A9). Research question: can the weaker non-public gate
  (no ROA) be used to provision a range that the legitimate owner then cannot convert/repair in place?
- **Mechanism (doc evidence):** L85 "A ROA is not required to provision a non-public address range"; L87–88
  immutability note; deprovision latency L158.
- **Confirm/refute oracle:** provision your own IPv6 range non-public, then confirm there is **no** API/parameter
  to flip it to publicly-advertisable (search `ModifyByoip*` — none exists; `DescribeByoipCidrs` is read-only).
  **Breach oracle:** no in-place remediation path exists → recovery requires deprovision+reprovision.
- **Severity if true:** Low–Medium standalone (availability/operability), but it compounds the parent's Lead-5
  non-public-gate concern: the weaker-gated path is also the irreversible one.

### A7 — Account-global 10-second advertise/withdraw rate limit = shared-limiter contention  (bounds Lead 8)
- **Lens:** L (limits / shared-resource DoS).
- **Claim:** `advertise-byoip-cidr` and `withdraw-byoip-cidr` may each be called "at most once every 10 seconds,
  **even if you specify different address ranges**" — i.e. the limiter is **per-account/operation, not per-CIDR**.
  One principal (or one noisy automation) consuming the limiter delays every other principal's advertise/withdraw
  in the same account. In an incident (A1 malicious withdraw), the owner's **recovery** re-advertise is itself
  subject to the 10-second floor, bounding mean-time-to-restore.
- **Mechanism (doc evidence):** `byoip-onboard.md` L108–110; `API_AdvertiseByoipCidr.md` / `API_WithdrawByoipCidr.md`
  "once every 10 seconds, even if you specify different address ranges each time."
- **Confirm/refute oracle:** in your own account, issue two advertise calls <10 s apart for two different owned
  CIDRs; observe throttling of the second. **Breach oracle:** cross-CIDR throttling confirms a shared limiter.
- **Severity if true:** Low — a self-contention / recovery-delay bound, not a direct cross-tenant DoS (no evidence
  the limiter is cross-account). Documents the amplifier/attenuator for the parent's Lead 8 and A1's recovery path.

### A8 — NetworkBorderGroup selection at advertise time (Local Zone border-group mismatch)
- **Lens:** X (parameter the console under-surfaces) + W (operational footgun).
- **Claim:** `AdvertiseByoipCidr` accepts a `NetworkBorderGroup` (`us-east-1-dfw-2`, `us-west-2-lax-1`,
  `us-west-2-phx-2`; IPv6 not supported in Local Zones) chosen at advertise time, and in `eu-central-1-ist-1`
  advertise/withdraw are **asynchronous** (`pending-advertising`/`pending-withdrawal`). The EIP and the resource
  must reside in the **same** border group. Research question: does a wrong/omitted NBG strand the prefix or
  advertise it in an unintended border group, and does the async Local Zone path have the same no-auth-context
  exposure as A1 plus a wider state-observability gap?
- **Mechanism (doc evidence):** `API_AdvertiseByoipCidr.md` `NetworkBorderGroup` param + "Choose the network
  border group carefully as the EIP and the AWS resource … must reside in the same network border group";
  `byoip-onboard.md` L124–125 async note.
- **Confirm/refute oracle:** (own range) advertise with a mismatched NBG and observe failure/strand behaviour and
  the async state machine via `DescribeByoipCidrs`. **Breach oracle:** advertisement reaches an unintended border
  group, or a mismatch is silently accepted.
- **Severity if true:** Low — operability/mis-routing within one's own account; included for coverage of the
  advertise-time knob the onboarding prose under-surfaces.

### A9 — Deprovision ordering dependency + long async windows (observability gap)
- **Lens:** O (observability) + L (state machine).
- **Claim:** Teardown is an ordered multi-step sequence (release EIPs → disassociate IPv6 CIDRs → withdraw →
  deprovision) with long/async windows (`pending-provision` up to 1 week; non-public "within minutes";
  `failed-provision` requires manual re-run; deprovision "up to a day"; Local Zone async states). The only
  progress signal is `DescribeByoipCidrs` (read-only, no documented EventBridge/CloudTrail event for these
  transitions). Research question: during these windows is the prefix's control state ambiguous enough to enable a
  race (e.g. A1 withdraw during a victim's `pending-advertising`), and is there any automated detection a defender
  could rely on?
- **Mechanism (doc evidence):** `byoip-onboard.md` L127–158 (ordering + "up to a day"), L66/L72–78 (async
  provision + `failed-provision`), L124–125 (Local Zone async). Parent §8 flagged EventBridge/CloudTrail coverage
  as untraced.
- **Confirm/refute oracle:** (own range) walk the full lifecycle and record which transitions emit CloudTrail /
  EventBridge events vs are visible only by polling `DescribeByoipCidrs`. **Breach oracle:** a security-relevant
  state transition (advertise/withdraw) with **no** push event a defender could alarm on.
- **Severity if true:** Low–Medium — detection/monitoring gap that makes A1 harder to notice; primarily a
  defender-visibility finding, confirming the parent's open observability question for this specific procedure.

---

## §5 — Explicit null hypotheses (pages checked)

- **SSRF (Lens G) — N/A for this page.** Pages checked: full `byoip-onboard.md`. The only URL/host fields are
  *customer-run* client-side (`whois` servers, the RIPEstat `curl`) — the customer dereferences them from their
  own shell, not a field AWS fetches server-side. The one AWS-side dereference (the signed message relayed to the
  RIR) is to a fixed RIR, not a caller-supplied endpoint. No `…Url`/`…Endpoint`/callback field is accepted by any
  onboarding API. (The `CidrAuthorizationContext` does **not** contain a URL.) → not a server-side fetch surface.
- **Upload/blob parsing (Lens Q) — N/A.** The signature is a base64 string, not an uploaded file AWS stores/renders.
- **Injection into a translation layer (Lens F) — N/A for the onboarding procedure** (deferred to RIR-side ROA/
  RDAP parsing, which is outside AWS's plane and must not be probed).
- **Tagging/ABAC (Lens … tags):** `ProvisionByoipCidr` accepts `PoolTagSpecifications`, but the onboarding page
  does not describe tag-based authz; tag-condition-key analysis belongs to the parent/`list_ec2` audit, not here.

Each null above names the page(s) read, per the skill's discipline — none is an unexamined "N/A".

---

## §6 — Prioritization (concentrate fire)

1. **A1 (High)** — provision-time-only proof; the headline, most-actionable, intra-account testable lead.
2. **A2 (Low–Med, high leverage)** — public RIPEstat/RDAP recon oracle; cheap, read-only, enables target/timing selection for A1.
3. **A5 (High if true, likely null)** — algorithm-selector-in-signed-message downgrade; worth one strict test.
4. **A3 / A4 (Med)** — region/NBG-unbound + unbounded-expiry replay surface (sharpen parent Lead 3).
5. **A6 / A8 / A9 (Low–Med)** — immutability footgun, NBG mismatch, async observability gap — coverage + defender-visibility.
6. **A7 (Low)** — shared rate-limiter contention; bounds parent Lead 8 and A1 recovery.

---

## §7 — What a downstream hunter needs (handoff)

- **Read the parent first:** `/work/aws-docs/ec2-byoip-attack-research-plan.md` (Leads 1–10, IAM table with
  `list_ec2.md` line numbers, crypto-chain analysis). This plan assumes that context.
- **IAM authority:** `https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html`
  (`.md` twin `list_ec2.md`) — slug is `list_ec2`, **not** `list_amazonec2` (dead). The four lifecycle actions have
  empty resource types + `ec2:Region` only; no `ec2:Cidr`/`ec2:ByoipCidr`/pool-id/`ec2:Asn` key exists.
- **API refs confirming the §3 asymmetry:** `API_ProvisionByoipCidr.md` (has `CidrAuthorizationContext`),
  `API_AdvertiseByoipCidr.md` / `API_WithdrawByoipCidr.md` / `API_DeprovisionByoipCidr.md` (**no** auth-context
  param), `API_CidrAuthorizationContext.md` (`Message`+`Signature`, both `Required: Yes` within the struct, but the
  struct itself is `Required: No` on provision — parent Lead 2).
- **Test discipline:** own account + own IP ranges + synthetic/canary values only. A1/A6/A7/A8/A9 are intra-account
  behavioural tests. A2 is read-only against **your own** ranges or AWS's own published anchors — never a third
  party's. **Hard stop + disclose** if any observation implicates AWS's service plane, another tenant's prefix, or
  a real third party's RDAP/ROA record.
- **Open doc gaps (confirm against reference before relying):** (i) upper bound on message expiry — undocumented
  (A4b); (ii) whether `SHA256|RSAPSS` in the message is an honoured selector or cosmetic (A5); (iii)
  EventBridge/CloudTrail coverage of provision/advertise/withdraw/deprovision transitions — untraced (A9); (iv)
  whether the 10 s limiter is per-account or per-principal (A7). None resolvable from docs alone.

---

## §8 — One-line summary

The BYOIP **onboarding procedure** page's defining security property is a **two-phase trust asymmetry**: ownership
is proved **once**, cryptographically, at `ProvisionByoipCidr` — and never again, so every subsequent routing-control
action (`advertise`/`withdraw`/`deprovision`) is gated by **region-wide IAM alone**, with **no auth-context parameter
even defined** (A1). Supporting net-new surfaces: a **public, credential-less RIPEstat/RDAP recon oracle** for
onboarding state (A2), a signed-message proof that is **region/NBG-unbound** and potentially **non-expiring** (A3/A4),
an **immutable** advertisable flag reachable via the weaker ROA-less non-public path (A6), and an async lifecycle with
a **push-notification observability gap** (A9). All sharpen or extend — never duplicate — the parent
`ec2-byoip-attack-research-plan.md`.
