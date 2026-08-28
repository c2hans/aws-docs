---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/clb-multiple-az.html
---

# clb-multiple-az
<a name="clb-multiple-az"></a>

Checks if a Classic Load Balancer spans multiple Availability Zones (AZs). The rule is NON\_COMPLIANT if a Classic Load Balancer spans less than 2 AZs or does not span number of AZs mentioned in the `minAvailabilityZones` parameter (if provided).

**Identifier:** CLB\_MULTIPLE\_AZ

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except AWS GovCloud (US-East), AWS GovCloud (US-West), Asia Pacific (Taipei) Region

**Parameters:**

minAvailabilityZones (Optional)Type: int
Desired minimum number of expected AZs. Valid values are between 2 and 10, both inclusive. Default value is 2 if parameter is not specified.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d291c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
