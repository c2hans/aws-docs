---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/metrics-classic.html
---

# CloudWatch Metrics (Classic)
<a name="metrics-classic"></a>

CloudWatch Metrics (Classic) uses the `PutMetricData` API and embedded metric format (EMF) for ingestion, and provides CloudWatch Metrics Insights (SQL-based queries) for analysis. Classic metrics support up to 30 dimensions per metric with per-metric-per-month pricing.

Use Classic metrics when you have existing integrations with the CloudWatch API, need compatibility with AWS service metrics that are not yet available in OpenTelemetry format, or prefer SQL-based querying with CloudWatch Metrics Insights.

**Topics**
+ [Metrics concepts](cloudwatch_concepts.md)
+ [Basic monitoring and detailed monitoring in CloudWatch](cloudwatch-metrics-basic-detailed.md)
+ [Publish custom metrics (PutMetricData / EMF)](publishingMetrics.md)
+ [Query your CloudWatch metrics with CloudWatch Metrics Insights](query_with_cloudwatch-metrics-insights.md)
+ [View available metrics](viewing_metrics_with_cloudwatch.md)
+ [Retrieve metric data (GetMetricData)](metrics-classic-getdata.md)
+ [Get statistics for a metric (GetMetricStatistics)](getting-metric-statistics.md)
+ [Use metrics explorer to monitor resources by their tags and properties](CloudWatch-Metrics-Explorer.md)
+ [Use search expressions in graphs](using-search-expressions.md)
+ [Use metric streams](CloudWatch-Metric-Streams.md)
+ [Graphing metrics](graph_metrics.md)
+ [Math expressions with metrics](using-metric-math.md)
+ [Using CloudWatch anomaly detection](CloudWatch_Anomaly_Detection.md)
+ [Grafana integration](CloudWatch-Grafana-support.md)
+ [AWS services that publish CloudWatch metrics](aws-services-cloudwatch-metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
