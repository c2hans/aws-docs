---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceRecommendation.html
---

# ECSServiceRecommendation
<a name="API_ECSServiceRecommendation"></a>

 Describes an Amazon ECS service recommendation.

## Contents
<a name="API_ECSServiceRecommendation_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-ECSServiceRecommendation-accountId"></a>
 The AWS account ID of the Amazon ECS service.
Type: String
Required: No

 ** currentPerformanceRisk **   <a name="computeoptimizer-Type-ECSServiceRecommendation-currentPerformanceRisk"></a>
 The risk of the current Amazon ECS service not meeting the performance needs of its workloads. The higher the risk, the more likely the current service can't meet the performance requirements of its workload.
Type: String
Valid Values: `VeryLow | Low | Medium | High`
Required: No

 ** currentServiceConfiguration **   <a name="computeoptimizer-Type-ECSServiceRecommendation-currentServiceConfiguration"></a>
 The configuration of the current Amazon ECS service.
Type: [ServiceConfiguration](API_ServiceConfiguration.md) object
Required: No

 ** effectiveRecommendationPreferences **   <a name="computeoptimizer-Type-ECSServiceRecommendation-effectiveRecommendationPreferences"></a>
 Describes the effective recommendation preferences for Amazon ECS services.
Type: [ECSEffectiveRecommendationPreferences](API_ECSEffectiveRecommendationPreferences.md) object
Required: No

 ** finding **   <a name="computeoptimizer-Type-ECSServiceRecommendation-finding"></a>
 The finding classification of an Amazon ECS service.
Findings for Amazon ECS services include:
+  ** `Underprovisioned` ** — When Compute Optimizer detects that there’s not enough memory or CPU, an Amazon ECS service is considered under-provisioned. An under-provisioned service might result in poor application performance.
+  ** `Overprovisioned` ** — When Compute Optimizer detects that there’s excessive memory or CPU, an Amazon ECS service is considered over-provisioned. An over-provisioned service might result in additional infrastructure costs.
+  ** `Optimized` ** — When both the CPU and memory of your Amazon ECS service meet the performance requirements of your workload, the service is considered optimized.
Type: String
Valid Values: `Optimized | Underprovisioned | Overprovisioned`
Required: No

 ** findingReasonCodes **   <a name="computeoptimizer-Type-ECSServiceRecommendation-findingReasonCodes"></a>
 The reason for the finding classification of an Amazon ECS service.
Finding reason codes for Amazon ECS services include:
+  ** `CPUUnderprovisioned` ** — The service CPU configuration can be sized up to enhance the performance of your workload. This is identified by analyzing the `CPUUtilization` metric of the current service during the look-back period.
+  ** `CPUOverprovisioned` ** — The service CPU configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `CPUUtilization` metric of the current service during the look-back period.
+  ** `MemoryUnderprovisioned` ** — The service memory configuration can be sized up to enhance the performance of your workload. This is identified by analyzing the `MemoryUtilization` metric of the current service during the look-back period.
+  ** `MemoryOverprovisioned` ** — The service memory configuration can be sized down while still meeting the performance requirements of your workload. This is identified by analyzing the `MemoryUtilization` metric of the current service during the look-back period.
Type: Array of strings
Valid Values: `MemoryOverprovisioned | MemoryUnderprovisioned | CPUOverprovisioned | CPUUnderprovisioned`
Required: No

 ** lastRefreshTimestamp **   <a name="computeoptimizer-Type-ECSServiceRecommendation-lastRefreshTimestamp"></a>
 The timestamp of when the Amazon ECS service recommendation was last generated.
Type: Timestamp
Required: No

 ** launchType **   <a name="computeoptimizer-Type-ECSServiceRecommendation-launchType"></a>
 The launch type the Amazon ECS service is using.
Compute Optimizer only supports the Fargate launch type.
Type: String
Valid Values: `EC2 | Fargate`
Required: No

 ** lookbackPeriodInDays **   <a name="computeoptimizer-Type-ECSServiceRecommendation-lookbackPeriodInDays"></a>
 The number of days the Amazon ECS service utilization metrics were analyzed.
Type: Double
Required: No

 ** serviceArn **   <a name="computeoptimizer-Type-ECSServiceRecommendation-serviceArn"></a>
 The Amazon Resource Name (ARN) of the current Amazon ECS service.
 The following is the format of the ARN:
 `arn:aws:ecs:region:aws_account_id:service/cluster-name/service-name`
Type: String
Required: No

 ** serviceRecommendationOptions **   <a name="computeoptimizer-Type-ECSServiceRecommendation-serviceRecommendationOptions"></a>
 An array of objects that describe the recommendation options for the Amazon ECS service.
Type: Array of [ECSServiceRecommendationOption](API_ECSServiceRecommendationOption.md) objects
Required: No

 ** tags **   <a name="computeoptimizer-Type-ECSServiceRecommendation-tags"></a>
 A list of tags assigned to your Amazon ECS service recommendations.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** utilizationMetrics **   <a name="computeoptimizer-Type-ECSServiceRecommendation-utilizationMetrics"></a>
 An array of objects that describe the utilization metrics of the Amazon ECS service.
Type: Array of [ECSServiceUtilizationMetric](API_ECSServiceUtilizationMetric.md) objects
Required: No

## See Also
<a name="API_ECSServiceRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ECSServiceRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ECSServiceRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ECSServiceRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
