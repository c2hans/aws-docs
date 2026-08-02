---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-sql-server-to-aws-using-distributed-availability-groups.html
---

# Migrate SQL Server to AWS using distributed availability groups
<a name="migrate-sql-server-to-aws-using-distributed-availability-groups"></a>

*Praveen Marthala, Amazon Web Services*

## Summary
<a name="migrate-sql-server-to-aws-using-distributed-availability-groups-summary"></a>

Microsoft SQL Server Always On availability groups provide a high availability (HA) and disaster recovery (DR) solution for SQL Server. An availability group consists of a primary replica that accepts read/write traffic, and up to eight secondary replicas that accept read traffic. An availability group is configured on a Windows Server Failover Cluster (WSFC) with two or more nodes.

Microsoft SQL Server Always On distributed availability groups provide a solution to configure two separate availability groups between two independent WFSCs. The availability groups that are part of the distributed availability group don’t have to be in the same data center. One availability group can be on premises, and the other availability group can be on the Amazon Web Services (AWS) Cloud on Amazon Elastic Compute Cloud (Amazon EC2) instances in a different domain.

This pattern outlines steps for using a distributed availability group to migrate on-premises SQL Server databases that are part of an existing availability group to SQL Server with availability groups set up on Amazon EC2. By following this pattern, you can migrate the databases to the AWS Cloud with minimal downtime during cutover. The databases are highly available on AWS immediately after the cutover. You can also use this pattern to change the underlying operating system from on-premises to AWS while keeping the same version of SQL Server.

## Prerequisites and limitations
<a name="migrate-sql-server-to-aws-using-distributed-availability-groups-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ AWS Direct Connect or AWS Site-to-Site VPN
+ The same version of SQL Server installed on-premises and on the two nodes on AWS

**Product versions**
+ SQL Server version 2016 and later
+ SQL Server Enterprise Edition

## Architecture
<a name="migrate-sql-server-to-aws-using-distributed-availability-groups-architecture"></a>

**Source technology stack**
+ Microsoft SQL Server database with Always On availability groups on premises

**Target technology stack**
+ Microsoft SQL Server database with Always On availability groups on Amazon EC2 on the AWS Cloud

**Migration architecture **

![SQL Server with synchronous replication in availability groups on premises and on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/6e229e30-9b11-4ccb-bccd-cbe6601139c0/images/79ee7911-d68f-4db7-9b94-113dcf09c28b.png)

*Terminology*
+ WSFC 1 – WSFC on premises
+ WSFC 2 – WSFC on the AWS Cloud
+ AG 1 – First availability group, which is in WSFC 1
+ AG 2 – Second availability group, which is in WSFC 2
+ SQL Server primary replica – Node in AG 1 that is considered the global primary for all writes
+ SQL Server forwarder – Node in AG 2 that receives data asynchronously from the SQL Server primary replica
+ SQL Server secondary replica – Nodes in AG 1 or AG 2 that receive data synchronously from the primary replica or the forwarder

## Tools
<a name="migrate-sql-server-to-aws-using-distributed-availability-groups-tools"></a>
+ [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) – AWS Direct Connect links your internal network to an AWS Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create *virtual interfaces* directly to public AWS services, bypassing internet service providers in your network path.
+ [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/concepts.html) – Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the AWS Cloud. You can use Amazon EC2 to launch as many or as few virtual servers as you need, and you can scale out or scale in.
+ [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) – AWS Site-to-Site VPN supports creating a site-to-site virtual private network (VPN). You can configure the VPN to pass traffic between instances that you launch on AWS and your own remote network.
+ [Microsoft SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms?view=sql-server-ver15) – Microsoft SQL Server Management Studio (SSMS) is an integrated environment for managing SQL Server infrastructure. It provides a user interface and a group of tools with rich script editors that interact with SQL Server.

## Epics
<a name="migrate-sql-server-to-aws-using-distributed-availability-groups-epics"></a>

### Set up a second availability group on AWS
<a name="set-up-a-second-availability-group-on-aws"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a WSFC on AWS. | Create WSFC 2 on Amazon EC2 instances with two nodes for HA. You will use this failover cluster to create the second availability group (AG 2) on AWS. | Systems administrator, SysOps administrator |
| Create the second availability group on WSFC 2. | Using SSMS, create AG 2 on two nodes in WSFC 2. The first node in WSFC 2 will act as the forwarder. The second node in WSFC 2 will act as the secondary replica of AG 2.<br />At this stage, no databases are available in AG 2. This is the starting point for setting up the distributed availability group. | DBA, Developer |
| Create databases with no recovery option on AG 2. | Back up databases on the on-premises availability group (AG 1). <br />Restore the databases to both the forwarder and the secondary replica of AG 2 with no recovery option. While restoring the databases, specify a location with enough disk space for the database data files and the log files.<br />At this stage, the databases are in the restoring state. They are not part of AG 2 or the distributed availability group, and they are not synchronizing. | DBA, Developer |

### Configure the distributed availability group
<a name="configure-the-distributed-availability-group"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the distributed availability group on AG 1. | To create the distributed availability group on AG 1, use the `CREATE AVAILABILITY GROUP` with the `DISTRIBUTED` option.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-sql-server-to-aws-using-distributed-availability-groups.html) | DBA, Developer |
| Create the distributed availability group on AG 2. | To create the distributed availability group on AG 2, use `ALTER AVAILABILITY GROUP` with the `DISTRIBUTED` option.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-sql-server-to-aws-using-distributed-availability-groups.html)<br />The distributed availability group is created between AG 1 and AG 2.<br />The databases in AG 2 are not yet configured to take part in the data flow from AG 1 to AG 2. | DBA, Developer |
| Add databases to the forwarder and secondary replica on AG 2. | Add the databases to the distributed availability group by using `ALTER DATABASE` with the `SET HADR` `AVAILABILITY GROUP` option in both the forwarder and the secondary replica on AG 2. <br />This starts asynchronous data flow between databases on AG 1 and AG 2. <br />The global primary takes writes, sends data synchronously to the secondary replica on AG 1, and sends data asynchronously to the forwarder on AG 2. The forwarder on AG 2 sends data synchronously to the secondary replica on AG 2. | DBA, Developer |

### Monitor asynchronous data flow between AG 1 and AG 2
<a name="monitor-asynchronous-data-flow-between-ag-1-and-ag-2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Use DMVs and SQL Server logs. | Monitor the status of the data flow between two availability groups by using dynamic management views (DMVs) and SQL Server logs. <br />DMVs that are of interest for monitoring include `sys.dm_hadr_availability_replica_states` and `sys.dm_hadr_automatic_seeding`.<br />For the status of forwarder synchronization, monitor the *synchronized state* in the SQL Server log on the forwarder. | DBA, Developer |

### Perform cutover activities for final migration
<a name="perform-cutover-activities-for-final-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop all traffic to the primary replica. | Stop incoming traffic to the primary replica in AG 1 so that no write activity occurs on the databases and the databases are ready for migration. | App owner, Developer |
| Change the availability mode of the distributed availability group on AG 1. | On the primary replica, set the availability mode of the distributed availability group to synchronous. <br />After you change the availability mode to synchronous, the data are sent synchronously from the primary replica in AG 1 to the forwarder in AG 2. | DBA, Developer |
| Check the LSNs in both availability groups. | Check the last Log Sequence Numbers (LSNs) in both AG 1 and AG 2. Because no writes are happening in the primary replica in AG 1, the data are synchronized, and last LSNs for both availability groups should match. | DBA, Developer |
| Update AG 1 to the secondary role. | When you update AG 1 to the secondary role, AG 1 loses the primary replica role and doesn't accept writes, and the data flow between two availability groups stops. | DBA, Developer |

### Fail over to the second availability group
<a name="fail-over-to-the-second-availability-group"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Manually fail over to AG 2. | On the forwarder in AG 2, alter the distributed availability group to allow data loss. Because you already checked and confirmed that the last LSNs on AG 1 and AG 2 match, data loss is not a concern.<br />When you allow data loss on the forwarder in AG 2, the roles of AG 1 and AG 2 change:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-sql-server-to-aws-using-distributed-availability-groups.html) | DBA, Developer |
| Change the availability mode of the distributed availability group on AG 2. | On the primary replica in AG 2, change the availability mode to asynchronous.<br />This changes the data movement from AG 2 to AG 1, from synchronous to asynchronous. This step is required to avoid network latency between AG 2 and AG 1, if any, and will not impact the performance of the database. | DBA, Developer |
| Start sending traffic to the new primary replica. | Update the connection string to use the listener URL endpoint on AG 2 for sending traffic to the databases.<br />AG 2 now accepts writes and sends data to the forwarder in AG 1, along with sending data to its own secondary replica in AG 2. Data moves asynchronously from AG 2 to AG 1. | App owner, Developer |

### Perform post-cutover activities
<a name="perform-post-cutover-activities"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Drop the distributed availability group on AG 2. | Monitor the migration for the planned amount of time. Then drop the distributed availability group on AG 2 to remove distributed availability group setup between AG 2 and AG 1. This removes the distributed availability group configuration, and data flow from AG 2 to AG 1 stops. <br />At this point, AG 2 is highly available on AWS, with a primary replica that takes writes and a secondary replica in the same availability group. | DBA, Developer |
| Decommission the on-premises servers. | Decommission the on-premises servers in WSFC 1 that are part of AG 1. | Systems administrator, SysOps administrator |

## Related resources
<a name="migrate-sql-server-to-aws-using-distributed-availability-groups-resources"></a>
+ [Distributed availability groups](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/distributed-groups.html)
+ [SQL Docs: Distributed availability groups](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/distributed-availability-groups?view=sql-server-ver15)
+ [SQL Docs: Always On availability groups: a high-availability and disaster-recovery solution](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/always-on-availability-groups-sql-server?view=sql-server-ver15)
