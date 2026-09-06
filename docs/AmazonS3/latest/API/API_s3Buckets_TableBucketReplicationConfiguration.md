---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableBucketReplicationConfiguration.html
---

# TableBucketReplicationConfiguration
<a name="API_s3Buckets_TableBucketReplicationConfiguration"></a>

The replication configuration for a table bucket. This configuration defines how tables in the source bucket are replicated to destination table buckets, including the IAM role used for replication.

## Contents
<a name="API_s3Buckets_TableBucketReplicationConfiguration_Contents"></a>

 ** role **   <a name="AmazonS3-Type-s3Buckets_TableBucketReplicationConfiguration-role"></a>
The Amazon Resource Name (ARN) of the IAM role that S3 Tables assumes to replicate tables on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.+:iam::[0-9]{12}:role/.+`
Required: Yes

 ** rules **   <a name="AmazonS3-Type-s3Buckets_TableBucketReplicationConfiguration-rules"></a>
An array of replication rules that define which tables to replicate and where to replicate them.
Type: Array of [TableBucketReplicationRule](API_s3Buckets_TableBucketReplicationRule.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## See Also
<a name="API_s3Buckets_TableBucketReplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableBucketReplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableBucketReplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableBucketReplicationConfiguration)
