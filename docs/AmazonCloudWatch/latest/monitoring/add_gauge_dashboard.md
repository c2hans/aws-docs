---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_gauge_dashboard.html
---

# Adding a gauge widget to a CloudWatch dashboard
<a name="add_gauge_dashboard"></a>

**Note**
 Only the new interface in the CloudWatch console supports creation of the gauge widget. You must set a gauge range when you create this widget.

**To add a gauge widget to a dashboard**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Dashboards**, and then choose a dashboard.

1. From the dashboard screen, choose the **\+** symbol, and then select **Gauge**.

1.  Choose **Browse**, and then select the metric that you want to graph.

1.  Choose **Options**. Under ***Gauge range***, set values for **Min** and **Max**. For percentages, such as CPU utilization, we recommend that you set the values for `Min` to `0` and `Max` to `100`.

1.  (Optional) To change the color of the gauge widget, choose **Graphed metrics** and select the color box next to the metric label. A menu appears where you can choose a different color or enter a six-digit hex color code to specify a color.

1.  Choose **Create widget**, and choose **Save dashboard**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
