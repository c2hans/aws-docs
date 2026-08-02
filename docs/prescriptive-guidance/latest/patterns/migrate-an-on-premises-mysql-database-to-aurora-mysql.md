---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-mysql-database-to-aurora-mysql.html
---

# Migrate an on-premises MySQL database to Aurora MySQL
<a name="migrate-an-on-premises-mysql-database-to-aurora-mysql"></a>

*Igor Obradovic, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-mysql-database-to-aurora-mysql-summary"></a>

This pattern explains how to migrate an on-premises MySQL source database to Amazon Aurora MySQL-Compatible Edition. It describes two options for migration: using AWS Database Migration Service (AWS DMS) or using native MySQL tools such as **mysqldbcopy** and **mysqldump**.

## Prerequisites and limitations
<a name="migrate-an-on-premises-mysql-database-to-aurora-mysql-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A source MySQL database in an on-premises data center

**Limitations**
+ Database size limit: 128 TB

**Product versions**
+ MySQL version 8.0 (Aurora MySQL version 3) is available under standard support.
+ MySQL version 5.7 (Aurora MySQL version 2) is available under extended support, for an additional cost.

For the latest list of supported versions, see [Amazon Aurora versions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.release-calendars.html) in the AWS documentation. If you're using AWS DMS, see also [Using a MySQL-Compatible Database as a Target for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html) for MySQL versions supported by AWS DMS.

## Architecture
<a name="migrate-an-on-premises-mysql-database-to-aurora-mysql-architecture"></a>

**Source technology stack**
+ An on-premises MySQL database

**Target technology stack**
+ Amazon Aurora MySQL-Compatible Edition

**Target architecture**

Aurora data is stored in a cluster volume, which is a single, virtual volume that uses solid state drives (SSDs). A cluster volume consists of copies of the data across three Availability Zones in a single AWS Region. Because the data is automatically replicated across Availability Zones, it is highly durable with less possibility of data loss.

Aurora automatically divides your database volume into 10 GB segments spread across many disks. Each 10 GB chunk of your database volume is replicated six ways, across three Availability Zones. The following diagram illustrates the relationship between the cluster volume, the writer DB instance, and reader DB instances in an Aurora DB cluster, and the separation of compute capacity and storage. For more information about this architecture, see the [Aurora documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html) and [FAQ](https://aws.amazon.com/rds/aurora/faqs/#product-faqs).

![Aurora MySQL DB instances and shared storage volume on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/22729803-e4ff-45a2-ab5b-8ba2445e5e21/images/0d7d8ebd-e0f2-4bcf-b296-8bdfb2f12b64.png)

**Data migration architecture**

*Using AWS DMS:*

The following diagram illustrates the migration of an on-premises MySQL database to an Aurora MySQL-Compatible cluster in the AWS Cloud, using AWS DMS.

![Migrating an on-premises MySQL database to Aurora MySQL by using AWS DMS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/22729803-e4ff-45a2-ab5b-8ba2445e5e21/images/e5d72ebd-d157-45d7-8844-d1011f1646c0.png)

*Using native MySQL tools:*

The following diagram illustrates the migration of an on-premises MySQL database to an Aurora MySQL-Compatible cluster in the AWS Cloud, using native MySQL tools such as **mysqldbcopy** and **mysqldump**.

![Migrating an on-premises MySQL database to Aurora MySQL by using mysqldbcopy and mysqldump.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/22729803-e4ff-45a2-ab5b-8ba2445e5e21/images/26258752-24f6-4241-a49f-59c15e946314.png)

## Tools
<a name="migrate-an-on-premises-mysql-database-to-aurora-mysql-tools"></a>
+ [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) supports several source and target database engines. For information about MySQL source and target databases supported by AWS DMS, see [Migrating MySQL-Compatible Databases to AWS](https://docs.aws.amazon.com/dms/latest/sbs/CHAP_MySQL.html). We recommend that you use the latest version of AWS DMS for the most comprehensive version and feature support.
+ [mysqldbcopy](https://manpages.ubuntu.com/manpages/focal/man1/mysqldbcopy.1.html) is a MySQL utility that copies a MySQL database on a single server or between servers.
+ [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html) is a MySQL utility that creates a dump file from a MySQL database for backup or migration purposes.

## Epics
<a name="migrate-an-on-premises-mysql-database-to-aurora-mysql-epics"></a>

### Plan the migration
<a name="plan-the-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate the version and engine. | Validate the database version and engine for the source and target databases. | DBA |
| Identify hardware requirements. | Identify hardware requirements for the target server instance. | DBA, Systems administrator |
| Identify storage requirements. | Identify storage requirements (storage type and capacity). | DBA, Systems administrator |
| Choose the instance type. | Choose the proper instance type based on your compute, storage, and network requirements. | DBA, Systems administrator |
| Determine network access security requirements. | Identify the network access security requirements for the source and target databases. | DBA, Systems administrator |
| Determine strategy. | Identify the application migration strategy. | DBA, App owner, Systems administrator |

### Configure the infrastructure
<a name="configure-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a virtual private cloud (VPC). | For instructions, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) in the Amazon Virtual Private Cloud (Amazon VPC) documentation. | Systems administrator |
| Create security groups. | For instructions, see [Create a security group for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/creating-security-groups.html) in the Amazon VPC documentation. | Systems administrator |
| Configure and start an Aurora MySQL-Compatible DB cluster in your AWS account. | For instructions, see [Creating an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html) in the Aurora documentation. | Systems administrator |

### Migrate data - option 1
<a name="migrate-data---option-1"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Use native MySQL tools or third-party tools to migrate database objects and data. | For instructions, see the documentation for MySQL tools such as [mysqldbcopy](https://manpages.ubuntu.com/manpages/focal/man1/mysqldbcopy.1.html) and [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html). | DBA |

### Migrate data - option 2
<a name="migrate-data---option-2"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate data with AWS DMS. | For instructions, see [Using a MySQL-compatible database as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html) and [Using a MySQL-compatible database as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html) in the AWS DMS documentation. | DBA |

### Migrate the application
<a name="migrate-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Follow the strategy. | Follow the application migration strategy. | DBA, App owner, Systems administrator |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Switch application clients. | Switch the application clients over to connect to the new Aurora cluster endpoint. | DBA, App owner, Systems administrator |

### Close the project
<a name="close-the-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Shut down resources. | Shut down temporary AWS resources. | DBA, Systems administrator |
| Review documentation. | Review and validate the project documents. | DBA, App owner, Systems administrator |
| Collect metrics. | Gather metrics around time to migrate, percentage of manual steps versus tool usage, cost savings, and so on. | DBA, App owner, Systems administrator |
| Complete migration project. | Close out the project and provide feedback. | App owner, DBA, Systems administrator |

## Related resources
<a name="migrate-an-on-premises-mysql-database-to-aurora-mysql-resources"></a>

**References**
+ [Migrating data to Amazon Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.html)
+ [AWS DMS website](https://aws.amazon.com/dms/)
+ [AWS DMS documentation](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
+ [Amazon Aurora Pricing](https://aws.amazon.com/rds/aurora/pricing/)
+ [Creating and connecting to an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.Aurora.html)
+ [Amazon VPC and Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html)
+ [Amazon Aurora documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

**Tutorials and videos**
+ [Getting Started with AWS DMS](https://aws.amazon.com/dms/getting-started/)
+ [Getting Started with Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.html)
