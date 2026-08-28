---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-share.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Sharing a change calendar
<a name="change-calendar-share"></a>

You can share a calendar in Change Calendar with other AWS accounts by using the AWS Systems Manager console. When you share a calendar, the calendar is read-only to users in the shared account. Maintenance windows, State Manager associations, and automations aren't shared.

**To share a change calendar**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Change Calendar**.

1. In the list of calendars, choose the name of the calendar that you want to share.

1. On the calendar's details page, choose the **Sharing** tab.

1. Choose **Actions, Share**.

1. In **Share calendar**, for **Account ID**, enter the ID number of a valid AWS account, and then choose **Share**.

   Users of the shared account can read the change calendar, but they can't make changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
