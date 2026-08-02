---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_SearchScope.html
---

# SearchScope
<a name="API_BKS_SearchScope"></a>

The search scope is all backup properties input into a search.

## Contents
<a name="API_BKS_SearchScope_Contents"></a>

 ** BackupResourceTypes **   <a name="Backup-Type-BKS_SearchScope-BackupResourceTypes"></a>
The resource types included in a search.
Eligible resource types include S3 and EBS.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `S3 | EBS`
Required: Yes

 ** BackupResourceArns **   <a name="Backup-Type-BKS_SearchScope-BackupResourceArns"></a>
The Amazon Resource Name (ARN) that uniquely identifies the backup resources.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** BackupResourceCreationTime **   <a name="Backup-Type-BKS_SearchScope-BackupResourceCreationTime"></a>
This is the time a backup resource was created.
Type: [BackupCreationTimeFilter](API_BKS_BackupCreationTimeFilter.md) object
Required: No

 ** BackupResourceTags **   <a name="Backup-Type-BKS_SearchScope-BackupResourceTags"></a>
These are one or more tags on the backup (recovery point).
Type: String to string map
Required: No

 ** SourceResourceArns **   <a name="Backup-Type-BKS_SearchScope-SourceResourceArns"></a>
The Amazon Resource Name (ARN) that uniquely identifies the source resources.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_BKS_SearchScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/SearchScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/SearchScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/SearchScope)
