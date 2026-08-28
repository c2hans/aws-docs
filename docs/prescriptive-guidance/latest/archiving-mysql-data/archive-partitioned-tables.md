---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/archiving-mysql-data/archive-partitioned-tables.html
---

# Archiving data in partitioned tables
<a name="archive-partitioned-tables"></a>

MySQL supports [partitioning](https://dev.mysql.com/doc/refman/8.0/en/partitioning.html) for the InnoDB storage engine, and you can use this feature to partition large tables. Partitions within the table are stored as separate physical tables, although the SQL that operates on the partitioned table reads the whole table. This gives you the freedom to remove unneeded partitions from the table without performing row-by-row deletes, so you can archive historical rows in your database.

Consider the following example code. `TABLE orders` exists within the `orderprocessing` schema. Its historical data is present in the partition `phistorica`l, which contains data belonging to 2021 and earlier. In the same table, application-level hot data is present in the live partitions for each month of 2022. To archive the data in the partition `phistorical`, you can create an archive `table orders_2021_and_older` with the same structure in the `archive` schema. You can then use the MySQL [EXCHANGE PARTITION](https://dev.mysql.com/doc/refman/8.0/en/partitioning-management-exchange.html) to move the partition `phistorical` into that table. Note that the archive table is not partitioned. After archiving, you can verify your data and move it to Amazon S3.

```
CREATE TABLE orders (
      orderid bigint NOT NULL AUTO_INCREMENT,
      customerid bigint DEFAULT NULL,
      ............
      ............
      order_date date NOT NULL,
      PRIMARY KEY (`orderid`,`order_date`))
    PARTITION BY RANGE (TO_DAYS(order_date)) (
          PARTITION pstart   VALUES LESS THAN (0),
          PARTITION phistorical VALUES LESS THAN (TO_DAYS('2022-01-01')),
          PARTITION p2022JAN VALUES LESS THAN (TO_DAYS('2022-02-01')),
          PARTITION p2022FEB VALUES LESS THAN (TO_DAYS('2022-03-01')),
          PARTITION p2022MAR VALUES LESS THAN (TO_DAYS('2022-04-01')),
          PARTITION p2022APR VALUES LESS THAN (TO_DAYS('2022-05-01')),
          PARTITION p2022MAY VALUES LESS THAN (TO_DAYS('2022-06-01')),
          PARTITION p2022JUN VALUES LESS THAN (TO_DAYS('2022-07-01')),
          PARTITION p2022JUL VALUES LESS THAN (TO_DAYS('2022-08-01')),
          PARTITION p2022AUG VALUES LESS THAN (TO_DAYS('2022-09-01')),
          PARTITION p2022SEP VALUES LESS THAN (TO_DAYS('2022-10-01')),
          PARTITION p2022OCT VALUES LESS THAN (TO_DAYS('2022-11-01')),
          PARTITION p2022NOV VALUES LESS THAN (TO_DAYS('2022-12-01')),
          PARTITION p2022DEC VALUES LESS THAN (TO_DAYS('2023-01-01')),
          PARTITION pfuture       VALUES LESS THAN MAXVALUE
      );
CREATE TABLE orders_2021_and_older (
        orderid bigint NOT NULL AUTO_INCREMENT,
        customerid bigint DEFAULT NULL,
        ............
        ............
        order_date date NOT NULL,
        PRIMARY KEY (`orderid`,`order_date`));
mysql> alter table orderprocessing.orders exchange partition phistorical with table archive.orders_2021_and_older;
  Query OK, 0 rows affected (0.33 sec)
```

When you use the `EXCHANGE PARTITION` feature to archive historical data, we recommend the following best practices:
+ Create a separate schema for storing archive data in your application. This schema will contain archive tables that will house archived data. An archive table in your archive schema should have the same structure as your live table, including its indexes and primary key. However, the target archive table cannot be a partitioned table. Exchanging partitions between two partitioned tables is not permitted in MySQL.
+ Follow a naming convention for your archive table that helps you to identify the historical data stored in it. This is useful when you perform auditing tasks or design jobs that move this data out to Amazon S3.
+ Perform the `EXCHANGE PARTITION` data definition language (DDL) statement in a downtime window when there is no traffic coming into your Aurora MySQL-Compatible writer, Amazon RDS for MySQL, or Amazon RDS for MariaDB instances.

  It might be possible to run `EXCHANGE PARTITION` during low-traffic windows in your application or microservice. However, there should be no writes and no or very few selects on the partitioned table. Existing long-running select queries can cause your `EXCHANGE PARTITION` DDL to wait, causing resource contentions on your database. Design scripts that verify all these conditions are met before you run `EXCHANGE PARTITION` on your system.

If your application design can support partitioned data and you currently have an unpartitioned table, consider moving your data into partitioned tables to support archiving your data. For more information, see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/alter-table-partition-operations.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
