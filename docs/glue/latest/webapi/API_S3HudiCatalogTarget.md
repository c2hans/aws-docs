---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3HudiCatalogTarget.html
---

# S3HudiCatalogTarget
<a name="API_S3HudiCatalogTarget"></a>

Specifies a target that writes to a Hudi data source in the AWS Glue Data Catalog.

## Contents
<a name="API_S3HudiCatalogTarget_Contents"></a>

 ** AdditionalOptions **   <a name="Glue-Type-S3HudiCatalogTarget-AdditionalOptions"></a>
Specifies additional connection options for the connector.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Database **   <a name="Glue-Type-S3HudiCatalogTarget-Database"></a>
The name of the database to write to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-S3HudiCatalogTarget-Inputs"></a>
The nodes that are inputs to the data target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-S3HudiCatalogTarget-Name"></a>
The name of the data target.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-S3HudiCatalogTarget-Table"></a>
The name of the table in the database to write to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AutoDataQuality **   <a name="Glue-Type-S3HudiCatalogTarget-AutoDataQuality"></a>
Specifies whether to automatically enable data quality evaluation for the S3 Hudi catalog target. When set to `true`, data quality checks are performed automatically during the write operation.
Type: [AutoDataQuality](API_AutoDataQuality.md) object
Required: No

 ** OutputSchemas **   <a name="Glue-Type-S3HudiCatalogTarget-OutputSchemas"></a>
Specifies the data schema for the S3 Hudi catalog target.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

 ** PartitionKeys **   <a name="Glue-Type-S3HudiCatalogTarget-PartitionKeys"></a>
Specifies native partitioning using a sequence of keys.
Type: Array of arrays of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** SchemaChangePolicy **   <a name="Glue-Type-S3HudiCatalogTarget-SchemaChangePolicy"></a>
A policy that specifies update behavior for the crawler.
Type: [CatalogSchemaChangePolicy](API_CatalogSchemaChangePolicy.md) object
Required: No

## See Also
<a name="API_S3HudiCatalogTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3HudiCatalogTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3HudiCatalogTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3HudiCatalogTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
