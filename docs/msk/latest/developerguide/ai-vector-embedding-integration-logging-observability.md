---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/ai-vector-embedding-integration-logging-observability.html
---

# Logging and observability
<a name="ai-vector-embedding-integration-logging-observability"></a>

All logs and metrics for real-time vector embedding blueprints can be enabled using CloudWatch logs.

All metrics that are available for a regular MSF application and Amazon Bedrock can monitor your [application](https://docs.aws.amazon.com/managed-flink/latest/java/metrics-dimensions.html) and [Bedrock metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html#runtime-cloudwatch-metrics).

There are two additional metrics for monitoring performance of generating embeddings. These metrics are part of the EmbeddingGeneration operation name in CloudWatch.
+ **BedrockTitanEmbeddingTokenCount**: monitors the number of tokens present in a single request to Bedrock.
+ **BedrockEmbeddingGenerationLatencyMs**: reports the time taken to send and receive a response from Bedrock for generating embeddings in milliseconds.

For OpenSearch Service, you can use the following metrics:
+ **OpenSearch Serverless collection metrics**: see [Monitoring OpenSearch Serverless with Amazon CloudWatch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-cloudwatch.html) in the *Amazon OpenSearch Service Developer Guide*.
+ **OpenSearch provisioned metrics**: see [Monitoring OpenSearch cluster metrics with Amazon CloudWatch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-cloudwatchmetrics.html) in the *Amazon OpenSearch Service Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
