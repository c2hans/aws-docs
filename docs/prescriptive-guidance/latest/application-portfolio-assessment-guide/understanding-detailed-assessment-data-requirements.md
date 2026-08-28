---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/understanding-detailed-assessment-data-requirements.html
---

# Understanding detailed assessment data requirements
<a name="understanding-detailed-assessment-data-requirements"></a>

The following table describes the information required to obtain a complete portfolio view of the applications in the migration and their associated infrastructure.

The tables use the following abbreviations:
+ R, for required
+ O, for optional
+ N/A, for not applicable

## Applications
<a name="applications.ec37dda2-674e-5502-a450-6968515f4dad"></a>

|
|
| **Attribute name** | **Description** | **Discovery, design, and migration strategy** | **Estimated run rate** | **Recommended fidelity level (minimum)** |
| --- |--- |--- |--- |--- |
| Unique identifier | For example, application ID. Typically available on existent CMDBs or other internal inventories and control systems. Consider creating unique IDs whenever these are not defined in your organization. | R | O | High |
| Application name | Name by which this application is known to your organization. Include commercial off-the-shelf (COTS) vendor and product name when applicable. | R | R | High |
| Is COTS? | Yes or No. Whether this is a commercial application or internal development | R | R | High |
| COTS product and version | Commercial software product name and version  | R | R | High |
| Description | Primary application function and context | R | O | High |
| Criticality | For example, strategic or revenue-generating application, or supporting a critical function | R | O | High |
| Type | For example, database, customer relationship management (CRM), web application, multimedia, IT shared service | R | O | High |
| Environment | For example, production, pre-production, development, test, sandbox | R | R | High |
| Compliance and regulatory | Frameworks applicable to the workload (for example, HIPAA, SOX, PCI-DSS, ISO, SOC, FedRAMP) and regulatory requirements | R | O | High |
| Dependencies | Upstream and downstream dependencies to internal and external applications or services | R | N/A | High |
| Infrastructure mapping | Mapping to physical and/or virtual assets that make up the application | R | R | High |
| License | Commodity software license type (for example, Microsoft SQL Server Enterprise) | R | R | High |
| Cost | Costs for software license, software operations, and maintenance | O | R | Medium-high |
| Business unit | For example, marketing, finance, sales | R | O | High |
| Owner details | Contact information for application owner | R | O | High |
| Architecture type | For example, web application, 2-tier, 3-tier, microservices, service-oriented architecture (SOA) | R | R | High |
| Recovery point objective (RPO), recovery time objective (RTO), and /service-level agreement (SLA) | Current service- management attributes | R | R | High |
| Revenue-generating Application or business-strategic application? | Yes, if application directly or indirectly influences company revenue or is considered strategic by the business. | R | O | Medium-high |
| Number of users (concurrent) | For example, internal, or external users or, internal and/or external users/customers | R | R | Medium-high |
| User location | Origin of user sessions | R | R | Medium-high |
| Risks and issues | Known risks and issues | R | O | Medium-high |
| Migration considerations | Any additional information that could be relevant for migration | R | R | Medium-high |
| Migration strategy | For example, one of the AWS  6 Rs for migration | R | R | Medium-high |
| Database details | For example, partitioning, encryption, replication, extensions, Secure Sockets Layer (SSL) support | R | R | High |
| Support teams | For example, application operations team name | R | O | Medium-high |
| Monitoring solution | Product used to monitor this application | R | O | Medium-high |
| Backup requirements | Required backup schedule in AWS | R | R | Medium-high |
| DR information | For example, disaster recovery components for this application | R | R | Medium-high |
| Target AWS requirements | For example, components, account placement, networking, security | R | R | High |

## Infrastructure
<a name="infrastructure.8125a2aa-5174-5b74-8d26-894d6a381389"></a>

|
|
| Attribute Name | Description | Discovery, design, and migration strategy | Estimated run rate | Recommended fidelity level (minimum) |
| --- |--- |--- |--- |--- |
| Unique identifier | For example, server ID. Typically available on existing CMDBs or other internal inventories and control systems. Consider creating unique IDs whenever these are not defined in your organization. | R | O | High |
| Network name | Asset name in the network (for example, hostname) | R | O | High |
| DNS name (fully qualified domain name, or FQDN) | DNS name | R | O | Medium-high |
| IP address and netmask | Internal and/or public IP addresses | R | R | High |
| Asset type | For example, physical or virtual server, hypervisor, container, device, database instance | R | R | High |
| Product name | Commercial vendor and product name (for example, VMware ESXi, IBM Power Systems, Exadata) | R | R | High |
| Operating system | For example, REHL 8, Windows Server 2019, AIX 6.1 | R | R | High |
| Configuration | Allocated CPU, number of cores, threads per core, total memory, storage, network cards | R | R | High |
| Utilization | CPU, memory, and storage peak and average. Database instance throughput. | R | R | High |
| License | Commodity license type (for example, RHEL Standard) | R | R | High |
| Application mapping | Applications or application components that run in this infrastructure | R | O | High |
| Communication data | For example, server to server at a process level | R | N/A | Medium-high |
| Target AWS requirements | For example, instance types, account, subnets, security groups, routing | R | R | High |
| Migration strategy, patterns, and tools | For example, one of the 6 Rs for migration, specific technical pattern, migration tooling | R | O |  <br />High |
| Risks and issues | Known risks and issues | R | O | Medium-high |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
