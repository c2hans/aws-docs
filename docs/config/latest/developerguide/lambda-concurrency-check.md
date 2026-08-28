---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/lambda-concurrency-check.html
---

# lambda-concurrency-check
<a name="lambda-concurrency-check"></a>

Checks if the Lambda function is configured with a function-level concurrent execution limit. The rule is NON\_COMPLIANT if the Lambda function is not configured with a function-level concurrent execution limit.

**Identifier:** LAMBDA\_CONCURRENCY\_CHECK

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Ningxia) Region

**Parameters:**

ConcurrencyLimitHigh (Optional)Type: String
Maximum concurrency execution limit

ConcurrencyLimitLow (Optional)Type: String
Minimum concurrency execution limit

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1057c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
