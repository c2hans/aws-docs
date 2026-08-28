---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-no-deprecated-ssl-protocols.html
---

# cloudfront-no-deprecated-ssl-protocols
<a name="cloudfront-no-deprecated-ssl-protocols"></a>

Checks if CloudFront distributions are using deprecated SSL protocols for HTTPS communication between CloudFront edge locations and custom origins. This rule is NON\_COMPLIANT for a CloudFront distribution if any ‘OriginSslProtocols’ includes ‘SSLv3’.

**Identifier:** CLOUDFRONT\_NO\_DEPRECATED\_SSL\_PROTOCOLS

**Resource Types:** AWS::CloudFront::Distribution

**Trigger type:** Configuration changes

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d311c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
