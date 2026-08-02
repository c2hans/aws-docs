---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CatalogPropertiesOutput.html
---

# CatalogPropertiesOutput
<a name="API_CatalogPropertiesOutput"></a>

Property attributes that include configuration properties for the catalog resource.

## Contents
<a name="API_CatalogPropertiesOutput_Contents"></a>

 ** CustomProperties **   <a name="Glue-Type-CatalogPropertiesOutput-CustomProperties"></a>
Additional key-value properties for the catalog, such as column statistics optimizations.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** DataLakeAccessProperties **   <a name="Glue-Type-CatalogPropertiesOutput-DataLakeAccessProperties"></a>
A `DataLakeAccessProperties` object with input properties to configure data lake access for your catalog resource in the AWS Glue Data Catalog.
Type: [DataLakeAccessPropertiesOutput](API_DataLakeAccessPropertiesOutput.md) object
Required: No

 ** IcebergOptimizationProperties **   <a name="Glue-Type-CatalogPropertiesOutput-IcebergOptimizationProperties"></a>
An `IcebergOptimizationPropertiesOutput` object that specifies Iceberg table optimization settings for the catalog, including configurations for compaction, retention, and orphan file deletion operations.
Type: [IcebergOptimizationPropertiesOutput](API_IcebergOptimizationPropertiesOutput.md) object
Required: No

## See Also
<a name="API_CatalogPropertiesOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CatalogPropertiesOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CatalogPropertiesOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CatalogPropertiesOutput)
