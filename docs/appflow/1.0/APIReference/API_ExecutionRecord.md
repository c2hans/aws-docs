---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ExecutionRecord.html
---

# ExecutionRecord
<a name="API_ExecutionRecord"></a>

 Specifies information about the past flow run instances for a given flow.

## Contents
<a name="API_ExecutionRecord_Contents"></a>

 ** dataPullEndTime **   <a name="appflow-Type-ExecutionRecord-dataPullEndTime"></a>
 The timestamp that indicates the last new or updated record to be transferred in the flow run.
Type: Timestamp
Required: No

 ** dataPullStartTime **   <a name="appflow-Type-ExecutionRecord-dataPullStartTime"></a>
 The timestamp that determines the first new or updated record to be transferred in the flow run.
Type: Timestamp
Required: No

 ** executionId **   <a name="appflow-Type-ExecutionRecord-executionId"></a>
 Specifies the identifier of the given flow run.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** executionResult **   <a name="appflow-Type-ExecutionRecord-executionResult"></a>
 Describes the result of the given flow run.
Type: [ExecutionResult](API_ExecutionResult.md) object
Required: No

 ** executionStatus **   <a name="appflow-Type-ExecutionRecord-executionStatus"></a>
 Specifies the flow run status and whether it is in progress, has completed successfully, or has failed.
Type: String
Valid Values: `InProgress | Successful | Error | CancelStarted | Canceled`
Required: No

 ** lastUpdatedAt **   <a name="appflow-Type-ExecutionRecord-lastUpdatedAt"></a>
 Specifies the time of the most recent update.
Type: Timestamp
Required: No

 ** metadataCatalogDetails **   <a name="appflow-Type-ExecutionRecord-metadataCatalogDetails"></a>
Describes the metadata catalog, metadata table, and data partitions that Amazon AppFlow used for the associated flow run.
Type: Array of [MetadataCatalogDetail](API_MetadataCatalogDetail.md) objects
Required: No

 ** startedAt **   <a name="appflow-Type-ExecutionRecord-startedAt"></a>
 Specifies the start time of the flow run.
Type: Timestamp
Required: No

## See Also
<a name="API_ExecutionRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ExecutionRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ExecutionRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ExecutionRecord)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
