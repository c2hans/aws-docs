---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/upgradeguide/upgrades-cl3-upg.html
---

# Cluster Upgrades in Conductor Live
<a name="upgrades-cl3-upg"></a>

There are two types of upgrade that you can perform on an AWS Elemental Conductor Live cluster:
+ **Standard upgrade**: Use this for any type of cluster and redundancy configuration. Do this type of upgrade in a maintenance window since all nodes are offline for the duration of the upgrade process.
+ **Reduced downtime upgrade**: Use this for clusters that have worker redundancy. This type of upgrade leverages worker node redundancy. Therefore the downtime is typically less than 30 seconds.

This document describes both upgrade processes.

**Topics**
+ [Standard Conductor Live upgrade](upgrades-cl3-upg-std.md)
+ [Reduced downtime Conductor Live upgrade](upgrades-cl3-upg-red.md)
+ [Sample Upgrade](sample-upg-cl3-upg.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
