---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-modelizeit.html
---

# modelizeIT
<a name="discovery-modelizeit"></a>

*Last update: June 19, 2026*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-modelizeit-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [modelizeIT](https://www.modelizeit.com/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Discovery, Planning, and Recommendation |
| **AWS Marketplace**<br />Link to subscribe or download | [modelizeIT on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-xscuklaacfezg) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + SaaS on AWS (vendor VPC)<br />+ Servers deployed on AWS (customer VPC)<br />+ Servers deployed on premises in customer environment<br />+ SaaS or servers in other cloud provider environment |
| **Compliance** | + General Data Protection Regulation (GDPR)<br />+ System and Organization Controls (SOC) and other certifications are available through delivery partners<br />+ modelizeIT can be deployed fully within customer environments (including air-gapped environments) – in that model, compliance with standards such as PCI DSS and HIPAA are the customer's responsibility |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support<br />+ Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-modelizeit-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | + Agentless<br />+ Agent-based<br />+ Login-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | + Servers and operating systems<br />+ Databases<br />+ Storage systems<br />+ Network devices<br />+ Software processes<br />+ Containers<br />+ Mainframe |
| **Operating systems discoverable** | + Linux – Amazon Linux, Mainframe zLinux<br />+ Windows<br />+ Others – FreeBSD, HP-UX, Hyper-V, IBM AIX, OpenVMS, SCO UNIX, Solaris, Tru64 UNIX, VMware |
| **Other resources discoverable** | Hypervisors: Windows, Hyper-V, VMware, Kernel-based Virtual Machine (KVM), Xen, Oracle virtualization server, IBM AIX LPARs and WPARs, Solaris LDOMs and Zones, HP VPARs. Their configurations, clustering, and VMs. |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | + Physical and virtual servers and their profiles<br />+ Attached storage and profiles – data storage device connected directly to a server or virtual machine (VM)<br />+ Detached storage and profiles – data storage accessed over a network such as network-attached storage (NAS) and storage area network (SAN)<br />+ Network devices and profiles |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | + Physical and virtual server utilization data collection<br />+ Attached storage utilization data collection<br />+ Detached storage utilization data collection<br />+ Network utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:+ Application and server dependency – Individual servers and dependencies that form an application<br />+ Application and software process dependency – Individual software processes, configurations, and dependencies that form an application<br />+ Application and code dependency – Individual programming code, configurations, and dependencies that form an application | + Application and server dependency<br />+ Application and software process dependency<br />+ Application and code dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:+ All resource and applications – An entire on-premises or source environment with all resources and applications<br />+ Single application – A single application across its resources, end to end<br />+ Single application and its software processes – Individual software processes and dependencies that form an application<br />+ Single application and its programming code – Individual programming code and dependencies that form an application | + All resource and applications<br />+ Single application<br />+ Single application and its software processes<br />+ Single application and its programming code |
| **Database details discovery, source database system** | + Database engine<br />+ Database editions<br />+ Schemas<br />+ Database size<br />+ Number of partitions<br />+ Clustering and servers in the cluster<br />+ Backups<br />+ Failover configuration (active-active, active-standby)<br />+ Mapping to storage via storage layers (for example, mapping of tablespaces via Automatic Storage Management file system for Oracle)<br />+ Runtime metrics (for example, server memory usage, client connections, transactions, batch requests) |
| **Database details discovery, database type** | 34 engines, including:+ MariaDB<br />+ Microsoft SQL Server<br />+ MongoDB<br />+ MySQL<br />+ Oracle<br />+ PostgreSQL<br />+ Redis<br />+ SQLite |
| **Storage details discovery, systems** | + Local storage<br />+ Storage Area Network (SAN)<br />+ Network Attached Storage (NAS) |
| **Storage details discovery, types**<br />The ability to discover storage system types and access protocols | + File storage (for example, NFS or SMB)<br />+ Block storage (for example, Fiber Channel or iSCSI)<br />+ Object storage (for example, Atmos, Vantara, HTTP, or REST) |
| **Storage details discovery, capacity** | + Volume identifier and volume size (GB)<br />+ Storage pool name and size (GB)<br />+ Storage raw total size, raw usable size (GB)<br />+ Used capacity (GB) |
| **Storage details discovery, configuration** | + Media types (for example, SSD, magnetic disks, tape)<br />+ LUN in SAN SCSI environment<br />+ RAID levels (RAID 0, RAID 1, …, RAID 6)<br />+ Relationships among disk, array, LUN, and VM |
| **Storage details discovery, utilization** | + Mean (average) IOPS<br />+ Peak IOPS<br />+ Mean (average) throughput (MB per second)<br />+ Peak throughput (MB per second) |
| **Storage details discovery, object metadata** | + Object type (for example, text file, image, database data)<br />+ Object size (MB) |
| **Storage systems discoverable**<br />The ability to discovery storage systems, such as EMC Isilon, EMC VMAX, Hitachi Vantara, HPE 3PAR, and Pure Storage | EMC Isilon, NetApp filers, other devices from IBM, EMC, HP, Dell for which the information is discoverable at the client side |
| **File system details discovery** | + File system types (for example, disk, tape)<br />+ File system configuration (for example, clustering, mount point)<br />+ Directory locations or hierarchies, size, size used, or file access frequency |
| **Software details discovery, programming languages** | SAP ABAP, COBOL, Java, JavaScript, Perl, PHP, PowerShell, Python, Shell script, VBS |
| **Software details discovery, frameworks or libraries** | Apache Tomcat, Microsoft IIS, Red Hat JBoss, Oracle Containers for J2EE, Oracle WebLogic, IBM WebSphere, and others |
| **Software details discovery, tools** | More than 2,000 models for various software vendors |
| **Software details discovery, ISV products**<br />The ability to discover independent software vendor (ISV) products, such as Splunk Enterprise or F5 BIG-IP Virtual Edition | Name, edition, and version |
| **Container details discovery** | IBM AIX WPARs, Docker (including frameworks on top of Docker such as Red Hat OpenShift and Rancher), Solaris containers (including Zones), Virtuozzo/OpenVZ. Containers are mapped to the applications deployed on them and related inter-dependencies. |
| **License discovery** | + Microsoft – Windows, Microsoft SQL Server, Hyper-V (150\+ total Microsoft products)<br />+ Oracle – 150\+ Oracle products are identified. Editions and versions are identified for Oracle Database, Oracle WebLogic, and many other products. Usage of database options, packs, features is analyzed. Products are mapped to CPU pools on the physical hosts for virtual and physical servers via various virtualization and containerization technologies with consideration of Oracle CPU partitioning rules. CPU pools are mapped to the counts of required Oracle processor licenses according to the corresponding Oracle CPU factors.<br />+ Application software – IBM Db2, IBM WebSphere, and various other products from IBM, Red Hat, TIBCO, and 670\+ other vendors. |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
