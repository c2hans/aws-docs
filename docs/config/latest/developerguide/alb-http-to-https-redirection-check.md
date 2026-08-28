---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/alb-http-to-https-redirection-check.html
---

# alb-http-to-https-redirection-check
<a name="alb-http-to-https-redirection-check"></a>

Checks if HTTP to HTTPS redirection is configured on all HTTP listeners of Application Load Balancers. The rule is NON\_COMPLIANT if one or more HTTP listeners of Application Load Balancer do not have HTTP to HTTPS redirection configured. The rule is also NON\_COMPLIANT if one of more HTTP listeners have forwarding to an HTTP listener instead of redirection.

**Identifier:** ALB\_HTTP\_TO\_HTTPS\_REDIRECTION\_CHECK

**Resource Types:** AWS::ElasticLoadBalancingV2::LoadBalancer

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7c21c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
