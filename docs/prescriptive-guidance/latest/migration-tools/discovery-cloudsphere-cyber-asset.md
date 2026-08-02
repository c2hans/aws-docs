---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-cloudsphere-cyber-asset.html
---

# CloudSphere Cyber Asset Management Platform
<a name="discovery-cloudsphere-cyber-asset"></a>

*Last update: May 15, 2023*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-cloudsphere-cyber-asset-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [CloudSphere Cyber Asset Management Platform](https://cloudsphere.com/solutions/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization Competency – Migration |
| **AWS Marketplace**<br />Link to subscribe or download | [Cyber Asset Management (CAM) Platform on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-mtwm6kkcvydfe) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | SaaS on AWS (vendor VPC) |
| **Compliance** | General Data Protection Regulation (GDPR)System and Organization Controls 2 (SOC 2) Type II |
| **Service model** | Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-cloudsphere-cyber-asset-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:Agentless – Uses protocols or interfaces such as SNMP or WMIAgent-based – Requires installation of software on the source resources, such as Linux or Windows serversLogin-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Agentless – WindowsLogin-based – Linux or Unix |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | Servers and operating systemsDatabasesSoftware processesContainers |
| **Operating systems discoverable** | WindowsLinux – Amazon Linux, CentOS, Debian GNU/Linux, Fedora Linux, Oracle Linux, Red Hat Enterprise Linux (RHEL), SUSESolarisIBM AIXHP-UX |
| **Other resources discoverable** | ApplicationsApplication interdependenciesMicrosoft SQL Server license discoveryMachine detailsSoftware relationshipsNetwork dependenciesPerformance metricsIP addresses and DNSClustersCyber asset details |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | Physical and virtual servers and their profilesAttached storage and profiles – data storage device connected directly to a server or virtual machine (VM) |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | Physical and virtual server utilization data collectionAttached storage utilization data collectionNetwork utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:Application and server dependency – Individual servers and dependencies that form an applicationApplication and software process dependency – Individual software processes, configurations, and dependencies that form an applicationApplication and code dependency – Individual programming code, configurations, and dependencies that form an application | Application and server dependencyApplication and software process dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:All resource and applications – An entire on-premises or source environment with all resources and applicationsSingle application – A single application across its resources, end to endSingle application and its software processes – Individual software processes and dependencies that form an applicationSingle application and its programming code – Individual programming code and dependencies that form an application | All resource and applicationsSingle applicationSingle application and its software processes |
| **Database details discovery, source database system** | Database engineDatabase editionsSchemasDatabase sizeNumber of partitionsClustering and servers in the cluster |
| **Database details discovery, database type** | MariaDBMicrosoft SQL ServerMongoDBMySQLOraclePostgreSQLRedisSQLite |
| **Storage details discovery, systems** | Local storage |
| **Storage details discovery, capacity** | Volume identifier and volume size (GB)Storage raw total size, raw usable size (GB)Used capacity (GB) |
| **Storage details discovery, utilization** | Mean (average) IOPSPeak IOPSMean (average) throughput (MB per second)Peak throughput (MB per second) |
| **File system details discovery** | File system configuration (for example, clustering, mount point)Directory locations or hierarchies, size, size used, or file access frequency |
| **Software details discovery, programming languages** | Not available |
| **Software details discovery, frameworks or libraries** | Not available |
| **Software details discovery, ISV products**<br />The ability to discover independent software vendor (ISV) products, such as Splunk Enterprise or F5 BIG-IP Virtual Edition | Any software installed using OS provided installation and packaging system mechanism |
| **Container details discovery** | Docker |
| **License discovery** | Microsoft – Microsoft SQL Server, Windows Server |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Not available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
