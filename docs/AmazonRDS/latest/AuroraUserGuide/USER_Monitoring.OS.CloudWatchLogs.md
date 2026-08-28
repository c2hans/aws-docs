---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring.OS.CloudWatchLogs.html
---

# Viewing OS metrics using CloudWatch Logs
<a name="USER_Monitoring.OS.CloudWatchLogs"></a>

After you have enabled Enhanced Monitoring for your DB cluster, you can view the metrics for it using CloudWatch Logs, with each log stream representing a single DB instance or DB cluster being monitored. The log stream identifier is the resource identifier (`DbiResourceId`) for the DB instance or DB cluster.

**To view Enhanced Monitoring log data**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. If necessary, choose the AWS Region that your DB cluster is in. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/index.html?rande.html) in the *Amazon Web Services General Reference*.

1. Choose **Logs** in the navigation pane.

1. Choose **RDSOSMetrics** from the list of log groups.

1. Choose the log stream that you want to view from the list of log streams.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
