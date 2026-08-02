---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsRedshiftClusterDetails.html
---

# AwsRedshiftClusterDetails
<a name="API_AwsRedshiftClusterDetails"></a>

Details about an Amazon Redshift cluster.

## Contents
<a name="API_AwsRedshiftClusterDetails_Contents"></a>

 ** AllowVersionUpgrade **   <a name="securityhub-Type-AwsRedshiftClusterDetails-AllowVersionUpgrade"></a>
Indicates whether major version upgrades are applied automatically to the cluster during the maintenance window.
Type: Boolean
Required: No

 ** AutomatedSnapshotRetentionPeriod **   <a name="securityhub-Type-AwsRedshiftClusterDetails-AutomatedSnapshotRetentionPeriod"></a>
The number of days that automatic cluster snapshots are retained.
Type: Integer
Required: No

 ** AvailabilityZone **   <a name="securityhub-Type-AwsRedshiftClusterDetails-AvailabilityZone"></a>
The name of the Availability Zone in which the cluster is located.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterAvailabilityStatus **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterAvailabilityStatus"></a>
The availability status of the cluster for queries. Possible values are the following:
+  `Available` - The cluster is available for queries.
+  `Unavailable` - The cluster is not available for queries.
+  `Maintenance` - The cluster is intermittently available for queries due to maintenance activities.
+  `Modifying` -The cluster is intermittently available for queries due to changes that modify the cluster.
+  `Failed` - The cluster failed and is not available for queries.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterCreateTime **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterCreateTime"></a>
Indicates when the cluster was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterIdentifier **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterIdentifier"></a>
The unique identifier of the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterNodes **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterNodes"></a>
The nodes in the cluster.
Type: Array of [AwsRedshiftClusterClusterNode](API_AwsRedshiftClusterClusterNode.md) objects
Required: No

 ** ClusterParameterGroups **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterParameterGroups"></a>
The list of cluster parameter groups that are associated with this cluster.
Type: Array of [AwsRedshiftClusterClusterParameterGroup](API_AwsRedshiftClusterClusterParameterGroup.md) objects
Required: No

 ** ClusterPublicKey **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterPublicKey"></a>
The public key for the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterRevisionNumber **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterRevisionNumber"></a>
The specific revision number of the database in the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterSecurityGroups **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterSecurityGroups"></a>
A list of cluster security groups that are associated with the cluster.
Type: Array of [AwsRedshiftClusterClusterSecurityGroup](API_AwsRedshiftClusterClusterSecurityGroup.md) objects
Required: No

 ** ClusterSnapshotCopyStatus **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterSnapshotCopyStatus"></a>
Information about the destination Region and retention period for the cross-Region snapshot copy.
Type: [AwsRedshiftClusterClusterSnapshotCopyStatus](API_AwsRedshiftClusterClusterSnapshotCopyStatus.md) object
Required: No

 ** ClusterStatus **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterStatus"></a>
The current status of the cluster.
Valid values: `available` \| `available, prep-for-resize` \| `available, resize-cleanup` \|` cancelling-resize` \| `creating` \| `deleting` \| `final-snapshot` \| `hardware-failure` \| `incompatible-hsm` \|` incompatible-network` \| `incompatible-parameters` \| `incompatible-restore` \| `modifying` \| `paused` \| `rebooting` \| `renaming` \| `resizing` \| `rotating-keys` \| `storage-full` \| `updating-hsm`
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterSubnetGroupName **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterSubnetGroupName"></a>
The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ClusterVersion **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ClusterVersion"></a>
The version ID of the Amazon Redshift engine that runs on the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DBName **   <a name="securityhub-Type-AwsRedshiftClusterDetails-DBName"></a>
The name of the initial database that was created when the cluster was created.
The same name is returned for the life of the cluster.
If an initial database is not specified, a database named `devdev` is created by default.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeferredMaintenanceWindows **   <a name="securityhub-Type-AwsRedshiftClusterDetails-DeferredMaintenanceWindows"></a>
List of time windows during which maintenance was deferred.
Type: Array of [AwsRedshiftClusterDeferredMaintenanceWindow](API_AwsRedshiftClusterDeferredMaintenanceWindow.md) objects
Required: No

 ** ElasticIpStatus **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ElasticIpStatus"></a>
Information about the status of the Elastic IP (EIP) address.
Type: [AwsRedshiftClusterElasticIpStatus](API_AwsRedshiftClusterElasticIpStatus.md) object
Required: No

 ** ElasticResizeNumberOfNodeOptions **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ElasticResizeNumberOfNodeOptions"></a>
The number of nodes that you can use the elastic resize method to resize the cluster to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Encrypted **   <a name="securityhub-Type-AwsRedshiftClusterDetails-Encrypted"></a>
Indicates whether the data in the cluster is encrypted at rest.
Type: Boolean
Required: No

 ** Endpoint **   <a name="securityhub-Type-AwsRedshiftClusterDetails-Endpoint"></a>
The connection endpoint.
Type: [AwsRedshiftClusterEndpoint](API_AwsRedshiftClusterEndpoint.md) object
Required: No

 ** EnhancedVpcRouting **   <a name="securityhub-Type-AwsRedshiftClusterDetails-EnhancedVpcRouting"></a>
Indicates whether to create the cluster with enhanced VPC routing enabled.
Type: Boolean
Required: No

 ** ExpectedNextSnapshotScheduleTime **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ExpectedNextSnapshotScheduleTime"></a>
Indicates when the next snapshot is expected to be taken. The cluster must have a valid snapshot schedule and have backups enabled.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** ExpectedNextSnapshotScheduleTimeStatus **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ExpectedNextSnapshotScheduleTimeStatus"></a>
The status of the next expected snapshot.
Valid values: `OnTrack` \| `Pending`
Type: String
Pattern: `.*\S.*`
Required: No

 ** HsmStatus **   <a name="securityhub-Type-AwsRedshiftClusterDetails-HsmStatus"></a>
Information about whether the Amazon Redshift cluster finished applying any changes to hardware security module (HSM) settings that were specified in a modify cluster command.
Type: [AwsRedshiftClusterHsmStatus](API_AwsRedshiftClusterHsmStatus.md) object
Required: No

 ** IamRoles **   <a name="securityhub-Type-AwsRedshiftClusterDetails-IamRoles"></a>
A list of IAM roles that the cluster can use to access other AWS services.
Type: Array of [AwsRedshiftClusterIamRole](API_AwsRedshiftClusterIamRole.md) objects
Required: No

 ** KmsKeyId **   <a name="securityhub-Type-AwsRedshiftClusterDetails-KmsKeyId"></a>
The identifier of the AWS KMS encryption key that is used to encrypt data in the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LoggingStatus **   <a name="securityhub-Type-AwsRedshiftClusterDetails-LoggingStatus"></a>
Information about the logging status of the cluster.
Type: [AwsRedshiftClusterLoggingStatus](API_AwsRedshiftClusterLoggingStatus.md) object
Required: No

 ** MaintenanceTrackName **   <a name="securityhub-Type-AwsRedshiftClusterDetails-MaintenanceTrackName"></a>
The name of the maintenance track for the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ManualSnapshotRetentionPeriod **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ManualSnapshotRetentionPeriod"></a>
The default number of days to retain a manual snapshot.
If the value is `-1`, the snapshot is retained indefinitely.
This setting doesn't change the retention period of existing snapshots.
Valid values: Either `-1` or an integer between 1 and 3,653
Type: Integer
Required: No

 ** MasterUsername **   <a name="securityhub-Type-AwsRedshiftClusterDetails-MasterUsername"></a>
The master user name for the cluster. This name is used to connect to the database that is specified in as the value of `DBName`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NextMaintenanceWindowStartTime **   <a name="securityhub-Type-AwsRedshiftClusterDetails-NextMaintenanceWindowStartTime"></a>
Indicates the start of the next maintenance window.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** NodeType **   <a name="securityhub-Type-AwsRedshiftClusterDetails-NodeType"></a>
The node type for the nodes in the cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NumberOfNodes **   <a name="securityhub-Type-AwsRedshiftClusterDetails-NumberOfNodes"></a>
The number of compute nodes in the cluster.
Type: Integer
Required: No

 ** PendingActions **   <a name="securityhub-Type-AwsRedshiftClusterDetails-PendingActions"></a>
A list of cluster operations that are waiting to start.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** PendingModifiedValues **   <a name="securityhub-Type-AwsRedshiftClusterDetails-PendingModifiedValues"></a>
A list of changes to the cluster that are currently pending.
Type: [AwsRedshiftClusterPendingModifiedValues](API_AwsRedshiftClusterPendingModifiedValues.md) object
Required: No

 ** PreferredMaintenanceWindow **   <a name="securityhub-Type-AwsRedshiftClusterDetails-PreferredMaintenanceWindow"></a>
The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.
Format: ` <day>:HH:MM-<day>:HH:MM`
For the day values, use `mon` \| `tue` \| `wed` \| `thu` \| `fri` \| `sat` \| `sun`
For example, `sun:09:32-sun:10:02`
Type: String
Pattern: `.*\S.*`
Required: No

 ** PubliclyAccessible **   <a name="securityhub-Type-AwsRedshiftClusterDetails-PubliclyAccessible"></a>
Whether the cluster can be accessed from a public network.
Type: Boolean
Required: No

 ** ResizeInfo **   <a name="securityhub-Type-AwsRedshiftClusterDetails-ResizeInfo"></a>
Information about the resize operation for the cluster.
Type: [AwsRedshiftClusterResizeInfo](API_AwsRedshiftClusterResizeInfo.md) object
Required: No

 ** RestoreStatus **   <a name="securityhub-Type-AwsRedshiftClusterDetails-RestoreStatus"></a>
Information about the status of a cluster restore action. Only applies to a cluster that was created by restoring a snapshot.
Type: [AwsRedshiftClusterRestoreStatus](API_AwsRedshiftClusterRestoreStatus.md) object
Required: No

 ** SnapshotScheduleIdentifier **   <a name="securityhub-Type-AwsRedshiftClusterDetails-SnapshotScheduleIdentifier"></a>
A unique identifier for the cluster snapshot schedule.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SnapshotScheduleState **   <a name="securityhub-Type-AwsRedshiftClusterDetails-SnapshotScheduleState"></a>
The current state of the cluster snapshot schedule.
Valid values: `MODIFYING` \| `ACTIVE` \| `FAILED`
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsRedshiftClusterDetails-VpcId"></a>
The identifier of the VPC that the cluster is in, if the cluster is in a VPC.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcSecurityGroups **   <a name="securityhub-Type-AwsRedshiftClusterDetails-VpcSecurityGroups"></a>
The list of VPC security groups that the cluster belongs to, if the cluster is in a VPC.
Type: Array of [AwsRedshiftClusterVpcSecurityGroup](API_AwsRedshiftClusterVpcSecurityGroup.md) objects
Required: No

## See Also
<a name="API_AwsRedshiftClusterDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsRedshiftClusterDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsRedshiftClusterDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsRedshiftClusterDetails)
