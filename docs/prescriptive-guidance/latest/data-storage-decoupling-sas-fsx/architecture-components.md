---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/data-storage-decoupling-sas-fsx/architecture-components.html
---

# Architecture components
<a name="architecture-components"></a>

This section outlines the specifications of the following important functional architecture components:
+ **SAS server** – This server is the central compute component for analytics processing and includes local direct-attached storage (DAS).
+ **SAS subversion server** – This server acts as the centralized version control system for SAS.
+ **Amazon FSx for Windows File Server** – This is an SMB file server for sharing storage between the SAS server and terminal servers. End users store and archive their pre- and post-processed data files on FSx for Windows File Server.
+ **Microsoft Remote Desktop Services (RDS), also known as Terminal Services** – RDS allows end users to access SAS servers by using a SAS client.
+ **Infrastructure automation** – You can use the AWS Cloud Development Kit (AWS CDK) with AWS CodePipeline and AWS CodeCommit to automate your infrastructure. CodePipeline can help you provision your infrastructure components. CodePipeline is a continuous delivery service for modelling, visualizing, and automating the steps required to release code. Additionally, CodePipeline provides a shared central environment and enables infrastructure management that's independent from local machines. CodeCommit is a secure, highly scalable, fully managed source control service that hosts private Git repositories. You can use CodeCommit to store AWS CDK infrastructure automation code and parameters.

## Environment separation
<a name="environment-separation"></a>

The following diagram shows an architecture for separating a SAS integration and SAS production environment.

![Architecture diagram for separating SAS integration and production environments](https://docs.aws.amazon.com/prescriptive-guidance/latest/data-storage-decoupling-sas-fsx/images/guide-img/f83bb357-cf26-4b94-abb6-1bd9d91feaa4/images/241db150-4fd7-4abb-84b5-6c56ceacb17d.png)

## Infrastructure components
<a name="infrastructure-components"></a>

This section provides an overview of the infrastructure components that are required for the recommended architecture in this guide.

### Production environment
<a name="production-environment.6754d664-ba0f-556f-89ee-7200848e8fec"></a>

We recommend that you use the following infrastructure components for your production environment.

|
|
| Type | Instance type | Resources |
| --- |--- |--- |
| **1 SAS server** | m6i.4xlarge | 16 vCPUs (8 cores)<br />64 GB RAM |
| **2 Citrix terminal servers** | m6i.4xlarge | 16 vCPUs (8 cores)<br />64 GB RAM (for example, 1–2 GB per user session for Microsoft Office and Adobe Suite and 500–1024 MB per SAS client on average)<br />25\+ users<br />Potential to scale out with more terminal servers in the future |
| **1 SAS subversion server** | m6i.2xlarge | 8 vCPUs<br />4 cores<br />32 GB RAM |

### Integration environment
<a name="integration-environment.3b3c7f1e-e0d6-5049-bf62-5f6688b0aef9"></a>

We recommend that you use the following infrastructure components for your integration environment.

|
|
| Type | Instance type | Resources |
| --- |--- |--- |
| **1 SAS server** | m6i.2xlarge | 8 vCPUs (4 cores)<br />32 GB RAM |
| **2 terminal servers** | m6i.2xlarge<br />  | 8 vCPUs (4 cores)<br />32 GB RAM |
| **1 SAS subversion server** | m6i.xlarge | 4 vCPUs (2 cores)<br />16 GB RAM |

## Local storage for SAS servers
<a name="local-storage-sas-server"></a>

The recommended architecture uses M6i instances based on the latest Intel Xeon Scalable processors and uses the Nitro Hypervisor from the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/). The M6i instance type is optimized for [Amazon Elastic Block Store (Amazon EBS) ](https://aws.amazon.com/ebs/)and offers dedicated bandwidth for network-accessed EBS volumes. The following table includes details about instance storage configuration for non-shared storage. You can attach additional EBS volumes on demand.

|
|
| Server | Type | Capacity | Production | Testing |
| --- |--- |--- |--- |--- |
| SAS server | Storage type | AWS resource/service and EBS type | Requirement on seq. IO (read/write) | Same as production |
| SAS server | Operating system boot and swap | EBS 200 GB (gp3) | Not relevant for sizing due to low requirements | Same as production |
| SAS server | SASWORK | EBS 2x 512 GB (gp3/each 5,000 IOPS) in RAID 0 | 8 \* 150 Mbps, 1200 Mbps or \~ 11.5 Gbps<br />M6i instance support<br />12.5 Gbps EBS storage bandwidth with gp3 EBS volumes | 1x 1024 GB volume<br />gp3 5,000 IOPS |
| SAS server | SAS Software Depot and other auxiliary storage (to include SAS install in addition) | EBS 125 GB (gp3) | Not relevant for sizing due to low requirements | Same as production |
| SAS terminal server | Operating system boot and swap | EBS 100 GB (gp3) | Not relevant for sizing due to low requirements | Same as production |
| SAS SVN server | Operating system boot and swap | EBS 100 GB (gp3)<br />  | Not relevant for sizing due to low requirements | 100 GB |
| SAS SVN server | Subversion repositories | EBS 1000 GB (gp3) | Default | 400 GB in addition to ops drive |

## Shared storage infrastructure
<a name="shared-storage-infrastructure"></a>

We recommend using FSx for Windows File Server as a shared storage solution for your SAS server and the Citrix terminal servers. You don't have to use S3 buckets for any additional file storage, unless you need the bucket for maintaining system information or automation scripts.

You can also store the subversion checkout/working copy of project code on FSx for Windows File Server. The SAS subversion server stores the repositories locally. The subversion server acts as the central version control system.

We recommend that you use FSx for Windows File Server to store Windows user profiles across your Citrix terminal servers. This will enable seamless load balancing across both servers.

### Production environment
<a name="production-environment.d5347a71-ba23-5cf4-968c-f981f58d23a4"></a>

The architecture in this guide is designed to meet the following requirements for the production environment:
+ **Storage type** – FSx for Windows File Server
+ **Type** – Multiple Availability Zones
+ **Resource/throughput** – 1024 MB
+ **Storage** – 1.2 TB SSD

### Integration and testing environment
<a name="integration-and-testing-environment.895db678-0688-5af1-8dce-6a13c280ac40"></a>

The architecture in this guide is designed to meet the following requirements for the integration environment:
+ **Storage type** – FSx for Windows File Server
+ **Type** – Multiple Availability Zones
+ **Resource/throughput** – 512 MB
+ **Storage** – 512 GB SSD

### Performance
<a name="performance.64afbdcc-aac6-5e8b-984e-037f65b26f5d"></a>

The I/O throughput for FSx for Windows File Server is easy to adjust, and you can build I/O throughput dashboards to meet your monitoring needs. You can also enable the operations team to adjust throughput based on end-user needs.

## Back up and file recovery
<a name="back-up-file-recovery"></a>

All SAS data resides on a separate FSx for Windows File Server as persistent storage. There are two levels of backup implemented on the data stored in FSx for Windows File Server:

1. **Daily backups** **retained for 30 days** – These backups are retained in an S3 bucket. You can use this snapshot-based backup for recovery if an Amazon FSx volume is corrupted or lost.

1. **Backups retained using Microsoft Volume Shadow Copy Service (VSS) **– Files on the FSx for Windows File Server are snapshotted for backup to a special storage partition on the FSx for Windows File Server twice per day and retained indefinitely. The backup is based on available storage of the VSS partition on FSx for Windows File Server (up to 10 percent of total storage space). If end users corrupt or lose a file on FSx for Windows File Server, they can initiate their own restore directly from Windows File Explorer on the SAS terminal servers.

## Disaster recovery
<a name="disaster-recovery"></a>

The decoupling architecture in this guide is designed with disaster recovery in mind. Amazon FSx is deployed across two AWS Availability Zones. If the Availability Zone where the active FSx for Windows File Server resides become unavailable, then the service automatically fails over and provides the file sharing services from the second Availability Zone.
