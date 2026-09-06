---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ResaleAuthorizationFilters.html
---

# ResaleAuthorizationFilters
<a name="API_ResaleAuthorizationFilters"></a>

Object containing all the filter fields for resale authorization entity. Client can add only one wildcard filter and a maximum of 8 filters in a single `ListEntities` request.

## Contents
<a name="API_ResaleAuthorizationFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AvailabilityEndDate **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-AvailabilityEndDate"></a>
Allows filtering on the `AvailabilityEndDate` of a ResaleAuthorization.
Type: [ResaleAuthorizationAvailabilityEndDateFilter](API_ResaleAuthorizationAvailabilityEndDateFilter.md) object
Required: No

 ** CreatedDate **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-CreatedDate"></a>
Allows filtering on the `CreatedDate` of a ResaleAuthorization.
Type: [ResaleAuthorizationCreatedDateFilter](API_ResaleAuthorizationCreatedDateFilter.md) object
Required: No

 ** EntityId **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-EntityId"></a>
Allows filtering on the `EntityId` of a ResaleAuthorization.
Type: [ResaleAuthorizationEntityIdFilter](API_ResaleAuthorizationEntityIdFilter.md) object
Required: No

 ** LastModifiedDate **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-LastModifiedDate"></a>
Allows filtering on the `LastModifiedDate` of a ResaleAuthorization.
Type: [ResaleAuthorizationLastModifiedDateFilter](API_ResaleAuthorizationLastModifiedDateFilter.md) object
Required: No

 ** ManufacturerAccountId **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-ManufacturerAccountId"></a>
Allows filtering on the `ManufacturerAccountId` of a ResaleAuthorization.
Type: [ResaleAuthorizationManufacturerAccountIdFilter](API_ResaleAuthorizationManufacturerAccountIdFilter.md) object
Required: No

 ** ManufacturerLegalName **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-ManufacturerLegalName"></a>
Allows filtering on the `ManufacturerLegalName` of a ResaleAuthorization.
Type: [ResaleAuthorizationManufacturerLegalNameFilter](API_ResaleAuthorizationManufacturerLegalNameFilter.md) object
Required: No

 ** Name **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-Name"></a>
Allows filtering on the `Name` of a ResaleAuthorization.
Type: [ResaleAuthorizationNameFilter](API_ResaleAuthorizationNameFilter.md) object
Required: No

 ** OfferExtendedStatus **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-OfferExtendedStatus"></a>
Allows filtering on the `OfferExtendedStatus` of a ResaleAuthorization.
Type: [ResaleAuthorizationOfferExtendedStatusFilter](API_ResaleAuthorizationOfferExtendedStatusFilter.md) object
Required: No

 ** ProductId **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-ProductId"></a>
Allows filtering on the `ProductId` of a ResaleAuthorization.
Type: [ResaleAuthorizationProductIdFilter](API_ResaleAuthorizationProductIdFilter.md) object
Required: No

 ** ProductName **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-ProductName"></a>
Allows filtering on the `ProductName` of a ResaleAuthorization.
Type: [ResaleAuthorizationProductNameFilter](API_ResaleAuthorizationProductNameFilter.md) object
Required: No

 ** ResellerAccountID **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-ResellerAccountID"></a>
Allows filtering on the `ResellerAccountID` of a ResaleAuthorization.
Type: [ResaleAuthorizationResellerAccountIDFilter](API_ResaleAuthorizationResellerAccountIDFilter.md) object
Required: No

 ** ResellerLegalName **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-ResellerLegalName"></a>
Allows filtering on the `ResellerLegalName` of a ResaleAuthorization.
Type: [ResaleAuthorizationResellerLegalNameFilter](API_ResaleAuthorizationResellerLegalNameFilter.md) object
Required: No

 ** ResellerRole **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-ResellerRole"></a>
Allows filtering on the `ResellerRole` of a ResaleAuthorization.
Type: [ResaleAuthorizationResellerRoleFilter](API_ResaleAuthorizationResellerRoleFilter.md) object
Required: No

 ** Status **   <a name="AWSMarketplaceService-Type-ResaleAuthorizationFilters-Status"></a>
Allows filtering on the `Status` of a ResaleAuthorization.
Type: [ResaleAuthorizationStatusFilter](API_ResaleAuthorizationStatusFilter.md) object
Required: No

## See Also
<a name="API_ResaleAuthorizationFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ResaleAuthorizationFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ResaleAuthorizationFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ResaleAuthorizationFilters)
