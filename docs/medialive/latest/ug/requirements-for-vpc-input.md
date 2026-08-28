---
source_url: https://docs.aws.amazon.com/medialive/latest/ug/requirements-for-vpc-input.html
---

# Requirements for Amazon Elastic Compute Cloud—VPC inputs
<a name="requirements-for-vpc-input"></a>

Your deployment might include push inputs that connect to MediaLive from a VPC that you created with Amazon VPC.

When a user creates this type of input on the MediaLive console, they have the option to choose the subnet and security group from a dropdown list. For the dropdown list to be populated with the resources in Amazon VPC, the user must have the appropriate permissions. For more information about Amazon VPC inputs, see [Creating an input](create-input.md).

The following table shows the actions in IAM that relate to access for populating the dropdown.

| Permissions | Service name in IAM | Actions |
| --- | --- | --- |
| View the VPC subnets and VPC security groups on the MediaLive console | EC2 | DescribeSubnets`DescribeSecurityGroups` |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaLive. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query medialive` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
