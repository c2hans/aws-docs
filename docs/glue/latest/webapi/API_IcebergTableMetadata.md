---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IcebergTableMetadata.html
---

# IcebergTableMetadata
<a name="API_IcebergTableMetadata"></a>

The Apache Iceberg table metadata, including format version, table identifier, schemas, partition specifications, sort orders, and table properties. This structure captures the current state of an Iceberg table's metadata as managed by the AWS Glue Data Catalog.

## Contents
<a name="API_IcebergTableMetadata_Contents"></a>

 ** CurrentSchemaId **   <a name="Glue-Type-IcebergTableMetadata-CurrentSchemaId"></a>
The identifier of the schema that is currently active for the Iceberg table. Matches an entry in `Schemas`.
Type: Integer
Required: No

 ** DefaultSortOrderId **   <a name="Glue-Type-IcebergTableMetadata-DefaultSortOrderId"></a>
The identifier of the sort order that is currently used by default when writing new data to the Iceberg table.
Type: Integer
Required: No

 ** DefaultSpecId **   <a name="Glue-Type-IcebergTableMetadata-DefaultSpecId"></a>
The identifier of the partition specification that is currently used by default when writing new data to the Iceberg table.
Type: Integer
Required: No

 ** FormatVersion **   <a name="Glue-Type-IcebergTableMetadata-FormatVersion"></a>
The Apache Iceberg table format version, such as `1` or `2`. Determines the set of features and on-disk layout supported by the table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** LastColumnId **   <a name="Glue-Type-IcebergTableMetadata-LastColumnId"></a>
The highest column identifier that has been assigned in the Iceberg table's schema, used to ensure unique IDs as new columns are added.
Type: Integer
Required: No

 ** LastPartitionId **   <a name="Glue-Type-IcebergTableMetadata-LastPartitionId"></a>
The highest partition field identifier that has been assigned across the table's partition specifications.
Type: Integer
Required: No

 ** Location **   <a name="Glue-Type-IcebergTableMetadata-Location"></a>
The base S3 location where the Iceberg table's data and metadata files are stored.
Type: String
Length Constraints: Maximum length of 2056.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** PartitionSpecs **   <a name="Glue-Type-IcebergTableMetadata-PartitionSpecs"></a>
The list of partition specifications that have been associated with the Iceberg table over its history, supporting partition evolution.
Type: Array of [IcebergPartitionSpec](API_IcebergPartitionSpec.md) objects
Required: No

 ** Properties **   <a name="Glue-Type-IcebergTableMetadata-Properties"></a>
A map of key-value pairs that define table-level properties and configuration settings for the Iceberg table.
Type: String to string map
Required: No

 ** Schemas **   <a name="Glue-Type-IcebergTableMetadata-Schemas"></a>
The list of schemas that have been associated with the Iceberg table over its history, supporting schema evolution.
Type: Array of [IcebergSchema](API_IcebergSchema.md) objects
Required: No

 ** SortOrders **   <a name="Glue-Type-IcebergTableMetadata-SortOrders"></a>
The list of sort order specifications that have been associated with the Iceberg table over its history.
Type: Array of [IcebergSortOrder](API_IcebergSortOrder.md) objects
Required: No

 ** TableUuid **   <a name="Glue-Type-IcebergTableMetadata-TableUuid"></a>
The unique identifier (UUID) for the Iceberg table, assigned when the table is created and used to track the table across metadata updates.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_IcebergTableMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IcebergTableMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IcebergTableMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IcebergTableMetadata)
