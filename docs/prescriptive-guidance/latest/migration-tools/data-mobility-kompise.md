---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/data-mobility-kompise.html
---

# Komprise Elastic Data Migration
<a name="data-mobility-kompise"></a>

*Last update: November 15, 2024*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="data-mobility-kompise-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Komprise Elastic Data Migration](https://www.komprise.com/product/elastic-data-migration/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | Migration and Modernization ISV Competency |
| **AWS Marketplace**<br />Link to subscribe or download | [Komprise Intelligent Data Management on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-gre4qozwl6vqi) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | Servers deployed on AWS (customer VPC)SaaS on AWS (vendor VPC)Servers deployed on premises in customer environmentSaaS or servers in other cloud provider environment |
| **Compliance** | System and Organization Controls 2 (SOC 2) |
| **Service model** | Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support |
| **Pricing model** | Subscription |

## Data migration
<a name="data-mobility-kompise-data-migration"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Replication method**<br />The ability to support one or more of the following replication methods:Agentless – Uses protocols or interfaces such as SNMP or WMIAgent-based – Requires installation of software on the source resources, such as Linux or Windows serversLogin-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Agent-based |
| **Replication source**<br />Support for one or more of the following sources:BlockFileObjectTapeOther | FileObjectOther – Any NFS, SMB, Object interface (including tape with file front-end) |
| **Automation**<br />The ability to manage a migration through scheduling controls:Product can be accessed, configured, and managed programmaticallyProduct can schedule migration jobsProduct can pause and resume migrationsProduct can schedule bandwidth throttling (for example, to increase throughput during off-peak periods) | Access programmaticallySchedule migrationsPause and resume migrationSchedule bandwidth throttling |
| **Performance**<br />The ability to optimize performance:Manage bandwidth consumption, such as through throttlingCompress data before transfer to reduce network trafficRun multithreaded or concurrent process for data migration tasks | Managed bandwidth consumptionMultithreaded or concurrent process support |
| **Security**<br />The ability to secure the product and data transfers:Encrypt data in transit from source to destinationSupport the use of customer-provided encryption keysStore all actions requested by the user and performed by the tool in a tamper-proof audit logIntegrate with third-party identity providers for authentication | Encrypt data in transit from source to destinationStore all actions requested by the user and performed by the tool in a tamper-proof audit logIntegrate with third-party identity providers for authentication |
| **Synchronization type**<br />The ability to support multiple data-synchronization options:One-time transferPeriodic transferContinuous transfer | One-time transferPeriodic transferContinuous transfer |
| **File-transfer options**<br />The ability to support file migration options:Track all files copied previously and compare against source data in the subsequent copyCopy only modified portions of a file instead of the entire fileSupport include or exclude patterns for copying files and folders with simple or regular expression patterns | Changed-file trackingInclude or exclude patterns |
| **NFS and SMB options**<br />For Network File System (NFS) and Server Message Block (SMB) file systems, the ability to do the following:Preserve symbolic linkPreserve hard linkMove open files | Preserve symbolic linkPreserve hard link |
| **Data validation**<br />The ability to validate data transfers by using checksums for data integrity | Available |
| **Discovery**<br />The ability to scan and report on source system data (such as file name, type, size, usage, file timestamps, and summary statistics) and produce a pre-migration assessment report | Available |
| **Reporting and alerting**<br />The ability to report on data-transfer progress and statistics:File and object transfer statisticsNetwork statisticsTime and duration statistics, including time taken and forecast completionGeneration of a detailed post-migration reportGeneration of a full validation report after migration completionAlerting on failure scenarios, job completion | File and object transfer statisticsNetwork statisticsTime and duration statistics, including time taken and forecast completionGeneration of a detailed post-migration reportGeneration of a full validation report after migration completionAlerting on failure scenarios, job completion |
| **Failure handling**<br />The ability to retry transfer operations if a network failure or connectivity issue occurs | Available |

## Database migration
<a name="kompise-database-migration"></a>

Not available
