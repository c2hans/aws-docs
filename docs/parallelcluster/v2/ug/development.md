---
source_url: https://docs.aws.amazon.com/parallelcluster/v2/ug/development.html
---

# Development
<a name="development"></a>

You can use the following sections to get started with the development of AWS ParallelCluster.

**Important**
The following sections include instructions for using a custom version of the cookbook recipes and a custom AWS ParallelCluster node package. This information covers an advanced method of customizing AWS ParallelCluster, with potential issues that can be hard to debug. The AWS ParallelCluster team highly recommends using the scripts in [Custom Bootstrap Actions](pre_post_install.md) for customization, because post-install hooks are generally easier to debug and more portable across releases of AWS ParallelCluster.

**Topics**
+ [Setting up a custom AWS ParallelCluster cookbook](custom_cookbook.md)
+ [Setting up a custom AWS ParallelCluster node package](custom_node_package.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
