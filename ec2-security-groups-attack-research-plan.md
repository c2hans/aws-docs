# EC2 Security Groups (chapter HUB) — Attack Research Plan

**Target:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html
(offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-security-groups.md`; online `.md` twin checked — identical content, no drift)

**Authoritative IAM source:** `https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html` (fetched to `/tmp/list_ec2.md`, 35,512 lines HTML form; byte-identical to a fresh curl). Trust this over UserGuide prose where they disagree.

---

## 0. How to use this document

This is the **chapter HUB** for the EC2 Security Groups documentation cluster. A comprehensive sibling already exists and **owns the SG core**:

> **`ec2-security-groups-privatelink-attack-research-plan.md`** (same directory) — owns **Areas 1–8**:
> 1. SG-referencing bypasses IAM authz + cross-account CloudTrail (Lens S/O)
> 2. `security-group-rule` ABAC enforced only if caller opts in via `TagSpecifications` (Lens S/R)
> 3. No IAM condition key covers SG rule *contents* — CIDR/port/protocol/peer (Lens S/U)
> 4. `ec2:Vpc` binds the SG's **home** VPC, not the association target (Lens S)
> 5. Unsharing an Organizations-shared SG does not sever existing enforcement (Lens AA)
> 6. Connection tracking lets a flow outlive the rule that permitted it (Lens V/U — cross-ref `ena-nitro-perf`)
> 7. PrivateLink/interface-endpoint default posture is full-access + custom-policy audit gap (Lens U/O/R)
> 8. SG-referencing silently fails across a routed middlebox hop (Lens U/V)

**Do not re-execute Areas 1–8.** This hub routes to them and owns only **net-new material the landing page and child pages surface that the sibling does not cover**:
- **H1** — stateful response-channel **egress-filter bypass / exfil** (landing-page property)
- **H2** — self-referencing-SG **intra-membership full-mesh lateral movement** (rules-reference idiom)
- **H3** — additive-only / "most-permissive-rule-wins" / **no-deny aggregation model** (false-narrowing primitive)
- **H4** — four **`Describe*` unscopable read oracles** (quantified from `list_ec2`)
- **H5** — `AssociateSecurityGroupVpc` **cross-account standing-to-associate** as a reach-widener (extends, does not duplicate, Area 4)
- **H6** — **stale-rule re-peering un-stale** + **customer-managed prefix-list unshare** continued propagation (Lens AA — distinct from Area 5's Organizations-SG case)
- **H7** — operational / doc-accuracy footguns (propagation overclaim, bulk-delete partial failure, swapped CLI labels, default-SG doc gaps)

Everything here is documentation-derived. Nothing was tested live. **HARD STOP:** any lead that reaches an AWS service-plane credential/identity/ARN → stop, preserve evidence, flag for disclosure.

---

## 1. Pentest Objectives

Determine, for EC2 Security Groups as a per-ENI stateful firewall:
1. Whether the **stateful** property can be used as an **egress-control bypass / covert exfil channel** that the customer's outbound rules cannot stop.
2. Whether the documented **self-reference "allow-all-from-this-SG"** idiom silently converts SG membership into unrestricted full-mesh trust, and whether that mesh can be stretched cross-VPC/cross-account via `AssociateSecurityGroupVpc`.
3. Whether the **additive-only, most-permissive-wins** aggregation model creates a reliable "false sense of narrowing" primitive (one broad rule silently defeats narrow intent).
4. Which SG **read** APIs are **unscopable** (region-only), making them account-wide reconnaissance oracles.
5. Whether **revocation is complete** across the lifecycle seams the sibling's Area 5 does *not* cover: peering re-creation un-staling dormant rules, and customer-managed prefix-list unshare.

---

## 2. Components, Assets, and Design (hub-level synthesis)

**What it is.** A Security Group is a *stateful* virtual firewall **enforced per-ENI by the Nitro system**. Control-plane configured (EC2 API), data-plane enforced (Nitro). Allow-only, additive model: there are **no deny rules**; "it evaluates all rules from all security groups that are associated with the instance" and the union is permitted.

**Verbatim landing-page facts this hub OWNS:**
- Statefulness (H1 root): *"Security groups are stateful—if you send a request from your instance, the response traffic for that request is allowed to flow in regardless of inbound security group rules. Also, responses to allowed inbound traffic are allowed to flow out, **regardless of outbound rules**."*
- Self-reference (H2 root): *"If the security group contains a rule that allows all traffic from the resources associated with it, then each instance can receive any traffic sent from the other instances."*
- Aggregation (H3 root): *"it evaluates all rules from all security groups that are associated with the instance"*; default SG used if none specified; *"After you launch an instance, you can change its security groups."*
- Rules-reference confirms the self-reference idiom as a **documented standard use case**: inbound rule `-1 (All) / -1 (All) / -1 (All) / <the ID of the security group>` — *"The rule allows all types of traffic."* (`security-group-rules-reference.md`)

**Resource identifiers.** `security-group/${SecurityGroupId}` (`sg-…`), `security-group-rule/${SecurityGroupRuleId}` (`sgr-…`), `vpc/${VpcId}`. SG IDs are not low-entropy/sequential, but are routinely shared across accounts (cross-account referencing uses `123456789012/sg-1a2b3c4d`).

**Ownership split that matters.** `SecurityGroupVpcAssociation` models **`groupOwnerId` ≠ `vpcOwnerId`** as a first-class state — an SG owner in Account X can associate their SG onto a VPC owned by Account Y **if the VPC "was shared with you"** (subnet-level RAM share), with no per-SG consent step from the VPC owner (H5).

```
                 EC2 control plane (API: Authorize/Revoke/Modify/Associate/Describe)
                        │ configures
                        ▼
   ENI ── Nitro data-plane enforcement (stateful conntrack) ── ENI
    │  SG set = union of all associated SGs (allow-only, most-permissive wins)
    │
    ├─ H1 stateful: response traffic bypasses egress rules
    ├─ H2 self-ref: SG membership == full-mesh any/any trust
    ├─ H3 aggregation: one 0.0.0.0/0 rule anywhere defeats all narrow rules on that port
    └─ H5 AssociateSecurityGroupVpc: stretch this SG (and its H2 mesh) into VPCs merely "shared with you"
```

---

## 3. Trust-Boundary Map (net-new rows; see sibling §3 for the rest)

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Compromised instance (inside tenant) | Internet / blocked egress target | **Stateful response channel** — inbound-allowed flow's responses egress "regardless of outbound rules" | Data leaves via a port the egress rules forbid, riding the return path of an allowed inbound flow → egress control is bypassable (H1) |
| Any workload joined to a shared SG | Every other member of that SG | Self-reference "allow-all-from-this-SG" rule | Any protocol/port reaches a sibling member that security intent never meant to expose (H2) |
| SG owner (Account X) | VPC owned by Account Y | `AssociateSecurityGroupVpc` where "VPC was shared with you" | X's SG rules (incl. H2 mesh) become enforceable in Y's VPC with no per-SG approval by Y (H5) |
| Any principal with region access | All SGs / rules / associations in the account+region | `DescribeSecurityGroups` / `…Rules` / `…VpcAssociations` / `DescribeStaleSecurityGroups` | Full topology read with **only `ec2:Region`** scoping possible — account-wide recon oracle (H4) |
| Prefix-list / peer-SG owner | Consumer's SG rule after "revocation" | Unshare / peering-delete leaving stale-but-live or re-stale-able reference | Consumer rule keeps enforcing, owner keeps pushing updates, after the trust relationship ended (H6) |

---

## 4. API / Interface Inventory (SG-relevant, hub view)

| Name | Mutating | Resource-scopable? | Notes |
|---|---|---|---|
| CreateSecurityGroup | yes | **Yes** — `aws:RequestTag`/`aws:TagKeys` (force tag-on-create) + optional `vpc` row (`ec2:VpcID`/`ec2:Tenancy`) | tag-on-create *is* enforceable here |
| DeleteSecurityGroup | yes | **Yes** — tag / `ec2:SecurityGroupID` / `ec2:Vpc` | fully scopable |
| AuthorizeSecurityGroup{Ingress,Egress} | yes | SG row scopable; **rule contents NOT** (→ sibling Area 3); rule-tag ABAC opt-in only (→ sibling Area 2) | |
| RevokeSecurityGroup{Ingress,Egress} | yes | SG row only — **no `security-group-rule` row at all** | |
| ModifySecurityGroupRules | yes | `prefix-list`(opt)+`security-group*`+`security-group-rule*`; rule row = tag/Region only | |
| AssociateSecurityGroupVpc | yes | `security-group*`+`vpc*` both required; `ec2:Vpc`(home)≠`ec2:VpcID`(target) → sibling Area 4; **H5** cross-account depth | |
| DisassociateSecurityGroupVpc | yes | same, `vpc` optional | |
| **DescribeSecurityGroups** | no | **NO — blank resource, `ec2:Region` only** | H4 oracle |
| **DescribeSecurityGroupRules** | no | **NO — `ec2:Region` only** | H4 oracle |
| **DescribeSecurityGroupVpcAssociations** | no | **NO — `ec2:Region` only** | H4 oracle |
| **DescribeStaleSecurityGroups** | no | **NO — `ec2:Region` only** | H4 oracle |
| DescribeSecurityGroupReferences | no | **Yes** — `security-group*` row w/ tag/`ec2:SecurityGroupID`/`ec2:Vpc` | the one scopable Describe; only passive detection surface for being referenced |
| GetSecurityGroupsForVpc | no | `vpc*` required | |

---

## 5. Recommended Areas of Focus (net-new; Areas 1–8 → sibling)

### H1 — Stateful response channel as an egress-filter bypass / exfil primitive (Lens U, V)
**Claim:** A customer's outbound (egress) security-group rules cannot stop data leaving an instance if the data rides the **return path of an allowed inbound flow**, because responses to allowed inbound traffic "are allowed to flow out, regardless of outbound rules."
**Mechanism (doc evidence):** landing-page statefulness paragraph (quoted §2). The egress ruleset is *not consulted* for return traffic of a tracked inbound connection.
**Confirm/Refute oracle:** on an instance whose egress is locked to deny-all, open a listening service permitted by one inbound rule; show that arbitrary response-body bytes exit to the inbound peer despite the deny-all egress policy. Egress exfil succeeding = guarantee ("my egress rules bound what leaves") broken.
**Preconditions:** one permitted inbound rule (extremely common — any exposed service); attacker controls, or can reach, the inbound peer.
**Cost:** low. **Severity:** Medium–High (defeats a control operators believe prevents exfil; pairs with any RCE/webshell).
**Stop condition:** demonstrate one return-path byte leaving against deny-all egress. Do **not** stage real data — synthetic canary only.

### H2 — Self-referencing SG = unrestricted intra-membership full mesh (Lens U, V, EE)
**Claim:** Membership in a self-referencing SG grants **any/any** reachability to every co-member; "narrowing" an app to "its own tier" silently authorizes all ports/protocols among everything that ever joins that SG.
**Mechanism:** landing-page self-reference sentence + rules-reference `-1/-1/-1/<self sg-id>` "allows all types of traffic" standard use case. Enforcement key is *SG membership*, not workload identity/purpose.
**Confirm/Refute oracle:** add a second, unrelated instance to a self-referencing "web tier" SG; confirm it can reach every other member on **any** port (e.g. SSH/DB) with no additional rule. Reachability on a port the operator never intended = breach of the inferred guarantee.
**Preconditions:** ability to attach an instance/ENI to the SG (same account, or cross-account via H5).
**Cost:** low. **Severity:** Medium alone; **High** as a lateral-movement amplifier once combined with H5 (mesh crosses VPC/account) or H3 (a broad rule widens the mesh further).
**Stop condition:** one unintended member-to-member connection on a non-intended port.

### H3 — Additive-only / most-permissive-wins → false-narrowing primitive (Lens U)
**Claim:** Because there are no deny rules and "the most permissive rule" wins across the union of all associated SGs, a single broad rule (e.g. `0.0.0.0/0:22`) **silently overrides** every narrower rule on that port — with no warning at rule-add time.
**Mechanism:** `creating-security-group.md` — *"If there is more than one rule for a specific port, Amazon EC2 applies the most permissive rule. For example … allows access to TCP port 22 … from anywhere, then everyone has access to TCP port 22."* Plus landing-page "evaluates all rules from all security groups associated."
**Confirm/Refute oracle:** on an instance with a narrow SSH rule, attach a *second* SG (or add a sibling rule) containing `0.0.0.0/0:22`; confirm the narrow rule is silently defeated and no API warning is emitted. Also test: does any SG posture-tool/console flag the widening? (If not → detection gap.)
**Preconditions:** ability to add a rule or attach a second SG (the operation the IAM layer *cannot* content-scope — sibling Area 3).
**Cost:** low. **Severity:** High — this is the mechanism that makes sibling Area 3 (no content key) *impactful*: not only can IAM not forbid `0.0.0.0/0`, but one such rule anywhere in the union wins.
**Stop condition:** confirm the widening occurs and is silent. Routes mitigation discussion to sibling Area 3 (declarative policies as the only native preventive control).

### H4 — Four unscopable `Describe*` SG read oracles (Lens A, O)
**Claim:** `DescribeSecurityGroups`, `DescribeSecurityGroupRules`, `DescribeSecurityGroupVpcAssociations`, and `DescribeStaleSecurityGroups` have an **empty resource-type cell and only `ec2:Region`** as a condition key — they cannot be scoped per-SG/per-tag, so any principal granted them reads the **entire account+region** SG topology (every rule, every CIDR, every cross-VPC association, every stale/dormant reference).
**Mechanism:** `list_ec2.md` action tables (DescribeSecurityGroups L23289, Rules L23261, VpcAssociations L23275, Stale L23457 — all blank-resource + `ec2:Region`). Only `DescribeSecurityGroupReferences` (L23243) carries a scopable `security-group*` row.
**Confirm/Refute oracle:** with a policy granting `DescribeSecurityGroups` conditioned on a tag or SG-ID, confirm via `SimulatePrincipalPolicy` (or live call) that the condition is a **no-op** and all SGs are returned. Non-filterability = oracle confirmed.
**Preconditions:** any read grant for these actions (common in "read-only"/auditor roles).
**Cost:** none. **Severity:** Medium — reconnaissance primitive that feeds H2/H3/H5 target selection and exposes `DescribeStaleSecurityGroups` dormant-rule intel (H6).
**Stop condition:** confirm the resource/tag condition is ignored for one of the four.

### H5 — `AssociateSecurityGroupVpc` cross-account standing-to-associate as a reach-widener (Lens A, U — extends sibling Area 4, does not duplicate)
**Claim:** An SG owner can **stretch their SG (including its H2 full-mesh rules) into a VPC they do not own**, gated only by "the VPC was shared with you" (a generic subnet-level RAM decision), with the VPC owner given **only passive visibility**, no per-SG approval. Sibling Area 4 covers the *IAM-authoring* confusion (`ec2:Vpc` vs `ec2:VpcID`); this covers the *trust-model* depth.
**Mechanism:** `API_AssociateSecurityGroupVpc.md` — *"You can associate the security group with another VPC if your account owns the VPC **or if the VPC was shared with you**. You must own the security group."* `SecurityGroupVpcAssociation` has distinct `groupOwnerId`/`vpcOwnerId`. `security-group-assoc.md` — *"Both the security group owner and the VPC owner can view the security group VPC associations"* (visibility is the only guaranteed VPC-owner control). The feature is explicitly chained to SG-referencing ("reference this security group in an existing security group rule"), i.e. it widens the preconditions of H2 and sibling Area 1.
**Confirm/Refute oracle:** as a shared-subnet participant (own one shared subnet in Account Y's VPC), associate your own SG onto Y's VPC; confirm it succeeds without any Y-side approval step and that your SG's rules now enforce for ENIs in Y's VPC. Success = the subnet-share consent was silently overloaded into SG-layering standing.
**Preconditions:** be a RAM shared-subnet participant in the target VPC; own the SG; same Region; non-default VPC + non-default SG.
**Cost:** low. **Severity:** High (cross-account network-posture influence from a share granted for a different purpose).
**Stop condition:** one successful cross-owner association. **HARD STOP** if any identity encountered belongs to the AWS service plane rather than Account Y.
**Doc gap to carry:** `security-group-assoc.md` is **silent** on whether removing a VPC association marks dependent SG-reference rules stale (contrast peering, which is explicit) — flag for live confirmation.

### H6 — Revocation-completeness seams the sibling's Area 5 does not cover (Lens AA, U)
Sibling Area 5 = Organizations-shared-SG unshare. This hub owns two **distinct** AA gaps:

**H6a — Peering re-creation un-stales a dormant rule.** `vpc-peering-security-groups.md`: a reference rule marked stale when peering is deleted *"will no longer be marked as stale if you create a new VPC peering connection with the same VPCs."* A rule the operator believed dead silently **resumes enforcement** when an unrelated later re-peering happens, with no re-review. **Oracle:** create ref rule → delete peering (rule goes stale) → re-peer same VPCs → confirm rule enforces again without being re-authored. Severity High.

**H6b — Customer-managed prefix-list unshare keeps enforcing *and* keeps updating.** `work-with-shared-prefixes.md`: *"If the prefix list is already referenced in the consumer's resources, those references continue to function as normal … If you update the prefix list to a new version, the references use the latest version."* After unshare: consumer's rule keeps enforcing, **owner retains a unilateral, invisible-to-consumer write channel** into the consumer's SG posture (consumer simultaneously *"can no longer view the prefix list or its entries"*). **Oracle:** share list → consumer references `pl-…` in an SG rule → unshare → owner edits list entries → confirm consumer's rule reflects the new CIDRs while consumer cannot inspect them. Severity High. **Positive control to note:** full prefix-list *deletion* (vs unshare) *is* blocked until all consumer references are removed — so the gap is specific to unshare, not deletion.

### (Routing reminders)
- Cross-account SG-referencing with no authz/CloudTrail → **sibling Area 1** (do not re-run; H2/H5 feed its preconditions).
- Rule-content IAM gap, TagSpecifications ABAC opt-in → **sibling Areas 3, 2**.
- Connection-tracking flow outliving its rule → **sibling Area 6 / `ena-nitro-perf`**.

---

## 6. Threat-Model Test Objectives

| Objective | API / mechanism | Confirm via |
|---|---|---|
| Exfil past deny-all egress on an allowed inbound flow's return path | Nitro stateful conntrack (H1) | Synthetic canary egress against deny-all egress rules |
| Reach a co-member on an unintended port via self-ref SG | self-reference rule (H2) | Add unrelated instance to the SG; non-intended-port connection |
| Silently defeat a narrow rule with one broad rule | union + most-permissive-wins (H3) | Attach 2nd SG w/ `0.0.0.0/0`; confirm no warning + narrow rule defeated |
| Read entire account+region SG topology under a "scoped" read policy | 4 bare `Describe*` (H4) | `SimulatePrincipalPolicy` proving tag/ID condition is a no-op |
| Layer own SG onto a VPC owned by another account | `AssociateSecurityGroupVpc` (H5) | Shared-subnet participant associates SG w/o VPC-owner approval |
| Reactivate a believed-revoked rule by re-peering | stale-rule un-stale (H6a) | Delete peering → re-peer same VPCs → rule enforces again |
| Keep pushing CIDR changes into a consumer after "unsharing" | customer-managed prefix list (H6b) | Post-unshare list edit reflected in consumer rule |

---

## 7. Out-of-Scope / Hard Stops
- No live testing in this pass (documentation-derived plan only).
- **HARD STOP** on any AWS service-plane identity/credential/ARN — preserve evidence, flag for disclosure, do not probe further.
- Read-only, synthetic-canary PoCs only; confirm existence, never exploit beyond it; tear down anything created.
- Stay in-scope HTTP/application + EC2 control-plane; no DNS/port-scan/subdomain work.

---

## 8. Null Hypotheses / Doc Gaps (hub-level)

- **Lens B/PassRole, Lens C/credential-vending, Lens F/injection** — null for SGs themselves (no role-assumption, no translation layer); checked landing + create/change/delete + rules-reference pages. SG name/description character constraints are **not documented** on `creating-security-group.md` (immutable post-create) — doc gap, not a confirmed injection surface; cross-ref API reference if pursued.
- **Lens EE (predictable name / ID reuse)** — `deleting-security-group.md` is **silent** on whether a deleted SG's ID or a deleted-then-recreated same-named SG can inherit stale references. Doc gap; pair with H6a (re-peering un-stale) if pursued.
- **Org-scoped condition keys** (`aws:PrincipalOrgID`, `aws:ResourceOrgID`, etc.) — **zero occurrences** anywhere in `list_ec2.md`; they are global keys documented elsewhere, so their absence from EC2 per-action rows is expected, but note no EC2 SG resource row advertises them.
- **Operational / doc-accuracy footguns (H7, low severity, carry for completeness):**
  - `changing-security-group.md` claims rule edits are *"automatically applied"* / immediate with **no stated propagation SLA or eventual-consistency caveat** — overclaim risk; confirm actual propagation latency.
  - `changing-security-group.md` CLI examples appear to **swap `revoke-security-group-egress` / `-ingress`** under the inbound/outbound removal headings and use `--group id` (space) — an operator following them could revoke the wrong direction and leave an inbound allow intact believing it removed.
  - `changing-security-group.md` ships a literal `0.0.0.0/0` in the `modify-security-group-rules` example (port 80) **immediately below a warning against anywhere-access** — AWS-authored sample normalizing the pattern it just warned against (weaker Lens R than the sibling's items; port 80 not 22/3389).
  - `deleting-security-group.md` **console bulk-delete partial-failure UX** (*"we display the status of each security group, which indicates whether it will be deleted"*) can leave an operator believing a batch delete fully succeeded while some SGs are stranded (CLI/PowerShell are single-group, so this is console-specific).
  - **Default SG is undocumented** on the create/delete child pages — its allow-all-among-members / allow-all-egress content and non-deletability are only implied by the parent chapter. Doc gap for anyone relying on the child pages alone.
- **Positive controls (working as intended — record so they are not re-chased):**
  - `DeleteSecurityGroup` **is** fully resource-scopable (tag/ID/VPC) — not an oracle.
  - `CreateSecurityGroup` **can** force tags on create (`aws:RequestTag`/`aws:TagKeys`) and pin the VPC (`ec2:VpcID`) — tag-ABAC *is* enforceable at creation (contrast the rule-level opt-in gap, sibling Area 2).
  - `deleting-security-group.md`: deletion is **blocked** (not silent) while the SG is attached to any ENI or referenced by another SG — a non-silent-failure control that works.
  - Prefix-list **deletion** (not unshare) is blocked until all consumer references are removed (H6b positive control).

---

*Hub plan. Owns H1–H7. Routes Areas 1–8 to `ec2-security-groups-privatelink-attack-research-plan.md`; connection tracking to `ena-nitro-perf`; broad EC2-Security chapter to `ec2-security-attack-research-plan.md`.*
