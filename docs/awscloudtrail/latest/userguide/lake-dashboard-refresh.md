---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-refresh.html
---

# Set a refresh schedule for a custom dashboard with the CloudTrail console
<a name="lake-dashboard-refresh"></a>

This section describes how to set a dashboard refresh schedule. You can set a refresh schedule to allow CloudTrail Lake to refresh a dashboard every 1 hour, 6 hours, 12 hours, or 24 hours (1 day).

When you set a refresh schedule using the CloudTrail console, CloudTrail attaches a resource-based policy to the dashboard that allows CloudTrail to refresh the dashboard on your behalf.

**To set a refresh schedule**

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1.  In the left navigation pane, under **Lake**, choose **Dashboard**.

1. Choose the **Managed and custom dashboards** tab.

1. In **Custom dashboards**, choose the dashboard that you want to set a refresh schedule for.

1. Choose the refresh frequency from the dropdown list.

1. To create a refresh schedule, CloudTrail attaches a resource-based policy to the dashboard to allow CloudTrail to refresh the dashboard on your behalf. Expand **Dashboard resource policy** to view the resource-based policy that CloudTrail will attach to the dashboard.

1. Because running queries incurs costs, CloudTrail asks you to confirm that you want CloudTrail to run queries for the scheduled frequency. Choose **Confirm** to set a refresh schedule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
