---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/distributed-groups.html
---

# Distributed availability groups
<a name="distributed-groups"></a>

A distributed availability group spans two separate availability groups. You can think of it as an availability group of availability groups. The underlying availability groups are configured on two different WSFC clusters. The availability groups that participate in a distributed availability group do not need to share the same location. They can be physical or virtual, on premises or in the public cloud. The availability groups in a distributed availability group don't have to run the same version of SQL Server. The target DB instance can run a later version of SQL Server than the source DB instance.

A distributed availability group architecture gives you a flexible way to rehost a mission-critical SQL Server instance or database on AWS. It provides a hybrid solution for lifting and shifting (or lifting and transforming) your critical SQL Server databases on AWS.

Using a distributed availability group architecture is more efficient than extending existing on-premises WFSC clusters to AWS. Data is transferred only from the on-premises primary to one of the AWS replicas (the *forwarder*). The forwarder is responsible for sending data to other secondary read replicas in AWS.

In the following diagram, the first WSFC cluster (WSFC 1) is hosted on premises and has an on-premises availability group (AG 1). The second WSFC cluster (WSFC 2) is hosted on AWS and has an AWS availability group (AG 2). [AWS Direct Connect](https://aws.amazon.com/directconnect/) is used as a dedicated network connection between the on-premises environment and AWS. The on-premises availability group (AG 1) has two replicas (*nodes*). The data transfer between the nodes is synchronous, with automatic failover. Similarly, the AWS availability group (AG 2) also has two replicas, and the data transfer between them is synchronous with automatic failover. The distributed availability group keeps the databases in sync in an asynchronous manner. Data is transferred from the SQL Server primary replica in AG 1 (which is on premises) to the primary replica (the forwarder) in AG 2 (which is on AWS). The forwarder is responsible for sending data to other read replicas on AWS and keeping them updated. After the on-premises and AWS databases are synchronized, you can perform a manual failover of the distributed availability group to AWS. The AWS database becomes the primary database for read/write access from applications.

![SQL Server migration process with distributed availability groups.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/f074e8ac-1930-48e8-9d3d-bb86ce128c3c.png)

**Note**
At any given point of time, there is only one database that is available for write operations. You can use the remaining secondary replicas for read operations. To scale out your read workloads, you can add more read replicas in multiple Availability Zones on AWS.

For more information about distributed availability groups, see:
+ [Microsoft SQL Server documentation](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/distributed-availability-groups)
+ [How to architect a hybrid Microsoft SQL Server solution using distributed availability groups](https://aws.amazon.com/blogs/database/how-to-architect-a-hybrid-microsoft-sql-server-solution-using-distributed-availability-groups/) on the AWS Database blog
+ [Migrate SQL Server to AWS using distributed availability groups](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-sql-server-to-aws-using-distributed-availability-groups.html) on the AWS Prescriptive Guidance website
