---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws.html
---

# Configure read-only routing in Always On availability groups in SQL Server on AWS
<a name="configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws"></a>

*Subhani Shaik, Amazon Web Services*

## Summary
<a name="configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-summary"></a>

This pattern covers how to use the standby secondary replica in SQL Server Always On by offloading the read-only workloads from the primary replica to the secondary replica.

Database mirroring has one-to-one mapping. You can’t read the secondary database directly, so you must create snapshots. The Always On availability group feature was introduced in Microsoft SQL Server 2012. In later versions, major functionalities have been introduced, including read-only routing. In Always On availability groups, you can read the data directly from the secondary replica by changing the replica mode to read-only.

The Always On availability groups solution supports high availability (HA), disaster recovery (DR), and an alternative to database mirroring. Always On availability groups work at the database level and maximize the availability of a set of user databases.

SQL Server uses the read-only routing mechanism to redirect the incoming read-only connections to the secondary read replica. To achieve this, you should add the following parameters and values in the connection string:
+ `ApplicationIntent=ReadOnly`
+ `Initial Catalog=<database name>`

## Prerequisites and limitations
<a name="configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-prereqs"></a>

**Prerequisites**
+ An active AWS account with a virtual private cloud (VPC), two Availability Zones, private subnets, and a security group
+ Two Amazon Elastic Compute Cloud (Amazon EC2) machines with [SQL Server 2019 Enterprise Edition Amazon Machine Image](https://aws.amazon.com/marketplace/pp/prodview-btjcozd246p6w) with [Windows Server Failover Clustering (WSFC)](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/ec2-fci.html) configured at the instance level and an Always On availability group configured at the SQL Server level between the primary node (`WSFCNODE1`) and the secondary node (`WSFCNODE2`), which are part of the AWS Directory Service for Microsoft Active Directory directory named `tagechtalk.com`
+ One or more nodes configured to accept `read-only` in the secondary replica
+ A listener named `SQLAG1` for the Always On availability group
+ SQL Server Database Engine running with the same service account on two nodes
+ SQL Server Management Studio (SSMS)
+ A test database named `test`

**Product versions**
+ SQL Server 2014 and later

## Architecture
<a name="configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-architecture"></a>

**Target technology stack**
+ Amazon EC2
+ AWS Managed Microsoft AD
+ Amazon FSx

**Target architecture**

The following diagram shows how the Always On availability group (AG) listener redirects queries that contain the `ApplicationIntent` parameter in the connection to the appropriate secondary node.

![Three step-process between two Availability Zones for node 1 WSFC and node 2 WSFC with Amazon EFS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/19b5937b-da10-4c74-8619-fdcb758f2211/images/f9ba0f89-7dc2-4f4c-8eee-bef56968ad2d.png)

1. A request is sent to the Always On availability group listener.

1. If the connection string does not have the `ApplicationIntent` parameter, the request is sent to the primary instance.

1. If the connection string contains `ApplicationIntent=ReadOnly`, the request is sent to the secondary instance with read-only routing configuration, which is WSFC with an Always On availability group.

## Tools
<a name="configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-tools"></a>

**AWS services**
+ [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) enables your directory-aware workloads and AWS resources to use Microsoft Active Directory in the AWS Cloud.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon FSx](https://docs.aws.amazon.com/fsx/?id=docs_gateway) provides file systems that support industry-standard connectivity protocols and offer high availability and replication across AWS Regions.

**Other services**
+ SQL Server Management Studio (SSMS) is a tool for connecting, managing, and administering the SQL Server instances.
+ sqlcmd is a command-line utility.

## Best practices
<a name="configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-best-practices"></a>

For more information about Always On availability groups, see the [SQL Server documentation](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/always-on-availability-groups-sql-server?view=sql-server-ver16).

## Epics
<a name="configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-epics"></a>

### Set up read-only routing
<a name="set-up-read-only-routing"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the replicas to read-only. | To update both the primary and the secondary replica to read-only, connect to the primary replica from SSMS, and run the *Step 1* code from the [Additional information](#configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-additional) section. | DBA |
| Create the routing URL. | To create routing URL for both replicas, run the *Step 2* code from the [Additional information](#configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-additional) section. In this code, `tagechtalk.com` is the name of the AWS Managed Microsoft AD directory. | DBA |
| Create the routing list. | To create the routing list for both replicas, run the *Step 3* code from the [Additional information](#configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-additional) section. | DBA |
| Validate the routing list. | Connect to the primary instance from SQL Server Management Studio, and run the *Step 4* code from the [Additional information](#configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-additional) section to validate the routing list. | DBA |

### Test the read-only routing
<a name="test-the-read-only-routing"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect by using the `ApplicationIntent` parameter. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws.html) | DBA |
| Perform a failover. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws.html) | DBA |

### Connect by using the sqlcmd command-line utility
<a name="connect-by-using-the-sqlcmd-command-line-utility"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect by using sqlcmd. | To connect from sqlcmd, run the *Step 5* code from the [Additional information](#configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-additional) section at the command prompt. After you are connected, run the following command to show the connected server name.<pre>SELECT SERVERPROPERTY('ComputernamePhysicalNetBios') .</pre><br />The output will display the current secondary replica name (`WSFCNODE1`). | DBA |

## Troubleshooting
<a name="configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Creating the listener fails with the message 'The WSFC cluster could not bring the Network Name resource online'. | For information, see the Microsoft blog post [Create Listener Fails with Message 'The WSFC cluster could not bring the Network Name resource online'](https://techcommunity.microsoft.com/blog/sqlserversupport/create-listener-fails-with-message-the-wsfc-cluster-could-not-bring-the-network-/318235). |
| Potential issues, including other listener issues or network access issues. | See [Troubleshoot Always On Availability Groups Configuration (SQL Server)](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/troubleshoot-always-on-availability-groups-configuration-sql-server?view=sql-server-ver16) in the Microsoft documentation. |

## Related resources
<a name="configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-resources"></a>
+ [Configure read-only routing for an Always On availability group](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/configure-read-only-routing-for-an-availability-group-sql-server?view=sql-server-ver16)
+ [Troubleshoot Always On Availability Groups Configuration (SQL Server)](https://docs.microsoft.com/en-us/sql/database-engine/availability-groups/windows/troubleshoot-always-on-availability-groups-configuration-sql-server?view=sql-server-ver16)

## Additional information
<a name="configure-read-only-routing-in-an-always-on-availability-group-in-sql-server-on-aws-additional"></a>

*Step 1. Update the replicas to read-only*

```
ALTER AVAILABILITY GROUP [SQLAG1] MODIFY REPLICA ON N'WSFCNODE1' WITH (SECONDARY_ROLE (ALLOW_CONNECTIONS = READ_ONLY))
GO
ALTER AVAILABILITY GROUP [SQLAG1] MODIFY REPLICA ON N'WSFCNODE2' WITH (SECONDARY_ROLE (ALLOW_CONNECTIONS = READ_ONLY))
GO
```

*Step 2. Create the routing URL*

```
ALTER AVAILABILITY GROUP [SQLAG1] MODIFY REPLICA ON N'WSFCNODE1' WITH (SECONDARY_ROLE (READ_ONLY_ROUTING_URL = N'TCP://WSFCNode1.tagechtalk.com:1433'))
GO
ALTER AVAILABILITY GROUP [SQLAG1] MODIFY REPLICA ON N'WSFCNODE2' WITH (SECONDARY_ROLE (READ_ONLY_ROUTING_URL = N'TCP://WSFCNode2.tagechtalk.com:1433'))
GO
```

*Step 3. Create the routing list*

```
ALTER AVAILABILITY GROUP [SQLAG1] MODIFY REPLICA ON N'WSFCNODE1' WITH (PRIMARY_ROLE(READ_ONLY_ROUTING_LIST=('WSFCNODE2','WSFCNODE1')));
GO
ALTER AVAILABILITY GROUP [SQLAG1] MODIFY REPLICA ON N'WSFCNODE2' WITH (PRIMARY_ROLE (READ_ONLY_ROUTING_LIST=('WSFCNODE1','WSFCNODE2')));
GO
```

*Step 4. Validate the routing list*

```
SELECT AGSrc.replica_server_name AS PrimaryReplica, AGRepl.replica_server_name AS ReadOnlyReplica, AGRepl.read_only_routing_url AS RoutingURL , AGRL.routing_priority AS RoutingPriority FROM sys.availability_read_only_routing_lists AGRL INNER JOIN sys.availability_replicas AGSrc ON AGRL.replica_id = AGSrc.replica_id INNER JOIN sys.availability_replicas AGRepl ON AGRL.read_only_replica_id = AGRepl.replica_id INNER JOIN sys.availability_groups AV ON AV.group_id = AGSrc.group_id ORDER BY PrimaryReplica
```

*Step 5. SQL Command Utility*

```
sqlcmd -S SQLAG1,1433 -E -d test -K ReadOnly
```
