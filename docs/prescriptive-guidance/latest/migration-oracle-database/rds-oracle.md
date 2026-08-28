---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/rds-oracle.html
---

# Amazon RDS for Oracle
<a name="rds-oracle"></a>

Amazon RDS for Oracle is a managed database service that simplifies the provisioning and management of Oracle Database on AWS. Amazon RDS makes it easy to set up, operate, and scale Oracle Database deployments in the cloud. You can deploy your database in minutes and choose either General Purpose (SSD) storage or Provisioned IOPS storage. (For details, see [Amazon RDS storage types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html#Concepts.Storage) in the AWS documentation.)

Amazon RDS frees you up to focus on application development, because it manages time-consuming database administration tasks, including provisioning, backups, software patching, monitoring, and hardware scaling. Amazon RDS for Oracle easily provisions read replica and Multi-AZ databases to enhance availability, performance, and reliability for production workloads.

## When to choose Amazon RDS
<a name="rds-oracle-choosing"></a>

Amazon RDS for Oracle is a good migration option when:
+ You want to focus on your business and applications, and you want AWS to take care of undifferentiated heavy lifting tasks such as the provisioning of the database, management of backup and recovery tasks, management of security patches, minor Oracle version upgrades, and storage management.
+ You need a highly available database solution, and you want to take advantage of the push-button, synchronous Multi-AZ replication offered by Amazon RDS, without having to manually set up and maintain a standby database.
+ You want to have synchronous replication to a standby instance, to provide high availability for your Oracle Database Standard Edition One (SE1) or Standard Edition Two (SE2) database, instead of having to pay for Oracle Database Enterprise Edition (EE).
+ You want to pay for the Oracle license as part of the instance cost on an hourly basis instead of making a large, upfront investment.
+ Your database size and IOPS needs are supported by Amazon RDS for Oracle. See [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) in the AWS documentation for the current maximum limits.
+ You don't want to manage backups or point-in-time recoveries of your database.
+ You would rather focus on high-level tasks, such as performance tuning and schema optimization, instead of the daily administration of the database.
+ You want to scale the instance type up or down based on your workload patterns without being concerned about licensing complexities.

After assessing your database and project requirements, if you decide to migrate to Amazon RDS for Oracle, see the details provided in the following sections, and review the migration best practices we discuss later in this guide.

## High availability
<a name="rds-oracle-ha"></a>

Amazon RDS provides high availability and failover support for databases that are deployed with the Multi-AZ option. When you provision your database with the Multi-AZ option, Amazon RDS automatically provisions and maintains a synchronous standby replica in a different Availability Zone. The primary database synchronously replicates the data to the standby replica across Availability Zones. In case of infrastructure failure or Availability Zone disruption, Amazon RDS performs an automatic failover to the standby replica so you can resume database operations as soon as the failover is complete. This provides high redundancy, durability, and enhanced availability of your primary database. It also offloads your primary database by taking automated backups from the standby replica. For more information, see [High Availability (Multi-AZ) for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) in the AWS documentation.

The following diagram illustrates the Amazon RDS for Oracle Multi-AZ deployment option. The database application and users connect to the primary Oracle database, and all changes are synchronously replicated to the secondary database, which is in a different Availability Zone. The secondary database is not available to users until the failover is complete. After failover, the endpoint remains the same, so users and database applications can resume database operations without any manual intervention.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/images/guide-img/b6e66b32-33d8-4097-909d-dcc9b3b4a45a/images/c4bb3d8e-0d3d-43a7-99db-030ee48ee4cb.png)

## Read replicas
<a name="rds-oracle-replicas"></a>

A read replica is a special type of Amazon RDS for Oracle DB instance that helps reduce the load on your primary DB instance. Updates made to your primary DB instance are asynchronously copied to the read replica, which you can set up in the same AWS Region or in another AWS Region.

You can provision an Amazon RDS for Oracle database with read replicas by using Oracle Active Data Guard to offload your read-only workload from the primary Oracle database. Oracle Active Data Guard replicates database changes from the source DB instance to the read replicas. This feature supports managed disaster recovery for mission-critical databases by allowing a read replica in another AWS Region to be promoted as a new, standalone, production database. You can provision up to five read replicas for your Amazon RDS for Oracle database.

Amazon RDS for Oracle makes it easy to create the read replicas by managing the configuration of Active Data Guard and maintaining secure network connections between a primary DB instance and its read replicas. For more information, see [Working with read replicas for Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html) in the Amazon RDS documentation.

To use the read replica feature, you must use the Bring Your Own License (BYOL) model with Oracle Database Enterprise Edition (EE) and also have an Active Data Guard license.

### Using a read replica in the same AWS Region
<a name="using-a-read-replica-in-the-same-aws-region.66840e8c-0b51-599a-b030-ae9df37b0c96"></a>

The following diagram illustrates an Amazon RDS for Oracle DB instance in a Multi-AZ environment with a read replica in another Availability Zone within the same AWS Region. Not all AWS Regions offer more than two Availability Zones, so you should [check the Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) you're planning to use before adopting this strategy.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/images/guide-img/b6e66b32-33d8-4097-909d-dcc9b3b4a45a/images/5b8d1a93-5f38-477e-a4fa-24679024c855.png)

### Using a read replica in another AWS Region
<a name="using-a-read-replica-in-another-aws-region.f3309f3c-cd3e-5026-978f-b74da509f819"></a>

Amazon RDS for Oracle also supports cross-Region read replicas. It uses Oracle Active Data Guard to create and manage the configuration of physical standby DB instances in different AWS Regions from the primary DB instance. It replicates data over secure network connections between a primary DB instance and its read replicas across Regions.

Cross-Region read replicas provide:
+ High availability and data protection against single-Region failure.
+ The ability to scale read operations to another AWS Region that's closer to your application's users.

You can promote an Oracle read replica to a standalone DB instance explicitly, or you can promote it implicitly by deleting its source DB instance. When you promote a read replica, the DB instance is rebooted before it becomes available. The promoted read replica behaves the same as any other Oracle DB instance.

The following diagram shows the configuration of Amazon RDS for Oracle cross-Region read replicas.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/images/guide-img/b6e66b32-33d8-4097-909d-dcc9b3b4a45a/images/68626e32-5a5d-4c2c-8f7e-252936c87107.png)

The data transferred for cross-Region replication incurs Amazon RDS data transfer charges.

For more information about using read replicas, see [Working with DB instance read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) and [Working with read replicas for Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html) in the AWS documentation. For more information about data transfer pricing, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
