---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_SubsidiaryAuthorizationFilters.html
---

# SubsidiaryAuthorizationFilters
<a name="API_SubsidiaryAuthorizationFilters"></a>

The filters that you can use with the `ListEntities` operation to filter subsidiary authorizations. You can filter by `EntityId`, `Status`, `ResourceId`, `ResourceName`, `Name`, `SubsidiaryAccountId`, `CreatedDate`, and `LastModifiedDate`. You can add only one wildcard filter in a single `ListEntities` request.

## Contents
<a name="API_SubsidiaryAuthorizationFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreatedDate **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationFilters-CreatedDate"></a>
A filter that matches subsidiary authorizations by creation date.
Type: [SubsidiaryAuthorizationCreatedDateFilter](API_SubsidiaryAuthorizationCreatedDateFilter.md) object
Required: No

 ** EntityId **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationFilters-EntityId"></a>
A filter that matches subsidiary authorizations by entity ID.
Type: [SubsidiaryAuthorizationEntityIdFilter](API_SubsidiaryAuthorizationEntityIdFilter.md) object
Required: No

 ** LastModifiedDate **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationFilters-LastModifiedDate"></a>
A filter that matches subsidiary authorizations by last modified date.
Type: [SubsidiaryAuthorizationLastModifiedDateFilter](API_SubsidiaryAuthorizationLastModifiedDateFilter.md) object
Required: No

 ** Name **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationFilters-Name"></a>
A filter that matches subsidiary authorizations by name.
Type: [SubsidiaryAuthorizationNameFilter](API_SubsidiaryAuthorizationNameFilter.md) object
Required: No

 ** ResourceId **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationFilters-ResourceId"></a>
A filter that matches subsidiary authorizations by the ID of the authorized resource.
Type: [SubsidiaryAuthorizationResourceIdFilter](API_SubsidiaryAuthorizationResourceIdFilter.md) object
Required: No

 ** ResourceName **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationFilters-ResourceName"></a>
A filter that matches subsidiary authorizations by the name of the authorized resource.
Type: [SubsidiaryAuthorizationResourceNameFilter](API_SubsidiaryAuthorizationResourceNameFilter.md) object
Required: No

 ** Status **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationFilters-Status"></a>
A filter that matches subsidiary authorizations by status.
Type: [SubsidiaryAuthorizationStatusFilter](API_SubsidiaryAuthorizationStatusFilter.md) object
Required: No

 ** SubsidiaryAccountId **   <a name="AWSMarketplaceService-Type-SubsidiaryAuthorizationFilters-SubsidiaryAccountId"></a>
A filter that matches subsidiary authorizations by the AWS account ID of the subsidiary account.
Type: [SubsidiaryAuthorizationSubsidiaryAccountIdFilter](API_SubsidiaryAuthorizationSubsidiaryAccountIdFilter.md) object
Required: No

## See Also
<a name="API_SubsidiaryAuthorizationFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/SubsidiaryAuthorizationFilters)
