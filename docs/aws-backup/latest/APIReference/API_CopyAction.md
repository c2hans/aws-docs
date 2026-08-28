---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CopyAction.html
---

# CopyAction
<a name="API_CopyAction"></a>

The details of the copy operation.

## Contents
<a name="API_CopyAction_Contents"></a>

 ** DestinationBackupVaultArn **   <a name="Backup-Type-CopyAction-DestinationBackupVaultArn"></a>
An Amazon Resource Name (ARN) that uniquely identifies the destination backup vault for the copied backup. For example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.
Type: String
Required: Yes

 ** Lifecycle **   <a name="Backup-Type-CopyAction-Lifecycle"></a>
Specifies the time period, in days, before a recovery point transitions to cold storage or is deleted.
Backups transitioned to cold storage must be stored in cold storage for a minimum of 90 days. Therefore, on the console, the retention setting must be 90 days greater than the transition to cold after days setting. The transition to cold after days setting can't be changed after a backup has been transitioned to cold.
Resource types that can transition to cold storage are listed in the [Feature availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-availability.html#features-by-resource) table. AWS Backup ignores this expression for other resource types.
To remove the existing lifecycle and retention periods and keep your recovery points indefinitely, specify -1 for `MoveToColdStorageAfterDays` and `DeleteAfterDays`.
Type: [Lifecycle](API_Lifecycle.md) object
Required: No

## See Also
<a name="API_CopyAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/CopyAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/CopyAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/CopyAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
