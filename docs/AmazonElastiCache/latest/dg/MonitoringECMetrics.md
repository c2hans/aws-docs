---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/MonitoringECMetrics.html
---

# Logging and monitoring in Amazon ElastiCache
<a name="MonitoringECMetrics"></a>

To manage your cache, it's important that you know how your caches are performing. ElastiCache generates metrics that are published to Amazon CloudWatch Logs for monitoring your cache performance. In addition, ElastiCache generates events when significant changes happen on your cache resources (e.g. a new cache is created, or a cache is deleted).

**Topics**
+ [Metrics and events for Valkey and Redis OSS serverless caches](serverless-metrics-events-redis.md)
+ [Metrics and events for node-based Valkey and Redis OSS clusters](self-designed-metrics-events.valkey-and-redis.md)
+ [Metrics and events for Memcached caches and clusters](serverless-metrics-events.memcached.md)
+ [Logging Amazon ElastiCache API calls with AWS CloudTrail](logging-using-cloudtrail.md)
+ [Amazon SNS monitoring of ElastiCache events](ECEvents.md)
+ [Log delivery](Log_Delivery.md)
+ [Monitoring use with CloudWatch Metrics](CacheMetrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
