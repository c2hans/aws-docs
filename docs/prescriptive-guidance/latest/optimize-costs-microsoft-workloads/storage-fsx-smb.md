---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-fsx-smb.html
---

# Choose the right SMB file storage
<a name="storage-fsx-smb"></a>

## Overview
<a name="storage-fsx-smb-overview"></a>

AWS offers a variety of fully managed storage services that give you the rich capabilities of industry-leading file services, while combining the latest AWS infrastructure innovations and security. You can incorporate AWS services into infrastructure as code (IaC) workflows and integrate them with AWS compute, monitoring, and data protection services. For Windows workloads, you can choose from two fully managed file services that can be used to match your application needs: FSx for Windows File Server and Amazon FSx for NetApp ONTAP.

### FSx for Windows File Server
<a name="9999999999999999fsxwindows-.643e7096-a353-5ca4-86ce-dd448da754c2"></a>

Amazon FSx for Windows File Server provides fully managed shared storage built on Windows Server, and delivers a wide range of data access, data management, and administrative capabilities. FSx for Windows File Server integrates easily with Windows environments because it's a Windows-native service. We recommend using FSx for Windows File Server for user and group shares, Always On Failover Cluster Instances for SQL Server, Windows applications, and virtual desktop infrastructure (VDI). FSx for Windows File Server also integrates well with Amazon FSx File Gateway, Amazon Kendra, audit logs for Amazon S3, and Amazon Data Firehose.

### FSx for ONTAP
<a name="9999999999999999fsxontap-.a1bf20d1-19de-5434-ac78-c76316334caa"></a>

FSx for ONTAP is based on NetApp's proprietary ONTAP file system. It takes some level of upskilling and is recommended mostly to existing on-premises NetApp users. Typical use cases include user and group shares, Always On Failover Cluster Instances for SQL Server, and Windows applications. FSx for ONTAP supports multiple protocols, larger than 64 TB file systems (PB scale without a DFS namespace server), cloning, replication, snapshots, compression (storage efficiency), and intelligent tiering of data.

## Cost impact
<a name="storage-fsx-smb-cost"></a>

### FSx for Windows File Server
<a name="9999999999999999fsxwindows-.73b53cfc-0e4e-584b-8563-a27a59a69d7b"></a>

FSx for Windows File Server was the first shared storage solution on AWS for deploying Failover Cluster Instances for SQL Server. With FSx for Windows File Server, you could launch Failover Cluster Instances using SQL Standard edition licensing. This, however, prevents you from relying on Always On availability groups, which require SQL Server Enterprise edition licenses. By switching from SQL Server Enterprise Standard edition to SQL Server Standard edition, you could save 65–75 percent on your [SQL Server licensing](sql-server-editions.md).

You can use FSx for Windows File Server for Failover Cluster Instances to offload storage I/O from typical EBS storage. By offloading I/O to FSx for Windows File Server, you could scale down EC2 instances, which rely on high Amazon EBS throughput and IOPS, without affecting storage throughput.

### FSx for ONTAP
<a name="9999999999999999fsxontap-.f805f96a-276e-5e76-8307-fe01034b42f9"></a>

You can use FSx for ONTAP to run your Microsoft failover cluster on block protocol iSCSI and benefit from SQL Server instant file initialization, cross-Region replication using SnapMirror, antivirus support, and cloning. If you create multiple copies of databases for testing, cloning can make a significant difference in both space consumption and how quick those database copies can be created. Additionally, you can use NetApp SnapCenter to manage backup, restore, and clone functionality with your EC2 instances for SQL Server by using FSx for ONTAP. FSx for ONTAP also provides automatic tiering from SSD to a low cost capacity pool storage for a mixture of performance and cost efficiency.

FSx for ONTAP supports NetApp's file system (ONTAP), unlike FSx for Windows File Server, which supports a Windows native NTFS file system. The minimum size for FSx for ONTAP is 1024 GB, while FSx for Windows File Server can start as low as 32 GB.

### Integration with Microsoft Distributed File System
<a name="integration-with-microsoft-distributed-file-system.3ea7a69c-df30-504f-b98f-6c4f22d5d985"></a>

FSx for Windows File Server and FSx for ONTAP integrate with Microsoft's [Distributed File System (DFS)](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj127250(v=ws.11)) for seamless integration into existing deployments. Keep the following in mind when planning your architecture:
+ FSx for Windows File Server and FSx for ONTAP support [DFS Namespaces (DFSN)](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview) on both deployment types (multiple Availability Zones and single Availability Zones).
+ Only FSx for Windows File Server supports [DFS Replication (DFSR)](https://learn.microsoft.com/en-us/windows-server/storage/dfs-replication/dfsr-overview), and only when using single Availability Zones.

## Cost optimization recommendations
<a name="storage-fsx-smb-rec"></a>

Performance for both FSx for Windows File Server and FSx for ONTAP is very configuration dependent, as is their pricing. FSx for Windows File Server pricing primarily depends on storage capacity and storage type, throughput capacity, backup, and data transferred. With FSx for ONTAP, you pay for SSD storage, SSD IOPS, capacity pool usage, throughput capacity, and backup.

|
|
| File service | Cost for 5 TB storage | Configuration | Region |
| --- |--- |--- |--- |
| FSx for Windows File Server | $982.78 | Single Availability Zone<br />SSD (15,000 IOPS)<br />32 MBps<br />5 TB backup (no deduplication savings) | US East (N. Virginia) |
| FSx for ONTAP | $979.28 | Single Availability Zone<br />100% SSD<br />15,000 read-write capacity tier<br />15,000 SSD IOPS<br />128 MBps<br />5 TB backup (no deduplication savings) | US East (N. Virginia) |

Keep in mind the following:
+ Deduplication and compression enable you to store more data on physical devices by shrinking data size, but you pay for the provisioned solid state drive (SSD) or hard disk drive (HDD) storage.
+ You can use FSx for ONTAP to tier your data. It's extremely rare for 100 percent of your data to be accessed regularly and require SSD storage. You can move cold and infrequently accessed data to a capacity tier for cost savings.
+ The prices mentioned here are calculated with 100 percent data on the SSD tier and 15,000 IOPS on the SSD tier.

### Backup
<a name="backup.361539ec-d1e6-5e40-ab52-9131f46a8215"></a>

By default, both FSx for ONTAP and FSx for Windows File Server store their fully managed backup on Amazon S3. However, with FSx for ONTAP there is an additional option for backup using SnapVault, which can configure backups to reside in the capacity tier. Backing up with SnapVault is a self-managed mechanism that's more cost-efficient than the default fully-managed backup option. The fully-managed backup option is $0.05 per GB-month. The SnapVault backup on FSx for ONTAP (10:1 SSD to capacity pool storage) is $0.03221 (0.9x0.0219\+0.1x0.125).

Keep in mind the following:
+ AWS managed backups offer granularity of one hour. [SnapVault](https://docs.netapp.com/us-en/ontap/concepts/snapvault-archiving-concept.html) enables you to go as low as five minutes.
+ You can use NetApp's tools (such as the CLI and API) to configure the SnapVault relationships and snapshot replication.
+ Enable the `all` tiering policy on a SnapVault volume to use the capacity tier as storage for the backup data.
+ SnapVault destinations can be in the same AWS Region, cross-Region, or on-premises. This is usually to a single Availability Zone or multiple Availability Zone file system backup destination. In comparison, AWS Backup is backed by the regional resiliency of Amazon S3.

### Right sizing
<a name="right-sizing.aea3ee99-5792-5350-b3c3-23f34d98f012"></a>

You can also save on costs and get the most out of your file system by right sizing and preventing over provisioning.

To right size, do the following:

1. Identify your current needs based on data. For typical Windows workloads, you can use built-in operating system tools like [Performance Monitor](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc749154(v%3dws.11)).

1. In Performance Monitor, use the following counters to gauge your current performance needs. The capture interval is set to one second, with a maximum log size of 1,000 MB and overwrite enabled.

   ```
   Logman.exe create counter PerfLog-Short -o "c:\perflogs\PerfLog-Long.blg" -f bincirc -v mmddhhmm -max 1024 -c "\LogicalDisk(*)\*" "\Memory\*" "\.NET CLR Memory(*)\*" "\Cache\*" "\Network Interface(*)\*" "\Paging File(*)\*" "\PhysicalDisk(*)\*" "\Processor(*)\*" "\Processor Information(*)\*" "\Process(*)\*" "\Thread(*)\*" "\Redirector\*" "\Server\*" "\System\*" "\Server Work Queues(*)\*" "\Terminal Services\*" -si 00:00:01
   ```

1. To start the log capture, run the `logman start PerfLog-Short` command. To stop the log capture, run the `logman stop PerfLog-Short` command.
**Note**
You can find performance log files in **c:\\perflogs** on the server running the capture. For more information, see [Windows Performance Monitor Overview](https://techcommunity.microsoft.com/blog/askperf/windows-performance-monitor-overview/375481) in the Microsoft documentation.

1. After you identify the correct the configuration, test if your estimate is correct on the Amazon FSx file system by using disk stress tools like Microsoft [DISKSPD](https://learn.microsoft.com/en-us/azure-stack/hci/manage/diskspd-overview).

1. If you're satisfied with the performance, cut over to the file share.

We recommend a conservative approach to storage capacity as it can only be scaled up. Throughput capacity can be scaled up and down as needed.

## Additional resources
<a name="storage-fsx-smb-resources"></a>
+ [Amazon FSx for NetApp ONTAP FAQs](https://aws.amazon.com/fsx/netapp-ontap/faqs/) (AWS website)
+ [Optimizing Amazon FSx for Windows File Server performance with new metrics](https://aws.amazon.com/blogs/storage/optimizing-amazon-fsx-for-windows-file-server-performance-with-new-metrics/) (AWS Storage Blog)
