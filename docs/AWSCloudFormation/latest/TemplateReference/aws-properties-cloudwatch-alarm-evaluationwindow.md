---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alarm-evaluationwindow.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alarm EvaluationWindow
<a name="aws-properties-cloudwatch-alarm-evaluationwindow"></a>

The evaluation window that an alarm uses to select the range of metric data that it evaluates each time it runs. This is a union type. Set exactly one of its members, `SlidingWindow` or `WallClockWindow`. If you don't set `EvaluationWindow`, the alarm uses a `SlidingWindow` by default.

For more information, see [Alarm evaluation windows](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-evaluation-window.html) in the *CloudWatch User Guide*.

## Syntax
<a name="aws-properties-cloudwatch-alarm-evaluationwindow-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alarm-evaluationwindow-syntax.json"></a>

```
{
  "[SlidingWindow](#cfn-cloudwatch-alarm-evaluationwindow-slidingwindow)" : {{Json}},
  "[WallClockWindow](#cfn-cloudwatch-alarm-evaluationwindow-wallclockwindow)" : {{WallClockWindow}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alarm-evaluationwindow-syntax.yaml"></a>

```
  [SlidingWindow](#cfn-cloudwatch-alarm-evaluationwindow-slidingwindow): {{Json}}
  [WallClockWindow](#cfn-cloudwatch-alarm-evaluationwindow-wallclockwindow): {{
    WallClockWindow}}
```

## Properties
<a name="aws-properties-cloudwatch-alarm-evaluationwindow-properties"></a>

`SlidingWindow`  <a name="cfn-cloudwatch-alarm-evaluationwindow-slidingwindow"></a>
A sliding window, which advances each time the alarm is evaluated, forming a rolling time window. This is the default evaluation window.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WallClockWindow`  <a name="cfn-cloudwatch-alarm-evaluationwindow-wallclockwindow"></a>
A wall clock window, which aligns the evaluated range to fixed clock boundaries that match the alarm's period, such as the top of the hour, midnight, or the start of the calendar week.
*Required*: No
*Type*: [WallClockWindow](aws-properties-cloudwatch-alarm-wallclockwindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
