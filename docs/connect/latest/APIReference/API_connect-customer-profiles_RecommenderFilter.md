---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_RecommenderFilter.html
---

# RecommenderFilter
<a name="API_connect-customer-profiles_RecommenderFilter"></a>

A filter that specifies criteria for including or excluding items from recommendations.

## Contents
<a name="API_connect-customer-profiles_RecommenderFilter_Contents"></a>

 ** Name **   <a name="connect-Type-connect-customer-profiles_RecommenderFilter-Name"></a>
The name of the recommender filter to apply.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** Values **   <a name="connect-Type-connect-customer-profiles_RecommenderFilter-Values"></a>
The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma.
Type: String to string map
Map Entries: Maximum number of 25 items.
Key Length Constraints: Maximum length of 50.
Key Pattern: `[A-Za-z0-9_]+`
Value Length Constraints: Maximum length of 3000.
Required: No

## See Also
<a name="API_connect-customer-profiles_RecommenderFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/RecommenderFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/RecommenderFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/RecommenderFilter)
