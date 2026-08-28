---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-remove-failed.html
---

# Step G: Remove the failed worker node
<a name="upg-red-remove-failed"></a>

Remove the failed worker node from the redundancy group and then from the cluster. It can then be upgraded while the backup worker continues to encode.

**Topics**
+ [Step A: Remove failed worker from redundancy groups](#upg-std-remove-w-red)
+ [Step B: Remove failed worker from the cluster](#upg-std-remove-w-cluster)

## Step A: Remove failed worker from redundancy groups
<a name="upg-std-remove-w-red"></a>

Remove the active worker that you just failed over from the worker redundancy group.

**To remove the failed worker from a redundancy group**

1. On the web interface for the primary Conductor Live node, go to the **Cluster** page.

1.  On the **Cluster** page, choose **Redundancy**.

1. In the navigation bar, choose the Elemental Live redundancy group.

1. On the **Backup Nodes** tab, choose **Delete** (trash icon) for the failed worker.

## Step B: Remove failed worker from the cluster
<a name="upg-std-remove-w-cluster"></a>

Remove the failed worker from the cluster so that you can perform the upgrade process.

**To remove the failed worker from the cluster**

1. On the **Cluster** page, choose **Nodes**.

1.  On each the failed worker, choose the downward triangle and select **Remove Node**.

1. Move on to the upgrade process for this worker.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
