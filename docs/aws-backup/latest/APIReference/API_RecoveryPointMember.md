---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RecoveryPointMember.html
---

# RecoveryPointMember
<a name="API_RecoveryPointMember"></a>

This is a recovery point which is a child (nested) recovery point of a parent (composite) recovery point. These recovery points can be disassociated from their parent (composite) recovery point, in which case they will no longer be a member.

## Contents
<a name="API_RecoveryPointMember_Contents"></a>

 ** BackupVaultName **   <a name="Backup-Type-RecoveryPointMember-BackupVaultName"></a>
The name of the backup vault (the logical container in which backups are stored).
Type: String
Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`
Required: No

 ** RecoveryPointArn **   <a name="Backup-Type-RecoveryPointMember-RecoveryPointArn"></a>
The Amazon Resource Name (ARN) of the parent (composite) recovery point.
Type: String
Required: No

 ** ResourceArn **   <a name="Backup-Type-RecoveryPointMember-ResourceArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies a saved resource.
Type: String
Required: No

 ** ResourceType **   <a name="Backup-Type-RecoveryPointMember-ResourceType"></a>
The AWS resource type that is saved as a recovery point.
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

## See Also
<a name="API_RecoveryPointMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RecoveryPointMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
