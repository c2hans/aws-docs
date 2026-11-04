---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_IngestionJobDetail.html
---

# IngestionJobDetail
<a name="API_IngestionJobDetail"></a>

Details about an ingestion job.

## Contents
<a name="API_IngestionJobDetail_Contents"></a>

 ** activeAlerts **   <a name="opensearchserverless-Type-IngestionJobDetail-activeAlerts"></a>
Active alerts about operational issues that currently affect the ingestion job. Alerts are cleared when the issue is resolved.
Type: Array of [IngestionAlert](API_IngestionAlert.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** arn **   <a name="opensearchserverless-Type-IngestionJobDetail-arn"></a>
The Amazon Resource Name (ARN) of the ingestion job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-c|aws-iso-d|aws-iso-e):aoss:[a-z0-9-]+:\d{12}:collection/[a-z0-9]{3,40}/ingestion-job/[a-z0-9]{20,64}`
Required: No

 ** collectionId **   <a name="opensearchserverless-Type-IngestionJobDetail-collectionId"></a>
The unique identifier of the collection that the ingestion job belongs to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: No

 ** createdAt **   <a name="opensearchserverless-Type-IngestionJobDetail-createdAt"></a>
The date and time when the ingestion job was created.
Type: Timestamp
Required: No

 ** failureIndexName **   <a name="opensearchserverless-Type-IngestionJobDetail-failureIndexName"></a>
The name of the index where documents that fail to be ingested are recorded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9.][a-z0-9._-]*`
Required: No

 ** failureReasons **   <a name="opensearchserverless-Type-IngestionJobDetail-failureReasons"></a>
The reasons that the ingestion job reached a terminal failure state, if applicable.
Type: Array of [IngestionFailureReason](API_IngestionFailureReason.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** indexName **   <a name="opensearchserverless-Type-IngestionJobDetail-indexName"></a>
The name of the index that documents are ingested into.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9.][a-z0-9._-]*`
Required: No

 ** ingestionJobId **   <a name="opensearchserverless-Type-IngestionJobDetail-ingestionJobId"></a>
The unique identifier of the ingestion job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: No

 ** ingestionJobName **   <a name="opensearchserverless-Type-IngestionJobDetail-ingestionJobName"></a>
The name of the ingestion job.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]*`
Required: No

 ** revision **   <a name="opensearchserverless-Type-IngestionJobDetail-revision"></a>
The revision number of the ingestion job.
Type: Long
Required: No

 ** source **   <a name="opensearchserverless-Type-IngestionJobDetail-source"></a>
The Amazon S3 source that the ingestion job ingests data from.
Type: [IngestionJobSource](API_IngestionJobSource.md) object
Required: No

 ** state **   <a name="opensearchserverless-Type-IngestionJobDetail-state"></a>
The current processing state of the ingestion job. For example, `SCANNING`, `INGESTION_IN_PROGRESS`, or `INGESTION_COMPLETE`.
Type: String
Valid Values: `STARTING | SCANNING | INGESTION_IN_PROGRESS | INGESTION_COMPLETE | STOPPED | FAILED`
Required: No

 ** statistics **   <a name="opensearchserverless-Type-IngestionJobDetail-statistics"></a>
Processing statistics for the ingestion job, such as the number of Amazon S3 objects discovered, ingested, and failed.
Type: [IngestionStatistics](API_IngestionStatistics.md) object
Required: No

 ** status **   <a name="opensearchserverless-Type-IngestionJobDetail-status"></a>
The current lifecycle status of the ingestion job. For example, `CREATING`, `ACTIVE`, `COMPLETED`, or `CANCELLED`.
Type: String
Valid Values: `CREATING | ACTIVE | COMPLETED | CANCELLING | CANCELLED | FAILED | CREATE_FAILED | CANCEL_FAILED`
Required: No

 ** updatedAt **   <a name="opensearchserverless-Type-IngestionJobDetail-updatedAt"></a>
The date and time when the ingestion job was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_IngestionJobDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/IngestionJobDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/IngestionJobDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/IngestionJobDetail)
