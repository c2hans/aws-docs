---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_TaskScheduleDetails.html
---

# TaskScheduleDetails
<a name="API_TaskScheduleDetails"></a>

Provides information about your AWS DataSync [task schedule](https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html).

## Contents
<a name="API_TaskScheduleDetails_Contents"></a>

 ** DisabledBy **   <a name="DataSync-Type-TaskScheduleDetails-DisabledBy"></a>
Indicates how your task schedule was disabled.
+  `USER` - Your schedule was manually disabled by using the [UpdateTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateTask.html) operation or DataSync console.
+  `SERVICE` - Your schedule was automatically disabled by DataSync because the task failed repeatedly with the same error.
Type: String
Valid Values: `USER | SERVICE`
Required: No

 ** DisabledReason **   <a name="DataSync-Type-TaskScheduleDetails-DisabledReason"></a>
Provides a reason if the task schedule is disabled.
If your schedule is disabled by `USER`, you see a `Manually disabled by user.` message.
If your schedule is disabled by `SERVICE`, you see an error message to help you understand why the task keeps failing. For information on resolving DataSync errors, see [Troubleshooting issues with DataSync transfers](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-locations-tasks.html).
Type: String
Length Constraints: Maximum length of 8192.
Pattern: `^[\w\s.,'?!:;\/=|<>()-]*$`
Required: No

 ** StatusUpdateTime **   <a name="DataSync-Type-TaskScheduleDetails-StatusUpdateTime"></a>
Indicates the last time the status of your task schedule changed. For example, if DataSync automatically disables your schedule because of a repeated error, you can see when the schedule was disabled.
Type: Timestamp
Required: No

## See Also
<a name="API_TaskScheduleDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/TaskScheduleDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/TaskScheduleDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/TaskScheduleDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
