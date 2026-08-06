---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-dynatrace.html
---

# Dynatrace
<a name="discovery-dynatrace"></a>

*Last update: May 15, 2023*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-dynatrace-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Dynatrace](https://www.dynatrace.com/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Application Monitoring and Orchestration |
| **AWS Marketplace**<br />Link to subscribe or download | [Dynatrace on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=1422b3b0-b081-4af9-9d2b-34e6eb924f05) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | + SaaS on AWS (vendor VPC)<br />+ Servers deployed on AWS (customer VPC)<br />+ Servers deployed on premises in customer environment<br />+ SaaS or servers in other cloud provider environment |
| **Compliance** | + General Data Protection Regulation (GDPR)<br />+ International Organization for Standardization (ISO) 27001<br />+ System and Organization Controls 2 (SOC 2) Type IIThe Dynatrace SaaS infrastructure is hosted in AWS, which meets many certification requirements, including System and Organization Controls (SOC) 1-3 / SSAE-16, ISO 27001, ISO 27017, ISO 27018, Payment Card Industry Data Security Standard (PCI DSS) level 1, Federal Risk and Authorization Management Program (FedRAMP), and more. |
| **Service model** | + Full self-service – Deployment, management, and maintenance can be done by the customer or end-user<br />+ Self-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor support<br />+ Managed service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-dynatrace-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:+ Agentless – Uses protocols or interfaces such as SNMP or WMI<br />+ Agent-based – Requires installation of software on the source resources, such as Linux or Windows servers<br />+ Login-based – Uses protocols, such as SSH and RDP, to log in to the source servers | + Agentless<br />+ Agent-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | + Servers and operating systems<br />+ Databases<br />+ Storage systems<br />+ Network devices<br />+ Software processes<br />+ Containers<br />+ Mainframe |
| **Operating systems discoverable** | + Linux<br />+ Windows<br />+ Other – Android, IBM AIX, iOS, Solaris, IBM z/OS |
| **Other resources discoverable** | Citrix NetScaler 10.5\+, IBM DataPower 4.0\+, F5 BIG-IP LTM 11\+, IBM iSeries (AS/400) - Preview 7.2\+, IBM MQ 8.0\+, Juniper Networks - Preview 12.1\+, SAP ABAP platform - Preview 7.31\+, Windows Server 2003\+ |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | + Physical and virtual servers and their profiles<br />+ Attached storage and profiles – data storage device connected directly to a server or virtual machine (VM)<br />+ Network devices and profiles |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | + Physical and virtual server utilization data collection<br />+ Attached storage utilization data collection<br />+ Network utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:+ Application and server dependency – Individual servers and dependencies that form an application<br />+ Application and software process dependency – Individual software processes, configurations, and dependencies that form an application<br />+ Application and code dependency – Individual programming code, configurations, and dependencies that form an application | + Application and server dependency<br />+ Application and software process dependency<br />+ Application and code dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:+ All resource and applications – An entire on-premises or source environment with all resources and applications<br />+ Single application – A single application across its resources, end to end<br />+ Single application and its software processes – Individual software processes and dependencies that form an application<br />+ Single application and its programming code – Individual programming code and dependencies that form an application | + All resource and applications<br />+ Single application<br />+ Single application and its software processes<br />+ Single application and its programming code |
| **Database details discovery, source database system** | + Database engine<br />+ Runtime metrics (for example, server memory usage, client connections, transactions, batch requests) |
| **Storage details discovery**<br />The ability to discover storage details, such as systems, types, capacity, configuration, utilization, and object metadata | Not available |
| **File system details discovery** | Not available |
| **Software details discovery, programming languages** | Java, .NET, .NET Core, C / C\+\+, Go, NodeJS, PHP, Python, Scala |
| **Software details discovery, frameworks or libraries** | Over 100 frameworks supported, Database, Web, Web services, Remoting, JavaScript, .NET, C\+\+, Java |
| **Container details discovery** | + BOSH bpm<br />+ containerd<br />+ CRI-O<br />+ Docker<br />+ Docker Enterprise<br />+ Garden-runC<br />+ Kubernetes<br />+ Red Hat OpenShift<br />+ SUSE CaaS<br />+ VMware Tanzu Kubernetes Grid |
| **License discovery** | Not available |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
