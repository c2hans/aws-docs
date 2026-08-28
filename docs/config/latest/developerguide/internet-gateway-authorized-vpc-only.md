---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/internet-gateway-authorized-vpc-only.html
---

# internet-gateway-authorized-vpc-only
<a name="internet-gateway-authorized-vpc-only"></a>

Checks if internet gateways are attached to an authorized virtual private cloud (Amazon VPC). The rule is NON\_COMPLIANT if internet gateways are attached to an unauthorized VPC.

**Identifier:** INTERNET\_GATEWAY\_AUTHORIZED\_VPC\_ONLY

**Resource Types:** AWS::EC2::InternetGateway

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

AuthorizedVpcIds (Optional)Type: CSV
Comma-separated list of the authorized VPC IDs with attached IGWs. If parameter is not provided all attached IGWs will be NON\_COMPLIANT.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d981c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
