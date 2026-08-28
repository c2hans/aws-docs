---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricstat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy PredictiveScalingMetricStat
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricstat"></a>

 This structure defines the CloudWatch metric to return, along with the statistic and unit.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-syntax.json"></a>

```
{
  "[Metric](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-metric)" : {{PredictiveScalingMetric}},
  "[Stat](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-stat)" : {{String}},
  "[Unit](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-syntax.yaml"></a>

```
  [Metric](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-metric): {{
    PredictiveScalingMetric}}
  [Stat](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-stat): {{String}}
  [Unit](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-unit): {{String}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-properties"></a>

`Metric`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-metric"></a>
 The CloudWatch metric to return, including the metric name, namespace, and dimensions. To get the exact metric name, namespace, and dimensions, inspect the [Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html) object that is returned by a call to [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html).
*Required*: No
*Type*: [PredictiveScalingMetric](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stat`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-stat"></a>
 The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in [Statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic) in the *Amazon CloudWatch User Guide*.
The most commonly used metrics for predictive scaling are `Average` and `Sum`.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricstat-unit"></a>
 The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html) data type in the *Amazon CloudWatch API Reference*.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `1023`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
