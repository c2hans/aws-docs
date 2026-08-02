---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceRecommendedOptionProjectedMetric.html
---

# ECSServiceRecommendedOptionProjectedMetric
<a name="API_ECSServiceRecommendedOptionProjectedMetric"></a>

 Describes the projected metrics of an Amazon ECS service recommendation option.

To determine the performance difference between your current Amazon ECS service and the recommended option, compare the metric data of your service against its projected metric data.

## Contents
<a name="API_ECSServiceRecommendedOptionProjectedMetric_Contents"></a>

 ** projectedMetrics **   <a name="computeoptimizer-Type-ECSServiceRecommendedOptionProjectedMetric-projectedMetrics"></a>
 An array of objects that describe the projected metric.
Type: Array of [ECSServiceProjectedMetric](API_ECSServiceProjectedMetric.md) objects
Required: No

 ** recommendedCpuUnits **   <a name="computeoptimizer-Type-ECSServiceRecommendedOptionProjectedMetric-recommendedCpuUnits"></a>
 The recommended CPU size for the Amazon ECS service.
Type: Integer
Required: No

 ** recommendedMemorySize **   <a name="computeoptimizer-Type-ECSServiceRecommendedOptionProjectedMetric-recommendedMemorySize"></a>
 The recommended memory size for the Amazon ECS service.
Type: Integer
Required: No

## See Also
<a name="API_ECSServiceRecommendedOptionProjectedMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ECSServiceRecommendedOptionProjectedMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ECSServiceRecommendedOptionProjectedMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ECSServiceRecommendedOptionProjectedMetric)
