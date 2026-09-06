---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy PredictiveScalingCustomizedScalingMetric
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric"></a>

<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric-description"></a>The `PredictiveScalingCustomizedScalingMetric` property type specifies Property description not available. for an [AWS::ApplicationAutoScaling::ScalingPolicy](aws-resource-applicationautoscaling-scalingpolicy.md).

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric-syntax.json"></a>

```
{
  "[MetricDataQueries](#cfn-applicationautoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric-metricdataqueries)" : {{[ PredictiveScalingMetricDataQuery, ... ]}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric-syntax.yaml"></a>

```
  [MetricDataQueries](#cfn-applicationautoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric-metricdataqueries): {{
    - PredictiveScalingMetricDataQuery}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric-properties"></a>

`MetricDataQueries`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric-metricdataqueries"></a>
 One or more metric data queries to provide data points for a metric specification.
*Required*: Yes
*Type*: Array of [PredictiveScalingMetricDataQuery](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricdataquery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
