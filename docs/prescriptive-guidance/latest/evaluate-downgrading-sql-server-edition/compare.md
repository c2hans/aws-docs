---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/compare.html
---

# Compare SQL Server Enterprise and Standard edition features
<a name="compare"></a>

The following table is a short version of the list of SQL Server Enterprise edition features and possible alternatives in the Standard edition. For additional information, see a more extensive feature comparison (attached) .

|
|
| Functional area | Feature | Enterprise edition | Standard edition | Notes |
| --- |--- |--- |--- |--- |
| **Scale limits** | Maximum number of processors or cores per instance | OS maximum | 4 sockets or 24 cores | See [DB instance class support for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.InstanceClasses) on Amazon RDS for SQL. |
| Maximum memory used per instance | OS maximum | 128 GB (SQL Server 2016 and later) |
| Maximum memory-optimized data size per database | Unlimited memory (SQL Server 2014 and later) | 32 GB (SQL Server 2016 and later) |  |
| **High availability** | Always On availability groups | Yes | Basic availability groups (SQL Server 2016 and later) | The Multi-AZ feature of Amazon RDS replicates database updates across two Availability Zones to increase durability and availability. For planned maintenance and unplanned disruptions, Amazon RDS automatically fails over to the standby. |
| Online indexing | Yes | No | Where possible, plan for these activities during a downtime window. |
| Online schema change | Yes | No |
| Resumable online index rebuilds | Yes (SQL Server 2017 and later) | No |
| Accelerated database recovery | Yes (SQL Server 2019) | Yes (SQL Server 2019) | Both SQL Server editions support ADR in SQL Server 2019. |
| **Scalability and performance** | Table and index partitioning | Yes | Yes (SQL Server 2016 SP1 and later) |  |
| Data compression | Yes | Yes (SQL Server 2016 SP1 and later) |  |
| Partition table parallelism | Yes | Yes (SQL Server 2016 SP1 and later) |  |
| In-Memory OLTP | Yes (SQL 2014 and later) | Yes (SQL Server 2016 SP1 and later) |  |
| Delayed durability | Yes (SQL Server 2014 and later) | Yes (SQL Server 2014 and later) |  |
| Columnstore | Yes (SQL Server 2016 and later) | Yes (SQL Server 2016 and later) |  |
| Interleaved execution for multi-statement table valued functions | Yes (SQL Server 2017 and later) | Yes (SQL Server 2017 and later) |  |
| Intelligent Database: batch mode on rowstore | Yes (SQL Server 2019) | No | Not available in Standard edition, but you can take advantage of the other features of Intelligent Database. |
| Intelligent Database: approximate count distinct | Yes (SQL Server 2019) | Yes (SQL Server 2019) |  |
| Intelligent Database: table variable deferred compilation | Yes (SQL Server 2019) | Yes (SQL Server 2019) |  |
| Intelligent Database: scalar UDF inlining | Yes (SQL Server 2019) | Yes (SQL Server 2019) |  |
| **Security** | Transparent database encryption (TDE) | Yes | Yes (SQL Server 2019) |  |
| Contained databases | Yes | Yes |  |
