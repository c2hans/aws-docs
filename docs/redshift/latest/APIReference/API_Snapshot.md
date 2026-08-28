---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_Snapshot.html
---

# Snapshot
<a name="API_Snapshot"></a>

Describes a snapshot.

## Contents
<a name="API_Snapshot_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountsWithRestoreAccess.AccountWithRestoreAccess.N **
A list of the AWS accounts authorized to restore the snapshot. Returns `null` if no accounts are authorized. Visible only to the snapshot owner.
Type: Array of [AccountWithRestoreAccess](API_AccountWithRestoreAccess.md) objects
Required: No

 ** ActualIncrementalBackupSizeInMegaBytes **
The size of the incremental backup.
Type: Double
Required: No

 ** AvailabilityZone **
The Availability Zone in which the cluster was created.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** BackupProgressInMegaBytes **
The number of megabytes that have been transferred to the snapshot backup.
Type: Double
Required: No

 ** ClusterCreateTime **
The time (UTC) when the cluster was originally created.
Type: Timestamp
Required: No

 ** ClusterIdentifier **
The identifier of the cluster for which the snapshot was taken.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ClusterVersion **
The version ID of the Amazon Redshift engine that is running on the cluster.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** CurrentBackupRateInMegaBytesPerSecond **
The number of megabytes per second being transferred to the snapshot backup. Returns `0` for a completed backup.
Type: Double
Required: No

 ** DBName **
The name of the database that was created when the cluster was created.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ElapsedTimeInSeconds **
The amount of time an in-progress snapshot backup has been running, or the amount of time it took a completed backup to finish.
Type: Long
Required: No

 ** Encrypted **
If `true`, the data in the snapshot is encrypted at rest.
Type: Boolean
Required: No

 ** EncryptedWithHSM **
A boolean that indicates whether the snapshot data is encrypted using the HSM keys of the source cluster. `true` indicates that the data is encrypted using HSM keys.
Type: Boolean
Required: No

 ** EngineFullVersion **
The cluster version of the cluster used to create the snapshot. For example, 1.0.15503.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** EnhancedVpcRouting **
An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see [Enhanced VPC Routing](https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html) in the Amazon Redshift Cluster Management Guide.
If this option is `true`, enhanced VPC routing is enabled.
Default: false
Type: Boolean
Required: No

 ** EstimatedSecondsToCompletion **
The estimate of the time remaining before the snapshot backup will complete. Returns `0` for a completed backup.
Type: Long
Required: No

 ** KmsKeyId **
The AWS Key Management Service (KMS) key ID of the encryption key that was used to encrypt data in the cluster from which the snapshot was taken.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** MaintenanceTrackName **
The name of the maintenance track for the snapshot.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** ManualSnapshotRemainingDays **
The number of days until a manual snapshot will pass its retention period.
Type: Integer
Required: No

 ** ManualSnapshotRetentionPeriod **
The number of days that a manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely.
The value must be either -1 or an integer between 1 and 3,653.
Type: Integer
Required: No

 ** MasterPasswordSecretArn **
The Amazon Resource Name (ARN) for the cluster's admin user credentials secret.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** MasterPasswordSecretKmsKeyId **
The ID of the AWS Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** MasterUsername **
The admin user name for the cluster.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** NodeType **
The node type of the nodes in the cluster.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** NumberOfNodes **
The number of nodes in the cluster.
Type: Integer
Required: No

 ** OwnerAccount **
For manual snapshots, the AWS account used to create or copy the snapshot. For automatic snapshots, the owner of the cluster. The owner can perform all snapshot actions, such as sharing a manual snapshot.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Port **
The port that the cluster is listening on.
Type: Integer
Required: No

 ** RestorableNodeTypes.NodeType.N **
The list of node types that this cluster snapshot is able to restore into.
Type: Array of strings
Length Constraints: Maximum length of 2147483647.
Required: No

 ** SnapshotArn **
The Amazon Resource Name (ARN) of the snapshot.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** SnapshotCreateTime **
The time (in UTC format) when Amazon Redshift began the snapshot. A snapshot contains a copy of the cluster data as of this exact time.
Type: Timestamp
Required: No

 ** SnapshotIdentifier **
The snapshot identifier that is provided in the request.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** SnapshotRetentionStartTime **
A timestamp representing the start of the retention period for the snapshot.
Type: Timestamp
Required: No

 ** SnapshotType **
The snapshot type. Snapshots created using [CreateClusterSnapshot](API_CreateClusterSnapshot.md) and [CopyClusterSnapshot](API_CopyClusterSnapshot.md) are of type "manual".
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** SourceRegion **
The source region from which the snapshot was copied.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Status **
The snapshot status. The value of the status depends on the API operation used:
+  [CreateClusterSnapshot](API_CreateClusterSnapshot.md) and [CopyClusterSnapshot](API_CopyClusterSnapshot.md) returns status as "creating".
+  [DescribeClusterSnapshots](API_DescribeClusterSnapshots.md) returns status as "creating", "available", "final snapshot", or "failed".
+  [DeleteClusterSnapshot](API_DeleteClusterSnapshot.md) returns status as "deleted".
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Tags.Tag.N **
The list of tags for the cluster snapshot.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TotalBackupSizeInMegaBytes **
The size of the complete set of backup data that would be used to restore the cluster.
Type: Double
Required: No

 ** VpcId **
The VPC identifier of the cluster if the snapshot is from a cluster in a VPC. Otherwise, this field is not in the output.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

## See Also
<a name="API_Snapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/Snapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/Snapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/Snapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
