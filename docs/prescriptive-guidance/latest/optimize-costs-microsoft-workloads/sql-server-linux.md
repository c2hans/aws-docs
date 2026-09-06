---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-linux.html
---

# Evaluate SQL Server on Linux
<a name="sql-server-linux"></a>

## Overview
<a name="sql-server-linux-overview"></a>

Since SQL Server 2017, it's been possible to install SQL Server on Linux operating systems. SQL Server on Linux is enterprise ready and offers flexibility, high performance, security features, reduced TCO, HA/DR features, and a great user experience. You can switch from SQL Server on Windows Server to SQL Server on Linux to save on Windows Server licensing costs.

For Linux, SQL Server is available to deploy on Red Hat Enterprise Linux (RHEL), SUSE Linux Enterprise Server (SLES), Ubuntu, and Amazon Linux 2. The SQL Server database engine runs the same way on both Windows Server and Linux, but there are some fundamental changes to certain tasks when using Linux. One key difference between running SQL Server Always On applications on Linux and Windows is related to failover clustering. If you deploy Always On availability groups on a Windows Server host, you can take advantage of [Windows Server Failover Clustering (WSFC)](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/windows/windows-server-failover-clustering-wsfc-with-sql-server?view=sql-server-ver16) and Active Directory as built-in features that support failover clustering. However, neither WSFC nor Active Directory are available to support failover clustering on Linux. If you want to launch failover clustering for SQL Server on Linux, you can use [AWS Launch Wizard](https://aws.amazon.com/launchwizard/) to simplify cluster setup and SQL installation on Linux instances by using [ClusterLabs Pacemaker](https://aws.amazon.com/blogs/opensource/deploying-a-highly-available-microsoft-sql-server-on-linux-on-aws/).

SQL Server on Windows and Linux share a common code base. That is, the SQL Server core engine hasn't been changed, at all, to run on Linux. SQL Server introduced a Platform Abstraction Layer (SQLPAL), as shown in the following diagram.

![The Sequel Server Platform Abstraction Layer (SQLPAL)](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/e0a110b3-ecdf-41ec-a636-a64e9060d19d.png)

SQLPAL is responsible for abstraction of calls and communication between SQL Server and the underlying operating system. The host extension is simply a native Linux application. Low-level operating system functions are native calls to optimize the I/O, memory, and CPU usage. When the host extension starts, it loads and initializes SQLPAL, which then brings up SQL Server. SQLPAL launches isolated software processes that provide the required translation for the rest of the code. Adding this new layer to the SQL Server architecture means that the same enterprise-level core features and benefits that have made SQL Server so powerful on Windows are available regardless of operating system.

## Cost impact
<a name="sql-server-linux-cost-impact"></a>

For r5.2xlarge instances, the Windows Server licensing cost reduction is about $268 in each scenario. The reduction is a higher percentage of the total server cost compared to using less expensive SQL Server editions. The following table shows the costs savings.

|
|
| Instance | Edition | Monthly cost of SQL Server on Windows | Monthly cost of SQL Server on Linux | Savings |
| --- |--- |--- |--- |--- |
| r5.2xlarge | Web | $735 | $466 | 37% |
| r5.2xlarge | Standard | $1,337 | $1068 | 20% |
| r5.2xlarge | Enterprise | $2,826 | $2,558 | 10% |

|
|
| Note: The price estimation in the preceding table is based on on-demand pricing in the `us-east-1` Region and can be viewed directly in the [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=fd37122637710aa7ba46d1949e8b6a15f68d3c0f). |
| --- |

Consider an example scenario where an ISV customer in the SMB segment is looking to save costs on their development environment. They're already using SQL Server Developer edition on a set of Windows servers. By switching from Windows with SQL Server Developer edition to Linux with SQL Server Developer edition, the ISV customer can save 33 percent on their development workload. The following table shows the following estimated costs for this scenario.

|
|
| Estimate | Monthly cost |
| --- |--- |
| [Windows \+ SQL Server](https://calculator.aws/#/estimate?id=da0a0f5f58ddf91aa3398af3a78691cfa2204673) | $9,307.72 |
| [Linux \+ SQL Server](https://calculator.aws/#/estimate?id=131966c579020eaec957f441c67e9aa0bfd32411) | $6,218.36 |
| Estimated cost savings | $3,089.36  (33%) |

In another example scenario, a company migrates license-included SQL Server EC2 instances from Windows to Linux. The company saves a total of $300,000 per year on Windows Server licensing costs—roughly 20 percent of their total AWS bill.

## Cost optimization recommendations
<a name="sql-server-linux-optrec"></a>

We recommend that you consider the following:
+ SQL Server on Linux is supported starting with SQL Server 2017.
+ To help make the switch, you can use the [Windows to Linux replatforming assistant for Microsoft SQL Server Databases](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/replatform-sql-server.html). The replatforming assistant is a scripting tool that can help you move existing SQL Server workloads from Windows to Linux operating systems by checking for common incompatibilities, exporting the databases from the Windows host, and then importing the databases into an EC2 instance running Microsoft SQL Server 2017 on Ubuntu 16.04.
+ You can also use the [backup and restore](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver16) capabilities in SQL Server to switch from SQL Server on Windows to Linux.
+ You can easily and quickly deploy to SQL Server on Linux or Ubuntu by using the [AWS Launch Wizard](https://docs.aws.amazon.com/launchwizard/latest/userguide/what-is-launch-wizard.html). The Launch Wizard can deploy SQL Server on Linux or Ubuntu in both standalone and high availability scenarios based on your application needs. For more information, see the [Deploying to SQL Server Always on Linux with AWS Launch Wizard](https://aws.amazon.com/blogs/modernizing-with-aws/deploy-microsoft-sql-server-always-on-to-linux-with-aws-launch-wizard/) post in the Microsoft Workloads on AWS blog.

The following diagram shows an architecture for a solution that uses the Windows to Linux replatforming assistant for Microsoft SQL Server Databases.

![Windows to Linux replatforming assistant architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/images/guide-img/480a01db-b8a4-4c65-9cb9-61f06d23096c/images/5adc01bb-a2ed-4850-894b-c1d7e8bfdf94.png)

## Additional resources
<a name="sql-server-linux-resources"></a>
+ [Overview of SQL Server on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-overview?view=sql-server-ver16) (Microsoft Learn)
+ [Installation guide for SQL Server on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup?view=sql-server-ver16) (Microsoft Learn)
+ [Deploying to SQL Server Always on Linux with AWS Launch Wizard](https://aws.amazon.com/blogs/modernizing-with-aws/deploy-microsoft-sql-server-always-on-to-linux-with-aws-launch-wizard) (Microsoft Workloads on AWS Blog)
+ [Highly Available SQL Server on Linux](https://aws.amazon.com/blogs/opensource/deploying-a-highly-available-microsoft-sql-server-on-linux-on-aws/) (AWS Open Source Blog)
