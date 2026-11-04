---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_IngestionStreamSummary.html
---

# IngestionStreamSummary
<a name="API_IngestionStreamSummary"></a>

Summary information about an ingestion stream.

## Contents
<a name="API_IngestionStreamSummary_Contents"></a>

 ** arn **   <a name="opensearchserverless-Type-IngestionStreamSummary-arn"></a>
The Amazon Resource Name (ARN) of the ingestion stream.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-c|aws-iso-d|aws-iso-e):aoss:[a-z0-9-]+:\d{12}:collection/[a-z0-9]{3,40}/ingestion-stream/[a-z0-9]{20,64}`
Required: No

 ** createdAt **   <a name="opensearchserverless-Type-IngestionStreamSummary-createdAt"></a>
The date and time when the ingestion stream was created.
Type: Timestamp
Required: No

 ** indexName **   <a name="opensearchserverless-Type-IngestionStreamSummary-indexName"></a>
The name of the index that documents are ingested into.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9.][a-z0-9._-]*`
Required: No

 ** ingestionStreamId **   <a name="opensearchserverless-Type-IngestionStreamSummary-ingestionStreamId"></a>
The unique identifier of the ingestion stream.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: No

 ** ingestionStreamName **   <a name="opensearchserverless-Type-IngestionStreamSummary-ingestionStreamName"></a>
The name of the ingestion stream.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]*`
Required: No

 ** status **   <a name="opensearchserverless-Type-IngestionStreamSummary-status"></a>
The current lifecycle status of the ingestion stream.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | CREATE_FAILED | DELETE_FAILED`
Required: No

 ** updatedAt **   <a name="opensearchserverless-Type-IngestionStreamSummary-updatedAt"></a>
The date and time when the ingestion stream was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_IngestionStreamSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/IngestionStreamSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/IngestionStreamSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/IngestionStreamSummary)
