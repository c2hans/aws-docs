---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/always-on.html
---

# Always On availability groups
<a name="always-on"></a>

SQL Server Always On availability groups is an advanced, enterprise-level feature to provide high availability and disaster recovery solutions. This feature is available if you are using SQL Server 2014 and later versions. You can also use an Always On availability group to migrate your on-premises SQL Server databases to Amazon EC2 on AWS. This approach enables you to migrate your databases either with downtime or with minimal downtime.

If you have an existing on-premises deployment of SQL Server Always On availability groups, your primary replica and secondary replica will be synchronously replicating data within the availability group. So, to migrate your database to the AWS Cloud, you can extend your Windows Server Failover Clustering (WSFC) cluster to the cloud. This can be temporary, just for migration purposes.  You then create a secondary replica in the AWS Cloud and use asynchronous replication, as shown in the following diagram. After the secondary replica is synchronized with the primary on-premises database, you can perform a manual failover whenever you are ready for cutover.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/6c77c27b-b957-4491-b7db-b06996fa3e11.png)

**Note**
At any given point of time, there is only one database that is available for write operations. You can use the remaining secondary replicas for read operations. To scale out your read workloads, you can add more read replicas in multiple Availability Zones on AWS.

For more information about distributed availability groups, see:
+ [Microsoft SQL Server documentation](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/distributed-availability-groups),
+ [How to architect a hybrid Microsoft SQL Server solution using distributed availability groups](https://aws.amazon.com/blogs/database/how-to-architect-a-hybrid-microsoft-sql-server-solution-using-distributed-availability-groups/) on the AWS Database blog
+ [Migrate SQL Server to AWS using distributed availability groups](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-sql-server-to-aws-using-distributed-availability-groups.html) on the AWS Prescriptive Guidance website
