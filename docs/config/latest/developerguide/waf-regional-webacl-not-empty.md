---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/waf-regional-webacl-not-empty.html
---

# waf-regional-webacl-not-empty
<a name="waf-regional-webacl-not-empty"></a>

Checks if a WAF regional Web ACL contains any WAF rules or rule groups. The rule is NON\_COMPLIANT if there are no WAF rules or rule groups present within a Web ACL.

**Identifier:** WAF\_REGIONAL\_WEBACL\_NOT\_EMPTY

**Resource Types:** AWS::WAFRegional::WebACL

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1635c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
