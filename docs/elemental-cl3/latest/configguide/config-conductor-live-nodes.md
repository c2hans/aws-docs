---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/configguide/config-conductor-live-nodes.html
---

# Configuring the cluster
<a name="config-conductor-live-nodes"></a>

A AWS Elemental Conductor Live cluster consists of Conductor Live, Elemental Live, and Elemental Statmux nodes. To set up a cluster, you must add these nodes to the cluster. If you are implementing node redundancy, you must also create redundancy groups, then add each node to its redundancy group.

**Topics**
+ [Managing nodes in the Conductor Live cluster](conductor-live-config-nodes.md)
+ [Creating redundancy groups](conductor-live-config-redundancy.md)
+ [High availability (HA)](conductor-live-config-ha-about.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
