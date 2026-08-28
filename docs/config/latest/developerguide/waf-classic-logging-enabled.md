---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/waf-classic-logging-enabled.html
---

# waf-classic-logging-enabled
<a name="waf-classic-logging-enabled"></a>

Checks if logging is enabled on AWS WAF classic global web access control lists (web ACLs). The rule is NON\_COMPLIANT for a global web ACL, if it does not have logging enabled.

**Identifier:** WAF\_CLASSIC\_LOGGING\_ENABLED

**Resource Types:** AWS::WAF::WebACL

**Trigger type:** Periodic

**AWS Region:** Only available in US East (N. Virginia) Region

**Parameters:**

KinesisFirehoseDeliveryStreamArns (Optional)Type: CSV
Comma separated list of Amazon Kinesis stream ARN for AWS WAF logs.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1623c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
