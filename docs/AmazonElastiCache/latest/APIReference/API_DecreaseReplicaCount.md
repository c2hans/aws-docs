---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DecreaseReplicaCount.html
---

# DecreaseReplicaCount
<a name="API_DecreaseReplicaCount"></a>

Dynamically decreases the number of replicas in a Valkey or Redis OSS (cluster mode disabled) replication group or the number of replica nodes in one or more node groups (shards) of a Valkey or Redis OSS (cluster mode enabled) replication group. This operation is performed with no cluster down time.

## Request Parameters
<a name="API_DecreaseReplicaCount_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplyImmediately **
If `True`, the number of replica nodes is decreased immediately. `ApplyImmediately=False` is not currently supported.
Type: Boolean
Required: Yes

 ** ReplicationGroupId **
The id of the replication group from which you want to remove replica nodes.
Type: String
Required: Yes

 ** NewReplicaCount **
The number of read replica nodes you want at the completion of this operation. For Valkey or Redis OSS (cluster mode disabled) replication groups, this is the number of replica nodes in the replication group. For Valkey or Redis OSS (cluster mode enabled) replication groups, this is the number of replica nodes in each of the replication group's node groups.
The minimum number of replicas in a shard or replication group is:
+ Valkey or Redis OSS (cluster mode disabled)
  + If Multi-AZ is enabled: 1
  + If Multi-AZ is not enabled: 0
+ Valkey or Redis OSS (cluster mode enabled): 0 (though you will not be able to failover to a replica if your primary node fails)
Type: Integer
Required: No

 **ReplicaConfiguration.ConfigureShard.N**
A list of `ConfigureShard` objects that can be used to configure each shard in a Valkey or Redis OSS replication group. The `ConfigureShard` has three members: `NewReplicaCount`, `NodeGroupId`, and `PreferredAvailabilityZones`.
Type: Array of [ConfigureShard](API_ConfigureShard.md) objects
Required: No

 **ReplicasToRemove.member.N**
A list of the node ids to remove from the replication group or node group (shard).
Type: Array of strings
Required: No

## Response Elements
<a name="API_DecreaseReplicaCount_ResponseElements"></a>

The following element is returned by the service.

 ** ReplicationGroup **
Contains all of the attributes of a specific Valkey or Redis OSS replication group.
Type: [ReplicationGroup](API_ReplicationGroup.md) object

## Errors
<a name="API_DecreaseReplicaCount_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClusterQuotaForCustomerExceeded **
The request cannot be processed because it would exceed the allowed number of clusters per customer.
HTTP Status Code: 400

 ** InsufficientCacheClusterCapacity **
The requested cache node type is not available in the specified Availability Zone. For more information, see [InsufficientCacheClusterCapacity](http://docs.aws.amazon.com/AmazonElastiCache/latest/dg/ErrorMessages.html#ErrorMessages.INSUFFICIENT_CACHE_CLUSTER_CAPACITY) in the ElastiCache User Guide.
HTTP Status Code: 400

 ** InvalidCacheClusterState **
The requested cluster is not in the `available` state.
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

 ** NodeGroupsPerReplicationGroupQuotaExceeded **
The request cannot be processed because it would exceed the maximum allowed number of node groups (shards) in a single replication group. The default maximum is 90
HTTP Status Code: 400

 ** NodeQuotaForCustomerExceeded **
The request cannot be processed because it would exceed the allowed number of cache nodes per customer.
HTTP Status Code: 400

 ** NoOperationFault **
The operation was not performed because no changes were required.
HTTP Status Code: 400

 ** ReplicationGroupNotFoundFault **
The specified replication group does not exist.
HTTP Status Code: 404

 ** ServiceLinkedRoleNotFoundFault **
The specified service linked role (SLR) was not found.
HTTP Status Code: 400

## Examples
<a name="API_DecreaseReplicaCount_Examples"></a>

### Example
<a name="API_DecreaseReplicaCount_Example_1"></a>

The following example removes two replicas from each node group in the replication group `sample-repl-group`.

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DecreaseReplicaCount
   &ApplyImmediately=True
   &NewReplicaCount=2
   &ReplicasToRemove.ReplicaToRemove.1=0001
   &ReplicasToRemove.ReplicaToRemove.2=0003
   &ReplicationGroupId=sample-repl-group
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

### Example
<a name="API_DecreaseReplicaCount_Example_2"></a>

The following example removes replicas from two node groups. Because there are multiple node groups, this example is for a Valkey or Redis OSS (cluster mode enabled) replication group.

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DecreaseReplicaCount
   &ApplyImmediately=True
   &ReplicaConfiguration.ConfigureShard.1.NodeGroupId=0001
   &ReplicaConfiguration.ConfigureShard.1.NewReplicaCount=1
   &ReplicaConfiguration.ConfigureShard.1.PreferredAvailabilityZones.PreferredAvailabilityZone.1=us-east-1a
   &ReplicaConfiguration.ConfigureShard.1.PreferredAvailabilityZones.PreferredAvailabilityZone.2=us-east-1c
   &ReplicaConfiguration.ConfigureShard.2.NodeGroupId=0003
   &ReplicaConfiguration.ConfigureShard.2.NewReplicaCount=2
   &ReplicaConfiguration.ConfigureShard.2.PreferredAvailabilityZones.PreferredAvailabilityZone.1=us-east-1a
   &ReplicaConfiguration.ConfigureShard.2.PreferredAvailabilityZones.PreferredAvailabilityZone.2=us-east-1b
   &ReplicaConfiguration.ConfigureShard.2.PreferredAvailabilityZones.PreferredAvailabilityZone.4=us-east-1c
   &ReplicationGroupId=samplem--repl-group
   &Version=2015-02-02
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20150202T192317Z
   &X-Amz-Credential=<credential>
```

## See Also
<a name="API_DecreaseReplicaCount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/DecreaseReplicaCount)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/DecreaseReplicaCount)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/DecreaseReplicaCount)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/DecreaseReplicaCount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/DecreaseReplicaCount)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/DecreaseReplicaCount)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/DecreaseReplicaCount)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/DecreaseReplicaCount)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/DecreaseReplicaCount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/DecreaseReplicaCount)
