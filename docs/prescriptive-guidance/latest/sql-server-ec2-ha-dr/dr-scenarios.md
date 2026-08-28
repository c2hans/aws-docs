---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-ha-dr/dr-scenarios.html
---

# Disaster recovery scenarios
<a name="dr-scenarios"></a>

This section provides examples of a single Availability Zone or AWS Region failure, and discusses options for disaster recovery (DR). The examples assume a recovery point objective (RPO) of 15 minutes and a recovery time objective (RTO) of 4 hours.

## Availability Zone failure
<a name="az-failure"></a>

You can use one of the following options to recover from a single Availability Zone failure within the given parameters (RPO of 15 minutes, RTO of 4 hours).
+ Provision the application recovery by using the most recent Amazon EC2 image backup, and connect to the existing warm standby database instance through an Always On availability group deployment or log shipping.
  + A SQL Server Always On availability group setup for DR with two or more nodes provides automatic failover to the secondary node through synchronous-commit or asynchronous-commit mode, so the database is available immediately. For an HA setup, both nodes are available for read operations. This option meets both RTO and RPO requirements comfortably. In SQL Server Standard edition, using basic availability groups is also an option, but it's limited to two nodes, because an availability group can include only one database. However, you can set up multiple availability groups within one Region or across Regions. This setup provides cost savings, because there is no additional cost for the secondary node, which isn't accessible for read operations. SQL Server Enterprise edition provides full functionality and failover for all databases within a single availability group. For examples of this option, see the following architecture diagrams:
    + [Two-node HA/DR architecture with Always On availability group cluster (single-Region, Multi-AZ)](architecture.md#two-node-one-region)
    + [Three-node HA/DR architecture (single-Region, Multi-AZ)](architecture.md#three-node-ha-dr-architecture-single-region-multi-az)
    + [Four-node HA/DR architecture with Always On distributed availability group cluster (multi-Region, Multi-AZ)](architecture.md#four-node-two-region)
    + [Three-node HA/DR architecture with single availability group (multi-Region)](architecture.md#three-node-ha-dr-architecture-with-single-availability-group-multi-region)
  + SQL Server log shipping as a DR solution requires a manual failover to a standby server and depends on the frequency of log backups. This is one of the least expensive DR options. SQL Server editions for the primary and log-shipped DR site do not need to match. This option meets the RPO (using transaction log backups every 5 minutes and RTO, but requires maintenance through manual, custom scripts. For an example of this option, see [Three-node HA/DR architecture with log shipping (multi-Region)](architecture.md#three-node-ha-dr-architecture-with-log-shipping-multi-region).
+ If you have an application such as an SQL Server Reporting Services (SSRS) application that has a scaled-out deployment, the load balancer can redirect all traffic to the secondary node.
+ You can use Amazon EC2 base AMIs for the application and database server to provision the infrastructure. Databases can be restored in a new Availability Zone, depending on their size and backup frequency, from the most recent native backups (full backup, differential backup, or transaction log backups every 5 minutes) or by using Amazon EBS snapshots. This option meets the RPO and RTO requirements but requires custom scripting. You must also consider the time required to provision the infrastructure, and meeting RPO and RTO requirements can be challenging.
+ Amazon EC2 images (including EBS volumes) for both applications and the database server can be restored in a new Availability Zone. RPO can be challenging, depending on the most recent backup, but this option can be combined with the most recent transaction logs to meet requirements. This option supports Windows Volume Shadow Copy Service (VSS) snapshots.

## Region failure
<a name="region-failure"></a>

You can use one of the following options to recover from a single AWS Region failure within the given parameters (RPO of 15 minutes, RTO of 4 hours).
+ You can use Amazon EC2 base Amazon Machine Images (AMIs) for the application and database server to provision the infrastructure. Databases can be restored in a new Region, depending on their size and backup frequency, from the most recent native backups (full backup, differential backup, or transaction log backups every 5 minutes). This option meets the RPO and RTO requirements but requires custom scripting.
  + SQL Server log shipping as a DR solution requires a manual failover to a standby server and depends on the frequency of log backups. This is one of the least expensive DR options. SQL Server editions for the primary and log-shipped DR site do not need to match. This option meets the RPO (by using transaction log backups every 5 minutes) and RTO, but requires maintenance through manual, custom scripts. Large databases require long restoration times.
+ You can use Amazon EC2 AMI for both the application and the database server and restore it to a target in a new Region. RPO depends on the size and frequency of the backups.
  + The most recent application images can be restored by using an AMI. You can use recent native differential or transaction log backups every 5 minutes to bring the database up to date to meet the RPO.
  + RTO depends on the size and time to transfer and restore the snapshots to the new Region, if the source isn't already in sync with the target.
+ The solution with the least downtime is to restore the application backup image and have a warm standby SQL Server node in a remote Region by using a two-node, three-node, or four-node availability group setup (basic, classic, or distributed) and to connect to the standby database server after a failover. The synchronous-commit mode replica meets the RPO requirements, whereas asynchronous-commit mode replica might be delayed depending on the volume of transactions. You can use a distributed availability group configuration to scale out database nodes in a new Region, if needed. This configuration also reduces complexity because it uses two independently availability groups instead of a single availability group spread across Regions in either synchronous-commit or asynchronous-commit mode, and meets both RTO and RPO requirements comfortably. Alternatively, using SQL Server basic availability groups in the Standard edition is also an option. However, it has limitations because it supports only up to two nodes, and only one database can be in a single availability group although multiple availability groups are supported. You can set up SQL Server Standard edition within one Region or across Regions. This edition provides cost savings because it doesn't charge for the secondary node, which isn't accessible for read operations. SQL Server Enterprise edition provides full functionality, and supports the failover of all databases as a single availability group failover.

## Common use cases
<a name="common-use-cases"></a>

As a sizing exercise, 80% of SQL Server applications running on Amazon EC2 that have a normal OLTP workload can be grouped into one of three categories based on how critical they are:
+ SQL Server HA/DR with SQL Server backups, using two synchronous-commit replicas and one asynchronous-commit mode replica
+ AWS Backup HA/DR with SQL Server backups, using an Amazon EC2 AMI (for both the application and the database) and Amazon EBS storage
+ AWS Backup HA/DR with SQL Server backups, using an Amazon EC2 base AMI for the database server, an Amazon EC2 image for the application, and Amazon EBS snapshots

 The following table provides details about each category.

|
|
| Category | SQL Server HA/ DR with SQL Server backups  | AWS Backup HA/DR with AMIs, EBS storage, and SQL Server backups | AWS Backup HA/DR with AMIs, EBS snapshots, and SQL Server backups  |
| --- |--- |--- |--- |
| Restore process in case of a disaster | + Restore Amazon EC2 base AMI for the application from AWS Backup<br />+ Fail over to the standby instance in the Region (in the case of Availability Zone failure) or to the cross-Region instance (in case of Region failure)<br />+ Meets RPO and RTO requirements | + Restore Amazon EC2 images from backups for both the application and the database <br />+ Provides both in-Region and cross-Region support<br />+ Apply most recent SQL Server differential and transaction log backups (every 15 minutes) to meet RPO and RTO requirements for the database | + Restore Amazon EC2 image from backup for the application<br />+ Restore Amazon EC2 base AMI for the database server<br />+ Restore EBS snapshots (if any).<br />+ Cluster has to be rebuilt<br />+ Provides both in-Region and cross-Region support <br />+ Apply most recent differential and transaction log backups to the database to meet RPO requirements, but RTO might not be met |
| Primary resources | + Three SQL Server Enterprise edition licenses (passive HA and DR nodes license is free if you have an existing Software Assurance licensing agreement with Microsoft; see [announcement](https://cloudblogs.microsoft.com/sqlserver/2019/10/30/new-high-availability-and-disaster-recovery-benefits-for-sql-server/))<br />+ Amazon EC2 backup space on Amazon S3<br />+ Cross-Region data transfer | + One SQL Server license (any edition)<br />+ Amazon EC2 backup space on Amazon S3<br />+ SQL Server backups (differential and log files) on Amazon S3<br />+ Cross-Region data transfer | + One SQL Server license (any edition)<br />+ Amazon EC2 backup space on Amazon S3<br />+ SQL Server backups (differential or log files) on Amazon S3<br />+ Cross-Region data transfer |
| HA/DR | Offers HA and DR | Offers DR only | Offers DR only |
| RPO | Failover is handled by SQL Server availability group (DR is manual) | Manual or custom scripted | Manual or custom scripted |
| RTO | Seconds to minutes | Minutes to hours | Multiple hours |
| Risk of missing SLAs | Low | Medium | High |
| Manageability | Simple | Medium | Medium |
| Scaling | Simple | Medium | Medium |
| File size limitations for uploads to Amazon S3 or cross-Region transfer | N/A - Handled in synchronous-commit mode or asynchronous-commit mode to a warm standby | Yes | Yes |
| Data loss | Near zero (depends on the workload and infrastructure provisioned) | Depends on the frequency of Amazon EC2 backup images and SQL Server backups | Depends on the frequency of Amazon EC2 backup images or EBS snapshots and SQL Server backups |
| Cost | Medium | Low - medium | Low - medium |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
