---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-tidal-accelerator.html
---

# Tidal Accelerator
<a name="discovery-tidal-accelerator"></a>

*Last update: October 22, 2024*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-tidal-accelerator-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Tidal Accelerator](https://tidalcloud.com/accelerator/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Discovery, Planning, and Recommendation |
| **AWS Marketplace**<br />Link to subscribe or download | Not available |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | SaaS on AWS (vendor VPC) |
| **Compliance** | + General Data Protection Regulation (GDPR)<br />+ Health Insurance Portability and Accountability Act (HIPAA)<br />+ System and Organization Controls (SOC)<br />+ System and Organization Controls 2 (SOC 2) Type II |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support<br />+ Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-tidal-accelerator-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | + Agentless<br />+ Login-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | + Servers and operating systems<br />+ Databases<br />+ Software processes |
| **Operating systems discoverable** | + Windows<br />+ Linux<br />+ Solaris<br />+ IBM AIX |
| **Other resources discoverable** | Not available |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | + Physical and virtual servers and their profiles<br />+ Attached storage and profiles – data storage device connected directly to a server or virtual machine (VM)<br />+ Network devices and profiles |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | + Physical and virtual server utilization data collection<br />+ Attached storage utilization data collection<br />+ Network utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:+ Application and server dependency – Individual servers and dependencies that form an application<br />+ Application and software process dependency – Individual software processes, configurations, and dependencies that form an application<br />+ Application and code dependency – Individual programming code, configurations, and dependencies that form an application | + Application and server dependency<br />+ Application and software process dependency<br />+ Application and code dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:+ All resource and applications – An entire on-premises or source environment with all resources and applications<br />+ Single application – A single application across its resources, end to end<br />+ Single application and its software processes – Individual software processes and dependencies that form an application<br />+ Single application and its programming code – Individual programming code and dependencies that form an application | Single application |
| **Database details discovery, source database system** | Database engine |
| **Database details discovery, database type** | + Microsoft SQL Server<br />+ MySQL<br />+ Oracle<br />+ PostgreSQL<br />+ Redis<br />+ Neo4j |
| **Storage details discovery, systems** | Local storage |
| **Storage details discovery, types**<br />The ability to discover storage system types and access protocols | Not available |
| **Storage details discovery, capacity** | + Volume identifier and volume size (GB)<br />+ Storage raw total size, raw usable size (GB)<br />+ Used capacity (GB) |
| **Storage details discovery, configuration** | Not available |
| **Storage details discovery, utilization** | Not available |
| **Storage details discovery, object metadata** | Not available |
| **Storage systems discoverable**<br />The ability to discovery storage systems, such as EMC Isilon, EMC VMAX, Hitachi Vantara, HPE 3PAR, and Pure Storage | Not available |
| **File system details discovery** | Not available |
| **Software details discovery, programming languages** | From the [Tidal guides](https://guides.tidal.cloud/code-analysis-overview.html): C\#, Java, JavaScript, Python, COBOL, PHP, C\+\+, C, sh/bash., JSP, Perl, Visual Basic, VB.NET, VBScript |
| **Software details discovery, frameworks or libraries** | + All libraries frameworks in C\#, JavaScript, Python<br />+ Application frameworks: Apache Tomcat, Oracle WebLogic, IBM WebSphere |
| **Software details discovery, ISV products**<br />The ability to discover independent software vendor (ISV) products, such as Splunk Enterprise or F5 BIG-IP Virtual Edition | Not available |
| **Container details discovery** | Not available |
| **License discovery** | Not available |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Not available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
| **Code analysis**<br />The ability to support static and dynamic code analysis, optionally identifying:+ Deprecated code<br />+ Security concerns in code<br />+ Resilience concerns in code | Security concerns in code |
| **Pipeline integration**<br />The ability to integrate with CI/CD pipelines for continuous code analysis | Available |
| **Service discovery, mapping**<br />The ability to automate service discovery mapping, which identifies the underlying services, dependencies, and communication patterns (including to external resources, such as SaaS providers) | Not available |
| **Service discovery, recommendations**<br />The ability to suggest optimizations for discovered services | Not available |
| **Monolith decomposition, identification**<br />The ability to identify candidate microservices, given classes, objects, functions, and stored procedures | Not available |
| **Monolith decomposition, impact analysis**<br />The ability to analyze the impact of the decomposition process | Available |
| **Open source compliance analysis, identification**<br />The ability to identify non-compliant open source solutions within an application | Not available |
| **Open source compliance analysis, recommendations**<br />The ability to suggest compliant alternatives or remediation steps | Not available |
| **Framework migration, standard**<br />The ability to support framework migrations, such as Spring to Spring Boot or .NET Framework to .NET 6\+ | Not available |
| **Framework migration, legacy**<br />The ability to migrate legacy frameworks, databases, or data formats during framework migrations | Not available |
| **Environmental impact analysis**<br />The ability to provide guidance about the sustainability of applications, such as before and after a migration | Available |
| **Cost of change analysis, effort**<br />The ability to estimate the effort required to modernize an application | Not available |
| **Cost of change analysis, architecture**<br />The ability to estimate the target architecture costs after modernizing an application | Not available |
| **Predictive outcome analysis**<br />The ability to rate modernization outcomes based on aggregated, anonymized data, such as the risk of change, the effort of change, and a confidence level that the change will be successful | Available |
| **Weighted analysis, preferences**<br />The ability to weight preferences for modernization recommendations based on considerations such as performance, resilience, and cost | Available |
| **Weighted analysis, organizational priorities**<br />The ability to customize and adjust weights as organizational priorities change | Available |
