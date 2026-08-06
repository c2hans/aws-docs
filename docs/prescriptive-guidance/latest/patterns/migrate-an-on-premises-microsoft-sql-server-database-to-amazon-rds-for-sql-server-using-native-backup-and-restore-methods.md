---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-native-backup-and-restore-methods.html
---

# Migrate an on-premises Microsoft SQL Server database to Amazon RDS for SQL Server using native backup and restore methods
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-native-backup-and-restore-methods"></a>

*Tirumala Dasari, David Queiroz, and Vishal Singh, Amazon Web Services*

## Summary
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-native-backup-and-restore-methods-summary"></a>

This pattern describes how to migrate an on-premises Microsoft SQL Server database to an Amazon Relational Database Service (Amazon RDS) for SQL Server DB instance (homogeneous migration). The migration process is based on native SQL Server backup and restore methods. It uses SQL Server Management Studio (SSMS) to create a database backup file, and an Amazon Simple Storage Service (Amazon S3) bucket to store the backup file before restoring it in Amazon RDS for SQL Server.

## Prerequisites and limitations
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-native-backup-and-restore-methods-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ AWS Identity and Access Management (IAM) role policies to access the S3 bucket and the Amazon RDS for SQL Server DB instance.

**Limitations**
+ The process described in this pattern migrates only the database. SQL logins or database users, including any SQL Server Agent jobs, aren’t migrated because they require additional steps.

**Product versions**
+ SQL Server 2012-2017. For the latest list of supported versions and features, see [Microsoft SQL Server on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html#SQLServer.Concepts.General.FeatureSupport) in the AWS documentation.

## Architecture
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-native-backup-and-restore-methods-architecture"></a>

**Source technology stack**
+ An on-premises Microsoft SQL Server database

**Target technology stack**
+ Amazon RDS for SQL Server DB instance

**Data migration**** architecture**

![Architecture to migrate an on-premises SQL Server DB to an Amazon RDS for SQL Server DB instance.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c2dcd6ab-deb1-4d5e-b3c5-3bf48c02ca4e/images/29f90473-6dd4-4574-bfbd-5c6a0481c40e.png)

## Tools
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-native-backup-and-restore-methods-tools"></a>
+ Microsoft SQL Server Management Studio (SSMS) is an integrated environment for managing SQL Server infrastructure. It provides a user interface and a group of tools with rich script editors that interact with SQL Server.

## Epics
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-native-backup-and-restore-methods-epics"></a>

### Create an Amazon RDS for SQL Server DB instance
<a name="create-an-amazon-rds-for-sql-server-db-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Select SQL Server as the database engine in Amazon RDS for SQL Server. |  | DBA |
| Choose the SQL Server Express Edition. |  | DBA |
| Specify database details. | For more information about creating a DB instance, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html). | DBA, App owner |

### Create a backup file from the on-premises SQL Server database
<a name="create-a-backup-file-from-the-on-premises-sql-server-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect to the on-premises SQL Server database through SSMS. |  | DBA |
| Create a backup of the database. | For instructions, see the [SSMS documentation](https://learn.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms). | DBA, App owner |

### Upload the backup file to Amazon S3
<a name="upload-the-backup-file-to-amazon-s3"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a bucket in Amazon S3. | For more information, see the [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html). | DBA |
| Upload the backup file to the S3 bucket. | For more information, see the [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html). | SysOps administrator |

### Restore the database in Amazon RDS for SQL Server
<a name="restore-the-database-in-amazon-rds-for-sql-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add the option group to Amazon RDS. | 1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).<br />2. In the navigation pane, choose **Option groups**, **Create group**.<br />3. Complete the information for the option group, and then choose **Create**.<br />4. Add the `SQLSERVER_BACKUP_RESTORE` option to the option group, and then choose **Add option**.For more information, see the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html). | SysOps administrator |
| Restore the database. | 1. Connect to Amazon RDS for SQL Server through SSMS.<br />2. Call the `msdb.dbo.rds_restore_database` stored procedure to restore the database. | DBA |

### Validate the target database
<a name="validate-the-target-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate objects and data. | Validate the objects and data between the source database and Amazon RDS for SQL Server.This task migrates the database only. Logins and jobs will not be migrated. | App owner, DBA |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Redirect application traffic. | After validation, redirect application traffic to the Amazon RDS for SQL Server DB instance. | App owner, DBA |

## Related resources
<a name="migrate-an-on-premises-microsoft-sql-server-database-to-amazon-rds-for-sql-server-using-native-backup-and-restore-methods-resources"></a>
+ [Amazon S3 documentation](https://docs.aws.amazon.com/s3/)
+ [Amazon RDS for SQL Server documentation ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html)
+ [Options for the Microsoft SQL Server Database Engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.html)
