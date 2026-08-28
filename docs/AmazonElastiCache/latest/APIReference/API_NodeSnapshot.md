---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_NodeSnapshot.html
---

# NodeSnapshot
<a name="API_NodeSnapshot"></a>

Represents an individual cache node in a snapshot of a cluster.

## Contents
<a name="API_NodeSnapshot_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CacheClusterId **
A unique identifier for the source cluster.
Type: String
Required: No

 ** CacheNodeCreateTime **
The date and time when the cache node was created in the source cluster.
Type: Timestamp
Required: No

 ** CacheNodeId **
The cache node identifier for the node in the source cluster.
Type: String
Required: No

 ** CacheSize **
The size of the cache on the source cache node.
Type: String
Required: No

 ** NodeGroupConfiguration **
The configuration for the source node group (shard).
Type: [NodeGroupConfiguration](API_NodeGroupConfiguration.md) object
Required: No

 ** NodeGroupId **
A unique identifier for the source node group (shard).
Type: String
Required: No

 ** SnapshotCreateTime **
The date and time when the source node's metadata and cache data set was obtained for the snapshot.
Type: Timestamp
Required: No

## See Also
<a name="API_NodeSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/NodeSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/NodeSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/NodeSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
