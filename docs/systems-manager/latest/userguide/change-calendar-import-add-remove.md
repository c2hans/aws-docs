---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-import-add-remove.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Updating all events from a third-party calendar provider
<a name="change-calendar-import-add-remove"></a>

If several events are added to or removed from your source calendar after you have imported its iCalendar `.ics` file, you can reflect those changes in Change Calendar. First, re-export the source calendar, and then import the new file into Change Calendar, which is a tool in AWS Systems Manager. Events in your change calendar will be updated to reflect the contents of the newer file.

**To update all events from a third-party calendar provider**

1. In your third-party calendar, add or remove events as you want them to be reflected in Change Calendar, and then re-export the calendar to a new `.ics` file.

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Change Calendar**.

1. From the list of calendars, choose the calendar name from the list.

1. On the **Actions** menu, choose **Edit**.

1. In the **Import calendar** section, choose **Choose file**.

1. Navigate to and select the replacement `.ics` file.

1. Choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
