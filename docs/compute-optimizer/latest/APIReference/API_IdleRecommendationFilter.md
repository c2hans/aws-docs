---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleRecommendationFilter.html
---

# IdleRecommendationFilter
<a name="API_IdleRecommendationFilter"></a>

Describes a filter that returns a more specific list of idle resource recommendations.

## Contents
<a name="API_IdleRecommendationFilter_Contents"></a>

 ** name **   <a name="computeoptimizer-Type-IdleRecommendationFilter-name"></a>
 The name of the filter.
 Specify `Finding` to return recommendations with a specific finding classification.
You can filter your idle resource recommendations by `tag:key` and `tag-key` tags.
A `tag:key` is a key and value combination of a tag assigned to your idle resource recommendations. Use the tag key in the filter name and the tag value as the filter value. For example, to find all idle resource service recommendations that have a tag with the key of `Owner` and the value of `TeamA`, specify `tag:Owner` for the filter name and `TeamA` for the filter value.
A `tag-key` is the key of a tag assigned to your idle resource recommendations. Use this filter to find all of your idle resource recommendations that have a tag with a specific key. This doesn’t consider the tag value. For example, you can find your idle resource service recommendations with a tag key value of `Owner` or without any tag keys assigned.
Type: String
Valid Values: `Finding | ResourceType`
Required: No

 ** values **   <a name="computeoptimizer-Type-IdleRecommendationFilter-values"></a>
The value of the filter.
Type: Array of strings
Required: No

## See Also
<a name="API_IdleRecommendationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/IdleRecommendationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/IdleRecommendationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/IdleRecommendationFilter)
