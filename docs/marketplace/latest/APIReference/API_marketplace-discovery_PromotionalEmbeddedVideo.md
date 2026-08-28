---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PromotionalEmbeddedVideo.html
---

# PromotionalEmbeddedVideo
<a name="API_marketplace-discovery_PromotionalEmbeddedVideo"></a>

An embedded promotional video for a product.

## Contents
<a name="API_marketplace-discovery_PromotionalEmbeddedVideo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** preview **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PromotionalEmbeddedVideo-preview"></a>
The URL of the high-resolution preview image for the video.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`
Required: Yes

 ** thumbnail **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PromotionalEmbeddedVideo-thumbnail"></a>
The URL of the thumbnail image for the video.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`
Required: Yes

 ** title **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PromotionalEmbeddedVideo-title"></a>
The title displayed when hovering over the video.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** url **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PromotionalEmbeddedVideo-url"></a>
The URL of the video file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`
Required: Yes

 ** description **   <a name="AWSMarketplaceService-Type-marketplace-discovery_PromotionalEmbeddedVideo-description"></a>
An optional description of the video.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_marketplace-discovery_PromotionalEmbeddedVideo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/PromotionalEmbeddedVideo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/PromotionalEmbeddedVideo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/PromotionalEmbeddedVideo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
