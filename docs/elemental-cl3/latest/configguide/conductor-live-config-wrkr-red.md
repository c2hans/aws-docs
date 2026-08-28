---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-wrkr-red.html
---

# Creating worker redundancy groups
<a name="conductor-live-config-wrkr-red"></a>

To set up worker nodes for failover resiliency, you create one or more redundancy groups, then you add worker nodes to each group.

For general information about how failover resiliency works, and for detailed information about design redundancy groups that meet your requirements, see [*Conductor Live User Guide*](https://docs.aws.amazon.com/elemental-cl3/latest/ug).

**To create a redundancy group**

1. On the primary Conductor Live web interface, go to the **Cluster** page and choose **Redundancy**.

1. On the **Redundancy** page, choose **New Redundancy Group** and select the node type.

1. Enter a name for the redundancy group and choose **Add**.

The group is added to the list on the left side of the Redundancy screen. At this point, no nodes are in the group.

**To add nodes**

Follow these steps on the primary Conductor Live node.

1. On the **Redundancy** page, select the group that you're adding nodes to. Two tabs appear on the right — **Active Nodes** and **Backup Nodes**.

1. Select **Active Nodes** tab, then choose **Add Active Nodes**.

1. On the dialog, select a node from the **Nodes** dropdown list. Only nodes that aren't in a redundancy group appear in this list.

   If you are setting up an N\+M type of group, add several nodes.

1. Choose **Add** to add the selected nodes to the group.

1. Repeat these steps to add nodes to the **Backup Nodes** tab.

The nodes are listed on the **Active Nodes** or the **Backup Nodes** tab of the redundancy group.

Make sure that you add nodes to both tabs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
