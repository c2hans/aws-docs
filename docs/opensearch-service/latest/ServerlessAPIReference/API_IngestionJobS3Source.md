---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_IngestionJobS3Source.html
---

# IngestionJobS3Source
<a name="API_IngestionJobS3Source"></a>

The Amazon S3 source configuration for an ingestion job.

## Contents
<a name="API_IngestionJobS3Source_Contents"></a>

 ** bucket **   <a name="opensearchserverless-Type-IngestionJobS3Source-bucket"></a>
The name or Amazon Resource Name (ARN) of the Amazon S3 bucket to ingest data from.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 2048.
Pattern: `(arn:[a-z0-9\-]+:s3:::[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]|[a-z0-9][a-z0-9.-]{1,61}[a-z0-9])`
Required: No

 ** bucketOwnerAccountId **   <a name="opensearchserverless-Type-IngestionJobS3Source-bucketOwnerAccountId"></a>
The AWS account ID that owns the Amazon S3 bucket.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** keyPrefix **   <a name="opensearchserverless-Type-IngestionJobS3Source-keyPrefix"></a>
A key prefix that limits ingestion to objects in the Amazon S3 bucket whose keys begin with the prefix.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_IngestionJobS3Source_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/IngestionJobS3Source)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/IngestionJobS3Source)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/IngestionJobS3Source)
