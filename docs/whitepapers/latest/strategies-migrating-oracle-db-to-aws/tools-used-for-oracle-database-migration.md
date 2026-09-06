---
source_url: https://docs.aws.amazon.com/whitepapers/latest/strategies-migrating-oracle-db-to-aws/tools-used-for-oracle-database-migration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Tools used for Oracle Database migration
<a name="tools-used-for-oracle-database-migration"></a>

 A number of tools and technologies are available for data migration. You can use some of these tools interchangeably, or you can use other third-party tools or open-source tools available in the market.
+  **[AWS DMS](https://aws.amazon.com/dms/)** helps you move databases to and from AWS easily and securely. It supports most commercial and open-source databases, and facilitates both homogeneous and heterogeneous migrations. AWS DMS offers [change data capture](https://en.wikipedia.org/wiki/Change_data_capture) technology to keep databases in sync and minimize downtime during a migration. It is a managed service with no client install required.
+  **[Oracle Recovery Manager](https://www.oracle.com/database/technologies/high-availability/rman.html) (RMAN)** is a tool available from Oracle for performing and managing Oracle Database backups and restorations. RMAN allows full hot or cold backups, plus incremental backups. RMAN maintains a catalogue of the backups, making the restoration process simple and dependable. RMAN can also duplicate, or clone, a database from a backup or from an active database.
+  **[Oracle Data Pump Export](https://docs.oracle.com/cd/B28359_01/server.111/b28319/dp_export.htm#g1022624)** is a versatile utility for exporting and importing data and metadata from or to Oracle databases. You can perform Data Pump export/import on an entire database, selective schemas, table spaces, or database objects. Data Pump export/import also has powerful data-filtering capabilities for selective export or import of data.
+  **[Oracle GoldenGate](https://www.oracle.com/integration/goldengate/)** is a tool for replicating data between a source and one or more destination databases. You can use it to build high-availability architectures. You can also use it to perform real-time data integration, transactional change data capture, and replication in heterogeneous IT environments.
+  **[Oracle SQL Developer](https://www.oracle.com/database/technologies/appdev/sqldeveloper-landing.html)** is a no-cost GUI tool available from Oracle for data manipulation, development, and management. This Java-based tool is available for Microsoft Windows, Linux, or iOS X.
+  **[Oracle SQL\*Loader](https://docs.oracle.com/cd/B19306_01/server.102/b14215/part_ldr.htm)** is a bulk data-load utility available from Oracle for loading data from external files into a database. SQL\*Loader is included as part of the full database client installation.
