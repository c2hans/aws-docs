---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingMetricStat
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat"></a>

This structure defines the CloudWatch metric to return, along with the statistic and unit.

`TargetTrackingMetricStat` is a property of the [AWS::ApplicationAutoScaling::ScalingPolicy TargetTrackingMetricDataQuery](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricdataquery.html) property type.

For more information about the CloudWatch terminology below, see [Amazon CloudWatch concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html) in the *Amazon CloudWatch User Guide*.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat-syntax.json"></a>

```
{
  "[Metric](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-metric)" : {{TargetTrackingMetric}},
  "[Stat](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-stat)" : {{String}},
  "[Unit](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat-syntax.yaml"></a>

```
  [Metric](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-metric): {{
    TargetTrackingMetric}}
  [Stat](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-stat): {{String}}
  [Unit](#cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-unit): {{String}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetricstat-properties"></a>

`Metric`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-metric"></a>
The CloudWatch metric to return, including the metric name, namespace, and dimensions. To get the exact metric name, namespace, and dimensions, inspect the [Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html) object that is returned by a call to [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html).
*Required*: No
*Type*: [TargetTrackingMetric](aws-properties-applicationautoscaling-scalingpolicy-targettrackingmetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Stat`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-stat"></a>
The statistic to return. It can include any CloudWatch statistic or extended statistic. For a list of valid values, see the table in [Statistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Statistic) in the *Amazon CloudWatch User Guide*.
The most commonly used metric for scaling is `Average`.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-applicationautoscaling-scalingpolicy-targettrackingmetricstat-unit"></a>
The unit to use for the returned data points. For a complete list of the units that CloudWatch supports, see the [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html) data type in the *Amazon CloudWatch API Reference*.
*Required*: No
*Type*: String
*Pattern*: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
*Minimum*: `1`
*Maximum*: `1023`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
