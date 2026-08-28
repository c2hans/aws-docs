---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_CurrentSearchProgress.html
---

# CurrentSearchProgress
<a name="API_BKS_CurrentSearchProgress"></a>

This contains information results retrieved from a search job that may not have completed.

## Contents
<a name="API_BKS_CurrentSearchProgress_Contents"></a>

 ** ItemsMatchedCount **   <a name="Backup-Type-BKS_CurrentSearchProgress-ItemsMatchedCount"></a>
This number is the sum of all items that match the item filters in a search job in progress.
Type: Long
Required: No

 ** ItemsScannedCount **   <a name="Backup-Type-BKS_CurrentSearchProgress-ItemsScannedCount"></a>
This number is the sum of all items that have been scanned so far during a search job.
Type: Long
Required: No

 ** RecoveryPointsScannedCount **   <a name="Backup-Type-BKS_CurrentSearchProgress-RecoveryPointsScannedCount"></a>
This number is the sum of all backups that have been scanned so far during a search job.
Type: Integer
Required: No

## See Also
<a name="API_BKS_CurrentSearchProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/CurrentSearchProgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/CurrentSearchProgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/CurrentSearchProgress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
