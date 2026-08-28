---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/monitoring-cloudwatch.html
---

# Monitoring MemoryDB with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor MemoryDB using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

The following sections list the metrics and dimensions for MemoryDB.

**Topics**
+ [Host-Level Metrics](metrics.HostLevel.md)
+ [Metrics for MemoryDB](metrics.memorydb.md)
+ [Which Metrics Should I Monitor?](metrics.whichshouldimonitor.md)
+ [Choosing Metric Statistics and Periods](metrics.ChoosingStatisticsAndPeriods.md)
+ [Monitoring CloudWatch metrics](cloudwatchmetrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
