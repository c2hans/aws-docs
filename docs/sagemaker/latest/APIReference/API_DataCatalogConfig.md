---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DataCatalogConfig.html
---

# DataCatalogConfig
<a name="API_DataCatalogConfig"></a>

The meta data of the Glue table which serves as data catalog for the `OfflineStore`.

## Contents
<a name="API_DataCatalogConfig_Contents"></a>

 ** Catalog **   <a name="sagemaker-Type-DataCatalogConfig-Catalog"></a>
The name of the Glue table catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** Database **   <a name="sagemaker-Type-DataCatalogConfig-Database"></a>
The name of the Glue table database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** TableName **   <a name="sagemaker-Type-DataCatalogConfig-TableName"></a>
The name of the Glue table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## See Also
<a name="API_DataCatalogConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DataCatalogConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DataCatalogConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DataCatalogConfig)
