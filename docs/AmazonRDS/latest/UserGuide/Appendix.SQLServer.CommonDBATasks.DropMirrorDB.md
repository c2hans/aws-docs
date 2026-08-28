---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.DropMirrorDB.html
---

# Dropping a database in an Amazon RDS for Microsoft SQL Server DB instance
<a name="Appendix.SQLServer.CommonDBATasks.DropMirrorDB"></a>

You can drop a database on an Amazon RDS DB instance running Microsoft SQL Server in a Single-AZ or Multi-AZ deployment. To drop the database, use the following command:

```
--replace {{your-database-name}} with the name of the database you want to drop
EXECUTE msdb.dbo.rds_drop_database  N'{{your-database-name}}'
```

**Note**
Use straight single quotes in the command. Smart quotes will cause an error.

After you use this procedure to drop the database, Amazon RDS drops all existing connections to the database and removes the database's backup history.

To grant backup and restore allowance to other users, follow this procedure:

```
USE master
GO
CREATE LOGIN {{user1}} WITH PASSWORD=N'{{changeThis}}', DEFAULT_DATABASE=master, CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
USE msdb
GO
CREATE USER {{user1}} FOR LOGIN {{user1}}
GO
use msdb
GO
GRANT EXECUTE ON msdb.dbo.rds_backup_database TO {{user1}}
GO
GRANT EXECUTE ON msdb.dbo.rds_restore_database TO {{user1}}
GO
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
