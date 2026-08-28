---
source_url: https://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/chap-sql-server-aurora-pg.tuning.html
---

# Performance tuning overview
<a name="chap-sql-server-aurora-pg.tuning"></a>

This topic provides conceptual information about query execution plans, feature compatibility, and statistics in the context of migrating from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. You can gain insights into how these database management systems approach query optimization, execution plan generation, and statistical data management. The content compares and contrasts the methods used by SQL Server and PostgreSQL, highlighting key differences in functionality such as database hints, graphical execution plans, and statistics collection. Understanding these concepts is crucial for database administrators and developers who are planning or executing a migration from SQL Server to Aurora PostgreSQL, as it helps them anticipate changes in query performance optimization strategies and adapt their database management practices accordingly.

**Topics**
+ [Tuning run plans](chap-sql-server-aurora-pg.tuning.plans.md)
+ [Query hints and plan guides](chap-sql-server-aurora-pg.tuning.queryplanning.md)
+ [Managing statistics](chap-sql-server-aurora-pg.tuning.statistics.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
