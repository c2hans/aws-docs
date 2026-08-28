---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-maintenance.html
---

# Table maintenance
<a name="msk-data-delivery-iceberg-maintenance"></a>

S3 Tables provides optional automated table maintenance jobs — compaction, snapshot expiration, and unreferenced file cleanup. Enabling these jobs is recommended: they optimize query performance by merging small data files, reduce storage costs by removing obsolete snapshots, and prevent metadata bloat over time as the Channel continuously writes to your table.

You can also enable a record expiration job to automatically delete records older than a specified retention period when your table is partitioned by a `timestamptz` column. This helps you manage storage costs and meet data-retention requirements without running manual delete operations against your Iceberg table.

For more details, see [S3 Tables maintenance overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance-overview.html) in the *Amazon S3 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
