---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html
---

# EC2 Security Group Rules Reference ("Security group rules for different use cases") — Attack Research Plan

Source of leads: `AWSEC2/latest/UserGuide/security-group-rules-reference.html` (offline twin `/work/aws-docs/docs/AWSEC2/latest/UserGuide/security-group-rules-reference.md`, **confirmed byte-identical to the online `.md` 2026-10-15** modulo frontmatter/blank-line/trailing-newline), cross-checked against the authoritative mechanism page `vpc/latest/userguide/security-group-rules.md` (online fetched 2026-10-15) and `list_ec2.md`. Status: documentation-derived hypotheses only; nothing tested against a live account.

> **This is a page-level deep-dive CHILD of the EC2 Security Groups chapter HUB** (`ec2-security-groups-attack-research-plan.md`). The target page is a **cookbook/catalog**: eight tables of example SG rules for common use cases (web server, database, SSH/RDP from your computer, same-SG communication, ping/ICMP, DNS, EFS, ELB). It introduces **NO new API, no new IAM action, no new condition key, no new resource type.** Its entire security value is as a collection of **AWS-authored, copy-verbatim sample rules** (Lens R variant: "AWS-published sample CODE insecure defaults") plus two **doc-vs-mechanism integrity defects** (Lens U). Everything mechanical about SG rules — the aggregation model, self-reference semantics, IAM scoping gaps, middlebox inertness, stateful-response egress — is **already owned by siblings and is only cross-referenced here, never restated.**

> **De-duplication contract (what this plan does NOT re-own):**
> - **Self-referencing-SG `-1/-1/-1` any/any full-mesh lateral movement** → HUB **H2**. This page is the *source* of the `-1/-1/-1/<self sg-id>` "allows all types of traffic" idiom; the mesh mechanism/oracle lives in H2.
> - **Additive-only / most-permissive-rule-wins aggregation (no deny rules)** → HUB **H3**. This plan owns only the **egress-specific** instance of H3 (see Area 3), which H3 states as the ingress-`0.0.0.0/0:22` case.
> - **Stateful response-channel egress bypass** → HUB **H1**.
> - **No rule-content (CIDR/port/protocol/direction) IAM condition key** → HUB **H3** + `changing-security-group` plan (settles that IAM cannot forbid `0.0.0.0/0`, a port, or a protocol in a rule).
> - **SG-referencing is NOT authorized against in `Authorize*`/`Revoke*` (IAM-no-effect + cross-account-no-CloudTrail)** → `ec2-security-groups-privatelink-attack-research-plan.md` **Area 1** (confirmed verbatim at `security-group-rules.md` L73–75).
> - **SG referencing silently inert across a routed middlebox hop** → privatelink **Area 8**. This page carries the matching "Note" verbatim; the topology test lives in Area 8.
> - **CLI runbook footguns (mislabeled revoke-ingress/egress, `0.0.0.0/0` in the modify example)** → `changing-security-group` plan **Area 5**.
> - **Open-egress default at create + no create-time forbid** → `creating-security-group` plan.

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- This page is **null-dominant**: the only two *exploitable network primitives* it would surface (self-ref mesh, most-permissive-wins) are owned by HUB H2/H3. The genuinely NET-NEW, filable items here are **AWS-authored secure-default / doc-integrity defects** (Lens R/U) — Low–Medium, AWS-owned, Tier-2 reportable because the samples are copy-verbatim and the defects are in AWS's own reference table. Rate honestly; do not inflate a cookbook into a cross-tenant bug.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Not reachable from this page — pure doc artifact.)

## 1. Pentest Objectives
Concrete, observable outcomes a hunter should aim to produce from leads anchored on this page:
1. Demonstrate that a customer who **copies the page's canonical sample rules verbatim** lands in a materially over-permissive posture AWS's own text would not flag at apply-time (web-server `0.0.0.0/0`+`::/0`; same-SG `-1/-1/-1` any/any; ping/ICMP "from anywhere").
2. Demonstrate the **egress fail-open**: adding the page's "restrict outbound" HTTP/HTTPS egress rules *without first deleting the default allow-all egress* yields **zero** egress restriction, with no synchronous signal (Area 3 — the egress instance of HUB H3; composes with HUB H1).
3. File the **ICMP source-address-family doc defect** (Area 2) and the **protocol/port `-1` semantics footgun** (Area 4) as AWS-owned doc-integrity findings.
4. (Deferred) The network-reachability exploitation of any posture above is executed under HUB H1/H2/H3 and privatelink Area 1/8 — this plan only establishes that the *sample content* steers the operator into those owned primitives.

## 2. Components, Assets, and Design
- **Interface:** none new. The page is read-only prose + eight rule tables. The rules are applied via `AuthorizeSecurityGroupIngress`/`Egress`, `ModifySecurityGroupRules`, `RevokeSecurityGroupIngress`/`Egress` (all owned by HUB / `changing-security-group`).
- **Asset:** the **sample rule set** itself — an AWS-authored artifact the customer is explicitly told to copy ("For instructions, see Create a security group and Configure security group rules"). A weak default *in the sample* is AWS's defect (Lens R carve-out), even though the resulting SG config is customer-applied data-plane.
- **Rule primitives named on the page (for reference):** protocol numbers `6`=TCP, `17`=UDP, `1`=ICMP, `58`=ICMPv6, `-1`=all; port `-1`=all ports; sources: CIDR (IPv4 `0.0.0.0/0`, IPv6 `::/0`), a security-group ID (self-reference / cross-SG reference), or (per VPC page) a prefix-list ID.
- **The eight use-case tables and their default breadth:**

```
 Use case            | Sample source/dest shipped          | Breadth as written
 --------------------|-------------------------------------|------------------------------------
 Web server (in)     | 0.0.0.0/0 AND ::/0  (80,443)        | ENTIRE INTERNET (v4+v6) — canonical 1st example
 Database (in)       | CIDR *or* SG-ID (1433/3306/5439/... )| operator-chosen (least-priv possible)
 Database (out)      | 0.0.0.0/0 / ::/0 (80,443) AFTER      | requires DELETING default allow-all first (Area 3)
                     |   removing default allow-all egress  |
 SSH/RDP from you    | "public IP of your computer / range"| scoped (GOOD example — no 0.0.0.0/0)
 Same-SG comms       | -1/-1/-1  <self sg-id>  (ANY/ANY)   | FULL MESH any proto/any port (HUB H2)
 ping/ICMP (in)      | "...or an IPv4 or IPv6 address FROM  | ANYWHERE offered as a source option
                     |   ANYWHERE"                         |   + address-family mismatch (Area 2)
 DNS server (in)     | CIDR *or* SG-ID (TCP/UDP 53)         | operator-chosen
 EFS (in)            | <self sg-id>  (NFS 2049)            | self-ref SCOPED to 2049 (GOOD contrast to same-SG)
 EFS (in)            | SSH 22 "your computer / network"    | scoped
 ELB                 | → defers to Elastic Load Balancing docs | pointer only (Lens X null)
```

- **Design observation (the net-new "tell"):** the page proves AWS *can and does* write a **port-scoped self-reference** sample (EFS: `<self sg-id>` on NFS 2049) — yet for the general "same security group" use case it ships the **unscoped `-1/-1/-1` any/any** rule. The breadth asymmetry is gratuitous: the safer pattern exists two tables down. (Owns the *comparative* observation; the mesh exploit is HUB H2.)

## 3. API / Interface Inventory
No new APIs. The page is a lead *source* for sample content; the mutating actions it steers toward are inventoried in the HUB and `changing-security-group` plan. For completeness:

| Name | Mutating | New/Existing | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|
| `AuthorizeSecurityGroupIngress`/`Egress` | Yes | Existing | Yes (SigV4/console) | SG-write holder | Applies the page's sample rules. **Owned by HUB** (no rule-content key). |
| `ModifySecurityGroupRules` | Yes | Existing | Yes | SG-write holder | Edits a rule to a sample value. **Owned by HUB / changing-SG.** |
| `RevokeSecurityGroupIngress`/`Egress` | Yes | Existing | Yes | SG-write holder | Required to delete the default allow-all egress (Area 3). CLI label-swap footgun **owned by changing-SG Area 5.** |

**Console-hidden knob sweep:** none introduced by this page (it predates and merely illustrates the actions above). The relevant undocumented-knob leads (`ec2:Attribute` casing, the SG-target row on `ModifyInstanceAttribute`) live in `changing-security-group`.

## 4. Trust-Boundary Map
This page crosses no new trust boundary itself; it steers the operator into boundaries other plans own. One row is net-new as a *comparative* observation:

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Operator copying the sample verbatim | The entire IPv4+IPv6 internet | Web-server sample ships `0.0.0.0/0`+`::/0` as the first example | A web/app tier that is internet-exposed because the canonical sample is, with no apply-time warning (Area 1). Owner-to-fix: AWS (sample), customer (apply). |
| Operator "restricting" egress | Attacker-controlled exfil endpoint | Default allow-all egress survives unless explicitly deleted first | After adding the sample narrow egress rules, arbitrary outbound still succeeds (Area 3 → composes HUB H1 stateful exfil). |
| (Deferred) any SG member | every co-member, any port | `-1/-1/-1/<self sg-id>` sample | **HUB H2** — not re-owned here. |

## 5. Recommended Areas of Focus

### Area 1 — Canonical sample rules ship over-permissive defaults as copy-verbatim code (Lens R / U, AWS-owned, Tier-2 reportable)
**Background.** The page is explicitly a copy-source ("For instructions, see Create a security group and Configure security group rules"). Its **first and most-copied example** — Web server rules — ships inbound `0.0.0.0/0` on 80/443 *and* `::/0` on 80/443 ("Allows inbound HTTP/HTTPS access from any IPv4/IPv6 address"). The same-SG example ships `-1/-1/-1/<self sg-id>` ("allows all types of traffic"). The ping/ICMP example offers "an IPv4 or IPv6 address from anywhere" as a source.
**Security Concern.** These are AWS-authored samples a customer pastes verbatim. There is **no rule-content IAM condition key** (HUB H3 / `changing-security-group`) that an org admin can use to forbid `0.0.0.0/0`, a protocol, or a port in the applied rule — so the sample's breadth is the *only* line of defense and nothing warns at apply-time. The web-server `::/0` is a separate, additional rule (double the internet exposure, easy to leave on even after narrowing v4). Per the Lens R carve-out, a weak default in an **AWS-published, copy-verbatim sample** is AWS's defect, not a customer footgun — reportable as a secure-default gap, **not** out-of-scope.
**High-level Test Scenarios (falsifiable claims):**
- **Claim:** Applying the Web server sample verbatim exposes 80/443 to the entire IPv4+IPv6 internet with no apply-time warning. → **Oracle:** `authorize-security-group-ingress` with the four sample rows returns success; `describe-security-group-rules` shows `0.0.0.0/0` + `::/0`; no advisory emitted. **Severity:** Medium (secure-default gap; the exposure itself is customer-applied).
- **Claim:** AWS ships a *scoped* self-reference sample (EFS 2049) but an *unscoped* one (`-1/-1/-1`) for the general same-SG case — a gratuitously broad canonical pattern. → **Oracle:** doc-comparison already confirmed (EFS NFS table vs same-SG table). File as a secure-default inconsistency; the mesh exploit itself is **HUB H2** (do not re-run). **Severity:** Low–Medium (doc/secure-default).
- **Claim:** The ping/ICMP sample normalizes "from anywhere" ICMP ingress. → **Oracle:** doc-confirmed; secure-default note. **Severity:** Low.
**Doc evidence:** `security-group-rules-reference.md` "Web server rules" / "same security group" / "ping/ICMP" tables. **Owner-to-fix:** AWS (sample) + customer (apply). **Stop condition:** doc-confirmed; this is a report, not a live-exploit lead (exploitation = HUB H1/H2/H3).

### Area 2 — ICMP table source-address-family doc defect + anywhere-ICMP (Lens U doc-vs-mechanism integrity, AWS-owned)
**Background.** The ping/ICMP tables read:
- IPv4 rows ("Custom ICMP - IPv4 / Echo request" and "All ICMP - IPv4"): source = "The public IPv4 address of your computer, a specific IPv4 address, **or an IPv4 or IPv6 address from anywhere**."
- IPv6 row ("All ICMP - IPv6 / IPv6 ICMP (58)"): source = "The IPv6 address of your computer, **a specific IPv4 address**, or an IPv4 or IPv6 address from anywhere."
**Security Concern.** An **ICMPv6 rule cannot match an IPv4 source**, and an IPv4-ICMP rule's source is an IPv4/CIDR (or SG/prefix-list), not "an IPv6 address." AWS's own reference table lists cross-address-family sources on both rows. This is a **doc-vs-mechanism integrity defect** (Lens U): a customer who copies the IPv6 row and tries "a specific IPv4 address" either gets a rejected/silently-dropped rule, or (worse, must be confirmed) a rule whose effective match differs from what the table implies — a false mental model of what ICMP ingress is actually permitted. Also, "an IPv4 or IPv6 address from anywhere" offered as a routine source normalizes anywhere-ICMP (recon/amplification surface; informational).
**High-level Test Scenarios:**
- **Claim:** Attempting the documented IPv4-source on an `All ICMP - IPv6` rule is not actually accceptable/meaningful. → **Oracle:** `authorize-security-group-ingress --ip-permissions IpProtocol=icmpv6,...` with an IPv4 `--cidr` → observe `ValidationException`/`InvalidParameterValue` (defect = doc says it's a valid source) vs silent acceptance that doesn't match v6 ICMP (defect = inert rule). Either outcome confirms the doc table is wrong. **Severity:** Informational–Low (AWS-owned doc integrity; file to AWS-Security as a reference-table correction).
- **Claim:** the cross-family source text is a copy/transcription error consistent across both v4 and v6 rows. → **Oracle:** doc-confirmed (both rows mismatched). File as a single doc-correction item.
**Doc evidence:** `security-group-rules-reference.md` "Rules for ping/ICMP" tables; authoritative types from `vpc/latest/userguide/security-group-rules.md` L38 ("type 8 for ICMP Echo Request or type 128 for ICMPv6 Echo Request"). **Stop condition:** one `authorize` DryRun/live call settles accept-vs-reject; then it is a doc-correction report.

### Area 3 — Egress "restriction" fail-open: narrow egress rules are inert unless the default allow-all is deleted FIRST (Lens U + HUB H3 egress instance; composes HUB H1)
**Background.** Database server section, verbatim: *"You can optionally restrict outbound traffic... You must first remove the default outbound rule that allows all outbound traffic."* Confirmed by `security-group-rules.md` L23: *"When you first create a security group, it has an outbound rule that allows all outbound traffic... If your security group has no outbound rules, no outbound traffic is allowed."*
**Security Concern.** The SG model is **additive-only with no deny and most-permissive-wins** (HUB H3). Adding the page's narrow HTTP/HTTPS egress rules **alongside** the default `0.0.0.0/0`/`::/0` allow-all does **nothing** — the broad default silently wins, and there is **no synchronous warning/validation** at the moment the operator adds a "restrictive" rule. The entire restriction depends on a single, easy-to-miss prose sentence ("You must first remove the default outbound rule"). An operator who adds the sample egress rules but skips/misreads that sentence believes outbound is locked to 80/443 while in reality **all** egress — including an attacker's exfil channel and the HUB-H1 stateful response path — remains open. This is the **egress-direction instance** of HUB H3 (which develops the ingress `0.0.0.0/0:22` case); the AWS-owned part is the design decision to make "restrict" a two-step delete-then-add with no apply-time signal, plus a sample that lists only the add step's rules.
**High-level Test Scenarios:**
- **Claim:** With the default allow-all egress still present, adding the sample narrow egress rules leaves arbitrary outbound reachable. → **Oracle:** on an instance in such an SG, open a connection to an arbitrary external IP on an arbitrary port (e.g. 4444) → succeeds; `describe-security-group-rules` shows both the narrow rules and the surviving `0.0.0.0/0` default. **Severity:** Medium (security-outcome: silent non-restriction + exfil channel open; High when chained to a sensitive data-plane via HUB H1).
- **Claim:** No API warning/validation is emitted when a narrow egress rule is added while the default allow-all egress exists. → **Oracle:** `authorize-security-group-egress` for 443 on a fresh SG returns success with no advisory; confirm console likewise silent. **Severity:** Low (detection/UX gap, AWS-owned).
- **Chain:** compose with **HUB H1** (responses to allowed inbound flow out regardless of egress rules) — even a *correctly* restricted egress SG does not stop reply-channel exfil; the Area-3 fail-open makes it worse. Rate at the end of the chain (unrestricted exfil from a workload believed egress-locked).
**Doc evidence:** `security-group-rules-reference.md` "Database server rules" ("You must first remove the default outbound rule..."); `security-group-rules.md` L23. **Cross-ref:** HUB H1, H3. **Stop condition:** one live egress connection test settles the primitive; the aggregation mechanism is owned by H3 (do not re-derive).

### Area 4 — Protocol/port `-1` ("All") semantics footgun (Lens U/S, Low)
**Background.** The same-SG table ships `-1 (All) / -1 (All) / -1 (All)`. Protocol `-1` means **all protocols**, and port `-1` means **all ports**; when protocol is `-1` the port field is **ignored** (all ports regardless of any port value).
**Security Concern.** An operator who sets protocol `-1` intending "all of one service" but types a specific port, or who copies the `-1/-1/-1` row intending only intra-tier app traffic, gets **all ports/all protocols** with no narrowing. The page never shows the *scoped* alternative for the same-SG case (contrast EFS's `6/2049/<self sg-id>` scoped self-ref). This is the sample-content root of HUB H2's any/any mesh; owned here only as the **protocol/port-semantics clarity gap** (that `-1` protocol voids the port scope).
**High-level Test Scenarios:**
- **Claim:** A rule with protocol `-1` and a specific port still permits all ports. → **Oracle:** `authorize-security-group-ingress IpProtocol=-1,FromPort=3306,ToPort=3306` → the resulting rule allows all ports (confirm via `describe` normalization + a connection on an off-port). **Severity:** Low (semantics footgun; the mesh exploit = HUB H2).
**Doc evidence:** same-SG table `-1 (All)` rows; `security-group-rules.md` L36 (protocol list). **Stop condition:** `describe` normalization confirms; report as clarity note.

### Area 5 — Cross-service sample pointers (EFS self-ref, ELB) (Lens X cross-service, mostly null)
**Background.** EFS rules ship a **scoped** self-reference (`<self sg-id>` on NFS 2049) plus a scoped SSH 22. ELB rules carry **no content** — they defer to three Elastic Load Balancing doc pages.
**Security Concern.** EFS's scoped self-ref is the *correct* counter-example to the same-SG any/any (reinforces Area 1's asymmetry observation); no distinct EFS primitive here (NFS/EFS mount-target SG scoping is EFS-owned). The ELB section is a **pointer only** — any SG-for-LB misconfiguration lead belongs to the ELB service plan, not EC2 SGs. The one EC2-relevant note: the ELB pattern (LB SG must allow comms with instance SG) is another **cross-SG reference** instance → governed by the same `Authorize*`-not-authorized-against-referenced-SG fact (privatelink **Area 1**), not re-owned.
**High-level Test Scenarios:** none net-new. Record EFS-scoped-self-ref as the positive control for Area 1; ELB → out-of-scope (ELB service).
**Doc evidence:** "Amazon EFS rules" / "Elastic Load Balancing rules" sections. **Stop condition:** pointer only.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack | Owned by |
|---|---|---|---|
| Verbatim web-server sample exposes 80/443 to all of IPv4+IPv6 | Web server sample rules | the sample itself (no IAM rule-content key exists to forbid `0.0.0.0/0`) | **This plan Area 1** |
| ICMP table lists cross-address-family / "anywhere" sources | ping/ICMP sample | the reference table's correctness | **This plan Area 2** (file to AWS) |
| Narrow egress rules inert because default allow-all not deleted | Database egress sample | the "You must first remove the default outbound rule" sentence + no apply-time signal | **This plan Area 3** (+ HUB H1/H3) |
| `-1` protocol voids a specific port scope | same-SG sample | protocol/port semantics clarity | **This plan Area 4** (exploit = HUB H2) |
| Self-ref `-1/-1/-1` any/any full mesh | same-SG sample | SG-membership-as-trust model | **HUB H2** (cross-ref only) |
| One broad rule silently defeats a narrow one | aggregation model | additive-only / most-permissive-wins | **HUB H3** (cross-ref only) |
| Referenced-SG in `Authorize*`/`Revoke*` IAM has no effect; cross-acct no CloudTrail | SG referencing | — (documented limitation) | **privatelink Area 1** (cross-ref only) |
| SG-reference inert across a middlebox hop → broader CIDR fallback | same-SG Note | the middlebox "Note" | **privatelink Area 8** (cross-ref only) |

## 7. Out-of-Scope Risk Categories
- **The network-reachability exploitation** of any over-permissive posture the samples produce (lateral movement, internet exposure, exfil) — executed under **HUB H1/H2/H3** and **privatelink Area 1/8**; this plan only establishes that the sample *content* steers the operator there.
- **Customer-applied SG config in general** is a customer footgun — in scope here **only** because the specific rule values are **AWS-authored copy-verbatim samples** (Lens R carve-out). A hunter must not report a customer's own hand-written `0.0.0.0/0` as an AWS defect.
- **ELB SG configuration** → Elastic Load Balancing service (the page is a pointer).
- **EFS mount-target SG / NFS scoping** → Amazon EFS service.
- **RDS default DB ports** (1433/3306/5439/5432/1521) → informational; port numbers are not a vulnerability.
- **IMDS, cross-tenant, service-plane** — not reachable from a static reference page.

## 8. Null hypotheses / doc gaps
- **Lens A (IDOR), C (vending), D (data→control), F (injection), J (OAuth), K (prompt), M (session), N (migration), T (secret reachability), V (segmentation reach), W (attestation), Y (transport), AA (share/revoke), BB/CC/DD/EE/FF** — **all null for this page.** It is a static catalog of example rule tables with no identifier, no fetched URL, no uploaded blob, no role ARN, no token, no parser, no cache, no namespace. Pages checked: the full `security-group-rules-reference.md` (all 8 tables) + the authoritative `vpc/latest/userguide/security-group-rules.md`.
- **Lens G (SSRF) / Q (upload):** null — no field on the page is a URL the service dereferences and no field carries an uploaded blob. (The only "sources" are CIDRs/SG-IDs/prefix-list-IDs = identifiers matched at the ENI, never fetched.)
- **Lens I / S (ABAC / condition-key semantics):** no condition key governs rule *content* (HUB H3 settles this) — so there is nothing new to scope here; the only Lens-S flavor present is the `-1`-protocol-voids-port semantics (Area 4).
- **Lens R applies but is thin:** the samples are data-plane SG rules, not IAM policy JSON; the reportable defects are secure-default/doc-integrity (Areas 1–2), honestly Low–Medium, AWS-owned.
- **Lens U fires at Areas 2, 3, 4** (doc-vs-mechanism integrity + the egress fail-open workflow). These are the plan's genuinely net-new, filable items.
- **Lens X (twin/cross-service):** the ELB section is a pointer (null here); the EFS/ELB cross-SG-reference reuses privatelink Area 1 (cross-ref).
- **Doc gaps / live-settle-before-investing:**
  1. Area 2 — does `authorize-security-group-ingress` with an IPv4 source on an `icmpv6` protocol rule **reject** (confirming the doc is simply wrong) or **silently accept an inert rule** (worse: false mental model)? One DryRun/live `authorize` call settles it.
  2. Area 3 — confirm there is **no** apply-time advisory when adding a narrow egress rule while the default allow-all egress survives (console + API). If an advisory *does* exist, the fail-open severity drops to Low.
  3. Area 4 — confirm `-1` protocol normalization voids `FromPort`/`ToPort` on `describe-security-group-rules` output.
- **Offline/online parity:** confirmed identical 2026-10-15 (no mirror drift). The authoritative mechanism page (`vpc/.../security-group-rules.md`) is the companion to read for enforcement semantics; this reference page is illustrative only.

---
*Built as a page-level child of the EC2 Security Groups HUB. Cross-references: HUB H1 (stateful egress), H2 (self-ref mesh), H3 (most-permissive-wins / no rule-content key); `ec2-security-groups-privatelink` Area 1 (SG-ref IAM/CloudTrail no-effect) + Area 8 (middlebox inertness); `changing-security-group` Area 5 (CLI runbook footguns); `creating-security-group` (open-egress default). See `project-aws-research-plans` memory for the convention.*
