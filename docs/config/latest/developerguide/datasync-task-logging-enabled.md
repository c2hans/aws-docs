---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/datasync-task-logging-enabled.html
---

# datasync-task-logging-enabled
<a name="datasync-task-logging-enabled"></a>

Checks if an AWS DataSync task has Amazon CloudWatch logging enabled. The rule is NON\_COMPLIANT if an AWS DataSync task does not have Amazon CloudWatch logging enabled or if the logging level is not equivalent to the logging level that you specify.

**Identifier:** DATASYNC\_TASK\_LOGGING\_ENABLED

**Resource Types:** AWS::DataSync::Task

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

logLevel (Optional)Type: String
String value for the logging level. Valid values include: 'BASIC' and 'TRANSFER'. If not specified, the default value is 'BASIC'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d443c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
