---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elb-cross-zone-load-balancing-enabled.html
---

# elb-cross-zone-load-balancing-enabled
<a name="elb-cross-zone-load-balancing-enabled"></a>

Checks if cross-zone load balancing is enabled for Classic Load Balancers. The rule is NON\_COMPLIANT if cross-zone load balancing is not enabled for Classic Load Balancers.

**Identifier:** ELB\_CROSS\_ZONE\_LOAD\_BALANCING\_ENABLED

**Resource Types:** AWS::ElasticLoadBalancing::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d789c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
