---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SpecializationDetail.html
---

# SpecializationDetail

A specialization result for a listing. Exactly one member is set: a specialization or a category under one.

## Contents
<a name="API_marketplace-discovery_SpecializationDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** specialization **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SpecializationDetail-specialization"></a>
A specialization earned for the listing.
Type: [Specialization](API_marketplace-discovery_Specialization.md) object
Required: No

 ** specializationCategory **   <a name="AWSMarketplaceService-Type-marketplace-discovery_SpecializationDetail-specializationCategory"></a>
A category under a specialization that the listing earned.
Type: [SpecializationCategory](API_marketplace-discovery_SpecializationCategory.md) object
Required: No

## See Also
<a name="API_marketplace-discovery_SpecializationDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/SpecializationDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/SpecializationDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/SpecializationDetail)
