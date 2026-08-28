---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/alb-http-drop-invalid-header-enabled.html
---

# alb-http-drop-invalid-header-enabled
<a name="alb-http-drop-invalid-header-enabled"></a>

Checks if rule evaluates AWS Application Load Balancers (ALB) to ensure they are configured to drop http headers. The rule is NON\_COMPLIANT if the value of routing.http.drop\_invalid\_header\_fields.enabled is set to false

**Identifier:** ALB\_HTTP\_DROP\_INVALID\_HEADER\_ENABLED

**Resource Types:** AWS::ElasticLoadBalancingV2::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7c19c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
