---
source_url: https://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/chap-sql-server-aurora-pg.storage.html
---

# Physical storage overview
<a name="chap-sql-server-aurora-pg.storage"></a>

This topic provides conceptual content comparing feature compatibility between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. It covers three main areas: columnstore indexes, indexed views and materialized views, and partitioning. The content explores how these features are implemented in both database systems, highlighting similarities, differences, and potential migration challenges. By understanding these concepts, database administrators and developers can better prepare for the transition from SQL Server to Aurora PostgreSQL. This knowledge allows them to anticipate feature gaps, plan for necessary adjustments in their database design and optimization strategies, and make informed decisions when migrating their data warehousing and analytical workloads.

**Topics**
+ [Columnstore index functionality](chap-sql-server-aurora-pg.storage.columnstore.md)
+ [Indexed view functionality](chap-sql-server-aurora-pg.storage.materializedviews.md)
+ [Partitioning databases](chap-sql-server-aurora-pg.storage.partitioning.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Database Migration Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
