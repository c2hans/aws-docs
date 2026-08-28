---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_EBSResultItem.html
---

# EBSResultItem
<a name="API_BKS_EBSResultItem"></a>

These are the items returned in the results of a search of Amazon EBS backup metadata.

## Contents
<a name="API_BKS_EBSResultItem_Contents"></a>

 ** BackupResourceArn **   <a name="Backup-Type-BKS_EBSResultItem-BackupResourceArn"></a>
These are one or more items in the results that match values for the Amazon Resource Name (ARN) of recovery points returned in a search of Amazon EBS backup metadata.
Type: String
Required: No

 ** BackupVaultName **   <a name="Backup-Type-BKS_EBSResultItem-BackupVaultName"></a>
The name of the backup vault.
Type: String
Required: No

 ** CreationTime **   <a name="Backup-Type-BKS_EBSResultItem-CreationTime"></a>
These are one or more items in the results that match values for creation times returned in a search of Amazon EBS backup metadata.
Type: Timestamp
Required: No

 ** FilePath **   <a name="Backup-Type-BKS_EBSResultItem-FilePath"></a>
These are one or more items in the results that match values for file paths returned in a search of Amazon EBS backup metadata.
Type: String
Required: No

 ** FileSize **   <a name="Backup-Type-BKS_EBSResultItem-FileSize"></a>
These are one or more items in the results that match values for file sizes returned in a search of Amazon EBS backup metadata.
Type: Long
Required: No

 ** FileSystemIdentifier **   <a name="Backup-Type-BKS_EBSResultItem-FileSystemIdentifier"></a>
These are one or more items in the results that match values for file systems returned in a search of Amazon EBS backup metadata.
Type: String
Required: No

 ** LastModifiedTime **   <a name="Backup-Type-BKS_EBSResultItem-LastModifiedTime"></a>
These are one or more items in the results that match values for Last Modified Time returned in a search of Amazon EBS backup metadata.
Type: Timestamp
Required: No

 ** SourceResourceArn **   <a name="Backup-Type-BKS_EBSResultItem-SourceResourceArn"></a>
These are one or more items in the results that match values for the Amazon Resource Name (ARN) of source resources returned in a search of Amazon EBS backup metadata.
Type: String
Required: No

## See Also
<a name="API_BKS_EBSResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/EBSResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/EBSResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/EBSResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
