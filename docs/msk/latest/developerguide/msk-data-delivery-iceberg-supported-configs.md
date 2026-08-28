---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-supported-configs.html
---

# Supported configurations
<a name="msk-data-delivery-iceberg-supported-configs"></a>

| Configuration | Streaming tables for Apache Iceberg |
| --- | --- |
| Cluster / broker type | Amazon MSK Provisioned with Express brokers only |
| Input format | JSON or JSON\_SCHEMA\_GSR |
| Output format | Apache Iceberg tables; Parquet files with ZSTD or Snappy compression |
| Schema source | AWS Glue Schema Registry (required) |
| Schema evolution | Not supported |
| Partitioning | Time-based (TIME\_HOUR) |
| Data freshness | 5–15 minutes (default 10) |
| Storage class | Managed by S3 Tables |

**Note**
**Input formats:** `JSON` is plain JSON objects — you provide the Glue Schema Registry ARN that defines the schema. `JSON_SCHEMA_GSR` is GSR-serialized JSON, where the schema ID is embedded in each record.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
