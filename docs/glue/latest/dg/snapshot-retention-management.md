---
source_url: https://docs.aws.amazon.com/glue/latest/dg/snapshot-retention-management.html
---

# Snapshot retention optimization
<a name="snapshot-retention-management"></a>

Apache Iceberg snapshot retention feature allows users to query historical data at specific points in time and revert unwanted modifications to their tables. In the AWS Glue Data Catalog, snapshot retention configuration controls how long these snapshots (versions of the table data) are kept before being expired and removed. This helps manage storage costs and metadata overhead by automatically removing older snapshots based on a configured retention period or maximum number of snapshots to keep.

You can configure the retention period in days and the maximum number of snapshots to retain for a table. AWS Glue removes snapshots that are older than the specified retention period from the table metadata, while keeping the most recent snapshots up to the configured limit. After removing old snapshots from the metadata, AWS Glue deletes the corresponding data and metadata files that are no longer referenced and unique to the expired snapshots. This allows time travel queries only up to the remaining retained snapshots, while reclaiming storage space used by expired snapshot data.

**Topics**
+ [Enabling snapshot retention optimizer](enable-snapshot-retention.md)
+ [Updating snapshot retention optimizer](update-snapshot-retention.md)
+ [Disabling snapshot retention optimizer](disable-snapshot-retention.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
