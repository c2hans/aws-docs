# Share a Placement Group (`share-placement-group`) — Attack Research Plan (PAGE-LEVEL CHILD)

Source of leads: `AWSEC2/latest/UserGuide/share-placement-group.html` (the target page; offline
`docs/AWSEC2/latest/UserGuide/share-placement-group.md` present, 69 lines; online fetched 2026-10-15 —
content consistent, no security-relevant drift) + the IAM Service Authorization Reference
`list_ec2.md` (`PutResourcePolicy`/`DeleteResourcePolicy`/`GetResourcePolicy` rows, offline, targeted grep,
lines 9821/9858/9901) + `list_ram.md` + `ram/latest/userguide/shareable.md` (line 174) +
`ram/latest/userguide/doc-history.md` (line 57). Status: **documentation-derived hypotheses only;
nothing tested against a live account.**

## Relationship to the HUB plan — READ FIRST
This is the **page-level deep-dive child** of `placement-groups-attack-research-plan.md` (the HUB) for the
single `share-placement-group` page. It is the sibling of `create-placement-group-attack-research-plan.md`,
`delete-placement-group-attack-research-plan.md`, and `placement-strategies-attack-research-plan.md`.
It does **not** restate the hub's cross-cutting surface — it cross-references and **explicitly defers**:

- **Cross-account co-residency in a shared `cluster` PG + topology `nn-` side-channel confirmation
  (CROWN JEWEL / HARD STOP)** → **hub Area 1** and the `ec2-instance-topology` plan (A6). This child owns the
  *grant* and *revoke* mechanics that create and persist that adjacency; the **confirmation** step
  (reading a shared `nn-` node) belongs to the hub.
- **The IAM-backbone condition-key map** (`ec2:PlacementGroupStrategy`/`PlacementGroupName` existence,
  the 0-org-key fact) → **hub Area 4**. This child owns only the *resource-policy actions'* specific
  condition-key coverage and the grantee-scoping gap.
- **`spread`/`partition` "physical isolation" = availability-not-security framing** → **hub Area 5** /
  `placement-strategies` child.
- **`DescribePlacementGroups` unscopable read oracle** → **hub Area 3** (this child adds the *resource-policy*
  read oracle `GetResourcePolicy`).
- **Predictable-name land-grab / name-only-condition footgun** → **hub Area 6**.
- **Create-time parameters (`ParentGroupId`, reserved `LinkedGroupId`/`Operator`, tag-on-create self-widening)**
  → `create-placement-group` child.

**Net-new surface this child OWNS** (none of it is developed in the hub, which was built from the 6 UG pages +
`list_ec2`/`list_ram`/`list_outposts` and treated the sharing seam only at summary level): the **two sharing
paths** this page documents (native EC2 resource-based policy via `ec2:PutResourcePolicy` **vs** AWS RAM
resource shares), the **grantee/destination-scoping gap** on the resource-policy actions, the **"Required
permissions" block as a shipped Lens-R artifact** that lists only the native actions and omits all RAM
permissions, the **unshare-does-not-evict revocation-completeness** facts (instances + capacity reservations
disassociated but keep running / remain available), the **native-grant-vs-RAM-invitation acceptance
asymmetry**, the **consumer-side isolation claim** ("can't view or modify instances/CRs you don't own"),
the **name-vs-ID naming requirement** for consumer launches, and the **AZ-ID co-residency-targeting
precursor** note.

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- `iam:SimulateCustomPolicy`/`SimulatePrincipalPolicy` is the safe first oracle for every condition-key / scoping claim (no resources touched). Escalate to a scoped live call only with synthetic canary data under a role holding **exactly** the artifact under test (never the over-privileged tester). **Treat `DryRun` as caller-IAM-only, NOT an ownership/grantee-existence oracle** — it is evaluated before resource resolution.
- Cross-account leads need a **two-account (ideally three-account) canary**: Owner `O`, intended consumer `T`, and a third account `C` that `O` never shared with. The sharpest oracles below turn on what `C` (or a non-member org account) can do.
- **HARD STOP:** the moment a share (or a *survived* share after revoke) is shown to produce **confirmed cross-account physical adjacency** (a `nn-` topology node shared with a foreign account), or any identity/credential/ARN/account belonging to AWS's own placement engine / service plane appears — stop, preserve evidence, flag for AWS-Security disclosure, and hand the confirmation step to **hub Area 1**.

## 1. Pentest Objectives (sharing-action-scoped)
1. Prove an admin who grants `ec2:PutResourcePolicy` on a placement group **cannot** bound *who* the holder shares it with — no destination-account / OU / org condition key exists — so the holder can share a `cluster` PG to **any** AWS account (sanctioned cross-account co-residency precursor; chains to hub Area 1).
2. Attach a resource-based policy (native path) that grants a **non-existent / non-member / foreign-org** account or OU and observe whether `PutResourcePolicy` validates grantee existence/membership (Lens AA grantee-validation).
3. Determine whether the **native `ec2:PutResourcePolicy` path bypasses the RAM invitation/acceptance handshake** that the page says an out-of-org consumer must complete — i.e. can `O` unilaterally grant `C` access to launch into a shared PG with no acceptance by `C`?
4. Show that **unsharing does not evict already-co-resident consumer instances** ("they continue to run") → cross-account physical adjacency established under a share **survives** `DeleteResourcePolicy` / RAM unshare (revocation incompleteness).
5. Read the sharing policy of **any** placement group via `GetResourcePolicy` despite a tag/name Deny (resource-policy read oracle) → enumerate cross-account grants.
6. Break the consumer-side isolation claim — a consumer in a shared PG viewing/modifying the **owner's** or a **sibling consumer's** instances/capacity reservations ("you can't view or modify … not owned by you").
7. Demonstrate the "Required permissions" block (Lens R artifact) is incomplete/mis-scoped: a principal holding exactly `ec2:PutResourcePolicy`+`ec2:DeleteResourcePolicy` either cannot drive the RAM flow the page describes (fail-closed → pushes operator to broader grant), or the two paths reach the same cross-account exposure with divergent condition-key / audit coverage (Lens X).

## 2. Components, Assets, and Design (sharing path only)

**What this page adds to the PG model.** A placement group (Region+Account-scoped, name-identified,
ARN `arn:${Partition}:ec2:${Region}:${Account}:placement-group/${PlacementGroupName}`) can be made
reachable by **other accounts** so those accounts' principals can **launch instances into it** (and reserve
capacity in it). For a `cluster` PG this means the consumer's instances become **physically co-resident on
shared hardware across an account boundary** — the asset of highest interest and the reason this page exists.

**Two distinct sharing paths (the central structural fact).**
1. **Native EC2 resource-based policy** — `ec2:PutResourcePolicy` "attach[es] an IAM policy that enables
   cross-account sharing to a resource"; `ec2:GetResourcePolicy` reads it; `ec2:DeleteResourcePolicy`
   "remove[s]" it. These are the **only** two actions in the page's "Required permissions" block.
2. **AWS RAM resource share** — the body of the page describes sharing by adding the PG to a RAM resource
   share (`ram:CreateResourceShare` / `AssociateResourceShare*`), with an invitation/acceptance handshake
   for accounts **outside** the owner's organization. RAM confirms placement groups are shareable as
   `ec2:PlacementGroup` (since 2022-11-08, `ram/shareable.md:174`), "**Can share with any AWS account**,
   both within and outside your organization."

The page presents these as one feature but they are two control planes with different authz grain and
different consent semantics. **Neither path has an EC2 condition key that bounds the destination** — EC2
has **zero** `aws:PrincipalOrgID`/`aws:ResourceOrgID`/`…OrgPaths` keys (grep of full `list_ec2.md` = 0), and
the resource-policy actions carry no account/OU/principal condition key (see Area 1).

**Ownership / enforcement reality.**
- You may share only a PG you **own**; you cannot re-share a PG shared *to* you.
- Shared partition/spread PGs keep their 7-partition / 7-instance-per-AZ limits.
- Consumers "**can't view or modify instances and capacity reservations** that are associated with a shared
  placement group but **not owned by** you" — an isolation guarantee enforced by the service plane, not by
  any customer-visible mechanism.
- The ARN embeds the **owner account ID** — the page tells consumers to read it to identify the owner
  (acknowledged, by-design disclosure; not a finding on its own).
- Unshare is reversible-looking but **leaves running instances in place** (Area 4).

```
  Owner account O                                      Consumer account T (and foreign C?)
  ┌───────────────────────────┐                        ┌───────────────────────────────┐
  │ owns cluster PG "pg-hpc"  │                        │ RunInstances(PlacementGroupId) │
  │                           │                        │  → instance co-resident on     │
  │ PATH 1 ec2:PutResourcePolicy ─ attach rbp ───────▶ │     shared hardware with O     │
  │   (no grantee condition key)                       │                               │
  │ PATH 2 RAM resource share ─ invite ──▶ accept ───▶ │  (acceptance only out-of-org) │
  └───────────────────────────┘                        └───────────────────────────────┘
            │ DeleteResourcePolicy / RAM unshare                 ▲
            └── consumer can no longer LAUNCH … but ─────────────┘
                already-launched instances KEEP RUNNING (co-residency survives revoke)
                            │
                            ▼  confirm nn- shared node  → HARD STOP → hub Area 1 / ec2-instance-topology A6
```

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Low-priv principal in O holding `ec2:PutResourcePolicy` on a PG | Arbitrary external account / OU / org as grantee | Resource-based policy document (no IAM key bounds the grantee) | A share is created to an account the granting admin's policy never intended (e.g. account `C`); `SimulateCustomPolicy` shows no condition can deny it |
| Owner O | Non-existent / non-member / foreign-org grantee | `PutResourcePolicy` / RAM associate | Grant accepted for a grantee that fails existence/membership validation (Lens AA) |
| Owner O (native path) | Consumer C, no acceptance step | `ec2:PutResourcePolicy` naming C directly | C can launch into the shared PG with **no invitation accepted** — unilateral cross-account grant |
| Consumer T/C launched into shared `cluster` PG | Physical host adjacency to O's instances | EC2 placement engine | A `nn-` topology node shared across the account boundary (**HARD STOP → hub Area 1**) |
| Consumer T/C **after** O unshares | Same physical adjacency | Residual running instance (disassociated but running) | Consumer instance still runs co-resident after `DeleteResourcePolicy`/unshare |
| Principal with `ec2:GetResourcePolicy` on `*` | Any PG's sharing policy | Resource-type-optional read action | Reading the resource policy (grantee list) of a PG the caller does not own / is tag-Denied |
| Consumer in shared PG | Owner's / sibling-consumer's instances & CRs | `Describe*` / topology | Viewing or modifying an instance/CR "not owned by you" (breaks the stated isolation) |
| **Any customer surface** | **AWS placement-engine / service plane** | — | **Hard stop** — any AWS-owned identity/ARN/account |

## 4. API / Interface Inventory

| Name | Mutating | Ext-facing | Functionality | Authorized callers | Notes |
|---|---|---|---|---|---|
| `ec2:PutResourcePolicy` (on `placement-group`) | **Yes** (Permissions management, Write) | Yes | Attach resource-based policy enabling cross-account sharing | PG owner | `list_ec2:9901`. Resource type **NOT `*required`** (no asterisk). Keys: `aws:ResourceTag`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region`, `ec2:ResourceTag`. **No grantee/account/OU/org key.** |
| `ec2:DeleteResourcePolicy` (on `placement-group`) | **Yes** (Permissions mgmt, Write) | Yes | Remove the sharing resource policy | PG owner | `list_ec2:9821`. Resource type **NOT `*required`** → wildcard-usable (parity concern, Area 5). Same keys as Put. |
| `ec2:GetResourcePolicy` (on `placement-group`) | No (Read) | Yes | Read the sharing resource policy | — | `list_ec2:9858`. Resource type **NOT `*required`** → `Resource:"*"` read oracle of any PG's grantee list. |
| `ram:CreateResourceShare` / `AssociateResourceShare` / `…Permission` | Yes | Yes | Add PG to a RAM share; invite consumers | Owner | **Absent from the page's "Required permissions" block** (Area 3). PG = `ec2:PlacementGroup` shareable type (`ram/shareable.md:174`). |
| RAM invitation accept (`ram:AcceptResourceShareInvitation`) | Yes | Yes | Out-of-org consumer accepts | Consumer | Page: external-org consumer "receives an invitation … can access … after accepting." In-org = auto. **Does the native Path 1 skip this? (Area 2b)** |
| `ec2:RunInstances` (consumer, `--placement GroupId=…`) | Yes | Yes | Launch into shared PG | Consumer | Page: via CLI must use **ID, not name**; name only if owner (Area 5 naming divergence). |
| `DescribePlacementGroups` / `DescribeInstances` (consumer) | No | Yes | View membership | — | Isolation claim "can't view … not owned by you" (Area 6); hub Area 3 owns the unscopable-read depth. |

## 5. Recommended Areas of Focus (one block per firing lens)

### Area 1 — The sharing grant has NO grantee/destination condition key (HEADLINE; Lens S + U + AA)
**Background.** The page lets an owner share a PG "with specific AWS accounts inside or outside of its
organization," "an organizational unit," or "its entire organization." The *only* IAM actions required are
`ec2:PutResourcePolicy` / `ec2:DeleteResourcePolicy`.
**Security Concern.** `list_ec2` gives `PutResourcePolicy` on `placement-group` exactly these condition keys:
`aws:ResourceTag/${TagKey}`, `ec2:PlacementGroupName`, `ec2:PlacementGroupStrategy`, `ec2:Region`,
`ec2:ResourceTag/${TagKey}` — all of which scope **which PG** is shared, **none** of which scope **to whom**.
There is **no** `aws:PrincipalOrgID`/`aws:ResourceOrgID`/account/OU/principal condition key on the action
(and EC2 defines **zero** org keys corpus-wide — grep = 0). The resource policy document's `Principal` is
request-body content, not an IAM-evaluable key. ⇒ an admin who grants a team `ec2:PutResourcePolicy` on a PG
(even tightly scoped to one `ec2:PlacementGroupName`) **cannot** prevent that team from sharing it to **any**
external account — including a `cluster` PG, which turns the grant into a sanctioned cross-account
**co-residency** primitive. RAM corroborates: placement groups "Can share with **any** AWS account"
(`shareable.md:174`). "within your organization" is a RAM/SCP boundary only, never an EC2 resource-level one.
**High-level Test Scenarios.**
- Claim: *A policy allowing `ec2:PutResourcePolicy` on `placement-group/pg-hpc` cannot restrict the share
  destination.* → Oracle: `iam:SimulateCustomPolicy` with every plausible condition (`aws:PrincipalOrgID`,
  a fabricated account key) shows none constrains the grantee; a live `PutResourcePolicy` naming account `C`
  (outside O's org) under that scoped role succeeds. Severity: **High** (enables cross-account co-residency
  reachable from a narrowly-scoped grant; **Critical** once adjacency confirmed → hub Area 1 HARD STOP).
- Claim: *The only way to bound sharing is an SCP / `ram:` org-sharing-disable toggle, not an EC2 identity
  policy.* → Oracle: confirm `ram/security-disable-sharing-with-orgs.md` and SCP are the sole controls;
  document that an EC2-only admin has no lever.
**Doc evidence:** page §"Required permissions" + §"Placement group sharing"; `list_ec2:9901`; `shareable.md:174`.
**Severity-if-true:** High → Critical (co-residency). AWS-owned framing gap (Lens U): the page promises granular
"specific accounts / OU / org" targeting with no note that EC2 IAM cannot enforce any of it.

### Area 2 — Grantee validation + native-grant-vs-RAM-acceptance asymmetry (Lens AA + X)
**Background.** The page: for an in-org consumer, "sharing within your organization is enabled, and consumers
in your organization are granted access"; for an out-of-org account, "the AWS account owner **receives an
invitation** … can access the shared placement group **after accepting**."
**Security Concern (2a — grantee validation).** When a resource-based policy (Path 1) or RAM association names
a **non-existent, non-member, or foreign-org** account/OU, is the grantee validated for existence/membership
at grant time, or accepted blindly (the EIP-transfer / `launchPermission Add OrganizationArn` shape where
unvalidated grantee targets were accepted)? An accepted-but-unvalidated grant is a latent mis-share and a
pre-registration primitive (a future account id claimed early).
**Security Concern (2b — acceptance bypass, higher value).** The invitation/acceptance step is the
**consumer's consent gate** for out-of-org sharing. Path 2 (RAM) enforces it. Does **Path 1** (native
`ec2:PutResourcePolicy` naming the consumer principal directly) **skip** it — granting `C` the ability to
launch into O's shared `cluster` PG with **no acceptance by C and no acceptance by O's org admin**? If so, the
two paths diverge on consent (Lens X twin-parity): the documented "they must accept" guarantee holds only for
the RAM path, and the native resource-policy path is a quieter unilateral grant.
**High-level Test Scenarios.**
- Oracle (2a): `PutResourcePolicy` / RAM-associate a grantee account that does not exist (or an OU in a
  different org) → does it return success or a validation error? Success = unvalidated grantee (Medium–High).
- Oracle (2b): O attaches a native resource policy naming `C` (out-of-org). Without `C` performing any RAM
  accept, can `C` `RunInstances --placement GroupId=pg-…` into the shared PG? A successful launch = acceptance
  bypass / unilateral cross-account grant (**High**).
**Doc evidence:** page §"Placement group sharing" (invitation/accept) vs §"Required permissions" (native actions).
**Severity-if-true:** 2b High (consent-gate bypass + cross-account co-residency); 2a Medium–High.

### Area 3 — "Required permissions" is a shipped artifact that omits the RAM path (Lens R + U)
**Background.** The page's "Required permissions" block prints exactly two actions: `ec2:PutResourcePolicy`,
`ec2:DeleteResourcePolicy`. The rest of the page says sharing is performed by **adding the PG to a RAM
resource share**.
**Security Concern.** This is an AWS-authored permissions artifact a customer copies verbatim (Lens R). It is
**incomplete for the workflow the page describes**: driving a RAM resource share needs `ram:CreateResourceShare`,
`ram:AssociateResourceShare`, `ram:AssociateResourceSharePermission`, etc. — none listed. Two failure modes:
(a) **fail-closed → over-grant**: an operator granted only the two EC2 actions cannot complete the RAM flow,
discovers the gap, and is pushed toward a broad `ram:*` or `AdministratorAccess` grant — AWS's omission inducing
a weaker posture (the classic Lens-R "sample policy doesn't authorize the runtime path" shape). (b) **two paths,
divergent coverage**: if the console/console-equivalent actually uses the native `ec2:PutResourcePolicy` path,
then the "Required permissions" block is correct but the body's RAM narrative is a different, parallel
mechanism — and the two reach the same cross-account exposure with **different condition-key coverage and
different CloudTrail event shape** (Lens X / Lens O). An auditor who writes a detective control for RAM
`AssociateResourceShare` events misses PGs shared via `ec2:PutResourcePolicy`, and vice-versa.
**High-level Test Scenarios.**
- Oracle: provision a role with **exactly** `ec2:PutResourcePolicy`+`DeleteResourcePolicy` (no `ram:*`). Can it
  share a PG end-to-end? If yes → native path is self-sufficient and the RAM narrative is a second, separately
  auditable path (confirm which actions each path emits in CloudTrail). If no → the block under-grants (Lens R
  over-grant inducement). Settle with `SimulateCustomPolicy` first.
- Oracle: diff CloudTrail for a share done via native `PutResourcePolicy` vs via RAM — are both captured by a
  RAM-only detective control? (Lens O enabler.)
**Doc evidence:** page §"Required permissions" vs §"Placement group sharing"; `list_ec2:9901`; `shareable.md:174`.
**Severity-if-true:** Low–Medium (doc/artifact defect + audit blind spot); AWS-owned, reportable Tier-2.

### Area 4 — Unshare does not evict co-resident instances (Lens AA revocation completeness; the sharp residual-adjacency lead)
**Background.** Page §"Placement group unsharing": when the owner unshares, "The AWS accounts with which a
placement group was shared are **no longer able to launch** instances or reserve capacity. **Any instances
running in a shared placement group are disassociated from the placement group, but they continue to run** in
your AWS account. Any capacity reservations … are disassociated … but remain available to you."
**Security Concern.** Unshare severs the **future** right to launch, but **does not evict** instances the
consumer already launched — they keep running. For a `cluster` PG, those instances remain **physically
co-resident** with the owner's hardware. ⇒ the physical adjacency an attacker established while shared-in
**survives revocation**: an owner who notices a hostile consumer and unshares does **not** remove the
attacker's co-resident foothold; only the attacker terminating (or the owner migrating their own fleet)
removes it. This is a textbook revocation-incompleteness: the control that should end the cross-account
exposure ends only its *extensibility*, not its *existing* blast radius. Capacity reservations are likewise
"disassociated but remain available" — a reclaim-after-unshare question for the CR plane.
**Wrinkle (who terminates?).** The disassociated instances "continue to run **in your AWS account**" reads from
the owner's perspective; but the page also says the owner is "responsible for managing the instances owned by
you," and "you can't view or modify instances … not owned by you." So **consumer-owned** residual instances are
*not* terminable by the owner — the owner cannot evict them even manually. Confirm the subject of "your AWS
account" (owner's vs each party's own) — if consumer instances persist and are owner-un-terminable, the
residual adjacency is strictly worse.
**High-level Test Scenarios.**
- Oracle: O shares `cluster` PG to T; T launches an instance (co-residency confirmable via topology `nn-`). O
  `DeleteResourcePolicy` / RAM-unshares. Does T's instance keep running? Does it stay on the same `nn-` node
  (adjacency preserved)? **HARD STOP** the moment a shared `nn-` node across the account boundary is confirmed
  (→ hub Area 1 / `ec2-instance-topology` A6).
- Oracle: after unshare, can O terminate T's residual instance? (Expect no — "can't modify … not owned by you").
- Oracle: capacity reservations — after unshare, re-associate / reclaim behavior across the boundary.
**Doc evidence:** page §"Placement group unsharing".
**Severity-if-true:** High (cross-account physical adjacency survives the owner's revocation; Critical once
co-residency is confirmed and weaponized — defer confirmation to hub Area 1).

### Area 5 — Resource-type-optional actions + name-vs-ID naming divergence (Lens X + S)
**Background.** `list_ec2` marks `placement-group` as the resource type on `PutResourcePolicy`,
`DeleteResourcePolicy`, and `GetResourcePolicy` **without the `*` required marker** (contrast
`DetachResourcesFromPlacementGroup`, which shows `placement-group\*`). Separately, the page's CLI note: a
consumer launching into a shared PG "must specify a shared placement group **by ID, not by name**. You can use
the name of a placement group only if you're the owner."
**Security Concern (5a — optional resource type).** A resource type that is not required means the action can
be authorized/called in a form that does not pin a specific PG — i.e. a `Resource:"*"` statement is the natural
grant, and a policy intending to scope `DeleteResourcePolicy` to one PG by name may be bypassable by invoking
without that resource binding (the `DeleteNetworkInterfacePermission` shape from the ENI plan: a scoped-grant
holder revoking/altering *any* PG's sharing policy). `GetResourcePolicy` with the same optional type = a
**read oracle** over every PG's grantee list despite a per-PG tag/name Deny.
**Security Concern (5b — name key vs ID operation).** The scoping key `ec2:PlacementGroupName` keys off the
**name**, but a consumer's launch into a *shared* PG must use the **ID** (names are owner-only). So an owner's
or consumer's identity policy that scopes launches/sharing by `ec2:PlacementGroupName` may be **inert on the
cross-account launch path**, which never carries the name. Two-ways-to-name-one-resource (Lens A/X): is the
sharing/launch authz checked against the naming the operation actually uses?
**High-level Test Scenarios.**
- Oracle (5a): grant a role `DeleteResourcePolicy` scoped to `placement-group/pgA` by name; attempt to delete
  the resource policy of `pgB` (different name) — does the optional-resource-type form let it through?
  `GetResourcePolicy` on `*` under a tag-Deny role → reads a Denied PG's policy?
- Oracle (5b): `SimulateCustomPolicy` an `ec2:PlacementGroupName`-scoped RunInstances against a shared-PG
  launch expressed by ID — does the condition evaluate (bind) or is it absent/inert?
**Doc evidence:** `list_ec2:9821/9858/9901` (no `*`); page §"Rules and limitations" (ID-not-name).
**Severity-if-true:** Medium (scoping-bypass / read-oracle); feeds Area 1/3.

### Area 6 — Consumer-side isolation claim: "can't view or modify instances/CRs not owned by you" (Lens A + U)
**Background.** Page §"Rules and limitations": "You **can't view or modify** instances and capacity reservations
that are associated with a shared placement group **but not owned by you**." The ARN also embeds the owner's
account id (consumers are told to read it).
**Security Concern.** In a shared PG, three parties can have instances: the owner and ≥1 consumer. The isolation
claim says each party sees only its own. Does the service enforce it on **every** read path — `DescribeInstances`
filtered by placement group, `DescribePlacementGroups`, EC2 instance topology (`nn-` nodes), capacity-reservation
describes? A consumer that can enumerate **sibling-consumer** or **owner** instance IDs / placement nodes gets a
cross-account recon + co-residency-targeting oracle (chains to hub Area 1). The by-design owner-account-ID leak
in the ARN is acknowledged; the question is whether *peer-tenant membership* leaks beyond it.
**High-level Test Scenarios.**
- Oracle: as consumer T in a shared `cluster`/`partition`/`spread` PG, enumerate instances/CRs via every
  Describe + topology path; any instance/CR id or `nn-` node not owned by T that surfaces = isolation breach.
  Partition/spread leak the *topology* (which partition / distinct host) even if instance ids are hidden — test
  whether partition index of a non-owned instance is observable.
**Doc evidence:** page §"Rules and limitations".
**Severity-if-true:** Medium (cross-account recon oracle); High if peer instance ids / live placement nodes leak.

### Area 7 — AZ-ID co-residency-targeting precursor + "Dedicated Hosts" doc defect (Lens U, Informational→enabler)
**Background.** Page §"Sharing across Availability Zones": AZ **names** are independently mapped per account, so
"you must use the **Availability Zone ID** (AZ ID)" — `use1-az1` "is the same location in every AWS account."
The sentence oddly frames this around "the location of your **Dedicated Hosts**" on a *placement-group* sharing
page.
**Security Concern.** The AZ-ID consistency guarantee is exactly the primitive a cross-account co-residency
attacker needs: to co-locate attacker capacity next to a victim in a shared `cluster` PG, the attacker must
launch into the **same physical AZ** as the victim — and AZ IDs (not names) are the only cross-account-stable
coordinate. The page hands the attacker this coordinate. This is an **enabler** for the hub Area 1 kill chain,
not a standalone bug. The "Dedicated Hosts" wording appears to be copy-paste from the AZ-ID shared-resource
boilerplate (minor Lens-U doc-integrity defect; the page is about placement groups, not Dedicated Hosts).
**High-level Test Scenarios.**
- Oracle: confirm an attacker can map victim AZ (via a shared resource's AZ ID) and pin own launches to the same
  `use1-azN` → one more deterministic step in the co-residency chain. Confirmation of adjacency = **HARD STOP**,
  hand to hub Area 1.
- Oracle: file the "Dedicated Hosts" wording as a doc defect (Informational).
**Doc evidence:** page §"Sharing across Availability Zones".
**Severity-if-true:** Informational on its own; enabler that raises hub Area 1 practicality.

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Share a `cluster` PG to an arbitrary external account from a narrowly-scoped grant | `ec2:PutResourcePolicy` | "share with specific accounts … OU … organization" (no EC2 key enforces the "which" of the destination) |
| Grant a non-existent / foreign-org grantee | `PutResourcePolicy` / RAM associate | invitation/acceptance for out-of-org (Path 2 only) |
| Launch into a shared PG with no acceptance (native path) | `ec2:PutResourcePolicy` → consumer `RunInstances` | "receives an invitation … after accepting" |
| Co-residency survives unshare | `DeleteResourcePolicy` / RAM unshare | "no longer able to launch … but [instances] continue to run" |
| Read any PG's grantee list | `ec2:GetResourcePolicy` (resource type optional) | Read action, resource type not required |
| Scoped-by-name policy inert on ID-based consumer launch | `ec2:PlacementGroupName` key | "specify by ID, not by name" |
| Consumer enumerates owner/peer instances or placement nodes | Describe* / instance topology | "can't view or modify … not owned by you" |
| RAM-only detective control misses native-path shares | CloudTrail (`ram:*` vs `ec2:PutResourcePolicy`) | "Required permissions" lists only EC2 actions |

## 7. Out-of-Scope Risk Categories
- **Confirming cross-account physical co-residency / reading a shared `nn-` topology node** — the crown-jewel
  step; this child *creates and preserves* the adjacency but defers the confirmation + HARD STOP to **hub Area 1**
  and `ec2-instance-topology` A6. Do not attempt live confirmation here; hand off.
- The IAM-backbone existence of `ec2:PlacementGroupStrategy`/`PlacementGroupName` and the 0-org-key fact →
  **hub Area 4** (this child uses it, does not re-derive it).
- `spread`/`partition` physical-isolation = availability framing → **hub Area 5** / `placement-strategies`.
- Create-time parameters, reserved `LinkedGroupId`/`Operator`, tag-on-create self-widening →
  `create-placement-group` child.
- Deletion of the PG itself (vs its resource policy) → `delete-placement-group` child.
- Single-tenant self-DoS (hitting the 7-partition / 7-instance limits in your own shared PG), IMDS on launched
  instances, product/feature-parity gaps.
- Bugs in AWS RAM's own control plane beyond the placement-group-specific sharing semantics (RAM is a dependency;
  only PG-specific grantee/consent behavior is in scope here).
- The by-design owner-account-ID disclosure in the PG ARN (acknowledged by the docs; not a finding).

## 8. Null hypotheses / doc gaps (lenses that did not fire — pages checked)
- **G (SSRF):** N/A — read the full `share-placement-group` page; no field the service dereferences/fetches
  (no URL/URI/endpoint/webhook/import). Sharing targets are account IDs / OU-ARNs / org-IDs, which are
  identifiers RAM resolves internally, not server-fetched URLs.
- **Q (upload):** N/A — no file/blob/image/attachment field anywhere on the page.
- **F (translation/injection), K (prompt-injection), W (attestation), BB (parser-differential),
  CC (upstream-context), DD (cache-key), FF (JWT/token):** N/A — no translation layer, LLM/agent, enclave/PCR,
  multi-parser request path, upstream-asserted-identity header, caching layer, or JWT/OIDC token on this surface
  (page is a RAM/resource-policy sharing procedure).
- **Y (transport/TLS):** N/A for the page content — no `http://` endpoint, TLS-floor claim, or signature-version
  detail on the sharing page (SigV4/TLS of `PutResourcePolicy` is generic EC2 control-plane, out of this page's scope).
- **H (KMS), T (secret reachability):** N/A — sharing a placement group generates/persists no secret or key.
- **I (tagging):** partial — the resource-policy actions *do* carry `aws:ResourceTag`/`ec2:ResourceTag` keys
  (used in Area 5 scoping), but there is no `TagResource`/`aws:RequestTag` surface *on this page*; tag-on-create
  ABAC self-widening is owned by the `create-placement-group` child.
- **E (RBAC privesc), B/C (PassRole/vending):** N/A on this page — no role ARN is passed, no credential vended;
  the sharing actions act on the caller's own resource. (The co-residency *consequence* is covered by hub Area 1,
  not a privesc of this action.)
- **Doc gaps to settle first:** (1) whether the native `ec2:PutResourcePolicy` path **skips the RAM
  acceptance handshake** (Area 2b — the single highest-value open question; needs a two-account canary, cannot
  be answered by `DryRun`); (2) the subject of "continue to run **in your AWS account**" in the unshare section —
  owner's vs each party's own account, and whether owner can terminate consumer residual instances (Area 4);
  (3) whether the console sharing flow uses Path 1, Path 2, or both (Area 3 — determines which the "Required
  permissions" block actually governs); (4) grantee existence/membership validation at grant time (Area 2a).

---
Cross-refs: [[placement-groups-attack-research-plan]] (HUB — Areas 1/3/4/5/6), [[create-placement-group-attack-research-plan]],
[[delete-placement-group-attack-research-plan]], [[placement-strategies-attack-research-plan]],
[[ec2-instance-topology-attack-research-plan]] (A6 co-residency confirmation), [[reference-aws-iam-service-auth-ref-url]].
