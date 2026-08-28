---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AutonomousDatabaseBackupSummary.html
---

# AutonomousDatabaseBackupSummary
<a name="API_AutonomousDatabaseBackupSummary"></a>

A summary of an Autonomous Database backup.

## Contents
<a name="API_AutonomousDatabaseBackupSummary_Contents"></a>

 ** autonomousDatabaseBackupArn **   <a name="odb-Type-AutonomousDatabaseBackupSummary-autonomousDatabaseBackupArn"></a>
The Amazon Resource Name (ARN) of the Autonomous Database backup.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-z0-9-_]{6,64}`
Required: No

 ** autonomousDatabaseBackupId **   <a name="odb-Type-AutonomousDatabaseBackupSummary-autonomousDatabaseBackupId"></a>
The unique identifier of the Autonomous Database backup.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** autonomousDatabaseId **   <a name="odb-Type-AutonomousDatabaseBackupSummary-autonomousDatabaseId"></a>
The unique identifier of the Autonomous Database that the backup was created from.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 64.
Pattern: `[a-zA-Z0-9_~.-]+`
Required: No

 ** dbVersion **   <a name="odb-Type-AutonomousDatabaseBackupSummary-dbVersion"></a>
The Oracle Database software version of the Autonomous Database backup.
Type: String
Required: No

 ** displayName **   <a name="odb-Type-AutonomousDatabaseBackupSummary-displayName"></a>
The user-friendly name of the Autonomous Database backup.
Type: String
Required: No

 ** isAutomatic **   <a name="odb-Type-AutonomousDatabaseBackupSummary-isAutomatic"></a>
Indicates whether the backup was created automatically.
Type: Boolean
Required: No

 ** ocid **   <a name="odb-Type-AutonomousDatabaseBackupSummary-ocid"></a>
The Oracle Cloud Identifier (OCID) of the Autonomous Database backup.
Type: String
Required: No

 ** retentionPeriodInDays **   <a name="odb-Type-AutonomousDatabaseBackupSummary-retentionPeriodInDays"></a>
The retention period, in days, for the Autonomous Database backup.
Type: Integer
Required: No

 ** sizeInTBs **   <a name="odb-Type-AutonomousDatabaseBackupSummary-sizeInTBs"></a>
The size of the Autonomous Database backup, in terabytes (TB).
Type: Double
Required: No

 ** status **   <a name="odb-Type-AutonomousDatabaseBackupSummary-status"></a>
The current status of the Autonomous Database backup.
Type: String
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | FAILED`
Required: No

 ** statusReason **   <a name="odb-Type-AutonomousDatabaseBackupSummary-statusReason"></a>
Additional information about the current status of the Autonomous Database backup, if applicable.
Type: String
Required: No

 ** timeAvailableTill **   <a name="odb-Type-AutonomousDatabaseBackupSummary-timeAvailableTill"></a>
The date and time until which the Autonomous Database backup is available for restore.
Type: Timestamp
Required: No

 ** timeEnded **   <a name="odb-Type-AutonomousDatabaseBackupSummary-timeEnded"></a>
The date and time when the Autonomous Database backup ended.
Type: Timestamp
Required: No

 ** timeStarted **   <a name="odb-Type-AutonomousDatabaseBackupSummary-timeStarted"></a>
The date and time when the Autonomous Database backup started.
Type: Timestamp
Required: No

 ** type **   <a name="odb-Type-AutonomousDatabaseBackupSummary-type"></a>
The type of the Autonomous Database backup.
Type: String
Valid Values: `INCREMENTAL | FULL | LONGTERM | VIRTUAL_FULL | CUMULATIVE_INCREMENTAL | ROLL_FORWARD_IMAGE_COPY`
Required: No

## See Also
<a name="API_AutonomousDatabaseBackupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AutonomousDatabaseBackupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AutonomousDatabaseBackupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AutonomousDatabaseBackupSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
