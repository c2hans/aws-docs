---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-notification-check.html
---

# cloudformation-stack-notification-check
<a name="cloudformation-stack-notification-check"></a>

Checks if your CloudFormation stacks send event notifications to an Amazon SNS topic. Optionally checks if specified Amazon SNS topics are used. The rule is NON\_COMPLIANT if CloudFormation stacks do not send notifications.

**Identifier:** CLOUDFORMATION\_STACK\_NOTIFICATION\_CHECK

**Resource Types:** AWS::CloudFormation::Stack

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Melbourne), Israel (Tel Aviv), Europe (Spain) Region

**Parameters:**

snsTopic2 (Optional)Type: String
SNS topic ARN.

snsTopic1 (Optional)Type: String
SNS topic ARN.

snsTopic5 (Optional)Type: String
SNS topic ARN.

snsTopic4 (Optional)Type: String
SNS topic ARN.

snsTopic3 (Optional)Type: String
SNS topic ARN.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d295c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
