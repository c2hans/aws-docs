---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_BasicCatalogTarget.html
---

# BasicCatalogTarget
<a name="API_BasicCatalogTarget"></a>

Specifies a target that uses a AWS Glue Data Catalog table.

## Contents
<a name="API_BasicCatalogTarget_Contents"></a>

 ** Database **   <a name="Glue-Type-BasicCatalogTarget-Database"></a>
The database that contains the table you want to use as the target. This database must already exist in the Data Catalog.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-BasicCatalogTarget-Inputs"></a>
The nodes that are inputs to the data target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-BasicCatalogTarget-Name"></a>
The name of your data target.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-BasicCatalogTarget-Table"></a>
The table that defines the schema of your output data. This table must already exist in the Data Catalog.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** PartitionKeys **   <a name="Glue-Type-BasicCatalogTarget-PartitionKeys"></a>
The partition keys used to distribute data across multiple partitions or shards based on a specific key or set of key.
Type: Array of arrays of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_BasicCatalogTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/BasicCatalogTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/BasicCatalogTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/BasicCatalogTarget)
