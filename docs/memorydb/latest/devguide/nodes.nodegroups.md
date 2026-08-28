---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.nodegroups.html
---

# MemoryDB nodes and shards
<a name="nodes.nodegroups"></a>

A shard is a hierarchical arrangement of nodes, each wrapped in a cluster. Shards support replication. Within a shard, one node functions as the read/write primary node. All the other nodes in a shard function as read-only replicas of the primary node. MemoryDB supports multiple shards within a cluster. This support enables partitioning of your data in a MemoryDB cluster.

MemoryDB supports replication via shards. The API operation [DescribeClusters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeClusters.html) lists the shards with the member nodes, the node names, endpoints and also other information.

After a MemoryDB cluster is created, it can be altered (scaled in or out). For more information, see [Scaling](scaling.md) and [Replacing nodes](nodes.nodereplacement.md).

When you create a new cluster, you can seed it with data from the old cluster so it doesn't start out empty. Doing this can be helpful if you need change your node type, engine version or migrate from Amazon ElastiCache (Redis OSS). For more information, see [Making manual snapshots](snapshots-manual.md) and [Restoring from a snapshot](snapshots-restoring.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
