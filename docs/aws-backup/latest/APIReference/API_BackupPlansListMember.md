---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BackupPlansListMember.html
---

# BackupPlansListMember
<a name="API_BackupPlansListMember"></a>

Contains metadata about a backup plan.

## Contents
<a name="API_BackupPlansListMember_Contents"></a>

 ** AdvancedBackupSettings **   <a name="Backup-Type-BackupPlansListMember-AdvancedBackupSettings"></a>
Contains a list of `BackupOptions` for a resource type.
Type: Array of [AdvancedBackupSetting](API_AdvancedBackupSetting.md) objects
Required: No

 ** BackupPlanArn **   <a name="Backup-Type-BackupPlansListMember-BackupPlanArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies a backup plan; for example, `arn:aws:backup:us-east-1:123456789012:plan:8F81F553-3A74-4A3F-B93D-B3360DC80C50`.
Type: String
Required: No

 ** BackupPlanId **   <a name="Backup-Type-BackupPlansListMember-BackupPlanId"></a>
Uniquely identifies a backup plan.
Type: String
Required: No

 ** BackupPlanName **   <a name="Backup-Type-BackupPlansListMember-BackupPlanName"></a>
The display name of a saved backup plan.
Type: String
Required: No

 ** CreationDate **   <a name="Backup-Type-BackupPlansListMember-CreationDate"></a>
The date and time a resource backup plan is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** CreatorRequestId **   <a name="Backup-Type-BackupPlansListMember-CreatorRequestId"></a>
A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional.
If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.
Type: String
Required: No

 ** DeletionDate **   <a name="Backup-Type-BackupPlansListMember-DeletionDate"></a>
The date and time a backup plan is deleted, in Unix format and Coordinated Universal Time (UTC). The value of `DeletionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** LastExecutionDate **   <a name="Backup-Type-BackupPlansListMember-LastExecutionDate"></a>
The last time this backup plan was run. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of `LastExecutionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** VersionId **   <a name="Backup-Type-BackupPlansListMember-VersionId"></a>
Unique, randomly generated, Unicode, UTF-8 encoded strings that are at most 1,024 bytes long. Version IDs cannot be edited.
Type: String
Required: No

## See Also
<a name="API_BackupPlansListMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/BackupPlansListMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/BackupPlansListMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/BackupPlansListMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
