---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-oracle-partitioned-table-to-postgresql-by-using-aws-dms.html
---

# Migrate an Oracle partitioned table to PostgreSQL by using AWS DMS
<a name="migrate-an-oracle-partitioned-table-to-postgresql-by-using-aws-dms"></a>

*Saurav Mishra and Eduardo Valentim, Amazon Web Services*

## Summary
<a name="migrate-an-oracle-partitioned-table-to-postgresql-by-using-aws-dms-summary"></a>

This pattern describes how to speed up loading a partitioned table from Oracle to PostgreSQL by using AWS Database Migration Service (AWS DMS), which doesn't support native partitioning. The target PostgreSQL database can be installed on Amazon Elastic Compute Cloud (Amazon EC2), or it can be an Amazon Relational Database Service (Amazon RDS) for PostgreSQL or Amazon Aurora PostgreSQL-Compatible Edition DB instance.

Uploading a partitioned table includes the following steps:

1. Create a parent table similar to the Oracle partition table, but don't include any partition.

1. Create child tables that will inherit from the parent table that you created in step 1.

1. Create a procedure function and trigger to handle the inserts in the parent table.

However, because the trigger is fired for every insert, the initial load using AWS DMS can be very slow.

To speed up initial loads from Oracle to PostgreSQL 9.0, this pattern creates a separate AWS DMS task for each partition and loads the corresponding child tables. You then create a trigger during cutover.

PostgreSQL version 10 supports native partitioning. However, you might decide to use inherited partitioning in some cases. For more information, see the [Additional information](#migrate-an-oracle-partitioned-table-to-postgresql-by-using-aws-dms-additional) section.

## Prerequisites and limitations
<a name="migrate-an-oracle-partitioned-table-to-postgresql-by-using-aws-dms-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A source Oracle database with a partitioned table
+ A PostgreSQL database on AWS

**Product versions**
+ PostgreSQL 9.0

## Architecture
<a name="migrate-an-oracle-partitioned-table-to-postgresql-by-using-aws-dms-architecture"></a>

**Source technology stack**
+ A partitioned table in Oracle

**Target technology stack**
+ A partitioned table in PostgreSQL (on Amazon EC2, Amazon RDS for PostgreSQL, or Aurora PostgreSQL)

**Target architecture**

![Partitioned table data in Oracle moving to an AWS DMS task for each partition, then into PostgreSQL.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7fa2898e-3308-436a-aec8-ab6f680d7bac/images/1b9742ea-a13d-434c-83a7-56686cf76ea0.png)

## Tools
<a name="migrate-an-oracle-partitioned-table-to-postgresql-by-using-aws-dms-tools"></a>
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) helps you migrate data stores into the AWS Cloud or between combinations of cloud and on-premises setups.

## Epics
<a name="migrate-an-oracle-partitioned-table-to-postgresql-by-using-aws-dms-epics"></a>

### Set up AWS DMS
<a name="set-up-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the tables in PostgreSQL. | Create the parent and corresponding child tables in PostgreSQL with the required check conditions for partitions. | DBA |
| Create the AWS DMS task for each partition. | Include the filter condition of the partition in the AWS DMS task. Map the partitions to the corresponding PostgreSQL child tables. | DBA |
| Run the AWS DMS tasks using full load and change data capture (CDC). | Make sure that the `StopTaskCachedChangesApplied` parameter is set to `true` and the `StopTaskCachedChangesNotApplied` parameter is set to `false`. | DBA |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop the replication tasks. | Before you stop the tasks, confirm that the source and destination are in sync. | DBA |
| Create a trigger on the parent table. | Because the parent table will receive all insert and update commands, create a trigger that will route these commands to the respective child tables based on the partitioning condition. | DBA |

## Related resources
<a name="migrate-an-oracle-partitioned-table-to-postgresql-by-using-aws-dms-resources"></a>
+ [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
+ [Table Partitioning (PostgreSQL documentation)](https://www.postgresql.org/docs/10/ddl-partitioning.html)

## Additional information
<a name="migrate-an-oracle-partitioned-table-to-postgresql-by-using-aws-dms-additional"></a>

Although PostgreSQL version 10 supports native partitioning, you might decide to use inherited partitioning for the following use cases:
+ Partitioning enforces a rule that all partitions must have the same set of columns as the parent, but table inheritance supports children having extra columns.
+ Table inheritance supports multiple inheritances.
+ Declarative partitioning supports only list and range partitioning. With table inheritance, you can divide the data as you want. However, if the constraint exclusion can't prune partitions effectively, query performance will suffer.
+ Some operations need a stronger lock when using declarative partitioning than when using table inheritance. For example, adding or removing a partition to or from a partitioned table requires an `ACCESS EXCLUSIVE` lock on the parent table, whereas a `SHARE UPDATE EXCLUSIVE` lock is enough for regular inheritance.

When you use separate job partitions, you can also reload partitions if there are any AWS DMS validation issues. For better performance and replication control, run tasks on separate replication instances.
