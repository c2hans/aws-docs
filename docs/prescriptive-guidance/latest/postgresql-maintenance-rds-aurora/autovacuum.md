---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/autovacuum.html
---

# Vacuuming and analyzing tables automatically
<a name="autovacuum"></a>

Autovacuum is a daemon (that is, it runs in the background) that automatically *vacuums* (cleans up) dead tuples, reclaims storage, and gathers statistics. It checks for bloated tables in the database and clears the bloat to reuse the space. It monitors database tables and indexes and adds them to a vacuum job after they reach a specific threshold of update or delete operations.

Autovacuum manages vacuuming by automating the PostgreSQL `VACUUM` and `ANALYZE` commands. `VACUUM` removes bloat from tables and reclaims the space, whereas `ANALYZE` updates the statistics that enable the optimizer to produce efficient plans. `VACUUM` also performs a major task called *vacuum freezing* to prevent transaction ID wraparound issues in the database. Every row that is updated in the database receives a transaction ID from the PostgreSQL transaction control mechanism. These IDs control the row's visibility to other concurrent transactions. The transaction ID is a 32-bit number. Two billion IDs are always kept in the visible past. The remaining (about 2.2 billion) IDs are preserved for transactions that will take place in the future and are hidden from the current transaction. PostgreSQL requires an occasional cleaning and *freezing* of old rows in order to prevent transactions from wrapping around and making old, existing rows invisible when new transactions are created. For more information, see [Preventing Transaction ID Wraparound Failures](https://www.postgresql.org/docs/current/routine-vacuuming.html#VACUUM-FOR-WRAPAROUND) in the PostgreSQL documentation.

|
|
| Parameter | Description | Default for Amazon RDS | Default for Aurora |
| --- |--- |--- |--- |
| `autovacuum_vacuum_threshold` | The minimum number of tuple update or delete operations that must occur on a table before autovacuum vacuums it. | 50 operations | 50 operations |
| `autovacuum_analyze_threshold` | The minimum number of tuple inserts, updates, or deletes that must occur on a table before autovacuum analyzes it. | 50 operations | 50 operations |
| `autovacuum_vacuum_scale_factor` | The percentage of tuples that must be modified in a table before autovacuum vacuums it. | 0.1 | 0.1 |
| `autovacuum_analyze_scale_factor` | The percentage of tuples that must be modified in a table before autovacuum analyzes it. | 0.05 | 0.05 |
| `autovacuum_freeze_max_age` | The maximum age of frozen IDs before a table is vacuumed to prevent transaction ID wraparound issues. | 200,000,000 transactions | 200,000,000 transactions |

Autovacuum makes a list of tables to process based on specific threshold formulas, as follows.
+ Threshold for running `VACUUM` on a table:

  ```
  vacuum threshold = autovacuum_vacuum_threshold + (autovacuum_vacuum_scale_factor * Total row count of table)
  ```
+ Threshold for running `ANALYZE` on a table:

  ```
  analyze threshold = autovacuum_analyze_threshold + (autovacuum_analyze_scale_factor * Total row count of table)
  ```

For small to medium-sized tables, the default values might be sufficient. However, a large table that has frequent data modifications will have a higher number of dead tuples. In this case, autovacuum might process the table frequently for maintenance, and the maintenance of other tables might get delayed or ignored until the large table finishes. To avoid this, you can tune the following autovacuum parameters.

## Autovacuum memory-related parameters
<a name="autovacuum-parameters"></a>

### autovacuum\_max\_workers
<a name="autovacuum-max-workers.ac0535f1-d1f8-5c9f-98bf-04a82d9d4a52"></a>

Specifies the maximum number of autovacuum processes (other than the autovacuum launcher) that can run at the same time. This parameter can be set only when you start the server. If the autovacuum process is busy with a large table, this parameter helps run the cleanup for other tables.

### maintenance\_work\_mem
<a name="maintenance-work-mem.e4d4826b-ff86-561c-a3ab-3a283c7d9aec"></a>

Specifies the maximum amount of memory to be used by maintenance operations such as `VACUUM`, `CREATE INDEX`, and `ALTER`. In Amazon RDS and Aurora, memory is allocated based on the instance class by using the formula `GREATEST({DBInstanceClassMemory/63963136*1024},65536)`. When autovacuum runs, up to `autovacuum_max_workers` times that calculated value can be allocated, so be careful not to set the value too high. To control this, you can set `autovacuum_work_mem` separately.

### autovacuum\_work\_mem
<a name="autovacuum-work-mem.626df705-022b-5efc-8ca4-6b28204ecc0f"></a>

Specifies the maximum amount of memory to be used by each autovacuum worker process. This parameter defaults to -1, which indicates that you should use the value of `maintenance_work_mem` instead.

For more information about autovacuum memory parameters, see [Allocating memory for autovacuum](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.html#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.WorkMemory) in the Amazon RDS documentation.

## Tuning autovacuum parameters
<a name="autovacuum-tuning"></a>

Users might need to tune autovacuum parameters depending on the their update and delete operations. The settings for the following parameters can be set at the table, instance, or cluster level.

### Cluster or instance level
<a name="cluster-or-instance-level.f0a8d2eb-db8c-5919-873e-d03550052df1"></a>

As an example, let's look at a banking database where continuous data manipulation language (DML) operations are expected. To maintain the database's health, you should tune autovacuum parameters at the cluster level for Aurora and at the instance level for Amazon RDS, and apply the same parameter group to the reader as well. In the case of a failover, the same parameters should apply to the new writer.

### Table level
<a name="table-level.1d0aa731-04f2-51b4-a025-918141c13365"></a>

For example, in a database for food delivery where continuous DML operations are expected on a single table called `orders`, you should consider tuning the `autovacuum_analyze_threshold` parameter at the table level by using the following command:

```
ALTER TABLE <table_name> SET (autovacuum_analyze_threshold = <threshold rows>)
```

### Using aggressive autovacuum settings at the table level
<a name="using-aggressive-autovacuum-settings-at-the-table-level.8a8b0bee-c588-50c6-90c0-aaedb00bab4a"></a>

The example orders table that has continuous update and delete operations becomes a candidate for vacuuming  because of default autovacuum settings.This leads to bad plan generation and slow queries. Clearing the bloat and updating statistics requires table-level aggressive autovaccum settings.

To determine settings, keep track of the duration of queries running on this table and identify the percentage of DML operations that result in plan changes. The `pg_stat_user_tables` view helps you track insert, update, and delete operations.

**Example:**

Let's assume that the optimizer generates bad plans whenever 5 percent of the `orders` table changes. In this case, you should change the scale factor threshold to 2 percent as follows:

```
ALTER TABLE orders SET (autovacuum_vacuum_scale_factor = 0.02)
```

**Tip**
Select aggressive autovacuum settings carefully to avoid high consumption of resources.

For more information, see the following:
+ [Understanding autovacuum in Amazon RDS for PostgreSQL environments](https://aws.amazon.com/blogs/database/understanding-autovacuum-in-amazon-rds-for-postgresql-environments/) (AWS blog post)
+ [Automatic vacuuming parameters](https://www.postgresql.org/docs/17/runtime-config-autovacuum.html) (PostgreSQL documentation)

To make sure that autovacuum works effectively, monitor dead rows, disk usage, and the last time autovacuum or `ANALYZE` ran on a regular basis. The `pg_stat_all_tables` view provides information on each table (`relname`) and how many dead tuples (`n_dead_tup`) are in the table.

Monitoring the number of dead tuples in each table, especially in frequently updated tables, helps you determine if the autovacuum processes are periodically removing the dead tuples so their disk space can be reused for better performance. You can use the following query to check the number of dead tuples and when the last autovacuum ran on the tables:

```
SELECT
relname AS TableName,n_live_tup AS LiveTuples,n_dead_tup AS DeadTuples,
last_autovacuum AS Autovacuum,last_autoanalyze AS Autoanalyze FROM
pg_stat_user_tables;
```

## Advantages and limitations
<a name="advantages-limitations"></a>

Autovacuum provides the following advantages:
+ It removes bloat from tables automatically.
+ It prevents transaction ID wraparound.
+ It keeps database statistics up to date.

Limitations:
+ If queries use parallel processing, the number of worker processes might not be enough for autovacuum.
+ If autovacuum runs during peak hours, resource utilization might increase. You should tune parameters to handle this issue.
+ If table pages are occupied in another session, autovacuum might skip those pages.
+ Autovacuum can't access temporary tables.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
