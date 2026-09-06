---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataSourceSyncJob.html
---

# DataSourceSyncJob
<a name="API_DataSourceSyncJob"></a>

Provides information about an Amazon Q Business data source connector synchronization job.

## Contents
<a name="API_DataSourceSyncJob_Contents"></a>

 ** dataSourceErrorCode **   <a name="qbusiness-Type-DataSourceSyncJob-dataSourceErrorCode"></a>
If the reason that the synchronization failed is due to an error with the underlying data source, this field contains a code that identifies the error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** endTime **   <a name="qbusiness-Type-DataSourceSyncJob-endTime"></a>
The Unix timestamp when the synchronization job completed.
Type: Timestamp
Required: No

 ** error **   <a name="qbusiness-Type-DataSourceSyncJob-error"></a>
If the `Status` field is set to `FAILED`, the `ErrorCode` field indicates the reason the synchronization failed.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** executionId **   <a name="qbusiness-Type-DataSourceSyncJob-executionId"></a>
The identifier of a data source synchronization job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** metrics **   <a name="qbusiness-Type-DataSourceSyncJob-metrics"></a>
Maps a batch delete document request to a specific data source sync job. This is optional and should only be supplied when documents are deleted by a data source connector.
Type: [DataSourceSyncJobMetrics](API_DataSourceSyncJobMetrics.md) object
Required: No

 ** startTime **   <a name="qbusiness-Type-DataSourceSyncJob-startTime"></a>
The Unix time stamp when the data source synchronization job started.
Type: Timestamp
Required: No

 ** status **   <a name="qbusiness-Type-DataSourceSyncJob-status"></a>
The status of the synchronization job. When the `Status` field is set to `SUCCEEDED`, the synchronization job is done. If the status code is `FAILED`, the `ErrorCode` and `ErrorMessage` fields give you the reason for the failure.
Type: String
Valid Values: `FAILED | SUCCEEDED | SYNCING | INCOMPLETE | STOPPING | ABORTED | SYNCING_INDEXING`
Required: No

## See Also
<a name="API_DataSourceSyncJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DataSourceSyncJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DataSourceSyncJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DataSourceSyncJob)
