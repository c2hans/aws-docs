---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_OfferInformation.html
---

# OfferInformation
<a name="API_marketplace-discovery_OfferInformation"></a>

Summary information about an offer, including the offer identifier, name, and seller of record.

## Contents
<a name="API_marketplace-discovery_OfferInformation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** offerId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferInformation-offerId"></a>
The unique identifier of the offer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** sellerOfRecord **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferInformation-sellerOfRecord"></a>
The entity responsible for selling the product under this offer.
Type: [SellerInformation](API_marketplace-discovery_SellerInformation.md) object
Required: Yes

 ** offerName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_OfferInformation-offerName"></a>
The display name of the offer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_marketplace-discovery_OfferInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/OfferInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/OfferInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/OfferInformation)
