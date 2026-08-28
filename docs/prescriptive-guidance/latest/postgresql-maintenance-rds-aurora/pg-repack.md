---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/pg-repack.html
---

# Removing bloat with pg\_repack
<a name="pg-repack"></a>

You can use the `pg_repack` extension to remove table and index bloat with minimal database locking. You can create this extension in the database instance and run the `pg_repack` client (where the client version matches the extension version) from Amazon Elastic Compute Cloud (Amazon EC2) or from a computer that can connect to your database.

Unlike `VACUUM FULL`, `pg_repack` doesn't require downtime or a maintenance window, and won't block other sessions.

`pg_repack` is helpful in situations where `VACUUM FULL`, `CLUSTER`, or `REINDEX` might not work. It creates a new table that contains the data of the bloated table, tracks the changes from the original table, and then replaces the original table with the new one. It doesn't lock the original table for read or write operations while it's building the new table.

You can use `pg_repack` for a full table or for an index. To see a list of tasks, see the [pg\_repack documentation](https://reorg.github.io/pg_repack/).

Limitations:
+ To run `pg_repack`, your table must have a primary key or a unique index.
+ `pg_repack `won't work with temporary tables.
+ `pg_repack` won't work on tables that have global indexes.
+ When `pg_repack` is in progress, you can't perform DDL operations on tables.

The following table describes the differences between `pg_repack` and `VACUUM FULL`.

|  |  |
| --- |--- |
| `VACUUM FULL` | `pg_repack` |
| Built-in  command | An extension that you run from Amazon EC2 or your local computer |
| Requires an `ACCESS EXCLUSIVE` lock while it's working on a table | Requires an `ACCESS EXCLUSIVE` lock only for a short time |
| Works with all tables | Works on tables that have primary and unique keys only |
| Requires double the storage that's consumed by the table and indexes | Requires double the storage that's consumed by the table and indexes |

To run `pg_repack` on a table, use the command:

```
pg_repack -h <host> -d <dbname> --table <tablename> -k
```

To run `pg_repack` on an index, use the command:

```
pg_repack -h <host> -d <dbname> --index <index name>
```

For more information, see the AWS blog post [Remove bloat from Amazon Aurora and RDS for PostgreSQL with pg\_repack](https://aws.amazon.com/blogs/database/remove-bloat-from-amazon-aurora-and-rds-for-postgresql-with-pg_repack/).

## Caveat:
<a name="caveat-.5ae1139f-77c6-59e5-97b3-0c8dde555970"></a>

The `error-on-invalid-index` error in `pg_repack` usually means that one or more indexes on the table are corrupt or invalid. `pg_repack` cannot safely operate on tables that have invalid indexes because it relies on the indexes for data consistency during the repack process.

This error occurs when:
+ The index is marked as invalid (for example, because of a failed `CREATE INDEX CONCURRENTLY` statement).
+ The index is corrupted (possibly due to hardware issues or abrupt shutdowns).

Use the following query to identify invalid indexes and to drop them first if you find them.

```
SELECT indexrelid::regclass, indisvalid FROM pg_index WHERE indrelid = 'orders'::regclass AND NOT indisvalid; Drop the invalid index: DROP INDEX index_name;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
