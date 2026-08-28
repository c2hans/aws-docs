---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_VisualizationFieldQuery.html
---

# Tutorial: Run a query that produces a visualization grouped by log fields
<a name="CWL_AnalyzeLogData_VisualizationFieldQuery"></a>

When you run a query that uses the `stats` function to group the returned results by the values of one or more fields in the log entries, you can view the results as a bar chart, pie chart, line graph or stacked area graph. This helps you more efficiently visualize trends in your logs.

**To run a query for visualization**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, and then choose **Logs Insights**.

1. In the **Select log group(s)** drop down, choose one or more log groups to query.

    If this is a monitoring account in CloudWatch cross-account observability, you can select log groups in the source accounts as well as the monitoring account. A single query can query logs from different accounts at once.

   You can filter the log groups by log group name, account ID, or account label.

1. In the query editor, delete the current contents, enter the following `stats` function, and then choose **Run query**.

   ```
   stats count(*) by @logStream
       | limit 100
   ```

   The results show the number of log events in the log group for each log stream. The results are limited to only 100 rows.

1. Choose the **Visualization** tab.

1. Select the arrow next to **Line**, and then choose **Bar**.

   The bar chart appears, showing a bar for each log stream in the log group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
