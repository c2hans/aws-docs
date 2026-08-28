---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-rem-sec.html
---

# Step M: Remove the secondary Conductor Live node
<a name="upg-red-rem-sec"></a>

If you have only one Conductor Live, skip this step and go to [Step O: Upgrade the primary Conductor node](upg-red-pri.md).

Prior to upgrading, you must remove the secondary Conductor Live node first from the redundancy group, and then from the cluster. You can't remove the node from the cluster if it's still in the redundancy group.

**To remove the secondary node from the redundancy group**

1. On the web interface for the primary Conductor Live node, access **Cluster** > **Redundancy** and ensure that you have the Conductor Live redundancy group selected.

1. Locate the secondary Conductor Live and click Delete (trash icon) to delete it from the redundancy group.

When the secondary Conductor Live node is removed from the redundancy group, remove it from the cluster.

**To remove the secondary node from the cluster**

1. On the web interface for the primary Conductor Live node, access **Cluster** > **Nodes**.

1. Locate the secondary Conductor Live node and display the options by choosing the down-facing arrow.

1. Select **Remove Node**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
