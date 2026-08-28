---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AutoScaling::ScalingPolicy PredictiveScalingCustomizedCapacityMetric
<a name="aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric"></a>

Contains capacity metric information for the `CustomizedCapacityMetricSpecification` property of the [AWS::AutoScaling::ScalingPolicy PredictiveScalingMetricSpecification](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-autoscaling-scalingpolicy-predictivescalingmetricspecification.html) property type.

## Syntax
<a name="aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-syntax.json"></a>

```
{
  "[MetricDataQueries](#cfn-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-metricdataqueries)" : {{[ MetricDataQuery, ... ]}}
}
```

### YAML
<a name="aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-syntax.yaml"></a>

```
  [MetricDataQueries](#cfn-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-metricdataqueries): {{
    - MetricDataQuery}}
```

## Properties
<a name="aws-properties-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-properties"></a>

`MetricDataQueries`  <a name="cfn-autoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-metricdataqueries"></a>
One or more metric data queries to provide the data points for a capacity metric. Use multiple metric data queries only if you are performing a math expression on returned data.
*Required*: Yes
*Type*: Array of [MetricDataQuery](aws-properties-autoscaling-scalingpolicy-metricdataquery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
