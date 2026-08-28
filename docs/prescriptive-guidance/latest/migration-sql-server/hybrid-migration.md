---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/hybrid-migration.html
---

# Hybrid migration scenarios for SQL Server
<a name="hybrid-migration"></a>

You can also run SQL Server workloads in a hybrid environment that includes AWS. For example, you might already be running SQL Server in your on-premises or co-located data center but want to use the AWS Cloud to enhance your architecture to provide a high availability or disaster recovery solution. You can also use hybrid solutions to store long-term SQL Server backups on AWS, to roll back your migration, in case of issues, or to run a secondary replica using SQL Server Always On availability groups in the AWS Cloud.  SQL Server has several replication technologies that offer high availability and disaster recovery solutions.

## Backing up your SQL Server databases to the AWS Cloud
<a name="hybrid-backup"></a>

Amazon Simple Storage Service (Amazon S3) enables you to take advantage of the flexibility and pricing of cloud storage. It gives you the ability to back up your SQL Server databases to a secure, highly available, highly durable, reliable storage system. You can securely store your SQL Server backups in Amazon S3. You can also use Amazon S3 Lifecycle policies to store your backups for the long term. Amazon S3 allows you to store large amounts of data at a very low cost. You can also use [AWS DataSync](https://aws.amazon.com/datasync/) to transfer backup files to Amazon S3.

You can use AWS Storage Gateway to store your on-premises SQL Server backups and archive data on Amazon S3 or Amazon S3 Glacier. You can create cached storage volumes and mount them as Internet Small Computer System Interface (iSCSI) devices from your on-premises backup application servers. All data is securely transferred to AWS over SSL and stored in encrypted format in Amazon S3. Using gateway cached volumes saves the upfront cost of maintaining and scaling costly storage hardware on premises. If you want to keep your primary data or backups on premises, you can use gateway stored volumes to keep this data locally, and back up the data off-site to Amazon S3.

## Extending high availability and disaster recovery solutions
<a name="hybrid-extend-ha-dr"></a>

You can extend your existing on-premises high availability practices and provide a disaster recovery solution in AWS by using the native log shipping feature in SQL Server. You can transfer your SQL Server transaction logs from your on-premises or co-located data centers to a SQL Server instance that is running on an Amazon EC2 instance or an Amazon RDS for SQL Server DB instance in a virtual private cloud (VPC). You can transmit this data securely over a dedicated network connection by using AWS Direct Connect, or transmit it over a secure VPN tunnel. The transaction log backups are sent to the Amazon EC2 instance, and they are applied to secondary database instances.

You can use the AWS Cloud to provide a higher level of high availability and disaster recovery by using SQL Server Always On availability groups between your on-premises data center and Amazon EC2. This can be done by extending your data center into a VPC on AWS by using a dedicated network connection like AWS Direct Connect, or by setting secure VPN tunnels between these two environments.

Here are a few things to consider when planning a hybrid implementation of SQL Server Always On availability groups:
+ Establish secure, reliable, and consistent network connections between your on-premises environment and AWS through AWS Direct Connect or VPN.
+ Create a VPC by using the Amazon Virtual Private Cloud (Amazon VPC) service. Use Amazon VPC route tables and security groups to enable the appropriate communications between the two environments.
+ Extend Active Directory domains into the VPC by deploying domain controllers as Amazon EC2 instances, or by using AWS Directory Service for Microsoft Active Directory. For Amazon RDS for SQL Server, you can also use AWS Managed Microsoft AD. For more information, see the Amazon RDS[ documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.html).

## AWS Storage Gateway
<a name="hybrid-storage-gateway"></a>

AWS Storage Gateway enables you to store and retrieve files by using a Server Message Block (SMB) share for Windows. You can join the storage gateway to your on-premises Active Directory domain. By having your SQL Server database and storage gateway in the same domain, you can take the backups directly to the SMB network share instead of storing them locally and then uploading them to the network share. The storage gateway is configured to use an Amazon S3 bucket, so all your backups will be available in the Amazon S3 bucket on AWS. You can restore your database by downloading the backup files to SQL Server on an Amazon EC2 instance, or restore the database directly to Amazon RDS.

The following diagram shows how to store and access backups by using AWS Storage Gateway and Amazon S3. For more information, see the [Storage Gateway documentation](https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html).

![Hybrid migration with &AWSSG; and &S3;](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/images/guide-img/aa3b9357-4901-48ca-9fc9-a997d21ade3e/images/5708a19d-d68b-4b34-8159-4113ae150eee.png)

## Using AWS DMS and AWS SCT
<a name="hybrid-dms-sct"></a>

You can use AWS DMS in hybrid SQL Server environments, to migrate data from your on-premises database to the cloud, or the other way around.

You can migrate your SQL Server database to MySQL or PostgreSQL by using AWS DMS with AWS SCT. For migration steps, see the [AWS SCT documentation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_GettingStarted.html). Before you migrate your data, you can run a [migration assessment report](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html#CHAP_UserInterface.AssessmentReport) that flags any additional manual work that might be required.

You can also use AWS DMS for ongoing replication (change data capture or CDC). For more information, see [Using ongoing replication (CDC) from a SQL Server source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.CDC) in the AWS DMS documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
