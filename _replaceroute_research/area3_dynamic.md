# Area 3 — Dynamic Routing / Route Server / Route Priority / Edge Routing
Research notes for downstream pentester. Documentation-only. No live AWS calls made.
Sources: offline mirror `/work/aws-docs/docs/vpc/latest/userguide/*.md` (each verified against live
`docs.aws.amazon.com` via WebFetch where noted — no sync drift found on any page fetched).

GA/age context (from `WhatsNew.md`):
- **VPC Route Server** — GA **March 31, 2025** (~19 months old as of 2026-10-20).
- **Route inbound VPC traffic to public IP addresses** (igw ingress routing) — GA **August 13, 2025**
  (~14 months old). Both are the newest routing primitives in the VPC route-table family and the
  least likely to have had deep external security review — matches task framing.
- Neither page carries an explicit `[NEW]`/preview badge on-page; GA status is only recoverable via
  `WhatsNew.md` dates. No "preview" language found anywhere in the route-server or ingress-routing
  doc set (grep across `route-server-*.md`, `dynamic-routing-route-server.md`, `advanced-routing.md`,
  `igw-ingress-routing.md` for `preview|\[new\]|general availability|GA\b` → zero hits). Both features
  are presented as fully GA, no beta caveats.

---

## 1. Route Server / BGP dynamic routing

### 1.1 CLAIM — The documented minimal IAM policy for route-server peer/endpoint lifecycle grants
account-wide security-group tampering, not scoped to route-server resources

**Mechanism:** `/work/aws-docs/docs/vpc/latest/userguide/route-server-iam.md` (verified identical on
live `docs.aws.amazon.com/vpc/latest/userguide/route-server-iam.html` via WebFetch — not a mirror sync
artifact, this is AWS's actual published guidance). The page states: "ensure that the IAM user or role
... has the required IAM permissions. Below is a guide to which permissions are required for each API."
The JSON policy it then shows is, verbatim:

```json
{
  "Sid": "CreateRouteServer",      "Action": ["sns:CreateTopic"],  "Resource": "*"
  "Sid": "DeleteRouteServer",      "Action": ["sns:DeleteTopic"],  "Resource": "*"
  "Sid": "CreateRouteServerEndpoint", "Action": [
      "ec2:CreateNetworkInterface","ec2:CreateNetworkInterfacePermission",
      "ec2:CreateSecurityGroup","ec2:DescribeSecurityGroups",
      "ec2:AuthorizeSecurityGroupIngress","ec2:CreateTags","ec2:DeleteTags"], "Resource": "*"
  "Sid": "DeleteRouteServerEndpoint", "Action": [
      "ec2:DeleteNetworkInterface","ec2:DeleteSecurityGroup",
      "ec2:RevokeSecurityGroupIngress","ec2:CreateTags","ec2:DeleteTags"], "Resource": "*"
  "Sid": "CreateRouteServerPeer",  "Action": ["ec2:AuthorizeSecurityGroupIngress"], "Resource": "*"
  "Sid": "DeleteRouteServerPeer",  "Action": ["ec2:RevokeSecurityGroupIngress"],    "Resource": "*"
}
```

Two anomalies, both load-bearing:
- The `Sid`s named `CreateRouteServer`/`DeleteRouteServer` grant **`sns:CreateTopic`/`sns:DeleteTopic`**
  — not any `ec2:*RouteServer*` action. The actual API calls used throughout the tutorial
  (`route-server-tutorial-create.md`) are `aws ec2 create-route-server` /
  `describe-route-servers`, yet the IAM guide never lists `ec2:CreateRouteServer`,
  `ec2:DeleteRouteServer`, `ec2:AssociateRouteServer`, `ec2:DisassociateRouteServer`,
  `ec2:CreateRouteServerPeer`, `ec2:DeleteRouteServerPeer`, `ec2:EnableRouteServerPropagation`,
  `ec2:DisableRouteServerPropagation`, `ec2:Describe*RouteServer*`, etc. anywhere. This looks like a
  copy/paste doc bug (an SNS-topic example policy fragment accidentally left in), but it is the
  *only* IAM guidance AWS publishes for this feature, so operators following it verbatim will deploy
  a policy that cannot actually call the real route-server create/delete APIs, and will not know
  the true least-privilege action list from the docs.
- `CreateRouteServerPeer` is documented as requiring only `ec2:AuthorizeSecurityGroupIngress` on
  `Resource: "*"` — with **no condition keys** (no `aws:ResourceTag`, no
  `ec2:AuthorizedSecurityGroupId`, no scoping to the route-server-managed SG). Per this doc, the
  "minimum" permission to let someone create a route-server BGP peer is a permission that lets them
  add an ingress rule to **any security group in the account**, not just the one the route server
  manages. Same for `DeleteRouteServerPeer` → `ec2:RevokeSecurityGroupIngress` on `Resource: "*"`.

**Confirm/Refute oracle:** In a test account, attach *only* this exact JSON policy to an IAM
principal and attempt:
  (a) `aws ec2 create-route-server` — expect `AccessDenied` (refutes the doc's claim that this
      policy is sufficient — confirms the doc/IAM-action mismatch is real and operationally
      blocking, not just cosmetic).
  (b) `aws ec2 authorize-security-group-ingress --group-id <unrelated-sg-not-created-by-route-server>`
      — if it succeeds, confirms the "account-wide SG tampering" over-grant: a principal who was
      only meant to manage route-server peers can modify ingress on arbitrary security groups
      (potential lateral path: open port 22/3389 on a victim SG).
  Also check CloudTrail `eventName` for the actual underlying IAM action names used by
  `CreateRouteServer`/`CreateRouteServerPeer` etc. to build the correct policy and compare against
  what's documented.

**Preconditions:** Attacker/insider has (or compromises a role with) exactly the SG-ingress actions
above, granted following this doc's example verbatim — plausible in real orgs that copy AWS's own
sample policy as "least privilege."

**Severity if true:** Medium-High — privilege escalation / lateral movement via SG modification
reachable from a role intended only to manage BGP route-server peers; distinct from, but adjacent to,
ReplaceRoute-style routing-authorization gaps the task is scoped around.

**Null-hypothesis note:** No AWS-managed policy for route server is named anywhere in the doc set
(checked `route-server-iam.md`, `dynamic-routing-route-server.md`, `security-iam-awsmanpol.md` —
zero hits for "RouteServer" in the managed-policy-update doc). No service-linked role is documented
for route server (checked for "service-linked role" + "route server" co-occurrence — zero hits).
If true operationally, this means route-server permissions must be hand-built from this flawed
guide, raising the odds real deployments over- or under-grant.

### 1.2 CLAIM — Route-server propagation installs device-advertised BGP routes into live VPC/IGW
route tables with no documented prefix validation, filtering, or peer-identity-to-prefix binding

**Mechanism:** `route-server-how-it-works.md`: "The route server endpoints update the route server
to withdraw routes ... The route server computes a ... FIB from the RIB, selecting the best available
routes. Route server updates the configured route tables with the routes from the FIB." The example
walks through Device A/B advertising `192.0.0.0/24` via BGP with MED, and route server installing
whichever has the lower MED as the FIB entry/next-hop for the **entire subnet route table**. Nothing
in `route-server-how-it-works.md`, `dynamic-routing-route-server.md`, `route-server-terms.md`, or the
8-step tutorial describes: prefix filtering/allow-lists, peer-to-ASN/prefix authorization binding,
RPKI-style origin validation, or any check that a peer may only advertise prefixes "it owns." Any
peer that establishes a session can apparently advertise any prefix, and best-path selection (MED)
is the only differentiator among peers.
`route-server-terms.md` defines "Route server peer" solely by network-layer requirements (has an
ENI in the VPC, speaks BGP, can initiate a session) — not by any AWS-side authorization of *which
prefixes* that peer is allowed to advertise.
`route-server-tutorial-create.md` IAM/creation flow also never ties specific CIDR ranges to a peer
at creation time — `create-route-server-peer` only takes `--peer-address`/`--bgp-options
PeerAsn=...`, no prefix allow-list parameter.

**Confirm/Refute oracle:** Stand up two route-server peers (A, legitimate device; B, "attacker"
device sharing the same subnet/VPC). Have B advertise a prefix it does not legitimately own
(e.g., a /32 inside a range normally owned by A, or a more-specific subset of an existing static
route's destination) with a lower MED than A. Observe via `describe-route-tables` / route-server
peer logs (`route-server-peer-logging.md` event types `RouteStatus: ADVERTISED/UPDATED`) whether:
  - the FIB installs B's route and the live VPC/IGW route table changes next-hop to B's ENI;
  - any AWS-side rejection, filtering, or alarm fires for the unauthorized-looking advertisement.
If the table updates and traffic to that prefix routes through B with no block/alert, the claim is
confirmed: a compromised or malicious BGP-speaking device inside the VPC can redirect or blackhole
traffic for arbitrary destinations it did not previously own, by simply advertising a route with a
favorable MED.

**Preconditions:** Attacker controls (or compromises) any EC2 instance/appliance that can establish
an ENI-based BGP session to a route-server endpoint in the target VPC, and that VPC has route-server
propagation enabled on a route table it cares about. Note IAM for *peer creation* is a separate gate
(§1.1) — but once a peer exists and BGP is up, the docs describe no further prefix-level
authorization at the routing-protocol layer itself (Lens F/K: untrusted routing input → trusted
routing-table action, enforced only by whatever IAM gated peer creation, not by the protocol).

**Severity if true:** High — this is the core route-injection / traffic-redirection primitive the
task flags as highest value. A single compromised appliance with route-server-peer rights can
redirect or blackhole traffic for the whole propagation-enabled route table, including traffic for
prefixes unrelated to that device's normal function.

**Null-hypothesis note:** Docs do not claim the opposite either — there is no statement that route
server validates/authorizes advertised prefixes, so this is a documentation *gap* (absence of a
control), not a confirmed vulnerability from docs alone. Flag explicitly for the hunter: this must be
tested live, because AWS may enforce prefix scoping at an undocumented layer (e.g., via the peer's
security group / ENI route reachability) that the docs simply don't mention.

### 1.3 CLAIM — No documented BGP session authentication (MD5/TTL security) for route-server peers

**Mechanism:** Grepped `dynamic-routing-route-server.md`, all `route-server-*.md`, and
`advanced-routing.md` for `md5|ttl security|bgp auth|authentication` — **zero matches**. The only
peer liveness/session options documented (`route-server-tutorial-create-peer.md`) are **BGP
keepalive** (default) or **BFD**; no TCP-MD5 password or GTSM/TTL-security option is exposed in the
console fields or the `create-route-server-peer` CLI example (`--bgp-options
PeerAsn=65001,PeerLivenessDetection=bfd` — no auth/password key). Session establishment appears
gated purely by network reachability (ENI in the VPC, IP reachability to the endpoint) plus whatever
security group rules IAM allowed (§1.1), not by a BGP-layer secret.

**Confirm/Refute oracle:** Attempt to create a route-server peer and establish BGP from an
unauthorized-but-network-reachable ENI (e.g., an instance in the same subnet that isn't the intended
appliance) without any shared secret. If the session establishes (`BGPStatus: UP` in peer logs) with
no credential exchange, this is confirmed: authorization to peer == authorization to inject routes,
gated only by security-group/ENI reachability and whichever IAM actions created the
`RouteServerPeer` object — not by any protocol-level secret.

**Preconditions:** Attacker has network path (L3 reachability + permitted SG) to a route-server
endpoint's ENI inside the VPC — i.e., any compromised instance in the same VPC/subnet as the
endpoint, if SGs allow it.

**Severity if true:** High in combination with 1.2 — no cryptographic peer authentication means the
only gate against rogue route injection is IAM-governed peer-object creation (§1.1, shown to be
weakly scoped per the docs) plus security groups. Lens U: "guarantee" (BGP peering implies trusted
device) vs. "enforcement" (no MD5/TTL, just reachability + IAM) gap.

**Null-hypothesis note:** This is an absence-of-evidence finding — docs may simply omit an existing
feature. Must be tested against the live `create-route-server-peer` API (check for an undocumented
`BgpOptions` auth field) before treating as confirmed.

### 1.4 CLAIM — Quotas create a bounded but still useful DoS/starvation surface, not a hard safety net

**Mechanism:** `amazon-vpc-limits.md` §"Route servers" (`vpc-limits-route-servers`):
- Route servers per VPC: 5 (adjustable)
- Route server endpoints per route server: 10 (adjustable)
- Peering sessions per network interface: 20 (adjustable)
- Route server endpoints per route server and subnet: 2 (not adjustable)
- **Routes per route server peer: 100 (not adjustable)** — "number of routes that can be dynamically
  advertised over a route server peer"
- **Routes per route server: 100 (not adjustable)** — "number of routes that can be installed in the
  FIB of a route server"

Separately, `igw-ingress-routing.md` "Advanced option" section states: "a maximum of 32 BGP peers can
advertise the same prefix to the same route table using route server" — implying ECMP-style
multi-peer advertisement of one prefix is supported up to 32 peers.

**Confirm/Refute oracle:** From a single compromised peer, advertise >100 distinct prefixes and
observe whether the 101st is silently dropped, errors, or evicts an existing (possibly legitimate)
FIB entry — determines whether the 100-route/peer cap is a hard reject or a fail-open eviction
(latter would let an attacker peer evict legitimate routes from the shared 100-route/route-server FIB
cap by flooding advertisements, since "Routes per route server: 100" is a *total* ceiling, not
per-peer additive). This is a concrete DoS angle: a single malicious/compromised peer advertising
100 junk prefixes could fill the whole route-server's FIB quota (shared across all peers on that
route server) and starve out legitimate routes from other peers.

**Preconditions:** Attacker controls one route-server peer (see §1.1/1.3 for how that's obtained).

**Severity if true:** Medium — availability impact (route starvation) rather than confidentiality/
integrity, but could be chained with 1.2 to blackhole specific destinations deliberately rather than
just by flooding.

### 1.5 CLAIM — Persist-routes feature can keep attacker-injected routes alive after the attacker's
BGP session is torn down

**Mechanism:** `route-server-tutorial-create.md`, "Persist routes" option: "If enabled: Routes will
be preserved in the route server's routing database even if all BGP sessions end... If you enabled
persist routes, for Persist duration, enter a value between 1-5 minutes... your device has 1 minute
[default] after re-establishing BGP to relearn and advertise its routes before the route server
resumes normal functionality." This is a resilience feature (survive brief appliance restarts), but
it also means a malicious route, once advertised and installed in the FIB, can **outlive the BGP
session that injected it** by up to 5 minutes — a window in which the injected route remains active
in live route tables with no peer currently proving it's still "owned"/live.

**Confirm/Refute oracle:** Enable persist-routes (max 5 min), have a malicious peer advertise a
hijacking route, then tear down the BGP session (simulating "hit and run" injection) and verify via
`describe-route-tables` that the injected route remains active in the FIB/route table for up to the
configured persist duration after the peer disconnects.

**Preconditions:** Route server configured with persist-routes enabled (an operator choice, but one
the docs recommend for availability) and attacker achieves even transient peer/BGP access.

**Severity if true:** Low-Medium — extends the window of an already-successful injection (§1.2) by
minutes; not a standalone vuln but an amplifier.

---

## 2. Route priority / longest-prefix (static vs. propagated vs. prefix-list vs. route-server/BGP)

### 2.1 CLAIM — Priority order is documented and is exploitable: a more-specific injected route
always wins regardless of source trust, and even a less-specific *static* route beats a
same-specificity propagated/BGP route — meaning the hijack vector differs by whether the attacker
can get a static-looking entry or must rely on specificity

**Mechanism:** `route-tables-priority.md`, verbatim priority list (confirmed identical against live
docs via WebFetch):
```
1. Longest prefix match (overrides everything else, independent of route type)
2. Static routes (igw, nat gw, eni, instance, gateway VPC endpoint, transit gateway,
   VPC peering, Gateway Load Balancer endpoint)
3. Prefix list routes
4. Propagated routes
   a. Direct Connect BGP routes
   b. VPN static routes
   c. VPN BGP routes (e.g. virtual private gateway)
```
And explicitly: "Please note that for routes that overlap, more specific routes always take priority
irrespective of whether they are propagated routes, static routes, or routes that reference prefix
lists" (under "Route priority for prefix lists"). So **longest-prefix-match is the single overriding
rule** — a /32 propagated-or-BGP route beats a /24 static route, full stop, regardless of trust
level of the route's origin.
Separately, for *equal-specificity* collisions, static beats propagated (worked example:
`172.31.0.0/24` static-to-IGW beats `172.31.0.0/24` propagated-from-VGW).
Where does **route-server-installed FIB routes** fit in this list? `route-tables-priority.md` never
mentions "route server" at all — the list enumerates VGW/DX/VPN propagation explicitly but is silent
on route-server-sourced routes. This is a genuine documentation gap: the hunter cannot tell from this
page alone whether a route-server/BGP-FIB route is treated as a "propagated route" (bottom of
priority, loses ties to static) or has its own undocumented tier.

**Confirm/Refute oracle (falsifiable, with concrete oracle):**
1. Create a subnet route table with a static route `10.0.0.0/24 -> igw-X`.
2. Enable route-server propagation on that table; have a peer advertise `10.0.0.5/32` (longest
   prefix, fully contained in the static /24) via BGP with any MED.
3. `describe-route-tables` and trace actual traffic to `10.0.0.5`: if it egresses via the
   route-server-installed next-hop (not igw-X), this **confirms** that an attacker who can get even
   one longer-prefix route accepted by route server can silently override an operator's static route
   for that specific destination — a true "longest-prefix hijack," independent of ReplaceRoute
   authorization on the static route itself, because the override comes from the LPM rule, not from
   modifying the existing entry.
4. Repeat with equal specificity (`10.0.0.0/24` advertised by route server vs. the existing static
   `10.0.0.0/24 -> igw-X`) to determine whether route-server/BGP routes are treated as "propagated"
   (static wins, per the general rule) or something else (undocumented).

**Preconditions:** Attacker/compromised peer can get a route accepted into the FIB for a longer
prefix than an existing static route covers (needs route-server-peer access, see §1 chain) — no
separate authorization check on "does this prefix fall inside a protected static route's CIDR" is
documented anywhere.

**Severity if true:** High — this is the clean "route-priority-override" finding the task asks for:
static routes (which an operator may believe are an immutable safety net, e.g. pointing all of
10.0.0.0/24 at a trusted firewall) can be silently circumvented for any sub-range via a more-specific
dynamically-injected route, with LPM as the documented, by-design mechanism. No special privilege
beyond "get one route accepted by route server" is needed — the priority rule itself is the bypass,
not a bug in enforcement of who-can-call-ReplaceRoute.

**Null-hypothesis / gap to flag:** Docs do not state where route-server-origin routes rank among
"propagated routes" vs. some new undocumented tier — recommend the hunter test this explicitly and
report back to the docs team / treat as an evidence gap rather than assuming either answer.

### 2.2 CLAIM — Overlapping-prefix-list tie-break is nondeterministic on first install ("we randomly
choose") — minor but real integrity oracle gap

**Mechanism:** `route-tables-priority.md`: "If your route table references multiple prefix lists
that have overlapping CIDR blocks to different targets, we randomly choose which route takes
priority. Thereafter, the same route always takes priority." Documented as "random," not
attacker-influenceable by itself, but worth noting: an attacker who can get a second overlapping
managed prefix list attached to a route table (if prefix-list management is a weaker trust boundary
than route-table write access — needs separate check, out of scope here) introduces non-determinism
an operator cannot fully reason about statically.

**Confirm/Refute oracle:** Attach two prefix lists with overlapping CIDRs pointing to different
targets on the same route table repeatedly (new route table each time) and observe whether the
"winning" target is genuinely random per table or deterministic by some unstated tie-break (e.g.
prefix-list-ID ordering, creation time) — matters for whether an attacker could predict/force the
outcome.

**Severity if true:** Low — mostly an operational-reliability finding unless combined with a prefix-
list write-access flaw elsewhere (not covered in this area).

### 2.3 CLAIM (null hypothesis, explicitly checked) — `route-table-routes-troubleshoot.md` contains
no route-priority or route-server detail

**Mechanism:** The entire page content is two sentences pointing to Reachability Analyzer as a
separate static-analysis tool; it contains no route-priority mechanics, no route-server mentions, no
troubleshooting steps of its own. Checked and confirmed empty of relevant signal — do not expect
additional leads from this page.

---

## 3. Gateway / edge association & ingress routing

### 3.1 CLAIM — Gateway route tables let any principal with route-table-gateway-association rights
force **all** inbound internet (or VPN) traffic into a middlebox appliance ENI, VPC-wide, and the
only documented isolation boundary is "same VPC"

**Mechanism:** `gateway-route-tables.md`: "You can associate a route table with an internet gateway
or a virtual private gateway... you can intercept the traffic that enters your VPC through an
internet gateway by redirecting that traffic to a middlebox appliance." Rules: target can replace
the **entire VPC CIDR's local route** ("Traffic destined for all subnets within the VPC is routed to
the network interface" — worked example 2) or a more specific subnet CIDR. The only cross-boundary
constraint documented: "You cannot use a gateway route table to control or intercept traffic outside
of your VPC... You can intercept traffic that enters your VPC and redirect it to another target in
the same VPC only." I.e., the isolation model is VPC-scoped, not subnet/owner-scoped — once an
attacker can attach a gateway route table to the IGW, they intercept **all inbound internet traffic
for the whole VPC**, not just their own subnet's traffic.
`associate-route-table-gateway.md` shows the actual authorization surface is just the
`associate-route-table`/`disassociate-route-table` EC2 API called with `--gateway-id` instead of
`--subnet-id` — i.e., **the same IAM action** (`ec2:AssociateRouteTable` /
`ec2:DisassociateRouteTable`) governs both "attach my route table to my subnet" (low blast radius)
and "attach my route table to the IGW, hijacking all VPC ingress" (full-VPC blast radius). No
separate, more restrictive IAM action or condition key is mentioned for the gateway-association case
specifically on this page.

**Confirm/Refute oracle:** In IAM policy simulator / live test, check whether `ec2:AssociateRouteTable`
can be scoped (via condition key, e.g. `ec2:AssociatedResource` or resource ARN pattern) to subnet-
only association, disallowing gateway (IGW/VGW) association, or whether any principal with generic
"manage route tables" rights can silently escalate to full-VPC-ingress interception by targeting
`--gateway-id` instead of `--subnet-id`. If no such distinguishing condition key exists/works, this
confirms a privilege-scoping gap: "can edit my subnet's route table" and "can hijack all VPC ingress
traffic" are the same permission.

**Preconditions:** Principal has `ec2:AssociateRouteTable`/`ec2:CreateRoute` rights intended for
ordinary subnet route-table management, and the target VPC's IGW is not yet edge-associated (or is
replaceable).

**Severity if true:** High — full VPC ingress traffic interception (classic on-path MITM setup for
every external connection into the VPC) from what may be a commonly-granted "route table editor"
permission, if IAM cannot distinguish subnet-association from gateway-edge-association. This directly
parallels the ReplaceRoute family's core risk (routing-action authorization) but at the edge/gateway
tier instead of the subnet-route tier.

**Preconditions caveat / rules that limit it:** `gateway-route-tables.md` "Rules and considerations"
also states you cannot associate a gateway if the route table "contains existing routes with targets
other than a network interface, Gateway Load Balancer endpoint, or the default local route," and
"Route propagation is enabled for the route table" blocks association too — so an attacker must use a
purpose-built, propagation-disabled route table containing only local/ENI/GWLBe routes. This is a
real but narrow gate, not a strong authorization control — it constrains route-table *shape*, not
*who* may perform the association.

### 3.2 CLAIM — IGW ingress routing (BYOIP-to-ENI) + VPC Block Public Access interaction is a
documented, explicit control-bypass footnote, not a bug — but worth flagging as an operational trap

**Mechanism:** `igw-ingress-routing.md`, "Important" callout: "If you are using VPC Block Public
Access (BPA), when BPA is enabled, it will block traffic to subnets using ingress routing, **even if
you've set a subnet-level BPA exclusion**. Subnet-level exclusions do not work for ingress routing.
To allow ingress routing traffic with BPA enabled: Disable BPA completely, or Use a VPC-level
exclusion." This means operators who believe a narrow, subnet-scoped BPA exclusion is sufficiently
minimal for this feature are wrong per AWS's own documentation — the only ways to make ingress
routing work are account/VPC-wide BPA relaxations, not scoped ones. This is a security-guardrail
granularity gap (Lens U: operator's believed guarantee — "I excluded just this one subnet" — vs.
actual enforcement — "BPA exclusion granularity doesn't apply here, you weakened VPC- or account-wide
BPA").

**Confirm/Refute oracle:** Not independently testable as a "vulnerability" — it's AWS's documented
behavior. Oracle for the hunter: in a BPA-enabled test VPC, set only a subnet-level exclusion, enable
IGW ingress routing for that subnet's BYOIP pool, and confirm traffic is in fact still blocked (docs
say it will be) — then escalate to VPC-level exclusion and confirm traffic flows, documenting the
resulting *broader* BPA posture (i.e., what else became reachable because the operator had to use a
wider exclusion than intended) as the actual blast-radius increase to report.

**Preconditions:** Org uses VPC BPA as a security boundary and adopts ingress routing without reading
this caveat.

**Severity if true:** Medium — availability/misconfiguration-risk finding (operators over-widening a
guardrail to make a feature work), not a direct exploit.

### 3.3 CLAIM (null hypothesis) — No separate authorization model beyond standard
`ec2:AssociateRouteTable`/gateway/BYOIP-pool IAM actions is documented for edge/gateway association

**Mechanism:** Checked `associate-route-table-gateway.md`, `gateway-route-tables.md`,
`igw-ingress-routing.md` for any mention of a dedicated condition key, resource-level restriction, or
separate managed policy gating edge association specifically — none found. The CLI examples use
plain `associate-route-table --gateway-id` / `--public-ipv4-pool` with no additional
`--condition`/policy guidance referenced on these pages. Flag as an evidence gap: the authorization
model for this high-blast-radius action is simply "whatever IAM policy already grants
ec2:AssociateRouteTable," per the docs — consistent with and reinforcing claim 3.1.

---

## Summary of strongest leads for the hunter (priority order)

1. **§2.1 Longest-prefix override of static routes via route-server-injected more-specific prefixes**
   — clean, falsifiable, AWS-documented-by-design bypass of an operator's static safety-net route;
   highest confidence because the priority rule itself ("more specific routes always take priority
   irrespective of... static... or propagated") is explicit AWS doc text, not an inference.
2. **§1.2 No documented prefix validation/authorization on BGP-advertised routes from route-server
   peers** — the core route-injection primitive; AWS's own worked example (Device A/B MED-based
   failover) shows arbitrary peers can swing a FIB entry for a subnet-wide destination with no
   mentioned ownership check.
3. **§1.1 `route-server-iam.md`'s sample policy is both broken (never grants the real
   `ec2:*RouteServer*` actions) and over-permissive (`ec2:AuthorizeSecurityGroupIngress`/
   `RevokeSecurityGroupIngress` on `Resource: "*"` with zero conditions for peer create/delete)** —
   verified identical between offline mirror and live docs.aws.amazon.com, so this is AWS's actual
   current published guidance, not a mirror artifact. Strong, concrete, immediately testable in a
   sandbox account.
4. **§3.1 Gateway/edge route-table association appears to share the same IAM action
   (`ec2:AssociateRouteTable`) as ordinary subnet route-table association**, yet escalates blast
   radius from "one subnet" to "all VPC ingress traffic" — worth confirming whether any condition key
   actually distinguishes the two in practice.
5. **§1.3 No documented BGP session authentication (MD5/TTL-security)** for route-server peers —
   null-hypothesis-flavored (absence of evidence, not evidence of absence) but combines multiplicatively
   with #2 and #3 if confirmed live.
6. Secondary/amplifier leads: §1.4 (100-routes-per-route-server shared quota as a DoS/eviction
   vector), §1.5 (persist-routes extends an injected route's lifetime past BGP teardown), §3.2 (BPA
   subnet-exclusion-doesn't-work-for-ingress-routing operational trap).

Null hypotheses explicitly checked and found absent in docs (report as gaps, not findings): no SLR
for route server; no AWS-managed IAM policy named for route server; no MD5/TTL BGP auth mentioned;
no mention of route-server priority tier in `route-tables-priority.md`; `route-table-routes-
troubleshoot.md` has no relevant content.
