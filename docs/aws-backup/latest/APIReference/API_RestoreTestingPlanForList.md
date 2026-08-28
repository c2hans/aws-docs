---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RestoreTestingPlanForList.html
---

# RestoreTestingPlanForList
<a name="API_RestoreTestingPlanForList"></a>

This contains metadata about a restore testing plan.

## Contents
<a name="API_RestoreTestingPlanForList_Contents"></a>

 ** CreationTime **   <a name="Backup-Type-RestoreTestingPlanForList-CreationTime"></a>
The date and time that a restore testing plan was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: Yes

 ** RestoreTestingPlanArn **   <a name="Backup-Type-RestoreTestingPlanForList-RestoreTestingPlanArn"></a>
An Amazon Resource Name (ARN) that uniquely identifiesa restore testing plan.
Type: String
Required: Yes

 ** RestoreTestingPlanName **   <a name="Backup-Type-RestoreTestingPlanForList-RestoreTestingPlanName"></a>
The restore testing plan name.
Type: String
Required: Yes

 ** ScheduleExpression **   <a name="Backup-Type-RestoreTestingPlanForList-ScheduleExpression"></a>
A CRON expression in specified timezone when a restore testing plan is executed. When no CRON expression is provided, AWS Backup will use the default expression `cron(0 5 ? * * *)`.
Type: String
Required: Yes

 ** LastExecutionTime **   <a name="Backup-Type-RestoreTestingPlanForList-LastExecutionTime"></a>
The last time a restore test was run with the specified restore testing plan. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of `LastExecutionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** LastUpdateTime **   <a name="Backup-Type-RestoreTestingPlanForList-LastUpdateTime"></a>
The date and time that the restore testing plan was updated. This update is in Unix format and Coordinated Universal Time (UTC). The value of `LastUpdateTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** ScheduleExpressionTimezone **   <a name="Backup-Type-RestoreTestingPlanForList-ScheduleExpressionTimezone"></a>
Optional. This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.
Type: String
Required: No

 ** StartWindowHours **   <a name="Backup-Type-RestoreTestingPlanForList-StartWindowHours"></a>
Defaults to 24 hours.
A value in hours after a restore test is scheduled before a job will be canceled if it doesn't start successfully. This value is optional. If this value is included, this parameter has a maximum value of 168 hours (one week).
Type: Integer
Required: No

## See Also
<a name="API_RestoreTestingPlanForList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RestoreTestingPlanForList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingPlanForList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingPlanForList)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
