---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-microsoft-sql-server-always-on-group-using-mgn.html
---

# Migrate Microsoft SQL Server Always On availability group using AWS Transform MGN
<a name="migrate-microsoft-sql-server-always-on-group-using-mgn"></a>

*Sreenivas Nettem, Bharath Kumar Pammi Ramesh, Anantharaman Seshadri, and Gireesh Sreekantan, Amazon Web Services*

## Summary
<a name="migrate-microsoft-sql-server-always-on-group-using-mgn-summary"></a>

AWS Transform MGN (AWS MGN) is a preferred tool for rehosting existing environments in the AWS Cloud, which allows customers to move away from on-premises data centers. This pattern outlines the process of using AWS MGN to migrate Windows clusters with Microsoft SQL Server Always On availability groups.

## Prerequisites and limitations
<a name="migrate-microsoft-sql-server-always-on-group-using-mgn-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ An AWS Identity and Access Management (IAM) role for AWS MGN orchestration.
+ Access to source database servers (SQL Server Always On availability group).
+ Active Directory in an AWS landing zone to retain DNS names.
+ A staging subnet with closed network communication to Active Directory.
+ Target subnets that can communicate with Active Directory.
+ Two reserved IP addresses for the Windows cluster in a target subnet (one in each Availability Zone).
+ Two reserved IP addresses for the SQL Always On listener in a target subnet (one in each Availability Zone).

**Product versions**
+ Windows Server 2012 or later
+ SQL Server 2012 or later

## Architecture
<a name="migrate-microsoft-sql-server-always-on-group-using-mgn-architecture"></a>

**Source technology stack**

Microsoft Windows cluster (on-premises physical or virtual machine) Microsoft SQL Server Always On availability group

**Target technology stack**

Amazon EC2 Windows instance

**Target architecture**

![AWS architecture for migrating SQL Server Always On availability using AWS MGN.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/aa94040b-5ecf-42f9-90e3-929d0fa5e715/images/0b85c613-51df-475b-9598-3da3f9cd47c6.png)

## Tools
<a name="migrate-microsoft-sql-server-always-on-group-using-mgn-tools"></a>

*AWS services*
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html) helps you rehost (lift and shift) applications to the AWS Cloud without change and with minimal downtime.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.

*Other tools*
+ [Microsoft SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms) is a tool for managing SQL Server, including accessing, configuring, and administering SQL Server components.

## Best practices
<a name="migrate-microsoft-sql-server-always-on-group-using-mgn-best-practices"></a>

For AWS MGN, see [Best practices for AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/best_practices_mgn.html).

## Epics
<a name="migrate-microsoft-sql-server-always-on-group-using-mgn-epics"></a>

### Prepare the target account
<a name="prepare-the-target-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Initialize AWS MGN. | Initialize AWS MGN in the target AWS Region. This creates the required IAM roles and policies. For more information, see [Initializing MGN with the console](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize-console.html). | Cloud administrator |
| Create replication and launch templates. | Configure the replication and launch templates for use with AWS MGN. For more information, see [Configuring the templates](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialization-templates.html) in the AWS documentation. | Cloud administrator |
| Allow communication ports. | To enable network communications for AWS MGN, allow traffic over TCP ports 443 and 1500. For more information, see [Network requirements for MGN](https://docs.aws.amazon.com/mgn/latest/ug/Network-Requirements.html) in the AWS documentation. | Cloud administrator, Network administrator |

### Prepare the source server
<a name="prepare-the-source-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify AWS MGN prerequisites. | Verify that the source servers meet the prerequisites for the AWS MGN agent installation. For more information, see [Installation requirements](https://docs.aws.amazon.com/mgn/latest/ug/installation-requirements.html) in the AWS documentation. | Migration engineer |
| Install AWS MGN agent. | Install the AWS MGN agent on the source servers. During the installation, choose the AWS Region where the servers will be migrated. After installation, the agent communicates with the service and starts replication. For more information, see [Installing the AWS Replication Agent on Windows servers](https://docs.aws.amazon.com/mgn/latest/ug/windows-agent.html). | Migration engineer |
| Check source server status. | In the AWS MGN console, check the status of source servers. The servers display **Ready for testing** when replication begins.<br />If you encounter any errors, see [Troubleshooting communication errors](https://docs.aws.amazon.com/mgn/latest/ug/Troubleshooting-Communication-Errors.html) in the AWS MGN documentation. | Cloud administrator, Migration engineer |
| Optimize replication settings. | SQL Always On clusters use high I/O synchronous replication from the primary server to the secondary server. To optimize replication and avoid lag, use a [dedicated replication server](https://docs.aws.amazon.com/mgn/latest/ug/replication-settings-template.html) for each SQL Always On server.<br />If the database is greater than 5 TB, consider choosing a larger replication server instance size such as **m5.large** instead of the default **t3.small**. | Cloud administrator, Migration engineer |
| Update launch template. | Update the [launch settings](https://docs.aws.amazon.com/mgn/latest/ug/launch-settings.html) and choose subnets for the SQL Always On servers. The SQL Always On cluster servers are spread across different AWS Availability Zones for high availability. | Migration engineer, Migration lead |
| Update launch settings. | Based on your size and performance requirements, update the instance type and input/output operations per second (IOPS) in the launch settings.<br />(Optional) Choose an existing elastic network interface in the launch settings. | Migration engineer, Migration lead |

### Test cutover
<a name="test-cutover"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify source servers. | In the AWS MGN console, verify that the source server status is **Ready for testing**. | Cloud administrator, Migration engineer |
| Launch the test instances. | 1. [Launch the test instances](https://docs.aws.amazon.com/mgn/latest/ug/launching-test-gs.html) and verify in the Amazon EC2 console that the automated checks pass. <br />2. Select and launch test instances for the witness server.<br />3. Verify that you can sign in to the servers through the AWS MGN console.<br />4. Select the SQL Always On cluster servers and launch the test instances together. | Cloud administrator, Migration engineer |
| Test for connectivity and database integrity. | Test the connectivity and database integrity of the test instances. Then mark the source servers as **Ready for cutover** in the AWS MGN console. | Cloud administrator, Migration engineer |

### Pre-migration tasks
<a name="pre-migration-tasks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the database integrity. | This helps to ensure there are no database integrity issues at the source prior to migration. Run `DBCC CHECKDB` and specify `WITH_PHYSICAL_ONLY`. Running this check without `WITH_PHYSICAL_ONLY` can cause performance issues at the source. To maintain database integrity, run a weekly full check of the database.<br />These commands check the database’s logical and physical integrity by detecting potential corruption issues. The check verifies the database’s structure, such as pages, rows, indexes, and system tables. | Data engineer, DBA |
| Test the connections to linked servers. | Test the connections among all existing servers, and document their status. This helps to ensure that linked servers work as intended after the migration. | Data engineer, DBA |
| Verify the backups. | Confirm the integrity of source backups. | Data engineer, DBA |

### AWS MGN cutover
<a name="aws-mgn-cutover"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop the SQL Server and cluster services. | Stop the SQL Server and Microsoft cluster services on all SQL cluster nodes. | DBA, Migration engineer |
| Verify the servers. | In the AWS MGN console, verify that the status of the source servers is **Ready for cutover** and that the data replication status is **Healthy**. | Migration engineer |
| Launch the cutover. | 1. Launch the AWS MGN cutover for the witness server.<br />2. Launch the AWS MGN cutover for the SQL Always On cluster instances.<br />3. Verify that the status changes to **Cutover in progress**.For more information, see [Launching a cutover instance](https://docs.aws.amazon.com/mgn/latest/ug/launch-cutover-gs.html) in the AWS MGN documentation. | Migration engineer |
| Test the launched servers. | Log in to the launched Amazon EC2 instances and validate the cluster’s health. Verify that the servers are in the correct subnets, the instance size and IOPS settings are correct, and the witness server is accessible. | DBA, Migration engineer |

### Database post-cutover tasks
<a name="database-post-cutover-tasks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the cluster IP address. | Update the cluster IP address for the Windows cluster using the two reserved IP addresses in the target subnets. For more information, see [Change the IP Address of a Failover Cluster Instance](https://learn.microsoft.com/en-us/sql/sql-server/failover-clusters/windows/change-the-ip-address-of-a-failover-cluster-instance?view=sql-server-2016). | DBA, Migration engineer |
| Update the Always On availability group listener IPs. | 1. Open the failover cluster manager.<br />2. Choose the Always On availability group role.<br />3. Expand the availability group listener name.<br />4. In the context (right-click) menu, choose **IP address properties**.<br />5. Update the IP address using the address reserved for the listener in the target subnet.<br />6. Connect to the SQL Server primary instance using SSMS, and verify that the Always On listener is using both subnet IPs. | DBA, Migration engineer |
| Verify the connection. | Using SSMS, connect to the Always On availability group listener, and confirm that the connection succeeds. | DBA, Migration engineer |
| Check the health of Always On availability group. | 1. Navigate to the **Availability groups** folder, open the context (right-click) menu, and choose **Show dashboard**.<br />2. For all replicas, verify that the synchronization state is **Synchronized**. | DBA, Migration engineer |
| Check the error log. | Open the error log, and verify any errors reported for the SQL Server instance. Ensure that the recovery is complete for all databases. | DBA, Migration engineer |
| Test the linked servers. | Test the connectivity of any linked servers. In case of any connectivity issues, ensure that the target server and port are accessible. | DBA, Migration engineer |

### Finalize the cutover
<a name="finalize-the-cutover"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Finalize the cutover. | After you validate the target SQL Always On clusters, [finalize](https://docs.aws.amazon.com/mgn/latest/ug/launch-cutover-gs.html#revert-finalize-cutover-gs) the cutover through the AWS MGN console. This stops data replication from the source servers and discards the data from the replication server. It also removes the replication server and its associated resources. | Cloud administrator, Migration engineer |

## Troubleshooting
<a name="migrate-microsoft-sql-server-always-on-group-using-mgn-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| AWS MGN troubleshooting | For common issues and resolutions, see the [Troubleshooting](https://docs.aws.amazon.com/mgn/latest/ug/troubleshooting.html) and [FAQ](https://docs.aws.amazon.com/mgn/latest/ug/FAQ.html) sections in the AWS MGN documentation. |

## Related resources
<a name="migrate-microsoft-sql-server-always-on-group-using-mgn-resources"></a>

*AWS resources*
+ [Option-1 Rehost - AWS Transform MGN (AWS)](https://catalog.us-east-1.prod.workshops.aws/workshops/c6bdf8dc-d2b2-4dbd-b673-90836e954745/en-US/04-application-migration/01-mgn)
+ [What Is AWS Transform MGN?](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)

*SQL Server resources*
+ [What is SQL Server Management Studio (SSMS)?](https://learn.microsoft.com/en-us/ssms/sql-server-management-studio-ssms)

## Additional information
<a name="migrate-microsoft-sql-server-always-on-group-using-mgn-additional"></a>

For standard security requirements for migrating workloads to the AWS Cloud, see the [Best Practices for Security, Identity, and Compliance](https://aws.amazon.com/architecture/security-identity-compliance/) on the AWS website.
