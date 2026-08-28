---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_S3ResultItem.html
---

# S3ResultItem
<a name="API_BKS_S3ResultItem"></a>

These are the items returned in the results of a search of Amazon S3 backup metadata.

## Contents
<a name="API_BKS_S3ResultItem_Contents"></a>

 ** BackupResourceArn **   <a name="Backup-Type-BKS_S3ResultItem-BackupResourceArn"></a>
These are items in the returned results that match recovery point Amazon Resource Names (ARN) input during a search of Amazon S3 backup metadata.
Type: String
Required: No

 ** BackupVaultName **   <a name="Backup-Type-BKS_S3ResultItem-BackupVaultName"></a>
The name of the backup vault.
Type: String
Required: No

 ** CreationTime **   <a name="Backup-Type-BKS_S3ResultItem-CreationTime"></a>
These are one or more items in the returned results that match values for item creation time input during a search of Amazon S3 backup metadata.
Type: Timestamp
Required: No

 ** ETag **   <a name="Backup-Type-BKS_S3ResultItem-ETag"></a>
These are one or more items in the returned results that match values for ETags input during a search of Amazon S3 backup metadata.
Type: String
Required: No

 ** ObjectKey **   <a name="Backup-Type-BKS_S3ResultItem-ObjectKey"></a>
This is one or more items returned in the results of a search of Amazon S3 backup metadata that match the values input for object key.
Type: String
Required: No

 ** ObjectSize **   <a name="Backup-Type-BKS_S3ResultItem-ObjectSize"></a>
These are items in the returned results that match values for object size(s) input during a search of Amazon S3 backup metadata.
Type: Long
Required: No

 ** SourceResourceArn **   <a name="Backup-Type-BKS_S3ResultItem-SourceResourceArn"></a>
These are items in the returned results that match source Amazon Resource Names (ARN) input during a search of Amazon S3 backup metadata.
Type: String
Required: No

 ** VersionId **   <a name="Backup-Type-BKS_S3ResultItem-VersionId"></a>
These are one or more items in the returned results that match values for version IDs input during a search of Amazon S3 backup metadata.
Type: String
Required: No

## See Also
<a name="API_BKS_S3ResultItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/S3ResultItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/S3ResultItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/S3ResultItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
