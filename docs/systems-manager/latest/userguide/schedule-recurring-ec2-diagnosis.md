---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/schedule-recurring-ec2-diagnosis.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Scheduling a recurring scan for unmanaged EC2 instances
<a name="schedule-recurring-ec2-diagnosis"></a>

You can run an on-demand scan for Amazon EC2 instances in your account or organization that Systems Manager can't manage due to configuration issues. You can also schedule this scan to occur automatically on a regular schedule.

**To schedule a recurring scan for unmanaged EC2 instances**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Diagnose and remediate**.

1. Choose the **Unmanaged EC2 instances issue** tab.

1. In the **Diagnose unmanaged EC2 instances** section, turn on **Schedule recurring diagnosis**.

1. For **Diagnostic frequency**, select whether to run the diagnosis once a day or once a week.

1. (Optional) For **Start time**, enter a time, in 24-hour format, for the diagnosis to begin. For example, for 8:15 PM, enter **20:15**.

   The time you enter is for your current local time zone.

   If you don't specify a time, the diagnostic scan runs immediately. Systems Manager also schedules the scan to run in the future at the current time. If you specify a time, Systems Manager waits to run the diagnostic scan at the specified time.

1. Choose **Execute**. The diagnosis runs immediately, but will also run on the schedule you have specified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
