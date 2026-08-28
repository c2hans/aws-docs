---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ColumnStatisticsTaskSettings.html
---

# ColumnStatisticsTaskSettings
<a name="API_ColumnStatisticsTaskSettings"></a>

The settings for a column statistics task.

## Contents
<a name="API_ColumnStatisticsTaskSettings_Contents"></a>

 ** CatalogID **   <a name="Glue-Type-ColumnStatisticsTaskSettings-CatalogID"></a>
The ID of the Data Catalog in which the database resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ColumnNameList **   <a name="Glue-Type-ColumnStatisticsTaskSettings-ColumnNameList"></a>
A list of column names for which to run statistics.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** DatabaseName **   <a name="Glue-Type-ColumnStatisticsTaskSettings-DatabaseName"></a>
The name of the database where the table resides.
Type: String
Required: No

 ** LastExecutionAttempt **   <a name="Glue-Type-ColumnStatisticsTaskSettings-LastExecutionAttempt"></a>
The last `ExecutionAttempt` for the column statistics task run.
Type: [ExecutionAttempt](API_ExecutionAttempt.md) object
Required: No

 ** Role **   <a name="Glue-Type-ColumnStatisticsTaskSettings-Role"></a>
The role used for running the column statistics.
Type: String
Required: No

 ** SampleSize **   <a name="Glue-Type-ColumnStatisticsTaskSettings-SampleSize"></a>
The percentage of data to sample.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** Schedule **   <a name="Glue-Type-ColumnStatisticsTaskSettings-Schedule"></a>
A schedule for running the column statistics, specified in CRON syntax.
Type: [Schedule](API_Schedule.md) object
Required: No

 ** ScheduleType **   <a name="Glue-Type-ColumnStatisticsTaskSettings-ScheduleType"></a>
The type of schedule for a column statistics task. Possible values may be `CRON` or `AUTO`.
Type: String
Valid Values: `CRON | AUTO`
Required: No

 ** SecurityConfiguration **   <a name="Glue-Type-ColumnStatisticsTaskSettings-SecurityConfiguration"></a>
Name of the security configuration that is used to encrypt CloudWatch logs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** SettingSource **   <a name="Glue-Type-ColumnStatisticsTaskSettings-SettingSource"></a>
The source of setting the column statistics task. Possible values may be `CATALOG` or `TABLE`.
Type: String
Valid Values: `CATALOG | TABLE`
Required: No

 ** TableName **   <a name="Glue-Type-ColumnStatisticsTaskSettings-TableName"></a>
The name of the table for which to generate column statistics.
Type: String
Required: No

## See Also
<a name="API_ColumnStatisticsTaskSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ColumnStatisticsTaskSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ColumnStatisticsTaskSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ColumnStatisticsTaskSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
