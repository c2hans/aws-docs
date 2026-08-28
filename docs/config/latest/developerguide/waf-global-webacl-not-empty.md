---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/waf-global-webacl-not-empty.html
---

# waf-global-webacl-not-empty
<a name="waf-global-webacl-not-empty"></a>

Checks whether a WAF Global Web ACL contains any WAF rules or rule groups. This rule is NON\_COMPLIANT if a Web ACL does not contain any WAF rule or rule group.

**Identifier:** WAF\_GLOBAL\_WEBACL\_NOT\_EMPTY

**Resource Types:** AWS::WAF::WebACL

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1629c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
