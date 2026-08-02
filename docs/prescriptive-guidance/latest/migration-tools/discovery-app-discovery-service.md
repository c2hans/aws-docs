---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-app-discovery-service.html
---

# AWS Application Discovery Service
<a name="discovery-app-discovery-service"></a>

*Last update: May 15, 2023*

## Product overview
<a name="discovery-app-discovery-service-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [AWS Application Discovery Service](https://aws.amazon.com/application-discovery/) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | SaaS on AWS (vendor VPC)Servers deployed on premises in customer environment |
| **Compliance** | Not available |
| **Service model** | Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support |
| **Pricing model** | No charge |

## Discovery, planning, and recommendation capabilities
<a name="discovery-app-discovery-service-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:Agentless – Uses protocols or interfaces such as SNMP or WMIAgent-based – Requires installation of software on the source resources, such as Linux or Windows serversLogin-based – Uses protocols, such as SSH and RDP, to log in to the source servers | AgentlessAgent-basedLogin-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | Servers and operating systemsDatabasesSoftware processes |
| **Operating systems discoverable** | LinuxWindows |
| **Other resources discoverable** | No additional information |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | Physical and virtual servers and their profilesAttached storage and profiles – data storage device connected directly to a server or virtual machine (VM) |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | Physical and virtual server utilization data collectionAttached storage utilization data collectionNetwork utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:Application and server dependency – Individual servers and dependencies that form an applicationApplication and software process dependency – Individual software processes, configurations, and dependencies that form an applicationApplication and code dependency – Individual programming code, configurations, and dependencies that form an application | Application and server dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:All resource and applications – An entire on-premises or source environment with all resources and applicationsSingle application – A single application across its resources, end to endSingle application and its software processes – Individual software processes and dependencies that form an applicationSingle application and its programming code – Individual programming code and dependencies that form an application | All resource and applicationsSingle application |
| **Database details discovery, source database system** | Database engineDatabase editionsSchemasDatabase sizeRuntime metrics (for example, server memory usage, client connections, transactions, batch requests) |
| **Database details discovery, database type** | Microsoft SQL ServerMySQLOraclePostgreSQL |
| **Storage details discovery, systems** | Local storage |
| **Storage details discovery, utilization** | Mean (average) IOPSPeak IOPSMean (average) throughput (MB per second)Peak throughput (MB per second) |
| **File system details discovery** | Not available |
| **Software details discovery** | Not available |
| **Container details discovery** | Not available |
| **License discovery** | Not available |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Not available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
