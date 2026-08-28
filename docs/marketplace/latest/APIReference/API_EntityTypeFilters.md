---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_EntityTypeFilters.html
---

# EntityTypeFilters
<a name="API_EntityTypeFilters"></a>

Object containing all the filter fields per entity type.

## Contents
<a name="API_EntityTypeFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AmiProductFilters **   <a name="AWSMarketplaceService-Type-EntityTypeFilters-AmiProductFilters"></a>
A filter for AMI products.
Type: [AmiProductFilters](API_AmiProductFilters.md) object
Required: No

 ** ContainerProductFilters **   <a name="AWSMarketplaceService-Type-EntityTypeFilters-ContainerProductFilters"></a>
A filter for container products.
Type: [ContainerProductFilters](API_ContainerProductFilters.md) object
Required: No

 ** DataProductFilters **   <a name="AWSMarketplaceService-Type-EntityTypeFilters-DataProductFilters"></a>
A filter for data products.
Type: [DataProductFilters](API_DataProductFilters.md) object
Required: No

 ** MachineLearningProductFilters **   <a name="AWSMarketplaceService-Type-EntityTypeFilters-MachineLearningProductFilters"></a>
The filters that you can use with the ListEntities operation to filter machine learning products. You can filter by `EntityId`, `astModifiedDate`, `ProductTitle`, and `Visibility`.
Type: [MachineLearningProductFilters](API_MachineLearningProductFilters.md) object
Required: No

 ** OfferFilters **   <a name="AWSMarketplaceService-Type-EntityTypeFilters-OfferFilters"></a>
A filter for offers.
Type: [OfferFilters](API_OfferFilters.md) object
Required: No

 ** OfferSetFilters **   <a name="AWSMarketplaceService-Type-EntityTypeFilters-OfferSetFilters"></a>
A filter for offer sets.
Type: [OfferSetFilters](API_OfferSetFilters.md) object
Required: No

 ** ResaleAuthorizationFilters **   <a name="AWSMarketplaceService-Type-EntityTypeFilters-ResaleAuthorizationFilters"></a>
A filter for Resale Authorizations.
Type: [ResaleAuthorizationFilters](API_ResaleAuthorizationFilters.md) object
Required: No

 ** SaaSProductFilters **   <a name="AWSMarketplaceService-Type-EntityTypeFilters-SaaSProductFilters"></a>
A filter for SaaS products.
Type: [SaaSProductFilters](API_SaaSProductFilters.md) object
Required: No

## See Also
<a name="API_EntityTypeFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/EntityTypeFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/EntityTypeFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/EntityTypeFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
