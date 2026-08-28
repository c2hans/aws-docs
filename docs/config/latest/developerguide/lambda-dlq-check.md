---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/lambda-dlq-check.html
---

# lambda-dlq-check
<a name="lambda-dlq-check"></a>

Checks whether an AWS Lambda function is configured with a dead-letter queue. The rule is NON\_COMPLIANT if the Lambda function is not configured with a dead-letter queue.

**Identifier:** LAMBDA\_DLQ\_CHECK

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Ningxia) Region

**Parameters:**

dlqArns (Optional)Type: CSV
Comma-separated list of Amazon SQS and Amazon SNS ARNs that must be configured as the Lambda function dead-letter queue target

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1059c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
