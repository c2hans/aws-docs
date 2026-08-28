---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/userguide/issues-grouping.html
---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Grouping issues
<a name="issues-grouping"></a>

Grouping is used to organize issues on the board by multiple parameters, such as assignee, labels, and priority.

**To group issues**

1. Navigate to your project.

1. In the navigation pane, choose **Issues**. The default view is the **Board**.

1. (Optional) Choose **Active issues** to open the **issues view switcher** dropdown menu to navigate to a different issues view.

1. Choose **Group**.

1. In **Group by**, choose a parameter to group by:
   + If you choose **Assignee** or **Priority**, choose the **Group order**.
   + If you choose **Label**, choose the labels and then choose **Group order**.

1. (Optional) Choose the **Show empty groups** toggle to show or hide groups that have no issues currently assigned to them.

1. The view updates as you make your choices. An issue only appears in the group that matches the configured parameters.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeCatalyst. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecatalyst` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
