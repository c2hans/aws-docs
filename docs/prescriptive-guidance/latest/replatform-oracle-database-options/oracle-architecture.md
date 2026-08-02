---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/oracle-architecture.html
---

# Oracle multi-tenant architecture
<a name="oracle-architecture"></a>

[Oracle multi-tenant architecture](https://docs.oracle.com/en/database/oracle/oracle-database/19/multi/introduction-to-the-multitenant-architecture.html#GUID-C5B0AF7D-ABE8-4F69-9552-F4DAF40281F1) enables an Oracle database to function as a container database (CDB), and includes multiple pluggable databases (PDBs). By consolidating multiple Oracle databases into a single instance, the multi-tenant architecture reduces both cost and management efforts:
+ Both Amazon RDS for Oracle and Amazon RDS Custom for Oracle support multi-tenant architecture in Oracle Database Enterprise Edition (EE) and Standard Edition 2 (SE2).
+ Amazon RDS for Oracle supports Oracle multi-tenant architecture in versions 19c and 21c. Amazon RDS Custom for Oracle supports the architecture in version 19c only.
+ Amazon RDS for Oracle also supports Oracle single-tenant architecture in versions 19c and 21c. Amazon RDS Custom for Oracle currently does not support single-tenant architecture.
+ With EE, an Amazon RDS for Oracle CDB instance supports up to 30 PDBs, depending on the licenses. Amazon RDS Custom for Oracle doesn't restrict the number of PDBs that you can create.
+ In SE2, both Amazon RDS for Oracle and Amazon RDS Custom for Oracle support up to 3 PDBs per CDB.

For more information, see the AWS documentation for [Amazon RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.CDBs.html) and [Amazon RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating.html#custom-creating.overview).

|
|
| Tenancy configuration | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| --- |--- |--- |
| Multi-tenant-supported edition | EE & SE2 | EE & SE2 |
| Multi-tenant-supported version | 19c, 21c | 19c |
| Single-tenant architecture | Yes | No |
| Multi-tenant architecture | Yes | Yes |
| Number of PDBs per CDB in EE | Up to 30 | No restriction |
| Number of PDBs per CDB in SE2 | Up to 3 | Up to 3 |
