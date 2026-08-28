---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-replication-options/compare-solutions.html
---

# Comparing Amazon Aurora replication solutions
<a name="compare-solutions"></a>

The following table provides a comparison of the three Amazon Aurora replication solutions.

|  |
| --- |
|  | Aurora Replicas | Cross-Region Aurora Replicas | Aurora global databases |
| --- |--- |--- |--- |
| Provides high availability | Yes | No | No |
| Provides disaster recovery | No | Yes | Yes |
| Replication type | Asynchronous | Asynchronous | Asynchronous |
| Automated failover | Yes | No | No |
| Offloads SELECT queries | Yes | Yes | Yes |
| Can issue writes against replica | No | Yes (not recommended) | No |
| Proximity to primary cluster | Always exists in the same Region as the primary. | Cannot exist in the same Region as the primary. | Cannot exist in the same Region as the primary. |
| Replication lag | Usually much less than 100 milliseconds | Depends on transaction volume. Typically, a few seconds for most systems. | Typically, less than 1 second. |
| Cost considerations | Pay only for additional DB instance nodes. | You pay standard Aurora rates for instances, storage, cross-Region data transfer, backup storage, and replicated write I/Os between the primary Region and each secondary Region. | You pay standard Aurora rates for instances, storage, cross-Region data transfer, backup storage, and replicated write I/Os between the primary Region and each secondary Region. |
| Number of replicas supported | 15 within the same Region. | Up to five secondary DB clusters in different Regions for Amazon Aurora MySQL-Compatible Edition. Amazon Aurora. (PostgreSQL-Compatible Edition does not support cross-Region replicas.) | Up to five secondary DB clusters in different Regions. |
| Time to provision | Less than 5 minutes, irrespective of the database size. | Depends on the database size because creating the replica requires the entire copy of the database to be replicated to the secondary Regions. | Depends on the database size because creating the replica requires the entire copy of the database to be replicated to the secondary Regions. |

When deciding which option to implement, use the following guidelines:
+ If you need high availability of your Aurora cluster, use Aurora Replicas. Aurora will automatically promote one of the Aurora Replicas if the primary instance fails. Aurora Replicas are also great for horizontally scaling your read workloads. The Aurora connection manager will automatically distribute workload across multiple Aurora Replicas within the same AWS Region by using the common reader endpoint.
+ If you are looking for cross-Region disaster recovery (DR), use Aurora global databases. With Aurora global databases, you can span multiple AWS Regions to enable fast local reads and quick DR. You can use a secondary Region as a backup option in case you need to recover quickly from a regional degradation or outage. A database in a secondary Region can be promoted to full read/write capabilities in less than 1 minute.
+ Cross-Region Aurora Replicas serve a couple use cases. First, if you need a cross-Region copy of your Aurora database and you can't use a global database because of some of its limitations, you can use cross-Region Aurora Replicas. Second, if you need to migrate from Amazon Relational Database Service (Amazon RDS) for MySQL to Amazon Aurora MySQL-Compatible Edition, you can set up an Aurora MySQL-Compatible replica.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
