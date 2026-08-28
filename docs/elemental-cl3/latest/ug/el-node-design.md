---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/el-node-design.html
---

# Number of primary Elemental Live nodes
<a name="el-node-design"></a>

Determine the number of *primary nodes *you need:
+ You need at least sufficient Elemental Live nodes to run the channels for all the encoding workflows and MPTS workflows.
+ You don't need to run each SPTS channel on its own node. A node can run multiple channels, including multiple SPTS channels.

After you have determined the number of primary nodes, you should identify your redundant node requirements. See [Worker node redundancy](redundancy-worker.md).

**Rules for association between SPTS channels and the MPTS**

The following rules help you identify the number of nodes that you need.

The SPTS channels for a single MPTS can originate from one node.

![Diagram showing Elemental Live node A with three channels connecting to Elemental Statmux node MPTS.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/Channel-source-1-node.png)

Or the SPTS channels can originate from two or more nodes.

![Diagram showing two Elemental Live nodes connected to an Elemental Statmux node with MPTS.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/Channel-source-2-nodes.png)

A node can contain SPTS channels that go to different MPTSes. There is no requirement for a node to be dedicated to one MPTS. In the following diagram, node A contains SPTS channels for two different MPTSes.

![Diagram showing two Elemental Live nodes connected to two Elemental Statmux nodes with MPTS.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/node-feeds-2-mpts.png)

An SPTS channel can't be used by two different Statmux MPTS.

![Diagram showing incompatibility between Elemental Live node and two Elemental Statmux nodes.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/Channel-not-feed-2-mpts.png)

A node that has SPTS channels can also produce other channels (events). The node doesn't have to be dedicated to producing SPTSes.

![Diagram showing Elemental Live node A with channels connecting to Elemental Statmux node MPTS.](http://docs.aws.amazon.com/elemental-cl3/latest/ug/images/Node-produce-other-channels.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
