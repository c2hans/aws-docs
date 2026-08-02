---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/introduction.html
---

# Migrating Microsoft SQL Server databases to the AWS Cloud
<a name="introduction"></a>

*Sagar Patel, Amazon Web Services*

Amazon Web Services (AWS) provides a comprehensive set of services and tools for deploying Microsoft SQL Server databases on the reliable and secure AWS Cloud infrastructure. Benefits of running SQL Server on AWS include cost savings, scalability, high availability and disaster recovery, better performance, and ease of management. For more information, see [Learn why AWS is the best cloud to run Microsoft Windows Server and SQL Server workloads](https://aws.amazon.com/blogs/compute/learn-why-aws-is-the-best-cloud-to-run-microsoft-windows-server-and-sql-server-workloads/) on the AWS Compute blog.

This guide describes the options available for migrating SQL Server databases from on premises to the AWS Cloud, to Amazon Relational Database Service (Amazon RDS), Amazon Elastic Compute Cloud (Amazon EC2), or VMware Cloud on AWS. It dives into the best practices and recommendations for using these migration options. It also provides information about how to set up a high availability and disaster recovery solution between an on-premises SQL Server environment and AWS, using native SQL Server features like log shipping, replication, and Always On availability groups.

**Note**
As of April 30, 2024, VMware Cloud on AWS is no longer resold by AWS or its channel partners. The service will continue to be available through Broadcom. We encourage you to reach out to your AWS representative for details.

This guide is for program or project managers, product owners, database administrators, database engineers, and operations or infrastructure managers who are planning to migrate their on-premises SQL Server databases to AWS.

## Overview
<a name="overview"></a>

The first step is to perform an analysis of your application and SQL Server database workloads by understanding the complexity, compatibility, and cost of migration. Here are some of the top points you should consider when you plan to migrate:
+ **Database size** – Check the current size and overall capacity growth of your database. For example, if you're planning to migrate your SQL Server database to Amazon RDS or Amazon RDS Custom, you can create Amazon RDS DB instances with up to 16 TiB of storage. You can request more storage by [opening a support ticket with AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html). For the latest information, see [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html) in the Amazon RDS documentation.
+ **IOPS** – Determine the IOPS and throughput of your databases. If you're planning to migrate to Amazon RDS, consider the [I/O performance of Amazon RDS DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html).
+ **Dependencies** – Check current database dependencies. If your database is dependent on other databases, you can either migrate them together or create dependencies after you migrate your main database.

  If your database supports legacy, custom, or packaged applications, Amazon RDS Custom for SQL Server might be a good choice. This service lets you retain control over database configurations, shared file systems, and operating system patches.

  Inventory all SQL Server dependencies. Find out which web servers (for example, reporting servers or business intelligence servers) interface with SQL Server. When it's time to migrate, this information helps you determine what will be impacted and how you can minimize the impact.
+ **Compliance** – Review your current architecture and auditing or compliance needs, to make sure you can satisfy these requirements after moving to Amazon RDS or Amazon EC2.
+ **HA/DR** – Do you need high availability (HA) and automated failover capabilities? If you are running a production workload, high availability and disaster recovery (DR) are recommended best practices.

  Understand your HA/DR requirements to determine whether you need a multi-Region architecture. If so, migrate your SQL Server database to Amazon EC2. Amazon RDS doesn't support a multi-Region configuration.
+ **Version support** – Check the version and edition of your SQL Server software if you're planning to move to Amazon RDS for SQL Server (see [currently supported versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html)).
+ **Network connectivity** – Check the network connectivity between your on-premises environment and AWS, to make sure that it provides enough bandwidth for fast transfers of data between on premises and AWS.
+ **Migration downtime** – Determine the amount of downtime available for migration so you can plan your migration approach and decide whether you want to use online or offline migration.
+ **RTO, RPO, SLA requirements** – Identify your recovery time objective (RTO), recovery point objective (RPO), and service-level agreement (SLA) requirements for your existing database workloads.
+ **Licensing** – Understand your licensing options. You can choose license-included options on Amazon EC2 and Amazon RDS, or choose to [bring your own license](https://aws.amazon.com/windows/faq/#byol-sql) (BYOL) on Amazon EC2.
+ **Feature support** – Identify the database features and functionality that your application uses, whether it was developed in-house or it's commercial-off-the-shelf (COTS) software. This information can help you determine whether you can reduce your licensing costs by switching from SQL Server Enterprise edition to Standard edition. However, review Standard edition resource limitations before you switch. For example, Standard edition supports only 128 GB of RAM.

  Does your workload fit within the features and capabilities offered by Amazon RDS for SQL Server? For more information, see [SQL Server features on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.FeatureSupport). If you need features that aren't supported, migrating to Amazon EC2 is an option.
