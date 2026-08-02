---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-tools/discovery-virtana.html
---

# Virtana
<a name="discovery-virtana"></a>

*Last update: February 16, 2024*

**Note**
AWS Partner product descriptions and reported qualifications, including compliance, are provided by the AWS Partner and are not verified by AWS. For more information about these products, contact the AWS Partner. You are encouraged to conduct your own additional due diligence before choosing to use any of the products listed.

## Product overview
<a name="discovery-virtana-overview"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Product website** | [Virtana](https://www.virtana.com/) |
| **Product certifications**<br />[AWS Competency Program](https://aws.amazon.com/partners/offerings/) competencies and other certifications | AWS Migration and Modernization – Discovery, Planning, and Recommendation |
| **AWS Marketplace**<br />Link to subscribe or download | [Virtana on AWS Marketplace](https://aws.amazon.com/marketplace/seller-profile?id=897186a6-d3ec-4b15-b358-f3173ec615d5) |
| **Tool deployment model**<br />Product can be SaaS-based or customer-deployed | SaaS on AWS (vendor VPC)Servers deployed on premises in customer environment |
| **Compliance** | System and Organization Controls (SOC) |
| **Service model** | Full self-service – Deployment, management, and maintenance can be done by the customer or end-userSelf-service with vendor support – Deployment, management, and maintenance can be done by customer or end-user with the option of vendor supportManaged service (including partner-enabled service) – Deployment, management, and maintenance require professional services |
| **Pricing model** | Subscription |

## Discovery, planning, and recommendation capabilities
<a name="discovery-virtana-discovery"></a>

|
|
| Category | Product capabilities |
| --- |--- |
| **Discovery method**<br />The ability to support one or more of the following discovery methods:Agentless – Uses protocols or interfaces such as SNMP or WMIAgent-based – Requires installation of software on the source resources, such as Linux or Windows serversLogin-based – Uses protocols, such as SSH and RDP, to log in to the source servers | AgentlessLogin-based |
| **Resources discoverable**<br />The ability to discover servers, databases, storage systems, network devices, software processes, containers, and mainframes | Servers and operating systemsDatabasesStorage systemsNetwork devicesContainers |
| **Operating systems discoverable** | LinuxWindowsSolaris |
| **Other resources discoverable** | KVM, Hyper-V, AppDynamics, Dynatrace, ServiceNow, NetFlow, Cisco UCS, IBM PowerVM, Kubernetes, Brocade SAN Switch, Cisco SAN Switch, Dell PowerFlex, PowerMax, VPLEX, PowerStore, XtremIO, Hitachi VSP, NetApp Storage, Pure, Cisco Nexus |
| **Discovery of resource profiles**<br />The ability to discover the CPU family (such as x86 or RISC/PowerPC), number of CPU cores, memory size, number of disks, storage size, IOPS, network interfaces, or bandwidth | Physical and virtual servers and their profilesAttached storage and profiles – data storage device connected directly to a server or virtual machine (VM)Detached storage and profiles – data storage accessed over a network such as network-attached storage (NAS) and storage area network (SAN)Network devices and profiles |
| **Resource utilization data collection**<br />The ability to collect time-series utilization data, such peak, average, median, standard deviation, IOPS, throughput, percentile with sampling interval of 5 minutes, and minimum sampling duration of 1 month | Physical and virtual server utilization data collectionAttached storage utilization data collectionDetached storage utilization data collectionNetwork utilization data collection |
| **Application dependency level**<br />The ability to discover application dependency and export dependency data:Application and server dependency – Individual servers and dependencies that form an applicationApplication and software process dependency – Individual software processes, configurations, and dependencies that form an applicationApplication and code dependency – Individual programming code, configurations, and dependencies that form an application | Application and server dependencyApplication and software process dependencyApplication and code dependency |
| **Visualization level**<br />The ability to provide multiple-level visualization of applications:All resource and applications – An entire on-premises or source environment with all resources and applicationsSingle application – A single application across its resources, end to endSingle application and its software processes – Individual software processes and dependencies that form an applicationSingle application and its programming code – Individual programming code and dependencies that form an application | All resource and applicationsSingle applicationSingle application and its software processes |
| **Database details discovery, source database system** | Database engineClustering and servers in the cluster |
| **Database details discovery, database type** | MariaDBMicrosoft SQL ServerMongoDBMySQLOraclePostgreSQL |
| **Storage details discovery, systems** | Local storageStorage Area Network (SAN)Network Attached Storage (NAS) |
| **Storage details discovery, configuration** | File storage (for example, NFS or SMB)Block storage (for example, Fiber Channel or iSCSI)Object storage (for example, Atmos, Vantara, HTTP, or REST) |
| **Storage details discovery, capacity** | Volume identifier and volume size (GB)Storage pool name and size (GB)Storage raw total size, raw usable size (GB)Used capacity (GB) |
| **Storage details discovery, types**<br />The ability to discover storage system types and access protocols | LUN in SAN SCSI environmentRAID levels (RAID 0, RAID 1, …, RAID 6)Relationships among disk, array, LUN, and VM |
| **Storage details discovery, utilization** | Mean (average) IOPSPeak IOPSMean (average) throughput (MB per second)Peak throughput (MB per second)Mean disk latency (milliseconds)Peak disk latency (milliseconds) |
| **Storage details discovery, object metadata** | Not available |
| **Storage systems discoverable**<br />The ability to discovery storage systems, such as EMC Isilon, EMC VMAX, Hitachi Vantara, HPE 3PAR, and Pure Storage | Dell PowerFlex, Hitachi VSP, HPE, IBM SVC, Infinidat, NetApp Storage, PowerMax, PowerProtect, PowerStore, Pure, Unity, VPLEX, XtremIO |
| **File system details discovery** | Not available |
| **Software details discovery** | Not available |
| **Container details discovery** | AWSKubernetesMicrosoft AzureRed Hat OpenShift |
| **License discovery** | Not available |
| **Data sovereignty support**<br />The ability to keep discovered data within a specific geographic region | Available |
| **Data export ability**<br />The ability to export the discovered data into a usable format, such as CSV or JSON | Available |
