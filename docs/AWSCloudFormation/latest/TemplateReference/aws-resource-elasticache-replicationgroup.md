---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticache-replicationgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::ReplicationGroup
<a name="aws-resource-elasticache-replicationgroup"></a>

The `AWS::ElastiCache::ReplicationGroup` resource creates an Amazon ElastiCache (Valkey or Redis OSS) replication group. A Valkey or Redis OSS (cluster mode disabled) replication group is a collection of cache clusters, where one of the clusters is a primary read-write cluster and the others are read-only replicas.

A Valkey or Redis OSS (cluster mode enabled) cluster is comprised of from 1 to 90 shards (API/CLI: node groups). Each shard has a primary node and up to 5 read-only replica nodes. The configuration can range from 90 shards and 0 replicas to 15 shards and 5 replicas, which is the maximum number or replicas allowed.

The node or shard limit can be increased to a maximum of 500 per cluster if the engine version is Valkey 7.2 or higher, or Redis OSS 5.0.6 or higher. For example, you can choose to configure a 500 node cluster that ranges between 83 shards (one primary and 5 replicas per shard) and 500 shards (single primary and no replicas). Make sure there are enough available IP addresses to accommodate the increase. Common pitfalls include the subnets in the subnet group have too small a CIDR range or the subnets are shared and heavily used by other clusters. For more information, see [Creating a Subnet Group](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.Creating.html). For versions below 5.0.6, the limit is 250 per cluster.

To request a limit increase, see [Amazon Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) and choose the limit type **Nodes per cluster per instance type**.

## Syntax
<a name="aws-resource-elasticache-replicationgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticache-replicationgroup-syntax.json"></a>

```
{
  "Type" : "AWS::ElastiCache::ReplicationGroup",
  "Properties" : {
      "[AtRestEncryptionEnabled](#cfn-elasticache-replicationgroup-atrestencryptionenabled)" : {{Boolean}},
      "[AuthToken](#cfn-elasticache-replicationgroup-authtoken)" : {{String}},
      "[AutomaticFailoverEnabled](#cfn-elasticache-replicationgroup-automaticfailoverenabled)" : {{Boolean}},
      "[AutoMinorVersionUpgrade](#cfn-elasticache-replicationgroup-autominorversionupgrade)" : {{Boolean}},
      "[CacheNodeType](#cfn-elasticache-replicationgroup-cachenodetype)" : {{String}},
      "[CacheParameterGroupName](#cfn-elasticache-replicationgroup-cacheparametergroupname)" : {{String}},
      "[CacheSubnetGroupName](#cfn-elasticache-replicationgroup-cachesubnetgroupname)" : {{String}},
      "[ClusterMode](#cfn-elasticache-replicationgroup-clustermode)" : {{String}},
      "[DataTieringEnabled](#cfn-elasticache-replicationgroup-datatieringenabled)" : {{Boolean}},
      "[Durability](#cfn-elasticache-replicationgroup-durability)" : {{String}},
      "[Engine](#cfn-elasticache-replicationgroup-engine)" : {{String}},
      "[EngineVersion](#cfn-elasticache-replicationgroup-engineversion)" : {{String}},
      "[GlobalReplicationGroupId](#cfn-elasticache-replicationgroup-globalreplicationgroupid)" : {{String}},
      "[IpDiscovery](#cfn-elasticache-replicationgroup-ipdiscovery)" : {{String}},
      "[KmsKeyId](#cfn-elasticache-replicationgroup-kmskeyid)" : {{String}},
      "[LogDeliveryConfigurations](#cfn-elasticache-replicationgroup-logdeliveryconfigurations)" : {{[ LogDeliveryConfigurationRequest, ... ]}},
      "[MultiAZEnabled](#cfn-elasticache-replicationgroup-multiazenabled)" : {{Boolean}},
      "[NetworkType](#cfn-elasticache-replicationgroup-networktype)" : {{String}},
      "[NodeGroupConfiguration](#cfn-elasticache-replicationgroup-nodegroupconfiguration)" : {{[ NodeGroupConfiguration, ... ]}},
      "[NotificationTopicArn](#cfn-elasticache-replicationgroup-notificationtopicarn)" : {{String}},
      "[NumCacheClusters](#cfn-elasticache-replicationgroup-numcacheclusters)" : {{Integer}},
      "[NumNodeGroups](#cfn-elasticache-replicationgroup-numnodegroups)" : {{Integer}},
      "[Port](#cfn-elasticache-replicationgroup-port)" : {{Integer}},
      "[PreferredCacheClusterAZs](#cfn-elasticache-replicationgroup-preferredcacheclusterazs)" : {{[ String, ... ]}},
      "[PreferredMaintenanceWindow](#cfn-elasticache-replicationgroup-preferredmaintenancewindow)" : {{String}},
      "[PrimaryClusterId](#cfn-elasticache-replicationgroup-primaryclusterid)" : {{String}},
      "[ReplicasPerNodeGroup](#cfn-elasticache-replicationgroup-replicaspernodegroup)" : {{Integer}},
      "[ReplicationGroupDescription](#cfn-elasticache-replicationgroup-replicationgroupdescription)" : {{String}},
      "[ReplicationGroupId](#cfn-elasticache-replicationgroup-replicationgroupid)" : {{String}},
      "[SecurityGroupIds](#cfn-elasticache-replicationgroup-securitygroupids)" : {{[ String, ... ]}},
      "[SnapshotArns](#cfn-elasticache-replicationgroup-snapshotarns)" : {{[ String, ... ]}},
      "[SnapshotName](#cfn-elasticache-replicationgroup-snapshotname)" : {{String}},
      "[SnapshotRetentionLimit](#cfn-elasticache-replicationgroup-snapshotretentionlimit)" : {{Integer}},
      "[SnapshottingClusterId](#cfn-elasticache-replicationgroup-snapshottingclusterid)" : {{String}},
      "[SnapshotWindow](#cfn-elasticache-replicationgroup-snapshotwindow)" : {{String}},
      "[Tags](#cfn-elasticache-replicationgroup-tags)" : {{[ Tag, ... ]}},
      "[TransitEncryptionEnabled](#cfn-elasticache-replicationgroup-transitencryptionenabled)" : {{Boolean}},
      "[TransitEncryptionMode](#cfn-elasticache-replicationgroup-transitencryptionmode)" : {{String}},
      "[UserGroupIds](#cfn-elasticache-replicationgroup-usergroupids)" : {{[ String, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-elasticache-replicationgroup-syntax.yaml"></a>

```
Type: AWS::ElastiCache::ReplicationGroup
Properties:
  [AtRestEncryptionEnabled](#cfn-elasticache-replicationgroup-atrestencryptionenabled): {{Boolean}}
  [AuthToken](#cfn-elasticache-replicationgroup-authtoken): {{String}}
  [AutomaticFailoverEnabled](#cfn-elasticache-replicationgroup-automaticfailoverenabled): {{Boolean}}
  [AutoMinorVersionUpgrade](#cfn-elasticache-replicationgroup-autominorversionupgrade): {{Boolean}}
  [CacheNodeType](#cfn-elasticache-replicationgroup-cachenodetype): {{String}}
  [CacheParameterGroupName](#cfn-elasticache-replicationgroup-cacheparametergroupname): {{String}}
  [CacheSubnetGroupName](#cfn-elasticache-replicationgroup-cachesubnetgroupname): {{String}}
  [ClusterMode](#cfn-elasticache-replicationgroup-clustermode): {{String}}
  [DataTieringEnabled](#cfn-elasticache-replicationgroup-datatieringenabled): {{Boolean}}
  [Durability](#cfn-elasticache-replicationgroup-durability): {{String}}
  [Engine](#cfn-elasticache-replicationgroup-engine): {{String}}
  [EngineVersion](#cfn-elasticache-replicationgroup-engineversion): {{String}}
  [GlobalReplicationGroupId](#cfn-elasticache-replicationgroup-globalreplicationgroupid): {{String}}
  [IpDiscovery](#cfn-elasticache-replicationgroup-ipdiscovery): {{String}}
  [KmsKeyId](#cfn-elasticache-replicationgroup-kmskeyid): {{String}}
  [LogDeliveryConfigurations](#cfn-elasticache-replicationgroup-logdeliveryconfigurations): {{
    - LogDeliveryConfigurationRequest}}
  [MultiAZEnabled](#cfn-elasticache-replicationgroup-multiazenabled): {{Boolean}}
  [NetworkType](#cfn-elasticache-replicationgroup-networktype): {{String}}
  [NodeGroupConfiguration](#cfn-elasticache-replicationgroup-nodegroupconfiguration): {{
    - NodeGroupConfiguration}}
  [NotificationTopicArn](#cfn-elasticache-replicationgroup-notificationtopicarn): {{String}}
  [NumCacheClusters](#cfn-elasticache-replicationgroup-numcacheclusters): {{Integer}}
  [NumNodeGroups](#cfn-elasticache-replicationgroup-numnodegroups): {{Integer}}
  [Port](#cfn-elasticache-replicationgroup-port): {{Integer}}
  [PreferredCacheClusterAZs](#cfn-elasticache-replicationgroup-preferredcacheclusterazs): {{
    - String}}
  [PreferredMaintenanceWindow](#cfn-elasticache-replicationgroup-preferredmaintenancewindow): {{String}}
  [PrimaryClusterId](#cfn-elasticache-replicationgroup-primaryclusterid): {{String}}
  [ReplicasPerNodeGroup](#cfn-elasticache-replicationgroup-replicaspernodegroup): {{Integer}}
  [ReplicationGroupDescription](#cfn-elasticache-replicationgroup-replicationgroupdescription): {{String}}
  [ReplicationGroupId](#cfn-elasticache-replicationgroup-replicationgroupid): {{String}}
  [SecurityGroupIds](#cfn-elasticache-replicationgroup-securitygroupids): {{
    - String}}
  [SnapshotArns](#cfn-elasticache-replicationgroup-snapshotarns): {{
    - String}}
  [SnapshotName](#cfn-elasticache-replicationgroup-snapshotname): {{String}}
  [SnapshotRetentionLimit](#cfn-elasticache-replicationgroup-snapshotretentionlimit): {{Integer}}
  [SnapshottingClusterId](#cfn-elasticache-replicationgroup-snapshottingclusterid): {{String}}
  [SnapshotWindow](#cfn-elasticache-replicationgroup-snapshotwindow): {{String}}
  [Tags](#cfn-elasticache-replicationgroup-tags): {{
    - Tag}}
  [TransitEncryptionEnabled](#cfn-elasticache-replicationgroup-transitencryptionenabled): {{Boolean}}
  [TransitEncryptionMode](#cfn-elasticache-replicationgroup-transitencryptionmode): {{String}}
  [UserGroupIds](#cfn-elasticache-replicationgroup-usergroupids): {{
    - String}}
```

## Properties
<a name="aws-resource-elasticache-replicationgroup-properties"></a>

`AtRestEncryptionEnabled`  <a name="cfn-elasticache-replicationgroup-atrestencryptionenabled"></a>
A flag that enables encryption at rest when set to `true`.
**Required:** Only available when creating a replication group in an Amazon VPC using Redis OSS version `3.2.6` or `4.x` onward.
Default: `false`
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuthToken`  <a name="cfn-elasticache-replicationgroup-authtoken"></a>
**Reserved parameter.** The password used to access a password protected server.
`AuthToken` can be specified only on replication groups where `TransitEncryptionEnabled` is `true`. For more information, see [Authenticating Valkey or Redis OSS users with the AUTH Command](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/auth.html).
For HIPAA compliance, you must specify `TransitEncryptionEnabled` as `true`, an `AuthToken`, and a `CacheSubnetGroup`.
Password constraints:
+ Must be only printable ASCII characters.
+ Must be at least 16 characters and no more than 128 characters in length.
+ Nonalphanumeric characters are restricted to (\!, &, \#, $, ^, <, >, -, ).
For more information, see [AUTH password](http://redis.io/commands/AUTH) at http://redis.io/commands/AUTH.
If ADDING the AuthToken, update requires [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement).
*Required*: No
*Type*: String
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`AutomaticFailoverEnabled`  <a name="cfn-elasticache-replicationgroup-automaticfailoverenabled"></a>
Specifies whether a read-only replica is automatically promoted to read/write primary if the existing primary fails.
`AutomaticFailoverEnabled` must be enabled for Valkey or Redis OSS (cluster mode enabled) replication groups.
Default: false
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AutoMinorVersionUpgrade`  <a name="cfn-elasticache-replicationgroup-autominorversionupgrade"></a>
If you are running Valkey 7.2 or later, or Redis OSS 6.0 or later, set this parameter to yes if you want to opt-in to the next minor version upgrade campaign. This parameter is disabled for previous versions.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CacheNodeType`  <a name="cfn-elasticache-replicationgroup-cachenodetype"></a>
The compute and memory capacity of the nodes in the node group (shard).
The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.
+ General purpose:
  + Current generation:

    **M8g node types:**`cache.m8g.large`, `cache.m8g.xlarge`, `cache.m8g.2xlarge`, `cache.m8g.4xlarge`, `cache.m8g.8xlarge`, `cache.m8g.12xlarge`, `cache.m8g.16xlarge`

    **M7g node types:**`cache.m7g.large`, `cache.m7g.xlarge`, `cache.m7g.2xlarge`, `cache.m7g.4xlarge`, `cache.m7g.8xlarge`, `cache.m7g.12xlarge`, `cache.m7g.16xlarge`

    **M6g node types:**`cache.m6g.large`, `cache.m6g.xlarge`, `cache.m6g.2xlarge`, `cache.m6g.4xlarge`, `cache.m6g.12xlarge`, `cache.m6g.24xlarge`

    **M5 node types:**`cache.m5.large`, `cache.m5.xlarge`, `cache.m5.2xlarge`, `cache.m5.4xlarge`, `cache.m5.12xlarge`, `cache.m5.24xlarge`

    **M4 node types:**`cache.m4.large`, `cache.m4.xlarge`, `cache.m4.2xlarge`, `cache.m4.4xlarge`, `cache.m4.10xlarge`

    **T4g node types:**`cache.t4g.micro`, `cache.t4g.small`, `cache.t4g.medium`

    **T3 node types:**`cache.t3.micro`, `cache.t3.small`, `cache.t3.medium`

    **T2 node types:**`cache.t2.micro`, `cache.t2.small`, `cache.t2.medium`
  + Previous generation: (not recommended)

     **T1 node types:** `cache.t1.micro`

    **M1 node types:**`cache.m1.small`, `cache.m1.medium`, `cache.m1.large`, `cache.m1.xlarge`

    **M3 node types:**`cache.m3.medium`, `cache.m3.large`, `cache.m3.xlarge`, `cache.m3.2xlarge`
+ Compute optimized:
  + Previous generation: (not recommended)

     **C1 node types:** `cache.c1.xlarge`
+ Memory optimized:
  + Current generation:

    **R8g node types:**`cache.r8g.large`, `cache.r8g.xlarge`, `cache.r8g.2xlarge`, `cache.r8g.4xlarge`, `cache.r8g.8xlarge`, `cache.r8g.12xlarge`, `cache.r8g.16xlarge`

    **R7g node types:**`cache.r7g.large`, `cache.r7g.xlarge`, `cache.r7g.2xlarge`, `cache.r7g.4xlarge`, `cache.r7g.8xlarge`, `cache.r7g.12xlarge`, `cache.r7g.16xlarge`

    **R6gd node types:**`cache.r6gd.xlarge`, `cache.r6gd.2xlarge`, `cache.r6gd.4xlarge`, `cache.r6gd.8xlarge`, `cache.r6gd.12xlarge`, `cache.r6gd.16xlarge`
**Note**
The `r6gd` family is available in the following regions: `us-east-2`, `us-east-1`, `us-west-2`, `us-west-1`, `eu-west-1`, `eu-central-1`, `ap-northeast-1`, `ap-southeast-1`, `ap-southeast-2`.

    **R6g node types:**`cache.r6g.large`, `cache.r6g.xlarge`, `cache.r6g.2xlarge`, `cache.r6g.4xlarge`, `cache.r6g.12xlarge`, `cache.r6g.24xlarge`

    **R5 node types:**`cache.r5.large`, `cache.r5.xlarge`, `cache.r5.2xlarge`, `cache.r5.4xlarge`, `cache.r5.12xlarge`, `cache.r5.24xlarge`

    **R4 node types:**`cache.r4.large`, `cache.r4.xlarge`, `cache.r4.2xlarge`, `cache.r4.4xlarge`, `cache.r4.8xlarge`, `cache.r4.16xlarge`
  + Previous generation: (not recommended)

    **M2 node types:**`cache.m2.xlarge`, `cache.m2.2xlarge`, `cache.m2.4xlarge`

    **R3 node types:**`cache.r3.large`, `cache.r3.xlarge`, `cache.r3.2xlarge`, `cache.r3.4xlarge`, `cache.r3.8xlarge`
+ Network optimized:
  + Current generation:

    **C8gn node types:**`cache.c8gn.large`, `cache.c8gn.xlarge`, `cache.c8gn.2xlarge`, `cache.c8gn.4xlarge`, `cache.c8gn.8xlarge`, `cache.c8gn.12xlarge`, `cache.c8gn.16xlarge`

    **C7gn node types:**`cache.c7gn.large`, `cache.c7gn.xlarge`, `cache.c7gn.2xlarge`, `cache.c7gn.4xlarge`, `cache.c7gn.8xlarge`, `cache.c7gn.12xlarge`, `cache.c7gn.16xlarge`
For region availability, see [Supported Node Types by Amazon Region](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion)
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CacheParameterGroupName`  <a name="cfn-elasticache-replicationgroup-cacheparametergroupname"></a>
The name of the parameter group to associate with this replication group. If this argument is omitted, the default cache parameter group for the specified engine is used.
If you are running Valkey or Redis OSS version 3.2.4 or later, only one node group (shard), and want to use a default parameter group, we recommend that you specify the parameter group by name.
+ To create a Valkey or Redis OSS (cluster mode disabled) replication group, use `CacheParameterGroupName=default.redis3.2`.
+ To create a Valkey or Redis OSS (cluster mode enabled) replication group, use `CacheParameterGroupName=default.redis3.2.cluster.on`.
If this replication group is associated with a Global Datastore, Amazon ElastiCache automatically replaces the parameter group with a global parameter group. After that, you cannot modify `CacheParameterGroupName` on this replication group. Any AWS CloudFormation stack update that attempts to change this property will fail. To modify parameters for a replication group in a Global Datastore, use the global parameter group directly through the `AWS::ElastiCache::GlobalReplicationGroup` resource.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CacheSubnetGroupName`  <a name="cfn-elasticache-replicationgroup-cachesubnetgroupname"></a>
The name of the cache subnet group to be used for the replication group.
If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see [AWS::ElastiCache::SubnetGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html).
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClusterMode`  <a name="cfn-elasticache-replicationgroup-clustermode"></a>
The mode can be enabled or disabled. To change the cluster mode from disabled to enabled, you must first set the cluster mode to compatible. The compatible mode allows your Valkey or Redis OSS clients to connect using both cluster mode enabled and cluster mode disabled. After you migrate all Valkey or Redis OSS clients to use cluster mode enabled, you can then complete cluster mode configuration and set the cluster mode to enabled. For more information, see [Modify cluster mode](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/modify-cluster-mode.html).
Valid values: `enabled` \| `disabled` \| `compatible`
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DataTieringEnabled`  <a name="cfn-elasticache-replicationgroup-datatieringenabled"></a>
Enables data tiering. Data tiering is only supported for replication groups using the r6gd node type. This parameter must be set to true when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/data-tiering.html).
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Durability`  <a name="cfn-elasticache-replicationgroup-durability"></a>
Specifies the durability setting for the replication group. When set to `default`, the service determines the effective durability based on the engine version, cluster mode, and other parameters. The resolved setting is reflected in the `EffectiveDurability` property of the replication group. For more information, see [Durability](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/durability.html).
*Required*: No
*Type*: String
*Allowed values*: `default | async | sync | disabled`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-elasticache-replicationgroup-engine"></a>
The name of the cache engine to be used for the clusters in this replication group. The value must be set to `valkey` or `redis`.
Upgrading an existing engine from redis to valkey is done through in-place migration, and requires a parameter group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EngineVersion`  <a name="cfn-elasticache-replicationgroup-engineversion"></a>
The version number of the cache engine to be used for the clusters in this replication group. To view the supported cache engine versions, use the `DescribeCacheEngineVersions` operation.
**Important:** You can upgrade to a newer engine version (see [Selecting a Cache Engine and Version](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement)) in the *ElastiCache User Guide*, but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalReplicationGroupId`  <a name="cfn-elasticache-replicationgroup-globalreplicationgroupid"></a>
The name of the Global datastore
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpDiscovery`  <a name="cfn-elasticache-replicationgroup-ipdiscovery"></a>
The network type you choose when creating a replication group, either `ipv4` \| `ipv6`. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 or Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](https://aws.amazon.com/ec2/nitro/).
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | ipv6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyId`  <a name="cfn-elasticache-replicationgroup-kmskeyid"></a>
The ID of the KMS key used to encrypt the disk on the cluster.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogDeliveryConfigurations`  <a name="cfn-elasticache-replicationgroup-logdeliveryconfigurations"></a>
Specifies the destination, format and type of the logs.
*Required*: No
*Type*: Array of [LogDeliveryConfigurationRequest](aws-properties-elasticache-replicationgroup-logdeliveryconfigurationrequest.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MultiAZEnabled`  <a name="cfn-elasticache-replicationgroup-multiazenabled"></a>
A flag indicating if you have Multi-AZ enabled to enhance fault tolerance. For more information, see [Minimizing Downtime: Multi-AZ](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/AutoFailover.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkType`  <a name="cfn-elasticache-replicationgroup-networktype"></a>
Must be either `ipv4` \| `ipv6` \| `dual_stack`. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](https://aws.amazon.com/ec2/nitro/).
*Required*: No
*Type*: String
*Allowed values*: `ipv4 | ipv6 | dual_stack`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NodeGroupConfiguration`  <a name="cfn-elasticache-replicationgroup-nodegroupconfiguration"></a>
`NodeGroupConfiguration ` is a property of the `AWS::ElastiCache::ReplicationGroup` resource that configures an Amazon ElastiCache (ElastiCache) Valkey or Redis OSS cluster node group.
If you set [UseOnlineResharding](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-useonlineresharding) to `true`, you can update `NodeGroupConfiguration` without interruption. When `UseOnlineResharding` is set to `false`, or is not specified, updating `NodeGroupConfiguration` results in [replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement).
*Required*: No
*Type*: [Array](aws-properties-elasticache-replicationgroup-nodegroupconfiguration.md) of [NodeGroupConfiguration](aws-properties-elasticache-replicationgroup-nodegroupconfiguration.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`NotificationTopicArn`  <a name="cfn-elasticache-replicationgroup-notificationtopicarn"></a>
The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.
The Amazon SNS topic owner must be the same as the cluster owner.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumCacheClusters`  <a name="cfn-elasticache-replicationgroup-numcacheclusters"></a>
The number of clusters this replication group initially has.
This parameter is not used if there is more than one node group (shard). You should use `ReplicasPerNodeGroup` instead.
If `AutomaticFailoverEnabled` is `true`, the value of this parameter must be at least 2. If `AutomaticFailoverEnabled` is `false` you can omit this parameter (it will default to 1), or you can explicitly set it to a value between 2 and 6.
The maximum permitted value for `NumCacheClusters` is 6 (1 primary plus 5 replicas).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumNodeGroups`  <a name="cfn-elasticache-replicationgroup-numnodegroups"></a>
An optional parameter that specifies the number of node groups (shards) for this Valkey or Redis OSS (cluster mode enabled) replication group. For Valkey or Redis OSS (cluster mode disabled) either omit this parameter or set it to 1.
If you set [UseOnlineResharding](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-useonlineresharding) to `true`, you can update `NumNodeGroups` without interruption. When `UseOnlineResharding` is set to `false`, or is not specified, updating `NumNodeGroups` results in [replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement).
Default: 1
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-elasticache-replicationgroup-port"></a>
The port number on which each member of the replication group accepts connections.
*Required*: No
*Type*: Integer
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreferredCacheClusterAZs`  <a name="cfn-elasticache-replicationgroup-preferredcacheclusterazs"></a>
A list of EC2 Availability Zones in which the replication group's clusters are created. The order of the Availability Zones in the list is the order in which clusters are allocated. The primary cluster is created in the first AZ in the list.
This parameter is not used if there is more than one node group (shard). You should use `NodeGroupConfiguration` instead.
If you are creating your replication group in an Amazon VPC (recommended), you can only locate clusters in Availability Zones associated with the subnets in the selected subnet group.
The number of Availability Zones listed must equal the value of `NumCacheClusters`.
Default: system chosen Availability Zones.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreferredMaintenanceWindow`  <a name="cfn-elasticache-replicationgroup-preferredmaintenancewindow"></a>
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
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrimaryClusterId`  <a name="cfn-elasticache-replicationgroup-primaryclusterid"></a>
The identifier of the cluster that serves as the primary for this replication group. This cluster must already exist and have a status of `available`.
This parameter is not required if `NumCacheClusters`, `NumNodeGroups`, or `ReplicasPerNodeGroup` is specified.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicasPerNodeGroup`  <a name="cfn-elasticache-replicationgroup-replicaspernodegroup"></a>
An optional parameter that specifies the number of replica nodes in each node group (shard). Valid values are 0 to 5.
Using `ReplicasPerNodeGroup` with `NodeGroupConfiguration` results in resource replacement. For online scaling, use `ReplicasPerNodeGroup` alone.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationGroupDescription`  <a name="cfn-elasticache-replicationgroup-replicationgroupdescription"></a>
A user-created description for the replication group.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationGroupId`  <a name="cfn-elasticache-replicationgroup-replicationgroupid"></a>
The replication group identifier. This parameter is stored as a lowercase string.
Constraints:
+ A name must contain from 1 to 40 alphanumeric characters or hyphens.
+ The first character must be a letter.
+ A name cannot end with a hyphen or contain two consecutive hyphens.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecurityGroupIds`  <a name="cfn-elasticache-replicationgroup-securitygroupids"></a>
One or more Amazon VPC security groups associated with this replication group.
Use this parameter only when you are creating a replication group in an Amazon Virtual Private Cloud (Amazon VPC).
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotArns`  <a name="cfn-elasticache-replicationgroup-snapshotarns"></a>
A list of Amazon Resource Names (ARN) that uniquely identify the Valkey or Redis OSS RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new replication group. The Amazon S3 object name in the ARN cannot contain any commas. The new replication group will have the number of node groups (console: shards) specified by the parameter *NumNodeGroups* or the number of node groups configured by *NodeGroupConfiguration* regardless of the number of ARNs specified here.
Example of an Amazon S3 ARN: `arn:aws:s3:::my_bucket/snapshot1.rdb`
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotName`  <a name="cfn-elasticache-replicationgroup-snapshotname"></a>
The name of a snapshot from which to restore data into the new replication group. The snapshot status changes to `restoring` while the new replication group is being created.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotRetentionLimit`  <a name="cfn-elasticache-replicationgroup-snapshotretentionlimit"></a>
The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set `SnapshotRetentionLimit` to 5, a snapshot that was taken today is retained for 5 days before being deleted.
Default: 0 (i.e., automatic backups are disabled for this cluster).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshottingClusterId`  <a name="cfn-elasticache-replicationgroup-snapshottingclusterid"></a>
The cluster ID that is used as the daily snapshot source for the replication group. This parameter cannot be set for Valkey or Redis OSS (cluster mode enabled) replication groups.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotWindow`  <a name="cfn-elasticache-replicationgroup-snapshotwindow"></a>
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: `05:00-09:00`
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-elasticache-replicationgroup-tags"></a>
A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key=`myKey`, Value=`myKeyValue`. You can include multiple tags as shown following: Key=`myKey`, Value=`myKeyValue` Key=`mySecondKey`, Value=`mySecondKeyValue`. Tags on replication groups will be replicated to all nodes.
*Required*: No
*Type*: Array of [Tag](aws-properties-elasticache-replicationgroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitEncryptionEnabled`  <a name="cfn-elasticache-replicationgroup-transitencryptionenabled"></a>
A flag that enables in-transit encryption when set to `true`.
This parameter is only available when creating a replication group in an Amazon VPC using Valkey version `7.2` and above, Redis OSS version `3.2.6`, or Redis OSS version `4.x` and above, and the cluster is being created in an Amazon VPC.
If you enable in-transit encryption, you must also specify a value for `CacheSubnetGroup`.
TransitEncryptionEnabled is required when creating a new valkey replication group.
Default: `false`
For HIPAA compliance, you must specify `TransitEncryptionEnabled` as `true`, an `AuthToken`, and a `CacheSubnetGroup`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TransitEncryptionMode`  <a name="cfn-elasticache-replicationgroup-transitencryptionmode"></a>
A setting that allows you to migrate your clients to use in-transit encryption, with no downtime.
When setting `TransitEncryptionEnabled` to `true`, you can set your `TransitEncryptionMode` to `preferred` in the same request, to allow both encrypted and unencrypted connections at the same time. Once you migrate all your Valkey or Redis OSS clients to use encrypted connections you can modify the value to `required` to allow encrypted connections only.
Setting `TransitEncryptionMode` to `required` is a two-step process that requires you to first set the `TransitEncryptionMode` to `preferred`, after that you can set `TransitEncryptionMode` to `required`.
This process will not trigger the replacement of the replication group.
*Required*: No
*Type*: String
*Allowed values*: `preferred | required`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserGroupIds`  <a name="cfn-elasticache-replicationgroup-usergroupids"></a>
The ID of user group to associate with the replication group.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-elasticache-replicationgroup-return-values"></a>

### Ref
<a name="aws-resource-elasticache-replicationgroup-return-values-ref"></a>

When the logical ID of this resource is provided to the Ref intrinsic function, Ref returns the resource name.

 For more information about using the Ref function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticache-replicationgroup-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-elasticache-replicationgroup-return-values-fn--getatt-fn--getatt"></a>

`ConfigurationEndPoint.Address`  <a name="ConfigurationEndPoint.Address-fn::getatt"></a>
 The DNS hostname of the cache node.
Valkey or Redis OSS (cluster mode disabled) replication groups don't have this attribute. Therefore, `Fn::GetAtt` returns a value for this attribute only if the replication group is clustered. Otherwise, `Fn::GetAtt` fails. For Valkey or Redis OSS (cluster mode disabled) replication groups, use the `PrimaryEndpoint` or `ReadEndpoint` attributes.

`ConfigurationEndPoint.Port`  <a name="ConfigurationEndPoint.Port-fn::getatt"></a>
The port number that the cache engine is listening on.

`EffectiveDurability`  <a name="EffectiveDurability-fn::getatt"></a>
The effective durability of the replication group. When `Durability` is set to `default`, the service resolves the actual durability based on the engine version, cluster mode, and other parameters. This field reflects the resolved value. For more information, see [Configuring Durability](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/Durability.Configuring.html).

`PrimaryEndPoint.Address`  <a name="PrimaryEndPoint.Address-fn::getatt"></a>
The DNS address of the primary read-write cache node.

`PrimaryEndPoint.Port`  <a name="PrimaryEndPoint.Port-fn::getatt"></a>
The number of the port that the primary read-write cache engine is listening on.

`ReadEndPoint.Addresses`  <a name="ReadEndPoint.Addresses-fn::getatt"></a>
A string with a list of endpoints for the read-only replicas. The order of the addresses maps to the order of the ports from the `ReadEndPoint.Ports` attribute.

`ReadEndPoint.AddressesList`  <a name="ReadEndPoint.AddressesList-fn::getatt"></a>
Property description not available.

`ReadEndPoint.Ports`  <a name="ReadEndPoint.Ports-fn::getatt"></a>
A string with a list of ports for the read-only replicas. The order of the ports maps to the order of the addresses from the `ReadEndPoint.Addresses` attribute.

`ReadEndPoint.PortsList`  <a name="ReadEndPoint.PortsList-fn::getatt"></a>
Property description not available.

`ReaderEndPoint.Address`  <a name="ReaderEndPoint.Address-fn::getatt"></a>
The address of the reader endpoint.

`ReaderEndPoint.Port`  <a name="ReaderEndPoint.Port-fn::getatt"></a>
The port used by the reader endpoint.

## Examples
<a name="aws-resource-elasticache-replicationgroup--examples"></a>

**Topics**
+ [Declare a Replication Group with Two Nodes](#aws-resource-elasticache-replicationgroup--examples--Declare_a_Replication_Group_with_Two_Nodes)
+ [Declare a Replication Group with Two Node Groups](#aws-resource-elasticache-replicationgroup--examples--Declare_a_Replication_Group_with_Two_Node_Groups)

### Declare a Replication Group with Two Nodes
<a name="aws-resource-elasticache-replicationgroup--examples--Declare_a_Replication_Group_with_Two_Nodes"></a>

The following example declares a replication group with two nodes and automatic failover enabled.

#### JSON
<a name="aws-resource-elasticache-replicationgroup--examples--Declare_a_Replication_Group_with_Two_Nodes--json"></a>

```
{
    "myReplicationGroup": {
        "Type": "AWS::ElastiCache::ReplicationGroup",
        "Properties": {
            "ReplicationGroupDescription": "my description",
            "NumCacheClusters": "2",
            "Engine": "redis",
            "CacheNodeType": "cache.m3.medium",
            "AutomaticFailoverEnabled": "true",
            "CacheSubnetGroupName": "subnetgroup",
            "EngineVersion": "2.8.6",
            "PreferredMaintenanceWindow": "wed:09:25-wed:22:30",
            "SnapshotRetentionLimit": "4",
            "SnapshotWindow": "03:30-05:30"
        }
    }
}
```

#### YAML
<a name="aws-resource-elasticache-replicationgroup--examples--Declare_a_Replication_Group_with_Two_Nodes--yaml"></a>

```
myReplicationGroup:
  Type: 'AWS::ElastiCache::ReplicationGroup'
  Properties:
    ReplicationGroupDescription: my description
    NumCacheClusters: '2'
    Engine: redis
    CacheNodeType: cache.m3.medium
    AutomaticFailoverEnabled: 'true'
    CacheSubnetGroupName: subnetgroup
    EngineVersion: 2.8.6
    PreferredMaintenanceWindow: 'wed:09:25-wed:22:30'
    SnapshotRetentionLimit: '4'
    SnapshotWindow: '03:30-05:30'
```

### Declare a Replication Group with Two Node Groups
<a name="aws-resource-elasticache-replicationgroup--examples--Declare_a_Replication_Group_with_Two_Node_Groups"></a>

The following example declares a replication group with two nodes groups (shards) with three replicas in each group.

#### JSON
<a name="aws-resource-elasticache-replicationgroup--examples--Declare_a_Replication_Group_with_Two_Node_Groups--json"></a>

```
{
    "BasicReplicationGroup": {
        "Type": "AWS::ElastiCache::ReplicationGroup",
        "Properties": {
            "AutomaticFailoverEnabled": true,
            "CacheNodeType": "cache.r3.large",
            "CacheSubnetGroupName": {
                "Ref": "CacheSubnetGroup"
            },
            "Engine": "redis",
            "EngineVersion": "3.2",
            "NumNodeGroups": "2",
            "ReplicasPerNodeGroup": "3",
            "Port": 6379,
            "PreferredMaintenanceWindow": "sun:05:00-sun:09:00",
            "ReplicationGroupDescription": "A sample replication group",
            "SecurityGroupIds": [
                {
                    "Ref": "ReplicationGroupSG"
                }
            ],
            "SnapshotRetentionLimit": 5,
            "SnapshotWindow": "10:00-12:00"
        }
    }
}
```

#### YAML
<a name="aws-resource-elasticache-replicationgroup--examples--Declare_a_Replication_Group_with_Two_Node_Groups--yaml"></a>

```
BasicReplicationGroup:
  Type: 'AWS::ElastiCache::ReplicationGroup'
  Properties:
    AutomaticFailoverEnabled: true
    CacheNodeType: cache.r3.large
    CacheSubnetGroupName: !Ref CacheSubnetGroup
    Engine: redis
    EngineVersion: '3.2'
    NumNodeGroups: '2'
    ReplicasPerNodeGroup: '3'
    Port: 6379
    PreferredMaintenanceWindow: 'sun:05:00-sun:09:00'
    ReplicationGroupDescription: A sample replication group
    SecurityGroupIds:
      - !Ref ReplicationGroupSG
    SnapshotRetentionLimit: 5
    SnapshotWindow: '10:00-12:00'
```

## See also
<a name="aws-resource-elasticache-replicationgroup--seealso"></a>

[CreateReplicationGroup](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateReplicationGroup.html) in the *Amazon ElastiCache API Reference Guide*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
