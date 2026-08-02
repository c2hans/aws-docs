---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_KnowledgeBaseIngestionSummary.html
---

# KnowledgeBaseIngestionSummary
<a name="API_KnowledgeBaseIngestionSummary"></a>

A summary of an ingestion job for a knowledge base.

## Contents
<a name="API_KnowledgeBaseIngestionSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IngestionId **   <a name="QS-Type-KnowledgeBaseIngestionSummary-IngestionId"></a>
The unique identifier for the ingestion job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[0-9a-zA-Z-_=.+]+`
Required: Yes

 ** IngestionStatus **   <a name="QS-Type-KnowledgeBaseIngestionSummary-IngestionStatus"></a>
The status of the ingestion job.
Type: String
Valid Values: `QUEUED | RUNNING | FAILED | COMPLETED | INCOMPLETE | CANCELLED | CANCELLING | TIMEOUT`
Required: Yes

 ** EndTime **   <a name="QS-Type-KnowledgeBaseIngestionSummary-EndTime"></a>
The end time of the ingestion job.
Type: Timestamp
Required: No

 ** StartTime **   <a name="QS-Type-KnowledgeBaseIngestionSummary-StartTime"></a>
The start time of the ingestion job.
Type: Timestamp
Required: No

## See Also
<a name="API_KnowledgeBaseIngestionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/KnowledgeBaseIngestionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/KnowledgeBaseIngestionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/KnowledgeBaseIngestionSummary)
