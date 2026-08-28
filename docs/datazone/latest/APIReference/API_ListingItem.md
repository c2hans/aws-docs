---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListingItem.html
---

# ListingItem
<a name="API_ListingItem"></a>

The details of a listing (aka asset published in a Amazon DataZone catalog).

## Contents
<a name="API_ListingItem_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** assetListing **   <a name="datazone-Type-ListingItem-assetListing"></a>
An asset published in an Amazon DataZone catalog.
Type: [AssetListing](API_AssetListing.md) object
Required: No

 ** dataProductListing **   <a name="datazone-Type-ListingItem-dataProductListing"></a>
The data product listing.
Type: [DataProductListing](API_DataProductListing.md) object
Required: No

## See Also
<a name="API_ListingItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListingItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListingItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListingItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
