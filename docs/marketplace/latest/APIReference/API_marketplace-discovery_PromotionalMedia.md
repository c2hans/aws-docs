---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PromotionalMedia.html
---

# PromotionalMedia
<a name="API_marketplace-discovery_PromotionalMedia"></a>

Embedded promotional media for a product, such as images or videos. Each element contains exactly one media type.

## Contents
<a name="API_marketplace-discovery_PromotionalMedia_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** embeddedImage **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PromotionalMedia-embeddedImage"></a>
An embedded promotional image for a product.
Type: [PromotionalEmbeddedImage](API_marketplace-discovery_PromotionalEmbeddedImage.md) object
Required: No

 ** embeddedVideo **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PromotionalMedia-embeddedVideo"></a>
An embedded promotional video for a product.
Type: [PromotionalEmbeddedVideo](API_marketplace-discovery_PromotionalEmbeddedVideo.md) object
Required: No

## See Also
<a name="API_marketplace-discovery_PromotionalMedia_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/PromotionalMedia)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/PromotionalMedia)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/PromotionalMedia)
