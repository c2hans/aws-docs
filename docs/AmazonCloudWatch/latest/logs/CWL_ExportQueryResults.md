---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_ExportQueryResults.html
---

# Add query to dashboard or export query results
<a name="CWL_ExportQueryResults"></a>

After you run a query, you can add the query to a CloudWatch dashboard or copy the results to the clipboard.

Queries added to dashboards run every time you load the dashboard and every time that the dashboard refreshes. These queries count toward your limit of 100 concurrent CloudWatch Logs Insights queries.

**To add query results to a dashboard**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, and then choose **Logs Insights**.

1. Choose one or more log groups and run a query.

1. Choose **Add to dashboard**.

1. Select the dashboard, or choose **Create new** to create a dashboard for the query results.

1. Select the widget type to use for the query results.

1. Enter a name for the widget.

1. Choose **Add to dashboard**.

**To copy query results to the clipboard or download the query results**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, and then choose **Logs Insights**.

1. Choose one or more log groups and run a query.

1. Choose **Export results**, and then choose the option you want.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
