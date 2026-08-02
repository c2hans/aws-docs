---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/rds-outpost-read-replica.html
---

# Amazon RDS on AWS Outposts Read Replicas
<a name="rds-outpost-read-replica"></a>

Amazon RDS Read Replicas provide enhanced performance and durability for Amazon RDS database (DB) instances. They make it easy to elastically scale out beyond the capacity constraints of a single DB instance for read-heavy database workloads. Amazon RDS on AWS Outposts uses the MySQL and PostgreSQL DB engines' built-in replication functionality to create a read replica from a source DB instance. The source DB instance becomes the primary DB instance. Updates made to the primary DB instance are asynchronously copied to the read replica. Read replica use Customer-owned IP (CoIP) model and the replications runs on your local network.

## Considerations for Amazon RDS on Outposts Read Replicas
<a name="rds-outpost-read-replica-considerations"></a>

Review the following considerations for Amazon RDS on Outposts deployments for Read Replicas:
+ You can't create read replicas for RDS for SQL Server on RDS on Outposts DB instances.
+ Cross-Region read replicas aren't supported on RDS on Outposts.
+ Cascading read replicas aren't supported on RDS on Outposts.
+ The source RDS on Outposts DB instance can't have local backups. The backup target for the source DB instance must be your AWS Region. Ensure you have a redundant [service link connection](https://docs.aws.amazon.com/outposts/latest/userguide/region-connectivity.html) of at least 500 mbps to send your RDS backups to AWS Region databases with frequently changing data or heavy write traffic.
+ Read replicas require customer-owned IP (CoIP) pools.
+ Read replicas on RDS on Outposts can only be created in the same virtual private cloud (VPC) as the source DB instance.
+ Read replicas on RDS on Outposts can be located on the same Outpost or another Outpost in the same VPC as the source DB instance.
+ You can't create read replicas for DB instances encrypted with AWS KMS External Key Store (XKS).
+ Creating your read replica as a Multi-AZ DB instance is independent of whether the source database is a Multi-AZ DB instance.
