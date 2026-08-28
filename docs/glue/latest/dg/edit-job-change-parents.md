---
source_url: https://docs.aws.amazon.com/glue/latest/dg/edit-job-change-parents.html
---

# Changing the parent nodes for a node in the job diagram
<a name="edit-job-change-parents"></a>

You can change a node's parents to move nodes within the job diagram or to change a data source for a node.

**To change the parent node**

1. Choose the node in the job diagram that you want to modify.

1. In the node details panel, on the **Node properties** tab, under the heading **Node parents** remove the current parent for the node.

1. Choose a new parent node from the list.

1. Modify the other properties of the node as needed to match the newly selected parent node.

If you modified a node by mistake, you can use the **Undo** button on the toolbar to reverse the action.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
