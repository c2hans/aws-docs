---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BKS_SearchJobSummary.html
---

# SearchJobSummary
<a name="API_BKS_SearchJobSummary"></a>

This is information pertaining to a search job.

## Contents
<a name="API_BKS_SearchJobSummary_Contents"></a>

 ** CompletionTime **   <a name="Backup-Type-BKS_SearchJobSummary-CompletionTime"></a>
This is the completion time of the search job.
Type: Timestamp
Required: No

 ** CreationTime **   <a name="Backup-Type-BKS_SearchJobSummary-CreationTime"></a>
This is the creation time of the search job.
Type: Timestamp
Required: No

 ** Name **   <a name="Backup-Type-BKS_SearchJobSummary-Name"></a>
This is the name of the search job.
Type: String
Required: No

 ** SearchJobArn **   <a name="Backup-Type-BKS_SearchJobSummary-SearchJobArn"></a>
The unique string that identifies the Amazon Resource Name (ARN) of the specified search job.
Type: String
Required: No

 ** SearchJobIdentifier **   <a name="Backup-Type-BKS_SearchJobSummary-SearchJobIdentifier"></a>
The unique string that specifies the search job.
Type: String
Required: No

 ** SearchScopeSummary **   <a name="Backup-Type-BKS_SearchJobSummary-SearchScopeSummary"></a>
Returned summary of the specified search job scope, including:
+ TotalBackupsToScanCount, the number of recovery points returned by the search.
+ TotalItemsToScanCount, the number of items returned by the search.
Type: [SearchScopeSummary](API_BKS_SearchScopeSummary.md) object
Required: No

 ** Status **   <a name="Backup-Type-BKS_SearchJobSummary-Status"></a>
This is the status of the search job.
Type: String
Valid Values: `RUNNING | COMPLETED | STOPPING | STOPPED | FAILED`
Required: No

 ** StatusMessage **   <a name="Backup-Type-BKS_SearchJobSummary-StatusMessage"></a>
A status message will be returned for either a earch job with a status of `ERRORED` or a status of `COMPLETED` jobs with issues.
For example, a message may say that a search contained recovery points unable to be scanned because of a permissions issue.
Type: String
Required: No

## See Also
<a name="API_BKS_SearchJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backupsearch-2018-05-10/SearchJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backupsearch-2018-05-10/SearchJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backupsearch-2018-05-10/SearchJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Backup. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-backup` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
