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
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + Servers deployed on AWS (customer VPC)<br />+ SaaS on AWS (vendor VPC)<br />+ Servers deployed on premises in customer environment<br />+ SaaS or servers in other cloud provider environment |
| **Compliance** | System and Organization Controls 2 (SOC 2) |
| **Service model** | Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support |
| **Pricing model** | Subscription |

## Data migration
<a name="data-mobility-kompise-data-migration"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Replication method**<br />The ability to support one or more of the following replication methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Agent-based |
| **Replication source**<br />Support for one or more of the following sources:+ Block<br />+ File<br />+ Object<br />+ Tape<br />+ Other | + File<br />+ Object<br />+ Other – Any NFS, SMB, Object interface (including tape with file front-end) |
| **Automation**<br />The ability to manage a migration through scheduling controls:+ Product can be accessed, configured, and managed programmatically<br />+ Product can schedule migration jobs<br />+ Product can pause and resume migrations<br />+ Product can schedule bandwidth throttling (for example, to increase throughput during off-peak periods) | + Access programmatically<br />+ Schedule migrations<br />+ Pause and resume migration<br />+ Schedule bandwidth throttling |
| **Performance**<br />The ability to optimize performance:+ Manage bandwidth consumption, such as through throttling<br />+ Compress data before transfer to reduce network traffic<br />+ Run multithreaded or concurrent process for data migration tasks | + Managed bandwidth consumption<br />+ Multithreaded or concurrent process support |
| **Security**<br />The ability to secure the product and data transfers:+ Encrypt data in transit from source to destination<br />+ Support the use of customer-provided encryption keys<br />+ Store all actions requested by the user and performed by the tool in a tamper-proof audit log<br />+ Integrate with third-party identity providers for authentication | + Encrypt data in transit from source to destination<br />+ Store all actions requested by the user and performed by the tool in a tamper-proof audit log<br />+ Integrate with third-party identity providers for authentication |
| **Synchronization type**<br />The ability to support multiple data-synchronization options:+ One-time transfer<br />+ Periodic transfer<br />+ Continuous transfer | + One-time transfer<br />+ Periodic transfer<br />+ Continuous transfer |
| **File-transfer options**<br />The ability to support file migration options:+ Track all files copied previously and compare against source data in the subsequent copy<br />+ Copy only modified portions of a file instead of the entire file<br />+ Support include or exclude patterns for copying files and folders with simple or regular expression patterns | + Changed-file tracking<br />+ Include or exclude patterns |
| **NFS and SMB options**<br />For Network File System (NFS) and Server Message Block (SMB) file systems, the ability to do the following:+ Preserve symbolic link<br />+ Preserve hard link<br />+ Move open files | + Preserve symbolic link<br />+ Preserve hard link |
| **Data validation**<br />The ability to validate data transfers by using checksums for data integrity | Available |
| **Discovery**<br />The ability to scan and report on source system data (such as file name, type, size, usage, file timestamps, and summary statistics) and produce a pre-migration assessment report | Available |
| **Reporting and alerting**<br />The ability to report on data-transfer progress and statistics:+ File and object transfer statistics<br />+ Network statistics<br />+ Time and duration statistics, including time taken and forecast completion<br />+ Generation of a detailed post-migration report<br />+ Generation of a full validation report after migration completion<br />+ Alerting on failure scenarios, job completion | + File and object transfer statistics<br />+ Network statistics<br />+ Time and duration statistics, including time taken and forecast completion<br />+ Generation of a detailed post-migration report<br />+ Generation of a full validation report after migration completion<br />+ Alerting on failure scenarios, job completion |
| **Failure handling**<br />The ability to retry transfer operations if a network failure or connectivity issue occurs | Available |

## Database migration
<a name="kompise-database-migration"></a>

Not available

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
