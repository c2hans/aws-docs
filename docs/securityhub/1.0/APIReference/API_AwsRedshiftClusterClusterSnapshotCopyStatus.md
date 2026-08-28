---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRedshiftClusterClusterSnapshotCopyStatus.html
---

# AwsRedshiftClusterClusterSnapshotCopyStatus
<a name="API_AwsRedshiftClusterClusterSnapshotCopyStatus"></a>

You can configure Amazon Redshift to copy snapshots for a cluster to another AWS Region. This parameter provides information about a cross-Region snapshot copy.

## Contents
<a name="API_AwsRedshiftClusterClusterSnapshotCopyStatus_Contents"></a>

 ** DestinationRegion **   <a name="securityhub-Type-AwsRedshiftClusterClusterSnapshotCopyStatus-DestinationRegion"></a>
The destination Region that snapshots are automatically copied to when cross-Region snapshot copy is enabled.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ManualSnapshotRetentionPeriod **   <a name="securityhub-Type-AwsRedshiftClusterClusterSnapshotCopyStatus-ManualSnapshotRetentionPeriod"></a>
The number of days that manual snapshots are retained in the destination Region after they are copied from a source Region.
If the value is `-1`, then the manual snapshot is retained indefinitely.
Valid values: Either `-1` or an integer between 1 and 3,653
Type: Integer
Required: No

 ** RetentionPeriod **   <a name="securityhub-Type-AwsRedshiftClusterClusterSnapshotCopyStatus-RetentionPeriod"></a>
The number of days to retain automated snapshots in the destination Region after they are copied from a source Region.
Type: Integer
Required: No

 ** SnapshotCopyGrantName **   <a name="securityhub-Type-AwsRedshiftClusterClusterSnapshotCopyStatus-SnapshotCopyGrantName"></a>
The name of the snapshot copy grant.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsRedshiftClusterClusterSnapshotCopyStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRedshiftClusterClusterSnapshotCopyStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRedshiftClusterClusterSnapshotCopyStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRedshiftClusterClusterSnapshotCopyStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
