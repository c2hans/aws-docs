---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/redshift-enhanced-vpc-routing-enabled.html
---

# redshift-enhanced-vpc-routing-enabled
<a name="redshift-enhanced-vpc-routing-enabled"></a>

Checks if Amazon Redshift cluster has 'enhancedVpcRouting' enabled. The rule is NON\_COMPLIANT if 'enhancedVpcRouting' is not enabled or if the configuration.enhancedVpcRouting field is 'false'.

**Identifier:** REDSHIFT\_ENHANCED\_VPC\_ROUTING\_ENABLED

**Resource Types:** AWS::Redshift::Cluster

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Mexico (Central) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1313c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
