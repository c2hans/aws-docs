---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy PredictiveScalingMetricSpecification
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification"></a>

 This structure specifies the metrics and target utilization settings for a predictive scaling policy.

You must specify either a metric pair, or a load metric and a scaling metric individually. Specifying a metric pair instead of individual metrics provides a simpler way to configure metrics for a scaling policy. You choose the metric pair, and the policy automatically knows the correct sum and average statistics to use for the load metric and the scaling metric.

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-syntax.json"></a>

```
{
  "[CustomizedCapacityMetricSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-customizedcapacitymetricspecification)" : {{PredictiveScalingCustomizedCapacityMetric}},
  "[CustomizedLoadMetricSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-customizedloadmetricspecification)" : {{PredictiveScalingCustomizedLoadMetric}},
  "[CustomizedScalingMetricSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-customizedscalingmetricspecification)" : {{PredictiveScalingCustomizedScalingMetric}},
  "[PredefinedLoadMetricSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedloadmetricspecification)" : {{PredictiveScalingPredefinedLoadMetric}},
  "[PredefinedMetricPairSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedmetricpairspecification)" : {{PredictiveScalingPredefinedMetricPair}},
  "[PredefinedScalingMetricSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedscalingmetricspecification)" : {{PredictiveScalingPredefinedScalingMetric}},
  "[TargetValue](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-targetvalue)" : {{Number}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-syntax.yaml"></a>

```
  [CustomizedCapacityMetricSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-customizedcapacitymetricspecification): {{
    PredictiveScalingCustomizedCapacityMetric}}
  [CustomizedLoadMetricSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-customizedloadmetricspecification): {{
    PredictiveScalingCustomizedLoadMetric}}
  [CustomizedScalingMetricSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-customizedscalingmetricspecification): {{
    PredictiveScalingCustomizedScalingMetric}}
  [PredefinedLoadMetricSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedloadmetricspecification): {{
    PredictiveScalingPredefinedLoadMetric}}
  [PredefinedMetricPairSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedmetricpairspecification): {{
    PredictiveScalingPredefinedMetricPair}}
  [PredefinedScalingMetricSpecification](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedscalingmetricspecification): {{
    PredictiveScalingPredefinedScalingMetric}}
  [TargetValue](#cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-targetvalue): {{Number}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-properties"></a>

`CustomizedCapacityMetricSpecification`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-customizedcapacitymetricspecification"></a>
 The customized capacity metric specification.
*Required*: No
*Type*: [PredictiveScalingCustomizedCapacityMetric](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedcapacitymetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomizedLoadMetricSpecification`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-customizedloadmetricspecification"></a>
 The customized load metric specification.
*Required*: No
*Type*: [PredictiveScalingCustomizedLoadMetric](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedloadmetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomizedScalingMetricSpecification`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-customizedscalingmetricspecification"></a>
 The customized scaling metric specification.
*Required*: No
*Type*: [PredictiveScalingCustomizedScalingMetric](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingcustomizedscalingmetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PredefinedLoadMetricSpecification`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedloadmetricspecification"></a>
 The predefined load metric specification.
*Required*: No
*Type*: [PredictiveScalingPredefinedLoadMetric](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PredefinedMetricPairSpecification`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedmetricpairspecification"></a>
 The predefined metric pair specification that determines the appropriate scaling metric and load metric to use.
*Required*: No
*Type*: [PredictiveScalingPredefinedMetricPair](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PredefinedScalingMetricSpecification`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-predefinedscalingmetricspecification"></a>
 The predefined scaling metric specification.
*Required*: No
*Type*: [PredictiveScalingPredefinedScalingMetric](aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedscalingmetric.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TargetValue`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingmetricspecification-targetvalue"></a>
 Specifies the target utilization.
*Required*: Yes
*Type*: Number
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
