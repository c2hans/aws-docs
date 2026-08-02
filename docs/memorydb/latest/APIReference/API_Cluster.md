---
source_url: https://docs.aws.amazon.com/memorydb/latest/APIReference/API_Cluster.html
---

# Cluster
<a name="API_Cluster"></a>

Contains all of the attributes of a specific cluster.

## Contents
<a name="API_Cluster_Contents"></a>

 ** ACLName **   <a name="MemoryDB-Type-Cluster-ACLName"></a>
The name of the Access Control List associated with this cluster.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

 ** ARN **   <a name="MemoryDB-Type-Cluster-ARN"></a>
The Amazon Resource Name (ARN) of the cluster.
Type: String
Required: No

 ** AutoMinorVersionUpgrade **   <a name="MemoryDB-Type-Cluster-AutoMinorVersionUpgrade"></a>
When set to true, the cluster will automatically receive minor engine version upgrades after launch.
Type: Boolean
Required: No

 ** AvailabilityMode **   <a name="MemoryDB-Type-Cluster-AvailabilityMode"></a>
Indicates if the cluster has a Multi-AZ configuration (multiaz) or not (singleaz).
Type: String
Valid Values: `singleaz | multiaz`
Required: No

 ** ClusterEndpoint **   <a name="MemoryDB-Type-Cluster-ClusterEndpoint"></a>
The cluster's configuration endpoint
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** DataTiering **   <a name="MemoryDB-Type-Cluster-DataTiering"></a>
Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html).
Type: String
Valid Values: `true | false`
Required: No

 ** Description **   <a name="MemoryDB-Type-Cluster-Description"></a>
A description of the cluster
Type: String
Required: No

 ** Engine **   <a name="MemoryDB-Type-Cluster-Engine"></a>
The name of the engine used by the cluster.
Type: String
Required: No

 ** EnginePatchVersion **   <a name="MemoryDB-Type-Cluster-EnginePatchVersion"></a>
The Redis OSS engine patch version used by the cluster
Type: String
Required: No

 ** EngineVersion **   <a name="MemoryDB-Type-Cluster-EngineVersion"></a>
The Redis OSS engine version used by the cluster
Type: String
Required: No

 ** IpDiscovery **   <a name="MemoryDB-Type-Cluster-IpDiscovery"></a>
The mechanism that the cluster uses to discover IP addresses. Returns 'ipv4' when DNS endpoints resolve to IPv4 addresses, or 'ipv6' when DNS endpoints resolve to IPv6 addresses.
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** KmsKeyId **   <a name="MemoryDB-Type-Cluster-KmsKeyId"></a>
The ID of the KMS key used to encrypt the cluster
Type: String
Required: No

 ** MaintenanceWindow **   <a name="MemoryDB-Type-Cluster-MaintenanceWindow"></a>
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Type: String
Required: No

 ** MultiRegionClusterName **   <a name="MemoryDB-Type-Cluster-MultiRegionClusterName"></a>
The name of the multi-Region cluster that this cluster belongs to.
Type: String
Required: No

 ** Name **   <a name="MemoryDB-Type-Cluster-Name"></a>
The user-supplied name of the cluster. This identifier is a unique key that identifies a cluster.
Type: String
Required: No

 ** NetworkType **   <a name="MemoryDB-Type-Cluster-NetworkType"></a>
The IP address type for the cluster. Returns 'ipv4' for IPv4 only, 'ipv6' for IPv6 only, or 'dual-stack' if the cluster supports both IPv4 and IPv6 addressing.
Type: String
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

 ** NodeType **   <a name="MemoryDB-Type-Cluster-NodeType"></a>
The cluster's node type
Type: String
Required: No

 ** NumberOfShards **   <a name="MemoryDB-Type-Cluster-NumberOfShards"></a>
The number of shards in the cluster
Type: Integer
Required: No

 ** ParameterGroupName **   <a name="MemoryDB-Type-Cluster-ParameterGroupName"></a>
The name of the parameter group used by the cluster
Type: String
Required: No

 ** ParameterGroupStatus **   <a name="MemoryDB-Type-Cluster-ParameterGroupStatus"></a>
The status of the parameter group used by the cluster, for example 'active' or 'applying'.
Type: String
Required: No

 ** PendingUpdates **   <a name="MemoryDB-Type-Cluster-PendingUpdates"></a>
A group of settings that are currently being applied.
Type: [ClusterPendingUpdates](API_ClusterPendingUpdates.md) object
Required: No

 ** SecurityGroups **   <a name="MemoryDB-Type-Cluster-SecurityGroups"></a>
A list of security groups used by the cluster
Type: Array of [SecurityGroupMembership](API_SecurityGroupMembership.md) objects
Required: No

 ** Shards **   <a name="MemoryDB-Type-Cluster-Shards"></a>
A list of shards that are members of the cluster.
Type: Array of [Shard](API_Shard.md) objects
Required: No

 ** SnapshotRetentionLimit **   <a name="MemoryDB-Type-Cluster-SnapshotRetentionLimit"></a>
The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.
Type: Integer
Required: No

 ** SnapshotWindow **   <a name="MemoryDB-Type-Cluster-SnapshotWindow"></a>
The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard. Example: 05:00-09:00 If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.
Type: String
Required: No

 ** SnsTopicArn **   <a name="MemoryDB-Type-Cluster-SnsTopicArn"></a>
The Amazon Resource Name (ARN) of the SNS notification topic
Type: String
Required: No

 ** SnsTopicStatus **   <a name="MemoryDB-Type-Cluster-SnsTopicStatus"></a>
The SNS topic must be in Active status to receive notifications
Type: String
Required: No

 ** Status **   <a name="MemoryDB-Type-Cluster-Status"></a>
The status of the cluster. For example, Available, Updating, Creating.
Type: String
Required: No

 ** SubnetGroupName **   <a name="MemoryDB-Type-Cluster-SubnetGroupName"></a>
The name of the subnet group used by the cluster
Type: String
Required: No

 ** TLSEnabled **   <a name="MemoryDB-Type-Cluster-TLSEnabled"></a>
A flag to indicate if In-transit encryption is enabled
Type: Boolean
Required: No

## See Also
<a name="API_Cluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/memorydb-2021-01-01/Cluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/memorydb-2021-01-01/Cluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/memorydb-2021-01-01/Cluster)
