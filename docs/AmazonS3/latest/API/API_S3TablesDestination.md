---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3TablesDestination.html
---

# S3TablesDestination
<a name="API_S3TablesDestination"></a>

 The destination information for a V1 S3 Metadata configuration. The destination table bucket must be in the same Region and AWS account as the general purpose bucket. The specified metadata table name must be unique within the `aws_s3_metadata` namespace in the destination table bucket.

**Note**
If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete and re-create your configuration by using [CreateBucketMetadataConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) so that you can expire journal table records and create a live inventory table.

## Contents
<a name="API_S3TablesDestination_Contents"></a>

 ** TableBucketArn **   <a name="AmazonS3-Type-S3TablesDestination-TableBucketArn"></a>
 The Amazon Resource Name (ARN) for the table bucket that's specified as the destination in the metadata table configuration. The destination table bucket must be in the same Region and AWS account as the general purpose bucket.
Type: String
Required: Yes

 ** TableName **   <a name="AmazonS3-Type-S3TablesDestination-TableName"></a>
 The name for the metadata table in your metadata table configuration. The specified metadata table name must be unique within the `aws_s3_metadata` namespace in the destination table bucket.
Type: String
Required: Yes

## See Also
<a name="API_S3TablesDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/S3TablesDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/S3TablesDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/S3TablesDestination)
