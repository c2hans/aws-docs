---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateIcebergTableInput.html
---

# CreateIcebergTableInput
<a name="API_CreateIcebergTableInput"></a>

The configuration parameters required to create a new Iceberg table in the AWS Glue Data Catalog, including table properties and metadata specifications.

## Contents
<a name="API_CreateIcebergTableInput_Contents"></a>

 ** Location **   <a name="Glue-Type-CreateIcebergTableInput-Location"></a>
The S3 location where the Iceberg table data will be stored.
Type: String
Length Constraints: Maximum length of 2056.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Schema **   <a name="Glue-Type-CreateIcebergTableInput-Schema"></a>
The schema definition that specifies the structure, field types, and metadata for the Iceberg table.
Type: [IcebergSchema](API_IcebergSchema.md) object
Required: Yes

 ** PartitionSpec **   <a name="Glue-Type-CreateIcebergTableInput-PartitionSpec"></a>
The partitioning specification that defines how the Iceberg table data will be organized and partitioned for optimal query performance.
Type: [IcebergPartitionSpec](API_IcebergPartitionSpec.md) object
Required: No

 ** Properties **   <a name="Glue-Type-CreateIcebergTableInput-Properties"></a>
Key-value pairs of additional table properties and configuration settings for the Iceberg table.
Type: String to string map
Required: No

 ** WriteOrder **   <a name="Glue-Type-CreateIcebergTableInput-WriteOrder"></a>
The sort order specification that defines how data should be ordered within each partition to optimize query performance.
Type: [IcebergSortOrder](API_IcebergSortOrder.md) object
Required: No

## See Also
<a name="API_CreateIcebergTableInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateIcebergTableInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateIcebergTableInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateIcebergTableInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
