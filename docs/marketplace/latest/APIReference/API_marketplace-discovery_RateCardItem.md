---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_RateCardItem.html
---

# RateCardItem
<a name="API_marketplace-discovery_RateCardItem"></a>

A per-unit rate within a rate card, defining the price for a specific dimension.

## Contents
<a name="API_marketplace-discovery_RateCardItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** dimensionKey **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RateCardItem-dimensionKey"></a>
The machine-readable key identifying the dimension being priced.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RateCardItem-displayName"></a>
The human-readable name of the dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** price **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RateCardItem-price"></a>
The price per unit for the dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** unit **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RateCardItem-unit"></a>
The unit of measurement for the dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: Yes

 ** description **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RateCardItem-description"></a>
A description of the dimension being priced.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** dimensionLabels **   <a name="AWSMarketplaceService-Type-marketplace-discovery_RateCardItem-dimensionLabels"></a>
Labels used to categorize this dimension, such as by region.
Type: Array of [DimensionLabel](API_marketplace-discovery_DimensionLabel.md) objects
Required: No

## See Also
<a name="API_marketplace-discovery_RateCardItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/RateCardItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/RateCardItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/RateCardItem)
