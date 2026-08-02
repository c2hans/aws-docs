---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-new-relic-one.html
---

# New Relic One
<a name="discovery-new-relic-one"></a>

*Last update: May 15, 2023*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-new-relic-one-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [New Relic](https://newrelic.com/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Application Monitoring and Orchestration |
| **AWS Marketplace**<br />Link to subscribe or download | [New Relic Infrastructure and Application Monitoring on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-ov56chowabeb4) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | SaaS on AWS (vendor VPC)SaaS or servers in other cloud provider environment |
| **Compliance** | Federal Risk and Authorization Management Program (FedRAMP) moderateGeneral Data Protection Regulation (GDPR)Health Insurance Portability and Accountability Act (HIPAA)Payment card industry (PCI)System and Organization Controls (SOC) |
| **Service model** | Full self-service – Deployment, management, and maintenance can be done by the customer or end-userSelf-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor supportManaged service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-new-relic-one-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:Agentless – Uses protocols or interfaces such as SNMP or WMIAgent-based – Requires installation of software on the source resources, such as Linux or Windows serversLogin-based – Uses protocols, such as SSH and RDP, to log in to the source servers | AgentlessAgent-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | Servers and operating systemsDatabasesSoftware processesContainers |
| **Operating systems discoverable** | LinuxWindows |
| **Other resources discoverable** | No additional information |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | Physical and virtual servers and their profiles |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | Physical and virtual server utilization data collectionAttached storage utilization data collectionDetached storage utilization data collectionNetwork utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:Application and server dependency – Individual servers and dependencies that form an applicationApplication and software process dependency – Individual software processes, configurations, and dependencies that form an applicationApplication and code dependency – Individual programming code, configurations, and dependencies that form an application | Application and server dependencyApplication and software process dependencyApplication and code dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:All resource and applications – An entire on-premises or source environment with all resources and applicationsSingle application – A single application across its resources, end to endSingle application and its software processes – Individual software processes and dependencies that form an applicationSingle application and its programming code – Individual programming code and dependencies that form an application | All resource and applicationsSingle applicationSingle application and its software processesSingle application and its programming code |
| **Database details discovery, source database system** | Database engineDatabase editionsDatabase sizeClustering and servers in the clusterFailover configuration (active-active, active-standby)Runtime metrics (for example, server memory usage, client connections, transactions, batch requests) |
| **Storage details discovery**<br />The ability to discover storage details, such as systems, types, capacity, configuration, utilization, and object metadata | Not available |
| **File system details discovery** | File system types (for example, disk, tape)File system configuration (for example, clustering, mount point)Directory locations or hierarchies, size, size used, or file access frequency |
| **Software details discovery, programming languages** | .NET C\#, Go, Java, Node, PHP, Python, Ruby |
| **Software details discovery, frameworks or libraries** | Apache Tomcat, ASP.NET, most modern Java frameworks |
| **Software details discovery, ISV products**<br />The ability to discover independent software vendor (ISV) products, such as Splunk Enterprise or F5 BIG-IP Virtual Edition | Name, edition, and version |
| **Container details discovery** | DockerKubernetesRed Hat OpenShift |
| **License discovery** | Not available |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
