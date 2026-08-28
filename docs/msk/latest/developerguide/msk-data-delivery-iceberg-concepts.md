---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-concepts.html
---

# Key concepts
<a name="msk-data-delivery-iceberg-concepts"></a>

This section describes the key concepts behind Amazon MSK Data Delivery.
+ **Data freshness vs. throughput** — A Channel needs at least 2.4 MBps of uncompressed throughput for the minimum 5-minute freshness. For lower-throughput topics, increase freshness (up to 15 minutes) so the service can accumulate enough data for efficient delivery and inline compaction.
+ **Input formats** — `JSON` (plain JSON; you provide a GSR schema ARN) and `JSON_SCHEMA_GSR` (GSR-serialized JSON with the schema ID embedded in each record) are supported. The AWS Glue Schema Registry (GSR) is the source of truth, and the Channel fails to create if the schema cannot be resolved.
+ **Schema evolution** — Not supported. Changing the schema after creation can cause delivery failures.
+ **Partitioning** — S3 Tables delivery supports time-based partitioning only.
+ **No backfill** — only records produced after enablement are delivered.
+ **New table for each channel** — each Channel creates its own Iceberg table.
+ **Dead-letter queue** — both destinations require a DLQ S3 bucket. The Channel writes the identifiers (sequence numbers) of unprocessable records, along with error context — not the full record payloads.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
