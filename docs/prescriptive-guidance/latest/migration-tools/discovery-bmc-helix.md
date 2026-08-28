---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-bmc-helix.html
---

# BMC Helix Discovery
<a name="discovery-bmc-helix"></a>

*Last update: May 15, 2023*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-bmc-helix-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [BMC Helix Discovery](https://www.helixops.ai/products/bmc-helix-discovery.html) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Discovery, Planning, and Recommendation |
| **AWS Marketplace**<br />Link to subscribe or download | [BMC Helix on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-x6tfnnqvb6mli) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + SaaS on AWS (vendor VPC)<br />+ Servers deployed on AWS (customer VPC)<br />+ Servers deployed on premises in customer environment<br />+ SaaS or servers in other cloud provider environment |
| **Compliance** | + General Data Protection Regulation (GDPR)<br />+ Health Insurance Portability and Accountability Act (HIPAA)<br />+ Payment card industry (PCI)<br />+ System and Organization Controls (SOC) |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support<br />+ Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-bmc-helix-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | + Agentless<br />+ Login-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | + Servers and operating systems<br />+ Databases<br />+ Storage systems<br />+ Network devices<br />+ Software processes<br />+ Containers<br />+ Mainframe |
| **Operating systems discoverable** | + Linux – CentOS, Debian GNU/Linux, Fedora Linux, Gentoo Linux, Oracle, Red Hat Enterprise Linux (RHEL), Scientific Linux, SUSE, Ubuntu<br />+ Windows – Windows NT, Windows Server 2000 to 2019<br />+ HP – HP-UX, OpenVMS, Tru64 UNIX<br />+ IBM – IBM AIX, IBMi, Power HMC, VIO<br />+ VMware – VMware ESX Server, VMware ESXi Server, VMware vCenter<br />+ Other – FreeBSD, Novell NetWare, OpenBSD, Oracle VM Server, Solaris |
| **Other resources discoverable** | + Hyper-converged infrastructure<br />+ Load balancers<br />+ Management controllers<br />+ Software-defined networks<br />+ Software-defined storage |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | + Physical and virtual servers and their profiles<br />+ Attached storage and profiles – data storage device connected directly to a server or virtual machine (VM)<br />+ Detached storage and profiles – data storage accessed over a network such as network-attached storage (NAS) and storage area network (SAN)<br />+ Network devices and profiles |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | Not available |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:+ Application and server dependency – Individual servers and dependencies that form an application<br />+ Application and software process dependency – Individual software processes, configurations, and dependencies that form an application<br />+ Application and code dependency – Individual programming code, configurations, and dependencies that form an application | + Application and server dependency<br />+ Application and software process dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:+ All resource and applications – An entire on-premises or source environment with all resources and applications<br />+ Single application – A single application across its resources, end to end<br />+ Single application and its software processes – Individual software processes and dependencies that form an application<br />+ Single application and its programming code – Individual programming code and dependencies that form an application | + All resource and applications<br />+ Single application<br />+ Single application and its software processes |
| **Database details discovery, source database system** | + Database engine<br />+ Database editions<br />+ Schemas<br />+ Database size<br />+ Number of partitions<br />+ Clustering and servers in the cluster<br />+ Backups<br />+ Failover configuration (active-active, active-standby) |
| **Storage details discovery, systems** | Storage Area Network (SAN) |
| **Storage details discovery, types**<br />The ability to discover storage system types and access protocols | + File storage (for example, NFS or SMB)<br />+ Block storage (for example, Fiber Channel or iSCSI)<br />+ Object storage (for example, Atmos, Vantara, HTTP, or REST) |
| **Storage details discovery, capacity** | Volume identifier and volume size (GB) |
| **Storage details discovery, configuration** | Relationships among disk, array, LUN, and VM |
| **Storage details discovery, utilization** | Not available |
| **Storage details discovery, object metadata** | Object type (for example, text file, image, database data) |
| **Storage systems discoverable**<br />The ability to discovery storage systems, such as EMC Isilon, EMC VMAX, Hitachi Vantara, HPE 3PAR, and Pure Storage | + Cisco HyperFlex<br />+ Dell Compellent, EMC Isilon, Dell EqualLogic<br />+ EMC Celerra/VNX(NAS) and eNAS, EMC Data Domain, EMC RecoverPoint, EMC Unity, EMC VMAX, EMC VNXe 3200, EMC VPLEX, EMC XtremIO<br />+ Fujitsu ETERNUS DS<br />+ Hitachi HCP, Hitachi HDI, Hitachi HNAS, Hitachi VSP<br />+ HPE 3PAR, HP P2000, HP P6000 (EVA), HP P9000/P9500, HPE XP7, HPE XP8<br />+ Huawei Dorado (V3, V6), Huawei OceanStor (V3, V5, 9000)<br />+ IBM DS6000, IBM DS8000, IBM FlashSystem, IBM SVC/Storwize, IBM XIV<br />+ NetApp, NetApp E-Series, NetApp SolidFire<br />+ Other – Nimble, Nutanix, Oracle ZFS, Pure FlashArray, VMware vSAN |
| **File system details discovery** | + File system types (for example, disk, tape)<br />+ File system configuration (for example, clustering, mount point)<br />+ Directory locations or hierarchies, size, size used, or file access frequency |
| **Software details discovery, frameworks or libraries** | Apache Tomcat, IBM WebSphere, Microsoft IIS, Oracle GlassFish, Oracle WebLogic, Oracle Application Server, PostgreSQL, Red Hat JBoss, Sybase, Teradata, and around 2,500 software instance types |
| **Software details discovery, tools** | BMC Remedy, BMC TrueSight, CA Spectrum, Chef, Dynatrace, Flexera, HP OpenView, IBM Tivoli, Microsoft SCCM, New Relic, and hundreds more |
| **Software details discovery, ISV products**<br />The ability to discover independent software vendor (ISV) products, such as Splunk Enterprise or F5 BIG-IP Virtual Edition | Name, edition, and version |
| **Container details discovery** | + Amazon Elastic Kubernetes Service (Amazon EKS)<br />+ Azure Kubernetes Service<br />+ CRI-O<br />+ Docker<br />+ Google Kubernetes Engine<br />+ Kubernetes<br />+ Red Hat OpenShift<br />+ Rocket |
| **License discovery** | Not available |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
