---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/f-sx-for-ontap-as-the-storage-solution.html
---

# How it works
<a name="f-sx-for-ontap-as-the-storage-solution"></a>

## Amazon FSx for NetApp ONTAP as the storage solution
<a name="amazon-fsx-for-netapp-ontap-as-the-storage-solution.2f54237e-df1c-5e56-82aa-74ba999bbbfb"></a>

NetApp's ONTAP is an enterprise storage operating system with a long-standing reputation in on-premises data centers for its data management capabilities, particularly its space-efficient snapshots, replication, thin provisioning, and deduplication. These capabilities make it a natural fit for workloads that demand both storage efficiency and reliable, fast recovery. Amazon FSx for NetApp ONTAP brings this proven storage platform into AWS as a fully managed service, eliminating the operational burden of managing storage hardware, firmware updates, and high-availability configurations. This is precisely why it forms the foundation of the backup architecture described in this guide. Amazon FSx for NetApp ONTAP's native snapshot engine enables Commvault IntelliSnap to deliver the sub-5-minute RPO and sub-15-minute RTO targets at multi-terabyte scale. The service supports NFS, SMB, and iSCSI protocols, making it compatible with demanding enterprise workloads such as SAP HANA, Oracle, and SQL Server. AWS manages the underlying infrastructure, patching, and high availability, while customers retain full control over storage configuration, data management policies, and access controls through the full ONTAP REST API.

Amazon FSx for NetApp ONTAP provides several general storage capabilities that benefit SAP HANA backup and recovery workloads:

### Snapshot feature
<a name="snapshot-feature.dcb43dd3-d440-56d1-8c6a-06533cec95ba"></a>

Amazon FSx for NetApp ONTAP offers native snapshot functionality through redirect-on-write mechanisms. This creates point-in-time copies of HANA data volumes in seconds regardless of volume size. Snapshots consume storage exclusively for changed data blocks. The snapshot feature supports volume cloning. Snapshot-based recovery operations complete quickly and limit production impact to brief database quiescing during snapshot creation.

### Cross-account and geographic replication
<a name="cross-account-and-geographic-replication.872ee427-59d5-5f0c-9a27-e1e453f1f67c"></a>

Built-in SnapMirror technology performs asynchronous replication of snapshots. It replicates to secondary storage systems or different AWS accounts. SnapMirror delivers geographic redundancy and maintains backup copies in isolated accounts for compliance and disaster recovery (DR).

### Performance optimization
<a name="performance-optimization.8335abc6-6c1e-5665-a433-796c0cdf5a19"></a>

NetApp's storage architecture is optimized for database workloads. Features like thin provisioning, automatic tiering, and in-memory and NVMe caching maintain SAP HANA performance during backup operations.

#### SAP HANA configuration requirements
<a name="sap-hana-configuration-requirements.1f2a6e92-e3d9-5532-9a92-dd950971a6f4"></a>

Although the capabilities above are general to Amazon FSx for NetApp ONTAP, SAP HANA imposes two file system configuration requirements that you must apply:
+ **Capacity pool tiering must be set to **`None`**.** SAP HANA does not support capacity pool tiering, so keep all HANA data and log data on the primary SSD tier.
+ **Daily automatic backups must be disabled.** The default Amazon FSx for NetApp ONTAP daily backups are not application-aware and cannot restore SAP HANA to a consistent state. Instead, the Commvault IntelliSnap and Backint workflow described in this guide provides application-consistent protection.

For more information, see [Set up FSx for ONTAP file system, SVMs, and volumes](https://docs.aws.amazon.com/sap/latest/sap-hana/amazon-fsx-sap-hana.html) in the SAP HANA on AWS documentation.

##### Amazon FSx for NetApp ONTAP architecture for SAP HANA
<a name="amazon-f-sx-for-net-app-ontap-architecture-for-sap-hana"></a>

An Amazon FSx for NetApp ONTAP deployment for SAP HANA consists of:
+ **Storage Virtual Machine (SVM):** The storage container hosting HANA volumes with independent management and security policies.
+ **HANA data volumes:** Volumes storing HANA data files configured with snapshot policies for regular, automated snapshot creation.
+ **HANA log volumes:** Separate volumes for transaction logs with different backup characteristics and retention periods.
+ **Backup volumes: **In multi-account architecture, the Backup account stores SnapMirror copies of production snapshots on Amazon FSx for NetApp ONTAP instances.

##### Commvault backup architecture for SAP HANA on AWS
<a name="commvault-backup-architecture-for-sap-hana-on-aws"></a>

Commvault is a data protection and information management platform that unifies backup, recovery, replication, and data management functions across hybrid and multi-cloud environments. For SAP HANA on AWS, Commvault provides automated backup orchestration on Amazon FSx for NetApp ONTAP. It manages backup workflows, catalog management, retention enforcement, and self-service recovery.

##### Commvault infrastructure components
<a name="commvault-infrastructure-components.e2fd4da3-f1a5-5da2-981b-54c7e5ba02eb"></a>

To implement this solution, you need to understand five key Commvault infrastructure components that work together to protect your SAP HANA data:

##### CommServe
<a name="commserve.ffe82be7-b5c2-5f97-8a35-7e7cec2e20fb"></a>

Central management hub for all backup operations. It manages policies, scheduling, media management, and recovery operations. It is deployed in the backup AWS account. CommServe centralizes management and isolation from production.

##### MediaAgents (Media Servers)
<a name="mediaagents--media-servers-.44ab0370-e5ea-548e-b0c9-341505eebbf0"></a>

A MediaAgent is the Commvault software component that executes data transfer during backup and restore operations; the host it runs on is commonly called a Media Server. Deploying two or more MediaAgents enables parallel processing, which reduces backup windows.

##### Access Nodes
<a name="access-nodes.e1f88ffb-232d-50cd-86bd-164453496189"></a>

Access Nodes are MediaAgents assigned the IntelliSnap role, which establishes secure connectivity to Amazon FSx for NetApp ONTAP. They run the NetApp IntelliSnap integration components and handle storage-layer API communication with the ONTAP cluster. In other words, an Access Node is a MediaAgent specialized for array (snapshot) operations.

##### IntelliSnap agents
<a name="intellisnap-agents.6f9cbce1-3c0d-5817-a668-434070b14e3d"></a>

Software agents that are installed on Amazon Elastic Compute Cloud (Amazon EC2) instances running SAP HANA and coordinate with Commvault. They enable application-aware backup operations, capturing snapshots at consistent points in time.

##### Storage pools
<a name="storage-pools.cc13d7e5-1af3-5f9b-8212-850ea13eed1a"></a>

Logical groupings of storage resources where backup data is stored. They span Amazon FSx for NetApp ONTAP volumes or Amazon Simple Storage Service (Amazon S3) buckets.

##### Backup workflow architecture
<a name="backup-workflow-architecture"></a>

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/images/guide-img/1cbb8aa3-6197-4168-8624-86a93eec975a/images/db104d87-ffe1-49f9-ac04-dcd6fc1905aa.png)

*Fig 1. Backup workflow architecture *

The backup workflow shows how these components interact:

1. **Backup Job Initiation: **The CommServe (described in Infrastructure Components above) triggers the backup job based on the defined schedule**.** CommServe delegates the job to the MediaAgent on the designated Media Server.

1. **Job assignment and client coordination**: CommServe assigns the job to the Client. The Client validates subclient settings, application health, and script readiness before proceeding.

1. **Database quiescing (pre-snapshot): **The Commvault Client executes pre-snapshot scripts to quiesce SAP HANA database for application consistency**.**

1. **ONTAP snapshot creation (IntelliSnap):** The MediaAgent triggers an Amazon FSx for NetApp ONTAP snapshot via IntelliSnap. This is a metadata pointer operation that completes in seconds regardless of volume size, minimizing the quiesce-to-unquiesce window for the SAP HANA database.

1. **Database unquiescing:** The Commvault Client executes post-snapshot scripts to unquiesce SAP HANA and restart normal database operations. Production I/O resumes immediately after the snapshot completes.

1. **Replication:** With SAP HANA unquiesced and operating normally, SnapMirror asynchronously transfers only the changed blocks to backup storage. The data movement happens at the storage layer without traversing the active file system or impacting application performance.

1. **Index and catalog update:** The MediaAgent updates the Commvault index and catalog with backup metadata. Snapshot cloning becomes available to restore operations once the catalog is updated.

1. **Job completion and reporting:** The MediaAgent reports job status (Success/Warning/Failure) to CommServe. It includes detailed logs and automated alerts for errors.
