---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EffectiveRecommendationPreferences.html
---

# EffectiveRecommendationPreferences
<a name="API_EffectiveRecommendationPreferences"></a>

Describes the effective recommendation preferences for a resource.

## Contents
<a name="API_EffectiveRecommendationPreferences_Contents"></a>

 ** cpuVendorArchitectures **   <a name="computeoptimizer-Type-EffectiveRecommendationPreferences-cpuVendorArchitectures"></a>
Describes the CPU vendor and architecture for an instance or Auto Scaling group recommendations.
For example, when you specify `AWS_ARM64` with:
+ A [GetEC2InstanceRecommendations](API_GetEC2InstanceRecommendations.md) or [GetAutoScalingGroupRecommendations](API_GetAutoScalingGroupRecommendations.md) request, Compute Optimizer returns recommendations that consist of Graviton instance types only.
+ A [GetEC2RecommendationProjectedMetrics](API_GetEC2RecommendationProjectedMetrics.md) request, Compute Optimizer returns projected utilization metrics for Graviton instance type recommendations only.
+ A [ExportEC2InstanceRecommendations](API_ExportEC2InstanceRecommendations.md) or [ExportAutoScalingGroupRecommendations](API_ExportAutoScalingGroupRecommendations.md) request, Compute Optimizer exports recommendations that consist of Graviton instance types only.
Type: Array of strings
Valid Values: `AWS_ARM64 | CURRENT`
Required: No

 ** enhancedInfrastructureMetrics **   <a name="computeoptimizer-Type-EffectiveRecommendationPreferences-enhancedInfrastructureMetrics"></a>
Describes the activation status of the enhanced infrastructure metrics preference.
A status of `Active` confirms that the preference is applied in the latest recommendation refresh, and a status of `Inactive` confirms that it's not yet applied to recommendations.
For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.
Type: String
Valid Values: `Active | Inactive`
Required: No

 ** externalMetricsPreference **   <a name="computeoptimizer-Type-EffectiveRecommendationPreferences-externalMetricsPreference"></a>
 An object that describes the external metrics recommendation preference.
 If the preference is applied in the latest recommendation refresh, an object with a valid `source` value appears in the response. If the preference isn't applied to the recommendations already, then this object doesn't appear in the response.
Type: [ExternalMetricsPreference](API_ExternalMetricsPreference.md) object
Required: No

 ** inferredWorkloadTypes **   <a name="computeoptimizer-Type-EffectiveRecommendationPreferences-inferredWorkloadTypes"></a>
Describes the activation status of the inferred workload types preference.
A status of `Active` confirms that the preference is applied in the latest recommendation refresh. A status of `Inactive` confirms that it's not yet applied to recommendations.
Type: String
Valid Values: `Active | Inactive`
Required: No

 ** lookBackPeriod **   <a name="computeoptimizer-Type-EffectiveRecommendationPreferences-lookBackPeriod"></a>
 The number of days the utilization metrics of the AWS resource are analyzed.
Type: String
Valid Values: `DAYS_14 | DAYS_32 | DAYS_93`
Required: No

 ** preferredResources **   <a name="computeoptimizer-Type-EffectiveRecommendationPreferences-preferredResources"></a>
 The resource type values that are considered as candidates when generating rightsizing recommendations.
Type: Array of [EffectivePreferredResource](API_EffectivePreferredResource.md) objects
Required: No

 ** savingsEstimationMode **   <a name="computeoptimizer-Type-EffectiveRecommendationPreferences-savingsEstimationMode"></a>
 Describes the savings estimation mode applied for calculating savings opportunity for a resource.
Type: [InstanceSavingsEstimationMode](API_InstanceSavingsEstimationMode.md) object
Required: No

 ** utilizationPreferences **   <a name="computeoptimizer-Type-EffectiveRecommendationPreferences-utilizationPreferences"></a>
 The resource’s CPU and memory utilization preferences, such as threshold and headroom, that are used to generate rightsizing recommendations.
This preference is only available for the Amazon EC2 instance resource type.
Type: Array of [UtilizationPreference](API_UtilizationPreference.md) objects
Required: No

## See Also
<a name="API_EffectiveRecommendationPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/EffectiveRecommendationPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/EffectiveRecommendationPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/EffectiveRecommendationPreferences)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
