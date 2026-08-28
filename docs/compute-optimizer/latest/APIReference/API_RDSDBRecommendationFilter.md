---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDBRecommendationFilter.html
---

# RDSDBRecommendationFilter
<a name="API_RDSDBRecommendationFilter"></a>

 Describes a filter that returns a more specific list of DB instance recommendations. Use this filter with the [GetECSServiceRecommendations](API_GetECSServiceRecommendations.md) action.

## Contents
<a name="API_RDSDBRecommendationFilter_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-RDSDBRecommendationFilter-name"></a>
 The name of the filter.
 Specify `Finding` to return recommendations with a specific finding classification.
You can filter your DB instance recommendations by `tag:key` and `tag-key` tags.
A `tag:key` is a key and value combination of a tag assigned to your DB instance recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all DB instance recommendations that have a tag with the key of `Owner` and the value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
A `tag-key` is the key of a tag assigned to your DB instance recommendations. Use this filter to find all of your DB instance recommendations that have a tag with a specific key. This doesn’t consider the tag value. For example, you can find your DB instance recommendations with a tag key value of `Owner` or without any tag keys assigned.
Type: String
Valid Values: `InstanceFinding | InstanceFindingReasonCode | StorageFinding | StorageFindingReasonCode | Idle`
Required: No

 ** values **   <a name="computeoptimizer-Type-RDSDBRecommendationFilter-values"></a>
 The value of the filter.
Type: Array of strings
Required: No

## See Also
<a name="API_RDSDBRecommendationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RDSDBRecommendationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RDSDBRecommendationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RDSDBRecommendationFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
