---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_VolumeRecommendation.html
---

# VolumeRecommendation
<a name="API_VolumeRecommendation"></a>

Describes an Amazon Elastic Block Store (Amazon EBS) volume recommendation.

## Contents
<a name="API_VolumeRecommendation_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-VolumeRecommendation-accountId"></a>
The AWS account ID of the volume.
Type: String
Required: No

 ** currentConfiguration **   <a name="computeoptimizer-Type-VolumeRecommendation-currentConfiguration"></a>
An array of objects that describe the current configuration of the volume.
Type: [VolumeConfiguration](API_VolumeConfiguration.md) object
Required: No

 ** currentPerformanceRisk **   <a name="computeoptimizer-Type-VolumeRecommendation-currentPerformanceRisk"></a>
The risk of the current EBS volume not meeting the performance needs of its workloads. The higher the risk, the more likely the current EBS volume doesn't have sufficient capacity.
Type: String
Valid Values: `VeryLow | Low | Medium | High`
Required: No

 ** effectiveRecommendationPreferences **   <a name="computeoptimizer-Type-VolumeRecommendation-effectiveRecommendationPreferences"></a>
 Describes the effective recommendation preferences for Amazon EBS volume.
Type: [EBSEffectiveRecommendationPreferences](API_EBSEffectiveRecommendationPreferences.md) object
Required: No

 ** finding **   <a name="computeoptimizer-Type-VolumeRecommendation-finding"></a>
The finding classification of the volume.
Findings for volumes include:
+  ** `NotOptimized` **—A volume is considered not optimized when AWS Compute Optimizer identifies a recommendation that can provide better performance for your workload.
+  ** `Optimized` **—An volume is considered optimized when Compute Optimizer determines that the volume is correctly provisioned to run your workload based on the chosen volume type. For optimized resources, Compute Optimizer might recommend a new generation volume type.
Type: String
Valid Values: `Optimized | NotOptimized`
Required: No

 ** lastRefreshTimestamp **   <a name="computeoptimizer-Type-VolumeRecommendation-lastRefreshTimestamp"></a>
The timestamp of when the volume recommendation was last generated.
Type: Timestamp
Required: No

 ** lookBackPeriodInDays **   <a name="computeoptimizer-Type-VolumeRecommendation-lookBackPeriodInDays"></a>
The number of days for which utilization metrics were analyzed for the volume.
Type: Double
Required: No

 ** tags **   <a name="computeoptimizer-Type-VolumeRecommendation-tags"></a>
 A list of tags assigned to your Amazon EBS volume recommendations.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** utilizationMetrics **   <a name="computeoptimizer-Type-VolumeRecommendation-utilizationMetrics"></a>
An array of objects that describe the utilization metrics of the volume.
Type: Array of [EBSUtilizationMetric](API_EBSUtilizationMetric.md) objects
Required: No

 ** volumeArn **   <a name="computeoptimizer-Type-VolumeRecommendation-volumeArn"></a>
The Amazon Resource Name (ARN) of the current volume.
Type: String
Required: No

 ** volumeRecommendationOptions **   <a name="computeoptimizer-Type-VolumeRecommendation-volumeRecommendationOptions"></a>
An array of objects that describe the recommendation options for the volume.
Type: Array of [VolumeRecommendationOption](API_VolumeRecommendationOption.md) objects
Required: No

## See Also
<a name="API_VolumeRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/VolumeRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/VolumeRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/VolumeRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
