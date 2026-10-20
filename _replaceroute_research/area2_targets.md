# ReplaceRoute / CreateRoute — Route Targets: MITM & Cross-Account Research Notes

Scope: EC2 `ReplaceRoute`/`CreateRoute` route targets. Documentation-only analysis (offline mirror
`/work/aws-docs` + live docs.aws.amazon.com cross-check). No API calls made. All claims below are
sourced to specific files/lines; where the docs are silent, that silence is called out explicitly
as a null result / open question for live testing, not asserted as a vulnerability.

API parameter surface confirmed identical between the local mirror and the live page for both
actions (fetched 2026-10-20):
- `/work/aws-docs/docs/AWSEC2/latest/APIReference/API_ReplaceRoute.md:19-107`
- `/work/aws-docs/docs/AWSEC2/latest/APIReference/API_CreateRoute.md:25-109`
- Live: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRoute.html (verified verbatim match via WebFetch)

Neither API doc page contains **any** sentence about account ownership, cross-account validation,
"must belong to your account", "must be shared with you", or resource-level authorization for any
of the ID/ARN parameters (`TransitGatewayId`, `VpcPeeringConnectionId`, `CoreNetworkArn`,
`OdbNetworkArn`, `VpcEndpointId`, `NetworkInterfaceId`, `InstanceId`, `GatewayId`,
`LocalGatewayId`, `CarrierGatewayId`, `EgressOnlyInternetGatewayId`, `NatGatewayId`). This is a
genuine documentation silence — see Null Hypotheses at the end — and is the common thread behind
every lead below.

For contrast, `EnableVgwRoutePropagation` **does** document an explicit cross-resource validation
rule: "The virtual private gateway must be attached to the same VPC that the routing tables are
associated with" / "The routing table must be associated with the same VPC that the virtual
private gateway is attached to" (`/work/aws-docs/docs/AWSEC2/latest/APIReference/API_EnableVgwRoutePropagation.md:21,26`).
No equivalent same-VPC/same-account sentence exists anywhere in the ReplaceRoute/CreateRoute docs
for any target parameter — strengthens the case that this silence is meaningful rather than
boilerplate omission, and gives the pentester a concrete differential to test against.

---

## 1. Traffic-interception / MITM via ENI, NAT, and edge (ingress) route tables

**Claim:** A principal with `ec2:ReplaceRoute`/`ec2:CreateRoute` on a route table can redirect a
subnet's internet-bound, intra-VPC, or inbound-from-internet traffic through an arbitrary
ENI/appliance/NAT/GWLB-endpoint that they control, with no ENI-ownership check documented anywhere
in the routing path.

**Mechanism (doc evidence):**
- Inter-subnet (East-West) interception is the *documented, intended* use case: "You can add a
  route to your route tables that is more specific than the local route... to redirect traffic
  between subnets within a VPC (East-West traffic) to a middlebox appliance."
  (`/work/aws-docs/docs/vpc/latest/userguide/route-table-options.md:243`)
- The local route itself — the route that normally guarantees intra-VPC traffic stays intra-VPC —
  can be replaced wholesale: "You can change the target of the default local route."
  (`/work/aws-docs/docs/vpc/latest/userguide/replace-local-route-target.md:7-8`), with the CLI
  example `aws ec2 replace-route --destination-cidr-block 10.0.0.0/16 --network-interface-id
  eni-...` (same file, lines 38-42). This is explicitly the mechanism behind "Inspect traffic
  between subnets": "replace the target of the local route with... a network interface" to force
  **all** subnet-to-subnet traffic in the VPC through one ENI
  (`/work/aws-docs/docs/vpc/latest/userguide/route-table-options.md:263,308-312`;
  `/work/aws-docs/docs/vpc/latest/userguide/intra-vpc-route.md:8-9`).
- Ingress (edge) route tables let a route table associated with an internet gateway or VGW send
  **inbound internet traffic before it ever reaches a subnet** to an ENI: "To route inbound VPC
  traffic to an appliance, you associate a route table with the internet gateway or virtual
  private gateway, and specify the network interface of your appliance as the target."
  (`/work/aws-docs/docs/vpc/latest/userguide/route-table-options.md:226`, elaborated in
  `/work/aws-docs/docs/vpc/latest/userguide/gateway-route-tables.md:8,17-29`). The association
  mechanics are in `/work/aws-docs/docs/vpc/latest/userguide/associate-route-table-gateway.md:22-29`
  (`aws ec2 associate-route-table --route-table-id ... --gateway-id ...`).
- `igw-ingress-routing.md` documents an entire BYOIP-pool-to-single-ENI path where the **only**
  stated validation is that the *destination CIDR* must be a BYOIP range you own via the BYOIP
  process ("The BYOIP process ensures that your account owns the public IP CIDR")
  (`/work/aws-docs/docs/vpc/latest/userguide/igw-ingress-routing.md:79`) — there is no parallel
  statement that the **target ENI** (`--network-interface-id`) must belong to the same account,
  only that it must exist and be attached to a running instance
  (same file, "Route creation fails" troubleshooting bullets, lines 571-575).
- `gateway-route-tables.md` "Rules and considerations" lists CIDR-scope restrictions (destination
  must be inside the VPC's own CIDR ranges) and appliance-availability requirements, but **no**
  requirement that the target ENI/GWLB endpoint be owned by the caller
  (`/work/aws-docs/docs/vpc/latest/userguide/gateway-route-tables.md:51-65`).
- The middlebox routing wizard docs (`middlebox-routing-console.md:25-44`,
  `middlebox-routing-examples.md`, `gwlb-route.md`) describe the same ENI/GWLB-endpoint-as-target
  pattern as a first-class, wizard-automated feature, with zero mention of an ownership check on
  the appliance ENI — only operational prerequisites (separate subnet, source/dest check
  disabled, same hop position for multi-middlebox setups).

**Confirm/Refute oracle (for the live-test phase, not run here):** In a single-account VPC, create
an ENI in subnet C, then as an IAM principal who only holds `ec2:ReplaceRoute`/`ec2:CreateRoute`
(and `ec2:AssociateRouteTable` for the edge case) but has **no** permission on the ENI itself
(no `ec2:*NetworkInterface*` actions, no `DescribeNetworkInterfaces` even), attempt to:
  (a) replace the local route of subnet A's or subnet B's route table to target that ENI,
  (b) associate an edge route table with the VPC's IGW that sends `0.0.0.0/0`/BYOIP CIDR to that ENI.
If either succeeds without any `ec2:NetworkInterface` grant, the "route-content gap" is confirmed:
IAM gates *who can edit the route table* but the API does not re-check *who owns the thing the
route points at*. This matches the general EC2 pattern (route targets are referenced by ID, not by
an IAM resource-match against the target), but is not explicitly stated as a security boundary
anywhere in the docs reviewed.

**Severity if true:** High. A principal scoped to "network admin for route tables" (a very common
least-privilege role, e.g. for routing hygiene automation) could silently MITM intra-VPC or
internet-ingress traffic for subnets they don't otherwise have access to, by aiming a route at an
ENI/appliance under a *different* IAM principal's or even account's control (see Area 2 for the
cross-account ENI case via shared VPC participants, and Area 2's GWLB-endpoint note). Detection is
weak: CloudTrail logs `ReplaceRoute`/`CreateRoute` with the target ID but the event does not
itself flag "target belongs to a different owner" — an operator has to notice an unfamiliar
`eni-xxxx` in a route and go cross-reference `DescribeNetworkInterfaces`.

**Caveats / what the docs DO guard:**
- `gateway-route-tables.md:60`: "You cannot use a gateway route table to control or intercept
  traffic outside of your VPC, for example, traffic through an attached transit gateway. You can
  intercept traffic that enters your VPC and redirect it to another target in the same VPC only."
  — so edge/ingress hijacking is scoped to resources inside the same VPC; it cannot be used to pull
  in a target from a different VPC/account directly (the target ENI must be in the VPC the route
  table belongs to). This bounds Lens V/D to same-VPC blast radius, which is still cross-IAM-principal
  / cross-participant in a shared-VPC subnet (see Area 2).
- In a **shared VPC subnet** specifically, `ec2:CreateRoute`/`ReplaceRoute` on the subnet or
  gateway route tables is restricted to the VPC **owner** account only — participants "cannot
  work with route tables (for example, create, delete, or associate route tables) in a shared VPC
  subnet" (`/work/aws-docs/docs/vpc/latest/userguide/vpc-share-limitations.md:46-47`). That closes
  off the most obvious cross-account route-hijack vector for shared VPCs specifically, but says
  nothing about ordinary same-account IAM principals with scoped `ec2:*Route*` permissions, which
  remains the live open question above.

---

## 2. Cross-account / shared route targets (confused-deputy shape)

### 2a. TransitGatewayId

**Claim:** A transit gateway can be owned by account X and shared via AWS RAM to account Y; once
shared, account Y can attach its own VPC to it and route to it — this is the intended hub-spoke
design, not itself a bug. The open question is whether `ReplaceRoute`/`CreateRoute` validates that
the `TransitGatewayId` supplied is one that is actually attached/shared to the VPC that owns the
route table, or whether any syntactically valid, describable TGW ID is accepted.

**Mechanism (doc evidence):**
- "A transit gateway works across AWS accounts, and you can use AWS RAM to share your transit
  gateway with other accounts. After you share a transit gateway with another AWS account, the
  account owner can attach their VPCs to your transit gateway."
  (`/work/aws-docs/docs/vpc/latest/tgw/tgw-transit-gateways.md:8`)
- Permission split from RAM sharing: owner "Run[s] all transit gateway, transit gateway attachment,
  and transit gateway route tables APIs"; the share recipient can only "Run the APIs that create
  and describe attachments... in their VPCs" and "cannot create, modify, or delete its transit
  gateway route tables, or its transit gateway route table propagations and associations" once
  shared. (`/work/aws-docs/docs/vpc/latest/tgw/working-with-transit-gateways.md:40-58`)
- `route-table-options.md:186-211` shows the expected VPC-side config: once attached, you add a
  normal `CreateRoute ... --transit-gateway-id tgw-...` entry in your own VPC's subnet route table.
  No statement anywhere that `CreateRoute`/`ReplaceRoute` checks the TGW attachment state of the
  calling VPC before accepting the `TransitGatewayId` parameter.
- Shared-VPC-subnet caveat: "Only the VPC owner can attach a transit gateway to a shared VPC
  subnet. Participants can't." (`/work/aws-docs/docs/vpc/latest/userguide/vpc-share-limitations.md:60-61`;
  confirmed again in `/work/aws-docs/docs/vpc/latest/tgw/working-with-transit-gateways.md:75`).

**Confirm/Refute oracle:** From account Y (holding `ec2:CreateRoute` on its own route table but
with *no* RAM share and *no* attachment to TGW `tgw-X` owned by unrelated account X), attempt
`CreateRoute --transit-gateway-id tgw-X ...`. Expected-safe behavior: fails because the VPC has no
attachment to that TGW (attachment-existence is a natural precondition, likely enforced — this is
the most probable null result, since a dangling TGW reference with no attachment would silently
blackhole traffic and AWS route-table validation generally requires the referenced attachment to
exist in the table). This is flagged as **likely a null result** but worth confirming live, since
the docs never state the check explicitly — it's inferred from how VPC attachments/route
propagation are described elsewhere, not asserted as an API-level validation rule.

**Severity if true (i.e., if the check is missing):** Critical — would let any account reference
and silently route into another account's unrelated, unshared transit gateway. **Severity if null
(expected):** N/A / informational — confirms defense-in-depth exists at the attachment layer even
though the API docs don't say so directly.

### 2b. VpcPeeringConnectionId

**Claim:** A VPC peering connection spans two accounts by design (requester/accepter can differ).
Routing to it is symmetric and doc-mandated per side, but each side's `CreateRoute` call only
operates on routes the caller already has IAM permission to edit in their own VPC; there's no
evidence the API checks that the referenced `pcx-...` is actually associated with the VPC that
owns the route table being modified, versus any `pcx-...` the caller can merely `Describe`.

**Mechanism (doc evidence):**
- "The owner of the *requester VPC* sends a request to the owner of the *accepter VPC*... The
  accepter VPC can be owned by you, or another AWS account."
  (`/work/aws-docs/docs/vpc/latest/peering/vpc-peering-basics.md:10`)
- "To enable the routing of traffic between VPCs... you must add a route to one or more of your
  subnet route tables that points to the VPC peering connection... Similarly, the owner of the
  other VPC must add a route to their subnet route table to route traffic back."
  (`/work/aws-docs/docs/vpc/latest/userguide/route-table-options.md:122`)
- Shared-VPC caveat: "Only VPC owners can work with (describe, create, accept, reject, modify, or
  delete) peering connections. Participants cannot work with peering connections."
  (`/work/aws-docs/docs/vpc/latest/peering/vpc-peering-basics.md:83`) — this governs the peering
  connection resource itself, not whether `CreateRoute` validates the `pcx-` ID against the VPC.

**Confirm/Refute oracle:** As account Z (unrelated to a peering connection `pcx-AB` between
accounts A and B, but holding `ec2:CreateRoute` on some unrelated route table it owns in its own
VPC C), attempt `CreateRoute --vpc-peering-connection-id pcx-AB ...`. Expected: Z cannot even
`Describe`/reference `pcx-AB` unless Z is a participant, so this is likely rejected — but the
*rejection reason* matters: is it an IAM `UnauthorizedOperation` (resource-level IAM check on the
pcx ARN) or an EC2 service-side `InvalidVpcPeeringConnectionID.NotFound`/validation error (service
checks association)? Documentation does not distinguish; this is a genuine gap for live testing.

**Severity if true:** High if the association is not validated and only reachability (the VPC
itself being one side of the peering) gates it — i.e., if VPC C's owner could point a route at a
`pcx-` connection between two *other*, unrelated VPCs it merely knows the ID of. Likely null in
practice since peering connections are inherently two-sided and non-transitive ("You do not have
any peering relationship with VPCs that your VPC is not directly peered with",
`vpc-peering-basics.md:44`), but this transitivity statement is about routing *reachability*, not
about what `CreateRoute` itself validates at call time.

### 2c. CoreNetworkArn (AWS Cloud WAN)

**Claim:** `CoreNetworkArn` is an ARN-shaped parameter — the classic cross-account confused-deputy
input shape (ARNs embed an account ID that an API *could* check against the caller, or could
ignore). Docs do not state any explicit validation that the ARN's account matches the caller or
that the core network edge is actually attached to the caller's VPC.

**Mechanism (doc evidence):**
- `API_CreateRoute.md:31-34` / `API_ReplaceRoute.md:24-27`: "The Amazon Resource Name (ARN) of the
  core network." — no further constraint text, no example request using it (unlike GatewayId,
  InstanceId, VpcPeeringConnectionId, EgressOnlyInternetGatewayId, all of which have worked
  examples in the API doc). The complete absence of a `CoreNetworkArn` example in either API page
  is itself notable — it's the least-documented parameter of the whole set.
- Cloud WAN VPC attachment docs describe the cross-account/cross-VPC topology Cloud WAN is built
  for (multiple VPCs across accounts attached to the same core network edge,
  `/work/aws-docs/docs/network-manager/latest/cloudwan/cloudwan-vpc-attachment.md:5-8`,
  security-group-referencing section lines 61-85) but never describe the `CreateRoute
  --core-network-arn` call path itself, so there is no documented statement of what validation (if
  any) ties the ARN to an attachment.
- Shared-VPC support for Cloud WAN exists per
  `/work/aws-docs/docs/vpc/latest/userguide/vpc-sharing-service-behavior.md:26` (links to
  `cloudwan-vpc-attachment.md#cloudwan-vpc-attachments-shared-subnets`), reinforcing that this is
  a multi-account-by-design feature with the same "owner creates the attachment, route points at
  the resulting ARN" shape as TGW.

**Confirm/Refute oracle:** Supply a syntactically valid `CoreNetworkArn` for a core network that
exists in a completely unrelated account/org (one the caller's VPC has never been attached to) in
`CreateRoute`. If it's accepted, the API is not checking the ARN's account or the attachment state
— Critical, since this is exactly the confused-deputy shape the pentester should chase first,
given CoreNetworkArn has zero documented validation text anywhere found.

**Severity if true:** Critical. **This is the single strongest documented lead in this file** —
not because the docs show a vulnerability, but because they show a near-total documentation
vacuum around validation for precisely the parameter shape (bare ARN, no example, no constraints
section) most associated with confused-deputy bugs elsewhere in AWS's history (S3 bucket policies,
IAM role trust, SNS/SQS resource policies). Null hypothesis is NOT established here — unlike TGW/
peering, there's no "attachment must exist" statement anywhere to infer a fallback check from.

### 2d. OdbNetworkArn (Oracle Database@AWS)

**Claim:** Same ARN confused-deputy shape as CoreNetworkArn, but here the docs are unusually
explicit about the intended cross-account flow, which both clarifies the legitimate design and
sharpens the question of what `CreateRoute` validates.

**Mechanism (doc evidence):**
- ODB networks are explicitly RAM-shareable cross-account, and the ARN is the *required* form for
  referencing a shared one: "When using a resource that is shared, you must provide the Amazon
  Resource Name (ARN)." (`/work/aws-docs/docs/odb/latest/UserGuide/working-with-shared-resources.md:30,38`)
- "You can peer an ODB network in one account and a VPC in another account using AWS RAM. If you
  share an ODB network with another account, the trust account can directly initiate peering."
  (`/work/aws-docs/docs/odb/latest/UserGuide/how-it-works.md:165`)
- The doc gives a worked cross-account example that feeds an ODB network ARN directly into EC2
  `create-route`:
  ```
  aws ec2 create-route --route-table-id rtb-... --destination-cidr-block 10.0.0.0/16 \
      --odb-network-arn arn:aws:odb:us-east-1:111111111111:odb-network/odbnet_...
  ```
  (`/work/aws-docs/docs/odb/latest/UserGuide/working-with-shared-resources.md:192-197`) — note the
  example ARN's account (`111111111111`) is not asserted to equal the caller's account; the
  surrounding text frames this as the normal flow for peering with a *shared* ODB network from a
  "trusted account" that is NOT the owner. This is the clearest documented instance in the whole
  corpus of a cross-account ARN being fed straight into `CreateRoute`.
  - Also note `ODB peering` itself does validate some things: "Validates the network
    configurations, including checking for overlapping CIDR blocks with the Oracle VCN CIDR"
    (`/work/aws-docs/docs/odb/latest/UserGuide/how-it-works.md:178`) — but this is CIDR-overlap
    validation at **peering-connection creation** time, not an EC2-side ownership check on the ARN
    at **route-creation** time. The `create-route --odb-network-arn` step is described as a
    separate, caller-driven step the ODB peering workflow can optionally skip doing for you
    ("You can opt out of providing a VPC route table ID for Create ODB peering connection by
    updating VPC route tables manually using the Amazon EC2 create-route command",
    `how-it-works.md:186`), meaning the ODB service's own validation does not necessarily run at
    all when you call EC2 `CreateRoute` directly.
- Resource-sharing limitation note: "Resource sharing is supported only within the same AWS
  organization." (`working-with-shared-resources.md:21`) — bounds the blast radius to intra-org,
  not fully cross-tenant, but intra-org cross-account confused-deputy is still a real boundary
  (different billing/security domains, different teams).

**Confirm/Refute oracle:** From account Y (same org, but with NO RAM share of ODB network
`odbnet-X` owned by account X), call `ec2 create-route --odb-network-arn
arn:...:odb-network/odbnet-X ...` directly (bypassing `CreateOdbPeeringConnection` entirely, since
the doc says the route step is independent/optional-to-automate). If EC2 accepts the ARN and
creates the route without Y ever having gone through ODB peering/RAM acceptance for that network,
that is a confirmed confused-deputy / isolation bypass — Y's route table would carry a route to a
network Y was never granted access to, and (depending on whether EC2's route resolution actually
requires a live ODB peering attachment to forward packets) may or may not move real traffic, but
even a dangling/validated-at-attach-time reference is a config/IAM confusion worth flagging.

**Severity if true:** High to Critical, same reasoning as CoreNetworkArn, with the added
concreteness that AWS's own docs demonstrate the exact cross-account ARN input in a CLI example.

### 2e. VpcEndpointId (Gateway Load Balancer endpoint)

**Claim (and null result):** Initially flagged as a cross-account lead because the backing
*endpoint service* can be owned by a different account (standard PrivateLink provider/consumer
split). On closer reading this is **not** a route-target ownership problem: the `VpcEndpointId`
accepted by `CreateRoute`/`ReplaceRoute` must be a GWLB **endpoint** that the caller already
created in their own VPC (`CreateVpcEndpoint` against the service) — the endpoint object itself is
always same-account/same-VPC as the route table; only the upstream *service* behind it can be
third-party. Evidence:
- "For each subnet that you specify from your VPC, we create an endpoint network interface in the
  subnet..." (`/work/aws-docs/docs/vpc/latest/privatelink/gateway-load-balancer-endpoints.md:10`)
- "Before you can use the endpoint service the service provider must accept the connection
  requests." (same file, line 26) — i.e., cross-account trust is already gated at endpoint-creation
  time via PrivateLink's own permission/acceptance model, which is a separate, well-documented
  control plane from `CreateRoute`.
- `route-table-options.md:347`: "When using a Gateway Load Balancer endpoint as a target, you
  cannot specify a prefix list as a destination" — the only documented constraint on this target
  type is about destination shape, not ownership.

**Null hypothesis confirmed (by documentation structure, not by live testing):** this specific
target type does not present a novel cross-account route-target risk beyond the already-gated
PrivateLink connection-acceptance flow. Pages checked:
`gateway-load-balancer-endpoints.md`, `create-gateway-load-balancer-endpoint-service.md`,
`vpce-gateway-load-balancer.md` (titles only, not fully read — low remaining signal expected).

---

## 3. LocalTarget reset — intra-VPC isolation implications

**Claim:** Resetting/replacing the local route target is the documented mechanism that lets a
middlebox intercept **all** intra-VPC traffic for a subnet, including traffic to destinations the
subnet owner never explicitly routed anywhere — it silently expands scope from "traffic to a
specific other subnet" to "every packet leaving this subnet that isn't more specifically routed."

**Mechanism (doc evidence):**
- `/work/aws-docs/docs/vpc/latest/userguide/replace-local-route-target.md:7-8`: "You can change the
  target of the default local route. If you replace the target of a local route, you can later
  restore it to the default `local` target." No warning or caveat text in this page about scope
  expansion or isolation impact — it's presented as a purely mechanical procedure (console steps +
  two CLI examples, lines 10-52).
- The *use case* and isolation implication is spelled out one page over, in
  `/work/aws-docs/docs/vpc/latest/userguide/route-table-options.md:263,308-312` ("replace the
  target for the local route with the network interface of the appliance... to ensure that all
  traffic is automatically routed to the appliance, **including traffic destined for subnets that
  you add to the VPC in the future**") — i.e., this is forward-scoping: a subnet created *after*
  the local-route replacement automatically has its inbound-from-this-subnet traffic routed through
  the middlebox too, with no re-confirmation step.
- `intra-vpc-route.md` confirms the three-subnet worked example (A, B inspected via C) uses
  *specific* subnet-CIDR routes rather than a full local-route replacement, i.e. the docs present
  local-route replacement as the "blunter" of two documented options, with the subnet-specific
  route as the more surgical alternative — the choice of which to use is left entirely to the
  operator, no guidance on which is "safer."
- `gateway-route-tables.md:60`: scope of this interception technique is capped at "the same VPC
  only" — cannot be used to pull edge/ingress traffic out to a different VPC's resources, somewhat
  limiting blast radius for the *edge* route table variant, though the *subnet* route table local
  route replacement (via `replace-local-route-target.md`) is a plain EC2 VPC-wide action with no
  equivalent same-VPC assertion needed (replacing a subnet's own local route can only ever target
  something reachable, by definition, inside/adjacent to that same VPC's network fabric — so this
  caveat is structurally moot for the subnet case, only meaningful for the gateway/edge case).

**Confirm/Refute oracle:** Replace the local route of subnet A's route table to point at an
appliance ENI, then add a new subnet D to the VPC *after* the replacement, with no new explicit
route in A's table for D. Verify (per the doc's own claim) that A→D traffic is now also routed
through the appliance without any additional `CreateRoute` call — this would be a config-drift /
implicit-scope-creep finding worth calling out to the client even though AWS's docs present it as
intended behavior rather than a flaw.

**Severity if true (as documented, not a bug but a risk):** Medium — "intended behavior with a
sharp edge": an operator who replaces the local route for a legitimate two-subnet inspection need
may not realize every future subnet they add is automatically captured, until they explicitly
restore the local target. This is a decent example of a genuinely documented configuration-drift
risk (not a confused-deputy or missing-authz bug) worth flagging to the client as a hardening/
review item.

**Null hypothesis:** No cross-account implication was found for LocalTarget specifically — the
replace/restore CLI only accepts `--network-interface-id`/`--local-target` style flags scoped to
the route table's own VPC resources per `replace-local-route-target.md`'s examples; no ARN or
cross-account ID shape is involved in this particular sub-feature. Pages checked:
`replace-local-route-target.md`, `intra-vpc-route.md`, cross-referenced `route-table-options.md`
and `gateway-route-tables.md`.

---

## 4. Route propagation (EnableVgwRoutePropagation) and shared prefix lists

### 4a. EnableVgwRoutePropagation

**Null hypothesis (documented, not inferred):** Unlike every target parameter in Areas 1-2, this
API **does** state an explicit same-VPC cross-check: "The virtual private gateway must be attached
to the same VPC that the routing tables are associated with" and "The routing table must be
associated with the same VPC that the virtual private gateway is attached to."
(`/work/aws-docs/docs/AWSEC2/latest/APIReference/API_EnableVgwRoutePropagation.md:21,26`). No
cross-account route-scope-expansion lead found here — this API only toggles propagation for a VGW
already attached to the caller's own VPC. Page checked:
`API_EnableVgwRoutePropagation.md` (local + confirms parameter list only; no RAM-sharing path for
VGWs was found referenced anywhere in the VPC docs reviewed — VGWs are not RAM-shareable resources
per the corpus searched, unlike TGWs).

### 4b. DestinationPrefixListId — shared managed prefix lists

**Claim:** A customer-managed prefix list can be shared cross-account via RAM; once shared, a
consumer can reference it as a `DestinationPrefixListId` in their own `CreateRoute`/`ReplaceRoute`
calls — but the **owner**, not the consumer, controls the list's contents, and can expand it at any
time without the consumer's route table being touched or re-confirmed. This is a textbook
"someone else controls what my firewall/route rule actually matches" scope-expansion risk, and it
is explicitly, cleanly documented (not a gap — a confirmed, named behavior).

**Mechanism (doc evidence):**
- Sharing is RAM-based, to specific accounts, OUs, or whole orgs, **inside or outside** the
  sharer's own AWS Organization: "the owner of a customer-managed prefix list can share the prefix
  list with... Specific AWS accounts inside or outside of its organization in AWS Organizations...
  An entire organization in AWS Organizations." (`/work/aws-docs/docs/vpc/latest/userguide/sharing-managed-prefix-lists.md:8-11`)
  — note this is **broader** than ODB's "same org only" restriction (§2d) and broader than the
  TGW RAM examples shown, making prefix lists the most permissive cross-tenant sharing surface in
  this whole target set.
- Consumer capability: "Consumers can view the entries in a shared prefix list, and they can
  reference a shared prefix list in their AWS resources. However, consumers can't modify, restore,
  or delete a shared prefix list." (`/work/aws-docs/docs/vpc/latest/userguide/sharing-perms.md:14-16`)
  — confirms the consumer's route literally inherits content it cannot control or audit-lock.
- Owner capability / the scope-expansion vector itself: owners "are responsible for managing a
  shared prefix list and its entries" and explicitly **cannot** be stopped by a consumer from
  updating it: "they cannot add or remove references to a prefix list in AWS resources that are
  owned by consumers" (i.e., the owner can't touch the consumer's *route table association*, but
  nothing in this sentence or anywhere else restricts the owner from changing the list's *CIDR
  entries themselves*). (`/work/aws-docs/docs/vpc/latest/userguide/sharing-perms.md:8-12`)
- Confirmed propagation-without-re-confirmation: "If you update the prefix list to a new version,
  the references use the latest version" — stated even for the *unshare* case: "If the prefix list
  is already referenced in the consumer's resources, those references continue to function as
  normal... If you update the prefix list to a new version, the references use the latest
  version." (`/work/aws-docs/docs/vpc/latest/userguide/work-with-shared-prefixes.md:48`) This is the
  clearest documented statement that an owner-side content change silently and immediately changes
  what the consumer's route actually matches, with no consumer action, approval, or notification
  step documented anywhere.
- Sharing itself is one-hop only (no re-sharing): "To share a prefix list, you must own it. You
  cannot share a prefix list that has been shared with you."
  (`/work/aws-docs/docs/vpc/latest/userguide/work-with-shared-prefixes.md:30`) — bounds transitive
  risk but does not reduce the core owner-controls-consumer's-route-scope finding.
- GWLB-endpoint interaction note (cross-reference to §2e): you *cannot* combine a shared prefix
  list with a GWLB-endpoint target — "Cannot create or replace a prefix list route targeting a VPC
  Endpoint." (`/work/aws-docs/docs/vpc/latest/userguide/route-table-options.md:347`) — narrows
  where this specific confused-deputy shape can land (no prefix-list-into-GWLB chaining), but
  leaves TGW/NAT/ENI/peering targets all paired with prefix-list destinations as documented,
  supported patterns (`route-table-options.md:317-330` shows exactly this: `pl-123abc...` →
  `{{tgw-id}}`).

**Confirm/Refute oracle:** This one doesn't need a live-test oracle — it's a directly documented,
named AWS behavior, not a silence-based inference. The "test" for the pentester is really a
blast-radius exercise: enumerate, for the target account, which route tables reference a
`pl-...` whose `OwnerId` (per `describe-managed-prefix-lists`,
`/work/aws-docs/docs/vpc/latest/userguide/work-with-shared-prefixes.md:74`) is a foreign account,
and treat the owner of that prefix list as having a standing, silent write capability into the
effective reachability of every route table that references it.

**Severity if true (as documented — this is a confirmed finding, not a hypothesis):** Medium-High,
context-dependent on what the route's target is (e.g., a prefix-list-gated route to a NAT gateway
or TGW with broad reachability is worse than one gated to a narrow VPC endpoint). This is the one
finding in this document that doesn't need "if true" framing — AWS's own docs assert the owner
can expand route-match scope for a consumer's traffic without the consumer's participation, by
design.

---

## Null Hypotheses (explicit)

1. **No account/ownership-check language exists for any ReplaceRoute/CreateRoute target
   parameter**, across both API reference pages, checked against both the offline mirror and the
   live page (verbatim match confirmed via WebFetch for CreateRoute). This is a doc-silence null
   result for *all* targets equally — it is not evidence of a missing check, only evidence that
   the check (if any) is undocumented. Flagged per-target above with likelihood estimates based on
   adjacent documented behavior (TGW/peering: likely gated by attachment-existence, inferred, not
   stated; CoreNetworkArn/OdbNetworkArn: no adjacent statement to infer a fallback from).
2. **VpcEndpointId (GWLB) is NOT a cross-account route-target risk** — confirmed by doc structure:
   the endpoint object is always created in, and owned by, the same account/VPC as the route
   table; only the upstream service can be third-party, and that trust boundary is gated by
   PrivateLink's separate, well-documented connection-acceptance flow, not by `CreateRoute`. Pages
   checked: `gateway-load-balancer-endpoints.md`, `create-gateway-load-balancer-endpoint-service.md`.
3. **EnableVgwRoutePropagation has no cross-account route-scope-expansion issue** — it is the one
   API in this whole area with an explicit, documented same-VPC cross-check. Page checked:
   `API_EnableVgwRoutePropagation.md`. No VGW RAM-sharing path was found in the corpus searched
   (`vpc-sharing.md`, `vpc-share-limitations.md`, `working-with-transit-gateways.md`), suggesting
   VGWs (unlike TGWs) are not a RAM-shareable resource at all — unlike TGW, so the confused-deputy
   shape doesn't apply to VGW route propagation the way it might to TGW attachments.
4. **LocalTarget reset has no cross-account dimension** — only same-VPC resource IDs appear in its
   CLI surface; the risk here is config-drift/scope-creep (Medium), not confused-deputy. Pages
   checked: `replace-local-route-target.md`, `intra-vpc-route.md`.
5. **Shared-VPC-subnet participants cannot call ReplaceRoute/CreateRoute at all** on the owner's
   route tables (`vpc-share-limitations.md:46-47`), which closes off the most obvious
   literal-cross-account-IAM-principal route-hijack vector for that specific sharing model — but
   says nothing about same-account IAM principals with narrowly scoped `ec2:*Route*` permissions
   pointing at resources (ENIs, etc.) owned by *other IAM principals in the same account*, which
   remains open (see Area 1 oracle).

## Strongest leads, ranked

1. **CoreNetworkArn (§2c)** — zero documented validation, zero worked example in either API page,
   explicitly ARN-shaped (classic confused-deputy input). Top priority for live testing.
2. **OdbNetworkArn (§2d)** — same shape as CoreNetworkArn, but AWS's own docs hand you a working
   cross-account CLI example (`create-route --odb-network-arn arn:aws:odb:...:111111111111:...`)
   and state the route-table step can bypass the ODB peering service's own CIDR-overlap validation
   entirely when called directly against EC2. Second priority.
3. **Shared managed prefix lists (§4b)** — not a hypothesis, a confirmed documented behavior: the
   prefix-list owner has a standing, silent write capability into any route table that references
   their shared list, including accounts outside their own AWS Organization. Worth flagging as a
   governance/blast-radius finding regardless of live-test results.
4. **ENI/appliance route hijack via IAM-scoped ec2:*Route* permissions (§1)** — the
   "route-content gap": no documented check that a `NetworkInterfaceId`/appliance target in
   `CreateRoute`/`ReplaceRoute` belongs to the calling principal, for both intra-VPC local-route
   replacement and internet-gateway/VGW edge route tables. Needs a live IAM-permission-boundary
   test to confirm it's a real gap and not just undocumented.
5. **TransitGatewayId / VpcPeeringConnectionId (§2a/2b)** — most likely null results (attachment/
   peering-association almost certainly gates these in practice) but worth a quick live check since
   the docs never say so explicitly.
