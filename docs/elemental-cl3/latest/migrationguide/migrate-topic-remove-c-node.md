---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/migrationguide/migrate-topic-remove-c-node.html
---

# Removing a Conductor node from the cluster
<a name="migrate-topic-remove-c-node"></a>

You can remove a Conductor node that is not acting as the primary Conductor node — that isn't controlling the cluster. To remove a Conductor node, you first remove the node from the redundancy group, and then remove the node from the cluster.

1. Disable HA. On the web interface for the Conductor node, choose **Cluster** then choose **Redundancy**. Make sure that the Conductor Live redundancy group is selected. In the High Availability field, choose Disable. To verify that high availability is disabled, see the instructions in [Enabling or disabling high availability (HA)](migrate-topic-disable-ha.md).

1. Locate the Conductor to remove and click **Delete** (trash icon) to delete it from the redundancy group.

1. On the web interface for the primary Conductor node, choose **Cluster**, then choose **Nodes**.

1. Locate the Conductor node and display the options by choosing the down arrow. Select **Remove Node**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
