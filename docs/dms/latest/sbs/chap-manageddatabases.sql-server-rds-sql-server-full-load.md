---
source_url: https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sql-server-rds-sql-server-full-load.html
---

# Full load SQL Server database migration
<a name="chap-manageddatabases.sql-server-rds-sql-server-full-load"></a>

The full load migration phase populates the target database with a copy of the source data. In each section, you can find detailed information about the full load method and their results to help you choose the one that fits your use case. For all three methods, we use the [`dms_sample`](https://github.com/aws-samples/aws-database-migration-samples/blob/master/sqlserver/sampledb/v1/README.md) database as an example. The `dms_sample` database includes tables, views, indexes, stored procedures, and other database objects.

**Topics**
+ [SQL Server database backup and restore using Amazon S3](chap-manageddatabases.sql-server-rds-sql-server-full-load-backup-restore.md)
+ [SQL Server import and export wizard](chap-manageddatabases.sql-server-rds-sql-server-full-load-import-export.md)
+ [Generate and Publish Scripts wizard and Bulk Copy Program Utility](chap-manageddatabases.sql-server-rds-sql-server-full-load-bcp.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
