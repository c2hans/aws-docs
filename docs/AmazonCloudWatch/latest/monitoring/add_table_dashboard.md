---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/add_table_dashboard.html
---

# Adding a data table widget to a CloudWatch dashboard
<a name="add_table_dashboard"></a>

**To add a data table widget to a dashboard**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Dashboards** and then choose a dashboard.

1. Choose the **\+** button, select **Data table**, and choose **Next**.

1. In the **Browse** tab, search or browse for the metrics that you want to display in the table widget. Then select the metrics.

1. (Optional) To change the layout of the table, choose the **Options** tab and select **Invert rows and columns**.

   You can also use the **Options** tab to change what columns appear in the table and display the unit being used in the **Label** column.
**Tip**
To display more accurate thresholds, choose **Show as many digits as can fit before rounding**.

1. (Optional) To change your data table widget's time range, select one of the predefined time ranges in the upper area of the widget. The time ranges span from 1 hour to 1 week. To set your own time range, choose **Custom**.

1. (Optional) To change your data table widget's time range, select one of the predefined time ranges in the upper area of the widget. The time ranges span from 1 hour to 1 week. To set your own time range, choose **Custom**.

1. (Optional) To have this widget keep using the time range that you select, even if the time range for the rest of the dashboard is later changed, choose **Persist time range**.

1. Choose **Create widget** and then choose **Save dashboard**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
