---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergPartitionField.html
---

# IcebergPartitionField
<a name="API_s3Buckets_IcebergPartitionField"></a>

Defines a single partition field in an Iceberg partition specification.

## Contents
<a name="API_s3Buckets_IcebergPartitionField_Contents"></a>

 ** name **   <a name="AmazonS3-Type-s3Buckets_IcebergPartitionField-name"></a>
The name for this partition field. This name is used in the partitioned file paths.
Type: String
Required: Yes

 ** source-id **   <a name="AmazonS3-Type-s3Buckets_IcebergPartitionField-source-id"></a>
The ID of the source schema field to partition by. This must reference a valid field ID from the table schema.
Type: Integer
Required: Yes

 ** transform **   <a name="AmazonS3-Type-s3Buckets_IcebergPartitionField-transform"></a>
The partition transform to apply to the source field. Supported transforms include `identity`, `year`, `month`, `day`, `hour`, `bucket`, and `truncate`. For more information, see the [Apache Iceberg partition transforms documentation](https://iceberg.apache.org/spec/#partition-transforms).
Type: String
Required: Yes

 ** field-id **   <a name="AmazonS3-Type-s3Buckets_IcebergPartitionField-field-id"></a>
An optional unique identifier for this partition field. If not specified, S3 Tables automatically assigns a field ID.
Type: Integer
Required: No

## See Also
<a name="API_s3Buckets_IcebergPartitionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/IcebergPartitionField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/IcebergPartitionField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/IcebergPartitionField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
