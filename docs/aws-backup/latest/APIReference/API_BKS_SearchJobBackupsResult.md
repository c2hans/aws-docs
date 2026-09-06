---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_SearchJobBackupsResult.html
---

# SearchJobBackupsResult
<a name="API_BKS_SearchJobBackupsResult"></a>

This contains the information about recovery points returned in results of a search job.

## Contents
<a name="API_BKS_SearchJobBackupsResult_Contents"></a>

 ** BackupCreationTime **   <a name="Backup-Type-BKS_SearchJobBackupsResult-BackupCreationTime"></a>
This is the creation time of the backup (recovery point).
Type: Timestamp
Required: No

 ** BackupResourceArn **   <a name="Backup-Type-BKS_SearchJobBackupsResult-BackupResourceArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the backup resources.
Type: String
Required: No

 ** IndexCreationTime **   <a name="Backup-Type-BKS_SearchJobBackupsResult-IndexCreationTime"></a>
This is the creation time of the backup index.
Type: Timestamp
Required: No

 ** ResourceType **   <a name="Backup-Type-BKS_SearchJobBackupsResult-ResourceType"></a>
This is the resource type of the search.
Type: String
Valid Values: `S3 | EBS`
Required: No

 ** SourceResourceArn **   <a name="Backup-Type-BKS_SearchJobBackupsResult-SourceResourceArn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the source resources.
Type: String
Required: No

 ** Status **   <a name="Backup-Type-BKS_SearchJobBackupsResult-Status"></a>
This is the status of the search job backup result.
Type: String
Valid Values: `RUNNING | COMPLETED | STOPPING | STOPPED | FAILED`
Required: No

 ** StatusMessage **   <a name="Backup-Type-BKS_SearchJobBackupsResult-StatusMessage"></a>
This is the status message included with the results.
Type: String
Required: No

## See Also
<a name="API_BKS_SearchJobBackupsResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/SearchJobBackupsResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/SearchJobBackupsResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/SearchJobBackupsResult)
