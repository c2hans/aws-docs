---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_IndexedRecoveryPoint.html
---

# IndexedRecoveryPoint
<a name="API_IndexedRecoveryPoint"></a>

This is a recovery point that has an associated backup index.

Only recovery points with a backup index can be included in a search.

## Contents
<a name="API_IndexedRecoveryPoint_Contents"></a>

 ** BackupCreationDate **   <a name="Backup-Type-IndexedRecoveryPoint-BackupCreationDate"></a>
The date and time that a backup was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** BackupVaultArn **   <a name="Backup-Type-IndexedRecoveryPoint-BackupVaultArn"></a>
An ARN that uniquely identifies the backup vault where the recovery point index is stored.
For example, `arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.
Type: String
Required: No

 ** IamRoleArn **   <a name="Backup-Type-IndexedRecoveryPoint-IamRoleArn"></a>
This specifies the IAM role ARN used for this operation.
For example, arn:aws:iam::123456789012:role/S3Access
Type: String
Required: No

 ** IndexCreationDate **   <a name="Backup-Type-IndexedRecoveryPoint-IndexCreationDate"></a>
The date and time that a backup index was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.
Type: Timestamp
Required: No

 ** IndexStatus **   <a name="Backup-Type-IndexedRecoveryPoint-IndexStatus"></a>
This is the current status for the backup index associated with the specified recovery point.
Statuses are: `PENDING` \| `ACTIVE` \| `FAILED` \| `DELETING`
A recovery point with an index that has the status of `ACTIVE` can be included in a search.
Type: String
Valid Values: `PENDING | ACTIVE | FAILED | DELETING`
Required: No

 ** IndexStatusMessage **   <a name="Backup-Type-IndexedRecoveryPoint-IndexStatusMessage"></a>
A string in the form of a detailed message explaining the status of a backup index associated with the recovery point.
Type: String
Required: No

 ** RecoveryPointArn **   <a name="Backup-Type-IndexedRecoveryPoint-RecoveryPointArn"></a>
An ARN that uniquely identifies a recovery point; for example, `arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`
Type: String
Required: No

 ** ResourceType **   <a name="Backup-Type-IndexedRecoveryPoint-ResourceType"></a>
The resource type of the indexed recovery point.
+  `EBS` for Amazon Elastic Block Store
+  `S3` for Amazon Simple Storage Service (Amazon S3)
Type: String
Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`
Required: No

 ** SourceResourceArn **   <a name="Backup-Type-IndexedRecoveryPoint-SourceResourceArn"></a>
A string of the Amazon Resource Name (ARN) that uniquely identifies the source resource.
Type: String
Required: No

## See Also
<a name="API_IndexedRecoveryPoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-2018-11-15/IndexedRecoveryPoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-2018-11-15/IndexedRecoveryPoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-2018-11-15/IndexedRecoveryPoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
