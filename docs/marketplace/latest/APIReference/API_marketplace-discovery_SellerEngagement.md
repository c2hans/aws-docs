---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SellerEngagement.html
---

# SellerEngagement
<a name="API_marketplace-discovery_SellerEngagement"></a>

An engagement option available to potential buyers of a product, such as requesting a private offer or a demo.

## Contents
<a name="API_marketplace-discovery_SellerEngagement_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** contentType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SellerEngagement-contentType"></a>
The format of the engagement value, such as a URL.
Type: String
Valid Values: `LINK`
Required: Yes

 ** engagementType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SellerEngagement-engagementType"></a>
The type of engagement, such as `REQUEST_FOR_PRIVATE_OFFER` or `REQUEST_FOR_DEMO`.
Type: String
Valid Values: `REQUEST_FOR_PRIVATE_OFFER | REQUEST_FOR_DEMO`
Required: Yes

 ** value **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SellerEngagement-value"></a>
The engagement value, such as a URL to the engagement form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_marketplace-discovery_SellerEngagement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SellerEngagement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SellerEngagement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SellerEngagement)
