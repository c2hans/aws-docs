---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CatalogProperties.html
---

# CatalogProperties
<a name="API_CatalogProperties"></a>

A structure that specifies data lake access properties and other custom properties.

## Contents
<a name="API_CatalogProperties_Contents"></a>

 ** CustomProperties **   <a name="Glue-Type-CatalogProperties-CustomProperties"></a>
Additional key-value properties for the catalog, such as column statistics optimizations.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** DataLakeAccessProperties **   <a name="Glue-Type-CatalogProperties-DataLakeAccessProperties"></a>
A `DataLakeAccessProperties` object that specifies properties to configure data lake access for your catalog resource in the AWS Glue Data Catalog.
Type: [DataLakeAccessProperties](API_DataLakeAccessProperties.md) object
Required: No

 ** IcebergOptimizationProperties **   <a name="Glue-Type-CatalogProperties-IcebergOptimizationProperties"></a>
A structure that specifies Iceberg table optimization properties for the catalog. This includes configuration for compaction, retention, and orphan file deletion operations that can be applied to Iceberg tables in this catalog.
Type: [IcebergOptimizationProperties](API_IcebergOptimizationProperties.md) object
Required: No

## See Also
<a name="API_CatalogProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CatalogProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CatalogProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CatalogProperties)
