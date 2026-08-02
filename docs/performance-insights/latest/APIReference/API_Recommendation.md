---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_Recommendation.html
---

# Recommendation
<a name="API_Recommendation"></a>

The list of recommendations for the insight.

## Contents
<a name="API_Recommendation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RecommendationDescription **   <a name="performanceinsights-Type-Recommendation-RecommendationDescription"></a>
The recommendation details to help resolve the performance issue. For example, `Investigate the following SQLs that contributed to 100% of the total DBLoad during that time period: sql-id`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8000.
Pattern: `(.|\n)*`
Required: No

 ** RecommendationDetails **   <a name="performanceinsights-Type-Recommendation-RecommendationDetails"></a>
Detailed information about the recommendation, including steps to resolve the performance issue.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8000.
Pattern: `(.|\n)*`
Required: No

 ** RecommendationId **   <a name="performanceinsights-Type-Recommendation-RecommendationId"></a>
The unique identifier for the recommendation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_Recommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/Recommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/Recommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/Recommendation)
