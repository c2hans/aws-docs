---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/data-mobility-vcinity.html
---

# Vcinity Ultimate X
<a name="data-mobility-vcinity"></a>

*Last update: November 15, 2024*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="data-mobility-vcinity-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Vcinity Ultimate X](https://vcinity.io/product-ultimate-x/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | Migration and Modernization ISV Competency |
| **AWS Marketplace**<br />Link to subscribe or download | [Vcinity Ultimate X on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-cjqv6x62n2wes) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | Servers deployed on AWS (customer VPC)Servers deployed on premises in customer environment |
| **Compliance** | Not available |
| **Service model** | Full self-service – Deployment, management, and maintenance can be done by the customer or end-userSelf-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support |
| **Pricing model** | Subscription |

## Data migration
<a name="data-mobility-vcinity-data-migration"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Replication method**<br />The ability to support one or more of the following replication methods:Agentless – Uses protocols or interfaces such as SNMP or WMIAgent-based – Requires installation of software on the source resources, such as Linux or Windows serversLogin-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Login-based |
| **Replication source**<br />Support for one or more of the following sources:BlockFileObjectTapeOther | FileObject |
| **Automation**<br />The ability to manage a migration through scheduling controls:Product can be accessed, configured, and managed programmaticallyProduct can schedule migration jobsProduct can pause and resume migrationsProduct can schedule bandwidth throttling (for example, to increase throughput during off-peak periods) | Access programmatically |
| **Performance**<br />The ability to optimize performance:Manage bandwidth consumption, such as through throttlingCompress data before transfer to reduce network trafficRun multithreaded or concurrent process for data migration tasks | Managed bandwidth consumptionCompression before transferMultithreaded or concurrent process support |
| **Security**<br />The ability to secure the product and data transfers:Encrypt data in transit from source to destinationSupport the use of customer-provided encryption keysStore all actions requested by the user and performed by the tool in a tamper-proof audit logIntegrate with third-party identity providers for authentication | Encrypt data in transit from source to destinationSupport the use of customer-provided encryption keysStore all actions requested by the user and performed by the tool in a tamper-proof audit log |
| **Synchronization type**<br />The ability to support multiple data-synchronization options:One-time transferPeriodic transferContinuous transfer | One-time transfer |
| **File-transfer options**<br />The ability to support file migration options:Track all files copied previously and compare against source data in the subsequent copyCopy only modified portions of a file instead of the entire fileSupport include or exclude patterns for copying files and folders with simple or regular expression patterns | Not available |
| **NFS and SMB options**<br />For Network File System (NFS) and Server Message Block (SMB) file systems, the ability to do the following:Preserve symbolic linkPreserve hard linkMove open files | Not available |
| **Data validation**<br />The ability to validate data transfers by using checksums for data integrity | Available |
| **Discovery**<br />The ability to scan and report on source system data (such as file name, type, size, usage, file timestamps, and summary statistics) and produce a pre-migration assessment report | Not available |
| **Reporting and alerting**<br />The ability to report on data-transfer progress and statistics:File and object transfer statisticsNetwork statisticsTime and duration statistics, including time taken and forecast completionGeneration of a detailed post-migration reportGeneration of a full validation report after migration completionAlerting on failure scenarios, job completion | File and object transfer statisticsNetwork statisticsTime and duration statistics, including time taken and forecast completionGeneration of a detailed post-migration reportGeneration of a full validation report after migration completionAlerting on failure scenarios, job completion |
| **Failure handling**<br />The ability to retry transfer operations if a network failure or connectivity issue occurs | Available |

## Database migration
<a name="data-mobility-vcinity-database-migration"></a>

Not available
