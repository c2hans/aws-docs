---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-monitoring.html
---

# Monitoring Channel
<a name="msk-data-delivery-monitoring"></a>

A Channel publishes data-delivery metrics to Amazon CloudWatch under the `AWS/Kafka` namespace. The metric set depends on the destination type: `DeliveryToIceberg.*` for S3 Tables and `DeliveryToS3.*` for S3 buckets.

**Topics**
+ [Amazon CloudWatch metrics — S3 Tables (Iceberg) destination](msk-data-delivery-metrics-iceberg.md)
+ [Amazon CloudWatch metrics — S3 bucket destination](msk-data-delivery-metrics-s3.md)
+ [Metric dimensions](msk-data-delivery-metric-dimensions.md)
+ [Recommended alarms](msk-data-delivery-alarms.md)
+ [Viewing metrics in the console](msk-data-delivery-viewing-metrics.md)
