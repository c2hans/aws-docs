---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/deactivate-a-budget.html
---

# Deactivate a budget for a Deadline Cloud queue
<a name="deactivate-a-budget"></a>

You can deactivate any active budget. Deactivating a budget changes its status from **Active** to **Inactive**. When a budget is deactivated, it no longer tracks a resource to that budget's amount.

To deactivate a budget, use the following procedure.

1. If you haven't already, sign in to the AWS Management Console, open the Deadline Cloud [ console](https://us-west-2.console.aws.amazon.com/deadlinecloud/home), choose a farm, and then choose **Manage jobs**.

1. From the **Budget manager** page, in the **Active Budgets** tab, choose the button next to the budget that you want to deactivate.

1. From the **Actions** dropdown menu, select **Deactivate budget**. In a few moments, the selected budget will change from **Active** to **Inactive** and will move from the **Active Budgets** tab to the **Inactive Budgets** tab.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
