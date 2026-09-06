---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-concierto-cloud.html
---

# Concierto.cloud
<a name="discovery-concierto-cloud"></a>

*Last update: November 17, 2025*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-concierto-cloud-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Concierto.cloud](https://www.concierto.cloud/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Discovery, Planning, and Recommendation |
| **AWS Marketplace**<br />Link to subscribe or download | [Concierto.cloud on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=f4eb933a-efc0-4e94-a0da-9a28bc819cc4) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + SaaS on AWS (vendor VPC)<br />+ Servers deployed on AWS (customer VPC)<br />+ Servers deployed on premises in customer environment<br />+ SaaS or servers in other cloud provider environment |
| **Compliance** | + General Data Protection Regulation (GDPR)<br />+ System and Organization Controls (SOC)<br />+ International Organization for Standardization (ISO) 27001:2022<br />+ National Institute of Standards and Technology (NIST) 800-53<br />+ CSA Star Level 2 |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-concierto-cloud-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Agentless |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | + Servers and operating systems<br />+ Databases<br />+ Storage systems<br />+ Network devices<br />+ Software processes |
| **Operating systems discoverable** | + Windows<br />+ Linux |
| **Other resources discoverable** | Not available |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | + Physical and virtual servers and their profiles<br />+ Network devices and profiles |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | + Physical and virtual server utilization data collection<br />+ Network utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:+ Application and server dependency – Individual servers and dependencies that form an application<br />+ Application and software process dependency – Individual software processes, configurations, and dependencies that form an application<br />+ Application and code dependency – Individual programming code, configurations, and dependencies that form an application | + Application and server dependency<br />+ Application and software process dependency<br />+ Application and code dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:+ All resource and applications – An entire on-premises or source environment with all resources and applications<br />+ Single application – A single application across its resources, end to end<br />+ Single application and its software processes – Individual software processes and dependencies that form an application<br />+ Single application and its programming code – Individual programming code and dependencies that form an application | + All resource and applications<br />+ Single application<br />+ Single application and its software processes<br />+ Single application and its programming code |
| **Database details discovery, source database system** | + Database engine<br />+ Database editions<br />+ Schemas<br />+ Database size<br />+ Number of partitions<br />+ Clustering and servers in the cluster<br />+ Backups<br />+ Failover configuration (active-active, active-standby)<br />+ Mapping to storage via storage layers (for example, mapping of tablespaces via Automatic Storage Management file system for Oracle)<br />+ Runtime metrics (for example, server memory usage, client connections, transactions, batch requests) |
| **Database details discovery, database type** | + Microsoft SQL Server<br />+ MongoDB<br />+ MySQL<br />+ Oracle<br />+ PostgreSQL |
| **Storage details discovery, systems** | Local storage |
| **Storage details discovery, capacity** | + Volume identifier and volume size (GB)<br />+ Storage raw total size, raw usable size (GB)<br />+ Used capacity (GB) |
| **Storage details discovery, configuration** | Media types (for example, SSD, magnetic disks, tape) |
| **Storage details discovery, utilization** | + Mean (average) IOPS<br />+ Peak IOPS<br />+ Mean (average) throughput (MB per second)<br />+ Peak throughput (MB per second)<br />+ Mean disk latency (milliseconds)<br />+ Peak disk latency (milliseconds) |
| **Storage details discovery, object metadata** | + Object type (for example, text file, image, database data)<br />+ Object size (MB) |
| **Storage systems discoverable**<br />The ability to discovery storage systems, such as EMC Isilon, EMC VMAX, Hitachi Vantara, HPE 3PAR, and Pure Storage | Not available |
| **File system details discovery** | + File system types (for example, disk, tape)<br />+ File system configuration (for example, clustering, mount point)<br />+ Directory locations or hierarchies, size, size used, or file access frequency |
| **Software details discovery, programming languages** | + ASP.NET<br />+ C\+\+<br />+ C\#<br />+ Java<br />+ JavaScript<br />+ JSP<br />+ PHP<br />+ VB.NET |
| **Software details discovery, frameworks or libraries** | + Apache Tomcat<br />+ Oracle WebLogic<br />+ IBM WebSphere<br />+ Nginx with all other frameworks discoverable along with legacy application |
| **Software details discovery, tools** | Concierto.cloud identifies all the installed and running software |
| **Software details discovery, ISV products**<br />The ability to discover independent software vendor (ISV) products, such as Splunk Enterprise or F5 BIG-IP Virtual Edition | Name, edition, and version |
| **Container details discovery** | Not available |
| **License discovery** | Not available |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
| **Code analysis**<br />The ability to support static and dynamic code analysis, optionally identifying:+ Deprecated code<br />+ Security concerns in code<br />+ Resilience concerns in code | + Security concerns in code<br />+ Resilience concerns in code |
| **Pipeline integration**<br />The ability to integrate with CI/CD pipelines for continuous code analysis | Available |
| **Service discovery, mapping**<br />The ability to automate service discovery mapping, which identifies the underlying services, dependencies, and communication patterns (including to external resources, such as SaaS providers) | Available |
| **Service discovery, recommendations**<br />The ability to suggest optimizations for discovered services | Available |
| **Monolith decomposition, identification**<br />The ability to identify candidate microservices, given classes, objects, functions, and stored procedures | Available |
| **Monolith decomposition, impact analysis**<br />The ability to analyze the impact of the decomposition process | Available |
| **Open source compliance analysis, identification**<br />The ability to identify non-compliant open source solutions within an application | Available |
| **Open source compliance analysis, recommendations**<br />The ability to suggest compliant alternatives or remediation steps | Available |
| **Framework migration, standard**<br />The ability to support framework migrations, such as Spring to Spring Boot or .NET Framework to .NET 6\+ | Available; can report on compatibility and necessary changes |
| **Framework migration, legacy**<br />The ability to migrate legacy frameworks, databases, or data formats during framework migrations | Available |
| **Environmental impact analysis**<br />The ability to provide guidance about the sustainability of applications, such as before and after a migration | Available |
| **Cost of change analysis, effort**<br />The ability to estimate the effort required to modernize an application | Available |
| **Cost of change analysis, architecture**<br />The ability to estimate the target architecture costs after modernizing an application | Available |
| **Predictive outcome analysis**<br />The ability to rate modernization outcomes based on aggregated, anonymized data, such as the risk of change, the effort of change, and a confidence level that the change will be successful | Available |
| **Weighted analysis, preferences**<br />The ability to weight preferences for modernization recommendations based on considerations such as performance, resilience, and cost | Not available |
| **Weighted analysis, organizational priorities**<br />The ability to customize and adjust weights as organizational priorities change | Available |
