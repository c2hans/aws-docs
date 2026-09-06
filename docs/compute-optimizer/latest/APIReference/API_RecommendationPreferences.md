---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendationPreferences.html
---

# RecommendationPreferences
<a name="API_RecommendationPreferences"></a>

Describes the recommendation preferences to return in the response of a [GetAutoScalingGroupRecommendations](API_GetAutoScalingGroupRecommendations.md), [GetEC2InstanceRecommendations](API_GetEC2InstanceRecommendations.md), [GetEC2RecommendationProjectedMetrics](API_GetEC2RecommendationProjectedMetrics.md), [GetRDSDatabaseRecommendations](API_GetRDSDatabaseRecommendations.md), and [GetRDSDatabaseRecommendationProjectedMetrics](API_GetRDSDatabaseRecommendationProjectedMetrics.md) request.

## Contents
<a name="API_RecommendationPreferences_Contents"></a>

 ** cpuVendorArchitectures **   <a name="computeoptimizer-Type-RecommendationPreferences-cpuVendorArchitectures"></a>
Specifies the CPU vendor and architecture for Amazon EC2 instance and Auto Scaling group recommendations.
For example, when you specify `AWS_ARM64` with:
+ A [GetEC2InstanceRecommendations](API_GetEC2InstanceRecommendations.md) or [GetAutoScalingGroupRecommendations](API_GetAutoScalingGroupRecommendations.md) request, Compute Optimizer returns recommendations that consist of Graviton instance types only.
+ A [GetEC2RecommendationProjectedMetrics](API_GetEC2RecommendationProjectedMetrics.md) request, Compute Optimizer returns projected utilization metrics for Graviton instance type recommendations only.
+ A [ExportEC2InstanceRecommendations](API_ExportEC2InstanceRecommendations.md) or [ExportAutoScalingGroupRecommendations](API_ExportAutoScalingGroupRecommendations.md) request, Compute Optimizer exports recommendations that consist of Graviton instance types only.
Type: Array of strings
Valid Values: `AWS_ARM64 | CURRENT`
Required: No

## See Also
<a name="API_RecommendationPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RecommendationPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RecommendationPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RecommendationPreferences)
