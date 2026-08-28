---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-Insights.html
---

# Using anomaly detection in CloudWatch Logs Insights
<a name="LogsAnomalyDetection-Insights"></a>

In addition to creating log anomaly detectors for continuous monitoring, you can also use the `anomaly` command in CloudWatch Logs Insights queries to identify unusual patterns in your log data on-demand. This command extends the existing `pattern` functionality and uses machine learning to detect five types of anomalies including pattern frequency changes, new patterns, and token variations.

The `anomaly` command is particularly useful for:
+ Ad-hoc analysis of historical log data to identify unusual patterns
+ Investigating specific time periods for anomalous behavior
+ Monitoring applications like Lambda functions for execution issues

For more information about using the `anomaly` command in your queries, see [anomaly](CWL_QuerySyntax-Anomaly.md).

This query-based anomaly detection complements the continuous anomaly detectors described in the following sections, giving you both real-time monitoring and on-demand analysis capabilities.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
