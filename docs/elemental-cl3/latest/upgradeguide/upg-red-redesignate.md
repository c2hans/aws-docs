---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upg-red-redesignate.html
---

# Step K: Re-designate the backup worker node
<a name="upg-red-redesignate"></a>

Re-designate the backup worker as a backup so that it only runs active channels that have failed over from an active worker node.

**To designate a backup worker node**

1. On the web interface for the primary Conductor Live node, access **Cluster** > **Redundancy**.

1. Select the worker node redundancy group.

1. On the **Active Nodes** tab, locate the backup node that the channels failed over to and choose the **Move** button (circle).

   The node is moved back to the **Backup Nodes** tab.

1. When the backup node is moved back to the backup tab, choose a different active worker node and perform the steps [Step F: Fail over an active node](upg-red-fail.md) through this step for the same node. Repeat this entire process for each active worker node in the cluster until all have been processed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
