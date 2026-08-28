---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-ssl-policy-check.html
---

# cloudfront-ssl-policy-check
<a name="cloudfront-ssl-policy-check"></a>

Checks if Amazon CloudFront distributions are configured with the specified security policies.The rule is NON\_COMPLIANT if a CloudFront Distribution is not configured with security policies that you specify.

**Identifier:** CLOUDFRONT\_SSL\_POLICY\_CHECK

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

securityPoliciesType: CSV
Comma-separated list of CloudFront distribution security policies for the rule to check. For example: "TLSv1.2\_2018, TLSv1.2\_2019, TLSv1.2\_2021". For a list of valid value, see the Amazon CloudFront Developer Guide.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d327c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
