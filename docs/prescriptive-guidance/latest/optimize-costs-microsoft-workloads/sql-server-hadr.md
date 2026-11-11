---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-hadr.html
---

# Choose a high availability and disaster recovery solution
<a name="sql-server-hadr"></a>

## Overview
<a name="sql-server-hadr-overview"></a>

We recommend that you design an architecture for your SQL Server deployment on AWS that meets your business needs while also meeting your [disaster recovery (DR) objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/disaster-recovery-dr-objectives.html), including your recovery time objective (RTO) and recovery point objective (RPO). The following solutions can help you design the right architecture for SQL Server on Amazon Elastic Compute Cloud (Amazon EC2) while also optimizing costs for your SQL Server workloads.
+ **SQL Server Always On availability groups **–** **SQL Server Always On availability groups provide high availability and disaster recovery (HA/DR) solutions for SQL Server databases. An availability group consists of a set of user databases that fail over together. Always On availability groups also provide redundancy at the database level, but don't require shared storage—each replica has its own local storage. You can deploy this feature as an HA/DR solution. For more information, see [What is an Always On availability group?](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver16) in the Microsoft documentation.
+ **SQL Server Always On failover cluster instances (FCI)** –** **SQL Server Always On FCIs use Windows Server Failover Clustering (WSFC) to provide HA at the SQL Server instance level. FCIs require shared storage to host databases. You can use either shared block storage or shared file storage. For example, you can use Amazon FSx for Windows File Server or Amazon FSx for NetApp ONTAP as a shared storage solution with multiple Availability Zones. For more information, see [Always On Failover Cluster Instances (SQL Server)](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/windows/always-on-failover-cluster-instances-sql-server?view=sql-server-ver16) in the Microsoft documentation.
+ **SIOS DataKeeper** –** **SIOS DataKeeper can help you meet both HA and DR requirements by enabling a SQL Server FCI that spans both Availability Zones and AWS Regions. SIOS DataKeeper creates a clustered virtual SAN by using local Amazon Elastic Block Store (Amazon EBS) volumes. It uses synchronous replication between Availability Zones for HA and asynchronous replication between Regions for DR. For more information, see [High Availability Protection for Windows Applications](https://us.sios.com/products/windows/) in the SIOS documentation.
+ **Distributed availability groups** –** **Distributed availability groups are a special type of availability group that spans across two separate Always On availability groups. An availability group can reside across two separate Regions (for example, `us-east-1` and `us-west-1`). You can think of a distributed availability group as an availability group of availability groups because the underlying Always On availability groups are configured on two different WSFC clusters. SQL Server Enterprise edition is required to deploy distributed availability groups. For more information, see [Distributed availability groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/distributed-availability-groups?view=sql-server-ver16) in the Microsoft documentation.
+ **Log shipping** –** **You can implement log shipping to protect your databases across multiple Regions, in the rare event a Region is impacted and becomes unavailable. Depending on the transaction and log shipping frequency, you can achieve RPO and RTO within minutes. For more information, see [About Log Shipping (SQL Server)](https://learn.microsoft.com/en-us/sql/database-engine/log-shipping/about-log-shipping-sql-server?view=sql-server-ver16) in the Microsoft documentation.
+ **AWS Elastic Disaster Recovery** – Elastic Disaster Recovery is a service that manages the replication of servers from any infrastructure to AWS for DR purposes. You can also use Elastic Disaster Recovery to replicate SQL Server across Regions. Elastic Disaster Recovery is an agent-based solution that replicates entire virtual machines, including the operating system, all installed applications, and all databases into a staging area. For more information, see [What is Elastic Disaster Recovery?](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html) in the Elastic Disaster Recovery documentation.
+ **AWS Database Migration Service (AWS DMS)** –** **AWS DMS supports live migration of data to and from AWS, including a different Region. You can use this feature to set up a separate SQL Server instance in a different Region to serve as a disaster recovery database. For more information, see [What is AWS Database Migration Service?](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) in the AWS DMS documentation.

## SQL Server Always On availability groups
<a name="sql-server-always-on"></a>

If you're using SQL Server Enterprise edition just for a high availability [Always On availability group](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-ver16), you can downgrade to SQL Server Standard edition by using basic availability groups. You can reduce costs by approximately 65–75 percent by using basic availability groups instead of Always On availability groups.

|
|
| Note: For more information about cost differences between SQL Server editions, see the [Compare SQL Server editions](sql-server-editions.md) section of this guide. |
| --- |

**Features**
+ Available in SQL Server Standard edition
+ Limit of two replicas (primary and secondary)
+ No read access on secondary replica
+ No integrity checks on secondary replicas

**Limitations**
+ Support for only one availability database per availability group
+ Basic availability groups can't be part of a distributed availability group

The following diagram shows an example architecture for a Windows Server Failover Cluster solution.

![Windows Server Failover Cluster architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/b175cc18-c1ba-4700-ad23-9dde46081b8f.png)

## SQL Server Always On failover cluster instances
<a name="sql-server-always-on-failover"></a>

You can use failover cluster instances (FCIs) to help support continuous database operations while minimizing downtime and reducing the risk of data loss. FCIs offer a solution if you're seeking high availability for your SQL Server database without a read replica configuration.

Unlike availability groups, FCIs can provide a failover solution without requiring SQL Server Enterprise edition. Instead, FCIs require only SQL Server Standard edition licensing. By using FCIs, you might reduce SQL Server licensing costs by 65–75 percent, depending on your workload and licensing model.

|
|
| Note: For additional information on cost differences between SQL Server editions, see the [Compare SQL Server editions](sql-server-editions.md) section of this guide. |
| --- |

Consider the following:
+ Amazon FSx for Windows File Server offers a solution for meeting your SQL Server FCI shared storage requirements. You can use FSx for Windows File Server to avoid the need to purchase a license for a storage replication solution and manage shared storage on your own. This can result in cost savings of 30–40 percent. For more information, see the [Simplify your Microsoft SQL Server high availability deployments using Amazon FSx for Windows File Server](https://aws.amazon.com/blogs/storage/simplify-your-microsoft-sql-server-high-availability-deployments-using-amazon-fsx-for-windows-file-server/) post on the AWS Storage Blog.
+ With the [Software Assurance benefits summary](https://download.microsoft.com/download/0/0/3/0039F316-45CF-4083-AA6E-C35DA9D25C1B/SA_InteractiveBenefitsChart.pdf) (downloadable PDF) and the Bring Your Own License (BYOL) model, you can take advantage of passive failover benefits, as long as the secondary server is passive. This results in cost savings for SQL Server licensing because you don't have to provide licenses to the passive node of the cluster.

The following diagram shows an example architecture for a SQL Server FCI that uses FSx for Windows File Server.

![FSx for Windows File Server architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/5d841057-d3f5-4bb7-9a0c-7cd0649eb29a.png)

## SIOS DataKeeper
<a name="sql-server-sios-datakeeper"></a>

Consider shared storage requirements if you plan to deploy SQL Server FCIs on AWS. Traditional on-premises installations typically use a storage area network (SAN) to meet shared storage requirements, but this isn't a viable option on AWS. Amazon FSx for Windows File Server is the recommended storage solution for SQL Server FCI on AWS, but it has limitations that prevent adding cluster servers in different AWS Regions.

You can use [SIOS DataKeeper](https://aws.amazon.com/blogs/architecture/field-notes-implementing-ha-and-dr-for-microsoft-sql-server-using-always-on-failover-cluster-instance-and-sios-datakeeper/) to create a SQL Server FCI that spans both Availability Zones and Regions. Depending on your configuration, this approach can reduce costs by 58–71 percent.

Consider the following additional benefits of using SIOS DataKeeper:
+ SIOS DataKeeper creates a clustered virtual SAN by using local [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) (Amazon EBS) volumes and uses synchronous replication between Availability Zones for high availability. For disaster recovery, SIOS DataKeeper uses asynchronous replication between Regions.
+ SIOS DataKeeper provides clustering features for SQL Server Standard edition. This can reduce SQL Server licensing costs by 65–75 percent compared to implementing high availability with SQL Server Always On availability groups that use SQL Server Enterprise edition.

|
|
| Note: For more information about cost differences between SQL Server editions, see the [Compare SQL Server editions](sql-server-editions.md) section of this guide. |
| --- |

The following diagram shows an example architecture for a SQL Server FCI using a clustered virtual SAN solution.

![SQL Server FCI using a clustered virtual SAN solution.](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/fb020d77-e4f4-45b3-ab77-31b232c410c4.png)

## Always On availability groups
<a name="sql-server-alwayson-avail-groups"></a>

You can use Always On availability groups for both high availability and disaster recovery purposes. You can achieve high availability by deploying SQL Server across two Availability Zones in one Region. You can achieve disaster recovery by extending availability groups across Regions.

The following diagram shows an example architecture for a solution based on Always On availability groups. The replicas in Region 1 of the diagram use synchronous commit, which provides automatic failover of the availability group. The replica in Region 2 uses asynchronous commit, which requires manual failover of the availability group.

![Always On availability groups architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/adb0c392-d829-4324-9e14-1724de5408af.png)

## Distributed availability groups
<a name="sql-server-distributed-avail-groups"></a>

For mission-critical SQL Server deployments where you can't compromise on reliability or disaster recovery, we recommend a multi-Region approach. Distributing your availability groups across multiple Regions is a highly resilient solution for maintaining business continuity and minimizing downtime.

This architecture uses the capabilities of Amazon FSx for Windows File Server, including shared storage, synchronous file-level replication, and SQL Server Failover Cluster Instances (FCIs). These capabilities help you create a highly available SQL Server environment that spans multiple Availability Zones. By replicating this setup in another Region, you add redundancy that helps your system withstand major disruptions. The solution also provides flexibility and security. The domain-independent architecture of distributed availability groups enables underlying Windows cluster servers to join different Active Directory domains. Certificate-based authentication helps protect your SQL Server environments, and the architecture can help you meet strict recovery time objective (RTO) and recovery point objective (RPO) requirements for a multi-Region disaster recovery (DR) strategy. For information about building a multi-Region architecture, see [Field Notes: Building a Multi-Region Architecture for SQL Server using FCI and Distributed Availability Groups](https://aws.amazon.com/blogs/architecture/field-notes-building-a-multi-region-architecture-for-sql-server-using-fci-and-distributed-availability-groups/) in the AWS Architecture Blog.

The following diagram shows an example architecture for a multi-Region solution using distributed availability groups.

![Multi-Region architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/0ecd8634-bba5-430a-887d-ad384d61af60.png)

## Log shipping
<a name="sql-server-log-shipping"></a>

Log shipping is a proven, reliable, and cost-effective method to safeguard your databases across Regions in the event of an unexpected outage. Organizations have been using log shipping to protect their data for decades.

If you implement log shipping on AWS, you can achieve a recovery point objective (RPO) and recovery time objective (RTO) in minutes, depending on the frequency of transactions and log shipping jobs. If a Region becomes inaccessible, log shipping can help you recover your data.

Consider the following additional benefits of using log shipping:
+ Reduce costs and meet your business requirements by using log shipping for disaster recovery resilience across Regions. Log shipping can reduce your total cost of ownership (TCO) because you need only SQL Server Standard edition or SQL Server Web edition licenses.
+ Remove licensing costs from a passive disaster recovery server by using log shipping with active [Software Assurance](https://download.microsoft.com/download/0/0/3/0039F316-45CF-4083-AA6E-C35DA9D25C1B/SA_InteractiveBenefitsChart.pdf). When you use log shipping with Software Assurance, you need to license only the primary (active) SQL Server.
+ Reduce SQL Server licensing costs, in some configurations by 65–75 percent, by removing the need for SQL Server Enterprise edition to set up distributed availability groups between the Regions. To do this, use SQL Server Standard edition and SQL Server failover cluster instances (FCIs) combined with log shipping to meet your disaster recovery requirements.

|
|
| Note: For more information about cost differences between SQL Server editions, see the [Compare SQL Server editions](sql-server-editions.md) section of this guide. |
| --- |

For more information, see [Extend SQL Server DR using log shipping for SQL Server FCI with Amazon FSx for Windows configuration](https://aws.amazon.com/blogs/architecture/extend-sql-server-dr-using-log-shipping-for-sql-server-fci-with-amazon-fsx-for-windows-configuration/) in the AWS Architecture Blog.

The following diagram shows an example architecture for a log shipping solution.

![Log shipping architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/03d7bff5-7fcf-431f-aafb-2191f423b19d.png)

## AWS Database Migration Service
<a name="sql-server-aws-dms"></a>

You can use AWS Database Migration Service (AWS DMS) to design a high availability and disaster recovery (HA/DR) solution based on your application needs. AWS DMS helps you copy data to a secondary Microsoft SQL Server database in the same Region (HA) or across Regions (DR). This approach can help you use your AWS infrastructure efficiently while optimizing your resource usage.

With AWS DMS, you pay only for the replication instances and any additional log storage. Inbound data transfer into AWS DMS is free. You can use AWS DMS to help make your data available and accessible, while helping to reduce costs associated with licensing and resource usage.

The following diagram shows an example architecture for a solution based on AWS DMS.

![AWS DMS architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/ac2a7006-b989-4204-a5ee-d49ca2ef46d2.png)

## AWS Elastic Disaster Recovery
<a name="sql-server-aws-edr"></a>

Some organizations must ensure that all critical business applications have a disaster recovery plan in place. In the past, many of these organizations invested heavily in traditional disaster recovery solutions, which require you to pre-build and maintain an entire duplicate infrastructure. This approach is costly, time-consuming, and difficult to scale.

Now, you can use [AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide) to eliminate the need for pre-building a disaster recovery infrastructure. Elastic Disaster Recovery doesn't start disaster recovery machines until necessary, so you pay only for what you use when you need it. This means that you can reduce your software licensing and high-performance compute costs.

Additionally, the staging area for the disaster recovery solution contains low-cost [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) volumes. EBS volumes further reduce the cost of provisioning duplicate resources. This helps you reduce your overall disaster recovery costs while still meeting your business requirements. You can use Elastic Disaster Recovery to focus on your core business activities, while AWS manages the underlying infrastructure of the service.

For Microsoft SQL Server, you can use Elastic Disaster Recovery as a cost-effective disaster recovery option. Active Software Assurance covers the licensing for the passive node in a fault-tolerant, highly available SQL Server architecture. However, you still pay compute costs for the passive server to be online. With Elastic Disaster Recovery, the primary server can replicate to the disaster recovery environment without the need to maintain active Software Assurance and without having to pay for disaster recovery compute costs. This combination of savings can help reduce your SQL Server disaster recovery costs.

The following diagram shows an example architecture for a solution based on Elastic Disaster Recovery.

![Elastic Disaster Recovery architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/8bf86fd3-9b73-4565-97b0-a0d112fc417a.png)

For more information, see [How to set up high availability for SQL Server at DR site that was restored using AWS Elastic Disaster Recovery](https://aws.amazon.com/blogs/modernizing-with-aws/set-up-high-availability-for-sql-server-at-dr-site-using-aws-elastic-disaster-recovery/) on the Microsoft Workloads on AWS Blog.

## Cost comparison
<a name="sql-server-cost-comparison"></a>

The following table compares the costs of the HA/DR solutions covered in this section. The comparison uses these assumptions:
+ **Instance type** – r5d.xlarge
+ **License type** – License included for both Windows and SQL Server
+ **Region** – `us-east-1`

|
|
| Solution | High availability | Disaster recovery | Enterprise edition | Standard edition | Cost |
| --- |--- |--- |--- |--- |--- |
| Log shipping | No | Yes | Yes | Yes | SQL Server Enterprise edition: $32,674.8 (2 nodes)<br />SQL Server Standard edition: $14,804.4 (2 nodes) |
| Always On availability groups | Yes | Yes | Yes | Yes, but basic availability groups (2 nodes) | SQL Server Enterprise edition: $32,674.8 (2 nodes)<br />SQL Server Standard edition: $14,804.4 (2 nodes) |
| Always On FCIs | Yes | No | Yes | Yes (2 nodes) | SQL Server Standard edition: $14,804.4 |
| Distributed availability groups | Yes | Yes | Yes | No | SQL Server Enterprise edition: $65,349.6 (4 nodes) |
| Elastic Disaster Recovery | No | Yes | Yes | Yes | Approximately $107.48/month for replication of 1 instance and 1 TB of storageYou pay for Elastic Disaster Recovery hourly, per replicating server. The cost is the same regardless of the number of disks, the size of storage, the number of drill or recovery launches, or the Region that you replicate. |
| SIOS DataKeeper | Yes | Yes | Yes | Yes | Always On availability groups with Software Assurance (2 nodes, 24 cores): $213,480<br />2-node SQL Server cluster running on SQL Server Standard edition with SIOS DataKeeper and Software Assurance: $61,530 (2 nodes) |
| AWS DMS | No | Yes | Yes | Yes | $745.38/month for r5.xlarge instance and 1 TB of storage |

## Cost optimization recommendations
<a name="sql-server-opt-rec"></a>

We recommend that you take the following next steps to choose an HA/DR solution that meets your organization's requirements:
+ Review the [Select the right EC2 instance for SQL Server workloads](right-ec2-instance.md) section of this guide.
+ Determine the IOPS and throughput requirements of your workloads by running performance counters during peak workloads:
  + IOPS = disk reads/sec \+ disk writes/sec
  + Throughput = disk read bytes/sec \+ disk write bytes/sec
+ Use the following storage volume types for better performance and cost savings:
  + NVMe instance storage for `tempdb` and buffer pool extension
  + io2 volumes for database files
+ Use [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html) for recommendations on cost optimization for SQL Server on Amazon EC2. You don't need to install an agent for Trusted Advisor to do SQL Server optimization checks. Trusted Advisor inspects your Amazon EC2 SQL Server license-included instance configurations, such as virtual CPUs (vCPUs), version, and edition. Then, Trusted Advisor makes recommendations based on best practices.
+ Use AWS Compute Optimizer for both Amazon EC2 instance and Amazon EBS rightsizing recommendations.
+ Use [AWS Pricing Calculator](https://calculator.aws/#/) to estimate the costs of your HA/DR strategy.
+ To determine if you can downgrade from SQL Server Enterprise edition to SQL Server Standard edition, use the [sys.dm\_db\_persisted\_sku\_features](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-persisted-sku-features-transact-sql?view=sql-server-ver16) dynamic management view to identify edition-specific features that are active in the current database.

<table>
<tbody>
</tbody>
</table>

+ Perform disaster recovery drills once or twice a year to validate that your design can recover the database within your defined recovery time objective (RTO) and recovery point objective (RPO). These drills can also help you identify architecture weaknesses.

## Additional resources
<a name="sql-server-resources"></a>
+ [Simplify your Microsoft SQL Server high availability deployments using Amazon FSx for Windows File Server](https://aws.amazon.com/blogs/storage/simplify-your-microsoft-sql-server-high-availability-deployments-using-amazon-fsx-for-windows-file-server) (AWS Storage Blog)
+ [Field Notes: Building a Multi-Region Architecture for SQL Server using FCI and Distributed Availability Groups](https://aws.amazon.com/blogs/architecture/field-notes-building-a-multi-region-architecture-for-sql-server-using-fci-and-distributed-availability-groups/) (AWS Architecture Blog)
+ [Architect a disaster recovery for SQL Server on AWS: Part 1](https://aws.amazon.com/blogs/database/part-1-architect-a-disaster-recovery-for-sql-server-on-aws/) (AWS Database Blog)
+ [Microsoft SQL high availability with Amazon FSx for Windows](https://www.youtube.com/watch?v=8dsRkVLy0Nc) (YouTube)
+ [Maximizing Microsoft SQL Server Performance with Amazon EBS](https://aws.amazon.com/blogs/storage/maximizing-microsoft-sql-server-performance-with-amazon-ebs/) (AWS Storage Blog)
+ [Comparing your on-premises storage patterns with AWS Storage services](https://aws.amazon.com/blogs/storage/comparing-your-on-premises-storage-patterns-with-aws-storage-services/) (AWS Storage Blog)
+ [Planning to replace a data center NAS with Amazon FSx File Gateway](https://aws.amazon.com/blogs/storage/planning-to-replace-a-data-center-nas-with-amazon-fsx-file-gateway/) (AWS Storage Blog)
+ [Optimizing cost for your high availability SQL Server deployments on AWS](https://aws.amazon.com/blogs/storage/optimizing-cost-for-your-high-availability-sql-server-deployments-on-aws/) (AWS Storage Blog)
+ [How to set up disaster recovery for SQL Server Always On Availability Groups using AWS Elastic Disaster Recovery](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-set-up-disaster-recovery-for-sql-server-always-on-availability-groups-using-aws-elastic-disaster-recovery/) (Microsoft Workloads on AWS)
+ [How to set up high availability for SQL Server at DR site that was restored using AWS Elastic Disaster Recovery](https://aws.amazon.com/blogs/modernizing-with-aws/set-up-high-availability-for-sql-server-at-dr-site-using-aws-elastic-disaster-recovery/) (Microsoft Workloads on AWS)
