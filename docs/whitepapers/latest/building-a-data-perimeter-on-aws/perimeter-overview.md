---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-a-data-perimeter-on-aws/perimeter-overview.html
---

# Perimeter overview
<a name="perimeter-overview"></a>

This section provides an overview of a data perimeter’s objectives and the AWS services used to implement it.

**Topics**
+ [Perimeter objectives](#perimeter-objectives)
+ [AWS services](#aws-services)

## Perimeter objectives
<a name="perimeter-objectives"></a>

The goal of an AWS perimeter is to ensure access is allowed only if an authorization involves:
+ **Only trusted identities** - The [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) principals in your AWS organization or AWS acting on your behalf.
+ **Only trusted resources** - The resources in your AWS organization or resources AWS operates on your behalf.
+ **Only expected networks** - Your virtual private cloud (VPC) and on-premises networks or the networks AWS uses on your behalf.

These are the necessary (but not sufficient) authorization conditions for access inside an AWS perimeter to be allowed.

`Access in the Perimeter⇒(Trusted Identity)∧(Trusted Resource)∧(Expected Network)`

Ensuring the truth of these three conditions ultimately defines the objectives of the perimeter. Each authorization condition has two objectives.

- ** **Only trusted identities** **
  -  Ensure that my resources can be accessed by only trusted identities.
  -  Ensure that only trusted identities are allowed from my networks.

- ** **Only trusted resources ** **
  -  Ensure that my identities can access only trusted resources.
  -  Ensure that only trusted resources can be accessed from my networks.

- ** **Only expected networks ** **
  -  Ensure that my identities can access resources only from expected networks.
  -  Ensure my resources can only be accessed from expected networks.

## AWS services
<a name="aws-services"></a>

You can establish a data perimeter by using permissions guardrails that restrict access outside of an organization boundary. This is achieved using three primary AWS capabilities, AWS Organizations [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs), [resource control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html) (RCPs), and [VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html). The following is a summary of these different types of policies and some considerations.

### Service control policies
<a name="service-control-policies"></a>

SCPs are a type of organization policy that you can use to manage permissions in your organization and control the maximum available permissions for your principals. SCPs offer central control over the maximum available permissions for all principals in your organization. SCPs configured as [deny lists](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_evaluation.html#how_scps_deny) can limit the scope of access to resources or source networks in your organization or within specific accounts. It’s important to note that [SCPs do not apply](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html#scp-effects-on-permissions) to [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) (SLR) or [AWS service principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services).

Although you can define similar controls with IAM [identity-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html), the solutions in this document will favor using SCPs. They are a more scalable way to implement permissions guardrails for all your IAM principals than creating and managing individual policies for every IAM principal you own. However, access to resources in AWS requires explicit permissions in identity-based policies, so they are still a necessary component of providing access, but not as part of establishing data perimeter guardrails.

 SCPs are primarily going to use the `aws:ResourceOrgID` condition for achieving only trusted resources and `aws:SourceIp`, `aws:SourceVpc`, and `aws:ViaAWSService` as the conditions for achieving only expected networks as well as for managing exceptions required in the policies. Refer to **service\_control\_policies** in the [data perimeter policy examples repo](https://github.com/aws-samples/data-perimeter-policy-examples) for more details.

### Resource control policies
<a name="resource-control-policies"></a>

RCPs are a type of organization policy that you can use to control the maximum available permissions for resources in your organization. When you use RCPs with [supported services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html#rcp-supported-services), you can limit the scope of access to identities or source networks in your organization. Similarly to SCPs, RCPs do not apply to SLRs. RCPs, however, can be used to limit access by [AWS service principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services).

Although you can define similar controls with [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html), the solutions in this document favor using RCPs. They are a more scalable way to implement permissions guardrails on resources in your organization than creating and managing individual policies for every resource you own. RCPs help central admin teams to enforce security invariants and provide developers more freedom to manage resource-based policies. Developers can use resource-based policies to grant permissions as required by their applications. They are commonly used to provide cross-account access, and can be used to authorize external AWS credentials or anonymous access. Resource-based policies can also be used to apply data perimeter guardrails on resources that are not yet supported by RCPs. For a list of services that support resource-based policies, refer to [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html). See the *AWS Organizations User Guide* for the [List of AWS services that support RCPs](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html#rcp-supported-services).

Resource control policies are primarily going to use:
+ `aws:PrincipalOrgID`, `aws:PrincipalIsAWSService`, and `aws:SourceOrgID` conditions to achieve only trusted identities
+ `aws:SourceIp`, `aws:SourceVpc`, `aws:ViaAWSService`, and `aws:PrincipalIsAWSService` as conditions for achieving only expected networks, as well as for managing exceptions required in the policies

Refer to **resource\_control\_policies** in the [data perimeter policy examples repo](https://github.com/aws-samples/data-perimeter-policy-examples?tab=readme-ov-file#policy-types) for more details.

### VPC endpoint policies
<a name="vpc-endpoint-policies"></a>

These policies are a special type of resource-based policy that you attach to an endpoint that controls access to resources when they are accessed through that VPC endpoint. An endpoint policy does not override or replace IAM user policies or service-specific policies (such as Amazon S3 bucket policies). It is a separate policy for controlling access from the endpoint to the specified service. In VPC networks, traffic is routed to VPC endpoints automatically if you are using an AWS-provided domain name system (DNS).

For on-premises networks, you can also route AWS traffic through VPC endpoints if they are connected to AWS with Direct Connect or a VPN. For services that have [AWS PrivateLink](https://aws.amazon.com/privatelink/) interface endpoints, you can route traffic to those endpoints directly from an on-premises network. For a list of services that support VPC endpoints and VPC endpoint policies, refer to [AWS services that integrate with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/integrated-services-vpce-list.html).

 VPC endpoint policies are primarily going to use the `aws:PrincipalOrgID` and `aws:PrincipalIsAWSService` conditions to achieve only trusted identities and the `aws:ResourceOrgID` condition to achieve only trusted resources. Refer to **vpc\_endpoint\_policies** in the [data perimeter policy examples repo](https://github.com/aws-samples/data-perimeter-policy-examples) for more details.

**Note**
 For a VPC endpoint policy, it’s important to explicitly specify the AWS organization ID in the condition. **DO NOT** use a condition like this:

```
"Condition": {
  "StringNotEquals": {
    "aws:ResourceOrgID": "${aws:PrincipalOrgID}"
  }
}
```
 If an unintended principal in a different AWS organization tries to access a resource in their own organization over the VPC endpoint, this condition won’t deny the action because the values for both keys in the request context, `aws:ResourceOrgID` and `aws:PrincipalOrgID`, will be the unintended principal’s organization ID. This is different from an SCP because SCPs are only applied to principals that are part of your organization, but a VPC endpoint policy can apply to any principal. Instead, use a condition like the following in a VPC endpoint policy:

```
"Condition": {
  "StringNotEquals": {
    "aws:ResourceOrgID": "<my-org-id>",
    "aws:PrincipalOrgID": "<my-org-id>"
  }
}
```

### Summary
<a name="summary-1"></a>

The following table outlines how the different types of policies are used to achieve the perimeter objectives to support the necessary authorization conditions.

- ** **Only trusted identities ****
  - **Perimeter objective:**  Ensure that my resources can be accessed by only trusted identities.  / **Policy type used:**  RCPs  / **Primary IAM condition(s) used:**  aws:PrincipalOrgID, aws:PrincipalIsAWSService, aws:SourceOrgID
  - **Perimeter objective:**  Ensure that only trusted identities are allowed from my networks.  / **Policy type used:**  VPC endpoint policies  / **Primary IAM condition(s) used:**  aws:PrincipalOrgID, aws:PrincipalIsAWSService

- ** **Only trusted resources****
  - **Perimeter objective:**  Ensure that my identities can access only trusted resources.  / **Policy type used:**  SCPs  / **Primary IAM condition(s) used:**  aws:ResourceOrgID
  - **Perimeter objective:**  Ensure that only trusted resources can be accessed from my networks.  / **Policy type used:**  VPC endpoint policies  / **Primary IAM condition(s) used:**  aws:ResourceOrgID

- ** **Only expected networks****
  - **Perimeter objective:**  Ensure that my identities can access resources only from expected networks.  / **Policy type used:**  SCPs  / **Primary IAM condition(s) used:**  aws:SourceIp, aws:SourceVpc, aws:ViaAWSService
  - **Perimeter objective:**  Ensure my resources can only be accessed from expected networks.  / **Policy type used:**  RCPs / **Primary IAM condition(s) used:**  aws:SourceIp, aws:SourceVpc, aws:ViaAWSService, aws:PrincipalIsAWSService

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
