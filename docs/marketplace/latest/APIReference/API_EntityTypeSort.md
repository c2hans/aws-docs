---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_EntityTypeSort.html
---

# EntityTypeSort
<a name="API_EntityTypeSort"></a>

Object containing all the sort fields per entity type.

## Contents
<a name="API_EntityTypeSort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AmiProductSort **   <a name="AWSMarketplaceService-Type-EntityTypeSort-AmiProductSort"></a>
A sort for AMI products.
Type: [AmiProductSort](API_AmiProductSort.md) object
Required: No

 ** ContainerProductSort **   <a name="AWSMarketplaceService-Type-EntityTypeSort-ContainerProductSort"></a>
A sort for container products.
Type: [ContainerProductSort](API_ContainerProductSort.md) object
Required: No

 ** DataProductSort **   <a name="AWSMarketplaceService-Type-EntityTypeSort-DataProductSort"></a>
A sort for data products.
Type: [DataProductSort](API_DataProductSort.md) object
Required: No

 ** MachineLearningProductSort **   <a name="AWSMarketplaceService-Type-EntityTypeSort-MachineLearningProductSort"></a>
The sort options for machine learning products.
Type: [MachineLearningProductSort](API_MachineLearningProductSort.md) object
Required: No

 ** OfferSetSort **   <a name="AWSMarketplaceService-Type-EntityTypeSort-OfferSetSort"></a>
A sort for offer sets.
Type: [OfferSetSort](API_OfferSetSort.md) object
Required: No

 ** OfferSort **   <a name="AWSMarketplaceService-Type-EntityTypeSort-OfferSort"></a>
A sort for offers.
Type: [OfferSort](API_OfferSort.md) object
Required: No

 ** ResaleAuthorizationSort **   <a name="AWSMarketplaceService-Type-EntityTypeSort-ResaleAuthorizationSort"></a>
A sort for Resale Authorizations.
Type: [ResaleAuthorizationSort](API_ResaleAuthorizationSort.md) object
Required: No

 ** SaaSProductSort **   <a name="AWSMarketplaceService-Type-EntityTypeSort-SaaSProductSort"></a>
A sort for SaaS products.
Type: [SaaSProductSort](API_SaaSProductSort.md) object
Required: No

## See Also
<a name="API_EntityTypeSort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/EntityTypeSort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/EntityTypeSort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/EntityTypeSort)
