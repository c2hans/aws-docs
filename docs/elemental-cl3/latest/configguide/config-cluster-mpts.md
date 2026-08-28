---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-cluster-mpts.html
---

# Dedicating interfaces to MPTS
<a name="config-cluster-mpts"></a>

This section applies only of your cluster includes AWS Elemental Statmux nodes.

You must perform an extra configuration step on every Elemental Statmux node and on any Elemental Live node that will be produce SPTS outputs for an Elemental Statmux MPTS:
+ On each Elemental Statmux node, you must identify two interfaces that will handle MPTS communications between this node and any Elemental Live node.
+ On each affected Elemental Live node, you must identify two interfaces that will handle MPTS communications between this node and any Elemental Statmux node.

**To identify dedicated interfaces**

1. On each Elemental Statmux node, identify two interfaces from the Ethernet interfaces [that you have created](config-conductor-live-ethernet-create.md).

   On each Elemental Live node, identify two interfaces from the Ethernet interfaces [that you have created](config-conductor-live-ethernet-create.md).

   We recommend that you dedicate two interfaces on every node, to provided network redundancy. These interfaces can be separate or they can be already bonded together.

1. On the primary Conductor Live web interface, choose the **Cluster** page, then choose **Nodes**.

1. On the **Nodes** page, select the hostname of an Elemental Statmux or Elemental Live node. Don't selected the node by its IP address. The node details page appears for this node.

1. Choose the **Network** tab. On the menu across the top, choose the **MPTS Configuration** tab. (Note that this tab is the only read-write tab on this page. The other **Network** tabs are read-only.)

1. Complete the **MPTS Configuration** page as follows:
   + In the **Interface 1** and **Interface 2** fields, select the IP addresses that you identified.

     If you identified only one interface, select the same value in both fields.

     If you identified a bonded interface, select the same value in both fields.
   + In the **Cluster Multicast Address** field, enter a multicast address. A multicast address ensures that communications will resume if either the Elemental Statmux or the Elemental Live node fails over.

1. Repeat steps 3 to 5 on every Elemental Statmux node and on every affected Elemental Live node.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
