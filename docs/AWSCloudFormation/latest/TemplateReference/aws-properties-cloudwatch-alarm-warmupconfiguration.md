---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alarm-warmupconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alarm WarmUpConfiguration
<a name="aws-properties-cloudwatch-alarm-warmupconfiguration"></a>

The configuration settings that define the warm-up behavior for an alarm. Use these settings to delay alarm evaluation after you create or update the alarm, which reduces alarm noise while a new resource or service starts publishing data.

During the warm-up period, the alarm stays in `INSUFFICIENT_DATA` and does not perform alarm actions.

## Syntax
<a name="aws-properties-cloudwatch-alarm-warmupconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alarm-warmupconfiguration-syntax.json"></a>

```
{
  "[OnlyStartEvaluatingAfterWarmUpPeriodEnds](#cfn-cloudwatch-alarm-warmupconfiguration-onlystartevaluatingafterwarmupperiodends)" : {{Boolean}},
  "[WarmUpPeriodDurationInMinutes](#cfn-cloudwatch-alarm-warmupconfiguration-warmupperioddurationinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alarm-warmupconfiguration-syntax.yaml"></a>

```
  [OnlyStartEvaluatingAfterWarmUpPeriodEnds](#cfn-cloudwatch-alarm-warmupconfiguration-onlystartevaluatingafterwarmupperiodends): {{Boolean}}
  [WarmUpPeriodDurationInMinutes](#cfn-cloudwatch-alarm-warmupconfiguration-warmupperioddurationinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-cloudwatch-alarm-warmupconfiguration-properties"></a>

`OnlyStartEvaluatingAfterWarmUpPeriodEnds`  <a name="cfn-cloudwatch-alarm-warmupconfiguration-onlystartevaluatingafterwarmupperiodends"></a>
Specifies whether the alarm waits for the full warm-up period before it starts to evaluate. The default is `false`. If `true`, the alarm waits the entire `WarmUpPeriodDurationInMinutes` before it starts to evaluate, even if metric data arrives earlier. If `false`, the alarm ends the warm-up period early. Evaluation begins as soon as the alarm has enough metric data to fill its evaluation window.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WarmUpPeriodDurationInMinutes`  <a name="cfn-cloudwatch-alarm-warmupconfiguration-warmupperioddurationinminutes"></a>
The length of the warm-up period, in minutes. After you create or update the alarm, the alarm stays in `INSUFFICIENT_DATA` for this duration. During this time, the alarm does not perform alarm actions.
You can change this value at any time, including after the warm-up period ends. If you change it after the warm-up period ends, the new value does not restart the warm-up period.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `2880`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
