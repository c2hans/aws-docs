---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ExportTask.html
---

# ExportTask
<a name="API_ExportTask"></a>

Represents an export task.

## Contents
<a name="API_ExportTask_Contents"></a>

 ** destination **   <a name="CWL-Type-ExportTask-destination"></a>
The name of the S3 bucket to which the log data was exported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** destinationPrefix **   <a name="CWL-Type-ExportTask-destinationPrefix"></a>
The prefix that was used as the start of Amazon S3 key for every object exported.
Type: String
Required: No

 ** executionInfo **   <a name="CWL-Type-ExportTask-executionInfo"></a>
Execution information about the export task.
Type: [ExportTaskExecutionInfo](API_ExportTaskExecutionInfo.md) object
Required: No

 ** from **   <a name="CWL-Type-ExportTask-from"></a>
The start time, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`. Events with a timestamp before this time are not exported.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** logGroupName **   <a name="CWL-Type-ExportTask-logGroupName"></a>
The name of the log group from which logs data was exported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** status **   <a name="CWL-Type-ExportTask-status"></a>
The status of the export task.
Type: [ExportTaskStatus](API_ExportTaskStatus.md) object
Required: No

 ** taskId **   <a name="CWL-Type-ExportTask-taskId"></a>
The ID of the export task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** taskName **   <a name="CWL-Type-ExportTask-taskName"></a>
The name of the export task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** to **   <a name="CWL-Type-ExportTask-to"></a>
The end time, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`. Events with a timestamp later than this time are not exported.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ExportTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
