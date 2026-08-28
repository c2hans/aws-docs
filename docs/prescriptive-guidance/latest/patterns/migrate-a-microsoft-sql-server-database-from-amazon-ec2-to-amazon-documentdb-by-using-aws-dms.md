---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-a-microsoft-sql-server-database-from-amazon-ec2-to-amazon-documentdb-by-using-aws-dms.html
---

# Migrate a Microsoft SQL Server database from Amazon EC2 to Amazon DocumentDB by using AWS DMS
<a name="migrate-a-microsoft-sql-server-database-from-amazon-ec2-to-amazon-documentdb-by-using-aws-dms"></a>

*Umamaheswara Nooka, Amazon Web Services*

## Summary
<a name="migrate-a-microsoft-sql-server-database-from-amazon-ec2-to-amazon-documentdb-by-using-aws-dms-summary"></a>

This pattern describes how to use AWS Database Migration Service (AWS DMS) to migrate a Microsoft SQL Server database hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance to an Amazon DocumentDB (with MongoDB compatibility) database.

The AWS DMS replication task reads the table structure of the SQL Server database, creates the corresponding collection in Amazon DocumentDB, and performs a full-load migration.

You can also use this pattern to migrate an on-premises SQL Server or an Amazon Relational Database Service (Amazon RDS) for SQL Server DB instance to Amazon DocumentDB. For more information, see the guide [Migrating Microsoft SQL Server databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/welcome.html) on the AWS Prescriptive Guidance website.

## Prerequisites and limitations
<a name="migrate-a-microsoft-sql-server-database-from-amazon-ec2-to-amazon-documentdb-by-using-aws-dms-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ An existing SQL Server database on an EC2 instance.
+ Fixed database (**db\_owner**) role assigned to AWS DMS in the SQL Server database. For more information, see [Database-level roles](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles?view=sql-server-ver15) in the SQL Server documentation.
+ Familiarity with using the `mongodump`, `mongorestore`, `mongoexport`, and `mongoimport` utilities to [move data in and out of an Amazon DocumentDB cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/backup_restore-dump_restore_import_export_data.html).
+ [Microsoft SQL Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15), installed and configured.

**Limitations **
+ The cluster size limit in Amazon DocumentDB is 64 TB. For more information, see [Cluster limits](https://docs.aws.amazon.com/documentdb/latest/developerguide/limits.html#limits-cluster) in the Amazon DocumentDB documentation.
+ AWS DMS doesn't support the merging of multiple source tables into a single Amazon DocumentDB collection.
+ If AWS DMS processes any changes from a source table without a primary key, it will ignore large object (LOB) columns in the source table.

## Architecture
<a name="migrate-a-microsoft-sql-server-database-from-amazon-ec2-to-amazon-documentdb-by-using-aws-dms-architecture"></a>

**Source technology stack  **
+ Amazon EC2

**Target technology stack  **
+ Amazon DocumentDB

**Target architecture**

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f186220b-5a94-48b2-840d-f04aedf51651/images/00962b85-8b71-49df-b84a-3adcbc9ad3a3.png)

## Tools
<a name="migrate-a-microsoft-sql-server-database-from-amazon-ec2-to-amazon-documentdb-by-using-aws-dms-tools"></a>
+ [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html) – AWS Database Migration Service (AWS DMS) helps you migrate databases easily and securely.
+ [Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html) – Amazon DocumentDB (with MongoDB compatibility) is a fast, reliable, and fully managed database service.
+ [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) – Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the AWS Cloud.
+ [Microsoft SQL Server](https://docs.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver15) – SQL Server is a relational database management system.
+ [SQL Server Management Studio (SSMS)](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms?view=sql-server-ver15) – SSMS is a tool for managing SQL Server, including accessing, configuring, and administering SQL Server components.

## Epics
<a name="migrate-a-microsoft-sql-server-database-from-amazon-ec2-to-amazon-documentdb-by-using-aws-dms-epics"></a>

### Create and configure a VPC
<a name="create-and-configure-a-vpc"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a VPC. | Sign in to the AWS Management Console and open the Amazon VPC console. Create a virtual private cloud (VPC) with an IPv4 CIDR block range. | System administrator |
| Create security groups and network ACLs. | On the Amazon VPC console, create security groups and network access control lists (network ACLs) for your VPC, according to your requirements. You can also use the default settings for these configurations. For more information about this and other stories, see the "Related resources" section. | System administrator |

### Create and configure the Amazon DocumentDB cluster
<a name="create-and-configure-the-amazon-documentdb-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Create an Amazon DocumentDB cluster. | Open the Amazon DocumentDB console and choose "Clusters." Choose "Create," and create an Amazon DocumentDB cluster with one instance. Important: Make sure you configure this cluster with your VPC’s security groups. | System administrator  |
|  Install the mongo shell. | The mongo shell is a command-line utility that you use to connect to and query your Amazon DocumentDB cluster. To install it, run the "/etc/yum.repos.d/mongodb-org-3.6.repo" command to create the repository file. Run the "sudo yum install -y mongodb-org-shell" command to install the mongo shell. To encrypt data in transit, download the public key for Amazon DocumentDB, and then connect to your Amazon DocumentDB instance. For more information about these steps, see the "Related resources" section. | System administrator  |
| Create a database in the Amazon DocumentDB cluster.  | Run the "use" command with the name of your database to create a database in your Amazon DocumentDB cluster. | System administrator  |

### Create and configure the AWS DMS replication instance
<a name="create-and-configure-the-aws-dms-replication-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the AWS DMS replication instance. | Open the AWS DMS console and choose "Create replication instance." Enter a name and description for your replication task. Choose the instance class, engine version, storage, VPC, Multi-AZ, and make it publicly accessible. Choose the "Advanced" tab to set the network and encryption settings. Specify the maintenance settings, and then choose "Create replication instance." | System administrator  |
| Configure the SQL Server database.  | Log in to Microsoft SQL Server and add an inbound rule for communication between the source endpoint and the AWS DMS replication instance. Use the replication instance’s private IP address as the source. Important: The replication instance and target endpoint should be on the same VPC. Use an alternative source in the security group if the VPCs are different for the source and replication instances. | System administrator  |

### Create and test the source and target endpoints in AWS DMS
<a name="create-and-test-the-source-and-target-endpoints-in-aws-dms"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the source and target database endpoints. | Open the AWS DMS console and choose "Connect source and target database endpoints." Specify the connection information for the source and target databases. If required, choose the "Advanced" tab to set values for "Extra connection attributes." Download and use the certificate bundle in your endpoint configuration. | System administrator  |
| Test the endpoint connection.  | Choose "Run test" to test the connection. Troubleshoot any error messages by verifying the security group settings and the connections to the AWS DMS replication instance from both the source and target database instances. | System administrator  |

### Migrate data
<a name="migrate-data"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the AWS DMS migration task.  | On the AWS DMS console, choose "Tasks," "Create task." Specify the task options, including the source and destination endpoint names, and replication instance names. Under "Migration type" choose "Migrate existing data," and "Replicate data changes only." Choose "Start task." | System administrator  |
| Run the AWS DMS migration task. | Under "Task settings," specify the settings for the table preparation mode, such as "Do nothing," "Drop tables on target," "Truncate," and "Include LOB columns in replication." Set a maximum LOB size that AWS DMS will accept and choose "Enable logging." Leave the "Advanced settings" at their default values and choose "Create task." | System administrator  |
| Monitor the migration. | On the AWS DMS console, choose "Tasks" and choose your migration task. Choose "Task monitoring" to monitor your task. The task stops when the full-load migration is complete and cached changes are applied. | System administrator  |

### Test and verify the migration
<a name="test-and-verify-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Connect to the Amazon DocumentDB cluster by using the mongo shell. | Open the Amazon DocumentDB console, choose your cluster under "Clusters." In the "Connectivity and Security" tab, choose "Connect to this cluster with the mongo shell." | System administrator  |
| Verify the results of your migration. | Run the "use" command with the name of your database and then run the "show collections" command. Run the "db. .count();" command with the name of your database. If the results match your source database, then your migration was successful. | System administrator  |

## Related resources
<a name="migrate-a-microsoft-sql-server-database-from-amazon-ec2-to-amazon-documentdb-by-using-aws-dms-resources"></a>

**Create and configure a VPC **
+ [Create a security group for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#CreatingSecurityGroups)
+ [Create a network ACL](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

** **

**Create and configure the Amazon DocumentDB cluster**
+ [Create an Amazon DocumentDB cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html#cloud9-cluster)
+ [Install the mongo shell for Amazon DocumentDB ](https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html#cloud9-mongoshell)
+ [Connect to your Amazon DocumentDB cluster](https://docs.aws.amazon.com/documentdb/latest/developerguide/get-started-guide.html#cloud9-connectcluster)

** **

**Create and configure the AWS DMS replication instance **
+ [Use public and private replication instances](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.PublicPrivate)

** **

**Create and test the source and target endpoints in AWS DMS **
+ [Use Amazon DocumentDB as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/target.docdb.html)
+ [Use a SQL Server database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html)
+ [Use AWS DMS endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html)

** **

**Migrate data **
+ [Migrate to Amazon DocumentDB](https://docs.aws.amazon.com/documentdb/latest/developerguide/docdb-migration.html)

** **

**Other resources**
+ [Limitations on using SQL Server as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.Limitations)
+ [How to use Amazon DocumentDB to build and manage applications at scale](https://aws.amazon.com/blogs/database/how-to-use-amazon-documentdb-with-mongodb-compatibility-to-build-and-manage-applications-at-scale/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
