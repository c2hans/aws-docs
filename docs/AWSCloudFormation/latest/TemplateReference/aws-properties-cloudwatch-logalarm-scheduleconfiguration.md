---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-logalarm-scheduleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::LogAlarm ScheduleConfiguration
<a name="aws-properties-cloudwatch-logalarm-scheduleconfiguration"></a>

The schedule and time-range offset configuration for the underlying scheduled query.

## Syntax
<a name="aws-properties-cloudwatch-logalarm-scheduleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-logalarm-scheduleconfiguration-syntax.json"></a>

```
{
  "[EndTimeOffset](#cfn-cloudwatch-logalarm-scheduleconfiguration-endtimeoffset)" : {{Integer}},
  "[ScheduleExpression](#cfn-cloudwatch-logalarm-scheduleconfiguration-scheduleexpression)" : {{String}},
  "[StartTimeOffset](#cfn-cloudwatch-logalarm-scheduleconfiguration-starttimeoffset)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudwatch-logalarm-scheduleconfiguration-syntax.yaml"></a>

```
  [EndTimeOffset](#cfn-cloudwatch-logalarm-scheduleconfiguration-endtimeoffset): {{Integer}}
  [ScheduleExpression](#cfn-cloudwatch-logalarm-scheduleconfiguration-scheduleexpression): {{String}}
  [StartTimeOffset](#cfn-cloudwatch-logalarm-scheduleconfiguration-starttimeoffset): {{Integer}}
```

## Properties
<a name="aws-properties-cloudwatch-logalarm-scheduleconfiguration-properties"></a>

`EndTimeOffset`  <a name="cfn-cloudwatch-logalarm-scheduleconfiguration-endtimeoffset"></a>
The offset, in seconds, before the scheduled execution time at which the query time range ends. Must be non-negative and less than `StartTimeOffset`. The default is 0.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2592000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduleExpression`  <a name="cfn-cloudwatch-logalarm-scheduleconfiguration-scheduleexpression"></a>
The schedule expression that defines how often the underlying CloudWatch Logs scheduled query runs. Specify a `rate()` expression, for example `rate(5 minutes)`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartTimeOffset`  <a name="cfn-cloudwatch-logalarm-scheduleconfiguration-starttimeoffset"></a>
The offset, in seconds, before the scheduled execution time at which the query time range begins. For example, an offset of 360 (6 minutes) on a query running at 12:05:00 starts the query time range at 11:59:00.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2592000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
