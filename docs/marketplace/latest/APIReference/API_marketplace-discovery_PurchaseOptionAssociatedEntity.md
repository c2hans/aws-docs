---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PurchaseOptionAssociatedEntity.html
---

# PurchaseOptionAssociatedEntity
<a name="API_marketplace-discovery_PurchaseOptionAssociatedEntity"></a>

A product, offer, and optional offer set associated with a purchase option.

## Contents
<a name="API_marketplace-discovery_PurchaseOptionAssociatedEntity_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** offer **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionAssociatedEntity-offer"></a>
Information about the offer associated with the purchase option.
Type: [OfferInformation](API_marketplace-discovery_OfferInformation.md) object
Required: Yes

 ** product **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionAssociatedEntity-product"></a>
Information about the product associated with the purchase option.
Type: [ProductInformation](API_marketplace-discovery_ProductInformation.md) object
Required: Yes

 ** offerSet **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PurchaseOptionAssociatedEntity-offerSet"></a>
Information about the offer set, if the purchase option is part of a bundled offer set.
Type: [OfferSetInformation](API_marketplace-discovery_OfferSetInformation.md) object
Required: No

## See Also
<a name="API_marketplace-discovery_PurchaseOptionAssociatedEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/PurchaseOptionAssociatedEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/PurchaseOptionAssociatedEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/PurchaseOptionAssociatedEntity)
