---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EBSFilter.html
---

# EBSFilter
<a name="API_EBSFilter"></a>

Describes a filter that returns a more specific list of Amazon Elastic Block Store (Amazon EBS) volume recommendations. Use this filter with the [GetEBSVolumeRecommendations](API_GetEBSVolumeRecommendations.md) action.

You can use `LambdaFunctionRecommendationFilter` with the [GetLambdaFunctionRecommendations](API_GetLambdaFunctionRecommendations.md) action, `JobFilter` with the [DescribeRecommendationExportJobs](API_DescribeRecommendationExportJobs.md) action, and `Filter` with the [GetAutoScalingGroupRecommendations](API_GetAutoScalingGroupRecommendations.md) and [GetEC2InstanceRecommendations](API_GetEC2InstanceRecommendations.md) actions.

## Contents
<a name="API_EBSFilter_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-EBSFilter-name"></a>
The name of the filter.
Specify `Finding` to return recommendations with a specific finding classification (for example, `NotOptimized`).
You can filter your Amazon EBS volume recommendations by `tag:key` and `tag-key` tags.
A `tag:key` is a key and value combination of a tag assigned to your Amazon EBS volume recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all Amazon EBS volume recommendations that have a tag with the key of `Owner` and the value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
A `tag-key` is the key of a tag assigned to your Amazon EBS volume recommendations. Use this filter to find all of your Amazon EBS volume recommendations that have a tag with a specific key. This doesn’t consider the tag value. For example, you can find your Amazon EBS volume recommendations with a tag key value of `Owner` or without any tag keys assigned.
Type: String
Valid Values: `Finding`
Required: No

 ** values **   <a name="computeoptimizer-Type-EBSFilter-values"></a>
The value of the filter.
The valid values are `Optimized`, or `NotOptimized`.
Type: Array of strings
Required: No

## See Also
<a name="API_EBSFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/EBSFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/EBSFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/EBSFilter)
