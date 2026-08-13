---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CreateCacheCluster.html
---

# CreateCacheCluster
<a name="API_CreateCacheCluster"></a>

Creates a cluster. All nodes in the cluster run the same protocol-compliant cache engine software, either Memcached, Valkey or Redis OSS.

This operation is not supported for Valkey or Redis OSS (cluster mode enabled) clusters.

## Request Parameters
<a name="API_CreateCacheCluster_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** CacheClusterId **
The node group (shard) identifier. This parameter is stored as a lowercase string.
 **Constraints:**
+ A name must contain from 1 to 50 alphanumeric characters or hyphens.
+ The first character must be a letter.
+ A name cannot end with a hyphen or contain two consecutive hyphens.
Type: String
Required: Yes

 ** AuthToken **
 **Reserved parameter.** The password used to access a password protected server.
Password constraints:
+ Must be only printable ASCII characters.
+ Must be at least 16 characters and no more than 128 characters in length.
+ The only permitted printable special characters are \!, &, \#, $, ^, <, >, and -. Other printable special characters cannot be used in the AUTH token.
For more information, see [AUTH password](http://redis.io/commands/AUTH) at http://redis.io/commands/AUTH.
Type: String
Required: No

 ** AutoMinorVersionUpgrade **
 If you are running Valkey 7.2 and above or Redis OSS engine version 6.0 and above, set this parameter to yes to opt-in to the next auto minor version upgrade campaign. This parameter is disabled for previous versions.
Type: Boolean
Required: No

 ** AZMode **
Specifies whether the nodes in this Memcached cluster are created in a single Availability Zone or created across multiple Availability Zones in the cluster's region.
This parameter is only supported for Memcached clusters.
If the `AZMode` and `PreferredAvailabilityZones` are not specified, ElastiCache assumes `single-az` mode.
Type: String
Valid Values: `single-az | cross-az`
Required: No

 ** CacheNodeType **
The compute and memory capacity of the nodes in the node group (shard).
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
The name of the parameter group to associate with this cluster. If this argument is omitted, the default parameter group for the specified engine is used. You cannot use any parameter group which has `cluster-enabled='yes'` when creating a cluster.
Type: String
Required: No

 **CacheSecurityGroupNames.CacheSecurityGroupName.N**
A list of security group names to associate with this cluster.
Use this parameter only when you are creating a cluster outside of an Amazon Virtual Private Cloud (Amazon VPC).
Type: Array of strings
Required: No

 ** CacheSubnetGroupName **
The name of the subnet group to be used for the cluster.
Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).
If you're going to launch your cluster in an Amazon VPC, you need to create a subnet group before you start creating a cluster. For more information, see [Subnets and Subnet Groups](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SubnetGroups.html).
Type: String
Required: No

 ** Engine **
The name of the cache engine to be used for this cluster.
Valid values for this parameter are: `memcached` \| `redis`
Type: String
Required: No

 ** EngineVersion **
The version number of the cache engine to be used for this cluster. To view the supported cache engine versions, use the DescribeCacheEngineVersions operation.
 **Important:** You can upgrade to a newer engine version (see [Selecting a Cache Engine and Version](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/SelectEngine.html#VersionManagement)), but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster or replication group and create it anew with the earlier engine version.
Type: String
Required: No

 ** IpDiscovery **
The network type you choose when modifying a cluster, either `ipv4` \| `ipv6`. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/).
Type: String
Valid Values: `ipv4 | ipv6`
Required: No

 **LogDeliveryConfigurations.LogDeliveryConfigurationRequest.N**
Specifies the destination, format and type of the logs.
Type: Array of [LogDeliveryConfigurationRequest](API_LogDeliveryConfigurationRequest.md) objects
Required: No

 ** NetworkType **
Must be either `ipv4` \| `ipv6` \| `dual_stack`. IPv6 is supported for workloads using Valkey 7.2 and above, Redis OSS engine version 6.2 to 7.1 and Memcached engine version 1.6.6 and above on all instances built on the [Nitro system](http://aws.amazon.com/ec2/nitro/).
Type: String
Valid Values: `ipv4 | ipv6 | dual_stack`
Required: No

 ** NotificationTopicArn **
The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.
The Amazon SNS topic owner must be the same as the cluster owner.
Type: String
Required: No

 ** NumCacheNodes **
The initial number of cache nodes that the cluster has.
For clusters running Valkey or Redis OSS, this value must be 1. For clusters running Memcached, this value must be between 1 and 40.
If you need more than 40 nodes for your Memcached cluster, please fill out the ElastiCache Limit Increase Request form at [http://aws.amazon.com/contact-us/elasticache-node-limit-request/](http://aws.amazon.com/contact-us/elasticache-node-limit-request/).
Type: Integer
Required: No

 ** OutpostMode **
Specifies whether the nodes in the cluster are created in a single outpost or across multiple outposts.
Type: String
Valid Values: `single-outpost | cross-outpost`
Required: No

 ** Port **
The port number on which each of the cache nodes accepts connections.
Type: Integer
Required: No

 ** PreferredAvailabilityZone **
The EC2 Availability Zone in which the cluster is created.
All nodes belonging to this cluster are placed in the preferred Availability Zone. If you want to create your nodes across multiple Availability Zones, use `PreferredAvailabilityZones`.
Default: System chosen Availability Zone.
Type: String
Required: No

 **PreferredAvailabilityZones.PreferredAvailabilityZone.N**
A list of the Availability Zones in which cache nodes are created. The order of the zones in the list is not important.
This option is only supported on Memcached.
If you are creating your cluster in an Amazon VPC (recommended) you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group.
The number of Availability Zones listed must equal the value of `NumCacheNodes`.
If you want all the nodes in the same Availability Zone, use `PreferredAvailabilityZone` instead, or repeat the Availability Zone multiple times in the list.
Default: System chosen Availability Zones.
Type: Array of strings
Required: No

 ** PreferredMaintenanceWindow **
Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.
Type: String
Required: No

 ** PreferredOutpostArn **
The outpost ARN in which the cache cluster is created.
Type: String
Required: No

 **PreferredOutpostArns.PreferredOutpostArn.N**
The outpost ARNs in which the cache cluster is created.
Type: Array of strings
Required: No

 ** ReplicationGroupId **
The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
If the specified replication group is Multi-AZ enabled and the Availability Zone is not specified, the cluster is created in Availability Zones that provide the best spread of read replicas across Availability Zones.
This parameter is only valid if the `Engine` parameter is `redis`.
Type: String
Required: No

 **SecurityGroupIds.SecurityGroupId.N**
One or more VPC security groups associated with the cluster.
Use this parameter only when you are creating a cluster in an Amazon Virtual Private Cloud (Amazon VPC).
Type: Array of strings
Required: No

 **SnapshotArns.SnapshotArn.N**
A single-element string list containing an Amazon Resource Name (ARN) that uniquely identifies a Valkey or Redis OSS RDB snapshot file stored in Amazon S3. The snapshot file is used to populate the node group (shard). The Amazon S3 object name in the ARN cannot contain any commas.
This parameter is only valid if the `Engine` parameter is `redis`.
Example of an Amazon S3 ARN: `arn:aws:s3:::my_bucket/snapshot1.rdb`
Type: Array of strings
Required: No

 ** SnapshotName **
The name of a Valkey or Redis OSS snapshot from which to restore data into the new node group (shard). The snapshot status changes to `restoring` while the new node group (shard) is being created.
This parameter is only valid if the `Engine` parameter is `redis`.
Type: String
Required: No

 ** SnapshotRetentionLimit **
The number of days for which ElastiCache retains automatic snapshots before deleting them. For example, if you set `SnapshotRetentionLimit` to 5, a snapshot taken today is retained for 5 days before being deleted.
This parameter is only valid if the `Engine` parameter is `redis`.
Default: 0 (i.e., automatic backups are disabled for this cache cluster).
Type: Integer
Required: No

 ** SnapshotWindow **
The daily time range (in UTC) during which ElastiCache begins taking a daily snapshot of your node group (shard).
Example: `05:00-09:00`
If you do not specify this parameter, ElastiCache automatically chooses an appropriate time range.
This parameter is only valid if the `Engine` parameter is `redis`.
Type: String
Required: No

 **Tags.Tag.N**
A list of tags to be added to this resource.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TransitEncryptionEnabled **
A flag that enables in-transit encryption when set to true.
Type: Boolean
Required: No

## Response Elements
<a name="API_CreateCacheCluster_ResponseElements"></a>

The following element is returned by the service.

 ** CacheCluster **
Contains all of the attributes of a specific cluster.
Type: [CacheCluster](API_CacheCluster.md) object

## Errors
<a name="API_CreateCacheCluster_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CacheClusterAlreadyExists **
You already have a cluster with the given identifier.
HTTP Status Code: 400

 ** CacheParameterGroupNotFound **
The requested cache parameter group name does not refer to an existing cache parameter group.
HTTP Status Code: 404

 ** CacheSecurityGroupNotFound **
The requested cache security group name does not refer to an existing cache security group.
HTTP Status Code: 404

 ** CacheSubnetGroupNotFoundFault **
The requested cache subnet group name does not refer to an existing cache subnet group.
HTTP Status Code: 400

 ** ClusterQuotaForCustomerExceeded **
The request cannot be processed because it would exceed the allowed number of clusters per customer.
HTTP Status Code: 400

 ** InsufficientCacheClusterCapacity **
The requested cache node type is not available in the specified Availability Zone. For more information, see [InsufficientCacheClusterCapacity](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ErrorMessages.html#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY) in the ElastiCache User Guide.
HTTP Status Code: 400

 ** InvalidParameterCombination **
Two or more incompatible parameters were specified.
 ** message **
Two or more parameters that must not be used together were used together.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidReplicationGroupState **
The requested replication group is not in the `available` state.
HTTP Status Code: 400

 ** InvalidVPCNetworkStateFault **
The VPC network is in an invalid state.
HTTP Status Code: 400

 ** NodeQuotaForClusterExceeded **
The request cannot be processed because it would exceed the allowed number of cache nodes in a single cluster.
HTTP Status Code: 400

 ** NodeQuotaForCustomerExceeded **
The request cannot be processed because it would exceed the allowed number of cache nodes per customer.
HTTP Status Code: 400

 ** ReplicationGroupNotFoundFault **
The specified replication group does not exist.
HTTP Status Code: 404

 ** TagQuotaPerResourceExceeded **
The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.
HTTP Status Code: 400

## Examples
<a name="API_CreateCacheCluster_Examples"></a>

### CreateCacheCluster
<a name="API_CreateCacheCluster_Example_1"></a>

This example illustrates one usage of CreateCacheCluster.

#### Sample Request
<a name="API_CreateCacheCluster_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
	?Action=CreateCacheCluster
	&CacheClusterId=myMemcachedCluster
	&CacheNodeType=cache.m1.small
	&CacheSecurityGroupNames.CacheSecurityGroupName.1=default
	&Engine=memcached
	&NumCacheNodes=3
	&PreferredAvailabilityZones.PreferredAvailabilityZone.1=us-west-2a
	&PreferredAvailabilityZones.PreferredAvailabilityZone.2=us-west-2b
	&PreferredAvailabilityZones.PreferredAvailabilityZone.3=us-west-2c
	&SignatureMethod=HmacSHA256
	&SignatureVersion=4
	&Version=2015-02-02
	&X-Amz-Algorithm=AWS4-HMAC-SHA256
	&X-Amz-Credential=[your-access-key-id]/20150202/us-west-2/elasticache/AWS4_request
	&X-Amz-Date=20150202T170651Z
	&X-Amz-SignedHeaders=content-type;host;user-agent;x-amz-content-sha256;x-amz-date
	&X-Amz-Signature=[signature-value]
```

#### Sample Response
<a name="API_CreateCacheCluster_Example_1_Response"></a>

```
<CreateCacheClusterResponse xmlns="http://elasticache.amazonaws.com/doc/2015-02-02/">
  <CreateCacheClusterResult>
    <CacheCluster>
      <CacheClusterId>myMemcachedClustger</CacheClusterId>
      <CacheClusterStatus>creating</CacheClusterStatus>
      <CacheParameterGroup>
        <CacheParameterGroupName>default.memcached1.4</CacheParameterGroupName>
        <ParameterApplyStatus>in-sync</ParameterApplyStatus>
        <CacheNodeIdsToReboot/>
      </CacheParameterGroup>
      <CacheNodeType>cache.m1.small</CacheNodeType>
      <Engine>memcached</Engine>
      <PendingModifiedValues/>
      <EngineVersion>1.4.14</EngineVersion>
      <AutoMinorVersionUpgrade>true</AutoMinorVersionUpgrade>
      <PreferredMaintenanceWindow>sat:09:00-sat:10:00</PreferredMaintenanceWindow>
      <ClientDownloadLandingPage>https://console.aws.amazon.com/elasticache/home#client-download:</ClientDownloadLandingPage>
      <CacheSecurityGroups>
        <CacheSecurityGroup>
          <CacheSecurityGroupName>default</CacheSecurityGroupName>
          <Status>active</Status>
        </CacheSecurityGroup>
      </CacheSecurityGroups>
      <NumCacheNodes>3</NumCacheNodes>
    </CacheCluster>
  </CreateCacheClusterResult>
  <ResponseMetadata>
    <RequestId>69134921-10f9-11e4-81bb-d76bad68b8fd</RequestId>
  </ResponseMetadata>
</CreateCacheClusterResponse>
```

## See Also
<a name="API_CreateCacheCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/CreateCacheCluster)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/CreateCacheCluster)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CreateCacheCluster)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/CreateCacheCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CreateCacheCluster)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/CreateCacheCluster)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/CreateCacheCluster)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/CreateCacheCluster)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/CreateCacheCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CreateCacheCluster)
