---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_TrustCenterSourceSummary.html
---

# TrustCenterSourceSummary

Summary information for a source of trust center information.

## Contents
<a name="API_marketplace-discovery_TrustCenterSourceSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** contentType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterSourceSummary-contentType"></a>
The format of the trust center source value.
Type: String
Valid Values: `EMAIL | PHONE_NUMBER | LINK | OTHER`
Required: Yes

 ** provider **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterSourceSummary-provider"></a>
The provider hosting the trust center.
Type: String
Valid Values: `DRATA | VANTA | OTHER`
Required: Yes

 ** value **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterSourceSummary-value"></a>
The URL of the trust center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterSourceSummary-displayName"></a>
The trust center provider name displayed to you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_marketplace-discovery_TrustCenterSourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/TrustCenterSourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/TrustCenterSourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/TrustCenterSourceSummary)
