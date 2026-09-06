---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DataProductListingItem.html
---

# DataProductListingItem
<a name="API_DataProductListingItem"></a>

The asset of the data product listing.

## Contents
<a name="API_DataProductListingItem_Contents"></a>

 ** additionalAttributes **   <a name="datazone-Type-DataProductListingItem-additionalAttributes"></a>
The additional attributes of the asset of the data product.
Type: [DataProductListingItemAdditionalAttributes](API_DataProductListingItemAdditionalAttributes.md) object
Required: No

 ** createdAt **   <a name="datazone-Type-DataProductListingItem-createdAt"></a>
The timestamp at which the asset of the data product listing was created.
Type: Timestamp
Required: No

 ** description **   <a name="datazone-Type-DataProductListingItem-description"></a>
The description of the asset of the asset of the data product.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** entityId **   <a name="datazone-Type-DataProductListingItem-entityId"></a>
The entity ID of the asset of the asset of the data product.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** entityRevision **   <a name="datazone-Type-DataProductListingItem-entityRevision"></a>
The revision of the asset of the asset of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** glossaryTerms **   <a name="datazone-Type-DataProductListingItem-glossaryTerms"></a>
The glossary terms of the asset of the asset of the data product.
Type: Array of [DetailedGlossaryTerm](API_DetailedGlossaryTerm.md) objects
Required: No

 ** items **   <a name="datazone-Type-DataProductListingItem-items"></a>
The data of the asset of the data product.
Type: Array of [ListingSummaryItem](API_ListingSummaryItem.md) objects
Required: No

 ** listingCreatedBy **   <a name="datazone-Type-DataProductListingItem-listingCreatedBy"></a>
The timestamp at which the listing was created.
Type: String
Required: No

 ** listingId **   <a name="datazone-Type-DataProductListingItem-listingId"></a>
The ID of the listing.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** listingRevision **   <a name="datazone-Type-DataProductListingItem-listingRevision"></a>
The revision of the listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** listingUpdatedBy **   <a name="datazone-Type-DataProductListingItem-listingUpdatedBy"></a>
The user who updated the listing.
Type: String
Required: No

 ** name **   <a name="datazone-Type-DataProductListingItem-name"></a>
The name of the asset of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** owningProjectId **   <a name="datazone-Type-DataProductListingItem-owningProjectId"></a>
The ID of the owning project of the asset of the data product.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

## See Also
<a name="API_DataProductListingItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DataProductListingItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DataProductListingItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DataProductListingItem)
