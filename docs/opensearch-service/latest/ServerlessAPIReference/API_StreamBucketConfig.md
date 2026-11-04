---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_StreamBucketConfig.html
---

# StreamBucketConfig
<a name="API_StreamBucketConfig"></a>

The configuration for an Amazon S3 bucket that an ingestion stream ingests data from.

## Contents
<a name="API_StreamBucketConfig_Contents"></a>

 ** bucket **   <a name="opensearchserverless-Type-StreamBucketConfig-bucket"></a>
The name or Amazon Resource Name (ARN) of the Amazon S3 bucket to ingest data from.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `(arn:[a-z0-9\-]+:s3:::[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]|[a-z0-9][a-z0-9.-]{1,61}[a-z0-9])`
Required: Yes

 ** bucketOwnerAccountId **   <a name="opensearchserverless-Type-StreamBucketConfig-bucketOwnerAccountId"></a>
The AWS account ID that owns the Amazon S3 bucket. If omitted, the bucket is assumed to be owned by the same account as the one in `sqsArn`. For cross-account buckets, you must set this value to the account ID of the bucket owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** initialScan **   <a name="opensearchserverless-Type-StreamBucketConfig-initialScan"></a>
Specifies whether to perform a one-time scan of the objects that already exist in the bucket before the stream begins processing Amazon S3 event notifications. If `DISABLED`, only new objects are ingested.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_StreamBucketConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/StreamBucketConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/StreamBucketConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/StreamBucketConfig)
