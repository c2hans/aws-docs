---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/step-functions-state-machine-logging-enabled.html
---

# step-functions-state-machine-logging-enabled
<a name="step-functions-state-machine-logging-enabled"></a>

Checks if AWS Step Functions machine has logging enabled. The rule is NON\_COMPLIANT if a state machine does not have logging enabled or the logging configuration is not at the minimum level provided.

**Identifier:** STEP\_FUNCTIONS\_STATE\_MACHINE\_LOGGING\_ENABLED

**Resource Types:** AWS::StepFunctions::StateMachine

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

cloudWatchLogGroupArns (Optional)Type: CSV
Comma-separated list of Amazon Resource Names (ARNs) for Amazon CloudWatch Logs log groups. The rule checks if the specified log groups are configured for your state machine logs.

logLevel (Optional)Type: String
The minimum log level for your state machine. Valid values include: ALL, ERROR, FATAL.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1557c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
