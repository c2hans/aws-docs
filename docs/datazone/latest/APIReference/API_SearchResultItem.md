---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SearchResultItem.html
---

# SearchResultItem
<a name="API_SearchResultItem"></a>

The details of the results of the `SearchListings` action.

## Contents
<a name="API_SearchResultItem_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** assetListing **   <a name="datazone-Type-SearchResultItem-assetListing"></a>
The asset listing included in the results of the `SearchListings` action.
Type: [AssetListingItem](API_AssetListingItem.md) object
Required: No

 ** dataProductListing **   <a name="datazone-Type-SearchResultItem-dataProductListing"></a>
The data product listing.
Type: [DataProductListingItem](API_DataProductListingItem.md) object
Required: No

## See Also
<a name="API_SearchResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SearchResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SearchResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SearchResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
