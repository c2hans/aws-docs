---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_RestoreAccessBackupVaultListMember.html
---

# RestoreAccessBackupVaultListMember
<a name="API_RestoreAccessBackupVaultListMember"></a>

Contains information about a restore access backup vault.

## Contents
<a name="API_RestoreAccessBackupVaultListMember_Contents"></a>

 ** ApprovalDate **   <a name="Backup-Type-RestoreAccessBackupVaultListMember-ApprovalDate"></a>
The date and time when the restore access backup vault was approved.
Type: Timestamp
Required: No

 ** CreationDate **   <a name="Backup-Type-RestoreAccessBackupVaultListMember-CreationDate"></a>
The date and time when the restore access backup vault was created.
Type: Timestamp
Required: No

 ** LatestRevokeRequest **   <a name="Backup-Type-RestoreAccessBackupVaultListMember-LatestRevokeRequest"></a>
Information about the latest request to revoke access to this backup vault.
Type: [LatestRevokeRequest](API_LatestRevokeRequest.md) object
Required: No

 ** RestoreAccessBackupVaultArn **   <a name="Backup-Type-RestoreAccessBackupVaultListMember-RestoreAccessBackupVaultArn"></a>
The ARN of the restore access backup vault.
Type: String
Required: No

 ** VaultState **   <a name="Backup-Type-RestoreAccessBackupVaultListMember-VaultState"></a>
The current state of the restore access backup vault.
Type: String
Valid Values: `CREATING | AVAILABLE | FAILED`
Required: No

## See Also
<a name="API_RestoreAccessBackupVaultListMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/RestoreAccessBackupVaultListMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/RestoreAccessBackupVaultListMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/RestoreAccessBackupVaultListMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
