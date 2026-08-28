---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/lambda-function-application-log-level-check.html
---

# lambda-function-application-log-level-check
<a name="lambda-function-application-log-level-check"></a>

Checks if AWS Lambda functions with JSON structured logs are configured with a specified application log level. The rule is NON\_COMPLIANT if configuration.loggingConfig.applicationLogLevel is not a value specified in the required rule parameter.

**Identifier:** LAMBDA\_FUNCTION\_APPLICATION\_LOG\_LEVEL\_CHECK

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

logLevelType: String
The minimum application log level for the rule to check. The rule is NON\_COMPLIANT if configuration.loggingConfig.applicationLogLevel is configured with a value not specified in this parameter. Valid values include: 'TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', and 'FATAL'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1061c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
