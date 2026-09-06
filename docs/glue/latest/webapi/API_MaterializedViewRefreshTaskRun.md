---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_MaterializedViewRefreshTaskRun.html
---

# MaterializedViewRefreshTaskRun
<a name="API_MaterializedViewRefreshTaskRun"></a>

The object that shows the details of the materialized view refresh task run.

## Contents
<a name="API_MaterializedViewRefreshTaskRun_Contents"></a>

 ** CatalogId **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-CatalogId"></a>
The ID of the Catalog where the materialized view table resides. If none is supplied, the account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** CreationTime **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-CreationTime"></a>
The time that this task was created.
Type: Timestamp
Required: No

 ** CustomerId **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-CustomerId"></a>
The AWS account ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Required: No

 ** DatabaseName **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-DatabaseName"></a>
The database where the materialized view table resides.
Type: String
Required: No

 ** DPUSeconds **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-DPUSeconds"></a>
The calculated DPU usage in seconds for all autoscaled workers.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** EndTime **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-EndTime"></a>
The end time of the task.
Type: Timestamp
Required: No

 ** ErrorMessage **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-ErrorMessage"></a>
The error message for the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LastUpdated **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-LastUpdated"></a>
The last point in time when this task was modified.
Type: Timestamp
Required: No

 ** MaterializedViewRefreshTaskRunId **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-MaterializedViewRefreshTaskRunId"></a>
The identifier of the materialized view refresh task run.
Type: String
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`
Required: No

 ** ProcessedBytes **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-ProcessedBytes"></a>
The number of bytes the refresh task run has scanned to refresh the materialized view.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** RefreshType **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-RefreshType"></a>
The type of the refresh task run. Either FULL or INCREMENTAL.
Type: String
Valid Values: `FULL | INCREMENTAL`
Required: No

 ** Role **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-Role"></a>
The IAM role that the service assumes to run the materialized view refresh.
Type: String
Required: No

 ** StartTime **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-StartTime"></a>
The start time of the task.
Type: Timestamp
Required: No

 ** Status **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-Status"></a>
The status of the task run.
Type: String
Valid Values: `STARTING | RUNNING | SUCCEEDED | FAILED | STOPPED`
Required: No

 ** TableName **   <a name="Glue-Type-MaterializedViewRefreshTaskRun-TableName"></a>
The name of the table for which the materialized view resides.
Type: String
Required: No

## See Also
<a name="API_MaterializedViewRefreshTaskRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/MaterializedViewRefreshTaskRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/MaterializedViewRefreshTaskRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/MaterializedViewRefreshTaskRun)
