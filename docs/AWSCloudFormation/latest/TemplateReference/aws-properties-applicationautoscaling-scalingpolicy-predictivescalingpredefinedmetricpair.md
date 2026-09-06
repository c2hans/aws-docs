---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy PredictiveScalingPredefinedMetricPair
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair"></a>

 Represents a metric pair for a predictive scaling policy.

The following predefined metrics are available for predictive scaling:
+  `ECSServiceAverageCPUUtilization`
+  `ECSServiceAverageMemoryUtilization`
+  `ECSServiceCPUUtilization`
+  `ECSServiceMemoryUtilization`
+  `ECSServiceTotalCPUUtilization`
+  `ECSServiceTotalMemoryUtilization`
+  `ALBRequestCount`
+  `ALBRequestCountPerTarget`
+  `TotalALBRequestCount`

## Syntax
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-syntax.json"></a>

```
{
  "[PredefinedMetricType](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-predefinedmetrictype)" : {{String}},
  "[ResourceLabel](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-resourcelabel)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-syntax.yaml"></a>

```
  [PredefinedMetricType](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-predefinedmetrictype): {{String}}
  [ResourceLabel](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-resourcelabel): {{String}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-properties"></a>

`PredefinedMetricType`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-predefinedmetrictype"></a>
 Indicates which metrics to use. There are two different types of metrics for each metric type: one is a load metric and one is a scaling metric.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceLabel`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedmetricpair-resourcelabel"></a>
 A label that uniquely identifies a specific target group from which to determine the total and average request count.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1023`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
