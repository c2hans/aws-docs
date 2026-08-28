---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingMetricDataQuery
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery"></a>

The metric data to return. Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.

You can call for a single metric or perform math expressions on multiple metrics. Any expressions used in a metric specification must eventually return a single time series.

For more information and examples, see [Create a target tracking scaling policy for Application Auto Scaling using metric math](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-target-tracking-metric-math.html) in the *Application Auto Scaling User Guide*.

`TargetTrackingMetricDataQuery` is a property of the [AWS::ApplicationAutoScaling::ScalingPolicy CustomizedMetricSpecification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-customizedmetricspecification.html) property type.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-syntax.json"></a>

```
{
  "[Expression](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-expression)" : {{String}},
  "[Id](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-id)" : {{String}},
  "[Label](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-label)" : {{String}},
  "[MetricStat](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-metricstat)" : {{TargetTrackingMetricStat}},
  "[ReturnData](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-returndata)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-syntax.yaml"></a>

```
  [Expression](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-expression): {{String}}
  [Id](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-id): {{String}}
  [Label](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-label): {{String}}
  [MetricStat](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-metricstat): {{
    TargetTrackingMetricStat}}
  [ReturnData](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-returndata): {{Boolean}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-properties"></a>

`Expression`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-expression"></a>
The math expression to perform on the returned data, if this object is performing a math expression. This expression can use the `Id` of the other metrics to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions.
Conditional: Within each `TargetTrackingMetricDataQuery` object, you must specify either `Expression` or `MetricStat`, but not both.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-id"></a>
A short name that identifies the object's results in the response. This name must be unique among all `MetricDataQuery` objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-label"></a>
A human-readable label for this metric or expression. This is especially useful if this is a math expression, so that you know what the value represents.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricStat`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-metricstat"></a>
Information about the metric data to return.
Conditional: Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat`, but not both.
*Required*: No
*Type*: [TargetTrackingMetricStat](aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReturnData`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery-returndata"></a>
Indicates whether to return the timestamps and raw data values of this metric.
If you use any math expressions, specify `true` for this value for only the final math expression that the metric specification is based on. You must specify `false` for `ReturnData` for all the other metrics and expressions used in the metric specification.
If you are only retrieving metrics and not performing any math expressions, do not specify anything for `ReturnData`. This sets it to its default (`true`).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
