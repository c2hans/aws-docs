# EC2 ENA Express — *Configure* page — Attack / Research Plan

> **Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express-configure.html
> (`.md` twin fetched online; offline mirror `docs/AWSEC2/latest/UserGuide/ena-express-configure.md`
> read in full — **byte-identical, 210 lines**, no security-relevant drift, 2026-10-15).
> **Method:** `security-questionbuilder` skill — boundary-first, documentation-only; nothing tested
> against a live account.
> **Prepared:** 2026-10-15.

---

## 0 — How to use this plan

This is the **page-level HOW-TO companion** of the parent plan
`ena-express-attack-research-plan.md`. The parent already OWNS the feature-wide analysis — the
three-write-path IAM condition-key parity gap (Attach / RunInstances / Modify), the
`EnaSrd`-value-blind condition surface, the both-ends-opt-in fallback semantics as a non-primitive,
the Flow-Logs/Traffic-Mirroring observability blind spot, the eligible-vs-actual TX live-migration
side-channel, the `check-ena-express-settings.sh` download-and-run supply chain, and the
cross-tenant null hypothesis (explicitly distinguished from EFA). **Do not re-derive any of those
here.**

The configure page is the actual procedural surface the parent summarized. It introduces two
things worth developing at mechanism level that the parent treated only in a single table row:

1. **A fourth, indirect SRD-enable path — the launch template** (page §"Configure ENA Express at
   launch"). This is the net-new HEADLINE: SRD transport mode can be *baked into a launch template*,
   and `CreateLaunchTemplate`/`CreateLaunchTemplateVersion` carry **zero** condition keys, so the
   value is unscopable at authoring time AND re-resolved at every future launch (late-binding).
2. **The `EnaSrdSpecification` nested struct mechanics** — TCP-SRD gates UDP-SRD, `EnaSrdUdpEnabled`
   defaults to `false`, partial-merge update semantics ("default to `false` *if it has never been
   set previously*"), and the Example-3 UDP-only disable — none of which have an IAM lever to
   separate TCP-SRD from UDP-SRD.

Each is cross-referenced to the parent; the parent's leads are not restated.

**Non-duplication / ownership map (read first):**

| Fact / lead | Owner | This plan |
|---|---|---|
| 3-write-path IAM parity gap (Attach/Run no `ec2:Attribute`; Modify has it); `EnaSrd`-value-blind | parent `ena-express-attack-research-plan.md` §5.1 | cross-ref; extend with the **4th (launch-template)** path |
| SRD observability blind spot (Flow Logs / Traffic Mirroring); TX live-migration side-channel; UDP MTU/PMTUD blackhole | parent §5.2 | cross-ref only |
| `check-ena-express-settings.sh` supply chain | parent §5.3 | cross-ref only |
| Generic `ModifyNetworkInterfaceAttribute` attribute-name-vs-value distinction + attachment-scoped silent-revoke lifecycle | `modify-network-interface-attributes-attack-research-plan.md` §5.7 | cross-ref only |
| EFA OS-bypass RDMA cross-tenant frame injection (also "SRD"-branded, **distinct device**) | `ec2-networking-attack-research-plan.md` Lead [3] | distinguished, not transferable |
| Generic LT `$Latest`/`$Default` late-binding privesc (IamInstanceProfile/UserData/AMI) | `ec2-fleet-instance-weighting-walkthrough-attack-research-plan.md` Area 2 | cross-ref; here applied to the **EnaSrd/transport-mode** field specifically |

**This plan OWNS:** the launch-template late-binding of SRD transport mode as a 4th enable path and
its total IAM-unscopability at authoring time; the attach-time config path mechanics (SRD binds at
*attach*, not at ENI create); the `EnaSrdSpecification`/`EnaSrdUdpSpecification` nested-struct
dependency + partial-merge update semantics + the TCP-cannot-be-separated-from-UDP IAM gap.

---

## 1 — Pentest objectives

1. **Prove the launch-template path extends the parent's §5.1 gap:** can a principal holding only
   launch-template write perms (`CreateLaunchTemplateVersion` + `ModifyLaunchTemplate`), with **no**
   `RunInstances`, no `ModifyNetworkInterfaceAttribute`, and no `AttachNetworkInterface`, set the SRD
   transport mode of every future instance launched from that template — and is that value
   IAM-unscopable at authoring time? (Area 1.)
2. **Confirm attach-time is the binding point:** SRD is settable at `AttachNetworkInterface` on an
   ENI that could not carry it at `CreateNetworkInterface`; characterize detach/reattach as a reset
   path. (Area 2.)
3. **Resolve the nested-struct dependency enforcement:** is "UDP-SRD requires TCP-SRD" enforced
   server-side or console-UI-only; does a partial modify preserve or reset the un-named sub-field;
   and is there any IAM key that separates TCP-SRD from UDP-SRD? (Area 3.)
4. **Close the configure-page-specific null hypotheses** (no IDOR / SSRF / upload surface on this
   how-to page). (Area 5.)

---

## 2 — Components, assets, and design (delta vs parent)

The parent §2 holds. The configure page adds the concrete **four** write surfaces and their console
equivalents:

- **`attach-network-interface --ena-srd-specification`** — sets `EnaSrdSpecification` *as the ENI is
  attached*. Console flows: "Manage ENA Express for a network interface", "…for an instance", and
  "…when you attach a network interface" (the last offers the Enable checkboxes in the Attach
  dialog). Confirms SRD binds to the **attachment**, and an ENI with `Status: Available`
  (unattached) has no SRD setting to manage — the dialog action is hidden for unattached ENIs.
- **`modify-network-interface-attribute --ena-srd-specification`** — post-hoc update on a live
  attachment; the only path with an attribute-name condition key (parent §5.1). Example 3 shows a
  **UDP-only** partial update.
- **`RunInstances`** via the **launch instance wizard** → *Advanced network configuration* — sets
  `NetworkInterfaces[].EnaSrdSpecification` at launch.
- **Launch template** (`CreateLaunchTemplate` / `CreateLaunchTemplateVersion`, consumed by
  `RunInstances`, EC2 Fleet, Spot Fleet, Auto Scaling) → *Network settings → Advanced network
  configuration* — bakes `EnaSrdSpecification` into template data for **every future launch**.

**Resource/identifier shape:** `EnaSrdSpecification { EnaSrdEnabled: bool, EnaSrdUdpSpecification {
EnaSrdUdpEnabled: bool } }` — a 2-boolean nested struct. In a launch template it lives in the
template's network-interface block; at runtime it lands on
`NetworkInterfaces[].Attachment.EnaSrdSpecification` (attachment-scoped, dropped on detach/terminate).

```
  Four write paths → one attachment-scoped boolean-pair:

  CreateNetworkInterface ──(cannot set EnaSrd)──► ENI (no SRD)
                                                    │
  AttachNetworkInterface ──(--ena-srd-specification)┤
  RunInstances (wizard)  ──(NetworkInterfaces[].EnaSrdSpecification)┤
  Launch Template  ──bake into templateData──► RunInstances/Fleet/ASG ─┤──► Attachment.EnaSrdSpecification
  ModifyNetworkInterfaceAttribute ──(post-hoc)──────────────────────────┘      (read via Describe*)

  IAM condition surface:  Attach / Run / Create-LT / Create-LT-Version = NO ec2:Attribute, value-blind
                          Modify = ec2:Attribute (name only, still value-blind)
```

---

## 3 — API / interface inventory (configure-page delta)

| Name | Mutating | Sets EnaSrd | Condition keys (list_ec2.md) | Notes |
|---|---|---|---|---|
| `AttachNetworkInterface` | yes | at attach | tag/ENI/Subnet/VPC/AZ/Region — **no `ec2:Attribute`** (parent line 4861) | binding point for an ENI that had none |
| `RunInstances` (wizard) | yes | at launch | RequestTag/TagKeys/ENI/Subnet/VPC/AZ/`ec2:LaunchTemplate`/`ec2:IsLaunchTemplateResource` — **no `ec2:Attribute`** (parent line 9595) | wizard Advanced network config |
| **`CreateLaunchTemplate`** | yes | into template data | **BLANK — zero condition keys** (list_ec2.md line 565–566) | **net-new: value unscopable at authoring** |
| **`CreateLaunchTemplateVersion`** | yes | into template data | **BLANK — zero condition keys** (list_ec2.md line 570–571) | **net-new: new version can introduce/flip SRD** |
| `ModifyLaunchTemplate` | yes | selects default version | field-name-only (list_ec2.md line 3858–3859) | picks which (possibly SRD-on) version is `$Default` |
| `ModifyNetworkInterfaceAttribute` | yes | post-hoc | `ec2:Attribute` + name (parent line 8969) | Example 3 = UDP-only disable |
| `DescribeInstances` / `DescribeNetworkInterfaces` | no | reads | region-only, unscopable (parent) | read oracle — parent owns |
| `CreateNetworkInterface` | yes | **no** (EnaSrd not accepted) | ENI/Region | SRD not settable at ENI-create |

**Hidden-knob / value-key sweep (re-confirmed on this pass):** `grep -ni
"enasrd\|ec2:srd\|ena express" list_ec2.md` → **0 hits** across all 10,190 lines. No condition key
of any name inspects the SRD boolean value or distinguishes TCP-SRD from UDP-SRD, and
`CreateLaunchTemplate`/`...Version` have no condition keys at all. The launch-template is therefore
the **least-scopable** of the four write paths.

---

## 4 — Recommended areas of focus (per firing lens)

### 4.1 — Area 1 (HEADLINE): Launch-template late-binding of SRD transport mode — the 4th enable path (Lens B / E / X / S) — **Severity: Medium**

**Claim.** A principal who can only *author/update a launch template* — `CreateLaunchTemplateVersion`
(+ `ModifyLaunchTemplate` to set it `$Default`), with **no** `RunInstances`, **no**
`AttachNetworkInterface`, **no** `ModifyNetworkInterfaceAttribute` — controls the ENA Express /
SRD transport mode of **every future instance** launched from that template (directly, or via EC2
Fleet / Spot Fleet / Auto Scaling that reference it), and that value is **unscopable in IAM at
authoring time**. This extends the parent's three-write-path parity gap (§5.1) to a fourth,
*indirect, time-decoupled* path that the parent noted only as "wizard + launch template" inside the
`RunInstances` row.

**Mechanism (doc evidence).**
- Configure page §"Configure ENA Express at launch → **Launch template**": *"You can configure ENA
  Express at launch when you use a launch template … expand the **Network settings** section and
  review the **Advanced network configuration**."* → `EnaSrdSpecification` is template data.
- `list_ec2.md` line 565–566 (`CreateLaunchTemplate`) and 570–571 (`CreateLaunchTemplateVersion`):
  **Condition key cell is empty** — no `ec2:Attribute`, no tag, no network-interface key inspects
  the template body. The entire `EnaSrdSpecification` sub-struct inside the template is invisible to
  IAM at create time.
- Parent §5.1: the consuming `RunInstances` `network-interface*` row (line 9595) also carries **no
  `ec2:Attribute`**, so nothing re-inspects the SRD value when the template is resolved into a launch.
- Late-binding: a template referenced as `$Latest`/`$Default` re-resolves on every launch (corpus
  pattern — `ec2-fleet-instance-weighting-walkthrough` Area 2); `ModifyLaunchTemplate` chooses which
  version is `$Default` with only a field-name key (line 3858–3859), so flipping the default version
  to an SRD-on one silently changes the transport mode of all future `$Default` launches.

**Confirm/Refute oracle.** Fully resolvable from the IAM reference for the *authoring-unscopable*
half (done — `CreateLaunchTemplate*` condition cells are blank). Live confirmation (out of scope
here): under a role allowed `CreateLaunchTemplateVersion` + `ModifyLaunchTemplate` but **denied**
`RunInstances`/`AttachNetworkInterface`/`ModifyNetworkInterfaceAttribute`, create a template version
with `EnaSrdEnabled=true` in Advanced network config, set it `$Default`, have a *separate* launcher
role (or a Fleet/ASG) launch from `$Default`, then read back `Attachment.EnaSrdSpecification` via
`DescribeNetworkInterfaces`. SRD enabled on the launched attachment proves the LT-editor set
transport mode without holding any of the three direct SRD-write actions, and that an attribute-name
Deny on `ModifyNetworkInterfaceAttribute` (the parent's §5.1 "control") does not cover this path.

**Preconditions / cost.** Zero privilege to discover (IAM-reference read). To exploit: only
launch-template write perms, which are routinely granted to CI/CD, platform, and
"infrastructure-as-code" roles that are *not* thought of as holding network-transport authority.

**Severity: Medium** — policy-completeness / least-privilege footgun, same class as the parent's
§5.1 but with a wider and less-obvious principal set (template editors) and a time gap between the
grant-equivalent act (editing the template) and the effect (a future launch), which also weakens
attribution. Not a cross-tenant break. In scope as an AWS-doc-surfaced gap only to the extent a
customer builds a "no ENA Express" compliance control on the attribute-name Deny; the real fix is a
tag/action-scoped Deny on the launch path plus controlling template-version authorship.

> Cross-ref: generic `$Latest`/`$Default` late-binding of IamInstanceProfile/UserData/AMI is owned
> by `ec2-fleet-instance-weighting-walkthrough-attack-research-plan.md` Area 2 — **not restated**;
> this area owns only the application of that pattern to the `EnaSrdSpecification`/transport-mode
> field, which no sibling has covered.

### 4.2 — Area 2: Attach-time is the binding point; detach/reattach as a reset path (Lens X / S) — **Severity: Low**

**Claim.** SRD cannot be set at `CreateNetworkInterface` (parent confirmed the field is not
accepted) but **is** set at `AttachNetworkInterface` (configure page CLI Examples 1–2:
`attach-network-interface … --ena-srd-specification 'EnaSrdEnabled=true[,EnaSrdUdpSpecification=…]'`).
Because the setting is **attachment-scoped**, detaching and reattaching an ENI resets it to the
attach-time spec (or to default-off if omitted), independent of any prior `ModifyNetworkInterfaceAttribute`
state.

**Mechanism (doc evidence).** Configure page: three console attach/manage flows + two attach CLI
examples; the "Manage ENA Express" action is hidden for an unattached (`Available`) ENI
("If the network interface you selected is not attached to an instance, this action does not appear
in the menu."). `list_ec2.md` line 4861 (`AttachNetworkInterface`): no `ec2:Attribute`.

**Confirm/Refute oracle.** Resolvable from docs for the scoping half. Live (out of scope): set SRD
via `ModifyNetworkInterfaceAttribute`, detach the ENI, reattach via `AttachNetworkInterface`
*without* `--ena-srd-specification`, then `DescribeNetworkInterfaces` — if SRD reverts to off, the
attach-time spec (not the prior modify) is authoritative, confirming detach/reattach as a
state-reset that an attribute-name Deny on Modify neither sees nor prevents.

**Severity: Low** — operational / policy-completeness nuance; reinforces Area 1 and parent §5.1
(three/four value-blind write paths), no new boundary crossed. Attachment-scoped silent-revoke
lifecycle depth is owned by `modify-network-interface-attributes-attack-research-plan.md` §5.7.

### 4.3 — Area 3: `EnaSrdUdpSpecification` nested-struct dependency, partial-merge update, and the TCP-vs-UDP IAM gap (Lens U) — **Severity: Low / Informational**

**Claim(s).**
- (a) **TCP-SRD gates UDP-SRD.** The page repeats, in every console flow: *"When ENA Express is
  enabled, you can configure UDP settings."* → UDP-SRD is only configurable when TCP-SRD is on. Is
  this enforced server-side at `AttachNetworkInterface`/`ModifyNetworkInterfaceAttribute`/launch, or
  only in the console UI? i.e. does a request with `EnaSrdUdpEnabled=true` while `EnaSrdEnabled` is
  unset/`false` **reject** (ValidationException) or **silently honor / silently drop** it?
- (b) **Partial-merge update semantics.** Modify Example 1 note: *"allows `EnaSrdUdpEnabled` to
  default to `false` **if it has never been set previously**"* — implying modify does a **partial
  merge** of the sub-struct, not a full replace, so a modify naming only `EnaSrdEnabled` **preserves**
  a previously-set `EnaSrdUdpEnabled=true`. An operator who toggles only TCP-SRD may believe they
  reset UDP-SRD when they did not (integrity-of-intent).
- (c) **Example 3 UDP-only disable** (`--ena-srd-specification 'EnaSrdUdpSpecification={EnaSrdUdpEnabled=false}'`)
  mutates one leaf of the struct without naming the other — confirming independent per-leaf writes.
- (d) **No IAM key separates TCP-SRD from UDP-SRD.** Both leaves live inside the single value-blind
  `EnaSrdSpecification`; `grep enasrd list_ec2.md` = 0. A defender who wants "TCP-SRD allowed, UDP-SRD
  forbidden" (e.g. because a UDP middlebox/IDS can't follow SRD UDP reassembly) **cannot express it**
  in IAM at all — the `ec2:Attribute` name on Modify is `enaSrdSpecification` for the whole struct.

**Mechanism (doc evidence).** Configure page console steps (lines 25/27, 45/47, 61/63) + CLI
Examples 1–3 + the PowerShell `Get-EC2NetworkInterface … EnaSrdUdpEnabled` read-back projections.

**Confirm/Refute oracle.** (a) Submit `modify-network-interface-attribute --ena-srd-specification
'EnaSrdUdpSpecification={EnaSrdUdpEnabled=true}'` on an attachment with `EnaSrdEnabled=false`; a
`ValidationException` = server-side gate (fail-closed), a 200 with UDP silently off = silent-drop,
a 200 with UDP on = dependency not enforced. (b) Set both true, then modify naming only
`EnaSrdEnabled=true`, read back `EnaSrdUdpEnabled` — unchanged = partial-merge confirmed. (d)
Resolvable from the IAM reference (no TCP/UDP-separating key exists).

**Severity: Low / Informational** — doc-vs-enforcement precision + an expressivity gap in the IAM
condition surface; no cross-party impact. Worth filing (d) as a feature/condition-key gap if a
customer relies on IAM to permit one SRD transport sub-mode but not the other.

### 4.4 — Area 4: cross-refs (not developed here)

- **SRD observability blind spot** (Flow Logs / Traffic Mirroring see only the reassembled logical
  flow), **TX eligible-vs-actual live-migration side-channel**, **UDP MTU/PMTUD blackhole** →
  parent §5.2. The UDP MTU caveat is directly relevant to Area 3's "enable UDP-SRD" step but the
  analysis is the parent's.
- **`check-ena-express-settings.sh` download-and-run supply chain** → parent §5.3.
- **Unscopable `Describe*` read oracle** for reading any ENI/instance SRD state region-wide →
  parent §5.1 "Also test".

---

## 5 — Threat-model test objectives (priority order)

1. **[Medium — doc half already settled]** Area 1: prove the launch-template path sets SRD transport
   mode with only `CreateLaunchTemplateVersion`+`ModifyLaunchTemplate` and no direct SRD-write action;
   confirm `CreateLaunchTemplate*` condition cells are blank (done) and the launched attachment shows
   SRD on.
2. **[Low]** Area 3(a)/(b): server-side vs UI-only enforcement of the TCP-gates-UDP dependency, and
   partial-merge preservation of the un-named sub-field.
3. **[Low]** Area 2: detach/reattach-without-spec resets SRD regardless of prior Modify state.
4. **[Null-closing]** Area 6 below — document absence of IDOR/SSRF/upload surface on this page.

---

## 6 — Out of scope / hard stops

- **AWS backbone + Nitro/ENA SRD termination** = service plane; any identity/credential/packet from
  it is a **HARD STOP** (parent §7). No such surface is reachable via any configure-page interface.
- **EFA OS-bypass RDMA** is a different, also-"SRD"-branded feature — owned by
  `ec2-networking-attack-research-plan.md` Lead [3]; **not transferable** to ENA Express.
- Generic launch-template `$Latest`/`$Default` privesc via IamInstanceProfile/UserData/AMI →
  `ec2-fleet-instance-weighting-walkthrough` Area 2.
- No DNS/port/subdomain enumeration; control-plane + HTTP/application layer only; read-only PoC /
  dummy values only.

---

## 7 — Null hypotheses and documentation gaps (configure-page-specific)

| Hypothesis | Verdict | Pages / evidence checked |
|---|---|---|
| `CreateLaunchTemplate`/`...Version` carry a condition key that scopes the SRD/network-interface value in template data | **REFUTED** — condition-key cells are **blank** (unscopable at authoring) | `list_ec2.md` lines 565–566, 570–571 |
| Any IAM condition key distinguishes TCP-SRD from UDP-SRD (or inspects the EnaSrd value) | **REFUTED** — 0 hits for `enasrd`/`ec2:srd`; single value-blind `enaSrdSpecification` attribute name on Modify only | `list_ec2.md` full-file grep |
| SRD is settable at `CreateNetworkInterface` | **REFUTED** — binds at `AttachNetworkInterface`/launch only; CreateNetworkInterface does not accept EnaSrd | parent + configure-page CLI examples |
| TCP-gates-UDP dependency enforcement point (server vs console) | **DOC-GAP — confirm live** (page states the dependency in UI steps; API-ref/`list_ec2` silent on reject-vs-drop) | configure-page console steps + CLI Example notes |
| Modify does a partial merge (preserves un-named sub-field) | **STRONGLY IMPLIED, confirm live** — "default to `false` *if it has never been set previously*" | configure-page Modify Example 1 note |
| IDOR / cross-tenant surface on the configure page | **N/A (null)** — all four write paths and both Describe reads act on the caller's own `eni-`/`i-`/`eni-attach-` resources; attachment-scoped; no tenant/account/resource id consumed from an attacker-controlled field; no "revealed after a step" data | configure page read in full (210 lines, both console + CLI + PowerShell + launch sections) |
| SSRF (Lens G) | **N/A (null)** — no field on this page is a URL/host the service dereferences; the only links are doc cross-references and the GitHub helper script (parent §5.3), not server-side fetched inputs | configure page in full |
| Upload / rich-content (Lens Q) | **N/A (null)** — no file/blob/image/attachment input; `EnaSrdSpecification` is a 2-boolean struct | configure page in full |
| Prompt injection (Lens K), KMS (H), OAuth (J), attestation (W), token-validation (FF) | **N/A (null)** — no LLM/agent, no KMS key field, no 3P OAuth, no attestation gate, no JWT on this surface | configure page in full |

**Verification note:** online `.md` twin and offline mirror of `ena-express-configure.md` are
byte-identical (210 lines) as of 2026-10-15; `list_ec2.md` read via targeted offline grep (the
authoritative `docs/service-authorization/latest/reference/list_ec2.md`, 10,190 lines).

---

*Prepared with the `security-questionbuilder` skill, documentation-only, boundary-first. Companion
to `ena-express-attack-research-plan.md` (parent) — this plan owns only the launch-template
late-binding path, the attach-time binding mechanics, and the `EnaSrdSpecification` nested-struct
semantics; all other ENA Express leads are the parent's.*
