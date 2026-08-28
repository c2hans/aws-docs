---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-dashboard-custom-widgets.html
---

# Add a sample widget with the CloudTrail console
<a name="lake-dashboard-custom-widgets"></a>

This section describes how to add a sample widget to your dashboard. You can add a maximum of 10 widgets to a custom dashboard.

**Note**
Sample widgets are limited to a single event data store that exists in your account. To query across multiple event data stores in your account, [create a new widget](lake-dashboard-custom-widgets-new.md).

**To add a sample widget to a dashboard**

1. Sign in to the AWS Management Console and open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/).

1.  In the left navigation pane, under **Lake**, choose **Dashboard**.

1. Choose the **Managed and custom dashboards** tab.

1. In **Custom dashboards**, choose the dashboard that you want to add a widget to.

1. From **Actions**, choose **Edit dashboard**.

1. From **Actions**, choose **Add sample widget**.

1. Choose the event data store you'd like to run the query on. You can only choose event data stores that exist in your account.

1. Choose the sample widget you'd like to add. By default, all sample widgets are shown. You can filter by a widget type (for example, IAM widgets).

1. Choose **View query** to view the query for the selected widget.

1. Choose **Add to dashboard** to add the widget to the dashboard.

1. Choose **Save** to save the dashboard.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
