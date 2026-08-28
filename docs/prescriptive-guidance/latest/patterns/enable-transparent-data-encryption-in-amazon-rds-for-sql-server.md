---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-transparent-data-encryption-in-amazon-rds-for-sql-server.html
---

# Enable transparent data encryption in Amazon RDS for SQL Server
<a name="enable-transparent-data-encryption-in-amazon-rds-for-sql-server"></a>

*Ranga Cherukuri, Amazon Web Services*

## Summary
<a name="enable-transparent-data-encryption-in-amazon-rds-for-sql-server-summary"></a>

This pattern describes how to implement transparent data encryption (TDE) in Amazon Relational Database Service (Amazon RDS) for SQL Server to encrypt data at rest.

## Prerequisites and limitations
<a name="enable-transparent-data-encryption-in-amazon-rds-for-sql-server-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An Amazon RDS for SQL Server DB instance

**Product versions**

Amazon RDS currently supports TDE for the following SQL Server versions and editions:
+ SQL Server 2016 Enterprise Edition
+ SQL Server 2017 Enterprise Edition
+ SQL Server 2019 Standard and Enterprise Editions
+ SQL Server 2022 Standard and Enterprise Editions

For the latest information about supported versions and editions, see [Support for Transparent Data Encryption in SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.TDE.html) in the Amazon RDS documentation.

## Architecture
<a name="enable-transparent-data-encryption-in-amazon-rds-for-sql-server-architecture"></a>

**Technology stack**
+ Amazon RDS for SQL Server

**Architecture**

![Architecture for enabling TDE for Amazon RDS for SQL Server databases](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/f513ea66-fd14-48d3-a576-8eb281e77b21/images/8a121e67-9a90-42d2-988e-3bcab0e6bc35.png)

## Tools
<a name="enable-transparent-data-encryption-in-amazon-rds-for-sql-server-tools"></a>
+ Microsoft SQL Server Management Studio (SSMS) is an integrated environment for managing a SQL Server infrastructure. It provides a user interface and a group of tools with rich script editors that interact with SQL Server.

## Epics
<a name="enable-transparent-data-encryption-in-amazon-rds-for-sql-server-epics"></a>

### Create an option group in the Amazon RDS console
<a name="create-an-option-group-in-the-amazon-rds-console"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Open the Amazon RDS console.  | Sign in to the AWS Management Console and open the [Amazon RDS console](https://console.aws.amazon.com/rds/). | Developer, DBA |
| Create an option group. | In the navigation pane, choose **Option groups**, **Create group**. Choose **sqlserver-ee** as the DB engine, and then select the engine version. | Developer, DBA |
| Add the TRANSPARENT\_DATA\_ENCRYPTION option. | Edit the option group you created and add the option called `TRANSPARENT_DATA_ENCRYPTION`. | Developer, DBA |

### Associate the option group with the DB instance
<a name="associate-the-option-group-with-the-db-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Choose the DB instance. | In the Amazon RDS console, in the navigation pane, choose **Databases**, and then choose the DB instance you want to associate with the option group. | Developer, DBA |
| Associate the DB instance with the option group. | Choose **Modify**, and then use the **Option group** setting to associate the SQL Server DB instance with the option group you created earlier. | Developer, DBA |
| Apply the changes. | Apply the changes immediately or during the next maintenance window, as desired. | Developer, DBA |
| Get the certificate name. | Get the default certificate name by using the following query.<pre>USE [master]<br />GO<br />SELECT name FROM sys.certificates WHERE name LIKE 'RDSTDECertificate%'<br />GO</pre> | Developer, DBA |

### Create the database encryption key
<a name="create-the-database-encryption-key"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect to the Amazon RDS for SQL Server DB instance using SSMS. | For instructions, see [Using SSMS](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms) in the Microsoft documentation. | Developer, DBA |
| Create the database encryption key by using the default certificate. | Create a database encryption key by using the default certificate name you got earlier. Use the following T-SQL query to create a database encryption key. You can specify the AES\_256 algorithm instead of AES\_128.<pre>USE [Databasename]<br />GO<br />CREATE DATABASE ENCRYPTION KEY<br />WITH ALGORITHM = AES_128<br />ENCRYPTION BY SERVER CERTIFICATE [certificatename]<br />GO</pre> | Developer, DBA |
| Enable the encryption on the database. | Use the following T-SQL query to enable database encryption.<pre>ALTER DATABASE [Database Name]<br />SET ENCRYPTION ON<br />GO</pre> | Developer, DBA |
| Check the status of encryption. | Use the following T-SQL query to check the status of encryption.<pre>SELECT DB_NAME(database_id) AS DatabaseName, encryption_state, percent_complete FROM sys.dm_database_encryption_keys</pre> | Developer, DBA |

## Related resources
<a name="enable-transparent-data-encryption-in-amazon-rds-for-sql-server-resources"></a>
+ [Support for Transparent Data Encryption in SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.TDE.html) (Amazon RDS documentation)
+ [Working with Option Groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html) (Amazon RDS documentation)
+ [Modifying an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html) (Amazon RDS documentation)
+ [Transparent Data Encryption for SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption) (Microsoft documentation)
+ [Using SSMS](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms) (Microsoft documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
