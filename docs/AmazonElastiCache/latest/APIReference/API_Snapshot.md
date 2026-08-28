---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_Snapshot.html
---

# Snapshot
<a name="API_Snapshot"></a>

Represents a copy of an entire Valkey or Redis OSS cluster as of the time when the snapshot was taken.

## Contents
<a name="API_Snapshot_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ARN **
The ARN (Amazon Resource Name) of the snapshot.
Type: String
Required: No

 ** AutomaticFailover **
Indicates the status of automatic failover for the source Valkey or Redis OSS replication group.
Type: String
Valid Values: `enabled | disabled | enabling | disabling`
Required: No

 ** AutoMinorVersionUpgrade **
 If you are running Valkey 7.2 and above or Redis OSS engine version 6.0 and above, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions.
Type: Boolean
Required: No

 ** CacheClusterCreateTime **
The date and time when the source cluster was created.
Type: Timestamp
Required: No

 ** CacheClusterId **
The user-supplied identifier of the source cluster.
Type: String
Required: No

 ** CacheNodeType **
The name of the compute and memory capacity node type for the source cluster.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.
+ General purpose:
  + Current generation:
**Note**
For region availability, see [Supported Node Types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion)

     **M8g node types**: `cache.m8g.large`, `cache.m8g.xlarge`, `cache.m8g.2xlarge`, `cache.m8g.4xlarge`, `cache.m8g.8xlarge`, `cache.m8g.12xlarge`, `cache.m8g.16xlarge`

     **M7g node types**: `cache.m7g.large`, `cache.m7g.xlarge`, `cache.m7g.2xlarge`, `cache.m7g.4xlarge`, `cache.m7g.8xlarge`, `cache.m7g.12xlarge`, `cache.m7g.16xlarge`

     **M6g node types** (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): `cache.m6g.large`, `cache.m6g.xlarge`, `cache.m6g.2xlarge`, `cache.m6g.4xlarge`, `cache.m6g.8xlarge`, `cache.m6g.12xlarge`, `cache.m6g.16xlarge`

     **M5 node types:** `cache.m5.large`, `cache.m5.xlarge`, `cache.m5.2xlarge`, `cache.m5.4xlarge`, `cache.m5.12xlarge`, `cache.m5.24xlarge`

     **M4 node types:** `cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`, `cache.m4.4xlarge`, `cache.m4.10xlarge`

     **T4g node types** (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): `cache.t4g.micro`, `cache.t4g.small`, `cache.t4g.medium`

     **T3 node types:** `cache.t3.micro`, `cache.t3.small`, `cache.t3.medium`

     **T2 node types:** `cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`
  + Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)

     **T1 node types:** `cache.t1.micro`

     **M1 node types:** `cache.m1.small`, `cache.m1.medium`, `cache.m1.large`, `cache.m1.xlarge`

     **M3 node types:** `cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`, `cache.m3.2xlarge`
+ Compute optimized:
  + Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)

     **C1 node types:** `cache.c1.xlarge`
+ Memory optimized:
  + Current generation:
**Note**
For region availability, see [Supported Node Types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion)

     **R8g node types**: `cache.r8g.large`, `cache.r8g.xlarge`, `cache.r8g.2xlarge`, `cache.r8g.4xlarge`, `cache.r8g.8xlarge`, `cache.r8g.12xlarge`, `cache.r8g.16xlarge`

     **R7g node types**: `cache.r7g.large`, `cache.r7g.xlarge`, `cache.r7g.2xlarge`, `cache.r7g.4xlarge`, `cache.r7g.8xlarge`, `cache.r7g.12xlarge`, `cache.r7g.16xlarge`

     **R6g node types** (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): `cache.r6g.large`, `cache.r6g.xlarge`, `cache.r6g.2xlarge`, `cache.r6g.4xlarge`, `cache.r6g.8xlarge`, `cache.r6g.12xlarge`, `cache.r6g.16xlarge`

     **R5 node types:** `cache.r5.large`, `cache.r5.xlarge`, `cache.r5.2xlarge`, `cache.r5.4xlarge`, `cache.r5.12xlarge`, `cache.r5.24xlarge`

     **R4 node types:** `cache.r4.large`, `cache.r4.xlarge`, `cache.r4.2xlarge`, `cache.r4.4xlarge`, `cache.r4.8xlarge`, `cache.r4.16xlarge`
  + Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)

     **M2 node types:** `cache.m2.xlarge`, `cache.m2.2xlarge`, `cache.m2.4xlarge`

     **R3 node types:** `cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`, `cache.r3.4xlarge`, `cache.r3.8xlarge`
+ Network optimized:
  + Current generation:

     **C8gn node types**: `cache.c8gn.large`, `cache.c8gn.xlarge`, `cache.c8gn.2xlarge`, `cache.c8gn.4xlarge`, `cache.c8gn.8xlarge`, `cache.c8gn.12xlarge`, `cache.c8gn.16xlarge`

     **C7gn node types**: `cache.c7gn.large`, `cache.c7gn.xlarge`, `cache.c7gn.2xlarge`, `cache.c7gn.4xlarge`, `cache.c7gn.8xlarge`, `cache.c7gn.12xlarge`, `cache.c7gn.16xlarge`
 **Additional node type info**
+ All current generation instance types are created in Amazon VPC by default.
+ Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.
+ Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.
+ The configuration variables `appendonly` and `appendfsync` are not supported on Valkey, or on Redis OSS version 2.8.22 and later.
Type: String
Required: No

 ** CacheParameterGroupName **
The cache parameter group that is associated with the source cluster.
Type: String
Required: No

 ** CacheSubnetGroupName **
The name of the cache subnet group associated with the source cluster.
Type: String
Required: No

 ** DataTiering **
Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html).
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** Durability **
The durability setting of the cluster when the snapshot was taken. When restoring from this snapshot, the cluster uses this durability setting unless overridden in the restore request. For more information, see [Durability](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/durability.html).
Type: String
Valid Values: `default | async | sync | disabled`
Required: No

 ** Engine **
The name of the cache engine (`memcached` or `redis`) used by the source cluster.
Type: String
Required: No

 ** EngineVersion **
The version of the cache engine version that is used by the source cluster.
Type: String
Required: No

 ** KmsKeyId **
The ID of the KMS key used to encrypt the snapshot.
Type: String
Required: No

 ** NodeSnapshots.NodeSnapshot.N **
A list of the cache nodes in the source cluster.
Type: Array of [NodeSnapshot](API_NodeSnapshot.md) objects
Required: No

 ** NumCacheNodes **
The number of cache nodes in the source cluster.
For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.
Type: Integer
Required: No

 ** NumNodeGroups **
The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.
Type: Integer
Required: No

 ** Port **
The port number used by each cache nodes in the source cluster.
Type: Integer
Required: No

 ** PreferredAvailabilityZone **
The name of the Availability Zone in which the source cluster is located.
Type: String
Required: No

 ** PreferredMaintenanceWindow **
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Valid values for `ddd` are:
+  `sun`
+  `mon`
+  `tue`
+  `wed`
+  `thu`
+  `fri`
+  `sat`
Example: `sun:23:00-mon:01:30`
Type: String
Required: No

 ** PreferredOutpostArn **
The ARN (Amazon Resource Name) of the preferred outpost.
Type: String
Required: No

 ** ReplicationGroupDescription **
A description of the source replication group.
Type: String
Required: No

 ** ReplicationGroupId **
The unique identifier of the source replication group.
Type: String
Required: No

 ** SnapshotName **
The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.
Type: String
Required: No

 ** SnapshotRetentionLimit **
For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.
For manual snapshots, this field reflects the `SnapshotRetentionLimit` for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the `DeleteSnapshot` operation.
 **Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Type: Integer
Required: No

 ** SnapshotSource **
Indicates whether the snapshot is from an automatic backup (`automated`) or was created manually (`manual`).
Type: String
Required: No

 ** SnapshotStatus **
The status of the snapshot. Valid values: `creating` \| `available` \| `restoring` \| `copying` \| `deleting`.
Type: String
Required: No

 ** SnapshotWindow **
The daily time range during which ElastiCache takes daily snapshots of the source cluster.
Type: String
Required: No

 ** TopicArn **
The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.
Type: String
Required: No

 ** VpcId **
The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.
Type: String
Required: No

## See Also
<a name="API_Snapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/Snapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/Snapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/Snapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
