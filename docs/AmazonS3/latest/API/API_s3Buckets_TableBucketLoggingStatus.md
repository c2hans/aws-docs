---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_s3Buckets_TableBucketLoggingStatus.html
---

# TableBucketLoggingStatus
<a name="API_s3Buckets_TableBucketLoggingStatus"></a>

The server access logging status of a table bucket. To enable logging, specify `loggingEnabled`. To disable logging, specify an empty `TableBucketLoggingStatus`.

## Contents
<a name="API_s3Buckets_TableBucketLoggingStatus_Contents"></a>

 ** loggingEnabled **   <a name="AmazonS3-Type-s3Buckets_TableBucketLoggingStatus-loggingEnabled"></a>
Where logs for the table bucket are delivered and how the log objects are named. Must be populated to enable logging.
Type: [LoggingEnabled](API_s3Buckets_LoggingEnabled.md) object
Required: No

## See Also
<a name="API_s3Buckets_TableBucketLoggingStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/TableBucketLoggingStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/TableBucketLoggingStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/TableBucketLoggingStatus)
