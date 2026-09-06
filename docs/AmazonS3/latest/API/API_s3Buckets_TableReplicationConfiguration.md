---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableReplicationConfiguration.html
---

# TableReplicationConfiguration
<a name="API_s3Buckets_TableReplicationConfiguration"></a>

The replication configuration for an individual table. This configuration defines how the table is replicated to destination tables.

## Contents
<a name="API_s3Buckets_TableReplicationConfiguration_Contents"></a>

 ** role **   <a name="AmazonS3-Type-s3Buckets_TableReplicationConfiguration-role"></a>
The Amazon Resource Name (ARN) of the IAM role that S3 Tables assumes to replicate the table on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.+:iam::[0-9]{12}:role/.+`
Required: Yes

 ** rules **   <a name="AmazonS3-Type-s3Buckets_TableReplicationConfiguration-rules"></a>
An array of replication rules that define where this table should be replicated.
Type: Array of [TableReplicationRule](API_s3Buckets_TableReplicationRule.md) objects
Array Members: Fixed number of 1 item.
Required: Yes

## See Also
<a name="API_s3Buckets_TableReplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableReplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableReplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableReplicationConfiguration)
