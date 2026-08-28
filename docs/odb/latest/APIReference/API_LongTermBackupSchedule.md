---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_LongTermBackupSchedule.html
---

# LongTermBackupSchedule
<a name="API_LongTermBackupSchedule"></a>

The long-term backup schedule for an Autonomous Database.

## Contents
<a name="API_LongTermBackupSchedule_Contents"></a>

 ** isDisabled **   <a name="odb-Type-LongTermBackupSchedule-isDisabled"></a>
Indicates whether the long-term backup schedule is disabled.
Type: Boolean
Required: No

 ** repeatCadence **   <a name="odb-Type-LongTermBackupSchedule-repeatCadence"></a>
The cadence at which long-term backups are taken.
Type: String
Valid Values: `ONE_TIME | WEEKLY | MONTHLY | YEARLY`
Required: No

 ** retentionPeriodInDays **   <a name="odb-Type-LongTermBackupSchedule-retentionPeriodInDays"></a>
The retention period, in days, for long-term backups.
Type: Integer
Valid Range: Minimum value of 90. Maximum value of 3650.
Required: No

 ** timeOfBackup **   <a name="odb-Type-LongTermBackupSchedule-timeOfBackup"></a>
The date and time at which the long-term backup is taken.
Type: Timestamp
Required: No

## See Also
<a name="API_LongTermBackupSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/LongTermBackupSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/LongTermBackupSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/LongTermBackupSchedule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
