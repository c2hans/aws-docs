---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Insights-Query-History.html
---

# View running queries or query history
<a name="CloudWatchLogs-Insights-Query-History"></a>

You can view the queries currently in progress as well as your recent query history.

Queries currently running includes queries you have added to a dashboard. You are limited to 100 concurrent CloudWatch Logs Insights queries per account, including queries added to dashboards. Additionally, You can run 15 concurrent queries for either OpenSearch Service PPL or OpenSearch Service SQL.

**To view your recent query history**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Logs**, and then choose **Logs Insights**.

1. Choose **History**, if you are using the new design for the CloudWatch Logs console. If you are using the old design, choose **Actions**, **View query history for this account**.

   A list of your recent queries appears. You can run any of them again by selecting the query and choosing **Run**.

   Under **Status**, CloudWatch Logs displays **In progress** for any queries that are currently running.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
