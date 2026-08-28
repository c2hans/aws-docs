---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/consolidate-instances.html
---

# Consolidate instances
<a name="consolidate-instances"></a>

This section focuses on the cost optimization technique of combining multiple SQL Server instances onto the same server to minimize licensing costs and maximize resource utilization.

## Overview
<a name="consolidate-instances-overview"></a>

Creating an instance is part of the process for installing the SQL Server Database Engine. The SQL Server instance is a complete install, containing its own server files, security logins, and system databases (master, model, msdb, and tempdb). Because an instance has all its own files and services, you can install multiple SQL Server instances on the same operating system without the instances interfering with each other. However, since the instances are all installed on the same server, they all share the same hardware resources, such as compute, memory, and networking.

It's typical to use only a single SQL Server instance per server in production environments so that a "busy" instance doesn't overuse the shared hardware resources. Giving each SQL Server instance its own operating system, with its own resources, is a better boundary than relying on resource governance. This is especially true for high performance SQL Server workloads that require large amounts of RAM and CPU resources.

However, not all SQL Server workloads use a large amount of resources. For example, some organizations assign each of their customers their own dedicated SQL Server instance for compliance or security purposes. For smaller clients or clients that aren't typically active, that means running the SQL Server instances with minimal resources.

As noted in the [Microsoft SQL Server 2019: Licensing guide](https://download.microsoft.com/download/e/2/9/e29a9331-965d-4faa-bd2e-7c1db7cd8348/SQL_Server_2019_Licensing_guide.pdf), each server running SQL Server must account for a minimum of four CPU licenses. This means that even if you run a server with only two vCPUs, you must still license SQL Server for four vCPUs. Based on [Microsoft's public SQL Server pricing](https://www.microsoft.com/en-us/sql-server/sql-server-2022-pricing) that's a difference of $3,945 if you use SQL Server Standard edition. For organizations running multiple servers with single SQL Server instances using minimal resources, the combined cost of having to license unused resources can be substantial.

## Cost optimization scenario
<a name="consolidate-instances-cost-opt-scenario"></a>

This section explores an example scenario that compares the difference between running four Windows Server servers, each with a single SQL Server instance, to a single larger Windows Server server running multiple SQL Server instances simultaneously.

If each SQL Server instance only needs two vCPUs and 8 GB RAM, the total cost per server is $7,890 for the SQL Server license in addition to an hourly compute cost of $0.096.

|
|
| EC2 instance | vCPUs | RAM | Price | vCPUs to license | Total SQL Server licensing cost |
| --- |--- |--- |--- |--- |--- |
| m6i.large | 2 | 8 | 0.096 | 4 | $7,890 |

Expanding this out to four servers, the total cost is $31,560 for the SQL Server license with an hourly compute cost of $0.384.

|
|
| EC2 instances | Total vCPUs | Total RAM | Total price | vCPUs to license | Total SQL Server licensing cost |
| --- |--- |--- |--- |--- |--- |
| 4x m6i.large | 2 | 32 | 0.384 | 16 | $31,560 |

If you combine all four SQL Server instances onto a single EC2 instance, the total amount of compute resources and compute stays the same. However, by removing unnecessary SQL Server licensing costs, you can reduce the total cost to run the workload by $15,780.

|
|
| EC2 instance | vCPUs | RAM | Price | vCPUs to license | Total SQL Server licensing cost |
| --- |--- |--- |--- |--- |--- |
| m6i.2xlarge | 8 | 32 | 0.384 | 8 | $15,780 |

**Note**
In the preceding tables, compute costs show hourly on-demand pricing for Amazon EC2 servers running Windows Server in the `us-east-1` Region. The SQL Server Standard Edition licensing costs are referring to [Microsoft's public SQL Server pricing](https://www.microsoft.com/en-us/sql-server/sql-server-2022-pricing).

## Cost optimization recommendations
<a name="consolidate-instances-cost-opt-rec"></a>

If you're considering consolidating SQL Server instances, the biggest concern is the resource consumption for each of the instances that you want to consolidate. It's important to get performance metrics over long periods to get a better understanding of the workload patterns on each server. Some common tools for resource consumption monitoring are [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-basic-detailed.html), [Windows Performance Monitor](https://techcommunity.microsoft.com/blog/askperf/windows-performance-monitor-overview/375481) (perfmon), and the [native monitoring tools](https://learn.microsoft.com/en-us/sql/relational-databases/performance/performance-monitoring-and-tuning-tools?view=sql-server-ver16) of SQL Server.

We recommend that you consider the following questions when analyzing whether your SQL Server workloads could be combined to use the same server resources without them interfering with one another:
+ What resources (CPU, memory, and network bandwidth) are consumed during your steady state?
+ What resources (CPU, memory, and network bandwidth) are consumed during spikes?
+ How often do spikes take place? Are spikes consistent?
+ Do the resource spikes of one server coincide with the resource spikes of another server?
+ What are the storage [IOPS and throughput](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/iops-requirements.html) used by SQL Server?

If you wish to move forward with a plan to combine SQL Server instances, see the [Run multiple instances of SQL Server on one Amazon EC2 instance](https://aws.amazon.com/blogs/mt/run-multiple-instances-sql-server-on-one-amazon-ec2-instance/) post on the AWS Cloud Operations & Migrations Blog. This post provides instructions on how to make the configuration changes in SQL Server to add additional instances. Before you get started, consider the minor differences when multiple instances are installed on the same server:
+ The default SQL Server database instance is named `MSSQLSERVER` and uses port 1433.
+ Each additional instance installed on the same server is a "named" database instance.
+ Each named instance has a unique instance name and a unique port.
+ The [SQL Server Browser](https://learn.microsoft.com/en-us/sql/tools/configuration-manager/sql-server-browser-service?view=sql-server-ver16) must run to coordinate traffic to the named instances.
+ Each instance can use separate locations for database data files and separate logins.
+ The SQL Server [max server memory settings](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/server-memory-server-configuration-options?view=sql-server-ver16) must be configured according to the performance needs of each instance, with their combined total also leaving enough memory for the underlying operating system.
+ You can use the SQL Server [native backup and restore](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver16) capabilities or [AWS DMS](https://aws.amazon.com/blogs/database/consolidate-data-from-identical-sql-server-databases-into-a-single-amazon-rds-for-sql-server-database-using-aws-dms/) for migration or consolidation.

## Additional resources
<a name="consolidate-instances-resources"></a>
+ [SQL Server Licensing Datasheet](https://download.microsoft.com/download/0/5/c/05c60185-ebdd-4472-895a-3d8e8da55682/SQL_Server_2019_Licensing_Datasheet.pdf) (AWS Cloud Operations & Migrations Blog)
+ [SQL Server Multiple instance setup blog post](https://aws.amazon.com/blogs/mt/run-multiple-instances-sql-server-on-one-amazon-ec2-instance/) (AWS Cloud Operations & Migrations Blog)
+ [SQL Server Best practices guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/cpu-mismatch.html) (AWS Prescriptive Guidance documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
