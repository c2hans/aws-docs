---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/service-vpc-endpoint-enabled.html
---

# service-vpc-endpoint-enabled
<a name="service-vpc-endpoint-enabled"></a>

Checks if Service Endpoint for the service provided in rule parameter is created for each Amazon Virtual Private Cloud (Amazon VPC). The rule is NON\_COMPLIANT if an Amazon VPC doesn't have an Amazon VPC endpoint created for the service.

**Identifier:** SERVICE\_VPC\_ENDPOINT\_ENABLED

**Resource Types:** AWS::EC2::VPC

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

serviceNameType: String
The short name or suffix for the service. Note: To get a list of available service names or valid suffix list, use DescribeVpcEndpointServices.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1523c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
