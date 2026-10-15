# Delete an EC2 Security Group (`DeleteSecurityGroup`) — Attack Research Plan

Source of leads:
- PRIMARY target: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/deleting-security-group.html` (offline `docs/AWSEC2/latest/UserGuide/deleting-security-group.md`) — verified online==offline 2026-10-15.
- API: `docs/AWSEC2/latest/APIReference/API_DeleteSecurityGroup.md`.
- IAM: `docs/service-authorization/latest/reference/list_ec2.md` (detailed action→resource table L6160–6166; summary row L1214).
- Cross-page: `docs/vpc/latest/userguide/deleting-security-groups.md`; `docs/vpc/latest/userguide/security-group-rules.md` L105 (stale-rule behavior).

Status: documentation-derived hypotheses only; nothing tested against a live account.

> **Positioning.** This is the **page-level, action-scoped DELETE child** of the SG cluster. Do NOT duplicate:
> - `ec2-security-groups-attack-research-plan.md` (HUB) — owns H1–H7 (stateful-response egress bypass, self-ref mesh, most-permissive-wins, 4 unscopable Describe oracles, cross-acct `AssociateSecurityGroupVpc`, re-peering un-stale, prefix-list unshare). HUB already names "DeleteSecurityGroup fully scopable" and "delete blocked while attached/referenced" as **positive controls** — this plan confirms both and then attacks the *gaps around* them.
> - `ec2-security-groups-privatelink-attack-research-plan.md` — the SG+PrivateLink core (Areas 1–8).
> - `creating-security-group-attack-research-plan.md` — the `CreateSecurityGroup` twin (GroupName immutable/unique-per-VPC land-grab; participant-creates-SG-in-owner-VPC-and-owner-can't-delete). **This plan owns only `ec2:DeleteSecurityGroup` and `deleting-security-group.html`.**

---

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected on this page — single-account control-plane action.)
- This action is **confirmed fully scopable** (see §4). The leads here are **not** "can I delete across accounts" (positive control holds) — they are **(a) the delete-gate overclaim/revocation-completeness defect, (b) the GroupName-vs-ID authz-ordering bypass, (c) doc-vs-doc inconsistencies** a compliance control could be built on.

---

## 1. Pentest Objectives (boundary-breach goals)
1. **Delete a security group whose cross-VPC / shared-VPC referencing rule then survives as a *stale* rule** — proving the EC2 page's "can't be referenced by a rule in another security group" gate is incomplete and that deletion is *not* a reliable revocation of all references.
2. **Bypass an `ec2:SecurityGroupID`-scoped Deny by deleting the same SG via `GroupName`** (default VPC), if the SG-ID condition key is resolved after the authorization decision.
3. **Delete the wrong SG via `GroupName` resolution** in a default VPC (name collision / normalization), if resolution does not pin exactly one group.
4. Confirm the positive controls do *not* break: no cross-account delete; default-SG delete refused; attached/same-VPC-referenced delete refused.
5. Surface doc-vs-doc / doc-vs-API inconsistencies (EC2 page omits the default-SG blocker and the "VPC association" blocker, and narrows "any resources" to "instance or network interface") that a customer attestation/runbook could be built on falsely.

---

## 2. Components, Assets, and Design
- **Interface:** control-plane API `ec2:DeleteSecurityGroup` (SigV4). CLI `aws ec2 delete-security-group`; PowerShell `Remove-EC2SecurityGroup`; EC2 console *and* VPC console (two console surfaces, slightly different requirement text).
- **Resource:** a `security-group` (`sg-...` id; also a caller-chosen, immutable, unique-per-VPC **GroupName**). Lives in the SG owner's account, inside one VPC.
- **Inputs:** `GroupId` (any VPC) **or** `GroupName` (**default VPC only**, per API doc) + `DryRun`. No tag/role/URL/blob inputs.
- **Pre-delete dependency gates (the asset under test):** the server refuses the delete with `DependencyViolation` when the SG is (per API doc) *associated with an instance or network interface*, *referenced by another security group **in the same VPC***, or *has a VPC association*. The VPC-guide page adds a 4th: *is the default security group for a VPC*.
- **Design note:** deletion is **not** a rule-revocation primitive. Rules referencing the deleted SG **from another VPC** (peering/shared) are not torn down — they become **stale** and persist until manually removed (`security-group-rules.md` L105). This is the central seam.

```
caller (SigV4) --DeleteSecurityGroup(GroupId|GroupName,DryRun)--> EC2 control plane
                                                                     |
                        authz (security-group*: ResourceTag/Region/SecurityGroupID/Vpc)
                                                                     |
                        dependency check: instance|ENI assoc? same-VPC ref? VPC assoc? default-SG?
                                   |                                     |
                              any -> DependencyViolation            none -> DELETE
                                                                         |
                                   cross-VPC/shared-VPC referencing rule --> left as STALE (survives)
```

---

## 3. Trust-Boundary Map
| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Caller with ID-scoped IAM | SG named by `GroupName` | delete-by-name (default VPC) resolves name→id *after* policy eval | A delete succeeds against an SG whose `sg-id` an `ec2:SecurityGroupID` Deny should have blocked |
| SG owner (VPC A) | referencing rule in peer/shared VPC B | delete gate only checks *same-VPC* references | Delete returns `true`; a rule in VPC B still references the now-deleted group as a **stale** rule |
| Operator relying on EC2 page's gate list | actual server gates | doc enumerates fewer blockers than API/VPC-guide | Delete behaves differently than the EC2 page implies (default-SG refused though page is silent; "any resources" blocks though page says only instance/ENI) |
| Caller | another account's SG in a shared VPC | SG is owned in the creating account | Positive control — delete MUST be refused cross-account (see creating-sg Area 4) |

---

## 4. API / Interface Inventory
| Name | Method | Mutating | External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `ec2:DeleteSecurityGroup` | API/CLI/PS | **Yes** | Yes | Delete one SG by `GroupId` or (default-VPC) `GroupName` | Yes (SigV4) | principals with the action on the `security-group*` resource | **Fully scopable:** resource `security-group*` **required**; condition keys `aws:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, **`ec2:SecurityGroupID`**, **`ec2:Vpc`** (list_ec2.md L6160–6166). *Summary table L1214 shows blank keys — the detailed table is authoritative; note the discrepancy.* Supports `DryRun`. |

**Undocumented/console-hidden knob:** `GroupName` is accepted by the API/CLI but the EC2 console delete flow is id-centric; name-based delete is a reference/SDK path a hunter should exercise directly (see Area 2).

---

## 5. Recommended Areas of Focus

### Area 1 — Delete-gate overclaim → cross-VPC referencing rule survives as *stale* (revocation-completeness) — **PRIORITY**
**Background.** The EC2 UserGuide page states a flat requirement: "The security group can't be referenced by a rule in another security group." The **API doc narrows this**: deletion fails only if the SG "is referenced by another security group **in the same VPC**." `security-group-rules.md` L105 confirms the complement: a rule that references an SG **in a peer VPC or shared VPC** is **not** a delete-blocker — when the referenced SG is deleted, that rule is merely **marked stale** and persists ("You can delete stale security group rules as you would any other security group rule").
**Security Concern (Lens AA revoke-completeness + Lens U doc-vs-enforcement).** An operator who deletes an SG to *revoke* a cross-VPC trust relationship, trusting the EC2 page's unqualified gate, is wrong: the referencing rule in the other VPC is **not** torn down. It survives as a stale rule, and the trust it encodes (any later SG that re-occupies the relationship, or re-peering per HUB H6a "re-peering un-stales a dormant rule") can silently re-enforce. The gate protects *same-VPC* references only; the EC2 page hides that qualifier.
**High-level Test Scenarios:**
- Create SG-A in VPC-A; peer VPC-A↔VPC-B (or share a VPC); create SG-B in VPC-B with an ingress rule referencing SG-A. Confirm `DeleteSecurityGroup(SG-A)` returns `true` (NOT `DependencyViolation`). → Claim: cross-VPC reference does not block deletion.
- After deletion, enumerate SG-B's rules (and `DescribeStaleSecurityGroups`) — confirm the referencing rule still exists, now stale. → Oracle: a referencing rule survives a delete the EC2 page implied would be blocked.
- Compare with the *same-VPC* case (SG-B in VPC-A) — confirm that one **does** return `DependencyViolation`. → Isolates the defect to the cross-VPC path.
- Chain to HUB H6a: tear down and re-create the peering; test whether the stale rule re-enforces against a replacement group occupying the relationship.
**Doc evidence:** deleting-security-group.md L12 (unqualified gate) vs API_DeleteSecurityGroup.md ("in the same VPC") vs security-group-rules.md L105 (stale behavior). **Severity-if-true:** Medium (operator-facing revocation-completeness gap on an AWS-authored page; raises to High if chained with H6a silent re-enforcement across a trust boundary). Owner-to-fix: AWS (doc) + customer (cleanup).

### Area 2 — `GroupName` delete (default VPC) vs `ec2:SecurityGroupID`-scoped authorization ordering
**Background.** The API accepts `GroupName` instead of `GroupId` for groups in the **default VPC** ("You can specify either the security group name or the security group ID"). The action is scopable by `ec2:SecurityGroupID`. GroupName is caller-chosen, immutable, and unique-per-VPC (see creating-sg Area 3).
**Security Concern (Lens S inert-key / Lens BB name-vs-id parser gap).** If an administrator writes a Deny (or Allow) keyed on `ec2:SecurityGroupID` to protect a specific `sg-id`, is that condition still evaluated when the caller names the group by **GroupName**? The `sg-id` must be resolved from the name server-side; if resolution happens *after* the authorization decision, the SG-ID condition has nothing to bind and the Deny is **inert** — the SG is deleted despite an ID-scoped guard. This is the exact shape confirmed for `DeleteKeyPair` (KeyPairId bypass, see memory `delete-key-pair-plan-note`) and for inert-at-authz keys on create (creating-sg Area 2).
**High-level Test Scenarios:**
- Attach a policy: `Allow ec2:DeleteSecurityGroup` on `security-group*` with `Deny` when `ec2:SecurityGroupID == sg-TARGET`. Attempt `delete-security-group --group-id sg-TARGET` (expect Deny) vs `delete-security-group --group-name <name-of-sg-TARGET>` in the default VPC. → Oracle: the GroupName variant succeeds where the GroupId variant is denied = ID-scoped Deny bypass.
- Repeat keyed on `aws:ResourceTag`/`ec2:ResourceTag` and `ec2:Vpc` — determine which condition keys bind under name-based delete and which go inert. (Tag/Vpc are resource attributes resolvable from the name; `ec2:SecurityGroupID` is the one most likely to be request-derived.)
- Confirm/refute via `DryRun` first (IAM-only, no delete), then a single live delete with a disposable SG.
**Doc evidence:** API_DeleteSecurityGroup.md (GroupName default-VPC clause); list_ec2.md L6166 (`ec2:SecurityGroupID` listed). **Severity-if-true:** Medium–High (defeats an ID-pinned guardrail; intra-account). **Stop condition:** one disposable SG proving the Deny/Allow divergence.

### Area 3 — `GroupName` resolution: wrong-group deletion / normalization (default VPC)
**Background.** Default-VPC delete-by-name requires resolving one name to one `sg-id`. Names are unique *per VPC*; the default VPC is the implied scope.
**Security Concern (Lens A/EE).** Does name resolution pin exactly the caller's default VPC and exactly one group, or can a normalization variant (case/unicode/trailing-whitespace, per creating-sg Area 3 uniqueness-normalization question) or a cross-default-VPC ambiguity cause the *wrong* SG to be selected and deleted? Combined with the create-time land-grab (creating-sg), an attacker who pre-registers a colliding name could steer a name-based delete script onto the wrong group.
**High-level Test Scenarios:**
- In an account with a default VPC, create two SGs whose names differ only by case/trailing space (if create permits — tests the create-side uniqueness-normalization gap too). Issue `delete-security-group --group-name <variant>` and observe which `sg-id` is deleted. → Oracle: a delete lands on an SG the caller did not intend to name.
- Confirm name-based delete refuses in a non-default VPC (API says ID required there) — a positive control.
**Doc evidence:** API_DeleteSecurityGroup.md GroupName clause; creating-sg Area 3. **Severity-if-true:** Low–Medium (destructive misfire; depends on normalization behavior). Marked **doc-gap** — the page says nothing about resolution scope.

### Area 4 — Doc-vs-doc blocker inconsistency (default-SG and "any resources" omissions)
**Background.** Three documents describe the delete gates differently:
- EC2 UserGuide: "can't be associated with an instance or network interface" + "can't be referenced by a rule in another security group." (2 gates)
- VPC UserGuide: "can't be associated with **any resources**" + referenced-by-rule + "**can't be the default security group for a VPC**." (3 gates, broader)
- API: instance/ENI assoc + same-VPC ref + "**has a VPC association**" → `DependencyViolation`.
**Security Concern (Lens U doc integrity).** The EC2 page **omits the default-SG blocker entirely** and **narrows "any resources" to "instance or network interface"**, and neither UserGuide page mentions the "VPC association" blocker the API enforces. A customer who codes a precondition check or a compliance runbook from the EC2 page will (a) expect default SGs to be deletable, and (b) under-enumerate what blocks a delete. All deltas are **fail-safe** at runtime (the server blocks *more* than the page admits), so this is a documentation-integrity / attestation-risk finding, not a direct bypass.
**High-level Test Scenarios:**
- Attempt `DeleteSecurityGroup` on a VPC's default SG → confirm refusal (positive control the EC2 page fails to document).
- Attach a non-instance/non-ENI resource that creates a "VPC association," attempt delete → confirm `DependencyViolation` though the EC2 page lists neither.
**Doc evidence:** deleting-security-group.md L11–12 vs vpc/.../deleting-security-groups.md L10–13 vs API_DeleteSecurityGroup.md. **Severity-if-true:** Low / Informational (AWS-owned doc defect; reportable as a doc inconsistency a compliance control could rely on).

### Area 5 — `DryRun` is a caller-IAM oracle, NOT an existence/ownership oracle (hunter guardrail)
**Background.** `DeleteSecurityGroup` supports `DryRun` (returns `DryRunOperation` if permitted, `UnauthorizedOperation` otherwise).
**Security Concern (Lens A variant — false-positive trap).** `DryRun` is evaluated against caller IAM **before resource resolution**. A `DryRunOperation` response confirms the caller *holds the permission*, not that the SG exists or belongs to the caller. A hunter must not treat DryRun success as an SG-existence or ownership oracle; the condition keys (`ec2:SecurityGroupID`/`ec2:Vpc`/tags) may themselves require resource resolution and could make DryRun behave inconsistently with the real call — worth a note but not a cross-tenant signal.
**Doc evidence:** API_DeleteSecurityGroup.md DryRun clause. **Severity:** Informational (methodology guardrail; prevents a wasted enumeration lead).

---

## 6. Threat Model Test Objectives
| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Delete leaves cross-VPC referencing rule enforcing (stale) | delete dependency gate | EC2 page: "can't be referenced by a rule in another security group" (unqualified) |
| ID-scoped Deny bypassed via GroupName delete | authz ordering / `ec2:SecurityGroupID` | list_ec2.md condition-key scopability |
| Wrong-group delete via name normalization | GroupName resolution (default VPC) | GroupName uniqueness-per-VPC |
| Default-SG delete expectation mismatch | delete gate (default-SG blocker) | VPC page gate (EC2 page omits) |
| DryRun mistaken for existence/ownership | DryRun semantics | "checks whether you have the required permissions" |
| Cross-account delete of SG in shared VPC | account ownership | SG owned by creating account (positive control — expect refusal) |

---

## 7. Out-of-Scope Risk Categories
- **Cross-account delete** of another tenant's SG — SG is owned in the creating account; delete is same-account. Positive control, not a bug to chase (the *inverse* — a participant creating a persistent SG in the owner's VPC that the owner can't delete — belongs to `creating-security-group-attack-research-plan.md` Area 4, cross-ref only).
- Stateful connection-tracking survival after rule/SG removal (up to 5-day idle timeout) — owned by HUB H1 / `ena-nitro-perf`.
- The 4 unscopable Describe oracles, self-ref mesh, most-permissive-wins — HUB H2/H3/H4.
- Customer-authored IAM policy footguns (least-privilege is the customer's problem) — only the AWS-authored *doc* defect (Area 4) is in scope here.
- Shared-fleet / service-plane reach — not implicated by a single-account control-plane delete.

## 8. Null hypotheses / doc gaps
- **Lens B/C (PassRole/vending):** N/A — delete takes no role ARN/credential/token. Checked API params + IAM row.
- **Lens G (SSRF) / Q (upload) / F (injection):** N/A — no URL/blob/parsed-content input. Checked API request params (GroupId/GroupName/DryRun only).
- **Lens H (KMS) / T (secret reachability) / W (attestation) / FF (JWT):** N/A — no key, secret, attestation, or token surface on this action.
- **Lens I/S (tag/condition scopability — positive control):** `DeleteSecurityGroup` **is fully scopable** (`security-group*` required + 5 condition keys incl. `ec2:SecurityGroupID`, `ec2:Vpc`). This is a *strength*, not a finding — recorded so the hunter does not re-chase "unscopable delete." The live question is only the GroupName authz-ordering edge (Area 2).
- **Lens O (audit):** console bulk-delete shows per-SG status on partial failure (deleting-security-group.md L35); no evidence of an audit blind spot — note only. CloudTrail logs `DeleteSecurityGroup` normally.
- **Doc gaps to confirm surface first:** (a) exact binding of each condition key under `GroupName`-based delete (Area 2); (b) GroupName resolution scope/normalization (Area 3); (c) whether "has a VPC association" (`AssociateSecurityGroupVpc`, HUB H5) is the only non-instance/ENI blocker.

---
*Built 2026-10-15 from the EC2 UserGuide page + API_DeleteSecurityGroup + list_ec2 IAM detailed table + VPC-guide delete/stale pages. No subagents: single thin action-page, surface fully resolved from authoritative API/IAM refs and 2 sibling pages, nested under an already-deep SG cluster. Cross-refs: `ec2-security-groups-attack-research-plan.md` (HUB, H5/H6a), `creating-security-group-attack-research-plan.md` (GroupName land-grab, participant-owns-SG), `delete-key-pair-plan-note` (KeyPairId-vs-name authz-ordering precedent).*
