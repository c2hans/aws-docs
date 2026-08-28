---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-monitoring.html
---

# Monitoring
<a name="msk-data-delivery-s3-monitoring"></a>

A Channel publishes data-delivery metrics to Amazon CloudWatch under the `AWS/Kafka` namespace. Metrics for delivery to Amazon S3 general purpose buckets use the `DeliveryToS3.*` prefix.

**Topics**
+ [Amazon CloudWatch metrics](msk-data-delivery-s3-metrics.md)
+ [Metric dimensions](msk-data-delivery-s3-metric-dimensions.md)
+ [Recommended alarms](msk-data-delivery-s3-alarms.md)
+ [Metrics in the console](msk-data-delivery-s3-viewing-metrics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
