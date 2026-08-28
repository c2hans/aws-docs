---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/lambda-function-log-format-json.html
---

# lambda-function-log-format-json
<a name="lambda-function-log-format-json"></a>

Checks if AWS Lambda functions have the log format set to JSON for more control and better readability. The rule is NON\_COMPLIANT if configuration.loggingConfig.logFormat is not 'JSON'.

**Identifier:** LAMBDA\_FUNCTION\_LOG\_FORMAT\_JSON

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1065c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
