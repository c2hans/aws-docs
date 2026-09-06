---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/manual-vacuum.html
---

# Vacuuming and analyzing tables manually
<a name="manual-vacuum"></a>

If your database is vacuumed by the autovacuum process, it's best practice to avoid running manual vacuums on the entire database too frequently. A manual vacuum might result in unnecessary I/O loads or CPU spikes, and might also fail to remove any dead tuples. Run manual vacuums on a table-by-table basis only if it's really necessary, such as when the ratio of live to dead tuples is low, or when there are long gaps between autovacuums. In addition, you should run manual vacuums when there's minimal user activity.

Autovacuum also keeps a table's statistics up to date. When you run the `ANALYZE` command manually, it rebuilds these statistics instead of updating them. Rebuilding statistics when they are already updated by the regular autovacuum process might cause system resource utilization.

We recommend that you run the [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html) and [ANALYZE](https://www.postgresql.org/docs/current/sql-analyze.html) commands manually in the following scenarios:
+ During low peak hours on busier tables, when autovacuuming might not be sufficient.
+ Immediately after you bulk load data into the target table. In this case, running `ANALYZE` manually completely rebuilds statistics, which is a better option than waiting for autovacuum to begin.
+ To vacuum temporary tables (autovacuum can't access these).

To reduce the I/O impact when you run the `VACUUM` and `ANALYZE` commands on concurrent database activity, you can use the `vacuum_cost_delay` parameter. In many situations, maintenance commands such as `VACUUM` and `ANALYZE` don't have to finish quickly. However, these commands shouldn't interfere with the system's ability to perform other database operations. To prevent this, you can enable cost-based vacuum delays by using the `vacuum_cost_delay` parameter.

This parameter is disabled by default for manually issued `VACUUM` commands. To enable it, set it to a nonzero value.

## Running vacuum and cleanup operations in parallel
<a name="running-vacuum-and-cleanup-operations-in-parallel.66b8235b-c697-5780-b3ee-f9d080982df3"></a>

The `VACUUM` command [PARALLEL](https://www.postgresql.org/docs/current/sql-vacuum.html) option uses parallel workers for the index vacuum and index cleanup phases and is disabled by default. The number of parallel workers (the degree of parallelism) is determined by the number of indexes in the table and can be specified by the user. If you're running parallel `VACUUM` operations without an integer argument, the degree of parallelism is calculated based on the number of indexes in the table.

The following parameters help you configure parallel vacuuming in Amazon RDS for PostgreSQL and Aurora PostgreSQL-Compatible:
+ [max\_worker\_processes](https://www.postgresql.org/docs/current/runtime-config-resource.html) – Sets the maximum number of concurrent worker processes.
+ [min\_parallel\_index\_scan\_size](https://www.postgresql.org/docs/current/runtime-config-query.html) – Sets the minimum amount of index data that must be scanned in order for a parallel scan to be considered.
+ [max\_parallel\_maintenance\_workers](https://www.postgresql.org/docs/current/runtime-config-resource.html) – Sets the maximum number of parallel workers that can be started by a single utility command.

**Note**
The `PARALLEL` option is used only for vacuuming purposes. It doesn't affect the `ANALYZE` command. The following example illustrates database behavior when you use manual `VACUUM` and `ANALYZE` on a database.

Here's a sample table where autovacuum has been disabled (for illustration purposes only; disabling autovacuum isn't recommended):

```
create table t1 ( a int, b int, c int );
alter table t1 set (autovacuum_enabled=false);
```

```
apgl=> \d+ t1
Table "public.t1"
Column | Type | Collation | Nullable | Default | Storage | Stats target | Description
--------+---------+-----------+----------+---------+---------+--------------+-------------
a | integer | | | | plain | |
b | integer | | | | plain | |
c | integer | | | | plain | |
Access method: heap
Options: autovacuum_enabled=false
```

Add 1 million rows to table t1:

```
apgl=> select count(*) from t1;
count
1000000
(1 row)
```

Statistics of table t1:

```
select * from pg_stat_all_tables where relname='t1';
-[ RECORD 1 ]-------+--------
relid         | 914744
schemaname    | public
relname       | t1
seq_scan      | 0
seq_tup_read  | 0
idx_scan      |
idx_tup_fetch |
n_tup_ins     | 1000000
n_tup_upd     | 0
n_tup_del     | 0
n_tup_hot_upd | 0
n_live_tup    | 1000000
n_dead_tup    | 0
n_mod_since_analyze | 1000000
last_vacuum      |
last_autovacuum  |
last_analyze     |
last_autoanalyze |
vacuum_count     | 0
autovacuum_count | 0
analyze_count    | 0
autoanalyze_count | 0
```

Add an index:

```
create index i2 on t1 (b,a);
```

Run the `EXPLAIN` command (Plan 1):

```
Bitmap Heap Scan on t1 (cost=10521.17..14072.67 rows=5000 width=4)
Recheck Cond: (a = 5)
→ Bitmap Index Scan on i2 (cost=0.00..10519.92 rows=5000 width=0)
Index Cond: (a = 5)
(4 rows)
```

Run the `EXPLAIN ANALYZE` command  (Plan 2):

```
explain (analyze,buffers,costs off) select a from t1 where b = 5;
QUERY PLAN
Bitmap Heap Scan on t1 (actual time=0.023..0.024 rows=1 loops=1)
Recheck Cond: (b = 5)
Heap Blocks: exact=1
Buffers: shared hit=4
→ Bitmap Index Scan on i2 (actual time=0.016..0.016 rows=1 loops=1)
Index Cond: (b = 5)
Buffers: shared hit=3
Planning Time: 0.054 ms
Execution Time: 0.076 ms
(9 rows)
```

The `EXPLAIN `and `EXPLAIN ANALYZE `commands display different plans, because autovacuum was disabled on the table and the `ANALYZE` command wasn't performed manually. Now let's update a value in the table and regenerate the `EXPLAIN ANALYZE` plan:

```
update t1 set a=8 where b=5;
explain (analyze,buffers,costs off) select a from t1 where b = 5;
```

The `EXPLAIN ANALYZE` command (Plan 3) now displays:

```
apgl=> explain (analyze,buffers,costs off) select a from t1 where b = 5;
QUERY PLAN
Bitmap Heap Scan on t1 (actual time=0.075..0.076 rows=1 loops=1)
Recheck Cond: (b = 5)
Heap Blocks: exact=1
Buffers: shared hit=5
→ Bitmap Index Scan on i2 (actual time=0.017..0.017 rows=2 loops=1)
Index Cond: (b = 5)
Buffers: shared hit=3
Planning Time: 0.053 ms
Execution Time: 0.125 ms
```

If you compare the costs between Plan 2 and Plan 3 you will see the differences in planning and execution time, because we haven't collected statistics yet.

Now let's run a manual `ANALYZE` on the table, and then check the statistics and regenerate the plan:

```
apgl=> analyze t1
apgl→ ;
ANALYZE
Time: 212.223 ms

apgl=> select * from pg_stat_all_tables where relname='t1';
-[ RECORD 1 ]-------+------------------------------
relid          | 914744
schemaname     | public
relname        | t1
seq_scan       | 3
seq_tup_read   | 1000000
idx_scan       | 3
idx_tup_fetch  | 3
n_tup_ins      | 1000000
n_tup_upd      | 1
n_tup_del      | 0
n_tup_hot_upd  | 0
n_live_tup     | 1000000
n_dead_tup     | 1
n_mod_since_analyze | 0
last_vacuum       |
last_autovacuum   |
last_analyze      | 2023-04-15 11:39:02.075089+00
last_autoanalyze  |
vacuum_count      | 0
autovacuum_count  | 0
analyze_count     | 1
autoanalyze_count | 0

Time: 148.347 ms
```

Run the `EXPLAIN ANALYZE` command (Plan 4):

```
apgl=> explain (analyze,buffers,costs off) select a from t1 where b = 5;
QUERY PLAN
Index Only Scan using i2 on t1 (actual time=0.022..0.023 rows=1 loops=1)
Index Cond: (b = 5)
Heap Fetches: 1
Buffers: shared hit=4
Planning Time: 0.056 ms
Execution Time: 0.068 ms
(6 rows)

Time: 138.462 ms
```

If you compare all plan results after you manually analyze the table and collect statistics, you'll notice that the optimizer Plan 4 is better than the others and also decreases query execution time. This example shows how important it is to run maintenance activities on the database.

### Rewriting an entire table with VACUUM FULL
<a name="manual-vacuum-full"></a>

Running the `VACUUM `command with the `FULL` parameter rewrites the entire contents of a table into a new disk file with no extra space, and returns unused space to the operating system. This operation is much slower and requires an `ACCESS EXCLUSIVE` lock on each table. It also requires extra disk space, because it writes a new copy of the table and doesn't release the old copy until the operation is complete.

`VACUUM FULL` can be useful in the following cases:** **
+ When you want to reclaim a significant amount of space from the tables.
+ When you want to reclaim bloat space in non-primary key tables.

We recommend that you use `VACUUM FULL` when you have non-primary key tables, if your database can tolerate downtime.

Because `VACUUM FULL` requires more locking than other operations, it is more expensive to run on crucial databases. To replace this method, you can use the `pg_repack `extension, which is described in the [next section](pg-repack.md). This option is similar to `VACUUM FULL` but requires minimal locking and is supported by both Amazon RDS for PostgreSQL and Aurora PostgreSQL-Compatible.
