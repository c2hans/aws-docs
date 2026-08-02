---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DDBELTCatalogAdditionalOptions.html
---

# DDBELTCatalogAdditionalOptions
<a name="API_DDBELTCatalogAdditionalOptions"></a>

Specifies additional options for DynamoDB ELT catalog operations.

## Contents
<a name="API_DDBELTCatalogAdditionalOptions_Contents"></a>

 ** DynamodbExport **   <a name="Glue-Type-DDBELTCatalogAdditionalOptions-DynamodbExport"></a>
Specifies the DynamoDB export configuration for the ELT operation.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** DynamodbUnnestDDBJson **   <a name="Glue-Type-DDBELTCatalogAdditionalOptions-DynamodbUnnestDDBJson"></a>
Specifies whether to unnest DynamoDB JSON format. When set to `true`, nested JSON structures in DynamoDB items are flattened.
Type: Boolean
Required: No

## See Also
<a name="API_DDBELTCatalogAdditionalOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DDBELTCatalogAdditionalOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DDBELTCatalogAdditionalOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DDBELTCatalogAdditionalOptions)
