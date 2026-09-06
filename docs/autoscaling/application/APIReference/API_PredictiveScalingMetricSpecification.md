---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingMetricSpecification.html
---

# PredictiveScalingMetricSpecification
<a name="API_PredictiveScalingMetricSpecification"></a>

 This structure specifies the metrics and target utilization settings for a predictive scaling policy.

You must specify either a metric pair, or a load metric and a scaling metric individually. Specifying a metric pair instead of individual metrics provides a simpler way to configure metrics for a scaling policy. You choose the metric pair, and the policy automatically knows the correct sum and average statistics to use for the load metric and the scaling metric.

## Contents
<a name="API_PredictiveScalingMetricSpecification_Contents"></a>

 ** TargetValue **   <a name="autoscaling-Type-PredictiveScalingMetricSpecification-TargetValue"></a>
 Specifies the target utilization.
Type: Double
Required: Yes

 ** CustomizedCapacityMetricSpecification **   <a name="autoscaling-Type-PredictiveScalingMetricSpecification-CustomizedCapacityMetricSpecification"></a>
 The customized capacity metric specification.
Type: [PredictiveScalingCustomizedMetricSpecification](API_PredictiveScalingCustomizedMetricSpecification.md) object
Required: No

 ** CustomizedLoadMetricSpecification **   <a name="autoscaling-Type-PredictiveScalingMetricSpecification-CustomizedLoadMetricSpecification"></a>
 The customized load metric specification.
Type: [PredictiveScalingCustomizedMetricSpecification](API_PredictiveScalingCustomizedMetricSpecification.md) object
Required: No

 ** CustomizedScalingMetricSpecification **   <a name="autoscaling-Type-PredictiveScalingMetricSpecification-CustomizedScalingMetricSpecification"></a>
 The customized scaling metric specification.
Type: [PredictiveScalingCustomizedMetricSpecification](API_PredictiveScalingCustomizedMetricSpecification.md) object
Required: No

 ** PredefinedLoadMetricSpecification **   <a name="autoscaling-Type-PredictiveScalingMetricSpecification-PredefinedLoadMetricSpecification"></a>
 The predefined load metric specification.
Type: [PredictiveScalingPredefinedLoadMetricSpecification](API_PredictiveScalingPredefinedLoadMetricSpecification.md) object
Required: No

 ** PredefinedMetricPairSpecification **   <a name="autoscaling-Type-PredictiveScalingMetricSpecification-PredefinedMetricPairSpecification"></a>
 The predefined metric pair specification that determines the appropriate scaling metric and load metric to use.
Type: [PredictiveScalingPredefinedMetricPairSpecification](API_PredictiveScalingPredefinedMetricPairSpecification.md) object
Required: No

 ** PredefinedScalingMetricSpecification **   <a name="autoscaling-Type-PredictiveScalingMetricSpecification-PredefinedScalingMetricSpecification"></a>
 The predefined scaling metric specification.
Type: [PredictiveScalingPredefinedScalingMetricSpecification](API_PredictiveScalingPredefinedScalingMetricSpecification.md) object
Required: No

## See Also
<a name="API_PredictiveScalingMetricSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/PredictiveScalingMetricSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/PredictiveScalingMetricSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/PredictiveScalingMetricSpecification)
