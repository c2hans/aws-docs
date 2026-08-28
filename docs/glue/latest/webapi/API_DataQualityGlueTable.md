---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityGlueTable.html
---

# DataQualityGlueTable
<a name="API_DataQualityGlueTable"></a>

The database and table in the AWS Glue Data Catalog that is used for input or output data for Data Quality Operations.

## Contents
<a name="API_DataQualityGlueTable_Contents"></a>

 ** DatabaseName **   <a name="Glue-Type-DataQualityGlueTable-DatabaseName"></a>
A database name in the AWS Glue Data Catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** TableName **   <a name="Glue-Type-DataQualityGlueTable-TableName"></a>
A table name in the AWS Glue Data Catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-DataQualityGlueTable-AdditionalOptions"></a>
Additional options for the table. Currently there are two keys supported:
+  `pushDownPredicate`: to filter on partitions without having to list and read all the files in your dataset.
+  `catalogPartitionPredicate`: to use server-side partition pruning using partition indexes in the AWS Glue Data Catalog.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Value Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** CatalogId **   <a name="Glue-Type-DataQualityGlueTable-CatalogId"></a>
A unique identifier for the AWS Glue Data Catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ConnectionName **   <a name="Glue-Type-DataQualityGlueTable-ConnectionName"></a>
The name of the connection to the AWS Glue Data Catalog.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** PreProcessingQuery **   <a name="Glue-Type-DataQualityGlueTable-PreProcessingQuery"></a>
SQL Query of SparkSQL format that can be used to pre-process the data for the table in AWS Glue Data Catalog, before running the Data Quality Operation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

## See Also
<a name="API_DataQualityGlueTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityGlueTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityGlueTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityGlueTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
