---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-editions.html
---

# Compare SQL Server editions
<a name="sql-server-editions"></a>

## Overview
<a name="sql-server-editions-overview"></a>

Microsoft SQL Server licensing is one of the largest expenses for a Windows workload environment. Licensing costs for SQL Server can easily extend beyond the compute costs to run the workload. If you choose the wrong edition, you could pay for features that you aren't using or don't even need. This section compares the following SQL Server editions, including their features and relative costs:
+ **Enterprise** – SQL Server Enterprise edition provides data center capabilities with high performance, unlimited virtualization, and several business intelligence (BI) tools.
+ **Standard** – SQL Server Standard edition provides basic data management and business intelligence for smaller organizations and departments.
+ **Web** – SQL Server Web edition is suitable for companies that are web hosters or web value added providers (VAPs). This edition offers a low total cost of ownership, and it provides scalability and manageability capabilities for small to large scale web properties.

<table>
<tbody>
</tbody>
</table>

+ **Developer** – SQL Server Developer edition includes all the functionality of Enterprise edition, but it's intended for development purposes only.
+ **Express** – SQL Server Express edition is a free database and can be used for learning or for building desktop applications. You can update Express edition to other editions.

|
|
| Note: SQL Server Evaluation edition is available for a 180-day trial period. |
| --- |

## Cost impact
<a name="sql-server-editions-cost-impact"></a>

You can purchase SQL Server licenses from a Microsoft reseller and bring them to AWS with Software Assurance. Alternatively, you can use SQL Server licenses with a pay-as-you-go model that has license-included Amazon EC2 AMIs.

If you purchase SQL Server licenses from Microsoft resellers, the core licenses are sold in packs of two and you must license a minimum of four cores per server. The following table shows a cost comparison between Enterprise and Standard editions.

|
|
| Version | SQL Server Enterprise edition (2 cores pack) | SQL Server Standard edition (2 cores pack) | Savings |
| --- |--- |--- |--- |
| 2022 | $15,123 | $3,945 | 74% |
| 2019 | $13,748 | $3,586 | 74% |

|
|
| Note: Pricing in the preceding table is based on Microsoft's public pricing for [SQL Server 2022](https://www.microsoft.com/en-us/sql-server/sql-server-2022-pricing) and [SQL Server 2019](https://www.microsoft.com/en-us/sql-server/sql-server-2019-pricing). |
| --- |

The following cost comparison shows hosting different editions of SQL Server with license-included Amazon EC2 AMIs. In this comparison, SQL Server is hosted on r6i.xlarge (4 vCPU) in the `us-east-1` Region.

|
|
| Instance | Compute cost | Windows license cost | SQL Server license cost | Total |
| --- |--- |--- |--- |--- |
| R6i.xlarge (Linux) | $183.96 | – | – | $183.96 |
| R6i.xlarge \+ Windows | $183.96 | $134.32 | – | $318.28 |
| R6i.xlarge \+ SQL Server Web edition | $183.96 | $134.32 | $49.35 | $367.63 |
| R6i.xlarge \+ SQL Server Standard edition | $183.96 | $134.32 | $350.4 | $668.68 |
| R6i.xlarge \+ SQL Enterprise edition | $183.96 | $134.32 | $1,095 | $1,413.28 |

You can save up to 95 percent on SQL Server licensing costs by selecting the right SQL Server edition for your workload. The following table compares the cost of SQL Server licenses on r6i.xlarge instances.

|
|
| Edition | % savings |
| --- |--- |
| Standard compared to Enterprise | 68% |
| Web compared to Standard | 86% |
| Web compared to Enterprise | 95% |

In most scenarios, organizations switch from Enterprise to Standard edition, but there are some cases where switching from Standard or Enterprise edition down to Web edition is possible.

## Cost optimization recommendations
<a name="sql-server-editions-opt-rec"></a>

You can choose the best edition for your workload based on scaling limits, high availability, performance, and security. The following table shows features that are supported across SQL Server editions. This can help you decide which edition to use. This comparison applies to [SQL Server 2016 SP1 and later versions](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2022?view=sql-server-ver16).

### Scaling limits
<a name="scaling-limits.601cb7fd-1185-5cff-89fb-1448079c2bc2"></a>

The following table compares the scaling limits of the different SQL Server editions.

|
|
| Feature | Enterprise edition | Standard edition | Web edition | Express edition |
| --- |--- |--- |--- |--- |
| Maximum compute capacity used by a single instance of SQL Server Database Engine, SQL Server Analysis Services (SSAS), or SQL Server Reporting Services (SSRS) | Operating  system maximum | Limited to lesser of 4 sockets or 24 cores | Limited to lesser of 4 sockets or 16 cores | Limited to lesser of 4 sockets or 4 cores |
| Maximum memory for buffer pool per instance of SQL Server Database Engine | Operating system maximum        | 128 GB | 64 GB | 1410 MB |
| Maximum capacity for buffer pool extension per instance of SQL Server Database Engine | 32 times max memory configured       | 4 times max memory configured | N/A | N/A |
| Maximum relational database size | 524 PB | 524 PB | 524 PB | 10 GB |
| Maximum memory for Columnstore caches or memory optimized data | Operating system maximum | 32 GB | 16 GB | 352 MB |

If your application requires fewer than 16 cores (32 vCPUs) and 64 GB of RAM, then you can start evaluating from SQL Server Web edition. If your workload requires more than 64 GB of memory or other high availability options, then you must upgrade to SQL Server Standard edition.

You can use SQL Server Web edition to support public and internet accessible webpages, websites, web applications, and web services, but you can't use SQL Server Web edition to support line of business applications. For more information about use cases for SQL Server Web edition, contact [Microsoft Licensing Support](https://www.microsoft.com/licensing/docs/view/Licensing-Use-Rights) or your Microsoft reseller.

You can use SQL Server Standard edition for workloads up to 24 cores (48 vCPUs) and 128 GB memory. However, you can use [buffer pool extensions](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/buffer-pool-extension?view=sql-server-ver16) to enable SQL Server Standard edition to utilize [local instance storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html), like those present in r6id EC2 instances. This extends memory up to the size of four times the maximum memory configuration. This combination of features can delay a server from having to upgrade to Enterprise edition when memory requirements start to rise.

You can identify memory utilization by finding the databases pages in the buffer pool and [page life expectancy](https://learn.microsoft.com/en-us/sql/relational-databases/performance-monitor/sql-server-buffer-node?view=sql-server-ver16) counters. Page life expectancy tells you how long the page is in memory before being flushed back to disk. This counter default value is 300. If pages are residing in memory for hours or days, then there is a chance of reducing allocated memory.

### High availability
<a name="high-availability.5e759dee-36a7-5451-b3b8-cd827ec63912"></a>

The following table compares the high availability capabilities of the different SQL Server editions.

|
|
| Feature | Enterprise edition | Standard edition | Web edition | Express edition |
| --- |--- |--- |--- |--- |
| Server core support 1 | Yes | Yes | Yes | Yes |
| Log shipping | Yes | Yes | Yes | No |
| Database mirroring | Yes | FULL safety mode | Only as witness | Only as witness |
| Backup compression | Yes | Yes | No | No |
| Always On failover cluster instances | 16 nodes | 2 nodes | No | No |
| Always On availability groups | Up to 8 secondary replicas, including 2 synchronous secondary replicas            | No | No | No |
| Basic availability groups | No | 2 nodes | No | No |
| Online page and file restore | Yes | No | No | No |
| Online indexing | Yes | No | No | No |
| Online schema  change | Yes | No | No | No |
| Fast recovery | Yes | No | No | No |
| Mirrored backups | Yes | No | No | No |
| Hot add memory and CPU | Yes | No | No | No |
| Encrypted backup | Yes | Yes | No | No |
| Hybrid backup to Microsoft Azure (backup to URL) | Yes | Yes | No | No |
| Failover server for disaster recovery | Yes | Yes | No | No |
| Failover servers for high availability | Yes | Yes | No | No |

### Other common features
<a name="other-common-features.a066cc20-0b7f-5b92-bc59-f385787ca4c1"></a>

The following table compares the most common features of the different SQL Server editions. For an extensive list of features, see [Editions and supported features of SQL Server 2019](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver16) in the Microsoft documentation.

|
|
| Feature | Enterprise edition | Standard edition | Web edition | Express edition |
| --- |--- |--- |--- |--- |
| (Performance) Resource governor | Yes | No | No | No |
| (Security) Transparent Database Encryption (TDE) | Yes | Yes | No | No |
| (Security)  Extensible key management (EKM) | Yes | No | No | No |
| (Replication)  Oracle publication | Yes | No | No | No |
| (Replication) Peer to peer transactional replication | Yes | No | No | No |
| Change data capture | Yes | Yes | No | No |

### SQL Server Developer edition
<a name="sql-server-developer-edition.98593dc2-e705-575e-9078-a25b50eeaa2b"></a>

All non-production workloads, such as development, QA, testing, staging, and UAT environments, can use SQL Server Developer edition to save 100 percent on SQL Server licensing costs. After you [download SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-downloads), you can install SQL Server Developer edition on EC2 instances by using shared tenancy. Dedicated infrastructure isn't required for SQL Server Developer edition. For more information, see this guide's recommendation for [SQL Server Developer edition](sql-server-dev.md).

### Switching editions
<a name="switching-editions.0f70926c-40bf-53fe-9688-50729ca4e302"></a>

For existing workloads, switching from one edition to another edition requires extensive testing. It's a best practice to check workloads running on Enterprise or Standard editions to see if edition-specific features are used and if there are any alternative solutions for those features. For example, if you want to see if your databases are using any Enterprise-level features, you can run [dynamic management views (DMV)](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-persisted-sku-features-transact-sql?view=azuresqldb-current) on all databases as the following example command shows.

`SELECT feature_name FROM sys.dm_db_persisted_sku_features; GO`

There are some Enterprise edition features that can't be captured in T-SQL, such as online re-indexing as part of SQL maintenance jobs. These must be manually verified.

### Migration considerations
<a name="migration-considerations.5740074a-8d3d-574e-8cdd-342579246c11"></a>

How you license SQL Server will determine your options for switching editions. AMIs, including SQL Server AMIs, have the licensing cost included in the price of the EC2 instance—the licensing cost is bound to the AMI. You can use [AWS billing codes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/billing-info-fields.html) to verify the SQL Server version included in your AMI. For AWS license-included instances, changing the SQL Server edition inside the operating system won't change the billing associated with the AMI. You must migrate your databases to a new EC2 instance with an AMI running the new edition of SQL Server.

If you're bringing your own license, then you have more flexibility. It's usually still recommended to migrate to another EC2 instance that's running the new version. This allows for easy failback if something doesn't go as planned. However, if you must use the existing server, you can still do a side-by-side installation of SQL Server and migrate the databases between instances. For more detailed steps about side-by-side edition downgrades, see [Edition Upgrade and Downgrade in SQL Server](https://www.mssqltips.com/sqlservertip/6686/edition-upgrade-and-downgrade-in-sql-server/) on the MSSQLTips website.

## Additional resources
<a name="sql-server-editions-resources"></a>
+ [Editions and supported features of SQL Server 2022](https://learn.microsoft.com/en-us/sql/sql-server/editions-and-components-of-sql-server-2022?view=sql-server-ver16) (Microsoft Learn)
+ [sys.dm\_db\_persisted\_sku\_features (Transact-SQL)](https://learn.microsoft.com/en-us/sql/relational-databases/system-dynamic-management-views/sys-dm-db-persisted-sku-features-transact-sql?view=azuresqldb-current) (Microsoft Learn)
+ [Which Version of SQL Server Should You Use?](https://www.brentozar.com/archive/2019/01/which-version-of-sql-server-should-you-use/) (Brent Ozar Unlimited)
+ [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=e138c18348afd3853a4874681c660bc1947ec5ca) (AWS)
