---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_CaseStudyResource.html
---

# CaseStudyResource

A resource that a case study cites, such as supporting documentation or a web page.

## Contents
<a name="API_marketplace-discovery_CaseStudyResource_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** contentType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudyResource-contentType"></a>
The format of the resource value.
Type: String
Valid Values: `EMAIL | PHONE_NUMBER | LINK | OTHER`
Required: Yes

 ** resourceType **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudyResource-resourceType"></a>
The type of case study resource.
Type: String
Valid Values: `CASE_STUDY_WEBSITE`
Required: Yes

 ** value **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudyResource-value"></a>
The resource value, such as a URL.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: Yes

 ** displayName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudyResource-displayName"></a>
The resource name displayed to you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_marketplace-discovery_CaseStudyResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/CaseStudyResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/CaseStudyResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/CaseStudyResource)
