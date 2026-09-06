---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_LoggingEnabled.html
---

# LoggingEnabled
<a name="API_LoggingEnabled"></a>

Describes where logs are stored and the prefix that Amazon S3 assigns to all log object keys for a bucket. For more information, see [PUT Bucket logging](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlogging.html) in the *Amazon S3 API Reference*.

## Contents
<a name="API_LoggingEnabled_Contents"></a>

 ** TargetBucket **   <a name="AmazonS3-Type-LoggingEnabled-TargetBucket"></a>
Specifies the bucket where you want Amazon S3 to store server access logs. You can have your logs delivered to any bucket that you own, including the same bucket that is being logged. You can also configure multiple buckets to deliver their logs to the same target bucket. In this case, you should choose a different `TargetPrefix` for each source bucket so that the delivered log files can be distinguished by key.
Type: String
Required: Yes

 ** TargetPrefix **   <a name="AmazonS3-Type-LoggingEnabled-TargetPrefix"></a>
A prefix for all log object keys. If you store log files from multiple Amazon S3 buckets in a single bucket, you can use a prefix to distinguish which log files came from which bucket.
Type: String
Required: Yes

 ** TargetGrants **   <a name="AmazonS3-Type-LoggingEnabled-TargetGrants"></a>
Container for granting information.
Buckets that use the bucket owner enforced setting for Object Ownership don't support target grants. For more information, see [Permissions for server access log delivery](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html#grant-log-delivery-permissions-general) in the *Amazon S3 User Guide*.
Type: Array of [TargetGrant](API_TargetGrant.md) data types
Required: No

 ** TargetObjectKeyFormat **   <a name="AmazonS3-Type-LoggingEnabled-TargetObjectKeyFormat"></a>
Amazon S3 key format for log objects.
Type: [TargetObjectKeyFormat](API_TargetObjectKeyFormat.md) data type
Required: No

## See Also
<a name="API_LoggingEnabled_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/LoggingEnabled)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/LoggingEnabled)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/LoggingEnabled)
