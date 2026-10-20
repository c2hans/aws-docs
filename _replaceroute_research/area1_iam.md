# Area 1 — IAM Authorization Surface for EC2 Route-Table Action Family

Scope: `CreateRoute`, `ReplaceRoute`, `DeleteRoute`, `CreateRouteTable`, `AssociateRouteTable`,
`ReplaceRouteTableAssociation`, `DisassociateRouteTable`, `DeleteRouteTable`,
`EnableVgwRoutePropagation`, `DisableVgwRoutePropagation`, RouteServer actions.

Primary source: `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (10,190 lines).
Secondary sources: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md`,
`/work/aws-docs/docs/AWSEC2/latest/UserGuide/supported-iam-actions-tagging.md`,
`/work/aws-docs/docs/AWSEC2/latest/APIReference/API_CreateRoute.md`,
`/work/aws-docs/docs/AWSEC2/latest/APIReference/API_ReplaceRoute.md`,
AWS-managed-policy mirror under `/work/aws-docs/docs/aws-managed-policy/latest/reference/`.

This is documentation-only analysis. No AWS API calls were made.

---

## 1. Per-action resource types / condition keys / ARN format

Row citations are line numbers in `list_ec2.md` ("Actions defined by Amazon EC2" detail table, §starting line 4603).

| Action | Resource types (required marked `*`) | Condition keys | Evidence (file:line) |
|---|---|---|---|
| `CreateRoute` | `route-table*` (only) | `aws:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:RouteTableID`, `ec2:Vpc` | list_ec2.md:5403-5407 |
| `ReplaceRoute` | `route-table*` (only) | same 5 keys as above | list_ec2.md:9431-9435 |
| `DeleteRoute` | `route-table*` (only) | same 5 keys | list_ec2.md:6118-6122 |
| `CreateRouteTable` | `route-table*`, `vpc*` | route-table leg: `aws:RequestTag`, `aws:TagKeys`, `ec2:Region`, `ec2:RouteTableID`; vpc leg: `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag`, `ec2:Tenancy`, `ec2:VpcID` | list_ec2.md:5428-5433 |
| `AssociateRouteTable` | `internet-gateway`, `ipv4pool-ec2`, `route-table*`, `subnet`, `vpn-gateway` | per-leg; route-table leg has `ec2:RouteTableID`, `ec2:Vpc`; subnet leg also has `ec2:Vpc` | list_ec2.md:4786-4792 |
| `ReplaceRouteTableAssociation` | `internet-gateway`, `ipv4pool-ec2`, `ipv6pool-ec2`, `route-table*`, `subnet`, `vpn-gateway` | route-table leg: `ec2:RouteTableID`, `ec2:Vpc`; subnet leg also has `ec2:Vpc` | list_ec2.md:9437-9444 |
| `DisassociateRouteTable` | `internet-gateway`, `ipv4pool-ec2`, `ipv6pool-ec2`, `route-table` (not marked required `*` here), `subnet`, `vpn-gateway` | route-table leg: `ec2:RouteTableID`, `ec2:Vpc`; subnet leg also `ec2:Vpc` | list_ec2.md:7952-7960 |
| `DeleteRouteTable` | `route-table*` (only) | `aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag`, `ec2:RouteTableID`, `ec2:Vpc` | list_ec2.md:6142-6146 |
| `EnableVgwRoutePropagation` | `route-table*`, `vpn-gateway*` | route-table leg has `ec2:RouteTableID`, `ec2:Vpc`; vpn-gateway leg only tag/region keys | list_ec2.md:8132-8137 |
| `DisableVgwRoutePropagation` | `route-table*`, `vpn-gateway*` | same shape as Enable | list_ec2.md:7867-7872 |
| `AssociateRouteServer` | `route-server*`, `vpc*` | route-server leg: tag/region keys; vpc leg: tag/region/`ec2:Tenancy`/`ec2:VpcID` | list_ec2.md:4780-4784 |
| `CreateRouteServer`/`...Endpoint`/`...Peer`, `DeleteRouteServer*`, `DisableRouteServerPropagation`, `EnableRouteServerPropagation`, `GetRouteServer*`, `ModifyRouteServer`, `DisassociateRouteServer` | `route-server*`, `route-server-endpoint*`, `route-server-peer*`, `subnet*`, `vpc*` combos | tag/region-only keys, no destination/peer-ASN/peer-IP condition keys found | list_ec2.md:5409-5427, 7290-7303, 8992-8997 |

**Route-table ARN format** (list_ec2.md:9992):
```
arn:${Partition}:ec2:${Region}:${Account}:route-table/${RouteTableId}
```
Supported condition keys on this resource type: `aws:RequestTag/${TagKey}`, `aws:ResourceTag/${TagKey}`, `aws:TagKeys`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:RouteTableID`, `ec2:Vpc` — the same seven are the *entire* universe of conditions available anywhere in the `CreateRoute`/`ReplaceRoute`/`DeleteRoute` IAM surface.

**Dependent actions**: the current `list_ec2.md` format (unlike the legacy per-service IAM tables) has no "Dependent actions" column at all — grep for "dependent action" returns zero hits in the file. Null result: AWS's own authorization-reference doc does not expose a dependent-actions concept for this service in this doc generation; this is not evidence of an actual bypass, just that the documentation format doesn't surface it.

---

## 2. THE KEY QUESTION — can IAM constrain route destination or route target?

**Claim**: No IAM condition key exists, anywhere in the ~137-entry EC2 condition-key catalog, that lets a policy author restrict (a) the destination CIDR/prefix-list of a route created via `CreateRoute`/`ReplaceRoute`, or (b) which target resource (gateway/NAT/ENI/TGW/peering/etc.) that route may point to.

**Mechanism** (file:line doc evidence):
- `CreateRoute`/`ReplaceRoute`/`DeleteRoute` have exactly **one** resource type, `route-table*` (list_ec2.md:5403-5407, 9431-9435, 6118-6122). There is no second "required" resource leg for the target (no `internet-gateway`, `natgateway`, `vpc-peering-connection`, `network-interface`, `transit-gateway`, `vpc-endpoint`, `egress-only-internet-gateway`, `local-gateway`, `carrier-gateway`, or `core-network` resource type listed for any of the three actions) — contrast this with `AssociateRouteTable`/`ReplaceRouteTableAssociation`/`DisassociateRouteTable`, which *do* carry extra resource legs (`internet-gateway`, `subnet`, `vpn-gateway`) because those actions touch those resources directly for IAM-authorization purposes.
- The full condition-key catalog for the service (list_ec2.md:10036-10189, ~137 keys swept) was searched for every candidate key named in scope. Confirmed **absent**: `DestinationCidrBlock`, `DestinationIpv6CidrBlock`, `DestinationPrefixListId`, `ec2:GatewayId`, `NatGatewayId`, `CoreNetworkArn`, `OdbNetworkArn`, `EgressOnlyInternetGatewayId`, `LocalGatewayId` (only `ec2:DhcpOptionsID`-style per-resource keys like `ec2:NetworkInterfaceID`, `ec2:VpcPeeringConnectionID`, `ec2:transitGatewayId` exist, but these are scoped to the *resource type itself* (e.g. network-interface, vpc-peering-connection, transit-gateway actions) — they are never listed as available condition keys for `CreateRoute`/`ReplaceRoute`/`DeleteRoute` because those actions don't carry those resource types at all).
- Confirmed via grep (command output) that `carrier-gateway`, `egress-only-internet-gateway`, `local-gateway`, `natgateway`, `vpc-endpoint` all exist as independently ARN-addressable resource types elsewhere in the service (lines 9927, 9935, 9969, 9976, 10025) — i.e. AWS *could* technically plumb them into `CreateRoute`'s authorization model the way it did for `AssociateRouteTable`'s `subnet`/`internet-gateway`/`vpn-gateway` legs, but it did not.
- `API_CreateRoute.md` and `API_ReplaceRoute.md` confirm the API itself takes `DestinationCidrBlock`/`DestinationIpv6CidrBlock`/`DestinationPrefixListId` plus one-of `CarrierGatewayId, CoreNetworkArn, EgressOnlyInternetGatewayId, GatewayId, InstanceId, LocalGatewayId, NatGatewayId, NetworkInterfaceId, OdbNetworkArn, TransitGatewayId, VpcEndpointId, VpcPeeringConnectionId` as plain request parameters (API_CreateRoute.md:25-108, API_ReplaceRoute.md:19-107) — these are request-body fields, not IAM-checked resources. No `PassRole` parameter exists on either action.

**Confirm/Refute oracle**: `iam:SimulatePrincipalPolicy` (or a live test) against a policy such as:
```json
{"Effect":"Allow","Action":"ec2:CreateRoute","Resource":"arn:aws:ec2:*:ACCOUNT:route-table/rtb-xxxx",
 "Condition":{"StringEquals":{"ec2:VpcPeeringConnectionID":"pcx-evil"}}}
```
would show the condition key is simply ignored / not evaluated for this action (it is not a listed key for `CreateRoute`), so the Allow applies regardless of which `VpcPeeringConnectionId` / `GatewayId` / `TransitGatewayId` is actually supplied in the request. A hunter with `ec2:CreateRoute`/`ec2:ReplaceRoute` scoped to *any* route table (even one legitimately tag-scoped) can install a route to *any* target they can separately reach (any peering connection, ENI, NAT gateway, TGW attachment, etc. in the account/region) and to *any* destination CIDR, including `0.0.0.0/0`, with no IAM mechanism to stop them.

**Severity if true**: High. This directly mirrors the "IAM cannot constrain rule content" NACL finding for the sibling primitive: an attacker (or over-permissioned role) that only needs `ec2:CreateRoute`/`ec2:ReplaceRoute` on one route table can redirect traffic for that route table's associated subnets to an attacker-controlled ENI/ VPC-peering connection/ transit gateway attachment for traffic interception (on-path MITM), or black-hole/0.0.0.0/0-override routes for DoS — and no amount of IAM policy authoring can add a guardrail on "which CIDR" or "which target." The only available guardrail is which *route table* (by ARN/tag/VPC) the principal may touch at all. This is a genuine, confirmed (via documentation) IAM design gap, not a bug — same class of finding as the NACL content gap.

**Null-hypothesis checks performed and come up empty**: searched for `DestinationCidr`, `DestinationIpv6`, `DestinationPrefixList`, `ec2:GatewayId`, `NatGatewayId`, `CoreNetworkArn`, `OdbNetworkArn`, `EgressOnlyInternetGatewayId`, `LocalGatewayId`, `CarrierGatewayId`, `VpcEndpointId` as *condition keys* (not resource-ARN components) across all of `list_ec2.md` — zero matches as condition keys for the route-create/replace/delete actions.

---

## 3. Condition-key scoping-semantics traps (Lens S)

### 3a. `ec2:RouteTableID` on `CreateRouteTable` resolves to `*` at runtime

**Claim**: True, and it is AWS's own documented warning.

**Mechanism**: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md:270` states (the "ec2:ResourceID condition keys" section):
> "When using the following `ec2:{{Resource}}ID` condition keys with the specified API actions, the condition key value is used to specify the resulting resource that is created by the API action. `ec2:{{Resource}}ID` condition keys can't be used to specify a source resource that is specified in the API request. If you use one of the following `ec2:{{Resource}}ID` condition keys with a specified API, then you must always specify the wildcard (`*`). If you specify a different value, the condition always resolves to `*` during runtime."

`ec2:RouteTableID` – `CreateRouteTable` is explicitly listed in the "avoid using these condition keys with these API actions" bullet list (iam-policies-for-amazon-ec2.md:305). AWS's recommended fix is to use the `Resource` ARN element instead (iam-policies-for-amazon-ec2.md:313-331).

**Confirm/Refute oracle**: Write a policy allowing `ec2:CreateRouteTable` with `Condition: {"StringEquals":{"ec2:RouteTableID":"rtb-specificid"}}` and call `SimulatePrincipalPolicy`/actually call `CreateRouteTable` — the condition will always evaluate as if `rtb-specificid` were `*`, i.e. it is a dead condition that silently grants unconditional `CreateRouteTable` regardless of the value an author believes they typed. A pentester/auditor should flag any customer policy using `ec2:RouteTableID` on a *creating* action as a false sense of restriction (it restricts nothing beyond what `Resource:"*"` already would).

**Severity if true**: Medium — this is a policy-authoring footgun that produces broader-than-intended access (a policy author believes they scoped `CreateRouteTable` to one route table ID, but actually granted it unconditionally), not an AWS-side vulnerability. Worth flagging to a hunter reviewing customer policies: look for `ec2:RouteTableID` conditions on `CreateRouteTable` (or any *creating* action) as a signal the policy doesn't do what its author intended.

### 3b. `ec2:Vpc` exposed on multiple resource legs of `AssociateRouteTable` / `ReplaceRouteTableAssociation` (multi-resource condition pitfall)

**Claim**: True — confirmed multi-leg exposure, and AWS's own doc describes the general failure mode this causes.

**Mechanism**: From the detail rows (list_ec2.md:4786-4792 for `AssociateRouteTable`, 9437-9444 for `ReplaceRouteTableAssociation`), `ec2:Vpc` is a condition key on **two separate resource legs** of the same action: the `route-table*` leg and the `subnet` leg (and also appears on `vpc*` leg for other actions in the family, e.g. `CreateRouteTable`). Per `iam-policies-for-amazon-ec2.md:196`:
> "Many condition keys are specific to a resource, and some API actions use multiple resources. If you write a policy with a condition key, use the `Resource` element of the statement to specify the resource to which the condition key applies. If not, the policy may prevent users from performing the action at all, because the condition check fails for the resources to which the condition key does not apply. If you do not want to specify a resource, ... then you must use the `...IfExists` condition type to ensure that the condition key is ignored for resources that do not use it."

Applied to `AssociateRouteTable`: if a policy author writes a single statement with `Resource: "arn:aws:ec2:*:*:route-table/*"` plus `Condition: {StringEquals:{"ec2:Vpc":"arn:aws:ec2:*:ACCT:vpc/vpc-X"}}` and expects it to also cover the `subnet` resource leg the action needs, the condition will not apply to the subnet ARN at all (because the `Resource` element didn't include a subnet ARN entry), causing either (a) an unexpected Deny on the subnet leg (if this is the only statement granting subnet access) or (b) if a second permissive statement grants the subnet leg unconditionally, an unintended asymmetric trust boundary where the VPC check binds only the route-table side.

**Confirm/Refute oracle**: A hunter should build exactly this two-leg policy and call `AssociateRouteTable` cross-VPC with a subnet in VPC-B and a route table in VPC-A, to observe whether the `ec2:Vpc` condition is actually enforced against both legs or silently skipped for one. `iam:SimulatePrincipalPolicy` with `ResourcePolicy`/`ContextEntries` supplying both ARNs is the lower-risk oracle.

**Severity if true**: Medium — authoring pitfall that can produce accidental over-grant (route table in attacker-controlled VPC can be associated to a subnet in a victim VPC if only one leg is condition-checked) or accidental lockout, depending on which direction the misconfiguration goes. This is a generic AWS-documented "multi-resource condition" trap (not EC2/route-specific), but it lands squarely on the two actions in scope that are multi-resource (`AssociateRouteTable`, `ReplaceRouteTableAssociation`, `DisassociateRouteTable`).

### 3c. Does `CreateRoute` require PassRole or validate target ownership via IAM?

**Null result (confirmed via docs)**: `API_CreateRoute.md` and `API_ReplaceRoute.md` list no `PassRole`-style parameter, and neither action's IAM row (list_ec2.md:5403-5407, 9431-9435) carries any resource type for the target. There is no IAM-level ownership check on the target gateway/ENI/peering connection/TGW attachment — any cross-resource validation (e.g. "is this NAT gateway actually in this VPC") would be enforced only by the EC2 *service* at the API-semantics layer (not documented here as an IAM mechanism), which is out of scope for this IAM-surface analysis and not something the authorization docs claim. Treat as a genuine null: no PassRole, no documented IAM-level target-ownership validation.

### 3d. Case-sensitivity trap

**Mechanism**: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/supported-iam-actions-tagging.md:107`: "For conditions, the condition key is not case-sensitive and the condition value is case-sensitive. Therefore, to enforce the case-sensitivity of a tag key, use the `aws:TagKeys` condition key, where the tag key is specified as a value in the condition." This is a general EC2-tagging trap (applies equally to `aws:ResourceTag`/`aws:RequestTag` used on route-table resources) — a policy gating `CreateRoute` on `aws:ResourceTag/Environment=Prod` could be bypassed in terms of *tag-key* matching subtleties if an attacker can create a differently-cased tag *value* is still blocked (values are case-sensitive) but a policy relying on tag-key case folding could behave unexpectedly. No route-specific amplification found beyond this general tagging caveat.

---

## 4. ABAC self-widening via `CreateTags`/`DeleteTags` on route-table (Lens I)

**Claim**: `ec2:CreateTags`/`ec2:DeleteTags` both support the `route-table` resource type as one of ~200 "OR" resource-type legs (i.e. these actions work against any single taggable resource, selected by whichever ARN is in the `Resource` element of the request), with condition keys `aws:RequestTag/${TagKey}`, `aws:ResourceTag/${TagKey}`, `aws:TagKeys`, `ec2:CreateAction` (CreateTags only), `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:RouteTableID`, `ec2:Vpc`.

**Mechanism**: list_ec2.md line 67 (within the `CreateTags` block starting 5490, and within `DeleteTags` block starting 6190) — both show:
```
Resource types (*required): [route-table] / Condition keys: aws:RequestTag/${TagKey}, aws:ResourceTag/${TagKey},
aws:TagKeys, ec2:CreateAction, ec2:Region, ec2:ResourceTag/${TagKey}, ec2:RouteTableID, ec2:Vpc
```
AWS's own guidance (`supported-iam-actions-tagging.md:12`) is that customers *should* gate `ec2:CreateTags` with `ec2:CreateAction` (StringEquals to the specific resource-creating action, e.g. `RunInstances`/`CreateVolume`) to stop it being usable to retag *existing* resources. If a customer instead grants `ec2:CreateTags`/`ec2:DeleteTags` on `route-table/*` broadly (no `ec2:CreateAction` restriction, as several of the AWS-authored policies below in fact do — e.g. `AmazonVPCFullAccess` grants plain `ec2:CreateTags`/`ec2:DeleteTags` with `Resource:"*"` and zero condition), then any principal who can also tag route tables can self-stamp the ABAC gating tag that a *separate* `aws:ResourceTag`-conditioned `ec2:CreateRoute`/`ec2:ReplaceRoute` statement relies on, provided they can already write *some* tag to that resource (i.e. they are not blocked by a `aws:ResourceTag`-gated `CreateTags` statement themselves). This is the standard ABAC self-widening pattern: Tag-based authorization for resource X is only as strong as the authorization on who may change X's tags.

**Confirm/Refute oracle**: Build two statements — (1) `ec2:CreateRoute` Allow on `route-table/*` conditioned on `aws:ResourceTag/Env=Prod`; (2) `ec2:CreateTags` Allow on `route-table/*` with no condition (or only `aws:RequestTag` condition, not `ec2:CreateAction`). A principal holding both can tag any `Env=Dev` route table to `Env=Prod` via `CreateTags`, then immediately call `CreateRoute` against it. `SimulatePrincipalPolicy` for `ec2:CreateTags` on an arbitrary route-table ARN with `aws:RequestTag/Env=Prod` in context should return `allowed`, confirming the self-widening path.

**Severity if true**: Medium-High, conditional on customer policy hygiene — this is not an AWS platform bug (AWS documents the correct mitigation, `ec2:CreateAction`), but it is a very common real-world misconfiguration, and three of the AWS-authored managed policies inspected in §5 below (`AmazonVPCFullAccess`, `NetworkAdministrator`) grant unconditioned `ec2:CreateTags`/`DeleteTags` alongside unconditioned route-table write actions, so any customer who additionally layers a `aws:ResourceTag`-based ABAC guard on top of one of these AWS managed policies for other resource types is exposed to this self-widening pattern for route tables specifically.

---

## 5. AWS-authored sample/managed-policy audit (Lens R)

Grep sweep: `grep -rl "ec2:ReplaceRoute\|ec2:CreateRoute\b\|ec2:DeleteRoute\b\|AmazonVPCFullAccess\|\"ec2:\\*\"" docs/` across the full mirror. Below are the confirmed AWS-authored hits granting one or more in-scope route actions on `Resource:"*"` (or an unscoped `Resource` array) with **no Condition**. All are AWS managed policies or AWS first-party documentation tutorials, i.e. copy-paste material customers are expected to attach verbatim.

### 5a. `AmazonVPCFullAccess` (AWS managed policy, arn:aws:iam::aws:policy/AmazonVPCFullAccess)
File: `/work/aws-docs/docs/aws-managed-policy/latest/reference/AmazonVPCFullAccess.md`
- Sid: `"AmazonVPCFullAccess"` (lines 39-198), single statement, `Effect: Allow`, `Resource: "*"`, **no `Condition` block in the entire statement**.
- In-scope actions granted: `ec2:CreateRoute` (L73), `ec2:CreateRouteTable` (L74), `ec2:DeleteRoute` (L98), `ec2:DeleteRouteTable` (L99), `ec2:AssociateRouteTable` (L49), `ec2:DisassociateRouteTable` (L162), `ec2:ReplaceRoute` (L186), `ec2:ReplaceRouteTableAssociation` (L187), `ec2:EnableVgwRoutePropagation` (L166), `ec2:DisableVgwRoutePropagation` (L158). Essentially the entire route-table action family in scope (RouteServer actions not included — policy predates that feature) is granted account/region-wide with zero conditions.
- Per §2, since no condition key can bind destination/target anyway, this policy grants unrestricted "point any route table you can reach to any destination/any target" capability to anyone it's attached to.

### 5b. `AmazonEKSClusterPolicy` (AWS managed policy, attached to every EKS cluster's service role)
File: `/work/aws-docs/docs/aws-managed-policy/latest/reference/AmazonEKSClusterPolicy.md`
- Sid: `"AmazonEKSClusterPolicy"` (lines 39-104), `Resource: "*"`, no `Condition`.
- Grants `ec2:CreateRoute` (L46) and `ec2:DeleteRoute` (L50) unconditionally, account/region-wide, alongside ELB and EC2 volume/security-group actions. (`ReplaceRoute` not present in this policy.)
- Severity note: this is the IAM role every EKS *cluster itself* assumes — if an EKS control plane or a workload able to assume this role is compromised, it can create/delete routes in **any** route table in the account, not just ones related to the cluster's VPC.

### 5c. `NetworkAdministrator` (AWS managed job-function policy)
File: `/work/aws-docs/docs/aws-managed-policy/latest/reference/NetworkAdministrator.md`
- Sid `"AllowDefaultNetworkAdminActions"` (lines 39-214), `Resource: "*"`, no `Condition`: grants `ec2:CreateRoute` (L75), `ec2:CreateRouteTable` (L76), `ec2:AssociateRouteTable` (L55), `ec2:DisassociateRouteTable` (L151), `ec2:EnableVgwRoutePropagation` (L148)/`DisableVgwRoutePropagation` is also listed, `ec2:ReplaceRoute` (L178), `ec2:ReplaceRouteTableAssociation` (L179).
- Sid `"AllowVPCPermissions"` (lines 217-250), `Resource: ["*"]`, no `Condition`: grants `ec2:DeleteRoute` (L231), `ec2:DeleteRouteTable` (L232).
- Combined, this single AWS job-function policy grants the **entire** in-scope route-table action family unconditionally on `Resource:"*"`.

### 5d. `AmazonVPCCrossAccountNetworkInterfaceOperations` (AWS managed policy)
File: `/work/aws-docs/docs/aws-managed-policy/latest/reference/AmazonVPCCrossAccountNetworkInterfaceOperations.md`
- First statement (no Sid, lines 37-49), `Resource: ["*"]`, no `Condition`: `ec2:DescribeRouteTables`, `ec2:CreateRoute`, `ec2:DeleteRoute`, `ec2:ReplaceRoute`.
- Notable because this policy is explicitly named/intended for *cross-account* ENI operations (used by services doing cross-account networking, e.g. transit/shared VPC tooling), yet carries zero route-table scoping — anyone who can assume a role with this policy can modify routes in any route table account-wide, not just ones related to the cross-account ENI it's nominally meant to manage.

### 5e. AWS documentation tutorial — "Create a VPC with a public subnet"
File: `/work/aws-docs/docs/vpc/latest/userguide/vpc-policy-examples.md`
- Lines 112-142, this AWS first-party *tutorial example* (not a managed policy, but copy-paste doc content) grants `ec2:CreateRouteTable`, `ec2:CreateRoute`, `ec2:CreateInternetGateway`, `ec2:AttachInternetGateway`, `ec2:AssociateRouteTable` on `Resource: "*"` with no `Condition` (lines 123-139).
- Contrast: the very next example in the same doc ("Modify and delete VPC resources", lines 148-186) *does* scope `ec2:DeleteRouteTable`/`ec2:CreateRoute`/`ec2:ReplaceRoute`/`ec2:DeleteRoute` to `Resource: "arn:aws:ec2:*:*:route-table/*"` with `Condition: {"StringEquals":{"ec2:ResourceTag/{{Purpose}}":"{{Test}}"}}` — i.e. even AWS's own "best-practice" example in the same doc only ever scopes by *tag on the route table*, never by destination or target (reinforcing §2's null-hypothesis confirmation: no AWS-authored example anywhere in the mirror demonstrates target/destination-scoped route policy, because no such condition key exists to demonstrate).

**Severity assessment for §5 collectively**: High as a real-world attack-surface statement, even though each individual policy's design intent ("full VPC access", "EKS cluster needs route control for its own VPC", "network admin role") is plausible — the common failure is that **none of them scope to the VPC/route-tables that the use-case actually requires**, and because of §2's null result, no customer *could* tighten these further via condition keys even if they tried (they would have to fall back to resource-ARN wildcarding by account/region or tag, never by target/destination). A hunter reviewing a target account should specifically check: (1) is `AmazonVPCFullAccess`, `NetworkAdministrator`, or `AmazonEKSClusterPolicy` attached to any role reachable from a lower-trust boundary; (2) does any custom policy in the account copy the vpc-policy-examples.md "public subnet" pattern verbatim with `Resource:"*"`.

---

## 6. `DescribeRouteTables` read-scoping

**Claim**: `DescribeRouteTables` has no resource-level permission support at all; it is account/region-bounded only.

**Mechanism**: list_ec2.md:7308-7312:
```
- **   [DescribeRouteTables](...)  **
  - **Resource types (*required):**        <- blank, no resource type listed
  - **Condition keys:** ec2:Region
  - **Access level:** List
```
No resource type is listed (the field is present but empty), and the only condition key is `ec2:Region`. This matches the standard EC2 `Describe*` pattern: these actions must be granted with `Resource:"*"` and cannot be scoped to specific route-table ARNs or tags via IAM (tag-based *read* filtering for Describe calls in EC2 is a server-side API filter parameter, not an IAM authorization mechanism, and is out of scope for this IAM surface).

**Confirm/Refute oracle**: Attempt to write a policy restricting `ec2:DescribeRouteTables` to `Resource: "arn:aws:ec2:*:*:route-table/rtb-specific"` — IAM will still require `Resource:"*"` for the action to be grantable at all (or the statement becomes a no-op resource mismatch); `SimulatePrincipalPolicy` would show the action is only evaluable against `"*"`.

**Severity if true**: Informational/Low — this is standard, well-known EC2 Describe-action behavior and matches AWS's broader pattern (most List/Describe EC2 actions are account-wide only). Included for completeness per the task's explicit ask; this is a confirmed null (no resource-level read scoping exists), not a vulnerability.

---

## Summary of genuine null hypotheses (no finding, explicitly checked)

1. **No condition key constrains route destination** (`DestinationCidrBlock`, `DestinationIpv6CidrBlock`, `DestinationPrefixListId`) anywhere in `list_ec2.md`'s ~137-key catalog (lines 10036-10189) for `CreateRoute`/`ReplaceRoute`.
2. **No condition key constrains route target** (`GatewayId`, `NatGatewayId`, `NetworkInterfaceId`, `TransitGatewayId`, `VpcPeeringConnectionId`, `CoreNetworkArn`, `OdbNetworkArn`, `EgressOnlyInternetGatewayId`, `LocalGatewayId`, `CarrierGatewayId`, `VpcEndpointId`) for the same two actions — checked both as literal condition-key names and via the full resource-type table (lines 9914-10035) to confirm these are never listed as required resource legs of `CreateRoute`/`ReplaceRoute`/`DeleteRoute`.
3. **No documented "Dependent actions" list** exists in the current `list_ec2.md` doc-generation format for any action in scope (grep for "dependent action" = 0 hits) — a documentation-format limitation, not a security finding.
4. **No documented PassRole parameter or IAM-level target-ownership validation** for `CreateRoute`/`ReplaceRoute` — confirmed via `API_CreateRoute.md`/`API_ReplaceRoute.md` parameter lists.
5. **`DescribeRouteTables` has no resource-level read scoping** — confirmed blank resource-type field, `ec2:Region` only condition key.

## Pages checked for null-hypothesis confirmation
- `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (full file, all ~140 route*-related rows and the complete 137-entry condition-key appendix)
- `/work/aws-docs/docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md`
- `/work/aws-docs/docs/AWSEC2/latest/UserGuide/supported-iam-actions-tagging.md`
- `/work/aws-docs/docs/AWSEC2/latest/APIReference/API_CreateRoute.md`
- `/work/aws-docs/docs/AWSEC2/latest/APIReference/API_ReplaceRoute.md`
- `/work/aws-docs/docs/aws-managed-policy/latest/reference/AmazonVPCFullAccess.md`, `AmazonEKSClusterPolicy.md`, `NetworkAdministrator.md`, `AmazonVPCCrossAccountNetworkInterfaceOperations.md`, `AWSApplicationMigrationNetworkMigrationMultiAccount.md`, `AWSTransformNetworkMigrationAgentPolicy.md`, `AWSFaultInjectionSimulatorNetworkAccess.md`
- `/work/aws-docs/docs/vpc/latest/userguide/vpc-policy-examples.md`
