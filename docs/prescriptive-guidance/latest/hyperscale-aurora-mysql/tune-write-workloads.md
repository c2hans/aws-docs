---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hyperscale-aurora-mysql/tune-write-workloads.html
---

# Tuning write workloads
<a name="tune-write-workloads"></a>

Implementing load-balancing and freeing up the writer instance will help your write workload to perform better during high spikes. To achieve better write performance at high concurrency, follow these additional steps.

## Move referential integrity into the application layer
<a name="referential-integrity"></a>

Although referential integrity checks are important, with hyperscaling, they could be detrimental to your load. For each write, extra scans must be performed before the write itself is run, and this results in poor performance. If your application requires strict integrity checks, build them into the application layer to prevent them from throttling your writes.

## Avoid using heavy primary keys
<a name="primary-keys"></a>

Keep your primary keys light. The InnoDB storage engine appends the primary key to every other index that you create in your table. When your primary key is large, it affects the size of index. Storage and retrieval of data pages will slow down if the primary key is quite large. A common example is the usage of universally unique identifiers as primary keys. This is not a good approach if you target performance on an hyperscaled environment.

## Remove unused indexes
<a name="unused-indexes"></a>

[InnoDB](https://dev.mysql.com/doc/refman/8.0/en/innodb-storage-engine.html) optimizes its query plans based on the growth of your data, and it's a good idea to check for unused indexes in your Database and remove them. Unused indexes consume IO when the application writes data into a table. Check the list of unused indexes, and verify that they are not indexes that are used in rare situations, such as quarterly reports. Also, note that some indexes are used to enforce uniqueness or ordering and must also be considered.

## Use partition exchange for loading data into partitioned tables
<a name="partition-exchange"></a>

If you're writing large sets of data into partitioned tables, the combination of [LOAD DATA FROM S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.LoadFromS3.html) and [partition exchange](https://dev.mysql.com/doc/refman/5.7/en/partitioning-management-exchange.html) can improve performance, because the main table is not being accessed for the inserts. Partition exchange involves a data definition language (DDL), and it places a metadata lock on your table. Ensure that this is done when there are minimal or no queries running on the table so that the partition exchange DDL can obtain the metadata lock without waits. The exchange itself takes just milliseconds to complete.

## Ensure that old row versions are efficiently purged
<a name="old-row-versions"></a>

In the InnoDB implementation of multiversion concurrency control (MVCC), when a record is modified, the current (old) version of the data being modified is first recorded as an *undo record* in an undo log. A growing history list length (HLL) value indicates that the InnoDB garbage collection threads (purge threads) are not keeping up with the write workload, or that purging is blocked by a long-running query or transaction. When garbage collection is blocked or delayed, the database can develop a substantial purge lag that can negatively affect query performance. You can use the following recommendations for optimizing the purge process.
+ Keep transactions small.
+ For read queries, use the READ COMMITTED isolation level.
+ Increase the number of purge threads ([innodb\_purge\_threads](https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_purge_threads) and [innodb\_purge\_batch\_size](https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_purge_batch_size)). Note that tuning these parameters requires a reboot.
+ Monitor the HLL on a regular basis, and resolve any workload issues that prevent garbage collection from progressing.

## Ensure logging doesn't cause additional contention
<a name="logging"></a>

The general query log records client connections and disconnections as well asin addition to all statements received by the server in the order they were received. When activated, logging is synchronous, which can lead to a substantial performance penalty on a busy system. Unless required, we recommend deactivating the general log.

The slow query log records statements that took longer than the [long\_query\_time](https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_long_query_time) number of seconds to run, with the default setting of 10 seconds. When the setting is set to 0, all statements are synchronously logged, which can lead to a performance penalty on busy databases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
