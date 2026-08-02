---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SubscribedProductListing.html
---

# SubscribedProductListing
<a name="API_SubscribedProductListing"></a>

The data product listing.

## Contents
<a name="API_SubscribedProductListing_Contents"></a>

 ** assetListings **   <a name="datazone-Type-SubscribedProductListing-assetListings"></a>
The data assets of the data product listing.
Type: Array of [AssetInDataProductListingItem](API_AssetInDataProductListingItem.md) objects
Required: No

 ** description **   <a name="datazone-Type-SubscribedProductListing-description"></a>
The description of the data product listing.
Type: String
Required: No

 ** entityId **   <a name="datazone-Type-SubscribedProductListing-entityId"></a>
The ID of the data product listing.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** entityRevision **   <a name="datazone-Type-SubscribedProductListing-entityRevision"></a>
The revision of the data product listing.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** glossaryTerms **   <a name="datazone-Type-SubscribedProductListing-glossaryTerms"></a>
The glossary terms of the data product listing.
Type: Array of [DetailedGlossaryTerm](API_DetailedGlossaryTerm.md) objects
Required: No

 ** name **   <a name="datazone-Type-SubscribedProductListing-name"></a>
The name of the data product listing.
Type: String
Required: No

## See Also
<a name="API_SubscribedProductListing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SubscribedProductListing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SubscribedProductListing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SubscribedProductListing)
