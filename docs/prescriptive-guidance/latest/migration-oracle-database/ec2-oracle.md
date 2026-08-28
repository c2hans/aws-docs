---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/ec2-oracle.html
---

# Amazon EC2 for Oracle
<a name="ec2-oracle"></a>

Amazon EC2 supports a self-managed Oracle database—that is, it gives you full control over the setup of the infrastructure and the database environment. Running the database on Amazon EC2 is very similar to running the database on your own server. You have full control of the database and operating system-level access, so you can use your choice of tools to manage the operating system, database software, patches, data replication, backup, and restoration. This migration option requires you to set up, configure, manage, and tune all the components, including Amazon EC2 instances, storage volumes, scalability, networking, and security, based on AWS architecture best practices.

## When to choose Amazon EC2
<a name="ec2-oracle-choosing"></a>

Amazon EC2 is a good migration option for your Oracle database when:
+ You need full control over the database and access to its underlying operating system.
+ You want to control your backups, replication, and clustering.
+ You want to use features and options that aren't currently supported by Amazon RDS. For details, see [Oracle Database Feature Support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html#Oracle.Concepts.FeatureSupport) in the Amazon RDS documentation.
+ You need a specific Oracle Database version that isn't supported by Amazon RDS. For a list of supported version and editions, see [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html) in the Amazon RDS documentation.
+ Your database size and performance needs exceed Amazon RDS offerings. For details, see [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) in the Amazon RDS documentation.
+ You want to avoid automatic software patches that might not be compliant with your applications.
+ You want to achieve higher IOPS and provision storage capacity than the current limits. For details, see [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) in the Amazon RDS documentation.

## High availability
<a name="ec2-oracle-ha"></a>

Oracle Database on Amazon EC2 can work with any Oracle-supported replication technology to achieve high availability and disaster recovery. Some of the common solutions are Oracle Data Guard, Oracle Active Data Guard, and Oracle GoldenGate.

An Oracle database on Amazon EC2 uses Oracle Data Guard or Oracle Active Data Guard to achieve high availability, data protection, and disaster recovery.
+ Oracle Data Guard provides a set of services for creating, maintaining, and managing standby databases, to help protect Oracle production databases against disasters and data corruption. Oracle Data Guard automatically maintains each standby database by transmitting redo changes from the primary database, and then applying the redo to the standby database. If the primary database goes down for any planned or unplanned outage, you can fail over to the standby database by converting it into a primary read-write database. Oracle Data Guard is included with Oracle Database Enterprise Edition (EE) only and doesn't require a separate license.
+ Oracle Active Data Guard provides read-only access to a physical standby database for queries, sorting, reporting, and other read operations while it applies redo changes continuously from the primary database. Oracle Active Data Guard requires a separate license that must be additionally purchased with Oracle Database EE. Oracle Active Data Guard features include Real-Time Query, Automatic Block Repair, Far Sync, Standby Block Change Tracking, Active Data Guard Rolling Upgrade, Global Database Services, and Application Continuity.

The following diagram shows how you can use Oracle Database on Amazon EC2 in two Availability Zones within a single AWS Region. The primary database is a read-write database, and the standby database is configured with either Data Guard (physical standby with no read access) or Active Data Guard. All the redo data from the primary database is transferred and applied to the standby database asynchronously by default.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/images/guide-img/b6e66b32-33d8-4097-909d-dcc9b3b4a45a/images/357d6899-a21a-483d-8292-4383cc0c4cd4.png)

You can also use Oracle Data Guard or Oracle Active Data Guard to configure high availability and disaster recovery across multiple AWS Regions, using Oracle Database on Amazon EC2 for your primary database and standby database, as illustrated in the following diagram.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/images/guide-img/b6e66b32-33d8-4097-909d-dcc9b3b4a45a/images/ebc22379-24ff-4d0c-836d-392f1e1bd930.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
