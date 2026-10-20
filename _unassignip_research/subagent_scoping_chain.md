# `ec2:UnassignPrivateIpAddresses` — IAM Scoping Gap, Reassignment Chain, and Resource-ID Analysis

Documentation-only study. No AWS API calls were made; no live account was touched. All claims below are
cited to the offline AWS docs mirror at `/work/aws-docs` (same tree as `https://docs.aws.amazon.com/`).

---

## 1. IP/Prefix-value scoping gap

**Claim:** `ec2:UnassignPrivateIpAddresses` can be scoped by IAM only at whole-network-interface
granularity (plus tags/AZ/subnet/VPC/region/managed-operator metadata of that ENI). No condition key
exists anywhere in the EC2 service-authorization reference that can constrain *which* private IPv4
address or IPv4 Prefix Delegation prefix is unassigned.

**Evidence**

- Source: `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`
  (mirrors `https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html`).

- The action's row in the "Actions, resources, and condition keys" table (line 9696-9700):

  > `UnassignPrivateIpAddresses` — Description: "Grants permission to unassign one or more secondary
  > private IP addresses from a network interface." Resource types (*required): `network-interface*`.
  > Condition keys: `aws:ResourceTag/${TagKey}`, `ec2:AvailabilityZone`, `ec2:ManagedResourceOperator`,
  > `ec2:NetworkInterfaceID`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:Subnet`, `ec2:Vpc`.

  This matches the task's premise exactly and was re-confirmed independently by grep.

- I grepped the **entire** EC2 condition-key master table at the bottom of `list_ec2.md`
  (the full `Filters access by …` table, ~148 rows, lines ~9990-10190) for `PrivateIp`, `IpAddress`,
  `Prefix`, and `SecondaryIp`. Results:
  - `ec2:PublicIpAddress` — "Filters access by a public IP address" (String). This key exists only on
    the `elastic-ip` resource (used by `AssociateAddress`, `AllocateAddress`, etc. — see the
    `elastic-ip` resource row, line 9938) and is unrelated to private IPv4 addresses on an ENI.
  - `ec2:IpamPrefixListResolverTargetId`, `ec2:Ipv4IpamPoolId`, `ec2:Ipv6IpamPoolId` — these govern
    IPAM pool/prefix-list *resolver* resources (a different feature), not ENI secondary-IP or
    Prefix-Delegation values.
  - **No key** of the shape `ec2:PrivateIpAddress`, `ec2:SecondaryPrivateIpAddress`, `ec2:Ipv4Prefix`,
    `ec2:Ipv6Prefix`, or similar exists in the table at all.
  - A targeted grep for the literal action names `AssignPrivateIpAddresses` /
    `UnassignPrivateIpAddresses` in the action table (lines 110-111, 9595, 9696-9700) shows neither
    action lists any IP-address-valued condition key — `AssignPrivateIpAddresses`'s own condition-key
    set (line 9595) is: `aws:RequestTag`, `aws:TagKeys`, `ec2:AssociatePublicIpAddress`,
    `ec2:AuthorizedService`, `ec2:AvailabilityZone`, `ec2:IsLaunchTemplateResource`,
    `ec2:LaunchTemplate`, `ec2:ManagedResourceOperator`, `ec2:NetworkInterfaceID`, `ec2:Region`,
    `ec2:Subnet`, `ec2:Vpc` — again, nothing that binds a specific IP/prefix value.

**Conclusion:** Confirmed. `UnassignPrivateIpAddresses` (and its sibling `AssignPrivateIpAddresses`)
is scopable by IAM only at the granularity of "this network interface" (by ID, tag, AZ, subnet, VPC,
region, or managed-resource-operator presence). A policy author cannot write a condition that says
"only allow unassigning IP `10.0.2.60`" or "only allow unassigning prefixes, not whole addresses" or
vice versa — IAM has no visibility into the `PrivateIpAddress.N` / `Ipv4Prefix.N` request parameters
for authorization purposes. Anyone authorized to call this action on a given ENI can strip **any**
secondary private IP or Prefix-Delegation prefix currently on that ENI, in a single call, regardless
of which specific address they intend to target.

**Availability / teardown impact.** Because the grant is "all secondary addresses on this ENI or
nothing," least-privilege IAM design degenerates to an all-or-nothing choice per ENI. This matters
operationally because secondary private IPs on an ENI are commonly used as floating/virtual IPs that
a specific workload depends on for availability, independent of the underlying ENI's primary address:

- **Database failover VIP** — e.g., a PostgreSQL/MySQL HA pair where the secondary private IP is the
  "floating" address that application clients connect to, moved between primary/replica ENIs on
  failover (the classic EC2 HA pattern documented in `using-eni.md`, line 54: "secondary private IP
  addresses can be reassigned from one instance to another," and line 66, re: Elastic IP association
  per private IP). A principal with only `UnassignPrivateIpAddresses` on that ENI can silently detach
  the VIP from the active node, causing a client-visible outage with no automatic remediation (the HA
  software would need to re-detect and re-assign it).
- **HA cluster virtual IP** (e.g., Pacemaker/corosync, Windows Failover Clustering on EC2) — same
  mechanism: the cluster VIP is a secondary private IP; unassigning it silently breaks cluster
  reachability without touching the instance, security group, or route table, so monitoring aimed at
  those layers would not catch it.
- **Container/Pod IP** — in ENI-per-Pod designs (e.g., Amazon VPC CNI for EKS), each Pod is given a
  secondary IP (or an IPv4-Prefix-Delegation address drawn from a `/28` prefix, see
  `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-prefix-eni.md`) assigned to the node's ENI.
  `UnassignPrivateIpAddresses`/removing an `Ipv4Prefix` strips that address pool out from under running
  Pods.
- **Application-bound secondary IP** — any service that binds a listener to a specific secondary
  private IP (common for multi-tenant TLS/SNI-less setups, or for licensing tied to an IP) loses that
  bind point the instant the IP is unassigned, independent of whether the attacker (or an
  over-scoped automation principal) intended to affect a different address on the same ENI.

Because the IAM condition keys cannot discriminate *which* IP is removed, any policy written "to allow
a build/ops tool to release one IP it allocated" necessarily also authorizes removing every other
secondary IP/prefix on that same ENI — a privilege-scoping dead end purely from the IAM layer; the only
mitigation is application-layer validation or splitting workloads across dedicated ENIs so the
blast radius of an over-broad grant is limited to one ENI's secondary addresses.

---

## 2. Reassignment / IP-takeover chain

**`AllowReassignment` semantics** — Source:
`/work/aws-docs/docs/AWSEC2/latest/APIReference/API_AssignPrivateIpAddresses.md` (mirrors
`https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssignPrivateIpAddresses.html`), Request
Parameters section:

> **AllowReassignment** — "Indicates whether to allow an IP address that is already assigned to
> another network interface or instance to be reassigned to the specified network interface."
> Type: Boolean. Required: No.

The same page also documents (lines 12-14):

> "When you move a secondary private IP address to another network interface, any Elastic IP address
> that is associated with the IP address is also moved. Remapping an IP address is an asynchronous
> operation. When you move an IP address from one network interface to another, check
> `network/interfaces/macs/mac/local-ipv4s` in the instance metadata to confirm that the remapping is
> complete."

This is explicit, first-party confirmation that `AssignPrivateIpAddresses` with `AllowReassignment=true`
can move a secondary private IP that is **currently assigned to a different ENI** onto the caller's
target ENI — i.e., direct reassignment without going through `UnassignPrivateIpAddresses` first, *if*
the caller is authorized to call `AssignPrivateIpAddresses` on the target ENI.

**The chain as specified in the task is also directly supported without `AllowReassignment`:**

1. Principal A (or an over-privileged automation role) calls `UnassignPrivateIpAddresses` on
   victim ENI `eni-victim`, specifying `PrivateIpAddress.1=10.0.2.60` (the VIP/DB-failover/Pod IP).
   Per `API_UnassignPrivateIpAddresses.md`: "Unassigns the specified secondary private IP addresses
   or IPv4 Prefix Delegation prefixes from a network interface." The address is released back to the
   subnet's available pool — it is no longer "in use" from the subnet's perspective.
2. Principal B (attacker-controlled, in the same account, with `AssignPrivateIpAddresses` on their
   own ENI `eni-attacker` in the **same subnet**) calls `AssignPrivateIpAddresses` with
   `PrivateIpAddress.1=10.0.2.60` against `eni-attacker`. Per `API_AssignPrivateIpAddresses.md`:
   "If you don't specify an IP address, Amazon EC2 automatically selects an IP address within the
   subnet range" — implying (and consistent with general EC2 IP-allocation behavior) that a specified,
   currently-unassigned address within the subnet's CIDR is accepted without needing
   `AllowReassignment` at all, since it is no longer assigned to anything; `AllowReassignment` is
   needed only for the *direct steal* (step 1+2 collapsed into one call) when the address is still
   actively assigned elsewhere.
3. Any traffic inside the VPC/subnet destined for `10.0.2.60` (ARP/route-table resolution within the
   subnet is per-ENI) now resolves to `eni-attacker` instead of `eni-victim`. This is an intra-VPC,
   intra-subnet traffic-interception / IP-hijack primitive: whatever was relying on that address
   (the DB VIP, cluster VIP, Pod IP) for inbound traffic now has its traffic delivered to the
   attacker-controlled ENI instead.

**Trust model required.** This is **not** a privilege-escalation bug in the IAM engine — it is a
structural consequence of §1's granularity gap combined with a specific, realistic trust model:

- Two or more principals (IAM roles/users, or automation such as CI/CD, Lambda, or a Kubernetes
  controller) hold EC2 networking permissions scoped *per network interface* (by
  `ec2:NetworkInterfaceID`, tag, or subnet/VPC condition keys) rather than per IP address — which is
  the only scoping IAM supports (§1).
- Both principals' authorized ENIs sit in the **same VPC subnet** (a very common layout: e.g., a
  shared "app" subnet with per-team or per-service ENIs, or an EKS node subnet where many Pods'
  secondary IPs/prefixes are drawn from the same CIDR).
- One principal is compromised, malicious, or simply has an overly broad/stale policy (e.g., a CI
  pipeline that still has `ec2:UnassignPrivateIpAddresses`/`ec2:AssignPrivateIpAddresses` with
  `Resource: "*"` or a wildcard tag condition matching more ENIs than intended).
- This is a **single-account, intra-account** scenario. The `network-interface` ARN is
  account-scoped (`arn:${Partition}:ec2:${Region}:${Account}:network-interface/${NetworkInterfaceId}`,
  confirmed in `list_ec2.md` line 9982), so a principal in Account A cannot name or act on an ENI in
  Account B via this mechanism; there is no cross-account vector here absent a separate
  cross-account role grant.

**Severity rating:** Medium-High, intra-account only. Rationale:
- Impact: traffic interception / integrity and availability loss for whatever service relied on the
  stolen IP (potentially credential/data interception if the victim service is unauthenticated-by-IP
  or the attacker can present a plausible service on that IP) — this is a meaningful blast radius
  when IAM is being used to separate teams/workloads *within one account* (e.g., multi-tenant
  platform-engineering setups, shared VPC models).
- Likelihood/complexity: requires the attacker to already hold valid IAM credentials with
  `AssignPrivateIpAddresses`/`UnassignPrivateIpAddresses` scoped to *some* ENI in the *same subnet* as
  the victim — i.e., it is a lateral-movement / privilege-boundary-crossing primitive between two
  already-authenticated principals in one account, not an externally-exploitable bug and not a
  cross-account or cross-tenant (in the AWS-account sense) issue.
- This should be framed in the research plan as "IAM condition-key coverage gap enabling intra-account
  IP takeover between differently-scoped network principals," not as an AWS service vulnerability —
  AWS's documentation discloses both the condition-key set (§1) and the `AllowReassignment` behavior
  (§2) plainly; the risk is in how a customer composes least-privilege policies around ENI-level
  grants without realizing the IP-value granularity is unavailable.

---

## 3. Primary-IP protection (scope boundary)

**Claim:** Only secondary private IPv4 addresses can be unassigned; the primary private IPv4 address
of an ENI cannot be removed via this API.

**Evidence:**
- `API_UnassignPrivateIpAddresses.md`, title sentence: "Unassigns the specified **secondary** private
  IP addresses or IPv4 Prefix Delegation prefixes from a network interface" (emphasis added — the
  word "secondary" is in the source text, not added by me, confirmed at line 8 of the doc and again
  in its service-authorization description, "permission to unassign one or more **secondary** private
  IP addresses from a network interface," `list_ec2.md` line 9697).
- `/work/aws-docs/docs/AWSEC2/latest/UserGuide/using-eni.md`, line 54: "When you launch an EC2 instance
  into an IPv4-only or dual stack subnet, the instance receives a primary private IP address from the
  IPv4 address range of the subnet. You can also specify additional private IPv4 addresses, known as
  secondary private IPv4 addresses. **Unlike primary private IP addresses, secondary private IP
  addresses can be reassigned from one instance to another.**" This directly states primary IPs are
  categorically different and not subject to the reassignment/unassignment mechanics described in §2.
- The `UnassignPrivateIpAddresses` API parameters (`PrivateIpAddress.N`, `Ipv4Prefix.N`) have no
  "primary" flag or option — the action is defined purely in terms of secondary addresses/prefixes,
  so there is no code path in the documented API surface to target the primary address.

**Conclusion:** Confirmed scope boundary — this action cannot be used to strip an ENI of its primary
private IPv4 address (which would effectively orphan the ENI's base identity on the subnet). The
attack surface in §2 is limited to secondary addresses and Prefix-Delegation prefixes only. No doc
gap here; this is stated plainly and consistently across the API reference and the User Guide.

---

## 4. ENI ID entropy / IDOR considerations

**ARN / ID format.**
- Network-interface resource ARN (from `list_ec2.md`, Resources table, line 9982):
  `arn:${Partition}:ec2:${Region}:${Account}:network-interface/${NetworkInterfaceId}`.
  The ARN embeds the `${Account}` segment, so the resource is **account-scoped** — a policy's
  `Resource` element (or the implicit authorization check) requires the ARN's account component to
  match the resource's owning account. Cross-account `UnassignPrivateIpAddresses` calls against an
  ENI in a different account are blocked by this ARN/ownership boundary unless a cross-account IAM
  role or resource-based mechanism is separately and deliberately granted (EC2 network-interface
  resources have no resource-based policy of their own, so in practice this requires an assumed role
  in the target account).
- **ID format, observed directly in AWS's own example values across the API reference mirror**
  (`/work/aws-docs/docs/AWSEC2/latest/APIReference/*.md`):
  - Legacy short form (8 hex characters after `eni-`): `eni-197d9972`
    (`API_UnassignPrivateIpAddresses.md` sample request, line 61), `eni-d83388b1`
    (`API_AssignPrivateIpAddresses.md` sample request, line 95), `eni-ffda3197`
    (`API_AttachNetworkInterface.md`), `eni-1a2b3c4d` (`API_CreateNetworkInterfacePermission.md`).
    That's 32 bits of hex-encoded identifier space.
  - Current long form (17 hex characters after `eni-`): `eni-01d32da61c165ac3e`
    (`API_AssignPrivateIpAddresses.md` **sample response**, lines 107 and 141 — notably the same doc
    page uses the legacy 8-char form in its *request* example and the 17-char form in its *response*
    example, an internal documentation inconsistency worth flagging, not a technical one: AWS migrated
    EC2 resource IDs from 8-char to 17-char hex identifiers account-wide years ago via the
    "longer ID" opt-in/opt-out mechanism, documented generically through
    `API_ModifyIdFormat.md` / `API_DescribeIdFormat.md` / `API_DescribeIdentityIdFormat.md` in the
    same APIReference tree — but I could not find an EC2-specific User Guide page in the local mirror
    that states the bit-length/entropy rationale explicitly; see doc-gap note below).
    17 hex chars ≈ 68 bits of identifier space.

**IDOR / enumeration framing:** Even at 68 bits, ENI IDs are not secrets and are not intended as an
access-control boundary — IAM authorization, not ID guessability, is what's supposed to gate access
(and §1 showed that gate is coarse-grained but still account/resource-scoped). The 8-char legacy format
(32 bits) is far more guessable/enumerable in principle, but (a) legacy IDs are a shrinking minority of
resources today, (b) guessing an ID alone is insufficient — the caller still needs IAM permission on
that specific ARN (or a wildcard resource grant) to act on it, and the ARN requires the correct
account ID, which is not enumerable from the eni-ID alone. So ID entropy is a secondary factor at best;
the primary control is IAM policy scope (§1) plus the account segment of the ARN, not ID secrecy.

**DryRun is not an ownership oracle.** Evidence:
- `/work/aws-docs/docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md`, "Check that users have
  the required permissions" section (anchor `#check-required-permissions`, lines 371-378): "If the
  Amazon EC2 action that you are testing creates or modifies a resource, you should make the request
  using the `DryRun` parameter... **the call completes the authorization check, but does not complete
  the operation**... If the test user has the required permissions, the request returns
  `DryRunOperation`; otherwise, it returns `UnauthorizedOperation`."
- `/work/aws-docs/docs/AWSEC2/latest/APIReference/API_RunInstances.md` (DryRun parameter definition,
  lines 78-81), worded identically across EC2 actions that document it: "Checks whether you have the
  required permissions for the operation, without actually making the request, and provides an error
  response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise,
  it is `UnauthorizedOperation`."
- This confirms the task's premise: `DryRun` short-circuits at the **IAM authorization** step and
  returns a boolean-ish signal (`DryRunOperation` vs `UnauthorizedOperation`) before the service even
  attempts to resolve/validate the target resource's existence or ownership in the normal request
  path. A caller cannot safely use `DryRun=true` responses on an arbitrary `NetworkInterfaceId` as a
  cross-account/ownership oracle ("does this ENI exist and do I have access") purely from this
  mechanism, because a policy scoped by ARN would already fail/deny before resource resolution
  regardless of whether the resource exists — the two failure reasons are not reliably distinguishable
  from the `DryRunOperation`/`UnauthorizedOperation` signal alone as documented.

**Doc gap (flagged, not guessed):**
- The **`API_UnassignPrivateIpAddresses.md`** and **`API_AssignPrivateIpAddresses.md`** pages
  themselves do **not** list a `DryRun` request parameter at all (confirmed by grep — zero matches in
  either file), unlike e.g. `API_RunInstances.md` or `API_DetachNetworkInterface.md`, which do list it
  explicitly. Since `DryRun` is a near-universal EC2 mutating-action parameter in practice (and the
  User Guide's generic "Check that users have the required permissions" section above treats it as
  available for "the Amazon EC2 action that you are testing" without exception), this looks like an
  omission in AWS's per-action API reference page rather than an actual absence of support — but I
  could not find a page in the local mirror that explicitly confirms `DryRun` is honored by
  `UnassignPrivateIpAddresses`/`AssignPrivateIpAddresses` specifically. Flagged as a documentation gap
  rather than assumed either way.
- I could not find a User-Guide page in the local mirror that states the EC2 resource-ID length
  migration (8-char → 17-char) bit-length/rationale specifically for `network-interface`/`eni-*` IDs;
  the evidence for the two formats here is drawn from live examples embedded in the API reference
  pages (cited above) rather than from an explicit "ID format" policy page. Flagged as a documentation
  gap for completeness, though the two ID-format shapes themselves are directly evidenced.

---

## Summary of answers

1. **Scoping gap** — Confirmed via full grep of `list_ec2.md`'s condition-key table (~148 keys): no
   key constrains which private IP or IPv4/IPv6 prefix is (un)assigned. `UnassignPrivateIpAddresses`
   is scopable by IAM only at whole-`network-interface` granularity. Unassigning a secondary IP that a
   DB failover VIP, HA cluster VIP, container/Pod IP, or an app's bound secondary IP relies on causes
   an availability-impacting, silent "virtual IP removed" event that other layers (SG, route table)
   won't reflect.

2. **Reassignment/takeover chain** — Confirmed via `API_AssignPrivateIpAddresses.md`:
   `AllowReassignment=true` lets `AssignPrivateIpAddresses` take an IP currently assigned to another
   ENI/instance and reassign it to the caller's target ENI; separately, an already-unassigned address
   (freed by `UnassignPrivateIpAddresses`) can be claimed by any other ENI in the same subnet without
   needing `AllowReassignment` at all. Chain: unassign victim's secondary IP → (re)assign it to an
   attacker ENI in the same subnet → subnet traffic to that IP now lands on the attacker. Requires two
   principals (or one compromised one) in the **same account**, each scoped per-ENI rather than
   per-IP, with ENIs in the same subnet. Rated Medium-High severity, intra-account only — not a
   cross-account issue, and not an AWS service bug, but a condition-key-coverage gap that customers
   composing least-privilege ENI-scoped policies should account for.

3. **Primary-IP protection** — Confirmed: the API and User Guide both state the action only ever
   targets *secondary* private IPv4 addresses / Prefix-Delegation prefixes; primary private IPs are
   explicitly documented as behaving differently (not reassignable/unassignable this way). This is a
   hard scope boundary limiting the blast radius of §2 to secondary addresses only.

4. **ENI ID entropy/IDOR** — `network-interface` ARNs are account-scoped
   (`arn:${Partition}:ec2:${Region}:${Account}:network-interface/${NetworkInterfaceId}`), so
   cross-account access is blocked by the account segment of the ARN/ownership, not by ID secrecy.
   Observed both legacy 8-hex (`eni-197d9972`) and current 17-hex (`eni-01d32da61c165ac3e`) ID formats
   directly in AWS's own API reference examples. `DryRun` is documented as an IAM-authorization-only
   check ("completes the authorization check, but does not complete the operation") and returns
   `DryRunOperation`/`UnauthorizedOperation` based on permission, not resource existence/ownership —
   so it is not usable as a reliable ownership/existence oracle. Flagged two doc gaps: (a) `DryRun` is
   not listed on the `Assign`/`UnassignPrivateIpAddresses` API reference pages themselves even though
   it's treated as universally available elsewhere in the docs; (b) no local-mirror User Guide page
   explicitly documents the 8→17-char ID-format migration rationale for `network-interface` IDs
   specifically.

## Sources consulted (local mirror paths)
- `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`
- `/work/aws-docs/docs/AWSEC2/latest/APIReference/API_UnassignPrivateIpAddresses.md`
- `/work/aws-docs/docs/AWSEC2/latest/APIReference/API_AssignPrivateIpAddresses.md`
- `/work/aws-docs/docs/AWSEC2/latest/APIReference/API_RunInstances.md` (DryRun parameter wording)
- `/work/aws-docs/docs/AWSEC2/latest/APIReference/CommonParameters.md` (confirmed DryRun is *not* a
  common/signing parameter — it's action-specific where documented)
- `/work/aws-docs/docs/AWSEC2/latest/UserGuide/using-eni.md`
- `/work/aws-docs/docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md`
- `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ec2-prefix-eni.md` (Prefix Delegation context, referenced)
- Sampled ENI-ID examples across `/work/aws-docs/docs/AWSEC2/latest/APIReference/*.md`
  (`API_AttachNetworkInterface.md`, `API_CreateNetworkInterfacePermission.md`,
  `API_DeleteNetworkInterface.md`, `API_UnassignIpv6Addresses.md`, etc.)

Note: a non-canonical file was observed alongside the official mirror,
`/work/aws-docs/docs/AWSEC2/latest/UserGuide/skill-agent_docs.aws.amazon.com_AWSEC2_latest_UserGuide_using-eni.html.md`
(and a sibling for `instance-purchasing-options.html`). These appear to be artifacts from a prior
agent/tool run rather than part of the official AWS doc sync, so they were not used as citation
sources for this analysis — only the canonical `using-eni.md` etc. paths were cited above.
