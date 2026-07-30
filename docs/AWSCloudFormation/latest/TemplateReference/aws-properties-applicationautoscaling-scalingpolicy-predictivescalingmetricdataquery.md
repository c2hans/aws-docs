---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy PredictiveScalingMetricDataQuery
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery"></a>

 The metric data to return. Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-syntax.json"></a>

```
{
  "[Expression](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-expression)" : {{String}},
  "[Id](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-id)" : {{String}},
  "[Label](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-label)" : {{String}},
  "[MetricStat](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-metricstat)" : {{PredictiveScalingMetricStat}},
  "[ReturnData](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-returndata)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-syntax.yaml"></a>

```
  [Expression](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-expression): {{String}}
  [Id](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-id): {{String}}
  [Label](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-label): {{String}}
  [MetricStat](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-metricstat): {{
    PredictiveScalingMetricStat}}
  [ReturnData](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-returndata): {{Boolean}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-properties"></a>

`Expression`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-expression"></a>
 The math expression to perform on the returned data, if this object is performing a math expression. This expression can use the `Id` of the other metrics to refer to those metrics, and can also use the `Id` of other expressions to use the result of those expressions.
Conditional: Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat`, but not both.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Id`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-id"></a>
 A short name that identifies the object's results in the response. This name must be unique among all `MetricDataQuery` objects specified for a single scaling policy. If you are performing math expressions on this set of data, this name represents that data and can serve as a variable in the mathematical expression. The valid characters are letters, numbers, and underscores. The first character must be a lowercase letter.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-label"></a>
 A human-readable label for this metric or expression. This is especially useful if this is a math expression, so that you know what the value represents.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricStat`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-metricstat"></a>
 Information about the metric data to return.
Conditional: Within each `MetricDataQuery` object, you must specify either `Expression` or `MetricStat`, but not both.
*Required*: No
*Type*: [PredictiveScalingMetricStat](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricstat.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReturnData`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery-returndata"></a>
 Indicates whether to return the timestamps and raw data values of this metric.
If you use any math expressions, specify `true` for this value for only the final math expression that the metric specification is based on. You must specify `false` for `ReturnData` for all the other metrics and expressions used in the metric specification.
If you are only retrieving metrics and not performing any math expressions, do not specify anything for `ReturnData`. This sets it to its default (`true`).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
