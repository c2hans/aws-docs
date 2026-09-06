---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_TaskSchedule.html
---

# TaskSchedule
<a name="API_TaskSchedule"></a>

Configures your AWS DataSync task to run on a [schedule](https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html) (at a minimum interval of 1 hour).

## Contents
<a name="API_TaskSchedule_Contents"></a>

 ** ScheduleExpression **   <a name="DataSync-Type-TaskSchedule-ScheduleExpression"></a>
Specifies your task schedule by using a cron or rate expression.
Use cron expressions for task schedules that run on a specific time and day. For example, the following cron expression creates a task schedule that runs at 8 AM on the first Wednesday of every month:
 `cron(0 8 * * 3#1)`
Use rate expressions for task schedules that run on a regular interval. For example, the following rate expression creates a task schedule that runs every 12 hours:
 `rate(12 hours)`
For information about cron and rate expression syntax, see the [*Amazon EventBridge User Guide*](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html).
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^[a-zA-Z0-9\ \_\*\?\,\|\^\-\/\#\s\(\)\+]*$`
Required: Yes

 ** Status **   <a name="DataSync-Type-TaskSchedule-Status"></a>
Specifies whether to enable or disable your task schedule. Your schedule is enabled by default, but there can be situations where you need to disable it. For example, you might need to pause a recurring transfer to fix an issue with your task or perform maintenance on your storage system.
DataSync might disable your schedule automatically if your task fails repeatedly with the same error. For more information, see [TaskScheduleDetails](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskScheduleDetails.html).
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_TaskSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/TaskSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/TaskSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/TaskSchedule)
