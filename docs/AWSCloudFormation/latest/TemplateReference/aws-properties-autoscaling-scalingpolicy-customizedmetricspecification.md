---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-customizedmetricspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::ScalingPolicy CustomizedMetricSpecification
<a name="aws-properties-autoscaling-scalingpolicy-customizedmetricspecification"></a>

Contains customized metric specification information for a target tracking scaling policy for Amazon EC2 Auto Scaling.

To create your customized metric specification:
+ Add values for each required property from CloudWatch. You can use an existing metric, or a new metric that you create. To use your own metric, you must first publish the metric to CloudWatch. For more information, see [Publish Custom Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) in the *Amazon CloudWatch User Guide*.
+ Choose a metric that changes proportionally with capacity. The value of the metric should increase or decrease in inverse proportion to the number of capacity units. That is, the value of the metric should decrease when capacity increases.

For more information about CloudWatch, see [Amazon CloudWatch Concepts](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html).

`CustomizedMetricSpecification` is a property of the [AWS::AutoScaling::ScalingPolicy TargetTrackingConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-targettrackingconfiguration.html) property type.

## Syntax
<a name="aws-properties-autoscaling-scalingpolicy-customizedmetricspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-scalingpolicy-customizedmetricspecification-syntax.json"></a>

```
{
  "[Dimensions](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-dimensions)" : {{[ MetricDimension, ... ]}},
  "[MetricName](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-metricname)" : {{String}},
  "[Metrics](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-metrics)" : {{[ TargetTrackingMetricDataQuery, ... ]}},
  "[Namespace](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-namespace)" : {{String}},
  "[Period](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-period)" : {{Integer}},
  "[Statistic](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-statistic)" : {{String}},
  "[Unit](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-unit)" : {{String}}
}
```

### YAML
<a name="aws-properties-autoscaling-scalingpolicy-customizedmetricspecification-syntax.yaml"></a>

```
  [Dimensions](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-dimensions): {{
    - MetricDimension}}
  [MetricName](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-metricname): {{String}}
  [Metrics](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-metrics): {{
    - TargetTrackingMetricDataQuery}}
  [Namespace](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-namespace): {{String}}
  [Period](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-period): {{Integer}}
  [Statistic](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-statistic): {{String}}
  [Unit](#cfn-autoscaling-scalingpolicy-customizedmetricspecification-unit): {{String}}
```

## Properties
<a name="aws-properties-autoscaling-scalingpolicy-customizedmetricspecification-properties"></a>

`Dimensions`  <a name="cfn-autoscaling-scalingpolicy-customizedmetricspecification-dimensions"></a>
The dimensions of the metric.
Conditional: If you published your metric with dimensions, you must specify the same dimensions in your scaling policy.
*Required*: No
*Type*: Array of [MetricDimension](aws-properties-autoscaling-scalingpolicy-metricdimension.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetricName`  <a name="cfn-autoscaling-scalingpolicy-customizedmetricspecification-metricname"></a>
The name of the metric. To get the exact metric name, namespace, and dimensions, inspect the [Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html) object that is returned by a call to [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metrics`  <a name="cfn-autoscaling-scalingpolicy-customizedmetricspecification-metrics"></a>
The metrics to include in the target tracking scaling policy, as a metric data query. This can include both raw metric and metric math expressions.
*Required*: No
*Type*: Array of [TargetTrackingMetricDataQuery](aws-properties-autoscaling-scalingpolicy-targettrackingmetricdataquery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Namespace`  <a name="cfn-autoscaling-scalingpolicy-customizedmetricspecification-namespace"></a>
The namespace of the metric.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Period`  <a name="cfn-autoscaling-scalingpolicy-customizedmetricspecification-period"></a>
 The period of the metric in seconds. The default value is 60. Accepted values are 10, 30, and 60. For high resolution metric, set the value to less than 60. For more information, see [Create a target tracking policy using high-resolution metrics for faster response](https://docs.aws.amazon.com/autoscaling/ec2/userguide/policy-creating-high-resolution-metrics.html).
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Statistic`  <a name="cfn-autoscaling-scalingpolicy-customizedmetricspecification-statistic"></a>
The statistic of the metric.
*Required*: No
*Type*: String
*Allowed values*: `Average | Minimum | Maximum | SampleCount | Sum`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Unit`  <a name="cfn-autoscaling-scalingpolicy-customizedmetricspecification-unit"></a>
The unit of the metric. For a complete list of the units that CloudWatch supports, see the [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html) data type in the *Amazon CloudWatch API Reference*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
