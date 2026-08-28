---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-delete-association.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Deleting associations
<a name="systems-manager-state-manager-delete-association"></a>

Use the following procedure to delete an association by using the AWS Systems Manager console.

**To delete an association**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **State Manager**.

1. Select an association and then choose **Delete**.

You can delete multiple associations in a single operation by running an automation from the AWS Systems Manager console. When you select multiple associations for deletion, State Manager launches the automation runbook start page with the association IDs entered as input parameter values.

**To delete multiple associations in a single operation**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **State Manager**.

1. Select each association that you want to delete and then choose **Delete**.

1. (Optional) In the **Additional input parameters** area, select the Amazon Resource Name (ARN) for the *assume role* that you want the automation to use while running. To create a new assume role, choose **Create**.

1. Choose **Submit**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
