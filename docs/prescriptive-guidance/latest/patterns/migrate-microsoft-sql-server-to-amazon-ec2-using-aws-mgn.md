---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn.html
---

# Migrate an on-premises Microsoft SQL Server database to Amazon EC2 using MGN
<a name="migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn"></a>

*Senthil Ramasamy, Amazon Web Services*

## Summary
<a name="migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn-summary"></a>

This pattern describes the steps for migrating a Microsoft SQL Server database from an on-premises data center to an Amazon Elastic Compute Cloud (Amazon EC2) instance. It uses the AWS Transform MGN (AWS MGN) to rehost your database using an automated lift-and-shift migration. AWS MGN performs block-level replication of your source database server.

## Prerequisites and limitations
<a name="migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ A source Microsoft SQL Server database in an on-premises data center

**Limitations**
+ Your network bandwidth may be limited between the on-premises data center and AWS.
+ AWS MGN is limited to databases that are hosted on standalone servers with dedicated storage. It doesn’t support migrating clustered database systems and database systems where the rate of change exceeds a network’s throughput.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas page](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/), and choose the link for the service.

**Product versions**
+ All versions of Microsoft SQL Server database
+ Windows and Linux operating systems that [support AWS MGN](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html)

## Architecture
<a name="migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn-architecture"></a>

**Source technology stack**

An on-premises Microsoft SQL Server database

**Target technology stack**

A Microsoft SQL Server database on an Amazon EC2 instance

**Target architecture**

![Replicate data from an on-premises corporate data center to AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a459eaef-c256-4691-a7ec-2304f634228c/images/d8d6cee7-f42c-4686-bf92-6e6d39adfb17.png)

This architecture uses AWS MGN to replicate data from an on-premises corporate data center to AWS. The diagram shows the data replication process, API communications, and the test and cutover phases.

1. Data replication:
   + AWS MGN replicates data from the on-premises corporate data center to AWS and initiates ongoing replication of changes.
   + Replication servers in the staging subnet receive and process the data.

1. API communication:
   + Replication servers connect to AWS MGN, Amazon EC2, and Amazon Simple Storage Service (Amazon S3) API endpoints through TCP port 443.
   + AWS MGN manages the migration.
   + Amazon EC2 manages instance operations.

1. Test and cutover:
   + Test instances launch in the operational subnet using replicated data.
   + After successful testing, AWS MGN creates cutover instances for the final migration.

## Tools
<a name="migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn-tools"></a>
+ [AWS Transform MGN (AWS MGN)](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html) helps you rehost (*lift and shift*) applications to the AWS Cloud without change and with minimal downtime.
+ [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services while bypassing internet service providers in your network path.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

## Best practices
<a name="migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn-best-practices"></a>
+ Set up API regional endpoints for AWS MGN, Amazon EC2, and Amazon S3 in the virtual private cloud (VPC) to prohibit public access from the internet.
+ Set up AWS MGN launch settings to launch target database servers in a private subnet.
+ Allow only required ports in database security groups.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn-epics"></a>

### Set up AWS MGN
<a name="set-up-aws-mgn"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure AWS MGN. | Search for the AWS Transform MGN in the AWS Management Console, and initiate the setup process. This will create a replication template and redirect you to the MGN console **Source servers** page. As you configure the MGN service, choose a service role from the generated list. | DBA, Migration engineer |
| Add source server. | Add details of your on-premises source database server, and then add the server. | DBA, Migration engineer |
| Install the AWS MGN agent on the source server. | Download the AWS MGN agent installer to your local system, and transfer the installer to your source database server. To validate the installer hash, see Validating the downloaded [AWS Replication Agent installer for Windows 2012](https://docs.aws.amazon.com/mgn/latest/ug/windows-agent.html#installer-hash-table-2012). | DBA, Migration engineer |

### Install AWS MGN agent on source machines
<a name="install-aws-mgn-agent-on-source-machines"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Generate client IAM credentials. | Before you install the AWS MGN agent, generate AWS credentials by creating a new IAM user with the appropriate permissions.<br />For more information, see [AWS managed policies for AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol.html) and [Generating the required AWS credentials](https://docs.aws.amazon.com/mgn/latest/ug/credentials.html). | DBA, Migration engineer |
| Install the agent on the source server. | Install the agent on the source machine that hosts the Microsoft SQL Server database. For more information, see [Installing the AWS Replication Agent on Windows servers](https://docs.aws.amazon.com/mgn/latest/ug/windows-agent.html).<br />Provide the following AWS credentials:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn.html)<br />Your unique AWS credentials enable the AWS MGN agent to authenticate and perform migration tasks. | App owner, DBA, Migration engineer |
| Choose disks to replicate. | After entering your AWS credentials, the installer verifies that your server meets the minimum requirements for agent installation (for example, whether the server has enough disk space to install the AWS MGN agent). The installer displays the volume labels and storage details.<br />To replicate your database using AWS MGN service, select the applicable disks on your source server. Enter the path of each disk, separated by commas. If you want to replicate all of the disks, leave the path blank. After you confirm the selected disks, the installation proceeds. | DBA, Migration engineer |
| Monitor synchronization progress. | AWS Replication Agent initiates the synchronization process by first taking a snapshot of the selected disks and then replicating the data.<br />You can monitor the synchronization progress from the **Source server** page in the AWS MGN console. For more information, see [Monitor the server in the migration lifecycle](https://docs.aws.amazon.com/mgn/latest/ug/migration-dashboard.html). | DBA, Migration engineer |

### Replication using AWS MGN
<a name="replication-using-aws-mgn"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Manage replication progress. | After you start the initial synchronization, your source server appears in the AWS MGN console, where you can manage and monitor the migration. The console displays an estimated time for complete replication, which is based on the total size of selected disks and available network bandwidth. | DBA, Migration engineer |
| Verify the synchronization. | After the disks on the source server are fully synchronized, verify that all selected disks are listed as fully synced and no errors are reported in the console.<br />The AWS MGN console will then automatically transition the migration lifecycle status to **Ready for testing**, indicating that the replicated environment in AWS is prepared for performance and functionality testing. | App owner, DBA, Migration engineer |

### Test and cut over
<a name="test-and-cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure launch settings. | Choose the source server in the AWS MGN console, and update the launch settings for the target test instance. From the source **Server details** page, navigate to the **Launch settings** tab to configure the test instance.<br />Choose a cost-effective instance type and Amazon Elastic Block Store (Amazon EBS) volume type, and then configure the security groups and network requirements. For more information, see [Launch settings](https://docs.aws.amazon.com/mgn/latest/ug/launch-settings.html). | DBA, Migration engineer |
| Launch the target test instance. | Navigate to the AWS MGN console of your synchronized source machine, and launch a target test instance by choosing **Test and cut over** and then **Launch test instances**.<br />This creates a launch job that deploys the test instance using your configured settings. The instance launches in the AWS Cloud and replicates your source database server's environment. Monitor the launch progress from the **Launch history** page, where you can track the instance creation and address any issues. | DBA, Migration engineer |
| Validate the target test instance. | Validate the Amazon EC2 database server:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn.html)<br />Conduct validation tests to ensure the database functions as expected. | DBA, Migration engineer |
| Rename the server. | AWS MGN migration involves a storage-level copy of your on-premises source server. Your SQL Server EC2 instance contains only the original source server's details in its binaries, so update the binary information to reflect the new server's name.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn.html) | DBA, Migration engineer |
| Launch the cutover instance. | In the AWS MGN console, on the **Source servers** page, confirm that the migration lifecycle status of the server is **Ready for cutover**. Configure the launch settings for the cutover instance, ensuring that the settings mirror your on-premises environment.<br />Before initiating the cutover, shut down your on-premises database, which ensures the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn.html)<br />Initiate the cutover instance in the AWS MGN console. When the cutover instance is operational, log in to the instance and perform the following tests:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn.html) | App owner, DBA, Migration engineer, Migration lead |

## Troubleshooting
<a name="migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The initial synchronization fails at the authentication step. | This is a network connectivity issue. The replication server can’t connect to AWS MGN. |

## Related resources
<a name="migrate-microsoft-sql-server-to-amazon-ec2-using-aws-mgn-resources"></a>

**AWS documentation**
+ [Getting started with AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/getting-started.html)
+ [Migrate an on-premises Microsoft SQL Server database to Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-microsoft-sql-server-database-to-amazon-ec2.html)
+ [What is Microsoft SQL Server on Amazon EC2?](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/sql-server-on-ec2-overview.html)

**Videos**
+ [Performing a Lift and Shift Migration with AWS Transform MGN](https://www.youtube.com/watch?v=tB0sAR3aCb4) (video)
