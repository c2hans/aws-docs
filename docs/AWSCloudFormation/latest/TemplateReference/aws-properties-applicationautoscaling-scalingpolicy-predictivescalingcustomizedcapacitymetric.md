---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy PredictiveScalingCustomizedCapacityMetric
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric"></a>

 Represents a CloudWatch metric of your choosing for a predictive scaling policy.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-syntax.json"></a>

```
{
  "[MetricDataQueries](#cfn-applicationautoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-metricdataqueries)" : {{[ PredictiveScalingMetricDataQuery, ... ]}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-syntax.yaml"></a>

```
  [MetricDataQueries](#cfn-applicationautoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-metricdataqueries): {{
    - PredictiveScalingMetricDataQuery}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-properties"></a>

`MetricDataQueries`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric-metricdataqueries"></a>
 One or more metric data queries to provide data points for a metric specification.
*Required*: Yes
*Type*: Array of [PredictiveScalingMetricDataQuery](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
