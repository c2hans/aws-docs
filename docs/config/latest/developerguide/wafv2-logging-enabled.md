---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/wafv2-logging-enabled.html
---

# wafv2-logging-enabled
<a name="wafv2-logging-enabled"></a>

Checks if logging is enabled on AWS WAFv2 regional and global web access control lists (web ACLs). The rule is NON\_COMPLIANT if the logging is enabled but the logging destination does not match the value of the parameter.

**Note**
**Amazon Security Lake Exception**
This rule does not check logging done with Security Lake for AWS WAFV2 web ACLs.

**Identifier:** WAFV2\_LOGGING\_ENABLED

**Resource Types:** AWS::WAFv2::WebACL

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

KinesisFirehoseDeliveryStreamArns (Optional)Type: CSV
Comma separated list of Kinesis Firehose delivery stream ARNs

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1615c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
