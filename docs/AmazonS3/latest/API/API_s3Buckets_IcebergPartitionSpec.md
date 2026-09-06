---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergPartitionSpec.html
---

# IcebergPartitionSpec
<a name="API_s3Buckets_IcebergPartitionSpec"></a>

Defines how data in an Iceberg table is partitioned. Partitioning helps optimize query performance by organizing data into separate files based on field values. Each partition field specifies a transform to apply to a source field.

## Contents
<a name="API_s3Buckets_IcebergPartitionSpec_Contents"></a>

 ** fields **   <a name="AmazonS3-Type-s3Buckets_IcebergPartitionSpec-fields"></a>
The list of partition fields that define how the table data is partitioned. Each field specifies a source field and a transform to apply. This field is required if `partitionSpec` is provided.
Type: Array of [IcebergPartitionField](API_s3Buckets_IcebergPartitionField.md) objects
Required: Yes

 ** spec-id **   <a name="AmazonS3-Type-s3Buckets_IcebergPartitionSpec-spec-id"></a>
The unique identifier for this partition specification. If not specified, defaults to `0`.
Type: Integer
Required: No

## See Also
<a name="API_s3Buckets_IcebergPartitionSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/IcebergPartitionSpec)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/IcebergPartitionSpec)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/IcebergPartitionSpec)
