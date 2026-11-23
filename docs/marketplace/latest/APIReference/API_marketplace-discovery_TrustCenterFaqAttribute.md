---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_TrustCenterFaqAttribute.html
---

# TrustCenterFaqAttribute

A frequently asked question that a trust center publishes.

## Contents
<a name="API_marketplace-discovery_TrustCenterFaqAttribute_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** answer **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterFaqAttribute-answer"></a>
The answer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** question **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterFaqAttribute-question"></a>
The question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** subjectArea **   <a name="AWSMarketplaceService-Type-marketplace-discovery_TrustCenterFaqAttribute-subjectArea"></a>
The subject area of the question.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_marketplace-discovery_TrustCenterFaqAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/TrustCenterFaqAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/TrustCenterFaqAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/TrustCenterFaqAttribute)
