---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_IcebergSortField.html
---

# IcebergSortField
<a name="API_s3Buckets_IcebergSortField"></a>

Defines a single sort field in an Iceberg sort order specification.

## Contents
<a name="API_s3Buckets_IcebergSortField_Contents"></a>

 ** direction **   <a name="AmazonS3-Type-s3Buckets_IcebergSortField-direction"></a>
The sort direction. Valid values are `asc` for ascending order or `desc` for descending order.
Type: String
Valid Values: `asc | desc`
Required: Yes

 ** null-order **   <a name="AmazonS3-Type-s3Buckets_IcebergSortField-null-order"></a>
Specifies how null values are ordered. Valid values are `nulls-first` to place nulls before non-null values, or `nulls-last` to place nulls after non-null values.
Type: String
Valid Values: `nulls-first | nulls-last`
Required: Yes

 ** source-id **   <a name="AmazonS3-Type-s3Buckets_IcebergSortField-source-id"></a>
The ID of the source schema field to sort by. This must reference a valid field ID from the table schema.
Type: Integer
Required: Yes

 ** transform **   <a name="AmazonS3-Type-s3Buckets_IcebergSortField-transform"></a>
The transform to apply to the source field before sorting. Use `identity` to sort by the field value directly, or specify other transforms as needed.
Type: String
Required: Yes

## See Also
<a name="API_s3Buckets_IcebergSortField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/IcebergSortField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/IcebergSortField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/IcebergSortField)
