---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/trans-rep.html
---

# Transactional replication
<a name="trans-rep"></a>

Transactional replication is a SQL Server technology that is used to replicate changes between two databases. These changes can include database objects like tables (primary key is required), stored procedures, views, and so on, as well as data. The replication process involves a *publisher* (the primary database that publishes data), a *subscriber* (a secondary database that receives replicated data), and a *distributor* (a server that stores metadata and transactions for transactional replication). You can use transactional replication for SQL Server on Amazon EC2 and Amazon RDS for SQL Server DB instances.

Transactional replication creates a snapshot of the objects and data in your on-premises (publication) database and sends it to the subscriber database. After the snapshot is applied to the subscriber, all subsequent data changes and schema modifications made at the publisher are sent over to the subscriber as they occur. The data changes are then continuously applied to the subscriber in the same order as they occurred at the publisher.

After synchronization is complete, you perform validation on the target SQL Server DB instance. When the two databases are in sync, you stop stop the activity on the on-premises database, ensure that replication has completed, and then perform the cutover to the target SQL Server DB instance. You can then stop the push subscription, delete it, and start using Amazon RDS for SQL Server.

Subscriber databases can also be used as read-only databases. The distributor, which records synchronization jobs, is recommended to be on a separate server. If your target database is on Amazon RDS for SQL Server, you can set up a push subscription to propagate changes to the subscriber.

We recommend that you use transactional replication when you want to:
+ Perform a one-time migration of your data to Amazon RDS or Amazon EC2.
+ Migrate schema-level or table-level objects to AWS.
+ Migrate a portion of a database to AWS.
+ Migrate with minimal downtime using existing SQL Server replication strategies by adding additional subscribers.

If you're planning to use transactional replication for one-time migration of your data to Amazon RDS for SQL Server, we recommend that you set up a Single-AZ configuration for the replication. After the replication process is complete, you can convert your environment into a Multi-AZ architecture for high availability.

The following diagram shows the transactional replication process for databases on Amazon RDS and Amazon EC2.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/1d486d77-5620-452d-ab02-7ae465f15992.png)

For more information about transactional replication, see the [Microsoft SQL Server documentation](https://docs.microsoft.com/en-us/sql/relational-databases/replication/transactional/transactional-replication) and [How to migrate to Amazon RDS for SQL Server using transactional replication](https://aws.amazon.com/blogs/database/how-to-migrate-to-amazon-rds-for-sql-server-using-transactional-replication/) on the AWS Database blog.
