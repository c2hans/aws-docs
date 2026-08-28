---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergSortOrder.html
---

# IcebergSortOrder
<a name="API_s3Buckets_IcebergSortOrder"></a>

Defines the sort order for data within an Iceberg table. Sorting data can improve query performance by enabling more efficient data skipping.

## Contents
<a name="API_s3Buckets_IcebergSortOrder_Contents"></a>

 ** fields **   <a name="AmazonS3-Type-s3Buckets_IcebergSortOrder-fields"></a>
The list of sort fields that define how data is sorted within files. Each field specifies a source field, sort direction, and null ordering. This field is required if `writeOrder` is provided.
Type: Array of [IcebergSortField](API_s3Buckets_IcebergSortField.md) objects
Required: Yes

 ** order-id **   <a name="AmazonS3-Type-s3Buckets_IcebergSortOrder-order-id"></a>
The unique identifier for this sort order. If not specified, defaults to `1`. The order ID is used by Apache Iceberg to track sort order evolution.
Type: Integer
Required: Yes

## See Also
<a name="API_s3Buckets_IcebergSortOrder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/IcebergSortOrder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/IcebergSortOrder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/IcebergSortOrder)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
