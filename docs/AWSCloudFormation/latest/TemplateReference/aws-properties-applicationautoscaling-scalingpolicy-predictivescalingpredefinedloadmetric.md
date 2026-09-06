---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationAutoScaling::ScalingPolicy PredictiveScalingPredefinedLoadMetric
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric"></a>

 Describes a load metric for a predictive scaling policy.

When returned in the output of `DescribePolicies`, it indicates that a predictive scaling policy uses individually specified load and scaling metrics instead of a metric pair.

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
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-syntax.json"></a>

```
{
  "[PredefinedMetricType](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-predefinedmetrictype)" : {{String}},
  "[ResourceLabel](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-resourcelabel)" : {{String}}
}
```

### YAML
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-syntax.yaml"></a>

```
  [PredefinedMetricType](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-predefinedmetrictype): {{String}}
  [ResourceLabel](#cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-resourcelabel): {{String}}
```

## Properties
<a name="aws-properties-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-properties"></a>

`PredefinedMetricType`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-predefinedmetrictype"></a>
 The metric type.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceLabel`  <a name="cfn-applicationautoscaling-scalingpolicy-predictivescalingpredefinedloadmetric-resourcelabel"></a>
 A label that uniquely identifies a target group.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1023`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
