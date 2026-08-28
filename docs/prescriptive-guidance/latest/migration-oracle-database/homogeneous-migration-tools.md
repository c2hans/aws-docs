---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/homogeneous-migration-tools.html
---

# Tools for homogeneous database migrations
<a name="homogeneous-migration-tools"></a>

A number of tools and technologies are available for data migration. You can perform the migration in a single phase or in multiple phases, based on your database size, consistency, the bandwidth of the network connection between your on-premises environment and AWS, and the allowed time for database migration. The following chart provides a list of tools and information to help you choose the option that best meets your needs.

|
|
| Migration tool | Database size | Supports | Recommended for |
| --- |--- |--- |--- |
| [Oracle SQL Developer](#oracle-sql-developer) (Database Copy feature) | Up to 200 MB | Amazon RDS  Amazon EC2 | Small databases with any number of objects. |
| [Oracle SQL\*Loader](#oracle-sql-loader) | Up to 10 GB | Amazon RDS  Amazon EC2 | Small to medium-size databases with a limited number of objects. |
| [Oracle Export and Import Utilities](#oracle-export-import) | Up to 10 GB  | Amazon RDS  Amazon EC2  | Small to medium-size databases with a large number of objects. |
| [Oracle Data Pump](#oracle-data-pump) | Up to 20 TB | Amazon RDS  Amazon EC2 | Preferred method for any database that's 10 GB – 20 TB in size. |
| [AWS DMS](#homogeneous-tools-dms) | Any size | Amazon RDS<br />Amazon EC2<br />  | Minimal downtime migration. Database size is limited by bandwidth. You can use AWS DMS with Oracle Data Pump for large database migrations. |
| [Oracle GoldenGate](#oracle-goldengate) | Any size | Amazon RDS  Amazon EC2  VMware Cloud on AWS<br />  | Minimal downtime migration. Used with Oracle Data Pump for large database migrations. |
| [Oracle Data Guard](#oracle-data-guard) | Any size | Amazon RDS Custom  Amazon EC2  VMware Cloud on AWS | Minimal downtime migration. Used with Oracle RMAN to replicate changes after initial data transfer. |
| [Oracle RMAN](#oracle-rman) | Any size <br />  | Amazon RDS Custom  Amazon EC2<br />VMware Cloud on AWS  | Databases over 2 TB, or if database backup is already in Amazon Simple Storage Service (Amazon S3).  |
| AWS Application Migration Service | Any size | Amazon EC2 | Fast replication with minimal downtime during cutover. For more information, see the [Application Migration Service documentation](https://docs.aws.amazon.com/mgn/index.html). |
| [VMware HCX](#vmware-hcx) | Any size | VMware Cloud on AWS | HCX vMotion provides online or offline migration of a single virtual machine (VM) at a time with no downtime.  |

The following subsections provide more information about each tool.

## Oracle SQL Developer
<a name="oracle-sql-developer"></a>

[Oracle SQL Developer](https://docs.oracle.com/en/database/oracle/sql-developer/index.html) is a free GUI tool from Oracle for data manipulation, administration, development, and management. This Java-based tool is available for Microsoft Windows, Linux, or macOS. You can use the Database Copy feature to migrate small databases to AWS, where the total size of your data is under 200 MB. The data transfer between source and target database is done directly over the network. To use this option, you will need a reliable network connection between the source and target database. In addition, keep in mind that this method does not encrypt data during transfer.

Oracle SQL Developer supports both Amazon RDS for Oracle and Oracle databases on Amazon EC2.

## Oracle SQL\*Loader
<a name="oracle-sql-loader"></a>

[Oracle SQL\*Loader](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-sql-loader.html) is a bulk data load utility available from Oracle for loading data from external files into a database. SQL\*Loader is included with the full Oracle Database client binaries. You can use SQL\*Loader for small to medium-size databases under 10 GB that contain a limited number of objects. Because this is a schema-based method, it involves exporting specific schemas individually from the source database and loading them into the target database. If you have multiple schemas in a database, you have to repeat the process for each schema.

Oracle SQL\*Loader supports both Amazon RDS for Oracle and Oracle databases on Amazon EC2.

## Oracle Export and Import
<a name="oracle-export-import"></a>

[Oracle Export and Import utilities](https://docs.oracle.com/cd/B28359_01/server.111/b28300/preup.htm#BABFHFIJ) help you migrate databases that are smaller than 10 GB and don't include binary float and double data types. The import process creates the schema objects, so you don't have to run a script to create them beforehand. This makes the process well suited for databases that have a large number of small tables.

You can use this tool for both Amazon RDS for Oracle and Oracle databases on Amazon EC2.

## Oracle Data Pump
<a name="oracle-data-pump"></a>

[Oracle Data Pump](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump.html) is an enhanced version of Oracle Export and Import. This utility is used to export and import data and metadata from or to Oracle databases. You can run Data Pump export/import on an entire database, selective schemas, tablespaces, or database objects. Data Pump is the recommended tool for migrating data to AWS, for large databases that range from 10 GB to 20 TB in size. It allows a high degree of parallelism, flexible data extraction options, and scalable operations, which enable high-speed movement of data and metadata from source database to target database. Oracle Data Pump also supports encryption and compression when exporting your data to data dump files.

You can use this tool for both Amazon RDS for Oracle and Oracle databases on Amazon EC2. You can also use Oracle Data Pump with AWS DMS and Oracle GoldenGate to handle the initial data transfer for large databases.

For Amazon RDS for Oracle, after the data is exported into dump files using the Oracle Data Pump export utility, the Oracle Data Pump import utility requires the data files to be available in the database server instance to import them into the database. You can't access the file system in the Amazon RDS DB instance directly, so you will need to transfer the dump files to Amazon RDS using one of these options:
+ Use a database link between the two databases. This process uses Oracle Data Pump and the Oracle [DBMS\_FILE\_TRANSFER](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_FILE_TRANSFER.html) package. It creates a database link between the source (on-premises) Oracle database and the target Amazon RDS for Oracle database. This option requires higher bandwidth connectivity between source and target databases; we recommend that you use [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html). This option is recommended only for small databases.  For more information, see [Importing data with Oracle Data Pump and a database link](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.DataPump.html#Oracle.Procedural.Importing.DataPump.DBLink) in the Amazon RDS documentation.
+ Use an Amazon S3 bucket. Amazon RDS for Oracle supports Amazon S3 integration. This option is recommended when you have large data dump files and your database size is in terabytes. You can then copy the data dump files from on premises to your S3 bucket by using AWS Direct Connect (if your data size is from 10 GB to 5 TB) or AWS Snowball (if your data size is more than 5 TB) depending on the required migration time for your database.

After the data pump file is uploaded to Amazon S3, you can download it to the DATA\_PUMP\_DIR directory on the target Amazon RDS for Oracle DB instance, and then import the data into the DB instance. For more information, see [Importing data with Oracle Data Pump and an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.DataPump.html#Oracle.Procedural.Importing.DataPump.S3) in the Amazon RDS documentation.

With Oracle Data Pump, you can migrate larger databases in phases, on a schema-by-schema basis. You can migrate to a different version of the Oracle Database software and also migrate to platforms that have different hardware and software configurations.

## AWS DMS
<a name="homogeneous-tools-dms"></a>

[AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/) is a managed service that helps you move data to and from AWS easily and securely. AWS DMS supports most commercial and open-source databases, and facilitates both homogeneous and heterogeneous migrations. AWS DMS offers both one-time full database copy and change data capture (CDC) technology to keep the source and target databases in sync and to minimize downtime during a migration.

AWS DMS can perform a full copy of your Oracle database schema for small (10-20 GB) to medium (100-200 GB) sized databases. For very large databases, you can migrate the data to Amazon RDS or Amazon EC2 by using Oracle Data Pump, and then use the AWS DMS CDC feature for ongoing replication with minimal downtime. When the data is synchronized, you can cut over to the target database.

The following diagram shows how you can use Oracle Data Pump and AWS DMS together to migrate an on-premises database to Amazon RDS for Oracle with minimal downtime. The Oracle Data Pump export utility exports the schema to database dump files, and then transfers those files to Amazon S3 by using either AWS Direct Connect or AWS Snowball (depending on the size of the database, network bandwidth, and allowed migration time). After the dump files are loaded into Amazon S3, you can upload the files over to an Amazon RDS for Oracle DB instance. The Oracle Data Pump import utility then imports the data to Amazon RDS for Oracle, and AWS DMS CDC replicates all the changes from the source database to the target Amazon RDS for Oracle database.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/images/guide-img/b6e66b32-33d8-4097-909d-dcc9b3b4a45a/images/5d7029bf-8a06-4d78-ae7b-22e54c719b00.png)

** **

For more information about using AWS DMS to migrate Oracle source databases, see [Using an Oracle database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html) in the AWS documentation.

## Oracle GoldenGate
<a name="oracle-goldengate"></a>

[Oracle GoldenGate](https://docs.oracle.com/en/middleware/goldengate/index.html) is a tool for replicating data between a source database and one or more destination databases with minimal downtime. You can use it to build high availability architectures, and to perform real-time data integration, transactional change data capture, replication in heterogeneous environments, and continuous data replication.

You can run Oracle GoldenGate from your on-premises server in your source environment. However, we recommend that you install and run this tool from an EC2 instance, which serves as the GoldenGate hub, on AWS for better performance. You can have multiple GoldenGate hubs, especially if you are migrating data from one source database to multiple destinations. You can use GoldenGate with Amazon RDS for Active-Active database replication, zero-downtime migration and upgrades, disaster recovery, data protection, and in-region and cross-region replication. For details, see [Using Oracle GoldenGate with Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.html) in the AWS documentation.

The following diagram shows how to use Oracle Data Pump and Oracle GoldenGate together to migrate an on-premises Oracle database to Amazon RDS for Oracle.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/images/guide-img/b6e66b32-33d8-4097-909d-dcc9b3b4a45a/images/9ccaa50e-cc94-41d0-b8e4-d413de7f1145.png)

Oracle GoldenGate requires a separate license from Oracle.

Oracle GoldenGate supports both Amazon RDS for Oracle and Oracle databases running on Amazon EC2 or VMware Cloud on AWS.

## Oracle Data Guard
<a name="oracle-data-guard"></a>

[Oracle Data Guard](https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/introduction-to-oracle-data-guard-concepts.html) provides a set of services for creating, maintaining, monitoring and managing Oracle standby databases. You can migrate your entire Oracle database from on premises to Amazon EC2 with minimal downtime by using Oracle Recovery Manager (RMAN) and Oracle Data Guard. With RMAN, you restore your primary database to the target standby database on Amazon EC2, using either backup/restore or the duplicate database method. You then configure the target database as a physical standby database with Oracle Data Guard, allowing all the transaction/redo data changes from the primary on-premises database to the standby database.

When the primary on-premises Oracle database is in sync with the target standby database on the EC2 instance, you can switch over to the target database, which will convert it to a read-write database. You can then point your application connections to the new primary database. With this option, you can achieve minimum downtime and get an exact physical copy of your database on AWS. The migration is illustrated in the following diagram.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/images/guide-img/b6e66b32-33d8-4097-909d-dcc9b3b4a45a/images/7205accb-61ff-464b-9025-252aa7739b10.png)

Oracle Data Guard supports Oracle databases running on Amazon EC2, Amazon RDS Custom, and VMware Cloud on AWS.

## Oracle RMAN
<a name="oracle-rman"></a>

[Oracle Recovery Manager (RMAN)](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/getting-started-rman.html) is a tool provided by Oracle for performing and managing Oracle database backups and restorations. You can use RMAN to back up your Oracle database from on premises or from your data center, and restore it to an Oracle database on an EC2 instance. Use this method if you are planning to move your entire database to a self-managed Oracle database on an EC2 instance. The database can be of any size, and you can use parallelism, compression, and encryption in your backups.

You can place the Oracle RMAN backup of your on-premises Oracle database directly in an S3 bucket by using the Oracle Secure Backup (OSB) Cloud module, AWS Storage Gateway, or AWS DataSync. You can then use an AWS Identity and Access Management (IAM) role to give the S3 bucket access to your target Oracle database on an EC2 instance, and restore the database by using the RMAN backup files. You can take incremental backups from your on-premises Oracle database and apply them to the target Oracle database on the EC2 instance until the on-premises and target databases are in sync. You can then perform the switchover at a convenient time.

Oracle RMAN supports Amazon EC2, Amazon RDS Custom, and VMware Cloud on AWS migrations. It's the recommended approach when you can allow enough downtime for migrating your data to AWS.

## VMware HCX
<a name="vmware-hcx"></a>

[VMware Hybrid Cloud Extension (HCX](https://cloud.vmware.com/vmware-hcx)) enables you to migrate your on-premises Oracle databases to AWS without having to retrofit your VMware infrastructure. It includes several migration methods that are detailed in the blog posts [How to Migrate Oracle Workloads to VMware Cloud on AWS](https://aws.amazon.com/blogs/apn/how-to-migrate-oracle-workloads-to-vmware-cloud-on-aws/) and [Migrating Workloads to VMware Cloud on AWS with Hybrid Cloud Extension (HCX)](https://aws.amazon.com/blogs/apn/migrating-workloads-to-vmware-cloud-on-aws-with-hybrid-cloud-extension-hcx/). One of these methods, HCX vMotion, provides a live migration of a single VM with no downtime and high availability.

HCX is available free of charge to VMware Cloud on AWS customers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
