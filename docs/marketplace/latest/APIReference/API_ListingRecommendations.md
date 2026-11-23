---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ListingRecommendations.html
---

# ListingRecommendations

The recommendations that a listing recommendations control produced. Exactly one member is set, corresponding to the control: content recommendations for a product, content recommendations for a solution, or feature recommendations.

## Contents
<a name="API_ListingRecommendations_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** FeatureRecommendations **   <a name="AWSMarketplaceService-Type-ListingRecommendations-FeatureRecommendations"></a>
The recommendations for AWS Marketplace features to use with the listing, for a product or a solution.
Type: [FeatureRecommendations](API_FeatureRecommendations.md) object
Required: No

 ** ProductContentRecommendations **   <a name="AWSMarketplaceService-Type-ListingRecommendations-ProductContentRecommendations"></a>
The content recommendations for a product listing.
Type: [ProductContentRecommendations](API_ProductContentRecommendations.md) object
Required: No

 ** SolutionContentRecommendations **   <a name="AWSMarketplaceService-Type-ListingRecommendations-SolutionContentRecommendations"></a>
The content recommendations for a solution listing.
Type: [SolutionContentRecommendations](API_SolutionContentRecommendations.md) object
Required: No

## See Also
<a name="API_ListingRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ListingRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ListingRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ListingRecommendations)
