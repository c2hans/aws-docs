---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_DBCluster.html
---

# DBCluster
<a name="API_DBCluster"></a>

Contains the details of an Amazon Neptune DB cluster.

This data type is used as a response element in the [DescribeDBClusters](API_DescribeDBClusters.md).

## Contents
<a name="API_DBCluster_Contents"></a>

 ** AllocatedStorage **
 `AllocatedStorage` always returns 1, because Neptune DB cluster storage size is not fixed, but instead automatically adjusts as needed.
Type: Integer
Required: No

 ** AssociatedRoles.DBClusterRole.N **
Provides a list of the Amazon Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other Amazon services on your behalf.
Type: Array of [DBClusterRole](API_DBClusterRole.md) objects
Required: No

 ** AutomaticRestartTime **
Time at which the DB cluster will be automatically restarted.
Type: Timestamp
Required: No

 ** AvailabilityZones.AvailabilityZone.N **
Provides the list of EC2 Availability Zones that instances in the DB cluster can be created in.
Type: Array of strings
Required: No

 ** BackupRetentionPeriod **
Specifies the number of days for which automatic DB snapshots are retained.
Type: Integer
Required: No

 ** CharacterSetName **
Not supported by Neptune.
Type: String
Required: No

 ** CloneGroupId **
Identifies the clone group to which the DB cluster is associated.
Type: String
Required: No

 ** ClusterCreateTime **
Specifies the time when the DB cluster was created, in Universal Coordinated Time (UTC).
Type: Timestamp
Required: No

 ** CopyTagsToSnapshot **
 *If set to `true`, tags are copied to any snapshot of the DB cluster that is created.*
Type: Boolean
Required: No

 ** CrossAccountClone **
If set to `true`, the DB cluster can be cloned across accounts.
Type: Boolean
Required: No

 ** DatabaseName **
Contains the name of the initial database of this DB cluster that was provided at create time, if one was specified when the DB cluster was created. This same name is returned for the life of the DB cluster.
Type: String
Required: No

 ** DBClusterArn **
The Amazon Resource Name (ARN) for the DB cluster.
Type: String
Required: No

 ** DBClusterIdentifier **
Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.
Type: String
Required: No

 ** DBClusterMembers.DBClusterMember.N **
Provides the list of instances that make up the DB cluster.
Type: Array of [DBClusterMember](API_DBClusterMember.md) objects
Required: No

 ** DBClusterOptionGroupMemberships.DBClusterOptionGroup.N **
Not supported by Neptune.
Type: Array of [DBClusterOptionGroupStatus](API_DBClusterOptionGroupStatus.md) objects
Required: No

 ** DBClusterParameterGroup **
Specifies the name of the DB cluster parameter group for the DB cluster.
Type: String
Required: No

 ** DbClusterResourceId **
The Amazon Region-unique, immutable identifier for the DB cluster. This identifier is found in Amazon CloudTrail log entries whenever the Amazon KMS key for the DB cluster is accessed.
Type: String
Required: No

 ** DBSubnetGroup **
Specifies information on the subnet group associated with the DB cluster, including the name, description, and subnets in the subnet group.
Type: String
Required: No

 ** DeletionProtection **
Indicates whether or not the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled.
Type: Boolean
Required: No

 ** EarliestRestorableTime **
Specifies the earliest time to which a database can be restored with point-in-time restore.
Type: Timestamp
Required: No

 ** EnabledCloudwatchLogsExports.member.N **
A list of the log types that this DB cluster is configured to export to CloudWatch Logs. Valid log types are: `audit` (to publish audit logs to CloudWatch) and slowquery (to publish slow-query logs to CloudWatch). See [Publishing Neptune logs to Amazon CloudWatch logs](https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html).
Type: Array of strings
Required: No

 ** Endpoint **
Specifies the connection endpoint for the primary instance of the DB cluster.
Type: String
Required: No

 ** Engine **
Provides the name of the database engine to be used for this DB cluster.
Type: String
Required: No

 ** EngineVersion **
Indicates the database engine version.
Type: String
Required: No

 ** GlobalClusterIdentifier **
Contains a user-supplied global database cluster identifier. This identifier is the unique key that identifies a global database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z][0-9A-Za-z-:._]*`
Required: No

 ** HostedZoneId **
Specifies the ID that Amazon Route 53 assigns when you create a hosted zone.
Type: String
Required: No

 ** IAMDatabaseAuthenticationEnabled **
True if mapping of Amazon Identity and Access Management (IAM) accounts to database accounts is enabled, and otherwise false.
Type: Boolean
Required: No

 ** IOOptimizedNextAllowedModificationTime **
The next time you can modify the DB cluster to use the `iopt1` storage type.
Type: Timestamp
Required: No

 ** KmsKeyId **
If `StorageEncrypted` is true, the Amazon KMS key identifier for the encrypted DB cluster.
Type: String
Required: No

 ** LatestRestorableTime **
Specifies the latest time to which a database can be restored with point-in-time restore.
Type: Timestamp
Required: No

 ** MasterUsername **
Not supported by Neptune.
Type: String
Required: No

 ** MultiAZ **
Specifies whether the DB cluster has instances in multiple Availability Zones.
Type: Boolean
Required: No

 ** PendingModifiedValues **
This data type is used as a response element in the `ModifyDBCluster` operation and contains changes that will be applied during the next maintenance window.
Type: [ClusterPendingModifiedValues](API_ClusterPendingModifiedValues.md) object
Required: No

 ** PercentProgress **
Specifies the progress of the operation as a percentage.
Type: String
Required: No

 ** Port **
Specifies the port that the database engine is listening on.
Type: Integer
Required: No

 ** PreferredBackupWindow **
Specifies the daily time range during which automated backups are created if automated backups are enabled, as determined by the `BackupRetentionPeriod`.
Type: String
Required: No

 ** PreferredMaintenanceWindow **
Specifies the weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
Type: String
Required: No

 ** ReaderEndpoint **
The reader endpoint for the DB cluster. The reader endpoint for a DB cluster load-balances connections across the Read Replicas that are available in a DB cluster. As clients request new connections to the reader endpoint, Neptune distributes the connection requests among the Read Replicas in the DB cluster. This functionality can help balance your read workload across multiple Read Replicas in your DB cluster.
If a failover occurs, and the Read Replica that you are connected to is promoted to be the primary instance, your connection is dropped. To continue sending your read workload to other Read Replicas in the cluster, you can then reconnect to the reader endpoint.
Type: String
Required: No

 ** ReadReplicaIdentifiers.ReadReplicaIdentifier.N **
Contains one or more identifiers of the Read Replicas associated with this DB cluster.
Type: Array of strings
Required: No

 ** ReplicationSourceIdentifier **
Not supported by Neptune.
Type: String
Required: No

 ** ServerlessV2ScalingConfiguration **
Shows the scaling configuration for a Neptune Serverless DB cluster.
For more information, see [Using Amazon Neptune Serverless](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html) in the *Amazon Neptune User Guide*.
Type: [ServerlessV2ScalingConfigurationInfo](API_ServerlessV2ScalingConfigurationInfo.md) object
Required: No

 ** Status **
Specifies the current state of this DB cluster.
Type: String
Required: No

 ** StorageEncrypted **
Specifies whether the DB cluster is encrypted.
Type: Boolean
Required: No

 ** StorageType **
The storage type used by the DB cluster.
Valid Values:
+  ** `standard` **   –   ( *the default* ) Provides cost-effective database storage for applications with moderate to small I/O usage.
+  ** `iopt1` **   –   Enables [I/O-Optimized storage](https://docs.aws.amazon.com/neptune/latest/userguide/storage-types.html#provisioned-iops-storage) that's designed to meet the needs of I/O-intensive graph workloads that require predictable pricing with low I/O latency and consistent I/O throughput.

  Neptune I/O-Optimized storage is only available starting with engine release 1.3.0.0.
Type: String
Required: No

 ** VpcSecurityGroups.VpcSecurityGroupMembership.N **
Provides a list of VPC security groups that the DB cluster belongs to.
Type: Array of [VpcSecurityGroupMembership](API_VpcSecurityGroupMembership.md) objects
Required: No

## See Also
<a name="API_DBCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/DBCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DBCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/DBCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
