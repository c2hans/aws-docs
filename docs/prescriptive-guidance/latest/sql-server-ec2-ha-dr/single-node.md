---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-ha-dr/single-node.html
---

# SQL Server on Amazon EC2
<a name="single-node"></a>

The following diagram illustrates a recommended architecture for a single-node SQL Server on Amazon Elastic Compute Cloud (Amazon EC2) before adding support for high availability (HA) and disaster recovery (DR).

In this architecture, the SQL Server database is deployed to an EC2 instance, using an Amazon Machine Image (AMI) for SQL Server and separate volumes for OS, DATA, LOG, and backups. Non-volatile memory express (NVMe) storage is attached directly to the EC2 instance and used for the SQL Server tempdb database. AWS Directory Service is used to set up Windows authentication for the SQL Server database. You can also use AWS Systems Manager to detect and install SQL Server patches and updates.

![Single-node SQL Server architecture on Amazon EC2 before HA/DR](http://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-ha-dr/images/guide-img/09ec13da-971b-4981-975f-0940015d7fc0/images/b6644cca-48cf-40b2-befa-3be9909a2551.png)

 The following table summarizes the recommendations for configuring this architecture. These recommendations are discussed in detail in the sections that follow.

|
|
| Category | Recommendation |
| --- |--- |
| Instance type/AMI | + [Amazon Elastic Block Store (Amazon EBS)-optimized instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html#ebs-optimization-support) for performance<br />+ NVMe for instance storage (temporary) <br />+ [Amazon EC2 AMIs for SQL Server](https://aws.amazon.com/about-aws/whats-new/2021/10/amazon-ec2-microsoft-sql-server-windows-ami/) |
| SQL Server edition | + SQL Server Developer edition (non-production) <br />+ SQL Server Standard and  Enterprise editions (production) |
| Storage type | + [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html)<br />+ [NVMe](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/add-instance-store-volumes.html#adding-instance-storage-instance) (tempdb) (gp2/io1/io2) |
| Volumes | + OS<br />+ DATA  <br />+ LOG  <br />+ tempdb  <br />+ Scratch space for storing and downloading backups |
| DR options | + Amazon EC2<br />+ Amazon EBS snapshots  <br />+ SQL Server native backups |

## Instance types
<a name="instance-types"></a>

AWS offers a selection of [instance classes](https://aws.amazon.com/ec2/instance-types/) for your SQL Server workloads. You can choose among compute optimized, memory optimized, storage optimized, general purpose, and other types, depending on the expected workload on the database server, version, HA/DR options, cores required, and licensing considerations. We recommend that you choose Amazon EBS-optimized instance types for SQL Server. These offer the best throughput with attached EBS volumes in a dedicated network, which is critical for SQL Server workloads that might have heavy data access requirements. For standard database workloads, you can run memory optimized instance classes such as `R5`, `R5b`, `R5d`, and `R5n`. You can also include either instance storage or NVMe storage. These are both ideal for tempdb and offer balanced performance for database workloads.

For critical workloads, the high-performance [z1d instance](https://aws.amazon.com/ec2/instance-types/z1d/) is optimized for workloads that carry high licensing costs, such as SQL Server. The `z1d` instance is built with a custom Intel Xeon Scalable processor that delivers a sustained all-core turbo frequency of up to 4.0 GHz, which is significantly faster than other instances. For workloads that need faster sequential processing, you can run fewer cores with a `z1d` instance and get the same or better performance than other instances with more cores.

AWS also provides dedicated [AMIs for SQL Server on Microsoft Windows Server](https://aws.amazon.com/windows/resources/amis/) to help you host the latest SQL Server editions on Amazon EC2.

## Storage options
<a name="storage"></a>

Some instance types offer NVMe [instance store volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#instance-store-volumes). NVMe is a temporary (epheremal) storage option. This storage is directly attached to the EC2 instance. Although NVMe storage is temporary and data is lost on reboot, it offers the most optimal performance. Therefore, it is suitable for the SQL Server tempdb database, which has high I/O and random data access patterns. There is no additional charge for using an NVMe instance store for tempdb. For additional guidance, see the section [Place tempdb in an instance store](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/tempdb.html) in the guide *Best practices for deploying SQL Server on Amazon EC2*.

Amazon EBS is a durable storage solution that meets SQL Server's requirements for fast, available storage. Microsoft recommends keeping the data and log volumes separate for optimal performance. The reasons for this separation include the following:
+ Different data access methods. Data volumes use online transaction processing (OLTP) random data access, whereas log volumes use serial access.
+ Better recovery options. The loss of one volume doesn't affect the other volume, and helps in the recovery of data.
+ Different workload types. Data volumes are for OLTP workloads, whereas log volumes target online analytic processing (OLAP) workloads.
+ Different performance requirements. Data and log volumes have different IOPS and latency requirements, minimum throughput rates, and similar performance benchmarks.

To select the right Amazon EBS [volume type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html), you should analyze your database access methods, IOPS, and throughput. Collect metrics both during standard working hours and during peak usage. SQL Server uses extents to store data. The atomic unit of storage in SQL Server is a page, which is 8 KB in size. Eight physically contiguous pages make up an extent, which is 64 KB in size. Therefore, on a SQL Server machine, the NTFS allocation unit size for hosting SQL database files (including tempdb) should be 64 KB. For information about how to check the NTFS allocation size of your drives, see the guide [Best practices for deploying SQL Server on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/ntfs-size.html).

The choice of EBS volume depends on the workload—that is, whether the database is read-intensive or write-intensive, requires high IOPS, archive storage, and similar considerations. The following table shows a sample configuration.

|
|
| Amazon EBS resource | Type | Description |
| --- |--- |--- |
| OS disk | `gp3` | General-purpose storage. |
| DATA disk | `io2/io1` | Write-intensive storage. |
| LOG disk | `gp3` or `io2` | General-purpose storage for intensive workloads. |
| Backup disk | `st1` | Less expensive archive storage. For better performance, backups can also be stored on a faster disk if they're copied to Amazon Simple Storage Service (Amazon S3) regularly. |

## Amazon EBS and Amazon S3 considerations
<a name="ebs-s3"></a>

The following table shows a comparison of Amazon EBS and Amazon S3 for storage. Use this information to understand the differences between the two services and to choose the best approach for your use case.

|
|
| Service | Availability | Durability | Notes |
| --- |--- |--- |--- |
| Amazon EBS | + All EBS volume types offer durable snapshot capabilities and are designed for 99.999% availability.<br />+ You can use snapshots to provision new instances in different AWS Regions in case of a disaster. | + EBS volume data is replicated across multiple servers in a single Availability Zone to prevent the loss of data from the failure of any single component.<br />+ EBS volumes are designed for an annual failure rate (AFR) of between 0.1 and 0.2 percent, where failure refers to a complete or partial loss of the volume, depending on the size and performance of the volume. | + An Amazon EBS–optimized instance uses an optimized configuration stack and provides additional, dedicated bandwidth for Amazon EBS I/O. This optimization provides the best performance for your EBS volumes by minimizing contention between Amazon EBS I/O and other traffic from your instance.<br />+ Fast snapshot restores are supported for up to 50 snapshots at the same time. You must enable this feature explicitly on a per-snapshot basis.<br />+ An Amazon EBS–optimized instance offers full provisioned performance at initialization, so no warmup time is involved. |
| Amazon S3 | + Highly available.<br />+ Designed for 99.99% availability over a given year.<br />+ Multiple storage classes are available, such as S3 Standard and S3 Standard- Infrequent Access (S3 Standard-IA). You can move backup files to a storage class based on a retention period. | + Amazon S3, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive are designed for 99.999999999% (11 nines) of durability. Both Amazon S3 and S3 Glacier Flexible Retrieval offer reliable backup of data, with object replication across at least three, geographically dispersed Availability Zones.   | + You can use Amazon S3 for long-term SQL Server file-level backups (including full backups and transaction logs).<br />+ Amazon S3 supports:[Replication time control (RTC)](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-time-control.html)Cross-Region replication through S3 Lifecycle management and AWS BackupIntelligent tiering<br />+ Amazon S3 provides the least expensive storage. Cross-Region data transfer costs apply. |

## SQL Server on Amazon FSx for Windows File Server
<a name="fsx"></a>

[Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/sql-server.html) provides fast performance with baseline throughput up to 2 GB/second per file system, hundreds of thousands of IOPS, and consistent sub-millisecond latencies. To provide the right performance for your SQL Server instances, you can choose a throughput level that is independent of your file system size. Higher levels of throughput capacity also come with higher levels of IOPS that the file server can serve to the SQL Server instances accessing it. The storage capacity determines not only how much data you can store, but also how many I/O operations per second (IOPS) you can perform on the storage. Each GB of storage provides 3 IOPS. You can provision each file system to be up to 64 TiB in size (compared with 16 TiB for Amazon EBS). You can also use Amazon FSx systems as a file share witness for Windows Server Failover Cluster (WSFC) deployments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
