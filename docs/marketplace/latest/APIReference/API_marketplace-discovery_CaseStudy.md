---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_CaseStudy.html
---

# CaseStudy

A case study associated with a listing.

## Contents
<a name="API_marketplace-discovery_CaseStudy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** caseStudyId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudy-caseStudyId"></a>
The unique identifier of the case study.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: Yes

 ** caseStudyName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudy-caseStudyName"></a>
The case study name displayed to you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** shortDescription **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudy-shortDescription"></a>
A brief value proposition for the case study.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** challenge **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudy-challenge"></a>
The business challenge that the engagement addresses.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5000.
Required: No

 ** engagementDates **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudy-engagementDates"></a>
The key implementation dates for the engagement.
Type: [EngagementDates](API_marketplace-discovery_EngagementDates.md) object
Required: No

 ** implementationApproach **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudy-implementationApproach"></a>
The implementation approach used for the engagement.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5000.
Required: No

 ** outcome **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudy-outcome"></a>
The results and outcomes achieved by the engagement.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3000.
Required: No

 ** resolution **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudy-resolution"></a>
How the partner resolved the challenge.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 5000.
Required: No

 ** resources **   <a name="AWSMarketplaceService-Type-marketplace-discovery_CaseStudy-resources"></a>
Resources related to the case study.
Type: Array of [CaseStudyResource](API_marketplace-discovery_CaseStudyResource.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_marketplace-discovery_CaseStudy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/CaseStudy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/CaseStudy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/CaseStudy)
