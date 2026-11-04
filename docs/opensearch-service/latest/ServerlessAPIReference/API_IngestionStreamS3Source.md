---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_IngestionStreamS3Source.html
---

# IngestionStreamS3Source
<a name="API_IngestionStreamS3Source"></a>

The Amazon S3 source configuration for an ingestion stream.

## Contents
<a name="API_IngestionStreamS3Source_Contents"></a>

 ** sqsArn **   <a name="opensearchserverless-Type-IngestionStreamS3Source-sqsArn"></a>
The Amazon Resource Name (ARN) of the Amazon SQS queue that receives Amazon S3 event notifications for the source buckets.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-c|aws-iso-d|aws-iso-e):sqs:[a-z0-9-]+:\d{12}:.+`
Required: Yes

 ** buckets **   <a name="opensearchserverless-Type-IngestionStreamS3Source-buckets"></a>
The configuration for each Amazon S3 bucket that the ingestion stream ingests data from.
Type: Array of [StreamBucketConfig](API_StreamBucketConfig.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_IngestionStreamS3Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/IngestionStreamS3Source)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/IngestionStreamS3Source)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/IngestionStreamS3Source)
