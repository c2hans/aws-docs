---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/CloudWatch-using-the-query-editor.html
---

# Using the query editor
<a name="CloudWatch-using-the-query-editor"></a>

The CloudWatch data source in Amazon Managed Grafana provides a powerful query editor that allows you to retrieve and analyze metrics and logs from various AWS services that send data to CloudWatch. The query editor supports two distinct query modes: Metric Search and CloudWatch Logs.

The query editor mode for metrics uses the CloudWatch API to find metrics uploaded to CloudWatch. The mode for logs uses the CloudWatch Logs APIs to find log records. Each mode has its own specialized query editor. You select which API you want to query with by using the query mode switch at the top of the editor.

**Topics**
+ [Using the metric query editor](CloudWatch-using-the-metric-query-editor.md)
+ [Using the Amazon CloudWatch Logs query editor](CloudWatch-using-the-logs-query-editor.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
