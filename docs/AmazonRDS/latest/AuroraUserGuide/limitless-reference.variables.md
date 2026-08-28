---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reference.variables.html
---

# Variables in Aurora PostgreSQL Limitless Database
<a name="limitless-reference.variables"></a>

You can use the following variables to configure Aurora PostgreSQL Limitless Database.

**rds\_aurora.limitless\_active\_shard\_key**
Sets a single shard key while querying the database, causing all `SELECT` and DML queries to be appended with the shard key as a constant predicate. For more information, see [Setting an active shard key](limitless-query.single-shard.md#limitless-query.single-shard.active).

**rds\_aurora.limitless\_create\_table\_collocate\_with**
Set this variable to a specific table name to collocate newly created tables with that table. For more information, see [Creating limitless tables by using variables](limitless-creating-config.md).

**rds\_aurora.limitless\_create\_table\_mode**
Sets the table creation mode. For more information, see [Creating limitless tables by using variables](limitless-creating-config.md).

**rds\_aurora.limitless\_create\_table\_shard\_key**
Set this variable to an array of column names to use as shard keys. For more information, see [Creating limitless tables by using variables](limitless-creating-config.md).

**rds\_aurora.limitless\_explain\_options**
What to include in the `EXPLAIN` output. For more information, see [EXPLAIN](limitless-reference.DML-limitations.md#limitless-reference.DML-limitations.EXPLAIN).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
