---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_RateCardItem.html
---

# RateCardItem
<a name="API_marketplace-agreements_RateCardItem"></a>

Defines the per unit rates for each individual product dimension.

## Contents
<a name="API_marketplace-agreements_RateCardItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** dimensionKey **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RateCardItem-dimensionKey"></a>
Dimension for which the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

 ** price **   <a name="AWSMarketplaceService-Type-marketplace-agreements_RateCardItem-price"></a>
Per unit price for the product dimension that’s used for calculating the amount to be charged.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `(.)+`
Required: No

## See Also
<a name="API_marketplace-agreements_RateCardItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/RateCardItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/RateCardItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/RateCardItem)
