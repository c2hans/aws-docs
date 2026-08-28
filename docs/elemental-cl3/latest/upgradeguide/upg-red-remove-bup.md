---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-remove-bup.html
---

# Step C: Remove the backup worker nodes
<a name="upg-red-remove-bup"></a>

Remove the backup worker nodes from the redundancy group before removing them from the cluster. You can then upgrade them while the active workers continue to encode.

**Topics**
+ [Step A: Remove backup workers from redundancy groups](#upg-std-remove-w-red)
+ [Step B: Remove backup workers from the cluster](#upg-std-remove-w-cluster)

## Step A: Remove backup workers from redundancy groups
<a name="upg-std-remove-w-red"></a>

Remove all backup workers from the worker redundancy groups.

**To remove workers from redundancy groups**

1. On the web interface for the primary Conductor Live node, go to the **Cluster** page.

1.  On the **Cluster** page, choose **Redundancy**.

1. In the navigation bar, choose the Elemental Live redundancy group.

1. On the **Backup Nodes** tab, choose **Delete** (trash icon) for each node.

1. If you have multiple Elemental Live redundancy groups, repeat this procedure on each group, then go to the next step.

## Step B: Remove backup workers from the cluster
<a name="upg-std-remove-w-cluster"></a>

Remove the backup workers from the cluster so that you can perform the upgrade process.

**To remove workers from the cluster**

1. On the **Cluster** page, choose **Nodes**.

1.  On each backup worker, choose the downward triangle and select **Remove Node**.

1. Remove all backup workers from the cluster, then move on to the upgrade process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
