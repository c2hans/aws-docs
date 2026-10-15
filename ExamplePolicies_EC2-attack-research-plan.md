# Attack / Research Plan — EC2 "Example Policies to control access to the Amazon EC2 API"

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.html
**Offline twin:** `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md` (1841 lines) — online `.md` twin verified to match offline headings.
**Authoritative key reference:** `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (10190 lines; the real markdown twin of `list_ec2.html`). Trust this over User-Guide prose for whether an action supports a resource type / condition key.
**Method:** `security-questionbuilder` (6-step boundary-first). This page is a gallery of **AWS-authored sample IAM policies copied verbatim by customers**, so **Lens R** (AWS-authored IAM-artifact audit) and **Lens S** (condition-key scoping / fail-open) dominate; Lens U (guarantee-vs-enforcement), B (PassRole/confused-deputy), A (unscopable Describe oracle), and EE (predictable-name) are secondary.
**Analysts:** primary agent + 3 parallel deep-dive subagents (RunInstances/AMI/EBS/LT; Spot fail-open semantics; PassRole/IMDS/SourceInstanceARN). All condition-key existence claims below are cross-checked against `list_ec2.md` with line citations.

> **Scope discipline (inherited).** Documentation-only analysis. This plan is executed later by a hunter against an authorized account using **read-only oracles** (`iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` — no resources created). HARD STOP the moment any evidence touches AWS's own service-plane identity/credential/ARN/account. Customer-authored footguns are noted but only **AWS-authored artifact defects** are Tier-2-reportable to `aws-security`.

---

## Section 0 — TL;DR / Headline leads

| # | Lead | Lens | Tier / Severity | Confidence |
|---|------|------|-----------------|------------|
| **H1** | **Spot `spot-instances-request` resource non-evaluation fail-open** — a Deny *or* an Allow-tag-mandate scoped to `spot-instances-request` is silently **not evaluated** when the Spot request is created untagged. AWS ships two "NOT SUPPORTED – DO NOT USE" examples + "Surprise inconsistency number 2" admitting it. A tenant/admin who believes they blocked Spot (or mandated chargeback tags) has not. | S/U | **Tier-2, High** | **High** — AWS pre-admits mechanism; oracle is a tagged-vs-untagged `RunInstances` differential |
| **H2** | **IMDSv2-required Deny bypassed via Auto Scaling `$Latest`/`$Default`** — the four IMDS "combine into one policy" examples do **not** close the ASG late-binding gap; closing it needs a *separate* `autoscaling:LaunchTemplateVersionSpecified:true` statement AWS never ships in the bundle. Page's own "Important" callout (lines 1690–1696) discloses the bypass. | R/U | **Tier-2, High** | **High** — AWS-acknowledged in-page |
| **H3** | **PassRole prefix-privesc, no `iam:PassedToService`** — both IAM-role examples (lines 1486–1546) scope `iam:PassRole` only by name-prefix (`role/DevTeam*`, `role/TestRole-*`); Example 2 additionally leaves `AssociateIamInstanceProfile`/`ReplaceIamInstanceProfileAssociation` on `Resource:"*"` with **no condition**. AWS's own service-authorization reference (list_ec2:4457) recommends pairing PassRole with `iam:PassedToService: ec2.amazonaws.com` — the EC2 UserGuide examples omit it. | B/R | **Tier-2, High** | **High** |
| **H4** | **`ModifyInstanceMetadataOptions` hop-limit raise is ungated** — hop-limit Deny only targets `ec2:RunInstances`; the `ModifyInstanceMetadataOptions` Deny checks only `HttpTokens`, never `MetadataHttpPutResponseHopLimit`, though the key **is** valid on that action (list_ec2:8864). An instance launched compliant can post-launch raise its hop limit to defeat SSRF-depth mitigations with no Deny tripped. | S/U | **Tier-2, Medium-High** | **High** |
| **H5** | **`Allow`+`NotResource: launch-template/*` blast radius** (lines 962–987) — "launch-template-scoped" RunInstances grant places **zero** restriction on AMI owner / subnet / SG / instance-profile *baked into* the LT; safety transitively depends on a *separate*, uncalled-out LT-management+tag permission. | S | **Borderline Tier-2, Medium** | Medium — missing-caveat, not mechanism bug |
| **H6** | **EBS root-volume encryption guarantee gap** — `ec2:Encrypted` exists on `volume`/`snapshot` rows but **not** on the `image` row (list_ec2:9945); the sample enforces "launch-time volumes encrypted" but cannot enforce "AMI built from encrypted snapshots." | U | Footgun (AWS-disclosed), High-if-misread | High |
| **H7** | **`ec2:Owner:amazon` vs "trusted partners" prose mismatch** (line 263) — sample promises "Amazon or verified partners," JSON delivers Amazon-only (fail-**closed**). whoAMI spoof angle **refuted** (`ec2:Owner` is server-resolved, not caller-supplied). | R/U | Tier-2, Low (docs-accuracy) | High |
| **H8** | **Dead-slug doc defect** — page (line 215) links the dead `list_amazonec2.html` slug (302→JS shell); live slug is `list_ec2`. | R | Tier-3 docs-hygiene | Confirmed |

---

## Section 1 — Components, Assets, and Design

**What this page is.** Not a service — a **documentation artifact**: ~30 worked IAM policy examples teaching customers how to scope the EC2 control-plane API (`RunInstances`, tagging, Spot, Reserved Instances, launch templates, IAM-instance-profile association, IMDS options). The "interface" under test is therefore the **IAM policy-evaluation engine as applied to EC2 condition keys**, and the "assets" are the sample JSON blobs customers copy verbatim.

**Primary actors / zones.**
- **Author (admin)** — writes/attaches these policies. Intends a boundary ("only Amazon AMIs", "no Spot", "IMDSv2 only", "pass only DevTeam roles").
- **Caller (principal)** — the IAM user/role the policy is attached to; tries to reach beyond the intended boundary.
- **EC2 control plane** — evaluates condition keys; its *resource-evaluation rule* ("a resource type is only evaluated if the request touches it", lines 999–1006) is the root cause of the Spot fail-opens.
- **Downstream services reachable via passed roles / instance profiles** (S3, DynamoDB, RDS in the `SourceInstanceARN` example) — the privesc target of H3.
- **IAM/STS** — mints instance-profile credentials; `ec2:SourceInstanceARN` encodes *credential provenance*, not network origin (H / lead L5).

**Key "resources" and identifier shapes.** Instance ARNs (`i-…`), AMI IDs (`ami-…`, hardcoded `ami-9e1670f7`/`ami-45cf5c3c` at lines 247–248), role ARNs matched by **name prefix** (`role/DevTeam*`, `role/TestRole-*`), launch-template ARNs (wildcarded `launch-template/*`), tag keys/values. **Name-prefix matching on role ARNs is the H3 enabler** — any current-or-future role under the prefix is passable.

**Where untrusted/attacker-controlled input enters the authorization decision.** Request-time tags (`aws:RequestTag`, `aws:TagKeys`), whether a resource is tagged at all (the Spot fail-open trigger), the target role ARN of a PassRole, the launch-template content (H5), and the `HttpTokens`/`HopLimit` metadata options.

---

## Section 2 — Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller | "Spot is blocked" admin intent | `RunInstances` with `MarketType=spot`, **no** `spot-instances-request` tag | Spot request **created** despite a Deny on `spot-instances-request` → H1 fail-open confirmed |
| Caller | "mandatory chargeback tag" admin intent | `RunInstances` (Spot) with zero tags | Untagged Spot request created despite Allow-tag-mandate → H1 variant |
| Caller (low-priv) | A more-privileged role under `DevTeam*`/`TestRole-*` | `AssociateIamInstanceProfile`/`ReplaceIamInstanceProfileAssociation` + `iam:PassRole` (prefix-only) | Simulator returns `allowed` for passing a role the caller could not assume directly → H3 privesc |
| Caller (post-launch) | SSRF-depth mitigation (hop limit ≤N) | `ModifyInstanceMetadataOptions` raising `HopLimit` | No Deny trips (no `MetadataHttpPutResponseHopLimit` condition on that action) → H4 |
| ASG operator | IMDSv2 mandate | New LT version under `$Latest`/`$Default` | `RunInstances` IMDSv1-restriction **not re-checked** → H2 |
| LT author | "LT-scoped RunInstances is safe" admin intent | Attacker-chosen AMI/subnet/SG baked into a `Purpose=Webservers`-tagged LT | RunInstances succeeds with attacker AMI/subnet via the `NotResource` grant → H5 |
| Reader of sample JSON | "root volume is encrypted" belief | Launch from AMI built on **un**encrypted snapshots | Instance launches; root volume unencrypted; no condition could have caught it → H6 |
| **Any caller** | **AWS service plane** | — | **HARD STOP** — any AWS-fleet identity/credential/ARN surfaced ⇒ cease, preserve, flag. (Not expected on a docs-only IAM-sample page.) |

---

## Section 3 — API / interface surface (actions appearing in the samples)

| Action | Mutating | Scopable by condition? (list_ec2) | Notes / lead |
|---|---|---|---|
| `ec2:Describe*` | No | Read-only; Resource must be `*` (no resource-level perms) | Read-only sample on `*` → account-wide **oracle** (Lens A), expected/unavoidable |
| `ec2:RunInstances` | Yes | Per-resource-type keys; **resource only evaluated if touched** (l.999–1006) | Root cause of H1; resource-type list l.9586–9603 |
| `ec2:CreateTags` | Yes | `ec2:CreateAction` (l.10066), `aws:RequestTag`, `aws:TagKeys` | Tag-on-create scoping; `*/*` wildcard breadth (lead L7) |
| `ec2:AssociateIamInstanceProfile` | Yes | **IS scopable** — `ec2:NewInstanceProfile`, `ec2:InstanceProfile`, `ec2:ResourceTag`, `aws:ResourceTag` (detail row l.4749) | Sample uses `Resource:"*"` **no condition** → H3; `ec2:NewInstanceProfile` could have constrained *which* profile and wasn't used |
| `ec2:ReplaceIamInstanceProfileAssociation` | Yes | Same keys (detail row l.9401) | H3 |
| `ec2:DisassociateIamInstanceProfile` | Yes | same | part of Example 1 bundle |
| `iam:PassRole` | — | matched on **role ARN**, prefix-wildcarded; `iam:PassedToService` **omitted** | H3; recommended pairing at list_ec2:4457 |
| `ec2:ModifyInstanceMetadataOptions` | Yes | **summary row blank (l.3780) but detail `instance` row has keys incl. HopLimit/HttpTokens (l.8861–8865)** | H4 — key exists, example never uses it; prose (l.1804) wrongly implies "no fine-grained controls" |
| `ec2:PurchaseReservedInstancesOffering` | Yes (cost) | on `*`, no cost cap | Lead L8 (Lens L cost/DoS) |
| `ec2:ModifyInstanceMetadataOptions` admin gate | — | identity-based only (`ec2-imds-admins`) | reinforces H4 |

**Undocumented/console-hidden knob sweep:** `ec2:NewInstanceProfile` (the key that would constrain H3) is not surfaced in the examples at all — the single most relevant knob for the privesc lead is omitted from the sample that most needs it.

---

## Section 4 — Boundary-lens catalog (detailed leads)

### Lens S / U — condition-key scoping & fail-open  *(highest yield)*

**L1 (H1a) — Spot Deny fail-open.** `Claim:` a Deny scoped to `arn:…:spot-instances-request/*` on `ec2:RunInstances` is never evaluated for an **untagged** Spot request → Deny fails open. `Mechanism:` lines 1049–1084 ("NOT SUPPORTED" Deny `DenySpotInstancesRequestsNOTSUPPORTEDDONOTUSE`, no `Condition`), general rule l.999–1006. `Oracle:` attach `AllowRun`(On-Demand) + the Deny; call `RunInstances MarketType=spot` with **no** `spot-instances-request` tag → **succeeds** (fail-open); repeat **with** a tag → `UnauthorizedOperation`. The tagged/untagged differential is the diagnostic signature. `Severity:` High intra-account governance-bypass. `Tier-2` (AWS-admitted).

**L2 (H1b) — Spot Allow-tag-mandate bypass ("Surprise inconsistency number 2").** `Claim:` an Allow that mandates `environment=production` on `spot-instances-request` is bypassed by omitting tags. `Mechanism:` line 752 + example `RequestSpotInstancesOnlyIfTagIsEnvironmentProductionNOTSUPPORTEDDONOTUSE` (l.1175–1225): "non-tagged Spot Instance requests being created." `Oracle:` 3-way differential — no tag ⇒ **allow** (bypass), `environment=production` ⇒ allow, `environment=staging` ⇒ deny. `Severity:` High for chargeback/segregation controls. `Tier-2`.

**L3 (H4) — hop-limit raise ungated on ModifyInstanceMetadataOptions.** `Claim:` a compliant-at-launch instance can raise its IMDS hop limit post-launch undetected. `Mechanism:` hop-limit Deny targets only `ec2:RunInstances` (l.1770–1799); the `ModifyInstanceMetadataOptions` Deny checks only `HttpTokens` (l.1738–1766); key `ec2:MetadataHttpPutResponseHopLimit` **is** valid on that action (l.8864). `Oracle:` `iam:SimulateCustomPolicy`, Action `ec2:ModifyInstanceMetadataOptions`, ContextEntries `ec2:MetadataHttpPutResponseHopLimit=10`, against the 4-statement bundle → predicted `allowed` (no Deny). `Severity:` Medium-High. `Tier-2` (bundle incomplete vs. "combine into one policy" claim).

**L4 (H5) — Allow+NotResource LT blast radius.** `Claim:` the LT-scoped RunInstances grant (l.962–987) imposes no constraint on AMI owner/subnet/SG/instance-profile baked into the LT. `Mechanism:` `NotResource: launch-template/*` + `ArnLike(ec2:LaunchTemplate=launch-template/*)` + `Bool(ec2:IsLaunchTemplateResource=true)` grants every EC2 resource type except the LT itself, gated only by "sourced unmodified from *some* LT." `Oracle:` SimulateCustomPolicy with attacker AMI ARN + foreign subnet ARN + the two context keys → predicted `explicitAllow` regardless of AMI owner/subnet. `Severity:` Medium (contingent on separate LT-management+tag grant). `Borderline Tier-2` (missing caveat).

**L7 — `CreateTags` `*/*` breadth + `ForAllValues` vacuous-truth.** `*/*` resource wildcard (l.599) is broader than the example's prose ("instances and volumes", l.552) implies — only safe because `ec2:CreateAction=RunInstances` bounds which resources are in play. `ForAllValues:StringEquals` on `aws:TagKeys` (l.671–709) evaluates **true on absent key** — correct here, but the page never flags it as a reusable trap; a reader generalizing it to *mandate* a tag's presence gets it backwards (presence needs a `Null` condition). `Tier-3` customer footguns.

### Lens B / R — PassRole & confused-deputy

**L5core (H3) — PassRole prefix-privesc.** Detailed above. `Oracle:` `iam:SimulatePrincipalPolicy` for the caller on `ec2:AssociateIamInstanceProfile` + `iam:PassRole` with a target role ARN that matches the prefix but belongs to a more-privileged team → `allowed` confirms prefix is the sole control. Example 2's `Resource:"*"` (l.1527–1534, no Condition) makes it strictly broader than Example 1 (tag-gated `department=test`). **Note the omitted knob:** `ec2:NewInstanceProfile` (list_ec2:4749) could constrain *which* profile is attached and is absent. `Compounding precondition:` caller with `iam:CreateRole`+`AttachRolePolicy` under the prefix can self-provision the privileged role. `Tier-2, High`.

**L6 — instance-profile-name vs role-name mismatch.** Doc (l.1516) warns to use the **role** name not the instance-profile name in PassRole Resource. If an admin keys the wildcard off profile naming it can fail **open** (over-match) or closed. AWS flagging it admits confusability. `Tier-3` footgun, Medium.

### Lens B/C — `ec2:SourceInstanceARN`

**L5b — SourceInstanceARN is provenance, not origin.** `Claim:` the binding (l.1587–1620, `ArnEquals ec2:SourceInstanceARN`) does not survive credential theft/replay — it encodes *which instance the creds were minted for*, not request network origin (list_ec2:10160). `Oracle:` reasoning-only (Simulator can't model stolen-cred population); closest is SimulatePrincipalPolicy with an attacker-chosen `ec2:SourceInstanceARN` ContextEntry → `allowed` shows it's a bare string match. `Severity:` High for the stolen-creds-replayed-off-box threat model; the prose "the other instance cannot perform any of these actions" risks over-trust. `Tier-3` footgun (prose literally accurate).

### Lens U / EE — guarantee-vs-enforcement, predictable name

**L9 (H6) — EBS root-volume encryption gap.** Detailed above; `ec2:Encrypted` absent from the `image` row. AWS discloses the gap in its own next sentence (l.468) → footgun, **not** Tier-2, but High-if-misread.

**L10 (H7) — `ec2:Owner:amazon` vs partner prose.** Fail-closed mismatch; whoAMI spoof **refuted** (owner server-resolved). `Tier-2 low`.

**L11 — hardcoded AMI IDs** (l.247–248): AMI-ID reuse-after-deregister not corpus-confirmed; treat as background, not a lead.

### Lens A — unscopable Describe oracle
`ec2:Describe*` on `Resource:"*"` (read-only sample) is account-wide and cannot be resource-scoped — expected EC2 behavior (Describe actions take no resource-level perms), noted as the standard enumeration oracle, not a defect of this page.

### Lens L — cost/DoS
**L8 — `PurchaseReservedInstancesOffering` on `*`** with no cost ceiling; a compromised principal holding this sample can incur large RI spend. Intra-account cost-DoS, Low-Medium.

### Null hypotheses (pages/surfaces checked, no lead)
- **Cross-account / cross-tenant (Lens A core):** N/A — this is a single-account IAM-authoring page; no multi-tenant fleet, no resource-by-ID cross-tenant surface. Checked all RunInstances/tag/IAM-role/IMDS sections.
- **Translation-layer / wire-protocol injection (Lens F), SSRF-via-dereferenced-URL (Lens G), uploaded-blob parsing (Lens Q):** N/A — page defines no field the service fetches/renders; checked every example. 
- **whoAMI predictable-AMI (Lens EE):** refuted for `ec2:Owner` (server-resolved); the real whoAMI class lives in customer code calling DescribeImages without `--owners`, not in this IAM condition.
- **`$Latest`/`$Default` in the launch-template section:** not present there (grep zero hits in `ec2-launch-templates.md`); the warning lives only in the IMDS "Important" callout (l.1690–1696) = H2. Do not source H2 to the LT section.

---

## Section 5 — Prioritized NEW/changed surface (where to concentrate fire)

1. **H1 (Spot fail-open, L1+L2)** — fastest, highest-confidence confirm; AWS pre-admits it; one tagged-vs-untagged `RunInstances` differential settles both. **Do first.**
2. **H3 (PassRole prefix-privesc, L5core)** — highest-impact (credential theft/privesc); SimulatePrincipalPolicy settles it read-only.
3. **H2 (ASG IMDSv2 bypass)** — AWS-acknowledged; confirm the bundle omits `autoscaling:LaunchTemplateVersionSpecified`.
4. **H4 (hop-limit raise)** — SimulateCustomPolicy one-shot.
5. **H5 (LT blast radius)** — SimulateCustomPolicy with attacker AMI/subnet.
6. **H6/H7** — docs-accuracy/guarantee; verify via SimulateCustomPolicy that the key isn't evaluated on `image`.
7. **H8** — report the dead slug as docs-hygiene.

**Reporting routing:** H1, H2, H3, H4 → **Tier-2 to `aws-security`** (AWS-authored sample/bundle defects or divergence from AWS's own recommended pattern). H5 borderline Tier-2 (missing caveat). H6/H7/L6/L7/L8/L5b → customer footguns / docs-accuracy. H8 → docs-hygiene.

---

## Section 6 — Oracles cheat-sheet (read-only, no resources created)

- **`iam:SimulateCustomPolicy`** — paste the sample statement verbatim; set `ActionNames`, `ResourceArns`, `ContextEntries` (e.g. `ec2:Owner=aws-marketplace`, `ec2:Encrypted=false`, `ec2:MetadataHttpPutResponseHopLimit=10`, `ec2:LaunchTemplate=…`, `ec2:IsLaunchTemplateResource=true`). Read `EvalDecision`.
- **`iam:SimulatePrincipalPolicy`** — for H3: caller principal vs `ec2:AssociateIamInstanceProfile` + `iam:PassRole` with a prefix-matching foreign role ARN.
- **Spot differential (H1)** requires a live `RunInstances` dry-run style confirm (tagged vs untagged) — Simulator alone will not model the resource-non-evaluation rule; flag H1 as the one lead needing a live-account `RunInstances` call (use synthetic/canary values; it is a create, so hunter must weigh the create-a-request step — prefer `--dry-run` where the differential is still observable, else teardown immediately).

---

## Section 7 — Severity rubric applied

- **Critical** = cross-account — none on this single-account page.
- **High** = privesc / documented-control-bypass intra-account — H1, H2, H3, (H4 Medium-High).
- **Medium** = missing-caveat / composition / ABAC-soundness — H5, L6, L7(part), L5b.
- **Low** = docs-accuracy / cost — H7, H8, L8.

---

## Section 8 — Handoff notes for the next agent

- **Ground truth paths:** page = `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md`; keys = `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (NOT `/work/aws-docs/list_ec2.md`, which doesn't exist). Live slug `list_ec2`; `list_amazonec2.html` is dead.
- **Resolved contradictions:** (a) the IAM-instance-profile-association actions **are** condition-scopable (detail rows l.4749/9401 carry `ec2:NewInstanceProfile` etc.) — the earlier "blank condition cell" read was the compact summary-table row, not the detail row; this *strengthens* H3 (AWS could have scoped and didn't). (b) `$Latest`/`$Default` warning is in the **IMDS** section (l.1690–1696 = H2), not the LT section.
- **Refuted leads (do not re-chase):** whoAMI/`ec2:Owner` spoof (server-resolved); `HttpTokens` case-sensitivity fail-open (API enum-normalizes before IAM eval — low-confidence refute, worth one live enum-casing probe only); omitted RunInstances resource types (fails *closed*, availability footgun not security); AMI-ID reuse (not corpus-confirmed).
- **The one lead needing live `RunInstances` (H1)** is the headline and the only one not settleable by Simulator — plan the canary/teardown carefully.
- **Cross-reference siblings:** this plan complements the broader EC2 IAM-surface plans in `/work/aws-docs/` (see memory index); it is the authoritative treatment of the **sample-policy gallery** specifically — the Spot resource-non-evaluation fail-open (H1) and the ASG `$Latest`/`$Default` IMDSv2 bypass (H2) are its unique contributions.
