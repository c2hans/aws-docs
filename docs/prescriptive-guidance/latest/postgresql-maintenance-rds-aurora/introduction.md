---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/introduction.html
---

# Maintenance for PostgreSQL databases in Amazon RDS and Amazon Aurora to avoid performance issues
<a name="introduction"></a>

*anuradha chintha and Rajesh Madiwale, Amazon Web Services*

Amazon Aurora PostgreSQL-Compatible Edition and Amazon Relational Database Service (Amazon RDS) for PostgreSQL are fully managed relational database services for PostgreSQL databases. These managed services free the database administrator from many maintenance and management tasks. However, some maintenance tasks, such as `VACUUM`, require close monitoring and configuration based on your database usage. This guide describes PostgreSQL maintenance activities in Amazon RDS and Aurora.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

Database performance is a key measure that underlies the success of a business. Performing maintenance activities on your Aurora PostgreSQL-Compatible and Amazon RDS for PostgreSQL databases provide these benefits:
+ Helps achieve optimal query performance
+ Frees up bloated space for reuse by future transactions
+ Prevents transaction wraparound
+ Helps the optimizer generate good plans
+ Ensures proper index usage

## Multiversion concurrency control (MVCC)
<a name="mvcc"></a>

PostgreSQL database maintenance requires an understanding of *multiversion concurrency control (MVCC)*, which is a mechanism of PostgreSQL. When multiple transactions are processed concurrently in the database, MVCC ensures that atomicity and isolation, which are two characteristics of atomicity, consistency, isolation, durability (ACID) transactions, are maintained. In MVCC, every write operation generates a new version of data and stores the previous version. Readers and writers don't block one another. When a transaction reads data, the system chooses one of the versions to provide transaction isolation. PostgreSQL and some relational databases use an adaption of MVCC called *snapshot isolation (SI)*. For example, Oracle implements SI by using rollback segments. During a write operation, Oracle writes the old version of data to a rollback segment and overwrites the data area with the new version. PostgreSQL databases implement SI by using *visibility check rules* to evaluate versions. When new data is placed into a table page, PostgreSQL uses these rules to select the appropriate version of the data for a read operation.

When you modify data in a table row, PostgreSQL uses MVCC to maintain multiple versions of the row. During `UPDATE` and `DELETE` operations on the table, the database keeps the old versions of the rows for other running transactions that might need a consistent view of the data. These old versions are called *dead rows* (*tuples*). A collection of dead tuples produces bloat. A large amount of bloat in the database can cause a number of problems, including poor query plan generation, slow query performance, and increased disk space usage to store the older versions.

Removing bloat and keeping a database healthy requires periodic maintenance, which includes these activities, which are discussed in the following sections:
+ [Vacuuming and analyzing tables automatically](autovacuum.md)
+ [Vacuuming and analyzing tables manually](manual-vacuum.md)
+ [Removing bloat with pg\_repack](pg-repack.md)
+ [Rebuilding indexes](reindex.md)
