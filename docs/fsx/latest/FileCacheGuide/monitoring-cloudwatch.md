---
source_url: https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/monitoring-cloudwatch.html
---

# Monitoring with CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor caches using Amazon CloudWatch, which collects and processes raw data from Amazon File Cache into readable, near real-time metrics. These statistics are retained for a period of 15 months so that you can access historical information and gain a better perspective on how your web application or service is performing. By default, Amazon File Cache metric data is automatically sent to CloudWatch at 1-minute periods. For more information about CloudWatch, see [What Is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) in the *Amazon CloudWatch User Guide*.

CloudWatch metrics are reported as raw *Bytes*. Bytes are not rounded to either a decimal or binary multiple of the unit.

CloudWatch metrics for an Amazon File Cache resource are organized into three categories:
+ [Front-end I/O metrics](frontend-io-metrics.md)
+ [Backend I/O metrics](backend-io-metrics.md)
+ [Cache utilization metrics](utilization-metrics.md)

All CloudWatch metrics for Amazon File Cache are published to the `AWS/FSx` namespace in CloudWatch. For each metric, Amazon File Cache emits a data point per disk per minute. To view aggregate cache details, you can use the `Sum` statistic. Note that the file servers behind your caches are spread across multiple disks.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
