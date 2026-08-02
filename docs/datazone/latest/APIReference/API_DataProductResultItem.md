---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DataProductResultItem.html
---

# DataProductResultItem
<a name="API_DataProductResultItem"></a>

The data product.

## Contents
<a name="API_DataProductResultItem_Contents"></a>

 ** domainId **   <a name="datazone-Type-DataProductResultItem-domainId"></a>
The ID of the domain where the data product lives.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** id **   <a name="datazone-Type-DataProductResultItem-id"></a>
The ID of the data product.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** name **   <a name="datazone-Type-DataProductResultItem-name"></a>
The name of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** owningProjectId **   <a name="datazone-Type-DataProductResultItem-owningProjectId"></a>
The ID of the owning project of the data product.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** additionalAttributes **   <a name="datazone-Type-DataProductResultItem-additionalAttributes"></a>
The additional attributes of an Amazon DataZone data product.
Type: [DataProductItemAdditionalAttributes](API_DataProductItemAdditionalAttributes.md) object
Required: No

 ** createdAt **   <a name="datazone-Type-DataProductResultItem-createdAt"></a>
The timestamp at which the data product was created.
Type: Timestamp
Required: No

 ** createdBy **   <a name="datazone-Type-DataProductResultItem-createdBy"></a>
The user who created the data product.
Type: String
Required: No

 ** description **   <a name="datazone-Type-DataProductResultItem-description"></a>
The description of the data product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** firstRevisionCreatedAt **   <a name="datazone-Type-DataProductResultItem-firstRevisionCreatedAt"></a>
The timestamp at which first revision of the data product was created.
Type: Timestamp
Required: No

 ** firstRevisionCreatedBy **   <a name="datazone-Type-DataProductResultItem-firstRevisionCreatedBy"></a>
The user who created the first revision of the data product.
Type: String
Required: No

 ** glossaryTerms **   <a name="datazone-Type-DataProductResultItem-glossaryTerms"></a>
The glossary terms of the data product.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

## See Also
<a name="API_DataProductResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DataProductResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DataProductResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DataProductResultItem)
