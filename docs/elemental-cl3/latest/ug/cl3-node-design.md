---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/cl3-node-design.html
---

# Number of Conductor Live nodes
<a name="cl3-node-design"></a>

You need two Conductor Live nodes if you plan to implement Conductor Live node redundancy. Otherwise, you need only one node.

We recommend that you implement resiliency in Conductor Live nodes. For more information, see [Conductor Live node redundancy](redundancy-cl3.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
