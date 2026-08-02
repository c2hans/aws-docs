---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SAPODataSourceProperties.html
---

# SAPODataSourceProperties
<a name="API_SAPODataSourceProperties"></a>

 The properties that are applied when using SAPOData as a flow source.

## Contents
<a name="API_SAPODataSourceProperties_Contents"></a>

 ** objectPath **   <a name="appflow-Type-SAPODataSourceProperties-objectPath"></a>
 The object path specified in the SAPOData flow source.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

 ** paginationConfig **   <a name="appflow-Type-SAPODataSourceProperties-paginationConfig"></a>
Sets the page size for each concurrent process that transfers OData records from your SAP instance.
Type: [SAPODataPaginationConfig](API_SAPODataPaginationConfig.md) object
Required: No

 ** parallelismConfig **   <a name="appflow-Type-SAPODataSourceProperties-parallelismConfig"></a>
Sets the number of concurrent processes that transfers OData records from your SAP instance.
Type: [SAPODataParallelismConfig](API_SAPODataParallelismConfig.md) object
Required: No

## See Also
<a name="API_SAPODataSourceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/SAPODataSourceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/SAPODataSourceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/SAPODataSourceProperties)
