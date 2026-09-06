---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ReplicationGroup.html
---

# ReplicationGroup
<a name="API_ReplicationGroup"></a>

Contains all of the attributes of a specific Valkey or Redis OSS replication group.

## Contents
<a name="API_ReplicationGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ARN **
The ARN (Amazon Resource Name) of the replication group.
Type: String
Required: No

 ** AtRestEncryptionEnabled **
A flag that enables encryption at-rest on the cluster when set to `true`. In some cases, encryption at-rest may be enabled even when this value is false. Use `StorageEncryptionType` to view the effective encryption state of a cluster.
You cannot modify the value of `AtRestEncryptionEnabled` after the cluster is created.
Default: `true` when using Valkey, `false` when using Redis OSS
Type: Boolean
Required: No

 ** AuthTokenEnabled **
A flag that enables using an `AuthToken` (password) when issuing Valkey or Redis OSS commands.
Default: `false`
Type: Boolean
Required: No

 ** AuthTokenLastModifiedDate **
The date the auth token was last modified
Type: Timestamp
Required: No

 ** AutomaticFailover **
Indicates the status of automatic failover for this Valkey or Redis OSS replication group.
Type: String
Valid Values: `enabled | disabled | enabling | disabling`
Required: No

 ** AutoMinorVersionUpgrade **
If you are running Valkey 7.2 and above, or Redis OSS engine version 6.0 and above, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions.
Type: Boolean
Required: No

 ** CacheNodeType **
The name of the compute and memory capacity node type for each node in the replication group.
Type: String
Required: No

 ** ClusterEnabled **
A flag indicating whether or not this replication group is cluster enabled; i.e., whether its data can be partitioned across multiple shards (API/CLI: node groups).
Valid values: `true` \| `false`
Type: Boolean
Required: No

 ** ClusterMode **
Enabled or Disabled. To modify cluster mode from Disabled to Enabled, you must first set the cluster mode to Compatible. Compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to Enabled.
Type: String
Valid Values: `enabled | disabled | compatible`
Required: No

 ** ConfigurationEndpoint **
The configuration endpoint for this replication group. Use the configuration endpoint to connect to this replication group.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** DataTiering **
Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html).
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** Description **
The user supplied description of the replication group.
Type: String
Required: No

 ** Durability **
The durability setting of the replication group. For more information, see [Durability](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/durability.html).
Type: String
Valid Values: `default | async | sync | disabled`
Required: No

 ** EffectiveDurability **
The effective durability of the replication group. When `Durability` is set to `default`, the service resolves the actual durability based on the engine version, cluster mode, and other parameters. This field reflects the resolved value. For more information, see [Configuring Durability](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Durability.Configuring.html).
Type: String
Valid Values: `async | sync | disabled`
Required: No

 ** Engine **
The engine used in a replication group. The options are valkey, memcached or redis.
Type: String
Required: No

 ** GlobalReplicationGroupInfo **
The name of the Global datastore and role of this replication group in the Global datastore.
Type: [GlobalReplicationGroupInfo](API_GlobalReplicationGroupInfo.md) object
Required: No

 ** IpDiscovery **
The network type you choose when modifying a cluster, either `ipv4` \| `ipv6`. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/).
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** KmsKeyId **
The ID of the KMS key used to encrypt the disk in the cluster.
Type: String
Required: No

 ** LogDeliveryConfigurations.LogDeliveryConfiguration.N **
Returns the destination, format and type of the logs.
Type: Array of [LogDeliveryConfiguration](API_LogDeliveryConfiguration.md) objects
Required: No

 ** MemberClusters.ClusterId.N **
The names of all the cache clusters that are part of this replication group.
Type: Array of strings
Required: No

 ** MemberClustersOutpostArns.ReplicationGroupOutpostArn.N **
The outpost ARNs of the replication group's member clusters.
Type: Array of strings
Required: No

 ** MultiAZ **
A flag indicating if you have Multi-AZ enabled to enhance fault tolerance. For more information, see [Minimizing Downtime: Multi-AZ](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html)
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** NetworkType **
Must be either `ipv4` \| `ipv6` \| `dual_stack`. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/).
Type: String
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

 ** NodeGroups.NodeGroup.N **
A list of node groups in this replication group. For Valkey or Redis OSS (cluster mode disabled) replication groups, this is a single-element list. For Valkey or Redis OSS (cluster mode enabled) replication groups, the list contains an entry for each node group (shard).
Type: Array of [NodeGroup](API_NodeGroup.md) objects
Required: No

 ** PendingModifiedValues **
A group of settings to be applied to the replication group, either immediately or during the next maintenance window.
Type: [ReplicationGroupPendingModifiedValues](API_ReplicationGroupPendingModifiedValues.md) object
Required: No

 ** ReplicationGroupCreateTime **
The date and time when the cluster was created.
Type: Timestamp
Required: No

 ** ReplicationGroupId **
The identifier for the replication group.
Type: String
Required: No

 ** SnapshotRetentionLimit **
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set `SnapshotRetentionLimit` to 5, a snapshot that was taken today is retained for 5 days before being deleted.
 If the value of `SnapshotRetentionLimit` is set to zero (0), backups are turned off.
Type: Integer
Required: No

 ** SnapshottingClusterId **
The cluster ID that is used as the daily snapshot source for the replication group.
Type: String
Required: No

 ** SnapshotWindow **
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: `05:00-09:00`
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
This parameter is only valid if the `Engine` parameter is `redis`.
Type: String
Required: No

 ** Status **
The current state of this replication group - `creating`, `available`, `modifying`, `deleting`, `create-failed`, `snapshotting`.
Type: String
Required: No

 ** StorageEncryptionType **
Indicates the type of encryption for data stored at rest in the replication group. The value is `none` if at-rest encryption is not enabled, `sse-elasticache` if an ElastiCache service-managed key is used, or `sse-kms` if a customer-managed KMS key is used.
Type: String
Valid Values: `none | sse-elasticache | sse-kms`
Required: No

 ** TransitEncryptionEnabled **
A flag that enables in-transit encryption when set to `true`.
 **Required:** Only available when creating a replication group in an Amazon VPC using Redis OSS version `3.2.6`, `4.x` or later.
Default: `false`
Type: Boolean
Required: No

 ** TransitEncryptionMode **
A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.
Type: String
Valid Values: `preferred | required`
Required: No

 ** UserGroupIds.member.N **
The ID of the user group associated to the replication group.
Type: Array of strings
Length Constraints: Minimum length of 1.
Pattern: `[a-zA-Z][a-zA-Z0-9\-]*`
Required: No

## See Also
<a name="API_ReplicationGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ReplicationGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ReplicationGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ReplicationGroup)
