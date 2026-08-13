---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-auditing-on-aws/auditing-rds-sql-instance.html
---

# Auditing Amazon RDS for SQL Server DB instances
<a name="auditing-rds-sql-instance"></a>

This section provides information about auditing options for SQL Server on Amazon RDS, including creating audits, viewing audit logs, and monitoring results.

## Prerequisites
<a name="rds-prerequisites"></a>
+ An Amazon Simple Storage Service (Amazon S3) bucket for storing the audit files
+ An AWS Identity and Access Management (IAM) [role for accessing the S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.html#Appendix.SQLServer.Options.Audit.IAM)
+ A database login with the `ALTER ANY SERVER AUDIT` or `CONTROL SERVER` permission

## Supported versions
<a name="rds-versions"></a>
+ For Amazon RDS for SQL Server 2014, all editions support server-level audits. Enterprise edition also supports database-level audits.
+ Starting with SQL Server 2016 (13.x) SP1, all editions support both server-level and database-level audits.
+ Amazon RDS currently supports SQL Server audits in all AWS Regions except Middle East (Bahrain). For the latest information, see [Support for SQL Server Audit](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.html#Appendix.SQLServer.Options.Audit.Support) in the Amazon RDS documentation.

## Using C2 audit mode
<a name="rds-c2"></a>

C2 audit mode is a parameter in the Amazon RDS for SQL Server DB parameter group. It is disabled by default. You can enable it by updating the parameter value to 1. When C2 audit mode is enabled, it audits events such as user logins, stored procedure calls, and creation and deletion of objects. This mode can generate lot of data because it audits everything or nothing.

**Important**
Microsoft plans to remove C2 audit mode in a future version of SQL Server. We recommend that you avoid using this feature.

## Creating and viewing audits
<a name="rds-creating-viewing"></a>

You can audit Amazon RDS for SQL Server databases by using built-in SQL Server audit mechanisms that involve creating audits and audit specifications.
+ Audit logs are uploaded to an S3 bucket by using an IAM role that has the necessary permissions to access the bucket.
+ You can choose the IAM role, the S3 bucket, compression, and the retention period when you create the option group. The maximum retention period time is 35 days.
+ You create the option group and attach it to a new or existing Amazon RDS for SQL Server DB instance.  The audit logs are stored in `D:\rdsdbdata\SQLAudit`.
+ After SQL Server finishes writing to an audit log file or when the file reaches its size limit, Amazon RDS uploads the file to your S3 bucket.
+ If you enable retention, Amazon RDS moves the file into the retention folder at `D:\rdsdbdata\SQLAudit\transmitted`. Audit records are kept on the DB instance until the audit log file is uploaded.
+ You can also find audit records by querying for `dbo.rds_fn_get_audit_file`.

For Multi-AZ instances, the database audit specification objects are replicated to all nodes.  Server audit and server audit specifications aren't replicated to all nodes, so you should create these manually.

### Configuring the option group
<a name="configuring-the-option-group.28696a4a-9491-5008-a7a7-d0540337271f"></a>

Follow these steps to configure an option group to perform a SQL Server audit on your Amazon RDS for SQL Server DB instance. For detailed instructions, see [SQL Server Audit](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.html) in the Amazon RDS documentation.
+ Create an option group.
+ Add the [SQLSERVER\_AUDIT](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.html)** **option to the option group.
+ For **S3 destination**, create a new bucket or select an existing bucket for the audit logs.
+ For **IAM role**, create a new role or choose an existing role with the required policies. For more information, see [Manually creating an IAM role for SQL Server Audit](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.html#Appendix.SQLServer.Options.Audit.IAM) in the IAM documentation.
+ Expand **Additional information** and select **Enable compression** to compress audit logs (recommended).
+ To keep the audit logs for the DB instance, select **Enable retention** and specify a retention period (up to a maximum of 35 days).
+ Apply the options group to a new or existing Amazon RDS for SQL Server DB instance.
  + For a new DB instance, apply the option group when you launch the instance.
  + For an existing DB instance, [modify the instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html) and attach the option group.

### Creating audits
<a name="creating-audits.aa6b1b6a-47e5-57dd-b1b5-ea01ffd594e1"></a>

To create a server audit, use the following script. This script creates the audit file in the file path that you specify. For syntax, arguments, and examples, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-server-audit-transact-sql?view=sql-server-ver16). To avoid errors, review the list of limitations listed in [Amazon RDS documentation.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.html#Appendix.SQLServer.Options.Audit.CreateAuditsAndSpecifications)

```
--Creating the server audit
 use master
 GO
 CREATE SERVER AUDIT [Audit-<<servername>>]
 TO FILE  ( FILEPATH = N'D:\rdsdbdata\SQLAudit', MAXSIZE = 2 MB, RESERVE_DISK_SPACE = OFF)
 WITH ( QUEUE_DELAY = 1000, ON_FAILURE = CONTINUE)
 GO
-- Enabling the server audit
 ALTER SERVER AUDIT [Audit-<<servername>>] WITH (STATE = ON) ;
 GO
```

### Creating audit specifications
<a name="creating-audit-specifications.128cee1e-a790-5fd0-a70c-b70063a8b13c"></a>

After you create a server audit, you can record server-level events by creating a server audit specification with the following code. This specification determines what will be checked during the server audit. For syntax, arguments, and examples, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-server-audit-specification-transact-sql). The following specification audits failed login actions and tracks the creation, alteration, and deletion of server objects. For a list of actions, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions).

```
--Creating server audit specification
 USE [master]
 GO
 CREATE SERVER AUDIT SPECIFICATION [Audit-Spec-<<servername>>]
 FOR SERVER AUDIT  [Audit-<<servername>>]
 ADD (FAILED_LOGIN_GROUP), ADD (SERVER_OBJECT_CHANGE_GROUP)
 GO
--Enables the audit
 ALTER SERVER AUDIT [Audit-<<servername>>]
 WITH (STATE = ON);
 GO
```

You can use the following code to create a database audit specification that records database-level events. This example audits INSERT actions. For syntax, arguments, and more examples, see the [Microsoft SQL Server documentation](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-database-audit-specification-transact-sql).

```
--Creating database audit specification
 USE [<<DBName>>]
 GO

 CREATE DATABASE AUDIT SPECIFICATION [DatabaseAuditSpecification-<<DBName>>]
 FOR SERVER AUDIT [Audit-<<ServerName>>]
 ADD (INSERT ON DATABASE::[<<DBName>>] BY [dbo])
 WITH (STATE = ON)
 GO
```

### Viewing audit logs
<a name="viewing-audit-logs.9a24635d-b3c5-5946-8f97-0607282fa3f9"></a>

Use the following query to view the audit logs. Audit logs are kept in the DB instance until they are uploaded to Amazon S3. If you enable retention for the [**SQLSERVER\_AUDIT**](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.html)** **option, Amazon RDS moves the file into the retention folder `D:\rdsdbdata\SQLAudit\transmitted`.

You can also view the audit records in the retention folder by changing the filter to `D:\rdsdbdata\SQLAudit\transmitted\*.sqlaudit`.

```
--Viewing audit logs
SELECT   *
	FROM     msdb.dbo.rds_fn_get_audit_file
	             ('D:\rdsdbdata\SQLAudit\*.sqlaudit'
	             , default
	             , default )
--Viewing audit logs in retention folder
SELECT   *
	FROM     msdb.dbo.rds_fn_get_audit_file
	             ('D:\rdsdbdata\SQLAudit\transmitted\*.sqlaudit'
	             , default
	             , default )
```

Additional options for auditing SQL Server databases are discussed in the following AWS and Microsoft documentation:
+ SQL Server Extended Events: See the AWS blog post [Set up Extended Events in Amazon RDS for SQL Server](https://aws.amazon.com/blogs/database/set-up-extended-events-in-amazon-rds-for-sql-server/).
+ SQL Server triggers: See [Creating a rule that triggers on an Amazon RDS event](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-cloud-watch-events.html) in the Amazon RDS documentation.
+ Change tracking: See [Track data changes](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/track-data-changes-sql-server) in the Microsoft SQL Server documentation.
+ Change data capture: See [Using change data capture](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.CDC.html) in the Amazon RDS documentation.
+ C2 audit mode parameter: See [c2 audit mode Server Configuration Option](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/c2-audit-mode-server-configuration-option) in the Microsoft SQL Server documentation.

## Monitoring
<a name="rds-monitoring"></a>

You can use database activity streams in Amazon RDS to integrate SQL Server audit events with database activity monitoring tools from Imperva, McAfee, and IBM. For more information, see [Auditing in Microsoft SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.Overview.html#DBActivityStreams.Overview.SQLServer-auditing) in the Amazon RDS documentation.
