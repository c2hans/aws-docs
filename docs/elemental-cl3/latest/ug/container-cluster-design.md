---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/container-cluster-design.html
---

# Setup: Designing the cluster
<a name="container-cluster-design"></a>

You must design the cluster to suit the number of workflows you plan to create. You could be creating the following types of workflows:
+ Encoding workflows. These workflows require only Elemental Live.
+ MPTS workflows. These workflows require both Elemental Live and Elemental Statmux.

**Topics**
+ [Number of Conductor Live nodes](cl3-node-design.md)
+ [Number of primary Elemental Live nodes](el-node-design.md)
+ [Number of primary Elemental Statmux nodes](smx-node-design.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
