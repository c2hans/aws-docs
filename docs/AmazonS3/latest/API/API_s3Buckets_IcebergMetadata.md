---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergMetadata.html
---

# IcebergMetadata
<a name="API_s3Buckets_IcebergMetadata"></a>

Contains details about the metadata for an Iceberg table.

## Contents
<a name="API_s3Buckets_IcebergMetadata_Contents"></a>

 ** partitionSpec **   <a name="AmazonS3-Type-s3Buckets_IcebergMetadata-partitionSpec"></a>
The partition specification for the Iceberg table. Partitioning organizes data into separate files based on the values of one or more fields, which can improve query performance by reducing the amount of data scanned. Each partition field applies a transform (such as identity, year, month, or bucket) to a single field.
Type: [IcebergPartitionSpec](API_s3Buckets_IcebergPartitionSpec.md) object
Required: No

 ** properties **   <a name="AmazonS3-Type-s3Buckets_IcebergMetadata-properties"></a>
A map of custom configuration properties for the Iceberg table.
Type: String to string map
Required: No

 ** schema **   <a name="AmazonS3-Type-s3Buckets_IcebergMetadata-schema"></a>
The schema for an Iceberg table. Use this property to define table schemas with primitive types only. For schemas that include nested or complex types such as `struct`, `list`, or `map`, use `schemaV2` instead.
Type: [IcebergSchema](API_s3Buckets_IcebergSchema.md) object
Required: No

 ** schemaV2 **   <a name="AmazonS3-Type-s3Buckets_IcebergMetadata-schemaV2"></a>
The schema for an Iceberg table using the V2 format. Use this property to define table schemas that include nested or complex data types such as `struct`, `list`, or `map`, in addition to primitive types. For schemas with only primitive types, you can use either `schema` or `schemaV2`.
Type: [IcebergSchemaV2](API_s3Buckets_IcebergSchemaV2.md) object
Required: No

 ** writeOrder **   <a name="AmazonS3-Type-s3Buckets_IcebergMetadata-writeOrder"></a>
The sort order for the Iceberg table. Sort order defines how data is sorted within data files, which can improve query performance by enabling more efficient data skipping and filtering.
Type: [IcebergSortOrder](API_s3Buckets_IcebergSortOrder.md) object
Required: No

## See Also
<a name="API_s3Buckets_IcebergMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/IcebergMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/IcebergMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/IcebergMetadata)
