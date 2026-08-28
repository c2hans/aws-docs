---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_SearchScopeSummary.html
---

# SearchScopeSummary
<a name="API_BKS_SearchScopeSummary"></a>

The summary of the specified search job scope, including:
+ TotalBackupsToScanCount, the number of recovery points returned by the search.
+ TotalItemsToScanCount, the number of items returned by the search.

## Contents
<a name="API_BKS_SearchScopeSummary_Contents"></a>

 ** TotalItemsToScanCount **   <a name="Backup-Type-BKS_SearchScopeSummary-TotalItemsToScanCount"></a>
This is the count of the total number of items that will be scanned in a search.
Type: Long
Required: No

 ** TotalRecoveryPointsToScanCount **   <a name="Backup-Type-BKS_SearchScopeSummary-TotalRecoveryPointsToScanCount"></a>
This is the count of the total number of backups that will be scanned in a search.
Type: Integer
Required: No

## See Also
<a name="API_BKS_SearchScopeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/SearchScopeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/SearchScopeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/SearchScopeSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
