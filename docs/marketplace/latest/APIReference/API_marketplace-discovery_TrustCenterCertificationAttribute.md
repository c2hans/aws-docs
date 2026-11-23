---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_TrustCenterCertificationAttribute.html
---

# TrustCenterCertificationAttribute

A trust center certification associated with a listing.

## Contents
<a name="API_marketplace-discovery_TrustCenterCertificationAttribute_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** certificationType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterCertificationAttribute-certificationType"></a>
The certification type. The set of values is open and can include provider-defined certifications.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterCertificationAttribute-displayName"></a>
The authoritative certification name displayed to you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** logoUrl **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterCertificationAttribute-logoUrl"></a>
The URL of the certification logo.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`
Required: Yes

## See Also
<a name="API_marketplace-discovery_TrustCenterCertificationAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/TrustCenterCertificationAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/TrustCenterCertificationAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/TrustCenterCertificationAttribute)
