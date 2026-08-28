---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ClusterSnapshotCopyStatus.html
---

# ClusterSnapshotCopyStatus
<a name="API_ClusterSnapshotCopyStatus"></a>

Returns the destination region and retention period that are configured for cross-region snapshot copy.

## Contents
<a name="API_ClusterSnapshotCopyStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DestinationRegion **
The destination region that snapshots are automatically copied to when cross-region snapshot copy is enabled.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ManualSnapshotRetentionPeriod **
The number of days that automated snapshots are retained in the destination region after they are copied from a source region. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.
Type: Integer
Required: No

 ** RetentionPeriod **
The number of days that automated snapshots are retained in the destination region after they are copied from a source region.
Type: Long
Required: No

 ** SnapshotCopyGrantName **
The name of the snapshot copy grant.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_ClusterSnapshotCopyStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ClusterSnapshotCopyStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ClusterSnapshotCopyStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ClusterSnapshotCopyStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
