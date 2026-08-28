---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.html
---

# Managing nodes
<a name="nodes"></a>

A node is the smallest building block of a MemoryDB deployment. A node belongs to a shard which belongs to a cluster. Each node runs the engine version that was chosen when the cluster was created or last modified. Each node has its own Domain Name Service (DNS) name and port. Multiple types of MemoryDB nodes are supported, each with varying amounts of associated memory and computational power.

**Topics**
+ [MemoryDB nodes and shards](nodes.nodegroups.md)
+ [Supported node types](nodes.supportedtypes.md)
+ [MemoryDB reserved nodes](nodes.reservednodes.md)
+ [Replacing nodes](nodes.nodereplacement.md)

Important operations involving nodes include:
+ [Adding / Removing nodes from a cluster](clusters.deletenode.md)
+ [Scaling](scaling.md)
+ [Finding connection endpoints](endpoints.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
