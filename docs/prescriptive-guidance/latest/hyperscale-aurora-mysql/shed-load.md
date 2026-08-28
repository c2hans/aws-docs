---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/hyperscale-aurora-mysql/shed-load.html
---

# Shed load
<a name="shed-load"></a>

Improving response times and increasing available resources for critical workflows might require getting rid of extraneous load. Many of the solutions covered in this section are trade-off decisions. They have consequences to the application, and they must be carefully considered. Consider these using these solutions in the following situations:
+ You are already on the largest size instances, especially for the primary, writable database instance.
+ As a last resort to provide enough headroom in the short term to implement other changes.

Immediate changes include the following:
+ Move noncritical read traffic away from the primary DB instance.
+ Archive or purge old data.
+ Remove referential integrity.
+ Disable the binlog (if in use).
+ Defer non-critical extract, transform, load (ETL) processes.
+ Suspend or degrade nonessential application features.

Before undertaking these actions, evaluate them in the context of long-term business goals and risks.

## Separate read and write workloads
<a name="separate-workloads"></a>

A common technique when running applications powered by MySQL is to offload read operations from the writer (primary) database instance and onto one or more read-only database replicas. By offloading reads, you can reduce overall load on the primary database instance and make room for writes. Be sure to target only reads that are not dependent on immediate *read-after-write* consistency for replicas. A more efficient approach is to move all read traffic to the replica and plan for retrying the read-after-write in the event of replication delay. There are independent read workloads that can be offloaded, such as reporting services. Other reads will require changes at the application level, where the context of why the read was issued is well known.

An alternative approach is to implement a database proxy solution as an intermediary between the application and the database, which can provide the function of read-write splitting and query routing, without application awareness. [ProxySQL](https://proxysql.com/), [MariaDB MaxScale](https://mariadb.com/kb/en/maxscale/), [ScaleARC](https://www.scalearc.com/) and [Heimdall Data](https://aws.amazon.com/blogs/apn/using-the-heimdall-proxy-to-split-reads-and-writes-for-amazon-aurora-and-amazon-rds/) are some of the MySQL compatible proxy solutions available. These products offer multiple additional features, such as caching or connection multiplexing. When you are experiencing a sudden surge in traffic and implementing a new technology in your application stack, we recommend starting with the basic functionality for splitting read/write queries and testing the behavior and performance before using additional features that might have unintended side effects.

## Archive or purge older data
<a name="archive-purge"></a>

Another technique to improve database performance is to offload historical data to another table, database, or Amazon Simple Storage Service (Amazon S3). Many databases retain all the data inline for the whole history of the application. Under normal circumstances in a typical user facing application, this provides users the ability to see all their historical orders. When demand spikes suddenly, many users active on the application probably are new or are focused on placing a new order. If the historical data resides online, in a single table containing billions of rows, this compounds . The table likely also has large indexes. Both table data and indexes are stored in a tree structure. Having more entries in a table requires more levels on the tree, which requires more I/O operations to access the rows. This increases access time to find individual records. More importantly, it causes large unneeded portions of the index to be resident in the database page cache (InnoDB buffer pool).

Archiving older data to a separate table, separate database, or Amazon S3 can reduce access times for end-users, free precious cache, and improve overall application performance. Archiving older data, before the event (for example, retaining only 30 or 90 days) limits the size of the tables and indexes on critical tables. This change requires the application to be modified to query the older data from a secondary location only for the small subset of users who explicitly ask to see historical data.

## Defer noncritical ETL processes
<a name="defer-etl"></a>

Extractions from the main database system for ETL processes can present a stability risk for highly transactional and concurrent workloads during hyperscale conditions. ETL processes are known for the following characteristics:
+ Long-running transactions
+ Broad locks
+ CPU, memory and I/O consumption
+ Contention with transactional workloads serving critical end-user path.

ETL processes that are variable or unpredictable (for example, queries such as `INSERT INTO ... SELECT FROM ...;)` adds to the overall variability in load and contention, increasing the stability risk.

Where possible, defer or reduce the frequency at which ETL processes run, especially if they are not providing critical functions. For critical ETL processes, modify them so that they operate in bounded units of work, such as a processing batches of fixed numbers of rows (for example, using `LIMIT` clauses), using separate transactions, or pull smaller amounts of data over an extended period of time to reduce peak resource demands of the DB instance.

## Turn off less-critical application features
<a name="less-critical"></a>

Gracefully degrading the user experience or removing noncore features when handling a surge of requests conserves database resources for critical functions. This might require a slight change in the customer experience, but a different flow is better than the site being down. Perhaps the personalization on the front page of the site that always does a database call can be temporarily disabled. Or you can stop presenting customized offers to returning customers while selecting products. Temporarily turning off features can enable the page to be cached or delivered without requiring database access.

Other examples include a frontend that has a polling mechanism checking for data changes that require a database call. Reducing the polling frequency will immediately result in fewer database calls. User interfaces that require pagination or provide users the option to retrieve sorted result sets further away from the top result require progressively more expensive database calls. Limit the number of pages in a result set to protect the database from the most expensive database calls. Use feature flags in the application layer to enable the operations team to turn off or degrade features as the application or database load increases.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
