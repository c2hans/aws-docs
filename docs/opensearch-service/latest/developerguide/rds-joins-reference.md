---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/rds-joins-reference.html
---

# Joining data from multiple tables
<a name="rds-joins-reference"></a>

You can configure denormalized joins to automatically merge data from multiple related tables into single OpenSearch documents. This feature supports one-to-one and one-to-many relationships between parent and child tables. The pipeline reads change data capture (CDC) events from all configured tables and merges them into a parent document.

The joins configuration is the same for both Amazon RDS and Aurora sources. For configuration details and examples, see [Joining data from multiple tables to ingest into one document](aurora-denormalized-joins.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
