---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/elbv2-predefined-security-policy-ssl-check.html
---

# elbv2-predefined-security-policy-ssl-check
<a name="elbv2-predefined-security-policy-ssl-check"></a>

Checks if listeners for Application Load Balancers (ALBs) or Network Load Balancers (NLBs) use certain security policies. The rule is NON\_COMPLIANT if an HTTPS listener for an ALB or a TLS listener for a NLB does not use the security policies you specify.

**Identifier:** ELBV2\_PREDEFINED\_SECURITY\_POLICY\_SSL\_CHECK

**Resource Types:** AWS::ElasticLoadBalancingV2::Listener

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Israel (Tel Aviv), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

sslPoliciesType: CSV
Comma-separated list of SSL security policies for the rule to check. For example, "ELBSecurityPolicy-TLS13-1-2-2021-06".

## AWS CloudFormation template
<a name="w2aac20c16c17b7d781c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
