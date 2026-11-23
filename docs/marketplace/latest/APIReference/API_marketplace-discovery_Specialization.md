---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_Specialization.html
---

# Specialization

A specialization earned for the listing, such as an AWS Competency.

## Contents
<a name="API_marketplace-discovery_Specialization_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** specializationId **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Specialization-specializationId"></a>
The unique identifier of the specialization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9\-]+`
Required: Yes

 ** specializationName **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Specialization-specializationName"></a>
The name of the specialization displayed to you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** specializationTypes **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Specialization-specializationTypes"></a>
The types that categorize this specialization.
Type: Array of [SpecializationTypeDetail](API_marketplace-discovery_SpecializationTypeDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Required: Yes

 ** caseStudyIds **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Specialization-caseStudyIds"></a>
The identifiers of the case studies that this specialization cites. Retrieve the case studies with the `CASE_STUDY` attribute type.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\w\-]+`
Required: No

 ** description **   <a name="AWSMarketplaceService-Type-marketplace-discovery_Specialization-description"></a>
A description of the specialization displayed to you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_marketplace-discovery_Specialization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/Specialization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/Specialization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/Specialization)
