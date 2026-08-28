---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/conductor-live-config-redundancy.html
---

# Creating redundancy groups
<a name="conductor-live-config-redundancy"></a>

You must create redundancy groups as follows:
+ If your cluster includes a primary and a secondary AWS Elemental Conductor Live node, you must create a redundancy group and add both nodes to the group. It isn't enough to just add the Conductor Live nodes to the cluster.
+ If you want to set up worker nodes for failover resiliency, you must create one or more redundancy groups, then you add worker nodes to each group.

For general information about how failover resiliency works, and for detailed information about designing redundancy groups that meet your requirements, see [*AWS Elemental Conductor Live User Guide*](https://docs.aws.amazon.com/elemental-cl3/latest/ug). Then come back to this section to create the groups and add the nodes.

**Topics**
+ [Creating a Conductor Live redundancy group](conductor-live-config-redundancy-cl.md)
+ [Creating worker redundancy groups](conductor-live-config-wrkr-red.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
