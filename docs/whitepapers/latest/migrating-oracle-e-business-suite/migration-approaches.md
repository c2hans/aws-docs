---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/migration-approaches.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migration approaches
<a name="migration-approaches"></a>

 The following diagram shows the migration paths that customers may take depending on the current platform, tooling, and experiences available to them.

![Diagram showing possible migration approaches](https://docs.aws.amazon.com/whitepapers/latest/migrating-oracle-e-business-suite/images/migration-approaches.jpg)

 The current OS and endianness of the platform determines the appropriate tools you will need to migrate your Oracle E-Business Suite to AWS.

 The following table identifies each tool and its support for homogeneous and heterogeneous migrations.

 *Table 2 — Migration tools and their support for homogenous and heterogenous migrations*

|  **Migration tool or utility**  |   **Application/Database tier level**   |   **Homogeneous OS migration**   |   **Heterogeneous OS migration**   |   **Notes**   |
| --- | --- | --- | --- | --- |
|  **[AWS Application Migration Service (AWS MGN)](https://aws.amazon.com/application-migration-service/) **  |  Application and database tier  |  Yes  |  No  |  Block replication  |
|  [Oracle E-Business Suite Cloning ](https://docs.oracle.com/cd/E24628_01/doc.121/e57981/T508706T512065.htm)   |  Application tier  |  Yes  |  No  |  File system copy  |
|  [Oracle Data Guard](https://docs.oracle.com/cd/B19306_01/server.102/b14239/concepts.htm#g1049956)   |  Database tier  |  Yes  |  No  |  Database replication using [redo log](https://docs.oracle.com/cd/B28359_01/server.111/b28294/log_transport.htm#g1296022) [shipping](https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/oracle-data-guard-redo-transport-services.html)  |
|  [Oracle Transportable Tablespaces](https://docs.oracle.com/en/database/oracle/oracle-database/18/spmds/transportable-tablespaces.html#GUID-65DF5CB7-A79E-41DF-BCD3-51A55B7B512D)  |  Database tier  |  Yes  |  Yes  |  Migration of data files and database tablespaces structure  |
|  [Oracle RMAN](https://docs.oracle.com/cd/B28359_01/server.111/b28294/rman.htm#CHDHAJFD) [backup and](https://docs.oracle.com/en/database/oracle/oracle-database/19/sbydb/using-RMAN-in-oracle-data-guard-configurations.html) [restore](https://docs.oracle.com/cd/B28359_01/server.111/b28294/rman.htm#CHDHAJFD)  |  Database tier  |  Yes  |  No  |  [Oracle Native](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmquick.htm#BRADV89346) [Backup tool](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/getting-started-rman.html)  |
|  [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/)   |  Not supported for Oracle E- Business Suite Migration  |  N/A  |  N/A  |  Logical replication of a database  |
|  [Oracle Data Pump](https://docs.oracle.com/en/database/oracle/oracle-database/19/sutil/oracle-data-pump-overview.html)   |  Database tier  |  Yes  |  Yes  |  Export/import utility  |

 The preceding table should help you identify the tools for homogeneous or heterogeneous migrations. Further details on some of these tools are provided in the following sections.
