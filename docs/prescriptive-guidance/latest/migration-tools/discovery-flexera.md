---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-flexera.html
---

# Flexera Cloud Migration and Modernization
<a name="discovery-flexera"></a>

*Last update: May 15, 2023*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-flexera-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Flexera](https://www.flexera.com/solutions/cloud-cost/cloud-migration) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Discovery, Planning, and Recommendation |
| **AWS Marketplace**<br />Link to subscribe or download | [Flexera Cloud Migration and Modernization on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-ippp4uyj2nrey) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | SaaS on AWS (vendor VPC)Servers deployed on AWS (customer VPC)Servers deployed on premises in customer environment |
| **Compliance** | APP EntityGeneral Data Protection Regulation (GDPR)Health Insurance Portability and Accountability Act (HIPAA)Payment card industry (PCI)System and Organization Controls (SOC) |
| **Service model** | Full self-service – Deployment, management, and maintenance can be done by the customer or end-userSelf-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor supportManaged service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-flexera-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:Agentless – Uses protocols or interfaces such as SNMP or WMIAgent-based – Requires installation of software on the source resources, such as Linux or Windows serversLogin-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Agentless |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | Servers and operating systemsDatabasesStorage systemsNetwork devicesSoftware processes |
| **Operating systems discoverable** | Linux – CentOS (5.x, 6.x, 7.x), Red Hat Enterprise Linux (RHEL), SUSE, Ubuntu (12.04, 14.04, 16.04)WindowsOther – IBM AIX, Oracle, Unix |
| **Other resources discoverable** | Basic equipment (IP phones, printers, fax machines), databases, load balancers (NetScaler, F5 Networks), network equipment (switches, routers, firewalls, etc.), SUSE Linux Enterprise Server (9, 10, 11, 12) |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | Physical and virtual servers and their profilesAttached storage and profiles – data storage device connected directly to a server or virtual machine (VM)Detached storage and profiles – data storage accessed over a network such as network-attached storage (NAS) and storage area network (SAN)Network devices and profiles |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | Physical and virtual server utilization data collectionAttached storage utilization data collectionDetached storage utilization data collectionNetwork utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:Application and server dependency – Individual servers and dependencies that form an applicationApplication and software process dependency – Individual software processes, configurations, and dependencies that form an applicationApplication and code dependency – Individual programming code, configurations, and dependencies that form an application | Application and server dependencyApplication and software process dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:All resource and applications – An entire on-premises or source environment with all resources and applicationsSingle application – A single application across its resources, end to endSingle application and its software processes – Individual software processes and dependencies that form an applicationSingle application and its programming code – Individual programming code and dependencies that form an application | All resource and applicationsSingle applicationSingle application and its software processes |
| **Database details discovery, source database system** | Database engineDatabase editionsSchemasDatabase sizeMapping to storage via storage layers (for example, mapping of tablespaces via Automatic Storage Management file system for Oracle)Runtime metrics (for example, server memory usage, client connections, transactions, batch requests) |
| **Database details discovery, database type** | Microsoft SQL ServerMySQLOracle |
| **Storage details discovery, systems** | Local storageNetwork Attached Storage (NAS) |
| **Storage details discovery, types**<br />The ability to discover storage system types and access protocols | File storage (for example, NFS or SMB)Block storage (for example, Fiber Channel or iSCSI) |
| **Storage details discovery, capacity** | Volume identifier and volume size (GB)Storage raw total size, raw usable size (GB)Used capacity (GB) |
| **Storage details discovery, utilization** | Mean (average) IOPSPeak IOPSMean (average) throughput (MB per second)Peak disk latency (milliseconds) |
| **Storage systems discoverable**<br />The ability to discovery storage systems, such as EMC Isilon, EMC VMAX, Hitachi Vantara, HPE 3PAR, and Pure Storage | Based on credential support |
| **File system details discovery** | File system types (for example, disk, tape)File system configuration (for example, clustering, mount point)Directory locations or hierarchies, size, size used, or file access frequency |
| **Software details discovery, programming languages** | C\+\+, Fortran, Java, JavaScript, PHP, Python, SQL, essentially anything that is discovered in the Process List |
| **Software details discovery, frameworks or libraries** | Apache, Apache Tomcat, ASP.NET, BSD, Microsoft IIS, Java, Red Hat JBoss, NGen, Open Toolkit |
| **Software details discovery, tools** | Any tool with an on-premises component |
| **Software details discovery, ISV products**<br />The ability to discover independent software vendor (ISV) products, such as Splunk Enterprise or F5 BIG-IP Virtual Edition | Name, edition, and version |
| **Container details discovery** | Not available |
| **License discovery** | Microsoft – Microsoft SQL Server, WindowsOracle – All licenses publicly from vendorApplication software – All licenses publicly from vendor |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
