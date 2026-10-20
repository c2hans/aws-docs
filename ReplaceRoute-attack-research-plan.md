# EC2 VPC Route Table (ReplaceRoute) API Family — Attack Research Plan

**Source of leads:** Local mirror `/work/aws-docs` + live `docs.aws.amazon.com` (every `.html` cross-checked against its `.md` twin to rule out local sync drift). Anchor page: `https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_ReplaceRoute_section.html` (a thin CLI/PowerShell code example). Primary evidence pulled from:
- `docs/AWSEC2/latest/APIReference/`: `API_ReplaceRoute.md`, `API_CreateRoute.md`, `API_DeleteRoute.md`, `API_CreateRouteTable.md`, `API_AssociateRouteTable.md`, `API_ReplaceRouteTableAssociation.md`, `API_EnableVgwRoutePropagation.md`, `API_CreateRouteServer*.md`
- `docs/service-authorization/latest/reference/list_ec2.md` (authoritative IAM action / condition-key / resource tables; ~137 EC2 condition keys at `10036-10189`)
- `docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md`, `supported-iam-actions-tagging.md`
- `docs/vpc/latest/userguide/`: `route-table-options.md`, `route-tables-priority.md`, `replace-local-route-target.md`, `gateway-route-tables.md`, `igw-ingress-routing.md`, `middlebox-routing-examples.md`, `associate-route-table-gateway.md`, `managed-prefix-lists.md`, `sharing-managed-prefix-lists.md`, `work-with-shared-prefixes.md`, `sharing-perms.md`, `vpc-share-limitations.md`, `vpc-policy-examples.md`, and the full `route-server-*` set (`dynamic-routing-route-server.md`, `route-server-how-it-works.md`, `route-server-iam.md`, `route-server-terms.md`, `route-server-peer-logging.md`, `route-server-tutorial-*.md`)
- `docs/odb/latest/UserGuide/working-with-shared-resources.md` (cross-account `create-route` example)
- AWS-managed / sample policies: `AmazonVPCFullAccess.md`, `AmazonEKSClusterPolicy.md`, `NetworkAdministrator.md`, `AmazonVPCCrossAccountNetworkInterfaceOperations.md`

**Status:** Documentation-derived hypotheses only. Nothing has been tested against a live AWS account. Each lead is falsifiable with a stated oracle; a hunter must confirm empirically in an authorized account.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5). Look left and right for adjacent bugs.
- **Scope reality:** this is an EC2 control-plane **mutating** API family that edits a *VPC-level forwarding table* — the thing that decides, per destination CIDR, which next-hop (gateway / ENI / NAT / peering / TGW / core-network / ODB-network / prefix-list) a packet takes. The `route-table` ARN (`arn:${Partition}:ec2:${Region}:${Account}:route-table/${RouteTableId}`, `list_ec2.md:9992`) embeds the account → **cross-account resource access via a foreign `RouteTableId` is architecturally bounded and treated here as a genuine null hypothesis** (Section 8). The live-value leads are therefore (a) IAM authorization-granularity gaps that let a route redirect traffic the policy author never meant to expose, (b) *cross-account trust in the route **target*** (bare-ARN `CoreNetworkArn`/`OdbNetworkArn`, RAM-shared prefix lists/TGW/peering), (c) the **route-server / BGP** dynamic-routing surface (NEW), and (d) several **AWS-authored** weak IAM artifacts.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to AWS's **own service plane**, stop immediately, preserve evidence, flag for AWS-Security disclosure. (Not expected for this customer-plane API family, but the rule stands — especially when probing `CoreNetworkArn`/`OdbNetworkArn` cross-account behavior.)
- **Dummy-data / read-only discipline:** confirm existence of a boundary gap, never exploit beyond it. Mutating a route changes live traffic forwarding — a hunter must operate only in a disposable test VPC it owns, with synthetic subnets/ENIs, send only canary traffic, and restore/tear down every route, route table, prefix list, route server, and ENI it creates.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. **Route-content escape (anchor):** Prove that a principal authorized to `ec2:ReplaceRoute`/`ec2:CreateRoute` on a specific route table can install a route the policy author intended to forbid — specifically, point a destination CIDR (or the **local** route covering the whole VPC CIDR) at an **attacker-controlled ENI / NAT / GWLB endpoint** to intercept or black-hole traffic — i.e., that IAM cannot bound the route *target* or *destination*.
2. **Traffic interception / MITM:** Prove that redirecting a subnet's (or an edge/gateway route table's inbound) traffic through an attacker ENI succeeds with only route-table-scoped permission and no check that the ENI belongs to the caller.
3. **Second-path redirect:** Prove that a principal denied `ReplaceRoute` on a route table can still change a subnet's effective forwarding via `ReplaceRouteTableAssociation` (swap the subnet onto a permissive table) — the "govern one action, miss the twin" gap.
4. **Cross-account target trust:** Determine whether `CreateRoute`/`ReplaceRoute` validates, at call time, that `CoreNetworkArn`/`OdbNetworkArn` and RAM-shared `TransitGatewayId`/`VpcPeeringConnectionId`/prefix-list targets are owned-by / shared-to the caller — or only that they exist.
5. **Shared-prefix-list silent scope expansion:** Confirm that a route whose destination is a RAM-shared managed prefix list can have its matched address space silently widened by the (foreign) list owner with no consumer action.
6. **Route-server / BGP route injection (NEW surface):** Determine who can establish a route-server BGP peer and whether a peer (or a compromised appliance) can advertise arbitrary / more-specific prefixes that get installed into subnet route tables, overriding operator static routes (longest-prefix-match hijack), and whether peering authenticates (MD5/TTL).
7. **AWS-authored artifact weakness:** Confirm that the shipped `route-server-iam.md` "least-privilege" example and the named managed policies (`AmazonVPCFullAccess`, `AmazonEKSClusterPolicy`, `NetworkAdministrator`, `AmazonVPCCrossAccountNetworkInterfaceOperations`) grant the route family (and, for route-server, account-wide SG/ENI tampering) on `Resource:"*"` with no condition (uneditable / copy-verbatim AWS defects → Tier 2 disclosure).
8. **Condition-key scoping no-ops + ABAC self-widening:** Prove `ec2:RouteTableID` on `CreateRouteTable` resolves to `*`, the multi-resource `ec2:Vpc` pitfall on `ReplaceRouteTableAssociation`, and tag self-stamping via `CreateTags` on `route-table`.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 Query/JSON API over HTTPS (`https://ec2.<region>.amazonaws.com/`), SigV4 IAM auth, API version `2016-11-15`. Reached via CLI (`aws ec2 replace-route`), PowerShell (`Set-EC2Route`), all language SDKs, console. No non-SDK/internal API in the classic route family. The **route-server** family (`CreateRouteServer`/`CreateRouteServerEndpoint`/`CreateRouteServerPeer`, `list_ec2.md:668-677`) is newer and less-trodden.

**The managed asset: a VPC forwarding table.** A **route table** is an ordered-by-specificity set of routes; each route maps a *destination* (`DestinationCidrBlock` IPv4 / `DestinationIpv6CidrBlock` IPv6 / `DestinationPrefixListId` managed prefix list) to exactly one *target*. `ReplaceRoute` overwrites the target of an existing destination-matched route (`API_ReplaceRoute.md`). Targets: internet GW / virtual private GW (`GatewayId`), `EgressOnlyInternetGatewayId`, `NatGatewayId`, NAT `InstanceId`, `NetworkInterfaceId` (ENI), `TransitGatewayId`, `LocalGatewayId` (Outposts), `CarrierGatewayId` (Wavelength), `VpcPeeringConnectionId`, `VpcEndpointId` (GWLB endpoint only), `CoreNetworkArn` (Cloud WAN), `OdbNetworkArn` (Oracle Database@AWS), or `LocalTarget=true` to reset the default `local` route. The **local route** covers the entire VPC CIDR and — per `replace-local-route-target.md:37-42` — its target **can be replaced with an arbitrary ENI**.

**Resource identifiers.**
- `route-table` → `rtb-xxxxxxxxxxxxxxxxx`; ARN `arn:${Partition}:ec2:${Region}:${Account}:route-table/${RouteTableId}` (`list_ec2.md:9992`). **Account-scoped.**
- An association → `rtbassoc-xxxx` (opaque; not a standalone IAM resource — authorized via its route-table + subnet/gateway).
- A *route* is **not** an addressable IAM resource: it is identified only by (`RouteTableId`, destination) and carries a target field — none of which IAM can condition on.

**Identity / ownership.** Pure SigV4 IAM for the control plane. No service account, no multi-tenant shared fleet, no credential vending in the classic family. **Trust crosses accounts in two places:** (i) the route **target** may be a resource shared from or owned by another account (bare-ARN core/ODB networks, RAM-shared TGW/peering/prefix-lists); (ii) the **route-server BGP peer** is a data-plane device whose advertised prefixes become control-plane routes. The data plane (actual packet forwarding) is where the impact lands: a mis-authorized route silently re-points live traffic.

**Pipeline (control-plane edit → data-plane effect):**

```
Principal (SigV4) ──► EC2 API frontend ──► IAM authorization ──► route-table store ──► VPC data-plane forwarding
                                               │                      │                        │
             authorizes by: action +           │                      ▼                        ▼
             route-table ARN/ID/tag/VPC;        │        route set: {destination → target}   packets to dest CIDR
             CANNOT authorize by destination    │                      ▲                   go to chosen next-hop
             CIDR or by target (ENI/NAT/ARN/...) │                      │                   (ENI = interceptable)
                                                 │     ┌────────────────┴─────────────────┐
                                                 │     │ route-server (NEW): BGP peer      │
                                                 │     │ advertises prefix → FIB → installs│
                                                 │     │ route w/ advertiser ENI as nexthop│
                                                 └─────┴───────────────────────────────────┘
```

Decisive design fact: **IAM authorization granularity stops at the route-table object; it does not reach the destination CIDR or the target.** Once a principal is authorized against a route-table ARN, it may install *any* destination → *any* reachable target.

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Principal scoped to a route-table *object* | The *target* of a route (ENI/NAT/GWLBe/ARN) | `ReplaceRoute`/`CreateRoute` sets a target IAM never inspects | Installing a route whose target the policy intended to forbid (e.g. the local route → attacker ENI) succeeds — IAM never saw the target. **Confirmed-by-docs gap (A1); live test = demonstrating no policy can stop it.** |
| A subnet's legitimate traffic | An attacker-controlled ENI/appliance | Replace local route or add more-specific route → ENI | Canary traffic from the subnet arrives at the attacker ENI (interception / MITM). No doc check that the ENI is caller-owned. |
| Principal denied `ReplaceRoute` on table A | The subnet's effective forwarding | `ReplaceRouteTableAssociation` re-points subnet to permissive table B | Subnet forwarding changes without any `*Route` (entry) permission. |
| Caller account | A route **target** in another account | bare-ARN `CoreNetworkArn`/`OdbNetworkArn`; RAM-shared `TransitGatewayId`/`VpcPeeringConnectionId`/prefix list | `CreateRoute`/`ReplaceRoute` accepts a target the caller does not own / was not shared, or acts without a documented ownership check. |
| Foreign prefix-list **owner** | Consumer's route match-set | RAM-shared `DestinationPrefixListId`; "references use latest version" | Owner expands the list → consumer's route silently matches new address space, no consumer action. |
| Route-server **BGP peer** (data plane) | Subnet route tables (control plane) | Peer advertises prefix → route server installs into FIB → route table | A peer gets an arbitrary / more-specific prefix installed, overriding an operator static route (LPM hijack). No documented prefix-ownership/authorization check; no documented MD5/TTL auth. |
| Principal w/ tag-gated route mutation + `CreateTags` | The ABAC gating tag | `CreateTags` on `route-table` then satisfy `aws:ResourceTag` | Self-stamping the gate tag onto a same-account route table, then mutating it. |
| Naïve policy author's intent | Actual runtime scoping | `ec2:RouteTableID` on `CreateRouteTable`; multi-resource `ec2:Vpc` on `ReplaceRouteTableAssociation` | The key resolves to `*` / skips a resource leg → broader than written. |
| Principal in account X | route-table `rtb-*` in account Y | Any route action with a foreign `RouteTableId` | **Genuine null** — ARN embeds account; foreign ID won't resolve. Record, do not pursue. |
| Any customer surface | AWS service plane | — | **HARD STOP** if ever reached (watch during core/ODB-ARN probing). |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Facing | Required IAM resource(s) | Target/CIDR-scopable? | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| ReplaceRoute | Query/SDK | **Yes** | External | `route-table*` only | **No** (A1) | `ec2:ReplaceRoute` | Conds: `aws:ResourceTag`,`ec2:Region`,`ec2:ResourceTag`,`ec2:RouteTableID`,`ec2:Vpc` (`list_ec2.md:9431-9435`). Can replace the **local** route target → whole-VPC redirect. |
| CreateRoute | Query/SDK | **Yes** | External | `route-table*` only | **No** (A1) | `ec2:CreateRoute` | Same 5 keys (`list_ec2.md:5403-5407`). Adds a route; more-specific destination wins (priority). |
| DeleteRoute | Query/SDK | **Yes** | External | `route-table*` only | partial (no target/CIDR key) | `ec2:DeleteRoute` | Removing a route = black-hole / fail-over of that destination (`list_ec2.md:6118-6122`). |
| ReplaceRouteTableAssociation | Query/SDK | **Yes** | External | `route-table*` **and** `subnet` (+ `internet-gateway`/`vpn-gateway`/pools legs) | n/a | `ec2:ReplaceRouteTableAssociation` | `ec2:Vpc` on **two** legs → multi-resource condition pitfall (A5). Swaps the whole table under a subnet/gateway (`list_ec2.md:9437-9445`). |
| AssociateRouteTable | Query/SDK | **Yes** | External | `route-table*` + `subnet`/gateway | n/a | `ec2:AssociateRouteTable` | **Same action used for subnet AND edge/gateway association** → edge table can redirect all inbound VPC traffic; no distinguishing condition key (Area 3). |
| CreateRouteTable | Query/SDK | **Yes** | External | `route-table*` + `vpc*` | n/a | `ec2:CreateRouteTable` | `ec2:RouteTableID` here resolves to `*` at runtime (A5a, `iam-policies-for-amazon-ec2.md:270,305`). Tag-on-create. |
| EnableVgwRoutePropagation | Query/SDK | **Yes** | External | `route-table*` + `vpn-gateway` | n/a | `ec2:EnableVgwRoutePropagation` | **The one route API with a documented same-VPC cross-check** (`API_EnableVgwRoutePropagation.md:21,26`) — contrast with CreateRoute/ReplaceRoute targets. |
| CreateRouteServer / ...Endpoint / ...Peer | Query/SDK | **Yes** | External | (route-server resource types) | n/a | `ec2:CreateRouteServer*` | **NEW** dynamic-routing surface. BGP peer → routes injected into tables (Area 4). |
| DescribeRouteTables | Query/SDK | No | External | **none** (only `ec2:Region`) | n/a | `ec2:DescribeRouteTables` | **No resource-level read scoping** (`list_ec2.md:7308-7312`); account/region-bounded only. |

No classic-family `[NEW]` markers; the **route-server family is the new/less-reviewed surface** and is prioritized. The entire attack value is the *authorization-granularity delta* (IAM can't bound destination/target), *cross-account target trust*, *route-server injection*, and *AWS-authored artifact weakness* — not surface discovery.

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — IAM cannot constrain the route *target* or *destination* → traffic redirection/interception *(highest value; anchor finding)*
**Background.** `CreateRoute`/`ReplaceRoute`/`DeleteRoute` each take exactly **one** IAM resource type, `route-table*`, with only 5 condition keys (`aws:ResourceTag`, `ec2:Region`, `ec2:ResourceTag`, `ec2:RouteTableID`, `ec2:Vpc`) — `list_ec2.md:5403-5407, 9431-9435, 6118-6122`. The destination (`DestinationCidrBlock`/`DestinationIpv6CidrBlock`/`DestinationPrefixListId`) and target (`GatewayId`,`NatGatewayId`,`NetworkInterfaceId`,`TransitGatewayId`,`VpcPeeringConnectionId`,`CoreNetworkArn`,`OdbNetworkArn`,`EgressOnlyInternetGatewayId`,`LocalGatewayId`,`CarrierGatewayId`,`VpcEndpointId`) are plain API request parameters never bound to any IAM key.
**Security Concern.** A full sweep of EC2's ~137 condition keys (`list_ec2.md:10036-10189`) found **no** key for a route's destination or target. So once a principal is authorized against a route-table ARN, it may install **any** destination → **any** reachable target — including pointing the **local route** (whole VPC CIDR) at an attacker ENI to intercept all intra-VPC east-west traffic (`replace-local-route-target.md:37-42`, worked CLI example redirects `10.0.0.0/16` → `eni-...`), or a middlebox ENI/NAT/GWLBe (`route-table-options.md:218, 263-267, 308-312`). The docs state no check that the target ENI belongs to the calling principal (only that it exists/is attached).
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* A least-privilege policy intending "this role may manage route table `rtb-X` but must never expose its subnets to an arbitrary appliance" cannot be expressed. → *Oracle:* author the most restrictive IAM policy you can for `ec2:ReplaceRoute` on `rtb-X`; confirm it still permits `--destination-cidr-block 0.0.0.0/0 --network-interface-id <attacker-eni>` **and** `--local-target`-replacement to an ENI. Refuted only if some condition key blocks it (none found). → *Severity:* **High** (within-account traffic interception / least-privilege ceiling; the policy author cannot bound blast radius).
- *Claim:* The ENI target is not ownership-checked against the caller. → *Oracle:* in a single owned account with two IAM principals, principal P (route-table perms only) points a route at an ENI created/controlled by a different principal; canary traffic reaches that ENI.
- *Claim:* `DeleteRoute` lets the same principal black-hole a destination (DoS / forced fail-over) with the same coarse authorization.
**Doc evidence:** `list_ec2.md:5403-5407, 9431-9435, 6118-6122, 10036-10189`; `replace-local-route-target.md:37-42`; `route-table-options.md:213-312`. **Severity-if-true:** High. **Stop condition:** once you demonstrate no policy expresses the target/destination restriction and one ENI redirect intercepts canary traffic, the gap is proven; do not enumerate every target type.

### Area 2 — Cross-account trust in the route *target* (bare-ARN & RAM-shared) *(Lens A/B confused-deputy)*
**Background.** Two targets are **bare ARNs** with the least documentation of any parameter: `CoreNetworkArn` (Cloud WAN) and `OdbNetworkArn` (Oracle Database@AWS). `API_CreateRoute.md:31-34` / `API_ReplaceRoute.md:24-27` give `CoreNetworkArn` zero constraint text and zero worked example. For `OdbNetworkArn`, AWS's own docs (`odb/latest/UserGuide/working-with-shared-resources.md:192-197`) show a **"trust account" (not the owner)** calling `aws ec2 create-route --odb-network-arn arn:aws:odb:us-east-1:111111111111:odb-network/...` against a RAM-shared ODB network, and imply the CIDR-overlap validation that `CreateOdbPeeringConnection` performs is a *separate, optional* step the direct EC2 `create-route` path may not inherit. `TransitGatewayId`/`VpcPeeringConnectionId` and managed prefix lists can be RAM-shared across accounts (and prefix lists even outside the Organization — `sharing-managed-prefix-lists.md:8-11`).
**Security Concern.** Bare-ARN inputs the service dereferences/acts on are the classic confused-deputy shape. If `CreateRoute`/`ReplaceRoute` validates only *existence* (not account ownership / that the core/ODB network edge is attached to the caller's VPC), a caller could wire routing to a resource in another account, or the CIDR-overlap safety check could be bypassed by calling EC2 directly.
**High-level Test Scenarios:**
- *Claim:* `CreateRoute --core-network-arn <arn-in-another-account>` is accepted without an attachment/ownership check. → *Oracle:* attempt with a core network ARN not attached to the caller's VPC; `AccessDenied`/`InvalidParameter` = refuted (enforced), `200` = confirmed. **If the accepted ARN resolves to an AWS-owned/service core network, HARD STOP and disclose.**
- *Claim:* The ODB CIDR-overlap validation is skippable via direct `ec2:create-route`. → *Oracle:* follow `working-with-shared-resources.md:192-197` but with an overlapping/foreign CIDR; observe whether the route installs without the `CreateOdbPeeringConnection` validation.
- *Claim:* RAM-shared TGW/peering targets are accepted without a documented call-time association check. → *Oracle:* reference a TGW/peering shared-but-not-associated to the caller's VPC; likely enforced in practice but undocumented — quick live check.
**Doc evidence:** `API_CreateRoute.md:31-34`, `API_ReplaceRoute.md:24-27`; `odb/.../working-with-shared-resources.md:192-197`; `sharing-managed-prefix-lists.md:8-11`. **Severity-if-true:** cross-account routing to an unowned target = **High**; service-plane core network = **Critical + hard stop**. **Stop:** one accept/deny observation per target settles it.

### Area 3 — Twin-action / second-path parity: route edit vs re-association vs edge association *(Lens X)*
**Background.** Several independent IAM actions change a subnet's effective forwarding: `ec2:ReplaceRoute`/`ec2:CreateRoute`/`ec2:DeleteRoute` (edit routes in place), and `ec2:ReplaceRouteTableAssociation`/`ec2:AssociateRouteTable` (swap the whole table). Crucially, the **same `ec2:AssociateRouteTable` action associates a table to a subnet AND to an internet/virtual-private gateway (edge/ingress routing)**, and an edge table can redirect **all inbound** VPC traffic to a middlebox ENI (`gateway-route-tables.md:51-65`, `associate-route-table-gateway.md`, `igw-ingress-routing.md`). AWS applies a *shape* constraint (a gateway-associable table may only hold local/ENI/GWLBe targets, no propagation — `gateway-route-tables.md:60`), which is **not an identity/authorization constraint**.
**Security Concern.** A policy that locks down `ReplaceRoute` on a sensitive table does nothing to the association actions; a principal holding only `ReplaceRouteTableAssociation`/`AssociateRouteTable` can re-point the subnet (or the gateway) onto a permissive/attacker table and achieve the same redirect. No condition key distinguishes "associate my table to my subnet" from "associate it to the VPC's internet gateway."
**High-level Test Scenarios:**
- *Claim:* Deny all `ec2:*Route` (entry) on table T but leave `ec2:ReplaceRouteTableAssociation` → the subnet's forwarding can still be fully changed by swapping tables. → *Oracle:* with that policy, `ReplaceRouteTableAssociation` re-points the subnet to a permissive table; canary traffic follows the new table.
- *Claim:* `ec2:AssociateRouteTable` lets a principal install an **edge/ingress** route table that routes inbound internet traffic through an attacker ENI, with no condition key distinguishing edge association. → *Oracle:* `SimulatePrincipalPolicy` shows no key separates subnet vs gateway association; live, the gateway association succeeds and intercepts inbound canary traffic.
**Doc evidence:** `list_ec2.md:9437-9445`; `gateway-route-tables.md:51-65`; `igw-ingress-routing.md`; `associate-route-table-gateway.md`. **Severity-if-true:** Medium–High (control bypass; High for inbound-edge interception). **Stop:** once a single policy shows the divergence and one association redirect lands.

### Area 4 — Route Server / BGP dynamic-route injection *(NEW surface — Lens N + F/K influence + U)*
**Background.** VPC Route Server (`route-server-*`) lets a BGP-speaking device in the VPC advertise prefixes that the route server installs into subnet route tables with the advertiser's **ENI as next hop** (`route-server-how-it-works.md:40-44` worked example: a lower-MED peer swings a subnet-wide FIB entry). A "route server peer" is defined by purely network-layer criteria (has an ENI, speaks BGP, can initiate a session — `route-server-terms.md`); the doc set states **no ownership/authorization check on which prefixes a peer may advertise** and **no BGP MD5/TTL session authentication**.
**Security Concern.** This is the untrusted-input → routing-action seam. A compromised appliance (or a principal who can create a peer) can advertise an arbitrary or **more-specific** prefix; by longest-prefix-match it silently overrides the operator's static route for that sub-range (see Area 5). Secondary: a shared ~100-route-per-route-server quota (a malicious peer can evict legitimate routes → DoS), and `persist-routes` (up to 5 min) keeps an injected route alive after the attacker's BGP session drops.
**High-level Test Scenarios:**
- *Claim:* A route-server peer can advertise a prefix it does not "own" and have it installed, redirecting traffic. → *Oracle:* stand up a route server + peer in an owned VPC; advertise a more-specific prefix covering a victim destination; confirm the route table installs it with the peer ENI as next hop and canary traffic diverts. Refuted if the service filters advertised prefixes by an ownership/allow-list.
- *Claim:* No MD5/TTL authentication protects the BGP session (spoofable peer). → *Oracle:* inspect peer config options; absence of an auth key = confirmed as documented gap (flag for live validation).
- *Claim:* Route eviction / `persist-routes` abuse. → *Oracle:* advertise >quota routes and observe legitimate-route eviction; drop the session and confirm the injected route persists.
**Doc evidence:** `route-server-how-it-works.md:40-44`; `route-server-terms.md`; `route-server-peer-logging.md`; `route-tables-priority.md`. **Severity-if-true:** intra-VPC traffic hijack/DoS = **High**. **Stop:** once one advertised prefix installs and diverts canary traffic. **Note:** route-server-origin routes' rank among the listed propagation tiers (DX/VPN/VGW) is **undocumented** — a genuine evidence gap, confirm empirically.

### Area 5 — Longest-prefix-match hijack & route-priority integrity *(Lens X/U)*
**Background.** `route-tables-priority.md:8` states verbatim: "we direct traffic using the most specific route" and (`:68`) "more specific routes always take priority irrespective of whether they are propagated routes, static routes, or routes that reference prefix lists." Static routes beat propagated routes for identical destinations (`:44-52`).
**Security Concern.** Any actor who can insert a **more-specific** route (via Area 1 static route, Area 2 shared prefix list, or Area 4 BGP advertisement) silently overrides a legitimate broader route for that sub-range — a destination hijack the operator's existing static route cannot defend against (it is less specific).
**High-level Test Scenarios:**
- *Claim:* A `/32` (or longer-prefix) route to an attacker ENI overrides the operator's `/16` route to the correct target for that single address. → *Oracle:* install both; confirm traffic to the `/32` address goes to the attacker ENI while the rest follows the `/16`.
- *Claim (shared prefix list):* A RAM-shared `DestinationPrefixListId` route has its match-set silently widened by the foreign owner. → *Oracle:* `sharing-perms.md:8-16`, `work-with-shared-prefixes.md:48` confirm "references use the latest version" with no consumer action; live, the owner adds a CIDR and the consumer's route begins matching it. → *Severity:* Medium–High (cross-account silent route-scope expansion).
**Doc evidence:** `route-tables-priority.md:8,44-52,68`; `sharing-perms.md:8-16`; `work-with-shared-prefixes.md:48`. **Severity-if-true:** Medium–High. **Stop:** one override demonstration per vector.

### Area 6 — AWS-authored IAM-artifact weaknesses *(Lens R — in-scope, Tier 2 disclosure)*
**Background (two classes).**
- **(6a) Route-server sample policy is broken AND over-permissive.** `route-server-iam.md:15-79` (verified byte-identical mirror↔live) presents the "required IAM permissions" example where Sids `CreateRouteServer`/`DeleteRouteServer` map to `sns:CreateTopic`/`sns:DeleteTopic` (not any `ec2:*RouteServer*` action actually used in the tutorial — functionally broken), while `CreateRouteServerEndpoint`/`DeleteRouteServerEndpoint` grant `ec2:CreateNetworkInterface`, `ec2:CreateNetworkInterfacePermission`, `ec2:CreateSecurityGroup`, `ec2:AuthorizeSecurityGroupIngress`, `ec2:DeleteNetworkInterface`, `ec2:DeleteSecurityGroup` and `CreateRouteServerPeer`/`DeleteRouteServerPeer` grant `ec2:AuthorizeSecurityGroupIngress`/`RevokeSecurityGroupIngress` — **all on `Resource:"*"` with zero condition keys**. AWS's own "least-privilege" example for creating a BGP peer confers account-wide security-group tampering and ENI creation.
- **(6b) Named managed/sample policies grant the route family on `Resource:"*"` unconditioned.** `AmazonVPCFullAccess.md:39-198` (full route family); `AmazonEKSClusterPolicy.md:39-104` (`CreateRoute`/`DeleteRoute`, attached to **every EKS cluster service role**); `NetworkAdministrator.md:39-214, 217-250`; `AmazonVPCCrossAccountNetworkInterfaceOperations.md:37-49` (`CreateRoute`/`DeleteRoute`/`ReplaceRoute`, `Resource:["*"]`); and the tutorial `vpc-policy-examples.md:112-142`.
**Security Concern.** These are AWS-authored, copied/attached verbatim and uneditable (managed) — a weak default is AWS's defect, not a customer footgun. A principal holding any of them can redirect/black-hole **any** route table account-wide (Areas 1/3/5), and the route-server example additionally grants account-wide SG/ENI manipulation.
**High-level Test Scenarios:**
- *Claim:* A role holding only `AmazonEKSClusterPolicy` can `CreateRoute`/`DeleteRoute` on a route table unrelated to any EKS resource. → *Oracle:* `iam:SimulatePrincipalPolicy` for `ec2:CreateRoute` on an arbitrary account route-table ARN under that policy → `allowed` (safe, no resources touched; escalate to a live scoped call only on canary tables you own).
- *Claim:* A role holding the `route-server-iam.md` "CreateRouteServerPeer" statement can `AuthorizeSecurityGroupIngress` on an unrelated security group. → *Oracle:* `SimulatePrincipalPolicy` → `allowed`.
**Doc evidence:** `route-server-iam.md:15-79`; `AmazonVPCFullAccess.md:39-198`; `AmazonEKSClusterPolicy.md:39-104`; `NetworkAdministrator.md:39-214,217-250`; `AmazonVPCCrossAccountNetworkInterfaceOperations.md:37-49`; `vpc-policy-examples.md:112-142`. **Severity-if-true:** over-broad AWS-authored grant → route `aws-security`, **Tier 2**: account-wide route control = Medium–High; route-server SG/ENI tampering = Medium–High. **Stop:** Simulate-allow is sufficient proof.

### Area 7 — Condition-key scoping no-ops + ABAC self-widening *(Lens S / I)*
**Background & Concern.**
- **(7a) `ec2:RouteTableID` on `CreateRouteTable` resolves to `*` at runtime** — AWS's own warning (`iam-policies-for-amazon-ec2.md:270,305`): a policy pre-authorizing a specific future route-table ID is silently unscoped.
- **(7b) Multi-resource `ec2:Vpc` on `ReplaceRouteTableAssociation`/`AssociateRouteTable`** — `ec2:Vpc` is exposed on **both** the `route-table*` and `subnet` legs (`list_ec2.md:9442-9443`). Per the `iam-policies-for-amazon-ec2.md:196` "Important" box, a single `Condition` without per-`Resource` partitioning either blocks the action or (with `...IfExists`) silently skips the VPC check on the un-anchored leg → "pin to one VPC" weaker than intended.
- **(7c) ABAC self-widening** — `CreateTags`/`DeleteTags` support `route-table` with `aws:ResourceTag`/`aws:RequestTag`; AWS guidance is to gate with `ec2:CreateAction` (`supported-iam-actions-tagging.md:12`), but several AWS-authored policies don't, letting a principal with `ec2:CreateTags` on `route-table*` stamp a gating tag onto a same-account table and satisfy its own `aws:ResourceTag` route-mutation gate.
**Oracle.** For each, construct the "obvious" policy a careful author would write, then show (via `SimulatePrincipalPolicy` + a live scoped call on owned resources) the effective scope is broader than intended. **Doc evidence:** `iam-policies-for-amazon-ec2.md:196,270,305`; `list_ec2.md:9442-9443`; `supported-iam-actions-tagging.md:12`. **Severity-if-true:** Low–Medium (least-privilege scoping weaker than written; Medium where ABAC is the access control). **Stop:** one demonstration per sub-case.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Redirect/intercept a subnet's traffic to an attacker ENI under a "restrictive" policy | ReplaceRoute / CreateRoute (local-route or more-specific) | IAM route-table/tag/VPC scoping — **but no target/destination condition key** (A1) |
| Intercept all intra-VPC east-west traffic | ReplaceRoute `--local-target`→ENI | None at IAM layer; only route-table-object scoping (A1) |
| Bypass route-edit restriction by swapping/associating a table | ReplaceRouteTableAssociation / AssociateRouteTable | Separate IAM actions; shape-constraint only, no identity key for edge assoc (Area 3) |
| Wire routing to a core/ODB network in another account | CreateRoute/ReplaceRoute `CoreNetworkArn`/`OdbNetworkArn` | Undocumented whether call-time ownership/attachment is validated (Area 2) |
| Silent route-scope expansion by a foreign prefix-list owner | DestinationPrefixListId (RAM-shared) | "references use latest version"; owner controls contents (Area 5) |
| BGP peer injects a more-specific prefix to hijack a destination | Route Server / CreateRouteServerPeer | No documented prefix-ownership check; no MD5/TTL auth (Area 4) |
| Account-wide route control from a copy-verbatim AWS policy | AmazonEKSClusterPolicy / AmazonVPCFullAccess / NetworkAdministrator / CrossAccountNI | None — `Resource:"*"`, no Condition (Area 6) |
| Account-wide SG/ENI tampering from the route-server "least-privilege" sample | route-server-iam.md | None — `Resource:"*"`, no Condition (Area 6a) |
| Pre-authorize a specific created route-table ID | CreateRouteTable + `ec2:RouteTableID` | Key silently resolves to `*` (Area 7a) |
| Pin association to one VPC with a single `ec2:Vpc` condition | ReplaceRouteTableAssociation | Multi-resource condition pitfall; needs per-Resource statements (Area 7b) |
| Satisfy a tag gate by self-tagging the route table | CreateTags on route-table | `ec2:CreateAction`/`aws:TagKeys` exist but are opt-in (Area 7c) |
| Read another team's route tables | DescribeRouteTables | No resource-level read scoping; account/region-bounded only |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-account route-table access** via a foreign `rtb-*` id — the `route-table` ARN embeds the account (`list_ec2.md:9992`); a foreign id will not resolve. Genuine null, do not pursue. (Cross-account risk here lives in the *target*, Area 2, not the route table.)
- **Shared-VPC participants mutating the owner's route tables** — documented as **not permitted**: participants cannot call `CreateRoute`/`ReplaceRoute` on owner route tables (`vpc-share-limitations.md:46-47`). Null.
- **`VpcEndpointId` (GWLB) as a cross-account target** — the endpoint object is same-account/VPC by construction. Null (though the *endpoint service* behind it may be cross-account — that is a GWLB concern, not a route concern).
- **`LocalTarget` reset as a cross-account issue** — config-drift / self-inflicted only; no cross-account dimension.
- **Customer-authored over-broad policies** (a customer writing `ec2:ReplaceRoute` on `Resource:"*"`) — a customer least-privilege footgun, out of scope. (The AWS-*authored* policies in Area 6 are the carve-out and **are** in scope.)
- **Single-tenant self-DoS** — route-table route quotas, black-holing your own traffic. Record only.
- **The physical/data-plane forwarding fabric, IMDS on managed hosts, DNS/DHCP** — not route-table defects.
- Memory-safety / wire-protocol / deserialization / XXE / SSRF-via-URL-field / upload / KMS-encryption-context / OAuth / JWT / cache / canonicalization / attestation classes — **no corresponding surface** in this family (see Section 8 null hypotheses with pages checked). (`CoreNetworkArn`/`OdbNetworkArn` are ARNs, not fetched URLs → confused-deputy Lens A/B, not SSRF Lens G.)

---

## 8. Null Hypotheses / Doc Gaps (lenses that did not fire — pages checked named)

- **Lens A (cross-tenant IDOR):** null for cross-account route-table access (ARN embeds account, `list_ec2.md:9992`); shared-VPC participant mutation explicitly disallowed (`vpc-share-limitations.md:46-47`). *Intra-account* cross-team/cross-subnet reach IS possible but only via over-broad policy → surfaced as Areas 1/3/6, not a server authz defect. Checked: all route-action rows + `DescribeRouteTables` (`list_ec2.md:7308-7312`).
- **Lens G (SSRF):** N/A — no field in any route API page is a URL the service fetches/validates/renders server-side. `CoreNetworkArn`/`OdbNetworkArn` are resource ARNs the service *acts on* (→ Lens A/B confused-deputy, Area 2), not URLs it dereferences. Checked: `API_CreateRoute.md`, `API_ReplaceRoute.md`, `route-table-options.md`.
- **Lens Q (upload):** N/A — no blob/file/image parameter. Checked: same API pages.
- **Lens K (prompt injection):** N/A — no LLM/agent. (Route-server BGP is handled as untrusted-input→routing influence under Area 4, not an LLM.)
- **Lens C (credential vending):** N/A — no role-ARN/token/session input or STS path in any classic route action. Checked: request params of CreateRoute/ReplaceRoute/DeleteRoute/associations.
- **Lens B (PassRole):** N/A for the classic family — no `iam:PassRole` on CreateRoute/ReplaceRoute (confirmed `API_CreateRoute.md`/`API_ReplaceRoute.md`). The cross-account *target* trust is Area 2.
- **Lens H/W (KMS / attestation):** N/A — no encryption-context/KMS/PCR surface.
- **Lens J/FF (OAuth / JWT):** N/A — pure SigV4.
- **Lens Y (transport/sig):** inherits standard EC2 endpoint TLS/SigV4; nothing route-specific. **Exception to confirm:** route-server BGP sessions have **no documented MD5/TTL authentication** (Area 4) — a transport-trust gap flagged for live validation, not asserted.
- **Lens DD/BB/CC (cache / canonicalization / trusted-upstream header):** N/A — single EC2 API hop, no authorizer/CDN/proxy chain.
- **Lens EE (predictable-name land-grab):** N/A — route-table / route-server ids are AWS-assigned, not a customer/global namespace. Checked: `CreateRouteTable` + resource-type table.
- **Doc gaps to confirm empirically first (mark "doc-gap — confirm surface first"):**
  1. Whether `CreateRoute`/`ReplaceRoute` performs a **call-time ownership/attachment check** on `CoreNetworkArn`/`OdbNetworkArn`/RAM-shared TGW/peering targets (docs silent — Area 2).
  2. Whether the **route-server** installs a peer's advertised prefixes without an ownership/allow-list filter, and whether BGP sessions authenticate (docs silent — Area 4).
  3. Where **route-server-origin routes** rank among the documented propagation tiers (DX/VPN/VGW) in `route-tables-priority.md` (not listed — Area 4/5).
  4. Whether a target **ENI must belong to the calling principal** (docs state only existence/attachment — Area 1).

---

### Appendix — Kill-chain notes
- **Chain 1 (Area 6 → 3 → 1 → 5):** a role holding the copy-verbatim `AmazonEKSClusterPolicy` or `AmazonVPCFullAccess` (Area 6) uses `AssociateRouteTable`/`ReplaceRoute` (Area 3/1) to install a more-specific route (Area 5) pointing a sensitive destination at an attacker-controlled ENI — intercepting or black-holing traffic account-wide. Rate at chain end: effective account-wide traffic redirection = **High** within the account.
- **Chain 2 (Area 6a → 4):** the `route-server-iam.md` sample's unconditioned `ec2:AuthorizeSecurityGroupIngress`/`CreateNetworkInterface` (Area 6a) provisions the ENI/SG for a rogue BGP peer, which then injects a more-specific prefix (Area 4/5) to hijack intra-VPC traffic to that ENI. **High.**
- **Chain 3 (Area 2 → service plane):** probing `CoreNetworkArn`/`OdbNetworkArn` cross-account acceptance — **if an accepted ARN ever resolves to an AWS-owned/service network, HARD STOP and disclose** (potential Critical, out of the hunter's hands at that point).
