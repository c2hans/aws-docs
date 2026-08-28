---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_NodeGroup.html
---

# NodeGroup
<a name="API_NodeGroup"></a>

Represents a collection of cache nodes in a replication group. One node in the node group is the read/write primary node. All the other nodes are read-only Replica nodes.

## Contents
<a name="API_NodeGroup_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** NodeGroupId **
The identifier for the node group (shard). A Valkey or Redis OSS (cluster mode disabled) replication group contains only 1 node group; therefore, the node group ID is 0001. A Valkey or Redis OSS (cluster mode enabled) replication group contains 1 to 90 node groups numbered 0001 to 0090. Optionally, the user can provide the id for a node group.
Type: String
Required: No

 ** NodeGroupMembers.NodeGroupMember.N **
A list containing information about individual nodes within the node group (shard).
Type: Array of [NodeGroupMember](API_NodeGroupMember.md) objects
Required: No

 ** PrimaryEndpoint **
The endpoint of the primary node in this node group (shard).
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** ReaderEndpoint **
The endpoint of the replica nodes in this node group (shard). This value is read-only.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** Slots **
The keyspace for this node group (shard).
Type: String
Required: No

 ** Status **
The current state of this replication group - `creating`, `available`, `modifying`, `deleting`.
Type: String
Required: No

## See Also
<a name="API_NodeGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/NodeGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/NodeGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/NodeGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
