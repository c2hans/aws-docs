---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ProductContentRecommendations.html
---

# ProductContentRecommendations

The content recommendations for a product listing, with one member for each listing field. A member is absent if nothing is recommended for that field.

## Contents
<a name="API_ProductContentRecommendations_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Citations **   <a name="AWSMarketplaceService-Type-ProductContentRecommendations-Citations"></a>
The sources that the recommendations are based on. You can have up to 5 sources. The list is empty if there are none.
Type: Array of [RecommendationCitation](API_RecommendationCitation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: Yes

 ** AdditionalResources **   <a name="AWSMarketplaceService-Type-ProductContentRecommendations-AdditionalResources"></a>
The recommendation for the additional resources. Each alternative has up to 3 resources.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** Categories **   <a name="AWSMarketplaceService-Type-ProductContentRecommendations-Categories"></a>
The recommendation for the categories.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** Highlights **   <a name="AWSMarketplaceService-Type-ProductContentRecommendations-Highlights"></a>
The recommendation for the highlights.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** LongDescription **   <a name="AWSMarketplaceService-Type-ProductContentRecommendations-LongDescription"></a>
The recommendation for the long description.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** ProductTitle **   <a name="AWSMarketplaceService-Type-ProductContentRecommendations-ProductTitle"></a>
The recommendation for the product title.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** SearchKeywords **   <a name="AWSMarketplaceService-Type-ProductContentRecommendations-SearchKeywords"></a>
The recommendation for the search keywords.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** ShortDescription **   <a name="AWSMarketplaceService-Type-ProductContentRecommendations-ShortDescription"></a>
The recommendation for the short description.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

 ** SupportDescription **   <a name="AWSMarketplaceService-Type-ProductContentRecommendations-SupportDescription"></a>
The recommendation for the support description.
Type: [ContentRecommendation](API_ContentRecommendation.md) object
Required: No

## See Also
<a name="API_ProductContentRecommendations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ProductContentRecommendations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ProductContentRecommendations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ProductContentRecommendations)
