---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-migration-evaluator.html
---

# Migration Evaluator
<a name="discovery-migration-evaluator"></a>

*Last update: May 15, 2023*

## Product overview
<a name="discovery-migration-evaluator-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) |
| **Request for discovery assessment**<br />The ability to provide a business case to make sound AWS planning and migration decisions | [Submit request](https://pages.awscloud.com/Migration-Evaluator-request.html) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | Servers deployed on premises in customer environment |
| **Compliance** | General Data Protection Regulation (GDPR) |
| **Service model** | Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | No charge |

## Discovery, planning, and recommendation capabilities
<a name="discovery-migration-evaluator-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:Agentless – Uses protocols or interfaces such as SNMP or WMIAgent-based – Requires installation of software on the source resources, such as Linux or Windows serversLogin-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Agentless |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | Servers and operating systemsDatabases |
| **Operating systems discoverable** | LinuxWindows |
| **Other resources discoverable** | Virtualization stacks |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | Physical and virtual servers and their profilesAttached storage and profiles – data storage device connected directly to a server or virtual machine (VM) |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | Physical and virtual server utilization data collectionAttached storage utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:Application and server dependency – Individual servers and dependencies that form an applicationApplication and software process dependency – Individual software processes, configurations, and dependencies that form an applicationApplication and code dependency – Individual programming code, configurations, and dependencies that form an application | Application and server dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:All resource and applications – An entire on-premises or source environment with all resources and applicationsSingle application – A single application across its resources, end to endSingle application and its software processes – Individual software processes and dependencies that form an applicationSingle application and its programming code – Individual programming code and dependencies that form an application | All resources and applications through AWS Migration Hub |
| **Database details discovery, source database system** | Database engineDatabase editionsClustering and servers in the clusterFailover configuration (active-active, active-standby) |
| **Database details discovery, database type** | Microsoft SQL Server |
| **Storage details discovery, systems** | Local storage |
| **Storage details discovery, types**<br />The ability to discover storage system types and access protocols | Block storage (for example, Fiber Channel or iSCSI) |
| **Storage details discovery, capacity** | Volume identifier and volume size (GB)Storage raw total size, raw usable size (GB)Used capacity (GB) |
| **File system details discovery** | Not available |
| **Software details discovery** | Not available |
| **Container details discovery** | Not available |
| **License discovery** | Microsoft SQL Server version and edition |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
