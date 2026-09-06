---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_PredictiveScalingPredefinedMetricPairSpecification.html
---

# PredictiveScalingPredefinedMetricPairSpecification
<a name="API_PredictiveScalingPredefinedMetricPairSpecification"></a>

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

## Contents
<a name="API_PredictiveScalingPredefinedMetricPairSpecification_Contents"></a>

 ** PredefinedMetricType **   <a name="autoscaling-Type-PredictiveScalingPredefinedMetricPairSpecification-PredefinedMetricType"></a>
 Indicates which metrics to use. There are two different types of metrics for each metric type: one is a load metric and one is a scaling metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** ResourceLabel **   <a name="autoscaling-Type-PredictiveScalingPredefinedMetricPairSpecification-ResourceLabel"></a>
 A label that uniquely identifies a specific target group from which to determine the total and average request count.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1023.
Required: No

## See Also
<a name="API_PredictiveScalingPredefinedMetricPairSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/PredictiveScalingPredefinedMetricPairSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/PredictiveScalingPredefinedMetricPairSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/PredictiveScalingPredefinedMetricPairSpecification)
