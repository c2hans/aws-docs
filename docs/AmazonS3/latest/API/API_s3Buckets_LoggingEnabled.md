---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_LoggingEnabled.html
---

# LoggingEnabled
<a name="API_s3Buckets_LoggingEnabled"></a>

Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a table bucket.

## Contents
<a name="API_s3Buckets_LoggingEnabled_Contents"></a>

 ** targetBucket **   <a name="AmazonS3-Type-s3Buckets_LoggingEnabled-targetBucket"></a>
The name of the general purpose bucket that logs are delivered to. The bucket must be in the same AWS Region and owned by the same AWS account as the table bucket. The bucket can't use SSE-KMS or DSSE-KMS default encryption, can't have S3 Object Lock enabled, and can't have Requester Pays enabled. You can deliver logs from multiple table buckets to the same target bucket. In this case, choose a different `targetPrefix` for each table bucket so that you can tell their log objects apart.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Required: Yes

 ** targetObjectKeyFormat **   <a name="AmazonS3-Type-s3Buckets_LoggingEnabled-targetObjectKeyFormat"></a>
The key format of the log objects. Log object keys are always partitioned by date.
Type: [TargetObjectKeyFormat](API_s3Buckets_TargetObjectKeyFormat.md) object
Required: Yes

 ** targetPrefix **   <a name="AmazonS3-Type-s3Buckets_LoggingEnabled-targetPrefix"></a>
The prefix for the keys of the log objects that are delivered to the target bucket.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_s3Buckets_LoggingEnabled_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/LoggingEnabled)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/LoggingEnabled)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/LoggingEnabled)
