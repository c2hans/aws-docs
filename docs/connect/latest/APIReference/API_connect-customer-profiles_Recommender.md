---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_Recommender.html
---

# Recommender
<a name="API_connect-customer-profiles_Recommender"></a>

The recommender used to generate the recommendations.

## Contents
<a name="API_connect-customer-profiles_Recommender_Contents"></a>

 ** Name **   <a name="connect-Type-connect-customer-profiles_Recommender-Name"></a>
The unique name of the recommender.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** Filters **   <a name="connect-Type-connect-customer-profiles_Recommender-Filters"></a>
A list of filters to apply to the returned recommendations. Filters define criteria for including or excluding items from the recommendation results.
Type: Array of [RecommenderFilter](API_connect-customer-profiles_RecommenderFilter.md) objects
Array Members: Maximum number of 1 item.
Required: No

 ** PromotionalFilters **   <a name="connect-Type-connect-customer-profiles_Recommender-PromotionalFilters"></a>
A list of promotional filters to apply to the recommendations. Promotional filters allow you to promote specific items within a configurable subset of recommendation results.
Type: Array of [RecommenderPromotionalFilter](API_connect-customer-profiles_RecommenderPromotionalFilter.md) objects
Array Members: Maximum number of 1 item.
Required: No

## See Also
<a name="API_connect-customer-profiles_Recommender_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/Recommender)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/Recommender)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/Recommender)
