---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DataSourceSyncJobMetrics.html
---

# DataSourceSyncJobMetrics
<a name="API_DataSourceSyncJobMetrics"></a>

Maps a batch delete document request to a specific Amazon Q Business data source connector sync job.

## Contents
<a name="API_DataSourceSyncJobMetrics_Contents"></a>

 ** documentsAdded **   <a name="qbusiness-Type-DataSourceSyncJobMetrics-documentsAdded"></a>
The current count of documents added from the data source during the data source sync.
Type: String
Pattern: `(([1-9][0-9]*)|0)`
Required: No

 ** documentsDeleted **   <a name="qbusiness-Type-DataSourceSyncJobMetrics-documentsDeleted"></a>
The current count of documents deleted from the data source during the data source sync.
Type: String
Pattern: `(([1-9][0-9]*)|0)`
Required: No

 ** documentsFailed **   <a name="qbusiness-Type-DataSourceSyncJobMetrics-documentsFailed"></a>
The current count of documents that failed to sync from the data source during the data source sync.
Type: String
Pattern: `(([1-9][0-9]*)|0)`
Required: No

 ** documentsModified **   <a name="qbusiness-Type-DataSourceSyncJobMetrics-documentsModified"></a>
The current count of documents modified in the data source during the data source sync.
Type: String
Pattern: `(([1-9][0-9]*)|0)`
Required: No

 ** documentsScanned **   <a name="qbusiness-Type-DataSourceSyncJobMetrics-documentsScanned"></a>
The current count of documents crawled by the ongoing sync job in the data source.
Type: String
Pattern: `(([1-9][0-9]*)|0)`
Required: No

## See Also
<a name="API_DataSourceSyncJobMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/DataSourceSyncJobMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/DataSourceSyncJobMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/DataSourceSyncJobMetrics)
