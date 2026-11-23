---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListingAttributeResults.html
---

# ListingAttributeResults

An attribute associated with a listing. Each entry contains one attribute type.

## Contents
<a name="API_marketplace-discovery_ListingAttributeResults_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** caseStudy **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingAttributeResults-caseStudy"></a>
A case study associated with the listing.
Type: [CaseStudy](API_marketplace-discovery_CaseStudy.md) object
Required: No

 ** specializationDetail **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingAttributeResults-specializationDetail"></a>
A specialization earned for the listing. Each result is either a specialization or a category under a specialization.
Type: [SpecializationDetail](API_marketplace-discovery_SpecializationDetail.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** trustCenterCertification **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingAttributeResults-trustCenterCertification"></a>
A trust center certification associated with the listing.
Type: [TrustCenterCertificationAttribute](API_marketplace-discovery_TrustCenterCertificationAttribute.md) object
Required: No

 ** trustCenterControl **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingAttributeResults-trustCenterControl"></a>
A trust center control associated with the listing.
Type: [TrustCenterControl](API_marketplace-discovery_TrustCenterControl.md) object
Required: No

 ** trustCenterDocument **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingAttributeResults-trustCenterDocument"></a>
A trust center document associated with the listing.
Type: [TrustCenterDocumentAttribute](API_marketplace-discovery_TrustCenterDocumentAttribute.md) object
Required: No

 ** trustCenterFaq **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingAttributeResults-trustCenterFaq"></a>
A trust center frequently asked question associated with the listing.
Type: [TrustCenterFaqAttribute](API_marketplace-discovery_TrustCenterFaqAttribute.md) object
Required: No

 ** trustCenterSource **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingAttributeResults-trustCenterSource"></a>
A trust center source associated with the listing.
Type: [TrustCenterSource](API_marketplace-discovery_TrustCenterSource.md) object
Required: No

 ** trustCenterUpdate **   <a name="AWSMarketplaceService-Type-marketplace-discovery_ListingAttributeResults-trustCenterUpdate"></a>
A trust center update associated with the listing.
Type: [TrustCenterUpdateAttribute](API_marketplace-discovery_TrustCenterUpdateAttribute.md) object
Required: No

## See Also
<a name="API_marketplace-discovery_ListingAttributeResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-discovery-2026-02-05/ListingAttributeResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-discovery-2026-02-05/ListingAttributeResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-discovery-2026-02-05/ListingAttributeResults)
