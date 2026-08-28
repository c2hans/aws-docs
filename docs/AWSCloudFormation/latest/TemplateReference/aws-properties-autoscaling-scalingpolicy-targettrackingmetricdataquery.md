---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-targettrackingmetricdataquery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::ScalingPolicy TargetTrackingMetricDataQuery
<a name="aws-properties-autoscaling-scalingpolicy-targettrackingmetricdataquery"></a>

The metric data to return. Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.

You can use `TargetTrackingMetricDataQuery` structures with a [PutScalingPolicy](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_PutScalingPolicy.html) operation when you specify a [TargetTrackingConfiguration](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_TargetTrackingConfiguration.html) in the request.

You can call for a single metric or perform math expressions on multiple metrics. Any expressions used in a metric specification must eventually return a single time series.

For more information, see the [Create a target tracking scaling policy for Amazon EC2 Auto Scaling using metric math](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-target-tracking-metric-math.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Syntax
<a name="aws-properties-autoscaling-scalingpolicy-targettrackingmetricdataquery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-scalingpolicy-targettrackingmetricdataquery-syntax.json"></a>

```
{
  "[Expression](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-expression)" : {{String}},
  "[Id](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-id)" : {{String}},
  "[Label](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-label)" : {{String}},
  "[MetricStat](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-metricstat)" : {{TargetTrackingMetricStat}},
  "[Period](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-period)" : {{Integer}},
  "[ReturnData](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-returndata)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-autoscaling-scalingpolicy-targettrackingmetricdataquery-syntax.yaml"></a>

```
  [Expression](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-expression): {{String}}
  [Id](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-id): {{String}}
  [Label](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-label): {{String}}
  [MetricStat](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-metricstat): {{
    TargetTrackingMetricStat}}
  [Period](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-period): {{Integer}}
  [ReturnData](#cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-returndata): {{Boolean}}
```

## Properties
<a name="aws-properties-autoscaling-scalingpolicy-targettrackingmetricdataquery-properties"></a>

`Expression`  <a name="cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-expression"></a>
The math expression to perform on the returned data, if this object is performing a math expression. This expression can use the `Id` of the other metrics to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions.
Conditional: Within each `TargetTrackingMetricDataQuery` object, you must specify either `Expression` or `MetricStat`, but not both.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `2047`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-id"></a>
A short name that identifies the object's results in the response. This name must be unique among all `TargetTrackingMetricDataQuery` objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter.
*Required*: Yes
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-label"></a>
A human-readable label for this metric or expression. This is especially useful if this is a math expression, so that you know what the value represents.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Maximum*: `2047`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricStat`  <a name="cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-metricstat"></a>
Information about the metric data to return.
Conditional: Within each `TargetTrackingMetricDataQuery` object, you must specify either `Expression` or `MetricStat`, but not both.
*Required*: No
*Type*: [TargetTrackingMetricStat](aws-properties-autoscaling-scalingpolicy-targettrackingmetricstat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Period`  <a name="cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-period"></a>
 The period of the metric in seconds. The default value is 60. Accepted values are 10, 30, and 60. For high resolution metric, set the value to less than 60. For more information, see [Create a target tracking policy using high-resolution metrics for faster response](https://docs.aws.amazon.com/autoscaling/ec2/userguide/policy-creating-high-resolution-metrics.html).
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReturnData`  <a name="cfn-autoscaling-scalingpolicy-targettrackingmetricdataquery-returndata"></a>
Indicates whether to return the timestamps and raw data values of this metric.
If you use any math expressions, specify `true` for this value for only the final math expression that the metric specification is based on. You must specify `false` for `ReturnData` for all the other metrics and expressions used in the metric specification.
If you are only retrieving metrics and not performing any math expressions, do not specify anything for `ReturnData`. This sets it to its default (`true`).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
