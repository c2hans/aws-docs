---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-corent.html
---

# Corent SurPaas MaaS
<a name="discovery-corent"></a>

*Last update: May 15, 2023*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-corent-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Corent SurPaas MaaS](https://www.corenttech.com/SurPaaS_MaaS_Product.html) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Discovery, Planning, and Recommendation |
| **AWS Marketplace**<br />Link to subscribe or download | [Corent MaaS on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-mvp2a5il675ra) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | SaaS on AWS (vendor VPC) |
| **Compliance** | International Organization for Standardization (ISO) 27001 |
| **Service model** | Full self-service – Deployment, management, and maintenance can be done by the customer or end-userSelf-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor supportManaged service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-corent-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:Agentless – Uses protocols or interfaces such as SNMP or WMIAgent-based – Requires installation of software on the source resources, such as Linux or Windows serversLogin-based – Uses protocols, such as SSH and RDP, to log in to the source servers | AgentlessAgent-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | Servers and operating systemsDatabasesStorage systemsSoftware processes |
| **Operating systems discoverable** | LinuxWindowsOther – IBM AIX, HP-X, Solaris |
| **Other resources discoverable** | Dependency mappingPerformance monitoring |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | Physical and virtual servers and their profilesAttached storage and profiles – data storage device connected directly to a server or virtual machine (VM)Detached storage and profiles – data storage accessed over a network such as network-attached storage (NAS) and storage area network (SAN) |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | Physical and virtual server utilization data collectionAttached storage utilization data collectionDetached storage utilization data collectionNetwork utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:Application and server dependency – Individual servers and dependencies that form an applicationApplication and software process dependency – Individual software processes, configurations, and dependencies that form an applicationApplication and code dependency – Individual programming code, configurations, and dependencies that form an application | Application and server dependencyApplication and software process dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:All resource and applications – An entire on-premises or source environment with all resources and applicationsSingle application – A single application across its resources, end to endSingle application and its software processes – Individual software processes and dependencies that form an applicationSingle application and its programming code – Individual programming code and dependencies that form an application | All resource and applicationsSingle applicationSingle application and its software processes |
| **Database details discovery, source database system** | Database engineDatabase editionsSchemasDatabase sizeClustering and servers in the clusterFailover configuration (active-active, active-standby) |
| **Database details discovery, database type** | MariaDBMicrosoft SQL ServerMySQLOraclePostgreSQL |
| **Storage details discovery, systems** | Local storageStorage Area Network (SAN)Network Attached Storage (NAS) |
| **Storage details discovery, capacity** | Volume identifier and volume size (GB)Storage pool name and size (GB)Storage raw total size, raw usable size (GB)Used capacity (GB) |
| **Storage details discovery, configuration** | Media types (for example, SSD, magnetic disks, tape)LUN in SAN SCSI environment |
| **File system details discovery** | File system types (for example, disk, tape)File system configuration (for example, clustering, mount point)Directory locations or hierarchies, size, size used, or file access frequency |
| **Software details discovery, programming languages** | .NET, Java, Perl, PHP, Python, Ruby |
| **Software details discovery, frameworks or libraries** | Apache, Apache Tomcat, ASP.NET, Apache Tomcat, Microsoft IIS, Red Hat JBoss, IBM WebSphere |
| **Software details discovery, tools** | CRM, document management, ERP, SAP, Microsoft SharePoint |
| **Container details discovery** | Not available |
| **License discovery** | Microsoft – Windows, Microsoft SQL ServerOracle – Oracle Database |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
