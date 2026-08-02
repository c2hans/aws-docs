---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/data-mobility-cirata.html
---

# Cirata Data Migrator
<a name="data-mobility-cirata"></a>

*Last update: November 15, 2024*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="data-mobility-cirata-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Cirata Data Migrator](https://cirata.com/data-management/products/data-migrator) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | Migration and Modernization ISV Competency |
| **AWS Marketplace**<br />Link to subscribe or download | [Cirata Data Migrator on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-2pdrlrp7pu7yc) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | Servers deployed on AWS (customer VPC)Servers deployed on premises in customer environmentSaaS or servers in other cloud provider environment |
| **Compliance** | General Data Protection Regulation (GDPR) |
| **Service model** | Full self-service – Deployment, management, and maintenance can be done by the customer or end-userSelf-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor supportManaged service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Data migration
<a name="data-mobility-cirata-data-migration"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Replication method**<br />The ability to support one or more of the following replication methods:Agentless – Uses protocols or interfaces such as SNMP or WMIAgent-based – Requires installation of software on the source resources, such as Linux or Windows serversLogin-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Agent-based |
| **Replication source**<br />Support for one or more of the following sources:BlockFileObjectTapeOther | FileObject |
| **Automation**<br />The ability to manage a migration through scheduling controls:Product can be accessed, configured, and managed programmaticallyProduct can schedule migration jobsProduct can pause and resume migrationsProduct can schedule bandwidth throttling (for example, to increase throughput during off-peak periods) | Access programmaticallySchedule migrationsPause and resume migrationSchedule bandwidth throttling |
| **Performance**<br />The ability to optimize performance:Manage bandwidth consumption, such as through throttlingCompress data before transfer to reduce network trafficRun multithreaded or concurrent process for data migration tasks | Managed bandwidth consumptionMultithreaded or concurrent process support |
| **Security**<br />The ability to secure the product and data transfers:Encrypt data in transit from source to destinationSupport the use of customer-provided encryption keysStore all actions requested by the user and performed by the tool in a tamper-proof audit logIntegrate with third-party identity providers for authentication | Encrypt data in transit from source to destinationStore all actions requested by the user and performed by the tool in a tamper-proof audit logIntegrate with third-party identity providers for authentication |
| **Synchronization type**<br />The ability to support multiple data-synchronization options:One-time transferPeriodic transferContinuous transfer | One-time transferPeriodic transferContinuous transfer |
| **File-transfer options**<br />The ability to support file migration options:Track all files copied previously and compare against source data in the subsequent copyCopy only modified portions of a file instead of the entire fileSupport include or exclude patterns for copying files and folders with simple or regular expression patterns | Changed-file trackingInclude or exclude patterns |
| **NFS and SMB options**<br />For Network File System (NFS) and Server Message Block (SMB) file systems, the ability to do the following:Preserve symbolic linkPreserve hard linkMove open files | Preserve symbolic linkMove open files |
| **Data validation**<br />The ability to validate data transfers by using checksums for data integrity | Not available |
| **Discovery**<br />The ability to scan and report on source system data (such as file name, type, size, usage, file timestamps, and summary statistics) and produce a pre-migration assessment report | Not available |
| **Reporting and alerting**<br />The ability to report on data-transfer progress and statistics:File and object transfer statisticsNetwork statisticsTime and duration statistics, including time taken and forecast completionGeneration of a detailed post-migration reportGeneration of a full validation report after migration completionAlerting on failure scenarios, job completion | File and object transfer statisticsNetwork statisticsTime and duration statistics, including time taken and forecast completionGeneration of a detailed post-migration reportGeneration of a full validation report after migration completionAlerting on failure scenarios, job completion |
| **Failure handling**<br />The ability to retry transfer operations if a network failure or connectivity issue occurs | Available |

## Database migration
<a name="data-mobility-cirata-database-migration"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Migration approach**Homogeneous – Source and target engine are the sameHeterogeneous – Source and target engine are differentThe ability to convert source database engine metadata to be compatible with the target database engineThe ability of the tool to migrate large database objects, such as LOB and binary data types | HomogeneousHeterogeneousSchema conversionSupport for LOB data types |
| **Source engine**<br />The ability to migrate specific database engines, such as IBM Db2 LUW, MariaDB, Microsoft SQL Server, MySQL, Oracle, PostgreSQL, or others | Apache HiveApache IcebergDatabricksSnowflake |
| **Migration type**Full load only – Perform a one-time migration from source to targetFull load with CDC – Perform full load with change data capture (CDC) to continue replication from source to targetCDC only – Don't perform a one-time migration, but continue to replicate data changes from the source to the targetOffline – Migrate large data sets by using offline methods or external storage devices | Full load with CDC |
| **Data transform**<br />The ability to transform data during the migration | Metadata only, transforms Apache Hive compatible formats to Delta Lake formats and Snowflake formats |
| **Migration scope**<br />The ability to migrate metadata and application data:Metadata – Migrate database schema structure, including table, view, and stored procedure definitionTable data – Migrate table data | MetadataTable data |
| **Tool architecture, high availability**<br />The ability support one or more of the following high availability (HA) configurations:Built-in HA configurationManual HA configuration | Manual HA configuration |
| **Tool sizing**<br />The ability to size itself for the migration load:Intelligent sizing during discoveryManual sizing based on source database parameters, such as database size or change log | Manual sizing |
| **Data-type support**<br />The ability to migrate standard and custom data types | Standard |
| **Pre-migration assessment**<br />The ability to assess and warn of potential migration issues before starting the migration task | Available |
| **Data validation**<br />The ability to compare the data at the source and the target immediately after it performs a full data load | Available for all tables |
| **Monitoring and logging**<br />The ability to log and monitor the migration task and monitor tool performance | Task loggingTask monitoring and alertsPerformance monitoring |
| **Security**<br />The ability to retain data encryption (if any) from source to target | Available |
| **Data selection**<br />The ability to migrate a subset of data | Available |
| **Migration parallelism**<br />The ability to migrate multiple subsets of data in parallel | Available. Metadata migration is defined based on the table and database pattern. If the metadata matches the pattern, it will be migrated in parallel based on the configured thread count and system limits. |
