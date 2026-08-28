---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaFunctionRecommendationFilter.html
---

# LambdaFunctionRecommendationFilter
<a name="API_LambdaFunctionRecommendationFilter"></a>

Describes a filter that returns a more specific list of AWS Lambda function recommendations. Use this filter with the [GetLambdaFunctionRecommendations](API_GetLambdaFunctionRecommendations.md) action.

You can use `EBSFilter` with the [GetEBSVolumeRecommendations](API_GetEBSVolumeRecommendations.md) action, `JobFilter` with the [DescribeRecommendationExportJobs](API_DescribeRecommendationExportJobs.md) action, and `Filter` with the [GetAutoScalingGroupRecommendations](API_GetAutoScalingGroupRecommendations.md) and [GetEC2InstanceRecommendations](API_GetEC2InstanceRecommendations.md) actions.

## Contents
<a name="API_LambdaFunctionRecommendationFilter_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-LambdaFunctionRecommendationFilter-name"></a>
The name of the filter.
Specify `Finding` to return recommendations with a specific finding classification (for example, `NotOptimized`).
Specify `FindingReasonCode` to return recommendations with a specific finding reason code (for example, `MemoryUnderprovisioned`).
You can filter your Lambda function recommendations by `tag:key` and `tag-key` tags.
A `tag:key` is a key and value combination of a tag assigned to your Lambda function recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all Lambda function recommendations that have a tag with the key of `Owner` and the value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
A `tag-key` is the key of a tag assigned to your Lambda function recommendations. Use this filter to find all of your Lambda function recommendations that have a tag with a specific key. This doesn’t consider the tag value. For example, you can find your Lambda function recommendations with a tag key value of `Owner` or without any tag keys assigned.
Type: String
Valid Values: `Finding | FindingReasonCode`
Required: No

 ** values **   <a name="computeoptimizer-Type-LambdaFunctionRecommendationFilter-values"></a>
The value of the filter.
The valid values for this parameter are as follows, depending on what you specify for the `name` parameter:
+ Specify `Optimized`, `NotOptimized`, or `Unavailable` if you specify the `name` parameter as `Finding`.
+ Specify `MemoryOverprovisioned`, `MemoryUnderprovisioned`, `InsufficientData`, or `Inconclusive` if you specify the `name` parameter as `FindingReasonCode`.
Type: Array of strings
Required: No

## See Also
<a name="API_LambdaFunctionRecommendationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/LambdaFunctionRecommendationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/LambdaFunctionRecommendationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/LambdaFunctionRecommendationFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
