---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-snapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::Snapshot
<a name="aws-resource-elasticache-snapshot"></a>

Represents a copy of an entire Valkey or Redis OSS cluster as of the time when the snapshot was taken.

## Syntax
<a name="aws-resource-elasticache-snapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticache-snapshot-syntax.json"></a>

```
{
  "Type" : "AWS::ElastiCache::Snapshot",
  "Properties" : {
      "[CacheClusterId](#cfn-elasticache-snapshot-cacheclusterid)" : {{String}},
      "[KmsKeyId](#cfn-elasticache-snapshot-kmskeyid)" : {{String}},
      "[ReplicationGroupId](#cfn-elasticache-snapshot-replicationgroupid)" : {{String}},
      "[SnapshotName](#cfn-elasticache-snapshot-snapshotname)" : {{String}},
      "[Tags](#cfn-elasticache-snapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-elasticache-snapshot-syntax.yaml"></a>

```
Type: AWS::ElastiCache::Snapshot
Properties:
  [CacheClusterId](#cfn-elasticache-snapshot-cacheclusterid): {{String}}
  [KmsKeyId](#cfn-elasticache-snapshot-kmskeyid): {{String}}
  [ReplicationGroupId](#cfn-elasticache-snapshot-replicationgroupid): {{String}}
  [SnapshotName](#cfn-elasticache-snapshot-snapshotname): {{String}}
  [Tags](#cfn-elasticache-snapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-elasticache-snapshot-properties"></a>

`CacheClusterId`  <a name="cfn-elasticache-snapshot-cacheclusterid"></a>
The user-supplied identifier of the source cluster.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-elasticache-snapshot-kmskeyid"></a>
The ID of the KMS key used to encrypt the snapshot.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReplicationGroupId`  <a name="cfn-elasticache-snapshot-replicationgroupid"></a>
The unique identifier of the source replication group.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotName`  <a name="cfn-elasticache-snapshot-snapshotname"></a>
The name of a snapshot. For an automatic snapshot, the name is system-generated. For a manual snapshot, this is the user-provided name.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-elasticache-snapshot-tags"></a>
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticache-snapshot-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elasticache-snapshot-return-values"></a>

### Ref
<a name="aws-resource-elasticache-snapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-elasticache-snapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-elasticache-snapshot-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN (Amazon Resource Name) of the snapshot.

`AutomaticFailover`  <a name="AutomaticFailover-fn::getatt"></a>
Indicates the status of automatic failover for the source Valkey or Redis OSS replication group.

`AutoMinorVersionUpgrade`  <a name="AutoMinorVersionUpgrade-fn::getatt"></a>
 If you are running Valkey 7.2 and above or Redis OSS engine version 6.0 and above, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions.

`CacheClusterCreateTime`  <a name="CacheClusterCreateTime-fn::getatt"></a>
The date and time when the source cluster was created.

`CacheNodeType`  <a name="CacheNodeType-fn::getatt"></a>
The name of the compute and memory capacity node type for the source cluster.
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.
+ General purpose:
  + Current generation:

    **M7g node types**: `cache.m7g.large`, `cache.m7g.xlarge`, `cache.m7g.2xlarge`, `cache.m7g.4xlarge`, `cache.m7g.8xlarge`, `cache.m7g.12xlarge`, `cache.m7g.16xlarge`
**Note**
For region availability, see [Supported Node Types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion)

    **M6g node types** (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): `cache.m6g.large`, `cache.m6g.xlarge`, `cache.m6g.2xlarge`, `cache.m6g.4xlarge`, `cache.m6g.8xlarge`, `cache.m6g.12xlarge`, `cache.m6g.16xlarge`

    **M5 node types:**`cache.m5.large`, `cache.m5.xlarge`, `cache.m5.2xlarge`, `cache.m5.4xlarge`, `cache.m5.12xlarge`, `cache.m5.24xlarge`

    **M4 node types:**`cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`, `cache.m4.4xlarge`, `cache.m4.10xlarge`

    **T4g node types** (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): `cache.t4g.micro`, `cache.t4g.small`, `cache.t4g.medium`

    **T3 node types:**`cache.t3.micro`, `cache.t3.small`, `cache.t3.medium`

    **T2 node types:**`cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`
  + Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)

     **T1 node types:** `cache.t1.micro`

    **M1 node types:**`cache.m1.small`, `cache.m1.medium`, `cache.m1.large`, `cache.m1.xlarge`

    **M3 node types:**`cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`, `cache.m3.2xlarge`
+ Compute optimized:
  + Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)

     **C1 node types:** `cache.c1.xlarge`
+ Memory optimized:
  + Current generation:

    **R7g node types**: `cache.r7g.large`, `cache.r7g.xlarge`, `cache.r7g.2xlarge`, `cache.r7g.4xlarge`, `cache.r7g.8xlarge`, `cache.r7g.12xlarge`, `cache.r7g.16xlarge`
**Note**
For region availability, see [Supported Node Types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion)

    **R6g node types** (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): `cache.r6g.large`, `cache.r6g.xlarge`, `cache.r6g.2xlarge`, `cache.r6g.4xlarge`, `cache.r6g.8xlarge`, `cache.r6g.12xlarge`, `cache.r6g.16xlarge`

    **R5 node types:**`cache.r5.large`, `cache.r5.xlarge`, `cache.r5.2xlarge`, `cache.r5.4xlarge`, `cache.r5.12xlarge`, `cache.r5.24xlarge`

    **R4 node types:**`cache.r4.large`, `cache.r4.xlarge`, `cache.r4.2xlarge`, `cache.r4.4xlarge`, `cache.r4.8xlarge`, `cache.r4.16xlarge`
  + Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)

    **M2 node types:**`cache.m2.xlarge`, `cache.m2.2xlarge`, `cache.m2.4xlarge`

    **R3 node types:**`cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`, `cache.r3.4xlarge`, `cache.r3.8xlarge`
 **Additional node type info**
+ All current generation instance types are created in Amazon VPC by default.
+ Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.
+ Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.
+ The configuration variables `appendonly` and `appendfsync` are not supported on Valkey, or on Redis OSS version 2.8.22 and later.

`CacheParameterGroupName`  <a name="CacheParameterGroupName-fn::getatt"></a>
The cache parameter group that is associated with the source cluster.

`CacheSubnetGroupName`  <a name="CacheSubnetGroupName-fn::getatt"></a>
The name of the cache subnet group associated with the source cluster.

`DataTiering`  <a name="DataTiering-fn::getatt"></a>
Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html).

`Engine`  <a name="Engine-fn::getatt"></a>
The name of the cache engine (`memcached` or `redis`) used by the source cluster.

`EngineVersion`  <a name="EngineVersion-fn::getatt"></a>
The version of the cache engine version that is used by the source cluster.

`NodeSnapshots`  <a name="NodeSnapshots-fn::getatt"></a>
A list of the cache nodes in the source cluster.

`NumCacheNodes`  <a name="NumCacheNodes-fn::getatt"></a>
The number of cache nodes in the source cluster.
For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.

`NumNodeGroups`  <a name="NumNodeGroups-fn::getatt"></a>
The number of node groups (shards) in this snapshot. When restoring from a snapshot, the number of node groups (shards) in the snapshot and in the restored replication group must be the same.

`Port`  <a name="Port-fn::getatt"></a>
The port number used by each cache nodes in the source cluster.

`PreferredAvailabilityZone`  <a name="PreferredAvailabilityZone-fn::getatt"></a>
The name of the Availability Zone in which the source cluster is located.

`PreferredMaintenanceWindow`  <a name="PreferredMaintenanceWindow-fn::getatt"></a>
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

`ReplicationGroupDescription`  <a name="ReplicationGroupDescription-fn::getatt"></a>
A description of the source replication group.

`SnapshotRetentionLimit`  <a name="SnapshotRetentionLimit-fn::getatt"></a>
For an automatic snapshot, the number of days for which ElastiCache retains the snapshot before deleting it.
For manual snapshots, this field reflects the `SnapshotRetentionLimit` for the source cluster when the snapshot was created. This field is otherwise ignored: Manual snapshots do not expire, and can only be deleted using the `DeleteSnapshot` operation.
**Important** If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.

`SnapshotSource`  <a name="SnapshotSource-fn::getatt"></a>
Indicates whether the snapshot is from an automatic backup (`automated`) or was created manually (`manual`).

`SnapshotStatus`  <a name="SnapshotStatus-fn::getatt"></a>
The status of the snapshot. Valid values: `creating` \| `available` \| `restoring` \| `copying` \| `deleting`.

`SnapshotWindow`  <a name="SnapshotWindow-fn::getatt"></a>
The daily time range during which ElastiCache takes daily snapshots of the source cluster.

`TopicArn`  <a name="TopicArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the topic used by the source cluster for publishing notifications.

`VpcId`  <a name="VpcId-fn::getatt"></a>
The Amazon Virtual Private Cloud identifier (VPC ID) of the cache subnet group for the source cluster.
