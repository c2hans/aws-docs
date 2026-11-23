---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_TrustCenterCertificationSummary.html
---

# TrustCenterCertificationSummary

Summary information for a certification associated with a listing.

## Contents
<a name="API_marketplace-discovery_TrustCenterCertificationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** certificationType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterCertificationSummary-certificationType"></a>
The certification type. The set of values is open and can include provider-defined certifications.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterCertificationSummary-displayName"></a>
The certification name displayed to you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** logoUrl **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterCertificationSummary-logoUrl"></a>
The URL of the certification logo.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `https?://.*`
Required: Yes

## See Also
<a name="API_marketplace-discovery_TrustCenterCertificationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/TrustCenterCertificationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/TrustCenterCertificationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/TrustCenterCertificationSummary)
