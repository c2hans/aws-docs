---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/using-service-linked-roles-aws-org-discovery.html
---

# Service-linked roles for AWS Organization discovery in AWS Data Exchange
<a name="using-service-linked-roles-aws-org-discovery"></a>

AWS Data Exchange uses the service-linked role named `AWSServiceRoleForAWSDataExchangeOrganizationDiscovery` – this role allows AWS Data Exchange to retrieve information about your AWS organization to determine eligibility for AWS Data Exchange data grants license distribution.

**Note**
This role is only needed in the AWS Organization's management account.

The `AWSServiceRoleForAWSDataExchangeOrganizationDiscovery` service-linked role trusts the following services to assume the role:
+ `organization-discovery.dataexchange.amazonaws.com`

The role permissions policy named `AWSDataExchangeServiceRolePolicyForOrganizationDiscovery` allows AWS Data Exchange to complete the following actions on the specified resources:
+ Actions:
  + `organizations:DescribeOrganization`
  + `organizations:DescribeAccount`
  + `organizations:ListAccounts`
+ Resources:
  + All resources (`*`)

For more information about the `AWSDataExchangeServiceRolePolicyForOrganizationDiscovery` role, see [AWS managed policy: AWSDataExchangeServiceRolePolicyForOrganizationDiscovery](security-iam-awsmanpol.md#security-iam-awsmanpol-awsdataexchangeservicerolepolicyfororganizationdiscovery).

For more information about using the `AWSServiceRoleForAWSDataExchangeOrganizationDiscovery` service-linked role, see [Using service-linked roles for AWS Data Exchange](using-service-linked-roles-adx.md) earlier in this section.

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
