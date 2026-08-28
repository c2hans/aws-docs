---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetListingItem.html
---

# AssetListingItem
<a name="API_AssetListingItem"></a>

The details of an asset published in an Amazon DataZone catalog.

## Contents
<a name="API_AssetListingItem_Contents"></a>

 ** additionalAttributes **   <a name="datazone-Type-AssetListingItem-additionalAttributes"></a>
The additional attributes of an asset published in an Amazon DataZone catalog.
Type: [AssetListingItemAdditionalAttributes](API_AssetListingItemAdditionalAttributes.md) object
Required: No

 ** createdAt **   <a name="datazone-Type-AssetListingItem-createdAt"></a>
The timestamp of when an asset published in an Amazon DataZone catalog was created.
Type: Timestamp
Required: No

 ** description **   <a name="datazone-Type-AssetListingItem-description"></a>
The description of an asset published in an Amazon DataZone catalog.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** entityId **   <a name="datazone-Type-AssetListingItem-entityId"></a>
The identifier of the inventory asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** entityRevision **   <a name="datazone-Type-AssetListingItem-entityRevision"></a>
The revision of the inventory asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** entityType **   <a name="datazone-Type-AssetListingItem-entityType"></a>
The type of the inventory asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\.]*.*`
Required: No

 ** glossaryTerms **   <a name="datazone-Type-AssetListingItem-glossaryTerms"></a>
Glossary terms attached to the inventory asset.
Type: Array of [DetailedGlossaryTerm](API_DetailedGlossaryTerm.md) objects
Required: No

 ** governedGlossaryTerms **   <a name="datazone-Type-AssetListingItem-governedGlossaryTerms"></a>
The restricted glossary terms associated with an asset.
Type: Array of [DetailedGlossaryTerm](API_DetailedGlossaryTerm.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** listingCreatedBy **   <a name="datazone-Type-AssetListingItem-listingCreatedBy"></a>
The Amazon DataZone user who created the listing.
Type: String
Required: No

 ** listingId **   <a name="datazone-Type-AssetListingItem-listingId"></a>
The identifier of the listing (asset published in Amazon DataZone catalog).
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** listingRevision **   <a name="datazone-Type-AssetListingItem-listingRevision"></a>
The revision of the listing (asset published in Amazon DataZone catalog).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** listingUpdatedBy **   <a name="datazone-Type-AssetListingItem-listingUpdatedBy"></a>
The Amazon DataZone user who updated the listing.
Type: String
Required: No

 ** name **   <a name="datazone-Type-AssetListingItem-name"></a>
The name of the inventory asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** owningProjectId **   <a name="datazone-Type-AssetListingItem-owningProjectId"></a>
The identifier of the project that owns the inventory asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

## See Also
<a name="API_AssetListingItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetListingItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetListingItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetListingItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
