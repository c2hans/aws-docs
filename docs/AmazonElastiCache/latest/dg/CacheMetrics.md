---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheMetrics.html
---

# Monitoring use with CloudWatch Metrics
<a name="CacheMetrics"></a>

ElastiCache provides metrics that enable you to monitor your clusters. You can access these metrics through CloudWatch. For more information on CloudWatch, see the [CloudWatch documentation.](https://aws.amazon.com/documentation/cloudwatch/)

ElastiCache provides both host-level metrics (for example, CPU usage) and metrics that are specific to the cache engine software (for example, cache gets and cache misses). These metrics are measured and published for each Cache node in 60-second intervals.

**Important**
You should consider setting CloudWatch alarms on certain key metrics, so that you will be notified if your cluster's performance starts to degrade. For more information, see [Which Metrics Should I Monitor?](CacheMetrics.WhichShouldIMonitor.md) in this guide.

**Topics**
+ [Host-Level Metrics](CacheMetrics.HostLevel.md)
+ [Metrics for Valkey and Redis OSS](CacheMetrics.Redis.md)
+ [Metrics for Memcached](CacheMetrics.Memcached.md)
+ [Which Metrics Should I Monitor?](CacheMetrics.WhichShouldIMonitor.md)
+ [Choosing Metric Statistics and Periods](CacheMetrics.ChoosingStatisticsAndPeriods.md)
+ [Monitoring CloudWatch Cluster and Node Metrics](CloudWatchMetrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
