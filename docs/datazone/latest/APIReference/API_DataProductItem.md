---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DataProductItem.html
---

# DataProductItem
<a name="API_DataProductItem"></a>

The data product.

## Contents
<a name="API_DataProductItem_Contents"></a>

 ** identifier **   <a name="datazone-Type-DataProductItem-identifier"></a>
The ID of the data product.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** itemType **   <a name="datazone-Type-DataProductItem-itemType"></a>
The type of the data product.
Type: String
Valid Values: `ASSET`
Required: Yes

 ** glossaryTerms **   <a name="datazone-Type-DataProductItem-glossaryTerms"></a>
The glossary terms of the data product.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** revision **   <a name="datazone-Type-DataProductItem-revision"></a>
The revision of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_DataProductItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DataProductItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DataProductItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DataProductItem)
