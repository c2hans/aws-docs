---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ListingRecommendationsSummary.html
---

# ListingRecommendationsSummary

The details of the resource assessed under the Listing Recommendations framework.

## Contents
<a name="API_ListingRecommendationsSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Tier **   <a name="AWSMarketplaceService-Type-ListingRecommendationsSummary-Tier"></a>
The quality tier of the listing. Valid values are `NEEDS_IMPROVEMENT`, `BASIC`, `STRONG`, and `EXCELLENT`.
Type: String
Valid Values: `NEEDS_IMPROVEMENT | BASIC | STRONG | EXCELLENT`
Required: Yes

 ** EntityRevision **   <a name="AWSMarketplaceService-Type-ListingRecommendationsSummary-EntityRevision"></a>
The revision of the entity that the recommendations were generated against. To check whether the recommendations are out of date, compare this value with the current revision of the entity.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_ListingRecommendationsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ListingRecommendationsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ListingRecommendationsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ListingRecommendationsSummary)
