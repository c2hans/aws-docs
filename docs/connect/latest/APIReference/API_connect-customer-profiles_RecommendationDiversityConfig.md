---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_RecommendationDiversityConfig.html
---

# RecommendationDiversityConfig
<a name="API_connect-customer-profiles_RecommendationDiversityConfig"></a>

Runtime diversity configuration for a `GetProfileRecommendations` request.

## Contents
<a name="API_connect-customer-profiles_RecommendationDiversityConfig_Contents"></a>

 ** Enabled **   <a name="connect-Type-connect-customer-profiles_RecommendationDiversityConfig-Enabled"></a>
Whether diversity-aware recommendations are enabled for this request.
Type: Boolean
Required: Yes

 ** Values **   <a name="connect-Type-connect-customer-profiles_RecommendationDiversityConfig-Values"></a>
An optional map of placeholder name to integer cap value used to resolve `$name` placeholders defined in the recommender's `DiversityConfig` at inference time. Up to 2 entries are supported.
Type: String to integer map
Map Entries: Maximum number of 2 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Key Pattern: `^[a-zA-Z][a-zA-Z0-9_]*$`
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

## See Also
<a name="API_connect-customer-profiles_RecommendationDiversityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/RecommendationDiversityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/RecommendationDiversityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/RecommendationDiversityConfig)
