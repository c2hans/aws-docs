---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-cast-highlight.html
---

# CAST Highlight
<a name="discovery-cast-highlight"></a>

*Last update: October 22, 2024*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-cast-highlight-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [CAST Highlight](https://www.castsoftware.com/highlight/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Discovery, Planning, and Recommendation |
| **AWS Marketplace**<br />Link to subscribe or download | [CAST Highlight on AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-rjrikuvzqawl6) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | SaaS-based |
| **Compliance** | + General Data Protection Regulation (GDPR)<br />+ International Organization for Standardization (ISO) 27001, 27017, 27018, and 27701 |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support<br />+ Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-cast-highlight-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Agent-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | Not available |
| **Operating systems discoverable** | Not available |
| **Other resources discoverable** | CAST Highlight scans application source code and discovers a broad scope of insights such as cloud maturity, cloud blockers for migration and modernization (from customer premises to AWS, from other cloud to AWS, for on AWS modernization), containerization blockers, three types of open source risks, green software insights, and more. |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | Not available |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | Not available |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:+ Application and server dependency – Individual servers and dependencies that form an application<br />+ Application and software process dependency – Individual software processes, configurations, and dependencies that form an application<br />+ Application and code dependency – Individual programming code, configurations, and dependencies that form an application | Not available |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:+ All resource and applications – An entire on-premises or source environment with all resources and applications<br />+ Single application – A single application across its resources, end to end<br />+ Single application and its software processes – Individual software processes and dependencies that form an application<br />+ Single application and its programming code – Individual programming code and dependencies that form an application | + All resource and applications<br />+ Single application and its programming code |
| **Database details discovery, source database system** | Not available |
| **Storage details discovery**<br />The ability to discover storage details, such as systems, types, capacity, configuration, utilization, and object metadata | Not available |
| **Storage systems discoverable**<br />The ability to discovery storage systems, such as EMC Isilon, EMC VMAX, Hitachi Vantara, HPE 3PAR, and Pure Storage | Not available |
| **File system details discovery** | Not available |
| **Software details discovery, programming languages** | 50\+ languages, including C\#, C\+\+, Closure, COBOL, Go, Java, JavaScript, Kotlin, PHP, Python, Ruby, Scala, Swift, TypeScript, VB.NET. See [Technology Coverage](https://doc.casthighlight.com/#technologycoverage). |
| **Software details discovery, frameworks or libraries** | All the libraries and frameworks used by applications: defined in dependency files or through copy and pasting of public source code in public repositories |
| **Software details discovery, ISV products**<br />The ability to discover independent software vendor (ISV) products, such as Splunk Enterprise or F5 BIG-IP Virtual Edition | Detection of proprietary or private components listed in dependency files |
| **Container details discovery** | Not available |
| **License discovery** | Not available |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
| **Code analysis**<br />The ability to support static and dynamic code analysis, optionally identifying:+ Deprecated code<br />+ Security concerns in code<br />+ Resilience concerns in code | + Security concerns in code<br />+ Resilience concerns in code<br />+ Identification of cloud blockers and boosters, software health (resiliency, agility, elegance), software composition, three types of open source risks, use of proprietary components, software green insights. Recommendations of 5R disposition, migration and modernization waves, cloud or containerization blocker remediation and effort estimates, cloud-native services, open source risk remediation. All benchmarked with industry peers and with trends over time. |
| **Pipeline integration**<br />The ability to integrate with CI/CD pipelines for continuous code analysis | Available |
| **Service discovery, mapping**<br />The ability to automate service discovery mapping, which identifies the underlying services, dependencies, and communication patterns (including to external resources, such as SaaS providers) | Available |
| **Service discovery, recommendations**<br />The ability to suggest optimizations for discovered services | Partial: to a certain level of detail (for example, only on API calls) |
| **Monolith decomposition, identification**<br />The ability to identify candidate microservices, given classes, objects, functions, and stored procedures | Not available |
| **Monolith decomposition, impact analysis**<br />The ability to analyze the impact of the decomposition process | Not available |
| **Open source compliance analysis, identification**<br />The ability to identify non-compliant open source solutions within an application | Available |
| **Open source compliance analysis, recommendations**<br />The ability to suggest compliant alternatives or remediation steps | Available |
| **Framework migration, standard**<br />The ability to support framework migrations, such as Spring to Spring Boot or .NET Framework to .NET 6\+ | Not available |
| **Framework migration, legacy**<br />The ability to migrate legacy frameworks, databases, or data formats during framework migrations | Not available |
| **Environmental impact analysis**<br />The ability to provide guidance about the sustainability of applications, such as before and after a migration | Available |
| **Cost of change analysis, effort**<br />The ability to estimate the effort required to modernize an application | Available |
| **Cost of change analysis, architecture**<br />The ability to estimate the target architecture costs after modernizing an application | Not available |
| **Predictive outcome analysis**<br />The ability to rate modernization outcomes based on aggregated, anonymized data, such as the risk of change, the effort of change, and a confidence level that the change will be successful | Available |
| **Weighted analysis, preferences**<br />The ability to weight preferences for modernization recommendations based on considerations such as performance, resilience, and cost | Available |
| **Weighted analysis, organizational priorities**<br />The ability to customize and adjust weights as organizational priorities change | Available |
