---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elb-deletion-protection-enabled.html
---

# elb-deletion-protection-enabled
<a name="elb-deletion-protection-enabled"></a>

Checks whether an Elastic Load Balancer has deletion protection enabled. The rule is NON\_COMPLIANT if deletion\_protection.enabled is false.

**Identifier:** ELB\_DELETION\_PROTECTION\_ENABLED

**Resource Types:** AWS::ElasticLoadBalancingV2::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d793c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
