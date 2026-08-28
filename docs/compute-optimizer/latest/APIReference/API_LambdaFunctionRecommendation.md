---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaFunctionRecommendation.html
---

# LambdaFunctionRecommendation
<a name="API_LambdaFunctionRecommendation"></a>

Describes an AWS Lambda function recommendation.

## Contents
<a name="API_LambdaFunctionRecommendation_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-accountId"></a>
The AWS account ID of the function.
Type: String
Required: No

 ** currentMemorySize **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-currentMemorySize"></a>
The amount of memory, in MB, that's allocated to the current function.
Type: Integer
Required: No

 ** currentPerformanceRisk **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-currentPerformanceRisk"></a>
The risk of the current Lambda function not meeting the performance needs of its workloads. The higher the risk, the more likely the current Lambda function requires more memory.
Type: String
Valid Values: `VeryLow | Low | Medium | High`
Required: No

 ** effectiveRecommendationPreferences **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-effectiveRecommendationPreferences"></a>
 Describes the effective recommendation preferences for Lambda functions.
Type: [LambdaEffectiveRecommendationPreferences](API_LambdaEffectiveRecommendationPreferences.md) object
Required: No

 ** finding **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-finding"></a>
The finding classification of the function.
Findings for functions include:
+  ** `Optimized` ** — The function is correctly provisioned to run your workload based on its current configuration and its utilization history. This finding classification does not include finding reason codes.
+  ** `NotOptimized` ** — The function is performing at a higher level (over-provisioned) or at a lower level (under-provisioned) than required for your workload because its current configuration is not optimal. Over-provisioned resources might lead to unnecessary infrastructure cost, and under-provisioned resources might lead to poor application performance. This finding classification can include the `MemoryUnderprovisioned` and `MemoryUnderprovisioned` finding reason codes.
+  ** `Unavailable` ** — Compute Optimizer was unable to generate a recommendation for the function. This could be because the function has not accumulated sufficient metric data, or the function does not qualify for a recommendation. This finding classification can include the `InsufficientData` and `Inconclusive` finding reason codes.
**Note**
Functions with a finding of unavailable are not returned unless you specify the `filter` parameter with a value of `Unavailable` in your `GetLambdaFunctionRecommendations` request.
Type: String
Valid Values: `Optimized | NotOptimized | Unavailable`
Required: No

 ** findingReasonCodes **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-findingReasonCodes"></a>
The reason for the finding classification of the function.
Functions that have a finding classification of `Optimized` don't have a finding reason code.
Finding reason codes for functions include:
+  ** `MemoryOverprovisioned` ** — The function is over-provisioned when its memory configuration can be sized down while still meeting the performance requirements of your workload. An over-provisioned function might lead to unnecessary infrastructure cost. This finding reason code is part of the `NotOptimized` finding classification.
+  ** `MemoryUnderprovisioned` ** — The function is under-provisioned when its memory configuration doesn't meet the performance requirements of the workload. An under-provisioned function might lead to poor application performance. This finding reason code is part of the `NotOptimized` finding classification.
+  ** `InsufficientData` ** — The function does not have sufficient metric data for Compute Optimizer to generate a recommendation. For more information, see the [Supported resources and requirements](https://docs.aws.amazon.com/compute-optimizer/latest/ug/requirements.html) in the * AWS Compute Optimizer User Guide*. This finding reason code is part of the `Unavailable` finding classification.
+  ** `Inconclusive` ** — The function does not qualify for a recommendation because Compute Optimizer cannot generate a recommendation with a high degree of confidence. This finding reason code is part of the `Unavailable` finding classification.
Type: Array of strings
Valid Values: `MemoryOverprovisioned | MemoryUnderprovisioned | InsufficientData | Inconclusive`
Required: No

 ** functionArn **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-functionArn"></a>
The Amazon Resource Name (ARN) of the current function.
Type: String
Required: No

 ** functionVersion **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-functionVersion"></a>
The version number of the current function.
Type: String
Required: No

 ** lastRefreshTimestamp **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-lastRefreshTimestamp"></a>
The timestamp of when the function recommendation was last generated.
Type: Timestamp
Required: No

 ** lookbackPeriodInDays **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-lookbackPeriodInDays"></a>
The number of days for which utilization metrics were analyzed for the function.
Type: Double
Required: No

 ** memorySizeRecommendationOptions **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-memorySizeRecommendationOptions"></a>
An array of objects that describe the memory configuration recommendation options for the function.
Type: Array of [LambdaFunctionMemoryRecommendationOption](API_LambdaFunctionMemoryRecommendationOption.md) objects
Required: No

 ** numberOfInvocations **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-numberOfInvocations"></a>
The number of times your function code was applied during the look-back period.
Type: Long
Required: No

 ** tags **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-tags"></a>
 A list of tags assigned to your Lambda function recommendations.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** utilizationMetrics **   <a name="computeoptimizer-Type-LambdaFunctionRecommendation-utilizationMetrics"></a>
An array of objects that describe the utilization metrics of the function.
Type: Array of [LambdaFunctionUtilizationMetric](API_LambdaFunctionUtilizationMetric.md) objects
Required: No

## See Also
<a name="API_LambdaFunctionRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/LambdaFunctionRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/LambdaFunctionRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/LambdaFunctionRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
