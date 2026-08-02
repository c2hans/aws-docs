---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CatalogSource.html
---

# CatalogSource
<a name="API_CatalogSource"></a>

Specifies a data store in the AWS Glue Data Catalog.

## Contents
<a name="API_CatalogSource_Contents"></a>

 ** Database **   <a name="Glue-Type-CatalogSource-Database"></a>
The name of the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-CatalogSource-Name"></a>
The name of the data store.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-CatalogSource-Table"></a>
The name of the table in the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** OutputSchemas **   <a name="Glue-Type-CatalogSource-OutputSchemas"></a>
Specifies the data schema for the catalog source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

 ** PartitionPredicate **   <a name="Glue-Type-CatalogSource-PartitionPredicate"></a>
 Partitions satisfying this predicate are deleted. Files within the retention period in these partitions are not deleted.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_CatalogSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CatalogSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CatalogSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CatalogSource)
