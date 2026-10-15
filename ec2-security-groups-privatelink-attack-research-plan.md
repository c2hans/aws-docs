# EC2 Security Groups + AWS PrivateLink (Interface VPC Endpoints) — Attack Research Plan

Source of leads: offline mirror `/work/aws-docs/docs/AWSEC2/latest/UserGuide/{ec2-security-groups,creating-security-group,changing-security-group,deleting-security-group,security-group-connection-tracking,security-group-rules-reference,eice-security-groups,interface-vpc-endpoints,ec2-security,infrastructure-security,security-iam-awsmanpol}.md`, `/work/aws-docs/docs/vpc/latest/userguide/{security-group-rules,security-group-assoc,security-group-sharing,default-security-group}.md`, `/work/aws-docs/docs/vpc/latest/privatelink/{vpc-endpoints-access,vpc-endpoints-iam}.md`, and the authoritative IAM reference `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (grepped directly — the online copy truncates condition-key columns). Status: documentation-derived hypotheses only; nothing tested against a live account.

This cluster is the child of the EC2 Security chapter (`ec2-security.md`, topics "Security groups" and "AWS PrivateLink"). It **complements**, and does not duplicate, the existing `ec2-networking-attack-research-plan.md` and its ENI/EIP/connection-tracking siblings (`ena-nitro-perf-attack-research-plan.md`, `scenarios-enis-attack-research-plan.md`, `using-vpc-attack-research-plan.md`). Where this plan's leads touch the same mechanism (connection tracking, shared-VPC isolation), it cross-references rather than re-deriving.

## 0. How to use this document

- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure.
- `list_ec2.md` line numbers cited below are from the author's read of that file at research time; re-grep if the mirror is refreshed, since the file is ~10,190 lines and action entries shift.

## 1. Pentest Objectives

1. Determine whether an IAM principal can be scoped to *author only narrow security-group rules* (bounded CIDR/port/protocol/peer) — or whether the condition-key surface makes "no 0.0.0.0/0" / "no port 22" fundamentally unenforceable by IAM, forcing all such control into prose/Config rules.
2. Determine whether cross-account security-group **referencing** (RAM-shared VPC, peered VPC) creates an audit blind spot or an IAM-bypass for the referenced SG's owner.
3. Determine whether the `security-group-rule` resource-level permission (tag-on-create ABAC) is reliably enforced, or silently skipped when the optional `TagSpecifications` parameter is omitted.
4. Determine whether revoking a security-group rule, or un-sharing a shared security group, actually and immediately severs the access it granted — or whether a live/tracked connection or a stale association survives.
5. Determine whether the default PrivateLink (interface VPC endpoint) posture for the EC2 API is as closed as a customer creating a "private" endpoint would assume, and whether the one shipped sample endpoint policy is sound.
6. Determine whether `ec2:Vpc` is bound to the resource a policy author intends when used against the newer multi-VPC security-group actions (`AssociateSecurityGroupVpc`/`DisassociateSecurityGroupVpc`).

## 2. Components, Assets, and Design

**Customer-facing interface.** Security groups are configured exclusively through the EC2 control-plane API (`*SecurityGroup*` actions) — console, CLI, SDK, CloudFormation, and (per this cluster) through an EC2 interface VPC endpoint (`com.amazonaws.{region}.ec2`) using AWS PrivateLink, which places the EC2 API inside the customer's VPC without an IGW/NAT/VPN/DX hop. There is no customer-facing data-plane protocol for security groups themselves — they are a control-plane-configured, data-plane-enforced (per-ENI, in the Nitro hypervisor/Nitro Card) stateful packet filter.

**Enforcement point.** A security group's rules are evaluated at the ENI, by the Nitro system, for every associated instance's network interface — not by a separate appliance the customer can see or reach. Connection state (which flows are "tracked") is also Nitro-side (`security-group-connection-tracking.md`).

**Resources and identifier shapes.**
- `security-group` — `arn:${Partition}:ec2:${Region}:${Account}:security-group/${SecurityGroupId}` (`sg-...`). Scoped to exactly one "home" VPC (except once associated with additional VPCs via the newer multi-VPC-association feature).
- `security-group-rule` — a separately IAM-addressable resource type (`sgr-...`), introduced to let `TagSpecifications`-tagged rules be ABAC-scoped at creation. **Its enforcement is parameter-gated — see Lead 2.**
- A rule's "source"/"destination" can be a CIDR (v4/v6), a managed/customer prefix list, or **another security-group ID** ("security group referencing") — this last form is not a resource reference IAM evaluates (Lead 1).
- Interface VPC endpoint (`vpce-...`) with an attached **endpoint policy** — a resource-based IAM policy, JSON, ≤20,480 chars, that must name a `Principal`.

**Accounts/VPCs/ownership.** Three cross-boundary shapes exist in this cluster:
1. **Cross-VPC security-group association** (`AssociateSecurityGroupVpc`) — one account's SG, multiple VPCs in the same account or a VPC shared to it via RAM subnet-share.
2. **Cross-account security-group sharing via AWS Organizations** (`security-group-sharing.md`) — owner account shares an SG (via AWS RAM) to participant accounts in the same Organization; participants attach it to their own ENIs in a shared subnet. The *owner* retains write control of the rules; the *participant* only consumes.
3. **Cross-account/cross-VPC security-group referencing** (`security-group-rules.md` "Security group referencing") — a rule's source/destination names an SG that may belong to a different account (peered VPC, or RAM-shared VPC). This is the one explicitly **not IAM-authorized** per the docs (Lead 1).

**Identity.** All SG and endpoint-policy mutation is IAM-SigV4 only; there is no separate credential type. Endpoint policies additionally gate *which principal* may use the endpoint at all — a second, resource-based authorization layer in front of the identity-based one.

**ASCII connection/trust diagram**

```
 Customer VPC A (SG owner, Account 111111111111)
   ├─ EC2 instance ── ENI ── SG "web" (sg-aaa)  ← rules reference sg-bbb (another account) as source
   │                                             ← IAM AuthorizeSecurityGroupIngress call: NOT checked
   │                                                against sg-bbb's existence-as-resource beyond "exists?"
   ├─ Shared subnet (RAM) ──────────────────────────────────────────────┐
   │                                                                     │
 Customer VPC B / participant Account 222222222222                      │
   └─ EC2 instance ── ENI ── sg-aaa (SHARED, owned by 111...) ◄─────────┘
        (participant cannot edit sg-aaa's rules; owner can; unsharing
         does not detach sg-aaa from already-created participant ENIs)

 Customer VPC (any account)
   └─ Interface VPC endpoint (vpce-xxx) → com.amazonaws.{region}.ec2
        │  (AWS PrivateLink; no IGW/NAT/VPN/DX)
        │  Endpoint policy = resource-based IAM, default: Allow * / * / *
        └──► EC2 control plane (AWS service account/region fleet)
             — custom endpoint policy ⇒ some failed requests
               (RequestLimitExceeded) may not reach CloudTrail/CloudWatch
```

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| IAM principal (any account) | security-group rule *contents* (CIDR/port/protocol/peer-SG) | `Authorize/RevokeSecurityGroup{Ingress,Egress}`, `ModifySecurityGroupRules`, `UpdateSecurityGroupRuleDescriptions*` | A principal denied broad network opening by policy (intended via a Condition on rule contents) can still author a `0.0.0.0/0`/any-port rule — **the content has no condition key to deny against**. |
| Participant account (shared SG) | Owner account's security-group rule authorship audit trail | Cross-account security-group **referencing** in a rule's source/destination | A rule naming a foreign-account SG as source/destination produces **no CloudTrail event for the referenced SG's owner**, and an IAM policy scoped to that referenced SG ARN has **no effect** on the call. |
| Caller omitting `TagSpecifications` | `security-group-rule` resource-level ABAC gate | `AuthorizeSecurityGroupIngress`/`Egress` without `TagSpecifications` in the request | A policy that is supposed to gate rule-creation via `aws:RequestTag`/`aws:TagKeys` on the `security-group-rule` resource is **bypassed entirely** by a request that simply omits `TagSpecifications`. |
| Policy author restricting a *target* VPC | `AssociateSecurityGroupVpc` / `DisassociateSecurityGroupVpc` | `ec2:Vpc` condition key used on the `security-group*` resource statement | `ec2:Vpc` resolves to the SG's **home** VPC ARN, not the VPC named in the call's `VpcId` parameter (that is `ec2:VpcID`, gated on the separate `vpc*` resource statement) — a policy conflating the two under-constrains or mis-targets the control. |
| Org-member participant account, post-unshare | Owner-controlled, formerly-shared security group | `AWS RAM` unshare / `DeleteResourceShare` | After the owner stops sharing, **existing participant ENIs still receive rule updates** from the (no-longer-shared) SG; only *new* associations are blocked — a live cross-account control plane into the participant's traffic survives the "revoke." |
| Live/established connection | Revoked ingress/egress rule | `RevokeSecurityGroupIngress`/`Egress` while a flow is tracked | A connection matching a just-revoked rule is **not immediately interrupted** — it is allowed until the connection-tracking idle timeout (up to 432000s on non-Nitrov6 instances; 350s default on Nitro v6) elapses. |
| Anonymous/any AWS principal with network path to the endpoint | EC2 control-plane API, reached via PrivateLink | Interface VPC endpoint with no custom endpoint policy attached | The **default** endpoint policy is `Action:"*"`, `Resource:"*"`, `Principal:"*"` — a VPC endpoint created without an explicit custom policy constrains nothing beyond what identity policies already allow; a customer who believes "creating a private endpoint narrows access" is wrong by default. |
| Caller through a custom (non-default) EC2 endpoint policy | CloudTrail / CloudWatch visibility | Any failed call hitting `RequestLimitExceeded` through the endpoint | Documented: such failures "might not be logged" — an audit gap that is a direct, AWS-acknowledged side effect of attaching *any* custom endpoint policy. |

## 4. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `CreateSecurityGroup` | API | Existing | Mutating | External | Create SG in a VPC | Via SigV4/console/PrivateLink | IAM-scoped (`security-group*`, `vpc`) | Correctly keys target VPC on `ec2:VpcID` (`vpc` resource), §L5446-5449. |
| `AuthorizeSecurityGroupIngress`/`Egress` | API | Existing | Mutating | External | Add inbound/outbound rule | Yes | IAM-scoped on `security-group*` (Region/ResourceTag/SecurityGroupID/Vpc) + `security-group-rule` (RequestTag/TagKeys/Region, **only if `TagSpecifications` present**) | No condition key for CIDR/port/protocol/peer-SG — rule *contents* unauthorizable. Lead 1, 2, 3. |
| `RevokeSecurityGroupIngress`/`Egress` | API | Existing | Mutating | External | Remove rule | Yes | Same `security-group*` keys as Authorize; **no `security-group-rule` resource type at all** (not even the TagSpecifications-gated form) | Revoke is coarser-scoped than Authorize — asymmetry worth a quick Lens R/S check. |
| `ModifySecurityGroupRules` | API | Existing | Mutating | External | Bulk-edit existing rules | Yes | `security-group*`, `security-group-rule*` (both Region/ResourceTag only — **not gated by TagSpecifications presence**, unlike Authorize), `prefix-list` | Confirm whether Modify's `security-group-rule*` ABAC is unconditionally enforced where Authorize's is not — a parity gap either way is a lead. |
| `UpdateSecurityGroupRuleDescriptions{Ingress,Egress}` | API | Existing | Mutating | External | Edit rule description text only | Yes | `security-group*` only | Lowest-impact of the family; still inherits the "no rule-content key" gap, though impact there is cosmetic. |
| `AssociateSecurityGroupVpc` / `DisassociateSecurityGroupVpc` | API | **New** (multi-VPC SG associations) | Mutating | External | Attach/detach an SG to/from an additional VPC | Yes | `security-group*` (incl. `ec2:Vpc` = **home** VPC) + `vpc*` (incl. `ec2:VpcID` = **target** VPC) | Lead 4 — two different condition keys answer "which VPC," easy to conflate. |
| `DeleteSecurityGroup` | API | Existing | Mutating | External | Delete SG | Yes | `security-group*` | Blocked while ENIs/associations exist (per `security-group-assoc.md`); not itself a lead. |
| `CreateVpcEndpoint` / `ModifyVpcEndpoint` | API | Existing | Mutating | External | Create/modify interface endpoint + attach endpoint policy | Yes | IAM-scoped; endpoint policy itself is resource-based, `Principal`-gated | Default policy = full access. Lead 6. |
| EC2 API via `com.amazonaws.{region}.ec2` interface endpoint | PrivateLink | Existing | Both | External (from inside customer VPC) | Reach the whole EC2 API without IGW/NAT/VPN/DX | From inside the VPC only | Whoever the endpoint policy's `Principal`/`Condition` allows, intersected with identity policy | Non-default policy ⇒ documented CloudTrail/CloudWatch gap for some failed calls. Lead 7. |
| Security-group **referencing** (not a distinct API — a rule field) | N/A | Existing | N/A | N/A | Use another SG's ID as a rule's source/destination | N/A | **Not separately authorized** — "we only check whether the security group exists" | Lead 1 — the single highest-value doc-confirmed gap in this cluster. |

## 5. Recommended Areas of Focus

### Area 1 — Security-group referencing bypasses IAM authorization and cross-account audit (Lens S, O)

**Background.** `security-group-rules.md` ("Security group referencing") states explicitly: *"We do not authorize against referenced security groups in the following actions: `AuthorizeSecurityGroupIngress`, `AuthorizeSecurityGroupEgress`, `RevokeSecurityGroupIngress`, and `RevokeSecurityGroupEgress`. We only check whether the security group exists. This results in the following: Specifying the referenced security group in IAM policies for these actions has no effect. When a referenced security group is owned by another account, the owner account does not receive CloudTrail events for these actions."*

**Security Concern.** This is a confirmed, AWS-documented authorization-and-audit gap, not a hypothesis: (a) a referenced-SG owner **cannot** use IAM to control who may name their SG as a rule source/destination — including from a different account over a VPC peering connection or a RAM-shared VPC; (b) when the reference crosses accounts, the owner gets **zero CloudTrail signal** that someone authored (or revoked) a rule pointing at their resource. Combined with "Security group VPC Associations" / "Shared Security Group" (Organizations) features that explicitly create legitimate cross-account SG references, this is a live, in-scope control gap, not an edge case — it is the *normal* path for cross-account network segmentation via SG references.

**High-level Test Scenarios.**
1. From account B (holding a VPC peered to, or RAM-sharing a subnet with, account A), author an ingress rule on a B-owned SG that references an A-owned SG as the source. Confirm: (i) a deny-by-reference IAM policy in account A has no effect on B's call (expected per docs — IAM `simulate-principal-policy` is the safe first oracle); (ii) account A's CloudTrail shows no event for B's `AuthorizeSecurityGroupIngress` call, even filtered on "any event naming sg-A-id."
2. Determine the practical blast radius: does an SG owner have *any* way (resource policy, SCP, RCP, Config rule) to prevent foreign accounts from referencing their SG as a rule peer? If the answer is "no IAM/SCP mechanism exists," this elevates from an audit gap to a **control gap** — the only mitigation is detective (Config/Access Analyzer), not preventive.
3. Check whether the same gap applies to the newer `AssociateSecurityGroupVpc` cross-VPC association path, or whether that newer feature (which *is* IAM-scoped per `list_ec2.md`) was deliberately hardened against this exact pattern — i.e., is "SG referencing" the only legacy gap, while "SG VPC association" (the newer mechanism) closed it? If so, that is useful confirmation the gap is architecturally legacy, not fixed.

**Doc evidence:** `vpc/latest/userguide/security-group-rules.md` lines ~74-76 (verbatim quote above); `service-authorization/latest/reference/list_ec2.md` AuthorizeSecurityGroupIngress/Egress entries (condition keys limited to Region/ResourceTag/SecurityGroupID/Vpc on `security-group*`, nothing naming the referenced peer).
**Severity-if-true:** High (control gap) to Critical if a path exists where this gap lets a lower-trust account open traffic into a higher-trust account's workload with no detective signal at all for the victim.

### Area 2 — `security-group-rule` ABAC is enforced only if the caller opts in via `TagSpecifications` (Lens S, R)

**Background.** `list_ec2.md`'s `AuthorizeSecurityGroupIngress`/`Egress` entries state: *"Policies using the security-group-rule resource-level permission are only enforced when the API request includes TagSpecifications."*

**Security Concern.** If an administrator writes a policy intending to gate rule-creation on `aws:RequestTag`/`aws:TagKeys` against the `security-group-rule` resource (a natural ABAC pattern — "you may only create rules tagged `team=web`"), that gate is a **no-op** for any call that simply omits `TagSpecifications`. This is a fail-open-by-missing-optional-parameter shape: the caller controls whether the gate is even evaluated, by choosing not to tag the rule at all.

**High-level Test Scenarios.**
1. `iam:SimulatePrincipalPolicy` with a policy containing only a `security-group-rule`-scoped Allow conditioned on `aws:RequestTag/team: web`, denying everything else by omission (or an explicit Deny on `NotRequestTag`). Simulate `AuthorizeSecurityGroupIngress` (a) with `TagSpecifications` present and a non-matching tag — expect Deny; (b) with `TagSpecifications` omitted entirely — per the doc text, expect this to **evaluate as if the `security-group-rule` statement doesn't apply**, i.e., Allow if the `security-group*` resource statement alone permits it.
2. Compare `ModifySecurityGroupRules`, whose `security-group-rule*` condition keys (`list_ec2.md`, ~L9002) carry **no such "only enforced when TagSpecifications present" caveat** in the description — confirm whether Modify's ABAC is unconditional while Authorize/Revoke's is parameter-gated, i.e., an attacker denied by tag-ABAC on `AuthorizeSecurityGroupIngress` might still reach the same effective rule-creation outcome via `ModifySecurityGroupRules` if that path is less strictly gated (Lens X action-family parity).
3. Check `RevokeSecurityGroupIngress`/`Egress`: these have **no `security-group-rule` resource type at all** (not gated, not present) — confirm this means tag-ABAC cannot restrict *removal* of a tagged rule even when it successfully restricted *creation*, a revoke-side asymmetry (Lens AA adjacent).

**Doc evidence:** `list_ec2.md` AuthorizeSecurityGroupIngress (~L4894-4897) and AuthorizeSecurityGroupEgress (~L4888-4891) descriptions, verbatim "only enforced when the API request includes TagSpecifications"; `ModifySecurityGroupRules` (~L8998-9003) lacking that caveat; Revoke* (~L9573-9583) lacking the resource type entirely.
**Severity-if-true:** High if a customer's rule-authorship ABAC can be fully bypassed by a one-line parameter omission with no error returned.

### Area 3 — No IAM condition key covers security-group rule *contents* (Lens S, U)

**Background.** The full condition-key set for `AuthorizeSecurityGroupIngress`/`Egress`, `RevokeSecurityGroupIngress`/`Egress`, `ModifySecurityGroupRules`, and `UpdateSecurityGroupRuleDescriptions{Ingress,Egress}` against the `security-group*` resource is exactly: `aws:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:SecurityGroupID`, `ec2:Vpc`. None of these constrain the **CIDR, prefix list, protocol, port range, or referenced peer SG** that the rule being authorized actually contains.

**Security Concern.** This means "a principal may edit security groups, but may never open `0.0.0.0/0`" or "...may never open port 22/3389" is **not expressible as an IAM policy** against this service, full stop — contrast with, e.g., S3's rich condition-key set for bucket policies. Any organization relying on IAM/SCP to prevent "someone opens SSH to the world" is relying on a control that cannot exist at this layer; the only real controls are preventive-via-config (declarative policies / AWS Config rules with remediation) or detective-only. `creating-security-group.md`'s own guidance ("do not allow SSH/RDP access from anywhere... unsafe for production") is advisory prose with no IAM teeth.

**High-level Test Scenarios.**
1. Confirm via `iam:SimulatePrincipalPolicy` that no condition operator/key combination denies an `AuthorizeSecurityGroupIngress` call based on the `IpPermissions`/`CidrIp`/`FromPort`/`ToPort` values in the request — i.e., that this isn't a case of an *existing* key being overlooked.
2. Cross-check AWS's own "Declarative Policies" EC2 report (`DeclarativePoliciesEC2Report` managed policy, `security-iam-awsmanpol.md` ~L70) — does it, or any EC2 declarative-policy attribute, cover security-group rule shape? If declarative policies are the *only* AWS-native preventive control for this, that is useful confirmation and should be the plan's recommended mitigation pointer (not a vulnerability, but closes the loop for Area 3).
3. Confirm the "most permissive rule wins" aggregation rule (`creating-security-group.md`: *"If there is more than one rule for a specific port, Amazon EC2 applies the most permissive rule"*) compounds this: there is no Deny construct at all in the SG model (`security-group-rules.md`: *"You can specify allow rules, but not deny rules"*), so even a narrowly-scoped IAM principal who is only ever allowed to add *their own* narrow rule cannot be protected from a different principal/SG elsewhere in the aggregate silently overriding it.

**Doc evidence:** `list_ec2.md` condition-key lists cited in Area 1/2; `creating-security-group.md` "Considerations" bullets; `security-group-rules.md` "Security group rule basics" bullet 1.
**Severity-if-true:** This is a **confirmed documentation fact**, not a hypothesis to refute — frame the lead as "quantify the blast radius and the only available compensating control," not "look for a bug."

### Area 4 — `ec2:Vpc` binds the SG's home VPC, not the association target (Lens S variant-b)

**Background.** For `AssociateSecurityGroupVpc`/`DisassociateSecurityGroupVpc`, `list_ec2.md` lists two **separate required resource-type statements**: `security-group*` (condition keys include `ec2:Vpc` = "the ARN of the VPC," i.e., the SG's own associated/home VPC) and `vpc*` (condition keys include `ec2:VpcID` — the actual target VPC named in the API call's `VpcId` parameter).

**Security Concern.** A policy author who wants to restrict *which VPC an SG may be associated into* must gate the `vpc*` resource statement on `ec2:VpcID`. If they instead (or additionally, mistakenly) try to use `ec2:Vpc` for this purpose — a very natural mistake, since the key's description ("Filters access by the ARN of the VPC") does not disambiguate "home" vs. "target" — they are gating the wrong resource. This matches a confirmed wrong-resource-binding shape seen elsewhere in the EC2 condition-key surface.

**High-level Test Scenarios.**
1. `iam:SimulatePrincipalPolicy`: author a policy that Allows `AssociateSecurityGroupVpc` on the `security-group*` resource conditioned `ec2:Vpc = arn:...:vpc/vpc-TARGET`, with no statement at all for the `vpc*` resource type (or an unconditioned Allow there). Associate SG whose **home** VPC is `vpc-OTHER` into target `vpc-TARGET`. Expect: the policy's `ec2:Vpc` condition evaluates against `vpc-OTHER` (home), not `vpc-TARGET` — if the author's mental model was "this restricts which VPCs I can associate into," the simulation should reveal it does not.
2. Confirm the mirror-image for `DisassociateSecurityGroupVpc` (same two-resource-type shape, `list_ec2.md` ~L7962-7966).
3. Check whether this is also user-facing in `security-group-assoc.md`'s requirements list ("You must own the VPC or have one of the VPC subnets shared with you to associate a security group with the VPC") — confirm the UserGuide prose never clarifies the `ec2:Vpc` vs `ec2:VpcID` distinction, i.e., this is purely an IAM-reference-level gotcha with no UserGuide warning (a doc-gap in itself).

**Doc evidence:** `list_ec2.md` ~L4795-4799 (AssociateSecurityGroupVpc) and ~L7962-7966 (DisassociateSecurityGroupVpc); condition-key definitions ~L10036+ (`ec2:Vpc` = "ARN of the VPC" vs `ec2:VpcID` = "ID of a VPC").
**Severity-if-true:** Medium-High — this is a policy-authoring footgun with no live-account exploitation needed to prove (simulation suffices), but it is exactly the shape ("a condition key that binds the wrong resource") the AWS internal training material flags as a confirmed finding class elsewhere in EC2.

### Area 5 — Unsharing a cross-Organization security group does not sever existing enforcement (Lens AA)

**Background.** `security-group-sharing.md` ("Stop sharing a security group") states the post-unshare rules verbatim: *"Existing participant Elastic Network Interfaces (ENIs) continue to get any security group rule updates that are made to unshared security groups. Unsharing only prevents the participant from creating new associations with the unshared group."*

**Security Concern.** "Unshare" is the revoke operation for this cross-account grant, and the docs confirm it is **not** a clean severance: the owner retains a live, continuing network-control channel into the participant's already-associated ENIs (any rule change the owner makes keeps propagating), and the participant cannot detach except by disassociating the SG from every affected ENI themselves. From the participant's perspective, "unshare" by the owner does **not** restore the participant's full control over their own ENI's firewalling — they remain dependent on the (now-untrusted, since sharing stopped) owner's good behavior until they manually migrate every ENI off the SG. This is the inverse of the usual IDOR/revoke concern (owner retains access after revoke, rather than participant retaining access) — still squarely an AA-shaped incomplete-revocation finding, just with the retained privilege on the other side of the relationship.

**High-level Test Scenarios.**
1. Two-account Organization test: account A shares SG `sg-shared` via RAM; account B associates an ENI with it; A unshares. Confirm (per docs, should hold): B's ENI still enforces A's subsequent rule edits to `sg-shared`; B cannot create a *new* ENI association with `sg-shared`; B *can* `Describe`/disassociate/delete their own ENI.
2. The adversarial framing: if account A is compromised (or turns malicious) *after* a legitimate unshare, does A retain the ability to open or close traffic to B's still-associated ENI indefinitely? Quantify how long this exposure can realistically persist (there is no documented maximum) and whether B has any proactive signal that A is still able to do this (it is discoverable via `DescribeSecurityGroups`/`DescribeNetworkInterfaces`, but is it alerted?).
3. Check for a race: can a participant *create* a new association in the window between the owner initiating `delete-resource-share` and the share's state actually transitioning (console shows `Associated` → unshare → status change) — i.e., is the "no new associations" cutover atomic with the RAM share-deletion call, or eventually consistent with a race window?

**Doc evidence:** `security-group-sharing.md` lines ~154-159 (verbatim quote above).
**Severity-if-true:** Medium-High — not a bypass of a stated guarantee (AWS states this plainly), but worth confirming the practical blast radius and whether any detective control exists, since it is a frequently-overlooked operational-security gap in "stop sharing" runbooks.

### Area 6 — Connection tracking lets a flow outlive the rule that permitted it (Lens V, U — cross-ref `ena-nitro-perf`)

**Background.** `security-group-connection-tracking.md`: *"When you change a security group rule, its tracked connections are not immediately interrupted. The security group continues to allow packets until existing connections time out."* Idle timeouts default to 350s (Nitro v6) or 432000s (5 days — all other instance types, and P6e-GB200) for TCP, configurable up to those same maxima. Separately, the **untracked** flow case (both directions fully open, e.g. `0.0.0.0/0`↔`0.0.0.0/0` on all ports) is interrupted **immediately** on rule change, because it was never tracking state in the first place.

**Security Concern.** This produces a counter-intuitive inversion: the *more narrowly scoped* ("least privilege") a rule is, the *more likely* it is to be tracked, and therefore the *slower* a revoke takes effect for traffic already in flight — up to 5 days on non-Nitro-v6 instance types with default settings. An incident responder revoking an attacker's narrow inbound rule (e.g., a single-IP SSH allow that the attacker is actively using) may reasonably assume the connection drops immediately; per the docs, it does not, unless the responder also engineers an untracked-flow condition or waits out the timeout. This is the same underlying Nitro connection-tracking mechanism flagged in `ena-nitro-perf-attack-research-plan.md` for ENA performance; here the angle is incident-response/containment efficacy rather than throughput.

**High-level Test Scenarios.**
1. Establish a long-lived TCP session permitted by a narrow (tracked) ingress rule; revoke the rule; confirm the existing session is NOT reset and continues to pass traffic (packets, not just a lingering socket) until the configured idle timeout elapses. Repeat with the instance's `TcpEstablishedTimeout` set to its max (432000s) to quantify worst case.
2. Confirm the inverse: a fully-open (both-direction `0.0.0.0/0`-all-ports) connection is immediately dropped the instant either side's open rule is narrowed — i.e., validate the asymmetry is real and not just a doc simplification.
3. Document this as an operational-security finding for incident-response runbooks: "revoke the SG rule" is not sufficient containment for an active session; the runbook must also address existing tracked connections (e.g., via a NACL, which is stateless and does immediately cut traffic per the same doc page).

**Doc evidence:** `security-group-connection-tracking.md` "Untracked connections" / "Idle connection tracking timeout" sections; cross-reference `/work/aws-docs/ena-nitro-perf-attack-research-plan.md` for the adjacent ENA-performance angle on the same tracking substrate.
**Severity-if-true:** Medium (confirmed-by-docs behavior; the lead is about quantifying operational impact and checking the runbook guidance gap, not finding a bypass).

### Area 7 — PrivateLink/interface-endpoint default posture is full-access, and custom policies create an audit gap (Lens U, O, R)

**Background.** `vpc-endpoints-access.md`: *"The default endpoint policy grants full access to the endpoint"* (`Principal:"*", Action:"*", Resource:"*"`); *"If an AWS service doesn't support endpoint policies, we allow full access to any endpoint for the service."* `interface-vpc-endpoints.md` (EC2-specific): *"The default endpoint policy allows full access to the Amazon EC2 API through the interface endpoint"* and separately: *"When a non-default policy is applied to an interface VPC endpoint for Amazon EC2, certain failed API requests, such as those failing from RequestLimitExceeded, might not be logged to AWS CloudTrail or Amazon CloudWatch."*

**Security Concern.** Two distinct, AWS-stated facts combine into a customer-expectation gap: (1) simply creating a PrivateLink endpoint for EC2 does **not** reduce the API surface reachable from inside the VPC at all — it only adds a private network path; narrowing requires an explicit custom policy, which many "defense in depth" narratives assume is automatic. (2) The moment a customer *does* add the recommended custom policy (the security-conscious choice), they introduce a documented, AWS-acknowledged logging gap for throttled requests — a customer who hardens their endpoint loses visibility into some rejected calls, which is a perverse incentive against doing the hardening at all.

**High-level Test Scenarios.**
1. Confirm (doc-level, or via a scoped test account) that an interface endpoint with no policy attached permits every `ec2:*` action the calling identity's own IAM policy allows — i.e., the endpoint adds zero restriction by default. This should be treated as a documentation/expectation-gap finding (Lens U) rather than a "bug": flag it for any customer-facing hardening-guide gap (does any EC2/PrivateLink doc page actually tell customers "you must author a custom policy, the default is wide open"? `interface-vpc-endpoints.md` does say so explicitly — confirm no *contradicting* page implies otherwise).
2. With a custom (non-default) EC2 endpoint policy attached, generate `RequestLimitExceeded` throttling from inside the VPC and confirm whether the event is absent from CloudTrail/CloudWatch as documented — quantify exactly which failure classes are affected (only `RequestLimitExceeded`, "such as" implies others — enumerate).
3. Audit the one EC2-specific sample endpoint policy shipped in `interface-vpc-endpoints.md` (Lens R — this is an AWS-authored, copy-paste artifact): it grants `ec2:*`/Allow/`*`/`*` and then Denies `CreateVolume` and `RunInstances` when `ec2:Encrypted:"false"`. Confirm this Deny actually closes every unencrypted-volume path reachable through the endpoint — e.g., does `RunInstances` launching from a launch template whose block-device mapping omits `Encrypted` (defaulting per-account/region default-encryption setting) still evaluate `ec2:Encrypted` correctly at the endpoint-policy layer, or can an unencrypted root/data volume be created through this "hardened" policy via a code path the two Deny statements don't anticipate (e.g., `CopySnapshot`→`CreateVolume` chains, or an AMI with a pre-existing unencrypted snapshot)?

**Doc evidence:** `vpc-endpoints-access.md` "Considerations"/"Default endpoint policy"; `interface-vpc-endpoints.md` full text (default-policy sentence, the "Important" CloudTrail/CloudWatch note, and the sample policy JSON).
**Severity-if-true:** Medium (expectation gap, Lens U) to Medium-High if the sample policy's Deny-by-`ec2:Encrypted` coverage proves incomplete (Lens R — AWS-authored artifact, in scope even though "the customer chose to copy it").

### Area 8 — Security-group referencing silently fails to enforce traffic across a routed middlebox hop (Lens U/V, segmentation-design footgun)

**Background.** `security-group-rules.md` "Limitation": *"If you configure routes to forward the traffic between two instances in different subnets through a middlebox appliance, you must ensure that the security groups for both instances allow traffic to flow between the instances... If you reference the security group of the other instance as the source, this does not allow traffic to flow between the instances."* Identical language appears in `security-group-rules-reference.md`'s "Rules to connect to instances from an instance with the same security group" note.

**Security Concern.** SG referencing matches on the *actual* source/destination IP of the packet as it arrives at the ENI. When traffic is routed through a middlebox (firewall appliance, NVA, transparent proxy), the packet's L3 source as seen by the destination ENI is **not** the originating instance's IP — so a rule written as "allow from sg-of-the-other-instance" silently does not match, even though the design intent (and the rule's apparent documentation-sanctioned pattern — SG referencing is presented everywhere else as the preferred, least-privilege way to scope instance-to-instance traffic) suggests it should. This is a segmentation-design footgun: an architecture review that sees "SG references, not open CIDRs" would normally read as *more* secure, but in a routed-through-appliance topology the rule is simply inert, likely forcing the operator to fall back to a broader CIDR-based rule to make it work — silently *widening* the effective access to "anything in the subnet," which is a worse outcome than the reviewer would expect from reading the SG config alone.

**High-level Test Scenarios.**
1. Build the exact documented topology (two instances in different subnets, routed through a middlebox NVA) and confirm that an SG-referencing rule between them indeed does not pass traffic, while the same two instances without the middlebox hop (direct routing) do work with the identical rule — isolating the variable to "is a middlebox in the path."
2. Determine what the resulting rule a defeated administrator is likely to author instead (private-IP or subnet-CIDR source) and assess whether that fallback rule is scoped as tightly as the SG-reference form it replaced, or is a strict widening (e.g., "entire subnet CIDR" instead of "that one other instance's SG").
3. Check whether any AWS NVA/firewall partner integration guide (Marketplace appliances, Gateway Load Balancer) documents this limitation explicitly at the point where a customer would configure SG rules for GWLB-routed traffic — a doc-gap if the warning only lives in the generic `security-group-rules.md` page and not in the GWLB/NVA-specific guidance a customer actually reads.

**Doc evidence:** `security-group-rules.md` "Limitation" paragraph (verbatim above); `security-group-rules-reference.md` matching note.
**Severity-if-true:** Low-Medium as a direct finding (it's a documented limitation, not a bypass), but worth flagging because the *failure mode it induces* (operators widening to CIDR) is itself a real security regression this plan should name.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Author a wide-open ingress rule despite an IAM policy intended to prevent it | `AuthorizeSecurityGroupIngress` | None exists at the IAM layer (Area 3) — attack the *absence* of a mitigation, confirm via simulation. |
| Reference a foreign-account SG as rule source/destination with no owner visibility | SG referencing | "We only check whether the security group exists" (Area 1) — confirm zero CloudTrail signal to the referenced SG's owner. |
| Bypass tag-ABAC on rule creation | `AuthorizeSecurityGroupIngress`/`Egress` | Omit `TagSpecifications` (Area 2) — confirm the resource-level statement is skipped, not merely denied. |
| Mis-scope a cross-VPC SG-association policy | `AssociateSecurityGroupVpc` | Use `ec2:Vpc` where `ec2:VpcID` was needed (Area 4) — confirm via `SimulatePrincipalPolicy`. |
| Retain cross-account network control after "unsharing" | Shared Security Group (Organizations) | Owner continues to push rule updates to participant's existing ENIs post-unshare (Area 5) — confirm persistence and quantify duration. |
| Keep a revoked rule's traffic flowing | Connection tracking | Idle timeout (up to 432000s) on tracked flows (Area 6) — confirm active-session survival across revoke. |
| Reach EC2 API through a "private" endpoint with no narrowing | Interface VPC endpoint / default endpoint policy | Default policy = full access (Area 7.1) — confirm no implicit narrowing from endpoint creation alone. |
| Create an unencrypted volume despite the shipped sample endpoint-policy Deny | EC2 endpoint policy (sample JSON) | Find a volume-creation path the two `ec2:Encrypted` Deny statements don't cover (Area 7.3). |
| Make an SG-reference rule inert via routing design, inducing a broader fallback rule | SG referencing + middlebox routing | Confirmed-inert-by-design limitation (Area 8) — confirm the fallback widening actually occurs in practice. |

## 7. Out-of-Scope Risk Categories

- The Nitro-system packet-filtering enforcement mechanism itself (i.e., assuming the documented SG semantics are correctly implemented in the hypervisor/Nitro Card) — this plan only attacks the **authorization and lifecycle** layer around SG rules, not the packet-filter implementation.
- EC2 Instance Connect Endpoint (EICE) as a feature in its own right — `eice-security-groups.md` is a sibling page in the same directory and was read for context (it documents that *"traffic to the [EICE] endpoint... is allowed regardless of the inbound rules for the endpoint security group"* — a service-identity SG-inbound bypass), but EICE's broader attack surface (tunneling, `OpenTunnel` IAM, client-IP-preservation) belongs to a dedicated EICE-focused plan, not this one. Flagged as an adjacent null below.
- Gateway VPC endpoints (S3/DynamoDB) and their `Principal: {"AWS": "<account-id>"}` root-user-only footgun (`vpc-endpoints-access.md`) — EC2 only supports **interface** endpoints; the gateway-endpoint gotcha is real but belongs to the S3/DynamoDB PrivateLink plans.
- Shared-VPC owner/participant **instance** isolation (`DescribeInstances`/Stop/Terminate across the shared-subnet boundary) — already covered as Lead [5] in `ec2-networking-attack-research-plan.md`; not re-derived here.
- NACLs, Network Firewall, Route 53 Resolver DNS Firewall — mentioned in the SG docs as complementary/alternative controls, not security-group or PrivateLink mechanisms themselves.
- The underlying AWS RAM resource-sharing service's own security model (beyond the SG-specific sharing behavior documented in `security-group-sharing.md`/`security-group-assoc.md`).
- Physical/side-channel attacks, DNS rebinding, and any live-account exploitation — this is a documentation-derived plan only.

## 8. Null Hypotheses / Doc Gaps

Lenses walked with no firing trigger found in this cluster's pages (checked `ec2-security-groups.md`, `creating/changing/deleting-security-group.md`, `security-group-connection-tracking.md`, `security-group-rules-reference.md`, `eice-security-groups.md`, `interface-vpc-endpoints.md`, `ec2-security.md`, `infrastructure-security.md`, `security-iam-awsmanpol.md`, `vpc/latest/userguide/security-group-rules.md`, `security-group-assoc.md`, `security-group-sharing.md`, `default-security-group.md`, `vpc/latest/privatelink/vpc-endpoints-access.md`, `vpc-endpoints-iam.md`, and `list_ec2.md` in full):

- **Lens B (Confused deputy/PassRole)** — null. No SG or PrivateLink action in this cluster accepts a role ARN or passes a role to another service. `security-group-sharing.md` requires `AmazonEC2FullAccess`/`AWSResourceAccessManagerFullAccess` or the permission-only `ec2:PutResourcePolicy`/`ec2:DeleteResourcePolicy` actions to share via RAM, but these are not PassRole-shaped.
- **Lens C (Credential vending)** — null. No STS/session-policy/ProvidedContext mechanism in scope.
- **Lens D (Data-plane→control-plane escape)** — partially addressed by Area 7 (PrivateLink reaches the EC2 *control* plane by design — that's the feature, not a boundary violation); no separate control-ENI/storage-ENI exposed by SGs themselves. Null beyond Area 7.
- **Lens F (Translation-layer injection)** — null. No wire-protocol translation; SG rule fields are structured API parameters, not parsed text passed to a backend language.
- **Lens G (SSRF)** — null. No server-side-dereferenced URL/host field anywhere in SG or VPC-endpoint configuration (checked all pages above for any `*Url`/`*Uri`/webhook/callback field — none exist in this cluster).
- **Lens H (CMK/encryption-context confusion)** — null for SGs (no encryption). Touches EBS encryption only tangentially via the sample endpoint-policy's `ec2:Encrypted` condition (Area 7.3) — not a KMS-key-confusion issue per se, flagged there instead.
- **Lens I (Tagging/ABAC)** — fires, covered as Area 2 (the `security-group-rule` TagSpecifications-gated enforcement).
- **Lens J (OAuth/3P linking)** — null, no 3P integration surface.
- **Lens K (Prompt injection)** — null, no LLM/agent component in this cluster.
- **Lens L (Resource exhaustion/DoS)** — partial: "Security group size" quotas exist (`security-group-rules.md`) and connection-tracking allowance exhaustion is documented (`conntrack_allowance_exceeded`), but both are single-tenant-scoped per instance/ENI with no shared-fleet noisy-neighbor angle found in this cluster's pages — out-of-scope per the ena-nitro-perf plan's existing coverage, not re-derived.
- **Lens M (Shared-identifier interception)** — null, no session/token identifiers in this cluster.
- **Lens N (Namespace/ARN migration)** — null, no dual-namespace/migration window found for SGs or interface endpoints in these pages.
- **Lens P (Identity proofing/registration)** — null, no onboarding/OTP/uniqueness workflow in this cluster.
- **Lens Q (Upload/rich content)** — null.
- **Lens W (Attestation-conditioned auth)** — null, no NitroTPM/enclave attestation gate on SGs or endpoint policies.
- **Lens X (Action-family/twin parity)** — partially fires: Authorize vs. Modify vs. Revoke show differing `security-group-rule` ABAC coverage (Area 2, test scenario 2) — flagged there rather than as a separate area.
- **Lens Y (Transport/TLS/SigV4)** — null-ish: PrivateLink traffic is intra-VPC/AWS-backbone by construction; no documented cleartext-HTTP or TLS-downgrade path found for the EC2 interface endpoint specifically. **Doc-gap**: neither `interface-vpc-endpoints.md` nor `vpc-endpoints-iam.md` states a TLS-version floor or `aws:SecureTransport` recommendation for the EC2 endpoint explicitly — worth a follow-up read of the generic PrivateLink security page if this lens needs to be closed with confidence rather than left as a gap.
- **Lens BB (Canonicalization/parser differential)** — null, no multi-layer path/host canonicalization (API Gateway/CloudFront/ALB) in front of SG or EC2-interface-endpoint APIs.
- **Lens CC (Trusted-upstream-context injection)** — null, no authorizer/ALB-OIDC/X-Forwarded-* context in this cluster.
- **Lens DD (Cache-key vs authz-key divergence)** — null, no caching layer documented for SG rule evaluation or endpoint-policy decisions.
- **Lens EE (Predictable-name pre-registration)** — null, SG IDs (`sg-...`) are opaque/system-generated, not customer-chosen predictable names.
- **Lens FF (Token/claims validation)** — null, no JWT/OIDC/Cognito token in this cluster's auth path (SigV4 only).
- **Lens A, E, R, S, U, V, AA** — all fire; covered as Areas 1-8 above.

**Carried doc-gaps for a future pass:**
1. No offline/online page explicitly states a TLS-version floor for the EC2 interface VPC endpoint (Lens Y) — confirm against the generic AWS PrivateLink security/encryption-in-transit page before marking this lens fully null.
2. The sample endpoint policy's `ec2:Encrypted`-Deny completeness (Area 7.3) could not be fully resolved from documentation alone — it requires either a live `iam:SimulatePrincipalPolicy`/test-account check against `RunInstances` launch-template/AMI edge cases, or a close reading of the `ec2:Encrypted` condition key's exact evaluation points in the EBS encryption-by-default documentation (not read as part of this pass — out of the SG/PrivateLink cluster's page set).
3. Whether `AssociateSecurityGroupVpc`'s two-resource-type IAM evaluation (Area 4) actually denies-by-default when only one of the two required resource-type statements is authored (standard multi-resource IAM semantics would suggest yes, which bounds the practical exploitability of the `ec2:Vpc`/`ec2:VpcID` conflation to "policy author confusion / silent under-restriction," not an open bypass) — worth a `SimulatePrincipalPolicy` confirmation rather than asserting from the general IAM evaluation model alone.
4. EC2FastLaunch and Ec2InstanceConnectEndpoint AWS-managed/service-linked-role policies both touch security-group-adjacent actions (`ec2:ModifyNetworkInterfaceAttribute` on `security-group/*`, unconditioned, in `Ec2InstanceConnectEndpoint`'s SLR policy — `aws-managed-policy/latest/reference/Ec2InstanceConnectEndpoint.md`) — flagged as a minor Lens R observation but not developed into a full Area here since EICE is explicitly out-of-scope for this cluster (see §7); worth folding into a dedicated EICE plan.
