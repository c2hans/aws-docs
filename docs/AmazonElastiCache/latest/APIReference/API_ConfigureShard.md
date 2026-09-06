---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_ConfigureShard.html
---

# ConfigureShard
<a name="API_ConfigureShard"></a>

Node group (shard) configuration options when adding or removing replicas. Each node group (shard) configuration has the following members: NodeGroupId, NewReplicaCount, and PreferredAvailabilityZones.

## Contents
<a name="API_ConfigureShard_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** NewReplicaCount **
The number of replicas you want in this node group at the end of this operation. The maximum value for `NewReplicaCount` is 5. The minimum value depends upon the type of Valkey or Redis OSS replication group you are working with.
The minimum number of replicas in a shard or replication group is:
+ Valkey or Redis OSS (cluster mode disabled)
  + If Multi-AZ: 1
  + If Multi-AZ: 0
+ Valkey or Redis OSS (cluster mode enabled): 0 (though you will not be able to failover to a replica if your primary node fails)
Type: Integer
Required: Yes

 ** NodeGroupId **
The 4-digit id for the node group you are configuring. For Valkey or Redis OSS (cluster mode disabled) replication groups, the node group id is always 0001. To find a Valkey or Redis OSS (cluster mode enabled)'s node group's (shard's) id, see [Finding a Shard's Id](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/shard-find-id.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4.
Pattern: `\d+`
Required: Yes

 ** PreferredAvailabilityZones.PreferredAvailabilityZone.N **
A list of `PreferredAvailabilityZone` strings that specify which availability zones the replication group's nodes are to be in. The nummber of `PreferredAvailabilityZone` values must equal the value of `NewReplicaCount` plus 1 to account for the primary node. If this member of `ReplicaConfiguration` is omitted, ElastiCache selects the availability zone for each of the replicas.
Type: Array of strings
Required: No

 ** PreferredOutpostArns.PreferredOutpostArn.N **
The outpost ARNs in which the cache cluster is created.
Type: Array of strings
Required: No

## See Also
<a name="API_ConfigureShard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/ConfigureShard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/ConfigureShard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/ConfigureShard)
