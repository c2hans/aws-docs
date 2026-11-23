---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_TrustCenterDocumentAttribute.html
---

# TrustCenterDocumentAttribute

A trust center document associated with a listing.

## Contents
<a name="API_marketplace-discovery_TrustCenterDocumentAttribute_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** accessType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterDocumentAttribute-accessType"></a>
How the document can be accessed.
Type: String
Valid Values: `DOWNLOAD | VIEW | REQUEST_ACCESS`
Required: Yes

 ** contentType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterDocumentAttribute-contentType"></a>
The format of the document resource value.
Type: String
Valid Values: `EMAIL | PHONE_NUMBER | LINK | OTHER`
Required: Yes

 ** value **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterDocumentAttribute-value"></a>
The URL used to download, view, or request access to the document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterDocumentAttribute-displayName"></a>
The document name displayed to you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** subjectArea **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterDocumentAttribute-subjectArea"></a>
The subject area of the document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_marketplace-discovery_TrustCenterDocumentAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/TrustCenterDocumentAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/TrustCenterDocumentAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/TrustCenterDocumentAttribute)
