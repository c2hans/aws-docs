---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.FeatureSupport.UnsupportedRoles.html
---

# Microsoft SQL Server security
<a name="SQLServer.Concepts.General.FeatureSupport.UnsupportedRoles"></a>

The Microsoft SQL Server database engine uses role-based security. The master user name that you specify when you create a DB instance is a SQL Server Authentication login that is a member of the `processadmin`, `public`, and `setupadmin` fixed server roles.

Any user who creates a database is assigned to the db\_owner role for that database and has all database-level permissions except for those that are used for backups. Amazon RDS manages backups for you.

The following server-level roles aren't available in Amazon RDS for SQL Server:
+ bulkadmin
+ dbcreator
+ diskadmin
+ securityadmin
+ serveradmin
+ sysadmin

The following server-level permissions aren't available on RDS for SQL Server DB instances:
+ ALTER ANY DATABASE
+ ALTER ANY EVENT NOTIFICATION
+ ALTER RESOURCES
+ ALTER SETTINGS (you can use the DB parameter group API operations to modify parameters; for more information, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md))
+ AUTHENTICATE SERVER
+ CONTROL\_SERVER
+ CREATE DDL EVENT NOTIFICATION
+ CREATE ENDPOINT
+ CREATE SERVER ROLE
+ CREATE TRACE EVENT NOTIFICATION
+ DROP ANY DATABASE
+ EXTERNAL ACCESS ASSEMBLY
+ SHUTDOWN (You can use the RDS reboot option instead)
+ UNSAFE ASSEMBLY
+ ALTER ANY AVAILABILITY GROUP
+ CREATE ANY AVAILABILITY GROUP

## SSL support for Microsoft SQL Server DB instances
<a name="SQLServer.Concepts.General.SSL"></a>

You can use SSL to encrypt connections between your applications and your Amazon RDS DB instances running Microsoft SQL Server. You can also force all connections to your DB instance to use SSL. If you force connections to use SSL, it happens transparently to the client, and the client doesn't have to do any work to use SSL.

SSL is supported in all AWS Regions and for all supported SQL Server editions. For more information, see [Using SSL with a Microsoft SQL Server DB instance](SQLServer.Concepts.General.SSL.Using.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
