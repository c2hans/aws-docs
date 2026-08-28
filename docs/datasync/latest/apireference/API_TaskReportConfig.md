---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_TaskReportConfig.html
---

# TaskReportConfig
<a name="API_TaskReportConfig"></a>

Specifies how you want to configure a task report, which provides detailed information about for your AWS DataSync transfer.

For more information, see [Task reports](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html).

## Contents
<a name="API_TaskReportConfig_Contents"></a>

 ** Destination **   <a name="DataSync-Type-TaskReportConfig-Destination"></a>
Specifies the Amazon S3 bucket where DataSync uploads your task report. For more information, see [Task reports](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html#task-report-access).
Type: [ReportDestination](API_ReportDestination.md) object
Required: No

 ** ObjectVersionIds **   <a name="DataSync-Type-TaskReportConfig-ObjectVersionIds"></a>
Specifies whether your task report includes the new version of each object transferred into an S3 bucket. This only applies if you [enable versioning on your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html). Keep in mind that setting this to `INCLUDE` can increase the duration of your task execution.
Type: String
Valid Values: `INCLUDE | NONE`
Required: No

 ** OutputType **   <a name="DataSync-Type-TaskReportConfig-OutputType"></a>
Specifies the type of task report that you want:
+  `SUMMARY_ONLY`: Provides necessary details about your task, including the number of files, objects, and directories transferred and transfer duration.
+  `STANDARD`: Provides complete details about your task, including a full list of files, objects, and directories that were transferred, skipped, verified, and more.
Type: String
Valid Values: `SUMMARY_ONLY | STANDARD`
Required: No

 ** Overrides **   <a name="DataSync-Type-TaskReportConfig-Overrides"></a>
Customizes the reporting level for aspects of your task report. For example, your report might generally only include errors, but you could specify that you want a list of successes and errors just for the files that DataSync attempted to delete in your destination location.
Type: [ReportOverrides](API_ReportOverrides.md) object
Required: No

 ** ReportLevel **   <a name="DataSync-Type-TaskReportConfig-ReportLevel"></a>
Specifies whether you want your task report to include only what went wrong with your transfer or a list of what succeeded and didn't.
+  `ERRORS_ONLY`: A report shows what DataSync was unable to transfer, skip, verify, and delete.
+  `SUCCESSES_AND_ERRORS`: A report shows what DataSync was able and unable to transfer, skip, verify, and delete.
Type: String
Valid Values: `ERRORS_ONLY | SUCCESSES_AND_ERRORS`
Required: No

## See Also
<a name="API_TaskReportConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/TaskReportConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/TaskReportConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/TaskReportConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
