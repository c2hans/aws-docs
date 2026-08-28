---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access-disable.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Disabling just-in-time access with Systems Manager
<a name="systems-manager-just-in-time-node-access-disable"></a>

The following procedure describes how to disable just-in-time node access. After disabling just-in-time node access, users in your organization might be unable to connect to your nodes unless you've already implemented other connection methods.

**To disable just-in-time node access**

1. Log in to the Systems Manager delegated administrator account for your organization.

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. Select **Settings** in the navigation pane.

1. In the **Just-in-time node access** tab, select **Disable**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
