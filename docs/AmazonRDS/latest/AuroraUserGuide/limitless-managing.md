---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-managing.html
---

# Managing Aurora PostgreSQL Limitless Database
<a name="limitless-managing"></a>

The following topics describe how to manage your Aurora PostgreSQL Limitless Database DB clusters.

**Topics**
+ [Database and table size considerations](#limitless-db-size)
+ [Reclaiming storage space by vacuuming](limitless-vacuum.md)

## Database and table size considerations
<a name="limitless-db-size"></a>

For Aurora PostgreSQL Limitless Database, on each shard a sharded table is divided into a number of table slices that varies depending on how many shards are available in the DB shard group. Each table slice can grow up to 32 TiB, but each shard has a maximum capacity of 128 TiB. Reference tables have a size limit of 32 TiB for the entire DB shard group.

**Note**
The maximum capacity of each node (router or shard) is 128 TiB, as this is the maximum capacity for an Aurora PostgreSQL DB cluster.

The maximum number of relations per database (including tables, views, and indexes) in both Aurora PostgreSQL and Aurora PostgreSQL Limitless Database is 1,431,650,303.

For more information, see [Appendix K. PostgreSQL limits](https://www.postgresql.org/docs/current/limits.html) in the PostgreSQL documentation and [Amazon Aurora size limits](CHAP_Limits.md#RDS_Limits.FileSize.Aurora).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
