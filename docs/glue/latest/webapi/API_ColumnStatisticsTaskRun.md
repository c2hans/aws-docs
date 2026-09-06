---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ColumnStatisticsTaskRun.html
---

# ColumnStatisticsTaskRun
<a name="API_ColumnStatisticsTaskRun"></a>

The object that shows the details of the column stats run.

## Contents
<a name="API_ColumnStatisticsTaskRun_Contents"></a>

 ** CatalogID **   <a name="Glue-Type-ColumnStatisticsTaskRun-CatalogID"></a>
The ID of the Data Catalog where the table resides. If none is supplied, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ColumnNameList **   <a name="Glue-Type-ColumnStatisticsTaskRun-ColumnNameList"></a>
A list of the column names. If none is supplied, all column names for the table will be used by default.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ColumnStatisticsTaskRunId **   <a name="Glue-Type-ColumnStatisticsTaskRun-ColumnStatisticsTaskRunId"></a>
The identifier for the particular column statistics task run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ComputationType **   <a name="Glue-Type-ColumnStatisticsTaskRun-ComputationType"></a>
The type of column statistics computation.
Type: String
Valid Values: `FULL | INCREMENTAL`
Required: No

 ** CreationTime **   <a name="Glue-Type-ColumnStatisticsTaskRun-CreationTime"></a>
The time that this task was created.
Type: Timestamp
Required: No

 ** CustomerId **   <a name="Glue-Type-ColumnStatisticsTaskRun-CustomerId"></a>
The AWS account ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Required: No

 ** DatabaseName **   <a name="Glue-Type-ColumnStatisticsTaskRun-DatabaseName"></a>
The database where the table resides.
Type: String
Required: No

 ** DPUSeconds **   <a name="Glue-Type-ColumnStatisticsTaskRun-DPUSeconds"></a>
The calculated DPU usage in seconds for all autoscaled workers.
Type: Double
Valid Range: Minimum value of 0.0.
Required: No

 ** EndTime **   <a name="Glue-Type-ColumnStatisticsTaskRun-EndTime"></a>
The end time of the task.
Type: Timestamp
Required: No

 ** ErrorMessage **   <a name="Glue-Type-ColumnStatisticsTaskRun-ErrorMessage"></a>
The error message for the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** LastUpdated **   <a name="Glue-Type-ColumnStatisticsTaskRun-LastUpdated"></a>
The last point in time when this task was modified.
Type: Timestamp
Required: No

 ** NumberOfWorkers **   <a name="Glue-Type-ColumnStatisticsTaskRun-NumberOfWorkers"></a>
The number of workers used to generate column statistics. The job is preconfigured to autoscale up to 25 instances.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** Role **   <a name="Glue-Type-ColumnStatisticsTaskRun-Role"></a>
The IAM role that the service assumes to generate statistics.
Type: String
Required: No

 ** SampleSize **   <a name="Glue-Type-ColumnStatisticsTaskRun-SampleSize"></a>
The percentage of rows used to generate statistics. If none is supplied, the entire table will be used to generate stats.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** SecurityConfiguration **   <a name="Glue-Type-ColumnStatisticsTaskRun-SecurityConfiguration"></a>
Name of the security configuration that is used to encrypt CloudWatch logs for the column stats task run.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** StartTime **   <a name="Glue-Type-ColumnStatisticsTaskRun-StartTime"></a>
The start time of the task.
Type: Timestamp
Required: No

 ** Status **   <a name="Glue-Type-ColumnStatisticsTaskRun-Status"></a>
The status of the task run.
Type: String
Valid Values: `STARTING | RUNNING | SUCCEEDED | FAILED | STOPPED`
Required: No

 ** TableName **   <a name="Glue-Type-ColumnStatisticsTaskRun-TableName"></a>
The name of the table for which column statistics is generated.
Type: String
Required: No

 ** WorkerType **   <a name="Glue-Type-ColumnStatisticsTaskRun-WorkerType"></a>
The type of workers being used for generating stats. The default is `g.1x`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_ColumnStatisticsTaskRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ColumnStatisticsTaskRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ColumnStatisticsTaskRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ColumnStatisticsTaskRun)
