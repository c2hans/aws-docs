---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SearchInventoryResultItem.html
---

# SearchInventoryResultItem
<a name="API_SearchInventoryResultItem"></a>

The details of the search results.

## Contents
<a name="API_SearchInventoryResultItem_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** assetItem **   <a name="datazone-Type-SearchInventoryResultItem-assetItem"></a>
The asset item included in the search results.
Type: [AssetItem](API_AssetItem.md) object
Required: No

 ** dataProductItem **   <a name="datazone-Type-SearchInventoryResultItem-dataProductItem"></a>
The data product.
Type: [DataProductResultItem](API_DataProductResultItem.md) object
Required: No

 ** glossaryItem **   <a name="datazone-Type-SearchInventoryResultItem-glossaryItem"></a>
The glossary item included in the search results.
Type: [GlossaryItem](API_GlossaryItem.md) object
Required: No

 ** glossaryTermItem **   <a name="datazone-Type-SearchInventoryResultItem-glossaryTermItem"></a>
The glossary term item included in the search results.
Type: [GlossaryTermItem](API_GlossaryTermItem.md) object
Required: No

## See Also
<a name="API_SearchInventoryResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SearchInventoryResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SearchInventoryResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SearchInventoryResultItem)
