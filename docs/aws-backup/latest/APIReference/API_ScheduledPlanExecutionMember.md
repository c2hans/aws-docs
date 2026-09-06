---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ScheduledPlanExecutionMember.html
---

# ScheduledPlanExecutionMember
<a name="API_ScheduledPlanExecutionMember"></a>

Contains information about a scheduled backup plan execution, including the execution time, rule type, and associated rule identifier.

## Contents
<a name="API_ScheduledPlanExecutionMember_Contents"></a>

 ** ExecutionTime **   <a name="Backup-Type-ScheduledPlanExecutionMember-ExecutionTime"></a>
The timestamp when the backup is scheduled to run, in Unix format and Coordinated Universal Time (UTC). The value is accurate to milliseconds.
Type: Timestamp
Required: No

 ** RuleExecutionType **   <a name="Backup-Type-ScheduledPlanExecutionMember-RuleExecutionType"></a>
The type of backup rule execution. Valid values are `CONTINUOUS` (point-in-time recovery), `SNAPSHOTS` (snapshot backups), or `CONTINUOUS_AND_SNAPSHOTS` (both types combined).
Type: String
Valid Values: `CONTINUOUS | SNAPSHOTS | CONTINUOUS_AND_SNAPSHOTS`
Required: No

 ** RuleId **   <a name="Backup-Type-ScheduledPlanExecutionMember-RuleId"></a>
The unique identifier of the backup rule that will execute at the scheduled time.
Type: String
Required: No

## See Also
<a name="API_ScheduledPlanExecutionMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/ScheduledPlanExecutionMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/ScheduledPlanExecutionMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/ScheduledPlanExecutionMember)
