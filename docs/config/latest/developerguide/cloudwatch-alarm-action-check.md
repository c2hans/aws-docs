---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-action-check.html
---

# cloudwatch-alarm-action-check
<a name="cloudwatch-alarm-action-check"></a>

Checks if CloudWatch alarms have an action configured for the ALARM, INSUFFICIENT\_DATA, or OK state. Optionally checks if any actions match a named ARN. The rule is NON\_COMPLIANT if there is no action specified for the alarm or optional parameter.

**Identifier:** CLOUDWATCH\_ALARM\_ACTION\_CHECK

**Resource Types:** AWS::CloudWatch::Alarm

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

okActionRequiredType: StringDefault: false
Alarms have at least one action when the alarm transitions to an OK state from any other state.

insufficientDataActionRequiredType: StringDefault: true
Alarms have at least one action when the alarm transitions to the INSUFFICIENT\_DATA state from any other state.

alarmActionRequiredType: StringDefault: true
Alarms have at least one action.

action1 (Optional)Type: String
The action to execute, specified as an ARN.

action2 (Optional)Type: String
The action to execute, specified as an ARN.

action3 (Optional)Type: String
The action to execute, specified as an ARN.

action4 (Optional)Type: String
The action to execute, specified as an ARN.

action5 (Optional)Type: String
The action to execute, specified as an ARN.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d347c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
