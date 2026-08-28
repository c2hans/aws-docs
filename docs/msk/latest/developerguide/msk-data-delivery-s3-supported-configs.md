---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-s3-supported-configs.html
---

# Supported configurations
<a name="msk-data-delivery-s3-supported-configs"></a>

| Configuration | Amazon S3 general purpose buckets |
| --- | --- |
| Cluster / broker type | Amazon MSK Provisioned with Express brokers only |
| Input format | JSON, ByteArray, String |
| Output format | Objects (compression: NONE, GZIP, or ZSTD) |
| Schema source | Not required |
| Schema evolution | Not applicable |
| Partitioning | Object key template |
| Data freshness | 5–15 minutes (default 10) |
| Storage class | STANDARD, INTELLIGENT\_TIERING, GLACIER\_IR |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
