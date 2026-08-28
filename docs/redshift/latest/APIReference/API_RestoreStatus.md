---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_RestoreStatus.html
---

# RestoreStatus
<a name="API_RestoreStatus"></a>

Describes the status of a cluster restore action. Returns null if the cluster was not created by restoring a snapshot.

## Contents
<a name="API_RestoreStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CurrentRestoreRateInMegaBytesPerSecond **
The number of megabytes per second being transferred from the backup storage. Returns the average rate for a completed backup. This field is only updated when you restore to DC2 node types.
Type: Double
Required: No

 ** ElapsedTimeInSeconds **
The amount of time an in-progress restore has been running, or the amount of time it took a completed restore to finish. This field is only updated when you restore to DC2 node types.
Type: Long
Required: No

 ** EstimatedTimeToCompletionInSeconds **
The estimate of the time remaining before the restore will complete. Returns 0 for a completed restore. This field is only updated when you restore to DC2 node types.
Type: Long
Required: No

 ** ProgressInMegaBytes **
The number of megabytes that have been transferred from snapshot storage. This field is only updated when you restore to DC2 node types.
Type: Long
Required: No

 ** SnapshotSizeInMegaBytes **
The size of the set of snapshot data used to restore the cluster. This field is only updated when you restore to DC2 node types.
Type: Long
Required: No

 ** Status **
The status of the restore action. Returns starting, restoring, completed, or failed.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_RestoreStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RestoreStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RestoreStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RestoreStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
