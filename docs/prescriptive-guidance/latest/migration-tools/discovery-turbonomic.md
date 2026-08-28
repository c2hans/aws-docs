---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-turbonomic.html
---

# Turbonomic
<a name="discovery-turbonomic"></a>

*Last update: May 15, 2023*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-turbonomic-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [IBM Turbonomic](https://www.ibm.com/products/turbonomic) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | + AWS Cloud Management Tools Competency<br />+ AWS Microsoft Workloads Competency<br />+ AWS Cloud Migration Competency |
| **AWS Marketplace**<br />Link to subscribe or download | [Turbonomic on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=3493e57b-6545-412e-a1d4-f1edf709d9ce) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + Servers deployed on AWS (customer VPC)<br />+ Servers deployed on premises in customer environment<br />+ SaaS or servers in other cloud provider environment |
| **Compliance** | Not available |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-turbonomic-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | + Agentless<br />+ Login-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | + Servers and operating systems<br />+ Databases<br />+ Storage systems<br />+ Software processes<br />+ Containers<br />+ Mainframe |
| **Operating systems discoverable** | + Linux<br />+ Windows<br />+ IBM AIX |
| **Other resources discoverable** | Bare metal, business applications (via APMs), containers and pods, hyper-converged systems, other cloud resources |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | + Physical and virtual servers and their profiles<br />+ Attached storage and profiles – data storage device connected directly to a server or virtual machine (VM)<br />+ Detached storage and profiles – data storage accessed over a network such as network-attached storage (NAS) and storage area network (SAN) |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | + Physical and virtual server utilization data collection<br />+ Attached storage utilization data collection<br />+ Detached storage utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:+ Application and server dependency – Individual servers and dependencies that form an application<br />+ Application and software process dependency – Individual software processes, configurations, and dependencies that form an application<br />+ Application and code dependency – Individual programming code, configurations, and dependencies that form an application | Not available |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:+ All resource and applications – An entire on-premises or source environment with all resources and applications<br />+ Single application – A single application across its resources, end to end<br />+ Single application and its software processes – Individual software processes and dependencies that form an application<br />+ Single application and its programming code – Individual programming code and dependencies that form an application | All resource and applications |
| **Database details discovery, source database system** | + Database engine<br />+ Database editions<br />+ Runtime metrics (for example, server memory usage, client connections, transactions, batch requests) |
| **Storage details discovery, systems** | + Local storage<br />+ Storage Area Network (SAN)<br />+ Network Attached Storage (NAS) |
| **Storage details discovery, configuration** | Block storage (for example, Fiber Channel or iSCSI) |
| **Storage details discovery, capacity** | + Volume identifier and volume size (GB)<br />+ Storage raw total size, raw usable size (GB)<br />+ Used capacity (GB) |
| **Storage details discovery, types**<br />The ability to discover storage system types and access protocols | Relationships among disk, array, LUN, and VM |
| **Storage details discovery, utilization** | + Mean (average) IOPS<br />+ Peak IOPS<br />+ Mean (average) throughput (MB per second)<br />+ Peak throughput (MB per second)<br />+ Mean disk latency (milliseconds)<br />+ Peak disk latency (milliseconds) |
| **Storage details discovery, object metadata** | Not available |
| **Storage systems discoverable**<br />The ability to discovery storage systems, such as EMC Isilon, EMC VMAX, Hitachi Vantara, HPE 3PAR, and Pure Storage | + EMC ScaleIO, EMC VMAX, EMC VPLEX, EMC XtremIO<br />+ HPE 3PAR<br />+ NetApp<br />+ Pure Storage |
| **File system details discovery** | Not available |
| **Software details discovery** | Not available |
| **Container details discovery** | + Kubernetes<br />+ Red Hat OpenShift |
| **License discovery** | Microsoft – Windows, Microsoft SQL Server, Hyper-V (stand-alone of SSVMM) |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
