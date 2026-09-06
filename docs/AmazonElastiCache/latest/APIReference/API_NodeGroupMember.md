---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_NodeGroupMember.html
---

# NodeGroupMember
<a name="API_NodeGroupMember"></a>

Represents a single node within a node group (shard).

## Contents
<a name="API_NodeGroupMember_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CacheClusterId **
The ID of the cluster to which the node belongs.
Type: String
Required: No

 ** CacheNodeId **
The ID of the node within its cluster. A node ID is a numeric identifier (0001, 0002, etc.).
Type: String
Required: No

 ** CurrentRole **
The role that is currently assigned to the node - `primary` or `replica`. This member is only applicable for Valkey or Redis OSS (cluster mode disabled) replication groups.
Type: String
Required: No

 ** PreferredAvailabilityZone **
The name of the Availability Zone in which the node is located.
Type: String
Required: No

 ** PreferredOutpostArn **
The outpost ARN of the node group member.
Type: String
Required: No

 ** ReadEndpoint **
The information required for client programs to connect to a node for read operations. The read endpoint is only applicable on Valkey or Redis OSS (cluster mode disabled) clusters.
Type: [Endpoint](API_Endpoint.md) object
Required: No

## See Also
<a name="API_NodeGroupMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/NodeGroupMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/NodeGroupMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/NodeGroupMember)
