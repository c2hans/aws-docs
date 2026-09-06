---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/ingestion.html
---

# Ingestion
<a name="ingestion"></a>

 Ingestion module contains a web service that provides an endpoint to collect data through HTTP/HTTPS requests, which mainly is composed of Amazon Application Load Balancer and Amazon Elastic Container Service. It also supports sinking data into a stream service or S3 directly.

 You can create an ingestion module with the following settings:
+  [Ingestion endpoint settings](ingestion-endpoint.md): Create a web service as an ingestion endpoint to collect data sent from your SDKs.
+  Data sink settings: Configure how the guidance sinks the data for downstream consumption. Currently, the guidance supports three types of data sink:
  +  [Apache Kafka](data-sink-kafka.md)
  +  [Amazon S3](data-sink---s3.md)
  +  [Amazon Kinesis Data Stream (KDS)](data-sink-kinesis.md)

**Throttle**

Currently, there is no built-in throttling feature available with this guidance. If needed, you can configure AWS WAF to implement throttling feature. Please refer to [WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html) documentation.
