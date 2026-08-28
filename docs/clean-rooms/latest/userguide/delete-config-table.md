---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/userguide/delete-config-table.html
---

# Deleting a configured table
<a name="delete-config-table"></a>

You can delete a configured table that you own. This action cannot be undone and affects all related resources.

**Warning**
All collaborations to which the configured table is associated will be impacted. When you delete a configured table, all of its associations stop being queryable in the respective collaborations. All analyses that refer to this table fail.
Deleting a configured table does not delete your configured table associations or data stored in dependent intermediate tables in collaborations. For more information about cleaning up intermediate tables, see [Deleting an intermediate table](delete-intermediate-table.md).

**To delete a configured table**

1. Open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Configured tables**.

1. Choose the configured table that you want to delete.

1. Choose **Delete**.

1. In the confirmation dialog, review the warning that all collaborations to which the table is associated will be impacted.

1. To confirm the deletion, enter **confirm** in the text field, and then choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
