# `ec2:ManagedResourceOperator` and the requester-managed/AWS-managed ENI boundary
## Documentation-only analysis for `ec2:UnassignPrivateIpAddresses` research plan

Scope note: this document is produced entirely from AWS public documentation (local mirror at
`/work/aws-docs`, each file carrying a `source_url: https://docs.aws.amazon.com/...` front-matter
line pointing at the live page it was synced from). No AWS account, API, or network call against
real AWS infrastructure was made. Where documentation was thin or silent, this is called out
explicitly as "doc-gap" rather than inferred.

---

## 1. What `ec2:ManagedResourceOperator` is, per AWS documentation

**Primary definition** (service-authorization reference, the authoritative IAM condition-key list):

> Source: `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md` (line 10111),
> mirrors `https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html`
>
> | Condition key | Description | Type |
> |---|---|---|
> | `ec2:ManagedResourceOperator` | **"Filters access by the presence of an EC2 operator provisioning a managed resource"** | String |

The link target for this row, and the only other place the key is named in the EC2 User Guide
index, is `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#amazon-ec2-keys`
("Condition keys for Amazon EC2"). **Doc-gap**: the local mirror of that very page
(`/work/aws-docs/docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md`) contains the
`#amazon-ec2-keys` anchor and surrounding prose about condition keys in general, but
`grep -n "ManagedResourceOperator"` against that file returns **zero matches** — the key is
referenced by URL fragment but not actually discussed, defined, or exemplified in that User Guide
page's prose. The one-line table description above is the only explicit definition of the key
anywhere in the documentation corpus I could find. (I attempted to re-fetch the live
`list_ec2.html` page via WebFetch to cross-check freshness; the page is large enough that the
fetch tool's summarizer truncated before reaching the condition-key table, so this could not be
independently re-confirmed online in this session — treat the mirror's text as the source of
record, consistent with the task's note that online re-verification might not be fully available.)

**What it binds to and what values it takes** — not stated explicitly as a definition, but
recoverable with high confidence from *usage examples* in AWS's own published managed-policy
documentation (Section 3 below): the key's value is a string identifying the specific **AWS
service "operator"** that is provisioning/operating a resource on the customer's behalf, in a
format resembling a service-principal-ish operator name, e.g.:
- `scaler.lambda.amazonaws.com` (Lambda's managed-instance capacity scaler)
- `network-connectors.lambda.amazonaws.com` (Lambda's network-connector ENI manager)
- `workspaces-instances.amazonaws.com` (WorkSpaces Instances)
- `bedrock-agentcore.amazonaws.com` (Bedrock AgentCore runtime)

Every observed usage is `"StringEquals"` (or `"StringLike"` once) matching one single operator
string, always inside an **Allow** statement attached to an **AWS service-linked role**, never
inside a Deny and never inside a policy meant to be attached to an ordinary customer
principal/user/role for restricting *that user's own* actions. I found no documentation anywhere
stating the key is absent/null for ordinary customer-initiated API calls, but that is the only
coherent reading consistent with "Filters access by the **presence** of an EC2 operator" — i.e.,
it is populated by EC2 when the call is attributable to an AWS service's own operator role acting
on a managed resource, and (by implication, undocumented explicitly — doc-gap) presumably absent
otherwise.

---

## 2. Requester-managed / AWS-managed network interfaces (EC2 User Guide concept)

Source: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/requester-managed-eni.md`
(`https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requester-managed-eni.html`)

> "A requester-managed network interface is a network interface that an AWS service creates in
> your VPC on your behalf. The network interface is associated with a resource for another
> service, such as a DB instance from Amazon RDS, a NAT gateway, or an interface VPC endpoint from
> AWS PrivateLink."

And from `using-eni.md` (`https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html`),
line 74-75:

> "**Requester-managed network interfaces** — These network interfaces are created and managed by
> AWS services to enable you to use some resources and services. You can't manage these network
> interfaces yourself."

**Which services create managed ENIs** — the docs explicitly name only two in the definition
paragraph above (RDS, NAT gateway) plus one ("an interface VPC endpoint from AWS PrivateLink") as
named examples, not an exhaustive list. The companion CLI example output in the same page shows
real-world `Description` strings for requester-managed ENIs actually observed:
"VPC Endpoint Interface" (PrivateLink / interface endpoints) and "Resource Gateway Interface"
(`rgw-...`). **Doc-gap**: AWS does not publish a complete, authoritative enumeration of every
service that creates requester-managed ENIs (ELB/ALB/NLB, Lambda VPC-attached functions, EFS
mount targets, Transit Gateway, WorkSpaces, etc. are well-known in practice/community knowledge
to also create requester-managed or service-linked ENIs, and this research plan's own managed-policy
survey in Section 3 independently corroborates Lambda, RDS, FSx, API Gateway, VPC Lattice,
Bedrock AgentCore, and EKS as ENI-IP-managing operators — but the EC2 User Guide concept page
itself only names RDS, NAT gateway, and PrivateLink by name).

**Who is "operator"/requester vs owner**: per the Console field description in the same page —

> "**Requester ID**: The alias or AWS account ID of the principal or service that created the
> network interface. If you created the network interface, this is your AWS account ID.
> Otherwise, another principal or service created it."

So the ENI's ARN (`arn:aws:ec2:${Region}:${Account}:network-interface/${id}`) lives in the
**customer's own account** — the customer owns/is billed for/counts-against-quota for the
resource — while the **Requester ID** attributes creation/operation to the AWS service (or an
AWS-internal principal acting for that service), not the customer. This is the precise
owner-vs-operator split the task asked about: **account-level ownership stays with the customer;
operational control is delegated to an AWS service.**

### (a) Can a customer IAM principal call `UnassignPrivateIpAddresses` on a requester-managed ENI?

**Blocked — and explicitly documented, but blocked at the EC2 service/API layer, not via IAM.**
Same source, "Considerations" bullet list:

> "You can view the requester-managed network interfaces in your account and you can add or
> remove tags. However, **you can't perform the following actions** on a requester-managed
> network interface:
> + Modify network interface attributes
> + Attach or detach the network interface
> + Associate or disassociate Elastic IP addresses
> + **Assign or unassign private IP addresses**
> + Specify the network interface when launching an instance
>
> You can still reset network interface attributes, even though you can't modify them."

This is a direct, named statement that `ec2:AssignPrivateIpAddresses` /
`ec2:UnassignPrivateIpAddresses` cannot be performed by the customer against a requester-managed
ENI — **regardless of what the customer's IAM policy allows**. This is EC2 resource-state/business
logic (an API-level guard keyed off the ENI's `requester-managed` attribute), not an IAM
authorization decision. Corroborating **doc-gap**: the API reference page itself
(`/work/aws-docs/docs/AWSEC2/latest/APIReference/API_UnassignPrivateIpAddresses.md`,
mirrors `https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnassignPrivateIpAddresses.html`)
has an "Errors" section that says only "For information about the errors that are common to all
actions, see Common Error Types" — it does **not** name a specific error code/message for the
requester-managed-ENI case, and does not cross-reference `requester-managed-eni.md` at all. So the
restriction is real and documented, but only in the User Guide concept page, not in the API
reference for the action itself — a practitioner reading only the API reference would not learn
about this guard.

### (b) Is `ec2:ManagedResourceOperator` the customer's mechanism to Deny their own principals from touching service-managed ENIs?

**No evidence that this is its documented purpose; strong evidence it is not, from how AWS itself uses it.**
See Section 3 for the full survey. In every example found across the mirror, AWS uses
`ec2:ManagedResourceOperator` as an **Allow-side scoping condition inside AWS's own
service-linked-role policies** — i.e., it restricts what *the AWS service's own operator role* is
allowed to touch (only resources tagged/attributed to that specific operator), not something a
customer is instructed to use in a Deny statement against their own IAM principals. I found:
- No AWS-published example IAM policy (customer-facing) using this key as a Deny condition.
- No User Guide "how to block your users from touching managed ENIs" guidance referencing this key.
- No statement in `requester-managed-eni.md`, `using-eni.md`, or `iam-policies-for-amazon-ec2.md`
  recommending `ec2:ManagedResourceOperator` as the tool for that job.

The actual, documented protection against a customer's own principal mutating a requester-managed
ENI's private IPs is the **EC2-side hard block described in 3(a) above** — a resource-state
guard, not an IAM condition the customer configures. Based purely on the public documentation
available, `ec2:ManagedResourceOperator` reads as an AWS-internal least-privilege mechanism for
scoping **AWS's own service-linked/service-operator roles**, not a customer-facing control
surface for this purpose. Treating it as "the" customer lever to prevent accidental/malicious
unassign-IP calls against managed ENIs would be a documentation-unsupported assumption.

### (c) Is this condition key present in any AWS-published sample policy, AWS-managed policy, or User Guide example for network-interface actions — or absent (insecure-by-omission)?

Both, depending on the action:

- **Present, but never for IP-assignment actions.** Across the AWS Managed Policy Reference Guide
  mirror (`/work/aws-docs/docs/aws-managed-policy/latest/reference/*.md`), `ec2:ManagedResourceOperator`
  appears in real AWS-managed policy JSON for: `AWSLambdaManagedEC2ResourceOperator`
  (`ec2:RunInstances`, `ec2:AttachNetworkInterface`, scoped to `scaler.lambda.amazonaws.com`),
  `AWSLambdaNetworkConnectorOperatorPolicy` (`ec2:CreateTags` scoped to
  `network-connectors.lambda.amazonaws.com`), `AWSLambdaServiceRolePolicy`
  (`ec2:TerminateInstances` / `ec2:DeleteNetworkInterface`, same two operator strings),
  `AWSServiceRolePolicyForWorkspacesInstances` (via `workspaces-core` service-linked-role doc,
  `workspaces-instances.amazonaws.com`), and `BedrockAgentCoreRuntimeInstancesOperatorRolePolicy`
  / the Bedrock AgentCore service-linked-role doc (`ec2:TerminateInstances`,
  `ec2:DetachVolume`, `ec2:AttachNetworkInterface`, `ec2:RunInstances` against
  `launch-template`, scoped to `bedrock-agentcore.amazonaws.com`).
- **Absent exactly where this research plan cares most**: I grepped every AWS-managed policy in
  the mirror that actually grants `ec2:UnassignPrivateIpAddresses` —
  `AmazonEKS_CNI_Policy`, `AWSLambdaENIManagementAccess`,
  `AmazonVPCCrossAccountNetworkInterfaceOperations`, `AmazonRDSServiceRolePolicy`,
  `AmazonFSxServiceRolePolicy`, `APIGatewayServiceRolePolicy`, `AWSVpcLatticeServiceRolePolicy`,
  `BedrockAgentCoreNetworkServiceRolePolicy`, `AmazonEKSNetworkingPolicy`,
  `AmazonEKSVPCResourceController` — and **none of them condition that grant on
  `ec2:ManagedResourceOperator`**. Where a condition exists at all, it is a different mechanism:
  `BedrockAgentCoreNetworkServiceRolePolicy`'s `AllowManageEniWhenBedrockManaged` statement scopes
  `ec2:AssignPrivateIpAddresses`/`ec2:UnassignPrivateIpAddresses` via
  `"StringEquals": {"aws:ResourceTag/AmazonBedrockAgentCoreManaged": "true"}` — a resource **tag**
  condition, not `ec2:ManagedResourceOperator`. Most tellingly,
  **`AmazonVPCCrossAccountNetworkInterfaceOperations`** — an AWS managed policy explicitly
  documented as attachable directly to customer users/groups/roles ("You can attach
  `AmazonVPCCrossAccountNetworkInterfaceOperations` to your users, groups, and roles") — grants
  `ec2:AssignPrivateIpAddresses` and `ec2:UnassignPrivateIpAddresses` on `Resource: "*"`
  with **no condition block at all**.
- **Example policies page**: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md`
  (the EC2 User Guide's own curated example-policy catalog) contains **zero** occurrences of
  either `ManagedResourceOperator` or `UnassignPrivateIp` (`grep -c` = 0 for both).

**Conclusion for 3(c): insecure-by-omission is the accurate characterization for this action.**
The service-authorization reference *lists* `ec2:ManagedResourceOperator` as a valid, available
condition key for `ec2:UnassignPrivateIpAddresses` (and its sibling `ec2:UnassignIpv6Addresses`),
but no AWS-published policy — customer sample, AWS-managed policy, or service-linked-role policy
— actually uses it to scope that action, even where AWS itself grants the action broadly to a
customer-attachable managed policy (`AmazonVPCCrossAccountNetworkInterfaceOperations`) with no
condition whatsoever. A security-research plan should not assume the key's mere *availability* in
the IAM condition-key list implies any AWS-recommended or AWS-practiced usage pattern for this
specific action; the documented real-world scoping pattern for *this* action family is resource
tags (as in the Bedrock AgentCore case), not `ManagedResourceOperator`.

---

## 4. Service-plane boundary: where does responsibility sit?

Flagging explicitly, per the task's instruction:

- **Not a cross-account / service-plane breach by itself.** A requester-managed ENI's ARN is
  `arn:aws:ec2:${Region}:${CustomerAccount}:network-interface/${id}` — it is owned by, billed to,
  and counted against the **customer's own account** quotas (confirmed by `requester-managed-eni.md`'s
  "you can view the requester-managed network interfaces **in your account**" and the
  Requester-ID field description distinguishing *your* account from the creating principal/service).
  A customer IAM principal with sufficient EC2 permissions calling an EC2 API against such an ENI
  is operating entirely within its own account boundary — there is no account-isolation or
  service-plane wall being crossed merely by naming the resource. (Whether the call *succeeds* is
  the separate EC2 resource-state question answered in 3(a): assign/unassign and several other
  mutating actions are hard-blocked by EC2 itself for requester-managed ENIs, independent of IAM.)
- **It is, however, a shared-responsibility / availability concern one layer up.** The ENI backs
  another AWS service's control/data plane for that customer (an RDS instance's network path, a
  NAT gateway, a PrivateLink interface endpoint, etc.). Even where EC2's own guard prevents the
  *specific* IP-reassignment actions outright, the broader pattern of a customer's own
  over-broad IAM principal being able to read, tag, or (for the subset of actions EC2 does not
  block — e.g. the AWS-managed `AmazonVPCCrossAccountNetworkInterfaceOperations` policy explicitly
  grants `ec2:AssignPrivateIpAddresses`/`ec2:UnassignPrivateIpAddresses` with no scoping) actually
  mutate IPs on an ENI backing a managed service is a documented-by-omission availability risk:
  breaking that managed service's data plane (e.g., unassigning a PrivateLink endpoint's or NAT
  gateway's working secondary IP) degrades a service AWS is operating on the customer's behalf,
  but the fault and remediation responsibility for having granted that over-broad IAM permission
  sits with the **customer**, consistent with the standard AWS shared-responsibility model (AWS
  secures/operates the service's own control plane; the customer is responsible for how they
  configure IAM access to the underlying EC2 resources in their own account, including ENIs AWS
  provisioned there on their behalf).
- **Line, stated plainly**: Account/identity boundary = not crossed (same customer account
  throughout). Resource-mutation boundary = enforced by EC2 itself for the specific
  assign/unassign-IP and several other actions on requester-managed ENIs (3a), independent of
  IAM. Availability/blast-radius boundary = the customer's responsibility, via how permissively
  they scope IAM for `network-interface*` actions — and the documentation record shows AWS's own
  published policies are not uniformly conservative here (the no-condition
  `AmazonVPCCrossAccountNetworkInterfaceOperations` grant being the clearest example).

---

## Summary of citations used

| Claim | File (local mirror) | Live URL |
|---|---|---|
| `ec2:ManagedResourceOperator` definition | `docs/service-authorization/latest/reference/list_ec2.md` (L10111) | `https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html` |
| Condition keys listed for `UnassignPrivateIpAddresses` | `docs/service-authorization/latest/reference/list_ec2.md` (L9696-9700) | same |
| Requester-managed ENI definition + action block list | `docs/AWSEC2/latest/UserGuide/requester-managed-eni.md` | `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/requester-managed-eni.html` |
| "created and managed by AWS services... can't manage yourself" | `docs/AWSEC2/latest/UserGuide/using-eni.md` (L74-75) | `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html` |
| `ec2:ManagedResourceOperator` absent from EC2 condition-key prose page | `docs/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.md` | `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html#amazon-ec2-keys` |
| `AWSLambdaManagedEC2ResourceOperator` JSON (operator = `scaler.lambda.amazonaws.com`) | `docs/aws-managed-policy/latest/reference/AWSLambdaManagedEC2ResourceOperator.md` | `https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaManagedEC2ResourceOperator.html` |
| `AWSLambdaNetworkConnectorOperatorPolicy` JSON (operator = `network-connectors.lambda.amazonaws.com`) | `docs/aws-managed-policy/latest/reference/AWSLambdaNetworkConnectorOperatorPolicy.md` | `https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSLambdaNetworkConnectorOperatorPolicy.html` |
| WorkSpaces operator = `workspaces-instances.amazonaws.com` | `docs/workspaces-core/latest/ag/using-service-linked-roles.md` (L52-58) | `https://docs.aws.amazon.com/workspaces-core/latest/ag/using-service-linked-roles.html` |
| Bedrock AgentCore operator = `bedrock-agentcore.amazonaws.com` | `docs/bedrock-agentcore/latest/devguide/service-linked-roles.md` (L405-517) | `https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/service-linked-roles.html` |
| `AmazonVPCCrossAccountNetworkInterfaceOperations` — unconditioned Unassign/AssignPrivateIpAddresses, customer-attachable | `docs/aws-managed-policy/latest/reference/AmazonVPCCrossAccountNetworkInterfaceOperations.md` | `https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonVPCCrossAccountNetworkInterfaceOperations.html` |
| `BedrockAgentCoreNetworkServiceRolePolicy` — tag-scoped (not operator-scoped) Assign/UnassignPrivateIpAddresses | `docs/aws-managed-policy/latest/reference/BedrockAgentCoreNetworkServiceRolePolicy.md` | `https://docs.aws.amazon.com/aws-managed-policy/latest/reference/BedrockAgentCoreNetworkServiceRolePolicy.html` |
| `UnassignPrivateIpAddresses` API reference — no specific error documented for requester-managed ENI case | `docs/AWSEC2/latest/APIReference/API_UnassignPrivateIpAddresses.md` | `https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnassignPrivateIpAddresses.html` |
| `ExamplePolicies_EC2.md` — zero hits for `ManagedResourceOperator` or `UnassignPrivateIp` | `docs/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md` | `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.html` |
