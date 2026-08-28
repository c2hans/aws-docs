---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-description.html
---

# cloudwatch-alarm-description
<a name="cloudwatch-alarm-description"></a>

Checks if AWS CloudWatch Alarm resources contain an alarm description. The rule is NON\_COMPLIANT if the CloudWatch Alarm resource does not contain an AlarmDescription field or the AlarmDescription is empty.

**Identifier:** CLOUDWATCH\_ALARM\_DESCRIPTION

**Resource Types:** AWS::CloudWatch::Alarm

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d351c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
