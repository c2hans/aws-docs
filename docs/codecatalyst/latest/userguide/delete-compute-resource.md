---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/delete-compute-resource.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Deleting a provisioned fleet
<a name="delete-compute-resource"></a>

Use the following instructions to delete a provisioned fleet.

**To delete a provisioned fleet**
**Warning**
Before deleting a provisioned fleet, remove it from all actions by deleting the `Fleet` property from the action's YAML code. Any action that continues to reference a provisioned fleet after it is deleted will fail the next time the action runs.

1. In the navigation pane, choose **CI/CD**, and then choose **Compute**.

1. In the **Provisioned fleet** list, choose the fleet you want to delete.

1. Choose **Delete**.

1. Enter **delete** to confirm the deletion.

1. Choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
