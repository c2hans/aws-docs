---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/what-is.html
---

# About the Conductor Live solution
<a name="what-is"></a>

AWS Elemental Conductor Live lets you create and manage channels on AWS Elemental Live and/or MPTSes on AWS Elemental Statmux.

Each of the three products — AWS Elemental Conductor Live, AWS Elemental Live and AWS Elemental Statmux — runs on its own node. Conductor Live is a *management node*. Elemental Live and Elemental Statmux node are each *worker nodes*. And all the nodes are organized in a *cluster.*

A cluster contains at least one Conductor Live node and one Elemental Live node. If you want to produce MPTSes, a cluster contains at least one Conductor Live node, one Elemental Live node, and one Elemental Statmux node.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
