---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aurora-postgresql-integration/aurora-db-integration.html
---

# Aurora PostgreSQL-Compatible database integration
<a name="aurora-db-integration"></a>

To create connections between PostgreSQL databases and remote databases, you can use foreign data wrappers (FDWs). Foreign data wrappers offer the following advantages over SQL Server linked servers and Oracle database links:
+ **Native PostgreSQL integration** ‒ FDWs are native to PostgreSQL, and they use its SQL capabilities. This improves the integration experience.
+ **Integration and optimization** ‒ Linked servers (SQL Server) and database links (Oracle) are specific to their respective database ecosystems. By supporting queries to remote data sources and across database engines such as Oracle, SQL Server, MySQL, FDWs provide a more integrated and optimized approach for PostgreSQL.
+ **Cross-database querying** ‒ When you use FDWs, you can query data from multiple remote data sources within a single SQL statement. This supports cross-database analytics and reporting.
+ **Push-down optimization** ‒ FDWs can push operations such as filtering, projections, and sorting down to the remote data source. This reduces data transfer, and it improves query performance.
+ **Parallel runs** ‒ FDWs support running queries that involve remote data sources in parallel, which improves performance.

By using FDW integration, you can query and manipulate data from remote databases directly within Amazon Aurora PostgreSQL-Compatible Edition. This supports hybrid architectures and data integration scenarios.

This guide focuses on the `postgres_fdw` extension for connecting to remote PostgreSQL databases and the `tds_fdw` extension for connecting to SQL Server databases. Not covered in this guide are the following PostgreSQL extensions:
+ `oracle_fdw` for accessing data from Oracle databases
+ `mysql_fdw` for accessing data from MySQL databases
