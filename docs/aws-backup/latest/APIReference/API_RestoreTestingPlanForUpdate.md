---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RestoreTestingPlanForUpdate.html
---

# RestoreTestingPlanForUpdate
<a name="API_RestoreTestingPlanForUpdate"></a>

This contains metadata about a restore testing plan.

## Contents
<a name="API_RestoreTestingPlanForUpdate_Contents"></a>

 ** RecoveryPointSelection **   <a name="Backup-Type-RestoreTestingPlanForUpdate-RecoveryPointSelection"></a>
Required: `Algorithm`; `RecoveryPointTypes`; `IncludeVaults` (*one or more*).
Optional: *SelectionWindowDays* (*'30' if not specified*); `ExcludeVaults` (defaults to empty list if not listed).
Type: [RestoreTestingRecoveryPointSelection](API_RestoreTestingRecoveryPointSelection.md) object
Required: No

 ** ScheduleExpression **   <a name="Backup-Type-RestoreTestingPlanForUpdate-ScheduleExpression"></a>
A CRON expression in specified timezone when a restore testing plan is executed. When no CRON expression is provided, AWS Backup will use the default expression `cron(0 5 ? * * *)`.
Type: String
Required: No

 ** ScheduleExpressionTimezone **   <a name="Backup-Type-RestoreTestingPlanForUpdate-ScheduleExpressionTimezone"></a>
Optional. This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.
Type: String
Required: No

 ** StartWindowHours **   <a name="Backup-Type-RestoreTestingPlanForUpdate-StartWindowHours"></a>
Defaults to 24 hours.
A value in hours after a restore test is scheduled before a job will be canceled if it doesn't start successfully. This value is optional. If this value is included, this parameter has a maximum value of 168 hours (one week).
Type: Integer
Required: No

## See Also
<a name="API_RestoreTestingPlanForUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RestoreTestingPlanForUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RestoreTestingPlanForUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RestoreTestingPlanForUpdate)
