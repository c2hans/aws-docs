---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/data-mobility-tessell.html
---

# Tessell DBaaS
<a name="data-mobility-tessell"></a>

*Last update: November 15, 2024*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="data-mobility-tessell-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Tessell](https://www.tessell.com/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | Migration and Modernization ISV Competency |
| **AWS Marketplace**<br />Link to subscribe or download | [Tessell DBaaS on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-h2caqujt4pp3q) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + SaaS on AWS (vendor VPC)<br />+ Servers deployed on AWS (customer VPC)<br />+ SaaS or servers in other cloud provider environment |
| **Compliance** | + International Organization for Standardization (ISO) 27001 and 27701<br />+ Payment card industry (PCI)<br />+ System and Organization Controls (SOC) |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support |
| **Pricing model** | Subscription |

## Data migration
<a name="data-mobility-tessell-data-migration"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Replication method**<br />The ability to support one or more of the following replication methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Login-based |
| **Replication source**<br />Support for one or more of the following sources:+ Block<br />+ File<br />+ Object<br />+ Tape<br />+ Other | + Block<br />+ File |
| **Automation**<br />The ability to manage a migration through scheduling controls:+ Product can be accessed, configured, and managed programmatically<br />+ Product can schedule migration jobs<br />+ Product can pause and resume migrations<br />+ Product can schedule bandwidth throttling (for example, to increase throughput during off-peak periods) | + Access programmatically<br />+ Schedule migrations<br />+ Pause and resume migration<br />+ Schedule bandwidth throttling |
| **Performance**<br />The ability to optimize performance:+ Manage bandwidth consumption, such as through throttling<br />+ Compress data before transfer to reduce network traffic<br />+ Run multithreaded or concurrent process for data migration tasks | + Managed bandwidth consumption<br />+ Compression before transfer<br />+ Multithreaded or concurrent process support |
| **Security**<br />The ability to secure the product and data transfers:+ Encrypt data in transit from source to destination<br />+ Support the use of customer-provided encryption keys<br />+ Store all actions requested by the user and performed by the tool in a tamper-proof audit log<br />+ Integrate with third-party identity providers for authentication | + Encrypt data in transit from source to destination<br />+ Support the use of customer-provided encryption keys<br />+ Store all actions requested by the user and performed by the tool in a tamper-proof audit log<br />+ Integrate with third-party identity providers for authentication |
| **Synchronization type**<br />The ability to support multiple data-synchronization options:+ One-time transfer<br />+ Periodic transfer<br />+ Continuous transfer | + One-time transfer<br />+ Periodic transfer<br />+ Continuous transfer |
| **File-transfer options**<br />The ability to support file migration options:+ Track all files copied previously and compare against source data in the subsequent copy<br />+ Copy only modified portions of a file instead of the entire file<br />+ Support include or exclude patterns for copying files and folders with simple or regular expression patterns | + Changed-file tracking<br />+ Copy for only modified portions of a file |
| **NFS and SMB options**<br />For Network File System (NFS) and Server Message Block (SMB) file systems, the ability to do the following:+ Preserve symbolic link<br />+ Preserve hard link<br />+ Move open files | Not available |
| **Data validation**<br />The ability to validate data transfers by using checksums for data integrity | Available |
| **Discovery**<br />The ability to scan and report on source system data (such as file name, type, size, usage, file timestamps, and summary statistics) and produce a pre-migration assessment report | Available |
| **Reporting and alerting**<br />The ability to report on data-transfer progress and statistics:+ File and object transfer statistics<br />+ Network statistics<br />+ Time and duration statistics, including time taken and forecast completion<br />+ Generation of a detailed post-migration report<br />+ Generation of a full validation report after migration completion<br />+ Alerting on failure scenarios, job completion | + File and object transfer statistics<br />+ Time and duration statistics, including time taken and forecast completion<br />+ Generation of a detailed post-migration report<br />+ Generation of a full validation report after migration completion<br />+ Alerting on failure scenarios, job completion |
| **Failure handling**<br />The ability to retry transfer operations if a network failure or connectivity issue occurs | Available |

## Database migration
<a name="data-mobility-tessell-database-migration"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Migration approach**+ Homogeneous – Source and target engine are the same<br />+ Heterogeneous – Source and target engine are different<br />+ The ability to convert source database engine metadata to be compatible with the target database engine<br />+ The ability of the tool to migrate large database objects, such as LOB and binary data types | + Homogeneous<br />+ Support for LOB data types, including BLOB, CLOB, NCLOB, and BFILE |
| **Source engine**<br />The ability to migrate specific database engines, such as IBM Db2 LUW, MariaDB, Microsoft SQL Server, MySQL, Oracle, PostgreSQL, or others | + MariaDB<br />+ Microsoft SQL Server<br />+ Milvus<br />+ MongoDB<br />+ MySQL<br />+ Oracle<br />+ PostgreSQL |
| **Migration type**+ Full load only – Perform a one-time migration from source to target<br />+ Full load with CDC – Perform full load with change data capture (CDC) to continue replication from source to target<br />+ CDC only – Don't perform a one-time migration, but continue to replicate data changes from the source to the target<br />+ Offline – Migrate large data sets by using offline methods or external storage devices | + Full load with CDC<br />+ Offline |
| **Data transform**<br />The ability to transform data during the migration | + Metadata<br />+ Table data |
| **Migration scope**<br />The ability to migrate metadata and application data:+ Metadata – Migrate database schema structure, including table, view, and stored procedure definition<br />+ Table data – Migrate table data | + Metadata<br />+ Table data |
| **Tool architecture, high availability**<br />The ability support one or more of the following high availability (HA) configurations:+ Built-in HA configuration<br />+ Manual HA configuration | Built-in HA configuration |
| **Tool sizing**<br />The ability to size itself for the migration load:+ Intelligent sizing during discovery<br />+ Manual sizing based on source database parameters, such as database size or change log | + Intelligent sizing<br />+ Manual sizing |
| **Data-type support**<br />The ability to migrate standard and custom data types | + Standard<br />+ Custom |
| **Pre-migration assessment**<br />The ability to assess and warn of potential migration issues before starting the migration task | Available |
| **Data validation**<br />The ability to compare the data at the source and the target immediately after it performs a full data load | Available for all tables |
| **Monitoring and logging**<br />The ability to log and monitor the migration task and monitor tool performance | + Task logging<br />+ Task monitoring and alerts<br />+ Performance monitoring |
| **Security**<br />The ability to retain data encryption (if any) from source to target | Available |
| **Data selection**<br />The ability to migrate a subset of data | Available |
| **Migration parallelism**<br />The ability to migrate multiple subsets of data in parallel | Available. Multiple degrees of parallelism can be achieved when taking an [RMAN backup](https://docs.oracle.com/en/database/oracle/oracle-database/12.2/bradv/configuring-rman-client-advanced.html).<br />After the backup is restored, the subsequent data transfer through Oracle DataGuard happens serially in the order that the transactions were executed. The transfer is done this way so that the database at the destination always remains consistent and readable. |
