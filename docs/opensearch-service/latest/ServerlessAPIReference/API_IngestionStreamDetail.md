---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_IngestionStreamDetail.html
---

# IngestionStreamDetail
<a name="API_IngestionStreamDetail"></a>

Details about an ingestion stream.

## Contents
<a name="API_IngestionStreamDetail_Contents"></a>

 ** activeAlerts **   <a name="opensearchserverless-Type-IngestionStreamDetail-activeAlerts"></a>
Active alerts about operational issues that currently affect the ingestion stream. Alerts are cleared when the issue is resolved.
Type: Array of [IngestionAlert](API_IngestionAlert.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** arn **   <a name="opensearchserverless-Type-IngestionStreamDetail-arn"></a>
The Amazon Resource Name (ARN) of the ingestion stream.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-c|aws-iso-d|aws-iso-e):aoss:[a-z0-9-]+:\d{12}:collection/[a-z0-9]{3,40}/ingestion-stream/[a-z0-9]{20,64}`
Required: No

 ** collectionId **   <a name="opensearchserverless-Type-IngestionStreamDetail-collectionId"></a>
The unique identifier of the collection that the ingestion stream belongs to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** createdAt **   <a name="opensearchserverless-Type-IngestionStreamDetail-createdAt"></a>
The date and time when the ingestion stream was created.
Type: Timestamp
Required: No

 ** failureIndexName **   <a name="opensearchserverless-Type-IngestionStreamDetail-failureIndexName"></a>
The name of the index where documents that fail to be ingested are recorded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9.][a-z0-9._-]*`
Required: No

 ** failureReasons **   <a name="opensearchserverless-Type-IngestionStreamDetail-failureReasons"></a>
The reasons that the ingestion stream reached a terminal failure state, if applicable.
Type: Array of [IngestionFailureReason](API_IngestionFailureReason.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** indexName **   <a name="opensearchserverless-Type-IngestionStreamDetail-indexName"></a>
The name of the index that documents are ingested into.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9.][a-z0-9._-]*`
Required: No

 ** ingestionStreamId **   <a name="opensearchserverless-Type-IngestionStreamDetail-ingestionStreamId"></a>
The unique identifier of the ingestion stream.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: No

 ** ingestionStreamName **   <a name="opensearchserverless-Type-IngestionStreamDetail-ingestionStreamName"></a>
The name of the ingestion stream.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]*`
Required: No

 ** revision **   <a name="opensearchserverless-Type-IngestionStreamDetail-revision"></a>
The revision number of the ingestion stream.
Type: Long
Required: No

 ** roleArn **   <a name="opensearchserverless-Type-IngestionStreamDetail-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that OpenSearch Serverless assumes to read data from the source.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-c|aws-iso-d|aws-iso-e):iam::\d{12}:role/.+`
Required: No

 ** source **   <a name="opensearchserverless-Type-IngestionStreamDetail-source"></a>
The Amazon S3 source that the ingestion stream ingests data from.
Type: [IngestionStreamSource](API_IngestionStreamSource.md) object
Required: No

 ** state **   <a name="opensearchserverless-Type-IngestionStreamDetail-state"></a>
The current processing state of the ingestion stream. For example, `STARTING` or `INGESTION_IN_PROGRESS`.
Type: String
Valid Values: `STARTING | SCANNING | INGESTION_IN_PROGRESS | INGESTION_COMPLETE | STOPPED | FAILED`
Required: No

 ** statistics **   <a name="opensearchserverless-Type-IngestionStreamDetail-statistics"></a>
Processing statistics for the ingestion stream, such as the number of Amazon S3 objects discovered, ingested, and failed.
Type: [IngestionStatistics](API_IngestionStatistics.md) object
Required: No

 ** status **   <a name="opensearchserverless-Type-IngestionStreamDetail-status"></a>
The current lifecycle status of the ingestion stream. For example, `CREATING`, `ACTIVE`, or `DELETING`.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | CREATE_FAILED | DELETE_FAILED`
Required: No

 ** updatedAt **   <a name="opensearchserverless-Type-IngestionStreamDetail-updatedAt"></a>
The date and time when the ingestion stream was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_IngestionStreamDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/IngestionStreamDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/IngestionStreamDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/IngestionStreamDetail)
