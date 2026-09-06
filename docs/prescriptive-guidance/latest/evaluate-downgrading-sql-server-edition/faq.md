---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/faq.html
---

# FAQ
<a name="faq"></a>

**Q. Can I change the Amazon RDS for SQL Server edition that I'm running for a DB instance (for example, from SQL Server 2016 Standard edition to Enterprise edition)?**

**A.** Yes, to change the edition and retain your data, take a snapshot of your running DB instance, and create a DB instance of the desired edition from that snapshot. Then delete the old DB instance, unless you want to keep it running.

**Q. Which Microsoft SQL Server database editions are available with Amazon RDS for SQL Server?**

**A.** Amazon RDS supports Microsoft SQL Server versions 2012-2019 and the following editions:
+ Enterprise
+ Standard
+ Web
+ Express

For more information about supported versions and editions, see [Microsoft SQL Server on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html).

**Q. If I change the Amazon RDS for SQL Server edition (for example, change from Enterprise edition to Standard edition), do I need to buy new licenses?**

**A.** When you set up an Amazon RDS DB instance for Microsoft SQL Server, the software license is included. This means that you don't need to purchase SQL Server licenses separately. AWS holds the license for the SQL Server database software.

**Q. What types of licensing options are available with Amazon RDS for SQL Server?**

**A.** When you set up an Amazon RDS DB instance for Microsoft SQL Server, the software license is included. This means that you don't need to purchase SQL Server licenses separately. AWS holds the license for the SQL Server database software. Amazon RDS pricing includes the software license, underlying hardware resources, and Amazon RDS management capabilities.

**Q. What are the licensing policies for using Amazon RDS for SQL?**

**A.** Amazon RDS for SQL Server uses the License Included service model, so you do not need separately purchased SQL Server licenses. The SQL Server database software has been licensed by AWS for your use subject to Section 10.4 of the [AWS Service Terms](https://aws.amazon.com/service-terms/).

**Q. How does the license option impact DB instance scaling?**

**A.** DB instances running SQL Server can be scaled up and down at any point, subject to the prevailing hourly pricing for each DB instance class.

For more information on the scaling implications of reserved DB instances, see [DB instance class support for Microsoft SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.InstanceClasses).

**Q. How can I migrate from an on-premises or an Amazon EC2 Enterprise edition of SQL Server to Standard edition on AWS?**

**A.** Migrating from Enterprise edition to Standard edition requires logical export of data from the Enterprise edition database and importing the data into the Standard edition database instance. To move your data, use [backup and restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html) or [AWS Database Migration Service (AWS DMS)](https://aws.amazon.com/dms/).

**Q. How can I reduce downtime when downgrading my Enterprise edition SQL Server database to Standard edition?**

**A.** To reduce overall downtime, bulk load data into your Standard edition database. You can use backup and restore and logical replication tools such as [AWS DMS](https://aws.amazon.com/dms/) to synchronize your Standard edition database.

**Q. Can I have high availability in my Standard edition of Amazon RDS for SQL Server?**

**A.** Amazon RDS currently uses synchronous replication technology and automatic failover functionality to provide Multi-AZ deployments for SQL Server DB instances. Multi-AZ deployments are available for SQL Server Standard and Enterprise editions. For more information, see [Multi-AZ deployments for Amazon RDS for Microsoft SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.html).

**Q. How can I monitor the performance of my Amazon RDS for SQL Server Standard edition DB instance?**

**A.** To monitor your Standard edition DB instance, you can use [Amazon RDS Performance Insights](https://aws.amazon.com/rds/performance-insights/), [Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html), and [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/).

**Q. Can I have encryption on my Amazon RDS for SQL Server Standard edition DB instance?**

**A.** Amazon RDS can encrypt your Amazon RDS DB instances. Data that is *encrypted at rest* includes the underlying storage for DB instances, its automated backups, read replicas, and snapshots. To enable *encryption in transit*, you can use [Secure Sockets Layer (SSL) encryption for a SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.SSL.Using.html) with the rds.force\_ssl parameter.

**Q. How is Amazon RDS for SQL Server supported?**

**A.** If you have an active AWS Support account, you can contact AWS Support for service requests relating to Amazon RDS or SQL Server.

**Q. How do I know if Amazon RDS supports a specific SQL Server database feature?**

**A.** The SQL Server features that Amazon RDS for SQL Server supports vary, depending on the edition of SQL Server. For information about the SQL Server features that Amazon RDS currently supports, see the [Amazon RDS User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.FeatureSupport).
