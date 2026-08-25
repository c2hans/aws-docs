---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_OfferFilters.html
---

# OfferFilters
<a name="API_OfferFilters"></a>

Object containing all the filter fields for offers entity. Client can add only one wildcard filter and a maximum of 8 filters in a single `ListEntities` request.

## Contents
<a name="API_OfferFilters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AvailabilityEndDate **   <a name="AWSMarketplaceService-Type-OfferFilters-AvailabilityEndDate"></a>
Allows filtering on the `AvailabilityEndDate` of an offer.
Type: [OfferAvailabilityEndDateFilter](API_OfferAvailabilityEndDateFilter.md) object
Required: No

 ** BuyerAccounts **   <a name="AWSMarketplaceService-Type-OfferFilters-BuyerAccounts"></a>
Allows filtering on the `BuyerAccounts` of an offer.
Type: [OfferBuyerAccountsFilter](API_OfferBuyerAccountsFilter.md) object
Required: No

 ** CreatedBySource **   <a name="AWSMarketplaceService-Type-OfferFilters-CreatedBySource"></a>
Allows filtering on the `CreatedBySource` of an offer.
Type: [OfferCreatedBySourceFilter](API_OfferCreatedBySourceFilter.md) object
Required: No

 ** EntityId **   <a name="AWSMarketplaceService-Type-OfferFilters-EntityId"></a>
Allows filtering on `EntityId` of an offer.
Type: [OfferEntityIdFilter](API_OfferEntityIdFilter.md) object
Required: No

 ** LastModifiedDate **   <a name="AWSMarketplaceService-Type-OfferFilters-LastModifiedDate"></a>
Allows filtering on the `LastModifiedDate` of an offer.
Type: [OfferLastModifiedDateFilter](API_OfferLastModifiedDateFilter.md) object
Required: No

 ** Name **   <a name="AWSMarketplaceService-Type-OfferFilters-Name"></a>
Allows filtering on the `Name` of an offer.
Type: [OfferNameFilter](API_OfferNameFilter.md) object
Required: No

 ** OfferSetId **   <a name="AWSMarketplaceService-Type-OfferFilters-OfferSetId"></a>
Allows filtering on the `OfferSetId` of an offer.
Type: [OfferSetIdFilter](API_OfferSetIdFilter.md) object
Required: No

 ** ProductId **   <a name="AWSMarketplaceService-Type-OfferFilters-ProductId"></a>
Allows filtering on the `ProductId` of an offer.
Type: [OfferProductIdFilter](API_OfferProductIdFilter.md) object
Required: No

 ** ReleaseDate **   <a name="AWSMarketplaceService-Type-OfferFilters-ReleaseDate"></a>
Allows filtering on the `ReleaseDate` of an offer.
Type: [OfferReleaseDateFilter](API_OfferReleaseDateFilter.md) object
Required: No

 ** ResaleAuthorizationId **   <a name="AWSMarketplaceService-Type-OfferFilters-ResaleAuthorizationId"></a>
Allows filtering on the `ResaleAuthorizationId` of an offer.
Not all offers have a `ResaleAuthorizationId`. The response will only include offers for which you have permissions.
Type: [OfferResaleAuthorizationIdFilter](API_OfferResaleAuthorizationIdFilter.md) object
Required: No

 ** State **   <a name="AWSMarketplaceService-Type-OfferFilters-State"></a>
Allows filtering on the `State` of an offer.
Type: [OfferStateFilter](API_OfferStateFilter.md) object
Required: No

 ** TargetAgreementId **   <a name="AWSMarketplaceService-Type-OfferFilters-TargetAgreementId"></a>
Allows filtering on the `TargetAgreementId` of an offer.
Type: [OfferTargetAgreementIdFilter](API_OfferTargetAgreementIdFilter.md) object
Required: No

 ** TargetAgreementIntent **   <a name="AWSMarketplaceService-Type-OfferFilters-TargetAgreementIntent"></a>
Allows filtering on the `TargetAgreementIntent` of an offer.
Type: [OfferTargetAgreementIntentFilter](API_OfferTargetAgreementIntentFilter.md) object
Required: No

 ** Targeting **   <a name="AWSMarketplaceService-Type-OfferFilters-Targeting"></a>
Allows filtering on the `Targeting` of an offer.
Type: [OfferTargetingFilter](API_OfferTargetingFilter.md) object
Required: No

## See Also
<a name="API_OfferFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/OfferFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/OfferFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/OfferFilters)
