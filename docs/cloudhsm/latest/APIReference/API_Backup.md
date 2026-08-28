---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_Backup.html
---

# Backup
<a name="API_Backup"></a>

Contains information about a backup of an AWS CloudHSM cluster. All backup objects contain the `BackupId`, `BackupState`, `ClusterId`, and `CreateTimestamp` parameters. Backups that were copied into a destination region additionally contain the `CopyTimestamp`, `SourceBackup`, `SourceCluster`, and `SourceRegion` parameters. A backup that is pending deletion will include the `DeleteTimestamp` parameter.

## Contents
<a name="API_Backup_Contents"></a>

 ** BackupId **   <a name="CloudHSMV2-Type-Backup-BackupId"></a>
The identifier (ID) of the backup.
Type: String
Pattern: `backup-[2-7a-zA-Z]{11,16}`
Required: Yes

 ** BackupArn **   <a name="CloudHSMV2-Type-Backup-BackupArn"></a>
The Amazon Resource Name (ARN) of the backup.
Type: String
Pattern: `^(arn:aws(-(us-gov))?:cloudhsm:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]{1}):[0-9]{12}:backup/)?backup-[2-7a-zA-Z]{11,16}`
Required: No

 ** BackupState **   <a name="CloudHSMV2-Type-Backup-BackupState"></a>
The state of the backup.
Type: String
Valid Values: `CREATE_IN_PROGRESS | READY | DELETED | PENDING_DELETION`
Required: No

 ** ClusterId **   <a name="CloudHSMV2-Type-Backup-ClusterId"></a>
The identifier (ID) of the cluster that was backed up.
Type: String
Pattern: `cluster-[2-7a-zA-Z]{11,16}`
Required: No

 ** CopyTimestamp **   <a name="CloudHSMV2-Type-Backup-CopyTimestamp"></a>
The date and time when the backup was copied from a source backup.
Type: Timestamp
Required: No

 ** CreateTimestamp **   <a name="CloudHSMV2-Type-Backup-CreateTimestamp"></a>
The date and time when the backup was created.
Type: Timestamp
Required: No

 ** DeleteTimestamp **   <a name="CloudHSMV2-Type-Backup-DeleteTimestamp"></a>
The date and time when the backup will be permanently deleted.
Type: Timestamp
Required: No

 ** HsmType **   <a name="CloudHSMV2-Type-Backup-HsmType"></a>
The HSM type used to create the backup.
Type: String
Length Constraints: Maximum length of 32.
Pattern: `((p|)hsm[0-9][a-z.]*\.[a-zA-Z]+)`
Required: No

 ** Mode **   <a name="CloudHSMV2-Type-Backup-Mode"></a>
The mode of the cluster that was backed up.
Type: String
Valid Values: `FIPS | NON_FIPS`
Required: No

 ** NeverExpires **   <a name="CloudHSMV2-Type-Backup-NeverExpires"></a>
Specifies whether the service should exempt a backup from the retention policy for the cluster. `True` exempts a backup from the retention policy. `False` means the service applies the backup retention policy defined at the cluster.
Type: Boolean
Required: No

 ** SourceBackup **   <a name="CloudHSMV2-Type-Backup-SourceBackup"></a>
The identifier (ID) of the source backup from which the new backup was copied.
Type: String
Pattern: `backup-[2-7a-zA-Z]{11,16}`
Required: No

 ** SourceCluster **   <a name="CloudHSMV2-Type-Backup-SourceCluster"></a>
The identifier (ID) of the cluster containing the source backup from which the new backup was copied.
Type: String
Pattern: `cluster-[2-7a-zA-Z]{11,16}`
Required: No

 ** SourceRegion **   <a name="CloudHSMV2-Type-Backup-SourceRegion"></a>
The AWS Region that contains the source backup from which the new backup was copied.
Type: String
Pattern: `[a-z]{2}(-(gov))?-(east|west|north|south|central){1,2}-\d`
Required: No

 ** TagList **   <a name="CloudHSMV2-Type-Backup-TagList"></a>
The list of tags for the backup.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## See Also
<a name="API_Backup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/Backup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/Backup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/Backup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
