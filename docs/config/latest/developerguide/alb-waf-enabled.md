---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/alb-waf-enabled.html
---

# alb-waf-enabled
<a name="alb-waf-enabled"></a>

Checks if Web Application Firewall (WAF) is enabled on Application Load Balancers (ALBs). This rule is NON\_COMPLIANT if key: waf.enabled is set to false.

**Identifier:** ALB\_WAF\_ENABLED

**Resource Types:** AWS::ElasticLoadBalancingV2::LoadBalancer

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

wafWebAclIds (Optional)Type: CSV
Comma separated list of web ACL ID (for WAF) or web ACL ARN (for WAFV2) checking for ALB association

## AWS CloudFormation template
<a name="w2aac20c16c17b7c29c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
