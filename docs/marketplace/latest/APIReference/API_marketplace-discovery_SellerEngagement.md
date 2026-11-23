---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SellerEngagement.html
---

# SellerEngagement

A way you can engage with the seller of a product, such as requesting a private offer or a demo.

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
The type of engagement. This field has one of the following values:
BUY\_NOW
The product is available for immediate purchase.
EXPRESS\_PRIVATE\_OFFER
You can request an express private offer and accept it immediately.
REQUEST\_FOR\_DEMO
You can request a demo from the seller.
REQUEST\_FOR\_PRIVATE\_OFFER
You can request a private offer from the seller.
TRY\_FOR\_FREE
The product offers a free trial.
Type: String
Valid Values: `REQUEST_FOR_PRIVATE_OFFER | REQUEST_FOR_DEMO | EXPRESS_PRIVATE_OFFER | BUY_NOW | TRY_FOR_FREE`
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
