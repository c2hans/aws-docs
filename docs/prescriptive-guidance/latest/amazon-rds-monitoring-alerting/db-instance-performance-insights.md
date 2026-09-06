---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/db-instance-performance-insights.html
---

# Performance Insights metrics for DB instances
<a name="db-instance-performance-insights"></a>

Performance Insights monitors different types of metrics, as discussed in the following sections.

## Database load
<a name="database-load.2af2f8fd-ea13-539e-838e-93a58bcdc210"></a>

Database load (`DBLoad`) is a key metric in Performance Insights that measures the level of activity in your database. It is collected every second and automatically published to Amazon CloudWatch. It represents the activity of the DB instance in average active sessions (AAS), which are the number of sessions that are concurrently running SQL queries. The `DBLoad` metric is different from other time-series metrics, because it can be interpreted by using any of the five dimensions: waits, SQL, hosts, users, and databases. These dimensions are subcategories of the `DBLoad` metric. You can use them as *slice by* categories to represent different characteristics of the database load. For a detailed description of how we compute the database load, see [Database load](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.ActiveSessions.html) in the *Amazon RDS User Guide.*

The following screen illustration shows the Performance Insights tool.

![Database load in the Performance Insights tool](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/bf17749e-e7a9-4083-a37f-a3262d88d714.png)

## Dimensions
<a name="dimensions.5a2f9b5a-bdae-500b-bcf1-a9b440416800"></a>
+ *Wait events* are conditions that a database session waits for a resource or another operation to complete in order to continue its processing. If you run an SQL statement such as `SELECT * FROM big_table` and if this table is much bigger than the allocated InnoDB buffer pool, your session will most likely wait for `wait/io/file/innodb/innodb_data_file` wait events, which are caused by physical I/O operations on the data file. Wait events are an important dimension for database monitoring, because they indicate possible performance bottlenecks. Wait events indicate the resources and operations that the SQL statements you're running within sessions spend the most time waiting for. For example, the `wait/synch/mutex/innodb/trx_sys_mutex` event occurs when there is high database activity with a large number of transactions, and the `wait/synch/mutex/innodb/buf_pool_mutex` event occurs when a thread has acquired a lock on the InnoDB buffer pool to access a page in memory. For information about all MySQL and MariaDB wait events, see [Wait Event Summary Tables](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-wait-summary-tables.html) in the MySQL documentation. To understand how to interpret instrument names, see [Performance Schema Instrument Naming Conventions](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-instrument-naming.html) in the MySQL documentation.
+ *SQL* shows which SQL statements are contributing the most to the total database load. The *Top dimensions table*, which is located under the *Database load chart* in Amazon RDS Performance Insights, is interactive. You can obtain a detailed list of wait events associated with the SQL statement by clicking the bar in the *Load by waits (AAS)* When you select an SQL statement in the list, Performance Insights displays the associated wait events in the *Database load chart* and the SQL statement text in the *SQL text* section. SQL statistics are displayed on the right side of the* Top dimensions table*.
+ *Hosts* show the host names of the connected clients. This dimension helps you identify which client hosts are sending most of the load to the database.
+ *Users* group the DB load by users who are logged in to the database.
+ *Databases* group the DB load by the name of the database the client is connected to.

## Counter metrics
<a name="counter-metrics.302e6c5e-c77a-5a26-989d-386df5616e6d"></a>

Counter metrics are cumulative metrics whose values can only increase or reset to zero when the DB instance restarts. The value of a counter metric cannot be reduced to its previous value. These metrics represent a single, monotonically increasing counter.
+ [Native counters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.MySQL.Native) are metrics that are defined by the database engine and not by Amazon RDS. For example:
  + `SQL.Innodb_rows_inserted` represents the number of rows inserted into InnoDB tables.
  + `SQL.Select_scan` represents the number of joins that completed a full scan of the first table.
  + `Cache.Innodb_buffer_pool_reads` represents the number of logical reads that the InnoDB engine couldn't retrieve from the buffer pool and had to read directly from disk.
  + `Cache.Innodb_buffer_pool_read_requests` represents the number of logical read requests.

  For definitions of all native metrics, see [Server Status Variables](https://dev.mysql.com/doc/refman/8.0/en/server-status-variables.html) in the MySQL documentation.
+ [Non-native counters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html#USER_PerfInsights_Counters.MySQL.NonNative) are defined by Amazon RDS. You can obtain these metrics either by using a specific query or derive them by using two or more native metrics in calculations. Non-native counter metrics can represent latencies, ratios, or hit rates. For example:
  + `Cache.innoDB_buffer_pool_hits` represents the number of read operations that InnoDB could retrieve from the buffer pool without utilizing the disk. It is calculated from the native counter metrics as follows:

  ```
  db.Cache.Innodb_buffer_pool_read_requests - db.Cache.Innodb_buffer_pool_reads
  ```
+ `IO.innoDB_datafile_writes_to_disk` represents the number of InnoDB data file write operations to disk. It captures only operations on data files―not doublewrite or redo logging write operations. It is calculated as follows:

  ```
  db.IO.Innodb_data_writes - db.IO.Innodb_log_writes - db.IO.Innodb_dblwr_writes
  ```

You can visualize DB instance metrics directly in the Performance Insights dashboard. Choose ***Manage Metrics***, choose the ***Database metrics*** tab, and then select the metrics of interest, as shown in the following illustration.

![Selecting DB instance metrics in Performance Insights](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/f708c108-6b9d-4116-b412-b0a0f2cf10b2.png)

Choose the ***Update graph*** button to display the metrics you selected, as shown in the following illustration.

![Viewing DB instance metrics in Performance Insights](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/f1bcefb8-6b31-4a36-9c19-2880c721b13d.png)

## SQL statistics
<a name="sql-statistics.50920269-03ed-5098-b9cb-b203ab99ea1f"></a>

Performance Insights gathers performance-related metrics about SQL queries for each second that a query is running and for each SQL call. In general, Performance Insights collects [SQL statistics](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.html) at the statement and digest levels. However, for MariaDB and MySQL DB instances, statistics are collected only at the digest level.
+ Digest statistics is a composite metric of all queries that have the same pattern but eventually have different literal values. The digest replaces specific literal values with a variable; for example:

  ```
  SELECT department_id, department_name FROM departments WHERE location_id = ?
  ```
+ There are metrics that represent statistics *per second* for each digested SQL statement. For example, `sql_tokenized.stats.count_star_per_sec` represents calls per second (that is, how many times per second the SQL statement has been run).
+ Performance Insights also includes metrics that provide *per call* statistics for an SQL statement. For example, `sql_tokenized.stats.sum_timer_wait_per_call` shows the average latency of the SQL statement per call, in milliseconds.

SQL statistics are available in the Performance Insights dashboard, in the *Top SQL* tab of the *Top dimensions table*.

![SQL statistics](http://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-rds-monitoring-alerting/images/guide-img/9dd4cf9c-a2d9-4127-a3e3-2225b43b6c9a/images/2cd2fce0-17ea-4d85-ab86-1e4777a5aeef.png)
