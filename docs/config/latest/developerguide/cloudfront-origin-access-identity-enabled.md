---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-origin-access-identity-enabled.html
---

# cloudfront-origin-access-identity-enabled
<a name="cloudfront-origin-access-identity-enabled"></a>

Checks if CloudFront distribution with Amazon S3 Origin type has origin access identity configured. The rule is NON\_COMPLIANT if the CloudFront distribution is backed by S3 and any origin type is not OAI configured, or the origin is not an S3 bucket.

**Note**
The rule does not return `NOT_APPLICABLE` if the origin is not an S3 bucket.

**Identifier:** CLOUDFRONT\_ORIGIN\_ACCESS\_IDENTITY\_ENABLED

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d313c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
