---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendationPreferencesDetail.html
---

# RecommendationPreferencesDetail
<a name="API_RecommendationPreferencesDetail"></a>

Describes a recommendation preference.

## Contents
<a name="API_RecommendationPreferencesDetail_Contents"></a>

 ** enhancedInfrastructureMetrics **   <a name="computeoptimizer-Type-RecommendationPreferencesDetail-enhancedInfrastructureMetrics"></a>
The status of the enhanced infrastructure metrics recommendation preference.
When the recommendations page is refreshed, a status of `Active` confirms that the preference is applied to the recommendations, and a status of `Inactive` confirms that the preference isn't yet applied to recommendations.
For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.
Type: String
Valid Values: `Active | Inactive`
Required: No

 ** externalMetricsPreference **   <a name="computeoptimizer-Type-RecommendationPreferencesDetail-externalMetricsPreference"></a>
 An object that describes the external metrics recommendation preference.
 If the preference is applied in the latest recommendation refresh, an object with a valid `source` value appears in the response. If the preference isn't applied to the recommendations already, then this object doesn't appear in the response.
Type: [ExternalMetricsPreference](API_ExternalMetricsPreference.md) object
Required: No

 ** inferredWorkloadTypes **   <a name="computeoptimizer-Type-RecommendationPreferencesDetail-inferredWorkloadTypes"></a>
The status of the inferred workload types recommendation preference.
When the recommendations page is refreshed, a status of `Active` confirms that the preference is applied to the recommendations, and a status of `Inactive` confirms that the preference isn't yet applied to recommendations.
Type: String
Valid Values: `Active | Inactive`
Required: No

 ** lookBackPeriod **   <a name="computeoptimizer-Type-RecommendationPreferencesDetail-lookBackPeriod"></a>
 The preference to control the number of days the utilization metrics of the AWS resource are analyzed. If the preference isn’t set, this object is null.
Type: String
Valid Values: `DAYS_14 | DAYS_32 | DAYS_93`
Required: No

 ** preferredResources **   <a name="computeoptimizer-Type-RecommendationPreferencesDetail-preferredResources"></a>
 The preference to control which resource type values are considered when generating rightsizing recommendations. This object resolves any wildcard expressions and returns the effective list of candidate resource type values. If the preference isn’t set, this object is null.
Type: Array of [EffectivePreferredResource](API_EffectivePreferredResource.md) objects
Required: No

 ** resourceType **   <a name="computeoptimizer-Type-RecommendationPreferencesDetail-resourceType"></a>
The target resource type of the recommendation preference to create.
The `Ec2Instance` option encompasses standalone instances and instances that are part of Auto Scaling groups. The `AutoScalingGroup` option encompasses only instances that are part of an Auto Scaling group.
Type: String
Valid Values: `Ec2Instance | AutoScalingGroup | EbsVolume | EcsService | RdsDBInstance | AuroraDBClusterStorage`
Required: No

 ** savingsEstimationMode **   <a name="computeoptimizer-Type-RecommendationPreferencesDetail-savingsEstimationMode"></a>
 Describes the savings estimation mode used for calculating savings opportunity.
Only the account manager or delegated administrator of your organization can activate this preference.
Type: String
Valid Values: `AfterDiscounts | BeforeDiscounts`
Required: No

 ** scope **   <a name="computeoptimizer-Type-RecommendationPreferencesDetail-scope"></a>
An object that describes the scope of the recommendation preference.
Recommendation preferences can be created at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.
Type: [Scope](API_Scope.md) object
Required: No

 ** utilizationPreferences **   <a name="computeoptimizer-Type-RecommendationPreferencesDetail-utilizationPreferences"></a>
 The preference to control the resource’s CPU utilization threshold, CPU utilization headroom, and memory utilization headroom. If the preference isn’t set, this object is null.
This preference is only available for the Amazon EC2 instance resource type.
Type: Array of [UtilizationPreference](API_UtilizationPreference.md) objects
Required: No

## See Also
<a name="API_RecommendationPreferencesDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RecommendationPreferencesDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RecommendationPreferencesDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RecommendationPreferencesDetail)
