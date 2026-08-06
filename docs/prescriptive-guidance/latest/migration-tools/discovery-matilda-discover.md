---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-matilda-discover.html
---

# Matilda Discover
<a name="discovery-matilda-discover"></a>

*Last update: May 15, 2023*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-matilda-discover-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Matilda Discover](https://www.matildacloud.com/products) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Discovery, Planning, and Recommendation |
| **AWS Marketplace**<br />Link to subscribe or download | Not available |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + SaaS on AWS (vendor VPC)<br />+ Servers deployed on AWS (customer VPC)<br />+ Servers deployed on premises in customer environment<br />+ SaaS or servers in other cloud provider environment |
| **Compliance** | International Organization for Standardization (ISO) 27001 |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support<br />+ Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-matilda-discover-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | + Agentless<br />+ Agent-based<br />+ Login-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | + Servers and operating systems<br />+ Databases<br />+ Storage systems<br />+ Network devices<br />+ Software processes<br />+ Containers |
| **Operating systems discoverable** | + Linux – Ubuntu 12.04\+, Red Hat Enterprise Linux (RHEL) 5\+, CentOS 5\+, Oracle Enterprise 5\+, SUSE 11\+<br />+ Microsoft – Windows 2003 and later<br />+ HP – HP-UX 11 and later<br />+ Solaris – Solaris 10\+<br />+ IBM – IBM AIX 6\+ |
| **Other resources discoverable** | + Applications<br />+ Application interdependencies<br />+ Firewall rules<br />+ Client app DNS<br />+ IP addresses and DNS<br />+ Machine details<br />+ Microsoft SQL Server license discovery<br />+ Load balancers (hardware and software)<br />+ Storage devices<br />+ Network devices |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | + Physical and virtual servers and their profiles<br />+ Attached storage and profiles – data storage device connected directly to a server or virtual machine (VM)<br />+ Detached storage and profiles – data storage accessed over a network such as network-attached storage (NAS) and storage area network (SAN)<br />+ Network devices and profiles |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | + Physical and virtual server utilization data collection<br />+ Attached storage utilization data collection<br />+ Detached storage utilization data collection<br />+ Network utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:+ Application and server dependency – Individual servers and dependencies that form an application<br />+ Application and software process dependency – Individual software processes, configurations, and dependencies that form an application<br />+ Application and code dependency – Individual programming code, configurations, and dependencies that form an application | + Application and server dependency<br />+ Application and software process dependency<br />+ Application and code dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:+ All resource and applications – An entire on-premises or source environment with all resources and applications<br />+ Single application – A single application across its resources, end to end<br />+ Single application and its software processes – Individual software processes and dependencies that form an application<br />+ Single application and its programming code – Individual programming code and dependencies that form an application | + All resource and applications<br />+ Single application<br />+ Single application and its software processes |
| **Database details discovery, source database system** | + Database engine<br />+ Database editions<br />+ Schemas<br />+ Database size<br />+ Number of partitions<br />+ Clustering and servers in the cluster<br />+ Backups<br />+ Failover configuration (active-active, active-standby)<br />+ Runtime metrics (for example, server memory usage, client connections, transactions, batch requests) |
| **Database details discovery, database type** | + MariaDB<br />+ Microsoft SQL Server<br />+ MongoDB<br />+ MySQL<br />+ Oracle<br />+ PostgreSQL<br />+ Redis<br />+ SQLite |
| **Storage details discovery, systems** | + Local storage<br />+ Storage Area Network (SAN)<br />+ Network Attached Storage (NAS) |
| **Storage details discovery, types**<br />The ability to discover storage system types and access protocols | + File storage (for example, NFS or SMB)<br />+ Block storage (for example, Fiber Channel or iSCSI)<br />+ Object storage (for example, Atmos, Vantara, HTTP, or REST) |
| **Storage details discovery, capacity** | + Volume identifier and volume size (GB)<br />+ Storage pool name and size (GB)<br />+ Storage raw total size, raw usable size (GB)<br />+ Used capacity (GB) |
| **Storage details discovery, configuration** | + Media types (for example, SSD, magnetic disks, tape)<br />+ RAID levels (RAID 0, RAID 1, …, RAID 6) |
| **Storage details discovery, utilization** | + Mean (average) IOPS<br />+ Peak IOPS<br />+ Mean (average) throughput (MB per second)<br />+ Peak throughput (MB per second)<br />+ Mean disk latency (milliseconds)<br />+ Peak disk latency (milliseconds) |
| **Storage details discovery, object metadata** | + Object type (for example, text file, image, database data)<br />+ Object size (MB) |
| **Storage systems discoverable**<br />The ability to discovery storage systems, such as EMC Isilon, EMC VMAX, Hitachi Vantara, HPE 3PAR, and Pure Storage | Provided that SNMP is enabled |
| **File system details discovery** | + File system types (for example, disk, tape)<br />+ File system configuration (for example, clustering, mount point)<br />+ Directory locations or hierarchies, size, size used, or file access frequency |
| **Software details discovery, programming languages** | Java, .NET, Python, Ruby, NodeJS, Angular, React |
| **Software details discovery, frameworks or libraries** | Platform can identify all Java, .NET, Python, and Ruby based application frameworks. Platform can detect AngularJS, ReactJS frameworks. Applications running in Spring Boot services, Kubernetes platform. Other platforms such as Hadoop, SAP, and ERP systems. |
| **Software details discovery, ISV products**<br />The ability to discover independent software vendor (ISV) products, such as Splunk Enterprise or F5 BIG-IP Virtual Edition | Name, edition, and version |
| **Container details discovery** | + Docker<br />+ Kubernetes |
| **License discovery** | + Microsoft – Microsoft SQL Server, Windows operating systems, Hyper-V, Microsoft Office, Microsoft Active Directory<br />+ Oracle – Oracle Database, Oracle EBS applications, Oracle WebLogicPlatform can extract software licenses for a variety of application software, including software IBM Db2, Informix, SAP Systems, IBM WebSphere, Oracle WebLogic, Microsoft IIS, Red Hat JBoss, and WildFly |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
