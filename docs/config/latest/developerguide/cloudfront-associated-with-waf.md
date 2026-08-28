---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-associated-with-waf.html
---

# cloudfront-associated-with-waf
<a name="cloudfront-associated-with-waf"></a>

Checks if Amazon CloudFront distributions are associated with either web application firewall (WAF) or WAFv2 web access control lists (ACLs). The rule is NON\_COMPLIANT if a CloudFront distribution is not associated with a WAF web ACL.

**Identifier:** CLOUDFRONT\_ASSOCIATED\_WITH\_WAF

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

wafWebAclIds (Optional)Type: CSV
Comma-separated list of web ACL IDs for WAF or web ACL Amazon Resource Names (ARNs) for WAFV2

## AWS CloudFormation template
<a name="w2aac20c16c17b7d303c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
