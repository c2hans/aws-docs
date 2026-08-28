---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alarmmuterule-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::AlarmMuteRule Rule
<a name="aws-properties-cloudwatch-alarmmuterule-rule"></a>

The configuration that defines when and how long alarms should be muted.

## Syntax
<a name="aws-properties-cloudwatch-alarmmuterule-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alarmmuterule-rule-syntax.json"></a>

```
{
  "[Schedule](#cfn-cloudwatch-alarmmuterule-rule-schedule)" : {{Schedule}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alarmmuterule-rule-syntax.yaml"></a>

```
  [Schedule](#cfn-cloudwatch-alarmmuterule-rule-schedule): {{
    Schedule}}
```

## Properties
<a name="aws-properties-cloudwatch-alarmmuterule-rule-properties"></a>

`Schedule`  <a name="cfn-cloudwatch-alarmmuterule-rule-schedule"></a>
Defines the schedule configuration for an alarm mute rule.
The rule contains a schedule that specifies when and how long alarms should be muted. The schedule can be a recurring pattern using cron expressions or a one-time mute window using at expressions.
*Required*: Yes
*Type*: [Schedule](aws-properties-cloudwatch-alarmmuterule-schedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
