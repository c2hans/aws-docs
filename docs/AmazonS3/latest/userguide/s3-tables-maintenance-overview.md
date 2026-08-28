---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-maintenance-overview.html
---

# S3 Tables maintenance
<a name="s3-tables-maintenance-overview"></a>

Amazon S3 automatically performs maintenance to enhance the performance of your tables in S3 table buckets. Maintenance is performed at the table bucket and individual table level and includes the following:

**Table bucket-level maintenance:**
+ **Unreferenced file removal** – Cleans up orphaned files to optimize storage usage and costs.

**Table-level maintenance:**
+ **File compaction** – Consolidates small files to improve query performance and reduce storage costs.
+ **Snapshot management** – Controls table version history and prevents excessive metadata growth.

These options are enabled by default. You can edit or disable these operations through maintenance configuration files.

In addition to these options, you can also enable and configure record expiration settings for tables. With this option, Amazon S3 automatically removes records from a table when the records expire.

**Topics**
+ [S3 Tables maintenance job status](s3-tables-maintenance-status.md)
+ [Maintenance for table buckets](s3-table-buckets-maintenance.md)
+ [Maintenance for tables](s3-tables-maintenance.md)
+ [Record expiration for tables](s3-tables-record-expiration.md)
+ [Considerations and limitations for maintenance jobs](s3-tables-considerations.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
