---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/aws-service-logs.html
---

# AWS service logs
<a name="aws-service-logs"></a>

Centralized Logging with OpenSearch supports ingesting AWS service logs into Amazon OpenSearch Service through log analytics pipelines, which you can build using the **Centralized Logging with OpenSearch web console** or via a **standalone CloudFormation template**.

Centralized Logging with OpenSearch reads the data source, parse, cleanup/enrich, and ingest logs into Amazon OpenSearch Service domains for analysis. Moreover, the solution provides templated dashboards to facilitate log visualization.

Amazon OpenSearch Service is suitable for real-time log analytics and frequent queries and has full-text search capability.

As of release 2.1.0, the solution starts to support log ingestion into Light Engine, which is suitable for non-real-time log analytics and infrequent queries and has SQL-like search capability. You will see an option to choose the desired log analytics engine when creating the log analytics pipeline

**Important**
Supported AWS services must be in the same Region as Centralized Logging with OpenSearch. To ingest logs from different AWS Regions, we recommend using [S3 Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html#crr-scenario).
