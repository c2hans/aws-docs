---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/connect-instance-logging-enabled.html
---

# connect-instance-logging-enabled
<a name="connect-instance-logging-enabled"></a>

Checks if Amazon Connect instances have flow logs enabled in an Amazon CloudWatch log group. The rule is NON\_COMPLIANT if an Amazon Connect instance does not have flow logs enabled.

**Identifier:** CONNECT\_INSTANCE\_LOGGING\_ENABLED

**Resource Types:** AWS::Connect::Instance

**Trigger type:** Configuration changes

**AWS Region:** Only available in Africa (Cape Town), Europe (Frankfurt), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d425c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
