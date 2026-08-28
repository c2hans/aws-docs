---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-appdynamics.html
---

# AppDynamics
<a name="discovery-appdynamics"></a>

*Last update: May 15, 2023*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-appdynamics-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Cisco AppDynamics](https://www.cisco.com/c/en_au/solutions/data-center/appdynamics-application-performance-monitoring.html) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Application Monitoring and Orchestration |
| **AWS Marketplace**<br />Link to subscribe or download | Not available |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + SaaS on AWS (vendor VPC)<br />+ Servers deployed on AWS (customer VPC)<br />+ Servers deployed on premises in customer environment |
| **Compliance** | + Federal Risk and Authorization Management Program (FedRAMP)<br />+ General Data Protection Regulation (GDPR)<br />+ Payment card industry (PCI) |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support<br />+ Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-appdynamics-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | Agent-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | + Servers and operating systems<br />+ Databases<br />+ Software processes<br />+ Containers |
| **Operating systems discoverable** | + Linux<br />+ Windows<br />+ Solaris |
| **Other resources discoverable** | No additional information |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | Physical and virtual servers and their profiles |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | + Physical and virtual server utilization data collection<br />+ Network utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:+ Application and server dependency – Individual servers and dependencies that form an application<br />+ Application and software process dependency – Individual software processes, configurations, and dependencies that form an application<br />+ Application and code dependency – Individual programming code, configurations, and dependencies that form an application | + Application and server dependency<br />+ Application and software process dependency<br />+ Application and code dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:+ All resource and applications – An entire on-premises or source environment with all resources and applications<br />+ Single application – A single application across its resources, end to end<br />+ Single application and its software processes – Individual software processes and dependencies that form an application<br />+ Single application and its programming code – Individual programming code and dependencies that form an application | + All resource and applications<br />+ Single application<br />+ Single application and its software processes<br />+ Single application and its programming code |
| **Database details discovery, source database system** | + Database engine<br />+ Database editions<br />+ Schemas<br />+ Database size<br />+ Runtime metrics (for example, server memory usage, client connections, transactions, batch requests) |
| **Storage details discovery**<br />The ability to discover storage details, such as systems, types, capacity, configuration, utilization, and object metadata | Not available |
| **File system details discovery** | Not available |
| **Software details discovery** | Not available |
| **Container details discovery** | + Amazon Elastic Kubernetes Service (Amazon EKS)<br />+ Azure Kubernetes Service<br />+ Docker<br />+ Google Kubernetes Engine<br />+ Kubernetes<br />+ Red Hat OpenShift<br />+ Rancher |
| **License discovery** | Not available |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Not available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Not available |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
