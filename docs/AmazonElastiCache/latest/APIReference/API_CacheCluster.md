---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CacheCluster.html
---

# CacheCluster
<a name="API_CacheCluster"></a>

Contains all of the attributes of a specific cluster.

## Contents
<a name="API_CacheCluster_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ARN **
The ARN (Amazon Resource Name) of the cache cluster.
Type: String
Required: No

 ** AtRestEncryptionEnabled **
A flag that enables encryption at-rest when set to `true`.
You cannot modify the value of `AtRestEncryptionEnabled` after the cluster is created. To enable at-rest encryption on a cluster you must set `AtRestEncryptionEnabled` to `true` when you create a cluster.
 **Required:** Only available when creating a replication group in an Amazon VPC using Redis OSS version `3.2.6`, `4.x` or later.
Default: `false`
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

 ** AutoMinorVersionUpgrade **
 If you are running Valkey or Redis OSS engine version 6.0 or later, set this parameter to yes if you want to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions.
Type: Boolean
Required: No

 ** CacheClusterCreateTime **
The date and time when the cluster was created.
Type: Timestamp
Required: No

 ** CacheClusterId **
The user-supplied identifier of the cluster. This identifier is a unique key that identifies a cluster.
Type: String
Required: No

 ** CacheClusterStatus **
The current state of this cluster, one of the following values: `available`, `creating`, `deleted`, `deleting`, `incompatible-network`, `modifying`, `rebooting cluster nodes`, `restore-failed`, or `snapshotting`.
Type: String
Required: No

 ** CacheNodes.CacheNode.N **
A list of cache nodes that are members of the cluster.
Type: Array of [CacheNode](API_CacheNode.md) objects
Required: No

 ** CacheNodeType **
The name of the compute and memory capacity node type for the cluster.
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

 ** CacheParameterGroup **
Status of the cache parameter group.
Type: [CacheParameterGroupStatus](API_CacheParameterGroupStatus.md) object
Required: No

 ** CacheSecurityGroups.CacheSecurityGroup.N **
A list of cache security group elements, composed of name and status sub-elements.
Type: Array of [CacheSecurityGroupMembership](API_CacheSecurityGroupMembership.md) objects
Required: No

 ** CacheSubnetGroupName **
The name of the cache subnet group associated with the cluster.
Type: String
Required: No

 ** ClientDownloadLandingPage **
The URL of the web page where you can download the latest ElastiCache client library.
Type: String
Required: No

 ** ConfigurationEndpoint **
Represents a Memcached cluster endpoint which can be used by an application to connect to any node in the cluster. The configuration endpoint will always have `.cfg` in it.
Example: `mem-3.9dvc4r.cfg.usw2.cache.amazonaws.com:11211`
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** Engine **
The name of the cache engine (`memcached` or `redis`) to be used for this cluster.
Type: String
Required: No

 ** EngineVersion **
The version of the cache engine that is used in this cluster.
Type: String
Required: No

 ** IpDiscovery **
The network type associated with the cluster, either `ipv4` \| `ipv6`. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/).
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 ** LogDeliveryConfigurations.LogDeliveryConfiguration.N **
Returns the destination, format and type of the logs.
Type: Array of [LogDeliveryConfiguration](API_LogDeliveryConfiguration.md) objects
Required: No

 ** NetworkType **
Must be either `ipv4` \| `ipv6` \| `dual_stack`. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/).
Type: String
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

 ** NotificationConfiguration **
Describes a notification topic and its status. Notification topics are used for publishing ElastiCache events to subscribers using Amazon Simple Notification Service (SNS).
Type: [NotificationConfiguration](API_NotificationConfiguration.md) object
Required: No

 ** NumCacheNodes **
The number of cache nodes in the cluster.
For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.
Type: Integer
Required: No

 ** PendingModifiedValues **
A group of settings that are applied to the cluster in the future, or that are currently being applied.
Type: [PendingModifiedValues](API_PendingModifiedValues.md) object
Required: No

 ** PreferredAvailabilityZone **
The name of the Availability Zone in which the cluster is located or "Multiple" if the cache nodes are located in different Availability Zones.
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
The outpost ARN in which the cache cluster is created.
Type: String
Required: No

 ** ReplicationGroupId **
The replication group to which this cluster belongs. If this field is empty, the cluster is not associated with any replication group.
Type: String
Required: No

 ** ReplicationGroupLogDeliveryEnabled **
A boolean value indicating whether log delivery is enabled for the replication group.
Type: Boolean
Required: No

 ** SecurityGroups.member.N **
A list of VPC Security Groups associated with the cluster.
Type: Array of [SecurityGroupMembership](API_SecurityGroupMembership.md) objects
Required: No

 ** SnapshotRetentionLimit **
The number of days for which ElastiCache retains automatic cluster snapshots before deleting them. For example, if you set `SnapshotRetentionLimit` to 5, a snapshot that was taken today is retained for 5 days before being deleted.
 If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Type: Integer
Required: No

 ** SnapshotWindow **
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your cluster.
Example: `05:00-09:00`
Type: String
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

## See Also
<a name="API_CacheCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CacheCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CacheCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CacheCluster)
