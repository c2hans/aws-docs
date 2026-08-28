---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/api-gw-associated-with-waf.html
---

# api-gw-associated-with-waf
<a name="api-gw-associated-with-waf"></a>

Checks if an Amazon API Gateway API stage is using an AWS WAF web access control list (web ACL). The rule is NON\_COMPLIANT if an AWS WAF Web ACL is not used or if a used AWS Web ACL does not match what is listed in the rule parameter.

**Identifier:** API\_GW\_ASSOCIATED\_WITH\_WAF

**Resource Types:** AWS::ApiGateway::Stage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Taipei) Region

**Parameters:**

WebAclArns (Optional)Type: CSV
Comma-separated list of web ACL Amazon Resource Names (ARNs)

## AWS CloudFormation template
<a name="w2aac20c16c17b7c73c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
