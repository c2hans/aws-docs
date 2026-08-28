---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/live_data_dashboard.html
---

# Using live data for a CloudWatch dashboard
<a name="live_data_dashboard"></a>

**To choose whether to use live data on your entire dashboard**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Dashboards**, and then choose a dashboard.

1. To permanently turn live data on or off for all widgets on the dashboard, do the following:

   1. Choose **Actions**, **Settings**, **Bulk update live data.**

   1. Choose **Live Data on** or **Live Data off**, and choose **Set**.

1. To temporarily override the live data settings of each widget, choose **Actions**. Then, under **Overrides**, next to **Live data**, do one of the following:
   + Choose **On** to temporarily turn on live data for all widgets.
   + Choose **Off** to temporarily turn off live data for all widgets.
   + Choose **Do not override** to preserve each widget's live data setting.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
