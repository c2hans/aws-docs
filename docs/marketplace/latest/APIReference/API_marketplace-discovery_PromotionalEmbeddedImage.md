---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PromotionalEmbeddedImage.html
---

# PromotionalEmbeddedImage
<a name="API_marketplace-discovery_PromotionalEmbeddedImage"></a>

An embedded promotional image for a product.

## Contents
<a name="API_marketplace-discovery_PromotionalEmbeddedImage_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** title **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PromotionalEmbeddedImage-title"></a>
The title displayed when hovering over the image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** url **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PromotionalEmbeddedImage-url"></a>
The URL of the image file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`
Required: Yes

 ** description **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PromotionalEmbeddedImage-description"></a>
An optional description of the image.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_marketplace-discovery_PromotionalEmbeddedImage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/PromotionalEmbeddedImage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/PromotionalEmbeddedImage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/PromotionalEmbeddedImage)
