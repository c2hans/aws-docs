---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_OfferSetFilters.html
---

# OfferSetFilters
<a name="API_OfferSetFilters"></a>

Object containing all the filter fields for offer sets entity. Client can add a maximum of 8 filters in a single `ListEntities` request.

## Contents
<a name="API_OfferSetFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AssociatedOfferIds **   <a name="AWSMarketplaceService-Type-OfferSetFilters-AssociatedOfferIds"></a>
Allows filtering on the `AssociatedOfferIds` of an offer set.
Type: [OfferSetAssociatedOfferIdsFilter](API_OfferSetAssociatedOfferIdsFilter.md) object
Required: No

 ** EntityId **   <a name="AWSMarketplaceService-Type-OfferSetFilters-EntityId"></a>
Allows filtering on `EntityId` of an offer set.
Type: [OfferSetEntityIdFilter](API_OfferSetEntityIdFilter.md) object
Required: No

 ** LastModifiedDate **   <a name="AWSMarketplaceService-Type-OfferSetFilters-LastModifiedDate"></a>
Allows filtering on the `LastModifiedDate` of an offer set.
Type: [OfferSetLastModifiedDateFilter](API_OfferSetLastModifiedDateFilter.md) object
Required: No

 ** Name **   <a name="AWSMarketplaceService-Type-OfferSetFilters-Name"></a>
Allows filtering on the `Name` of an offer set.
Type: [OfferSetNameFilter](API_OfferSetNameFilter.md) object
Required: No

 ** ReleaseDate **   <a name="AWSMarketplaceService-Type-OfferSetFilters-ReleaseDate"></a>
Allows filtering on the `ReleaseDate` of an offer set.
Type: [OfferSetReleaseDateFilter](API_OfferSetReleaseDateFilter.md) object
Required: No

 ** SolutionId **   <a name="AWSMarketplaceService-Type-OfferSetFilters-SolutionId"></a>
Allows filtering on the `SolutionId` of an offer set.
Type: [OfferSetSolutionIdFilter](API_OfferSetSolutionIdFilter.md) object
Required: No

 ** State **   <a name="AWSMarketplaceService-Type-OfferSetFilters-State"></a>
Allows filtering on the `State` of an offer set.
Type: [OfferSetStateFilter](API_OfferSetStateFilter.md) object
Required: No

## See Also
<a name="API_OfferSetFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/OfferSetFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/OfferSetFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/OfferSetFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
