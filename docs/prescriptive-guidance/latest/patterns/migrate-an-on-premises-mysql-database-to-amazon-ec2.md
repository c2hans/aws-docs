---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-mysql-database-to-amazon-ec2.html
---

# Migrate an on-premises MySQL database to Amazon EC2
<a name="migrate-an-on-premises-mysql-database-to-amazon-ec2"></a>

*Lorenzo Mota, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-mysql-database-to-amazon-ec2-summary"></a>

This pattern provides guidance for migrating an on-premises MySQL database to a MySQL database on an Amazon Elastic Compute Cloud (Amazon EC2) instance. The pattern discusses the use of AWS Database Migration Service (AWS DMS) or native MySQL tools such as **mysqldump** for the migration. It focuses on full database migration to a MySQL DB instance.

The pattern is primarily for DBAs and solutions architects. It can be used in small or large projects, in a testing or final migration phase. We recommend that you run at least one testing cycle before you use this pattern in a production environment.

## Prerequisites and limitations
<a name="migrate-an-on-premises-mysql-database-to-amazon-ec2-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A MySQL source database in an on-premises data center

**Product versions**
+ MySQL version 5.5 and later
+ A target operating system supported by Amazon EC2; see [Amazon EC2 FAQs](https://aws.amazon.com/ec2/faqs/)

## Architecture
<a name="migrate-an-on-premises-mysql-database-to-amazon-ec2-architecture"></a>

**Source  technology stack **
+ An on-premises MySQL database

**Target  technology stack **
+ A MySQL database instance on Amazon EC2

**AWS data migration methods**
+ AWS DMS
+ Native MySQL tools such as [mysqldump](https://dev.mysql.com/doc/refman/en/mysqldump.html), or third-party tools such as [Percona XtraBackup](https://www.percona.com/mysql/software/percona-xtrabackup)

**Target architecture**

The following diagram illustrates the target Amazon EC2 implementation after cutover.

![A MySQL DB instance on Amazon EC2 with replication to a standby MySQL DB instance.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d22b3e25-4d3b-4bd7-ad07-501748d67752/images/34cab6f9-9107-4c3b-98ec-a6d7fa9f298a.png)

**AWS data migration architecture**

*Using AWS DMS:*

The following diagram illustrates the data migration workflow based on AWS DMS for sending full and incremental changes to the target MySQL database until cutover. The network connection from on premises to AWS depends on the requirements of the SQL client and is outside the scope of this pattern.

![Using AWS DMS to send data to a target MySQL DB on Amazon EC2.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d22b3e25-4d3b-4bd7-ad07-501748d67752/images/c906c45d-fac5-4bb9-b8c8-55e2f9f05fd8.png)

*Using other MySQL tools:*

The following diagram illustrates the data migration workflow based on using MySQL tools to generate export dump files from the on-premises database. These files are moved to Amazon Simple Storage Service (Amazon S3) and imported into the target MySQL database before cutover. The network connection from on premises to AWS depends on the requirements of the SQL client and is outside the scope of this pattern.

![Using native MySQL tools to send data to a target MySQL DB on Amazon EC2.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d22b3e25-4d3b-4bd7-ad07-501748d67752/images/18e88877-7879-4a99-b985-25c56bf7c35f.png)

Notes:
+ Depending on down time considerations and the size of the database for the final cutover, you can use AWS DMS or another change data capture (CDC) tool to minimize the cutover time. When you use a CDC tool such as AWS DMS, you can migrate to the target database in minutes.
+ An offline strategy with **mysqldump** can suffice if the size of the database and network latency allow for a short cutover migration window. (We recommend that you perform testing to get an approximate time.)
+ Usually a CDC strategy through AWS DMS requires more monitoring and complexity than an offline option.

## Tools
<a name="migrate-an-on-premises-mysql-database-to-amazon-ec2-tools"></a>

**AWS services**
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) supports several source and target databases. For information about MySQL source and target databases supported by AWS DMS, see [Using a MySQL-compatible database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html) and [Using a MySQL-compatible database as a target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html). If your source database isn't supported by AWS DMS, you must choose another method to migrate your data.

**Other tools**
+ [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) is a MySQL utility that creates a dump file from a MySQL database for backup or migration purposes.
+ [Percona XtraBackup](https://www.percona.com/mysql/software/percona-xtrabackup) is an open source utility for performing non-blocking backups on MySQL databases.

## Epics
<a name="migrate-an-on-premises-mysql-database-to-amazon-ec2-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the database versions. | Validate the versions of the source and target databases. For information about MySQL versions supported by AWS DMS, see [Sources for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Sources.html) and [Targets for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Targets.html) in the AWS DMS documentation. | DBA |
| Identify the target operating system. | Determine the version of the target operating system. For a list of target operating systems supported by Amazon EC2, see [Amazon EC2 FAQs](https://aws.amazon.com/ec2/faqs/). | DBA, Systems administrator |
| Identify hardware requirements. | Determine the hardware requirements for the [target server instance](https://aws.amazon.com/rds/instance-types/) based on the MySQL compatibility list and capacity requirements. | DBA, Systems administrator |
| Identify storage requirements. | Determine the storage type and capacity for the target database. | DBA, Systems administrator |
| Identify network requirements. | Determine networking requirements such as latency and bandwidth. | DBA, Systems administrator |
| Choose the target instance type. | Choose the [target instance type](https://aws.amazon.com/rds/instance-types/) based on capacity, storage features, and network features. | DBA, Systems administrator |
| Identify security requirements. | Determine the network or host access security requirements for the source and target databases. | DBA, Systems administrator |
| Identify users. | Determine the list of operating system users for the MySQL software installation. For more information, see the [MySQL documentation](https://dev.mysql.com/doc/mysql-security-excerpt/en/access-control.html). | DBA, Systems administrator |
| Determine a backup strategy. |  | DBA |
| Determine availability requirements. |  | DBA |
| Identify the application migration or switchover strategy. |  | DBA, Systems administrator |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC) and subnets. | Configure route tables, internet gateway, NAT gateways, and subnets. For more information, see [VPC configuration options](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc-options.html) in the Amazon VPC documentation. | Systems administrator |
| Create security groups and network access control lists (ACLs). | Configure ports (default for MySQL is 3306) and CIDR ranges or specific IPs depending on your requirements. | Systems administrator |
| Configure and start an EC2 instance. | For instructions, see [Launch an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html) in the Amazon EC2 documentation. | Systems administrator |

### Install MySQL software
<a name="install-mysql-software"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create users and groups. | Create the operating system users and groups who need access to the server and database. For more information, see [Access Control and Account Management](https://dev.mysql.com/doc/refman/en/access-control.html) in the MySQL documentation. | DBA, Systems administrator |
| Download MySQL. | Download the MySQL software. For instructions and binaries, see [Installing MySQL](https://dev.mysql.com/doc/refman/en/installing.html) in the MySQL documentation. | DBA, Systems administrator |
| Install MySQL on the EC2 instance and configure the server. | Connect to your EC2 instance and install the MySQL software. For more information, see [Connect to your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html) in the Amazon EC2 documentation. | DBA, Systems administrator |

### Migrate data – option 1
<a name="migrate-data-option-1"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate data with native MySQL or third-party tools. | This option uses native MySQL tools or third-party tools to migrate database objects and data. For instructions, see the documentation for [mysqldump](https://dev.mysql.com/doc/refman/en/mysqldump.html) or [Percona XtraBackup](https://docs.percona.com/percona-xtrabackup/2.4/index.html) (for physical migration). For more information about using these tools, see the AWS blog post [Migration options for MySQL to Amazon RDS for MySQL or Amazon Aurora MySQL](https://aws.amazon.com/blogs/database/migration-options-for-mysql-to-amazon-rds-for-mysql-or-amazon-aurora-mysql/). | DBA |

### Migrate data – option 2
<a name="migrate-data-option-2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate data with AWS DMS. | For more information, see [High-level view of AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.HighLevelView.html) in the AWS DMS documentation. | DBA |

### Prepare for cutover
<a name="prepare-for-cutover"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Gather object counts. | Gather object counts from source database and new target databases. Fix any discrepancies in the target database. | DBA |
| Check dependencies. | Confirm that dependencies (links) to and from other databases are still valid and work correctly. | DBA |
| Test. | If this is a testing cycle, perform query testing, gather metrics, and fix any issues. | DBA |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Move clients. | Switch the application clients over to the new infrastructure. | DBA, App owner, Systems administrator |
| Provide support. | Provide support during functional application testing. | DBA |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down resources. | Shut down the AWS DMS replication instance and other temporary AWS resources. | DBA, Systems administrator |
| Review and project documents. | Review and validate the project documents. | DBA, App owner, Systems administrator |
| Collect metrics. | Collect metrics such as time to migrate, percentage of manual changes compared with tool-aided changes, and cost savings. | DBA, App owner, Systems administrator |
| Close out project. | Close out the migration project and provide feedback. | DBA, App owner, Systems administrator |
| Decommission source database. | Decommission the on-premises MySQL database. | DBA, Systems administrator |

## Related resources
<a name="migrate-an-on-premises-mysql-database-to-amazon-ec2-resources"></a>

**References**
+ [Amazon EC2 documentation](https://docs.aws.amazon.com/ec2/)
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/)
+ [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/)
+ [AWS DMS Step-by-Step Walkthroughs](https://docs.aws.amazon.com/dms/latest/sbs/DMS-SBS-Welcome.html)
+ [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)
+ [Percona XtraBackup](https://www.percona.com/mysql/software/percona-xtrabackup)

**Tutorials and videos**
+ [Getting Started with AWS DMS](https://aws.amazon.com/dms/getting-started/)
+ [Introduction to Amazon EC2 – Elastic Cloud Server & Hosting with AWS](https://www.youtube.com/watch?v=TsRBftzZsQo) (video)
