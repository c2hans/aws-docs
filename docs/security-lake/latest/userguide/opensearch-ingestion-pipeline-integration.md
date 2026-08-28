---
source_url: https://docs.aws.amazon.com/security-lake/latest/userguide/opensearch-ingestion-pipeline-integration.html
---

# Integration with Amazon OpenSearch Service Ingestion pipeline
<a name="opensearch-ingestion-pipeline-integration"></a>

**Integration type:**Subscriber, Source

Amazon OpenSearch Service Ingestion is a fully managed, serverless data collector that streams logs, metrics, and trace data to OpenSearch Service and Security Lake.

**Send data to Security Lake using OpenSearch Ingestion pipeline**
You can use an Amazon Simple Storage Service (Amazon S3) sink plugin in OpenSearch Ingestion to send data from any supported source to Security Lake. Security Lake automatically centralizes security data from AWS environments, on-premises environments, and SaaS providers into a purpose-built data lake. For more information, see [Using an OpenSearch Ingestion pipeline with Amazon Security Lake as a sink](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-sink-security-lake.html).

**Send data from Security Lake to OpenSearch using OpenSearch Ingestion pipeline**
You can use an Amazon S3 source plugin to ingest data into your OpenSearch Ingestion pipeline. For more information, see [Using an OpenSearch Ingestion pipeline with Amazon Security Lake as a source](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configure-client-source-security-lake.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
