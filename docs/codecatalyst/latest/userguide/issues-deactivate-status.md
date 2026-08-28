---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-deactivate-status.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# To deactivate a status
<a name="issues-deactivate-status"></a>

1. In the navigation pane, choose **Issues**.

1. Choose **Active issues** to open the **issues view switcher** dropdown menu and choose **Settings**.

1. In **Statuses**, choose a status you want to deactivate.

1. On the status you want to deactivate, choose the toggle on the status. The status is now grayed out.
**Note**
The deactivated status appears on the board until all issues are moved out of it. Issues cannot be added to a deactivated status.

1. To reactivate a deactivated status, choose the toggle on the status. The status is no longer grayed out.
**Note**
There must be at least one active status in each category. If there is only one status in the category, you cannot deactivate it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
