---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-distribution-key-group-enabled.html
---

# cloudfront-distribution-key-group-enabled
<a name="cloudfront-distribution-key-group-enabled"></a>

Checks whether Amazon CloudFront distributions use only trusted key groups for signed URL or signed cookie authentication for all cache behaviors. The rule is NON\_COMPLIANT if cache behaviors use trusted signers or no authentication is configured.

**Identifier:** CLOUDFRONT\_DISTRIBUTION\_KEY\_GROUP\_ENABLED

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d309c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
