---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/msk-data-delivery-iceberg-attributes.html
---

# Table attributes
<a name="msk-data-delivery-iceberg-attributes"></a>

The Iceberg table a Channel creates has the following attributes (designed for governance and compliance):
+ **Managed table** — The table is read-only from your perspective. You cannot modify the schema or table properties, or write to the table directly outside of the Channel.
+ **No manual record deletion** — You cannot issue delete operations against individual records in the table. To remove old data, enable the record-expiration maintenance job, which automatically deletes records older than a specified retention period based on a timestamp column.
+ **Access control** — Table buckets and tables are always private. Use IAM policies to control access.
+ **S3 Tables quotas** — All S3 Tables service quotas apply to your service-managed tables. For more information, see [S3 Tables Regions and quotas](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-regions-quotas.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
