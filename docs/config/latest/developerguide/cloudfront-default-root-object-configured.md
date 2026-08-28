---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-default-root-object-configured.html
---

# cloudfront-default-root-object-configured
<a name="cloudfront-default-root-object-configured"></a>

Checks if an Amazon CloudFront distribution is configured to return a specific object that is the default root object. The rule is NON\_COMPLIANT if Amazon CloudFront distribution does not have a default root object configured.

**Identifier:** CLOUDFRONT\_DEFAULT\_ROOT\_OBJECT\_CONFIGURED

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d307c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
