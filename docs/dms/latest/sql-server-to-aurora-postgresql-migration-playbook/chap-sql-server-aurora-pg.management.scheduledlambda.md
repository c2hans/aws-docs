---
source_url: https://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/chap-sql-server-aurora-pg.management.scheduledlambda.html
---

# SQL Server Agent and PostgreSQL
<a name="chap-sql-server-aurora-pg.management.scheduledlambda"></a>

This topic provides reference information about the differences between SQL Server Agent and PostgreSQL in the context of migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. You can understand the key functions of SQL Server Agent, including scheduling automated maintenance jobs and alerting, and how these features are utilized in SQL Server.

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.management.scheduledlambda.sqlserver"></a>

SQL Server Agent provides two main functions: scheduling automated maintenance jobs and alerting.

**Note**
Other SQL Server built-in frameworks such as replication, also use SQL Server Agent jobs.

For more information, see [Maintenance Plans](chap-sql-server-aurora-pg.management.maintenanceplans.md) and [Alerting](chap-sql-server-aurora-pg.management.alerting.md).

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.management.scheduledlambda.pg"></a>

Currently, there is no equivalent in Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) for scheduling tasks but you can create scheduled AWS Lambda that will run a stored procedure. Find an example in [Database Mail](chap-sql-server-aurora-pg.management.databasemail.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
