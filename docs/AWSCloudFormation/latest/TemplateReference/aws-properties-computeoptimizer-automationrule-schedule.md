---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-computeoptimizer-automationrule-schedule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ComputeOptimizer::AutomationRule Schedule
<a name="aws-properties-computeoptimizer-automationrule-schedule"></a>

Configuration for scheduling when automation rules should execute, including timing and execution windows.

## Syntax
<a name="aws-properties-computeoptimizer-automationrule-schedule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-computeoptimizer-automationrule-schedule-syntax.json"></a>

```
{
  "[ExecutionWindowInMinutes](#cfn-computeoptimizer-automationrule-schedule-executionwindowinminutes)" : {{Integer}},
  "[ScheduleExpression](#cfn-computeoptimizer-automationrule-schedule-scheduleexpression)" : {{String}},
  "[ScheduleExpressionTimezone](#cfn-computeoptimizer-automationrule-schedule-scheduleexpressiontimezone)" : {{String}}
}
```

### YAML
<a name="aws-properties-computeoptimizer-automationrule-schedule-syntax.yaml"></a>

```
  [ExecutionWindowInMinutes](#cfn-computeoptimizer-automationrule-schedule-executionwindowinminutes): {{Integer}}
  [ScheduleExpression](#cfn-computeoptimizer-automationrule-schedule-scheduleexpression): {{String}}
  [ScheduleExpressionTimezone](#cfn-computeoptimizer-automationrule-schedule-scheduleexpressiontimezone): {{String}}
```

## Properties
<a name="aws-properties-computeoptimizer-automationrule-schedule-properties"></a>

`ExecutionWindowInMinutes`  <a name="cfn-computeoptimizer-automationrule-schedule-executionwindowinminutes"></a>
The time window in minutes during which the automation rule can start implementing recommended actions.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `1440`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleExpression`  <a name="cfn-computeoptimizer-automationrule-schedule-scheduleexpression"></a>
The expression that defines when the schedule runs. `cron` expression is supported. A `cron` expression consists of six fields separated by white spaces: (`minutes``hours``day_of_month``month``day_of_week``year`)
You can schedule rules to run at most once per day. Your cron expression must use specific values (not wildcards) for the minutes and hours fields. For example: (`30 12 * * *`) runs daily at 12:30 PM UTC.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleExpressionTimezone`  <a name="cfn-computeoptimizer-automationrule-schedule-scheduleexpressiontimezone"></a>
The timezone to use when interpreting the schedule expression.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
